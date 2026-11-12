"""
promote.py — review and promote draft KB entries.

Usage:
    python scripts/promote.py --list                 # show pending drafts
    python scripts/promote.py --show drafts/regions/ho-cort_44__Fridriksson2018.md
    python scripts/promote.py --diff drafts/regions/ho-cort_44__Fridriksson2018.md
    python scripts/promote.py --approve drafts/regions/ho-cort_44__Fridriksson2018.md \
                      --reviewer "michele"
    python scripts/promote.py --reject  drafts/regions/ho-cort_44__Fridriksson2018.md \
                      --reviewer "michele" --reason "sample too small"

Approve uses atomic file replacements and a recoverable journal:
  1. Validates the draft against v2 schema. Refuses if invalid.
  2. Sets status: approved, reviewer:, reviewed_on:.
  3. If a file with the same id already exists in the canonical folder,
     merges the draft's findings into it (giving them fresh f-ids).
     Otherwise, moves the draft to the canonical folder.
  4. Removes the draft file.
  5. Appends a line to logs/extraction_log.md.

This script is the *only* way an entry is supposed to leave drafts/.

Review provenance (docs/GOVERNANCE.md, schema v2.5)
----------------------------------------------
--reviewer is normalised to `human:<name>` or `model:<ollama-tag>`.
A bare name is treated as a person. `auto-reviewer` is refused: the
deterministic checks never approve anything.

A model reviewer may only approve Tier A drafts and must name the
extractor it is independent of:

    python scripts/promote.py --approve <draft> --reviewer model:gemma4:31b \
        --tier A --extractor agent:gemma4:26b

The approval is stamped on every finding (`review: {reviewer,
reviewed_on, tier}`) so a canonical entry that accumulates findings from
several reviews reports each one honestly, and the log line reads
`MODEL-APPROVED` instead of `APPROVED`.
"""

from __future__ import annotations

import argparse
import hashlib
import datetime as dt
import difflib
import re
import shutil
import sys
from pathlib import Path

import yaml

# Reuse the validator from the loader
sys.path.insert(0, str(Path(__file__).parent))
from aphasia_kb import (
    parse_markdown, _validate_v2_entry,
    KnowledgeBase, REVIEWER_PREFIXES, REVIEW_TIER_VOCAB,
)

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
LOG = ROOT / "logs/extraction_log.md"


# ============================================================
# Helpers
# ============================================================
def _read(path: Path) -> tuple[dict, str, str]:
    """Return (frontmatter_dict, body_string, full_text)."""
    text = path.read_text(encoding="utf-8")
    fm, body = parse_markdown(path)
    return fm, body, text


def _write(path: Path, fm: dict, body: str):
    """Serialize frontmatter + body back to markdown."""
    yaml_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True,
                               default_flow_style=False)
    from pipeline_files import atomic_write
    atomic_write(path, f"---\n{yaml_text}---\n{body}")


def normalize_reviewer(raw: str) -> str:
    """`michele` -> `human:michele`; prefixed values pass through.

    Refuses the deterministic reviewer name: under docs/GOVERNANCE.md §2 the
    automatic checks can reject or defer but never approve.
    """
    r = (raw or "").strip()
    if not r:
        raise ValueError("reviewer is required")
    low = r.lower()
    if low in ("auto-reviewer", "auto_reviewer", "auto"):
        raise ValueError("'auto-reviewer' cannot approve or reject; "
                         "use human:<name> or model:<tag>")
    if low.startswith(REVIEWER_PREFIXES):
        if not r.split(":", 1)[1].strip():
            raise ValueError("reviewer name or tag must not be empty")
        return r
    if ":" in r:
        raise ValueError(f"reviewer {r!r} must start with one of "
                         f"{REVIEWER_PREFIXES}")
    return f"human:{r}"


def _bare_tag(s: str | None) -> str:
    """Strip agent:/model: prefixes so extractor and reviewer tags compare."""
    from review_identity import model_tag
    return model_tag(s)


def validate_review_args(reviewer: str, tier: str | None,
                         extractor: str | None, fm: dict) -> list[str]:
    """Policy checks for an approval. Returns a list of problems."""
    problems: list[str] = []
    if tier is not None and tier not in REVIEW_TIER_VOCAB - {"legacy"}:
        problems.append(f"--tier must be A or B, got {tier!r}")
    if reviewer.lower().startswith("model:"):
        if tier != "A":
            problems.append("a model reviewer may only approve Tier A "
                            "drafts (--tier A); anything else needs a person")
        ext = extractor or fm.get("created_by")
        if not _bare_tag(ext) or not _bare_tag(reviewer):
            problems.append("a model approval must name the extractor "
                            "(--extractor agent:<tag>) so independence "
                            "can be checked")
        elif extractor and fm.get("created_by") and _bare_tag(extractor) != _bare_tag(fm["created_by"]):
            problems.append("--extractor disagrees with recorded created_by")
        elif _bare_tag(ext) == _bare_tag(reviewer):
            problems.append(f"reviewer {reviewer!r} is the same model as the "
                            f"extractor {ext!r}; a model never reviews its "
                            f"own drafts")
    return problems


def _bucket_for(draft_path: Path) -> str:
    """Return regions/impairments/therapies/predictors for a draft path."""
    from pipeline_files import BUCKETS
    relative = draft_path.resolve().relative_to((ROOT / "drafts").resolve())
    if len(relative.parts) != 2 or relative.parts[0] not in BUCKETS:
        raise ValueError(f"Not an active draft path: {draft_path}")
    return relative.parts[0]


def _canonical_path_for(fm: dict, bucket: str) -> Path:
    """Where the entry should live once approved."""
    from pipeline_files import safe_child
    return safe_child(ROOT / bucket, f"{fm['id']}.md")


def _next_finding_id(existing_ids: set[str], wanted: str) -> str:
    """If `wanted` is taken, return the next free f<n> id."""
    if wanted not in existing_ids:
        return wanted
    n = 1
    while f"f{n}" in existing_ids:
        n += 1
    return f"f{n}"


# ============================================================
# Commands
# ============================================================
def cmd_list(args):
    kb = KnowledgeBase(ROOT, include=["draft", "in_review"])
    if kb.drafts.empty:
        print("No pending drafts.")
        return
    print(f"{len(kb.drafts)} pending draft(s):\n")
    for r in kb.drafts.itertuples():
        print(f"  [{r.status:<10s}] {r.path}  ({r.n_findings} findings)")
        print(f"               id={r.id}  by={r.created_by}  on={r.created_on}")


def cmd_show(args):
    p = Path(args.show)
    print(p.read_text(encoding="utf-8"))


def cmd_diff(args):
    """Show what would change in the canonical file if this draft were approved."""
    draft = Path(args.diff)
    fm_d, body_d, text_d = _read(draft)
    canonical = _canonical_path_for(fm_d, _bucket_for(draft))
    if not canonical.exists():
        print(f"(no existing canonical file at {canonical} — draft becomes a new entry)")
        print(text_d)
        return
    text_c = canonical.read_text(encoding="utf-8")
    diff = difflib.unified_diff(
        text_c.splitlines(keepends=True),
        text_d.splitlines(keepends=True),
        fromfile=str(canonical), tofile=str(draft),
    )
    sys.stdout.writelines(diff)


def cmd_approve(args):
    import fcntl
    from promotion_transaction import recover_pending
    draft = Path(args.approve).resolve()
    _bucket_for(draft)
    # Lock covers read/merge as well as recovery and writes.
    with (ROOT / '.promotion.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if recover_pending(ROOT, draft):
            print('Recovered interrupted promotion')
            return
        return _approve_locked(args)


def _approve_locked(args):
    draft = Path(args.approve).resolve()
    fm, body, _ = _read(draft)
    bucket = _bucket_for(draft)

    # 1. Validate
    issues = []
    _validate_v2_entry(fm, str(draft), issues)
    if issues:
        print(f"❌ Cannot approve — {len(issues)} validation issue(s):")
        for i in issues:
            print(f"  {i}")
        sys.exit(1)

    # 1a. Reviewer marks (review_app.py): passages the reviewer flagged for
    # re-extraction must be resolved first — refocus.py turns them into
    # findings, or the reviewer removes them in the workbench.
    pending = [m.get("id") for m in fm.get("reviewer_marks") or []
               if isinstance(m, dict) and m.get("status", "pending") not in ("done", "dismissed")]
    if pending:
        print(f"❌ Cannot approve — {len(pending)} reviewer mark(s) still pending "
              f"({', '.join(map(str, pending))}): run scripts/refocus.py on the draft, or remove "
              f"them in scripts/review_app.py")
        sys.exit(1)
    if not isinstance(fm.get("findings"), list) or not fm["findings"]:
        raise ValueError("Cannot approve an empty entry")
    fm.pop("reviewer_marks", None)   # the register of marks stays in the draft's history, not in the KB

    # 1b. Policy checks (docs/GOVERNANCE.md §2–§3)
    problems = validate_review_args(args.reviewer, args.tier,
                                    args.extractor, fm)
    if problems:
        print("❌ Cannot approve — review policy:")
        for pr in problems:
            print(f"  {pr}")
        sys.exit(1)

    # Recompute the policy at the one canonical-write boundary. A caller's
    # --tier and --extractor labels are not evidence of a second reading.
    import auto_review as AR
    checks = AR.run_deterministic_checks(fm, draft, papers_dir=ROOT / "papers")
    pdf = next((c for c in checks if c.name == "pdf_quote_match"), None)
    if pdf is not None and pdf.passed is False:
        raise ValueError("Cannot approve: absent source passages")
    actual_tier, reasons = AR.classify_tier(fm, checks, draft, root=ROOT)
    if args.reviewer.lower().startswith("model:"):
        if actual_tier != "A":
            raise ValueError("Model approval requires actual Tier A: " + "; ".join(reasons))
        report_path = ROOT / "logs/auto_review" / bucket / f"{draft.stem}.yaml"
        report = yaml.safe_load(report_path.read_text()) if report_path.exists() else {}
        run = ((report or {}).get("runs") or [{}])[-1]
        llm = run.get("llm_review") or {}
        if (run.get("draft_sha256") != hashlib.sha256(draft.read_bytes()).hexdigest()
                or run.get("verdict") != AR.Verdict.APPROVE
                or run.get("review_tier") != "A"
                or _bare_tag(llm.get("model")) != _bare_tag(args.reviewer)
                or not llm.get("independent") or not llm.get("unanimous")):
            raise ValueError("Model approval requires a current, unanimous independent review report")
        for finding in fm.get("findings") or []:
            author = (finding.get("provenance") or {}).get("extracted_by")
            if author and not AR.reviewer_is_independent(author, args.reviewer):
                raise ValueError("Cannot establish independence from every finding's extractor")
    args.tier = actual_tier

    # 2. Stamp approval
    today = dt.date.today().isoformat()
    fm["status"]      = "approved"
    fm["reviewer"]    = args.reviewer
    fm["reviewed_on"] = today
    if args.tier:
        fm["review_tier"] = args.tier
    review_block = {"reviewer": args.reviewer, "reviewed_on": today}
    if args.tier:
        review_block["tier"] = args.tier
    extractor = args.extractor or fm.get("created_by")
    if args.reviewer.lower().startswith("model:") and extractor:
        review_block["extractor"] = extractor
    for f in fm.get("findings") or []:
        f["review"] = dict(review_block)

    # 3. Merge or move
    canonical = _canonical_path_for(fm, bucket)
    if canonical.exists():
        fm_c, body_c, _ = _read(canonical)
        existing_ids = {f.get("id") for f in (fm_c.get("findings") or [])}
        merged = list(fm_c.get("findings") or [])
        added  = []
        for f in fm.get("findings") or []:
            new_id = _next_finding_id(existing_ids, f.get("id", "f1"))
            f = dict(f)
            f["id"] = new_id
            existing_ids.add(new_id)
            merged.append(f)
            added.append(new_id)
        fm_c["findings"] = merged
        fm_c["last_reviewed"] = fm["reviewed_on"]
        # The file-level reviewer stays whoever approved the entry first;
        # per-finding `review` blocks carry the truth for merged findings.
        output_fm, output_body = fm_c, body_c
        message = (f"✓ Merged {len(added)} new finding(s) ({', '.join(added)}) "
                   f"into {canonical.relative_to(ROOT)}")
    else:
        canonical.parent.mkdir(parents=True, exist_ok=True)
        output_fm, output_body = fm, body
        message = f"✓ Promoted {draft.name} → {canonical.relative_to(ROOT)}"

    # 4. Prepare the audit entry before any canonical mutation
    cite = "?"
    for f in fm.get("findings") or []:
        if f.get("citation"):
            cite = f["citation"]; break
    LOG.parent.mkdir(parents=True, exist_ok=True)
    action = ("MODEL-APPROVED" if args.reviewer.lower().startswith("model:")
              else "APPROVED")
    extra = ""
    if action == "MODEL-APPROVED":
        extra += f" | extractor: {extractor}"
    if args.tier:
        extra += f" | tier: {args.tier}"
    line = (f"{today} | {action} | {cite} | "
            f"{fm.get('id')} | reviewer: {args.reviewer}{extra}\n")
    from promotion_transaction import commit
    text = '---\n' + yaml.safe_dump(output_fm, sort_keys=False, allow_unicode=True) + '---\n' + output_body
    opinions = fm.get('portal_reviews') or []
    latest = opinions[-1] if opinions and isinstance(opinions[-1], dict) else {}
    record_ids = ([latest['record']] if latest.get('record') and not latest.get('stale')
                  and latest.get('by') == args.reviewer and latest.get('verdict') == 'approve' else [])
    commit(ROOT, draft, canonical, text, LOG, line, record_ids=record_ids)
    print(message)
    print(f"  logged: {line.strip()}")


def cmd_reject(args):
    draft = Path(args.reject)
    fm, body, _ = _read(draft)
    fm["status"]   = "rejected"
    fm["reviewer"] = args.reviewer
    fm["reviewed_on"] = dt.date.today().isoformat()
    fm.setdefault("notes", "")
    fm["notes"] = (str(fm.get("notes") or "")
                   + f"\n\nRejected {dt.date.today().isoformat()} by {args.reviewer}: "
                   + (args.reason or "(no reason given)"))
    _write(draft, fm, body)
    print(f"✗ Marked rejected: {draft}")
    cite = "?"
    for f in fm.get("findings") or []:
        if f.get("citation"):
            cite = f["citation"]; break
    line = (f"{dt.date.today().isoformat()} | REJECTED | {cite} | "
            f"{fm.get('id')} | reviewer: {args.reviewer} | reason: "
            f"{args.reason or '(none)'}\n")
    with LOG.open("a") as fh:
        fh.write(line)
    print(f"  logged: {line.strip()}")


# ============================================================
# Main
# ============================================================
def resolve_passage_edit(record_path, canonical, source_pdf, actor, execute=False):
    """Complete an explicitly authorized, passage-only portal edit after promotion.

    Claims, finding IDs and original approval stamps are preserved. The caller must
    inspect the cited PDF page; this operation records a correction, not a new review.
    """
    import json
    import fcntl
    import pymupdf
    from pipeline_files import atomic_write, BUCKETS
    from promotion_transaction import commit, recover_pending
    from quote_check import PaperText, grade_quote
    record_path, canonical, source_pdf = map(lambda p: Path(p).resolve(), (record_path, canonical, source_pdf))
    if record_path.parent != (ROOT / 'logs/portal/inbox').resolve():
        raise ValueError('Correction must name an inbox record')
    if not actor.startswith(('agent:', 'human:')):
        raise ValueError('Name the actual operator as agent: or human:')
    archived = ROOT / 'logs/portal/applied' / record_path.name
    if not record_path.exists():
        if archived.exists() and json.loads(archived.read_text()).get('_outcome', {}).get('status') == 'applied':
            return 'Already resolved'
        raise ValueError('Missing inbox record')
    rec = json.loads(record_path.read_text())
    if rec.get('kind') != 'edit' or rec.get('fields') or not rec.get('passages_added'):
        raise ValueError('Only passage-only edits can use this correction path')
    original = Path(str(rec.get('id', '')))
    if original.parts[:1] != ('drafts',) or len(original.parts) != 3 or original.parts[1] not in BUCKETS or '__' not in original.stem:
        raise ValueError('Invalid original draft identity')
    entry, key = original.stem.split('__', 1)
    if canonical != (ROOT / original.parts[1] / (entry + '.md')).resolve():
        raise ValueError('Canonical entry does not match the original draft')
    if rec.get('citation') != '@' + key or source_pdf.stem != key:
        raise ValueError('Citation/PDF identity mismatch')
    stage = ROOT / 'drafts/_review' / ('passage-correction-' + record_path.name)
    with (ROOT / '.promotion.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if execute:
            recover_pending(ROOT, stage)
        fm, body, _ = _read(canonical)
        matches = [f for f in fm.get('findings', []) if f.get('citation') == rec['citation']]
        if fm.get('status') != 'approved' or len(matches) != 1:
            raise ValueError('Requires one unambiguous approved finding for this citation')
        finding = matches[0]
        already = any(e.get('record') == record_path.name for e in finding.get('edits', []))
        passages = []
        with pymupdf.open(source_pdf) as doc:
            for q in rec['passages_added']:
                page = q.get('page')
                if type(page) is not int or not 1 <= page <= len(doc):
                    raise ValueError('Invalid source page')
                raw = doc[page - 1].get_text()
                # Recover only PDF whitespace/soft-hyphen differences, never paraphrases.
                indices = [i for i, ch in enumerate(raw) if not ch.isspace() and ch != '\u00ad']
                compact = ''.join(raw[i] for i in indices)
                wanted = ''.join(ch for ch in str(q.get('quote') or '') if not ch.isspace() and ch != '\u00ad')
                pos = compact.find(wanted)
                if len(wanted) < 20 or pos < 0 or compact.find(wanted, pos + 1) >= 0:
                    raise ValueError('Passage is absent or ambiguous on its stated page')
                quote = raw[indices[pos]:indices[pos + len(wanted) - 1] + 1]
                if grade_quote(quote, PaperText.from_text(raw)) != 'exact':
                    raise ValueError('Recovered quote does not exactly match the PDF')
                passages.append({'section': 'Statistical analysis (portal correction)', 'page': page,
                                 'quote': quote, 'supports': q.get('supports') or 'statistics'})
        if not execute:
            return f"Would add {len(passages)} source passage(s) to {canonical.name} {finding['id']} and resolve {record_path.name}"
        today = dt.date.today().isoformat()
        if not already:
            finding.setdefault('source_passages', []).extend(passages)
            finding.setdefault('edits', []).append({'by': actor, 'date': today, 'fields': ['source_passages'],
                'record': record_path.name, 'requested_by': rec.get('reviewer'),
                'source_pdf_sha256': hashlib.sha256(source_pdf.read_bytes()).hexdigest(),
                'note': 'Completed user-authorized passage-only correction after promotion; source page inspected; original approval preserved.'})
            atomic_write(stage, json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
            text = '---\n' + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + '---\n' + body
            line = f"{today} | SOURCE-CORRECTED | {rec['citation']} | {fm['id']} {finding['id']} | operator: {actor} | record: {record_path.name}\n"
            commit(ROOT, stage, canonical, text, LOG, line, record_ids=[record_path.name])
        rec['_outcome'] = {'status': 'applied', 'message': f"Source passages added to {canonical.relative_to(ROOT)} {finding['id']}; original approval preserved", 'by': actor, 'at': dt.datetime.now(dt.timezone.utc).isoformat()}
        atomic_write(archived, json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
        record_path.unlink()
        return rec['_outcome']['message']


def main(argv=None):
    p = argparse.ArgumentParser(description="Review/promote draft KB entries")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--list",    action="store_true", help="list pending drafts")
    g.add_argument("--show",    metavar="PATH",      help="print one draft")
    g.add_argument("--diff",    metavar="PATH",      help="diff against canonical")
    g.add_argument("--approve", metavar="PATH",      help="approve a draft")
    g.add_argument("--reject",  metavar="PATH",      help="reject a draft")
    g.add_argument("--resolve-passage-edit", metavar="RECORD", help="resolve an authorized passage-only edit after promotion (preview unless --execute)")
    p.add_argument("--canonical", help="approved entry for the source correction")
    p.add_argument("--source-pdf", help="main PDF inspected for the source correction")
    p.add_argument("--actor", help="actual correction operator, agent:<name> or human:<name>")
    p.add_argument("--execute", action="store_true", help="write a source correction")
    p.add_argument("--reviewer", help="human:<name> (a bare name is a person) "
                                      "or model:<ollama-tag>; required for "
                                      "approve/reject")
    p.add_argument("--reason",   help="reason for rejection")
    p.add_argument("--tier", choices=["A", "B"], default=None,
                   help="review tier from auto_review.py's classification; "
                        "required (and must be A) for a model reviewer")
    p.add_argument("--extractor", default=None,
                   help="agent:<tag> that wrote the draft (default: the "
                        "draft's created_by); a model reviewer must differ")
    args = p.parse_args(argv)

    if args.resolve_passage_edit:
        if not all((args.canonical, args.source_pdf, args.actor)):
            p.error("Source correction requires --canonical, --source-pdf and --actor")
        print(resolve_passage_edit(args.resolve_passage_edit, args.canonical, args.source_pdf, args.actor, args.execute))
        return
    if args.approve and not args.reviewer:
        p.error("--approve requires --reviewer")
    if args.reject and not args.reviewer:
        p.error("--reject requires --reviewer")
    if args.reviewer:
        try:
            args.reviewer = normalize_reviewer(args.reviewer)
        except ValueError as e:
            p.error(str(e))

    if args.list:    cmd_list(args)
    if args.show:    cmd_show(args)
    if args.diff:    cmd_diff(args)
    if args.approve: cmd_approve(args)
    if args.reject:  cmd_reject(args)


if __name__ == "__main__":
    main()
