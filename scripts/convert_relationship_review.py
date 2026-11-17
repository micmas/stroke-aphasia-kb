"""Map saved relationship proposals into source-bound, held KB drafts.
No models, approvals, canonical replacements, or edits to review outputs.
"""
import argparse
import copy
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
import yaml
from aphasia_kb import _validate_v2_entry

ROOT = Path(__file__).resolve().parents[1]
BUCKETS = {'regions', 'impairments', 'therapies', 'ingredients', 'predictors', 'reviews'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def load_review(path):
    state = read(path / 'status.json')
    if state.get('status') not in {'requires_revision', 'requires_source_review'}:
        raise ValueError(f'{path.name}: review is not complete')
    hashes = state.get('output_hashes', {})
    for name in ('proposals.json', 'evidence.json', 'audit.json', 'study-frame.json'):
        if hashes.get(name) != digest(path / name):
            raise ValueError(f'{path.name}: missing or changed review hash for {name}')
    return state, read(path / 'proposals.json'), read(path / 'evidence.json')


def prepare(review_dir, mapping):
    items, skipped = [], []
    for path in sorted(review_dir.iterdir()):
        if not path.is_dir() or not (path / 'status.json').exists():
            continue
        if read(path / 'status.json').get('status') not in {'requires_revision', 'requires_source_review'}:
            skipped.append(path.name)
            continue
        state, proposals, evidence = load_review(path)
        for unit in proposals['units']:
            items.append({'paper': path.name, 'proposal_id': unit['id'],
                          'mapping_date': dt.date.today().isoformat(),
                          'review_status_sha256': digest(path / 'status.json'),
                          'proposal': unit, 'bucket': None, 'entry': None,
                          'instructions': 'Supply a schema 2.8 entry containing exactly one finding. Choose anatomy/target/method/sample from source review, never from labels alone. Unmapped proposals remain pending.'})
    payload = {'version': 1, 'review_dir': str(review_dir.resolve()), 'items': items,
               'skipped_incomplete': skipped, 'approved': False}
    with mapping.open('x') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f'{len(items)} proposals prepared; {len(skipped)} unfinished papers skipped. Mapping: {mapping}')


def build(item, review_dir):
    paper = item['paper']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', paper):
        raise ValueError('Invalid paper key')
    path = review_dir / paper
    state, proposals, evidence = load_review(path)
    if digest(path / 'status.json') != item['review_status_sha256']:
        raise ValueError(f'{paper}: review changed since mapping preparation')
    unit = next((u for u in proposals['units'] if u['id'] == item['proposal_id']), None)
    if unit is None:
        raise ValueError('Proposal no longer exists')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', str(unit['id'])):
        raise ValueError('Invalid proposal ID')
    bucket = item.get('bucket')
    if bucket not in BUCKETS:
        raise ValueError('Choose a supported KB bucket')
    entry = copy.deepcopy(item['entry'])
    if not isinstance(entry, dict) or len(entry.get('findings', [])) != 1:
        raise ValueError('Supply exactly one mapped finding per proposal')
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', str(entry.get('id', ''))):
        raise ValueError('Invalid entry ID')
    for field in ('reviewer', 'reviewed_on', 'review_tier', 'audited_by', 'audited_on'):
        entry.pop(field, None)
    mapping_date = dt.date.fromisoformat(item['mapping_date']).isoformat()
    entry.update(schema_version='2.8', status='draft', created_by='agent:relationship-converter',
                 created_on=mapping_date)
    finding = entry['findings'][0]
    finding.pop('review', None)
    finding['citation'] = '@' + paper
    passages = {p['evidence_id']: p['source'] for p in evidence['passages']}
    selected = list(dict.fromkeys(unit['evidence_ids'] + unit.get('qualifier_ids', [])))
    if not selected or any(i not in passages for i in selected):
        raise ValueError('Missing original source evidence')
    # Source text/page is copied, never generated or accepted from the mapping file.
    finding['source_passages'] = [dict(section='Source passage ' + i,
        page=passages[i]['page'], quote=passages[i]['text'], supports='claim') for i in selected]
    # Source checking can recover omitted Methods/Results without editing the model run.
    # Only existing source IDs are accepted; the converter still copies original text.
    for support in item.get('additional_evidence', []):
        sid = support['source_id']
        if sid not in passages:
            raise ValueError(f'Unknown additional source ID: {sid}')
        finding['source_passages'].append(dict(section=support.get('section', 'Source passage ' + sid),
            page=passages[sid]['page'], quote=passages[sid]['text'], supports=support['supports']))
    if item.get('pdf_evidence'):
        import pymupdf
        pdf = Path(item['source_pdf'])
        if digest(pdf) != state['binding']['input_hashes']['pdf']:
            raise ValueError('Source PDF differs from the reviewed PDF')
        with pymupdf.open(pdf) as document:
            for support in item['pdf_evidence']:
                page = support['page']
                if not isinstance(page, int) or not 1 <= page <= len(document):
                    raise ValueError('Invalid PDF evidence page')
                quote = support['quote']
                if not quote.strip() or ' '.join(quote.split()) not in ' '.join(document[page - 1].get_text().split()):
                    raise ValueError('Additional quotation not found on its source PDF page')
                finding['source_passages'].append({k: support[k] for k in ('section', 'page', 'quote', 'supports')})
    provenance = {'paper': paper, 'proposal_id': unit['id'], 'review_status_sha256': item['review_status_sha256'],
                  'review_binding': state['binding'], 'proposal': unit, 'audit': read(path / 'audit.json'),
                  'study_frame': read(path / 'study-frame.json'), 'approved': False}
    if item.get('source_check'):
        provenance['source_check'] = item['source_check']
    entry['relationship_review'] = provenance
    entry['reviewer_marks'] = [{'id': 'relationship-source-check', 'page': passages[selected[0]]['page'],
        'quote': passages[selected[0]]['text'], 'status': 'pending', 'by': 'agent:relationship-converter',
        'date': mapping_date,
        'note': 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'}]
    issues = []
    _validate_v2_entry(entry, paper, issues)
    if issues:
        raise ValueError('\n'.join(issues))
    suffix = item.get('draft_suffix', '')
    if suffix and not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', suffix):
        raise ValueError('Invalid draft suffix')
    filename = f"{entry['id']}__{paper}__{unit['id']}" + (f'__{suffix}' if suffix else '') + '.md'
    body = '\n# Source review required\n\nThis draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.\n'
    return Path('drafts') / bucket / filename, '---\n' + yaml.safe_dump(entry, sort_keys=False, allow_unicode=True) + '---\n' + body


def convert(mapping, root, execute=False):
    data = read(mapping)
    if data.get('version') != 1:
        raise ValueError('Unsupported mapping version')
    review_dir = Path(data['review_dir'])
    ready, pending = [], 0
    for item in data['items']:
        if item.get('entry') is None:
            pending += 1
            continue
        relative, text = build(item, review_dir)
        path = root / relative
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Draft destination escapes repository: {path}')
        if path.exists():
            if path.read_text() == text:
                continue
            raise ValueError(f'Refusing to overwrite existing draft: {path}')
        if any(p == path for p, _ in ready):
            raise ValueError(f'Duplicate draft destination: {path}')
        ready.append((path, text))
    # Validate the entire batch before writing anything. Exclusive creation protects existing work.
    if execute:
        for path, text in ready:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('x') as f:
                f.write(text)
    print(f'{len(ready)} drafts {"created" if execute else "ready (preview)"}; {pending} proposals still need mapping. Nothing approved or published.')
    return ready


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--review-dir', type=Path, help='Prepare a mapping sheet from completed reviews')
    p.add_argument('--mapping', required=True, type=Path, help='New mapping sheet, or completed mapping to convert')
    p.add_argument('--repo', type=Path, default=ROOT, help='Draft destination; use a separate folder for a trial')
    p.add_argument('--execute', action='store_true')
    args = p.parse_args()
    try:
        if args.review_dir:
            if args.execute:
                p.error('Preparation does not use --execute; fill the mapping then convert separately')
            prepare(args.review_dir, args.mapping)
        else:
            convert(args.mapping, args.repo, args.execute)
    except (ValueError, KeyError, OSError) as exc:
        p.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
