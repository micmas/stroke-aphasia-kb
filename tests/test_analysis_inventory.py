import json
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import extract_analysis_inventory as inventory

TEXT='=== PAGE 1 ===\nThe association was not significant.\n=== PAGE 2 ===\nThe adjusted association was positive.\n'


def result():
    return {'citation':'@Example2020','outcomes':['naming'], 'analyses':[
        {'id':'a1','outcome':'naming','outcome_timing':'current level','method':'regression',
         'predictors':['volume'],'selected_predictors':[],'covariates':[],
         'result':'not significant','estimates':[],'uncertainties':[],
         'evidence':[{'source_id':'P1-S1','quote':'The association was not significant.'}]}],
        'discrepancies':[],'coverage_notes':[]}


def test_source_units_preserve_pages_and_text():
    units=inventory.source_units(TEXT)
    assert units['P1-S1']['page']==1
    assert units['P2-S1']['page']==2
    assert 'The association was not significant.' in units['P1-S1']['text']
    long=''.join(f'Line {i} with words.\n' for i in range(500))
    units=inventory.source_units('=== PAGE 1 ===\n'+long)
    for line in long.splitlines(): assert any(line in u['text'] for u in units.values())


def test_wrong_source_changed_negation_and_missing_outcome_are_reported():
    units=inventory.source_units(TEXT); data=result()
    assert inventory.audit_inventory(data,units,'@Example2020')==[]
    data['analyses'][0]['evidence'][0]['source_id']='P2-S1'
    assert any('not exact' in x for x in inventory.audit_inventory(data,units,'@Example2020'))
    data=result();data['analyses'][0]['evidence'][0]['quote']='The association was significant.'
    assert any('not exact' in x for x in inventory.audit_inventory(data,units,'@Example2020'))
    data=result();data['outcomes'].append('comprehension')
    assert any('no analysis' in x for x in inventory.audit_inventory(data,units,'@Example2020'))


def test_failure_keeps_raw_and_metadata_and_refuses_overwrite(tmp_path,monkeypatch):
    monkeypatch.setattr(inventory,'_extract_pdf_text',lambda _: (TEXT,2))
    monkeypatch.setattr(inventory,'chat',lambda *a,**kw: {'text':'bad JSON'})
    pdf=tmp_path/'paper.pdf';pdf.write_bytes(b'fixture');out=tmp_path/'run'
    with pytest.raises(ValueError): inventory.run(pdf,'@Example2020',out,'test')
    assert (out/'raw.json').read_text()=='bad JSON'
    assert json.loads((out/'meta.json').read_text())['status']=='failed'
    with pytest.raises(FileExistsError): inventory.run(pdf,'@Example2020',out,'test')
    assert pdf.read_bytes()==b'fixture'


def test_truncated_run_is_preserved_without_selective_retry(tmp_path,monkeypatch):
    monkeypatch.setattr(inventory,'_extract_pdf_text',lambda _: (TEXT,2))
    calls=[]
    def truncated(*args,**kwargs):
        calls.append(kwargs)
        return {'text':json.dumps(result()),'truncated_output':True}
    monkeypatch.setattr(inventory,'chat',truncated)
    pdf=tmp_path/'paper.pdf';pdf.write_bytes(b'fixture');out=tmp_path/'run'
    with pytest.raises(ValueError,match='Truncated'):inventory.run(pdf,'@Example2020',out,'test')
    assert len(calls)==1
    assert json.loads((out/'raw.json').read_text())==result()
    assert json.loads((out/'meta.json').read_text())['status']=='failed'


def test_empty_source_does_not_call_model(tmp_path,monkeypatch):
    monkeypatch.setattr(inventory,'_extract_pdf_text',lambda _: ('=== PAGE 1 ===\n',1))
    def forbidden(*args,**kwargs):raise AssertionError('Model must not run')
    monkeypatch.setattr(inventory,'chat',forbidden)
    with pytest.raises(ValueError,match='No extractable'):inventory.run(tmp_path/'x.pdf','@X2020',tmp_path/'run','test')


def test_larger_output_budget_reaches_transport_context_and_metadata(tmp_path,monkeypatch):
    monkeypatch.setattr(inventory,'_extract_pdf_text',lambda _: (TEXT,2))
    calls=[]
    def complete(prompt,**kwargs):
        calls.append((prompt,kwargs))
        return {'text':json.dumps(result()),'truncated_output':False}
    monkeypatch.setattr(inventory,'chat',complete)
    pdf=tmp_path/'paper.pdf';pdf.write_bytes(b'fixture');out=tmp_path/'run'
    assert inventory.run(pdf,'@Example2020',out,'test',max_tokens=20000)==0
    prompt,options=calls[0]
    assert options['max_tokens']==20000
    assert options['num_ctx']==inventory._autosize_num_ctx(prompt,20000)
    assert json.loads((out/'meta.json').read_text())['max_output_tokens']==20000
    with pytest.raises(ValueError,match='positive'):
        inventory.run(pdf,'@Example2020',tmp_path/'invalid','test',max_tokens=0)
    assert not (tmp_path/'invalid').exists()
