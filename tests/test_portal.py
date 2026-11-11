#!/usr/bin/env python3
"""
test_portal.py — the review portal's two Python halves, without Cloudflare or a browser:
publish_portal.py mirrors annotated PDFs into the bucket by licence (index in portal/papers.json);
portal_import.py applies the records the portal writes (screen, edit, mark, comment,
verdict) under the reviewer's name and refuses what no longer matches.

    python tests/test_portal.py
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root
sys.path.insert(0, str(ROOT / "scripts"))

DRAFT = """---
schema_version: 2.8
id: left_angular_gyrus
name: Left angular gyrus
kind: atlas
status: draft
created_by: agent:test
created_on: 2026-11-05
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Damage to the left angular gyrus is associated with poorer naming accuracy.
  direction: likely
  relationship: causal
  citation: '@TestPaper2020'
  method: VLSM
  strength: moderate
  source_passages:
  - {section: Abstract, page: 1, quote: Damage to the left angular gyrus was associated with poorer naming., supports: claim}
---
Test draft.
"""


class Publish(unittest.TestCase):
    def test_sync_mirrors_pdfs_by_licence_and_writes_the_index(self):
        import publish_portal as P
        with tempfile.TemporaryDirectory() as d:
            papers = Path(d) / "papers"; index = Path(d) / "papers.json"
            papers.mkdir()
            for k in ("Open2020", "Closed2021", "Unknown2022"):
                (papers / f"{k}_annotated.pdf").write_bytes(b"%PDF-1.4 " + k.encode())
            (papers / "Closed2021.pdf").write_bytes(b"%PDF-1.4 source")       # not annotated: a source, never uploaded
            lic = {"@Open2020": {"category": "cc", "label": "CC BY 4.0"}, "@Closed2021": {"category": "rights_reserved"}}
            bucket: dict[str, str] = {}
            calls: list[tuple] = []
            abstracts = Path(d) / "abstracts.jsonl"; abstracts.write_text('{"id": "C1", "abstract": "x"}\n')

            class Done:
                returncode = 0; stderr = ""
            def put(obj, path, ctype):
                calls.append(("put", obj)); bucket[obj] = Path(path).name; return Done()
            def delete(obj):
                calls.append(("delete", obj)); bucket.pop(obj, None); return Done()
            saved = P.licences
            P.licences = lambda root=None: lic
            try:
                out = P.sync_pdfs(papers, "test-bucket", index_path=index, put=put, delete=delete, abstracts_path=abstracts)
                self.assertEqual(sorted(bucket), ["cc/Open2020_annotated.pdf", "pdf/Closed2021_annotated.pdf", "pdf/Unknown2022_annotated.pdf", "private/abstracts.jsonl"])
                self.assertEqual(out["abstracts"]["object"], "private/abstracts.jsonl")
                self.assertTrue(out["papers"]["@Open2020"]["public"])
                self.assertEqual(out["papers"]["@Unknown2022"]["annotated"], "pdf/Unknown2022_annotated.pdf")   # unknown licence stays private
                self.assertEqual(len(out["papers"]["@Open2020"]["sha256"]), 64)
                self.assertEqual(out["sources"]["keys"], ["@Closed2021"])
                self.assertTrue(index.exists())
                # nothing changed → nothing uploaded
                calls.clear()
                P.sync_pdfs(papers, "test-bucket", index_path=index, put=put, delete=delete, abstracts_path=abstracts)
                self.assertEqual(calls, [])
                # licence changes → the object moves; a re-annotated file is re-put; a removed one is deleted
                lic["@Open2020"] = {"category": "rights_reserved"}
                (papers / "Closed2021_annotated.pdf").write_bytes(b"%PDF-1.4 Closed2021 v2")
                (papers / "Unknown2022_annotated.pdf").unlink()
                out = P.sync_pdfs(papers, "test-bucket", index_path=index, put=put, delete=delete, abstracts_path=abstracts)
                self.assertEqual(sorted(bucket), ["pdf/Closed2021_annotated.pdf", "pdf/Open2020_annotated.pdf", "private/abstracts.jsonl"])
                self.assertIn(("delete", "cc/Open2020_annotated.pdf"), calls)
                self.assertIn(("put", "pdf/Closed2021_annotated.pdf"), calls)
                self.assertNotIn("@Unknown2022", out["papers"])
                # a dry run touches nothing
                calls.clear(); before = index.read_text()
                (papers / "New2023_annotated.pdf").write_bytes(b"%PDF-1.4 new")
                P.sync_pdfs(papers, "test-bucket", dry=True, index_path=index, put=put, delete=delete, abstracts_path=abstracts)
                self.assertEqual(calls, []); self.assertEqual(index.read_text(), before)
                # the build reads the index, not the papers folder
                loaded = P.load_index(index)
                self.assertEqual(set(loaded["papers"]), {"@Open2020", "@Closed2021"})
            finally:
                P.licences = saved

    def test_full_texts_to_assess_are_mirrored_and_removed_when_decided(self):
        import publish_portal as P
        with tempfile.TemporaryDirectory() as d:
            papers = Path(d) / "papers"; index = Path(d) / "papers.json"; papers.mkdir()
            (papers / "Smith2020.pdf").write_bytes(b"%PDF-1.4 smith")
            (papers / "C0002_download name.pdf").write_bytes(b"%PDF-1.4 c2")
            bucket: dict[str, str] = {}

            class Done:
                returncode = 0; stderr = ""
            put = lambda obj, path, ctype: (bucket.__setitem__(obj, Path(path).name), Done())[1]
            delete = lambda obj: (bucket.pop(obj, None), Done())[1]
            ft = {"C0001": papers / "Smith2020.pdf", "C0002": papers / "C0002_download name.pdf"}
            out = P.sync_pdfs(papers, "b", index_path=index, put=put, delete=delete, abstracts_path=Path(d) / "none", fulltext=ft)
            self.assertEqual(bucket, {"pdf/C0001_fulltext.pdf": "Smith2020.pdf", "pdf/C0002_fulltext.pdf": "C0002_download name.pdf"})
            self.assertEqual(out["fulltext"]["C0002"]["object"], "pdf/C0002_fulltext.pdf")
            # C0001 decided → its copy leaves the bucket; C0002 unchanged → not re-sent
            bucket["pdf/C0002_fulltext.pdf"] = "kept"
            out = P.sync_pdfs(papers, "b", index_path=index, put=put, delete=delete, abstracts_path=Path(d) / "none", fulltext={"C0002": ft["C0002"]})
            self.assertEqual(bucket, {"pdf/C0002_fulltext.pdf": "kept"})
            self.assertEqual(set(P.load_index(index)["fulltext"]), {"C0002"})


class Import(unittest.TestCase):
    def setUp(self):
        import portal_import as PI
        self.PI = PI
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "drafts" / "regions").mkdir(parents=True)
        (self.tmp / "logs" / "portal" / "inbox").mkdir(parents=True)
        self.draft = self.tmp / "drafts" / "regions" / "left_angular_gyrus__TestPaper2020.md"
        self.draft.write_text(DRAFT, encoding="utf-8")
        self.saved = {k: getattr(PI, k) for k in ("ROOT", "INBOX", "APPLIED", "LOG", "REVIEWERS")}
        PI.ROOT = self.tmp
        PI.INBOX = self.tmp / "logs" / "portal" / "inbox"
        PI.APPLIED = self.tmp / "logs" / "portal" / "applied"
        PI.LOG = self.tmp / "logs" / "extraction_log.md"
        PI.REVIEWERS = self.tmp / "reviewers.yaml"
        PI.REVIEWERS.write_text(yaml.safe_dump({"reviewers": {"m@uq.edu.au": {"name": "michele", "approver": True},
                                                               "alex@example.org": {"name": "alex", "approver": False}}}), encoding="utf-8")

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(self.PI, k, v)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_who(self):
        t = self.PI.reviewers()
        self.assertEqual(self.PI.who("M@UQ.edu.au", t), ("michele", True, True))
        self.assertEqual(self.PI.who("alex@example.org", t), ("alex", False, True))
        self.assertEqual(self.PI.who("new.person@x.org", t), ("new_person", False, False))

    def test_edit_mark_comment_verdict(self):
        PI = self.PI
        rel = "drafts/regions/left_angular_gyrus__TestPaper2020.md"
        state: dict = {}
        msg = PI.apply_edit({"id": rel, "finding": "f1", "submitted": "2026-11-05T10:00:00Z",
                             "fields": {"strength": {"old": "moderate", "new": "strong"}, "direction": {"old": "unlikely", "new": "mixed"}},
                             "passages_added": [{"page": 3, "quote": "Poorer naming was associated with damage.", "supports": "statistics"}]},
                            "alex", True, state)
        self.assertIn("strength", msg)
        self.assertIn("stale: direction", msg)
        fm, _ = PI.parse_markdown(self.draft)
        f = fm["findings"][0]
        self.assertEqual(f["strength"], "strong")
        self.assertEqual(f["direction"], "likely")                       # stale edit not applied
        self.assertEqual(len(f["source_passages"]), 2)
        self.assertEqual(f["edits"][0], {"by": "human:alex", "date": "2026-11-05", "fields": ["source_passages", "strength"], "via": "portal"})
        msg = PI.apply_mark({"id": rel, "page": 3, "quote": "Our findings replicate earlier reports.", "note": "x", "submitted": "2026-11-05"}, "alex", True, state)
        self.assertIn("mark m1", msg)
        self.assertIn("already present", PI.apply_mark({"id": rel, "page": 3, "quote": "Our findings replicate earlier reports."}, "alex", True, state))
        PI.apply_comment({"id": rel, "finding": "f1", "text": "check the threshold", "submitted": "2026-11-05"}, "alex", True, state)
        fm, _ = PI.parse_markdown(self.draft)
        self.assertEqual(fm["reviewer_marks"][0]["status"], "pending")
        self.assertEqual(fm["findings"][0]["portal_comments"][0]["by"], "human:alex")
        # a non-approver's approve is an opinion; an approver's approve would promote, but pending marks block it
        msg = PI.apply_verdict({"id": rel, "verdict": "approve", "rationale": "fine", "submitted": "2026-11-05",
                                "per_finding": [{"id": "f1", "verdict": "agree", "supports_approval": True}]}, "alex", False, True, True, state)
        self.assertIn("opinion", msg)
        msg = PI.apply_verdict({"id": rel, "verdict": "approve", "rationale": "fine", "submitted": "2026-11-05",
                                "per_finding": [{"id": "f1", "verdict": "agree", "supports_approval": True}]}, "michele", True, True, True, state)
        self.assertIn("pending reviewer marks", msg)
        fm, _ = PI.parse_markdown(self.draft)
        self.assertEqual([r["by"] for r in fm["portal_reviews"]], ["human:alex", "human:michele"])
        self.assertEqual(fm["status"], "draft")
        self.assertIn("skip: no draft", PI.apply_edit({"id": "regions/left_angular_gyrus.md", "finding": "f1", "fields": {}}, "alex", True, state))
        self.assertIn("skip: no draft", PI.apply_edit({"id": "drafts/../README.md", "finding": "f1", "fields": {}}, "alex", True, state))

    def test_pdf_upload_lands_in_papers(self):
        PI = self.PI
        saved = (PI.PAPERS, PI.PORTAL, dict(PI.FETCH), PI.S.load_candidates)
        papers = self.tmp / "papers"; papers.mkdir()
        PI.PAPERS = papers; PI.PORTAL = self.tmp / "portal"; (PI.PORTAL / ".uploads").mkdir(parents=True)
        cands = [{"id": "C0001", "title": "A paper with a key", "key": "@Smith2020"},
                 {"id": "C0002", "title": "A paper without a key"},
                 {"id": "C0003", "title": "A duplicate", "duplicate_of": "C0001"}]
        PI.S.load_candidates = lambda *a, **k: cands
        pdf = b"%PDF-1.4\n" + b"x" * 2000
        import hashlib
        sha = hashlib.sha256(pdf).hexdigest()
        got, deleted = [], []
        def fake_get(bucket, obj, dest):
            got.append((bucket, obj)); dest.write_bytes(pdf); return None
        PI.FETCH["get"] = fake_get
        PI.FETCH["delete"] = lambda bucket, obj: deleted.append((bucket, obj)) or None
        try:
            state: dict = {"citation_keys": {"jones2019", "lee2018"}}   # as if in citations.md
            rec = {"id": "C0001", "name": "smith.pdf", "bytes": len(pdf), "sha256": sha, "bucket": "b", "object": "uploads/c0001.pdf"}
            self.assertIn("would fetch", PI.apply_pdf(rec, "alex", False, state))
            msg = PI.apply_pdf(rec, "alex", True, state)
            self.assertIn("papers/Smith2020.pdf", msg)
            self.assertEqual((papers / "Smith2020.pdf").read_bytes(), pdf)
            self.assertEqual(got, [("b", "uploads/c0001.pdf")]); self.assertEqual(deleted, [("b", "uploads/c0001.pdf")])
            # second upload for the same paper: discarded, bucket copy removed
            self.assertIn("already in papers/", PI.apply_pdf(rec, "sam", True, state)); self.assertEqual(len(deleted), 2)
            # no key → named after the candidate, linked as pdf_file
            rec2 = {"id": "C0002", "name": "Some Journal (2021).pdf", "bytes": len(pdf), "sha256": sha, "bucket": "b", "object": "uploads/c0002.pdf"}
            msg = PI.apply_pdf(rec2, "alex", True, state)
            self.assertIn("linked to C0002", msg)
            self.assertTrue((papers / "C0002_Some Journal (2021).pdf").exists())
            self.assertEqual(cands[1]["pdf_file"], "C0002_Some Journal (2021).pdf"); self.assertTrue(state["candidates_dirty"])
            # a citation key straight from a draft view; a wrong checksum; a duplicate; an unknown id
            self.assertIn("papers/Jones2019.pdf", PI.apply_pdf({"id": "@Jones2019", "name": "j.pdf", "sha256": sha, "bucket": "b", "object": "uploads/jones2019.pdf"}, "alex", True, state))
            self.assertIn("does not match", PI.apply_pdf({"id": "@Lee2018", "sha256": "0" * 64, "bucket": "b", "object": "uploads/lee2018.pdf"}, "alex", True, state))
            self.assertFalse((papers / "Lee2018.pdf").exists())
            self.assertIn("duplicate", PI.apply_pdf({"id": "C0003", "bucket": "b", "object": "x"}, "alex", True, state))
            self.assertIn("skip: no candidate", PI.apply_pdf({"id": "C0999", "bucket": "b", "object": "x"}, "alex", True, state))
            # a local (portal_dev.py) upload is copied from portal/.uploads and removed there
            local = PI.PORTAL / ".uploads" / "c0004.pdf"; local.write_bytes(pdf); local.with_suffix(".json").write_text("{}")
            cands.append({"id": "C0004", "title": "Local", "key": "@Local2022"})
            self.assertIn("papers/Local2022.pdf", PI.apply_pdf({"id": "C0004", "sha256": sha, "local_path": "portal/.uploads/c0004.pdf"}, "alex", True, state))
            self.assertFalse(local.exists()); self.assertFalse(local.with_suffix(".json").exists())
            self.assertEqual(state["pdfs_added"], 4)
        finally:
            PI.PAPERS, PI.PORTAL = saved[0], saved[1]; PI.FETCH.update(saved[2]); PI.S.load_candidates = saved[3]

    def test_run_moves_applied_records(self):
        PI = self.PI
        rel = "drafts/regions/left_angular_gyrus__TestPaper2020.md"
        (PI.INBOX / "20261105T100000Z_comment_alex_x.json").write_text(json.dumps({"kind": "comment", "id": rel, "text": "hi", "reviewer": "alex@example.org", "submitted": "2026-11-05T10:00:00Z"}), encoding="utf-8")
        (PI.INBOX / "20261105T100001Z_edit_alex_y.json").write_text(json.dumps({"kind": "edit", "id": "drafts/regions/missing.md", "finding": "f1", "fields": {}, "reviewer": "alex@example.org"}), encoding="utf-8")
        PI.run(execute=True, promote=False, only_kind=None)
        self.assertEqual([p.name for p in PI.APPLIED.glob("*.json")], ["20261105T100000Z_comment_alex_x.json"])
        self.assertEqual(len(list(PI.INBOX.glob("*.json"))), 1)       # the one that could not be applied stays
        self.assertIn("PORTAL-APPLIED", PI.LOG.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
