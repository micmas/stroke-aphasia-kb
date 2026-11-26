import hashlib
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import sync_open_access as sync

PDF=b'%PDF-licensed source'
ROW={'id':'C1234','key':'@Smith2024','title':'A study','doi':'10.1234/test','screening':[{'stage':'title_abstract','decision':'include'}]}
STATUS={'status':'available','source':{'licence':'cc-by','sha256':hashlib.sha256(PDF).hexdigest(),'bytes':len(PDF),'provider':'PMC'}}
class Store:
    def __init__(self,decisions=None):self.decisions=decisions or [];self.reads=0;self.exclude_on_download=False
    def entries(self,prefix):return [{'custom_metadata':d} for d in self.decisions]
    def decision(self,item):return item['custom_metadata']
    def call(self,*args):
        self.reads+=1
        if self.exclude_on_download:self.decisions=[{'stage':'title_abstract','decision':'exclude'}]
        return PDF

def test_only_current_kept_screening_decisions_qualify():
    assert sync.kept(ROW,[])
    assert not sync.kept(ROW,[{'stage':'title_abstract','decision':'pending'}])
    assert not sync.kept(ROW,[{'stage':'full_text','decision':'exclude'}])
    assert not sync.kept({'id':'PLE-0123456789abcdef'},[{'stage':'evidence_review','decision':'include'}])
    assert not sync.kept(dict(ROW,duplicate_of='C1233'),[])
    assert sync.kept(ROW,[{'stage':'evidence_review','decision':'exclude'}])

def test_names_keep_record_identity_and_registered_key():
    assert sync.filename(ROW)=='C1234_Smith2024.pdf'
    assert sync.filename({'id':'PLE-0123456789abcdef','authors':['Hébert, Jane'],'year':2022})=='PLE-0123456789abcdef_Hebert2022.pdf'
    assert '/' not in sync.filename(dict(ROW,key='../../bad/key'))

def test_copy_preserves_source_metadata_and_second_sync_does_not_download(tmp_path,monkeypatch):
    monkeypatch.setattr(sync.oa,'verify_pdf',lambda data:1)
    store=Store();folder=tmp_path/'incoming';papers=tmp_path/'papers'
    result=sync.sync_record(store,ROW,STATUS,folder,papers,execute=True)
    assert result['status']=='downloaded'
    assert (folder/'C1234_Smith2024.pdf').read_bytes()==PDF
    assert (folder/'C1234_Smith2024.source.json').is_file()
    assert sync.sync_record(store,ROW,STATUS,folder,papers,result,True)['status']=='already_synced'
    assert store.reads==1

def test_existing_working_original_is_reused_without_overwrite(tmp_path):
    papers=tmp_path/'papers';originals=papers/'_originals';originals.mkdir(parents=True)
    (papers/'C1234_Smith2024.pdf').write_bytes(b'OCR working version')
    (originals/'C1234_Smith2024.pdf').write_bytes(PDF)
    store=Store();result=sync.sync_record(store,ROW,STATUS,tmp_path/'incoming',papers,execute=True)
    assert result['status']=='already_in_papers' and store.reads==0
    assert (papers/'C1234_Smith2024.pdf').read_bytes()==b'OCR working version'

def test_changed_local_copy_is_never_overwritten(tmp_path):
    folder=tmp_path/'incoming';folder.mkdir();path=folder/'C1234_Smith2024.pdf';path.write_bytes(b'local work')
    store=Store();result=sync.sync_record(store,ROW,STATUS,folder,tmp_path/'papers',execute=True)
    assert result['status']=='local_copy_changed' and store.reads==0
    assert path.read_bytes()==b'local work'

def test_exclusion_during_download_does_not_create_local_copy(tmp_path,monkeypatch):
    monkeypatch.setattr(sync.oa,'verify_pdf',lambda data:1)
    store=Store();store.exclude_on_download=True;folder=tmp_path/'incoming'
    result=sync.sync_record(store,ROW,STATUS,folder,tmp_path/'papers',execute=True)
    assert result['status']=='not_kept' and not folder.exists()

def test_preview_does_not_download_or_create_directories(tmp_path):
    store=Store();folder=tmp_path/'incoming'
    result=sync.sync_record(store,ROW,STATUS,folder,tmp_path/'papers')
    assert result['status']=='would_download' and store.reads==0 and not folder.exists()

def test_bad_checksum_and_unlicensed_metadata_are_not_imported(tmp_path):
    status={'status':'available','source':dict(STATUS['source'],sha256='0'*64)}
    with pytest.raises(ValueError,match='checksum'):sync.sync_record(Store(),ROW,status,tmp_path/'incoming',tmp_path/'papers',execute=True)
    status['source']['licence']=None
    assert sync.sync_record(Store(),ROW,status,tmp_path/'incoming',tmp_path/'papers',execute=True)['status']=='no_collected_copy'
    assert not (tmp_path/'incoming').exists()
