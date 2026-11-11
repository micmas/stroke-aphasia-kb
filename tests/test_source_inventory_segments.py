import json,sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_inventory_segments as s


def text():
    return ''.join(f'=== PAGE {p} ===\n'+''.join('The association was not significant.\n' for _ in range(180)) for p in range(1,6))


def answer(prompt):
    import re
    key=re.search(r'CORE: \["([^"]+)',prompt).group(1)
    return {'citation':'@Test','outcomes':['naming'],'analyses':[{'id':'a1','outcome':'naming',
      'outcome_timing':'current level','method':'correlation','predictors':[],'selected_predictors':[],
      'covariates':[],'result':'No association detected','estimates':[],
      'evidence':[{'source_id':key,'quote':'The association was not significant.'}],'uncertainties':[]}],
      'discrepancies':[],'coverage_notes':[]}


def test_every_core_unit_once_and_context_is_original():
    units=s.source_units(text());plan=s.plan_segments(units,10000)
    ids=[k for part in plan for k in part['core_ids']]
    assert ids==list(units) and len(set(ids))==len(ids)
    assert len(plan)>1
    for part in plan:
        prompt,subset=s.segment_prompt(units,'@Test',part)
        assert all(subset[k]==units[k] for k in subset)
        assert set(part['core_ids']).isdisjoint(part['context_ids'])
        assert 'CONTEXT:' in prompt and 'not the full paper' in prompt


def test_merge_keeps_all_records_and_original_source_ids(tmp_path,monkeypatch):
    monkeypatch.setattr(s,'_extract_pdf_text',lambda p:(text(),5))
    prompts=[]
    def chat(prompt,**kw):
        prompts.append(prompt);return {'text':json.dumps(answer(prompt)), 'truncated_output':False}
    monkeypatch.setattr(s,'chat',chat)
    pdf=tmp_path/'p.pdf';pdf.write_bytes(b'pdf');out=tmp_path/'A'
    assert s.run_segmented(pdf,'@Test',out,'model',32000,10000)==0
    raw=json.loads((out/'raw.json').read_text());meta=json.loads((out/'meta.json').read_text())
    assert len(raw['analyses'])==len(prompts)>1
    assert len({a['id'] for a in raw['analyses']})==len(prompts)
    assert meta['status']=='requires_review' and meta['approved'] is False
    assert meta['coverage']['core_units_processed']==len(s.source_units(text()))
    with pytest.raises(FileExistsError):s.run_segmented(pdf,'@Test',out,'model',32000,10000)


def test_failed_segment_never_publishes_aggregate(tmp_path,monkeypatch):
    monkeypatch.setattr(s,'_extract_pdf_text',lambda p:(text(),5))
    monkeypatch.setattr(s,'chat',lambda *a,**kw:{'text':'partial','truncated_output':True})
    pdf=tmp_path/'p.pdf';pdf.write_bytes(b'pdf');out=tmp_path/'A'
    with pytest.raises(ValueError,match='Truncated'):s.run_segmented(pdf,'@Test',out,'model',32000,10000)
    assert not (out/'raw.json').exists()
    assert (out/'segments/001/raw.json').read_text()=='partial'
    assert json.loads((out/'meta.json').read_text())['status']=='failed'


def test_empty_non_substantive_segment_kept_for_review(tmp_path,monkeypatch):
    monkeypatch.setattr(s,'_extract_pdf_text',lambda p:(text(),5));calls=[]
    def chat(prompt,**kw):
        calls.append(prompt)
        data=answer(prompt) if len(calls)==1 else {'citation':'@Test','outcomes':[], 'analyses':[], 'discrepancies':[], 'coverage_notes':['References only; verify this disposition.']}
        return {'text':json.dumps(data)}
    monkeypatch.setattr(s,'chat',chat)
    pdf=tmp_path/'p.pdf';pdf.write_bytes(b'pdf');out=tmp_path/'A'
    s.run_segmented(pdf,'@Test',out,'model',32000,10000)
    assert json.loads((out/'meta.json').read_text())['empty_segments_requiring_review']
