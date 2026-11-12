#!/usr/bin/env python3
"""
publish_portal.py — assemble (and deploy) the review portal: a private
Cloudflare Pages site where collaborators review drafts beside the annotated
PDFs, screen candidates and send their decisions back to this repository.

    python scripts/publish_portal.py --sync          # on the maintainer's machine: send changed annotated PDFs
                                                     # (and the abstracts file) to the portal's R2 bucket and
                                                     # write portal/papers.json, the index the build reads
    python scripts/publish_portal.py                 # assemble portal/dist/ (anywhere, incl. CI) and say what it holds
    python scripts/publish_portal.py --deploy        # … then `wrangler pages deploy` (needs `npx wrangler login` once)

The PDFs are not part of the deployment: they live in the R2 bucket (portal.config.json
`pdfsBucket`) under cc/ (Creative-Commons, public) and pdf/ (everything else, behind
Access), and two Pages Functions serve them from there. That is what lets CI rebuild and
deploy the portal on every push (.github/workflows/portal.yml) without the papers folder:
the build only needs portal/papers.json, which --sync writes and which is committed.

What goes where (docs/PORTAL.md):
  <bucket>/cc/<Key>_annotated.pdf        annotated PDFs of Creative-Commons papers — served on the public
                                         path (Access bypass), linked from the explorer
  <bucket>/pdf/<Key>_annotated.pdf       every other annotated PDF — served behind Cloudflare Access
                                         (allow-listed reviewers only); never in git
  <bucket>/private/abstracts.jsonl       the abstracts cache (not in git), fetched by CI for the queue
  portal/papers.json                     the index of the above: key → licence, size, sha256; source PDFs present
  portal/dist/manifest.json              which PDFs exist, their licence category, the KB commit, maintainers
  portal/dist/screening.json             candidates awaiting title/abstract or full-text screening, with
                                         their abstracts (private)
  portal/dist/export/*.json              the two exports the portal reads (approved; approved + drafts)
  portal/dist/*.html|js|css              the portal itself (portal/web/)
  portal/functions/                      Pages Functions: who is signed in, write a review to GitHub,
                                         uploads, cc/ and pdf/ from the bucket, the maintainer's Apply

Which PDFs are public follows screening/licences.yaml (screen.py licences): `cc` (the published
version is Creative Commons) is redistributable with the citation as attribution. `cc_manuscript`
means only the accepted manuscript is: the file in papers/ may well be the publisher's version, so
it stays private unless a person has confirmed that this exact file is the openly licensed copy
(`publish_portal.py --confirm-public-copy @Key --by <name>`, which records the sha256 of the
source PDF and of the annotated copy as `public_copy` in licences.yaml; changing either file later
means private again).
`free_to_read`, `rights_reserved` and `unknown` always stay private.
"""
from __future__ import annotations
from paper_paths import resolve_paper, citation_stem

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import screening as S  # noqa: E402

PORTAL = ROOT / "portal"
WEB = PORTAL / "web"
DIST = PORTAL / "dist"
PAPERS = ROOT / "papers"
INDEX = PORTAL / "papers.json"
ABSTRACTS_OBJECT = "private/abstracts.jsonl"
PUBLIC_CATEGORIES = ("cc",)                  # public whatever copy of the paper we hold
CONFIRMABLE_CATEGORIES = ("cc_manuscript",)  # public only for a confirmed file (public_copy.sha256)


def config() -> dict:
    path = PORTAL / "portal.config.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def licences(root: Path = ROOT) -> dict[str, dict]:
    path = root / "screening" / "licences.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): dict(v or {}) for k, v in (data.get("papers") or {}).items()}


def git(*args) -> str:
    try:
        done = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=20)
        return done.stdout.strip() if done.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def public_basis(key: str, rec: dict | None, papers_dir: Path) -> str | None:
    """Why the annotated PDF of `key` may be served openly, or None (private).

    `cc`: the published version is Creative Commons, so any copy may be shared. A
    `cc_manuscript` paper only when licences.yaml carries a person's confirmation for the very
    file we hold: public_copy.sha256 equal to the sha256 of papers/<Key>.pdf (the source the
    annotated copy is made from). Everything else, and any doubt, is private."""
    rec = rec or {}
    cat = rec.get("category") or "unknown"
    if cat in PUBLIC_CATEGORIES:
        return "cc"
    if cat in CONFIRMABLE_CATEGORIES and _confirmation_holds(key, rec.get("public_copy"), papers_dir):
        return "confirmed_copy"
    return None


def _person(who) -> bool:
    """human:<name> with a real name (not empty, not a model or agent tag)."""
    who = str(who or "")
    if not who.startswith("human:"):
        return False
    name = who[len("human:"):].strip()
    return bool(name) and ":" not in name and name.lower() not in ("model", "agent", "legacy", "unnamed")


def _confirmation_holds(key: str, copy, papers_dir: Path) -> bool:
    """A person's public_copy confirmation is complete and still describes both files we hold: the
    source papers/<Key>.pdf (sha256) and the annotated copy that would be published
    (annotated_sha256). Re-annotating or replacing either file voids it until confirmed again."""
    if not isinstance(copy, dict):
        return False
    if not (_person(copy.get("confirmed_by")) and str(copy.get("confirmed_on") or "").strip() and str(copy.get("version") or "").strip()):
        return False
    src = resolve_paper(papers_dir, f"{key.lstrip('@')}.pdf")
    ann = resolve_paper(papers_dir, f"{key.lstrip('@')}_annotated.pdf")
    want_src = str(copy.get("sha256") or "").lower()
    want_ann = str(copy.get("annotated_sha256") or "").lower()
    return bool(want_src and want_ann and src.is_file() and ann.is_file()
                and _sha256(src) == want_src and _sha256(ann) == want_ann)


def scan_pdfs(papers_dir: Path, lic: dict[str, dict]) -> dict[str, dict]:
    """The annotated PDFs in papers/ as index entries: key → where it is served from (cc/ or pdf/,
    see public_basis), category, size and sha256. Nothing is copied."""
    out: dict[str, dict] = {}
    if not papers_dir.is_dir():
        return out
    for pdf in sorted(papers_dir.glob("*_annotated.pdf")):
        key = "@" + citation_stem(pdf)
        rec = lic.get(key) or {}
        cat = rec.get("category") or "unknown"
        basis = public_basis(key, rec, papers_dir)
        sub = "cc" if basis else "pdf"
        out[key] = {"annotated": f"{sub}/{pdf.name}", "category": cat, "label": rec.get("label"),
                    "public": sub == "cc", "bytes": pdf.stat().st_size, "sha256": _sha256(pdf)}
        if basis:
            out[key]["public_basis"] = basis
    return out


def confirm_public_copy(key: str, by: str, version: str = "accepted manuscript", papers_dir: Path = PAPERS,
                        root: Path = ROOT, today: str | None = None) -> str:
    """Record that papers/<Key>.pdf is the openly licensed copy of a cc_manuscript paper, and that
    papers/<Key>_annotated.pdf (the file that would be published) is made from it: the person
    has opened both. Writes public_copy {sha256, annotated_sha256, version, confirmed_by,
    confirmed_on} into screening/licences.yaml; the next --sync serves it from cc/. Changing either
    file afterwards makes it private again. Returns what was done."""
    import licences as L  # noqa: WPS433
    key = key if key.startswith("@") else f"@{key}"
    by = str(by or "").strip()
    if not _person(by if by.startswith("human:") else f"human:{by}"):
        raise ValueError("--by must name a person")
    path = root / "screening" / "licences.yaml"
    papers = L.load(path)
    rec = dict(papers.get(key) or {})
    if rec.get("category") not in CONFIRMABLE_CATEGORIES:
        raise ValueError(f"{key} is {rec.get('category') or 'not in licences.yaml'}; only {', '.join(CONFIRMABLE_CATEGORIES)} papers need a confirmed copy")
    src = resolve_paper(papers_dir, f"{key.lstrip('@')}.pdf")
    ann = resolve_paper(papers_dir, f"{key.lstrip('@')}_annotated.pdf")
    for f in (src, ann):
        if not f.is_file():
            raise ValueError(f"no {f.name} in {papers_dir}: both the source and the annotated copy must be checked")
    if not str(version or "").strip():
        raise ValueError("--version must say which version the file is (e.g. accepted manuscript)")
    rec["public_copy"] = {"sha256": _sha256(src), "annotated_sha256": _sha256(ann), "version": str(version).strip(),
                          "confirmed_by": by if by.startswith("human:") else f"human:{by}",
                          "confirmed_on": today or dt.date.today().isoformat()}
    papers[key] = rec
    L.save(path, papers)
    return f"{key}: {src.name} ({rec['public_copy']['sha256'][:12]}…) confirmed as the {version} by {rec['public_copy']['confirmed_by']}"


def _rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def load_index(path: Path = INDEX) -> dict:
    if not path.exists():
        return {"papers": {}, "sources": {"keys": [], "files": []}, "fulltext": {}, "abstracts": None}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("papers", {}); data.setdefault("sources", {"keys": [], "files": []}); data.setdefault("abstracts", None)
    data.setdefault("fulltext", {})
    data.setdefault("pending_deletions", [])
    return data


def serves_publicly(entry: dict) -> bool:
    """An index entry the cc/ route may serve: public, under cc/, and public for a reason this
    version accepts (cc, or a person-confirmed copy). An index synced before cc_manuscript became
    private still says public for those; they are not served."""
    return bool(isinstance(entry, dict) and entry.get("public") and str(entry.get("annotated") or "").startswith("cc/")
                and (entry.get("category") == "cc" or entry.get("public_basis") == "confirmed_copy"))


def public_allowlist(index: dict) -> list[str]:
    """File names under cc/ the deployed portal may serve (portal/dist/public-pdfs.json). Built on
    every deploy, so revoking a paper takes effect at the next push even when deleting the R2
    object failed; an object still waiting to be deleted is never listed."""
    pending = set(index.get("pending_deletions") or [])
    return sorted(Path(v["annotated"]).name for v in (index.get("papers") or {}).values()
                  if serves_publicly(v) and v["annotated"] not in pending)


def wrangler(*args, timeout: int = 600) -> subprocess.CompletedProcess:
    return subprocess.run(["npx", "wrangler", *args], cwd=str(PORTAL), capture_output=True, text=True, timeout=timeout)


FT_STAGES = ("awaiting_ta", "unsure_ta", "awaiting_ft", "unsure_ft", "included")


def fulltext_pdfs(papers_dir: Path, annotated: dict, root: Path = ROOT) -> dict[str, Path]:
    """Candidates awaiting screening or annotation whose PDF has no annotated copy
    in the portal: {candidate id: the PDF}. The portal shows these beside the decision, from the
    private bucket (pdf/<id>_fulltext.pdf)."""
    if not papers_dir.is_dir():
        return {}
    out: dict[str, Path] = {}
    try:
        rows = S.enrich(S.load_candidates(root), S.kb_facts(root))
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠ full-text PDFs skipped: the register could not be read ({str(e)[:80]})")
        return {}
    for r in rows:
        if r.get("stage") not in FT_STAGES or (r.get("key") and r["key"] in annotated):
            continue
        for name in ([f"{str(r['key']).lstrip('@')}.pdf"] if r.get("key") else []) + ([str(r["pdf_file"])] if r.get("pdf_file") else []):
            f = resolve_paper(papers_dir, name)
            if f.is_file():
                out[r["id"]] = f
                break
    return out


def sync_pdfs(papers_dir: Path, bucket: str, dry: bool = False, index_path: Path = INDEX, put=None, delete=None,
              abstracts_path: Path | None = None, fulltext: dict[str, Path] | None = None) -> dict:
    """Mirror the annotated PDFs (and screening/abstracts.jsonl) into the R2 bucket and write the index.

    Only files whose sha256 differs from the index are uploaded; a PDF whose licence category moved
    it between cc/ and pdf/ is re-put and the old object deleted; a PDF gone from papers/ is deleted
    from the bucket. `put`/`delete` are swapped in by the tests; the defaults call wrangler."""
    put = put or (lambda obj, path, ctype: wrangler("r2", "object", "put", f"{bucket}/{obj}", "--file", str(path), "--content-type", ctype, "--remote"))
    delete = delete or (lambda obj: wrangler("r2", "object", "delete", f"{bucket}/{obj}", "--remote"))
    lic = licences()
    old = load_index(index_path)
    new = scan_pdfs(papers_dir, lic)
    ups, dels, failed = [], [], []
    # objects a previous sync could not delete: retried first, and kept until they are gone
    # (an unpublished PDF must not stay reachable because one delete call failed)
    pending: set[str] = set(old.get("pending_deletions") or [])
    attempted: set[str] = set()          # deletes tried in this run (each object at most once)

    def do_put(obj: str, path: Path, ctype: str) -> bool:
        if dry:
            print(f"  would upload {obj} ({path.stat().st_size // 1024} KB)")
            return True
        try:
            done = put(obj, path, ctype)
            ok = getattr(done, "returncode", 0) == 0
        except Exception as e:  # noqa: BLE001
            done, ok = type("Failed", (), {"stderr": str(e)})(), False
        if ok:
            pending.discard(obj)             # wanted again and now uploaded: no longer to be deleted
        print(f"  {'↑' if ok else '✗'} {obj}" + ("" if ok else f": {(getattr(done, 'stderr', '') or '').strip()[-200:]}"))
        return ok

    def do_delete(obj: str) -> bool:
        if dry:
            print(f"  would delete {obj}")
            dels.append(obj)
            return True
        attempted.add(obj)
        try:
            done = delete(obj)
            ok = getattr(done, "returncode", 0) == 0
        except Exception as e:  # noqa: BLE001
            done, ok = None, False
            print(f"  ✗ {obj}: {e}")
        if ok:
            pending.discard(obj); dels.append(obj)
        else:
            pending.add(obj)
        print(f"  {'−' if ok else '✗'} {obj}" + ("" if ok else f" (delete failed: kept in pending_deletions, retried at the next --sync)"
                                                   + (f": {(getattr(done, 'stderr', '') or '').strip()[-200:]}" if done is not None else "")))
        return ok

    def unsure(obj: str) -> bool:
        """The bucket may not hold what the index says: a delete of it failed earlier (pending)
        or happened in this run. Such an object is uploaded again, never skipped as unchanged."""
        return obj in pending or obj in dels

    for key, entry in list(new.items()):
        prev = old["papers"].get(key)
        if (prev and prev.get("sha256") == entry["sha256"] and prev.get("annotated") == entry["annotated"]
                and not unsure(entry["annotated"])):
            continue
        moved = bool(prev and prev.get("annotated") and prev["annotated"] != entry["annotated"])
        revoked = moved and str(prev["annotated"]).startswith("cc/") and not entry["public"]
        if do_put(entry["annotated"], papers_dir / Path(entry["annotated"]).name, "application/pdf"):
            ups.append(key)
            if moved:
                do_delete(prev["annotated"])
        else:
            failed.append(key)
            if revoked:
                # no longer public: take the open copy down even though the private one failed to upload
                do_delete(prev["annotated"])
                new.pop(key, None)
            elif prev:
                new[key] = prev                      # the index stays truthful: the bucket still has the old file
            else:
                new.pop(key, None)
    for key, prev in old["papers"].items():
        if key not in new and prev.get("annotated") and prev["annotated"] not in pending and prev["annotated"] not in dels:
            do_delete(prev["annotated"])
    # full-text screening: the source PDF of each candidate awaiting assessment (no annotated copy yet)
    ft_files = fulltext_pdfs(papers_dir, new) if fulltext is None else fulltext
    ft_new: dict[str, dict] = {}
    for cid, path in sorted(ft_files.items()):
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        entry = {"object": f"pdf/{cid}_fulltext.pdf", "sha256": sha, "bytes": path.stat().st_size, "file": path.name}
        prev = old["fulltext"].get(cid)
        if prev and prev.get("sha256") == sha and not unsure(entry["object"]):
            ft_new[cid] = {**prev, "file": path.name}          # renamed in papers/: same bytes, no upload
        elif do_put(entry["object"], path, "application/pdf"):
            ft_new[cid] = entry; ups.append(cid)
        else:
            failed.append(cid)
            if prev:
                ft_new[cid] = prev
    for cid, prev in old["fulltext"].items():
        if cid not in ft_new and prev.get("object") and prev["object"] not in pending and prev["object"] not in dels:
            do_delete(prev["object"])
    # deletes left over from earlier syncs, last: an object that is wanted again (and was just
    # uploaded, or failed to upload and stays pending, never served) is not deleted
    wanted = {v["annotated"] for v in new.values() if v.get("annotated")} | {v["object"] for v in ft_new.values() if v.get("object")}
    for obj in sorted(pending - wanted - attempted):
        do_delete(obj)
    abstracts = old.get("abstracts")
    abs_path = abstracts_path or (ROOT / "screening" / "abstracts.jsonl")
    if abs_path.exists():
        sha = hashlib.sha256(abs_path.read_bytes()).hexdigest()
        if not abstracts or abstracts.get("sha256") != sha:
            if do_put(ABSTRACTS_OBJECT, abs_path, "application/x-ndjson"):
                abstracts = {"object": ABSTRACTS_OBJECT, "sha256": sha, "bytes": abs_path.stat().st_size,
                             "synced": dt.datetime.now().isoformat(timespec="minutes")}
    index = {"synced": old.get("synced") if dry else dt.datetime.now().isoformat(timespec="minutes"), "bucket": bucket,
             "papers": new, "sources": source_pdfs(papers_dir), "fulltext": ft_new, "abstracts": abstracts,
             "pending_deletions": sorted(old.get("pending_deletions") or []) if dry else sorted(pending)}
    if not dry:
        tmp = index_path.with_suffix(index_path.suffix + ".tmp")
        tmp.write_text(json.dumps(index, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
        tmp.replace(index_path)                      # never a half-written index
    n_public = sum(1 for v in new.values() if v["public"])
    verb = ("to upload", "to delete") if dry else ("uploaded", "deleted")
    print(f"  bucket {bucket}: {len(ups)} {verb[0]}, {len(dels)} {verb[1]}, {len(failed)} failed · index: {n_public} public + {len(new) - n_public} private annotated PDFs, "
          f"{len(index['sources']['keys'])} source PDFs, {len(ft_new)} full texts to assess" + (" (dry run, index not written)" if dry else f" → {_rel(index_path)}"))
    if failed:
        print(f"  ⚠ not uploaded: {', '.join(failed)} — run --sync again")
    if index["pending_deletions"] and not dry:
        print(f"  ⚠ {len(index['pending_deletions'])} object(s) could not be deleted and stay in pending_deletions "
              f"(never listed as public; retried at the next --sync): {', '.join(index['pending_deletions'])}")
    return {**index, "sync_failed": failed}


def source_pdfs(papers_dir: Path) -> dict:
    """What papers/ holds besides the annotated copies: `keys` (@Key of every <Key>.pdf, so the
    portal knows the maintainer already has the paper even when it is not annotated yet) and
    `files` (the other PDF names, which screening records point to through `pdf_file`)."""
    keys, files = [], []
    try:
        cited = {k.lstrip("@").lower(): k.lstrip("@") for k in S.citation_blocks()}
    except Exception:  # noqa: BLE001
        cited = {}
    if papers_dir.is_dir():
        for pdf in sorted(papers_dir.glob("*.pdf")):
            if pdf.stem.endswith("_annotated"):
                continue
            if citation_stem(pdf).lower() in cited or re.fullmatch(r"[A-Za-z][A-Za-z'\-]*\d{4}[A-Za-z0-9]*", citation_stem(pdf)):
                keys.append("@" + cited.get(citation_stem(pdf).lower(), citation_stem(pdf)))
            else:
                files.append(pdf.name)
    return {"keys": keys, "files": files}


def screening_bundle(root: Path = ROOT, ta_limit: int = 300) -> dict:
    """Candidates a reviewer can still decide on, with abstracts, for the private site.

    Title/abstract: the next ``ta_limit`` records of the prioritised queue (SCREENING.md §4.1 —
    the same order screen_app.py uses), not the whole register. Full text: every record
    awaiting assessment."""
    sys.path.insert(0, str(root / "scripts"))
    import screen as SC  # noqa: WPS433
    abstracts = SC.load_abstracts()
    data = S.collect(root)
    searches = {s["id"]: {k: s.get(k) for k in ("id", "database", "date", "for")} for s in data["searches"]}
    rows = {r["id"]: r for r in data["candidates"]}
    ta_ids = [r["id"] for r in data["candidates"] if r["stage"] in ("awaiting_ta", "unsure_ta")]
    ft_ids = [r["id"] for r in data["candidates"] if r["stage"] in ("awaiting_ft", "unsure_ft")]
    rank_info: dict = {}
    if len(ta_ids) > ta_limit:
        try:
            candidates = S.load_candidates(root)
            order, rank_info = SC.rank_order(candidates, ta_ids, abstracts, S.load_strategies())
            ta_ids = [i for i in order if i in rows][:ta_limit]
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠ prioritised ranking failed ({str(e)[:80]}); taking the first {ta_limit} by id")
            ta_ids = sorted(ta_ids)[:ta_limit]
    # Keep the ranked T/A order stable; uploads outside the capped page are appended.
    uploaded_ta = [r["id"] for r in rows.values() if r.get("pdf_uploaded_at")
                   and r["stage"] in ("awaiting_ta", "unsure_ta")]
    ta_ids = list(dict.fromkeys(ta_ids + uploaded_ta))
    ft_ids.sort(key=lambda cid: str(rows[cid].get("pdf_uploaded_at") or ""), reverse=True)
    cands = []
    for cid in ta_ids + ft_ids:
        r = rows[cid]
        cands.append({k: r.get(k) for k in ("id", "key", "doi", "pmid", "title", "year", "first_author", "authors", "journal",
                                             "stage", "for", "sources", "pdf_file", "pdf_uploaded_at", "upload_ids") if r.get(k) not in (None, "", [])}
                     | {"abstract": abstracts.get(r["id"], ""), "history": [{k: d.get(k) for k in ("stage", "decision", "reason", "by", "date") if d.get(k)}
                                                                               for d in (r.get("screening") or [])],
                        "suggestion": r.get("suggestion")})
    return {"built": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"), "candidates": cands, "searches": searches,
            "reasons": data["reasons"], "stageLabels": data["stageLabels"],
            "queue": {"title_abstract": len(ta_ids), "title_abstract_total": sum(1 for r in rows.values() if r["stage"] in ("awaiting_ta", "unsure_ta")),
                      "full_text": len(ft_ids), "ranked": bool(rank_info)}}


def _export_version(path: Path) -> dict:
    try:
        return (json.loads(path.read_text(encoding="utf-8")) or {}).get("version") or {}
    except (OSError, ValueError):
        return {}


def export_is_current(ver: dict, root: Path = ROOT) -> bool:
    """The drafts export was made from the files as they are now: its contentDigest equals the
    digest export_webapp.version computes for the same statuses from the current tree."""
    want = ver.get("contentDigest")
    statuses = tuple(ver.get("statuses") or ())
    if not want or not statuses:
        return False
    try:
        import types
        import export_webapp as EW  # noqa: WPS433
        # version() reads only the files for the digest; the counts come from a stub
        stub = types.SimpleNamespace(include=statuses, findings={}, regions=[], impairments=[], therapies=[], predictors=[])
        return EW.version(root, stub).get("contentDigest") == want
    except Exception:  # noqa: BLE001
        return False


def maintainers(root: Path = ROOT) -> list[str]:
    """Emails marked `maintainer: true` in portal/reviewers.yaml: they see the Apply button."""
    path = root / "portal" / "reviewers.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return sorted(str(k).lower() for k, v in (data.get("reviewers") or {}).items() if (v or {}).get("maintainer"))


def build(ta_limit: int = 300, index_path: Path = INDEX) -> dict:
    DIST.mkdir(parents=True, exist_ok=True)
    index = load_index(index_path)
    pdfs = {k: {**v, "sha256": str(v.get("sha256") or "")[:16]} for k, v in index["papers"].items()}
    sources = index["sources"]
    n_public = sum(1 for v in pdfs.values() if v["public"])
    if not index_path.exists():
        print(f"  ⚠ {_rel(index_path)} missing — run `publish_portal.py --sync` on the maintainer's machine; no PDFs listed")
    print(f"  PDFs (from the index, served from the bucket): {n_public} public (Creative Commons), {len(pdfs) - n_public} private")
    for sub in ("cc", "pdf"):                       # left by builds that copied the PDFs into dist/
        if (DIST / sub).is_dir():
            shutil.rmtree(DIST / sub)
    # the portal itself
    for f in WEB.iterdir():
        if f.is_file():
            shutil.copy2(f, DIST / f.name)
    shutil.copy2(ROOT / "explorer" / "styles.css", DIST / "explorer-styles.css")
    # The welcome page (web/welcome/): the one part of the portal that is open without a
    # sign-in. It may only load what sits under /welcome/, so it gets its own copy of the styles.
    if (DIST / "welcome").is_dir():
        shutil.rmtree(DIST / "welcome")
    shutil.copytree(WEB / "welcome", DIST / "welcome")
    shutil.copy2(ROOT / "explorer" / "styles.css", DIST / "welcome" / "styles.css")
    # A new build must not run against a browser's cached copy of the old page code: the
    # page asks for its script and stylesheets under this build's stamp.
    stamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    page = DIST / "index.html"
    html = page.read_text(encoding="utf-8")
    for name in ("app.js", "portal.css", "explorer-styles.css"):
        html = re.sub(rf'((?:src|href)="{re.escape(name)})(?:\?v=\d+)?"', rf'\1?v={stamp}"', html)
    page.write_text(html, encoding="utf-8")
    welcome = DIST / "welcome" / "index.html"
    welcome.write_text(re.sub(r'(href="styles\.css)(?:\?v=\d+)?"', rf'\1?v={stamp}"', welcome.read_text(encoding="utf-8")), encoding="utf-8")
    # pdf.js, vendored from portal/node_modules (npm install in portal/ once)
    build_dir = PORTAL / "node_modules" / "pdfjs-dist" / "build"
    (DIST / "vendor").mkdir(exist_ok=True)
    if build_dir.is_dir():
        for name in ("pdf.min.mjs", "pdf.worker.min.mjs"):
            shutil.copy2(build_dir / name, DIST / "vendor" / name)
    else:
        print("  ⚠ portal/node_modules/pdfjs-dist missing — run `npm install` in portal/ (the PDF pane needs it)")
    # exports (the portal reads its own copies, so it does not depend on GitHub Pages being up)
    (DIST / "export").mkdir(exist_ok=True)
    for name in ("stroke-aphasia-kb.json", "stroke-aphasia-kb-drafts.json"):
        src = ROOT / "export" / name
        if src.exists():
            shutil.copy2(src, DIST / "export" / name)
        else:
            print(f"  ⚠ export/{name} missing — run scripts/export_webapp.py first")
    # screening queue with abstracts (private)
    sb = screening_bundle(ta_limit=ta_limit)
    (DIST / "screening.json").write_text(json.dumps(sb, ensure_ascii=False, default=str), encoding="utf-8")
    # Full identity index: matching cannot be restricted to the visible ranked queue.
    identity_index = [{k: c.get(k) for k in ("id", "key", "title", "doi", "stage", "duplicate_of", "upload_ids") if c.get(k)} for c in S.collect(ROOT)["candidates"]]
    (DIST / "screening-index.json").write_text(json.dumps({"candidates": identity_index}, ensure_ascii=False), encoding="utf-8")
    q = sb["queue"]
    print(f"  screening.json: {q['title_abstract']} of {q['title_abstract_total']} title/abstract records "
          f"({'prioritised order' if q['ranked'] else 'all'}) + {q['full_text']} full-text records")
    cfg = config()
    drafts_export = _export_version(DIST / "export" / "stroke-aphasia-kb-drafts.json")
    export_file = DIST / "export" / "stroke-aphasia-kb-drafts.json"
    export_sha = _sha256(export_file) if export_file.exists() else None
    manifest = {"built": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"), "kbCommit": git("rev-parse", "--short", "HEAD"),
                "buildId": f"{stamp}-{git('rev-parse', '--short', 'HEAD') or 'nogit'}", "exportDigest": drafts_export.get("contentDigest"),
                "exportSha256": export_sha,
                "kbDate": git("log", "-1", "--format=%cs"), "papers": pdfs, "sources": sources, "config": cfg,
                "fulltext": {k: {"object": v.get("object"), "bytes": v.get("bytes")} for k, v in (index.get("fulltext") or {}).items()},
                "pdfsSynced": index.get("synced"), "maintainers": maintainers(),
                "counts": {"public": n_public, "private": len(pdfs) - n_public, "candidates": len(sb["candidates"]),
                           "sources": sum(1 for k in sources["keys"] if k not in pdfs), "sourceFiles": len(sources["files"])}}
    (DIST / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    # what each draft is, as built: a verdict carries its digest so the import can tell whether
    # the draft changed after the reviewer opened it (review_binding.py, REVIEW.md #10)
    # Only against an export made from these very files: a stale export would show reviewers one
    # version and bind their verdicts to another. If they differ, no bindings: verdicts are refused.
    import review_binding as RB  # noqa: WPS433
    fresh = export_is_current(drafts_export)
    bindings = RB.drafts_bindings(ROOT) if fresh else {}
    (DIST / "drafts.json").write_text(json.dumps({"built": manifest["built"], "kbCommit": manifest["kbCommit"], "buildId": manifest["buildId"],
                                                  "exportDigest": manifest["exportDigest"] if fresh else None,
                                                  "exportSha256": export_sha if fresh else None, "drafts": bindings},
                                                 ensure_ascii=False, sort_keys=True), encoding="utf-8")
    if fresh:
        print(f"  drafts.json: review bindings for {len(bindings)} draft(s)")
    else:
        print("  ⚠ drafts.json: the drafts export is not from the current files (run scripts/export_webapp.py --include "
              "approved,in_review,draft first): no review bindings, the portal will refuse draft verdicts")
    # what cc/ may serve (portal/lib/pdfs.js checks every public request against it)
    allow = public_allowlist(index)
    (DIST / "public-pdfs.json").write_text(json.dumps({"built": manifest["built"], "files": allow}, indent=1), encoding="utf-8")
    print(f"  public-pdfs.json: {len(allow)} annotated PDF(s) the open cc/ path may serve")
    (DIST / "_headers").write_text("/*\n  X-Robots-Tag: noindex\n  Cache-Control: no-cache\n", encoding="utf-8")
    return manifest


def deploy(project: str, branch: str) -> int:
    cmd = ["npx", "wrangler", "pages", "deploy", "dist", "--project-name", project, "--branch", branch, "--commit-dirty=true"]
    print("  → " + " ".join(cmd))
    return subprocess.call(cmd, cwd=str(PORTAL))


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--sync", action="store_true", help="send changed annotated PDFs and the abstracts file to the R2 bucket and write portal/papers.json (maintainer's machine)")
    ap.add_argument("--dry-run", action="store_true", help="with --sync: say what would be uploaded or deleted")
    ap.add_argument("--papers-dir", type=Path, default=PAPERS, help="with --sync: the papers folder (default papers/)")
    ap.add_argument("--bucket", default=None, help="with --sync: the R2 bucket (default: pdfsBucket in portal/portal.config.json)")
    ap.add_argument("--deploy", action="store_true", help="run wrangler pages deploy after assembling")
    ap.add_argument("--project", default=None, help="Cloudflare Pages project name (default: portal.config.json)")
    ap.add_argument("--branch", default="main", help="Pages branch to deploy to (main = production)")
    ap.add_argument("--ta-limit", type=int, default=300, help="title/abstract records offered, in prioritised order (default 300)")
    ap.add_argument("--confirm-public-copy", metavar="@KEY", help="a cc_manuscript paper: record that papers/<Key>.pdf is the openly licensed copy and <Key>_annotated.pdf is made from it — open both first (needs --by)")
    ap.add_argument("--by", help="with --confirm-public-copy: the person who checked the file")
    ap.add_argument("--version", default="accepted manuscript", help="with --confirm-public-copy: which version the file is")
    args = ap.parse_args(argv)
    if args.confirm_public_copy:
        try:
            print("  " + confirm_public_copy(args.confirm_public_copy, args.by or "", args.version, papers_dir=args.papers_dir))
        except ValueError as e:
            print(f"  ✗ {e}")
            return 1
        print("  Run --sync to serve it from cc/, then commit screening/licences.yaml and portal/papers.json.")
        return 0
    if args.sync:
        bucket = args.bucket or config().get("pdfsBucket")
        if not bucket:
            print("  no bucket: pass --bucket or set pdfsBucket in portal/portal.config.json")
            return 1
        print(f"Syncing annotated PDFs from {args.papers_dir} to the R2 bucket {bucket}")
        result = sync_pdfs(args.papers_dir, bucket, dry=args.dry_run)
        incomplete = bool(result.get("sync_failed")) or (bool(result.get("pending_deletions")) and not args.dry_run)
        if not args.deploy:
            print("  Commit portal/papers.json and push: the portal rebuilds from the push (or build here: publish_portal.py --deploy).")
            return 1 if incomplete else 0
    else:
        incomplete = False
    print(f"Assembling the review portal in {DIST.relative_to(ROOT)}/")
    manifest = build(args.ta_limit)
    print(f"  KB {manifest.get('kbCommit') or '?'} · {len(manifest.get('papers') or {})} annotated PDFs · built {manifest.get('built')}")
    if args.deploy:
        cfg = manifest.get("config") or {}
        project = args.project or cfg.get("pagesProject")
        if not project:
            print("  no project name: pass --project or set pagesProject in portal/portal.config.json")
            return 1
        rc = deploy(project, args.branch)
        if incomplete:
            print("  ⚠ deployed, but the sync was incomplete (see above): exit 1")
        return rc or (1 if incomplete else 0)
    print("  Deploy with: python scripts/publish_portal.py --deploy   (or: cd portal && npx wrangler pages deploy dist)")
    return 1 if incomplete else 0


if __name__ == "__main__":
    sys.exit(_cli())
