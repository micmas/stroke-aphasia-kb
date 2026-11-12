#!/usr/bin/env python3
"""
test_endnote.py — endnote_match.py against a small fake EndNote library (the same SQLite
tables and PDF folder layout): DOI, PMID and title matches, trashed references and non-PDF
attachments ignored, nothing copied on a dry run, the library never modified, a keyless
candidate linked through `pdf_file`.

    python tests/test_endnote.py
"""
from __future__ import annotations

import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def make_library(folder: Path) -> Path:
    pkg = folder / "Lib.enlp"; data = pkg / "Lib.Data" / "PDF"; data.mkdir(parents=True)
    con = sqlite3.connect(str(pkg / "Lib.enl"))
    con.execute("create table refs (id integer primary key, trash_state int, author text, year text, title text, electronic_resource_number text, accession_number text, url text)")
    con.execute("create table file_res (refs_id int, file_path text, file_type int, file_pos int)")
    con.execute("create table ret_watch (refs_id int, clean_doi text, clean_pmid text)")
    rows = [(1, 0, "Smith, A.\rJones, B.", "2020", "Lesion correlates of naming after stroke: a voxel-based study", "https://doi.org/10.1000/ABC.2020", "", ""),
            (2, 0, "Lee, C.", "2019", "Auditory comprehension outcome in Wernicke's aphasia over time", "", "31234567", ""),
            (3, 0, "Roy, D.", "2018", "White matter bottlenecks and chronic aphasia severity: a tractography study", "", "", ""),
            (4, 1, "Old, E.", "2017", "A trashed reference that would otherwise match by DOI", "10.1000/trash.2017", "", ""),
            (5, 0, "Doc, F.", "2016", "A reference whose only attachment is a Word file, not a PDF", "10.1000/word.2016", "", "")]
    con.executemany("insert into refs values (?,?,?,?,?,?,?,?)", rows)
    files = [(1, "111/smith.pdf", 1, 0), (1, "111/smith-supplement.pdf", 1, 1), (2, "222/lee.pdf", 1, 0), (3, "333/roy.pdf", 1, 0),
             (4, "444/old.pdf", 1, 0), (5, "555/notes.docx", 1, 0)]
    con.executemany("insert into file_res values (?,?,?,?)", files)
    con.commit(); con.close()
    for _, path, _, _ in files:
        f = data / path; f.parent.mkdir(exist_ok=True)
        f.write_bytes(b"%PDF-1.4 " + path.encode() if path.endswith(".pdf") else b"PK docx")
    return pkg


class EndNote(unittest.TestCase):
    def test_match_and_copy(self):
        import endnote_match as E
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); pkg = make_library(d); papers = d / "papers"; papers.mkdir(); log = d / "log.md"
            cands = [{"id": "C0001", "key": "@Smith2020", "doi": "10.1000/abc.2020", "title": "x", "year": 2020, "stage": "awaiting_ft"},
                     {"id": "C0002", "key": None, "pmid": "31234567", "title": "y", "year": 2019, "stage": "awaiting_ft"},
                     {"id": "C0003", "key": None, "title": "White Matter Bottlenecks and Chronic Aphasia Severity — a tractography study", "year": 2018, "stage": "included"},
                     {"id": "C0004", "key": None, "doi": "10.1000/trash.2017", "title": "t", "year": 2017, "stage": "awaiting_ft"},
                     {"id": "C0005", "key": None, "doi": "10.1000/word.2016", "title": "w", "year": 2016, "stage": "awaiting_ft"},
                     {"id": "C0006", "key": None, "doi": "10.1000/nowhere", "title": "n", "year": 2015, "stage": "awaiting_ft"}]
            enl, pdfs = E.locate(pkg)
            self.assertEqual(enl.name, "Lib.enl")
            refs = E.read_library(enl)
            self.assertEqual(sorted(r["id"] for r in refs), [1, 2, 3])                      # trashed and PDF-less references are out
            self.assertEqual(refs[0]["doi"], "10.1000/abc.2020"); self.assertEqual(refs[0]["author"], "Smith, A.")
            got = {m["candidate"]["id"]: m["how"] for m in E.match(cands, refs)}
            self.assertEqual(got, {"C0001": "DOI", "C0002": "PMID"})                        # titles only on request
            got = {m["candidate"]["id"]: m["how"] for m in E.match(cands, refs, titles=True)}
            self.assertEqual(got, {"C0001": "DOI", "C0002": "PMID", "C0003": "title + year"})
            before = sorted((p.name, p.stat().st_size, p.stat().st_mtime_ns) for p in pkg.rglob("*") if p.is_file())
            saved = (E.wanted, E.S.load_candidates, E.S.save_candidates)
            register = [dict(c) for c in cands]; written = []
            E.wanted = lambda root=None, papers_=None, ids=None: [c for c in cands if not E.has_pdf(c, papers)]
            E.S.load_candidates = lambda root=None: register
            E.S.save_candidates = lambda rows, root=None: written.append(rows)
            try:
                E.run(pkg, False, True, None, "tester", root=d, papers=papers, log=log)
                self.assertEqual(list(papers.iterdir()), [])                                # a dry run copies nothing
                E.run(pkg, True, True, None, "tester", root=d, papers=papers, log=log)
            finally:
                E.wanted, E.S.load_candidates, E.S.save_candidates = saved
            self.assertEqual(sorted(p.name for p in papers.iterdir()), ["C0001_Smith2020.pdf", "C0002_lee.pdf", "C0003_roy.pdf"])
            self.assertEqual((papers / "C0001_Smith2020.pdf").read_bytes(), b"%PDF-1.4 111/smith.pdf")   # the first attachment
            self.assertEqual(register[1]["pdf_file"], "C0002_lee.pdf"); self.assertNotIn("pdf_file", register[0])
            self.assertEqual(len(written), 1)
            self.assertEqual(log.read_text().count("ENDNOTE-PDF"), 3)
            after = sorted((p.name, p.stat().st_size, p.stat().st_mtime_ns) for p in pkg.rglob("*") if p.is_file())
            self.assertEqual(before, after)                                                 # the library is untouched

    def test_normalising(self):
        import endnote_match as E
        self.assertEqual(E.norm_doi("doi:10.1016/J.Bandl.2018.08.005."), "10.1016/j.bandl.2018.08.005")
        self.assertEqual(E.norm_doi("no doi here"), "")
        self.assertEqual(E.norm_pmid(" PMID: 30179751 "), "30179751"); self.assertEqual(E.norm_pmid("WOS:000123"), "")
        self.assertEqual(E.pmid_from_url("https://www.ncbi.nlm.nih.gov/pubmed/29724159"), "29724159")


if __name__ == "__main__":
    unittest.main(verbosity=1)
