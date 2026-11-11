"""Freeze the full registered KB paper inventory; never reads or changes findings."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from strict_data import load_yaml


def prepare(repo, output):
    if output.exists():
        raise ValueError('Manifest already exists; keep it frozen or choose a new path')
    text = (repo/'citations.md').read_text()
    entries = re.findall(r'^## @([A-Za-z0-9_-]+)[^\n]*', text, re.M)
    if not entries:
        raise ValueError('No bibliography keys found')
    refused = set(re.findall(r'^## @([A-Za-z0-9_-]+)\s+\[refused\]', text, re.M))
    registry = load_yaml((repo/'screening/licences.yaml').read_text()).get('papers', {})
    # Resolve uploaded filenames only when the screening DOI matches the bibliography.
    blocks = dict(re.findall(r'^## @([A-Za-z0-9_-]+)(.*?)(?=^## |\Z)', text, re.M | re.S))
    candidate_path = repo/'screening/candidates.yaml'
    candidates = load_yaml(candidate_path.read_text()).get('candidates', []) if candidate_path.exists() else []
    aliases = {}
    for key, block in blocks.items():
        doi_match = re.search(r'(10\.\d{4,9}/[^\s<>]+)', block, re.I)
        if not doi_match:
            continue
        doi = doi_match.group(1).rstrip('.,;)').lower()
        matches = {c.get('pdf_file') for c in candidates
                   if str(c.get('doi', '')).lower() == doi and c.get('pdf_file')}
        if len(matches) == 1:
            name = matches.pop()
            if Path(name).name == name and name.endswith('.pdf') and not name.endswith('_annotated.pdf'):
                aliases[key] = repo/'papers'/name
    papers, pending = [], []
    for key in sorted(set(entries)):
        pdf = repo/'papers'/f'{key}.pdf'
        if not pdf.is_file() and key in aliases:
            pdf = aliases[key]
        if key in refused or not pdf.is_file():
            pending.append({'key': key, 'status': 'source_preparation_required',
                            'reason': 'Bibliography marks source not extractable' if key in refused else 'Main PDF missing'})
            continue
        papers.append({'key': key, 'citation': '@'+key, 'pdf': str(pdf.resolve()),
                       'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                       'licence_evidence': registry.get('@'+key) or {'category': 'unknown'},
                       'processing': 'local_only; review/publication rights checked separately'})
    used = {Path(p['pdf']).stem for p in papers}
    unregistered = sorted(p.stem for p in (repo/'papers').glob('*.pdf')
                          if p.stem not in entries and p.stem not in used and not p.stem.endswith('_annotated'))
    data = {'source_scope': 'main_paper_only',
            'method': 'source-inventory-v2: two independent extractions plus separate source review',
            'selection': 'Every registered bibliography paper, regardless of prior extraction or approval. Only main PDFs are queued. No supplements or annotated copies. Licence metadata is provenance, not permission for external sharing.',
            'papers': papers, 'pending': pending,
            'unregistered_pdf_stems_requiring_identification': unregistered}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2)+'\n')
    print(f'{len(papers)} ready; {len(pending)} need source preparation; {len(unregistered)} unregistered PDFs need identification')
    return data


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    prepare(a.repo.resolve(), a.output.resolve())
