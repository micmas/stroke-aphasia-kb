#!/usr/bin/env python3
"""
test_rereview.py — rereview.py sends a legacy canonical entry back to drafts/, one draft per
paper, keeping every finding and the old approval as history; a fresh draft for the same
paper blocks the move without dropping legacy findings; nothing moves without --execute and a name.

    python tests/test_rereview.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

ENTRY = {
    "schema_version": 2.8, "id": "naming_therapy_x", "name": "Naming therapy X", "kind": "therapy",
    "status": "approved", "review_tier": "legacy", "reviewer": "auto-reviewer", "reviewed_on": "2026-05-05",
    "created_by": "agent:claude-sonnet-4-6", "created_on": "2026-05-01", "targets_impairments": ["anomia"],
    "findings": [
        {"id": "f1", "citation": "@Smith2020", "target": "anomia", "target_kind": "impairment", "claim": "A.", "direction": "likely",
         "relationship": "treatment_response", "strength": "moderate", "therapy": {"id": "naming_therapy_x", "name": "Naming therapy X"},
         "review": {"reviewer": "auto-reviewer", "reviewed_on": "2026-05-05"}},
        {"id": "f2", "citation": "@Smith2020", "target": "anomia", "target_kind": "impairment", "claim": "B.", "direction": "likely",
         "relationship": "treatment_response", "strength": "weak", "therapy": {"id": "naming_therapy_x", "name": "Naming therapy X"}},
        {"id": "f3", "citation": "@Jones2019", "target": "anomia", "target_kind": "impairment", "claim": "C.", "direction": "mixed",
         "relationship": "treatment_response", "strength": "weak", "therapy": {"id": "naming_therapy_x", "name": "Naming therapy X"}},
        {"id": "f4", "target": "anomia", "target_kind": "impairment", "claim": "D, uncited.", "direction": "likely",
         "relationship": "treatment_response", "strength": "weak", "therapy": {"id": "naming_therapy_x", "name": "Naming therapy X"}},
    ],
}


def write_entry(path: Path, fm: dict, body="Body text.\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n" + body, encoding="utf-8")


class Rereview(unittest.TestCase):
    def setUp(self):
        import rereview as RR
        self.RR = RR
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (RR.ROOT, RR.LOG)
        RR.ROOT = self.tmp
        RR.LOG = self.tmp / "logs" / "extraction_log.md"
        write_entry(self.tmp / "therapies" / "naming_therapy_x.md", ENTRY)
        write_entry(self.tmp / "therapies" / "fresh_one.md", {**ENTRY, "id": "fresh_one", "reviewer": "human:alex", "review_tier": "B"})
        (self.tmp / "drafts" / "therapies").mkdir(parents=True)
        write_entry(self.tmp / "drafts" / "therapies" / "naming_therapy_x__Jones2019.md", {**ENTRY, "status": "draft", "review_tier": None})

    def tearDown(self):
        self.RR.ROOT, self.RR.LOG = self.saved
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_dry_run_moves_nothing(self):
        self.RR.run(("therapies",), [], False, None, root=self.tmp)
        self.assertTrue((self.tmp / "therapies" / "naming_therapy_x.md").exists())
        self.assertEqual(self.RR.run(("therapies",), [], True, None, root=self.tmp), 2)   # --execute without --by is refused
        self.assertTrue((self.tmp / "therapies" / "naming_therapy_x.md").exists())

    def test_existing_draft_blocks_without_losing_findings(self):
        original = self.tmp / 'therapies/naming_therapy_x.md'
        before = original.read_bytes()
        self.assertEqual(self.RR.run(('therapies',), [], True, 'michele', root=self.tmp), 2)
        self.assertEqual(original.read_bytes(), before)
        self.assertEqual(len(list((self.tmp / 'drafts/therapies').glob('*.md'))), 1)

    def test_execute_splits_by_paper_and_keeps_history(self):
        (self.tmp / 'drafts/therapies/naming_therapy_x__Jones2019.md').unlink()
        self.RR.run(("therapies",), [], True, "michele", root=self.tmp)
        self.assertFalse((self.tmp / "therapies" / "naming_therapy_x.md").exists())
        self.assertTrue((self.tmp / "therapies" / "fresh_one.md").exists())              # a human-reviewed entry is untouched
        d = self.tmp / "drafts" / "therapies"
        names = sorted(p.name for p in d.glob("*.md"))
        self.assertEqual(names, ["naming_therapy_x__Jones2019.md", "naming_therapy_x__Smith2020.md", "naming_therapy_x__nocitation.md"])
        from aphasia_kb import parse_markdown
        fm, body = parse_markdown(d / "naming_therapy_x__Smith2020.md")
        self.assertEqual(fm["status"], "in_review")
        self.assertNotIn("reviewer", fm); self.assertNotIn("review_tier", fm)
        self.assertEqual(fm["previous_review"]["reviewer"], "auto-reviewer")
        self.assertEqual(fm["rereview_of"], "therapies/naming_therapy_x.md")
        self.assertEqual([f["id"] for f in fm["findings"]], ["f1", "f2"])
        self.assertNotIn("review", fm["findings"][0]); self.assertEqual(fm["findings"][0]["previous_review"]["reviewer"], "auto-reviewer")
        self.assertEqual(body, "Body text.\n")
        fm2, _ = parse_markdown(d / "naming_therapy_x__nocitation.md")
        self.assertIn("no citation", fm2["notes"]); self.assertEqual([f["id"] for f in fm2["findings"]], ["f4"])
        fm3, _ = parse_markdown(d / "naming_therapy_x__Jones2019.md")
        self.assertEqual(fm3["status"], "in_review")                                        # the fresh draft was not overwritten
        log = (self.tmp / "logs" / "extraction_log.md").read_text(encoding="utf-8")
        self.assertIn("REREVIEW | @Smith2020, @Jones2019, (no citation) | naming_therapy_x | by: human:michele | 3 draft(s) | previous: auto-reviewer", log)


if __name__ == "__main__":
    unittest.main(verbosity=1)
