#!/usr/bin/env python3
"""Resumable OA source collection for Stroke KB; never changes eligibility or extraction.

Only explicitly licensed, identifier-matched copies are saved to each chapter's
private R2 prefix. Exclusions remove those copies, retaining source/checksum history.
"""
from __future__ import annotations
import argparse
from collections import Counter
import datetime as dt
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import socket
import time
import unicodedata
import urllib.error
import urllib.parse as U
import urllib.request as H
import xml.etree.ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'open-access/'
BUCKETS = {'aphasia':'stroke-aphasia-kb-pdfs','dysphagia':'dysphagia-kb-private'}
MAX_PDF = 60 * 1024 * 1024
EMAIL = 'm.massontrottier@uq.edu.au'
S3 = 'https://pmc-oa-opendata.s3.amazonaws.com/'
ID = re.compile(r'^(?:C\d+|U[a-f0-9]{32}|DYS-[a-f0-9]{16})$')

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def doi(value):
    return re.sub(r'^https?://(?:dx\.)?doi.org/|^doi:\s*', '', str(value or ''), flags=re.I).strip().lower()

def licence(value):
    value = str(value or '').lower().replace('_','-').replace(' ','-')
    value=re.sub(r'^https?://creativecommons.org/(?:licenses|publicdomain)/','',value).rstrip('/')
    match = re.fullmatch(r'(cc0|cc-by(?:-nc)?(?:-sa|-nd)?|by(?:-nc)?(?:-sa|-nd)?|zero)(?:[/\-][1-4]\.0)?', value)
    if not match: return None
    code = match[1]
    return 'cc0' if code in ('zero','cc0') else code if code.startswith('cc-') else 'cc-'+code

def safe_url(url):
    p = U.urlsplit(url)
    if p.scheme != 'https' or not p.hostname or p.username or p.password or p.port not in (None,443):
        raise ValueError('Unsafe download address')
    for item in socket.getaddrinfo(p.hostname,443,type=socket.SOCK_STREAM):
        if not ipaddress.ip_address(item[4][0]).is_global: raise ValueError('Non-public download address')
    return url

class Redirects(H.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        safe_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def public_get(url, limit=8*1024*1024):
    safe_url(url)
    request=H.Request(url,headers={'User-Agent':f'Stroke-KB/1.0 (mailto:{EMAIL})','Accept':'application/json, application/pdf, */*'})
    with H.build_opener(Redirects()).open(request,timeout=35) as response:
        if int(response.headers.get('Content-Length') or 0)>limit: raise ValueError('File exceeds size limit')
        content=response.read(limit+1)
        if len(content)>limit: raise ValueError('File exceeds size limit')
        return content,response.geturl()

def get_json(url):
    return json.loads(public_get(url)[0])

def normal_text(value):
    return re.sub(r'[^a-z0-9]+','',unicodedata.normalize('NFKD',re.sub(r'<[^>]+>','',str(value or ''))).encode('ascii','ignore').decode().lower())

def identify(record):
    """Resolve missing IDs only with one exact title/year/first-author match."""
    if record.get('doi') or record.get('pmid'): return record
    authors=record.get('authors') or []
    first=authors[0] if isinstance(authors,list) and authors else str(authors).split(';')[0]
    family=normal_text(first.split(',')[0].split(' ')[0])
    title=record.get('title') or ''; year=str(record.get('year') or '')
    if len(normal_text(title))<20 or not re.fullmatch(r'\d{4}',year) or not family: return record
    words=' '.join(re.findall(r'\w+',title))[:400]
    query=f'TITLE:"{words}" AND FIRST_PDATE:[{year}-01-01 TO {year}-12-31]'
    url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+U.urlencode({'query':query,'format':'json','pageSize':25,'resultType':'lite'})
    results=get_json(url).get('resultList',{}).get('result',[])
    matches=[r for r in results if normal_text(r.get('title'))==normal_text(title)
             and str(r.get('pubYear'))==year and normal_text(str(r.get('authorString','')).split(' ')[0])==family
             and (r.get('doi') or (r.get('source')=='MED' and r.get('id')))]
    if len(matches)!=1: return record
    match=matches[0]
    return dict(record,doi=match.get('doi'),pmid=match.get('id') if match.get('source')=='MED' else None,
                identifier_match={'provider':'Europe PMC','method':'exact title, year and first author','url':url})

class R2:
    def __init__(self, bucket):
        self.bucket=bucket
        self.base=f"https://api.cloudflare.com/client/v4/accounts/{os.environ['CLOUDFLARE_ACCOUNT_ID']}/r2/buckets/{bucket}/objects"
        self.token=os.environ['CLOUDFLARE_API_TOKEN']
    def call(self, method, key='', data=None, query=None, content_type='application/json'):
        url=self.base+('/'+U.quote(key,safe='') if key else '')+('?' + U.urlencode(query) if query else '')
        for attempt in range(4):
            try:
                req=H.Request(url,data=data,method=method,headers={'Authorization':'Bearer '+self.token,'Content-Type':content_type})
                with H.urlopen(req,timeout=90) as res: return res.read()
            except urllib.error.HTTPError as e:
                if e.code==404 and method in ('GET','DELETE'): return None
                if e.code not in (429,500,502,503,504) or attempt==3: raise RuntimeError(f'R2 {method} failed: HTTP {e.code}') from None
                time.sleep(2**attempt*2)
        raise RuntimeError('R2 unavailable')
    def get(self,key,default=None):
        raw=self.call('GET',key)
        return json.loads(raw) if raw is not None else default
    def put(self,key,value):
        self.call('PUT',key,json.dumps(value,ensure_ascii=False).encode())
    def delete(self,key): self.call('DELETE',key)
    def entries(self,prefix,limit=None):
        cursor=None
        while True:
            q={'prefix':prefix,'per_page':min(limit or 1000,1000)}
            if cursor: q['cursor']=cursor
            data=json.loads(self.call('GET',query=q))
            if not data.get('success'): raise RuntimeError('R2 listing failed')
            yield from data['result']
            info=data.get('result_info',{})
            if limit or not info.get('is_truncated'): break
            cursor=info['cursor']
    def keys(self,prefix,limit=None):
        return (item['key'] for item in self.entries(prefix,limit))
    def decision(self,item):
        metadata=item.get('custom_metadata')
        return metadata if isinstance(metadata,dict) and 'decision' in metadata else self.get(item['key'])
    def blocked(self,id):
        return any(self.decision(item).get('decision')=='exclude'
                   for item in self.entries(f'{PREFIX}decisions/{id}/'))

def candidates(chapter,store):
    if chapter=='dysphagia':
        if not store.get(PREFIX+'decisions-ready.json'):
            raise RuntimeError('Dysphagia decision reconciliation must finish before collecting PDFs')
        manifest=store.get('screening/records.json')
        if not manifest: raise RuntimeError('Missing Dysphagia import')
        return [r for name in manifest['chunks'] for r in store.get('screening/'+name)]
    data=yaml.load((ROOT/'screening/candidates.yaml').read_text(),Loader=yaml.CSafeLoader)
    rows=data if isinstance(data,list) else data['candidates']
    by_id={r['id']:r for r in rows}
    # Pending human decisions must take effect before the six-hour register apply.
    for path in sorted((ROOT/'logs/portal/inbox').glob('*_screen_*.json')):
        event=json.loads(path.read_text())
        if event.get('id') in by_id and not event.get('role'):
            by_id[event['id']].setdefault('screening',[]).append(event)
    for row in rows:
        latest={d['stage']:d for d in row.get('screening',[]) if not d.get('role') and d.get('stage')}
        row['excluded']=bool(row.get('duplicate_of') or any(d.get('decision')=='exclude' for d in latest.values()))
        row['kept']=any(d.get('decision')=='include' for d in latest.values())
    return rows

def pmc_locations(record):
    identifier=str(record.get('pmid') or doi(record.get('doi')))
    if not identifier: return []
    q=U.urlencode({'ids':identifier,'format':'json','tool':'stroke-kb','email':EMAIL})
    mapped=get_json('https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?'+q).get('records',[])
    pmc=next((r for r in mapped if r.get('pmcid') and str(r.get('requested-id','')).lower()==identifier.lower()),None)
    if not pmc or pmc.get('live') is False or pmc.get('live')=='false': return []
    pmcid=pmc['pmcid']
    if not re.fullmatch(r'PMC\d+',pmcid): return []
    xml=ET.fromstring(public_get(S3+'?'+U.urlencode({'list-type':2,'prefix':pmcid+'.','delimiter':'/'}))[0])
    prefixes=[x.text for x in xml.findall('{*}CommonPrefixes/{*}Prefix')]
    out=[]
    for prefix in prefixes[:10]:
        version=prefix.rstrip('/')
        if not re.fullmatch(re.escape(pmcid)+r'\.\d+',version): continue
        metadata=get_json(S3+version+'/'+version+'.json')
        if doi(record.get('doi')) and doi(metadata.get('doi'))!=doi(record['doi']): continue
        if record.get('pmid') and str(metadata.get('pmid'))!=str(record['pmid']): continue
        code=licence(metadata.get('license_code'))
        if not code or not metadata.get('pdf_url'): continue
        url=metadata['pdf_url']
        if url.startswith('s3://pmc-oa-opendata/'): url=S3+url.removeprefix('s3://pmc-oa-opendata/')
        if U.urlsplit(url).hostname!='pmc-oa-opendata.s3.amazonaws.com': continue
        out.append({'url':url,'licence':code,'licence_text':metadata.get('license_code'),'provider':'PMC','pmcid':pmcid,
                    'version':'acceptedVersion' if str(metadata.get('is_manuscript')).lower() in ('yes','true') else 'publishedVersion',
                    'metadata_url':S3+version+'/'+version+'.json'})
    return sorted(out,key=lambda x:x['version']!='publishedVersion')

def unpaywall_locations(record):
    identifier=doi(record.get('doi'))
    if not identifier: return []
    url='https://api.unpaywall.org/v2/'+U.quote(identifier,safe='')+'?'+U.urlencode({'email':EMAIL})
    try: data=get_json(url)
    except urllib.error.HTTPError as exc:
        if exc.code==404: return []
        raise
    if doi(data.get('doi'))!=identifier or not data.get('is_oa'): return []
    locations=data.get('oa_locations') or []
    return [{'url':loc['url_for_pdf'],'licence':licence(loc['license']),'licence_text':loc['license'],'provider':'Unpaywall',
             'version':loc.get('version'),'metadata_url':'https://api.unpaywall.org/v2/'+U.quote(identifier,safe='')}
            for loc in locations if loc.get('url_for_pdf') and licence(loc.get('license'))
            and not (U.urlsplit(loc['url_for_pdf']).hostname or '').endswith('ncbi.nlm.nih.gov')]

def verify_pdf(content):
    if len(content)<1024 or not content.startswith(b'%PDF-'): raise ValueError('Response is not a PDF')
    import pymupdf
    with pymupdf.open(stream=content,filetype='pdf') as doc:
        if doc.is_encrypted or doc.page_count<1: raise ValueError('Unreadable PDF')
        return doc.page_count

def retrieve(record):
    errors=[]
    try: record=identify(record)
    except Exception as exc: errors.append(f'identifier lookup: {type(exc).__name__}')
    for resolver in (pmc_locations,unpaywall_locations):
        try: locations=resolver(record)
        except Exception as exc:
            errors.append(f'{resolver.__name__}: {type(exc).__name__}')
            continue
        for location in locations:
            try:
                content,final_url=public_get(location['url'],MAX_PDF)
                pages=verify_pdf(content)
                return content,dict(location,final_url=final_url,pages=pages,bytes=len(content),sha256=hashlib.sha256(content).hexdigest(),identifier_match=record.get('identifier_match')),errors
            except Exception as exc: errors.append(f"{location['provider']} PDF: {type(exc).__name__}")
    return None,None,errors

def collect_one(store,record,old=None):
    id=record['id']; pdf=f'{PREFIX}pdf/{id}.pdf'
    status={'id':id,'checked_at':now(),'status':'not_found','doi':doi(record.get('doi')) or None}
    if record.get('excluded') or store.blocked(id):
        store.delete(pdf)
        return dict(old or status,status='excluded',checked_at=now())
    content,source,errors=retrieve(record)
    if content is None:
        status.update(status='retry' if errors else 'not_found',errors=errors)
        return status
    if store.blocked(id): return dict(status,status='excluded')
    store.call('PUT',pdf,content,content_type='application/pdf')
    # Covers exclusions saved while an HTTP download or R2 upload was in flight.
    if store.blocked(id):
        store.delete(pdf)
        return dict(status,status='excluded',source=source)
    return dict(status,status='available',source=source)

def run(chapter,max_records,deadline):
    store=R2(BUCKETS[chapter]); rows=candidates(chapter,store)
    rows=[r for r in rows if ID.fullmatch(str(r.get('id','')))]
    index=store.get(PREFIX+'index.json',{})
    blocked={item['key'].split('/')[2] for item in store.entries(PREFIX+'decisions/')
             if store.decision(item).get('decision')=='exclude'}
    present={Path(key).stem for key in store.keys(PREFIX+'pdf/')}
    retry={Path(key).stem for key in store.keys(PREFIX+'retry/')}
    # Reconcile deletions across the whole collection before starting new downloads.
    for row in rows:
        id=row['id']
        if row.get('excluded') or id in blocked:
            if index.get(id,{}).get('status')!='excluded':
                if id in index:
                    store.delete(f'{PREFIX}pdf/{id}.pdf')
                    store.put(f'{PREFIX}status/{id}.json',dict(index[id],status='excluded',checked_at=now()))
                index[id]=dict(index.get(id,{ }),id=id,status='excluded',checked_at=now())
    def due(row):
        s=index.get(row['id'],{})
        if row.get('excluded') or row['id'] in blocked: return False
        if not s or s.get('status')=='excluded': return True
        if row['id'] in retry: return True
        if s.get('status')=='available' and row['id'] not in present: return True
        if s.get('status')=='available': return False
        age=(dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat(s['checked_at'])).total_seconds()
        return age>(86400 if s.get('status')=='retry' else 30*86400)
    todo=sorted((r for r in rows if due(r)),key=lambda r:(r['id'] not in retry,not r.get('kept',False),r['id']))
    processed=0
    for row in todo[:max_records]:
        if time.monotonic()>deadline: break
        status=collect_one(store,row,index.get(row['id']))
        index[row['id']]=status
        stamp=status['checked_at'].replace(':','-')
        store.put(f"{PREFIX}history/{row['id']}/{stamp}.json",status)
        store.put(f"{PREFIX}status/{row['id']}.json",status)
        # Keep retries for retained records until they have actually been attempted.
        store.delete(f"{PREFIX}retry/{row['id']}.json")
        processed+=1
        print(json.dumps({'chapter':chapter,'id':row['id'],'status':status['status']}),flush=True)
        if processed%10==0:
            store.put(PREFIX+'index.json',index)
            store.put(PREFIX+'summary.json',{'chapter':chapter,'updated':now(),'candidates':len(rows),'processed_this_run':processed,
                      'remaining_this_pass':len(todo)-processed,'running':True,'counts':dict(Counter(x['status'] for x in index.values()))})
    store.put(PREFIX+'index.json',index)
    summary={'chapter':chapter,'updated':now(),'candidates':len(rows),'processed_this_run':processed,'running':False,
             'remaining_this_pass':len(todo)-processed,'counts':dict(Counter(x['status'] for x in index.values()))}
    store.put(PREFIX+'summary.json',summary)
    print(json.dumps(summary),flush=True)
    return summary

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapter',choices=[*BUCKETS,'all'],default='all')
    parser.add_argument('--max-records',type=int,default=500)
    parser.add_argument('--minutes',type=int,default=45)
    args=parser.parse_args()
    chapters=list(BUCKETS) if args.chapter=='all' else [args.chapter]
    failed=False
    for chapter in chapters:
        try: run(chapter,args.max_records,time.monotonic()+args.minutes*60/len(chapters))
        except Exception as exc:
            print(json.dumps({'chapter':chapter,'error':str(exc)}),flush=True)
            failed=True
    if failed: raise SystemExit(1)

if __name__=='__main__': main()
