"""Run a frozen, explicitly selected main-paper cohort without changing KB drafts."""
from paper_paths import resolve_paper
import argparse
import fcntl
import hashlib
import json
import re
from pathlib import Path
from dual_extract import run_pair


def load_manifest(path):
    data = json.loads(path.read_text())
    if data.get('source_scope') != 'main_paper_only':
        raise ValueError('Manifest must declare main_paper_only')
    rows = data.get('papers')
    if not isinstance(rows, list) or not rows:
        raise ValueError('Nonempty papers list required')
    seen = set()
    for row in rows:
        key = row.get('key', '')
        if not re.fullmatch(r'[A-Za-z0-9_-]+', key) or key in seen:
            raise ValueError('Unsafe or duplicate paper key')
        seen.add(key)
        if row.get('citation') != '@' + key or not row.get('licence_evidence'):
            raise ValueError(f'{key}: citation and licence metadata required (unknown must be explicit)')
        pdf = Path(row['pdf'])
        if not pdf.is_absolute():
            pdf = path.parent / pdf
        pdf = resolve_paper(pdf.parent, pdf.name)
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != row.get('pdf_sha256'):
            raise ValueError(f'{key}: PDF checksum mismatch')
        row['pdf'] = str(pdf.resolve())
    return data


def _batch(manifest, output, models, budget=20000, execute=False, retry_failed=False, continue_on_error=False):
    if budget <= 0 or len(models) != 2:
        raise ValueError('Positive output budget and two models required')
    data = load_manifest(manifest)
    # Include script/prompt code in the frozen identity so resume cannot mix versions.
    scripts = Path(__file__).parent
    code = {name: hashlib.sha256((scripts/name).read_bytes()).hexdigest()
            for name in ['batch_dual_extract.py', 'dual_extract.py', 'extract_analysis_inventory.py',
                         'extract.py', 'ollama_client.py', 'quote_check.py', 'strict_data.py', 'source_inventory_segments.py', 'source_limits.py']}
    config = {'manifest': data, 'models': models, 'max_output_tokens': budget, 'code': code}
    frozen = output / 'batch-config.json'
    if output.exists():
        if not frozen.exists() or json.loads(frozen.read_text()) != config:
            raise ValueError('Existing batch differs or is incomplete; use a new output directory')
    print(f"{'RUN' if execute else 'PREVIEW'}: {len(data['papers'])} papers, two independent extractions each", flush=True)
    if not execute:
        for row in data['papers']:
            print(row['key'])
        return 0
    output.mkdir(parents=True, exist_ok=True)
    if not frozen.exists():
        frozen.write_text(json.dumps(config, indent=2) + '\n')
    failures = []
    for row in data['papers']:
        dest = output / row['key']
        if dest.exists():
            status = dest / 'status.json'
            if status.exists() and json.loads(status.read_text()).get('status') == 'awaiting_independent_review':
                print(f"Reuse {row['key']}: awaiting source review", flush=True)
                continue
            if not retry_failed and continue_on_error:
                failures.append(row['key'])
                print(f"Skip {row['key']}: failed attempt preserved; --retry-failed required", flush=True)
                continue
            if not retry_failed:
                raise ValueError(f"{row['key']}: incomplete/failed output preserved; inspect, then use --retry-failed")
            archive = output / '_failed' / row['key']
            archive.mkdir(parents=True, exist_ok=True)
            attempt = 1
            while (archive / str(attempt)).exists():
                attempt += 1
            dest.rename(archive / str(attempt))
            print(f"Preserved failed attempt at {archive / str(attempt)}", flush=True)
        print(f"Extract {row['key']}", flush=True)
        options = {'segment_chars': row['segment_chars']} if row.get('segment_chars') is not None else {}
        if row.get('allow_long_paper') is True:
            options['allow_long_paper'] = True
        if run_pair(Path(row['pdf']), row['citation'], dest, models, max_tokens=budget, **options):
            print(f"Failed {row['key']}; failure preserved. No drafts changed.", flush=True)
            failures.append(row['key'])
            if not continue_on_error:
                return 1
    print(f'Extraction pass ended: {len(failures)} failed; successful papers await source review. Nothing approved or published.', flush=True)
    (output/'batch-status.json').write_text(json.dumps({'approved': False, 'failed': failures, 'pending_sources': data.get('pending', []), 'status': 'requires_source_review'}, indent=2)+'\n')
    return 1 if failures else 0


def batch(manifest, output, models, budget=20000, execute=False, retry_failed=False, continue_on_error=False):
    if not execute:
        return _batch(manifest, output, models, budget, False, retry_failed, continue_on_error)
    output.parent.mkdir(parents=True, exist_ok=True)
    # The lock survives directory creation and is released even after Ctrl-C.
    with (output.parent / (output.name + '.lock')).open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('This batch is already running') from None
        return _batch(manifest, output, models, budget, True, retry_failed, continue_on_error)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest', type=Path, required=True)
    p.add_argument('--output-dir', type=Path, required=True)
    p.add_argument('--models', nargs=2, default=['gemma4:31b', 'qwen3.8:27b'])
    p.add_argument('--max-output-tokens', type=int, default=20000)
    p.add_argument('--run', action='store_true', help='Execute inference; default previews only')
    p.add_argument('--retry-failed', action='store_true', help='Archive failed paper attempts and explicitly retry them')
    p.add_argument('--continue-on-error', action='store_true', help='Preserve paper failures and continue through the cohort')
    a = p.parse_args()
    raise SystemExit(batch(a.manifest.resolve(), a.output_dir.resolve(), a.models,
                          a.max_output_tokens, a.run, a.retry_failed, a.continue_on_error))
