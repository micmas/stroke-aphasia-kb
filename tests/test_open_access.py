import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import collect_open_access as oa

class Store:
    def __init__(self,blocks):self.blocks=iter(blocks);self.files={};self.deleted=[]
    def blocked(self,id):return next(self.blocks)
    def delete(self,key):self.deleted.append(key);self.files.pop(key,None)
    def call(self,method,key,data=None,**kwargs):self.files[key]=data

def test_exclusion_during_upload_removes_bytes_and_keeps_source_receipt(monkeypatch):
    monkeypatch.setattr(oa,'retrieve',lambda r:(b'%PDF-source',{'sha256':'receipt','licence':'cc-by'},[]))
    store=Store([False,False,True])
    result=oa.collect_one(store,{'id':'C1234'})
    assert result['status']=='excluded'
    assert result['source']['sha256']=='receipt'
    assert store.files=={}
    assert store.deleted==['open-access/pdf/C1234.pdf']

def test_excluded_candidates_are_never_fetched(monkeypatch):
    monkeypatch.setattr(oa,'retrieve',lambda r:pytest.fail('Excluded paper downloaded'))
    store=Store([])
    result=oa.collect_one(store,{'id':'C1234','excluded':True},{'source':{'sha256':'existing'}})
    assert result['status']=='excluded' and result['source']['sha256']=='existing'

def test_available_copy_records_provenance_and_bytes(monkeypatch):
    monkeypatch.setattr(oa,'retrieve',lambda r:(b'%PDF-source',{'sha256':'receipt','licence':'cc-by'},[]))
    store=Store([False,False,False]);result=oa.collect_one(store,{'id':'C1234'})
    assert result['status']=='available'
    assert store.files=={'open-access/pdf/C1234.pdf':b'%PDF-source'}

def test_missing_copy_and_temporary_failure_are_distinct(monkeypatch):
    monkeypatch.setattr(oa,'retrieve',lambda r:(None,None,[]))
    assert oa.collect_one(Store([False]),{'id':'C1234'})['status']=='not_found'
    monkeypatch.setattr(oa,'retrieve',lambda r:(None,None,['HTTPError']))
    assert oa.collect_one(Store([False]),{'id':'C1234'})['status']=='retry'

def test_licences_and_pdf_validation():
    assert oa.licence('CC BY-NC-ND')=='cc-by-nc-nd'
    assert oa.licence('https://creativecommons.org/licenses/by/4.0/')=='cc-by'
    assert oa.licence('https://creativecommons.org/publicdomain/zero/1.0/')=='cc0'
    for value in ('publisher-specific','TDM','unknown','not-cc-by',None):assert oa.licence(value) is None
    with pytest.raises(ValueError):oa.verify_pdf(b'<html>not a PDF</html>'*100)

def test_download_rejects_local_hosts_credentials_and_redirects(monkeypatch):
    for url in ('file:///etc/passwd','http://example.org/p.pdf','https://user:secret@example.org/p.pdf'):
        with pytest.raises(ValueError):oa.safe_url(url)
    monkeypatch.setattr(oa.socket,'getaddrinfo',lambda *a,**kw:[(None,None,None,None,('127.0.0.1',443))])
    with pytest.raises(ValueError):oa.safe_url('https://example.org/p.pdf')

def test_unpaywall_requires_matching_doi_and_explicit_licence(monkeypatch):
    monkeypatch.setattr(oa,'get_json',lambda url:{'doi':'10.1234/wrong','is_oa':True,'oa_locations':[{'url_for_pdf':'https://publisher.org/p.pdf','license':'cc-by'}]})
    assert oa.unpaywall_locations({'doi':'10.1234/right'})==[]

def test_missing_ids_require_unambiguous_title_year_author_match(monkeypatch):
    record={'id':'C1234','title':'Swallowing impairment after cerebral stroke','year':2024,'authors':['Smith, Jane']}
    hit={'title':record['title'],'pubYear':'2024','authorString':'Smith J, Doe K','source':'MED','id':'123456','doi':'10.1234/test'}
    monkeypatch.setattr(oa,'get_json',lambda url:{'resultList':{'result':[hit]}})
    found=oa.identify(record)
    assert found['pmid']=='123456' and found['identifier_match']['provider']=='Europe PMC'
    assert 'pmid' not in record
    monkeypatch.setattr(oa,'get_json',lambda url:{'resultList':{'result':[hit,dict(hit,id='456789')]}})
    assert oa.identify(record)==record
    monkeypatch.setattr(oa,'get_json',lambda url:{'resultList':{'result':[dict(hit,authorString='Smithson J')]}})
    assert oa.identify(record)==record
    monkeypatch.setattr(oa,'get_json',lambda url:{'doi':'10.1234/right','is_oa':True,'oa_locations':[{'url_for_pdf':'https://publisher.org/p.pdf','license':None}]})
    assert oa.unpaywall_locations({'doi':'10.1234/right'})==[]


def test_practice_candidates_use_their_own_ready_import():
    class ImportStore:
        def get(self,key):
            return {'open-access/decisions-ready.json':{'at':'ready'},
                    'screening/records.json':{'chunks':['records-000.json']},
                    'screening/records-000.json':[{'id':'PLE-0123456789abcdef','title':'Practice paper'}]}[key]
    rows=oa.candidates('practice',ImportStore())
    assert rows[0]['id']=='PLE-0123456789abcdef' and oa.ID.fullmatch(rows[0]['id'])
    assert oa.BUCKETS['practice'] not in [oa.BUCKETS['aphasia'],oa.BUCKETS['dysphagia']]


def test_collections_start_together_and_one_failure_does_not_stop_the_others(monkeypatch):
    import threading
    from concurrent.futures import ThreadPoolExecutor
    barrier=threading.Barrier(3);finished=[]
    def fake_run(chapter,max_records,deadline):
        barrier.wait(timeout=3)
        if chapter=='dysphagia':raise RuntimeError('One provider failed')
        finished.append(chapter)
    monkeypatch.setattr(oa,'ProcessPoolExecutor',ThreadPoolExecutor)
    monkeypatch.setattr(oa,'run',fake_run)
    assert oa.run_collections(list(oa.BUCKETS),20,999999999) is True
    assert set(finished)=={'aphasia','practice'}


def test_interrupted_collection_saves_records_before_the_ten_record_checkpoint(monkeypatch):
    class MemoryStore:
        def __init__(self):self.files={}
        def get(self,key,default=None):return self.files.get(key,default)
        def put(self,key,value):self.files[key]=value.copy()
        def delete(self,key):self.files.pop(key,None)
        def entries(self,prefix):return []
        def keys(self,prefix):return []
    store=MemoryStore();rows=[{'id':'C'+str(n)} for n in range(5)];calls=[]
    def collect(store,row,old):
        if len(calls)==2:raise KeyboardInterrupt
        calls.append(row['id'])
        return {'id':row['id'],'checked_at':oa.now(),'status':'not_found'}
    monkeypatch.setattr(oa,'R2',lambda bucket:store)
    monkeypatch.setattr(oa,'candidates',lambda *args:rows)
    monkeypatch.setattr(oa,'collect_one',collect)
    with pytest.raises(KeyboardInterrupt):oa.run('practice',20,oa.time.monotonic()+60)
    assert set(store.files[oa.PREFIX+'index.json'])=={'C0','C1'}
    assert store.files[oa.PREFIX+'summary.json']['processed_this_run']==2
    assert store.files[oa.PREFIX+'summary.json']['running'] is False
