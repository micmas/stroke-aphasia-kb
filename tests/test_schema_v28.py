#!/usr/bin/env python3
"""
test_schema_v28.py — schema v2.8: a therapy finding names its therapy, a
symptom is not a syndrome, and the migration (retarget_symptoms.py) and
the therapy backfill checker behave.

    python tests/test_schema_v28.py
"""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root
sys.path.insert(0, str(ROOT / "scripts"))

import aphasia_kb as K  # noqa: E402

FINDING = {
    "id": "f1", "target": "anomia", "target_kind": "impairment",
    "claim": "Increased activation in the left MFG following treatment is associated with improved naming.",
    "direction": "likely", "relationship": "treatment_response", "citation": "@X2020",
    "method": "fMRI_activation", "design": "longitudinal", "strength": "moderate", "evidence_quality": "cohort",
    "sample": {"n": 19, "population": "chronic stroke with aphasia", "time_post_onset": ">= 8 months", "phase": "chronic"},
    "statistics": {"threshold": "p < 0.05"}, "confounders_controlled": [], "confounders_not_controlled": [],
    "region_definition": {"kind": "atlas"}, "imaging_details": {"reference_space": "MNI152", "atlases_used": []},
    "author_limitations": [], "provenance": {"extracted_by": "agent:t", "extracted_on": "2026-10-27", "paper_section": "Results",
                                             "confidence": "high", "flags": []},
    "source_passages": [{"section": "Results", "page": 3, "quote": "Activation increased after treatment.", "supports": "claim"}],
}
ENTRY = {"schema_version": 2.8, "id": "left_mfg", "name": "Left MFG", "kind": "atlas", "status": "draft",
         "created_by": "agent:t", "created_on": "2026-10-27", "hemisphere": "left", "findings": [FINDING]}


def issues(entry):
    out = []
    e = copy.deepcopy(entry)
    e["_path"] = "x.md"
    K._validate_v2_entry(e, "x.md", out)
    return [i.split(": ", 1)[-1] for i in out]


class SchemaV28(unittest.TestCase):
    def test_therapy_required_for_treatment_findings(self):
        self.assertTrue(any("therapy" in i for i in issues(ENTRY)))
        ok = copy.deepcopy(ENTRY)
        ok["findings"][0]["therapy"] = {"id": "cueing_hierarchy_naming_treatment", "name": "cueing hierarchy anomia treatment"}
        self.assertEqual([i for i in issues(ok) if "therapy" in i], [])
        bad = copy.deepcopy(ok)
        bad["findings"][0]["therapy"] = {"id": "Cueing Hierarchy", "name": ""}
        self.assertEqual(len([i for i in issues(bad) if "therapy" in i]), 2)
        causal = copy.deepcopy(ENTRY)
        causal["findings"][0].update({"relationship": "causal", "method": "VLSM"})
        causal["findings"][0]["lesion_mapping"] = {"analysis": "univariate", "n_analysed": 19, "lesion_volume_correction": "covariate", "multiple_comparisons": "fdr"}
        self.assertEqual([i for i in issues(causal) if "therapy" in i], [])

    def test_older_schema_not_bound(self):
        old = copy.deepcopy(ENTRY)
        old["schema_version"] = 2.7
        self.assertEqual([i for i in issues(old) if "therapy" in i], [])

    def test_symptom_not_syndrome(self):
        e = copy.deepcopy(ENTRY)
        e["findings"][0]["therapy"] = {"name": "x therapy"}
        e["findings"][0]["target"] = "anomic_aphasia"
        self.assertTrue(any("syndrome" in i for i in issues(e)))
        e["findings"][0]["claim"] = "The SVM classified anomic aphasia against conduction aphasia with 89% accuracy."
        self.assertEqual([i for i in issues(e) if "syndrome" in i], [])
        self.assertTrue(K._syndrome_claim({"claim": "Patients with Broca's aphasia showed …"}))
        self.assertFalse(K._syndrome_claim({"claim": "Naming accuracy improved after therapy."}))

    def test_findings_table_carries_therapy(self):
        import pandas as pd  # noqa: F401
        e = copy.deepcopy(ENTRY)
        e["findings"][0]["therapy"] = {"id": "sfa", "name": "semantic feature analysis"}
        kb = K.KnowledgeBase(ROOT, include=("approved",))
        row = kb.findings.iloc[0]
        self.assertIn("therapy_name", row.index)

    def test_retarget_plan_and_backfill_check(self):
        import retarget_symptoms as RS
        import backfill as B
        f_sym = {"id": "f1", "target": "anomic_aphasia", "target_kind": "impairment", "claim": "Damage predicts poorer naming."}
        f_syn = {"id": "f2", "target": "anomic_aphasia", "target_kind": "impairment", "claim": "Lesion load predicted anomic aphasia versus Broca's aphasia classification."}
        self.assertFalse(K._syndrome_claim(f_sym))
        self.assertTrue(K._syndrome_claim(f_syn))
        self.assertIn("naming", RS.NAMING_IDS)
        self.assertEqual(RS.SYMPTOM_FOR["anomic_aphasia"], "anomia")

        class P:
            norm = "participants received a cueing hierarchy treatment for anomia over two weeks"
            nospace = norm.replace(" ", "")
        val, quotes, why = B.check("therapy", {"value": {"name": "cueing hierarchy treatment", "id": ""},
                                               "quote": "participants received a cueing hierarchy treatment for anomia"}, P())
        self.assertEqual(val["id"], "cueing_hierarchy_treatment")
        self.assertEqual(len(quotes), 1)
        val, _, why = B.check("therapy", {"value": {"name": "melodic intonation therapy"},
                                          "quote": "participants received a cueing hierarchy treatment for anomia"}, P())
        self.assertIsNone(val)
        self.assertIn("does not name", why)
        val, _, why = B.check("therapy", {"value": {"name": "x"}, "quote": "nowhere"}, P())
        self.assertIsNone(val)


if __name__ == "__main__":
    unittest.main(verbosity=1)
