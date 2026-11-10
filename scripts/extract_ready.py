#!/usr/bin/env python3
"""
extract_ready.py — included papers still waiting for extraction, and the one command that extracts them.

    python scripts/extract_ready.py                  # list them (dry run)
    python scripts/extract_ready.py --execute        # on the maintainer's Mac: do the whole step, then push
    python scripts/extract_ready.py --notice DIR     # CI: write the notice (DIR/body.md, comment.md, signature)

Everything else happens online: full-text screening and PDF uploads in the review portal,
citation keys in the portal-apply workflow (screen.py register), and the notice itself
(.github/workflows/extract-notice.yml opens or updates the issue "Papers ready to extract",
assigned to the maintainer, so GitHub emails it). Extraction cannot: it runs the local model
(models.yaml roles.extract, through Ollama) on the PDFs in papers/ (OneDrive, not in the
repository). This script is that one step.

--execute, in order:
  1. portal_import.py --execute --kind pdf   PDFs uploaded in the portal → papers/
     intake_papers.py --execute               every new PDF: cover sheets, OCR, checked against its
                                             record, named, registered (see intake_papers.py)
  2. screen.py register --execute            citation keys; PDFs under a download name → papers/<Key>.pdf
  3. extract.py --pdf papers/<Key>.pdf        one per paper that has its PDF (20–30 min each; annotates)
  4. publish_portal.py --sync                annotated PDFs, and the PDFs of papers awaiting full-text
                                             screening, → the portal's R2 bucket, portal/papers.json
  5. git commit (only the paths this step writes) and git push → the portal rebuilds; the drafts
     show up in its Drafts queue, and the notice closes itself once nothing is left.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import screening as S  # noqa: E402

PORTAL = "https://review.aphasia-kb.app"
REPO_DIR = "~/GITHUB/stroke-aphasia-kb"
COMMAND = f"cd {REPO_DIR} && git pull && python scripts/extract_ready.py --execute"
COMMIT_PATHS = ["drafts", "logs", "citations.md", "screening", "portal/papers.json"]
DONE_STATES = ("in_kb", "in_review", "rejected")       # drafts exist (or the paper is in the KB)


def _portal_index(root: Path) -> tuple[set[str], list[str]]:
    try:
        idx = json.loads((root / "portal" / "papers.json").read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return set(), []
    src = idx.get("sources") or {}
    keys = src.get("keys") or []
    files = src.get("files") or []
    keys = set(keys if isinstance(keys, list) else keys.keys())
    files = list(files if isinstance(files, list) else files.keys())
    return keys | {f"@{k}" for k in (idx.get("papers") or {})}, files


def _uploads_waiting(root: Path) -> set[str]:
    ids = set()
    for f in (root / "logs" / "portal" / "inbox").glob("*.json"):
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if rec.get("kind") == "pdf" and rec.get("id"):
            ids.add(str(rec["id"]))
    return ids


def fulltexts_to_send(root: Path = ROOT) -> list[dict]:
    """Candidates awaiting full-text screening whose PDF the maintainer has (portal/papers.json
    sources) but the portal cannot show yet (no annotated copy, no synced full text)."""
    try:
        idx = json.loads((root / "portal" / "papers.json").read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return []
    shown = set(idx.get("fulltext") or {})
    annotated = {f"@{k.lstrip('@')}" for k in (idx.get("papers") or {})}
    keys, files = _portal_index(root)
    out = []
    for r in S.enrich(S.load_candidates(root), S.kb_facts(root)):
        if r.get("stage") not in ("awaiting_ft", "unsure_ft") or r["id"] in shown or (r.get("key") in annotated):
            continue
        if (r.get("key") and r["key"] in keys) or any(f.startswith(f"{r['id']}_") for f in files) or (r.get("pdf_file") in files):
            out.append({"id": r["id"], "key": r.get("key"), "title": r.get("title") or "", "year": r.get("year") or ""})
    return sorted(out, key=lambda x: x["id"])


def ready(root: Path = ROOT) -> list[dict]:
    """Included papers with no drafts yet: [{id, key, title, year, doi, pdf}], where pdf is
    'yes' (in papers/), 'no' (papers/ checked, not there), 'synced' (the maintainer has it,
    per portal/papers.json), 'uploaded' (uploaded in the portal, not fetched yet) or 'missing'
    (nobody has it: upload it in the portal)."""
    candidates = S.load_candidates(root)
    facts = S.kb_facts(root)
    papers = root / "papers"
    local = papers.is_dir()
    keys, files = _portal_index(root)
    uploads = _uploads_waiting(root)
    out = []
    for r in S.enrich(candidates, facts):
        if r.get("stage") != "included" or (r.get("kb") or {}).get("state") in DONE_STATES:
            continue
        key = r.get("key")
        if local:
            have = bool((key and (papers / f"{str(key).lstrip('@')}.pdf").exists())
                        or (r.get("pdf_file") and (papers / str(r["pdf_file"])).exists()))
            pdf = "yes" if have else ("uploaded" if {r["id"], key} & uploads else "no")
        elif (key and key in keys) or any(f.startswith(f"{r['id']}_") for f in files) or r.get("pdf_file") in files:
            pdf = "synced"
        elif {r["id"], key} & uploads:
            pdf = "uploaded"
        else:
            pdf = "missing"
        out.append({"id": r["id"], "key": key, "title": r.get("title") or "", "year": r.get("year") or "",
                    "doi": S.norm_doi(r.get("doi")) if r.get("doi") else None, "pdf": pdf})
    return sorted(out, key=lambda x: x["id"])


def _row(p: dict) -> str:
    return (f"  {p['id']}  {str(p['key'] or '(no key yet)'):<26} {p['pdf']:<9} {str(p['year']):<5} "
            f"{p['title'][:70]}")


def notice(out_dir: Path, root: Path = ROOT) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    papers = ready(root)
    send = fulltexts_to_send(root)
    body, comment, sig = out_dir / "body.md", out_dir / "comment.md", out_dir / "signature"
    if not papers and not send:
        for f in (body, comment, sig):
            f.write_text("", encoding="utf-8")
        print("nothing waiting for extraction")
        return 0
    signature = "extract-ready:" + hashlib.sha256(
        "\n".join([f"{p['id']} {p['key']} {p['pdf']}" for p in papers] + [f"send {p['id']}" for p in send]).encode()).hexdigest()[:16]
    can = [p for p in papers if p["pdf"] != "missing"]
    need = [p for p in papers if p["pdf"] == "missing"]
    lines = []
    if papers:
        lines += [f"**{len(papers)} included paper{'s' if len(papers) != 1 else ''} waiting to be extracted.**", ""]
    if send:
        lines += [f"**{len(send)} paper{'s' if len(send) != 1 else ''} to assess at full text {'are' if len(send) != 1 else 'is'} on your Mac "
                  f"but not in the portal yet** ({', '.join(p['id'] for p in send)}): the same command sends "
                  f"{'them' if len(send) != 1 else 'it'} to the full-text screen.", ""]
    if can or send:
        lines += ["Run this in Terminal on your Mac (about 20–30 min per paper; leave it running):", "",
                  "```", COMMAND, "```", "",
                  "It fetches the PDFs uploaded in the portal, gives the papers their citation keys, extracts "
                  "each one with the local model, sends the annotated PDFs to the portal and pushes. The drafts "
                  f"then appear in the portal's [Drafts queue]({PORTAL}/#/drafts), and this issue closes itself "
                  "when nothing is left.", ""]
    if papers:
        lines += ["| Candidate | Key | PDF | Year | Title |", "|---|---|---|---|---|"]
    label = {"synced": "on your Mac", "uploaded": "uploaded in the portal", "missing": "**none yet**",
             "yes": "on your Mac", "no": "**none yet**"}
    for p in papers:
        title = p["title"].replace("|", "/")[:110]
        if p["doi"]:
            title = f"[{title}](https://doi.org/{p['doi']})"
        lines.append(f"| {p['id']} | {p['key'] or '—'} | {label[p['pdf']]} | {p['year']} | {title} |")
    if need:
        lines += ["", f"{len(need)} of them have no PDF anywhere yet: upload them on the portal's "
                      f"[PDFs page]({PORTAL}/#/pdfs) first (the command skips them)."]
    lines += ["", f"<!-- {signature} -->", ""]
    body.write_text("\n".join(lines), encoding="utf-8")
    comment.write_text(f"The list changed: {len(papers)} paper{'s' if len(papers) != 1 else ''} to extract "
                       f"({len(can)} with a PDF), {len(send)} full text{'s' if len(send) != 1 else ''} to send to the portal. Command, as above:\n\n```\n{COMMAND}\n```\n", encoding="utf-8")
    sig.write_text(signature, encoding="utf-8")
    print(f"{len(papers)} to extract ({len(can)} with a PDF), {len(send)} full texts to send — {signature}")
    return 0


def _run(*cmd: str) -> int:
    print(f"\n$ {' '.join(cmd)}", flush=True)
    return subprocess.run(list(cmd), cwd=ROOT).returncode


def execute(only: list[str] | None, limit: int | None, commit: bool, push: bool) -> int:
    if not (ROOT / "papers").is_dir():
        print("papers/ is not reachable here: run this on the computer that has the PDFs (the OneDrive folder).")
        return 2
    py = sys.executable
    if _run(py, "scripts/portal_import.py", "--execute", "--kind", "pdf", "--no-intake"):
        print("  ⚠ fetching the uploaded PDFs failed (wrangler login?); carrying on with the PDFs already in papers/")
    # every PDF in papers/: cover sheets, OCR, link/check/name screening PDFs, register, rename
    _run(py, "scripts/intake_papers.py", "--execute", "--no-sync")
    _run(py, "scripts/screen.py", "register", "--execute")
    papers = ready()
    if only:
        papers = [p for p in papers if p["id"] in only or str(p["key"]).lstrip("@") in {o.lstrip("@") for o in only}]
    todo = [p for p in papers if p["pdf"] == "yes" and p["key"]]
    skipped = [p for p in papers if p not in todo]
    if limit:
        todo = todo[:limit]
    print(f"\n{len(todo)} to extract" + (f"; {len(skipped)} skipped (no key or no PDF)" if skipped else ""))
    for p in skipped:
        print(_row(p))
    done, failed = [], []
    for i, p in enumerate(todo, 1):
        print(f"\n[{i}/{len(todo)}] {p['key']} — {p['title'][:80]}", flush=True)
        rc = _run(py, "scripts/extract.py", "--pdf", f"papers/{str(p['key']).lstrip('@')}.pdf")
        (failed if rc else done).append(p)
    # always: it also sends the PDFs of papers awaiting full-text screening to the portal
    if _run(py, "scripts/publish_portal.py", "--sync"):
        print("  ⚠ the PDF sync failed: run `python scripts/publish_portal.py --sync` again before pushing")
    print(f"\nExtracted {len(done)}" + (f"; failed {len(failed)}: {', '.join(str(p['key']) for p in failed)}" if failed else ""))
    if not commit:
        return 1 if failed else 0
    msg = f"Extracted {len(done)} included paper{'s' if len(done) != 1 else ''}" + (
        f": {', '.join(str(p['key']).lstrip('@') for p in done)}" if done else "")
    paths = [x for x in COMMIT_PATHS if (ROOT / x).exists()]
    subprocess.run(["git", "add", "--", *paths], cwd=ROOT)
    if subprocess.run(["git", "diff", "--cached", "--quiet", "--", *paths], cwd=ROOT).returncode == 0:
        print("nothing to commit")
        return 1 if failed else 0
    if _run("git", "commit", "-m", msg, "-m", "Made by scripts/extract_ready.py --execute.", "--", *paths):
        return 1
    if push:
        for _ in range(3):
            if not _run("git", "push"):
                print("\nPushed: the portal rebuilds in a few minutes with the new drafts.")
                break
            _run("git", "pull", "--rebase", "--autostash")
        else:
            print("  ⚠ push failed: run `git push` yourself")
            return 1
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--execute", action="store_true", help="fetch uploads, register, extract, sync, commit and push")
    ap.add_argument("--papers", nargs="*", metavar="ID_OR_KEY", help="only these (C0123 or Key)")
    ap.add_argument("--limit", type=int, help="extract at most this many")
    ap.add_argument("--no-commit", action="store_true", help="leave the changes uncommitted")
    ap.add_argument("--no-push", action="store_true", help="commit but do not push")
    ap.add_argument("--notice", type=Path, metavar="DIR", help="write the notice files for the extract-notice workflow")
    a = ap.parse_args(argv)
    if a.notice:
        return notice(a.notice)
    if a.execute:
        return execute(a.papers, a.limit, not a.no_commit, not a.no_push)
    papers = ready()
    print(f"{len(papers)} included paper(s) without drafts yet:" if papers else "Nothing waiting for extraction.")
    for p in papers:
        print(_row(p))
    if papers:
        print(f"\nTo extract them: {COMMAND}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
