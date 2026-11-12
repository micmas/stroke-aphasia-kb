"""Two independent local source inventories plus a source-grounded review packet.

The reviewer is a separate step: this command never claims model agreement is
approval, never merges results by majority vote, and never writes KB findings.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from extract_analysis_inventory import run
from strict_data import load_json
from source_limits import source_hold

REVIEW_INSTRUCTIONS = '''Review BOTH independent extractions against the original paper.
Do not prefer either model or treat agreement as evidence. Work from the union of
reported findings, then search the source for findings both omitted. Independently
check every outcome, predictor, adjustment, coefficient, sign, uncertainty and
quote/page. Preserve source discrepancies. Distinguish retained predictors from
significant coefficients. Do not turn group associations into individual diagnostic
rules or cross-sectional scores into future recovery. Inspect tables and figures
visually. Scope is the main paper only, including its tables and figures.
Do not retrieve or use supplements. Mark supplement-dependent details as outside
source scope rather than filling them from assumptions.

Create inventory.json (same source-first schema), decisions.md (retained,
corrected, rejected and reviewer-added results with source locators),
final-extraction.md (complete readable extraction including anatomy, imaging,
spatial reference, timing, outcomes, models, nulls and limitations), and
coverage.json (every substantive main-paper outcome/model/table/figure,
its covered record ids or explicit unresolved reason). Preserve original source
IDs. Record supplementary files as excluded by scope, never as extracted evidence.
Never invent KB target mappings. Do not silently discard an unmatched finding.
Final means reconciled extraction, not clinical validation or automatic KB approval.
'''


def prepare_review(first: Path, second: Path, output: Path) -> Path:
    arms = []
    for label,directory in [('A',first),('B',second)]:
        meta = load_json((directory/'meta.json').read_text())
        raw_path = directory/'raw.json'
        source_path = directory/'source-units.json'
        arms.append({'label':label,'directory':str(directory.resolve()),
                     'meta':meta,'raw_sha256':hashlib.sha256(raw_path.read_bytes()).hexdigest(),
                     'source_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
                     'extraction':load_json(raw_path.read_text())})
    for key in ['pdf_sha256','citation','prompt_sha256']:
        if not arms[0]['meta'].get(key) or arms[0]['meta'][key] != arms[1]['meta'].get(key):
            raise ValueError(f'Independent runs differ in {key}; reconcile inputs before comparing')
    if arms[0]['source_sha256'] != arms[1]['source_sha256']:
        raise ValueError('Source units differ')
    output.mkdir(parents=True,exist_ok=False)
    packet={'status':'awaiting_independent_review','approved':False,'arms':arms,
            'source_units':load_json((first/'source-units.json').read_text()),
            'review_instructions':REVIEW_INSTRUCTIONS}
    (output/'packet.json').write_text(json.dumps(packet,indent=2,ensure_ascii=False))
    (output/'review-instructions.txt').write_text(REVIEW_INSTRUCTIONS)
    return output/'packet.json'


def run_pair(pdf, citation, output, models, max_tokens=10000, segment_chars=None, allow_long_paper=False):
    if max_tokens <= 0:
        raise ValueError('max_tokens must be positive')
    output.mkdir(parents=True,exist_ok=False)
    hold = source_hold(pdf, allow_long_paper)
    if hold:
        (output/'status.json').write_text(json.dumps({'approved': False, **hold}, indent=2))
        print(hold['reason'], flush=True)
        return 1
    errors = []
    for label,model in zip(['A','B'],models):
        # Only original PDF and citation enter each run. No prior model output.
        try:
            if segment_chars is None:
                run(pdf,citation,output/label,model,max_tokens=max_tokens)
            else:
                from source_inventory_segments import run_segmented
                run_segmented(pdf,citation,output/label,model,max_tokens=max_tokens,segment_chars=segment_chars)
        except Exception as exc:
            errors.append({'arm':label,'error':str(exc)})
    if not errors:
        try: prepare_review(output/'A',output/'B',output/'review')
        except Exception as exc: errors.append({'review_packet':str(exc)})
    (output/'status.json').write_text(json.dumps({'approved':False,
        'status':'failed' if errors else 'awaiting_independent_review','errors':errors},indent=2))
    return 1 if errors else 0


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdf',type=Path,required=True)
    p.add_argument('--citation',required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--models',nargs=2,default=['gemma4:31b','qwen3.8:27b'])
    p.add_argument('--max-output-tokens',type=int,default=10000)
    p.add_argument('--allow-long-papers', action='store_true', help='Explicitly allow the complete source over 50 pages')
    a=p.parse_args()
    raise SystemExit(run_pair(a.pdf,a.citation,a.output_dir,a.models,a.max_output_tokens,allow_long_paper=a.allow_long_papers))
