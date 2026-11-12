import hashlib
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import portal_import as P


def test_received_original_resolves_processed_pdf_without_overwriting(monkeypatch,tmp_path):
    monkeypatch.setattr(P,'PAPERS',tmp_path)
    c={'id':'C0001','key':'@Smith2020'}
    monkeypatch.setattr(P.S,'load_candidates',lambda:[c])
    working=tmp_path/'C0001_Smith2020.pdf';working.write_bytes(b'processed')
    (tmp_path/'_originals').mkdir()
    original=tmp_path/'_originals/C0001_Smith2020_original.pdf';original.write_bytes(b'raw')
    deletes=[];monkeypatch.setitem(P.FETCH,'delete',lambda *a:deletes.append(a))
    record={'id':'C0001','sha256':hashlib.sha256(b'raw').hexdigest(),'bucket':'b','object':'uploads/c0001.pdf'}
    msg=P.apply_pdf(record,'test',True,{})
    assert 'exact uploaded bytes verified at _originals/' in msg
    assert working.read_bytes()==b'processed' and original.read_bytes()==b'raw'
    assert len(deletes)==1
    record['sha256']=hashlib.sha256(b'unseen replacement').hexdigest()
    assert P.apply_pdf(record,'test',True,{}).startswith('skip:')
    assert len(deletes)==1 and working.read_bytes()==b'processed'


def test_original_of_other_record_is_not_a_receipt(monkeypatch,tmp_path):
    monkeypatch.setattr(P,'PAPERS',tmp_path)
    (tmp_path/'_originals').mkdir()
    (tmp_path/'_originals/C0002_other.pdf').write_bytes(b'raw')
    assert P.received_pdf({'sha256':hashlib.sha256(b'raw').hexdigest()},tmp_path/'working.pdf',{'id':'C0001'}) is None
