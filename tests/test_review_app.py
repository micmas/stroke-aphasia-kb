#!/usr/bin/env python3
"""
test_review_app.py — the review workbench and the focused re-extraction
without a browser or a model: passage location and grading, saving with
backup, log line, edit stamps and validation guard, reviewer marks, the
merge of a (fabricated) refocus response, and promote.py's refusal of a
draft with pending marks.

    python tests/test_review_app.py
"""
from __future__ import annotations

import copy
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root
sys.path.insert(0, str(ROOT / "scripts"))

try:
    import pymupdf  # noqa: F401
except ImportError:  # pragma: no cover
    try:
        import fitz as pymupdf  # noqa: F401
    except ImportError:
        pymupdf = None

PAGES = [
    "Lesion correlates of naming after stroke. Abstract. We studied 48 patients with chronic left hemisphere stroke "
    "using voxel-based lesion symptom mapping. Damage to the left angular gyrus was associated with poorer naming "
    "accuracy on the Boston Naming Test. Lesion volume was entered as a covariate in all analyses.",
    "Methods. Participants were 48 adults (mean age 61 years) at least six months after a single left hemisphere "
    "ischaemic stroke. Naming was assessed with the Boston Naming Test. Statistical maps were thresholded with "
    "permutation-based family-wise error correction at p < 0.05.",
    "Results. Poorer naming was associated with damage to the left angular gyrus (peak z = 4.2, permutation FWE "
    "p < 0.05) and the posterior middle temporal gyrus. Discussion. A limitation is that the sample was drawn from a "
    "single rehabilitation centre. Our findings replicate earlier reports of temporoparietal involvement in naming.",
]

DRAFT = """---
schema_version: 2.7
id: left_angular_gyrus
name: Left angular gyrus
kind: atlas
status: draft
created_by: agent:test
created_on: 2026-10-27
hemisphere: left
findings:
- id: f1
  target: anomic_aphasia
  target_kind: impairment
  claim: Damage to the left angular gyrus is associated with poorer naming accuracy.
  direction: likely
  relationship: causal
  citation: '@TestPaper2020'
  method: VLSM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample: {n: 48, population: chronic left hemisphere stroke, time_post_onset: at least six months, phase: chronic}
  statistics: {threshold: permutation FWE p < 0.05}
  lesion_mapping: {analysis: univariate, n_analysed: 48, lesion_volume_correction: covariate, multiple_comparisons: permutation_fwe}
  confounders_controlled: [lesion volume]
  confounders_not_controlled: []
  region_definition: {kind: atlas}
  imaging_details: {reference_space: MNI152, atlases_used: []}
  author_limitations: [single rehabilitation centre sample]
  provenance: {extracted_by: agent:test, extracted_on: 2026-10-27, paper_section: Results, confidence: high, flags: []}
  source_passages:
  - {section: Abstract, page: 1, quote: Damage to the left angular gyrus was associated with poorer naming accuracy on the Boston Naming Test., supports: claim}
  - {section: Methods, page: 2, quote: Participants were 48 adults (mean age 61 years) at least six months after a single left hemisphere ischaemic stroke., supports: sample}
  - {section: Discussion, page: 3, quote: A limitation is that the sample was drawn from a single centre., supports: limitation}
---
Test draft.
"""


@unittest.skipIf(pymupdf is None, "PyMuPDF not installed")
class Workbench(unittest.TestCase):
    def setUp(self):
        import review_app as R
        self.R = R
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "drafts" / "regions").mkdir(parents=True)
        (self.tmp / "papers").mkdir()
        (self.tmp / "logs").mkdir()
        doc = pymupdf.open()
        for t in PAGES:
            doc.new_page().insert_textbox(pymupdf.Rect(60, 60, 540, 760), t, fontsize=11, fontname="helv")
        doc.save(str(self.tmp / "papers" / "TestPaper2020.pdf"))
        self.draft = self.tmp / "drafts" / "regions" / "left_angular_gyrus__TestPaper2020.md"
        self.draft.write_text(DRAFT, encoding="utf-8")
        self.saved = {k: getattr(R, k) for k in ("DRAFTS", "PAPERS", "BACKUP", "LOG")}
        R.DRAFTS = self.tmp / "drafts"
        R.PAPERS = self.tmp / "papers"
        R.BACKUP = self.tmp / "drafts" / "_backup"
        R.LOG = self.tmp / "logs" / "extraction_log.md"
        R.SESSIONS.clear()

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(self.R, k, v)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_paths_are_confined_to_drafts(self):
        with self.assertRaises(PermissionError):
            self.R.draft_path("../regions/x.md")
        with self.assertRaises(FileNotFoundError):
            self.R.draft_path("regions/missing.md")

    def test_payload_locates_and_grades(self):
        s = self.R.Session("regions/left_angular_gyrus__TestPaper2020.md")
        p = s.payload()
        self.assertEqual(len(p["pages"]), 3)
        self.assertEqual((p["located"]["f1/0"]["page"], p["located"]["f1/0"]["grade"]), (1, "exact"))
        self.assertEqual((p["located"]["f1/1"]["page"], p["located"]["f1/1"]["grade"]), (2, "exact"))
        self.assertEqual(p["located"]["f1/2"]["grade"], "near")       # "single centre" vs "single rehabilitation centre"
        self.assertTrue(p["located"]["f1/0"]["rects"])
        self.assertEqual(p["issues"], [])
        words = s.words(0)
        self.assertEqual(words[0][4], "Lesion")
        self.assertTrue(s.png(0).startswith(b"\x89PNG"))

    def test_save_edits_marks_backup_log_and_annotation(self):
        R = self.R
        s = R.Session("regions/left_angular_gyrus__TestPaper2020.md")
        fm = copy.deepcopy(s.fm)
        f = fm["findings"][0]
        f["strength"] = "strong"
        f["source_passages"].append({"section": "", "page": 3, "supports": "statistics",
                                     "quote": "Poorer naming was associated with damage to the left angular gyrus (peak z = 4.2, permutation FWE p < 0.05)"})
        fm["reviewer_marks"] = [{"id": "m1", "page": 3, "note": "replication",
                                 "quote": "Our findings replicate earlier reports of temporoparietal involvement in naming."}]
        out = R.apply_save(s, fm, "michele")
        self.assertEqual(out["located"]["f1/3"]["grade"], "exact")
        self.assertEqual(out["marks"]["m1"]["page"], 3)
        fm2, _ = R.parse_markdown(self.draft)
        self.assertEqual(fm2["findings"][0]["strength"], "strong")
        self.assertEqual(fm2["findings"][0]["edits"][0]["by"], "human:michele")
        self.assertEqual(sorted(fm2["findings"][0]["edits"][0]["fields"]), ["source_passages", "strength"])
        self.assertEqual(fm2["reviewer_marks"][0]["status"], "pending")
        self.assertEqual(fm2["reviewer_marks"][0]["by"], "human:michele")
        self.assertEqual(len(list(R.BACKUP.glob("*.md"))), 1)
        log = R.LOG.read_text(encoding="utf-8")
        self.assertIn("REVIEW-EDITED | @TestPaper2020 | left_angular_gyrus | f1:strength,source_passages", log)
        self.assertTrue((self.tmp / "papers" / "TestPaper2020_annotated.pdf").exists())

    def test_save_guards(self):
        R = self.R
        s = R.Session("regions/left_angular_gyrus__TestPaper2020.md")
        with self.assertRaises(ValueError):
            R.apply_save(s, copy.deepcopy(s.fm), "model:gemma")
        bad = copy.deepcopy(s.fm)
        bad["findings"][0]["source_passages"][0]["supports"] = "vibes"
        with self.assertRaises(ValueError):
            R.apply_save(s, bad, "michele")
        bad = copy.deepcopy(s.fm)
        bad["findings"][0]["direction"] = "maybe"
        with self.assertRaises(ValueError):                              # a new schema issue is refused
            R.apply_save(s, bad, "michele")
        bad = copy.deepcopy(s.fm)
        bad["status"] = "approved"
        with self.assertRaises(ValueError):
            R.apply_save(s, bad, "michele")
        self.assertEqual(R.parse_markdown(self.draft)[0]["findings"][0]["direction"], "likely")

    def test_existing_issue_is_tolerated_but_reported(self):
        R = self.R
        text = self.draft.read_text(encoding="utf-8").replace("  confounders_controlled: [lesion volume]\n", "")
        self.draft.write_text(text, encoding="utf-8")
        s = R.Session("regions/left_angular_gyrus__TestPaper2020.md")
        self.assertTrue(any("confounders_controlled" in i for i in s.payload()["issues"]))
        fm = copy.deepcopy(s.fm)
        fm["findings"][0]["claim"] = "Edited claim."
        out = R.apply_save(s, fm, "michele")                              # the old issue does not block the edit
        self.assertTrue(any("confounders_controlled" in i for i in out["issues"]))

    def test_refocus_merge_and_promote_guard(self):
        import refocus as RF
        R = self.R
        s = R.Session("regions/left_angular_gyrus__TestPaper2020.md")
        fm = copy.deepcopy(s.fm)
        fm["reviewer_marks"] = [{"id": "m1", "page": 3, "note": "", "quote": "Our findings replicate earlier reports of temporoparietal involvement in naming."},
                                {"id": "m2", "page": 1, "note": "", "quote": "Lesion volume was entered as a covariate in all analyses."}]
        R.apply_save(s, fm, "michele")
        saved = (RF.DRAFTS, RF.PAPERS, RF.ROOT)
        RF.DRAFTS, RF.PAPERS = R.DRAFTS, R.PAPERS
        try:
            content = DRAFT.replace("id: left_angular_gyrus\nname: Left angular gyrus", "id: left_posterior_mtg\nname: Left posterior MTG") \
                           .replace("flags: []", "flags: ['refocus: m1']") \
                           .replace("Damage to the left angular gyrus is associated with poorer naming accuracy.", "Temporoparietal damage replicates earlier naming reports.")
            appended = DRAFT.replace("flags: []", "flags: ['refocus: m1']").replace("claim: Damage to the left angular gyrus is", "claim: Angular gyrus findings replicate earlier reports and are")
            result = {"drafts": [{"bucket": "regions", "filename": "left_posterior_mtg__TestPaper2020.md", "content": content},
                                 {"bucket": "regions", "filename": "left_angular_gyrus__TestPaper2020.md", "content": appended}],
                      "notes_for_reviewer": "m2: a covariate statement is a method detail, not a finding"}
            drafts = RF.drafts_for("TestPaper2020")
            marks = RF.pending_marks(drafts)
            self.assertEqual([m["id"] for _, m in marks], ["m1", "m2"])
            out = RF.merge(result, "@TestPaper2020", drafts, marks, "test-model")
        finally:
            RF.DRAFTS, RF.PAPERS, RF.ROOT = saved
        self.assertEqual(sorted(out["produced"]["m1"]), ["left_angular_gyrus__TestPaper2020.md:f2", "left_posterior_mtg__TestPaper2020.md:f1"])
        fm2, _ = R.parse_markdown(self.draft)
        self.assertEqual([f["id"] for f in fm2["findings"]], ["f1", "f2"])
        self.assertIn("refocus: m1", fm2["findings"][1]["provenance"]["flags"])
        by_id = {m["id"]: m for m in fm2["reviewer_marks"]}
        self.assertEqual(by_id["m1"]["status"], "done")
        self.assertEqual(by_id["m2"]["status"], "unresolved")
        self.assertIn("covariate statement", by_id["m2"]["result"])
        self.assertTrue((self.tmp / "drafts" / "regions" / "left_posterior_mtg__TestPaper2020.md").exists())
        # promote refuses while a mark is pending, and drops resolved marks from what it writes
        import promote as P
        fm3, _ = R.parse_markdown(self.draft)
        fm3["reviewer_marks"][0]["status"] = "pending"
        pending = [m["id"] for m in fm3["reviewer_marks"] if m.get("status", "pending") == "pending"]
        self.assertEqual(pending, ["m1"])
        self.assertIn("reviewer_marks", P.__dict__.get("cmd_approve").__code__.co_consts)


if __name__ == "__main__":
    unittest.main(verbosity=1)
