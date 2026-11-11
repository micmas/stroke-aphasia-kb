#!/usr/bin/env python3
"""
review_binding.py — what a portal review is bound to: a digest of the draft as the reviewer saw it.

The portal build (publish_portal.py) writes portal/dist/drafts.json: for every draft, its
`digest`, its finding ids and its open obligations. A reviewer's `verdict` record carries the
digest and the finding ids it was given. portal_import.py recomputes the digest from the file
and applies an approval only when the draft is still what the reviewer reviewed (REVIEW.md #10).

The digest covers everything a decision is about: every frontmatter field, every finding, the
reviewer marks and their status (open marks are obligations that must be resolved first),
and the edit stamps. It leaves out only the opinion and conversation lists that reviewing itself
appends (`portal_reviews`, and `portal_comments` on the draft or a finding), so that one person's
verdict or comment does not invalidate another's review of the same content.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

EXCLUDED_TOP = ("portal_reviews", "portal_comments")
EXCLUDED_FINDING = ("portal_comments",)
RESOLVED_MARKS = ("done", "dismissed")


def review_content(fm: dict) -> dict:
    """The frontmatter less what reviewing appends (see the module docstring)."""
    out = {k: copy.deepcopy(v) for k, v in (fm or {}).items() if k not in EXCLUDED_TOP}
    if isinstance(out.get("findings"), list):
        out["findings"] = [{k: v for k, v in f.items() if k not in EXCLUDED_FINDING} if isinstance(f, dict) else f
                           for f in out["findings"]]
    return out


def review_digest(fm: dict) -> str:
    text = json.dumps(review_content(fm), sort_keys=True, ensure_ascii=False, default=str, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def finding_ids(fm: dict) -> list[str]:
    return [str(f.get("id")) for f in (fm or {}).get("findings") or [] if isinstance(f, dict) and f.get("id") is not None]


def open_obligations(fm: dict) -> list[str]:
    """Reviewer marks nobody has resolved: `pending` (not yet re-extracted) and `unresolved`
    (refocus.py could not answer it) both still need a person."""
    return [str(m.get("id") or "?") for m in (fm or {}).get("reviewer_marks") or []
            if isinstance(m, dict) and str(m.get("status") or "pending") not in RESOLVED_MARKS]


def binding(fm: dict) -> dict:
    return {"digest": review_digest(fm), "findings": finding_ids(fm), "obligations": open_obligations(fm)}


def drafts_bindings(root: Path) -> dict[str, dict]:
    """{drafts/<bucket>/<file>.md: binding} for the active drafts (backups and review scratch left out)."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from aphasia_kb import parse_markdown  # noqa: WPS433
    out: dict[str, dict] = {}
    base = root / "drafts"
    if not base.is_dir():
        return out
    for p in sorted(base.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        if any(part.startswith("_") for part in p.relative_to(base).parts[:-1]):
            continue
        try:
            fm, _ = parse_markdown(p)
        except Exception:  # noqa: BLE001 — an unreadable draft is not in the export either
            continue
        if isinstance(fm, dict):
            out[rel] = binding(fm)
    return out
