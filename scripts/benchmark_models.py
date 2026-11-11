#!/usr/bin/env python3
"""
benchmark_models.py — are we using the best local model? Run the candidates on papers
we have already curated and score them the same way, so the choice in models.yaml is a
measured one (docs/MODELS.md §3, "how we decide").

    python scripts/benchmark_models.py --list-references
        # papers that can serve as reference: human-reviewed findings in the KB and a PDF in papers/

    python scripts/benchmark_models.py --models gemma4:31b-it-q8_0 qwen3.8:27b ornith-1.5:122b \\
        --papers Alyahya2018NounVerb Bonilha2014
        # extract each paper with each model into _compare/<model>/ (sandbox: the KB is untouched),
        # score, print the table, write _compare/benchmark_<date>.{json,md}

    python scripts/benchmark_models.py --models qwen3.8:27b --auto-papers 2 --min-findings 5 --seed 7
        # let the script pick 2 random reference papers with ≥5 findings, from 2 different buckets
        # (--seed makes the pick repeatable; the pick is written into the results JSON)

    python scripts/benchmark_models.py --untested --auto-papers 2
        # every candidate listed in docs/MODELS.md §4 that fits this machine and has not been
        # tested yet (no row in §5, no sandbox in _compare/): pulled if needed, then run

    python scripts/benchmark_models.py --models ... --papers ... --skip-extract
        # re-score sandboxes that already exist (after editing the grader, say)

    python scripts/benchmark_models.py --pulled --papers Alyahya2018NounVerb --publish
        # a clean run of every model already pulled on this machine on one paper, published;
        # then add a second paper without redoing the first:
    python scripts/benchmark_models.py --pulled --resume --papers Alyahya2018NounVerb Yourganov2015Predicting --publish

    python scripts/benchmark_models.py --untested --sandboxes --resume --papers ... --publish
        # carry on after an interrupted run: extract only what is missing, score everything that
        # has a sandbox, and write export/model-benchmark.json for the explorer's Models page

    python scripts/benchmark_models.py --refresh-sources
        # only refresh "where each model comes from" on the Models page: model_sources.yaml (curated:
        # developer, licence, release, upstream weights) and, when Ollama runs, what is installed here

    python scripts/benchmark_models.py ... --append-log
        # also append one row per model × paper to the decision log in docs/MODELS.md §5

Scoring, in the order a failure stops the reading (MODELS.md §3):

  1. fidelity    absent quotes / all quotes — any absent quote disqualifies the model for
                 `extract` (a quote that is not in the paper is a fabrication, not a style issue);
                 also the share verified (exact + elided + table) and the near/anchored rest
  2. schema      validation issues across the drafts (errors cost review time on every paper)
  3. coverage    findings and entries vs the curated reference — by default only the findings
                 approved under the governance policy, never the legacy ones (--reference) —
                 and link recall: the share of
                 the reference's entry ↔ target links the candidate also produced, whichever
                 side it filed them under and under whichever id (plus link precision: the
                 share of the candidate's links that the reference has too)
  4. calibration mean strength and confidence vs the reference (over-claiming is the
                 small-model failure; prefer a model that under-claims)
  5. support     source passages per finding (thin support = more reviewer work)
  6. cost        wall-clock per paper and, when ollama is reachable, the processor split
                 (100 % GPU, or a CPU spill) from `ollama ps` during the run

Eligible = zero absent quotes on every paper AND schema issues and calibration no worse
than the incumbent (roles.extract.model in models.yaml). The script says which candidates
are eligible; the decision — and the row in the log — is a person's.

_compare/ is git-ignored (it holds verbatim paper text). Nothing in the canonical folders,
drafts/, logs/ or papers/ is written.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import compare_extraction as CE  # noqa: E402
from aphasia_kb import parse_markdown, reviewer_kind  # noqa: E402

PAPERS = ROOT / "papers"
COMPARE = ROOT / "_compare"
MODELS_YAML = ROOT / "models.yaml"
MODELS_MD = ROOT / "docs" / "MODELS.md"
BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews", "ingredients")
STRENGTH_RANK = {"weak": 1, "moderate": 2, "strong": 3}
CONF_RANK = {"low": 1, "medium": 2, "high": 3}


def slug(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9.]+", "-", model).strip("-")


def incumbent() -> str:
    manifest = json.loads((ROOT / "benchmark_manifest.json").read_text())
    required = set(manifest["papers"])
    if path.exists():
        previous = json.loads(path.read_text())
        required.update(p["key"] for p in previous.get("papers", []))
    if not required.issubset(papers):
        raise ValueError("Incomplete benchmark publication; missing papers: " + ", ".join(sorted(required - set(papers))))
    if not rows or incumbent_model not in {r["model"] for r in rows}:
        raise ValueError("Publication requires scored rows and the incumbent")
    for model in {r["model"] for r in rows}:
        mine = [r for r in rows if r["model"] == model]
        if len(mine) != len(set(papers)) or {r["paper"] for r in mine} != set(papers):
            raise ValueError(f"Incomplete or duplicate paper rows for {model}")
    verdicts = summarise(rows, incumbent_model)
    try:
        cfg = yaml.safe_load(MODELS_YAML.read_text(encoding="utf-8")) or {}
        return str((cfg.get("roles") or {}).get("extract", {}).get("model") or cfg.get("default") or "")
    except Exception:  # noqa: BLE001
        return ""


# ------------------------------------------------------------------ references
def reference_papers(root: Path = ROOT, papers_dir: Path = PAPERS) -> list[dict]:
    """Papers whose canonical findings were all approved by a person, with the PDF present.
    These are the only fair references: the benchmark compares a model with a human reading."""
    by_cit: dict[str, dict] = {}
    for b in BUCKETS:
        for p in sorted((root / b).glob("*.md")) if (root / b).is_dir() else []:
            try:
                fm, _ = parse_markdown(p)
            except Exception:  # noqa: BLE001
                continue
            if not isinstance(fm, dict):
                continue
            file_kind = reviewer_kind(fm.get("reviewer"), fm.get("review_tier"))
            for f in fm.get("findings") or []:
                if not isinstance(f, dict) or not f.get("citation"):
                    continue
                cit = str(f["citation"]).strip()
                rv = f.get("review") if isinstance(f.get("review"), dict) else None
                kind = reviewer_kind(rv.get("reviewer"), rv.get("tier")) if rv else file_kind
                rec = by_cit.setdefault(cit, {"citation": cit, "findings": 0, "human": 0, "model": 0, "entries": set(), "buckets": set(), "per_bucket": {}})
                rec["findings"] += 1
                rec["human"] += 1 if kind == "human" else 0
                rec["model"] += 1 if kind == "model" else 0
                rec["entries"].add(fm.get("id")); rec["buckets"].add(b)
                rec["per_bucket"][b] = rec["per_bucket"].get(b, 0) + 1
    out = []
    for cit, rec in by_cit.items():
        key = cit.lstrip("@")
        pdf = papers_dir / f"{key}.pdf"
        rec["pdf"] = pdf.exists()
        rec["all_human"] = rec["human"] == rec["findings"]
        rec["current"] = rec["human"] + rec["model"]          # approved under the governance policy; the rest is legacy
        rec["usable"] = usable_count(rec)
        rec["entries"] = sorted(x for x in rec["entries"] if x); rec["buckets"] = sorted(rec["buckets"])
        rec["main_bucket"] = max(rec["per_bucket"], key=rec["per_bucket"].get)   # where most of its findings live
        out.append(rec)
    return sorted(out, key=lambda r: (-int(r["all_human"] and r["pdf"]), -r["findings"], r["citation"]))


# Which canonical findings count as the reference. Legacy findings were approved before the
# governance policy, largely without anyone reading the paper: a model that disagrees with
# them may simply be right. So by default only findings approved under the policy are used.
REFERENCE = "current"
REFERENCE_KINDS = {"current": ("human", "model"), "human": ("human",), "all": ("human", "model", "legacy", "none")}
REFERENCE_TEXT = {"current": "findings approved under the governance policy (by a person, or model-approved Tier A); legacy findings left out",
                  "human": "findings approved by a person only", "all": "every canonical finding, legacy ones included"}


def usable_count(rec: dict, which: str | None = None) -> int:
    which = which or REFERENCE
    return {"current": rec["human"] + rec["model"], "human": rec["human"], "all": rec["findings"]}[which]


def reference_findings(root: Path, citation: str, which: str | None = None) -> tuple[list[dict], list[Path], int]:
    """(the reference findings for this paper, the canonical entries they sit in, how many findings
    were left out) — the findings are those whose approval is of a kind `which` accepts."""
    keep = REFERENCE_KINDS[which or REFERENCE]
    found: list[dict] = []
    paths: list[Path] = []
    left_out = 0
    for p in canonical_entries(root, citation):
        try:
            fm, _ = parse_markdown(p)
        except Exception:  # noqa: BLE001
            continue
        file_kind = reviewer_kind(fm.get("reviewer"), fm.get("review_tier"))
        mine = []
        for f in fm.get("findings") or []:
            if not isinstance(f, dict) or not CE._citations_match(f.get("citation"), citation):
                continue
            rv = f.get("review") if isinstance(f.get("review"), dict) else None
            kind = reviewer_kind(rv.get("reviewer"), rv.get("tier")) if rv else file_kind
            if kind not in keep:
                left_out += 1
                continue
            f = dict(f)
            f["_entry"] = p.stem; f["_entry_id"] = fm.get("id") or p.stem; f["_path"] = p; f["_review_kind"] = kind
            mine.append(f)
        if mine:
            found += mine
            paths.append(p)
    return found, paths, left_out


def pick_papers(refs: list[dict], n: int = 2, min_findings: int = 5, seed: int | None = None) -> tuple[list[dict], list[str]]:
    """n random reference papers with a PDF and at least min_findings findings that count as
    reference (see REFERENCE), each from a different bucket (the bucket where most of its
    findings live). Papers whose findings all count are preferred. Returns (picked, notes)."""
    import random
    rng = random.Random(seed)
    pool = [r for r in refs if r["pdf"] and usable_count(r) >= min_findings]
    notes = []
    if not pool:
        return [], [f"no paper has a PDF in papers/ and at least {min_findings} reference findings ({REFERENCE_TEXT[REFERENCE]})"]
    picked: list[dict] = []
    for prefer_human in (True, False):
        cands = [r for r in pool if r not in picked and (usable_count(r) == r["findings"] or not prefer_human)]
        rng.shuffle(cands)
        for r in cands:
            if len(picked) >= n:
                break
            if any(r["main_bucket"] == q["main_bucket"] for q in picked):
                continue
            picked.append(r)
        if len(picked) >= n:
            break
    if len(picked) < n:
        # not enough distinct buckets: fill from what is left, say so
        rest = [r for r in pool if r not in picked]
        rng.shuffle(rest)
        for r in rest[: n - len(picked)]:
            picked.append(r)
        notes.append(f"only {len({q['main_bucket'] for q in picked})} distinct bucket(s) available among papers with ≥{min_findings} reference findings")
    left = sum(r["findings"] - usable_count(r) for r in picked)
    if left:
        notes.append(f"{left} finding(s) of the picked papers are left out of the reference ({REFERENCE_TEXT[REFERENCE]})")
    return picked, notes


def print_references(refs: list[dict]) -> None:
    good = sorted((r for r in refs if r["pdf"] and usable_count(r) >= 3), key=lambda r: -usable_count(r))
    print(f"Reference: {REFERENCE_TEXT[REFERENCE]}.")
    print(f"Reference candidates: {len(good)} papers with a PDF and at least 3 such findings\n")
    print(f"  {'paper':32} {'reference':>9} {'(person':>8} {'model)':>7} {'legacy':>7}  main bucket (all)")
    for r in good:
        print(f"  {r['citation']:32} {usable_count(r):>9} {r['human']:>8} {r['model']:>7} {r['findings'] - r['current']:>7}  {r['main_bucket']} ({', '.join(r['buckets'])})")
    rest = [r for r in refs if r not in good]
    if rest:
        print(f"\n  not usable yet: {len(rest)} papers (too few findings approved under the policy, or no PDF in papers/)")
        for r in rest[:8]:
            why = [] if r["pdf"] else ["no PDF"]
            if usable_count(r) < 3:
                why.append(f"{usable_count(r)} reference finding(s) of {r['findings']}")
            print(f"    {r['citation']:32} {'; '.join(why)}")
        if len(rest) > 8:
            print(f"    … {len(rest) - 8} more")
    print("\nPick 2–3 of different kinds (lesion-symptom mapping, therapy trial, review); one paper is not enough.")


# ------------------------------------------------------------------ candidates from MODELS.md
def machine_ram_gb() -> int | None:
    try:
        if sys.platform == "darwin":
            out = subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, timeout=5).stdout.strip()
            return round(int(out) / 1024 ** 3)
        for line in Path("/proc/meminfo").read_text().splitlines():
            if line.startswith("MemTotal:"):
                return round(int(line.split()[1]) / 1024 ** 2)
    except Exception:  # noqa: BLE001
        pass
    return None


def candidates_from_models_md(md_path: Path = MODELS_MD) -> tuple[list[dict], set[str]]:
    """The landscape tables of MODELS.md §4 → [{tag, ram_class, caveat}], and the tags that §5 has
    already logged. The §4 tables are read in order: the first lists 32–48 GB machines, the second
    ≥ 96 GB; rows under 'Considered and set aside' are not candidates."""
    text = md_path.read_text(encoding="utf-8")
    i = text.find("## 4."); j = text.find("Considered and set aside", i); k = text.find("## 5.")
    section = text[i:j if j > 0 else k]
    cands, table_no, in_table = [], 0, False
    for line in section.splitlines():
        if line.startswith("|") and not in_table:
            in_table = True; table_no += 1
        elif not line.startswith("|"):
            in_table = False
        if not (line.startswith("| `") and in_table):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        tags = re.findall(r"`([^`]+)`", cells[0])
        for t in tags:
            cands.append({"tag": t, "ram_class": 48 if table_no == 1 else 96, "caveat": cells[-1][:120] if len(cells) > 5 else ""})
    tested = set()
    for line in text[k:].splitlines() if k > 0 else []:
        if line.startswith("| 20"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) > 2 and cells[1] == "extract":
                tested.update(re.findall(r"`([^`]+)`", cells[2]))
    return cands, tested


def ollama_list(host: str) -> set[str]:
    try:
        env = dict(os.environ, OLLAMA_HOST=host)
        out = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=15, env=env).stdout
        return {line.split()[0] for line in out.splitlines()[1:] if line.strip()}
    except Exception:  # noqa: BLE001
        return set()


def untested_candidates(ram_gb: int | None, host: str, compare_dir: Path = COMPARE) -> tuple[list[dict], list[str]]:
    """Candidates in MODELS.md §4 that fit this machine and have neither a §5 row nor a sandbox yet."""
    cands, tested = candidates_from_models_md()
    inc = incumbent()
    have_sandbox = {d.name for d in compare_dir.iterdir() if d.is_dir()} if compare_dir.is_dir() else set()
    notes, out, seen = [], [], set()
    for c in cands:
        t = c["tag"]
        if t in seen:
            continue
        seen.add(t)
        if t == inc or t in tested or slug(t) in have_sandbox:
            continue
        if ram_gb is not None and c["ram_class"] > ram_gb:
            notes.append(f"{t}: needs a ≥{c['ram_class']} GB machine (this one has {ram_gb} GB)")
            continue
        low = c["caveat"].lower()
        c["low_priority"] = any(w in low for w in ("superseded", "lower quality", "only to settle", "only if"))
        out.append(c)
    return out, notes


def ensure_pulled(tags: list[str], host: str, pull: bool) -> list[str]:
    """Pull the models that are not local yet (ollama pull); returns the tags that are usable."""
    have = ollama_list(host)
    usable = []
    for t in tags:
        if t in have or f"{t}:latest" in have:
            usable.append(t); continue
        if not pull:
            print(f"  · {t}: not pulled — skipped (run without --no-pull, or `ollama pull {t}`)")
            continue
        print(f"  ⇣ ollama pull {t}  (this can be tens of GB; {dt.datetime.now():%H:%M:%S})", flush=True)
        rc = subprocess.call(["ollama", "pull", t], env=dict(os.environ, OLLAMA_HOST=host))
        if rc == 0:
            usable.append(t)
        else:
            print(f"  ✗ {t}: pull failed (exit {rc}) — skipped")
    return usable


# ------------------------------------------------------------------ extraction
def ollama_processor(host: str) -> str:
    """'100% GPU' / '38%/62% CPU/GPU' from `ollama ps`, or '' when not reachable."""
    try:
        env = dict(os.environ, OLLAMA_HOST=host)
        out = subprocess.run(["ollama", "ps"], capture_output=True, text=True, timeout=10, env=env).stdout
        for line in out.splitlines()[1:]:
            m = re.search(r"(\d+%\s*/\s*\d+%\s*CPU/GPU|\d+%\s*GPU|\d+%\s*CPU)", line)
            if m:
                return m.group(1).replace(" ", "")
    except Exception:  # noqa: BLE001
        pass
    return ""


def run_extraction(model: str, paper: str, out_dir: Path, host: str, timeout: int) -> dict:
    """extract.py in sandbox mode for one model × paper; returns timing and the exit status."""
    pdf = PAPERS / f"{paper}.pdf"
    cmd = [sys.executable, str(ROOT / "scripts" / "extract.py"), "--pdf", str(pdf), "--citation", f"@{paper}",
           "--model", model, "--out-dir", str(out_dir), "--no-monitor", "--timeout", str(timeout)]
    t0 = time.monotonic()
    proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    processor = ""
    lines: list[str] = []
    while True:
        line = proc.stdout.readline() if proc.stdout else ""
        if line:
            lines.append(line.rstrip())
            if not processor and "Citation key" in line:
                time.sleep(20)                    # give the model time to load, then look once
                processor = ollama_processor(host)
        elif proc.poll() is not None:
            break
    elapsed = time.monotonic() - t0
    tail = "\n".join(lines[-6:])
    return {"ok": proc.returncode == 0, "elapsed_s": round(elapsed, 1), "processor": processor, "tail": tail}


# ------------------------------------------------------------------ scoring
# A finding links two things: the entry it is filed under and its target. The reference and a
# candidate may file the same link from either side (the curated KB has "semantics → left
# angular gyrus" in the impairment entry; an extractor may write "left angular gyrus →
# semantics" in a region draft), and under an older or longer id. Coverage is therefore
# measured on unordered links between normalised ids, not on targets alone.
LEGACY_IDS = {  # ids renamed since the reference entries were written (schema v2.8)
    "auditory_comprehension": "form_to_meaning", "sentence_comprehension": "form_to_meaning",
    "reading_comprehension": "form_to_meaning", "comprehension": "form_to_meaning",
    "naming": "anomia", "confrontation_naming": "anomia", "word_retrieval": "anomia", "lexical_retrieval": "anomia",
    "speech_fluency": "fluency", "phonological_output": "phonological_production",
    "apraxia_of_speech": "form_to_articulation",
}
_ABBR = {"stg": "superiortemporalgyrus", "mtg": "middletemporalgyrus", "itg": "inferiortemporalgyrus",
         "ifg": "inferiorfrontalgyrus", "smg": "supramarginalgyrus", "slf": "superiorlongitudinalfasciculus",
         "atl": "anteriortemporallobe", "wernicke": "wernickes", "broca": "brocas"}
_alias_cache: dict[str, str] | None = None
_display: dict[str, str] = {}             # normalised id → an id a person can read (the canonical entry's, else as written)


def _squash(x) -> str:
    """`Left pre-central gyrus`, `left_precentral_gyrus` and `left_pre_central_gyrus` are one id."""
    tokens = re.split(r"[^a-z0-9]+", re.sub(r"\(.*?\)", " ", str(x or "").lower().replace("'", "")))
    return "".join(_ABBR.get(t, t) for t in tokens if t)


def _aliases(root: Path = ROOT) -> dict[str, str]:
    """squashed id / name / alias of every canonical entry → its squashed id."""
    global _alias_cache
    if _alias_cache is None:
        out: dict[str, str] = {}
        for b in BUCKETS:
            for p in sorted((root / b).glob("*.md")) if (root / b).is_dir() else []:
                try:
                    fm, _ = parse_markdown(p)
                except Exception:  # noqa: BLE001
                    continue
                if not isinstance(fm, dict) or not fm.get("id"):
                    continue
                eid = _squash(fm["id"])
                _display.setdefault(eid, str(fm["id"]))
                for x in [fm["id"], fm.get("name"), *(fm.get("aliases") or [])]:
                    if x and _squash(x):
                        out.setdefault(_squash(x), eid)
        _alias_cache = out
    return _alias_cache


def canon_id(x) -> str:
    x = str(x or "").strip().lower()
    x = LEGACY_IDS.get(x, x)
    q = _squash(x)
    out = _aliases().get(q, q)
    if out:
        _display.setdefault(out, x)
    return out


def _links(findings: list[dict]) -> dict[frozenset, set[str]]:
    """{frozenset({entry, target}): relationships seen on that link}; self-links are not links."""
    out: dict[frozenset, set[str]] = {}
    for f in findings:
        a, b = canon_id(f.get("_entry_id") or str(f.get("_entry") or "").split("__")[0]), canon_id(f.get("target"))
        if a and b and a != b:
            out.setdefault(frozenset((a, b)), set()).add(str(f.get("relationship") or "").lower())
    return out


def _link_name(link: frozenset) -> str:
    return " ↔ ".join(sorted(_display.get(k, k) for k in link))


def _mean(findings: list[dict], key: str, ranks: dict) -> float | None:
    vals = []
    for f in findings:
        v = f.get("strength") if key == "strength" else (f.get("provenance") or {}).get("confidence")
        if ranks.get(v):
            vals.append(ranks[v])
    return round(sum(vals) / len(vals), 2) if vals else None


def canonical_entries(root: Path, citation: str) -> list[Path]:
    """The reference: canonical entries (not drafts) with a finding citing the paper."""
    out = []
    for b in BUCKETS:
        for p in sorted((root / b).glob("*.md")) if (root / b).is_dir() else []:
            try:
                fm, _ = parse_markdown(p)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(fm, dict) and any(CE._citations_match(f.get("citation"), citation) for f in (fm.get("findings") or []) if isinstance(f, dict)):
                out.append(p)
    return out


def score(model: str, paper: str, sandbox: Path, papers_dir: Path = PAPERS, root: Path = ROOT) -> dict:
    cit = f"@{paper}"
    ref_f, ref_paths, ref_left_out = reference_findings(root, cit)
    cand_paths = CE._find_entries(sandbox, cit)
    cand_f = CE._load_findings(cand_paths, cit) if cand_paths else []
    ref_l, cand_l = _links(ref_f), _links(cand_f)
    shared = set(ref_l) & set(cand_l)
    out = {"model": model, "paper": paper, "drafts": len(cand_paths), "findings": len(cand_f), "ref_findings": len(ref_f),
           "ref_entries": len(ref_paths), "ref_left_out": ref_left_out, "reference": REFERENCE}
    if not cand_paths:
        out.update({"failed": True, "absent": None})
        return out
    q = CE._quote_check(cand_f, papers_dir)
    issues = CE._schema_issues(cand_paths)
    verified = q["exact"] + q["elided"] + q["table"]
    has_passages = any((f.get("source_passages") or []) for f in cand_f)
    out.update({
        "ungraded": bool(not cand_f or not q["total"] or q.get("missing_papers")),   # passages exist but no PDF text to grade them against
        "quotes": q["total"], "absent": q["absent"], "verified": verified, "near": q["near"], "anchored": q["anchored"],
        "absent_examples": q["absent_list"][:3], "no_quote_findings": len(q["no_quotes"]),
        "schema_issues": sum(len(v) for v in issues.values()), "schema_examples": [x for v in issues.values() for x in v][:3],
        "passages_per_finding": round(q["total"] / len(cand_f), 1) if cand_f else 0.0,
        "ref_links": len(ref_l), "links": len(cand_l), "shared_links": len(shared),
        "link_recall": round(len(shared) / len(ref_l), 2) if ref_l else None,
        "link_precision": round(len(shared) / len(cand_l), 2) if cand_l else None,
        "relationship_agreement": round(sum(1 for k in shared if ref_l[k] & cand_l[k]) / len(shared), 2) if shared else None,
        "missed_links": sorted(_link_name(k) for k in set(ref_l) - set(cand_l))[:8],
        "new_links": sorted(_link_name(k) for k in set(cand_l) - set(ref_l))[:8],
        "strength": _mean(cand_f, "strength", STRENGTH_RANK), "ref_strength": _mean(ref_f, "strength", STRENGTH_RANK),
        "confidence": _mean(cand_f, "confidence", CONF_RANK), "ref_confidence": _mean(ref_f, "confidence", CONF_RANK),
    })
    return out


def summarise(rows: list[dict], incumbent_model: str) -> dict[str, dict]:
    """Per model: eligible or not under the decision rule, with the reasons."""
    by_model: dict[str, list[dict]] = {}
    for r in rows:
        by_model.setdefault(r["model"], []).append(r)
    base = by_model.get(incumbent_model, [])
    base_issues = sum(r.get("schema_issues") or 0 for r in base)
    base_over = [((r.get("strength") or 0) - (r.get("ref_strength") or 0)) for r in base if r.get("strength") and r.get("ref_strength")]
    base_cal = sum(base_over) / len(base_over) if base_over else 0.0
    out = {}
    for m, rs in by_model.items():
        absent = sum(r.get("absent") or 0 for r in rs)
        failed = [r["paper"] for r in rs if r.get("failed")]
        issues = sum(r.get("schema_issues") or 0 for r in rs)
        over = [((r.get("strength") or 0) - (r.get("ref_strength") or 0)) for r in rs if r.get("strength") and r.get("ref_strength")]
        cal = sum(over) / len(over) if over else 0.0
        reasons = []
        expected = {r["paper"] for r in rows}
        if {r["paper"] for r in rs} != expected or len(rs) != len(expected):
            reasons.append("incomplete or duplicate paper evaluations")
        if not base or {r["paper"] for r in base} != expected:
            reasons.append("no complete paired incumbent baseline")
        if any(not r.get("findings") or not r.get("quotes") or not r.get("ref_findings") for r in rs):
            reasons.append("empty extraction, ungraded quotes, or empty reference")
        if m != incumbent_model and any(r.get("failed") or r.get("ungraded") or not r.get("quotes") for r in base):
            reasons.append("incumbent fidelity is unknown")
        if failed:
            reasons.append(f"no drafts for {', '.join(failed)}")
        ungraded = [r["paper"] for r in rs if r.get("ungraded")]
        if ungraded:
            reasons.append(f"quotes could not be graded for {', '.join(ungraded)} (no PDF text) — fidelity unknown")
        if absent:
            reasons.append(f"{absent} absent quote(s) — disqualified for extract")
        if m != incumbent_model and base and issues > base_issues:
            reasons.append(f"more schema issues than the incumbent ({issues} vs {base_issues})")
        if m != incumbent_model and base and cal > base_cal + 0.2:
            reasons.append(f"over-claims more than the incumbent (strength +{cal:.2f} vs +{base_cal:.2f})")
        out[m] = {"eligible": not reasons, "reasons": reasons, "absent": absent, "schema_issues": issues,
                  "calibration_delta": round(cal, 2), "papers": len(rs),
                  "mean_elapsed_s": round(sum(r.get("elapsed_s") or 0 for r in rs) / max(1, len(rs)), 0),
                  "link_recall": round(sum(r.get("shared_links") or 0 for r in rs) / max(1, sum(r.get("ref_links") or 0 for r in rs)), 2),
                  "link_precision": (round(sum(r.get("shared_links") or 0 for r in rs) / sum(r.get("links") or 0 for r in rs), 2)
                                     if sum(r.get("links") or 0 for r in rs) else None)}
    return out


# ------------------------------------------------------------------ output
def pct(v) -> str:
    return "—" if v is None else f"{v:.0%}"


def _hms(s: float | None) -> str:
    if not s:
        return "—"
    s = int(s)
    return f"{s // 3600}h{(s % 3600) // 60:02d}m" if s >= 3600 else f"{s // 60}m{s % 60:02d}s"


def table(rows: list[dict], verdicts: dict[str, dict], incumbent_model: str) -> str:
    L = ["| Model | Paper | Absent / quotes | Verified | Schema issues | Findings vs ref | Links found / in ref (recall) | Strength vs ref | Confidence vs ref | Passages / finding | Time · processor |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda x: (x["model"] != incumbent_model, x["model"], x["paper"])):
        if r.get("failed"):
            L.append(f"| `{r['model']}` | {r['paper']} | — | — | — | 0 drafts | — | — | — | — | {_hms(r.get('elapsed_s'))} |")
            continue
        absent = f"**{r['absent']}** / {r['quotes']}" if r["absent"] else f"0 / {r['quotes']}"
        L.append(f"| `{r['model']}`{' (incumbent)' if r['model'] == incumbent_model else ''} | {r['paper']} | {absent} | {r['verified']} | {r['schema_issues']} | "
                 f"{r['findings']} / {r['drafts']} entries vs {r['ref_findings']} / {r['ref_entries']} | "
                 f"{r['shared_links']} / {r['ref_links']} ({pct(r['link_recall'])}) | "
                 f"{r['strength'] if r['strength'] is not None else '—'} vs {r['ref_strength'] if r['ref_strength'] is not None else '—'} | "
                 f"{r['confidence'] if r['confidence'] is not None else '—'} vs {r['ref_confidence'] if r['ref_confidence'] is not None else '—'} | "
                 f"{r['passages_per_finding']} | {_hms(r.get('elapsed_s'))}{(' · ' + r['processor']) if r.get('processor') else ''} |")
    L.append("")
    L.append("| Model | Eligible for `extract`? | Why / why not | Absent | Schema | Link recall | Link precision | Strength − ref | Mean time |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for m, v in verdicts.items():
        L.append(f"| `{m}`{' (incumbent)' if m == incumbent_model else ''} | {'**yes**' if v['eligible'] else 'no'} | {'; '.join(v['reasons']) or 'zero absent quotes; schema and calibration not worse than the incumbent'} | "
                 f"{v['absent']} | {v['schema_issues']} | {pct(v['link_recall'])} | {pct(v['link_precision'])} | {v['calibration_delta']:+.2f} | {_hms(v['mean_elapsed_s'])} |")
    return "\n".join(L)


def _remember_timing(sandbox: Path, paper: str, timing: dict) -> dict:
    """How long an extraction took is only known while it runs: keep it beside the drafts
    (_timings.json) so a later --resume or --skip-extract can still report it."""
    path = sandbox / "_timings.json"
    try:
        known = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except ValueError:
        known = {}
    if timing.get("elapsed_s") is not None and timing.get("ok", True):
        known[paper] = {k: timing[k] for k in ("elapsed_s", "processor") if timing.get(k) is not None}
        if sandbox.is_dir():
            path.write_text(json.dumps(known, indent=1), encoding="utf-8")
        return timing
    return known.get(paper) or timing


PUBLIC = ROOT / "export" / "model-benchmark.json"
_PUBLIC_ROW = ("paper", "failed", "ungraded", "drafts", "findings", "ref_findings", "ref_entries", "quotes", "absent", "verified", "near",
               "anchored", "schema_issues", "no_quote_findings", "links", "ref_links", "shared_links", "link_recall", "link_precision",
               "relationship_agreement", "missed_links", "new_links", "strength", "ref_strength", "confidence", "ref_confidence",
               "passages_per_finding", "elapsed_s", "processor")


MODEL_SOURCES = ROOT / "model_sources.yaml"
_SOURCE_KEYS = ("family", "developer", "released", "licence", "licence_url", "architecture", "context", "data_cutoff",
                "lineage", "upstream", "library", "weights", "checked")
_SHOW_KEYS = {"architecture": "architecture", "parameters": "parameters", "context length": "context_length",
              "quantization": "quantization", "format": "format"}


def model_sources(path: Path = MODEL_SOURCES) -> tuple[str, dict[str, dict]]:
    """model_sources.yaml → (the page-level note on how models are obtained, {tag: provenance}).
    Curated by hand; only the known fields are kept, as strings."""
    try:
        d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        return "", {}
    out = {}
    for tag, e in (d.get("models") or {}).items():
        out[str(tag)] = {k: " ".join(str(v).split()) for k, v in (e or {}).items() if k in _SOURCE_KEYS and v not in (None, "")}
    return " ".join(str(d.get("sourcing") or "").split()), out


def parse_ollama_show(text: str) -> dict:
    """The 'Model' block of `ollama show <tag>` → {architecture, parameters, context_length, quantization, format}."""
    out, section = {}, None
    for line in text.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= 2:
            section = line.strip().lower()
            continue
        if section == "model":
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=1)
            if len(parts) == 2 and parts[0].lower() in _SHOW_KEYS:
                out[_SHOW_KEYS[parts[0].lower()]] = parts[1].strip()
    return out


def ollama_facts(tag: str, host: str) -> dict:
    """What this machine actually runs under `tag`: `ollama show` (format, quantisation, parameters),
    the digest from `ollama list`, and the Ollama version. Empty when Ollama is not reachable."""
    env = dict(os.environ, OLLAMA_HOST=host)
    run = lambda *a: subprocess.run(["ollama", *a], capture_output=True, text=True, timeout=30, env=env)  # noqa: E731
    try:
        show = run("show", tag)
        if show.returncode != 0:
            return {}
        out = parse_ollama_show(show.stdout)
        for line in run("list").stdout.splitlines()[1:]:
            cells = line.split()
            if len(cells) > 1 and cells[0] == tag:
                out["digest"] = cells[1]
        m = re.search(r"(\d+\.\d+\.\d+\S*)", run("--version").stdout)
        if m:
            out["ollama_version"] = m.group(1)
        return out
    except Exception:  # noqa: BLE001
        return {}


def attach_sources(data: dict, host: str | None = None) -> dict:
    """Add each model's provenance (model_sources.yaml) to the public summary and, when Ollama is
    reachable, what was installed on this machine. Facts recorded earlier are kept when Ollama is not."""
    sourcing, srcs = model_sources()
    caveats = {c["tag"]: c.get("caveat") for c in candidates_from_models_md()[0]}
    if sourcing:
        data["sourcing"] = sourcing
    for m in data.get("models") or []:
        if caveats.get(m.get("model")):
            m["note"] = caveats[m["model"]]
        if srcs.get(m.get("model")):
            m["source"] = srcs[m["model"]]
        else:
            m.pop("source", None)
        facts = ollama_facts(m["model"], host) if host else {}
        if facts:
            m["local"] = facts
    return data


def publish(rows: list[dict], verdicts: dict[str, dict], incumbent_model: str, papers: list[str], seed, by: str, path: Path = PUBLIC, host: str | None = None) -> Path:
    """The public summary for the explorer's Models page: numbers and ids only — no quote text, no
    file names from the papers folder, nothing a publisher could object to."""
    try:
        cfg = yaml.safe_load(MODELS_YAML.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        cfg = {}
    roles = {name: {"model": (r or {}).get("model") or cfg.get("default")} for name, r in (cfg.get("roles") or {}).items()}
    cands = {c["tag"]: c for c in candidates_from_models_md()[0]}
    refs = {r["citation"].lstrip("@"): r for r in reference_papers()}
    models = []
    for m, v in verdicts.items():
        mine = [r for r in rows if r["model"] == m]
        c = cands.get(m) or {}
        models.append({"model": m, "incumbent": m == incumbent_model, **v, "ram_class": c.get("ram_class"), "note": c.get("caveat"),
                       "quotes": sum(r.get("quotes") or 0 for r in mine), "verified": sum(r.get("verified") or 0 for r in mine),
                       "findings": sum(r.get("findings") or 0 for r in mine), "ref_findings": sum(r.get("ref_findings") or 0 for r in mine),
                       "shared_links": sum(r.get("shared_links") or 0 for r in mine), "ref_links": sum(r.get("ref_links") or 0 for r in mine),
                       "links": sum(r.get("links") or 0 for r in mine),
                       "processor": next((r.get("processor") for r in mine if r.get("processor")), None),
                       "rows": [{k: r.get(k) for k in _PUBLIC_ROW if r.get(k) is not None} for r in mine]})
    data = {"schema": 1, "date": dt.date.today().isoformat(), "by": by, "incumbent": incumbent_model, "roles": roles, "seed": seed,
            "reference": REFERENCE, "reference_text": REFERENCE_TEXT[REFERENCE],
            "papers": [{"key": p, "findings": usable_count(refs[p]) if p in refs else 0,            # the findings the models were scored against
                        "left_out": (refs[p]["findings"] - usable_count(refs[p])) if p in refs else 0,   # canonical findings not used as reference
                        "human_reviewed": (refs.get(p) or {}).get("human"), "model_approved": (refs.get(p) or {}).get("model"),
                        "all_human": bool((refs.get(p) or {}).get("all_human")), "bucket": (refs.get(p) or {}).get("main_bucket")} for p in papers],
            "models": models,
            "rule": "Eligible = zero absent quotes on every paper, and schema issues and over-claiming no worse than the incumbent (docs/MODELS.md §3)."}
    attach_sources(data, host)
    path.parent.mkdir(parents=True, exist_ok=True)
    from pipeline_files import atomic_write
    data["manifest_version"] = manifest["version"]
    atomic_write(path, json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    return path


def log_rows(rows: list[dict], by: str) -> list[str]:
    """Rows in the shape of the decision log in docs/MODELS.md §5 (Decision left for a person)."""
    today = dt.date.today().isoformat()
    out = []
    for r in rows:
        if r.get("failed"):
            out.append(f"| {today} | extract | `{r['model']}` | {r['paper']} | — | — | 0 drafts | — | {_hms(r.get('elapsed_s'))} | **Failed:** no drafts returned (see _compare/). | {by} |")
            continue
        absent = f"**{r['absent']}/{r['quotes']} absent**" if r["absent"] else f"**0/{r['quotes']} absent** ({r['verified']} verified, {r['anchored']} anchored, {r['near']} near)"
        out.append(f"| {today} | extract | `{r['model']}` | {r['paper']} | {absent} | {r['schema_issues']} issue(s) | "
                   f"{r['findings']} findings / {r['drafts']} entries vs {r['ref_findings']} / {r['ref_entries']}; link recall {pct(r['link_recall'])} ({r['shared_links']}/{r['ref_links']}) | "
                   f"{r['strength'] if r['strength'] is not None else '—'} vs {r['ref_strength'] if r['ref_strength'] is not None else '—'} | "
                   f"{_hms(r.get('elapsed_s'))}{(', ' + r['processor']) if r.get('processor') else ''} | *(decision pending — benchmark_models.py)* | {by} |")
    return out


def append_log(lines: list[str], md_path: Path = MODELS_MD) -> bool:
    text = md_path.read_text(encoding="utf-8")
    i = text.find("## 5. Decision log")
    if i < 0:
        return False
    # the table ends at the first blank line after its header rows
    j = text.find("\n|", i)
    if j < 0:
        return False
    k = text.find("\n\n", j)
    k = len(text) if k < 0 else k
    new = text[:k].rstrip("\n") + "\n" + "\n".join(lines) + text[k:]
    md_path.write_text(new, encoding="utf-8")
    return True


# ------------------------------------------------------------------ main
def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list-references", action="store_true", help="show papers that can serve as the curated reference")
    ap.add_argument("--models", nargs="*", default=[], help="Ollama tags to compare (the incumbent from models.yaml is added unless --no-incumbent)")
    ap.add_argument("--papers", nargs="*", default=[], help="citation keys without @ (see --list-references)")
    ap.add_argument("--untested", action="store_true", help="instead of --models: every candidate in MODELS.md §4 that fits this machine and has no §5 row or sandbox yet")
    ap.add_argument("--ram", type=int, metavar="GB", help="with --untested: the machine's memory (default: detected)")
    ap.add_argument("--no-pull", action="store_true", help="do not `ollama pull` missing models; skip them instead")
    ap.add_argument("--all-candidates", action="store_true", help="with --untested: also the low-priority rows (superseded generations, smaller quants, 'only to settle' variants)")
    ap.add_argument("--exclude", nargs="*", default=[], metavar="TAG", help="tags to leave out")
    ap.add_argument("--auto-papers", type=int, metavar="N", help="instead of --papers: pick N random reference papers from different buckets")
    ap.add_argument("--min-findings", type=int, default=5, help="with --auto-papers: a paper needs at least this many canonical findings (default 5)")
    ap.add_argument("--seed", type=int, help="with --auto-papers: make the random pick repeatable")
    ap.add_argument("--no-incumbent", action="store_true")
    ap.add_argument("--reference", choices=sorted(REFERENCE_KINDS), default="current",
                    help="which canonical findings the models are scored against: current = approved under the governance policy, "
                         "legacy left out (default); human = approved by a person only; all = everything, legacy included")
    ap.add_argument("--skip-extract", action="store_true", help="only score sandboxes that already exist")
    ap.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    ap.add_argument("--timeout", type=int, default=7200, help="seconds per paper (default 2 h)")
    ap.add_argument("--pulled", action="store_true", help="instead of --models: every model of MODELS.md §4 (and the incumbent) that is already pulled in Ollama; nothing is downloaded")
    ap.add_argument("--sandboxes", action="store_true", help="also score every known model (incumbent, MODELS.md §4) that already has a sandbox in _compare/")
    ap.add_argument("--resume", action="store_true", help="do not extract a model × paper again when its drafts are already in _compare/; just score them")
    ap.add_argument("--publish", action="store_true", help="write export/model-benchmark.json, the numbers-only summary the explorer's Models page shows (commit it)")
    ap.add_argument("--refresh-sources", action="store_true", help="only update where each model comes from (model_sources.yaml, and `ollama show` when Ollama runs) in export/model-benchmark.json; nothing is extracted or scored")
    ap.add_argument("--append-log", action="store_true", help="append the rows to docs/MODELS.md §5 (decision left blank)")
    ap.add_argument("--by", default=os.environ.get("USER", "maintainer"), help="name for the log rows")
    args = ap.parse_args(argv)
    global REFERENCE
    REFERENCE = args.reference

    if args.list_references:
        print_references(reference_papers())
        return 0
    if args.refresh_sources:
        if not PUBLIC.is_file():
            print(f"No {PUBLIC.relative_to(ROOT)} yet: run a benchmark with --publish first.")
            return 1
        data = attach_sources(json.loads(PUBLIC.read_text(encoding="utf-8")), args.ollama_host)
        PUBLIC.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        missing = [m["model"] for m in data.get("models") or [] if not m.get("source")]
        local = [m["model"] for m in data.get("models") or [] if m.get("local")]
        print(f"Updated {PUBLIC.relative_to(ROOT)}: provenance for {len(data.get('models') or []) - len(missing)} model(s), "
              f"local install facts for {len(local)}." + (f" Not in model_sources.yaml: {', '.join(missing)}." if missing else ""))
        return 0
    if args.untested:
        ram = args.ram or machine_ram_gb()
        cands, notes = untested_candidates(ram, args.ollama_host)
        for n_ in notes:
            print(f"  · {n_}")
        if not cands:
            print(f"Nothing left to test: every candidate in docs/MODELS.md §4 that fits {ram or '?'} GB has a row in §5 or a sandbox in _compare/.")
            return 0
        skipped = [c["tag"] for c in cands if c.get("low_priority") and not args.all_candidates]
        cands = [c for c in cands if not (c.get("low_priority") and not args.all_candidates)]
        if skipped:
            print("  · low priority, skipped (add --all-candidates to include): " + ", ".join(skipped))
        print(f"Untested candidates for a {ram or '?'} GB machine (from docs/MODELS.md §4): " + ", ".join(c["tag"] for c in cands))
        args.models = list(dict.fromkeys(args.models + [c["tag"] for c in cands]))
    if args.pulled:
        have = ollama_list(args.ollama_host)
        known = [incumbent()] + [c["tag"] for c in candidates_from_models_md()[0]]
        local = [t for t in dict.fromkeys(known) if t and (t in have or f"{t}:latest" in have)]
        absent = [t for t in dict.fromkeys(known) if t and t not in local]
        print(f"  · pulled on this machine: {', '.join(local) or 'none'}")
        if absent:
            print(f"  · listed in MODELS.md but not pulled, so not run: {', '.join(absent)}")
        args.models = list(dict.fromkeys(local + args.models))
    if args.sandboxes:
        known = [incumbent()] + [c["tag"] for c in candidates_from_models_md()[0]]
        have = [t for t in dict.fromkeys(known) if t and (COMPARE / slug(t) / "drafts").is_dir()]
        print(f"  · with a sandbox in _compare/: {', '.join(have) or 'none'}")
        sandbox_only = [t for t in have if t not in args.models]
        args.models = list(dict.fromkeys(have + args.models))
    if args.exclude:
        args.models = [m for m in args.models if m not in set(args.exclude)]
    if not args.sandboxes:
        sandbox_only = []
    picked_note = []
    if args.auto_papers and not args.papers:
        picked, picked_note = pick_papers(reference_papers(), args.auto_papers, args.min_findings, args.seed)
        args.papers = [r["citation"].lstrip("@") for r in picked]
        if picked:
            print("Papers picked at random (" + (f"seed {args.seed}" if args.seed is not None else "no seed") + "): "
                  + "; ".join(f"{r['citation']} ({r['findings']} findings, {r['main_bucket']}{'' if r['all_human'] else ', not all human-reviewed'})" for r in picked))
        for n_ in picked_note:
            print(f"  ⚠ {n_}")
    if not args.models or not args.papers:
        ap.error("--models and --papers (or --auto-papers N) are required, or --list-references")
    inc = incumbent()
    # A sandbox left by an older run that never saw these papers would show as a failure it is not.
    stale = [t for t in sandbox_only if t != inc and not all(CE._find_entries(COMPARE / slug(t), f"@{p}") for p in args.papers)]
    if stale:
        print(f"  · left out, their sandbox does not hold all of these papers (name them with --models to run them): {', '.join(stale)}")
        args.models = [m for m in args.models if m not in stale]
    models = list(dict.fromkeys(([inc] if inc and not args.no_incumbent else []) + args.models))
    if not args.skip_extract:
        models = ensure_pulled(models, args.ollama_host, pull=not args.no_pull)
        if not models:
            print("No model available to run.", file=sys.stderr)
            return 2
    missing = [p for p in args.papers if not (PAPERS / f"{p}.pdf").exists()]
    if missing:
        print(f"no PDF in papers/ for: {', '.join(missing)}", file=sys.stderr)
        return 2
    refs = {r["citation"].lstrip("@"): r for r in reference_papers()}
    for p in args.papers:
        r = refs.get(p)
        if r is None:
            print(f"  ⚠ {p}: no canonical findings cite it — coverage and calibration cannot be measured, fidelity can")
        else:
            used, left = usable_count(r), r["findings"] - usable_count(r)
            print(f"  · {p}: reference = {used} finding(s) ({r['human']} approved by a person, {r['model']} model-approved)"
                  + (f"; {left} left out ({REFERENCE_TEXT[REFERENCE]})" if left else ""))
            if used < 3:
                print(f"  ⚠ {p}: only {used} reference finding(s) — coverage and calibration on this paper say very little")

    if not args.skip_extract:
        n_runs = len(models) * len(args.papers)
        print(f"\n{len(models)} model(s) × {len(args.papers)} paper(s) = {n_runs} extraction(s); at 20–40 min each expect roughly "
              f"{n_runs * 20 // 60}–{n_runs * 40 // 60} h. Each paper's result is scored as soon as it finishes; Ctrl-C keeps what is done "
              f"(re-score later with --skip-extract).")
    rows: list[dict] = []
    for m in models:
        sandbox = COMPARE / slug(m)
        for p in args.papers:
            timing: dict = {}
            if args.resume and not args.skip_extract and CE._find_entries(sandbox, f"@{p}"):
                print(f"\n↷ {m} × {p}: drafts already in {sandbox.relative_to(ROOT)}/ — kept, scoring them", flush=True)
            elif not args.skip_extract:
                print(f"\n▶ {m} × {p}  →  {sandbox.relative_to(ROOT)}/   ({dt.datetime.now():%H:%M:%S})", flush=True)
                for old in CE._find_entries(sandbox, f"@{p}"):       # a fresh run must not be scored together with an older run's drafts
                    old.unlink()
                timing = run_extraction(m, p, sandbox, args.ollama_host, args.timeout)
                if not timing["ok"]:
                    print("  ✗ extraction failed:\n    " + timing["tail"].replace("\n", "\n    "))
                else:
                    print(f"  done in {_hms(timing['elapsed_s'])}{(' · ' + timing['processor']) if timing.get('processor') else ''}")
            timing = _remember_timing(sandbox, p, timing)
            try:
                r = score(m, p, sandbox)
            except Exception as e:  # noqa: BLE001 — one result that cannot be scored must not end a run of many hours
                print(f"  ✗ {m} × {p} could not be scored: {type(e).__name__}: {str(e)[:200]} (counted as a failure; --skip-extract scores it again)")
                r = {"model": m, "paper": p, "failed": True, "absent": None, "drafts": 0, "findings": 0, "error": f"{type(e).__name__}: {str(e)[:200]}"}
            r.update({k: timing.get(k) for k in ("elapsed_s", "processor") if timing.get(k) is not None})
            rows.append(r)
            if not r.get("failed"):
                print(f"  {m} × {p}: {r['absent']}/{r['quotes']} absent · {r['schema_issues']} schema issues · "
                      f"{r['findings']} findings vs {r['ref_findings']} · links {r['shared_links']}/{r['ref_links']} ({pct(r['link_recall'])}) · "
                      f"strength {r['strength']} vs {r['ref_strength']}")
    verdicts = summarise(rows, inc)
    md = table(rows, verdicts, inc)
    print("\n" + md)
    COMPARE.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    (COMPARE / f"benchmark_{stamp}.json").write_text(json.dumps({"date": stamp, "incumbent": inc, "papers": args.papers, "seed": args.seed, "picked_notes": picked_note,
                                                                  "rows": rows, "verdicts": verdicts}, indent=1), encoding="utf-8")
    (COMPARE / f"benchmark_{stamp}.md").write_text(f"# Model benchmark {stamp}\n\nIncumbent: `{inc}`\n\n{md}\n", encoding="utf-8")
    print(f"\nWritten: _compare/benchmark_{stamp}.md and .json")
    if args.publish:
        out = publish(rows, verdicts, inc, args.papers, args.seed, args.by, host=args.ollama_host)
        print(f"Published the numbers-only summary: {out.relative_to(ROOT)} — commit and push it; the explorer's Models page reads it.")
    if args.append_log:
        ok = append_log(log_rows(rows, args.by))
        print("Appended to docs/MODELS.md §5 — fill in the Decision column." if ok else "Could not find the decision log table in docs/MODELS.md.")
    eligible = [m for m, v in verdicts.items() if v["eligible"] and m != inc]
    if eligible:
        print(f"\nEligible to replace the incumbent on these papers: {', '.join(eligible)}. Read the claims (compare_extraction.py --show-claims) before deciding.")
    else:
        print(f"\nNo candidate beats the decision rule against `{inc}` on these papers.")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
