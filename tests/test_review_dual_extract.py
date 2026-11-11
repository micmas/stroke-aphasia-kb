import hashlib
import json
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import review_dual_extract as r

TEXT='=== PAGE 1 ===\nThe association was not significant.\n'
TAGS={'extract-a':'digest-a','extract-b':'digest-b','reviewer':'digest-c'}


def inventory():
    return {'citation':'@Test2026','outcomes':['naming'],'analyses':[{
        'id':'a1','outcome':'naming','outcome_timing':'current level','method':'correlation',
        'predictors':['volume'],'selected_predictors':[],'covariates':[],
        'result':'not significant','estimates':[],'uncertainties':[],
        'evidence':[{'source_id':'P1-S1','quote':'The association was not significant.'}]}],
        'discrepancies':[],'coverage_notes':[]}


def final():
    return {'inventory':inventory(),'decisions':[
        {'arm':arm,'analysis_id':'a1','action':'retain','final_ids':['a1'],'reason':'Source confirms the null.',
         'evidence':inventory()['analyses'][0]['evidence']} for arm in ['A','B']],
        'coverage':[{'source_id':'P1-S1','status':'covered','final_ids':['a1'],'reason':'Null association.'}],
        'study_context':'Small observational cohort; other details unreported.',
        'summary':'No association detected.','unresolved':[]}


@pytest.fixture
def paper(tmp_path,monkeypatch):
    run=tmp_path/'run'; folder=run/'Test2026';folder.mkdir(parents=True)
    pdf=tmp_path/'main.pdf';pdf.write_bytes(b'pdf')
    row={'key':'Test2026','citation':'@Test2026','pdf':str(pdf),'pdf_sha256':r.digest(pdf)}
    r.write(run/'batch-config.json',{'manifest':{'papers':[row]}})
    r.write(folder/'status.json',{'status':'awaiting_independent_review'})
    for arm,model in [('A','extract-a'),('B','extract-b')]:
        d=folder/arm;d.mkdir();(d/'prompt.txt').write_text('original')
        r.write(d/'meta.json',{'status':'requires_review','citation':row['citation'],
           'pdf_sha256':row['pdf_sha256'],'prompt_sha256':r.digest(d/'prompt.txt'),
           'model':model,'source_scope':'main_paper_only','inference':{}})
        r.write(d/'raw.json',inventory());r.write(d/'source-units.json',r.source_units(TEXT))
    monkeypatch.setattr(r,'_extract_pdf_text',lambda p:(TEXT,1))
    monkeypatch.setattr(r,'identities',lambda host:dict(TAGS))
    return run,row,tmp_path/'reviews'


def responses(monkeypatch, invalid=False):
    prompts=[]
    def chat(prompt,**kwargs):
        prompts.append(prompt)
        result=inventory() if len(prompts)%2 else final()
        if invalid and len(prompts)%2==0:result['decisions']=[]
        return {'text':json.dumps(result),'truncated_input':False,'truncated_output':False}
    monkeypatch.setattr(r,'chat',chat)
    return prompts


def test_two_stages_resume_and_never_approve(paper,monkeypatch):
    run,row,out=paper;prompts=responses(monkeypatch)
    before={str(p):r.digest(p) for p in run.rglob('*') if p.is_file()}
    assert r.batch(run,out,'reviewer',True)==0
    assert len(prompts)==2 and 'EXTRACTIONS:' not in prompts[0] and 'EXTRACTIONS:' in prompts[1]
    state=r.read(out/row['key']/'status.json')
    assert state['status']=='requires_visual_review' and state['approved'] is False
    assert r.read(out/row['key']/'visual-review-required.json')['pages']==[1]
    assert r.batch(run,out,'reviewer',True)==0
    assert len(prompts)==2
    assert before=={str(p):r.digest(p) for p in run.rglob('*') if p.is_file()}


def test_preview_does_not_call_model_or_write(paper,monkeypatch):
    run,row,out=paper
    monkeypatch.setattr(r,'chat',lambda *a,**k:pytest.fail('inference'))
    assert r.batch(run,out,'reviewer')==0 and not out.exists()


def test_missing_decisions_requires_revision(paper,monkeypatch):
    run,row,out=paper;responses(monkeypatch,True)
    assert r.batch(run,out,'reviewer',True)==1
    assert r.read(out/row['key']/'status.json')['status']=='requires_revision'


def test_validation_rejects_bad_quote_and_coverage():
    f=final();f['decisions'][0]['evidence']=[{'source_id':'P1-S1','quote':'was significant'}];f['coverage']=[]
    arms={a:{'extraction':inventory()} for a in ['A','B']}
    issues=r.validate(f,r.source_units(TEXT),'@Test2026',arms)
    assert any('not exact' in x for x in issues) and 'Source-unit coverage incomplete' in issues


def test_failed_pair_not_reviewed(paper,monkeypatch):
    run,row,out=paper;r.write(run/row['key']/'status.json',{'status':'failed'})
    assert r.completed(run)[0]==[]
    with pytest.raises(ValueError,match='completed'):r.load_paper(run,row)


def test_source_tamper_rejected(paper):
    run,row,out=paper;Path(row['pdf']).write_bytes(b'changed')
    with pytest.raises(ValueError,match='PDF differs'):r.load_paper(run,row)


def test_reviewer_alias_rejected(paper):
    run,row,out=paper
    with pytest.raises(ValueError,match='differ'):
        r.review_one(run,row,out/'Test2026','alias','http://localhost:11434',20000,dict(TAGS,alias='digest-a'))
    assert not out.exists()


def test_active_extraction_blocks_review(paper,monkeypatch):
    import fcntl
    run,row,out=paper;monkeypatch.setattr(r,'chat',lambda *a,**k:pytest.fail('inference'))
    with (run.parent/'run.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        with pytest.raises(ValueError,match='Stop extraction'):r.batch(run,out,'reviewer',True)


def test_truncation_preserves_raw_and_never_exports_inventory(paper,monkeypatch):
    run,row,out=paper
    monkeypatch.setattr(r,'chat',lambda *a,**k:{'text':'partial','truncated_output':True})
    assert r.batch(run,out,'reviewer',True)==1
    d=out/row['key'];assert (d/'source-first/raw.json').read_text()=='partial'
    assert r.read(d/'status.json')['status']=='failed' and not (d/'inventory.json').exists()


def test_saved_review_tamper_not_reused(paper,monkeypatch):
    run,row,out=paper;prompts=responses(monkeypatch);r.batch(run,out,'reviewer',True)
    (out/row['key']/'inventory.json').write_text('{}')
    assert r.batch(run,out,'reviewer',True)==1 and len(prompts)==2


def test_output_must_not_touch_extraction(paper):
    run,row,out=paper
    with pytest.raises(ValueError,match='separate'):r.batch(run,run/'reviews','reviewer')


def test_remote_host_rejected():
    with pytest.raises(ValueError,match='loopback'):r.identities('https://example.com')
