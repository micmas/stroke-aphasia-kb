"""Offline reproductions of observed bugs, not assertions of desired behavior.
Run explicitly: python -m pytest tests/review_reproductions.py -q
All writes are temporary and remote services are replaced with fakes.
"""
import copy
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import pytest
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import auto_review as ar
import promote as pr
import extract as ex
import quote_check as qc
import portal_import as pi
import publish_portal as pp
import benchmark_models as bm
import ollama_client as oc
from aphasia_kb import parse_markdown, _validate_v2_entry

def entry():
    return dict(schema_version=2.8, id='example', name='Example', kind='region',
                status='draft', created_by='agent:ollama-extract-cli/gemma4:31b',
                created_on='2026-11-11', findings=[])

def write(p, fm):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('---\n'+yaml.safe_dump(fm)+'---\n')

def test_same_extractor_is_considered_independent():
    assert ar.reviewer_is_independent(entry()['created_by'], 'gemma4:31b')
    assert pr.validate_review_args('model:gemma4:31b','A',None,entry()) == []

def test_supplied_tier_allows_new_therapy_without_pdf(tmp_path, monkeypatch):
    monkeypatch.setattr(pr, 'ROOT', tmp_path)
    monkeypatch.setattr(pr, 'LOG', tmp_path/'logs/log.md')
    p=tmp_path/'drafts/therapies/example__X.md'
    fm=entry(); fm['kind']='therapy'; write(p,fm)
    pr.cmd_approve(SimpleNamespace(approve=str(p), reviewer='model:other', tier='A', extractor=None))
    assert parse_markdown(tmp_path/'therapies/example.md')[0]['status']=='approved'

def test_one_absent_of_five_passes(tmp_path):
    (tmp_path/'X.txt').write_text('This sentence is present in the study results.')
    fm={'findings':[{'citation':'@X','source_passages':[{'quote':'This sentence is present in the study results.'}]*4+[{'quote':'Invented unicorns reversed every neurological deficit.'}]}]}
    c=ar.check_pdf_quote_match(fm,tmp_path)
    assert c.passed is True and 'absent 1' in c.details[0]

def test_elision_discards_fabricated_short_fragment():
    a='Participants were examined after their first stroke.'
    b='Follow-up measurements were collected after six months.'
    assert qc.grade_quote(a+' [...] cured everyone [...] '+b,qc.PaperText.from_text(a+' '+b))=='elided'
    assert qc.grade_quote(b+' [...] '+a,qc.PaperText.from_text(a+' '+b))=='elided'

def test_model_filename_escapes_drafts_and_overwrites(tmp_path):
    p=tmp_path/'regions/example.md'; write(p,entry())
    ex.save_drafts([{'bucket':'regions','filename':'../../regions/example.md','content':'---\nid: overwritten\n---\n'}],tmp_path)
    assert parse_markdown(p)[0]['id']=='overwritten'

def test_save_overwrites_person_review_and_keeps_invalid_yaml(tmp_path):
    p=tmp_path/'drafts/regions/example.md'; fm=entry(); fm['portal_reviews']=[{'by':'human:A'}]; write(p,fm)
    ex.save_drafts([{'bucket':'regions','filename':'example.md','content':'---\natlases_used: [""MNI152 atlas"]\n---\n'}],tmp_path)
    assert 'portal_reviews' not in p.read_text()
    with pytest.raises(yaml.YAMLError): parse_markdown(p)

def test_normalizer_does_not_fill_status(tmp_path):
    fm=entry(); del fm['status']
    text,_=ex._normalize_findings('---\n'+yaml.safe_dump(fm)+'---\n','regions',None,tmp_path)
    assert 'status:' not in text

def test_pdf_upload_destination_escapes_papers(tmp_path, monkeypatch):
    monkeypatch.setattr(pi,'PAPERS',tmp_path/'papers')
    monkeypatch.setattr(pi.S,'load_candidates',lambda: [])
    p,_,err=pi.pdf_destination({'id':'@../outside'}, {})
    assert not err and p.resolve()==tmp_path/'outside.pdf'

def test_manuscript_metadata_publishes_any_annotated_version(tmp_path):
    (tmp_path/'X_annotated.pdf').write_bytes(b'%PDF-fake publisher version')
    assert pp.scan_pdfs(tmp_path,{'@X':{'category':'cc_manuscript'}})['@X']['public']

def test_failed_public_deletion_forgotten(tmp_path, monkeypatch):
    papers=tmp_path/'papers'; papers.mkdir(); (papers/'X_annotated.pdf').write_bytes(b'%PDF-fake')
    idx=tmp_path/'index.json'
    old=pp.scan_pdfs(papers,{'@X':{'category':'cc'}})
    idx.write_text(json.dumps({'papers':old,'sources':{},'fulltext':{}}))
    monkeypatch.setattr(pp,'licences',lambda:{'@X':{'category':'rights_reserved'}})
    deleted=[]
    def delete(obj): deleted.append(obj); return SimpleNamespace(returncode=1)
    kw=dict(index_path=idx,put=lambda *a:SimpleNamespace(returncode=0),delete=delete,fulltext={},abstracts_path=tmp_path/'absent')
    pp.sync_pdfs(papers,'fake',**kw); pp.sync_pdfs(papers,'fake',**kw)
    assert deleted==['cc/X_annotated.pdf']
    assert json.loads(idx.read_text())['papers']['@X']['annotated']=='pdf/X_annotated.pdf'

def test_manual_require_pdf_match_is_ignored(tmp_path, monkeypatch):
    p=tmp_path/'x.md'; write(p,entry())
    monkeypatch.setattr(ar,'write_report',lambda *a,**k: None)
    verdict,_=ar.apply_manual_verdict(p,verdict_override='approve',rationale='checked',require_pdf_match=True,
                                    auto_promote_on_approve=False,papers_dir=tmp_path/'missing')
    assert verdict==ar.Verdict.APPROVE

def test_stale_portal_verdict_has_no_content_binding(tmp_path, monkeypatch):
    p=tmp_path/'drafts/regions/x.md'; fm=entry(); fm['name']='Changed after review'; write(p,fm)
    monkeypatch.setattr(pi,'ROOT',tmp_path)
    received=[]
    monkeypatch.setattr(ar,'apply_manual_verdict',lambda *a,**k:(received.append(parse_markdown(a[0])[0]['name']) or 'auto_approve',[]))
    pi.apply_verdict({'id':'drafts/regions/x.md','verdict':'approve','per_finding':[]},'Reviewer',True,True,True,{})
    assert received==['Changed after review']

def test_backup_is_selected(tmp_path, monkeypatch):
    p=tmp_path/'_backup/stamp/regions/x.md'; write(p,entry())
    monkeypatch.setattr(ar,'DRAFTS_DIR',tmp_path)
    assert p in ar.select_drafts(all_drafts=True)

def test_empty_extraction_can_be_eligible():
    r={'model':'candidate','paper':'X','findings':0,'quotes':0,'absent':0,'schema_issues':0}
    assert bm.summarise([r],'incumbent')['candidate']['eligible']

def test_publish_replaces_previous_papers(tmp_path, monkeypatch):
    monkeypatch.setattr(bm,'reference_papers',lambda:[])
    monkeypatch.setattr(bm,'attach_sources',lambda *a:None)
    p=tmp_path/'public.json'; p.write_text(json.dumps({'papers':[{'key':'Old'}]}))
    bm.publish([],{},'incumbent',['New'],0,'review',path=p)
    assert [x['key'] for x in json.loads(p.read_text())['papers']]==['New']

def test_loop_detection_raises_name_error(monkeypatch):
    class Resp:
        def __enter__(self): return self
        def __exit__(self,*a): pass
        def __iter__(self):
            for _ in range(128): yield json.dumps({'message':{'content':'x'*40}}).encode()
    monkeypatch.setattr(oc,'model_capabilities',lambda *a:[])
    monkeypatch.setattr(oc.urllib.request,'urlopen',lambda *a,**k:Resp())
    with pytest.raises(NameError,match='LOOP_BLOCK'): oc.chat('fake',verbose=False)

def test_approved_status_in_draft_enters_default_loader(tmp_path):
    import aphasia_kb as kb
    from test_schema_v28 import ENTRY
    fm=copy.deepcopy(ENTRY)
    fm.update(status='approved', reviewer='human:invented', reviewed_on='2026-11-11')
    fm['findings'][0]['therapy']={'id':'test','name':'Test'}
    write(tmp_path/'drafts/regions/injected.md',fm)
    loaded=kb.KnowledgeBase(tmp_path)
    assert len(loaded.findings)==1

def test_loader_sends_v28_to_v1_validator(tmp_path):
    import aphasia_kb as kb
    from test_schema_v28 import ENTRY
    fm=copy.deepcopy(ENTRY) # missing therapy, rejected by actual v2.8 validator
    write(tmp_path/'regions/x.md',fm)
    calls=[]
    with patch.object(kb,'_validate_v2_entry',side_effect=lambda *a:calls.append('v2')), patch.object(kb,'_validate_v1_entry',side_effect=lambda *a:calls.append('v1')):
        kb.KnowledgeBase(tmp_path)
    assert calls==['v1']

def test_normalization_erases_numeric_range():
    assert qc.grade_quote('There were 12 participants.',qc.PaperText.from_text('There were 1–2 participants.'))=='exact'
