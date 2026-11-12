#!/usr/bin/env python3
"""
portal_import.py — apply what reviewers sent through the review portal.

    git pull
    python scripts/portal_import.py              # dry run: what is in logs/portal/inbox/ and what each record would do
    python scripts/portal_import.py --execute    # apply, move the records to logs/portal/applied/, log
    python scripts/portal_import.py --execute --promote   # also promote drafts an approver approved

The portal (portal/, docs/PORTAL.md) writes one JSON record per decision into
logs/portal/inbox/ through the GitHub API; the repository is otherwise never
written from the web. This script is the only consumer. Record kinds:

  screen   {id: C0123, stage, decision, reason, note}
           → screening/candidates.yaml via screen._apply_decision, as `by: <name>`
  verdict  {id: drafts/<bucket>/<file>.md, verdict, rationale, per_finding: [{id, verdict, concern, supports_approval, passages}],
            draft_digest, finding_ids}
           → the draft's `portal_reviews` list (who said what, with per-finding verdicts); with
             --promote and a reviewer listed as an approver in portal/reviewers.yaml, an `approve`
             runs auto_review.apply_manual_verdict (promote.py) as human:<name>; `reject` likewise.
             Only when the draft is still what was reviewed (review_binding.py: draft_digest and
             finding_ids against the file now, or against the run's start plus that same send's
             own edits), an approval agrees with every finding, and no reviewer mark is open;
             otherwise the verdict is recorded as a stale or blocked opinion and not promoted.

Every record ends in one outcome (Outcome): applied, recorded, stale or blocked move it to
logs/portal/applied/ (with `_outcome`) and add a line to logs/portal/ledger.jsonl; skip and error
leave it in the inbox. Each record's id (its file name) is stamped on what it writes, so a replay
after an interruption does not apply it twice; a verdict whose draft was already promoted is
recognised from promote.py's journal (logs/promotion_transactions, `record_ids`).
  edit     {id: draft, finding, fields: {field: {old, new}}, passages_added: [{page, quote, supports}]}
           → the finding, when the field still has the old value (else noted), stamped `edits: {by, date, fields}`
  mark     {id: draft, page, quote, note}
           → the draft's `reviewer_marks` (refocus.py turns them into findings)
  comment  {id: draft, finding?, text}
           → the finding's (or draft's) `portal_comments`
  pdf      {id: C0123 or @Key, name, bytes, sha256, bucket, object}
           → the uploaded file is pulled from the portal's R2 bucket (`wrangler r2 object get`,
             the login used for deploying) into papers/<Key>.pdf — or papers/<id>_<name> for a
             candidate without a key, linked as its `pdf_file` — then deleted from the bucket.
             papers/ is the OneDrive folder, so that is where the PDF lands. Run
             intake_papers.py afterwards as for any new PDF.

Reviewers are identified by the email Cloudflare Access verified. portal/reviewers.yaml
maps emails to the `human:<name>` used in the KB and says who may approve
(docs/GOVERNANCE.md §2); an unknown email is applied as `human:<local part>` with
no approval right, and listed so you can add it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import screen as SC  # noqa: E402
import screening as S  # noqa: E402
import review_binding as RB  # noqa: E402
from aphasia_kb import parse_markdown  # noqa: E402

INBOX = ROOT / "logs" / "portal" / "inbox"
APPLIED = ROOT / "logs" / "portal" / "applied"
LEDGER: Path | None = None   # default ROOT/logs/portal/ledger.jsonl, resolved at call time (see ledger_path)
LOG = ROOT / "logs" / "extraction_log.md"
REVIEWERS = ROOT / "portal" / "reviewers.yaml"
PAPERS = ROOT / "papers"
PORTAL = ROOT / "portal"
EDITABLE = ("claim", "direction", "relationship", "strength", "target", "target_kind")


def reviewers() -> dict[str, dict]:
    if not REVIEWERS.exists():
        return {}
    data = yaml.safe_load(REVIEWERS.read_text(encoding="utf-8")) or {}
    return {str(k).lower(): dict(v or {}) for k, v in (data.get("reviewers") or {}).items()}


def who(email: str, table: dict[str, dict]) -> tuple[str, bool, bool]:
    """(name for `by:`, may approve, known)"""
    e = str(email or "").lower()
    rec = table.get(e)
    if rec:
        return str(rec.get("name") or e.split("@")[0]), bool(rec.get("approver")), True
    return e.split("@")[0].replace(".", "_") or "portal", False, False


def _write(path: Path, fm: dict, body: str) -> None:
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    path.write_text(f"---\n{text}---\n{body}", encoding="utf-8")


def _draft(rel: str) -> Path | None:
    p = (ROOT / rel).resolve()
    if p.suffix == ".md" and (ROOT / "drafts").resolve() in p.parents and p.exists():
        return p
    return None


def _rel(p: Path) -> str:
    """p relative to the repository, tolerant of a symlinked root (/var vs /private/var on macOS)."""
    for base in (ROOT, ROOT.resolve()):
        try:
            return p.relative_to(base).as_posix()
        except ValueError:
            continue
    return p.name


def _log(line: str) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(line.rstrip() + "\n")


# ------------------------------------------------------------------ outcomes
class Outcome(str):
    """An applier's message, with what happened to the record:

      applied    everything the record asked for was done
      recorded   an opinion was recorded and nothing more was asked (or allowed: not an approver)
      stale      recorded as an opinion, but the draft is no longer what the reviewer reviewed:
                 not promoted; the reviewer (or another) has to review the current draft
      blocked    recorded; the promotion it asked for was refused (incomplete approval, open
                 reviewer marks, or the checks in auto_review/promote.py)
      skip       nothing done (no such draft or candidate, malformed …): stays in the inbox
      error      something failed part-way (e.g. promotion raised): stays in the inbox and is
                 retried; what was already written is not written twice (record ids, ledger)

    The first four are final: the record moves to applied/ and gets a ledger line."""

    def __new__(cls, text: str, status: str):
        obj = super().__new__(cls, text)
        obj.status = status
        return obj


FINAL = ("applied", "recorded", "stale", "blocked")


def status_of(msg: str) -> str:
    st = getattr(msg, "status", None)
    if st:
        return st
    return "skip" if msg.startswith("skip") else "error" if msg.startswith("error") else "applied"


def _record_id(rec: dict) -> str:
    """The record's file name: unique, written by the portal's functions (portal/lib/github.js)."""
    return str(rec.get("_record") or "")


def _has_record(items, rid: str) -> bool:
    return bool(rid) and any(isinstance(x, dict) and x.get("record") == rid for x in items or [])


def ledger_path() -> Path:
    """One line per record fully dealt with (replay-safe). Derived from ROOT when called, so a
    caller (or a test) that points ROOT elsewhere never writes the repository's ledger."""
    return LEDGER if LEDGER is not None else ROOT / "logs" / "portal" / "ledger.jsonl"


def load_ledger(path: Path | None = None) -> dict[str, dict]:
    path = path or ledger_path()
    out: dict[str, dict] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if isinstance(row, dict) and row.get("record") and row.get("status") in FINAL:
                out[str(row["record"])] = row
    return out


def append_ledger(rows: list[dict], path: Path | None = None) -> None:
    if not rows:
        return
    path = path or ledger_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        fh.flush()


# ------------------------------------------------------------------ appliers
def _candidate_for_id(cands: list[dict], rid: str):
    return next((c for c in cands if c.get("id") == rid or rid in (c.get("upload_ids") or [])), None)


def apply_paper(rec: dict, by: str, execute: bool, state: dict) -> str:
    """Register a reviewer-supplied source or prioritize a match; never make a decision."""
    rid = str(rec.get("id") or "")
    title = str(rec.get("title") or "").strip()
    doi = str(rec.get("doi") or "").strip().lower()
    if not re.fullmatch(r"(?:C\d{1,7}|U[0-9a-f]{32})", rid) or not 8 <= len(title) <= 500:
        return "skip: invalid paper identity"
    if doi and not re.fullmatch(r"10\.\d{4,9}/\S{1,180}", doi):
        return "skip: invalid DOI"
    cands = state.setdefault("candidates", S.load_candidates())
    c = _candidate_for_id(cands, rid)
    norm = lambda t: " ".join(re.sub(r"[^\w]+", " ", str(t or "").casefold()).split())
    if c is None:
        matches = [x for x in cands if not x.get("duplicate_of") and ((doi and str(x.get("doi") or "").lower() == doi) or (norm(x.get("title")) == norm(title) and not (doi and x.get("doi") and str(x["doi"]).lower() != doi)))]
        if len(matches) > 1:
            return "skip: ambiguous paper identity; resolve the register first"
        c = matches[0] if matches else None
    if c is None:
        if not rec.get("new_candidate") or not rid.startswith("U"):
            return "skip: matched candidate no longer exists"
        c = {"id": rid, "title": title, "doi": doi or None, "sources": [], "screening": []}
        cands.append(c)
    elif doi and c.get("doi") and str(c["doi"]).lower() != doi:
        return "skip: DOI conflicts with candidate"
    if c.get("duplicate_of"):
        c = _candidate_for_id(cands, c["duplicate_of"])
        if c is None:
            return "skip: missing canonical duplicate"
    if rid != c["id"] and rid not in c.setdefault("upload_ids", []):
        c["upload_ids"].append(rid)
    record = _record_id(rec)
    if not any(x.get("record") == record for x in c.get("sources", []) if record):
        c.setdefault("sources", []).append({"kind": "hand_picked", "date": str(rec.get("submitted") or "")[:10], "by": by, "note": "Reviewer PDF upload (other source)", "record": record})
    c["pdf_uploaded_at"] = max(str(c.get("pdf_uploaded_at") or ""), str(rec.get("submitted") or ""))
    state["candidates_dirty"] = True
    return f"{c['id']}: PDF supplied by {by}; prioritized without changing screening decisions"


def apply_screen(rec: dict, by: str, execute: bool, state: dict) -> str:
    cands = state.setdefault("candidates", S.load_candidates())
    by_id = {c["id"]: c for c in cands}
    c = _candidate_for_id(cands, str(rec.get("id")))
    if c is None:
        return f"skip: no candidate {rec.get('id')}"
    if _has_record(c.get("screening"), _record_id(rec)):
        return Outcome(f"{c['id']}: already applied ({_record_id(rec)})", "applied")
    stage = rec.get("stage") or "title_abstract"
    err = SC._apply_decision(c, stage, str(rec.get("decision")), rec.get("reason") or None, by, rec.get("note") or None,
                             str(rec.get("submitted") or "")[:10] or dt.date.today().isoformat(), seq=SC._next_seq(cands))
    if err:
        return f"skip: {err}"
    if _record_id(rec):
        c["screening"][-1]["record"] = _record_id(rec)
    state["candidates_dirty"] = True
    return f"{c['id']}: {stage} {rec.get('decision')}{' ' + str(rec.get('reason')) if rec.get('reason') else ''} by {by}"


def apply_edit(rec: dict, by: str, execute: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    f = next((x for x in fm.get("findings") or [] if isinstance(x, dict) and x.get("id") == rec.get("finding")), None)
    if f is None:
        return f"skip: no finding {rec.get('finding')} in {p.name}"
    if _has_record(f.get("edits"), _record_id(rec)):
        return Outcome(f"{p.name} {f.get('id')}: already applied ({_record_id(rec)})", "applied")
    applied, stale = [], []
    for k, ch in (rec.get("fields") or {}).items():
        if k not in EDITABLE or not isinstance(ch, dict):
            continue
        if f.get(k) != ch.get("old") and str(f.get(k)) != str(ch.get("old")):
            stale.append(f"{k} (now {f.get(k)!r}, reviewer saw {ch.get('old')!r})")
            continue
        f[k] = ch.get("new")
        applied.append(k)
    for q in rec.get("passages_added") or []:
        if isinstance(q, dict) and str(q.get("quote") or "").strip():
            f.setdefault("source_passages", []).append({"section": "added in the review portal", "page": q.get("page"),
                                                        "quote": str(q["quote"]).strip(), "supports": q.get("supports") or "claim"})
            applied.append("source_passages")
    if applied:
        f.setdefault("edits", []).append({"by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10] or dt.date.today().isoformat(),
                                          "fields": sorted(set(applied)), "via": "portal"}
                                         | ({"record": _record_id(rec)} if _record_id(rec) else {}))
        if execute:
            _write(p, fm, body)
        state.setdefault("touched", set()).add(p)
    return f"{p.name} {f.get('id')}: {', '.join(sorted(set(applied))) or 'nothing'} by {by}" + (f"; stale: {'; '.join(stale)}" if stale else "")


def apply_mark(rec: dict, by: str, execute: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    marks = fm.setdefault("reviewer_marks", [])
    if _has_record(marks, _record_id(rec)) or any(isinstance(m, dict) and m.get("quote") == rec.get("quote") for m in marks):
        return Outcome(f"{p.name}: mark already present", "applied")
    n = 1 + max([int(str(m.get("id", "m0"))[1:] or 0) for m in marks if isinstance(m, dict)] or [0])
    marks.append({"id": f"m{n}", "page": rec.get("page"), "quote": str(rec.get("quote") or "").strip(), "note": rec.get("note") or "",
                  "by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10] or dt.date.today().isoformat(), "status": "pending"}
                 | ({"record": _record_id(rec)} if _record_id(rec) else {}))
    if execute:
        _write(p, fm, body)
    state.setdefault("touched", set()).add(p)
    return f"{p.name}: mark m{n} by {by} (python scripts/refocus.py {_rel(p)})"


def apply_comment(rec: dict, by: str, execute: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    entry = {"by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10], "text": str(rec.get("text") or "").strip()}
    if _record_id(rec):
        entry["record"] = _record_id(rec)
    target = fm
    if rec.get("finding"):
        target = next((x for x in fm.get("findings") or [] if isinstance(x, dict) and x.get("id") == rec.get("finding")), fm)
    if _has_record(target.get("portal_comments"), _record_id(rec)):
        return Outcome(f"{p.name}: comment already present ({_record_id(rec)})", "applied")
    target.setdefault("portal_comments", []).append(entry)
    if execute:
        _write(p, fm, body)
    state.setdefault("touched", set()).add(p)
    return f"{p.name}: comment by {by}"


def _binding_problem(rec: dict, p: Path, fm: dict, state: dict) -> str | None:
    """Why this verdict no longer applies to the draft as it is now, or None.

    Trusted references only: the importer's own digest of the file now, and the digest it took
    when this run started (state["batch_start"]). A verdict is current when the digest it carries
    equals the file's digest now; or equals the batch-start digest and every change made to the
    draft since then in this run came from records of the same send (same verified reviewer email
    and the same server-set `submitted` time) — the reviewer's own edits and marks sent with the
    verdict. Anything the client sends (ids, flags) is never an exemption on its own."""
    want = str(rec.get("draft_digest") or "")
    if not want:
        return "the record does not say which version of the draft was reviewed (sent before content binding)"
    now = RB.review_digest(fm)
    ids = [str(x) for x in rec.get("finding_ids") or []]
    if ids != RB.finding_ids(fm):
        return f"the draft now has findings {', '.join(RB.finding_ids(fm)) or 'none'}; the reviewer saw {', '.join(ids) or 'none'}"
    if want == now:
        return None
    key = str(p.resolve())
    start = (state.get("batch_start") or {}).get(key)
    if start and want == start:
        send = (str(rec.get("reviewer") or "").lower(), str(rec.get("submitted") or ""))
        changes = (state.get("changes") or {}).get(key) or []
        if changes and all(c == send for c in changes):
            return None
        return "the draft was changed in this run by another record than the reviewer's own send"
    return "the draft changed after the reviewer opened it"


TRANSACTIONS = "logs/promotion_transactions"   # promote.py's journals (promotion_transaction.py)


def _journals_for(rel: str, rid: str) -> list[tuple[Path, dict]]:
    """promote.py journals for this draft path that name this portal record in `record_ids`
    (the ids in the draft's portal_reviews when it was promoted). Only an explicit record id
    counts: a canonical file of the same name proves nothing about this record."""
    out = []
    want = Path(str(rel or "")).as_posix()
    if not rid or not want.startswith("drafts/"):
        return out
    for j in sorted((ROOT / TRANSACTIONS).glob("*.json")) if (ROOT / TRANSACTIONS).is_dir() else []:
        try:
            row = json.loads(j.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(row, dict) and Path(str(row.get("draft") or "")).as_posix() == want and rid in (row.get("record_ids") or []):
            out.append((j, row))
    return out


def _promoted_earlier(rec: dict, execute: bool) -> Outcome | None:
    """The draft is gone. If promote.py's journal shows that this very record's approval was
    promoted (a crash came between promotion and the ledger), the record is done; a journal left
    pending is finished first (promotion_transaction.recover_pending, as promote.py does)."""
    rel, rid = str(rec.get("id") or ""), _record_id(rec)
    found = _journals_for(rel, rid)
    if not found:
        return None
    if any(row.get("done") for _, row in found):
        j = next(j for j, row in found if row.get("done"))
        return Outcome(f"{Path(rel).name}: already promoted for this record ({TRANSACTIONS}/{j.name})", "applied")
    if not execute:
        return Outcome(f"{Path(rel).name}: promotion for this record is pending in {TRANSACTIONS}; --execute finishes it", "applied")
    try:
        import promotion_transaction as PT  # noqa: WPS433 — promote.py's journal module
        import fcntl
        with (ROOT / '.promotion.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            PT.recover_pending(ROOT, ROOT / rel)
    except Exception as e:  # noqa: BLE001
        return Outcome(f"error: {Path(rel).name}: the pending promotion for this record could not be finished: {e}", "error")
    if any(row.get("done") for _, row in _journals_for(rel, rid)):
        return Outcome(f"{Path(rel).name}: pending promotion for this record finished from its journal", "applied")
    return Outcome(f"error: {Path(rel).name}: the promotion journal for this record is still pending", "error")


def apply_verdict(rec: dict, by: str, approver: bool, execute: bool, promote: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return _promoted_earlier(rec, execute) or f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    rid = _record_id(rec)
    per = [x for x in rec.get("per_finding") or [] if isinstance(x, dict)]
    problem = _binding_problem(rec, p, fm, state)
    if not _has_record(fm.get("portal_reviews"), rid):
        entry = {"by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10], "verdict": rec.get("verdict"),
                 "rationale": rec.get("rationale") or "", "approver": approver,
                 "findings": [{k: x.get(k) for k in ("id", "verdict", "concern") if x.get(k) not in (None, "")}
                              | ({"passages": x["passages"]} if x.get("passages") else {}) for x in per]}
        if rec.get("draft_digest"):
            entry["reviewed_digest"] = str(rec["draft_digest"])
        if problem:
            entry["stale"] = problem
        if rid:
            entry["record"] = rid
        fm.setdefault("portal_reviews", []).append(entry)
        if execute:
            _write(p, fm, body)
        state.setdefault("touched", set()).add(p)
    agree = sum(1 for x in per if x.get("verdict") == "agree")
    summary = f"{p.name}: {rec.get('verdict') or 'no overall verdict'} by {by} ({agree}/{len(per)} findings agreed)"
    if problem:
        return Outcome(summary + f" — recorded as an opinion, not applied: {problem}; review the current draft again", "stale")
    wants = rec.get("verdict") in ("approve", "reject")
    if not (promote and approver and wants):
        if rec.get("verdict") == "approve" and not approver:
            return Outcome(summary + " — recorded as an opinion (not an approver)", "recorded")
        return Outcome(summary, "recorded")
    if rec.get("verdict") == "approve":
        ids = RB.finding_ids(fm)
        said = {str(x.get("id")): x.get("verdict") for x in per}
        if not ids:
            return Outcome(summary + " — not promoted: the draft has no findings to approve", "blocked")
        short = [i for i in ids if said.get(i) != "agree"]
        if short:
            return Outcome(summary + f" — not promoted: an approval must agree with every finding ({', '.join(short)} not agreed)", "blocked")
    open_marks = RB.open_obligations(fm)
    if open_marks:
        return Outcome(summary + f" — not promoted: reviewer marks {', '.join(open_marks)} are not resolved (refocus.py, then a person)", "blocked")
    if not execute:
        return Outcome(summary + f" — would {rec.get('verdict')} via promote.py", "applied")
    import auto_review as AR  # noqa: WPS433
    try:
        final, _ = AR.apply_manual_verdict(p, verdict_override=rec["verdict"], rationale=rec.get("rationale") or "(portal review)",
                                           per_finding=[{"id": x.get("id"), "concern": x.get("concern") or "",
                                                         "supports_approval": x.get("verdict") == "agree"} for x in per],
                                           reviewer=f"human:{by}", auto_promote_on_approve=True)
    except Exception as e:  # noqa: BLE001
        return Outcome(summary + f" — error: promotion failed, the record stays in the inbox and is retried: {e}", "error")
    final = str(final)
    if rec["verdict"] == "approve" and final != str(AR.Verdict.APPROVE):
        return Outcome(summary + f" — not promoted: the checks gave {final}", "blocked")
    return Outcome(summary + f" — {final} via promote.py", "applied")


# ------------------------------------------------------------------ uploaded PDFs
def bucket_name() -> str:
    """The R2 bucket bound in portal/wrangler.toml (fallback when a record names none)."""
    toml = PORTAL / "wrangler.toml"
    if toml.exists():
        m = re.search(r'bucket_name\s*=\s*"([^"]+)"', toml.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return ""


def _wrangler(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["npx", "wrangler", *args], cwd=str(PORTAL), capture_output=True, text=True, timeout=600)


def r2_get(bucket: str, obj: str, dest: Path) -> str | None:
    """Download one object with the deploy login. Returns an error message or None."""
    done = _wrangler(["r2", "object", "get", f"{bucket}/{obj}", "--file", str(dest), "--remote"])
    if done.returncode != 0 or not dest.exists():
        return (done.stderr or done.stdout).strip().splitlines()[-1:][0] if (done.stderr or done.stdout).strip() else f"wrangler exit {done.returncode}"
    return None


def r2_delete(bucket: str, obj: str) -> str | None:
    done = _wrangler(["r2", "object", "delete", f"{bucket}/{obj}", "--remote"])
    return None if done.returncode == 0 else (done.stderr or done.stdout).strip()[-200:]


# swapped out by the tests
FETCH = {"get": r2_get, "delete": r2_delete}


def _safe_name(name: str) -> str:
    base = re.sub(r"[^\w.() -]+", "_", str(name or "")).strip(" .")[:100] or "paper.pdf"
    return base if base.lower().endswith(".pdf") else base + ".pdf"


CANDIDATE_ID = re.compile(r"^C\d{1,7}$")
CITATION_KEY = re.compile(r"^@?[A-Za-z][A-Za-z0-9]{0,79}$")
PAPER_FILE = re.compile(r"^[A-Za-z0-9][\w.() -]{0,200}\.pdf$")


def _known_keys(state: dict) -> set[str]:
    """Citation keys in citations.md, lower-cased without @ (loaded once per run)."""
    if "citation_keys" not in state:
        try:
            state["citation_keys"] = {k.lstrip("@").lower() for k in S.citation_blocks()}
        except Exception:  # noqa: BLE001
            state["citation_keys"] = set()
    return state["citation_keys"]


def _inside_papers(name: str) -> tuple[Path | None, str]:
    """papers/<name> when `name` is a plain PDF file name that stays inside papers/, else a reason.
    Containment is checked on the resolved path, so a symlinked papers/ (OneDrive) still works."""
    name = str(name or "")
    if not PAPER_FILE.match(name) or name in (".", "..") or "/" in name or "\\" in name:
        return None, f"not a plain PDF file name: {name!r}"
    root = PAPERS.resolve()
    dest = (PAPERS / name)
    if dest.resolve().parent != root:
        return None, f"{name!r} would land outside papers/"
    return dest, ""


def pdf_destination(rec: dict, state: dict) -> tuple[Path | None, dict | None, str]:
    """Where an upload belongs: papers/<Key>.pdf for a citation key or a candidate with a key,
    papers/<cid>_<name> for a candidate without one (linked as its `pdf_file`).

    The record is untrusted input (anyone admitted by Access can write one): the id must be a
    candidate in the register or a key in citations.md, and every destination is a plain file
    name inside papers/."""
    rid = str(rec.get("id") or "").strip()
    if not rid:
        return None, None, "skip: no id"
    if not (CANDIDATE_ID.match(rid) or CITATION_KEY.match(rid)):
        return None, None, f"skip: {rid!r} is neither a candidate id nor a citation key"
    cands = state.setdefault("candidates", S.load_candidates())
    c = _candidate_for_id(cands, rid)
    if c is None:
        c = next((x for x in cands if x.get("key") and str(x["key"]).lstrip("@").lower() == rid.lstrip("@").lower()), None)
    if c is None:
        if rid.startswith("@") and rid.lstrip("@").lower() in _known_keys(state):
            dest, why = _inside_papers(f"{rid.lstrip('@')}.pdf")
            return (dest, None, "") if dest else (None, None, f"skip: {why}")
        return None, None, f"skip: no candidate or citation {rid}"
    if c.get("duplicate_of"):
        return None, c, f"skip: {rid} is a duplicate of {c['duplicate_of']}"
    if c.get("key"):
        key = str(c["key"]).lstrip("@")
        if not CITATION_KEY.match(key):
            return None, c, f"skip: candidate {c.get('id')} has a malformed key {c['key']!r}"
        name = f"{key}.pdf"
    elif c.get("pdf_file"):
        name = str(c["pdf_file"])
    else:
        name = f"{c['id']}_{_safe_name(rec.get('name'))}"
    dest, why = _inside_papers(name)
    return (dest, c, "") if dest else (None, c, f"skip: {why}")


def apply_pdf(rec: dict, by: str, execute: bool, state: dict) -> str:
    dest, cand, err = pdf_destination(rec, state)
    if err:
        return err
    bucket = str(rec.get("bucket") or "") or bucket_name()
    obj = str(rec.get("object") or "")
    local = rec.get("local_path")
    src = f"portal/.uploads ({local})" if local else f"{bucket}/{obj}"
    if dest.exists():
        if execute and not local and obj and bucket:
            FETCH["delete"](bucket, obj)
        return f"{dest.name}: already in papers/ — upload by {by} discarded ({src})"
    if not local and (not obj or not bucket):
        return "skip: record names no bucket object"
    size_kb = int(rec.get("bytes") or 0) // 1024
    if not execute:
        return f"would fetch {src} ({size_kb} KB) → papers/{dest.name}" + (f" and link it to {cand['id']}" if cand is not None and not cand.get("key") else "")
    PAPERS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "upload.pdf"
        if local:
            lp = (ROOT / str(local)).resolve()
            if not lp.exists() or PORTAL.resolve() not in lp.parents:
                return f"skip: local upload {local} not found"
            shutil.copy2(lp, tmp)
        else:
            e = FETCH["get"](bucket, obj, tmp)
            if e:
                return f"error: could not fetch {src}: {e}"
        data = tmp.read_bytes()
        if not data.startswith(b"%PDF-"):
            return f"error: {src} is not a PDF"
        want = str(rec.get("sha256") or "")
        if want and hashlib.sha256(data).hexdigest() != want:
            return f"error: {src} does not match the sha256 in the record"
        shutil.move(str(tmp), str(dest))
    if cand is not None and not cand.get("key") and cand.get("pdf_file") != dest.name:
        cand["pdf_file"] = dest.name
        state["candidates_dirty"] = True
    if local:
        lp = (ROOT / str(local)).resolve()
        for p in (lp, lp.with_suffix(".json")):
            if p.exists():
                p.unlink()
    elif obj and bucket:
        e = FETCH["delete"](bucket, obj)
        if e:
            print(f"      (left in the bucket: {e})")
    state["pdfs_added"] = state.get("pdfs_added", 0) + 1
    return f"papers/{dest.name} ← {src} ({size_kb} KB) by {by}" + (f"; linked to {cand['id']}" if cand is not None and not cand.get("key") else "")


# ------------------------------------------------------------------ run
DRAFT_KINDS = ("edit", "mark", "comment", "verdict")


def _order(files: list[Path], records: dict[Path, dict]) -> list[Path]:
    """Chronological, and within one send (same reviewer, same `submitted`) every edit, mark and
    comment before the verdict: the reviewer approves the draft with their own changes in it.
    (The portal writes a send's records with one time stamp; their file names alone would put the
    verdict, record 01, first.)"""
    def key(f: Path):
        r = records.get(f) or {}
        stamp = f.name.split("_", 1)[0].split("-", 1)[0]
        return (stamp, str(r.get("reviewer") or ""), str(r.get("submitted") or ""), 1 if r.get("kind") == "verdict" else 0, f.name)
    return sorted(files, key=key)


def _draft_digest(path: Path) -> str | None:
    try:
        fm, _ = parse_markdown(path)
        return RB.review_digest(fm)
    except Exception:  # noqa: BLE001
        return None


def run(execute: bool, promote: bool, only_kind: str | None, skip_kinds: tuple[str, ...] = (), intake: bool = False) -> int:
    files = sorted(INBOX.glob("*.json")) if INBOX.is_dir() else []
    if not files:
        print("logs/portal/inbox/ is empty — nothing to apply (did you git pull?)")
        return 0
    table = reviewers()
    unknown: set[str] = set()
    state: dict = {"batch_start": {}, "changes": {}}
    done: list[tuple[Path, str, str]] = []
    counts: dict[str, int] = {}
    statuses: dict[str, int] = {}
    ledger = load_ledger()
    later: list[dict] = []          # ledger lines that may only be written once the register is saved
    records: dict[Path, dict] = {}
    for f in files:
        try:
            records[f] = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as e:
            print(f"  ✗ {f.name}: not JSON ({e})")
    # the trusted reference for every draft a record touches: its digest before anything is applied
    for rec in records.values():
        if isinstance(rec, dict) and str(rec.get("kind")) in DRAFT_KINDS:
            d = _draft(str(rec.get("id")))
            if d is not None and str(d.resolve()) not in state["batch_start"]:
                state["batch_start"][str(d.resolve())] = _draft_digest(d)
    for f in _order(list(records), records):
        rec = records[f]
        if not isinstance(rec, dict):
            print(f"  ✗ {f.name}: not a record")
            continue
        kind = str(rec.get("kind"))
        if (only_kind and kind != only_kind) or kind in skip_kinds:
            continue
        rec["_record"] = f.name
        by, approver, known = who(rec.get("reviewer"), table)
        if not known:
            unknown.add(str(rec.get("reviewer")))
        if f.name in ledger:
            msg = Outcome(f"already dealt with ({ledger[f.name].get('status')}, {ledger[f.name].get('at', '')}) — archiving", ledger[f.name]["status"])
            print(f"  ✓ {f.name}\n      {msg}")
            done.append((f, msg.status, msg))
            continue
        target = _draft(str(rec.get("id"))) if kind in DRAFT_KINDS else None
        before = _draft_digest(target) if target is not None and execute else None
        try:
            if kind == "paper":
                msg = apply_paper(rec, by, execute, state)
            elif kind == "screen":
                msg = apply_screen(rec, by, execute, state)
            elif kind == "edit":
                msg = apply_edit(rec, by, execute, state)
            elif kind == "mark":
                msg = apply_mark(rec, by, execute, state)
            elif kind == "comment":
                msg = apply_comment(rec, by, execute, state)
            elif kind == "verdict":
                msg = apply_verdict(rec, by, approver, execute, promote, state)
            elif kind == "pdf":
                msg = apply_pdf(rec, by, execute, state)
            else:
                msg = f"skip: unknown kind {kind}"
        except Exception as e:  # noqa: BLE001
            msg = f"error: {e}"
        if target is not None and execute and target.exists():
            after = _draft_digest(target)
            if after != before:
                state["changes"].setdefault(str(target.resolve()), []).append(
                    (str(rec.get("reviewer") or "").lower(), str(rec.get("submitted") or "")))
        st = status_of(msg)
        statuses[st] = statuses.get(st, 0) + 1
        ok = st in FINAL
        counts[kind] = counts.get(kind, 0) + (1 if ok else 0)
        mark = {"applied": "✓", "recorded": "✓", "stale": "⚠", "blocked": "⚠"}.get(st, "·")
        print(f"  {mark} {f.name}  [{st}]\n      {msg}")
        if ok:
            done.append((f, st, msg))
            row = {"record": f.name, "status": st, "kind": kind, "id": str(rec.get("id")), "by": by,
                   "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "message": str(msg)[:300]}
            if execute:
                if kind in ("screen", "paper"):
                    later.append(row)            # only true once candidates.yaml is written
                else:
                    append_ledger([row])         # the effect is on disk already: replaying it must not redo it
    if execute:
        if state.get("candidates_dirty"):
            S.save_candidates(state["candidates"])
        append_ledger(later)
        APPLIED.mkdir(parents=True, exist_ok=True)
        for f, st, msg in done:
            data = records.get(f) or {}
            data.pop("_record", None)
            data["_outcome"] = {"status": st, "message": str(msg)[:500],
                                "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
            (APPLIED / f.name).write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            f.unlink()
        if done:
            _log(f"{dt.date.today().isoformat()} | PORTAL-APPLIED | — | {len(done)} record(s) | "
                 + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
                 + "".join(f", {n} {s}" for s, n in sorted(statuses.items()) if s in ("stale", "blocked"))
                 + f" | by: {', '.join(sorted({who((records.get(f) or {}).get('reviewer'), table)[0] for f, _, _ in done}))}")
        print(f"\n{len(done)} record(s) dealt with and moved to logs/portal/applied/ "
              f"({', '.join(f'{n} {s}' for s, n in sorted(statuses.items()))}); {len(files) - len(done)} left in the inbox. "
              "Commit screening/, drafts/ and logs/ and push: the explorer and the portal rebuild from the push.")
        if state.get("pdfs_added"):
            print(f"{state['pdfs_added']} PDF(s) landed in papers/ (OneDrive).")
            if intake:                  # cover sheets, OCR, link/check/name, register, rename, portal sync
                import intake_papers
                intake_papers.process(execute=True)
            else:
                print("Run `python scripts/intake_papers.py --execute` to clean, OCR, check, name and sync them.")
    else:
        print(f"\nDry run: {len(done)} of {len(files)} record(s) would be dealt with. Add --execute.")
    if unknown:
        print(f"Unknown reviewer email(s) — add them to portal/reviewers.yaml: {', '.join(sorted(unknown))}")
    if statuses.get("error"):
        print(f"⚠ {statuses['error']} record(s) failed part-way and stay in the inbox; the next run retries them "
              "without writing twice what they already wrote.")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--promote", action="store_true", help="run promote.py for approve/reject verdicts from approvers")
    ap.add_argument("--kind", choices=["paper", "screen", "verdict", "edit", "mark", "comment", "pdf"])
    ap.add_argument("--skip-pdf", action="store_true",
                    help="leave `pdf` records in the inbox (for CI, which has no papers/ folder to pull the uploads into)")
    ap.add_argument("--no-intake", action="store_true",
                    help="do not run intake_papers.py on the PDFs taken in (a caller that runs it itself)")
    args = ap.parse_args(argv)
    return run(args.execute, args.promote, args.kind, ("pdf",) if args.skip_pdf else (), intake=not args.no_intake)


if __name__ == "__main__":
    sys.exit(_cli())
