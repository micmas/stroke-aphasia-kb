#!/usr/bin/env python3
"""Copy kept, licensed PDFs into local incoming folders; never overwrite working sources."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import unicodedata
import collect_open_access as oa

STAGES=('title_abstract','full_text')

def receipts(store,id):
    return [store.decision(item) for item in store.entries(f'{oa.PREFIX}decisions/{id}/')]

def kept(record,decisions):
    if record.get('duplicate_of'):return False
    selected=[]
    for stage in STAGES:
        remote=[d for d in decisions if d.get('stage')==stage]
        if remote:selected.extend(d.get('decision') for d in remote)
        else:
            local=[d for d in record.get('screening',[]) if d.get('stage')==stage and not d.get('role')]
            if local:selected.append(local[-1].get('decision'))
    return 'include' in selected and 'exclude' not in selected

def filename(record):
    label=str(record.get('key') or '').lstrip('@')
    if not label:
        authors=record.get('authors') or []
        first=record.get('first_author') or (authors[0] if isinstance(authors,list) and authors else str(authors).split(';')[0])
        first=str(first or 'Paper').split(',')[0]
        label=first+str(record.get('year') or '')
    label=unicodedata.normalize('NFKD',label).encode('ascii','ignore').decode()
    label=re.sub(r'[^A-Za-z0-9_-]','',label)[:100] or 'Paper'
    if not oa.ID.fullmatch(str(record.get('id',''))):raise ValueError('Invalid record ID')
    return record['id']+'_'+label+'.pdf'

def checksum(path):
    with path.open('rb') as handle:return hashlib.file_digest(handle,'sha256').hexdigest()

def matches(path,source):
    return path.is_file() and (not source.get('bytes') or path.stat().st_size==source['bytes']) and checksum(path)==source['sha256']

def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile('w',dir=path.parent,prefix='.sync-',delete=False) as handle:
        json.dump(value,handle,ensure_ascii=False,indent=2);handle.write('\n');name=handle.name
    try:os.replace(name,path)
    finally:Path(name).unlink(missing_ok=True)

def sync_record(store,record,status,folder,papers,old=None,execute=False):
    id=record['id'];source=status.get('source') or {}
    result={'id':id,'title':record.get('title'),'doi':record.get('doi'),'citation_key':record.get('key'),
            'checked_at':oa.now(),'eligible':False,'source':source}
    if not kept(record,receipts(store,id)):return dict(result,status='not_kept')
    result['eligible']=True
    if status.get('status')!='available' or not oa.licence(source.get('licence')) or not re.fullmatch(r'[a-f0-9]{64}',str(source.get('sha256',''))):
        return dict(result,status='no_collected_copy')
    target=folder/filename(record)
    if old and old.get('path'):
        previous=Path(old['path'])
        if previous.parent.resolve()==folder.resolve() and previous.name.startswith(id+'_') and previous.suffix=='.pdf' and previous.exists():target=previous
    if target.exists():
        return dict(result,status='already_synced' if matches(target,source) else 'local_copy_changed',path=str(target))
    # Existing OCR/working sources and originals are read only, never replaced.
    if id.startswith('C'):
        existing=[p for p in papers.glob(id+'_*.pdf') if not p.stem.endswith('_annotated')]
        originals=list((papers/'_originals').glob(id+'_*.pdf'))
        for path in existing+originals:
            if matches(path,source):return dict(result,status='already_in_papers',path=str(path))
        result['working_copy_exists']=bool(existing)
    result['path']=str(target)
    if not execute:return dict(result,status='would_download')
    content=store.call('GET',f'{oa.PREFIX}pdf/{id}.pdf')
    if content is None:return dict(result,status='copy_unavailable')
    if hashlib.sha256(content).hexdigest()!=source['sha256']:raise ValueError(f'{id}: PDF checksum differs from the collection receipt')
    oa.verify_pdf(content)
    if not kept(record,receipts(store,id)):return dict(result,status='not_kept',eligible=False)
    folder.mkdir(parents=True,exist_ok=True)
    # Exclusive creation preserves an unexpected existing file or another writer.
    created=False
    try:
        with target.open('xb') as handle:
            created=True;handle.write(content);handle.flush();os.fsync(handle.fileno())
        if not kept(record,receipts(store,id)):
            target.unlink();return dict(result,status='not_kept',eligible=False)
        result['status']='downloaded'
        write_json(target.with_suffix('.source.json'),result)
    except BaseException:
        if created:target.unlink(missing_ok=True)
        raise
    return result

def sync_chapter(chapter,destination,papers,execute=False,limit=None):
    print(f'{chapter.title()}: checking collected copies and saved screening decisions…',flush=True)
    store=oa.R2(oa.BUCKETS[chapter]);index=store.get(oa.PREFIX+'index.json',{})
    available={id:s for id,s in index.items() if oa.ID.fullmatch(id) and s.get('status')=='available'}
    grouped={}
    for item in store.entries(oa.PREFIX+'decisions/'):
        d=store.decision(item);id=d.get('id') or item['key'].split('/')[2];grouped.setdefault(id,[]).append(d)
    if chapter!='aphasia':
        available={id:s for id,s in available.items() if kept({'id':id},grouped.get(id,[]))}
    rows=oa.candidates(chapter,store) if available else []
    selected=[r for r in rows if r['id'] in available and kept(r,grouped.get(r['id'],[]))]
    eligible_ids={r['id'] for r in selected}
    if limit is not None:selected=selected[:limit]
    folder=destination/chapter;ledger_path=folder/'.open-access-sync.json'
    ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {'version':1,'chapter':chapter,'records':{}}
    if ledger.get('version')!=1 or ledger.get('chapter')!=chapter:raise ValueError('Unrecognised local sync manifest; preserved without changes')
    for id,entry in ledger['records'].items():
        entry['eligible']=id in eligible_ids
        entry['selection_checked_at']=oa.now()
    counts={};failures=0
    for n,record in enumerate(selected,1):
        id=record['id']
        try:
            result=sync_record(store,record,available[id],folder,papers,ledger['records'].get(id),execute)
            ledger['records'][id]=result
            if execute:write_json(ledger_path,ledger)
            outcome=result['status'];counts[outcome]=counts.get(outcome,0)+1
            print(f'[{chapter} {n}/{len(selected)}] {filename(record)} — {outcome}',flush=True)
        except Exception as exc:
            failures+=1;print(f'[{chapter} {n}/{len(selected)}] {id} — {type(exc).__name__}: {exc}',flush=True)
    if execute and (selected or ledger_path.exists()):write_json(ledger_path,ledger)
    print(json.dumps({'chapter':chapter,'kept_with_collected_pdf':len(selected),'counts':counts,'errors':failures}),flush=True)
    return failures

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=oa.ROOT)
    p.add_argument('--destination',type=Path)
    p.add_argument('--chapter',choices=[*oa.BUCKETS,'all'],default='all')
    p.add_argument('--wrangler');p.add_argument('--account-id');p.add_argument('--limit',type=int)
    p.add_argument('--execute',action='store_true');p.add_argument('--dry-run',dest='execute',action='store_false')
    args=p.parse_args();oa.ROOT=args.repo.resolve();papers=(oa.ROOT/'papers').resolve()
    destination=(args.destination or papers/'_incoming/open-access').resolve()
    if args.wrangler:os.environ['STROKE_KB_WRANGLER']=args.wrangler
    if args.account_id:os.environ['CLOUDFLARE_ACCOUNT_ID']=args.account_id
    if args.limit is not None and args.limit<0:p.error('Limit must not be negative')
    lock=Path(tempfile.gettempdir())/('stroke-kb-local-sync-'+hashlib.sha256(str(destination).encode()).hexdigest()[:20]+'.lock')
    with lock.open('a') as handle:
        try:fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:raise SystemExit('A local PDF sync is already running for this folder.')
        failed=0
        for chapter in (list(oa.BUCKETS) if args.chapter=='all' else [args.chapter]):
            try:failed+=sync_chapter(chapter,destination,papers,args.execute,args.limit)
            except Exception as exc:failed+=1;print(f'{chapter}: {type(exc).__name__}: {exc}',flush=True)
    print(f'Incoming folder: {destination}\nNo working PDFs changed; no formatting or models started.',flush=True)
    if failed:raise SystemExit(1)

if __name__=='__main__':
    try:main()
    except KeyboardInterrupt:print('\nStopped. Run the same command to resume.',flush=True);raise SystemExit(130)
