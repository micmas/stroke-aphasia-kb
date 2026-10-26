#!/usr/bin/env python3
"""
test_screening.py — the screening register without network or model:
record parsers (PubMed XML, OpenAlex JSON, RIS, CSV), de-duplication,
derived stages, decision guardrails and the PRISMA arithmetic.

    python -m pytest tests/test_screening.py -q      # or: python tests/test_screening.py
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root
sys.path.insert(0, str(ROOT / "scripts"))
import screen  # noqa: E402
import screening as S  # noqa: E402

PUBMED_XML = b"""<?xml version="1.0"?><PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>12345678</PMID>
<Article><Journal><Title>Brain</Title><JournalIssue><PubDate><Year>2004</Year></PubDate></JournalIssue></Journal>
<ArticleTitle>Lesion analysis of the brain areas involved in <i>language</i> comprehension.</ArticleTitle>
<Abstract><AbstractText Label="BACKGROUND">We studied 64 patients.</AbstractText><AbstractText>Posterior MTG mattered.</AbstractText></Abstract>
<AuthorList><Author><LastName>Dronkers</LastName><Initials>NF</Initials></Author><Author><CollectiveName>PLORAS team</CollectiveName></Author></AuthorList>
<ELocationID EIdType="doi">10.1016/j.cognition.2003.11.002</ELocationID></Article></MedlineCitation>
<PubmedData><ArticleIdList><ArticleId IdType="doi">10.1016/J.COGNITION.2003.11.002</ArticleId></ArticleIdList></PubmedData></PubmedArticle></PubmedArticleSet>"""

OPENALEX = {"id": "https://openalex.org/W123", "doi": "https://doi.org/10.1000/X.1", "title": "A title.", "publication_year": 2020,
            "authorships": [{"author": {"display_name": "Ann Author"}}], "primary_location": {"source": {"display_name": "Stroke"}},
            "abstract_inverted_index": {"We": [0], "mapped": [1], "naming.": [2]}, "ids": {"pmid": "https://pubmed.ncbi.nlm.nih.gov/999"}, "type": "article"}


class Parsers(unittest.TestCase):
    def test_pubmed(self):
        (r,) = screen.parse_pubmed_xml(PUBMED_XML)
        self.assertEqual(r["pmid"], "12345678")
        self.assertEqual(r["doi"], "10.1016/j.cognition.2003.11.002")
        self.assertEqual(r["title"], "Lesion analysis of the brain areas involved in language comprehension")
        self.assertEqual(r["year"], 2004)
        self.assertEqual(r["authors"], ["Dronkers NF", "PLORAS team"])
        self.assertIn("BACKGROUND: We studied 64 patients.", r["abstract"])

    def test_openalex(self):
        r = screen.openalex_record(OPENALEX)
        self.assertEqual((r["openalex"], r["pmid"], r["doi"], r["year"]), ("W123", "999", "10.1000/x.1", 2020))
        self.assertEqual(r["abstract"], "We mapped naming.")
        self.assertEqual(r["journal"], "Stroke")

    def test_ris_and_csv(self):
        ris = "TY  - JOUR\nTI  - One\nAU  - A, B\nPY  - 2019\nDO  - https://doi.org/10.1/A.B\nAB  - abs\nJO  - J\nER  - \n\nTY  - JOUR\nT1  - Two\nY1  - 2020///\nN2  - n2\nER  - \n"
        rows = screen.parse_ris(ris)
        self.assertEqual([r["title"] for r in rows], ["One", "Two"])
        self.assertEqual(rows[0]["doi"], "10.1/a.b")
        self.assertEqual(rows[1]["year"], 2020)
        csv_text = 'Authors,Title,Year,Source title,DOI,PubMed ID,Abstract\n"Lee K; Park S","T",2019,"S",10.1/C,31,"a"\n'
        (r,) = screen.parse_csv(csv_text)
        self.assertEqual((r["doi"], r["pmid"], r["authors"]), ("10.1/c", "31", ["Lee K", "Park S"]))


class Register(unittest.TestCase):
    def test_dedupe_and_sources(self):
        cands = [{"id": "C0001", "doi": "10.1/a", "title": "Alpha beta gamma delta epsilon zeta", "year": 2001, "sources": [{"kind": "hand_picked"}], "screening": []}]
        new, known = screen.add_records([
            {"doi": "10.1/A", "title": "x", "year": 2001, "authors": ["Q R"]},                                 # same DOI
            {"doi": None, "pmid": None, "title": "Alpha, beta; gamma delta epsilon zeta", "year": 2001},       # same title+year
            {"doi": "10.1/b", "title": "Something new entirely here", "year": 2002, "authors": ["New N"], "abstract": "ab"},
        ], "S001", cands, abstracts := {})
        self.assertEqual((new, known), (1, 2))
        self.assertEqual([s.get("search") for s in cands[0]["sources"] if s.get("search")], ["S001"])
        self.assertEqual(cands[1]["id"], "C0002")
        self.assertEqual(abstracts, {"C0002": "ab"})
        self.assertEqual(S.arm_of(cands[0]), "databases")

    def test_stages(self):
        c = {"id": "C1", "sources": [{"search": "S1"}], "screening": []}
        self.assertEqual(S.stage_of(c), ("awaiting_ta", None))
        c["screening"].append({"stage": "title_abstract", "decision": "exclude", "reason": "not_stroke"})
        self.assertEqual(S.stage_of(c), ("excluded_ta", "not_stroke"))
        c["screening"].append({"stage": "title_abstract", "decision": "include"})     # a later decision supersedes
        self.assertEqual(S.stage_of(c), ("awaiting_ft", None))
        c["screening"].append({"stage": "full_text", "decision": "exclude", "reason": "not_retrieved"})
        self.assertEqual(S.stage_of(c), ("not_retrieved", "not_retrieved"))
        c["screening"].append({"stage": "full_text", "decision": "include"})
        self.assertEqual(S.stage_of(c), ("included", None))
        other = {"id": "C2", "sources": [{"kind": "seed"}], "skip_title_abstract": True, "screening": []}
        self.assertEqual(S.stage_of(other), ("awaiting_ft", None))
        self.assertEqual(S.stage_of({"id": "C3", "duplicate_of": "C1"}), ("duplicate", None))

    def test_decision_guardrails(self):
        c = {"id": "C1", "screening": []}
        self.assertIsNotNone(screen._apply_decision(c, "title_abstract", "exclude", None, "michele", None, "2026-01-01"))
        self.assertIsNotNone(screen._apply_decision(c, "title_abstract", "exclude", "not_retrieved", "michele", None, "2026-01-01"))
        self.assertIsNotNone(screen._apply_decision(c, "title_abstract", "exclude", "other", "michele", None, "2026-01-01"))
        self.assertIsNotNone(screen._apply_decision(c, "title_abstract", "include", None, "model", None, "2026-01-01"))
        self.assertIsNotNone(screen._apply_decision(c, "title_abstract", "include", None, "legacy", None, "2026-01-01"))
        self.assertEqual(c["screening"], [])
        self.assertIsNone(screen._apply_decision(c, "title_abstract", "include", "not_stroke", "michele", None, "2026-01-01"))
        self.assertNotIn("reason", c["screening"][0])                     # a reason only goes with an exclusion
        self.assertIsNone(screen._apply_decision(c, "full_text", "exclude", "not_retrieved", "michele", None, "2026-01-02"))

    def test_kb_state(self):
        self.assertEqual(S.kb_state(None), "not_registered")
        base = {"registered": True, "pdf": False, "drafts": 0, "draft_open": 0, "draft_rejected": 0, "approved_findings": 0, "refused": False}
        self.assertEqual(S.kb_state(base), "no_pdf")
        self.assertEqual(S.kb_state({**base, "pdf": True}), "awaiting_extraction")
        self.assertEqual(S.kb_state({**base, "drafts": 2, "draft_open": 2}), "in_review")
        self.assertEqual(S.kb_state({**base, "drafts": 2, "draft_rejected": 2}), "rejected")
        self.assertEqual(S.kb_state({**base, "drafts": 2, "draft_rejected": 1, "draft_open": 1, "approved_findings": 3}), "in_kb")
        self.assertEqual(S.kb_state({**base, "refused": True}), "refused")

    def test_prisma_arithmetic(self):
        searches = [{"id": "S1", "database": "pubmed", "retrieved": 10, "for": ["gap_a"]}]
        mk = lambda i, src, hist, **kw: {"id": f"C{i}", "sources": src, "screening": hist, **kw}  # noqa: E731
        cands = [
            mk(1, [{"search": "S1"}], [{"stage": "title_abstract", "decision": "exclude", "reason": "not_stroke"}]),
            mk(2, [{"search": "S1"}], [{"stage": "title_abstract", "decision": "include"}, {"stage": "full_text", "decision": "exclude", "reason": "not_retrieved"}]),
            mk(3, [{"search": "S1"}], [{"stage": "title_abstract", "decision": "include"}, {"stage": "full_text", "decision": "include"}], key="@K3"),
            mk(4, [{"search": "S1"}], []),
            mk(5, [{"search": "S1"}], [], duplicate_of="C3"),
            mk(6, [{"kind": "hand_picked"}], [{"stage": "full_text", "decision": "include", "by": "legacy"}], key="@K6", skip_title_abstract=True),
            mk(7, [{"kind": "seed"}], [], skip_title_abstract=True),
        ]
        facts = {"@K3": {"registered": True, "pdf": True, "drafts": 1, "draft_open": 1, "draft_rejected": 0, "approved_findings": 0, "refused": False, "entries": [], "tag": "seed"},
                 "@K6": {"registered": True, "pdf": True, "drafts": 0, "draft_open": 0, "draft_rejected": 0, "approved_findings": 4, "refused": False, "entries": ["regions/x"], "tag": "extracted"}}
        rows = S.enrich(cands, facts)
        p = S.prisma_counts(rows, searches)
        self.assertEqual(p["identification"]["databases"]["records"], 10)
        self.assertEqual(p["identification"]["duplicatesRemoved"], 1)
        sc = p["screening"]
        self.assertEqual((sc["screened"], sc["excludedTitleAbstract"], sc["awaitingTitleAbstract"]), (4, 1, 1))
        self.assertEqual((sc["sought"], sc["notRetrieved"], sc["assessed"], sc["included"]), (2, 1, 1, 1))
        self.assertEqual(sc["excludedTitleAbstractReasons"], {"not_stroke": 1})
        ot = p["other"]
        self.assertEqual((ot["sought"], ot["assessed"], ot["awaitingFullText"], ot["included"]), (2, 1, 1, 1))
        inc = p["included"]
        self.assertEqual(inc["total"], 2)
        self.assertEqual((inc["kb"]["in_review"], inc["kb"]["in_kb"], inc["approvedFindings"]), (1, 1, 4))
        cov = S.coverage(rows, searches, {"gap_a": {"kind": "thin", "areas": ["a"], "papers": ["@K6"]}})
        g = {x["id"]: x for x in cov}["gap_a"]
        self.assertEqual((g["found"], g["screened"], g["included"], g["in_kb"], g["approved_findings"]), (5, 4, 2, 1, 4))


class Backfill(unittest.TestCase):
    def test_backfill_from_a_small_repo(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "citations.md").write_text(
                "# Citations\n\n## Extracted papers\n\n## @Baldo2006  [extracted]\nBaldo JV, Dronkers NF.\nRole of frontal cortex in fluency.\n*JINS*. 2006;12:896.\ndoi:10.1017/S1355617706061078\n\n> note\n\n"
                "## Refused papers\n\n## @Brady2022RELEASE  [refused]\nBrady MC, et al.\nRELEASE.\n*IJS*. 2022.\n\n> Not extractable as it stands.\n\n"
                "## Seed references (added 2026-10-21): atlas-mapping evidence gaps\n\n## @Hillis2002  [seed]\nHillis AE, Wityk RJ.\nSubcortical aphasia and neglect in acute stroke.\n*Brain*. 2002.\n\n> Gap thalamus.\n", encoding="utf-8")
            (root / "regions").mkdir()
            (root / "regions" / "x.md").write_text("---\nid: x\nstatus: approved\nfindings:\n- id: f1\n  citation: '@Baldo2006'\n---\n", encoding="utf-8")
            cands, added = S.backfill_candidates(root, date="2026-10-26")
            self.assertEqual(added, 3)
            by = {c["key"]: c for c in cands}
            self.assertEqual(by["@Baldo2006"]["title"], "Role of frontal cortex in fluency")
            self.assertEqual(by["@Baldo2006"]["doi"], "10.1017/s1355617706061078")
            self.assertEqual(S.stage_of(by["@Baldo2006"]), ("included", None))
            self.assertEqual(S.stage_of(by["@Brady2022RELEASE"]), ("excluded_ft", "not_extractable"))
            self.assertEqual(S.stage_of(by["@Hillis2002"]), ("awaiting_ft", None))
            self.assertEqual(by["@Hillis2002"]["sources"][0]["kind"], "gap_analysis")
            self.assertTrue(all(d["by"] == "legacy" for c in cands for d in c["screening"]))
            facts = S.kb_facts(root)
            self.assertEqual(S.kb_state(facts["@Baldo2006"]), "in_kb")
            # idempotent
            S.save_candidates(cands, root)
            _, again = S.backfill_candidates(root, date="2026-10-26")
            self.assertEqual(again, 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
