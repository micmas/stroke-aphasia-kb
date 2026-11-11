#!/usr/bin/env python3
"""
recheck_drafts.py — check every draft against its paper and have the current extractor
rewrite the ones that fail, leaving alone anything a person has worked on.

    python scripts/recheck_drafts.py
        # audit only (no model, a few minutes): every quote of every draft is searched for in
        # the paper's PDF and every draft is validated; prints, paper by paper, what is wrong,
        # which papers would be re-extracted and which are a person's to look at

    python scripts/recheck_drafts.py --execute
        # re-extract the failing papers with the model in models.yaml (roles.extract), one
        # after the other; the old drafts are moved to drafts/_backup/<stamp>/ first

    python scripts/recheck_drafts.py --execute --limit 10        # ten papers tonight, the rest later
    python scripts/recheck_drafts.py --papers Robson2019 Bates2003 --execute

A paper is rewritten when one of its drafts has a quote that is nowhere in the paper (the
fabrication signal of quote_check.py), or does not pass the schema (including a file that
cannot be parsed). Nothing else is a reason: fewer findings than you hoped, or a strength you
would word differently, is what review is for.

A paper is never rewritten when a person has touched any of its drafts — portal reviews,
edits, reviewer marks or comments, a re-review in progress (`rereview_of`), a status other
than `draft` — because re-extraction replaces the drafts and would discard that work. Those
papers are listed under "for a person" with what the audit found.

The rewrite is kept only if it is better: fewer absent quotes, or as few and fewer schema
issues. Otherwise the old drafts are put back and the paper is listed for a person. A paper
whose rewrite is kept gets one `RECHECK` line in logs/extraction_log.md.

Stopping and carrying on: Ctrl-C puts the drafts of the paper being rewritten back as they
were and stops; papers already rewritten stay. Run the same command again and it re-audits
(a few minutes), skips what now passes and what was already tried without success with this
model (--retry tries those again), and continues with the rest.

The report is written to _compare/recheck_<stamp>.md (git-ignored: it quotes the papers).
Afterwards: `python scripts/auto_review.py --all`, then `python scripts/publish_portal.py
--sync` (re-extraction re-annotates the PDFs) and commit.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import compare_extraction as CE  # noqa: E402
from aphasia_kb import parse_markdown  # noqa: E402

DRAFTS = ROOT / "drafts"
PAPERS = ROOT / "papers"
BACKUP = DRAFTS / "_backup"
LOG = ROOT / "logs" / "extraction_log.md"
REPORTS = ROOT / "_compare"
BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews", "ingredients")


# ------------------------------------------------------------------ the drafts, paper by paper
def paper_key(path: Path) -> str | None:
    """`left_angular_gyrus__Alyahya2018NounVerb.md` → `Alyahya2018NounVerb`; else the first finding's citation."""
    if "__" in path.stem:
        key = path.stem.split("__", 1)[1]
        return None if key == "nocitation" else key
    try:
        fm, _ = parse_markdown(path)
    except Exception:  # noqa: BLE001
        return None
    for f in (fm or {}).get("findings") or []:
        if isinstance(f, dict) and f.get("citation"):
            return str(f["citation"]).lstrip("@")
    return None


def drafts_by_paper(drafts: Path = DRAFTS) -> dict[str, list[Path]]:
    out: dict[str, list[Path]] = {}
    for b in BUCKETS:
        for p in sorted((drafts / b).glob("*.md")) if (drafts / b).is_dir() else []:
            key = paper_key(p)
            if key:
                out.setdefault(key, []).append(p)
    return out


def touched_by_a_person(path: Path) -> str:
    """Why this draft must not be rewritten, or '' when only a model has written it."""
    try:
        fm, _ = parse_markdown(path)
    except Exception:  # noqa: BLE001
        return "unparsable existing draft: human inspection required"
    if not isinstance(fm, dict):
        return ""
    if str(fm.get("status") or "draft") != "draft":
        return f"status {fm.get('status')}"
    for field, why in (("portal_reviews", "portal review"), ("reviewer_marks", "reviewer marks"), ("portal_comments", "comments"),
                       ("rereview_of", "re-review in progress"), ("reviewer", "a named reviewer")):
        if fm.get(field):
            return why
    if not str(fm.get("created_by") or "").startswith("agent:"):
        return f"written by {fm.get('created_by') or 'a person'}"
    for f in fm.get("findings") or []:
        if isinstance(f, dict) and (f.get("edits") or f.get("review") or f.get("portal_comments")):
            return "edited or reviewed findings"
    return ""


def audit(key: str, paths: list[Path], papers: Path = PAPERS) -> dict:
    cit = f"@{key}"
    from quote_check import find_paper
    pdf = find_paper(cit, papers)
    findings = CE._load_findings(paths, cit)
    issues = CE._schema_issues(paths)
    q = CE._quote_check(findings, papers) if pdf else {"total": 0, "absent": 0, "absent_list": []}
    touched = sorted({w for w in (touched_by_a_person(p) for p in paths) if w})
    if pdf and pdf.suffix.lower() != ".pdf":
        touched.append("only a text copy of the paper is here, which the extractor cannot read")
    reasons = []
    if q["absent"]:
        reasons.append(f"{q['absent']} of {q['total']} quotes are not in the paper")
    n_issues = sum(len(v) for v in issues.values())
    if n_issues:
        reasons.append(f"{n_issues} schema issue(s)")
    return {"key": key, "paths": paths, "pdf": pdf, "findings": len(findings), "quotes": q["total"], "absent": q["absent"],
            "absent_list": list(q.get("absent_list") or []), "schema_issues": n_issues,
            "schema_examples": [f"{name}: {x}" for name, v in issues.items() for x in v][:6],
            "touched": touched, "reasons": reasons}


ATTEMPTS = BACKUP / "recheck_attempts.json"


def load_attempts(path: Path = ATTEMPTS) -> dict:
    """Papers whose rewrite was tried and not kept: {key: {model, date, why}} — so the next run
    does not spend another twenty minutes on the same paper with the same model."""
    try:
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except ValueError:
        return {}


def plan(rows: list[dict], attempts: dict | None = None, model: str | None = None, retry: bool = False) -> dict[str, list[dict]]:
    out = {"rewrite": [], "person": [], "no_pdf": [], "fine": []}
    for r in rows:
        tried = (attempts or {}).get(r["key"])
        if not r["pdf"]:
            out["no_pdf"].append(r)
        elif not r["reasons"]:
            out["fine"].append(r)
        elif r["touched"]:
            out["person"].append(r)
        elif tried and not retry and tried.get("model") == model:
            r["touched"] = [f"a rewrite with {tried['model']} on {tried.get('date', '?')} was not kept: {tried.get('why', '')}"]
            out["person"].append(r)
        else:
            out["rewrite"].append(r)
    return out


# ------------------------------------------------------------------ rewriting one paper
def run_extract(key: str, pdf: Path, model: str | None, timeout: int) -> tuple[bool, str]:
    cmd = [sys.executable, str(ROOT / "scripts" / "extract.py"), "--pdf", str(pdf), "--citation", f"@{key}", "--timeout", str(timeout)]
    if model:
        cmd += ["--model", model]
    done = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return done.returncode == 0, "\n".join((done.stdout or "").splitlines()[-6:])


def better(new: dict, old: dict) -> bool:
    return (new["absent"], new["schema_issues"]) < (old["absent"], old["schema_issues"]) and new["findings"] > 0


def rewrite(r: dict, stamp: str, model: str | None, timeout: int, extract=run_extract,
            drafts: Path = DRAFTS, papers: Path = PAPERS, backup: Path = BACKUP) -> dict:
    """Back the paper's drafts up, extract again, keep the result only if it is better. Returns the outcome."""
    key = r["key"]
    saved: list[tuple[Path, Path]] = []

    def restore() -> None:
        for p in drafts_by_paper(drafts).get(key, []):
            p.unlink()                              # whatever the interrupted or failed attempt left
        for orig, dest in saved:
            orig.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, orig)

    if any(touched_by_a_person(p) for p in r["paths"]):
        raise ValueError("Refusing to rewrite protected drafts")
    t0 = time.monotonic()
    removed = False
    try:
        for p in r["paths"]:                        # copy first, delete after: a draft is never in neither place
            dest = backup / stamp / p.parent.name / p.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)
            saved.append((p, dest))
        removed = True
        for p, _ in saved:
            p.unlink()
        ok, tail = extract(key, r["pdf"], model, timeout)
    except BaseException:
        if removed:
            restore()                                   # Ctrl-C: this paper is back as it was; run again to carry on
        raise
    elapsed = round(time.monotonic() - t0)
    new_paths = drafts_by_paper(drafts).get(key, [])
    if not ok or not new_paths:
        restore()
        return {"key": key, "kept": False, "why": "the extraction failed or returned no drafts; old drafts put back", "tail": tail, "elapsed_s": elapsed, "old": r}
    try:
        new = audit(key, new_paths, papers)
    except BaseException:
        restore()
        raise
    if not better(new, r):
        restore()
        return {"key": key, "kept": False, "elapsed_s": elapsed, "old": r, "new": new,
                "why": f"the rewrite was not better ({new['absent']} absent, {new['schema_issues']} schema issue(s), {new['findings']} findings); old drafts put back"}
    return {"key": key, "kept": True, "elapsed_s": elapsed, "old": r, "new": new, "why": ""}


# ------------------------------------------------------------------ report
def _mins(s) -> str:
    return f"{int(s) // 60} min {int(s) % 60:02d} s"


def report(groups: dict[str, list[dict]], outcomes: list[dict], model: str, executed: bool) -> str:
    L = [f"# Draft recheck {dt.datetime.now():%Y-%m-%d %H:%M}", "",
         f"Extractor: `{model}`. {sum(len(v) for v in groups.values())} papers with drafts: {len(groups['fine'])} pass, "
         f"{len(groups['rewrite'])} to rewrite, {len(groups['person'])} for a person, {len(groups['no_pdf'])} without a PDF here.", ""]
    if outcomes:
        L += ["## Rewritten", "", "| Paper | Before | After | Kept? | Time |", "|---|---|---|---|---|"]
        for o in outcomes:
            old, new = o["old"], o.get("new")
            L.append(f"| {o['key']} | {old['absent']} absent, {old['schema_issues']} schema, {old['findings']} findings | "
                     + (f"{new['absent']} absent, {new['schema_issues']} schema, {new['findings']} findings" if new else "—")
                     + f" | {'**yes**' if o['kept'] else 'no: ' + o['why']} | {_mins(o['elapsed_s'])} |")
        L.append("")
    todo = [r for r in groups["rewrite"] if r["key"] not in {o["key"] for o in outcomes}]
    if todo:
        L += [f"## {'Still to rewrite' if executed else 'Would be rewritten'} ({len(todo)})", ""]
        for r in todo:
            L.append(f"- **{r['key']}** ({len(r['paths'])} drafts, {r['findings']} findings): {'; '.join(r['reasons'])}")
            L += [f"    - not in the paper: {x}" for x in r["absent_list"][:3]] + [f"    - {x}" for x in r["schema_examples"][:3]]
        L.append("")
    if groups["person"]:
        L += [f"## For a person ({len(groups['person'])}): a problem was found, but someone has worked on these drafts", ""]
        for r in groups["person"]:
            L.append(f"- **{r['key']}** ({', '.join(r['touched'])}): {'; '.join(r['reasons'])}")
            L += [f"    - not in the paper: {x}" for x in r["absent_list"][:3]] + [f"    - {x}" for x in r["schema_examples"][:3]]
        L.append("")
    kept_back = [o for o in outcomes if not o["kept"]]
    if kept_back:
        L += [f"## Rewrite not kept ({len(kept_back)}): old drafts are back, these need a person", ""] + [f"- **{o['key']}**: {o['why']}" for o in kept_back] + [""]
    if groups["no_pdf"]:
        L += [f"## Not checked: no PDF in papers/ ({len(groups['no_pdf'])})", "", ", ".join(r["key"] for r in groups["no_pdf"]), ""]
    return "\n".join(L)


# ------------------------------------------------------------------ run
def run(execute: bool, only: list[str] | None, limit: int | None, model: str | None, timeout: int, by: str, retry: bool = False) -> int:
    from model_config import model_for
    try:
        tag = model or model_for("extract")
    except Exception:  # noqa: BLE001
        tag = model or "the model in models.yaml"
    grouped = drafts_by_paper()
    if only:
        want = {k.lstrip("@") for k in only}
        grouped = {k: v for k, v in grouped.items() if k in want}
    print(f"Checking {sum(len(v) for v in grouped.values())} drafts of {len(grouped)} papers against their PDFs…", flush=True)
    rows = [audit(k, v) for k, v in sorted(grouped.items())]
    attempts = load_attempts()
    groups = plan(rows, attempts, tag, retry)
    print(f"  {len(groups['fine'])} pass · {len(groups['rewrite'])} to rewrite · {len(groups['person'])} for a person · {len(groups['no_pdf'])} without a PDF here")
    todo = groups["rewrite"][:limit] if limit else groups["rewrite"]
    outcomes: list[dict] = []
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    if execute and todo:
        print(f"\nRe-extracting {len(todo)} paper(s) with {tag}; old drafts go to drafts/_backup/{stamp}/. Ctrl-C stops after putting the current paper's drafts back.")
        try:
            for i, r in enumerate(todo, 1):
                print(f"\n▶ {i}/{len(todo)} {r['key']}: {'; '.join(r['reasons'])}   ({dt.datetime.now():%H:%M:%S})", flush=True)
                o = rewrite(r, stamp, model, timeout)
                outcomes.append(o)
                if o["kept"]:
                    n = o["new"]
                    print(f"  ✓ kept: {n['absent']} absent of {n['quotes']} quotes, {n['schema_issues']} schema issue(s), {n['findings']} findings · {_mins(o['elapsed_s'])}")
                    LOG.parent.mkdir(parents=True, exist_ok=True)
                    with LOG.open("a", encoding="utf-8") as fh:
                        fh.write(f"{dt.date.today().isoformat()} | RECHECK | @{o['key']} | absent {r['absent']}→{n['absent']}, schema {r['schema_issues']}→{n['schema_issues']}, "
                                 f"findings {r['findings']}→{n['findings']} | rewritten by {tag} | old drafts: drafts/_backup/{stamp}/ | by: human:{by}\n")
                else:
                    print(f"  · {o['why']}")
                    attempts[o["key"]] = {"model": tag, "date": dt.date.today().isoformat(), "why": o["why"]}
                    ATTEMPTS.parent.mkdir(parents=True, exist_ok=True)
                    ATTEMPTS.write_text(json.dumps(attempts, indent=1), encoding="utf-8")
        except KeyboardInterrupt:
            print("\nStopped. The paper that was being rewritten is back as it was; the ones already done stay. "
                  "Run the same command again to carry on with the rest.")
    elif todo:
        print(f"\nDry run: {len(todo)} paper(s) would be re-extracted with {tag} (roughly {len(todo) * 5}–{len(todo) * 12} min). Add --execute.")
        for r in todo[:40]:
            print(f"  {r['key']}: {'; '.join(r['reasons'])}")
    text = report(groups, outcomes, tag, execute)
    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"recheck_{stamp}.md"
    out.write_text(text + "\n", encoding="utf-8")
    print(f"\nReport: {out.relative_to(ROOT)}")
    if outcomes:
        print("Next: python scripts/auto_review.py --all, then python scripts/publish_portal.py --sync, and commit.")
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--execute", action="store_true", help="re-extract the failing papers (default: audit and report only)")
    ap.add_argument("--papers", nargs="*", metavar="KEY", help="only these citation keys")
    ap.add_argument("--limit", type=int, metavar="N", help="with --execute: at most N papers this run")
    ap.add_argument("--model", default=None, help="extractor tag for this run (default: roles.extract in models.yaml)")
    ap.add_argument("--timeout", type=int, default=3600, help="seconds per paper (default 1 h)")
    ap.add_argument("--retry", action="store_true", help="try again the papers whose rewrite with this model was not kept last time")
    ap.add_argument("--by", default="michele", help="name for the log lines (default michele)")
    args = ap.parse_args(argv)
    return run(args.execute, args.papers, args.limit, args.model, args.timeout, args.by, args.retry)


if __name__ == "__main__":
    sys.exit(_cli())
