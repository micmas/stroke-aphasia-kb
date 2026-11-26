#!/usr/bin/env python3
"""Import practice search exports; private records never enter the public build."""
import argparse, collections, hashlib, json, re, shutil
from pathlib import Path
from build_dysphagia_staging import records, convert, norm
ROOT=Path(__file__).resolve().parents[1]
DATABASES=('pubmed','medline_ebsco','embase_com','cinahl_ebsco','psycinfo_ebsco','scopus','web_of_science')
def deduplicate(rows):
    groups=[]; indexes=collections.defaultdict(set)
    for row in rows:
        title=(norm(row['title']),row['year'],norm((row['authors'] or [''])[0].split(',')[0]))
        keys=[(k,row[k]) for k in ('doi','pmid') if row[k]]
        if all(title):keys.append(('title',title))
        candidates=set().union(*(indexes[k] for k in keys)) if keys else set()
        candidates={i for i in candidates if all(not(row[k] and groups[i][k] and row[k]!=groups[i][k]) for k in ('doi','pmid'))}
        if len(candidates)==1:
            i=candidates.pop();target=groups[i];target['sources'].extend(row['sources'])
            if len(row['abstract'])>len(target['abstract']):target['abstract']=row['abstract']
            for k in ('doi','pmid','journal','authors','year'):
                if not target[k]:target[k]=row[k]
        else:i=len(groups);groups.append(dict(row))
        for k in keys:indexes[k].add(i)
    for row in groups:
        s=row['sources'][0];row['id']='PLE-'+hashlib.sha256(f"{s['file']}:{s['record']}".encode()).hexdigest()[:16]
    return groups

def import_exports(exports):
    rows=[];files=[];warnings=[]
    for db in DATABASES:
        for strategy in ('q1','q2'):
            paths=sorted(p for p in (exports/db/strategy).glob('*') if p.suffix.lower() in ('.ris','.nbib'))
            if not paths:raise ValueError(f'Missing export: {db}/{strategy}')
            query_paths=sorted((exports/db/strategy).glob('query-v*.txt'));query=query_paths[-1].read_text().strip() if query_paths else ''
            for p in paths:
                raw=p.read_bytes();parsed=list(records(raw.decode('utf-8-sig'),p.suffix.lower()=='.nbib'));relative=str(p.relative_to(exports))
                expected=re.search(r'_(\d+)\.(ris|nbib)$',p.name)
                if expected and int(expected[1])!=len(parsed):warnings.append(f'{relative}: filename count {expected[1]}, actual {len(parsed)}.')
                files.append(dict(database=db,strategy=strategy,file=relative,records=len(parsed),sha256=hashlib.sha256(raw).hexdigest(),query=query,query_status='Prepared query; execution history not independently verified'))
                for n,r in enumerate(parsed,1):
                    row=convert(r,p.suffix.lower()=='.nbib')
                    if not row['title']:raise ValueError(f'Missing title in {relative} record {n}')
                    row['sources']=[dict(database=db,strategy=strategy,file=relative,record=n)];rows.append(row)
    unique=deduplicate(rows)
    summary=dict(section='practice',clinical_domains=['aphasia'],search_date='2026-11-26',raw_records=len(rows),unique_records=len(unique),duplicates_collapsed=len(rows)-len(unique),missing_abstracts=sum(not r['abstract'] for r in unique),files=files,warnings=warnings,deduplication='Exact DOI/PMID or compatible title/year/first-author match; conflicting identifiers and ambiguous matches retained. Every source occurrence is retained.')
    dest=ROOT/'staging/practice/dist';dest.mkdir(parents=True,exist_ok=True);chunks=[]
    for n in range(0,len(unique),1000):
        name=f'records-{n//1000:03}.json';chunks.append(name);(dest/name).write_text(json.dumps(unique[n:n+1000],ensure_ascii=False))
    (dest/'records.json').write_text(json.dumps(dict(summary=summary,chunks=chunks)))
    (dest/'record-ids.json').write_text(json.dumps([r['id'] for r in unique]))
    (ROOT/'screening/practice/import-manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='files'},indent=2));return summary

def build_review():
    dest=ROOT/'deployment/practice-review/dist';dest.mkdir(parents=True,exist_ok=True)
    for p in (ROOT/'staging/practice/web').iterdir():shutil.copy2(p,dest/p.name)
    for name in ('project-shell.css','project-shell.js'):shutil.copy2(ROOT/'explorer'/name,dest/name)
    (dest/'_headers').write_text('/*\n  Cache-Control: no-store\n  X-Robots-Tag: noindex, nofollow\n');print(dest)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--exports',type=Path);args=p.parse_args()
    if args.exports:import_exports(args.exports)
    build_review()
