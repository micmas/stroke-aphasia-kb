#!/usr/bin/env python3
"""
test_portal_security.py — the portal / publication fixes from REVIEW.md (findings 7–10 and 20),
offline: no Cloudflare, R2, GitHub or papers folder; temporary fixtures only.

    python tests/test_portal_security.py
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import portal_import as PI  # noqa: E402

PDF = b"%PDF-1.4\n" + b"x" * 2000
SHA = hashlib.sha256(PDF).hexdigest()


class _Patched:
    """Point portal_import at a temporary repository and restore it afterwards."""

    def __init__(self, test: unittest.TestCase, cands: list[dict] | None = None, keys: set[str] | None = None):
        self.t = test
        self.cands = cands or []
        self.keys = keys or set()

    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.saved = {k: getattr(PI, k) for k in ("ROOT", "PAPERS", "PORTAL", "INBOX", "APPLIED", "LOG", "REVIEWERS")}
        self.saved_fetch = dict(PI.FETCH)
        self.saved_load = PI.S.load_candidates
        PI.ROOT = self.root
        PI.PAPERS = self.root / "papers"
        PI.PORTAL = self.root / "portal"
        PI.INBOX = self.root / "logs" / "portal" / "inbox"
        PI.APPLIED = self.root / "logs" / "portal" / "applied"
        PI.LOG = self.root / "logs" / "extraction_log.md"
        PI.REVIEWERS = self.root / "portal" / "reviewers.yaml"
        for d in (PI.PAPERS, PI.PORTAL, PI.INBOX, PI.APPLIED):
            d.mkdir(parents=True, exist_ok=True)
        PI.S.load_candidates = lambda *a, **k: self.cands
        self.deleted: list[tuple[str, str]] = []
        PI.FETCH["get"] = lambda bucket, obj, dest: dest.write_bytes(PDF) and None
        PI.FETCH["delete"] = lambda bucket, obj: self.deleted.append((bucket, obj)) or None
        return self

    def state(self) -> dict:
        return {"citation_keys": set(self.keys)}

    def __exit__(self, *exc):
        for k, v in self.saved.items():
            setattr(PI, k, v)
        PI.FETCH.clear(); PI.FETCH.update(self.saved_fetch)
        PI.S.load_candidates = self.saved_load
        self.tmp.cleanup()


def _rec(rid: str, **kw) -> dict:
    return {"id": rid, "name": "paper.pdf", "bytes": len(PDF), "sha256": SHA, "bucket": "b", "object": "uploads/x.pdf", **kw}


class UploadContainment(unittest.TestCase):
    """Finding 7: an upload record cannot place a file outside papers/."""

    def test_traversal_and_absolute_ids_are_refused(self):
        with _Patched(self, keys={"smith2020"}) as P:
            for rid in ("@../outside", "@/tmp/abs", "@..", "../x", "@Smith2020/../../x", "C0001/../x", "@a\\b"):
                msg = PI.apply_pdf(_rec(rid), "alex", True, P.state())
                self.assertTrue(msg.startswith("skip"), f"{rid}: {msg}")
            self.assertEqual(sorted(p.name for p in P.root.rglob("*.pdf")), [])

    def test_unregistered_citation_key_is_refused(self):
        with _Patched(self, keys={"smith2020"}) as P:
            self.assertIn("skip: no candidate or citation", PI.apply_pdf(_rec("@Unknown2021"), "alex", True, P.state()))
            msg = PI.apply_pdf(_rec("@Smith2020"), "alex", True, P.state())
            self.assertIn("papers/Smith2020.pdf", msg)
            self.assertEqual((PI.PAPERS / "Smith2020.pdf").read_bytes(), PDF)

    def test_register_values_are_checked_too(self):
        cands = [{"id": "C0001", "pdf_file": "../../regions/evil.pdf"},
                 {"id": "C0002", "key": "@../../evil"},
                 {"id": "C0003", "title": "No key"}]
        with _Patched(self, cands=cands) as P:
            self.assertIn("skip: not a plain PDF file name", PI.apply_pdf(_rec("C0001"), "alex", True, P.state()))
            self.assertIn("malformed key", PI.apply_pdf(_rec("C0002"), "alex", True, P.state()))
            msg = PI.apply_pdf(_rec("C0003", name="../../x/Some Paper.pdf"), "alex", True, P.state())
            self.assertIn("papers/C0003_", msg)
            landed = [p for p in P.root.rglob("*.pdf")]
            self.assertEqual(len(landed), 1)
            self.assertEqual(landed[0].parent.resolve(), PI.PAPERS.resolve())

    def test_symlinked_papers_folder_still_works(self):
        with _Patched(self, keys={"smith2020"}) as P:
            elsewhere = P.root / "OneDrive" / "papers"
            elsewhere.mkdir(parents=True)
            PI.PAPERS.rmdir()
            os.symlink(elsewhere, PI.PAPERS)
            self.assertIn("papers/Smith2020.pdf", PI.apply_pdf(_rec("@Smith2020"), "alex", True, P.state()))
            self.assertTrue((elsewhere / "Smith2020.pdf").exists())
            self.assertIn("skip", PI.apply_pdf(_rec("@../outside"), "alex", True, P.state()))


class ManuscriptLicence(unittest.TestCase):
    """Finding 8: cc_manuscript is private unless a person confirmed the very file we hold."""

    def setUp(self):
        import publish_portal as PP
        self.PP = PP
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.papers = self.root / "papers"; self.papers.mkdir()
        for k in ("Open2020", "Manu2021", "Closed2022"):
            (self.papers / f"{k}_annotated.pdf").write_bytes(b"%PDF-annotated " + k.encode())
            (self.papers / f"{k}.pdf").write_bytes(b"%PDF-source " + k.encode())
        (self.root / "screening").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def lic(self, manu_extra: dict | None = None) -> dict:
        return {"@Open2020": {"category": "cc"}, "@Manu2021": {"category": "cc_manuscript", **(manu_extra or {})},
                "@Closed2022": {"category": "rights_reserved"}}

    def test_manuscript_only_metadata_is_private(self):
        idx = self.PP.scan_pdfs(self.papers, self.lic())
        self.assertEqual(idx["@Open2020"]["annotated"], "cc/Open2020_annotated.pdf")
        self.assertTrue(idx["@Open2020"]["public"])
        self.assertEqual(idx["@Manu2021"]["annotated"], "pdf/Manu2021_annotated.pdf")
        self.assertFalse(idx["@Manu2021"]["public"])
        self.assertFalse(idx["@Closed2022"]["public"])

    def test_confirmation_is_bound_to_the_source_file(self):
        sha = hashlib.sha256((self.papers / "Manu2021.pdf").read_bytes()).hexdigest()
        ok = {"public_copy": {"sha256": sha, "version": "accepted manuscript", "confirmed_by": "human:michele", "confirmed_on": "2026-11-11"}}
        idx = self.PP.scan_pdfs(self.papers, self.lic(ok))
        self.assertTrue(idx["@Manu2021"]["public"]); self.assertEqual(idx["@Manu2021"]["public_basis"], "confirmed_copy")
        # someone replaces papers/Manu2021.pdf with the publisher's version: private again
        (self.papers / "Manu2021.pdf").write_bytes(b"%PDF-publisher version")
        self.assertFalse(self.PP.scan_pdfs(self.papers, self.lic(ok))["@Manu2021"]["public"])
        # a hash without a person, or for a rights-reserved paper, does nothing
        nobody = {"public_copy": {"sha256": sha}}
        self.assertFalse(self.PP.scan_pdfs(self.papers, self.lic(nobody))["@Manu2021"]["public"])
        closed = self.lic(); closed["@Closed2022"]["public_copy"] = {"sha256": hashlib.sha256((self.papers / "Closed2022.pdf").read_bytes()).hexdigest(), "confirmed_by": "human:x"}
        self.assertFalse(self.PP.scan_pdfs(self.papers, closed)["@Closed2022"]["public"])

    def test_confirm_command_and_refresh_keeps_it(self):
        import licences as L
        path = self.root / "screening" / "licences.yaml"
        L.save(path, self.lic())
        msg = self.PP.confirm_public_copy("Manu2021", "michele", papers_dir=self.papers, root=self.root, today="2026-11-11")
        self.assertIn("confirmed", msg)
        rec = L.load(path)["@Manu2021"]
        self.assertEqual(rec["public_copy"]["confirmed_by"], "human:michele")
        self.assertTrue(self.PP.scan_pdfs(self.papers, L.load(path))["@Manu2021"]["public"])
        # screen.py licences --refresh writes a fresh record from metadata: the confirmation stays
        fresh = L.load(path); fresh["@Manu2021"] = {"category": "cc_manuscript", "label": "CC BY 4.0", "source": "crossref"}
        L.save(path, fresh)
        self.assertEqual(L.load(path)["@Manu2021"]["public_copy"]["sha256"], rec["public_copy"]["sha256"])
        for bad_key, bad_by in (("Open2020", "michele"), ("Closed2022", "michele"), ("Manu2021", ""), ("Manu2021", "model:gemma4:31b"), ("Manu2021", "human:")):
            with self.assertRaises(ValueError, msg=f"{bad_key} {bad_by}"):
                self.PP.confirm_public_copy(bad_key, bad_by, papers_dir=self.papers, root=self.root)

    def test_explorer_links_follow_the_index_not_the_category(self):
        import export_webapp as EW
        (self.root / "portal").mkdir()
        (self.root / "portal" / "portal.config.json").write_text(json.dumps({"portalUrl": "https://portal.test/"}))
        (self.root / "portal" / "papers.json").write_text(json.dumps({"papers": self.PP.scan_pdfs(self.papers, self.lic())}))
        out = EW.portal(self.root)
        self.assertEqual(out["publicPdfs"], ["@Open2020"])
        self.assertEqual(out["publicCategories"], ["cc"])
        self.assertEqual(out["publicPdfBase"], "https://portal.test/cc/")
        # an index synced before this change still marks the manuscript-only paper public: ignored
        stale = self.PP.scan_pdfs(self.papers, self.lic()); stale["@Manu2021"].update(annotated="cc/Manu2021_annotated.pdf", public=True)
        (self.root / "portal" / "papers.json").write_text(json.dumps({"papers": stale}))
        self.assertEqual(EW.portal(self.root)["publicPdfs"], ["@Open2020"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
