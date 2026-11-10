#!/usr/bin/env python3
"""
intake_papers.py — everything that has to happen to a PDF between the
download and the extractor, in one command.

    python scripts/intake_papers.py             # dry run: shows what each step would do
    python scripts/intake_papers.py --execute   # do it
    python scripts/intake_papers.py --from ~/Downloads --execute
                                        # also pull in PDFs from Downloads that
                                        # match a cited paper not yet in papers/
    python scripts/intake_papers.py --execute --extract
                                        # … and then extract every paper that
                                        # has no findings yet (20–30 min each)

Steps, in order, each one of the standalone scripts:
  0. (--from DIR) copy PDFs out of DIR whose DOI / filename matches a
                            cited key that has no PDF yet; other files in
                            DIR are left untouched, nothing is moved
  1. strip_cover_pages.py   drop JSTOR / T&F / HighWire / ProQuest … sheets
  2. batch_ocr.py           OCR scanned PDFs (needs ocrmypdf — the step
                            says what is missing and is skipped, the rest
                            still runs)
  3. screening PDFs         a PDF of a screening record (EndNote, a portal
                            upload, a download): linked to its record by
                            the DOI on its first pages (screen.py pdfs),
                            checked against the record (its DOI or title
                            must be on the first pages; a mismatch is
                            reported and the file left alone) and named
                            <id>_<Author><Year>.pdf. It becomes <Key>.pdf
                            when the paper is included (screen.py register)
  4. register_papers.py     a PDF with no citation entry gets one, built
                            from its DOI via Crossref (needs network;
                            skipped with a note when offline). Never a
                            screening record's PDF (step 3)
  5. match_papers.py        rename publisher-named PDFs to <Key>.pdf
  6. kb_status.py           the papers line: cited / present / missing,
                            plus files that match no citation key
  7. publish_portal.py --sync   (with --execute; --no-sync to skip) send
                            what changed to the review portal: annotated
                            PDFs, and the PDFs of papers awaiting full-text
                            screening. Commit portal/papers.json afterwards
  8. (--extract) extract.py --batch
                            run the local model on every PDF that has no
                            findings in drafts/ or the canonical folders

Every route that puts a PDF in papers/ (endnote_match.py, portal_import.py
for portal uploads, --from) runs this afterwards, so a paper is never left
unscanned, misnamed or missing from the portal.

Every step is idempotent, so re-running is the way to "skip what is
done": a file already named after its key is not renamed, a PDF whose
cover sheet is gone is not stripped again, a PDF with a text layer is
not OCR'd again, and a paper that already has findings is not
re-extracted (delete its drafts, or pass --pdf to extract.py, to redo
one on purpose).

Each step is dry-run unless --execute is given. --allow-probable lets
step 1 also rename author/year/title matches (see match_papers.py).
Nothing is deleted; originals of stripped or OCR'd files go to
papers/_originals/.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/

import batch_ocr  # noqa: E402
import kb_status  # noqa: E402
import match_papers  # noqa: E402
import register_papers  # noqa: E402
import strip_cover_pages  # noqa: E402


def _banner(n: int, title: str) -> None:
    print(f"\n{'─' * 70}\n {n}. {title}\n{'─' * 70}")


def pull_from(src_dir: Path, papers_dir: Path, execute: bool) -> int:
    """Copy PDFs in src_dir that match a cited key with no PDF yet."""
    cites = match_papers.read_citations(ROOT / "citations.md")
    have = {p.stem.lower() for p in papers_dir.glob("*.pdf")}
    n = 0
    for f in sorted(src_dir.glob("*.pdf")):
        try:
            text = match_papers.first_pages_text(f)
        except Exception:  # noqa: BLE001
            continue
        key, how = match_papers.match_one(text, cites, filename=f.name)
        if not key or how == "probable":
            continue
        bare = key.lstrip("@")
        if bare.lower() in have:
            continue
        target = papers_dir / f"{bare}.pdf"
        print(f"{'copied' if execute else 'would copy':12} {f.name}  →  papers/{target.name}")
        if execute:
            shutil.copy2(f, target)
            have.add(bare.lower())
        n += 1
    if not n:
        print(f"nothing in {src_dir} matches a cited paper that is still missing")
    return 0


def _label(c: dict) -> str:
    """<Author><Year> for a file name: ASCII letters of the first author's surname, then the year."""
    import unicodedata
    first = str(c.get("first_author") or (str(c.get("authors") or "").split(",")[0]) or "").strip()
    first = unicodedata.normalize("NFKD", first).encode("ascii", "ignore").decode()
    surname = re.sub(r"[^A-Za-z]", "", first.split()[0] if first else "") or "paper"
    return f"{surname[:1].upper()}{surname[1:]}{str(c.get('year') or '')[:4]}"


def identity(pdf: Path, c: dict) -> tuple[bool | None, str]:
    """Is this PDF the record's paper? True (its DOI, or most of its title, is on the first
    pages), False (the text is there but neither is), None (no text to tell: OCR first)."""
    import screening as S
    try:
        text = match_papers.first_pages_text(pdf) or ""
    except Exception as e:  # noqa: BLE001
        return None, f"unreadable ({str(e)[:60]})"
    if len(re.sub(r"\s+", "", text)) < 200:
        return None, "no text layer"
    doi = S.norm_doi(c.get("doi")) if c.get("doi") else None
    if doi and doi in {S.norm_doi(m.group(0)) for m in re.finditer(r"10\.\d{4,9}/[^\s\"<>]+", text)}:
        return True, "DOI"
    words = set(re.findall(r"[a-z]{4,}", text.lower()))
    title = [w for w in re.findall(r"[a-z]{4,}", str(c.get("title") or "").lower())][:12]
    if len(title) >= 3:
        share = sum(1 for w in title if w in words) / len(title)
        if share >= 0.7:
            return True, f"title ({share:.0%})"
        return False, f"neither its DOI nor its title is on the first pages (title words {share:.0%})"
    return False, "its DOI is not on the first pages"


def screening_pdfs(papers_dir: Path, execute: bool) -> int:
    """Step 3: link, check and name the PDFs of screening records (see the module docstring)."""
    import screening as S
    import screen as SC
    if not papers_dir.is_dir():
        print("papers/ not reachable")
        return 0
    cands = S.load_candidates()
    res = SC.link_pdfs(cands)
    for cid, name, how in res["linked"]:
        print(f"{'linked' if execute else 'would link':12} {cid}  ←  {name}   [{how}]")
    changed = bool(res["linked"])
    renamed, bad, unsure = 0, [], []
    for c in cands:
        name = c.get("pdf_file")
        if not name or c.get("duplicate_of"):
            continue
        src = papers_dir / str(name)
        if not src.is_file():
            continue
        ok, why = identity(src, c)
        if ok is False:
            bad.append((c["id"], name, why))
            continue
        if ok is None:
            unsure.append((c["id"], name, why))
        if c.get("key"):
            continue                          # included: screen.py register names it <Key>.pdf
        want = f"{c['id']}_{_label(c)}.pdf"
        if name == want:
            continue
        if (papers_dir / want).exists():
            print(f"{'skip':12} {name}: papers/{want} already exists (a second copy?)")
            continue
        print(f"{'renamed' if execute else 'would rename':12} {name}  →  {want}")
        renamed += 1
        if execute:
            src.rename(papers_dir / want)
            c["pdf_file"] = want
            changed = True
    for cid, name, why in bad:
        print(f"{'CHECK':12} {cid}: papers/{name} does not look like this paper — {why}. "
              f"Open it; if it is the wrong file, move it out of papers/.")
    for cid, name, why in unsure:
        print(f"{'unchecked':12} {cid}: papers/{name} — {why}" + (" (step 2 OCRs it once ocrmypdf is installed)" if why == "no text layer" else ""))
    if execute and changed:
        S.save_candidates(cands)
        SC._log("PDFS-PROCESSED", "screening register",
                f"{len(res['linked'])} linked, {renamed} renamed, {len(bad)} not matching their record")
    if not (res["linked"] or renamed or bad or unsure):
        print("every screening PDF is linked, checked and named")
    return 0


def process(execute: bool = True, sync: bool = True, papers_dir: Path | None = None) -> int:
    """The whole intake, as other scripts call it after putting PDFs in papers/."""
    argv = ["--execute"] if execute else []
    if not sync:
        argv.append("--no-sync")
    if papers_dir is not None:
        argv += ["--papers-dir", str(papers_dir)]
    return _cli(argv)


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--papers-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--execute", action="store_true", help="actually rename / strip / OCR")
    ap.add_argument("--allow-probable", action="store_true",
                    help="also rename author/year/title matches (match_papers.py)")
    ap.add_argument("--no-ocr", action="store_true", help="skip the OCR step")
    ap.add_argument("--no-register", action="store_true",
                    help="do not add citation entries for unknown PDFs (register_papers.py)")
    ap.add_argument("--from", dest="from_dir", type=Path, metavar="DIR",
                    help="first copy matching PDFs out of DIR (e.g. ~/Downloads)")
    ap.add_argument("--no-sync", action="store_true",
                    help="do not send the changes to the review portal (publish_portal.py --sync)")
    ap.add_argument("--extract", action="store_true",
                    help="afterwards run extract.py --batch on the papers with no findings "
                         "(with --execute; dry run lists them)")
    args = ap.parse_args(argv)

    ex = ["--execute"] if args.execute else []
    papers = ["--papers-dir", str(args.papers_dir)]
    rc = 0

    if args.from_dir:
        _banner(0, f"Copy cited papers out of {args.from_dir}")
        src = args.from_dir.expanduser()
        if not src.is_dir():
            print(f"not a directory: {src}")
            return 2
        rc |= pull_from(src, args.papers_dir, args.execute)

    _banner(1, "Strip publisher cover sheets  (strip_cover_pages.py)")
    rc |= strip_cover_pages._cli(papers + ex)

    if not args.no_ocr:
        _banner(2, "OCR scanned PDFs  (batch_ocr.py)")
        missing = batch_ocr.missing_tools() if args.execute else []
        if missing:
            print("skipped — OCR tools missing (macOS: brew install ocrmypdf):\n  " + "\n  ".join(missing))
            rc |= 2
        else:
            r = batch_ocr.main(papers + ex)
            rc |= (r if r != 1 else 0)   # 1 = some file failed; reported above

    _banner(3, "Screening PDFs: link, check against the record, name  (screen.py pdfs)")
    rc |= screening_pdfs(args.papers_dir, args.execute)

    if not args.no_register:
        _banner(4, "Register new PDFs in citations.md  (register_papers.py)")
        r = register_papers.register(args.papers_dir, ROOT / "citations.md", args.execute)
        if r:
            print("  ↑ these files will not be renamed or extracted until they have an entry")

    _banner(5, "Rename downloads to their citation key  (match_papers.py)")
    rc |= match_papers._cli(papers + ex + (["--allow-probable"] if args.allow_probable else []))

    _banner(6, "Papers status  (kb_status.py)")
    st = kb_status.collect(ROOT)
    missing_keys = [k for k, v in st["papers"].items() if not v["pdf_present"]]
    print(f"  {len(st['papers'])} cited · {len(st['papers']) - len(missing_keys)} with a PDF · "
          f"{len(missing_keys)} missing"
          + (f"  →  python scripts/kb_status.py --papers-needed" if missing_keys else ""))
    if st.get("papers_unmatched"):
        try:
            import screening as _S
            linked = {c["pdf_file"] for c in _S.load_candidates() if c.get("pdf_file")}
        except Exception:  # noqa: BLE001
            linked = set()
        waiting = [n for n in st["papers_unmatched"] if n in linked]
        loose = [n for n in st["papers_unmatched"] if n not in linked]
        if waiting:
            print(f"  {len(waiting)} file(s) linked to screening records, renamed on inclusion (screen.py register)")
        if loose:
            print(f"  {len(loose)} file(s) match no citation key and no screening record: "
                  + ", ".join(loose[:8]) + (" …" if len(loose) > 8 else ""))
            print("  (python scripts/screen.py pdfs to link them; otherwise chase the paper or move the file out)")

    if args.execute and not args.no_sync:
        _banner(7, "Send to the review portal  (publish_portal.py --sync)")
        done = subprocess.call([sys.executable, str(ROOT / "scripts" / "publish_portal.py"), "--sync"], cwd=str(ROOT))
        if done:
            print("  ⚠ the sync failed (npx wrangler login?) — run python scripts/publish_portal.py --sync again")
        else:
            print("  Commit portal/papers.json and push so the portal lists them.")

    if args.extract:
        _banner(8, "Extract papers that have no findings yet  (extract.py --batch)")
        cmd = [sys.executable, str(ROOT / "scripts" / "extract.py"), "--batch"]
        if not args.execute:
            cmd.append("--dry-run")
        print("  $ " + " ".join(cmd[1:]) + "\n")
        rc |= subprocess.call(cmd, cwd=str(ROOT.parent))

    if not args.execute:
        print("\nDry run throughout. Re-run with --execute to apply all steps.")
    return rc


if __name__ == "__main__":
    sys.exit(_cli())
