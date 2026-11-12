import json
import sys
from pathlib import Path
import pytest
import pymupdf
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import promote as P
from aphasia_kb import parse_markdown

@pytest.fixture
def case(tmp_path, monkeypatch):
    monkeypatch.setattr(P,'ROOT',tmp_path);monkeypatch.setattr(P,'LOG',tmp_path/'logs/extraction_log.md')
    canonical=tmp_path/'regions/region.md';canonical.parent.mkdir()
    P._write(canonical,{'id':'region','status':'approved','findings':[{'id':'f8','citation':'@Paper2022','claim':'Unchanged claim','review':{'reviewer':'human:michele','tier':'B'},'source_passages':[]}]},'Body stays.\n')
    pdf=tmp_path/'Paper2022.pdf';d=pymupdf.open();p=d.new_page();p.insert_text((50,50),'The threshold was p < 0.05 with v = 100.');d.save(pdf);d.close()
    rec=tmp_path/'logs/portal/inbox/edit.json';rec.parent.mkdir(parents=True)
    obj={'kind':'edit','id':'drafts/regions/region__Paper2022.md','citation':'@Paper2022','finding':'f1','fields':{},'reviewer':'reviewer@example.org','passages_added':[{'page':1,'quote':'The threshold was p < 0.05 with v = 100.','supports':'statistics'}]}
    rec.write_text(json.dumps(obj))
    return rec,canonical,pdf,obj

def test_preview_and_resolution_preserve_approval_and_findings(case):
    r,c,p,obj=case;before=c.read_bytes()
    P.resolve_passage_edit(r,c,p,'agent:codex')
    assert c.read_bytes()==before and r.exists()
    P.resolve_passage_edit(r,c,p,'agent:codex',True)
    fm,body=parse_markdown(c);f=fm['findings'][0]
    assert len(fm['findings'])==1 and f['id']=='f8' and f['claim']=='Unchanged claim'
    assert f['review']=={'reviewer':'human:michele','tier':'B'}
    assert f['edits'][0]['by']=='agent:codex' and len(f['source_passages'])==1
    assert not r.exists() and (P.ROOT/'logs/portal/applied/edit.json').exists()
    assert P.resolve_passage_edit(r,c,p,'agent:codex',True)=='Already resolved'
    assert body=='Body stays.\n'

@pytest.mark.parametrize('change',[{'fields':{'claim':{'new':'Unsupported'}}},{'passages_added':[{'page':1,'quote':'This quotation is not in this source PDF.'}]},{'citation':'@Other'}])
def test_refuse_unsupported_changes_without_writing(case,change):
    r,c,p,obj=case;before=c.read_bytes();obj.update(change);r.write_text(json.dumps(obj))
    with pytest.raises(ValueError):P.resolve_passage_edit(r,c,p,'agent:codex',True)
    assert c.read_bytes()==before and r.exists()

def test_archive_failure_can_resume_without_duplicate_passage(case,monkeypatch):
    import pipeline_files
    r,c,p,obj=case;write=pipeline_files.atomic_write
    def fail(path,text):
        if 'applied' in path.parts:raise OSError('simulated interruption')
        return write(path,text)
    monkeypatch.setattr(pipeline_files,'atomic_write',fail)
    with pytest.raises(OSError):P.resolve_passage_edit(r,c,p,'agent:codex',True)
    monkeypatch.setattr(pipeline_files,'atomic_write',write)
    P.resolve_passage_edit(r,c,p,'agent:codex',True)
    assert len(parse_markdown(c)[0]['findings'][0]['source_passages'])==1
