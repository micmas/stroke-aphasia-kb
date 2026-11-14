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


def relationship_result():
    data = result()
    data.update(schema_version='relationships-v1', approved=False,
                study={**{k:'not_reported' for k in ['design','population','sample','timing','setting','eligibility','limitations']},
                       'evidence':data['analyses'][0]['evidence']},
                relationship_coverage=[{'source_id':'P1-S1','status':'null_summary',
                                        'analysis_ids':['a1'],'reason':'Tested naming association was null'}])
    row = data['analyses'][0]
    row.update(relationship_type='association', evidence_origin='current_study',
               applicability='not_reported', factors=[{'name':'volume','kind':'imaging',
               'role':'tested_predictor','measurement':'volume','hemisphere':'not_reported',
               'spatial_reference':'not_reported','mapping_basis':'directly_measured',
               'evidence':row['evidence']}], result_status='not_detected',
               scope_limits=['Not proof of no association'])
    return data


def test_relationship_role_and_provenance_guards():
    units = inventory.source_units(TEXT)
    data = relationship_result()
    assert inventory.audit_inventory(data,units,'@Example2020',profile='relationships') == []
    # Adjustment alone must not be packaged as a tested outcome relationship.
    data['analyses'][0]['factors'][0]['role'] = 'adjustment_only'
    assert any('no tested' in x for x in inventory.audit_inventory(data,units,'@Example2020','relationships'))
    data = relationship_result()
    data['analyses'][0]['factors'][0]['mapping_basis'] = 'extractor_inferred_disconnectome'
    data['analyses'][0]['factors'][0]['evidence'] = [{'source_id':'P2-S1','quote':'The association was not significant.'}]
    data['relationship_coverage'][0]['analysis_ids'] = ['missing']
    issues = inventory.audit_inventory(data,units,'@Example2020','relationships')
    assert any('cannot be invented' in x for x in issues)
    assert any('evidence not exact' in x for x in issues)
    assert any('unknown analysis' in x for x in issues)
    data = relationship_result()
    data['analyses'][0]['relationship_type'] = 'longitudinal_prediction'
    assert any('validation scope required' in x for x in inventory.audit_inventory(data,units,'@Example2020','relationships'))


def test_relationship_profile_dispatches_to_literal_evidence(tmp_path, monkeypatch):
    import relationship_evidence
    calls=[]
    monkeypatch.setattr(relationship_evidence, 'run_evidence', lambda *args: calls.append(args) or 1)
    pdf=tmp_path/'paper.pdf';out=tmp_path/'run'
    assert inventory.run(pdf,'@Example2020',out,'test',profile='relationships') == 1
    assert calls == [(pdf, '@Example2020', out, 'test', 10000)]
    assert not out.exists()


def test_relationship_source_checklist_does_not_accept_model_completeness_claim():
    from relationship_inventory import review_checklist
    units={'P7-S2':{'page':7,'text':'Age and time post-onset were not significantly related to language scores.'}}
    data={'analyses':[{'id':'a1','evidence':[{'source_id':'P7-S2','quote':'language scores'}]}],
          'coverage_notes':['Everything extracted']}
    rows=review_checklist(data,units)
    assert rows[0]['cues']==['personal_or_clinical_factor_passage','null_or_qualification_passage']
    assert rows[0]['analyses_citing_unit']==['a1']
    assert rows[0]['status']=='source_review_required'


def test_focused_pass_preserves_valid_shared_nulls_but_flags_model_performance():
    from relationship_inventory import audit_focused_pass
    source = {'S1': {'text': 'Age and time post-onset were not significantly related (p > 0.05).'},
              'S2': {'text': 'The demographic model predicted scores with R2 = 0.01.'}}
    rows = [{'factors': [factor], 'direction': 'not_detected', 'correction': 'not_reported',
             'evidence': [{'source_id': 'S1', 'quote': source['S1']['text']}]}
            for factor in ('age', 'time_since_stroke')]
    assert audit_focused_pass({'findings': rows, 'dispositions': [{'source_id': key} for key in source]}, source, 'factors') == []
    rows.append({'factors': ['age'], 'evidence': [{'source_id': 'S2', 'quote': source['S2']['text']}]})
    assert any('Whole-model performance' in f['reason']
               for f in audit_focused_pass({'findings': rows}, source, 'factors'))


def test_focused_pass_flags_direction_without_turning_strong_correlation_into_positive():
    from relationship_inventory import audit_focused_pass
    quote = 'Lesion volume correlated strongly with tract metrics (p < 0.05).'
    row = {'factors': ['lesion_burden'], 'direction': 'positive',
           'evidence': [{'source_id': 'S1', 'quote': quote}]}
    flags = audit_focused_pass({'findings': [row]}, {'S1': {'text': quote}}, 'factors')
    assert any('Direction' in f['reason'] for f in flags)
    assert row['direction'] == 'positive'  # Original output remains unchanged.


def test_focused_context_keeps_excluded_subset_visible():
    from relationship_inventory import audit_focused_pass
    source = {'S1': {'text': 'We trained using 270 records.'},
              'S2': {'text': 'CYCLE scores are presented for n = 31.'}}
    data = {'selected': [], 'excluded': [{'source_id': 'S1'}, {'source_id': 'S2'}]}
    flags = audit_focused_pass(data, source, 'context')
    assert {f['path'] for f in flags} == {'excluded.0', 'excluded.1'}
    assert all('retain for review' in f['reason'] for f in flags)


def test_compact_registry_rejects_unknown_features_and_changed_quote():
    from relationship_inventory import audit_compact
    units = inventory.source_units(TEXT)
    evidence = [{'source_id':'P1-S1','quote':'The association was not significant.'}]
    data = {'schema_version':'relationships-v2','citation':'Example2020','approved':False,
        'features':[], 'unresolved':[], 'analyses':[{'id':'a1','method':'correlation',
        'relationship_type':'association','evidence_origin':'current_study','context_source_ids':[],
        'inputs':[],'adjustments':[],'explicit_non_adjustments':[],'evidence':evidence,
        'validation':{'design':'not_applicable',**{k:[] for k in ['training_source_ids','evaluation_source_ids','overlap_source_ids','selection_source_ids']}},
        'scope_limits':[], 'results':[{'id':'r1','feature_ids':[],'outcomes':['naming'],'context_source_ids':[],
        'outcome_timing':'current_level','effect_unit':'joint_model','comparison':'not_applicable',
        'status':'not_detected','direction':'not_applicable','correction':'not_reported',
        'estimates':[],'evidence':evidence,'table_locator':'not_applicable'}]}]}
    assert audit_compact(data,units)==[]
    data['analyses'][0]['inputs']=['missing']
    assert any('unknown feature ID' in x for x in audit_compact(data,units))
    evidence[0]['quote']='The association was significant.'
    assert any('quote not exact' in x for x in audit_compact(data,units))


def test_pdf_soft_hyphens_do_not_hide_changed_negation_or_numeric_sign():
    from annotate_paper import _normalize
    assert _normalize('corre\u00ad sponding') == _normalize('corresponding')
    assert _normalize('not related') != _normalize('related')
    assert _normalize('r = -0.5') != _normalize('r = 0.5')
