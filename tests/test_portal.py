#!/usr/bin/env python3
"""
test_portal.py — the review portal's two Python halves, without Cloudflare or a browser:
publish_portal.py sorts annotated PDFs by licence and bundles the screening queue;
portal_import.py applies the records the portal writes (screen, edit, mark, comment,
verdict) under the reviewer's name and refuses what no longer matches.

    python tests/test_portal.py
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root
sys.path.insert(0, str(ROOT / "scripts"))

DRAFT = """---
schema_version: 2.8
id: left_angular_gyrus
name: Left angular gyrus
kind: atlas
status: draft
created_by: agent:test
created_on: 2026-11-05
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Damage to the left angular gyrus is associated with poorer naming accuracy.
  direction: likely
  relationship: causal
  citation: '@TestPaper2020'
  method: VLSM
  strength: moderate
  source_passages:
  - {section: Abstract, page: 1, quote: Damage to the left angular gyrus was associated with poorer naming., supports: claim}
---
Test draft.
"""


class Publish(unittest.TestCase):
    def test_pdfs_sorted_by_licence(self):
        import publish_portal as P
        with tempfile.TemporaryDirectory() as d:
            papers = Path(d) / "papers"; dist = Path(d) / "dist"
            papers.mkdir()
            for k in ("Open2020", "Closed2021", "Unknown2022"):
                (papers / f"{k}_annotated.pdf").write_bytes(b"%PDF-1.4 test")
            (papers / "Closed2021.pdf").write_bytes(b"%PDF-1.4 source")       # not annotated: never copied
            lic = {"@Open2020": {"category": "cc", "label": "CC BY 4.0"}, "@Closed2021": {"category": "rights_reserved"}}
            out = P.copy_pdfs(papers, dist, lic)
            self.assertEqual(out["@Open2020"]["annotated"], "cc/Open2020_annotated.pdf")
            self.assertTrue(out["@Open2020"]["public"])
            self.assertEqual(out["@Closed2021"]["annotated"], "pdf/Closed2021_annotated.pdf")
            self.assertEqual(out["@Unknown2022"]["annotated"], "pdf/Unknown2022_annotated.pdf")   # unknown licence stays private
            self.assertFalse((dist / "pdf" / "Closed2021.pdf").exists())
            # licence changes → the file moves
            lic["@Open2020"] = {"category": "rights_reserved"}
            out = P.copy_pdfs(papers, dist, lic)
            self.assertEqual(out["@Open2020"]["annotated"], "pdf/Open2020_annotated.pdf")
            self.assertFalse((dist / "cc" / "Open2020_annotated.pdf").exists())
            # source removed → copy removed
            (papers / "Unknown2022_annotated.pdf").unlink()
            out = P.copy_pdfs(papers, dist, lic)
            self.assertNotIn("@Unknown2022", out)
            self.assertFalse((dist / "pdf" / "Unknown2022_annotated.pdf").exists())


class Import(unittest.TestCase):
    def setUp(self):
        import portal_import as PI
        self.PI = PI
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "drafts" / "regions").mkdir(parents=True)
        (self.tmp / "logs" / "portal" / "inbox").mkdir(parents=True)
        self.draft = self.tmp / "drafts" / "regions" / "left_angular_gyrus__TestPaper2020.md"
        self.draft.write_text(DRAFT, encoding="utf-8")
        self.saved = {k: getattr(PI, k) for k in ("ROOT", "INBOX", "APPLIED", "LOG", "REVIEWERS")}
        PI.ROOT = self.tmp
        PI.INBOX = self.tmp / "logs" / "portal" / "inbox"
        PI.APPLIED = self.tmp / "logs" / "portal" / "applied"
        PI.LOG = self.tmp / "logs" / "extraction_log.md"
        PI.REVIEWERS = self.tmp / "reviewers.yaml"
        PI.REVIEWERS.write_text(yaml.safe_dump({"reviewers": {"m@uq.edu.au": {"name": "michele", "approver": True},
                                                               "alex@example.org": {"name": "alex", "approver": False}}}), encoding="utf-8")

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(self.PI, k, v)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_who(self):
        t = self.PI.reviewers()
        self.assertEqual(self.PI.who("M@UQ.edu.au", t), ("michele", True, True))
        self.assertEqual(self.PI.who("alex@example.org", t), ("alex", False, True))
        self.assertEqual(self.PI.who("new.person@x.org", t), ("new_person", False, False))

    def test_edit_mark_comment_verdict(self):
        PI = self.PI
        rel = "drafts/regions/left_angular_gyrus__TestPaper2020.md"
        state: dict = {}
        msg = PI.apply_edit({"id": rel, "finding": "f1", "submitted": "2026-11-05T10:00:00Z",
                             "fields": {"strength": {"old": "moderate", "new": "strong"}, "direction": {"old": "unlikely", "new": "mixed"}},
                             "passages_added": [{"page": 3, "quote": "Poorer naming was associated with damage.", "supports": "statistics"}]},
                            "alex", True, state)
        self.assertIn("strength", msg)
        self.assertIn("stale: direction", msg)
        fm, _ = PI.parse_markdown(self.draft)
        f = fm["findings"][0]
        self.assertEqual(f["strength"], "strong")
        self.assertEqual(f["direction"], "likely")                       # stale edit not applied
        self.assertEqual(len(f["source_passages"]), 2)
        self.assertEqual(f["edits"][0], {"by": "human:alex", "date": "2026-11-05", "fields": ["source_passages", "strength"], "via": "portal"})
        msg = PI.apply_mark({"id": rel, "page": 3, "quote": "Our findings replicate earlier reports.", "note": "x", "submitted": "2026-11-05"}, "alex", True, state)
        self.assertIn("mark m1", msg)
        self.assertIn("already present", PI.apply_mark({"id": rel, "page": 3, "quote": "Our findings replicate earlier reports."}, "alex", True, state))
        PI.apply_comment({"id": rel, "finding": "f1", "text": "check the threshold", "submitted": "2026-11-05"}, "alex", True, state)
        fm, _ = PI.parse_markdown(self.draft)
        self.assertEqual(fm["reviewer_marks"][0]["status"], "pending")
        self.assertEqual(fm["findings"][0]["portal_comments"][0]["by"], "human:alex")
        # a non-approver's approve is an opinion; an approver's approve would promote, but pending marks block it
        msg = PI.apply_verdict({"id": rel, "verdict": "approve", "rationale": "fine", "submitted": "2026-11-05",
                                "per_finding": [{"id": "f1", "verdict": "agree", "supports_approval": True}]}, "alex", False, True, True, state)
        self.assertIn("opinion", msg)
        msg = PI.apply_verdict({"id": rel, "verdict": "approve", "rationale": "fine", "submitted": "2026-11-05",
                                "per_finding": [{"id": "f1", "verdict": "agree", "supports_approval": True}]}, "michele", True, True, True, state)
        self.assertIn("pending reviewer marks", msg)
        fm, _ = PI.parse_markdown(self.draft)
        self.assertEqual([r["by"] for r in fm["portal_reviews"]], ["human:alex", "human:michele"])
        self.assertEqual(fm["status"], "draft")
        self.assertIn("skip: no draft", PI.apply_edit({"id": "regions/left_angular_gyrus.md", "finding": "f1", "fields": {}}, "alex", True, state))
        self.assertIn("skip: no draft", PI.apply_edit({"id": "drafts/../README.md", "finding": "f1", "fields": {}}, "alex", True, state))

    def test_run_moves_applied_records(self):
        PI = self.PI
        rel = "drafts/regions/left_angular_gyrus__TestPaper2020.md"
        (PI.INBOX / "20261105T100000Z_comment_alex_x.json").write_text(json.dumps({"kind": "comment", "id": rel, "text": "hi", "reviewer": "alex@example.org", "submitted": "2026-11-05T10:00:00Z"}), encoding="utf-8")
        (PI.INBOX / "20261105T100001Z_edit_alex_y.json").write_text(json.dumps({"kind": "edit", "id": "drafts/regions/missing.md", "finding": "f1", "fields": {}, "reviewer": "alex@example.org"}), encoding="utf-8")
        PI.run(execute=True, promote=False, only_kind=None)
        self.assertEqual([p.name for p in PI.APPLIED.glob("*.json")], ["20261105T100000Z_comment_alex_x.json"])
        self.assertEqual(len(list(PI.INBOX.glob("*.json"))), 1)       # the one that could not be applied stays
        self.assertIn("PORTAL-APPLIED", PI.LOG.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
