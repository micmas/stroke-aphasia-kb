#!/usr/bin/env python3
"""
refocus.py — targeted re-extraction: the passages a reviewer marked in the
review workbench become findings, written by the local model for exactly
those passages and nothing else.

    python scripts/refocus.py drafts/regions/left_angular_gyrus__Breining2022.md             # dry run: the plan and prompt size
    python scripts/refocus.py drafts/regions/left_angular_gyrus__Breining2022.md --execute   # call the model, merge the findings
    python scripts/refocus.py --citation Breining2022 --execute                              # every draft of the paper with pending marks
    python scripts/refocus.py --all --execute                                               # every paper with pending marks, one call each

review_app.py saves marks under a draft as `reviewer_marks` (page, verbatim
quote, the reviewer's note). This script gathers the pending ones for a
paper, gives the model the full paper text, the existing drafts' findings
(so it does not repeat them) and the marks, and asks for findings whose
source passages include each marked quote. The usual extractor rules apply
(docs/EXTRACTION_SKILL.md, docs/schema.md, the controlled vocabularies); the response
goes through the same repairs and validation as extract.py.

Merging: a returned finding whose entry already has a draft for this paper
is appended to that draft (next free id); otherwise the returned draft is
saved as a new file in drafts/<bucket>/. Every new finding carries
`provenance.flags: ["refocus: m<n>"]` so the reviewer sees where it came
from, and each mark is set to `status: done` with the finding ids it
produced (or `status: unresolved` with the model's reason). The annotated
PDF is regenerated and a REFOCUSED line goes to logs/extraction_log.md. Nothing
canonical is touched; the new findings are drafts to review and promote as
usual.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
import extract as X  # noqa: E402
from aphasia_kb import _FRONTMATTER_RE, parse_markdown  # noqa: E402
from review_app import BUCKETS, DRAFTS, PAPERS, _write_draft  # noqa: E402
from quote_check import find_paper  # noqa: E402

FOCUS_HEADER = """

# FOCUSED RE-EXTRACTION (read this before answering)

A reviewer has read this paper against the drafts already extracted from it
and marked passages that no existing finding covers. Your job is ONLY to
write findings for the marked passages below — do not re-extract the paper,
do not repeat findings that already exist (listed after the marks).

Rules for this run:
  * One finding per mark, unless one passage clearly supports two distinct
    claims or two marks support the same claim (then say so in
    notes_for_reviewer).
  * Each finding's `source_passages` MUST include the marked quote verbatim
    (you may add further verbatim passages from the paper for sample,
    method, statistics and the authors' limitations).
  * Put the mark id in `provenance.flags`, exactly as `refocus: <id>`.
  * Use an existing entry id when the finding belongs to an entry already
    drafted for this paper (listed below) — it will be appended there —
    or an existing KB entry; otherwise choose a sensible new id as usual.
  * If a mark cannot become a schema-valid finding (no claim, no stroke
    sample, not what the schema holds), do not invent one: explain in
    notes_for_reviewer as "<id>: <reason>".
  * Return the same JSON object as a normal extraction (drafts, summary,
    extraction_log_line, notes_for_reviewer).

## Marked passages

{marks}

## Findings already extracted from this paper (do not repeat)

{existing}
"""


def _rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def _parse_content(content: str) -> tuple[dict, str]:
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    return yaml.safe_load(m.group("yaml")) or {}, m.group("body")


def drafts_for(key: str) -> list[Path]:
    out = []
    for b in BUCKETS:
        out.extend(sorted((DRAFTS / b).glob(f"*__{key}.md")))
    return out


def pending_marks(paths: list[Path]) -> list[tuple[Path, dict]]:
    out = []
    for p in paths:
        fm, _ = parse_markdown(p)
        for m in fm.get("reviewer_marks") or []:
            if isinstance(m, dict) and m.get("status", "pending") == "pending" and str(m.get("quote") or "").strip():
                out.append((p, m))
    return out


def existing_summary(paths: list[Path]) -> str:
    lines = []
    for p in paths:
        fm, _ = parse_markdown(p)
        lines.append(f"- draft `{p.parent.name}/{p.name}` (entry id `{fm.get('id')}`, bucket {p.parent.name}):")
        for f in fm.get("findings") or []:
            if isinstance(f, dict):
                lines.append(f"    - {f.get('id')}: → {f.get('target')} ({f.get('target_kind')}), {f.get('relationship')}, "
                             f"{f.get('strength')}: {str(f.get('claim') or '').strip()[:220]}")
    return "\n".join(lines) or "(none)"


def marks_block(marks: list[tuple[Path, dict]]) -> str:
    lines = []
    for p, m in marks:
        lines.append(f"- id `{m.get('id')}` (page {m.get('page')}, marked in {p.name}):\n"
                     f"    quote: \"{str(m.get('quote')).strip()}\"\n"
                     f"    reviewer's note: {str(m.get('note') or '').strip() or '(none)'}")
    return "\n".join(lines)


def build_focus_prompt(pdf: Path, citation: str, drafts: list[Path], marks: list[tuple[Path, dict]], model: str) -> str:
    paper_text, n_pages = X._extract_pdf_text(pdf)
    skill = X._load_text(ROOT / "docs/EXTRACTION_SKILL.md")
    schema = X._load_text(ROOT / "docs/schema.md")
    kb_summary = X._existing_kb_summary(ROOT)
    citations = ("(omitted — use exactly the citation key given in the Paper section below for every "
                 "finding's `citation`.)")
    prompt = X.build_prompt(skill, schema, citations, kb_summary, paper_text, citation, pdf.name, n_pages,
                            created_by=f"agent:ollama-refocus-cli/{model}")
    return prompt + FOCUS_HEADER.replace("{marks}", marks_block(marks)).replace("{existing}", existing_summary(drafts))


def _next_id(existing: set[str]) -> str:
    n = 1
    while f"f{n}" in existing:
        n += 1
    return f"f{n}"


def merge(result: dict, citation: str, drafts: list[Path], marks: list[tuple[Path, dict]], model: str) -> dict:
    """Append returned findings to existing drafts or save new drafts. Returns
    {mark id: [finding refs]} and the list of files touched."""
    key = citation.lstrip("@")
    by_entry = {}
    for p in drafts:
        fm, _ = parse_markdown(p)
        by_entry[(p.parent.name, str(fm.get("id")))] = p
    produced: dict[str, list[str]] = {}
    touched: list[Path] = []
    created_by = f"agent:ollama-refocus-cli/{model}"
    for d in result.get("drafts") or []:
        bucket = d.get("bucket")
        if bucket not in BUCKETS:
            print(f"  ⚠ skipping draft with invalid bucket={bucket!r}")
            continue
        content, notes = X._repair_frontmatter(d.get("content") or "", created_by)
        content, more = X._normalize_findings(content, bucket, citation, ROOT)
        fm_new, body_new = _parse_content(content)
        findings = [f for f in fm_new.get("findings") or [] if isinstance(f, dict)]
        if not findings:
            continue
        for f in findings:
            flags = (f.setdefault("provenance", {})).setdefault("flags", [])
            for mid in re.findall(r"refocus:\s*(m\d+)", " ".join(str(x) for x in flags)):
                produced.setdefault(mid, [])
        target = by_entry.get((bucket, str(fm_new.get("id"))))
        if target is not None:
            fm, body = parse_markdown(target)
            ids = {str(f.get("id")) for f in fm.get("findings") or [] if isinstance(f, dict)}
            for f in findings:
                f["id"] = _next_id(ids)
                ids.add(f["id"])
                fm.setdefault("findings", []).append(f)
                for mid in re.findall(r"refocus:\s*(m\d+)", " ".join(str(x) for x in f["provenance"].get("flags") or [])):
                    produced.setdefault(mid, []).append(f"{target.name}:{f['id']}")
            _write_draft(target, fm, body)
            touched.append(target)
            print(f"  ✓ {len(findings)} finding(s) appended to {_rel(target)}{'   [' + '; '.join(notes + more) + ']' if notes + more else ''}")
        else:
            out = DRAFTS / bucket / (d.get("filename") or f"{fm_new.get('id')}__{key}.md")
            if out.exists():
                out = out.with_name(f"{out.stem}_refocus.md")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(content, encoding="utf-8")
            touched.append(out)
            for f in findings:
                for mid in re.findall(r"refocus:\s*(m\d+)", " ".join(str(x) for x in (f.get("provenance") or {}).get("flags") or [])):
                    produced.setdefault(mid, []).append(f"{out.name}:{f.get('id')}")
            print(f"  ✓ wrote new draft {_rel(out)}")
    # stamp the marks
    notes = str(result.get("notes_for_reviewer") or "")
    today = dt.date.today().isoformat()
    for p, m in marks:
        fm, body = parse_markdown(p)
        for mm in fm.get("reviewer_marks") or []:
            if isinstance(mm, dict) and mm.get("id") == m.get("id"):
                refs = produced.get(str(m.get("id")))
                if refs:
                    mm["status"] = "done"
                    mm["result"] = refs
                else:
                    mm["status"] = "unresolved"
                    why = re.search(rf"{re.escape(str(m.get('id')))}\s*[:\-—]\s*([^\n;]+)", notes)
                    mm["result"] = why.group(1).strip() if why else "the model returned no finding for this mark"
                mm["refocused_on"] = today
                mm["model"] = model
        _write_draft(p, fm, body)
        if p not in touched:
            touched.append(p)
    touched = list(dict.fromkeys(touched))
    return {"produced": produced, "touched": touched}


def run(paths: list[Path], execute: bool, model: str | None, timeout: int) -> int:
    if not paths:
        print("no draft given")
        return 1
    fm0, _ = parse_markdown(paths[0])
    citation = next((str(f.get("citation")) for f in fm0.get("findings") or [] if isinstance(f, dict) and f.get("citation")), "")
    if not citation:
        print(f"{paths[0].name}: no citation in its findings")
        return 1
    key = citation.lstrip("@")
    drafts = drafts_for(key)
    marks = pending_marks(paths)
    if not marks:
        print(f"{citation}: no pending reviewer marks in {', '.join(p.name for p in paths)}")
        return 0
    pdf = find_paper(citation, PAPERS)
    if pdf is None or pdf.suffix.lower() != ".pdf":
        print(f"{citation}: no PDF in papers/")
        return 1
    spec = X.resolve_model("extract", model)
    model = spec["model"]
    prompt = build_focus_prompt(pdf, citation, drafts, marks, model)
    print(f"{citation}: {len(marks)} pending mark(s) across {len(paths)} draft(s); {len(drafts)} draft(s) of the paper exist")
    for p, m in marks:
        print(f"  {m.get('id')}  p.{m.get('page')}  {str(m.get('quote'))[:90]}…  — {str(m.get('note') or '')[:60]}")
    print(f"  Prompt: {len(prompt):,} chars (~{len(prompt) // 4:,} tokens) · model {model}")
    if not execute:
        out = ROOT / "_refocus_dry_run.txt"
        out.write_text(prompt, encoding="utf-8")
        print(f"  DRY RUN — prompt written to {out.name}. Add --execute to call the model.")
        return 0
    t0 = time.monotonic()
    raw = X.call_ollama(prompt, model, max_tokens=spec["max_tokens"], num_ctx=spec["num_ctx"], monitor=False, timeout=timeout)
    (ROOT / f"_last_refocus_response_{key}.txt").write_text(raw, encoding="utf-8")
    try:
        result = X.parse_response(raw)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ couldn't parse the model's JSON: {e} (raw response kept in _last_refocus_response_{key}.txt)")
        return 1
    merged = merge(result, citation, drafts, marks, model)
    n_new = sum(len(v) for v in merged["produced"].values())
    n_issues = X.validate_drafts([p for p in merged["touched"] if p.exists()])
    try:
        X.run_annotator(pdf, drafts_for(key), ROOT)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠ annotator: {e}")
    line = (f"{dt.date.today().isoformat()} | REFOCUSED | {citation} | "
            f"{', '.join(p.stem for p in merged['touched'])} | {len(marks)} mark(s) → {n_new} finding(s)"
            f"{' | ' + str(n_issues) + ' validation issue(s)' if n_issues else ''} | model: {model}")
    X.append_extraction_log(ROOT / "logs/extraction_log.md", line)
    notes = result.get("notes_for_reviewer")
    print(f"  {n_new} finding(s) from {len(marks)} mark(s) in {time.monotonic() - t0:.0f}s; "
          f"{', '.join(f'{k}: {len(v)}' for k, v in merged['produced'].items()) or 'nothing produced'}")
    if notes:
        print(f"  For reviewer: {notes}")
    print("  Review them: python scripts/review_app.py --citation " + key)
    return 0


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("drafts", nargs="*", type=Path, help="draft file(s) with pending reviewer_marks")
    ap.add_argument("--citation", help="every draft of this paper (@Key or Key)")
    ap.add_argument("--all", action="store_true", help="every paper that has drafts with pending marks (one model call per paper)")
    ap.add_argument("--model", help="override models.yaml role `extract`")
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--execute", action="store_true", help="call the model (default: dry run)")
    args = ap.parse_args(argv)
    if args.all:
        by_key: dict[str, list[Path]] = {}
        for b in BUCKETS:
            for p in sorted((DRAFTS / b).glob("*__*.md")):
                if pending_marks([p]):
                    by_key.setdefault(p.stem.split("__", 1)[1], []).append(p)
        if not by_key:
            print("no draft has pending reviewer marks")
            return 0
        print(f"{len(by_key)} paper(s) with pending marks: {', '.join(sorted(by_key))}")
        rc = 0
        for key in sorted(by_key):
            rc |= run(by_key[key], args.execute, args.model, args.timeout)
        return rc
    paths = list(args.drafts)
    if args.citation:
        paths += [p for p in drafts_for(args.citation.lstrip("@")) if p not in paths]
    return run(paths, args.execute, args.model, args.timeout)


if __name__ == "__main__":
    sys.exit(_cli())
