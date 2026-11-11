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


if __name__ == "__main__":
    unittest.main(verbosity=1)
