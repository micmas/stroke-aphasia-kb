#!/usr/bin/env python3
"""
screen.py — systematic identification and screening of candidate papers
(SCREENING.md). Feeds the existing intake → extract → review → promote
pipeline; never writes to drafts/ or the canonical folders.

    # 1. identify
    python screen.py search --db pubmed --query '"aphasia"[tiab] AND stroke[tiab] AND (lesion[tiab] OR VLSM[tiab])' \
                            --years 2000-2026 --for thalamus_basal_ganglia --by michele --execute
    python screen.py search --db openalex --query 'aphasia stroke lesion symptom mapping' --years 2015-2026 --execute
    python screen.py import --file ~/Downloads/scopus.ris --db scopus --query '<the query you ran>' --for right_hemisphere --execute
    python screen.py backfill --execute       # the bibliography as it stood before the register (once)

    # 2. screen
    python screen.py assist                   # local model's opinion on every unscreened title/abstract (suggestion only)
    python screen.py sheet                    # screening/_sheet/title_abstract.html — decide, download the CSV
    python screen.py decide --csv ~/Downloads/decisions.csv --by michele
    python screen.py decide --id C0012 --stage full_text --decision exclude --reason not_retrieved --by michele
    python screen.py sheet --stage full_text  # the same for the full-text pass

    # 3. hand over
    python screen.py register --execute       # included candidates → citations.md entries (DOI via Crossref)
    python screen.py status                   # the PRISMA numbers; --json for scripts
    python screen.py list --stage awaiting_ft # what is waiting, with ids

Everything is a dry run unless --execute is given (decide applies at once;
it is the decision itself). Every applied step appends a line to
extraction_log.md. Decisions are made by a named person (--by); the model
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

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import screening as S  # noqa: E402

UA = "stroke-aphasia-kb screen.py/1.0 (mailto:m.massontrottier@uq.edu.au)"
MAILTO = "m.massontrottier@uq.edu.au"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OPENALEX = "https://api.openalex.org/works"
LOG = ROOT / "extraction_log.md"
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

def pubmed_search(query: str, years=(None, None), max_results: int = 2000) -> tuple[list[dict], int]:
    """E-utilities: esearch (history server) then efetch in batches of 200."""
    term = query
    lo, hi = years
    if lo or hi:
        term = f"({term}) AND ({lo or 1800}[dp] : {hi or 3000}[dp])"
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
    return out, total


def parse_pubmed_xml(data: bytes) -> list[dict]:
    out = []
    root = ET.fromstring(data)
    for art in root.iter("PubmedArticle"):
        pmid = (art.findtext(".//MedlineCitation/PMID") or "").strip()
        title = " ".join("".join(art.find(".//ArticleTitle").itertext()).split()) if art.find(".//ArticleTitle") is not None else ""
        parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            label = ab.get("Label")
            text = " ".join("".join(ab.itertext()).split())
            parts.append(f"{label}: {text}" if label else text)
        doi = None
        for eid in art.findall(".//ArticleIdList/ArticleId"):
            if eid.get("IdType") == "doi":
                doi = S.norm_doi(eid.text)
        if not doi:
            for el in art.findall(".//ELocationID"):
                if el.get("EIdType") == "doi":
                    doi = S.norm_doi(el.text)
        year = art.findtext(".//JournalIssue/PubDate/Year") or art.findtext(".//JournalIssue/PubDate/MedlineDate") or ""
        ym = re.search(r"(19|20)\d{2}", year)
        authors = []
        for a in art.findall(".//AuthorList/Author"):
            last, ini, coll = a.findtext("LastName"), a.findtext("Initials"), a.findtext("CollectiveName")
            if last:
                authors.append(f"{last} {ini or ''}".strip())
            elif coll:
                authors.append(coll)
        out.append({"pmid": pmid, "doi": doi, "title": title.rstrip("."), "year": int(ym.group(0)) if ym else None,
                    "authors": authors, "journal": art.findtext(".//Journal/Title") or "",
                    "abstract": " ".join(parts), "pub_types": [pt.text for pt in art.findall(".//PublicationTypeList/PublicationType") if pt.text]})
    return out


def _openalex_abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos: list[tuple[int, str]] = []
    for word, idxs in inv.items():
        for i in idxs:
            pos.append((i, word))
    return " ".join(w for _, w in sorted(pos))


def openalex_search(query: str, years=(None, None), max_results: int = 2000) -> tuple[list[dict], int]:
    lo, hi = years
    filters = ["type:article|review"]
    if lo or hi:
        filters.append(f"publication_year:{lo or 1800}-{hi or 3000}")
    out: list[dict] = []
    cursor, total = "*", 0
    while cursor and len(out) < max_results:
        q = urllib.parse.urlencode({"search": query, "filter": ",".join(filters), "per-page": 200, "cursor": cursor, "mailto": MAILTO,
                                    "select": "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,ids,type"})
        data = json.loads(_get(f"{OPENALEX}?{q}", timeout=120))
        total = int(data.get("meta", {}).get("count") or 0)
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


def cmd_search(args) -> int:
    years = _years(args.years)
    if not args.query:
        raise SystemExit("--query is required")
    try:
        if args.db == "pubmed":
            records, total = pubmed_search(args.query, years, args.max)
        elif args.db == "openalex":
            records, total = openalex_search(args.query, years, args.max)
        else:
            raise SystemExit("--db must be pubmed or openalex for a live search; use `import` for a file export")
    except (urllib.error.URLError, OSError) as e:
        raise SystemExit(f"{args.db} could not be reached ({e}). Run from a machine with network access, or run the "
                         f"search in the database's own interface and bring the export in with `screen.py import`.")
    return _ingest(args, records, total, file=None)


def cmd_import(args) -> int:
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
    if args.notes:
        rec["notes"] = args.notes
    before = len(candidates)
    new, known = add_records(records, sid, candidates, abstracts)
    print(f"{sid} {args.db}: {total} hits, {len(records)} retrieved → {new} new candidates, {known} already in the register")
    if not args.execute:
        print("Dry run — nothing written. Add --execute.")
        return 0
    searches.append(rec)
    S.save_searches(searches)
    S.save_candidates(candidates)
    save_abstracts(abstracts)
    _log("SEARCHED", f"{sid} {args.db}", f"{len(records)} records | {new} new candidates (register {before}→{len(candidates)}) | by: {args.by}")
    return 0


def cmd_backfill(args) -> int:
    candidates, added = S.backfill_candidates(ROOT, by="legacy", date=args.date)
    print(f"{added} bibliography entries {'would be ' if not args.execute else ''}added to the register as 'other sources' "
          f"(decisions stamped by: legacy, so the register never claims a person screened them).")
    if args.execute and added:
        S.save_candidates(candidates)
        _log("SCREEN-BACKFILL", "screening register", f"{added} citations.md entries added as other-source candidates")
    return 0


# ---------------------------------------------------------------------------
# screening: model suggestion, sheet, decisions
# ---------------------------------------------------------------------------

SUGGEST_SCHEMA = {"type": "object", "required": ["decision", "reason", "rationale"],
                  "properties": {"decision": {"type": "string", "enum": ["include", "exclude", "unsure"]},
                                 "reason": {"type": "string", "enum": [k for k, v in S.REASONS.items() if not v["ft_only"]] + ["none"]},
                                 "rationale": {"type": "string"}}}


def _criteria_text() -> str:
    path = ROOT / "SCREENING.md"
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
        print(f"Nothing awaiting {STAGE_TEXT[stage]} screening.")
        return 0
    reasons = [(k, v["label"]) for k, v in S.REASONS.items() if stage == "full_text" or not v["ft_only"]]
    built = dt.datetime.now().isoformat(timespec="minutes")
    parts = [f"<!doctype html><html lang=en><head><meta charset=utf-8><title>Screening — {STAGE_TEXT[stage]}</title>"
             f"<style>{SHEET_CSS}</style></head><body data-stage=\"{stage}\" data-built=\"{html.escape(built)}\">"
             f"<header><h1>Screening · {STAGE_TEXT[stage]}</h1><span class=n id=count></span>"
             f"<label><input type=checkbox id=hide> hide decided</label>"
             f"<button id=dl type=button>Download decisions CSV</button>"
             f"<span class=m>Keys: <kbd>i</kbd> include · <kbd>e</kbd> exclude (then pick a reason) · <kbd>u</kbd> unsure · click a card first. "
             f"Then: <code>python screen.py decide --csv &lt;file&gt; --by &lt;you&gt;</code></span></header><main><form id=f>"]
    for c in todo:
        r = rows[c["id"]]
        doi = c.get("doi")
        sug = c.get("suggestion") if stage == "title_abstract" else None
        meta = " · ".join(x for x in [str(c.get("year") or ""), c.get("journal") or "", (c.get("authors") or "")[:120]] if x)
        srcs = ", ".join((s.get("search") or S.SOURCE_KINDS.get(s.get("kind"), s.get("kind"))) for s in (c.get("sources") or []) if isinstance(s, dict))
        prev = ""
        if stage == "full_text":
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
        key = (" · " + e(str(c["key"]))) if c.get("key") else ""
        abstract = abstracts.get(cid) or "(no abstract in the local cache — run `python screen.py fetch-abstracts`)"
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
    out = Path(args.out) if args.out else SHEET_DIR / f"{stage}.html"
    out.write_text("".join(parts), encoding="utf-8")
    print(f"{out}: {len(todo)} candidates to screen at {STAGE_TEXT[stage]}. Open it, decide, download the CSV, then\n"
          f"  python screen.py decide --csv <downloaded file> --by <your name>")
    return 0


def _apply_decision(c: dict, stage: str, decision: str, reason: str | None, by: str, note: str | None, date: str) -> str | None:
    if stage not in S.STAGES:
        return f"stage must be one of {S.STAGES}"
    if decision not in S.DECISIONS:
        return f"decision must be one of {S.DECISIONS}"
    if decision == "exclude":
        if reason not in S.REASONS:
            return f"an exclusion needs a reason from SCREENING.md: {', '.join(S.REASONS)}"
        if S.REASONS[reason]["ft_only"] and stage != "full_text":
            return f"reason {reason} applies at full text only"
        if reason in ("other", "duplicate_report") and not note:
            return f"reason {reason} needs a note"
    else:
        reason = None
    if not by or by.lower() in ("model", "legacy", "agent"):
        return "--by must name a person"
    rec = {"stage": stage, "decision": decision}
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
        err = _apply_decision(c, stage, decision, reason, args.by, note, today)
        if err:
            print(f"  {cid}: {err}", file=sys.stderr)
            errors += 1
            continue
        counts[f"{stage}:{decision}"] = counts.get(f"{stage}:{decision}", 0) + 1
        applied += 1
    if applied:
        S.save_candidates(candidates)
        _log("SCREENED", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())), f"{applied} decisions | by: {args.by}")
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
                              f"Included by the screening register ({c['id']}; SCREENING.md). Check the entry.")
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
            q = urllib.parse.urlencode({"filter": f"doi:{c['doi']}", "select": "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,ids,type", "mailto": MAILTO})
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
    print("Screening register (PRISMA 2020)")
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
        p.add_argument("--execute", action="store_true")

    p = sub.add_parser("search", help="run a PubMed or OpenAlex search and add the hits to the register")
    common_ingest(p)
    p.add_argument("--max", type=int, default=2000)
    p.set_defaults(fn=cmd_search)
    p = sub.add_parser("import", help="import a RIS or CSV export (Scopus, Embase, PsycINFO, Web of Science …)")
    common_ingest(p)
    p.add_argument("--file", required=True)
    p.set_defaults(fn=cmd_import)
    p = sub.add_parser("backfill", help="add the existing citations.md entries as other-source candidates")
    p.add_argument("--date")
    p.add_argument("--execute", action="store_true")
    p.set_defaults(fn=cmd_backfill)
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
    p.set_defaults(fn=cmd_sheet)
    p = sub.add_parser("decide", help="record decisions (from the sheet's CSV, or one by hand)")
    p.add_argument("--csv")
    p.add_argument("--id")
    p.add_argument("--stage", default="title_abstract")
    p.add_argument("--decision", choices=S.DECISIONS)
    p.add_argument("--reason", choices=list(S.REASONS))
    p.add_argument("--note")
    p.add_argument("--by", required=True, help="the person deciding")
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
