"""Safety boundaries for model source checks, not an accuracy benchmark."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_check_relationships as check

class SourceCheckTests(unittest.TestCase):
    def test_conversion_holds_borrowed_statistics_even_after_model_acceptance(self):
        result=copy.deepcopy(self.result)
        result['passages']=[{'source_id':'methods','supports':'statistics'}]
        before=copy.deepcopy(result)
        unit={'evidence_ids':['performance'],'qualifier_ids':['qualified_result']}
        held=check.statistics_scope_gate(result,unit)
        self.assertEqual(held['decision'],'hold')
        self.assertIsNone(held['entry'])
        self.assertIn('Human source confirmation',held['reason'])
        self.assertEqual(result,before)
        for sid in ['performance','qualified_result']:
            result['passages'][0]['source_id']=sid
            self.assertEqual(check.statistics_scope_gate(result,unit)['decision'],'supported')
        result['passages']=[{'source_id':'methods','supports':'method'}]
        self.assertEqual(check.statistics_scope_gate(result,unit)['decision'],'supported')

    def test_uncertainty_outside_selected_passage_does_not_contaminate_it(self):
        from source_prose_images import reading_value
        original='Participants were 55 adults with aphasia after stroke.'
        clean=reading_value(original,original+' Next sentence [ILLEGIBLE]')
        self.assertEqual(clean['uncertainties'],[])
        self.assertNotIn('Next',clean['transcription'])
        inside=reading_value(original,'Participants were 55 [ILLEGIBLE] adults with aphasia after stroke.')
        self.assertTrue(inside['uncertainties'])
        boundary=reading_value(original,'[ILLEGIBLE] were 55 adults with aphasia after stroke.')
        self.assertTrue(boundary['uncertainties'])

    def test_empty_limitations_citation_never_licenses_an_uncited_claim(self):
        from source_check_facets import evaluate_analysis
        item={'source_facts':'Result','source_ids':['result'],'proposed_field_meaning':'result','explanation':'fits','compatibility':'fits'}
        answer={k:copy.deepcopy(item) for k in ['direction','statistics','limitations','current_study']}
        answer['controls']=[];answer['limitations']['source_ids']=[]
        checks,issues=evaluate_analysis(answer,[],{'result'},limitations_listed=False)
        self.assertFalse(issues)
        self.assertEqual(checks['limitations'],'supported')
        with self.assertRaises(ValueError):evaluate_analysis(answer,[],{'result'},limitations_listed=True)
        answer['limitations']['compatibility']='conflict'
        with self.assertRaises(ValueError):evaluate_analysis(answer,[],{'result'},limitations_listed=False)
        answer['limitations']['compatibility']='fits';answer['limitations']['source_ids']=['invented']
        with self.assertRaises(ValueError):evaluate_analysis(answer,[],{'result'},limitations_listed=False)

    def test_bounding_wrapped_words_discards_neighbouring_invented_statistics(self):
        from source_prose_images import bounded_transcription,agreed_passage
        original='This overall best per-\nforming model correctly classified 51/55 participants as responders and nonresponders to language treat-\nment.'
        extra='Other result P<0.001. '+original+' Adjacent range 0.814 to 0.833.'
        bounded=bounded_transcription(original,extra)
        self.assertNotIn('0.001',bounded)
        self.assertNotIn('0.814',bounded)
        self.assertIn('51/55',bounded)
        self.assertIsNotNone(agreed_passage(original,[{'transcription':bounded,'uncertainties':[]}]*2))

    def test_named_atlas_ownership_is_explicitly_checked(self):
        from source_check_facets import analysis_controls
        result=copy.deepcopy(self.result)
        result['entry']['findings'][0]['imaging_details']={'atlases_used':['Atlas A','Atlas B']}
        assertions=analysis_controls(result)
        atlas_assertions=[a for a in assertions if a['variable'].startswith('atlas ')]
        self.assertEqual(len(atlas_assertions),2)
        self.assertTrue(all(a['claimed_use']=='controlled' for a in atlas_assertions))

    def test_image_word_boundaries_accept_wrapped_words_without_merging_signs(self):
        from source_prose_images import agreed_passage
        original='In\u00ad\nclusion criteria were accuracy>70% on test.'
        values=[{'transcription':'Inclusion criteria were accuracy>70% on test.','uncertainties':[]} for _ in range(2)]
        self.assertIsNotNone(agreed_passage(original,values))
        values[1]['transcription']='Inclusion criteria were accuracy>=70% on test.'
        self.assertIsNone(agreed_passage(original,values))

    def test_pdf_furniture_exclusion_preserves_body_numbers_and_ambiguous_matches(self):
        import pymupdf
        from source_pdf_layout import furniture,locate
        with pymupdf.open() as document:
            for i in range(3):
                page=document.new_page()
                page.insert_text((40,30),'A. Example et al.')
                page.insert_text((40,120),'Participants had >70% accuracy.')
                page.insert_text((40,300),'Fig. 1.')
                page.insert_text((280,820),str(i+1))
            original='Participants had >70% accuracy.\nA. Example et al.'
            found=locate(document,1,original,furniture(document))
            self.assertEqual(found['original_text'],original)
            self.assertEqual(found['anchor_text'],'Participants had >70% accuracy.')
            self.assertEqual(found['excluded_fragments'][0]['text'],'A. Example et al.')
            caption=locate(document,1,'Participants had >70% accuracy.\nFig. 1.',furniture(document))
            self.assertEqual(caption['excluded_fragments'],[])
            document[0].insert_text((40,180),'A. Example et al.')
            ambiguous=locate(document,1,original,furniture(document))
            self.assertEqual(ambiguous['excluded_fragments'],[])

    def test_correction_and_borrowed_statistics_require_individual_answers(self):
        from source_check_facets import analysis_controls,evaluate_analysis
        result=copy.deepcopy(self.result)
        finding=result['entry']['findings'][0]
        finding['confounders_controlled']=[];finding['confounders_not_controlled']=[]
        finding['lesion_mapping']={'multiple_comparisons':'fwe'}
        result['passages']=[{'source_id':'methods','supports':'statistics'}]
        assertions=analysis_controls(result,{'analysis_label':'ROI correlation','evidence_ids':['roi']})
        self.assertEqual(len(assertions),2)
        item={'source_facts':'ROI result','source_ids':['roi'],'proposed_field_meaning':'test','explanation':'fits','compatibility':'fits'}
        answer={key:copy.deepcopy(item) for key in ['direction','statistics','limitations','current_study']}
        answer['controls']=[{'index':a['index'],'source_facts':'Correction used for voxel selection only','source_ids':['methods'],'observed_use':'only_other_analysis'} for a in assertions]
        checks,issues=evaluate_analysis(answer,assertions,{'roi','methods'})
        self.assertEqual(checks['adjustment'],'contradicted')
        self.assertEqual(len(issues),2)
        answer['controls'].pop()
        with self.assertRaises(ValueError):evaluate_analysis(answer,assertions,{'roi','methods'})

    def test_mapper_decoder_rejects_unknown_sources_and_evidence_roles(self):
        import jsonschema
        result=copy.deepcopy(self.result)
        result['passages']=[{'source_id':'allowed','supports':'sample'}]
        schema=check.mapper_schema('[SOURCE allowed] original text [/SOURCE allowed]')
        jsonschema.validate(result,schema)
        result['passages'][0]['source_id']='invented'
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(result,schema)
        result['passages'][0]={'source_id':'allowed','supports':'outcome_timing'}
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(result,schema)

    def test_facet_cache_requires_identical_question_binding_and_intact_response(self):
        import tempfile,json,hashlib
        from source_check_facets import cached_facet
        with tempfile.TemporaryDirectory() as directory:
            unit=Path(directory);old=unit/'attempt-1/facets';new=unit/'attempt-2/facets'
            old.mkdir(parents=True);new.mkdir(parents=True)
            raw='{"answer": true}';binding={'pdf':'same','model':'same'}
            (old/'concept-raw.json').write_text(raw)
            (old/'concept-prompt.txt').write_text('question')
            (old/'concept-meta.json').write_text(json.dumps({'binding':binding,'raw_sha256':hashlib.sha256(raw.encode()).hexdigest(),'inference':{}}))
            schema={'type':'object','required':['answer']}
            self.assertEqual(cached_facet(new,'concept','question',binding,schema)['duration_s'],0)
            self.assertIsNone(cached_facet(new,'concept','different',binding,schema))
            self.assertIsNone(cached_facet(new,'concept','question',{'pdf':'changed','model':'same'},schema))
            (old/'concept-raw.json').write_text('{"answer": false}')
            self.assertIsNone(cached_facet(new,'concept','question',binding,schema))

    def test_image_math_formatting_does_not_hide_numeric_disagreement(self):
        from source_prose_images import canonical
        self.assertEqual(canonical(r'P<0.05; 0.2 cm3'),canonical(r'$P<0.05$; $0.2\text{ cm}^3$'))
        self.assertEqual(canonical(r'P ≤ 0.001'),canonical(r'$P \le 0.001$'))
        self.assertEqual(canonical(r'P ≥ 0.001'),canonical(r'$P \geq 0.001$'))
        self.assertNotEqual(canonical(r'P < 0.001'),canonical(r'$P \le 0.001$'))
        self.assertNotEqual(canonical(r'P<0.05; 0.2 cm3'),canonical(r'$P<=0.05$; $0.2\text{ cm}^3$'))
        self.assertNotEqual(canonical(r'0.2 cm3'),canonical(r'$0.2\text{ cm}^2$'))

    def test_summary_only_timing_and_missing_eligibility_require_repair(self):
        from source_check_facets import population_checks
        value={'compatibility':'fits','explanation':'Median is chronic','source_ids':['timing'],
               'phase_basis':'summary_only','missing_material_eligibility':['Digit span at least two']}
        result=copy.deepcopy(self.result);result['entry']['findings'][0]['sample']={'phase':'chronic'}
        checks,issues=population_checks(value,result)
        self.assertEqual(checks['timing'],'contradicted')
        self.assertEqual(checks['population'],'contradicted')
        result['entry']['findings'][0]['sample']['phase']='not_reported'
        value['missing_material_eligibility']=[]
        checks,issues=population_checks(value,result)
        self.assertFalse(issues)

    def test_statistics_cannot_borrow_uncited_table_numbers_or_flip_sign(self):
        result=copy.deepcopy(self.result)
        result['passages']=[{'source_id':'methods','supports':'statistics','quote':'P < .05; extent 25 voxels.'}]
        evidence={'methods_context_candidate_ids':['methods'],'passages':[{'evidence_id':'methods','classifications':{}}]}
        result['entry']['findings'][0]['statistics']={'threshold':'P < 0.05; extent 25 voxels'}
        check.validate_statistic_numbers(result,evidence)
        result['entry']['findings'][0]['statistics']={'threshold':'P ≤ 0.05', 'effect_size':'r = −0.32'}
        result['passages'][0]['quote']='P ≤ 0.05; r = −0.32'
        check.validate_statistic_numbers(result,evidence)
        result['entry']['findings'][0]['statistics']={'threshold':'P < 0.05; extent 25 voxels'}
        result['passages'][0]['quote']='P < .05; extent 25 voxels.'
        check.validate_unit_sources(result,{'analysis_label':'Analysis 1','evidence_ids':['claim']},evidence)
        result['entry']['findings'][0]['statistics']['effect_size']='Z = 5.86–7.84'
        with self.assertRaisesRegex(ValueError,'absent'):check.validate_statistic_numbers(result,evidence)
        result['entry']['findings'][0]['statistics']={'effect_size':'r = .32'}
        result['passages'][0]['quote']='r = −.32'
        with self.assertRaisesRegex(ValueError,'absent'):check.validate_statistic_numbers(result,evidence)

    def test_table_hints_reconcile_formatting_without_losing_sign_or_laterality(self):
        from source_check_facets import table_context
        a={'row_index':2,'column_index':3,'row_occurrence':1,'row_path':['Left tract'],
           'column_path':['Adjusted ORª (0.95-CI)'],'raw':'3.97 (1.02–15.46)'}
        b={**a,'column_path':['Adjusted ORa','(0.95-CI)']}
        def hints(x,y):
            return table_context({'tables':[{'table_id':'T1','facts':[{'source_A':x,'source_B':y}]}]})[0]
        matched=hints(a,b)
        self.assertEqual(len(matched['agreed_readings']),1)
        self.assertFalse(matched['approved'])
        self.assertEqual(matched['agreed_readings'][0]['reading_A']['raw'],a['raw'])
        self.assertFalse(hints(a,{**b,'row_path':['Right tract']})['agreed_readings'])
        self.assertFalse(hints({**a,'raw':'-.32'},{**b,'raw':'.32'})['agreed_readings'])
        self.assertFalse(hints(a,None)['agreed_readings'])

    def test_scoped_context_keeps_remote_methods_nearby_results_and_caveats(self):
        def row(sid,unit,text,**kw):
            return {'evidence_id':sid,'source':{'source_id':unit,'page':1,'text':text},'classifications':{},**kw}
        evidence={'methods_context_candidate_ids':['method'], 'passages':[
            row('claim','results','An association was found.',context_unit_ids=['following']),
            row('adjusted','following','It was absent after adjustment.'),
            row('method','methods','All models controlled age.'),
            row('caveat','discussion','No independent validation.',contains_limitation=True),
            row('table','table','Flattened cells must not become prose.',classifications={'A':'table_or_figure'}),
            row('prior','intro','An earlier study found another effect.')
        ]}
        result={'passages':[{'source_id':'claim','page':1,'quote':'An association was found.'}]}
        text=check.scoped_source_document(result,evidence)
        for sid in ['claim','adjusted','method','caveat']:self.assertIn('[SOURCE '+sid+']',text)
        self.assertNotIn('Flattened cells',text)
        self.assertNotIn('An earlier study',text)
        with self.assertRaisesRegex(ValueError,'identifiable source'):check.scoped_source_document({'passages':[]},evidence)

    def test_image_agreement_preserves_scientific_symbols(self):
        from source_prose_images import canonical
        self.assertEqual(canonical('range 12–74 months.\nAt least ≤12'),canonical('range 12-74 months At least <=12'))
        for a,b in [('>1','41'),('>1','>=1'),('.05','.5'),('−.32','.32'),('12–74','12–47'),('12-\n74','1274')]:
            self.assertNotEqual(canonical(a),canonical(b))

    def test_image_agreement_requires_complete_target_and_preserves_numbers(self):
        from source_prose_images import agreed_passage
        original='Methods. We studied 41 month survivors using structural images.'
        good='Methods. We studied >1 month survivors using structural images.'
        def readings(a,b):return [{'transcription':a,'uncertainties':[]},{'transcription':b,'uncertainties':[]}]
        self.assertEqual(agreed_passage(original,readings(good,good+' Next sentence.')),good)
        self.assertIsNone(agreed_passage(original,readings('Methods.','Methods.')))
        self.assertIsNone(agreed_passage(original,readings(good,good.replace('>1','>=1'))))
        self.assertIsNone(agreed_passage(original,readings(good,good.replace('>1','41'))))

    def test_source_identity_and_control_ownership_cannot_be_pooled(self):
        from source_check_facets import evaluate_analysis
        unit={'analysis_label':'primary','evidence_ids':['primary'],'qualifier_ids':['method']}
        with self.assertRaisesRegex(ValueError,'outside the selected analysis'):
            check.validate_unit_sources({'decision':'supported','passages':[{'source_id':'sensitivity','supports':'claim'}]},unit)
        good={'source_facts':'Primary result','source_ids':['primary'],'proposed_field_meaning':'same','explanation':'same','compatibility':'fits'}
        value={k:good for k in ['direction','statistics','limitations','current_study']}
        value['controls']=[{'index':0,'source_facts':'Age used only in sensitivity','source_ids':['primary'],'observed_use':'only_other_analysis'}]
        checks,issues=evaluate_analysis(value,[{'index':0,'variable':'age','claimed_use':'controlled'}],{'primary'})
        self.assertEqual(checks['adjustment'],'contradicted')
        self.assertEqual(checks['direction'],'supported')
        self.assertEqual(len(issues),1)
        value['controls']=[]
        with self.assertRaisesRegex(ValueError,'omitted'):
            evaluate_analysis(value,[{'index':0,'variable':'age','claimed_use':'controlled'}],{'primary'})

    def test_failed_image_reader_holds_source_without_failing_paper(self):
        import tempfile
        from unittest.mock import patch
        import pymupdf
        import source_prose_images as images
        import review_dual_extract
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);pdf=root/'paper.pdf'
            doc=pymupdf.open();page=doc.new_page();page.insert_text((72,72),'There were 12 patients.');doc.save(pdf);doc.close()
            evidence={'passages':[{'evidence_id':'P1-C1','source':{'page':1,'text':'There were 12 patients.'},'classifications':{'A':'population_or_timing'}}]}
            with patch.object(review_dual_extract,'identities',return_value={}),patch.object(review_dual_extract,'model_identity',side_effect=lambda m,t:m),patch.object(images,'chat',side_effect=RuntimeError('reader unavailable')):
                result=images.prepare(pdf,evidence,root/'images',['a','b'],['a','b'],'http://localhost:11434')
            self.assertEqual(result['P1-C1']['status'],'held')
            self.assertNotIn('transcription',result['P1-C1'])
            self.assertEqual(result['P1-C1']['original_text'],'There were 12 patients.')
            self.assertTrue((root/'images/P1-C1/error-1.json').exists())

    def test_checker_echo_of_exclusion_never_creates_supported_mapping(self):
        import tempfile,json
        from types import SimpleNamespace
        from unittest.mock import patch
        result=copy.deepcopy(self.result);result.update(decision='exclude',entry=None)
        audit={'verdict':'exclude','checks':{k:'not_applicable' for k in check.AUDIT_CHECKS},'issues':[]}
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(check,'chat',return_value={'text':json.dumps(audit)}):
                returned=check.semantic_check(result,self.pages,{'passages':[]},SimpleNamespace(checker_model='test',host='http://localhost:11434'),Path(tmp),{})
            self.assertEqual(returned['verdict'],'accept')
            self.assertEqual(result['decision'],'exclude')
            self.assertIsNone(result['entry'])
            self.assertTrue((Path(tmp)/'semantic-normalization.json').exists())

    def test_consolidation_cannot_lose_repeat_or_invent_candidates(self):
        units=[{'id':'U1'},{'id':'U2'},{'id':'U3'}]
        check.validate_groups([['U1','U2'],['U3']],units)
        for groups in [[['U1','U2']],[['U1','U2'],['U2','U3']],[['U1','U2'],['U4']],[[],['U1','U2','U3']]]:
            with self.assertRaises(ValueError):check.validate_groups(groups,units)

    def test_consolidation_preserves_qualifiers_and_original_candidates(self):
        units={'U1':{'id':'U1','evidence_ids':['a'],'qualifier_ids':['null']},
               'U2':{'id':'U2','evidence_ids':['b'],'qualifier_ids':['adjusted'],'outcome':{'text':'different?'}}}
        merged=check.consolidated_unit(['U1','U2'],units)
        self.assertEqual(merged['evidence_ids'],['a','b'])
        self.assertEqual(merged['qualifier_ids'],['null','adjusted'])
        self.assertEqual(merged['related_candidates'],[units['U2']])
        self.assertEqual(units['U1']['evidence_ids'],['a'])

    def test_incomplete_or_invalid_groups_preserve_every_candidate(self):
        units=[{'id':'U1'},{'id':'U2'},{'id':'U3'}]
        groups,notes=check.complete_groups([['U1','U2']],units)
        self.assertEqual(groups,[['U1','U2'],['U3']])
        self.assertTrue(notes)
        for bad in [[['U1','U2'],['U2','U3']],[['U1','unknown']]]:
            groups,notes=check.complete_groups(bad,units)
            self.assertEqual(groups,[['U1'],['U2'],['U3']])
            self.assertTrue(notes)

    def test_marked_paper_keeps_all_text_with_overlapping_sources(self):
        import re
        pages=['Before. The cohort had twenty people. After.', 'Unindexed page.']
        evidence={'passages':[
            {'evidence_id':'a','source':{'page':1,'text':'The cohort had twenty people.'}},
            {'evidence_id':'b','source':{'page':1,'text':'twenty people.'}}]}
        text=check.source_document(pages,evidence)
        stripped=re.sub(r'\[/?SOURCE [^]]+\]','',text)
        self.assertEqual(stripped,'PDF PAGE 1\n'+pages[0]+'\nPDF PAGE 2\n'+pages[1])
        self.assertIn('[SOURCE b]',text)

    def test_timing_effect_size_and_analysis_conflicts_are_rejected(self):
        r=copy.deepcopy(self.result);f=r['entry']['findings'][0]
        f['statistics']['effect_size']='P<0.001'
        with self.assertRaisesRegex(ValueError,'not an effect size'):check.validate_decision(r,self.pages)
        del f['statistics']['effect_size']
        self.pages[0]+=' Participants were at least 6 months after stroke.'
        r['passages']=[{'page':1,'quote':self.pages[0],'supports':s} for s in ['claim','sample','method','statistics']]
        f['sample']={'time_post_onset':'6 months'}
        with self.assertRaisesRegex(ValueError,'lower bound'):check.validate_decision(r,self.pages)
        f['sample']['time_post_onset']='at least 6 months'
        f['lesion_mapping']={'lesion_volume_correction':'covariate'}
        f['notes']='Including lesion volume reduced the significance.'
        with self.assertRaisesRegex(ValueError,'Adjustment changes'):check.validate_decision(r,self.pages)
        f['statistics']['threshold']='Adjusted for lesion volume: voxel p < .05'
        check.validate_decision(r,self.pages)

    def test_identical_claim_is_flagged_not_merged(self):
        r=copy.deepcopy(self.result);r['entry']['findings'][0]['claim']='The same finding.'
        self.assertEqual(check.duplicate_claim(r,{'the same finding':'U025'}),'U025')
        self.assertIsNone(check.duplicate_claim(r,{'a different finding':'U025'}))

    def setUp(self):
        self.pages=['The primary cohort included twenty participants. The association was not significant after adjustment.']
        self.result={'decision':'supported','reason':'Fixture','checks':{k:'supported' for k in check.CHECKS},
            'needs_visual_check':False,'bucket':'regions','entry':{'kind':'network','findings':[{'target':'anomia','statistics':{'threshold':'p<.05'}}]},
            'passages':[{'page':1,'quote':self.pages[0],'supports':s} for s in ['claim','sample','method','statistics']]}
    def test_literal_evidence_required_on_correct_page(self):
        check.validate_decision(self.result,self.pages)
        for alteration in [{'page':2},{'quote':'Invented significant association.'}]:
            r=copy.deepcopy(self.result);r['passages'][0].update(alteration)
            with self.assertRaises(ValueError):check.validate_decision(r,self.pages)
    def test_visual_or_unclear_checks_cannot_be_supported(self):
        r=copy.deepcopy(self.result);r['needs_visual_check']=True
        with self.assertRaises(ValueError):check.validate_decision(r,self.pages)
        r=copy.deepcopy(self.result);r['checks']['timing']='unclear'
        with self.assertRaises(ValueError):check.validate_decision(r,self.pages)
    def test_hold_cannot_smuggle_a_draft(self):
        r=copy.deepcopy(self.result);r['decision']='hold'
        with self.assertRaises(ValueError):check.validate_decision(r,self.pages)
        r['entry']=None;check.validate_decision(r,self.pages)
    def test_missing_population_evidence_is_held(self):
        self.result['passages']=[p for p in self.result['passages'] if p['supports']!='sample']
        with self.assertRaises(ValueError):check.validate_decision(self.result,self.pages)

    def test_source_ids_copy_original_and_reject_unknown_or_visual(self):
        result=copy.deepcopy(self.result)
        result['passages']=[{'source_id':'original','supports':'claim'}]
        evidence={'passages':[{'evidence_id':'original','source':{'page':1,'text':self.pages[0]}}]}
        resolved=check.resolve_passages(result,evidence)
        self.assertEqual(resolved['passages'][0]['quote'],self.pages[0])
        result['passages'][0]['source_id']='invented'
        with self.assertRaises(ValueError):check.resolve_passages(result,evidence)
        result['passages'][0]['source_id']='original'
        evidence['passages'][0]['display_requires_pdf_check']=True
        with self.assertRaises(ValueError):check.resolve_passages(result,evidence)

    def test_semantic_acceptance_cannot_ignore_contradictions(self):
        audit={'verdict':'accept','checks':{k:'supported' for k in check.AUDIT_CHECKS},'issues':[]}
        evidence={'passages':[]}
        check.validate_audit(audit,self.result,evidence)
        audit['checks']['target_label']='contradicted'
        with self.assertRaises(ValueError):check.validate_audit(audit,self.result,evidence)
        audit['checks']['target_label']='supported'
        audit['checks']['population']='not_applicable'
        with self.assertRaises(ValueError):check.validate_audit(audit,self.result,evidence)

    def test_recovery_requires_reason_and_known_source_ids(self):
        audit={'verdict':'recover','checks':{k:'supported' for k in check.AUDIT_CHECKS},'issues':[]}
        with self.assertRaises(ValueError):check.validate_audit(audit,self.result,{'passages':[]})
        audit['issues']=[{'field':'direction','reason':'Preserve the null result','source_ids':['missing']}]
        with self.assertRaises(ValueError):check.validate_audit(audit,self.result,{'passages':[]})
        check.validate_audit(audit,self.result,{'passages':[{'evidence_id':'missing'}]})

    def test_concept_type_mismatch_is_not_silently_mapped(self):
        self.result['entry']['findings'][0]['target_kind']='impairment'
        with self.assertRaisesRegex(ValueError,'different concept type'):
            check.validate_decision(self.result,self.pages,{'anomia':{'kinds':['predictor']}})

    def test_direct_correction_requires_specific_method_evidence(self):
        self.result['entry']['findings'][0]['lesion_mapping']={'lesion_volume_correction':'direct'}
        with self.assertRaisesRegex(ValueError,'analysis-specific Methods'):
            check.validate_decision(self.result,self.pages)

    def test_flattened_table_requires_visual_review_even_without_display_flag(self):
        r=copy.deepcopy(self.result);r['passages']=[{'source_id':'table','supports':'statistics'}]
        evidence={'passages':[{'evidence_id':'table','source':{'page':1,'text':self.pages[0]},'classifications':{'A':'table_or_figure'}}]}
        with self.assertRaisesRegex(ValueError,'visual inspection'):check.resolve_passages(r,evidence)

    def test_source_trend_cannot_disappear(self):
        self.pages[0]+=' The FA result was only a trend after adjustment.'
        self.result['passages']=[{'page':1,'quote':self.pages[0],'supports':s} for s in ['claim','sample','method','statistics']]
        with self.assertRaisesRegex(ValueError,'qualifier was omitted'):check.validate_decision(self.result,self.pages)
        self.result['entry']['findings'][0]['notes']='FA was a trend after adjustment.'
        check.validate_decision(self.result,self.pages)

    def test_mni_family_normalization_preserves_detail_without_guessing_template(self):
        self.result['entry']['findings'][0]['imaging_details']={'reference_space':'MNI','reference_space_detail':'Template variant unspecified'}
        normalized,changes=check.normalize_mapping(self.result)
        self.assertEqual(normalized['entry']['findings'][0]['imaging_details']['reference_space'],'other')
        self.assertIn('MNI',normalized['entry']['findings'][0]['imaging_details']['reference_space_detail'])
        self.assertEqual(self.result['entry']['findings'][0]['imaging_details']['reference_space'],'MNI')
        self.assertEqual(len(changes),1)

    def test_accepting_exclusion_keeps_it_excluded(self):
        self.result.update(decision='exclude',entry=None)
        audit={'verdict':'accept','checks':{k:'supported' for k in check.AUDIT_CHECKS},'issues':[]}
        check.validate_audit(audit,self.result,{'passages':[]})
        self.assertEqual(self.result['decision'],'exclude')
        self.assertIsNone(self.result['entry'])

    def test_recovery_refuses_changed_binding_or_truncated_attempt(self):
        import tempfile,json
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'raw.json';path.write_text('{}')
            binding={'pdf_sha256':'pdf','review_sha256':'review','model_digest':'model'}
            meta={'binding':binding,'inference':{}}
            path.with_name('meta.json').write_text(json.dumps(meta))
            self.assertEqual(check.recovery_response(path,binding)['text'],'{}')
            with self.assertRaisesRegex(ValueError,'binding differs'):
                check.recovery_response(path,{**binding,'pdf_sha256':'changed'})
            meta['inference']['truncated_input']=True
            path.with_name('meta.json').write_text(json.dumps(meta))
            with self.assertRaisesRegex(ValueError,'Truncated'):
                check.recovery_response(path,binding)

if __name__=='__main__':unittest.main()
