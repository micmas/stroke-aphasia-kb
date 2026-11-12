#!/usr/bin/env python3
"""
retarget_symptoms.py — move findings that target an aphasia *syndrome* but
speak of a *symptom* onto the symptom entry (schema v2.8), and unify the
scattered naming ids.

    python scripts/retarget_symptoms.py                 # dry run: what would change, and what stays
    python scripts/retarget_symptoms.py --execute       # drafts and canonical entries
    python scripts/retarget_symptoms.py --execute --drafts-only

The rule (docs/schema.md, impairments): an aphasia-type id such as
`anomic_aphasia` is a target only when the paper classified patients by
syndrome and the claim is about the type. A naming score predicted by a
lesion or improved by a therapy is about `anomia`, whichever type the
patients had.

What it does, per finding:
  * target `naming`, `confrontation_naming`, `naming_accuracy`, `word_finding`
    → `anomia` (always; these were never entries);
  * target `anomic_aphasia` whose claim, notes and claim quote never mention
    the syndrome (`aphasia_kb._syndrome_claim`) → `anomia`;
  * target `anomic_aphasia` with a syndrome claim → kept, listed for a person
    to confirm;
  * other `*_aphasia` targets with symptom claims → listed only (which symptom
    entry is the right one is a judgement; fix in the review workbench);
  * therapy entries whose `targets_impairments` list `anomic_aphasia`,
    `naming` or `lexical_retrieval` gain `anomia` (naming therapies treat
    the symptom; the syndrome id is kept), so the therapy matcher keeps
    finding them for a predicted naming deficit.

Every retargeted finding keeps its old target in `provenance.flags`
("retargeted anomic_aphasia → anomia (symptom, v2.8) on <date>") and gets an
`edits` record; one RETARGETED line per file goes to logs/extraction_log.md.
Canonical entries are edited too (the target is a modelling correction, the
claim and quotes are untouched), which `GOVERNANCE.md` allows for a logged,
reviewable change; re-run `export_webapp.py` afterwards.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
from aphasia_kb import _syndrome_claim, parse_markdown  # noqa: E402

BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews")
NAMING_IDS = {"naming", "confrontation_naming", "naming_accuracy", "word_finding", "word_retrieval", "naming_impairment"}
SYMPTOM_FOR = {"anomic_aphasia": "anomia"}
LOG = ROOT / "logs/extraction_log.md"


def _write(path: Path, fm: dict, body: str) -> None:
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    path.write_text(f"---\n{text}---\n{body}", encoding="utf-8")


def files(drafts_only: bool) -> list[tuple[Path, bool]]:
    out = []
    for b in BUCKETS:
        for p in sorted((ROOT / "drafts" / b).glob("*.md")):
            out.append((p, False))
        if not drafts_only:
            for p in sorted((ROOT / b).glob("*.md")):
                out.append((p, True))
    return out


def plan(drafts_only: bool) -> list[dict]:
    rows = []
    for path, canonical in files(drafts_only):
        try:
            fm, _ = parse_markdown(path)
        except Exception as e:  # noqa: BLE001
            rows.append({"path": path, "fid": "?", "action": "error", "why": str(e).splitlines()[0]})
            continue
        for f in fm.get("findings") or []:
            if not isinstance(f, dict):
                continue
            t = str(f.get("target") or "")
            if f.get("target_kind") not in ("impairment", None):
                continue
            if t in NAMING_IDS:
                rows.append({"path": path, "canonical": canonical, "fid": f.get("id"), "old": t, "new": "anomia",
                             "action": "retarget", "why": "naming id that was never an entry"})
            elif t in SYMPTOM_FOR:
                if _syndrome_claim(f):
                    rows.append({"path": path, "canonical": canonical, "fid": f.get("id"), "old": t, "new": t,
                                 "action": "keep", "why": "claim speaks of the syndrome — confirm"})
                else:
                    rows.append({"path": path, "canonical": canonical, "fid": f.get("id"), "old": t, "new": SYMPTOM_FOR[t],
                                 "action": "retarget", "why": "claim is about naming performance"})
            elif t.endswith("_aphasia") and not _syndrome_claim(f):
                rows.append({"path": path, "canonical": canonical, "fid": f.get("id"), "old": t, "new": "?",
                             "action": "review", "why": "symptom claim on a syndrome target — pick the symptom entry in the workbench"})
    return rows


THERAPY_TARGET_ALIASES = {"anomic_aphasia", "naming", "confrontation_naming", "lexical_retrieval", "word_retrieval"}


def therapy_targets_plan(drafts_only: bool) -> list[dict]:
    rows = []
    folders = [ROOT / "drafts" / "therapies"] + ([] if drafts_only else [ROOT / "therapies"])
    for folder in folders:
        for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
            try:
                fm, _ = parse_markdown(path)
            except Exception:  # noqa: BLE001
                continue
            targets = [str(t) for t in fm.get("targets_impairments") or []]
            if targets and "anomia" not in targets and THERAPY_TARGET_ALIASES & set(targets):
                rows.append({"path": path, "targets": targets})
    return rows


def execute_therapy_targets(rows: list[dict]) -> int:
    today = dt.date.today().isoformat()
    for r in rows:
        fm, body = parse_markdown(r["path"])
        fm["targets_impairments"] = list(fm.get("targets_impairments") or []) + ["anomia"]
        fm.setdefault("notes", "")
        fm["notes"] = (str(fm["notes"]).rstrip() + f"\n{today}: targets_impairments gained `anomia` (symptom, schema v2.8; retarget_symptoms.py).").strip()
        _write(r["path"], fm, body)
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(f"{today} | RETARGETED | — | {fm.get('id')} | targets_impairments += anomia | symptom not syndrome (schema v2.8); "
                     f"{'draft' if r['path'].parent.parent.name == 'drafts' else 'canonical'} | tool: retarget_symptoms.py\n")
    return len(rows)


def execute(rows: list[dict]) -> int:
    today = dt.date.today().isoformat()
    by_path: dict[Path, list[dict]] = {}
    for r in rows:
        if r["action"] == "retarget":
            by_path.setdefault(r["path"], []).append(r)
    n = 0
    for path, items in by_path.items():
        fm, body = parse_markdown(path)
        changed = []
        for f in fm.get("findings") or []:
            for r in items:
                if isinstance(f, dict) and f.get("id") == r["fid"] and f.get("target") == r["old"]:
                    f["target"] = r["new"]
                    f["target_kind"] = "impairment"
                    prov = f.setdefault("provenance", {})
                    prov.setdefault("flags", []).append(f"retargeted {r['old']} → {r['new']} (symptom, v2.8) on {today}")
                    f.setdefault("edits", []).append({"by": "tool:retarget_symptoms.py", "date": today, "fields": ["target"]})
                    changed.append(f"{r['fid']} {r['old']}→{r['new']}")
                    n += 1
        if changed:
            _write(path, fm, body)
            cite = next((str(x.get("citation")) for x in fm.get("findings") or [] if isinstance(x, dict) and x.get("citation")), "?")
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(f"{today} | RETARGETED | {cite} | {fm.get('id')} | {'; '.join(changed)} | symptom not syndrome (schema v2.8); "
                         f"{'draft' if path.parent.parent.name == 'drafts' else 'canonical'} | tool: retarget_symptoms.py\n")
    return n


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--drafts-only", action="store_true")
    args = ap.parse_args(argv)
    rows = plan(args.drafts_only)
    for action in ("retarget", "keep", "review", "error"):
        sel = [r for r in rows if r["action"] == action]
        if not sel:
            continue
        print(f"\n{action.upper()} ({len(sel)})")
        for r in sel:
            rel = r["path"].relative_to(ROOT)
            print(f"  {str(rel):<70} {str(r.get('fid')):<4} {r.get('old', ''):<22} → {r.get('new', ''):<10} {r.get('why', '')}")
    tt = therapy_targets_plan(args.drafts_only)
    if tt:
        print(f"\nTHERAPY TARGETS += anomia ({len(tt)})")
        for r in tt:
            print(f"  {str(r['path'].relative_to(ROOT)):<70} {', '.join(r['targets'])}")
    n_re = sum(1 for r in rows if r["action"] == "retarget")
    if not args.execute:
        print(f"\nDry run: {n_re} finding(s) would be retargeted, {len(tt)} therapy entries would gain `anomia`. Add --execute.")
        return 0
    n = execute(rows)
    m = execute_therapy_targets(tt)
    print(f"\n{n} finding(s) retargeted, {m} therapy entries gained `anomia`. Re-run export_webapp.py; review the KEEP and REVIEW rows in the workbench.")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
