#!/usr/bin/env python3
"""
rereview.py — send pre-policy ("legacy") entries back for a proper review.

    python scripts/rereview.py                       # what would move: every legacy entry, by bucket
    python scripts/rereview.py --bucket therapies    # one bucket (therapies first: GOVERNANCE.md §5)
    python scripts/rereview.py --entry semantic_feature_analysis
    python scripts/rereview.py --bucket therapies --execute --by michele

A legacy entry is a canonical entry stamped `review_tier: legacy`: approved before the
governance policy, by the auto-reviewer or a model, without a person re-reading the
paper (docs/GOVERNANCE.md §5). The way out is the ordinary review: a person reads the
findings beside the PDF and approves again. That needs the findings to be drafts, so
this script moves each legacy entry back into drafts/ — one draft per paper, named
<id>__<Key>.md like every other draft, with status `in_review` — and removes the
canonical file. From there the review portal, review_app.py and promote.py work as
usual; the first approval re-creates the canonical entry and later ones merge into it.

When a fresh draft for the same paper already exists (the paper was re-extracted by the
current model), the pre-policy findings for that paper are dropped, not moved: the fresh
reading supersedes them. The log line records how many were dropped and for which paper.

What is kept: every field and every finding, the body text, and the old approval under
`previous_review` (file level: reviewer, date, tier; per finding when it had its own
`review` block), plus `rereview_of: <bucket>/<id>.md` and `rereview_on`. What is
removed from the draft: `reviewer`, `reviewed_on`, `review_tier`, `audited_by` and the
per-finding `review` blocks — the new approval writes fresh ones.

While an entry is out for re-review it is absent from the approved export (the explorer
shows it in the drafts export); that is the point. Findings without a citation cannot be
checked against a paper and go to a single draft <id>__nocitation.md, flagged.

Every move is logged: REREVIEW | @Keys | id | by: human:<name> | <n> drafts | previous: <reviewer>.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
from aphasia_kb import parse_markdown  # noqa: E402

BUCKETS = ("therapies", "regions", "impairments", "predictors", "reviews", "ingredients")
LOG = ROOT / "logs" / "extraction_log.md"
STRIP_FILE = ("reviewer", "reviewed_on", "review_tier", "audited_by", "last_reviewed")
STRIP_FINDING = ("review",)


def _write(path: Path, fm: dict, body: str) -> None:
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    path.write_text(f"---\n{text}---\n{body}", encoding="utf-8")


def legacy_entries(root: Path = ROOT, buckets=BUCKETS) -> list[tuple[str, Path, dict, str]]:
    """(bucket, path, frontmatter, body) of every canonical entry tagged legacy."""
    out = []
    for b in buckets:
        d = root / b
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                fm, body = parse_markdown(p)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(fm, dict) and fm.get("status") == "approved" and fm.get("review_tier") == "legacy":
                out.append((b, p, fm, body))
    return out


def _key(citation) -> str:
    return str(citation or "").strip().lstrip("@")


def split_by_paper(fm: dict) -> dict[str, list[dict]]:
    """Findings grouped by citation key ('' for findings with none), in file order."""
    groups: dict[str, list[dict]] = {}
    for f in fm.get("findings") or []:
        if not isinstance(f, dict):
            continue
        groups.setdefault(_key(f.get("citation")), []).append(f)
    return groups


def draft_for(fm: dict, body: str, key: str, findings: list[dict], bucket: str, path: Path, today: str) -> dict:
    """The draft frontmatter for one paper's findings of a legacy entry."""
    d = {k: v for k, v in fm.items() if k not in STRIP_FILE and k != "findings"}
    d["status"] = "in_review"
    prev = {k: fm.get(k) for k in ("reviewer", "reviewed_on", "review_tier", "audited_by") if fm.get(k) is not None}
    prev["reason"] = "approved before the governance policy (GOVERNANCE.md §5); re-review against the paper"
    d["previous_review"] = prev
    d["rereview_of"] = f"{bucket}/{path.name}"
    d["rereview_on"] = today
    new_findings = []
    for f in findings:
        g = {k: v for k, v in f.items() if k not in STRIP_FINDING}
        if isinstance(f.get("review"), dict):
            g["previous_review"] = f["review"]
        new_findings.append(g)
    if not key:
        d.setdefault("notes", "")
        d["notes"] = (str(d.get("notes") or "") + "\n\nRe-review: these findings carry no citation and cannot be checked "
                      "against a paper. Find the source or reject them.").strip()
    d["findings"] = new_findings
    return d


def plan(entries, drafts_root: Path) -> list[dict]:
    """What each legacy entry becomes: [{bucket, path, fm, body, drafts: [(draft_path, key, n_findings)], blocked: [...]}]"""
    items = []
    for b, p, fm, body in entries:
        groups = split_by_paper(fm)
        drafts, superseded = [], []
        for key, fs in groups.items():
            eid = str(fm.get("id"))
            stem = eid if key and eid.endswith(f"__{key}") else f"{eid}__{key or 'nocitation'}"
            dp = drafts_root / b / f"{stem}.md"
            if dp.exists():
                # a fresh extraction of the same paper is already waiting for review: it
                # supersedes the pre-policy findings, which are dropped (and logged), not kept
                superseded.append((dp, key, len(fs)))
                continue
            drafts.append((dp, key, len(fs)))
        items.append({"bucket": b, "path": p, "fm": fm, "body": body, "drafts": drafts, "superseded": superseded, "groups": groups})
    return items


def run(buckets, entry_ids, execute: bool, by: str | None, root: Path = ROOT) -> int:
    entries = legacy_entries(root, buckets)
    if entry_ids:
        entries = [e for e in entries if e[2].get("id") in set(entry_ids)]
    if not entries:
        print("No legacy entries match (kb_status.py shows how many there are).")
        return 0
    if execute and not by:
        print("--execute needs --by <name>: the person who sends these entries back for review is logged.", file=sys.stderr)
        return 2
    today = dt.date.today().isoformat()
    items = plan(entries, root / "drafts")
    moved = 0
    for it in items:
        fm, p, b = it["fm"], it["path"], it["bucket"]
        n_f = len(fm.get("findings") or [])
        print(f"{b}/{p.name}  ({n_f} findings, approved by {fm.get('reviewer')!r} on {fm.get('reviewed_on')})")
        for dp, key, n in it["superseded"]:
            print(f"  ✗ {n} finding{'s' if n != 1 else ''} for @{key} dropped: a fresh extraction is already waiting in {dp.relative_to(root).as_posix()}")
        for dp, key, n in it["drafts"]:
            print(f"  → {dp.relative_to(root).as_posix()}  ({n} finding{'s' if n != 1 else ''}{'' if key else ', no citation'})")
        if not it["drafts"] and not it["superseded"]:
            print("  (no findings)")
        if not execute:
            continue
        for dp, key, n in it["drafts"]:
            dp.parent.mkdir(parents=True, exist_ok=True)
            _write(dp, draft_for(fm, it["body"], key, it["groups"][key], b, p, today), it["body"])
        p.unlink()
        keys = ", ".join(f"@{k}" if k else "(no citation)" for _, k, _ in it["drafts"]) or "—"
        dropped = "; ".join(f"{n} for @{k} superseded by a fresh draft" for _, k, n in it["superseded"])
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(f"{today} | REREVIEW | {keys} | {fm.get('id')} | by: human:{by} | {len(it['drafts'])} draft(s) | previous: {fm.get('reviewer')}"
                     + (f" | dropped: {dropped}" if dropped else "") + "\n")
        moved += 1
    if execute:
        print(f"\n{moved} entr{'y' if moved == 1 else 'ies'} moved back to drafts/. Next: review them in the portal or review_app.py and approve with promote.py; "
              f"then `python scripts/export_webapp.py …` and `python scripts/publish_portal.py --deploy`.")
    else:
        n_drop = sum(n for it in items for _, _, n in it["superseded"])
        print(f"\nDry run: {len(items)} entr{'y' if len(items) == 1 else 'ies'} would move ({sum(len(it['drafts']) for it in items)} drafts"
              + (f"; {n_drop} finding(s) dropped as superseded by fresh drafts" if n_drop else "") + "). Add --execute --by <name>.")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--bucket", action="append", choices=BUCKETS, help="only this bucket (repeatable); default: all")
    ap.add_argument("--entry", action="append", metavar="ID", help="only this entry id (repeatable)")
    ap.add_argument("--execute", action="store_true", help="move the files (default: show what would move)")
    ap.add_argument("--by", help="who sends them back (logged as human:<name>); required with --execute")
    args = ap.parse_args(argv)
    buckets = tuple(args.bucket) if args.bucket else BUCKETS
    by = re.sub(r"^human:", "", args.by) if args.by else None
    return run(buckets, args.entry or [], args.execute, by)


if __name__ == "__main__":
    sys.exit(_cli())
