#!/usr/bin/env python3
"""
screen.py — systematic identification and screening of candidate papers
(docs/SCREENING.md). Feeds the existing intake → extract → review → promote
pipeline; never writes to drafts/ or the canonical folders.

    # 0. protocol (docs/SCREENING.md, screening/strategies.yaml)
    python scripts/screen.py strategies               # the pre-specified strategies, fingerprint, lock state
    python scripts/screen.py strategies --show q1_lesion_impairment --db scopus   # the string to paste into Scopus
    python scripts/screen.py rebaseline --execute     # legacy decisions → `legacy`, legacy includes → benchmark (once)

    # 1. identify — protocol searches (refused with --execute until the protocol is locked and committed)
    python scripts/screen.py search --strategy q1_lesion_impairment --db pubmed --by michele            # dry run: hits + benchmark recall
    python scripts/screen.py search --strategy q1_lesion_impairment --db pubmed --by michele --execute
    python scripts/screen.py import --strategy q1_lesion_impairment --db scopus --file ~/Downloads/scopus.ris --by michele --execute
    python scripts/screen.py recall                   # relative recall of the searches against the benchmark
    python scripts/screen.py chase --doi 10.1038/384159a0 --cited-by C0123,C0201 \\
        --why "Source of the insula claim the insula_apraxia_of_speech gap contests" --by michele --execute
    # ad-hoc searches (recorded, reported, but not part of the protocol)
    python scripts/screen.py search --db pubmed --query '"aphasia"[tiab] AND stroke[tiab] AND (lesion[tiab] OR VLSM[tiab])' \
                            --years 2000-2026 --for thalamus_basal_ganglia --by michele --execute
    python scripts/screen.py search --db openalex --query 'aphasia stroke lesion symptom mapping' --years 2015-2026 --execute
    python scripts/screen.py import --file ~/Downloads/scopus.ris --db scopus --query '<the query you ran>' --for right_hemisphere --execute
    python scripts/screen.py backfill --execute       # the bibliography as it stood before the register (once)

    # 2. screen
    python scripts/screen.py assist                   # local model's opinion on every unscreened title/abstract (suggestion only)
    python scripts/screen.py sheet                    # screening/_sheet/title_abstract.html — decide, download the CSV
    python scripts/screen.py decide --csv ~/Downloads/decisions.csv --by michele
    python scripts/screen.py decide --id C0012 --stage full_text --decision exclude --reason not_retrieved --by michele
    python scripts/screen.py sheet --stage full_text  # the same for the full-text pass
    python scripts/screen.py sheet --check --sample 0.2 --seed 1          # blind sample for a second screener
    python scripts/screen.py decide --csv ~/Downloads/check.csv --by <second screener> --role check
    python scripts/screen.py agreement                # Cohen's kappa, and the disagreements to reconcile

    # 3. hand over
    python scripts/screen.py register --execute       # included candidates → citations.md entries (DOI via Crossref)
    python scripts/screen.py status                   # the PRISMA numbers; --json for scripts
    python scripts/screen.py list --stage awaiting_ft # what is waiting, with ids

Everything is a dry run unless --execute is given (decide applies at once;
it is the decision itself). Every applied step appends a line to
logs/extraction_log.md. Decisions are made by a named person (--by); the model
only ever writes `suggestion`. Abstracts are cached in
screening/abstracts.jsonl (git-ignored) and are re-fetchable.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import screening as S  # noqa: E402

UA = "stroke-aphasia-kb screen.py/1.0 (mailto:m.massontrottier@uq.edu.au)"
MAILTO = "m.massontrottier@uq.edu.au"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OPENALEX = "https://api.openalex.org/works"
OPENALEX_KEY_HELP = ("OpenAlex now needs a free API key (without one, every request shares one small daily budget per "
                     "network address — at UQ that is spent quickly). Get a key at https://openalex.org/settings/api, then "
                     "`export OPENALEX_API_KEY=<key>` (add it to ~/.zshrc to keep it). Never commit the key.")


def _openalex_auth() -> dict:
    """api_key from the OPENALEX_API_KEY environment variable (never stored in the repo), plus mailto."""
    import os
    key = os.environ.get("OPENALEX_API_KEY", "").strip()
    return {"api_key": key, "mailto": MAILTO} if key else {"mailto": MAILTO}
LOG = ROOT / "logs/extraction_log.md"
SHEET_DIR = ROOT / "screening" / "_sheet"
STAGE_TEXT = {"title_abstract": "title/abstract", "full_text": "full text"}


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def _get(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _log(action: str, what: str, meta: str) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{dt.date.today().isoformat()} | {action} | — | {what} | {meta}\n")


def _next_search_id(searches: list[dict]) -> str:
    n = 0
    for s in searches:
        m = re.match(r"^S(\d+)$", str(s.get("id") or ""))
        if m:
            n = max(n, int(m.group(1)))
    return f"S{n + 1:03d}"


def load_abstracts() -> dict[str, str]:
    out: dict[str, str] = {}
    if S.ABSTRACTS.exists():
        for line in S.ABSTRACTS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    rec = json.loads(line)
                    out[rec["id"]] = rec.get("abstract") or ""
                except (ValueError, KeyError):
                    continue
    return out


def save_abstracts(abstracts: dict[str, str]) -> None:
    S.DIR.mkdir(exist_ok=True)
    with S.ABSTRACTS.open("w", encoding="utf-8") as fh:
        for cid in sorted(abstracts):
            fh.write(json.dumps({"id": cid, "abstract": abstracts[cid]}, ensure_ascii=False) + "\n")


def _years(arg: str | None) -> tuple[int | None, int | None]:
    if not arg:
        return None, None
    m = re.match(r"^(\d{4})?\s*-\s*(\d{4})?$", arg.strip())
    if not m:
        raise SystemExit(f"--years must look like 2000-2026, 2010- or -2015 (got {arg!r})")
    return (int(m.group(1)) if m.group(1) else None), (int(m.group(2)) if m.group(2) else None)


# ---------------------------------------------------------------------------
# identification: PubMed, OpenAlex, RIS / CSV import
# ---------------------------------------------------------------------------

PUBMED_WINDOW = 9999        # E-utilities return at most the first 10,000 records of one query
LAST_MISSING: list[str] = []   # PMIDs a PubMed run counted but could not fetch


def _pubmed_count(term: str) -> int:
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": 0, "retmode": "json",
                                "tool": "stroke-aphasia-kb", "email": MAILTO})
    time.sleep(0.4)
    return int(json.loads(_get(f"{EUTILS}esearch.fcgi?{q}"))["esearchresult"].get("count") or 0)


def pubmed_search(query: str, years=(None, None), max_results: int = 2000) -> tuple[list[dict], int]:
    """E-utilities: esearch (history server) then efetch in batches of 200. A query
    with more hits than the E-utilities window is split into publication-year
    ranges, each under the window, so nothing is silently cut off."""
    LAST_MISSING.clear()
    lo, hi = years
    total = _pubmed_count(_pubmed_term(query, lo, hi))
    if total <= PUBMED_WINDOW or max_results <= PUBMED_WINDOW:
        return _pubmed_fetch(query, lo, hi, max_results)[0], total
    out: dict[str, dict] = {}
    for a, b in _pubmed_year_chunks(query, lo or 1800, hi or dt.date.today().year + 1):
        for r in _pubmed_fetch(query, a, b, max_results)[0]:
            out.setdefault(r.get("pmid") or f"x{len(out)}", r)
    return list(out.values())[:max_results], total


def _pubmed_term(query: str, lo, hi) -> str:
    return f"({query}) AND ({lo or 1800}[dp] : {hi or 3000}[dp])" if (lo or hi) else query


def _pubmed_year_chunks(query: str, lo: int, hi: int) -> list[tuple[int, int]]:
    n = _pubmed_count(_pubmed_term(query, lo, hi))
    if n <= PUBMED_WINDOW or lo >= hi:
        if n > PUBMED_WINDOW:
            raise SystemExit(f"PubMed: {n} hits in {lo} alone — more than one query can return; narrow the strategy.")
        return [(lo, hi)] if n else []
    mid = (lo + hi) // 2
    return _pubmed_year_chunks(query, lo, mid) + _pubmed_year_chunks(query, mid + 1, hi)


def _pubmed_fetch(query: str, lo, hi, max_results: int) -> tuple[list[dict], int]:
    term = _pubmed_term(query, lo, hi)
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": max_results, "retmode": "json", "usehistory": "y",
                                "tool": "stroke-aphasia-kb", "email": MAILTO})
    es = json.loads(_get(f"{EUTILS}esearch.fcgi?{q}"))["esearchresult"]
    total = int(es.get("count") or 0)
    webenv, qkey = es.get("webenv"), es.get("querykey")
    out: list[dict] = []
    for start in range(0, min(total, max_results), 200):
        q = urllib.parse.urlencode({"db": "pubmed", "WebEnv": webenv, "query_key": qkey, "retstart": start, "retmax": 200,
                                    "retmode": "xml", "tool": "stroke-aphasia-kb", "email": MAILTO})
        out.extend(parse_pubmed_xml(_get(f"{EUTILS}efetch.fcgi?{q}", timeout=120)))
        time.sleep(0.4)                 # 3 requests/s without an API key
    want = min(total, max_results)
    if len(out) < want and total <= PUBMED_WINDOW:
        # a batch came back short: fetch the missing records by PMID
        q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": PUBMED_WINDOW, "retmode": "json",
                                    "tool": "stroke-aphasia-kb", "email": MAILTO})
        ids = json.loads(_get(f"{EUTILS}esearch.fcgi?{q}"))["esearchresult"].get("idlist") or []
        have = {r.get("pmid") for r in out}
        missing = [i for i in ids if i not in have]
        for i in range(0, len(missing), 100):
            q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(missing[i:i + 100]), "retmode": "xml",
                                        "tool": "stroke-aphasia-kb", "email": MAILTO})
            out.extend(parse_pubmed_xml(_get(f"{EUTILS}efetch.fcgi?{q}", timeout=120)))
            time.sleep(0.4)
        have = {r.get("pmid") for r in out}
        LAST_MISSING[:] = [i for i in ids if i not in have]
    return out, total


def parse_pubmed_xml(data: bytes) -> list[dict]:
    """PubmedArticle (journal) and PubmedBookArticle (NCBI Bookshelf chapter) records.

    Identifiers come only from the record's own id list (PubmedData/ArticleIdList,
    BookDocument/ArticleIdList) and its ELocationID — never from ReferenceList, whose
    ArticleIdList elements are the DOIs of the papers it cites."""
    out = []
    root = ET.fromstring(data)
    for art in list(root.iter("PubmedArticle")) + list(root.iter("PubmedBookArticle")):
        book = art.tag == "PubmedBookArticle"
        pmid = (art.findtext("./MedlineCitation/PMID") or art.findtext("./BookDocument/PMID") or "").strip()
        t_el = art.find(".//ArticleTitle")
        if t_el is None or not "".join(t_el.itertext()).strip():
            t_el = art.find(".//BookTitle")
        title = " ".join("".join(t_el.itertext()).split()) if t_el is not None else ""
        parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            label = ab.get("Label")
            text = " ".join("".join(ab.itertext()).split())
            parts.append(f"{label}: {text}" if label else text)
        doi = None
        for eid in art.findall("./PubmedData/ArticleIdList/ArticleId") + art.findall("./BookDocument/ArticleIdList/ArticleId"):
            if eid.get("IdType") == "doi" and not doi:
                doi = S.norm_doi(eid.text)
        if not doi:
            for el in art.findall("./MedlineCitation/Article/ELocationID") + art.findall("./BookDocument/ELocationID"):
                if el.get("EIdType") == "doi":
                    doi = S.norm_doi(el.text)
                    break
        year = (art.findtext(".//JournalIssue/PubDate/Year") or art.findtext(".//JournalIssue/PubDate/MedlineDate")
                or art.findtext("./BookDocument/Book/PubDate/Year") or art.findtext("./BookDocument/ContributionDate/Year") or "")
        ym = re.search(r"(19|20)\d{2}", year)
        authors = []
        for a in (art.findall("./MedlineCitation/Article/AuthorList/Author") or art.findall("./BookDocument/AuthorList/Author")):
            last, ini, coll = a.findtext("LastName"), a.findtext("Initials"), a.findtext("CollectiveName")
            if last:
                authors.append(f"{last} {ini or ''}".strip())
            elif coll:
                authors.append(coll)
        out.append({"pmid": pmid, "doi": doi, "title": title.rstrip("."), "year": int(ym.group(0)) if ym else None,
                    "authors": authors, "journal": art.findtext(".//Journal/Title") or art.findtext(".//Book/BookTitle") or "",
                    "abstract": " ".join(parts), "book": book or None,
                    "pub_types": [pt.text for pt in art.findall(".//PublicationType") if pt.text]})
    return out


def _openalex_abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos: list[tuple[int, str]] = []
    for word, idxs in inv.items():
        for i in idxs:
            pos.append((i, word))
    return " ".join(w for _, w in sorted(pos))


LAST_COST = [0.0]   # OpenAlex usage of the last run, in US$ (the API reports it per request)


def openalex_search(query: str, years=(None, None), max_results: int = 2000, field: str = "search") -> tuple[list[dict], int]:
    """field 'search': OpenAlex relevance search (title, abstract, full text);
    field 'title_and_abstract': a boolean title+abstract filter — what the
    protocol strategies use, because it is reproducible and says where it looked."""
    LAST_COST[0] = 0.0
    lo, hi = years
    filters = ["type:article|review"]
    if lo or hi:
        filters.append(f"publication_year:{lo or 1800}-{hi or 3000}")
    params = {}
    if field == "title_and_abstract":
        if "," in query:
            raise SystemExit("an OpenAlex filter value cannot contain a comma; rewrite the query without commas")
        filters.append(f"title_and_abstract.search:{query}")
    else:
        params["search"] = query
    out: list[dict] = []
    cursor, total = "*", 0
    while cursor and len(out) < max_results:
        q = urllib.parse.urlencode({**params, **_openalex_auth(), "filter": ",".join(filters), "per-page": 200, "cursor": cursor,
                                    "select": "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,ids,type"})
        data = json.loads(_get(f"{OPENALEX}?{q}", timeout=120))
        total = int(data.get("meta", {}).get("count") or 0)
        LAST_COST[0] += float((data.get("meta") or {}).get("cost_usd") or 0)
        for w in data.get("results") or []:
            out.append(openalex_record(w))
        cursor = (data.get("meta") or {}).get("next_cursor")
        time.sleep(0.2)
    return out, total


def openalex_record(w: dict) -> dict:
    ids = w.get("ids") or {}
    pmid = (ids.get("pmid") or "").rsplit("/", 1)[-1] or None
    return {"openalex": (w.get("id") or "").rsplit("/", 1)[-1] or None, "pmid": pmid, "doi": S.norm_doi(w.get("doi")),
            "title": (w.get("title") or "").rstrip("."), "year": w.get("publication_year"),
            "authors": [((a.get("author") or {}).get("display_name") or "") for a in (w.get("authorships") or [])],
            "journal": (((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""),
            "abstract": _openalex_abstract(w.get("abstract_inverted_index")), "pub_types": [w.get("type") or ""]}


def parse_ris(text: str) -> list[dict]:
    out, rec = [], {}
    for line in text.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line)
        if not m:
            continue
        tag, val = m.group(1), m.group(2).strip()
        if tag == "TY":
            rec = {"authors": [], "title": "", "abstract": ""}
        elif tag == "ER":
            if rec:
                out.append(rec)
            rec = {}
        elif tag in ("TI", "T1"):
            rec["title"] = (rec.get("title") + " " + val).strip() if rec.get("title") else val
        elif tag in ("AU", "A1"):
            rec["authors"].append(val)
        elif tag in ("PY", "Y1"):
            ym = re.search(r"(19|20)\d{2}", val)
            rec["year"] = int(ym.group(0)) if ym else None
        elif tag == "DO":
            rec["doi"] = S.norm_doi(val)
        elif tag in ("AB", "N2"):
            rec["abstract"] = (rec.get("abstract") + " " + val).strip() if rec.get("abstract") else val
        elif tag in ("JO", "JF", "T2", "JA"):
            rec.setdefault("journal", val)
        elif tag in ("AN", "ID", "C1") and re.fullmatch(r"\d{6,9}", val):
            rec.setdefault("pmid", val)
        elif tag == "UR" and "doi.org" in val and not rec.get("doi"):
            rec["doi"] = S.norm_doi(val)
    for r in out:
        r["title"] = r["title"].rstrip(".")
    return out


_CSV_COLS = {"title": ("title", "article title", "document title"), "doi": ("doi",),
             "year": ("year", "publication year", "py"), "authors": ("authors", "author", "author names", "author full names"),
             "abstract": ("abstract",), "journal": ("source title", "journal", "source", "publication title"),
             "pmid": ("pubmed id", "pmid")}


def parse_csv(text: str) -> list[dict]:
    rows = list(csv.DictReader(text.splitlines()))
    out = []
    for row in rows:
        low = {str(k).strip().lower(): (v or "").strip() for k, v in row.items() if k}
        rec: dict = {}
        for field, names in _CSV_COLS.items():
            for n in names:
                if n in low and low[n]:
                    rec[field] = low[n]
                    break
        if not rec.get("title"):
            continue
        ym = re.search(r"(19|20)\d{2}", rec.get("year") or "")
        out.append({"title": rec["title"].rstrip("."), "doi": S.norm_doi(rec.get("doi")), "year": int(ym.group(0)) if ym else None,
                    "authors": [a.strip() for a in re.split(r";|, (?=[A-Z][a-z]+ [A-Z])", rec.get("authors") or "") if a.strip()],
                    "abstract": rec.get("abstract") or "", "journal": rec.get("journal") or "", "pmid": rec.get("pmid") or None})
    return out


def add_records(records: list[dict], search_id: str, candidates: list[dict], abstracts: dict[str, str]) -> tuple[int, int]:
    """Merge search results into the register. Returns (new, already known)."""
    index = S.build_identity_index(candidates)
    new = known = 0
    for r in records:
        dup = S.find_duplicate(r, index)
        if dup is not None:
            known += 1
            srcs = dup.setdefault("sources", [])
            if not any(isinstance(s, dict) and s.get("search") == search_id for s in srcs):
                srcs.append({"search": search_id})
            for k in ("doi", "pmid", "openalex", "journal", "year"):
                if not dup.get(k) and r.get(k):
                    dup[k] = r[k]
            if r.get("abstract") and not abstracts.get(dup["id"]):
                abstracts[dup["id"]] = r["abstract"]
            continue
        cand = {"id": S.next_id(candidates), "doi": r.get("doi"), "pmid": r.get("pmid"), "openalex": r.get("openalex"),
                "title": r.get("title"), "year": r.get("year"),
                "first_author": (r.get("authors") or [""])[0].split(",")[0].split(" ")[0] if r.get("authors") else None,
                "authors": ", ".join(r.get("authors") or [])[:400] or None, "journal": r.get("journal") or None,
                "sources": [{"search": search_id}], "screening": []}
        cand = {k: v for k, v in cand.items() if v not in (None, "", [])}
        cand.setdefault("screening", [])
        candidates.append(cand)
        if r.get("abstract"):
            abstracts[cand["id"]] = r["abstract"]
        for k in S.identity_keys(cand):
            index.setdefault(k, cand)
        new += 1
    return new, known


def _resolve_strategy(args) -> None:
    """Fill query / years / for from screening/strategies.yaml when --strategy is given,
    and stamp the protocol on args for _ingest."""
    args.protocol = None
    if not getattr(args, "strategy", None):
        if args.max is None:
            args.max = 2000
        return
    if args.query:
        raise SystemExit("give --strategy or --query, not both: a strategy's query is the one in screening/strategies.yaml")
    strategies = S.load_strategies()
    try:
        st = S.strategy(strategies, args.strategy)
        args.query = S.query_for_run(strategies, args.strategy, args.db)
    except KeyError as e:
        raise SystemExit(str(e).strip('"'))
    if not args.years:
        args.years = S.strategy_years(strategies, args.strategy)
    if not args.for_ and st.get("for"):
        args.for_ = ",".join(str(x) for x in st["for"])
    if args.max is None:
        args.max = 10 ** 6                       # a protocol search is never capped
    state = S.protocol_state()
    args.protocol = state
    if args.execute and not state["locked"] and not args.allow_unlocked:
        why = []
        if state["status"] != "locked":
            why.append(f"strategies.yaml has status: {state['status']}")
        if state["committed"] is False:
            why.append("docs/SCREENING.md or screening/strategies.yaml has uncommitted changes")
        if state["committed"] is None:
            why.append("git could not confirm the protocol files are committed")
        raise SystemExit("The protocol is not locked (" + "; ".join(why) + "). Set status: locked, commit both files, "
                         "then run again — or add --allow-unlocked for a pilot run (recorded as such).")


def cmd_search(args) -> int:
    _resolve_strategy(args)
    years = _years(args.years)
    if not args.query:
        raise SystemExit("--query or --strategy is required")
    try:
        if args.db == "pubmed":
            records, total = pubmed_search(args.query, years, args.max)
        elif args.db == "openalex":
            records, total = openalex_search(args.query, years, args.max,
                                             field="title_and_abstract" if args.strategy else args.oa_field)
        else:
            raise SystemExit("--db must be pubmed or openalex for a live search; use `import` for a file export")
    except urllib.error.HTTPError as e:
        if args.db == "openalex" and e.code in (401, 403, 429):
            raise SystemExit(f"OpenAlex refused the request (HTTP {e.code}). {OPENALEX_KEY_HELP}")
        raise SystemExit(f"{args.db} answered HTTP {e.code} ({e.reason}); try again later.")
    except (urllib.error.URLError, OSError) as e:
        raise SystemExit(f"{args.db} could not be reached ({e}). Run from a machine with network access, or run the "
                         f"search in the database's own interface and bring the export in with `screen.py import`.")
    return _ingest(args, records, total, file=None)


def cmd_import(args) -> int:
    _resolve_strategy(args)
    text = Path(args.file).read_text(encoding="utf-8", errors="replace")
    records = parse_ris(text) if args.file.lower().endswith(".ris") or "TY  -" in text[:2000] else parse_csv(text)
    return _ingest(args, records, len(records), file=str(Path(args.file).name))


def _ingest(args, records, total, file) -> int:
    searches, candidates = S.load_searches(), S.load_candidates()
    abstracts = load_abstracts()
    sid = _next_search_id(searches)
    rec = {"id": sid, "database": args.db, "query": args.query or "(see notes)", "date": args.date or dt.date.today().isoformat(),
           "run_by": args.by, "hits": int(total), "retrieved": len(records),
           "for": [x.strip() for x in (args.for_ or "").split(",") if x.strip()]}
    if args.years:
        rec["filters"] = {"years": args.years}
    if file:
        rec["file"] = file
    if getattr(args, "strategy", None):
        pr = args.protocol or {}
        rec["strategy"] = args.strategy
        rec["protocol"] = {"version": pr.get("version"), "fingerprint": pr.get("fingerprint"),
                           "commit": pr.get("commit"), "locked": bool(pr.get("locked"))}
    if args.notes:
        rec["notes"] = args.notes
    # what the benchmark (legacy includes) says about this run, before anything is merged
    lo_y, hi_y = S.year_window(args.years)
    in_win = (lambda c: not ((lo_y and (c.get("year") or 9999) < lo_y) or (hi_y and (c.get("year") or 0) > hi_y)))
    bench_every = [c for c in candidates if S.is_benchmark(c) and not c.get("duplicate_of")]
    bench_all = [c for c in bench_every if in_win(c)]
    bench_hit = [c for c in S.benchmark_hits(records, candidates) if in_win(c)]
    before = len(candidates)
    new, known = add_records(records, sid, candidates, abstracts)
    print(f"{sid} {args.db}: {total} hits, {len(records)} retrieved → {new} new candidates, {known} already in the register"
          + (f" · OpenAlex usage ${LAST_COST[0]:.3f}" if args.db == "openalex" and LAST_COST[0] else ""))
    if bench_all:
        line = (f"  benchmark: {len(bench_hit)} of {len(bench_all)} legacy-included papers retrieved"
                + (f" ({len(bench_every) - len(bench_all)} published outside {args.years} not counted)"
                   if len(bench_every) > len(bench_all) else ""))
        if getattr(args, "strategy", None):
            st = S.strategy(S.load_strategies(), args.strategy)
            want = set(st.get("buckets") or [])
            if want:
                buckets = S.kb_buckets()
                scope = [c for c in bench_all if want & buckets.get(c.get("key") or "", set())]
                got = {c["id"] for c in bench_hit}
                missed = [c for c in scope if c["id"] not in got]
                line += (f"; {len(scope) - len(missed)} of {len(scope)} in this strategy's folders ({', '.join(sorted(want))})"
                         + (f" = {100 * (len(scope) - len(missed)) / len(scope):.0f}%" if scope else "")
                         + " — this strategy alone; `screen.py recall` gives the union of all runs")
                if missed and not args.execute:
                    print(line)
                    line = ""
                    print("  not retrieved (check: out of scope under §2, or a missing term?):")
                    for c in missed[:40]:
                        print(f"    {c['id']}  {str(c.get('key') or ''):<26} {str(c.get('year') or ''):<5} {str(c.get('title') or '')[:90]}")
                    if len(missed) > 40:
                        print(f"    … {len(missed) - 40} more")
        if line:
            print(line)
    if total and len(records) < total and args.db in ("pubmed", "openalex"):
        msg = f"  only {len(records)} of {total} hits were retrieved"
        if args.db == "pubmed" and LAST_MISSING:
            msg += f" (PMIDs PubMed counted but did not return: {', '.join(LAST_MISSING[:20])}{' …' if len(LAST_MISSING) > 20 else ''})"
        if getattr(args, "strategy", None) and args.execute:
            raise SystemExit(msg + " — a protocol search must be complete; check --max and the network, then re-run.")
        print(msg + " (raise --max)")
    if not args.execute:
        print("Dry run — nothing written. Add --execute.")
        return 0
    searches.append(rec)
    S.save_searches(searches)
    S.save_candidates(candidates)
    save_abstracts(abstracts)
    strat = f" | strategy {args.strategy} v{(args.protocol or {}).get('version')} {(args.protocol or {}).get('fingerprint')}" \
        if getattr(args, "strategy", None) else ""
    _log("SEARCHED", f"{sid} {args.db}", f"{len(records)} records | {new} new candidates (register {before}→{len(candidates)}){strat} | by: {args.by}")
    return 0


def cmd_backfill(args) -> int:
    candidates, added = S.backfill_candidates(ROOT, by="legacy", date=args.date)
    print(f"{added} bibliography entries {'would be ' if not args.execute else ''}added to the register as 'other sources' "
          f"(decisions stamped by: legacy, so the register never claims a person screened them).")
    if args.execute and added:
        S.save_candidates(candidates)
        _log("SCREEN-BACKFILL", "screening register", f"{added} citations.md entries added as other-source candidates")
    return 0


def cmd_strategies(args) -> int:
    strategies = S.load_strategies()
    if args.show:
        db = args.db or "pubmed"
        try:
            print(S.query_for_run(strategies, args.show, db))
        except KeyError as e:
            raise SystemExit(str(e).strip('"'))
        yrs = S.strategy_years(strategies, args.show)
        if yrs and db != "scopus":
            print(f"# publication years {yrs}: `screen.py search` applies them as a filter; set the same limit "
                  f"by hand when running this string in the database's own interface", file=sys.stderr)
        return 0
    st = S.protocol_state()
    lock = "LOCKED" if st["locked"] else "not locked"
    print(f"Protocol v{st['version']} · years {strategies.get('years') or 'all'} · status {st['status']} · fingerprint {st['fingerprint']} · "
          f"{'committed' if st['committed'] else ('uncommitted changes' if st['committed'] is False else 'git unknown')}"
          f"{' @ ' + st['commit'] if st['commit'] else ''} → {lock}")
    runs = S.load_searches()
    for x in strategies.get("strategies") or []:
        done = [r for r in runs if r.get("strategy") == x.get("id")]
        dbs = ", ".join(f"{r.get('database')} {r.get('date')} ({r.get('retrieved')})" for r in done) or "not run"
        have = "/".join(k for k in ("pubmed", "openalex", "scopus", "psycinfo") if x.get(k))
        print(f"  {x.get('id'):<46} {have:<22} {dbs}")
        if args.verbose:
            for db in ("pubmed", "openalex", "scopus", "psycinfo"):
                if x.get(db):
                    print(f"      {db}: {S.query_for_run(strategies, x['id'], db)}")
    return 0


def cmd_rebaseline(args) -> int:
    candidates = S.load_candidates()
    st = S.protocol_state()
    today = args.date or dt.date.today().isoformat()
    out = S.rebaseline(candidates, today, protocol=st["fingerprint"])
    print(f"{out['candidates']} candidates carry legacy decisions: {out['benchmark']} legacy includes become the benchmark set, "
          f"{out['refused']} legacy refusals are re-opened; every one is screened afresh under protocol v{st['version']} "
          f"({st['fingerprint']}). The legacy decisions move to `legacy` on each candidate; nothing is deleted.")
    print("  After this, a legacy paper that a protocol search finds is screened at title/abstract like any database record;\n"
          "  one no search finds stays in the other-methods arm, awaiting full-text assessment.")
    if not args.execute:
        print("Dry run — nothing written. Add --execute.")
        return 0
    if out["candidates"]:
        S.save_candidates(candidates)
        _log("SCREEN-REBASELINE", "screening register",
             f"{out['candidates']} legacy decisions moved to `legacy` | benchmark {out['benchmark']} | protocol {st['fingerprint']}")
    return 0


def cmd_recall(args) -> int:
    data = S.recall(S.load_candidates(), S.load_searches(), S.load_strategies(), S.kb_buckets())
    if args.json:
        print(json.dumps(data, indent=1, default=str))
        return 0
    print_recall(data, verbose=True)
    return 0


def print_recall(data: dict, verbose: bool = False) -> None:
    if not data["benchmark"]:
        print("  Recall: no benchmark set (run `screen.py rebaseline` after `backfill`).")
        return
    if data["recall"] is None:
        out = len(data.get("outsideWindow") or [])
        print(f"  Recall: benchmark of {data['benchmark']} legacy-included papers"
              + (f" ({out} more published outside {data.get('window')})" if out else "") + "; no database search run yet.")
        return
    print(f"  Recall against the benchmark: {data['found']} of {data['benchmark']} legacy-included papers found by a database "
          f"search ({100 * data['recall']:.0f}%) · by database: " + (", ".join(f"{k} {v}" for k, v in data["byDatabase"].items()) or "—"))
    left = []
    if data.get("outsideWindow"):
        left.append(f"{len(data['outsideWindow'])} published outside {data.get('window')}")
    if data.get("excludedUnderProtocol"):
        left.append(f"{len(data['excludedUnderProtocol'])} since excluded at full text")
    if left:
        print(f"    (of {data.get('benchmarkAll')} benchmark papers; not counted: {', '.join(left)})")
    if not verbose:
        return
    for x in data["byStrategy"]:
        if not x["inScope"]:
            continue
        r = "not run" if x["recall"] is None else f"{x['found']}/{x['inScope']} = {100 * x['recall']:.0f}%"
        print(f"    {x['id']:<46} {r:<16} {', '.join(x['databases'])}")
    if data.get("outsideWindow"):
        print("  Outside the publication years (citation chasing if a pillar — `screen.py chase`):")
        for m in data["outsideWindow"]:
            print(f"    {m['id']}  {str(m.get('key') or ''):<26} {str(m.get('year') or ''):<5} {str(m.get('title') or '')[:80]}")
    if data["missed"]:
        print(f"  Not found by any search ({len(data['missed'])}) — classify each: out of scope under §2 (exclude it at "
              f"full text with that reason), a search gap (amend the strategy), or a pillar (`screen.py chase`):")
        for m in data["missed"]:
            print(f"    {m['id']}  {str(m.get('key') or ''):<26} {','.join(m['buckets']) or '—':<22} {str(m.get('title') or '')[:80]}")


def cmd_agreement(args) -> int:
    stages = [S.STAGES[0] if args.stage in ("ta", "title_abstract") else "full_text"] if args.stage else list(S.STAGES)
    cands = S.load_candidates()
    for stg in stages:
        a = S.agreement(cands, stg)
        if not a["pairs"]:
            print(f"{STAGE_TEXT[stg]}: no double-screened candidates yet.")
            continue
        print(f"{STAGE_TEXT[stg]}: {a['pairs']} double-screened ({', '.join(a['screeners'])}) · observed agreement "
              f"{100 * a['observed']:.0f}% · Cohen's kappa {a['kappa']:.2f}" + (f" · {a['skipped']} with an unsure left out" if a["skipped"] else ""))
        print("  " + " · ".join(f"{k} {v}" for k, v in a["table"].items()) + "   (record/check)")
        if len(a.get("byCheckScreener") or {}) > 1:
            print("  by second screener: " + " · ".join(f"{w} {v['pairs']} pairs, kappa {v['kappa']:.2f}"
                                                      for w, v in a["byCheckScreener"].items()))
        for d in a["disagreements"]:
            print(f"    {d['id']}  record {d['record']}{'/' + d['record_reason'] if d.get('record_reason') else ''} · "
                  f"check {d['check']}{'/' + d['check_reason'] if d.get('check_reason') else ''}  {str(d.get('title') or '')[:70]}")
        if a["disagreements"]:
            print("  Reconcile by discussion; record the agreed decision with `decide` (no --role) — it becomes the decision of record.")
    return 0


def cmd_chase(args) -> int:
    """A pillar paper the searches cannot return (before the publication years, a
    primary healthy-volunteer study, a record without an abstract, a review without
    the search terms) enters by citation chasing from included papers, with the
    reason it is needed. It goes to full-text assessment in the other-methods arm."""
    candidates = S.load_candidates()
    by_id = {c["id"]: c for c in candidates}
    cited_by = [x.strip() for x in (args.cited_by or "").split(",") if x.strip()]
    if not cited_by:
        raise SystemExit("--cited-by needs at least one candidate id of an included paper that cites it")
    if not args.why or len(args.why.strip()) < 20:
        raise SystemExit("--why must say what the KB needs this paper for (which entry or claim), in a sentence")
    if not args.by or args.by.lower() in ("model", "legacy", "agent"):
        raise SystemExit("--by must name a person")
    bad = []
    for cid in cited_by:
        c = by_id.get(cid)
        d = S.last_decision(c, "full_text") if c else None
        if not c:
            bad.append(f"{cid}: not in the register")
        elif not d or d.get("decision") != "include" or str(d.get("by")).lower() == "legacy":
            bad.append(f"{cid}: not included under the protocol yet (full-text include by a person)")
    if bad:
        raise SystemExit("Citation chasing starts from included papers:\n  " + "\n  ".join(bad))
    doi = S.norm_doi(args.doi)
    probe = {"doi": doi, "title": args.title, "year": int(args.year) if args.year else None}
    target = S.find_duplicate(probe, S.build_identity_index(candidates)) if (doi or args.title) else None
    if target is not None and S.arm_of(target) == "databases":
        print(f"{target['id']} was found by a database search ({', '.join(str(x.get('search')) for x in target.get('sources') or [] if isinstance(x, dict) and x.get('search'))}); "
              f"it is screened in the databases arm — no citation chasing needed.")
        return 0
    if target is None:
        rec = {"title": args.title, "year": probe["year"], "doi": doi}
        if doi and not (args.title and args.year):
            try:
                import register_papers as RP
                cr = RP.lookup(doi)
            except Exception as e:  # noqa: BLE001
                raise SystemExit(f"Crossref could not be reached ({str(e)[:60]}); give --title and --year")
            if cr is None:
                raise SystemExit(f"DOI {doi} not found at Crossref; give --title and --year")
            _, first = RP._author_line(cr)
            rec.update({"title": " ".join(cr.get("title") or [""]).rstrip(".") or args.title,
                        "year": int(RP._year(cr)) if str(RP._year(cr)).isdigit() else probe["year"],
                        "first_author": first or None})
        if not rec.get("title"):
            raise SystemExit("give --doi (looked up at Crossref) or --title and --year")
        target = {k: v for k, v in {"id": S.next_id(candidates), "doi": doi, "title": rec["title"], "year": rec["year"],
                                    "first_author": rec.get("first_author"), "sources": [], "skip_title_abstract": True,
                                    "screening": []}.items() if v not in (None, "")}
        target.setdefault("sources", [])
        target.setdefault("screening", [])
        candidates.append(target)
        new = True
    else:
        new = False
    src = {"kind": "citation_chasing", "cited_by": cited_by, "why": args.why.strip(), "by": args.by,
           "date": args.date or dt.date.today().isoformat()}
    target.setdefault("sources", []).append(src)
    target["pillar"] = True
    target["skip_title_abstract"] = True
    print(f"{'new candidate' if new else 'existing candidate'} {target['id']} ({target.get('year')}) {str(target.get('title'))[:80]}\n"
          f"  citation chasing from {', '.join(cited_by)}: {args.why.strip()}\n"
          f"  → full-text assessment (other-methods arm); the year window and the healthy-volunteer rule do not apply to a pillar.")
    if not args.execute:
        print("Dry run — nothing written. Add --execute.")
        return 0
    S.save_candidates(candidates)
    _log("CHASED", target["id"], f"cited by {', '.join(cited_by)} | {args.why.strip()[:120]} | by: {args.by}")
    return 0


# ---------------------------------------------------------------------------
# screening: model suggestion, sheet, decisions
# ---------------------------------------------------------------------------

SUGGEST_SCHEMA = {"type": "object", "required": ["decision", "reason", "rationale"],
                  "properties": {"decision": {"type": "string", "enum": ["include", "exclude", "unsure"]},
                                 "reason": {"type": "string", "enum": [k for k, v in S.REASONS.items() if not v["ft_only"]] + ["none"]},
                                 "rationale": {"type": "string"}}}


def _criteria_text() -> str:
    path = ROOT / "docs/SCREENING.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## 2\..*?(?=^## 3\.)", text, re.S | re.M)
    return m.group(0) if m else text[:6000]


def cmd_assist(args) -> int:
    import model_config  # noqa: WPS433
    import ollama_client
    try:
        spec = model_config.resolve("screen", args.model)
    except Exception:  # noqa: BLE001
        spec = model_config.resolve("review", args.model)
    candidates = S.load_candidates()
    abstracts = load_abstracts()
    facts = S.kb_facts()
    rows = {r["id"]: r for r in S.enrich(candidates, facts)}
    todo = [c for c in candidates if rows[c["id"]]["stage"] == "awaiting_ta" and (not c.get("suggestion") or args.redo)]
    if args.ids:
        want = set(args.ids.split(","))
        todo = [c for c in candidates if c["id"] in want]
    if not todo:
        print("Nothing awaiting a title/abstract suggestion.")
        return 0
    system = ("You are helping screen titles and abstracts for a knowledge base of stroke aphasia evidence. "
              "Apply the eligibility criteria below strictly and answer with JSON: decision (include / exclude / unsure), "
              "reason (one exclusion reason id, or 'none' when including), and a one-sentence rationale. "
              "When the abstract does not let you decide, say unsure. Your answer is a suggestion; a person decides.\n\n"
              + _criteria_text())
    done = 0
    for c in todo[: args.max]:
        prompt = (f"Title: {c.get('title')}\nYear: {c.get('year')}\nJournal: {c.get('journal') or 'unknown'}\n"
                  f"Abstract: {abstracts.get(c['id']) or '(no abstract available)'}\n")
        try:
            res = ollama_client.chat(prompt, model=spec["model"], system=system, max_tokens=400, fmt=SUGGEST_SCHEMA, verbose=False)
            ans = json.loads(res["text"])
        except Exception as e:  # noqa: BLE001
            print(f"  {c['id']}: model failed ({str(e)[:80]})")
            continue
        c["suggestion"] = {"stage": "title_abstract", "decision": ans.get("decision"), "reason": ans.get("reason"),
                           "rationale": str(ans.get("rationale") or "")[:400], "model": spec["model"], "date": dt.date.today().isoformat()}
        print(f"  {c['id']}: {ans.get('decision'):8} {ans.get('reason') or '':22} {str(c.get('title'))[:70]}")
        done += 1
        if done % 10 == 0:
            S.save_candidates(candidates)
    S.save_candidates(candidates)
    _log("SUGGESTED", "title/abstract", f"{done} suggestions by model:{spec['model']} (suggestions only; no decision)")
    print(f"{done} suggestions written (model:{spec['model']}). They are suggestions; decide in the sheet.")
    return 0


SHEET_CSS = """
body{font:15px/1.5 Inter,"Helvetica Neue",Arial,sans-serif;color:#2b2b3a;margin:0;background:#fff}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid #ebebeb;padding:.6rem 1rem;display:flex;gap:1rem;align-items:center;flex-wrap:wrap;z-index:5}
h1{font-size:1.1rem;color:#52489c;margin:0}
main{max-width:980px;margin:0 auto;padding:1rem}
article{border:1px solid #ebebeb;border-radius:6px;padding:.8rem 1rem;margin:.7rem 0}
article.decided{opacity:.6}
article:focus-within{border-color:#52489c;box-shadow:0 0 0 3px rgba(82,72,156,.12)}
.t{font-weight:600;margin:0 0 .2rem}
.m{font-size:.84rem;color:#5a5a66}
.ab{font-size:.92rem;margin:.5rem 0}
.sug{font-size:.84rem;background:rgba(64,98,187,.09);border-left:3px solid #4062bb;padding:.3rem .6rem;border-radius:0 4px 4px 0}
.dec{display:flex;gap:.8rem;flex-wrap:wrap;align-items:center;font-size:.9rem;margin-top:.5rem}
.dec label{cursor:pointer}
input[type=radio]{accent-color:#52489c}
select,input[type=text]{font:inherit;font-size:.85rem;padding:.2rem .4rem;border:1px solid #d6d6d6;border-radius:4px}
input[type=text]{min-width:260px}
button{font:inherit;padding:.35rem .8rem;border-radius:6px;border:1px solid #52489c;background:#52489c;color:#fff;cursor:pointer}
button.alt{background:#fff;color:#52489c}
.n{font-variant-numeric:tabular-nums;color:#5a5a66}
.chip{font-family:ui-monospace,Menlo,monospace;font-size:.78rem;background:#f7f7f7;border:1px solid #d6d6d6;border-radius:4px;padding:.02rem .35rem}
kbd{font:inherit;font-size:.78rem;border:1px solid #d6d6d6;border-bottom-width:2px;border-radius:3px;padding:0 .3rem;background:#f7f7f7}
.hide-decided article.decided{display:none}
"""

SHEET_JS = """
const KEY = 'screen-sheet:' + document.body.dataset.stage + ':' + document.body.dataset.built;
const form = document.getElementById('f');
function state(){ const o={}; for (const a of document.querySelectorAll('article')){ const id=a.dataset.id; const d=a.querySelector('input[type=radio]:checked'); o[id]={decision:d?d.value:'', reason:a.querySelector('select').value, note:a.querySelector('input[type=text]').value}; } return o; }
function apply(o){ for (const a of document.querySelectorAll('article')){ const s=o[a.dataset.id]; if(!s) continue; const r=a.querySelector(`input[type=radio][value="${s.decision}"]`); if(r) r.checked=true; a.querySelector('select').value=s.reason||''; a.querySelector('input[type=text]').value=s.note||''; } }
function refresh(){ let n=0; for (const a of document.querySelectorAll('article')){ const d=a.querySelector('input[type=radio]:checked'); a.classList.toggle('decided', Boolean(d)); if(d) n++; const sel=a.querySelector('select'); sel.disabled = !d || d.value!=='exclude'; } document.getElementById('count').textContent = `${n} of ${document.querySelectorAll('article').length} decided`; try{ localStorage.setItem(KEY, JSON.stringify(state())); }catch(e){} }
form.addEventListener('change', refresh);
form.addEventListener('input', refresh);
try{ const saved=localStorage.getItem(KEY); if(saved) apply(JSON.parse(saved)); }catch(e){}
refresh();
document.getElementById('hide').addEventListener('change', (e)=>document.body.classList.toggle('hide-decided', e.target.checked));
document.getElementById('dl').addEventListener('click', ()=>{ const o=state(); const rows=[['id','stage','decision','reason','note']]; for (const [id,s] of Object.entries(o)){ if(!s.decision) continue; if(s.decision==='exclude' && !s.reason){ alert(id+': an exclusion needs a reason'); return; } rows.push([id, document.body.dataset.stage, s.decision, s.decision==='exclude'?s.reason:'', s.note]); } const csv=rows.map(r=>r.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\\n'); const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv'})); a.download='decisions_'+document.body.dataset.stage+'_'+new Date().toISOString().slice(0,10)+'.csv'; a.click(); });
document.addEventListener('keydown', (e)=>{ if (e.target.tagName==='INPUT' && e.target.type==='text') return; const a=document.activeElement.closest ? document.activeElement.closest('article') : null; if(!a) return; const map={i:'include',e:'exclude',u:'unsure'}; if(map[e.key]){ const r=a.querySelector(`input[type=radio][value="${map[e.key]}"]`); if(r){ r.checked=true; refresh(); if(e.key!=='e'){ const next=a.nextElementSibling; if(next){ next.setAttribute('tabindex','-1'); next.focus(); next.scrollIntoView({block:'center'});} } else { a.querySelector('select').focus(); } } e.preventDefault(); } });
for (const a of document.querySelectorAll('article')) a.setAttribute('tabindex','-1');
"""


def cmd_sheet(args) -> int:
    stage = "full_text" if args.stage in ("ft", "full_text") else "title_abstract"
    candidates = S.load_candidates()
    abstracts = load_abstracts()
    rows = {r["id"]: r for r in S.enrich(candidates, S.kb_facts())}
    want = {"title_abstract": ("awaiting_ta", "unsure_ta"), "full_text": ("awaiting_ft", "unsure_ft")}[stage]
    if args.check:
        # a second screener's blind sample: candidates that already have a decision of record
        # at this stage and no check decision yet
        import random
        pool = [c for c in candidates if (d := S.last_decision(c, stage)) and str(d.get("by")).lower() != "legacy"
                and not S.last_decision(c, stage, role=S.CHECK_ROLE)]
        random.Random(args.seed).shuffle(pool)
        k = round(len(pool) * args.sample) if args.sample and args.sample < 1 else int(args.sample or len(pool))
        todo = sorted(pool[:k], key=lambda c: c["id"])
    else:
        todo = [c for c in candidates if rows[c["id"]]["stage"] in want]
    if args.for_:
        searches = {s["id"]: s for s in S.load_searches()}
        want_for = set(args.for_.split(","))

        def serves(c):
            ids = set(str(x) for x in (c.get("for") or []))
            for s in c.get("sources") or []:
                if isinstance(s, dict) and s.get("search"):
                    ids.update(str(x) for x in (searches.get(s["search"]) or {}).get("for") or [])
            return bool(ids & want_for)
        todo = [c for c in todo if serves(c)]
    if args.ids:
        keep = set(args.ids.split(","))
        todo = [c for c in todo if c["id"] in keep]
    if not todo:
        print(f"No {STAGE_TEXT[stage]} decisions of record without a check decision yet." if args.check
              else f"Nothing awaiting {STAGE_TEXT[stage]} screening.")
        return 0
    reasons = [(k, v["label"]) for k, v in S.REASONS.items() if stage == "full_text" or not v["ft_only"]]
    built = dt.datetime.now().isoformat(timespec="minutes")
    parts = [f"<!doctype html><html lang=en><head><meta charset=utf-8><title>Screening — {STAGE_TEXT[stage]}</title>"
             f"<style>{SHEET_CSS}</style></head><body data-stage=\"{stage}\" data-built=\"{html.escape(built)}\">"
             f"<header><h1>Screening · {STAGE_TEXT[stage]}</h1><span class=n id=count></span>"
             f"<label><input type=checkbox id=hide> hide decided</label>"
             f"<button id=dl type=button>Download decisions CSV</button>"
             f"<span class=m>Keys: <kbd>i</kbd> include · <kbd>e</kbd> exclude (then pick a reason) · <kbd>u</kbd> unsure · click a card first. "
             f"Then: <code>python scripts/screen.py decide --csv &lt;file&gt; --by &lt;you&gt;</code></span></header><main><form id=f>"]
    for c in todo:
        r = rows[c["id"]]
        doi = c.get("doi")
        sug = c.get("suggestion") if stage == "title_abstract" and not args.check else None
        meta = " · ".join(x for x in [str(c.get("year") or ""), c.get("journal") or "", (c.get("authors") or "")[:120]] if x)
        # Blind screening: at title/abstract, and in a check sheet, the screener sees the record as
        # the search returned it — no citation key, no "hand-picked"/legacy provenance.
        blind = stage == "title_abstract" or args.check
        srcs = ", ".join((s.get("search") or ("" if blind else S.SOURCE_KINDS.get(s.get("kind"), s.get("kind"))))
                         for s in (c.get("sources") or []) if isinstance(s, dict) and (s.get("search") or not blind))
        prev = ""
        if stage == "full_text" and not args.check:
            ta = S.last_decision(c, "title_abstract")
            if ta:
                prev = f" · title/abstract: {ta.get('decision')} by {ta.get('by')}"
        cid = c["id"]
        e = html.escape
        links = ""
        if doi:
            links += " · <a href=\"https://doi.org/" + e(doi) + "\" target=_blank rel=noopener>" + e(doi) + "</a>"
        if c.get("pmid"):
            pm = e(str(c["pmid"]))
            links += " · PMID <a href=\"https://pubmed.ncbi.nlm.nih.gov/" + pm + "\" target=_blank rel=noopener>" + pm + "</a>"
        key = (" · " + e(str(c["key"]))) if c.get("key") and not blind else ""
        abstract = abstracts.get(cid) or "(no abstract in the local cache — run `python scripts/screen.py fetch-abstracts`)"
        sug_html = ""
        if sug:
            reason = ""
            if sug.get("reason") and sug.get("reason") != "none":
                reason = " (" + e(S.REASONS.get(sug.get("reason"), {}).get("label", str(sug.get("reason")))) + ")"
            sug_html = ("<p class=sug>Model suggests <b>" + e(str(sug.get("decision"))) + "</b>" + reason + " — "
                        + e(str(sug.get("rationale") or "")) + " <span class=m>[" + e(str(sug.get("model")))
                        + "; a suggestion, not a decision]</span></p>")
        radios = "".join("<label><input type=radio name=\"d-" + cid + "\" value=\"" + d + "\"> " + d + "</label>" for d in ("include", "exclude", "unsure"))
        options = "".join("<option value=\"" + k + "\">" + e(l) + "</option>" for k, l in reasons)
        parts.append("<article data-id=\"" + cid + "\"><p class=t><span class=chip>" + cid + "</span> " + e(str(c.get("title") or "")) + "</p>"
                     + "<p class=m>" + e(meta) + links + " · from " + e(srcs or "unknown") + e(prev) + key + "</p>"
                     + "<p class=ab>" + e(abstract) + "</p>" + sug_html
                     + "<div class=dec>" + radios
                     + "<select name=\"r-" + cid + "\" aria-label=\"exclusion reason\"><option value=\"\">reason…</option>" + options + "</select>"
                     + "<input type=text name=\"n-" + cid + "\" placeholder=\"note (required for 'other' and duplicate_report)\"></div></article>")
    parts.append(f"</form></main><script>{SHEET_JS}</script></body></html>")
    SHEET_DIR.mkdir(parents=True, exist_ok=True)
    out = Path(args.out) if args.out else SHEET_DIR / (f"{stage}_check.html" if args.check else f"{stage}.html")
    out.write_text("".join(parts), encoding="utf-8")
    print(f"{out}: {len(todo)} candidates to screen at {STAGE_TEXT[stage]}. Open it, decide, download the CSV, then\n"
          f"  python scripts/screen.py decide --csv <downloaded file> --by <your name>" + (" --role check" if args.check else ""))
    return 0


def _apply_decision(c: dict, stage: str, decision: str, reason: str | None, by: str, note: str | None, date: str,
                    role: str | None = None) -> str | None:
    if stage not in S.STAGES:
        return f"stage must be one of {S.STAGES}"
    if decision not in S.DECISIONS:
        return f"decision must be one of {S.DECISIONS}"
    if decision == "exclude":
        if reason not in S.REASONS:
            return f"an exclusion needs a reason from docs/SCREENING.md: {', '.join(S.REASONS)}"
        if S.REASONS[reason]["ft_only"] and stage != "full_text":
            return f"reason {reason} applies at full text only"
        if reason in ("other", "duplicate_report") and not note:
            return f"reason {reason} needs a note"
    else:
        reason = None
    if not by or by.lower() in ("model", "legacy", "agent"):
        return "--by must name a person"
    if role:
        if role != S.CHECK_ROLE:
            return f"--role must be {S.CHECK_ROLE}"
        rec_d = S.last_decision(c, stage)
        if rec_d and str(rec_d.get("by") or "").lower() == by.lower():
            return "a check decision must come from a different person than the decision of record"
    rec = {"stage": stage, "decision": decision}
    if role:
        rec["role"] = role
    if reason:
        rec["reason"] = reason
    rec.update({"by": by, "date": date})
    if note:
        rec["note"] = note
    c.setdefault("screening", []).append(rec)
    return None


def cmd_decide(args) -> int:
    candidates = S.load_candidates()
    by_id = {c["id"]: c for c in candidates}
    today = args.date or dt.date.today().isoformat()
    todo: list[tuple[str, str, str, str | None, str | None]] = []
    if args.csv:
        with open(args.csv, newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                todo.append((row.get("id", "").strip(), row.get("stage", "").strip() or "title_abstract", row.get("decision", "").strip(),
                             (row.get("reason") or "").strip() or None, (row.get("note") or "").strip() or None))
    elif args.id:
        todo.append((args.id, "full_text" if args.stage in ("ft", "full_text") else "title_abstract", args.decision, args.reason, args.note))
    else:
        raise SystemExit("give --csv FILE or --id/--stage/--decision")
    applied, errors = 0, 0
    counts: dict[str, int] = {}
    for cid, stage, decision, reason, note in todo:
        c = by_id.get(cid)
        if c is None:
            print(f"  {cid}: not in the register", file=sys.stderr)
            errors += 1
            continue
        err = _apply_decision(c, stage, decision, reason, args.by, note, today, role=args.role)
        if err:
            print(f"  {cid}: {err}", file=sys.stderr)
            errors += 1
            continue
        counts[f"{stage}:{decision}"] = counts.get(f"{stage}:{decision}", 0) + 1
        applied += 1
    if applied:
        S.save_candidates(candidates)
        _log("SCREEN-CHECKED" if args.role else "SCREENED", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())),
             f"{applied} decisions | by: {args.by}")
    print(f"{applied} decisions recorded for {args.by}" + (f"; {errors} rejected (see above)" if errors else ""))
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# hand-over: included candidates → citations.md
# ---------------------------------------------------------------------------

def cmd_register(args) -> int:
    import register_papers as RP
    candidates = S.load_candidates()
    cites = S.citation_blocks()
    by_doi = {v["doi"]: k for k, v in cites.items() if v.get("doi")}
    rows = {r["id"]: r for r in S.enrich(candidates, S.kb_facts())}
    todo = [c for c in candidates if rows[c["id"]]["stage"] == "included" and not c.get("key")]
    blocks, linked, manual = [], 0, []
    existing = {k: {"doi": v.get("doi")} for k, v in cites.items()}
    for c in todo:
        doi = c.get("doi")
        if doi and doi in by_doi:
            c["key"] = by_doi[doi]
            linked += 1
            continue
        if not doi:
            manual.append((c["id"], "no DOI — add a citations.md block by hand and set `key:` on the candidate"))
            continue
        try:
            rec = RP.lookup(doi)
        except Exception as e:  # noqa: BLE001
            manual.append((c["id"], f"Crossref unreachable ({str(e)[:60]})"))
            continue
        if rec is None:
            manual.append((c["id"], f"DOI {doi} not found at Crossref"))
            continue
        _, first = RP._author_line(rec)
        title = " ".join(rec.get("title") or [""])
        key = RP.make_key(first, RP._year(rec), title, existing, doi)
        if not key:
            manual.append((c["id"], "Crossref record has no author/year"))
            continue
        block = RP.build_block(rec, key, doi, f"screening {c['id']}")
        block = block.replace("Check the entry; add a note on why the paper is in the KB.",
                              f"Included by the screening register ({c['id']}; docs/SCREENING.md). Check the entry.")
        blocks.append(block)
        existing[f"@{key}"] = {"doi": doi}
        c["key"] = f"@{key}"
        print(f"{'register' if args.execute else 'would register':16} {c['id']} → @{key}")
    for cid, why in manual:
        print(f"{'needs a hand':16} {cid}  ({why})")
    if not args.execute:
        print(f"Dry run: {len(blocks)} entries would be appended to citations.md, {linked} candidates linked to existing keys.")
        return 0
    if blocks:
        path = ROOT / "citations.md"
        text = path.read_text(encoding="utf-8").rstrip("\n") + "\n"
        if RP.SECTION not in text:
            text += (f"\n---\n\n{RP.SECTION}\n\n> Entries written by register_papers.py from the PDF's DOI, or by screen.py "
                     f"register for candidates the screening register included. Each says when.\n\n")
        else:
            text += "\n"
        text += "\n".join(blocks)
        path.write_text(text, encoding="utf-8")
    if blocks or linked:
        S.save_candidates(candidates)
        _log("REGISTERED", "screening → citations.md", f"{len(blocks)} entries appended, {linked} linked to existing keys")
    print(f"{len(blocks)} entries appended to citations.md; {linked} linked. Next: fetch the PDFs into papers/ and run intake_papers.py.")
    return 0


def cmd_fetch_abstracts(args) -> int:
    candidates = S.load_candidates()
    abstracts = load_abstracts()
    todo = [c for c in candidates if not abstracts.get(c["id"]) and (c.get("pmid") or c.get("doi"))]
    print(f"{len(todo)} candidates without a cached abstract")
    got = 0
    pm = [c for c in todo if c.get("pmid")]
    for i in range(0, len(pm), 100):
        batch = pm[i:i + 100]
        q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(str(c["pmid"]) for c in batch), "retmode": "xml",
                                    "tool": "stroke-aphasia-kb", "email": MAILTO})
        try:
            recs = {r["pmid"]: r for r in parse_pubmed_xml(_get(f"{EUTILS}efetch.fcgi?{q}", timeout=120))}
        except Exception as e:  # noqa: BLE001
            print(f"  PubMed failed: {str(e)[:80]}")
            break
        for c in batch:
            r = recs.get(str(c["pmid"]))
            if r and r.get("abstract"):
                abstracts[c["id"]] = r["abstract"]
                got += 1
        time.sleep(0.4)
    for c in [c for c in todo if not abstracts.get(c["id"]) and c.get("doi")][: args.max]:
        try:
            q = urllib.parse.urlencode({"filter": f"doi:{c['doi']}", "select": "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,ids,type", **_openalex_auth()})
            data = json.loads(_get(f"{OPENALEX}?{q}"))
            for w in data.get("results") or []:
                r = openalex_record(w)
                if r.get("abstract"):
                    abstracts[c["id"]] = r["abstract"]
                    got += 1
                for k in ("pmid", "openalex"):
                    if r.get(k) and not c.get(k):
                        c[k] = r[k]
            time.sleep(0.15)
        except Exception as e:  # noqa: BLE001
            print(f"  OpenAlex failed for {c['id']}: {str(e)[:80]}")
            break
    save_abstracts(abstracts)
    S.save_candidates(candidates)
    print(f"{got} abstracts cached in {S.ABSTRACTS.relative_to(ROOT)}")
    return 0


# ---------------------------------------------------------------------------
# status and listing
# ---------------------------------------------------------------------------

def print_status(data: dict) -> None:
    p = data["prisma"]
    idn, sc, ot, inc = p["identification"], p["screening"], p["other"], p["included"]
    pr = data.get("protocol") or {}
    print("Screening register (PRISMA 2020)")
    print(f"  Protocol v{pr.get('version')} · {pr.get('status')} · fingerprint {pr.get('fingerprint')}"
          f"{' · LOCKED' if pr.get('locked') else ' · not locked'}")
    print(f"  Identified: {idn['databases']['records']} records from {len(data['searches'])} database searches "
          f"({', '.join(f'{k} {v}' for k, v in idn['databases']['byDatabase'].items()) or 'none yet'}) · "
          f"{idn['other']['records']} from other sources ({', '.join(f'{k} {v}' for k, v in idn['other']['byKind'].items()) or 'none'}) · "
          f"{idn['duplicatesRemoved']} duplicates merged")
    print(f"  Databases arm: {sc['screened']} screened → {sc['excludedTitleAbstract']} excluded at title/abstract "
          f"({sc['awaitingTitleAbstract']} awaiting, {sc['unsureTitleAbstract']} unsure) → {sc['sought']} sought → "
          f"{sc['notRetrieved']} not retrieved → {sc['assessed']} assessed → {sc['excludedFullText']} excluded "
          f"({sc['awaitingFullText']} awaiting) → {sc['included']} included")
    print(f"  Other-sources arm: {ot['sought']} sought → {ot['notRetrieved']} not retrieved → {ot['assessed']} assessed → "
          f"{ot['excludedFullText']} excluded ({ot['awaitingFullText']} awaiting) → {ot['included']} included")
    for label, reasons in (("title/abstract", sc["excludedTitleAbstractReasons"]), ("full text", {**sc["excludedFullTextReasons"], **ot["excludedFullTextReasons"]})):
        if reasons:
            print(f"    exclusions at {label}: " + ", ".join(f"{S.REASONS.get(k, {}).get('label', k)} {v}" for k, v in reasons.items()))
    kb = inc["kb"]
    print(f"  Included {inc['total']}: in the KB {kb['in_kb']} ({inc['approvedFindings']} approved findings) · in review {kb['in_review']} · "
          f"awaiting extraction {kb['awaiting_extraction']} · no PDF {kb['no_pdf']} · not registered {kb['not_registered']} · "
          f"rejected {kb['rejected']} · refused {kb['refused']}")
    if data.get("recall"):
        print_recall(data["recall"])
    for stg, a in (data.get("agreement") or {}).items():
        if a.get("pairs"):
            print(f"  Dual screening at {STAGE_TEXT[stg]}: {a['pairs']} pairs, kappa {a['kappa']:.2f}")
    cov = [g for g in data["coverage"] if g.get("kind")]
    if cov:
        print("  Coverage of evidence gaps (found / included / in KB / approved findings):")
        for g in cov:
            print(f"    {g['id']:<44} {g['found']:>3} / {g['included']:>3} / {g['in_kb']:>3} / {g['approved_findings']:>3}   {g['kind']}")


def cmd_status(args) -> int:
    data = S.collect()
    if args.json:
        data.pop("facts", None)
        print(json.dumps(data, indent=1, default=str))
    else:
        print_status(data)
    return 0


def cmd_list(args) -> int:
    rows = S.enrich(S.load_candidates(), S.kb_facts())
    if args.stage:
        rows = [r for r in rows if r["stage"] == args.stage or (r["kb"] or {}).get("state") == args.stage]
    for r in rows:
        kb = r["kb"] or {}
        print(f"{r['id']}  {r['stage']:<14} {(kb.get('state') or ''):<20} {str(r.get('year') or ''):<5} {str(r.get('key') or ''):<28} {str(r.get('title') or '')[:80]}")
    print(f"{len(rows)} candidates")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common_ingest(p):
        p.add_argument("--db", required=True, help="pubmed | openalex (live) · scopus | embase | psycinfo | web_of_science | other (import)")
        p.add_argument("--query", help="the verbatim query string")
        p.add_argument("--years", help="e.g. 2000-2026")
        p.add_argument("--for", dest="for_", help="comma-separated evidence-gap ids / KB entry ids this search serves")
        p.add_argument("--by", default="unknown", help="who ran it")
        p.add_argument("--date", help="when (default today)")
        p.add_argument("--notes")
        p.add_argument("--strategy", help="a strategy id from screening/strategies.yaml (supplies the query, years and --for)")
        p.add_argument("--allow-unlocked", action="store_true", help="pilot run while the protocol is not locked (recorded as such)")
        p.add_argument("--execute", action="store_true")

    p = sub.add_parser("search", help="run a PubMed or OpenAlex search and add the hits to the register")
    common_ingest(p)
    p.add_argument("--max", type=int, default=None, help="cap on records (default 2000 ad hoc; none for a --strategy run)")
    p.add_argument("--oa-field", default="search", choices=("search", "title_and_abstract"),
                   help="OpenAlex: relevance search or boolean title+abstract filter (strategies always use the filter)")
    p.set_defaults(fn=cmd_search)
    p = sub.add_parser("import", help="import a RIS or CSV export (Scopus, Embase, PsycINFO, Web of Science …)")
    common_ingest(p)
    p.add_argument("--file", required=True)
    p.set_defaults(max=None)
    p.set_defaults(fn=cmd_import)
    p = sub.add_parser("backfill", help="add the existing citations.md entries as other-source candidates")
    p.add_argument("--date")
    p.add_argument("--execute", action="store_true")
    p.set_defaults(fn=cmd_backfill)
    p = sub.add_parser("strategies", help="the protocol's search strategies, fingerprint and lock state")
    p.add_argument("--show", metavar="ID", help="print one strategy's expanded query (for pasting into a database)")
    p.add_argument("--db", help="with --show: pubmed (default) | openalex | scopus | psycinfo")
    p.add_argument("-v", "--verbose", action="store_true", help="print every expanded query")
    p.set_defaults(fn=cmd_strategies)
    p = sub.add_parser("rebaseline", help="move legacy decisions aside; legacy includes become the recall benchmark")
    p.add_argument("--date")
    p.add_argument("--execute", action="store_true")
    p.set_defaults(fn=cmd_rebaseline)
    p = sub.add_parser("recall", help="relative recall of the database searches against the benchmark")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_recall)
    p = sub.add_parser("chase", help="enter a pillar paper by citation chasing from included papers (with the reason)")
    p.add_argument("--doi")
    p.add_argument("--title", help="when there is no DOI, or Crossref cannot be reached")
    p.add_argument("--year")
    p.add_argument("--cited-by", required=True, help="comma-separated candidate ids of included papers that cite it")
    p.add_argument("--why", required=True, help="what the KB needs it for (entry / claim)")
    p.add_argument("--by", required=True)
    p.add_argument("--date")
    p.add_argument("--execute", action="store_true")
    p.set_defaults(fn=cmd_chase)
    p = sub.add_parser("agreement", help="Cohen's kappa between decisions of record and a second screener's check decisions")
    p.add_argument("--stage", help="ta | ft (default both)")
    p.set_defaults(fn=cmd_agreement)
    p = sub.add_parser("assist", help="local model suggests include/exclude on title + abstract (suggestion only)")
    p.add_argument("--model")
    p.add_argument("--ids", help="comma-separated candidate ids (default: every one awaiting title/abstract)")
    p.add_argument("--max", type=int, default=100000)
    p.add_argument("--redo", action="store_true")
    p.set_defaults(fn=cmd_assist)
    p = sub.add_parser("sheet", help="write the HTML screening sheet")
    p.add_argument("--stage", default="title_abstract", help="title_abstract (ta) | full_text (ft)")
    p.add_argument("--for", dest="for_", help="only candidates serving these gap/entry ids")
    p.add_argument("--ids")
    p.add_argument("--out")
    p.add_argument("--check", action="store_true", help="a blind sheet for a second screener (already-decided candidates)")
    p.add_argument("--sample", type=float, default=0.2, help="with --check: a fraction (0.2) or a number (50) of candidates")
    p.add_argument("--seed", type=int, default=1, help="with --check: random seed, so the sample is reproducible")
    p.set_defaults(fn=cmd_sheet)
    p = sub.add_parser("decide", help="record decisions (from the sheet's CSV, or one by hand)")
    p.add_argument("--csv")
    p.add_argument("--id")
    p.add_argument("--stage", default="title_abstract")
    p.add_argument("--decision", choices=S.DECISIONS)
    p.add_argument("--reason", choices=list(S.REASONS))
    p.add_argument("--note")
    p.add_argument("--by", required=True, help="the person deciding")
    p.add_argument("--role", choices=[S.CHECK_ROLE], help="check: a second screener's independent decision (for kappa; not the decision of record)")
    p.add_argument("--date")
    p.set_defaults(fn=cmd_decide)
    p = sub.add_parser("register", help="included candidates without a key → citations.md entries (Crossref)")
    p.add_argument("--execute", action="store_true")
    p.set_defaults(fn=cmd_register)
    p = sub.add_parser("fetch-abstracts", help="fill the local abstract cache from PubMed / OpenAlex")
    p.add_argument("--max", type=int, default=500)
    p.set_defaults(fn=cmd_fetch_abstracts)
    p = sub.add_parser("status", help="the PRISMA numbers and gap coverage")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_status)
    p = sub.add_parser("list", help="candidates with their derived stage")
    p.add_argument("--stage", help="a stage (awaiting_ta, excluded_ta, awaiting_ft, included …) or KB state (in_kb, in_review, no_pdf …)")
    p.set_defaults(fn=cmd_list)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(_cli())
