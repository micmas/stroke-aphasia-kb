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
  verdict  {id: drafts/<bucket>/<file>.md, verdict, rationale, per_finding: [{id, verdict, concern, supports_approval, passages}]}
           → the draft's `portal_reviews` list (who said what, with per-finding verdicts); with
             --promote and a reviewer listed as an approver in portal/reviewers.yaml, an `approve`
             runs auto_review.apply_manual_verdict (promote.py) as human:<name>; `reject` likewise
  edit     {id: draft, finding, fields: {field: {old, new}}, passages_added: [{page, quote, supports}]}
           → the finding, when the field still has the old value (else noted), stamped `edits: {by, date, fields}`
  mark     {id: draft, page, quote, note}
           → the draft's `reviewer_marks` (refocus.py turns them into findings)
  comment  {id: draft, finding?, text}
           → the finding's (or draft's) `portal_comments`

Reviewers are identified by the email Cloudflare Access verified. portal/reviewers.yaml
maps emails to the `human:<name>` used in the KB and says who may approve
(docs/GOVERNANCE.md §2); an unknown email is applied as `human:<local part>` with
no approval right, and listed so you can add it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import screen as SC  # noqa: E402
import screening as S  # noqa: E402
from aphasia_kb import parse_markdown  # noqa: E402

INBOX = ROOT / "logs" / "portal" / "inbox"
APPLIED = ROOT / "logs" / "portal" / "applied"
LOG = ROOT / "logs" / "extraction_log.md"
REVIEWERS = ROOT / "portal" / "reviewers.yaml"
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


def _log(line: str) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(line.rstrip() + "\n")


# ------------------------------------------------------------------ appliers
def apply_screen(rec: dict, by: str, execute: bool, state: dict) -> str:
    cands = state.setdefault("candidates", S.load_candidates())
    by_id = {c["id"]: c for c in cands}
    c = by_id.get(str(rec.get("id")))
    if c is None:
        return f"skip: no candidate {rec.get('id')}"
    stage = rec.get("stage") or "title_abstract"
    err = SC._apply_decision(c, stage, str(rec.get("decision")), rec.get("reason") or None, by, rec.get("note") or None,
                             str(rec.get("submitted") or "")[:10] or dt.date.today().isoformat(), seq=SC._next_seq(cands))
    if err:
        return f"skip: {err}"
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
                                          "fields": sorted(set(applied)), "via": "portal"})
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
    if any(isinstance(m, dict) and m.get("quote") == rec.get("quote") for m in marks):
        return f"{p.name}: mark already present"
    n = 1 + max([int(str(m.get("id", "m0"))[1:] or 0) for m in marks if isinstance(m, dict)] or [0])
    marks.append({"id": f"m{n}", "page": rec.get("page"), "quote": str(rec.get("quote") or "").strip(), "note": rec.get("note") or "",
                  "by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10] or dt.date.today().isoformat(), "status": "pending"})
    if execute:
        _write(p, fm, body)
    state.setdefault("touched", set()).add(p)
    return f"{p.name}: mark m{n} by {by} (python scripts/refocus.py {p.relative_to(ROOT)})"


def apply_comment(rec: dict, by: str, execute: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    entry = {"by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10], "text": str(rec.get("text") or "").strip()}
    target = fm
    if rec.get("finding"):
        target = next((x for x in fm.get("findings") or [] if isinstance(x, dict) and x.get("id") == rec.get("finding")), fm)
    target.setdefault("portal_comments", []).append(entry)
    if execute:
        _write(p, fm, body)
    state.setdefault("touched", set()).add(p)
    return f"{p.name}: comment by {by}"


def apply_verdict(rec: dict, by: str, approver: bool, execute: bool, promote: bool, state: dict) -> str:
    p = _draft(str(rec.get("id")))
    if p is None:
        return f"skip: no draft {rec.get('id')}"
    fm, body = parse_markdown(p)
    per = [x for x in rec.get("per_finding") or [] if isinstance(x, dict)]
    entry = {"by": f"human:{by}", "date": str(rec.get("submitted") or "")[:10], "verdict": rec.get("verdict"),
             "rationale": rec.get("rationale") or "", "approver": approver,
             "findings": [{k: x.get(k) for k in ("id", "verdict", "concern") if x.get(k) not in (None, "")}
                          | ({"passages": x["passages"]} if x.get("passages") else {}) for x in per]}
    fm.setdefault("portal_reviews", []).append(entry)
    if execute:
        _write(p, fm, body)
    state.setdefault("touched", set()).add(p)
    agree = sum(1 for x in per if x.get("verdict") == "agree")
    summary = f"{p.name}: {rec.get('verdict') or 'no overall verdict'} by {by} ({agree}/{len(per)} findings agreed)"
    if promote and approver and rec.get("verdict") in ("approve", "reject"):
        if any(m.get("status", "pending") == "pending" for m in fm.get("reviewer_marks") or [] if isinstance(m, dict)):
            return summary + " — not promoted: pending reviewer marks (refocus.py first)"
        if not execute:
            return summary + f" — would {rec.get('verdict')} via promote.py"
        import auto_review as AR  # noqa: WPS433
        try:
            final, _ = AR.apply_manual_verdict(p, verdict_override=rec["verdict"], rationale=rec.get("rationale") or "(portal review)",
                                               per_finding=[{"id": x.get("id"), "concern": x.get("concern") or "",
                                                             "supports_approval": x.get("verdict") == "agree"} for x in per],
                                               reviewer=f"human:{by}", auto_promote_on_approve=True)
            return summary + f" — {final} via promote.py"
        except Exception as e:  # noqa: BLE001
            return summary + f" — promote failed: {e}"
    if rec.get("verdict") == "approve" and not approver:
        return summary + " — recorded as an opinion (not an approver)"
    return summary


# ------------------------------------------------------------------ run
def run(execute: bool, promote: bool, only_kind: str | None) -> int:
    files = sorted(INBOX.glob("*.json")) if INBOX.is_dir() else []
    if not files:
        print("logs/portal/inbox/ is empty — nothing to apply (did you git pull?)")
        return 0
    table = reviewers()
    unknown: set[str] = set()
    state: dict = {}
    done: list[Path] = []
    counts: dict[str, int] = {}
    for f in files:
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as e:
            print(f"  ✗ {f.name}: not JSON ({e})")
            continue
        kind = str(rec.get("kind"))
        if only_kind and kind != only_kind:
            continue
        by, approver, known = who(rec.get("reviewer"), table)
        if not known:
            unknown.add(str(rec.get("reviewer")))
        try:
            if kind == "screen":
                msg = apply_screen(rec, by, execute, state)
            elif kind == "edit":
                msg = apply_edit(rec, by, execute, state)
            elif kind == "mark":
                msg = apply_mark(rec, by, execute, state)
            elif kind == "comment":
                msg = apply_comment(rec, by, execute, state)
            elif kind == "verdict":
                msg = apply_verdict(rec, by, approver, execute, promote, state)
            else:
                msg = f"skip: unknown kind {kind}"
        except Exception as e:  # noqa: BLE001
            msg = f"error: {e}"
        ok = not msg.startswith(("skip", "error"))
        counts[kind] = counts.get(kind, 0) + (1 if ok else 0)
        print(f"  {'✓' if ok else '·'} {f.name}\n      {msg}")
        if ok:
            done.append(f)
    if execute:
        if state.get("candidates_dirty"):
            S.save_candidates(state["candidates"])
        APPLIED.mkdir(parents=True, exist_ok=True)
        for f in done:
            shutil.move(str(f), str(APPLIED / f.name))
        if done:
            _log(f"{dt.date.today().isoformat()} | PORTAL-APPLIED | — | {len(done)} record(s) | "
                 + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f" | by: {', '.join(sorted({who(json.loads((APPLIED / f.name).read_text())['reviewer'], table)[0] for f in done}))}")
        print(f"\n{len(done)} record(s) applied and moved to logs/portal/applied/; {len(files) - len(done)} left in the inbox. "
              f"Commit screening/, drafts/ and logs/, then `python scripts/export_webapp.py` and `python scripts/publish_portal.py --deploy`.")
    else:
        print(f"\nDry run: {len(done)} of {len(files)} record(s) would be applied. Add --execute.")
    if unknown:
        print(f"Unknown reviewer email(s) — add them to portal/reviewers.yaml: {', '.join(sorted(unknown))}")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--promote", action="store_true", help="run promote.py for approve/reject verdicts from approvers")
    ap.add_argument("--kind", choices=["screen", "verdict", "edit", "mark", "comment"])
    args = ap.parse_args(argv)
    return run(args.execute, args.promote, args.kind)


if __name__ == "__main__":
    sys.exit(_cli())
