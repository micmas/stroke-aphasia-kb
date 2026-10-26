#!/usr/bin/env python3
"""
screening.py — the screening register: what was searched, what was found,
what was included or excluded and why, and where each included paper now
stands in the knowledge base. The data contract behind screen.py, the
`screening` block of the webapp export and the explorer's Coverage view.

Two tracked files under screening/ (the protocol is docs/SCREENING.md):

* ``searches.yaml`` — one record per search run or file import: database,
  verbatim query, filters, date, hits, and ``for`` (the evidence gaps or
  KB entries the search serves).
* ``candidates.yaml`` — one record per de-duplicated candidate paper:
  identifiers, bibliographic fields, the sources it came from, and its
  screening history (title/abstract decision, then full-text decision —
  each with reason, who and when). A model's opinion, if asked for, is
  stored separately under ``suggestion`` and is never a decision.

Everything *after* inclusion is derived here from what already exists —
``citations.md`` (registered, refused), ``papers/`` (PDF present),
``drafts/`` (extracted, in review, rejected) and the canonical folders
(approved findings) — so there is one source of truth for each fact.

Nothing here calls a model or the network.
"""
from __future__ import annotations

import collections
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
from aphasia_kb import parse_markdown  # noqa: E402

DIR = ROOT / "screening"
SEARCHES = DIR / "searches.yaml"
CANDIDATES = DIR / "candidates.yaml"
ABSTRACTS = DIR / "abstracts.jsonl"          # local cache, git-ignored

CANONICAL_BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews")
DRAFT_BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews")

STAGES = ("title_abstract", "full_text")
DECISIONS = ("include", "exclude", "unsure")

# Exclusion reasons (docs/SCREENING.md §2). `ft_only` reasons apply at full text.
REASONS: dict[str, dict] = {
    "not_stroke": {"label": "Not (post-)stroke", "ft_only": False,
                   "text": "The population is not stroke (tumour, TBI, primary progressive aphasia, "
                           "dementia, healthy only without a stroke question)."},
    "not_aphasia": {"label": "No language or communication outcome", "ft_only": False,
                    "text": "No aphasia / language / communication measure is reported."},
    "design_out_of_scope": {"label": "Design out of scope", "ft_only": False,
                            "text": "Reports no lesion–behaviour, therapy-response, recovery-predictor or "
                                    "network evidence the schema can hold (e.g. pure modelling, instrument "
                                    "validation without brain or outcome data)."},
    "not_full_report": {"label": "Not a full report", "ft_only": False,
                        "text": "Editorial, letter, conference abstract, protocol, erratum or thesis."},
    "insufficient_sample": {"label": "Insufficient sample", "ft_only": False,
                            "text": "Below the sample threshold set in docs/SCREENING.md for the question asked."},
    "language": {"label": "Language", "ft_only": False,
                 "text": "Not available in a language the screener reads."},
    "duplicate_report": {"label": "Duplicate report of an included study", "ft_only": False,
                         "text": "A secondary publication of a cohort already included; note which."},
    "not_retrieved": {"label": "Full text not retrieved", "ft_only": True,
                      "text": "The full text could not be obtained through the screener's access."},
    "not_extractable": {"label": "Not extractable as it stands", "ft_only": True,
                        "text": "Read in full, but the findings cannot be written into the schema with "
                                "verbatim support (see the note)."},
    "other": {"label": "Other (see note)", "ft_only": False,
              "text": "Any other reason; the note is required."},
}

SOURCE_KINDS = {
    "search": "database search",
    "hand_picked": "hand-picked by a curator",
    "citation_chasing": "cited by an extracted paper",
    "gap_analysis": "suggested by the evidence-gap analysis",
    "registered": "registered automatically from a PDF in papers/",
    "seed": "starter reference",
}

# Where an included (or legacy) paper stands in the KB, in pipeline order.
KB_STATES = ("not_registered", "no_pdf", "awaiting_extraction", "in_review", "in_kb", "rejected", "refused")

# The one stage label the explorer facets and PRISMA boxes use.
STAGE_LABELS = {
    "duplicate": "duplicate (merged)",
    "awaiting_ta": "awaiting title/abstract screening",
    "excluded_ta": "excluded at title/abstract",
    "unsure_ta": "unsure at title/abstract",
    "awaiting_ft": "awaiting full-text assessment",
    "not_retrieved": "full text not retrieved",
    "excluded_ft": "excluded at full text",
    "unsure_ft": "unsure at full text",
    "included": "included",
}


# ---------------------------------------------------------------------------
# Loading and saving
# ---------------------------------------------------------------------------

def load_searches(root: Path = ROOT) -> list[dict]:
    path = root / "screening" / "searches.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("searches") or [])


def load_candidates(root: Path = ROOT) -> list[dict]:
    path = root / "screening" / "candidates.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("candidates") or [])


class _Dumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    if "\n" in data or len(data) > 100:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">" if len(data) > 100 and "\n" not in data else "|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_presenter)


def _dump(obj) -> str:
    return yaml.dump(obj, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100)


SEARCHES_HEADER = """# Search runs and file imports — one record each (docs/SCREENING.md §3).
# Written by screen.py; `for` and `notes` are meant to be edited by hand.
#   database: pubmed | openalex | scopus | embase | psycinfo | web_of_science | other
#   for:      evidence-gap ids (atlas_mapping/evidence_gaps.yaml) and/or KB entry ids this search serves
"""

CANDIDATES_HEADER = """# Screening register — one record per de-duplicated candidate paper (docs/SCREENING.md §4).
# Written by screen.py. Decisions are made by a named person; a model's opinion lives under
# `suggestion` and is never a decision. Abstracts are kept out of this file (screening/abstracts.jsonl,
# local). What happens after inclusion is derived from citations.md, papers/, drafts/ and the canonical
# folders — do not record it here.
"""


def save_searches(searches: list[dict], root: Path = ROOT) -> None:
    (root / "screening").mkdir(exist_ok=True)
    (root / "screening" / "searches.yaml").write_text(SEARCHES_HEADER + _dump({"searches": searches}), encoding="utf-8")


def save_candidates(candidates: list[dict], root: Path = ROOT) -> None:
    (root / "screening").mkdir(exist_ok=True)
    (root / "screening" / "candidates.yaml").write_text(CANDIDATES_HEADER + _dump({"candidates": candidates}),
                                                        encoding="utf-8")


# ---------------------------------------------------------------------------
# Identity and de-duplication
# ---------------------------------------------------------------------------

def norm_doi(doi) -> str | None:
    if not doi:
        return None
    d = str(doi).strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", d)
    d = d.rstrip(".,;)")
    return d if d.startswith("10.") else None


def norm_title(title) -> str:
    t = unicodedata.normalize("NFKD", str(title or "")).lower()
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", t)


def identity_keys(rec: dict) -> list[str]:
    """Keys under which a record is the same paper: doi, pmid, then title+year."""
    keys = []
    d = norm_doi(rec.get("doi"))
    if d:
        keys.append(f"doi:{d}")
    if rec.get("pmid"):
        keys.append(f"pmid:{str(rec['pmid']).strip()}")
    t = norm_title(rec.get("title"))
    if len(t) >= 20:
        keys.append(f"title:{t}:{rec.get('year') or ''}")
    return keys


def next_id(candidates: list[dict]) -> str:
    n = 0
    for c in candidates:
        m = re.match(r"^C(\d+)$", str(c.get("id") or ""))
        if m:
            n = max(n, int(m.group(1)))
    return f"C{n + 1:04d}"


def find_duplicate(rec: dict, index: dict[str, dict]) -> dict | None:
    for k in identity_keys(rec):
        if k in index:
            return index[k]
    return None


def build_identity_index(candidates: list[dict]) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for c in candidates:
        for k in identity_keys(c):
            index.setdefault(k, c)
    return index


# ---------------------------------------------------------------------------
# What the KB already knows about a citation key
# ---------------------------------------------------------------------------

_CITE_HEAD = re.compile(r"^##\s+(@\S+)\s*(?:\[(.*?)\])?", re.M)


def citation_blocks(root: Path = ROOT) -> dict[str, dict]:
    """@Key -> {tag, section, doi, title, year, first_author, note} from citations.md."""
    path = root / "citations.md"
    out: dict[str, dict] = {}
    if not path.exists():
        return out
    section = ""
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") and not line.startswith("## @"):
            section = line[3:].strip()
            cur = None
            continue
        m = _CITE_HEAD.match(line)
        if m:
            cur = m.group(1)
            out[cur] = {"tag": m.group(2) or "", "section": section, "doi": None, "title": None,
                        "year": None, "first_author": None, "note": "", "_lines": []}
            ym = re.search(r"(19|20)\d{2}", cur)
            out[cur]["year"] = int(ym.group(0)) if ym else None
            am = re.match(r"@([A-Za-z][A-Za-z'\-]*?)(?=\d{4})", cur)
            out[cur]["first_author"] = am.group(1) if am else None
            continue
        if cur is None:
            continue
        rec = out[cur]
        s = line.strip()
        if s.startswith(">"):
            rec["note"] += s.lstrip("> ").strip() + " "
            continue
        if s.startswith("#"):
            continue
        md = re.search(r"doi:\s*(10\.\S+)", s, re.I)
        if md and not rec["doi"]:
            rec["doi"] = norm_doi(md.group(1))
            continue
        if s and not s.startswith("*") and not s.startswith("---"):
            rec["_lines"].append(s)
    for rec in out.values():
        lines = rec.pop("_lines")
        # Author line(s) look like "Surname AB, Surname C." (match_papers._AUTHOR_LINE), possibly
        # wrapped over several lines or starting with a consortium name; the title follows them.
        title_lines, in_title = [], False
        for l in lines:
            if not in_title:
                if _is_author_line(l):
                    continue
                in_title = True
            title_lines.append(l)
            if l.endswith((".", "?")):
                break
        rec["title"] = " ".join(title_lines).strip().rstrip(".") or None
        rec["note"] = rec["note"].strip()
    return out


# "Leff AP" / "Rothi LJG" / "van der Meulen I" / "Vry M-S" — one author token of a citation line
_AUTHOR_TOKEN = re.compile(r"^(?:[A-Za-z][\w'’\-]*\s+)*[A-Z][\w'’\-]+\s+[A-Z][A-Z\-]{0,4}\.?$")
_AUTHOR_TAIL = re.compile(r"^(et al\.?|\(\d{4}\)\.?|\d{4}\.?|[A-Z][\w\-]+ (team|Team|group|Group|Consortium|Collaborators))$")


def _is_author_line(line: str) -> bool:
    """True for "Surname AB, Surname C, et al." style lines, also when wrapped
    mid-list, ending in "(1997)." or naming a consortium. A title never
    looks like a list of surname+initials tokens."""
    s = line.strip().rstrip(".")
    if re.match(r"^(The )?[A-Z].*\b(Collaborators|Group|Consortium|Investigators)\b", s):
        return True
    tokens = [t.strip() for t in s.split(",") if t.strip()]
    if not tokens:
        return False
    ok = sum(1 for t in tokens if _AUTHOR_TOKEN.match(t) or _AUTHOR_TAIL.match(t)
             or (" " in t and _AUTHOR_TOKEN.match(t.rsplit(" (", 1)[0])))
    return ok >= max(1, round(0.7 * len(tokens)))


def kb_facts(root: Path = ROOT) -> dict[str, dict]:
    """@Key -> {registered, tag, pdf, drafts, draft_rejected, approved_findings, refused}.

    One pass over citations.md, papers/, drafts/ and the canonical folders."""
    cites = citation_blocks(root)
    facts: dict[str, dict] = {}

    def f(key):
        return facts.setdefault(key, {"registered": key in cites, "tag": (cites.get(key) or {}).get("tag", ""),
                                      "pdf": False, "drafts": 0, "draft_rejected": 0, "draft_open": 0,
                                      "approved_findings": 0, "refused": False, "entries": set()})

    for key, rec in cites.items():
        f(key)["refused"] = rec["tag"] == "refused"
    papers = root / "papers"
    if papers.is_dir():
        for p in papers.iterdir():
            if p.suffix.lower() in (".pdf", ".txt") and not p.stem.endswith("_annotated"):
                f(f"@{p.stem}")["pdf"] = True
    else:
        # papers/ is local only (copyright): where it is absent — CI, another machine — PDF
        # presence is unknown and must not be reported as "no PDF".
        for rec in facts.values():
            rec["pdf"] = None
    for b in DRAFT_BUCKETS:
        d = root / "drafts" / b
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                fm, _ = parse_markdown(p)
            except Exception:  # noqa: BLE001
                continue
            keys = {str(x.get("citation")) for x in (fm.get("findings") or [])
                    if isinstance(x, dict) and re.match(r"^@[A-Za-z]", str(x.get("citation") or ""))}
            m = re.match(r"^(.*)__(\S+)\.md$", p.name)
            if m:
                keys.add(f"@{m.group(2)}")
            for key in keys:
                rec = f(key)
                rec["drafts"] += 1
                if fm.get("status") == "rejected":
                    rec["draft_rejected"] += 1
                else:
                    rec["draft_open"] += 1
    for b in CANONICAL_BUCKETS:
        d = root / b
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                fm, _ = parse_markdown(p)
            except Exception:  # noqa: BLE001
                continue
            if fm.get("status") != "approved":
                continue
            for x in fm.get("findings") or []:
                if isinstance(x, dict) and re.match(r"^@[A-Za-z]", str(x.get("citation") or "")):
                    rec = f(str(x["citation"]))
                    rec["approved_findings"] += 1
                    rec["entries"].add(f"{b}/{p.stem}")
    for rec in facts.values():
        rec["entries"] = sorted(rec["entries"])
        if not papers.is_dir():
            rec["pdf"] = None
    return facts


def kb_state(fact: dict | None) -> str | None:
    """Pipeline state of a registered paper, from kb_facts()."""
    if not fact or not fact.get("registered"):
        return "not_registered"
    if fact.get("refused"):
        return "refused"
    if fact.get("approved_findings"):
        return "in_kb"
    if fact.get("drafts") and fact.get("draft_open") == 0:
        return "rejected"
    if fact.get("draft_open"):
        return "in_review"
    if fact.get("pdf") is False:
        return "no_pdf"
    return "awaiting_extraction"


# ---------------------------------------------------------------------------
# Derived stage of a candidate
# ---------------------------------------------------------------------------

def last_decision(cand: dict, stage: str) -> dict | None:
    out = None
    for d in cand.get("screening") or []:
        if d.get("stage") == stage:
            out = d
    return out


def stage_of(cand: dict) -> tuple[str, str | None]:
    """(stage, reason) from the screening history alone."""
    if cand.get("duplicate_of"):
        return "duplicate", None
    ta = last_decision(cand, "title_abstract")
    ft = last_decision(cand, "full_text")
    # A paper that came in with full text already (hand-picked, registered) may have no T/A step.
    if ta is None and ft is None:
        return ("awaiting_ft" if cand.get("skip_title_abstract") else "awaiting_ta"), None
    if ta is not None and ft is None:
        if ta.get("decision") == "exclude":
            return "excluded_ta", ta.get("reason")
        if ta.get("decision") == "unsure":
            return "unsure_ta", None
        return "awaiting_ft", None
    if ft.get("decision") == "include":
        return "included", None
    if ft.get("decision") == "unsure":
        return "unsure_ft", None
    return ("not_retrieved" if ft.get("reason") == "not_retrieved" else "excluded_ft"), ft.get("reason")


def arm_of(cand: dict) -> str:
    """PRISMA 2020 arm: 'databases' if any source is a search, else 'other'."""
    for s in cand.get("sources") or []:
        if isinstance(s, dict) and s.get("search"):
            return "databases"
    return "other"


def enrich(candidates: list[dict], facts: dict[str, dict]) -> list[dict]:
    """Candidates with derived fields: stage, reason, arm, kb (state + counts), decided_by/on."""
    out = []
    for c in candidates:
        stage, reason = stage_of(c)
        key = c.get("key")
        fact = facts.get(key) if key else None
        kb = None
        if stage == "included" or (key and fact):
            kb = {"state": kb_state(fact), "pdf": bool(fact and fact.get("pdf")),
                  "drafts": int(fact["drafts"]) if fact else 0,
                  "draft_rejected": int(fact["draft_rejected"]) if fact else 0,
                  "approved_findings": int(fact["approved_findings"]) if fact else 0,
                  "entries": list(fact["entries"]) if fact else [],
                  "tag": fact.get("tag") if fact else None}
        last = (c.get("screening") or [None])[-1]
        row = dict(c)
        row.update({"stage": stage, "reason": reason, "arm": arm_of(c), "kb": kb,
                    "decided_by": (last or {}).get("by"), "decided_on": str((last or {}).get("date") or "") or None})
        out.append(row)
    return out


# ---------------------------------------------------------------------------
# PRISMA 2020 counts and coverage per gap
# ---------------------------------------------------------------------------

def prisma_counts(rows: list[dict], searches: list[dict]) -> dict:
    """The numbers of a PRISMA 2020 flow diagram (two identification arms) plus
    the KB's own stages after inclusion. `rows` are enrich()ed candidates."""
    by_db = collections.Counter()
    for s in searches:
        by_db[str(s.get("database") or "other")] += int(s.get("retrieved") or s.get("hits") or 0)
    by_kind = collections.Counter()
    for r in rows:
        if r["arm"] == "other":
            kinds = {str(s.get("kind") or "hand_picked") for s in (r.get("sources") or []) if isinstance(s, dict)}
            for k in kinds or {"hand_picked"}:
                by_kind[k] += 1
    dups = [r for r in rows if r["stage"] == "duplicate"]
    live = [r for r in rows if r["stage"] != "duplicate"]
    db = [r for r in live if r["arm"] == "databases"]
    other = [r for r in live if r["arm"] == "other"]

    def n(rs, *stages):
        return sum(1 for r in rs if r["stage"] in stages)

    def reasons(rs, stage):
        c = collections.Counter(str(r["reason"] or "other") for r in rs if r["stage"] == stage)
        return dict(c.most_common())

    # Records that reached full text in each arm: included at T/A (or came in with full text).
    db_sought = [r for r in db if r["stage"] in ("awaiting_ft", "not_retrieved", "excluded_ft", "unsure_ft", "included")]
    other_sought = other  # the other-methods arm has no title/abstract step in PRISMA 2020
    included = [r for r in live if r["stage"] == "included"]
    kb = collections.Counter((r["kb"] or {}).get("state") or "not_registered" for r in included)
    return {
        "identification": {
            "databases": {"records": sum(by_db.values()), "byDatabase": dict(by_db), "candidates": len(db) + sum(1 for r in dups if r["arm"] == "databases")},
            "other": {"records": len(other) + sum(1 for r in dups if r["arm"] == "other"), "byKind": dict(by_kind)},
            "duplicatesRemoved": len(dups),
        },
        "screening": {
            "screened": len(db),
            "awaitingTitleAbstract": n(db, "awaiting_ta"),
            "unsureTitleAbstract": n(db, "unsure_ta"),
            "excludedTitleAbstract": n(db, "excluded_ta"),
            "excludedTitleAbstractReasons": reasons(db, "excluded_ta"),
            "sought": len(db_sought),
            "notRetrieved": n(db_sought, "not_retrieved"),
            "assessed": n(db_sought, "excluded_ft", "included"),
            "awaitingFullText": n(db_sought, "awaiting_ft"),
            "unsureFullText": n(db_sought, "unsure_ft"),
            "excludedFullText": n(db_sought, "excluded_ft"),
            "excludedFullTextReasons": reasons(db_sought, "excluded_ft"),
            "included": n(db_sought, "included"),
        },
        "other": {
            "sought": len(other_sought),
            "notRetrieved": n(other_sought, "not_retrieved"),
            "assessed": n(other_sought, "excluded_ft", "excluded_ta", "included"),
            "awaitingFullText": n(other_sought, "awaiting_ft", "awaiting_ta"),
            "unsureFullText": n(other_sought, "unsure_ft", "unsure_ta"),
            "excludedFullText": n(other_sought, "excluded_ft", "excluded_ta"),
            "excludedFullTextReasons": {**reasons(other_sought, "excluded_ft"), **reasons(other_sought, "excluded_ta")},
            "included": n(other_sought, "included"),
        },
        "included": {
            "total": len(included),
            "kb": {k: int(kb.get(k, 0)) for k in KB_STATES},
            "approvedFindings": sum((r["kb"] or {}).get("approved_findings", 0) for r in included),
        },
    }


def load_gaps(root: Path = ROOT) -> dict[str, dict]:
    path = root / "atlas_mapping" / "evidence_gaps.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): dict(v or {}) for k, v in (data.get("gaps") or {}).items()}


def coverage(rows: list[dict], searches: list[dict], gaps: dict[str, dict]) -> list[dict]:
    """Per gap (and per any other `for` target named by a search or candidate):
    how many candidates were found, screened, included, extracted, in the KB."""
    targets: dict[str, dict] = {}

    def t(tid):
        g = gaps.get(tid) or {}
        return targets.setdefault(tid, {"id": tid, "kind": g.get("kind"), "areas": list(g.get("areas") or []),
                                        "need": g.get("need"), "suggested": list(g.get("papers") or []),
                                        "searches": 0, "found": 0, "screened": 0, "included": 0,
                                        "in_kb": 0, "approved_findings": 0, "candidates": []})

    search_for: dict[str, list[str]] = {}
    for s in searches:
        ids = [str(x) for x in (s.get("for") or [])]
        search_for[str(s.get("id"))] = ids
        for tid in ids:
            t(tid)["searches"] += 1
    for tid in gaps:
        t(tid)
    for r in rows:
        if r["stage"] == "duplicate":
            continue
        ids = set(str(x) for x in (r.get("for") or []))
        for s in r.get("sources") or []:
            if isinstance(s, dict) and s.get("search"):
                ids.update(search_for.get(str(s["search"]), []))
        # a candidate that became a suggested paper of a gap counts for that gap too
        for gid, g in gaps.items():
            if r.get("key") and r["key"] in (g.get("papers") or []):
                ids.add(gid)
        for tid in ids:
            rec = t(tid)
            rec["found"] += 1
            if r["stage"] not in ("awaiting_ta", "awaiting_ft", "unsure_ta", "unsure_ft"):
                rec["screened"] += 1
            if r["stage"] == "included":
                rec["included"] += 1
                if (r["kb"] or {}).get("state") == "in_kb":
                    rec["in_kb"] += 1
                    rec["approved_findings"] += (r["kb"] or {}).get("approved_findings", 0)
            rec["candidates"].append(r["id"])
    return sorted(targets.values(), key=lambda x: (x["kind"] is None, x["id"]))


# ---------------------------------------------------------------------------
# Backfill: the bibliography as it stood before the register existed
# ---------------------------------------------------------------------------

def _section_kind(section: str, tag: str) -> str:
    s = section.lower()
    if "registered automatically" in s:
        return "registered"
    if "gap" in s:
        return "gap_analysis"
    if tag == "cited":
        return "citation_chasing"
    if tag == "seed" or "seed" in s:
        return "seed"
    return "hand_picked"


def backfill_candidates(root: Path = ROOT, by: str = "legacy", date: str | None = None) -> tuple[list[dict], int]:
    """Add every citations.md key that is not yet a candidate, as an
    'other sources' record with the decisions its tag implies:

    * [extracted] / [extracted-as-review] / [re-extracted-as-review], or any key
      that drafts or canonical findings cite: full text assessed and included
      (it was read and findings were written);
    * [refused]: full text assessed and excluded, reason not_extractable;
    * [seed] / [cited]: identified, awaiting full-text assessment (no decision
      is invented for it).

    Decisions are stamped ``by: legacy`` with a note, so the register never
    claims a person screened what entered the bibliography before it existed."""
    candidates = load_candidates(root)
    index = build_identity_index(candidates)
    by_key = {c.get("key"): c for c in candidates if c.get("key")}
    cites = citation_blocks(root)
    facts = kb_facts(root)
    today = date or dt.date.today().isoformat()
    added = 0
    for key, rec in cites.items():
        if key in by_key:
            continue
        probe = {"doi": rec["doi"], "title": rec["title"], "year": rec["year"]}
        dup = find_duplicate(probe, index)
        if dup is not None:
            if not dup.get("key"):
                dup["key"] = key
            continue
        kind = _section_kind(rec["section"], rec["tag"])
        cand = {
            "id": next_id(candidates),
            "key": key,
            "doi": rec["doi"],
            "title": rec["title"],
            "year": rec["year"],
            "first_author": rec["first_author"],
            "sources": [{"kind": kind, "date": today, "note": f"citations.md [{rec['tag'] or 'untagged'}] — {rec['section']}"}],
            "skip_title_abstract": True,
            "screening": [],
        }
        tag = rec["tag"]
        fact = facts.get(key) or {}
        if tag in ("extracted", "extracted-as-review", "re-extracted-as-review") or fact.get("drafts") or fact.get("approved_findings"):
            cand["screening"].append({"stage": "full_text", "decision": "include", "by": by, "date": today,
                                      "note": "Entered the bibliography and was extracted before the screening register existed."})
        elif tag == "refused":
            cand["screening"].append({"stage": "full_text", "decision": "exclude", "reason": "not_extractable", "by": by,
                                      "date": today, "note": (rec["note"] or "")[:300]})
        candidates.append(cand)
        for k in identity_keys(cand):
            index.setdefault(k, cand)
        added += 1
    return candidates, added


# ---------------------------------------------------------------------------
# One call for the export and the status script
# ---------------------------------------------------------------------------

def collect(root: Path = ROOT) -> dict:
    searches = load_searches(root)
    candidates = load_candidates(root)
    facts = kb_facts(root)
    rows = enrich(candidates, facts)
    gaps = load_gaps(root)
    return {
        "searches": searches,
        "candidates": rows,
        "prisma": prisma_counts(rows, searches),
        "coverage": coverage(rows, searches, gaps),
        "reasons": {k: {"label": v["label"], "fullTextOnly": v["ft_only"]} for k, v in REASONS.items()},
        "sourceKinds": dict(SOURCE_KINDS),
        "stageLabels": dict(STAGE_LABELS),
        "kbStates": list(KB_STATES),
        "facts": facts,
    }
