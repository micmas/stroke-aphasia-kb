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
        self.saved = {k: getattr(PI, k) for k in ("ROOT", "PAPERS", "PORTAL", "INBOX", "APPLIED", "LOG", "REVIEWERS", "LEDGER")}
        self.saved_fetch = dict(PI.FETCH)
        self.saved_load = PI.S.load_candidates
        PI.ROOT = self.root
        PI.PAPERS = self.root / "papers"
        PI.PORTAL = self.root / "portal"
        PI.INBOX = self.root / "logs" / "portal" / "inbox"
        PI.APPLIED = self.root / "logs" / "portal" / "applied"
        PI.LOG = self.root / "logs" / "extraction_log.md"
        PI.REVIEWERS = self.root / "portal" / "reviewers.yaml"
        PI.LEDGER = self.root / "logs" / "portal" / "ledger.jsonl"
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
        h = lambda name: hashlib.sha256((self.papers / name).read_bytes()).hexdigest()  # noqa: E731
        full = {"sha256": h("Manu2021.pdf"), "annotated_sha256": h("Manu2021_annotated.pdf"), "version": "accepted manuscript",
                "confirmed_by": "human:michele", "confirmed_on": "2026-11-11"}
        public = lambda copy: self.PP.scan_pdfs(self.papers, self.lic({"public_copy": copy}))["@Manu2021"]["public"]  # noqa: E731
        idx = self.PP.scan_pdfs(self.papers, self.lic({"public_copy": full}))
        self.assertTrue(idx["@Manu2021"]["public"]); self.assertEqual(idx["@Manu2021"]["public_basis"], "confirmed_copy")
        # every part of the confirmation is required
        for missing in ("sha256", "annotated_sha256", "version", "confirmed_by", "confirmed_on"):
            self.assertFalse(public({k: v for k, v in full.items() if k != missing}), missing)
        for who in ("human:", "human: ", "michele", "model:gemma4:31b", "human:model", "human:a:b"):
            self.assertFalse(public({**full, "confirmed_by": who}), who)
        # the annotated copy is re-made (or still holds an older publisher copy): private again
        (self.papers / "Manu2021_annotated.pdf").write_bytes(b"%PDF-annotated from another file")
        self.assertFalse(public(full))
        (self.papers / "Manu2021_annotated.pdf").write_bytes(b"%PDF-annotated Manu2021")
        self.assertTrue(public(full))
        # someone replaces papers/Manu2021.pdf with the publisher's version: private again
        (self.papers / "Manu2021.pdf").write_bytes(b"%PDF-publisher version")
        self.assertFalse(public(full))
        sha = full["sha256"]
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
        self.assertEqual(rec["public_copy"]["annotated_sha256"], hashlib.sha256((self.papers / "Manu2021_annotated.pdf").read_bytes()).hexdigest())
        self.assertTrue(self.PP.scan_pdfs(self.papers, L.load(path))["@Manu2021"]["public"])
        # screen.py licences --refresh writes a fresh record from metadata: the confirmation stays
        fresh = L.load(path); fresh["@Manu2021"] = {"category": "cc_manuscript", "label": "CC BY 4.0", "source": "crossref"}
        L.save(path, fresh)
        self.assertEqual(L.load(path)["@Manu2021"]["public_copy"]["sha256"], rec["public_copy"]["sha256"])
        with self.assertRaises(ValueError):
            self.PP.confirm_public_copy("Manu2021", "michele", version=" ", papers_dir=self.papers, root=self.root)
        (self.papers / "Manu2021_annotated.pdf").unlink()
        with self.assertRaises(ValueError):                       # the published file must exist to be checked
            self.PP.confirm_public_copy("Manu2021", "michele", papers_dir=self.papers, root=self.root)
        (self.papers / "Manu2021_annotated.pdf").write_bytes(b"%PDF-annotated Manu2021")
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


class Revocation(unittest.TestCase):
    """Finding 9: an object that could not be deleted is retried until it is gone, and is never
    on the list of what the open cc/ path may serve."""

    def setUp(self):
        import publish_portal as PP
        self.PP = PP
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.papers = self.root / "papers"; self.papers.mkdir()
        (self.papers / "X_annotated.pdf").write_bytes(b"%PDF-x annotated")
        self.index = self.root / "papers.json"
        self.saved_lic = PP.licences
        self.lic = {"@X": {"category": "cc"}}
        PP.licences = lambda *a, **k: self.lic
        self.puts, self.deletes, self.fail_deletes, self.fail_puts = [], [], 0, 0
        self.bucket: dict[str, bytes] = {}

    def tearDown(self):
        self.PP.licences = self.saved_lic
        self.tmp.cleanup()

    def put(self, obj, path, ctype):
        self.puts.append(obj)
        if self.fail_puts:
            self.fail_puts -= 1
            return type("R", (), {"returncode": 1, "stderr": "boom"})()
        self.bucket[obj] = Path(path).read_bytes()
        return type("R", (), {"returncode": 0})()

    def delete(self, obj):
        self.deletes.append(obj)
        if self.fail_deletes:
            self.fail_deletes -= 1
            return type("R", (), {"returncode": 1, "stderr": "R2 unavailable"})()
        self.bucket.pop(obj, None)
        return type("R", (), {"returncode": 0})()

    def assert_consistent(self, out):
        """Everything the index points to is in the bucket, and cc/ holds nothing the build would not list."""
        for v in out["papers"].values():
            self.assertIn(v["annotated"], self.bucket, v)
        listed = set(self.PP.public_allowlist(out))
        for obj in self.bucket:
            if obj.startswith("cc/") and Path(obj).name not in listed:
                self.assertIn(obj, out["pending_deletions"], obj)

    def sync(self):
        return self.PP.sync_pdfs(self.papers, "b", index_path=self.index, put=self.put, delete=self.delete,
                                 fulltext={}, abstracts_path=self.root / "absent")

    def test_failed_deletion_is_retried_and_never_listed(self):
        first = self.sync()
        self.assertEqual(self.PP.public_allowlist(first), ["X_annotated.pdf"])
        self.lic = {"@X": {"category": "rights_reserved"}}       # licence corrected: no longer public
        self.fail_deletes = 1
        second = self.sync()
        self.assertEqual(second["papers"]["@X"]["annotated"], "pdf/X_annotated.pdf")
        self.assertEqual(second["pending_deletions"], ["cc/X_annotated.pdf"])
        self.assertEqual(json.loads(self.index.read_text())["pending_deletions"], ["cc/X_annotated.pdf"])
        self.assertEqual(self.PP.public_allowlist(second), [])
        third = self.sync()                                         # nothing else changed: the delete is retried
        self.assertEqual(self.deletes, ["cc/X_annotated.pdf", "cc/X_annotated.pdf"])
        self.assertEqual(third["pending_deletions"], [])

    def test_revoked_copy_comes_down_even_if_the_private_upload_fails(self):
        self.sync()
        self.lic = {"@X": {"category": "rights_reserved"}}
        self.fail_puts = 1
        out = self.sync()
        self.assertIn("cc/X_annotated.pdf", self.deletes)
        self.assertNotIn("@X", out["papers"])                      # not available until the next sync uploads pdf/
        self.assertEqual(out["sync_failed"], ["@X"])
        self.assertEqual(self.PP.public_allowlist(out), [])
        again = self.sync()
        self.assertEqual(again["papers"]["@X"]["annotated"], "pdf/X_annotated.pdf")

    def test_a_raising_delete_is_a_failure_not_a_crash(self):
        self.sync()
        self.lic = {"@X": {"category": "rights_reserved"}}
        def boom(obj):
            raise OSError("wrangler missing")
        out = self.PP.sync_pdfs(self.papers, "b", index_path=self.index, put=self.put, delete=boom, fulltext={},
                                abstracts_path=self.root / "absent")
        self.assertEqual(out["pending_deletions"], ["cc/X_annotated.pdf"])

    def test_revoke_fail_then_reauthorise(self):
        self.sync()
        self.lic = {"@X": {"category": "rights_reserved"}}
        self.fail_deletes = 1
        out = self.sync()                                   # cc/X could not be deleted: pending
        self.assertEqual(out["pending_deletions"], ["cc/X_annotated.pdf"]); self.assert_consistent(out)
        self.lic = {"@X": {"category": "cc"}}               # authorised again
        out = self.sync()
        self.assertEqual(out["papers"]["@X"]["annotated"], "cc/X_annotated.pdf")
        self.assertEqual(out["pending_deletions"], [])
        self.assertIn("cc/X_annotated.pdf", self.bucket)    # re-uploaded, not deleted after the fact
        self.assertNotIn("pdf/X_annotated.pdf", self.bucket)
        self.assertEqual(self.PP.public_allowlist(out), ["X_annotated.pdf"]); self.assert_consistent(out)

    def test_revoke_fail_reauthorise_with_upload_failure(self):
        self.sync()
        self.lic = {"@X": {"category": "rights_reserved"}}
        self.fail_deletes = 1
        self.sync()
        self.lic = {"@X": {"category": "cc"}}
        self.fail_puts = 1                                  # the upload to cc/ fails this time
        out = self.sync()
        self.assertEqual(out["sync_failed"], ["@X"])
        self.assertEqual(self.PP.public_allowlist(out), []) # nothing public while the state is uncertain
        self.assert_consistent(out)
        out = self.sync()                                   # next sync: uploaded, served
        self.assertEqual(out["papers"]["@X"]["annotated"], "cc/X_annotated.pdf")
        self.assertEqual(out["pending_deletions"], [])
        self.assertEqual(self.PP.public_allowlist(out), ["X_annotated.pdf"]); self.assert_consistent(out)

    def test_pending_object_wanted_unchanged_is_uploaded_not_deleted(self):
        first = self.sync()                                 # cc/X in the bucket, index cc/X with its sha
        data = json.loads(self.index.read_text()); data["pending_deletions"] = ["cc/X_annotated.pdf"]
        self.index.write_text(json.dumps(data))             # an earlier delete of the same object had failed
        self.bucket.pop("cc/X_annotated.pdf")               # … or did happen: the bucket's state is unknown
        out = self.sync()
        self.assertIn("cc/X_annotated.pdf", self.bucket)
        self.assertNotIn("cc/X_annotated.pdf", self.deletes)
        self.assertEqual(out["pending_deletions"], [])
        self.assertEqual(first["papers"]["@X"]["sha256"], out["papers"]["@X"]["sha256"]); self.assert_consistent(out)

    def test_sync_with_deploy_reports_an_incomplete_sync(self):
        saved = {k: getattr(self.PP, k) for k in ("sync_pdfs", "build", "deploy", "config")}
        try:
            self.PP.config = lambda: {"pdfsBucket": "b", "pagesProject": "p"}
            self.PP.build = lambda *a, **k: {"config": {"pagesProject": "p"}, "papers": {}}
            self.PP.deploy = lambda *a, **k: 0
            self.PP.sync_pdfs = lambda *a, **k: {"sync_failed": [], "pending_deletions": ["cc/X_annotated.pdf"]}
            self.assertEqual(self.PP._cli(["--sync", "--deploy"]), 1)
            self.assertEqual(self.PP._cli(["--sync"]), 1)
            self.PP.sync_pdfs = lambda *a, **k: {"sync_failed": [], "pending_deletions": []}
            self.assertEqual(self.PP._cli(["--sync", "--deploy"]), 0)
            self.PP.deploy = lambda *a, **k: 3
            self.assertEqual(self.PP._cli(["--sync", "--deploy"]), 3)
        finally:
            for k, v in saved.items():
                setattr(self.PP, k, v)

    def test_allowlist_ignores_stale_and_unconfirmed_entries(self):
        idx = {"papers": {"@A": {"annotated": "cc/A_annotated.pdf", "public": True, "category": "cc"},
                          "@B": {"annotated": "cc/B_annotated.pdf", "public": True, "category": "cc_manuscript"},
                          "@C": {"annotated": "cc/C_annotated.pdf", "public": True, "category": "cc_manuscript", "public_basis": "confirmed_copy"},
                          "@D": {"annotated": "pdf/D_annotated.pdf", "public": False, "category": "rights_reserved"},
                          "@E": {"annotated": "cc/E_annotated.pdf", "public": True, "category": "cc"}},
               "pending_deletions": ["cc/E_annotated.pdf"]}
        self.assertEqual(self.PP.public_allowlist(idx), ["A_annotated.pdf", "C_annotated.pdf"])


DRAFT = """---
schema_version: 2.8
id: left_angular_gyrus
name: Left angular gyrus
kind: atlas
status: draft
created_by: agent:test
created_on: 2026-11-05
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
- id: f2
  target: semantic_memory
  target_kind: impairment
  claim: Angular gyrus damage is associated with poorer semantic judgement.
  direction: likely
  relationship: causal
  citation: '@TestPaper2020'
  method: VLSM
  strength: weak
  source_passages:
  - {section: Results, page: 4, quote: Semantic judgement was poorer after angular gyrus damage., supports: claim}
---
Test draft.
"""
REL = "drafts/regions/left_angular_gyrus__TestPaper2020.md"


class _FakeAutoReview:
    """Stands in for auto_review in sys.modules: records the calls, can be told to raise."""

    class Verdict:
        APPROVE = "auto_approve"
        REJECT = "auto_reject"

    def __init__(self):
        self.calls, self.raise_next, self.result = [], 0, "auto_approve"

    def apply_manual_verdict(self, path, **kw):
        self.calls.append((Path(path).name, kw.get("verdict_override"), kw.get("reviewer")))
        if self.raise_next:
            self.raise_next -= 1
            raise RuntimeError("promote.py refused: transient")
        return (self.result if kw.get("verdict_override") == "approve" else "auto_reject"), []


class ReviewBinding(unittest.TestCase):
    """Finding 10 (content binding) and finding 20 (outcomes, replay)."""

    def setUp(self):
        import review_binding as RB
        self.RB = RB
        self.P = _Patched(self).__enter__()
        self.draft = PI.ROOT / REL
        self.draft.parent.mkdir(parents=True)
        self.draft.write_text(DRAFT, encoding="utf-8")
        import yaml
        PI.REVIEWERS.write_text(yaml.safe_dump({"reviewers": {"m@uq.edu.au": {"name": "michele", "approver": True},
                                                               "alex@example.org": {"name": "alex"}}}), encoding="utf-8")
        self.fake = _FakeAutoReview()
        self.saved_ar = sys.modules.get("auto_review")
        sys.modules["auto_review"] = self.fake
        self.seq = 0

    def tearDown(self):
        if self.saved_ar is not None:
            sys.modules["auto_review"] = self.saved_ar
        else:
            sys.modules.pop("auto_review", None)
        self.P.__exit__(None, None, None)

    def fm(self):
        return PI.parse_markdown(self.draft)[0]

    def seen(self):
        fm = self.fm()
        return {"draft_digest": self.RB.review_digest(fm), "finding_ids": self.RB.finding_ids(fm)}

    def put(self, kind, who="m@uq.edu.au", submitted="2026-11-11T01:00:00.000Z", stamp="20261111T010000Z", **body):
        self.seq += 1
        name = f"{stamp}-{self.seq:02d}_{kind}_{who.split('@')[0]}_x.json"
        rec = {"kind": kind, "id": REL, "reviewer": who, "submitted": submitted, "portal": 1, **body}
        (PI.INBOX / name).write_text(json.dumps(rec), encoding="utf-8")
        return name

    def approve(self, seen, **kw):
        return dict(verdict="approve", rationale="checked", per_finding=[{"id": "f1", "verdict": "agree"}, {"id": "f2", "verdict": "agree"}], **seen, **kw)

    def outcome(self, name):
        return json.loads((PI.APPLIED / name).read_text())["_outcome"]["status"]

    def test_current_approval_is_promoted(self):
        n = self.put("verdict", **self.approve(self.seen()))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.fake.calls, [(self.draft.name, "approve", "human:michele")])
        self.assertEqual(self.outcome(n), "applied")

    def test_changed_draft_makes_the_verdict_stale(self):
        seen = self.seen()
        self.draft.write_text(DRAFT.replace("strength: moderate", "strength: strong"), encoding="utf-8")   # changed after the build
        n = self.put("verdict", **self.approve(seen))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.fake.calls, [])
        self.assertEqual(self.outcome(n), "stale")
        rev = self.fm()["portal_reviews"][0]
        self.assertIn("changed after the reviewer opened it", rev["stale"])
        self.assertEqual(rev["reviewed_digest"], seen["draft_digest"])

    def test_unbound_or_wrong_findings_are_stale(self):
        seen = self.seen()
        a = self.put("verdict", **self.approve({}))                                     # an old client: no digest
        b = self.put("verdict", **self.approve({**seen, "finding_ids": ["f1"]}))        # saw other findings
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.fake.calls, [])
        self.assertEqual((self.outcome(a), self.outcome(b)), ("stale", "stale"))

    def test_own_edit_in_the_same_send_then_approve(self):
        seen = self.seen()                                    # the reviewer saw the draft before their edit
        n_v = self.put("verdict", **self.approve(seen))        # the portal numbers the verdict 01 …
        n_e = self.put("edit", finding="f1", fields={"strength": {"old": "moderate", "new": "strong"}})   # … and the edit 02
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.fm()["findings"][0]["strength"], "strong")      # the edit was applied first
        self.assertEqual(self.fake.calls, [(self.draft.name, "approve", "human:michele")])
        self.assertEqual((self.outcome(n_e), self.outcome(n_v)), ("applied", "applied"))

    def test_someone_elses_change_is_not_exempt(self):
        seen = self.seen()
        self.put("mark", who="alex@example.org", submitted="2026-11-11T00:59:00.000Z", stamp="20261111T005900Z",
                 page=2, quote="Another passage.", note="")
        v = self.put("verdict", **self.approve(seen))
        # a later send by the same approver, carrying the old digest: not the same send either
        e = self.put("edit", submitted="2026-11-11T02:00:00.000Z", stamp="20261111T020000Z", finding="f2",
                     fields={"strength": {"old": "weak", "new": "moderate"}})
        v2 = self.put("verdict", submitted="2026-11-11T03:00:00.000Z", stamp="20261111T030000Z", **self.approve(seen))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.fake.calls, [])
        self.assertEqual((self.outcome(v), self.outcome(v2), self.outcome(e)), ("stale", "stale", "applied"))

    def test_approval_must_cover_every_finding_and_obligations(self):
        part = self.put("verdict", **dict(self.approve(self.seen()), per_finding=[{"id": "f1", "verdict": "agree"}]))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.outcome(part), "blocked")
        text = DRAFT.replace("findings:\n", "reviewer_marks:\n- {id: m1, page: 2, quote: q, status: unresolved}\nfindings:\n", 1)
        self.draft.write_text(text, encoding="utf-8")
        marked = self.put("verdict", stamp="20261111T040000Z", submitted="2026-11-11T04:00:00.000Z", **self.approve(self.seen()))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.outcome(marked), "blocked")
        self.assertEqual(self.fake.calls, [])
        # the marks are part of what was reviewed: resolving one after the review makes the review stale
        old = self.seen()
        self.draft.write_text(text.replace("status: unresolved", "status: done"), encoding="utf-8")
        late = self.put("verdict", stamp="20261111T050000Z", submitted="2026-11-11T05:00:00.000Z", **self.approve(old))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.outcome(late), "stale")

    def test_failed_promotion_stays_in_the_inbox_and_is_not_duplicated(self):
        self.fake.raise_next = 1
        n = self.put("verdict", **self.approve(self.seen()))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertTrue((PI.INBOX / n).exists())
        self.assertFalse((PI.APPLIED / n).exists())
        self.assertEqual(len(self.fm()["portal_reviews"]), 1)
        PI.run(execute=True, promote=True, only_kind=None)                  # retried: now it works
        self.assertEqual(self.outcome(n), "applied")
        self.assertEqual(len(self.fm()["portal_reviews"]), 1)               # the opinion is not recorded twice
        self.assertEqual(len(self.fake.calls), 2)

    def test_checks_refusing_is_blocked_not_applied(self):
        self.fake.result = "auto_reject"
        n = self.put("verdict", **self.approve(self.seen()))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.outcome(n), "blocked")

    def test_replay_after_a_crash_does_not_apply_twice(self):
        e = self.put("edit", finding="f1", fields={}, passages_added=[{"page": 3, "quote": "An added passage.", "supports": "claim"}])
        PI.run(execute=True, promote=False, only_kind=None)
        self.assertEqual(len(self.fm()["findings"][0]["source_passages"]), 2)
        # the record comes back (the archive step was lost): the ledger says it was dealt with
        (PI.INBOX / e).write_text((PI.APPLIED / e).read_text())
        PI.run(execute=True, promote=False, only_kind=None)
        self.assertEqual(len(self.fm()["findings"][0]["source_passages"]), 2)
        # … and even without the ledger line, the record id in the draft stops a second application
        PI.ledger_path().unlink()
        (PI.INBOX / e).write_text((PI.APPLIED / e).read_text())
        PI.run(execute=True, promote=False, only_kind=None)
        self.assertEqual(len(self.fm()["findings"][0]["source_passages"]), 2)
        self.assertFalse((PI.INBOX / e).exists())

    def test_crash_after_promotion_is_recognised_from_the_journal(self):
        n = self.put("verdict", **self.approve(self.seen()))
        jdir = PI.ROOT / "logs" / "promotion_transactions"; jdir.mkdir(parents=True)
        self.draft.unlink()                                   # promoted, then the process died before the ledger line
        # a canonical file of the same name is not evidence; nor a journal for another record
        (PI.ROOT / "regions").mkdir(); (PI.ROOT / "regions" / "left_angular_gyrus.md").write_text("---\nid: x\n---\n")
        (jdir / "a.json").write_text(json.dumps({"draft": REL, "done": True, "record_ids": ["someone_else.json"]}))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertTrue((PI.INBOX / n).exists())               # still a skip: nothing proves this record was promoted
        (jdir / "b.json").write_text(json.dumps({"draft": REL, "done": True, "record_ids": [n]}))
        PI.run(execute=True, promote=True, only_kind=None)
        self.assertEqual(self.outcome(n), "applied")

    def test_pending_journal_is_finished_or_left_for_retry(self):
        n = self.put("verdict", **self.approve(self.seen()))
        jdir = PI.ROOT / "logs" / "promotion_transactions"; jdir.mkdir(parents=True)
        self.draft.unlink()
        (jdir / "p.json").write_text(json.dumps({"draft": REL, "done": False, "record_ids": [n]}))
        calls = []
        def recover_pending(root, draft):
            calls.append(Path(draft).relative_to(root).as_posix())
            row = json.loads((jdir / "p.json").read_text()); row["done"] = True
            (jdir / "p.json").write_text(json.dumps(row))
        fake = type(sys)("promotion_transaction"); fake.recover_pending = lambda root, draft: (_ for _ in ()).throw(OSError("disk"))
        saved = sys.modules.get("promotion_transaction"); sys.modules["promotion_transaction"] = fake
        try:
            PI.run(execute=True, promote=True, only_kind=None)
            self.assertTrue((PI.INBOX / n).exists())           # recovery failed: retried next time
            fake.recover_pending = recover_pending
            PI.run(execute=True, promote=True, only_kind=None)
        finally:
            if saved is not None:
                sys.modules["promotion_transaction"] = saved
            else:
                sys.modules.pop("promotion_transaction", None)
        self.assertEqual(calls, [REL])
        self.assertEqual(self.outcome(n), "applied")

    def test_build_bindings_cover_active_drafts_only(self):
        backup = PI.ROOT / "drafts" / "_backup" / "20261110" / "regions" / self.draft.name
        backup.parent.mkdir(parents=True); backup.write_text(DRAFT, encoding="utf-8")
        (PI.ROOT / "drafts" / "regions" / "broken__X.md").write_text("---\nfindings: [\"\"x\"]\n---\n", encoding="utf-8")
        b = self.RB.drafts_bindings(PI.ROOT)
        self.assertEqual(list(b), [REL])
        self.assertEqual(b[REL], self.RB.binding(self.fm()))
        self.assertEqual(b[REL]["findings"], ["f1", "f2"])

    def test_binding_ignores_opinions_but_not_content(self):
        fm = self.fm()
        d = self.RB.review_digest(fm)
        fm2 = dict(fm, portal_reviews=[{"by": "human:x"}], portal_comments=[{"text": "hi"}])
        fm2["findings"] = [dict(f, portal_comments=[{"text": "c"}]) for f in fm["findings"]]
        self.assertEqual(self.RB.review_digest(fm2), d)
        for change in ({"reviewer_marks": [{"id": "m1", "status": "pending"}]}, {"status": "in_review"}):
            self.assertNotEqual(self.RB.review_digest(dict(fm, **change)), d)
        fm3 = dict(fm); fm3["findings"] = [dict(fm["findings"][0], strength="strong"), fm["findings"][1]]
        self.assertNotEqual(self.RB.review_digest(fm3), d)


if __name__ == "__main__":
    unittest.main(verbosity=1)
