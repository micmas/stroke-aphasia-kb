#!/usr/bin/env python3
"""
endnote_match.py — find, in an EndNote library on this computer, the PDFs of papers the
knowledge base still needs, and copy them into papers/.

    python scripts/endnote_match.py --library ~/Documents/endnote/Michele.enlp
        # dry run: which of the papers awaiting a full-text decision (or included, with no
        # PDF here yet) are in the library with a PDF attached, and how each was matched

    python scripts/endnote_match.py --library … --execute
        # copy those PDFs into papers/ (never moves or changes anything in the library),
        # link candidates without a citation key through `pdf_file`, log one line each

    python scripts/endnote_match.py --library … --ids C2467 C0752      # only these candidates
    python scripts/endnote_match.py --library … --titles              # also accept title + year matches

Which papers: candidates whose stage is awaiting or unsure at full text, not retrieved, or
included, and that have no PDF in papers/ (neither <Key>.pdf nor the file named by `pdf_file`).

How a paper is matched, in this order: DOI, PubMed id, then (only with --titles) the same
normalised title and the same year. DOI and PMID matches are exact identifiers; a title
match is listed separately so a person can look before it is trusted.

The library is read, never written: its database (the .enl file, SQLite) is copied to a
temporary file and the copy is opened, so EndNote can stay open and nothing in the
library folder changes. PDFs are copied, not moved. An .enlp package, a .enl file, or the
folder that holds one are all accepted as --library.

After --execute: `python scripts/intake_papers.py --execute` registers, cleans and OCRs the
new PDFs as for any paper; then `python scripts/publish_portal.py --sync` and a commit of
portal/papers.json tell the portal the papers are here, which opens their full-text cards.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import screening as S  # noqa: E402

PAPERS = ROOT / "papers"
LOG = ROOT / "logs" / "extraction_log.md"
WANTED_STAGES = ("awaiting_ft", "unsure_ft", "not_retrieved", "included")


# ------------------------------------------------------------------ normalising identifiers
def norm_doi(x) -> str:
    """`https://doi.org/10.1016/J.X.2018.01.001.` and `doi:10.1016/j.x.2018.01.001` are one DOI."""
    m = re.search(r"10\.\d{4,9}/[^\s\"<>]+", str(x or ""), flags=re.I)
    return m.group(0).rstrip(".,;)").lower() if m else ""


def norm_pmid(x) -> str:
    m = re.fullmatch(r"\s*(?:pmid:?\s*)?(\d{5,9})\s*", str(x or ""), flags=re.I)
    return m.group(1) if m else ""


def pmid_from_url(x) -> str:
    m = re.search(r"(?:pubmed\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pubmed)/(\d{5,9})", str(x or ""))
    return m.group(1) if m else ""


def norm_title(x) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(x or "").lower())


def year_of(x) -> str:
    m = re.search(r"(19|20)\d{2}", str(x or ""))
    return m.group(0) if m else ""


# ------------------------------------------------------------------ the library
def locate(library: Path) -> tuple[Path, Path]:
    """(database file, PDF folder) for an .enlp package, a .enl file, or a folder holding one."""
    library = library.expanduser()
    if library.is_file():
        enl = library
    else:
        if not library.is_dir():
            raise FileNotFoundError(f"{library} is neither an EndNote library file nor a folder")
        enls = sorted(library.glob("*.enl"), key=lambda p: p.stat().st_size, reverse=True)
        named = [p for p in enls if p.stem == library.stem]        # Michele.enlp → Michele.enl
        if not enls:
            raise FileNotFoundError(f"no .enl file in {library}")
        enl = named[0] if named else enls[0]
    pdfs = enl.with_name(enl.stem + ".Data") / "PDF"
    if not pdfs.is_dir():
        raise FileNotFoundError(f"the library's PDF folder is missing: {pdfs}")
    return enl, pdfs


def read_library(enl: Path) -> list[dict]:
    """Live references that have at least one PDF attached: {id, doi, pmid, title, year, author, files}."""
    with tempfile.TemporaryDirectory() as td:
        copy = Path(td) / "library.sqlite"
        shutil.copyfile(enl, copy)                                  # never open the library's own file
        con = sqlite3.connect(str(copy))
        con.create_collation("ENCI_Base", lambda a, b: (a > b) - (a < b))   # EndNote's collation, only needed to open
        try:
            files: dict[int, list[str]] = {}
            for rid, path, pos in con.execute("select refs_id, file_path, file_pos from file_res order by refs_id, file_pos"):
                if str(path or "").lower().endswith(".pdf"):
                    files.setdefault(rid, []).append(str(path))
            clean: dict[int, tuple[str, str]] = {}
            try:
                for rid, doi, pmid in con.execute("select refs_id, clean_doi, clean_pmid from ret_watch"):
                    clean[rid] = (str(doi or ""), str(pmid or ""))
            except sqlite3.Error:
                pass                                                # older libraries have no such table
            out = []
            for rid, trash, author, year, title, doi, acc, url in con.execute(
                    "select id, trash_state, author, year, title, electronic_resource_number, accession_number, url from refs"):
                if trash or rid not in files:
                    continue
                cd, cp = clean.get(rid, ("", ""))
                out.append({"id": rid, "doi": norm_doi(doi) or norm_doi(cd) or norm_doi(url),
                            "pmid": norm_pmid(acc) or norm_pmid(cp) or pmid_from_url(url),
                            "title": str(title or ""), "year": year_of(year),
                            "author": str(author or "").replace("\r", "; ").split(";")[0].strip(), "files": files[rid]})
            return out
        finally:
            con.close()


# ------------------------------------------------------------------ what the KB still needs
def has_pdf(c: dict, papers: Path = PAPERS) -> bool:
    key = str(c.get("key") or "").lstrip("@")
    if key and (papers / f"{key}.pdf").exists():
        return True
    return bool(c.get("pdf_file")) and (papers / str(c["pdf_file"])).exists()


def wanted(root: Path = ROOT, papers: Path = PAPERS, ids: list[str] | None = None) -> list[dict]:
    rows = S.collect(root)["candidates"]
    if ids:
        want = {i.upper() for i in ids}
        rows = [r for r in rows if str(r.get("id", "")).upper() in want]
    else:
        rows = [r for r in rows if r.get("stage") in WANTED_STAGES]
    return [r for r in rows if not has_pdf(r, papers)]


def match(cands: list[dict], refs: list[dict], titles: bool = False) -> list[dict]:
    """[{candidate, ref, how}] — one match per candidate at most, DOI before PMID before title."""
    by_doi, by_pmid, by_title = {}, {}, {}
    for r in refs:
        if r["doi"]:
            by_doi.setdefault(r["doi"], r)
        if r["pmid"]:
            by_pmid.setdefault(r["pmid"], r)
        t = norm_title(r["title"])
        if len(t) >= 25:                                            # short titles collide ("Aphasia", "Editorial")
            by_title.setdefault((t, r["year"]), r)
    out = []
    for c in cands:
        ref, how = by_doi.get(norm_doi(c.get("doi"))), "DOI"
        if ref is None:
            ref, how = by_pmid.get(norm_pmid(c.get("pmid"))), "PMID"
        if ref is None and titles:
            ref, how = by_title.get((norm_title(c.get("title")), year_of(c.get("year")))), "title + year"
        if ref is not None:
            out.append({"candidate": c, "ref": ref, "how": how})
    return out


def destination(c: dict, source: Path, papers: Path = PAPERS) -> Path:
    key = str(c.get("key") or "").lstrip("@")
    if key:
        return papers / f"{key}.pdf"
    if c.get("pdf_file"):
        return papers / str(c["pdf_file"])
    safe = re.sub(r"[^\w.() -]+", "_", source.name).strip(" .")[:100] or "paper.pdf"
    return papers / f"{c['id']}_{safe}"


# ------------------------------------------------------------------ run
def run(library: Path, execute: bool, titles: bool, ids: list[str] | None, by: str,
        root: Path = ROOT, papers: Path = PAPERS, log: Path = LOG, intake: bool = False) -> int:
    enl, pdf_dir = locate(library)
    refs = read_library(enl)
    cands = wanted(root, papers, ids)
    print(f"EndNote library {enl.name}: {len(refs)} references with a PDF attached")
    print(f"Knowledge base: {len(cands)} paper(s) past title/abstract screening with no PDF in papers/")
    found = match(cands, refs, titles)
    if not found:
        print("None of them is in the library with a PDF." + ("" if titles else " (--titles also tries title + year.)"))
        return 0
    register = S.load_candidates(root) if execute else []
    by_id = {c["id"]: c for c in register}
    copied = linked = 0
    for m in sorted(found, key=lambda x: (x["how"] != "DOI", x["how"] != "PMID", str(x["candidate"]["id"]))):
        c, r = m["candidate"], m["ref"]
        src = pdf_dir / r["files"][0]
        dest = destination(c, src, papers)
        extra = f" (+{len(r['files']) - 1} more attachment(s), first one taken)" if len(r["files"]) > 1 else ""
        head = f"  {c['id']:>6} {str(c.get('key') or ''):<24} by {m['how']:<12} ← {r['author']} {r['year']}: {r['title'][:70]}"
        if not src.exists():
            print(f"{head}\n         ✗ the library lists {r['files'][0]} but the file is not there")
            continue
        if not execute:
            print(f"{head}\n         would copy {src.name} → papers/{dest.name}{extra}")
            continue
        try:
            with src.open("rb") as fh:
                if fh.read(5) != b"%PDF-":
                    print(f"{head}\n         ✗ {src.name} is not a PDF")
                    continue
            papers.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
        except OSError as e:
            print(f"{head}\n         ✗ could not copy {src.name}: {e}")
            continue
        copied += 1
        live = by_id.get(c["id"])
        if live is not None and not live.get("key") and live.get("pdf_file") != dest.name:
            live["pdf_file"] = dest.name
            linked += 1
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as fh:
            fh.write(f"{dt.date.today().isoformat()} | ENDNOTE-PDF | {c.get('key') or c['id']} | papers/{dest.name} | matched by {m['how']} | by: human:{by}\n")
        print(f"{head}\n         ✓ papers/{dest.name}{extra}")
    if execute:
        if linked:
            S.save_candidates(register, root)
        print(f"\n{copied} PDF(s) copied into papers/" + (f", {linked} linked to their candidate" if linked else "") + ".")
        if copied and intake:           # cover sheets, OCR, link/check/name, portal sync
            import intake_papers
            intake_papers.process(execute=True, papers_dir=papers)
        elif copied:
            print("Next: python scripts/intake_papers.py --execute (cleans, OCRs, checks, names and syncs them).")
    else:
        n_title = sum(1 for m in found if m["how"] == "title + year")
        print(f"\nDry run: {len(found)} of {len(cands)} would be copied" + (f" ({n_title} matched by title + year: check those)" if n_title else "") +
              ". Add --execute.")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--library", type=Path, required=True, help="the EndNote library: an .enlp package, a .enl file, or the folder holding one")
    ap.add_argument("--execute", action="store_true", help="copy the PDFs (default: only say what would be copied)")
    ap.add_argument("--titles", action="store_true", help="also match on normalised title + year when there is no DOI or PMID match")
    ap.add_argument("--ids", nargs="*", metavar="CID", help="only these candidates (any stage)")
    ap.add_argument("--by", default="michele", help="name for the log lines (default michele)")
    ap.add_argument("--no-intake", action="store_true", help="do not run intake_papers.py on the copied PDFs afterwards")
    args = ap.parse_args(argv)
    try:
        return run(args.library, args.execute, args.titles, args.ids, args.by, intake=not args.no_intake)
    except (FileNotFoundError, sqlite3.Error) as e:
        print(f"endnote_match: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(_cli())
