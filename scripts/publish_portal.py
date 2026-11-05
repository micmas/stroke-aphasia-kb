#!/usr/bin/env python3
"""
publish_portal.py — assemble (and deploy) the review portal: a private
Cloudflare Pages site where collaborators review drafts beside the annotated
PDFs, screen candidates and send their decisions back to this repository.

    python scripts/publish_portal.py                 # assemble portal/dist/ and say what it holds
    python scripts/publish_portal.py --deploy        # … then `wrangler pages deploy` (needs `npx wrangler login` once)
    python scripts/publish_portal.py --pdfs-only     # only refresh the PDF folders (after re-annotating)

What goes where (docs/PORTAL.md):
  portal/dist/cc/<Key>_annotated.pdf     annotated PDFs of Creative-Commons papers — public path (Access
                                         bypass), linked from the explorer
  portal/dist/pdf/<Key>_annotated.pdf    every other annotated PDF — behind Cloudflare Access (allow-listed
                                         reviewers only); never in git
  portal/dist/manifest.json              which PDFs exist, their licence category, the KB commit
  portal/dist/screening.json             candidates awaiting title/abstract or full-text screening, with
                                         their abstracts (private; abstracts are not in git)
  portal/dist/export/*.json              the two exports the portal reads (approved; approved + drafts)
  portal/dist/*.html|js|css              the portal itself (portal/web/)
  portal/functions/                      Pages Functions: who is signed in, write a review to GitHub

Which PDFs are public follows screening/licences.yaml (screen.py licences): categories
`cc` and `cc_manuscript` are redistributable under their licence with the citation as
attribution; `free_to_read`, `rights_reserved` and `unknown` are not and stay private.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
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
PUBLIC_CATEGORIES = ("cc", "cc_manuscript")


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


def copy_pdfs(papers_dir: Path, dist: Path, lic: dict[str, dict]) -> dict[str, dict]:
    """Annotated PDFs → dist/cc (public) or dist/pdf (private). Returns the manifest entries."""
    out: dict[str, dict] = {}
    for sub in ("cc", "pdf"):
        (dist / sub).mkdir(parents=True, exist_ok=True)
    if not papers_dir.is_dir():
        print(f"  papers/ not found at {papers_dir}; no PDFs copied")
        return out
    for pdf in sorted(papers_dir.glob("*_annotated.pdf")):
        key = "@" + pdf.stem[: -len("_annotated")]
        cat = (lic.get(key) or {}).get("category") or "unknown"
        sub = "cc" if cat in PUBLIC_CATEGORIES else "pdf"
        dest = dist / sub / pdf.name
        if not dest.exists() or dest.stat().st_mtime < pdf.stat().st_mtime or dest.stat().st_size != pdf.stat().st_size:
            shutil.copy2(pdf, dest)
        other = dist / ("pdf" if sub == "cc" else "cc") / pdf.name
        if other.exists():
            other.unlink()                         # licence category changed since the last build
        out[key] = {"annotated": f"{sub}/{pdf.name}", "category": cat, "label": (lic.get(key) or {}).get("label"),
                    "public": sub == "cc", "bytes": pdf.stat().st_size,
                    "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()[:16]}
    # drop files whose source is gone
    present = {v["annotated"] for v in out.values()}
    for sub in ("cc", "pdf"):
        for f in (dist / sub).glob("*.pdf"):
            if f"{sub}/{f.name}" not in present:
                f.unlink()
    return out


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
    cands = []
    for cid in ta_ids + ft_ids:
        r = rows[cid]
        cands.append({k: r.get(k) for k in ("id", "key", "doi", "pmid", "title", "year", "first_author", "authors", "journal",
                                             "stage", "for", "sources") if r.get(k) not in (None, "", [])}
                     | {"abstract": abstracts.get(r["id"], ""), "history": [{k: d.get(k) for k in ("stage", "decision", "reason", "by", "date") if d.get(k)}
                                                                               for d in (r.get("screening") or [])],
                        "suggestion": r.get("suggestion")})
    return {"built": dt.datetime.now().isoformat(timespec="minutes"), "candidates": cands, "searches": searches,
            "reasons": data["reasons"], "stageLabels": data["stageLabels"],
            "queue": {"title_abstract": len(ta_ids), "title_abstract_total": sum(1 for r in rows.values() if r["stage"] in ("awaiting_ta", "unsure_ta")),
                      "full_text": len(ft_ids), "ranked": bool(rank_info)}}


def build(papers_dir: Path, pdfs_only: bool = False, ta_limit: int = 300) -> dict:
    DIST.mkdir(parents=True, exist_ok=True)
    lic = licences()
    pdfs = copy_pdfs(papers_dir, DIST, lic)
    n_public = sum(1 for v in pdfs.values() if v["public"])
    print(f"  PDFs: {n_public} public (Creative Commons) in cc/, {len(pdfs) - n_public} private in pdf/")
    if pdfs_only:
        manifest_path = DIST / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        manifest["papers"] = pdfs
        manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
        return manifest
    # the portal itself
    for f in WEB.iterdir():
        if f.is_file():
            shutil.copy2(f, DIST / f.name)
    shutil.copy2(ROOT / "explorer" / "styles.css", DIST / "explorer-styles.css")
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
    q = sb["queue"]
    print(f"  screening.json: {q['title_abstract']} of {q['title_abstract_total']} title/abstract records "
          f"({'prioritised order' if q['ranked'] else 'all'}) + {q['full_text']} full-text records")
    cfg_path = PORTAL / "portal.config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8")) if cfg_path.exists() else {}
    manifest = {"built": dt.datetime.now().isoformat(timespec="minutes"), "kbCommit": git("rev-parse", "--short", "HEAD"),
                "kbDate": git("log", "-1", "--format=%cs"), "papers": pdfs, "config": cfg,
                "counts": {"public": n_public, "private": len(pdfs) - n_public, "candidates": len(sb["candidates"])}}
    (DIST / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    (DIST / "_headers").write_text("/*\n  X-Robots-Tag: noindex\n  Cache-Control: no-cache\n/cc/*\n  Cache-Control: public, max-age=86400\n",
                                   encoding="utf-8")
    return manifest


def deploy(project: str, branch: str) -> int:
    cmd = ["npx", "wrangler", "pages", "deploy", "dist", "--project-name", project, "--branch", branch, "--commit-dirty=true"]
    print("  → " + " ".join(cmd))
    return subprocess.call(cmd, cwd=str(PORTAL))


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--papers-dir", type=Path, default=PAPERS)
    ap.add_argument("--pdfs-only", action="store_true")
    ap.add_argument("--deploy", action="store_true", help="run wrangler pages deploy after assembling")
    ap.add_argument("--project", default=None, help="Cloudflare Pages project name (default: portal.config.json)")
    ap.add_argument("--branch", default="main", help="Pages branch to deploy to (main = production)")
    ap.add_argument("--ta-limit", type=int, default=300, help="title/abstract records offered, in prioritised order (default 300)")
    args = ap.parse_args(argv)
    print(f"Assembling the review portal in {DIST.relative_to(ROOT)}/")
    manifest = build(args.papers_dir, args.pdfs_only, args.ta_limit)
    print(f"  KB {manifest.get('kbCommit') or '?'} · {len(manifest.get('papers') or {})} annotated PDFs · built {manifest.get('built')}")
    if args.deploy:
        cfg = manifest.get("config") or {}
        project = args.project or cfg.get("pagesProject")
        if not project:
            print("  no project name: pass --project or set pagesProject in portal/portal.config.json")
            return 1
        return deploy(project, args.branch)
    print("  Deploy with: python scripts/publish_portal.py --deploy   (or: cd portal && npx wrangler pages deploy dist)")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
