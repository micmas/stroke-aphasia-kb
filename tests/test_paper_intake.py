import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import portal_import as P
import screening as S

def record(**kw):
    return {'id':'U'+'a'*32,'title':'A new aphasia paper','doi':'10.1234/test','new_candidate':True,'submitted':'2026-11-12T12:00:00Z','_record':'paper.json',**kw}

def test_new_paper_is_other_source_not_approved_and_replays_once(monkeypatch):
    monkeypatch.setattr(S,'load_candidates',lambda:[])
    state={'candidates':[]};r=record()
    P.apply_paper(r,'human:Test',True,state);P.apply_paper(r,'human:Test',True,state)
    assert len(state['candidates'])==1
    c=state['candidates'][0]
    assert S.arm_of(c)=='other' and S.stage_of(c)[0]=='awaiting_ta'
    assert len(c['sources'])==1 and not c['screening']

def test_concurrent_registration_reconciles_to_existing_id_and_retains_decisions(monkeypatch,tmp_path):
    monkeypatch.setattr(S,'load_candidates',lambda:[]);monkeypatch.setattr(P,'PAPERS',tmp_path)
    c={'id':'C12','doi':'10.1234/test','title':'A new aphasia paper','screening':[{'stage':'title_abstract','decision':'exclude'}]}
    state={'candidates':[c]};r=record()
    P.apply_paper(r,'human:Test',True,state)
    assert len(state['candidates'])==1 and r['id'] in c['upload_ids']
    assert c['screening'][0]['decision']=='exclude'
    dest,cand,err=P.pdf_destination({'id':r['id'],'name':'paper.pdf'},state)
    assert not err and cand is c and dest.name=='C12_paper.pdf'

def test_invalid_or_conflicting_identity_is_not_written(monkeypatch):
    monkeypatch.setattr(S,'load_candidates',lambda:[])
    state={'candidates':[{'id':'C1','doi':'10.1234/other','title':'Existing paper'}]}
    assert P.apply_paper(record(id='../x'),'Test',True,state).startswith('skip:')
    assert P.apply_paper(record(id='C1'),'Test',True,state).startswith('skip:')
    assert 'pdf_uploaded_at' not in state['candidates'][0]

def test_uploaded_candidate_is_included_above_ranked_queue_limit(monkeypatch,tmp_path):
    import publish_portal as B
    import screen as SC
    rows=[{'id':'C1','title':'Ranked paper','stage':'awaiting_ta'}, {'id':'C2','title':'Uploaded paper','stage':'awaiting_ta','pdf_uploaded_at':'2026-11-12T00:00:00Z'}]
    monkeypatch.setattr(S,'collect',lambda root:{'candidates':rows,'searches':[],'reasons':{},'stageLabels':{}})
    monkeypatch.setattr(S,'load_candidates',lambda *a:rows)
    monkeypatch.setattr(S,'load_strategies',lambda:{})
    monkeypatch.setattr(SC,'load_abstracts',lambda:{})
    monkeypatch.setattr(SC,'rank_order',lambda *a:(['C1','C2'],{'ranked':True}))
    bundle=B.screening_bundle(tmp_path,ta_limit=1)
    assert [c['id'] for c in bundle['candidates']]==['C2']
    assert bundle['candidates'][0]['pdf_uploaded_at']=='2026-11-12T00:00:00Z'
