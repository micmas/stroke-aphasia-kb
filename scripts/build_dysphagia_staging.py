#!/usr/bin/env python3
"""Import original RIS/NBIB exports and build the isolated, private staging screen.
Raw exports and abstracts remain outside Git. No screening decisions are inferred.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import shutil
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DBS = ('pubmed','scopus','psycinfo','embase','cinahl','wos','central','cdsr')

def norm(text):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode().lower())

def records(text, nbib=False):
    record, last = {}, None
    for line in text.lstrip('\ufeff').splitlines():
        match = re.match(r'^([A-Z0-9]{2,4})\s*-\s?(.*)$', line)
        if match:
            tag, value = match.groups()
            if (nbib and tag == 'PMID') or (not nbib and tag == 'TY'):
                if record:
                    if not nbib: raise ValueError('RIS record missing ER')
                    yield record
                record = {}
            if tag == 'ER':
                if record: yield record
                record, last = {}, None
                continue
            if record or tag in ('TY','PMID'):
                record.setdefault(tag, []).append(value.strip())
                last = tag
        elif line[:1].isspace() and line.strip() and record and last:
            record[last][-1] += ' ' + line.strip()
    if record:
        if not nbib: raise ValueError('Final RIS record missing ER')
        yield record

def convert(r, nbib):
    def first(*tags):
        return next((r[t][0] for t in tags if r.get(t)), '')
    year = re.search(r'\b(?:19|20)\d{2}\b', first('DP','PY','Y1'))
    doi = first('DO')
    if nbib:
        doi = next((v.split(' [doi]')[0] for v in r.get('AID',[]) + r.get('LID',[]) if '[doi]' in v), '')
    doi = re.sub(r'^https?://(?:dx\.)?doi.org/|^doi:\s*', '', doi, flags=re.I).strip().lower()
    authors = r.get('FAU') or r.get('AU') or r.get('A1') or []
    # AN/ID are database accessions, not reliable PubMed IDs.
    pmid = first('PMID') if nbib else first('C2','C5')
    if not pmid.isdigit(): pmid = ''
    return dict(title=first('TI','T1','BTI'), abstract='\n'.join(r.get('AB') or r.get('N2') or []),
                authors=authors, year=int(year[0]) if year else None, doi=doi, pmid=pmid,
                journal=first('JT','JF','JO','JA','T2'), document_type=first('M3','PT','TY'))

def deduplicate(rows):
    groups, doi_index, pmid_index, title_index = [], {}, {}, collections.defaultdict(list)
    for row in rows:
        key = (norm(row['title']), row['year'], norm((row['authors'] or [''])[0].split(',')[0]))
        matches = {i for value,index in [(row['doi'],doi_index),(row['pmid'],pmid_index)] if value and (i:=index.get(value)) is not None}
        if not matches and all(key):
            matches = {i for i in title_index[key]
                       if not (row['doi'] and groups[i]['doi'] and row['doi'] != groups[i]['doi'])
                       and not (row['pmid'] and groups[i]['pmid'] and row['pmid'] != groups[i]['pmid'])}
        # Ambiguous identity matches remain separate for human review.
        if len(matches) == 1:
            i = next(iter(matches)); target = groups[i]
            target['sources'].extend(row['sources'])
            if len(row['abstract']) > len(target['abstract']): target['abstract'] = row['abstract']
            for field in ('doi','pmid','journal','authors','year'):
                if not target[field]: target[field] = row[field]
        else:
            i = len(groups); groups.append(dict(row)); target = groups[i]
        if row['doi']: doi_index.setdefault(row['doi'], i)
        if row['pmid']: pmid_index.setdefault(row['pmid'], i)
        if i not in title_index[key]: title_index[key].append(i)
    for row in groups:
        # Source locator makes IDs reproducible for this immutable search batch.
        source = row['sources'][0]
        row['id'] = 'DYS-' + hashlib.sha256(f"{source['file']}:{source['record']}".encode()).hexdigest()[:16]
    return groups

def build(exports):
    rows, files, warnings = [], [], []
    for db in DBS:
        paths = sorted(p for p in (exports/db).glob('*') if p.suffix.lower() in ('.ris','.nbib'))
        if not paths: raise ValueError(f'No exports for {db}')
        for path in paths:
            raw = path.read_bytes(); parsed = list(records(raw.decode('utf-8-sig'),path.suffix=='.nbib'))
            expected = re.search(r'_(\d+)\.(?:ris|nbib)$',path.name)
            if expected and int(expected[1]) != len(parsed):
                warnings.append(f'{path.name}: filename says {expected[1]} records; file contains {len(parsed)} records.')
            relative = str(path.relative_to(exports))
            files.append(dict(database=db,file=relative,sha256=hashlib.sha256(raw).hexdigest(),records=len(parsed)))
            for index, r in enumerate(parsed,1):
                row = convert(r,path.suffix=='.nbib')
                if not row['title']: raise ValueError(f'Missing title: {relative} record {index}')
                row['sources'] = [dict(database=db,file=relative,record=index)]
                rows.append(row)
    unique = deduplicate(rows)
    summary = dict(chapter='dysphagia',search_date=exports.name,raw_records=len(rows),unique_records=len(unique),
                   duplicates_collapsed=len(rows)-len(unique),missing_abstracts=sum(not r['abstract'] for r in unique),
                   files=files,query_status='User reports searches completed; exact executed queries and filters not independently verified.',
                   deduplication='Exact DOI/PMID, or normalized title + year + first author with no identifier conflict; ambiguous matches retained.',
                   warnings=warnings, notes=['CENTRAL file has cdsr in filename; its folder and CN accession contents identify CENTRAL. Originals unchanged.'])
    dest = ROOT/'staging/dysphagia/dist'
    dest.mkdir(parents=True,exist_ok=True)
    for p in (ROOT/'staging/dysphagia/web').iterdir(): shutil.copy2(p,dest/p.name)
    for name in ('project-shell.css','project-shell.js'): shutil.copy2(ROOT/'explorer'/name,dest/name)
    chunks=[]
    for start in range(0,len(unique),1000):
        name=f'records-{start//1000:03}.json'; chunks.append(name)
        (dest/name).write_text(json.dumps(unique[start:start+1000],ensure_ascii=False))
    (dest/'records.json').write_text(json.dumps(dict(summary=summary,chunks=chunks),ensure_ascii=False))
    (dest/'_headers').write_text('/*\n  Cache-Control: no-store\n  X-Robots-Tag: noindex, nofollow\n')
    (ROOT/'screening/dysphagia/import-manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='files'},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exports',type=Path,required=True)
    build(parser.parse_args().exports)
