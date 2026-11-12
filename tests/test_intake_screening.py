#!/usr/bin/env python3
"""intake_papers.py step 3 (screening PDFs): a record's PDF is checked against the record
(DOI or title on the first pages), named <id>_<Author><Year>.pdf, and never registered as a
KB citation by register_papers.py. Run: python tests/test_intake_screening.py"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

try:
    import pymupdf
except ImportError:  # pragma: no cover
    pymupdf = None


def make_pdf(path: Path, text: str) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_textbox(pymupdf.Rect(50, 50, 550, 800), text, fontsize=10)
    doc.save(str(path))


BODY = ("Abstract. " + "Patients with chronic post-stroke aphasia were assessed with structural imaging and "
        "language batteries; lesion-symptom mapping related damage to behaviour. " * 4)


@unittest.skipIf(pymupdf is None, "PyMuPDF not installed")
class ScreeningPdfs(unittest.TestCase):
    def setUp(self):
        import intake_papers as IP
        import screening as S
        import screen as SC
        self.IP, self.S, self.SC = IP, S, SC
        self.tmp = Path(tempfile.mkdtemp()); self.papers = self.tmp / "papers"; self.papers.mkdir()
        self.cands = [
            {"id": "C0001", "title": "Predictors beyond the lesion: health and demographic factors in aphasia",
             "first_author": "Johnson", "year": 2022, "doi": "10.1016/j.cortex.2022.06.013", "pdf_file": "C0001_Johnson-2022-Predictors beyond.pdf"},
            {"id": "C0002", "title": "Fixel-based white matter correlates of sentence comprehension",
             "first_author": "Péronne", "year": 2025, "doi": "10.3390/brainsci15101039", "pdf_file": "C0002_download.pdf"},
            {"id": "C0003", "title": "Mapping sentence comprehension and syntactic complexity in stroke survivors",
             "first_author": "Biondo", "year": 2024, "doi": "10.1093/braincomms/fcae379", "pdf_file": "C0003_x.pdf"},
        ]
        make_pdf(self.papers / self.cands[0]["pdf_file"], f"doi: 10.1016/j.cortex.2022.06.013\n{BODY}")
        make_pdf(self.papers / self.cands[1]["pdf_file"], f"Fixel-based white matter correlates of sentence comprehension\n{BODY}")
        make_pdf(self.papers / self.cands[2]["pdf_file"], f"An unrelated paper about hip fractures in older adults. doi: 10.1000/xyz123\n{BODY}")
        self.saved = (S.load_candidates, S.save_candidates, SC.link_pdfs, SC._log)
        self.written = []
        S.load_candidates = lambda root=None: self.cands
        S.save_candidates = lambda c, root=None: self.written.append([dict(x) for x in c])
        SC.link_pdfs = lambda c, verbose=True: {"linked": [], "unknown": [], "already": []}
        SC._log = lambda *a: None

    def tearDown(self):
        self.S.load_candidates, self.S.save_candidates, self.SC.link_pdfs, self.SC._log = self.saved

    def test_checked_and_named(self):
        IP = self.IP
        self.assertEqual(IP.identity(self.papers / self.cands[0]["pdf_file"], self.cands[0])[0], True)
        self.assertEqual(IP.identity(self.papers / self.cands[1]["pdf_file"], self.cands[1])[0], True)
        self.assertEqual(IP.identity(self.papers / self.cands[2]["pdf_file"], self.cands[2])[0], False)
        IP.screening_pdfs(self.papers, execute=False)          # dry run: nothing moves
        self.assertTrue((self.papers / "C0001_Johnson-2022-Predictors beyond.pdf").exists())
        IP.screening_pdfs(self.papers, execute=True)
        self.assertTrue((self.papers / "C0001_Johnson2022.pdf").exists())
        self.assertTrue((self.papers / "C0002_Peronne2025.pdf").exists())    # accents folded
        self.assertTrue((self.papers / "C0003_x.pdf").exists())              # the wrong paper is left alone
        self.assertEqual([c["pdf_file"] for c in self.written[-1]], ["C0001_Johnson2022.pdf", "C0002_Peronne2025.pdf", "C0003_x.pdf"])

    def test_label(self):
        L = self.IP._label
        self.assertEqual(L({"first_author": "REhabilitation", "year": 2022}), "Rehabilitation2022")
        self.assertEqual(L({"first_author": "McCarthy", "year": 2019}), "McCarthy2019")
        self.assertEqual(L({"first_author": "van der Meulen", "year": 2014}), "VanDerMeulen2014")
        self.assertEqual(L({"authors": "Øster, K.; Lee, J.", "year": "2020-05"}), "Oster2020")

    def test_screening_pdfs_never_become_citations(self):
        import register_papers as RP
        cit = self.tmp / "citations.md"; cit.write_text("# Citations\n", encoding="utf-8")
        calls = []
        saved = RP.lookup
        RP.lookup = lambda doi: calls.append(doi)
        try:
            RP.register(self.papers, cit, execute=True, skip=set())
        finally:
            RP.lookup = saved
        self.assertEqual(calls, [])                           # C\d{4}_ files are skipped before any lookup
        self.assertEqual(cit.read_text(encoding="utf-8"), "# Citations\n")


if __name__ == "__main__":
    unittest.main(verbosity=1)
