#!/usr/bin/env python3
"""
test_recheck.py — recheck_drafts.py sorts papers into pass / rewrite / for a person / no PDF,
never rewrites a paper a person has touched, keeps a rewrite only when it is better and puts
the old drafts back otherwise. The quote check and the extractor are stood in for.

    python tests/test_recheck.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def draft(path: Path, key: str, quote: str, **extra):
    fm = {"schema_version": 2.8, "id": path.stem.split("__")[0], "name": "X", "kind": "atlas", "status": "draft",
          "created_by": "agent:ollama-extract-cli/test", "created_on": "2026-11-10",
          "findings": [{"id": "f1", "target": "anomia", "target_kind": "impairment", "claim": "c", "direction": "likely", "relationship": "causal",
                        "citation": f"@{key}", "strength": "weak", "source_passages": [{"page": 1, "quote": quote, "supports": "claim"}]}], **extra}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False) + "---\nbody\n", encoding="utf-8")


class Recheck(unittest.TestCase):
    def setUp(self):
        import recheck_drafts as R
        self.R = R
        self.tmp = Path(tempfile.mkdtemp()); self.drafts = self.tmp / "drafts"; self.papers = self.tmp / "papers"; self.papers.mkdir()
        for k in ("Good2020", "Bad2021", "Touched2022", "Worse2023"):
            (self.papers / f"{k}.pdf").write_bytes(b"%PDF-1.4")
        d = self.drafts / "regions"
        draft(d / "left_angular_gyrus__Good2020.md", "Good2020", "REAL one")
        draft(d / "left_angular_gyrus__Bad2021.md", "Bad2021", "FAKE quote")
        draft(d / "left_insula__Bad2021.md", "Bad2021", "REAL two")
        draft(d / "left_angular_gyrus__Touched2022.md", "Touched2022", "FAKE quote", portal_reviews=[{"by": "alex", "verdict": "agree_defer"}])
        draft(d / "left_angular_gyrus__Worse2023.md", "Worse2023", "FAKE quote")
        draft(d / "left_angular_gyrus__NoPdf2024.md", "NoPdf2024", "FAKE quote")
        self.saved = (R.CE._quote_check, R.CE._schema_issues)
        # stand-ins: a quote starting with FAKE is absent; no schema issues
        def quote_check(findings, papers_dir):
            quotes = [sp["quote"] for f in findings for sp in f.get("source_passages") or []]
            absent = [q for q in quotes if q.startswith("FAKE")]
            return {"total": len(quotes), "absent": len(absent), "absent_list": absent}
        R.CE._quote_check = quote_check
        R.CE._schema_issues = lambda paths: {}

    def tearDown(self):
        self.R.CE._quote_check, self.R.CE._schema_issues = self.saved

    def rows(self):
        return [self.R.audit(k, v, self.papers) for k, v in sorted(self.R.drafts_by_paper(self.drafts).items())]

    def test_plan(self):
        g = self.R.plan(self.rows())
        self.assertEqual([r["key"] for r in g["fine"]], ["Good2020"])
        self.assertEqual([r["key"] for r in g["rewrite"]], ["Bad2021", "Worse2023"])
        self.assertEqual([r["key"] for r in g["person"]], ["Touched2022"]); self.assertEqual(g["person"][0]["touched"], ["portal review"])
        self.assertEqual([r["key"] for r in g["no_pdf"]], ["NoPdf2024"])

    def test_rewrite_kept_only_when_better(self):
        R = self.R; g = R.plan(self.rows()); bad, worse = g["rewrite"]
        d = self.drafts / "regions"; backup = self.drafts / "_backup"
        def good_extract(key, pdf, model, timeout):
            draft(d / f"left_planum_temporale__{key}.md", key, "REAL new")
            return True, ""
        o = R.rewrite(bad, "stamp", None, 10, extract=good_extract, drafts=self.drafts, papers=self.papers, backup=backup)
        self.assertTrue(o["kept"]); self.assertEqual(o["new"]["absent"], 0)
        self.assertEqual(sorted(p.name for p in d.glob("*Bad2021.md")), ["left_planum_temporale__Bad2021.md"])     # the old drafts are gone…
        self.assertEqual(sorted(p.name for p in (backup / "stamp" / "regions").glob("*.md")), ["left_angular_gyrus__Bad2021.md", "left_insula__Bad2021.md"])  # …and kept in the backup
        def bad_extract(key, pdf, model, timeout):
            draft(d / f"left_planum_temporale__{key}.md", key, "FAKE again")
            return True, ""
        before = (d / "left_angular_gyrus__Worse2023.md").read_text()
        o = R.rewrite(worse, "stamp", None, 10, extract=bad_extract, drafts=self.drafts, papers=self.papers, backup=backup)
        self.assertFalse(o["kept"]); self.assertIn("not better", o["why"])
        self.assertEqual(sorted(p.name for p in d.glob("*Worse2023.md")), ["left_angular_gyrus__Worse2023.md"])     # put back, the failed attempt removed
        self.assertEqual((d / "left_angular_gyrus__Worse2023.md").read_text(), before)
        o = R.rewrite(R.audit("Worse2023", list(d.glob("*Worse2023.md")), self.papers), "stamp2", None, 10, extract=lambda *a: (False, "boom"),
                      drafts=self.drafts, papers=self.papers, backup=backup)
        self.assertFalse(o["kept"]); self.assertTrue((d / "left_angular_gyrus__Worse2023.md").exists())
        text = R.report(R.plan(self.rows()), [o], "test-model", True)
        self.assertIn("For a person", text); self.assertIn("Touched2022", text); self.assertIn("Rewrite not kept", text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
