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


PUBMED_WITH_REFS = b"""<?xml version="1.0"?><PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>111</PMID>
<Article><Journal><Title>Brain</Title><JournalIssue><PubDate><Year>2015</Year></PubDate></JournalIssue></Journal>
<ArticleTitle>Lesion mapping of naming after stroke in a large cohort</ArticleTitle>
<AuthorList><Author><LastName>Smith</LastName><Initials>J</Initials></Author></AuthorList></Article>
<CommentsCorrectionsList><CommentsCorrections RefType="Cites"><PMID>8918862</PMID></CommentsCorrections></CommentsCorrectionsList></MedlineCitation>
<PubmedData><ArticleIdList><ArticleId IdType="pubmed">111</ArticleId><ArticleId IdType="doi">10.1/own</ArticleId></ArticleIdList>
<ReferenceList><Reference><Citation>Dronkers 1996</Citation><ArticleIdList><ArticleId IdType="doi">10.1038/384159a0</ArticleId>
<ArticleId IdType="pubmed">8918862</ArticleId></ArticleIdList></Reference></ReferenceList></PubmedData></PubmedArticle>
<PubmedBookArticle><BookDocument><PMID Version="1">30422576</PMID><ArticleIdList><ArticleId IdType="bookaccession">NBK532981</ArticleId></ArticleIdList>
<Book><BookTitle book="statpearls">StatPearls</BookTitle><PubDate><Year>2026</Year></PubDate></Book>
<ArticleTitle book="statpearls">Frontal Lobe Syndrome</ArticleTitle><AuthorList><Author><LastName>Jabbari</LastName><Initials>B</Initials></Author></AuthorList>
<PublicationType UI="D000072643">Study Guide</PublicationType><Abstract><AbstractText>Frontal lobe syndrome is ...</AbstractText></Abstract>
</BookDocument></PubmedBookArticle></PubmedArticleSet>"""


class Parsers(unittest.TestCase):
    def test_pubmed_references_and_books(self):
        art, book = screen.parse_pubmed_xml(PUBMED_WITH_REFS)
        self.assertEqual((art["pmid"], art["doi"]), ("111", "10.1/own"))     # not the cited paper's DOI
        self.assertEqual(art["authors"], ["Smith J"])
        self.assertEqual((book["pmid"], book["title"], book["year"], book["journal"], book["book"]),
                         ("30422576", "Frontal Lobe Syndrome", 2026, "StatPearls", True))
        self.assertEqual(book["pub_types"], ["Study Guide"])

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
        scopus = "\ufeffTY  - JOUR\r\nAU  - Leff, A.P.\r\nTI  - The left superior temporal gyrus is a shared substrate\r\nPY  - 2009\r\nT2  - Brain\r\nDO  - 10.1093/brain/awp273\r\nAB  - We analysed 210 stroke patients.\r\nC2  - 19892765\r\nER  - \r\n"
        (r,) = screen.parse_ris(scopus)
        self.assertEqual((r["pmid"], r["doi"], r["year"], r["journal"]), ("19892765", "10.1093/brain/awp273", 2009, "Brain"))
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

    def test_doi_parentheses(self):
        self.assertEqual(S.norm_doi("10.1044/1058-0360(2004/025)"), "10.1044/1058-0360(2004/025)")
        self.assertEqual(S.norm_doi("10.1044/1058-0360(2004/025"), "10.1044/1058-0360(2004/025)")   # cut by a parser
        self.assertEqual(S.norm_doi("(doi:10.1000/abc)."), None)                                      # not a bare DOI
        self.assertEqual(S.norm_doi("https://doi.org/10.1000/ABC)."), "10.1000/abc")

    def test_same_title_different_paper(self):
        a = {"id": "C1", "title": "Unilateral opercular infarction presenting with foreign accent", "year": 2014,
             "pmid": "1", "doi": "10.1/a", "sources": [], "screening": []}
        idx = S.build_identity_index([a])
        self.assertIsNone(S.find_duplicate({"title": a["title"], "year": 2014, "pmid": "2", "doi": "10.1/b"}, idx))
        self.assertIs(S.find_duplicate({"title": a["title"], "year": 2014}, idx), a)        # no ids: same paper
        self.assertIs(S.find_duplicate({"title": a["title"], "year": 2014, "pmid": "1"}, idx), a)

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


STRATS = """
version: 3
status: draft
years: 2000-
blocks:
  pubmed:
    a: ("Aphasia"[Mesh] OR aphasi*[tiab])
    s: (stroke*[tiab])
strategies:
  - id: q1
    buckets: [regions]
    for: [q1]
    pubmed: ${a} AND ${s} AND lesion*[tiab]
    scopus: TITLE-ABS-KEY(aphasi*)
  - id: old
    years: 1990-1999
    pubmed: ${a}
  - id: bad
    pubmed: ${a} AND ${missing}
"""


class Protocol(unittest.TestCase):
    def test_expand_and_fingerprint(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "screening").mkdir()
            (root / "screening" / "strategies.yaml").write_text(STRATS, encoding="utf-8")
            st = S.load_strategies(root)
            self.assertEqual(S.expand_query(st, "q1", "pubmed"),
                             '("Aphasia"[Mesh] OR aphasi*[tiab]) AND (stroke*[tiab]) AND lesion*[tiab]')
            with self.assertRaises(KeyError):
                S.expand_query(st, "q1", "openalex")          # no openalex version
            with self.assertRaises(KeyError):
                S.expand_query(st, "bad", "pubmed")           # unknown block
            with self.assertRaises(KeyError):
                S.strategy(st, "nope")
            self.assertEqual(S.strategy_years(st, "q1"), "2000-")            # the protocol's window
            self.assertEqual(S.strategy_years(st, "old"), "1990-1999")       # a strategy's own
            self.assertEqual(S.query_for_run(st, "q1", "scopus"), "(TITLE-ABS-KEY(aphasi*)) AND PUBYEAR > 1999")
            self.assertEqual(S.query_for_run(st, "q1", "pubmed"), S.expand_query(st, "q1", "pubmed"))   # a filter, not text
            self.assertEqual(S.year_window("1990-1999"), (1990, 1999))
            fp = S.protocol_fingerprint(root)
            (root / "screening" / "strategies.yaml").write_text(STRATS + "\n# amended\n", encoding="utf-8")
            self.assertNotEqual(fp, S.protocol_fingerprint(root))
            state = S.protocol_state(root)               # not a git checkout: never locked
            self.assertFalse(state["locked"])
            self.assertEqual(state["version"], 3)

    def test_the_shipped_strategies_expand(self):
        st = S.load_strategies(ROOT)
        for x in st["strategies"]:
            for db in ("pubmed", "openalex", "scopus", "psycinfo"):
                if x.get(db):
                    q = S.expand_query(st, x["id"], db)
                    self.assertNotIn("${", q, (x["id"], db))
                    self.assertEqual(q.count("("), q.count(")"), (x["id"], db))
                    if db == "openalex":
                        self.assertNotIn(",", q, x["id"])
                        self.assertNotIn("*", q, x["id"])


def _legacy_cand(cid, key, title, include=True):
    d = {"stage": "full_text", "decision": "include" if include else "exclude", "by": "legacy", "date": "2026-10-26"}
    if not include:
        d["reason"] = "not_extractable"
    return {"id": cid, "key": key, "title": title, "year": 2010, "sources": [{"kind": "hand_picked"}],
            "skip_title_abstract": True, "screening": [d]}


class Rebaseline(unittest.TestCase):
    def test_rebaseline_recall_and_arms(self):
        a = _legacy_cand("C0001", "@A2010", "Lesion correlates of naming in chronic stroke aphasia")
        b = _legacy_cand("C0002", "@B2010", "Thalamic aphasia after haemorrhage in a large cohort")
        r = _legacy_cand("C0003", "@R2010", "A refused paper about something else entirely", include=False)
        cands = [a, b, r]
        self.assertTrue(S.is_benchmark(a))
        self.assertEqual(S.stage_of(a), ("included", None))
        out = S.rebaseline(cands, "2026-10-27", protocol="abc")
        self.assertEqual(out, {"benchmark": 2, "refused": 1, "candidates": 3})
        self.assertEqual(a["screening"], [])
        self.assertEqual(a["legacy"]["decisions"][0]["by"], "legacy")
        self.assertTrue(a["benchmark"] and S.is_benchmark(a))
        self.assertFalse(S.is_benchmark(r))
        self.assertEqual(S.stage_of(a), ("awaiting_ft", None))           # other-methods arm: full text
        self.assertEqual(S.rebaseline(cands, "2026-10-28")["candidates"], 0)   # idempotent
        # a search finds A: it moves to the database arm and is screened at title/abstract
        recs = [{"title": "Lesion correlates of naming in chronic stroke aphasia", "year": 2010, "pmid": "1"},
                {"title": "Something new about aphasia and the insula in stroke", "year": 2020, "pmid": "2"}]
        self.assertEqual([c["id"] for c in S.benchmark_hits(recs, cands)], ["C0001"])
        screen.add_records(recs, "S001", cands, {})
        self.assertEqual(S.arm_of(a), "databases")
        self.assertEqual(S.stage_of(a), ("awaiting_ta", None))
        self.assertEqual(S.stage_of(b), ("awaiting_ft", None))
        searches = [{"id": "S001", "database": "pubmed", "strategy": "q1"}]
        strategies = {"strategies": [{"id": "q1", "buckets": ["regions"]}, {"id": "q9", "buckets": ["therapies"]}]}
        rec = S.recall(cands, searches, strategies, {"@A2010": {"regions"}, "@B2010": {"regions"}})
        self.assertEqual((rec["benchmark"], rec["found"]), (2, 1))
        self.assertAlmostEqual(rec["recall"], 0.5)
        q1 = rec["byStrategy"][0]
        self.assertEqual((q1["inScope"], q1["found"], q1["missed"]), (2, 1, ["C0002"]))
        self.assertIsNone(rec["byStrategy"][1]["recall"])                    # not run, nothing in scope
        self.assertEqual([m["id"] for m in rec["missed"]], ["C0002"])
        # the publication window and full-text exclusions under the protocol leave the denominator
        old = _legacy_cand("C0004", "@O1996", "A classic paper from before the window")
        old["year"] = 1996
        cands.append(old)
        S.rebaseline(cands, "2026-10-27")
        self.assertIsNone(screen._apply_decision(b, "full_text", "exclude", "not_aphasia", "michele", None, "2026-10-28"))
        rec = S.recall(cands, searches, {**strategies, "years": "2000-"}, {"@A2010": {"regions"}, "@B2010": {"regions"}})
        self.assertEqual((rec["benchmarkAll"], rec["benchmark"], rec["found"], rec["recall"]), (3, 1, 1, 1.0))
        self.assertEqual([m["id"] for m in rec["outsideWindow"]], ["C0004"])
        self.assertEqual([m["id"] for m in rec["excludedUnderProtocol"]], ["C0002"])


class DualScreening(unittest.TestCase):
    def test_check_decisions_and_kappa(self):
        cands = [{"id": f"C{i}", "title": f"t{i}", "screening": []} for i in range(10)]
        record = ["include"] * 5 + ["exclude"] * 5
        check = ["include"] * 4 + ["exclude"] * 6
        for c, x, y in zip(cands, record, check):
            self.assertIsNone(screen._apply_decision(c, "title_abstract", x, "not_stroke" if x == "exclude" else None, "michele", None, "2026-10-27"))
            self.assertIsNone(screen._apply_decision(c, "title_abstract", y, "not_stroke" if y == "exclude" else None, "alex", None, "2026-10-28", role="check"))
        # the check decision never becomes the decision of record
        self.assertEqual(S.stage_of(cands[4]), ("awaiting_ft", None))
        self.assertEqual(S.last_decision(cands[4], "title_abstract")["by"], "michele")
        # same person cannot check their own decision
        self.assertIsNotNone(screen._apply_decision(cands[0], "title_abstract", "include", None, "michele", None, "2026-10-28", role="check"))
        a = S.agreement(cands, "title_abstract")
        self.assertEqual(a["pairs"], 10)
        self.assertAlmostEqual(a["observed"], 0.9)
        self.assertAlmostEqual(a["kappa"], 0.8)
        self.assertEqual([d["id"] for d in a["disagreements"]], ["C4"])
        self.assertEqual(list(a["byCheckScreener"]), ["alex"])


class Withdraw(unittest.TestCase):
    def test_withdraw_an_incomplete_import(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "screening").mkdir()
            cands = [{"id": "C0001", "key": "@A2010", "title": "Old", "benchmark": True,
                      "sources": [{"kind": "hand_picked"}, {"search": "S002"}], "screening": []},
                     {"id": "C0002", "title": "Only from the bad export", "sources": [{"search": "S002"}], "screening": []},
                     {"id": "C0003", "title": "From both", "sources": [{"search": "S001"}, {"search": "S002"}], "screening": []}]
            S.save_candidates(cands, root)
            S.save_searches([{"id": "S001", "database": "pubmed"}, {"id": "S002", "database": "scopus", "retrieved": 98}], root)
            orig = (S.load_searches, S.load_candidates, S.save_searches, S.save_candidates, S.load_withdrawn, screen._log,
                    screen.load_abstracts)
            S.load_searches = lambda root_=root: orig[0](root)
            S.load_candidates = lambda root_=root: orig[1](root)
            S.save_searches = lambda s, root_=root, withdrawn=None: orig[2](s, root, withdrawn)
            S.save_candidates = lambda c, root_=root: orig[3](c, root)
            S.load_withdrawn = lambda root_=root: orig[4](root)
            screen._log = lambda *a: None
            screen.load_abstracts = lambda: {}
            try:
                a = type("A", (), {"id": "S002", "why": "export held one page only", "by": "michele", "execute": True})()
                self.assertEqual(screen.cmd_withdraw(a), 0)
                self.assertEqual([s["id"] for s in S.load_searches()], ["S001"])
                self.assertEqual(S.load_withdrawn()[0]["withdrawn"]["why"], "export held one page only")
                self.assertEqual([c["id"] for c in S.load_candidates()], ["C0001", "C0003"])
                self.assertEqual(S.load_candidates()[0]["sources"], [{"kind": "hand_picked"}])
                self.assertEqual(screen._next_search_id(S.load_searches()), "S003")    # S002 is never reused
            finally:
                (S.load_searches, S.load_candidates, S.save_searches, S.save_candidates, S.load_withdrawn, screen._log,
                 screen.load_abstracts) = orig


class Prioritised(unittest.TestCase):
    def test_ranking_puts_relevant_first(self):
        import prioritise as P
        rel = ["Voxel-based lesion symptom mapping of naming in chronic stroke aphasia",
               "Arcuate fasciculus lesion load predicts speech production after stroke",
               "White matter disconnection and sentence comprehension in post-stroke aphasia",
               "Lesion location and recovery of aphasia: a voxel-wise study"]
        irr = [f"Knee arthroplasty outcomes in cohort {i} of older adults" for i in range(30)] + \
              [f"Dietary sodium and blood pressure trial {i}" for i in range(30)]
        texts = {f"R{i}": x for i, x in enumerate(rel)} | {f"I{i}": x for i, x in enumerate(irr)}
        texts["Q1"] = "Lesion symptom mapping of verbal fluency in stroke aphasia"
        texts["Q2"] = "Knee arthroplasty outcomes in a new cohort of adults"
        order = [i for i, _ in P.rank(texts, {"R0", "R1", "R2", "R3"}, set(), ["Q2", "Q1"], seed=3)]
        self.assertEqual(order, ["Q1", "Q2"])
        self.assertEqual(P.is_prior("C0001", 1, 0.5), P.is_prior("C0001", 1, 0.5))       # reproducible split
        self.assertEqual(P.rank(texts, set(), set(), ["Q2", "Q1"]), [("Q2", 0.0), ("Q1", 0.0)])

    def test_stopping_rule(self):
        strategies = {"years": "2000-", "prioritised_screening": {"seed": 1, "prior_fraction": 0.0,
                      "stop": {"min_screened_fraction": 0.5, "consecutive_exclusions": 3, "validation_found": 1.0}}}
        db = lambda i, **k: {"id": f"C{i:04d}", "title": f"t{i}", "year": 2010, "sources": [{"search": "S001"}],
                             "screening": [], **k}
        cands = [db(i) for i in range(1, 9)] + [db(9, benchmark=True)]
        seq = 1
        for c, dec in zip(cands[:5], ["include", "exclude", "exclude", "exclude", "exclude"]):
            self.assertIsNone(screen._apply_decision(c, "title_abstract", dec, "not_stroke" if dec == "exclude" else None,
                                                     "michele", None, "2026-10-28", seq=seq))
            seq += 1
        st = S.stopping_state(cands, strategies)
        self.assertEqual((st["records"], st["screened"], st["consecutiveExclusions"]), (9, 5, 4))
        self.assertEqual(st["checks"], {"screened": True, "consecutive": True, "validation": False})   # C0009 not seen yet
        self.assertFalse(st["met"])
        self.assertIsNone(screen._apply_decision(cands[8], "title_abstract", "include", None, "michele", None, "2026-10-28", seq=seq))
        st = S.stopping_state(cands, strategies)
        self.assertEqual((st["consecutiveExclusions"], st["validationScreened"]), (0, 1))
        self.assertFalse(st["met"])                    # the include broke the run of exclusions


class Chase(unittest.TestCase):
    def test_pillar_by_citation_chasing(self):
        inc = {"id": "C0001", "title": "Included lesion study of naming", "year": 2015, "sources": [{"search": "S001"}],
               "screening": [{"stage": "title_abstract", "decision": "include", "by": "michele"},
                             {"stage": "full_text", "decision": "include", "by": "michele"}]}
        pending = {"id": "C0002", "title": "Not yet assessed at full text by anyone", "year": 2016, "sources": [{"search": "S001"}], "screening": []}
        old = {"id": "C0003", "key": "@Dronkers1996", "doi": "10.1038/384159a0", "title": "A new brain region for coordinating speech articulation",
               "year": 1996, "sources": [{"kind": "hand_picked"}], "skip_title_abstract": True, "screening": [], "benchmark": True}
        store = {"c": [inc, pending, old]}
        saved, logged = [], []
        orig = (S.load_candidates, S.save_candidates, screen._log)
        S.load_candidates = lambda root=None: store["c"]
        S.save_candidates = lambda c, root=None: saved.append(len(c))
        screen._log = lambda *a: logged.append(a)
        try:
            args = lambda **k: type("A", (), {"doi": None, "title": None, "year": None, "cited_by": "C0001",
                                              "why": "Source of the insula claim that the gap contests", "by": "michele",
                                              "date": "2026-10-28", "execute": True, **k})()
            with self.assertRaises(SystemExit):
                screen.cmd_chase(args(doi="10.1038/384159a0", cited_by="C0002"))       # citing paper not included
            with self.assertRaises(SystemExit):
                screen.cmd_chase(args(doi="10.1038/384159a0", why="short"))            # reason required
            self.assertEqual(screen.cmd_chase(args(doi="10.1038/384159a0")), 0)
            self.assertTrue(old["pillar"])
            src = old["sources"][-1]
            self.assertEqual((src["kind"], src["cited_by"]), ("citation_chasing", ["C0001"]))
            self.assertEqual(S.stage_of(old), ("awaiting_ft", None))
            self.assertEqual((saved, logged[0][0]), ([3], "CHASED"))
            # a paper with no DOI enters with title and year, as a new candidate
            self.assertEqual(screen.cmd_chase(args(title="Disconnexion syndromes in animals and man", year="1965")), 0)
            self.assertEqual(store["c"][-1]["id"], "C0004")
            # a paper a search already found needs no chasing
            n = len(store["c"])
            self.assertEqual(screen.cmd_chase(args(title="Not yet assessed at full text by anyone", year="2016")), 0)
            self.assertNotIn("pillar", pending)
            self.assertEqual(len(store["c"]), n)
        finally:
            S.load_candidates, S.save_candidates, screen._log = orig


if __name__ == "__main__":
    unittest.main(verbosity=1)
