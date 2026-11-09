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

    python scripts/benchmark_models.py ... --append-log
        # also append one row per model × paper to the decision log in docs/MODELS.md §5

Scoring, in the order a failure stops the reading (MODELS.md §3):

  1. fidelity    absent quotes / all quotes — any absent quote disqualifies the model for
                 `extract` (a quote that is not in the paper is a fabrication, not a style issue);
                 also the share verified (exact + elided + table) and the near/anchored rest
  2. schema      validation issues across the drafts (errors cost review time on every paper)
  3. coverage    findings and entries vs the curated reference, and target recall: the share of
                 the reference's (target, relationship) pairs the candidate also produced
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
                rec = by_cit.setdefault(cit, {"citation": cit, "findings": 0, "human": 0, "entries": set(), "buckets": set(), "per_bucket": {}})
                rec["findings"] += 1
                rec["human"] += 1 if kind == "human" else 0
                rec["entries"].add(fm.get("id")); rec["buckets"].add(b)
                rec["per_bucket"][b] = rec["per_bucket"].get(b, 0) + 1
    out = []
    for cit, rec in by_cit.items():
        key = cit.lstrip("@")
        pdf = papers_dir / f"{key}.pdf"
        rec["pdf"] = pdf.exists()
        rec["all_human"] = rec["human"] == rec["findings"]
        rec["entries"] = sorted(x for x in rec["entries"] if x); rec["buckets"] = sorted(rec["buckets"])
        rec["main_bucket"] = max(rec["per_bucket"], key=rec["per_bucket"].get)   # where most of its findings live
        out.append(rec)
    return sorted(out, key=lambda r: (-int(r["all_human"] and r["pdf"]), -r["findings"], r["citation"]))


def pick_papers(refs: list[dict], n: int = 2, min_findings: int = 5, seed: int | None = None) -> tuple[list[dict], list[str]]:
    """n random reference papers with at least min_findings canonical findings and a PDF, each from a
    different bucket (the bucket where most of its findings live). Human-reviewed papers are preferred;
    others fill in with a note. Returns (picked, notes)."""
    import random
    rng = random.Random(seed)
    pool = [r for r in refs if r["pdf"] and r["findings"] >= min_findings]
    notes = []
    if not pool:
        return [], [f"no paper has a PDF in papers/ and at least {min_findings} findings"]
    picked: list[dict] = []
    for prefer_human in (True, False):
        cands = [r for r in pool if r not in picked and (r["all_human"] or not prefer_human)]
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
        notes.append(f"only {len({q['main_bucket'] for q in picked})} distinct bucket(s) available among papers with ≥{min_findings} findings")
    if any(not r["all_human"] for r in picked):
        notes.append("some picked papers have legacy/model-reviewed findings: coverage and calibration against them are soft (fidelity is not)")
    return picked, notes


def print_references(refs: list[dict]) -> None:
    good = [r for r in refs if r["all_human"] and r["pdf"]]
    print(f"Reference candidates: {len(good)} papers with human-reviewed findings and a PDF\n")
    print(f"  {'paper':32} {'findings':>8}  {'entries':>7}  main bucket (all)")
    for r in good:
        print(f"  {r['citation']:32} {r['findings']:>8}  {len(r['entries']):>7}  {r['main_bucket']} ({', '.join(r['buckets'])})")
    rest = [r for r in refs if not (r["all_human"] and r["pdf"])]
    if rest:
        print(f"\n  not usable yet: {len(rest)} papers (legacy/model-reviewed findings, or no PDF in papers/)")
        for r in rest[:8]:
            why = [] if r["pdf"] else ["no PDF"]
            if not r["all_human"]:
                why.append(f"{r['findings'] - r['human']}/{r['findings']} findings not human-reviewed")
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
def _pairs(findings: list[dict]) -> set[tuple[str, str]]:
    return {(str(f.get("target") or "").lower(), str(f.get("relationship") or "").lower()) for f in findings if f.get("target")}


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
    ref_paths = canonical_entries(root, cit)
    cand_paths = CE._find_entries(sandbox, cit)
    ref_f = CE._load_findings(ref_paths, cit) if ref_paths else []
    cand_f = CE._load_findings(cand_paths, cit) if cand_paths else []
    out = {"model": model, "paper": paper, "drafts": len(cand_paths), "findings": len(cand_f), "ref_findings": len(ref_f),
           "ref_entries": len(ref_paths)}
    if not cand_paths:
        out.update({"failed": True, "absent": None})
        return out
    q = CE._quote_check(cand_f, papers_dir)
    issues = CE._schema_issues(cand_paths)
    verified = q["exact"] + q["elided"] + q["table"]
    has_passages = any((f.get("source_passages") or []) for f in cand_f)
    out.update({
        "ungraded": bool(has_passages and q["total"] == 0),   # passages exist but no PDF text to grade them against
        "quotes": q["total"], "absent": q["absent"], "verified": verified, "near": q["near"], "anchored": q["anchored"],
        "absent_examples": q["absent_list"][:3], "no_quote_findings": len(q["no_quotes"]),
        "schema_issues": sum(len(v) for v in issues.values()), "schema_examples": [x for v in issues.values() for x in v][:3],
        "passages_per_finding": round(q["total"] / len(cand_f), 1) if cand_f else 0.0,
        "target_recall": round(len(_pairs(ref_f) & _pairs(cand_f)) / len(_pairs(ref_f)), 2) if _pairs(ref_f) else None,
        "new_targets": sorted(t for t, _ in (_pairs(cand_f) - _pairs(ref_f)))[:5],
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
                  "target_recall": round(sum(r.get("target_recall") or 0 for r in rs) / max(1, len([r for r in rs if r.get("target_recall") is not None])), 2)}
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
    L = ["| Model | Paper | Absent / quotes | Verified | Schema issues | Findings vs ref | Target recall | Strength vs ref | Confidence vs ref | Passages / finding | Time · processor |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda x: (x["model"] != incumbent_model, x["model"], x["paper"])):
        if r.get("failed"):
            L.append(f"| `{r['model']}` | {r['paper']} | — | — | — | 0 drafts | — | — | — | — | {_hms(r.get('elapsed_s'))} |")
            continue
        absent = f"**{r['absent']}** / {r['quotes']}" if r["absent"] else f"0 / {r['quotes']}"
        L.append(f"| `{r['model']}`{' (incumbent)' if r['model'] == incumbent_model else ''} | {r['paper']} | {absent} | {r['verified']} | {r['schema_issues']} | "
                 f"{r['findings']} / {r['drafts']} entries vs {r['ref_findings']} / {r['ref_entries']} | "
                 f"{pct(r['target_recall'])} | "
                 f"{r['strength'] if r['strength'] is not None else '—'} vs {r['ref_strength'] if r['ref_strength'] is not None else '—'} | "
                 f"{r['confidence'] if r['confidence'] is not None else '—'} vs {r['ref_confidence'] if r['ref_confidence'] is not None else '—'} | "
                 f"{r['passages_per_finding']} | {_hms(r.get('elapsed_s'))}{(' · ' + r['processor']) if r.get('processor') else ''} |")
    L.append("")
    L.append("| Model | Eligible for `extract`? | Why / why not | Absent | Schema | Target recall | Strength − ref | Mean time |")
    L.append("|---|---|---|---|---|---|---|---|")
    for m, v in verdicts.items():
        L.append(f"| `{m}`{' (incumbent)' if m == incumbent_model else ''} | {'**yes**' if v['eligible'] else 'no'} | {'; '.join(v['reasons']) or 'zero absent quotes; schema and calibration not worse than the incumbent'} | "
                 f"{v['absent']} | {v['schema_issues']} | {v['target_recall']:.0%} | {v['calibration_delta']:+.2f} | {_hms(v['mean_elapsed_s'])} |")
    return "\n".join(L)


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
                   f"{r['findings']} findings / {r['drafts']} entries vs {r['ref_findings']} / {r['ref_entries']}; target recall {pct(r['target_recall'])} | "
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
    ap.add_argument("--skip-extract", action="store_true", help="only score sandboxes that already exist")
    ap.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    ap.add_argument("--timeout", type=int, default=7200, help="seconds per paper (default 2 h)")
    ap.add_argument("--append-log", action="store_true", help="append the rows to docs/MODELS.md §5 (decision left blank)")
    ap.add_argument("--by", default=os.environ.get("USER", "maintainer"), help="name for the log rows")
    args = ap.parse_args(argv)

    if args.list_references:
        print_references(reference_papers())
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
    if args.exclude:
        args.models = [m for m in args.models if m not in set(args.exclude)]
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
        elif not r["all_human"]:
            print(f"  ⚠ {p}: {r['findings'] - r['human']} of {r['findings']} reference findings are not human-reviewed (legacy/model) — calibration against them is soft")

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
            if not args.skip_extract:
                print(f"\n▶ {m} × {p}  →  {sandbox.relative_to(ROOT)}/   ({dt.datetime.now():%H:%M:%S})", flush=True)
                timing = run_extraction(m, p, sandbox, args.ollama_host, args.timeout)
                if not timing["ok"]:
                    print("  ✗ extraction failed:\n    " + timing["tail"].replace("\n", "\n    "))
                else:
                    print(f"  done in {_hms(timing['elapsed_s'])}{(' · ' + timing['processor']) if timing.get('processor') else ''}")
            r = score(m, p, sandbox)
            r.update({k: timing.get(k) for k in ("elapsed_s", "processor") if timing.get(k) is not None})
            rows.append(r)
            if not r.get("failed"):
                print(f"  {m} × {p}: {r['absent']}/{r['quotes']} absent · {r['schema_issues']} schema issues · "
                      f"{r['findings']} findings vs {r['ref_findings']} · recall {pct(r['target_recall'])} · "
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
