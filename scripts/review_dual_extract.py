"""Local source-first reconciliation of completed dual extractions. Never approves KB entries.

Preview is the default. Text-only review always leaves visual verification pending.
The extraction batch must be stopped before --run (shared batch lock).
"""
from __future__ import annotations
from paper_paths import resolve_paper
import argparse
import fcntl
import hashlib
import json
from pathlib import Path
import time
import urllib.request
from extract_analysis_inventory import audit_inventory, build_prompt, source_units
from extract import _extract_pdf_text
from ollama_client import chat, autosize_num_ctx, normalize_host, is_local, DEFAULT_HOST, RepetitionLoop
from strict_data import load_json
from review_format import response_schema, quote_diagnostics, QUOTE_RULES
from review_stages import review_in_stages, ReviewGate

VERSION = 'local-source-review-v3'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


def read(path):
    return load_json(path.read_text())


def identities(host):
    host = normalize_host(host)
    if not is_local(host):
        raise ValueError('Review requires a loopback Ollama host')
    with urllib.request.urlopen(host+'/api/tags', timeout=15) as response:
        return {m['name']: m['digest'] for m in json.load(response)['models']}


def model_identity(model, tags):
    value = tags.get(model) or tags.get(model+':latest')
    if not value:
        raise ValueError(f'Model not installed: {model}. No models are downloaded automatically.')
    return value


def completed(run_dir):
    config = read(run_dir/'batch-config.json')
    ready, skipped = [], []
    for row in config['manifest']['papers']:
        folder = run_dir/row['key']
        status = read(folder/'status.json') if (folder/'status.json').exists() else {}
        if status.get('status') == 'awaiting_independent_review':
            ready.append(row)
        else:
            skipped.append({'key': row['key'], 'status': status.get('status', 'incomplete_or_not_started')})
    return ready, skipped


def load_paper(run_dir, row):
    folder = run_dir/row['key']
    if read(folder/'status.json').get('status') != 'awaiting_independent_review':
        raise ValueError('Only completed paper pairs may be reviewed')
    pdf = Path(row['pdf'])
    pdf = resolve_paper(pdf.parent, pdf.name)
    if digest(pdf) != row['pdf_sha256']:
        raise ValueError('PDF differs from frozen extraction source')
    arms, hashes = {}, {'pdf': digest(pdf)}
    units = None
    prompt_hash = None
    for label in ['A', 'B']:
        d = folder/label
        meta, raw, source = read(d/'meta.json'), read(d/'raw.json'), read(d/'source-units.json')
        if meta.get('profile') == 'relationships' or raw.get('schema_version') == 'relationships-v1':
            raise ValueError('Relationship pilot requires manual source review; incompatible automated review schema')
        if meta.get('status') != 'requires_review' or meta.get('citation') != row['citation'] or meta.get('pdf_sha256') != row['pdf_sha256']:
            raise ValueError(f'{label}: incomplete or mismatched extraction')
        if meta.get('source_scope') != 'main_paper_only':
            raise ValueError('Main-paper scope required')
        if meta.get('inference', {}).get('truncated_input') or meta.get('inference', {}).get('truncated_output'):
            raise ValueError('Truncated extraction cannot enter review')
        if units is not None and source != units:
            raise ValueError('Source units differ between arms')
        if prompt_hash is not None and meta.get('prompt_sha256') != prompt_hash:
            raise ValueError('Extraction prompts differ')
        if digest(d/'prompt.txt') != meta.get('prompt_sha256'):
            raise ValueError('Extraction prompt checksum mismatch')
        units, prompt_hash = source, meta['prompt_sha256']
        ids = [a.get('id') for a in raw.get('analyses', [])]
        if not ids or any(not isinstance(x, str) or not x for x in ids) or len(ids) != len(set(ids)):
            raise ValueError('Unique extraction analysis IDs required for decision tracking')
        arms[label] = {'model': meta['model'], 'extraction': raw,
                       'audit_issues': audit_inventory(raw, source, row['citation'])}
        for name in ['meta.json', 'raw.json', 'source-units.json', 'prompt.txt']:
            hashes[label+'/'+name] = digest(d/name)
    # Ensure reviewer evidence is the actual frozen PDF, not merely matching copies.
    text, _ = _extract_pdf_text(pdf)
    if source_units(text) != units:
        raise ValueError('Source units no longer reproduce from the PDF; investigate before review')
    return arms, units, hashes


def validate(result, units, citation, arms):
    if not isinstance(result, dict) or not isinstance(result.get('inventory'), dict):
        return ['Reconciled inventory missing']
    inventory = result['inventory']
    issues = audit_inventory(inventory, units, citation)
    final_ids = {a.get('id') for a in inventory.get('analyses', []) if isinstance(a, dict)}
    expected = {(label, a['id']) for label in arms for a in arms[label]['extraction']['analyses']}
    decisions = result.get('decisions')
    seen = set()
    if not isinstance(decisions, list):
        issues.append('Decision list missing'); decisions = []
    for d in decisions:
        if not isinstance(d, dict):
            issues.append('Invalid decision'); continue
        key = (d.get('arm'), d.get('analysis_id'))
        if key not in expected or key in seen:
            issues.append('Unknown or duplicate original analysis decision')
        seen.add(key)
        ids = d.get('final_ids')
        if not isinstance(ids, list) or any(not isinstance(i, str) or i not in final_ids for i in ids):
            issues.append('Invalid decision final_ids')
        if d.get('action') not in ['retain', 'correct', 'reject'] or not d.get('reason'):
            issues.append('Invalid decision action/reason')
        if d.get('action') in ['retain', 'correct'] and not ids:
            issues.append('Retained/corrected decision has no final record')
        # Reuse exact source checking for decision evidence, including rejections.
        evidence_probe = dict(inventory, analyses=inventory.get('analyses', []),
                              discrepancies=[{'evidence': d.get('evidence')}])
        issues += [x for x in audit_inventory(evidence_probe, units, citation) if x.startswith('discrepancy')]
    if seen != expected:
        issues.append('Not every original analysis has a decision')
    coverage = result.get('coverage')
    covered = set()
    mapped_final = set()
    if not isinstance(coverage, list):
        issues.append('Coverage list missing'); coverage = []
    for c in coverage:
        if not isinstance(c, dict):
            issues.append('Invalid coverage item'); continue
        sid = c.get('source_id')
        if not isinstance(sid, str) or sid not in units or sid in covered:
            issues.append('Unknown/duplicate coverage source_id')
        if isinstance(sid, str): covered.add(sid)
        ids = c.get('final_ids')
        if not isinstance(ids, list) or any(not isinstance(i, str) or i not in final_ids for i in ids):
            issues.append('Invalid coverage final_ids')
        if isinstance(ids, list):
            mapped_final.update(i for i in ids if isinstance(i, str))
        if c.get('status') == 'covered' and not ids:
            issues.append('Covered unit has no final record link')
        if c.get('status') not in ['covered', 'not_substantive', 'unresolved'] or not c.get('reason'):
            issues.append('Invalid coverage status/reason')
    if covered != set(units): issues.append('Source-unit coverage incomplete')
    if not final_ids.issubset(mapped_final): issues.append('Final records missing from coverage')
    for name in ['summary', 'study_context']:
        if not isinstance(result.get(name), str) or not result[name].strip(): issues.append(name+' missing')
    if not isinstance(result.get('unresolved'), list): issues.append('Unresolved list missing')
    return issues


def call_stage(prompt, directory, model, host, budget, schema):
    directory.mkdir()
    print(f'  Review stage: {directory.name} (up to {budget:,} output tokens)', flush=True)
    (directory/'prompt.txt').write_text(prompt)
    write(directory/'response-schema.json', schema)
    meta = {'model': model, 'prompt_sha256': digest(directory/'prompt.txt'), 'approved': False,
            'temperature': 0.0, 'think': False, 'max_output_tokens': budget, 'status': 'failed'}
    meta['response_schema_sha256'] = digest(directory/'response-schema.json')
    try:
        response = chat(prompt, model=model, host=host, max_tokens=budget,
                        num_ctx=autosize_num_ctx(prompt, budget), temperature=0.0,
                        think=False, fmt=schema, timeout=3600)
        (directory/'raw.json').write_text(response['text'])
        meta['inference'] = {k:v for k,v in response.items() if k != 'text'}
        if response.get('truncated_input') or response.get('truncated_output'):
            raise ValueError('Truncated review; preserve and retry explicitly after fixing budget/source')
        result = load_json(response['text'])
        if not isinstance(result, dict): raise ValueError('Expected review object')
        meta['status'] = 'generated'
        return result
    except RepetitionLoop as exc:
        (directory/'raw.json').write_text(exc.partial); meta['error'] = str(exc); raise
    except Exception as exc:
        meta['error'] = str(exc); raise
    finally:
        write(directory/'meta.json', meta)


def review_one(run_dir, row, output, model, host, budget, tags):
    if read(run_dir/'batch-config.json').get('profile') == 'relationships':
        from relationship_review import review_one as review_relationships
        return review_relationships(run_dir, row, output, model, host, budget, tags)
    arms, units, hashes = load_paper(run_dir, row)
    reviewer_digest = model_identity(model, tags)
    for arm in arms.values():
        if model == arm['model'] or reviewer_digest == model_identity(arm['model'], tags):
            raise ValueError('Reviewer must differ from both extraction models (including current digest aliases)')
    binding = {'version': VERSION, 'model': model, 'model_digest': reviewer_digest,
               'input_hashes': hashes, 'max_output_tokens': budget, 'host': normalize_host(host),
               'code_hashes': {p.name: digest(p) for p in [Path(__file__), Path(__file__).with_name('extract_analysis_inventory.py'),
                    Path(__file__).with_name('ollama_client.py'), Path(__file__).with_name('quote_check.py'),
                    Path(__file__).with_name('strict_data.py'), Path(__file__).with_name('review_format.py'),
                    Path(__file__).with_name('review_stages.py'), Path(__file__).with_name('extract.py')]}}
    if output.exists():
        meta = read(output/'status.json') if (output/'status.json').exists() else {}
        if meta.get('binding') == binding and meta.get('status') in ['requires_revision', 'requires_visual_review']:
            for name, sha in meta.get('output_hashes', {}).items():
                if digest(output/name) != sha: raise ValueError('Saved review changed; use a new output directory')
            if not meta.get('output_hashes'): raise ValueError('Review output hashes missing')
            print(f"Reuse review {row['key']}: {meta['status']}", flush=True)
            return meta['status']
        raise ValueError('Existing review incomplete or inputs/settings changed; preserve it and use a new output directory')
    output.mkdir(parents=True)
    state = {'status': 'running', 'approved': False, 'binding': binding,
             'limitation': 'Extraction-time model digests were not recorded by the original runner; identity checks use extraction tags and currently installed digests.'}
    write(output/'status.json', state)
    started = time.monotonic()
    try:
        # Blind inventory receives original source only, never either extractor's answer.
        blind = call_stage(build_prompt(units, row['citation']) + QUOTE_RULES, output/'source-first', model, host, budget,
                           response_schema(units, row['citation']))
        blind_issues = audit_inventory(blind, units, row['citation'])
        write(output/'source-first/audit.json', blind_issues)
        write(output/'source-first/quote-diagnostics.json', quote_diagnostics(blind, units))
        final = review_in_stages(units, row['citation'], arms, blind,
                                 lambda name, prompt, schema, tokens: call_stage(prompt, output/name, model, host, tokens, schema),
                                 lambda name, value: write(output/name, value), budget)
        issues = validate(final, units, row['citation'], arms)
        if any(c.get('status') == 'unresolved' for c in final['coverage']):
            issues.append('Source coverage has unresolved substantive content')
        write(output/'audit.json', {'blind_inventory_issues': blind_issues, 'reconciliation_issues': issues})
        # Inputs must remain unchanged over every review stage.
        if load_paper(run_dir, row)[2] != hashes:
            raise ValueError('Extraction inputs changed during review')
        if model_identity(model, identities(host)) != reviewer_digest:
            raise ValueError('Reviewer model digest changed during review')
        provisional = dict(final.get('inventory') or {})
        provisional['approved'] = False
        write(output/'inventory.json', provisional)
        write(output/'decisions.json', final.get('decisions'))
        write(output/'coverage.json', final.get('coverage'))
        write(output/'visual-review-required.json', {'status': 'not_performed', 'approved': False,
             'pages': sorted({u['page'] for u in units.values()}),
             'reason': 'Text-only review cannot verify image-only values, table geometry, figures or OCR fidelity. All main-PDF pages remain eligible for visual checking; absence of model flags does not waive it.'})
        (output/'provisional-extraction.txt').write_text('PROVISIONAL LOCAL TEXT REVIEW — NOT APPROVED\n\n'+str(final.get('study_context',''))+'\n\n'+str(final.get('summary',''))+'\n\nUNRESOLVED\n'+json.dumps(final.get('unresolved'),ensure_ascii=False,indent=2)+'\n')
        state['status'] = 'requires_revision' if issues else 'requires_visual_review'
        state['output_hashes'] = {str(p.relative_to(output)): digest(p) for p in output.rglob('*') if p.is_file() and p.name != 'status.json'}
        return state['status']
    except ReviewGate as exc:
        state['status'] = 'requires_revision'
        state['error'] = str(exc)
        state['output_hashes'] = {str(p.relative_to(output)): digest(p) for p in output.rglob('*') if p.is_file() and p.name != 'status.json'}
        print(f"Review stopped at validation gate: {exc}", flush=True)
        return state['status']
    except BaseException as exc:
        state['status'] = 'interrupted' if isinstance(exc, KeyboardInterrupt) else 'failed'
        state['error'] = str(exc) or type(exc).__name__; raise
    finally:
        state['seconds'] = time.monotonic()-started
        write(output/'status.json', state)


def batch(run_dir, output, model, execute=False, budget=20000, limit=None, host=DEFAULT_HOST):
    run_dir, output = run_dir.resolve(), output.resolve()
    if output == run_dir or run_dir in output.parents or output in run_dir.parents:
        raise ValueError('Review output must be separate from the extraction run directory')
    if budget <= 0 or (limit is not None and limit <= 0): raise ValueError('Budget/limit must be positive')
    ready, skipped = completed(run_dir)
    if limit: ready = ready[:limit]
    print(f"{'RUN' if execute else 'PREVIEW'}: {len(ready)} completed pairs; {len(skipped)} incomplete/failed/not started; reviewer {model}", flush=True)
    if not execute:
        for row in ready: print(row['key'])
        return 0
    # Same lock as the extraction batch: never compete with its models or resume.
    with (run_dir.parent/(run_dir.name+'.lock')).open('a') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: raise ValueError('Extraction/review is running. Stop extraction with Ctrl-C before local review.') from None
        tags = identities(host); model_identity(model, tags)
        outcomes = []
        for row in ready:
            print('Review '+row['key'], flush=True)
            try:
                status = review_one(run_dir, row, output/row['key'], model, host, budget, tags)
                outcomes.append({'paper': row['key'], 'status': status})
            except Exception as exc:
                print(f"Failed review {row['key']}: {exc}", flush=True)
                outcomes.append({'paper': row['key'], 'status': 'failed', 'error': str(exc)})
        output.mkdir(parents=True, exist_ok=True)
        write(output/'batch-status.json', {'approved': False, 'papers': outcomes, 'skipped': skipped,
              'note': 'No visual verification, KB replacement or approval performed.'})
        failed = sum(r['status'] == 'failed' for r in outcomes)
        revision = sum(r['status'] == 'requires_revision' for r in outcomes)
        print(f'Review pass ended: {len(outcomes)-failed} saved review aids; {revision} have unresolved source checks; {failed} failed. Nothing approved or published.', flush=True)
        print(f'Open each saved review.html and audit.json in {output}. Completeness is checked against original Results, tables and figures, not proposal counts.', flush=True)
        return int(any(r['status'] not in {'requires_visual_review', 'requires_source_review'} for r in outcomes))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-dir', type=Path, required=True)
    p.add_argument('--output-dir', type=Path, required=True)
    p.add_argument('--model', required=True, help='Installed reviewer distinct from both extractors; no automatic download')
    p.add_argument('--max-output-tokens', type=int, default=20000)
    p.add_argument('--limit', type=int)
    p.add_argument('--run', action='store_true')
    a = p.parse_args()
    raise SystemExit(batch(a.run_dir, a.output_dir, a.model, a.run, a.max_output_tokens, a.limit))
