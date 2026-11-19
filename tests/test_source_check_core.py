"""Core conversion boundaries; scientific quality is assessed on source pilots."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import jsonschema
import source_check_core as core


class CoreTests(unittest.TestCase):
    def test_every_question_requires_evidence_and_can_hold(self):
        names=['analysis_identity','direction','construct','qualifications','missing_material_caveat']
        audit={'source_result':'A null association.', 'own_result_source_ids':['result'],
            'result_status':'not_detected','patient_measurement':'regional_lesion_load','checks':{
            key:{'answer':'fits','reason':'The source supports the qualified null.','source_ids':['result']}
            for key in names}, 'optional_pending':[]}
        schema=core.review_schema({'result'})
        jsonschema.validate(audit,schema)
        self.assertEqual(core.review_decision(audit)['verdict'],'draft')
        for status in ['robustness_only','unresolved_source_conflict','unclear']:
            bad=copy.deepcopy(audit);bad['result_status']=status
            self.assertEqual(core.review_decision(bad)['verdict'],'hold')
        bad=copy.deepcopy(audit);bad['patient_measurement']='template_lesion_overlap'
        self.assertEqual(core.review_decision(bad,{'direction':'no_effect','method':'DTI'})['verdict'],'hold')
        for name in names:
            bad=copy.deepcopy(audit);bad['checks'][name]['answer']='unclear'
            self.assertEqual(core.review_decision(bad)['verdict'],'hold')
        for ids in [[], ['invented']]:
            bad=copy.deepcopy(audit);bad['checks']['direction']['source_ids']=ids
            with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(bad,schema)

    def test_context_is_allowed_but_cannot_replace_primary_result(self):
        rows={'passages':[{'evidence_id':sid,'source':{'text':text}} for sid,text in
            [('result','An association was detected.'),('context','Fifty participants were studied.')]]}
        card={'decision':'draft','kind':'predictor','bucket':'predictors','sample_n':51,
            'population':'Selected cohort','timing':'Concurrent',
            'claim':'Qualified association','qualifications':['Only in the selected population'],
            'optional_pending':[], 'passages':[
                {'source_id':'result','supports':'claim'}, {'source_id':'context','supports':'claim'},
                {'source_id':'context','supports':'sample'},{'source_id':'context','supports':'method'}]}
        original=copy.deepcopy(card)
        prepared,changes=core.prepare_card(card,{'evidence_ids':['result']},rows)
        self.assertEqual(card,original)
        self.assertEqual(prepared['claim'],card['claim'])
        self.assertEqual(prepared['qualifications'],card['qualifications'])
        self.assertIsNone(prepared['sample_n'])
        self.assertEqual(changes[0]['action'],'not_transcribed')
        with self.assertRaisesRegex(ValueError,'primary evidence'):
            core.prepare_card(card,{'evidence_ids':['another_result']},rows)

    def test_image_reading_supersedes_bad_numbers_without_changing_quote(self):
        rows={'passages':[{'evidence_id':'result','source':{'text':'Minimum 41 months after stroke; Thirty-six participants.'}}],
            'visual_readings':{'result':{'status':'agreed_model_transcription','transcription':'Minimum >1 month after stroke; Thirty-six participants.'}}}
        card={'decision':'draft','kind':'predictor','bucket':'predictors','sample_n':36,
            'population':'Thirty-six participants','timing':'Minimum 41 months after stroke',
            'claim':'Association','qualifications':[],'optional_pending':[],
            'passages':[{'source_id':'result','supports':role} for role in ['claim','sample','method']]}
        original=copy.deepcopy(rows)
        prepared,changes=core.prepare_card(card,{'evidence_ids':['result']},rows)
        self.assertEqual(prepared['sample_n'],36)
        self.assertIn('sample.time_post_onset',prepared['_pending_fields'])
        self.assertNotIn('41',prepared['timing'])
        self.assertEqual(rows,original)

    def test_disagreeing_table_boundaries_remain_visible_to_both_models(self):
        cell=lambda boundary:{'row_path':['Tract',boundary],'column_path':['Adjusted OR (95% CI)'],'raw':'4 (2–8)'}
        evidence={'tables':[{'table_id':'T1','pdf_page':2,'facts':[{'source_A':cell('>15%'),'source_B':cell('≥15%')}]}]}
        hints=core.table_hints(evidence)
        self.assertIn('>15%',hints);self.assertIn('≥15%',hints)
        self.assertIn('UNVERIFIED',hints)

    def test_optional_placeholders_are_explicit_and_never_approval(self):
        card={'entity_id':'test_predictor','name':'Test predictor','kind':'predictor',
            'predictor_type':'clinical','definition':'Measured predictor','assessment':[],
            'target':'anomia','target_kind':'impairment','claim':'No association detected after adjustment.',
            'direction':'no_effect','relationship':'correlational','method':'LSM','therapy':None,
            'sample_n':None,'population':'Selected stroke cohort','timing':'Concurrent',
            'qualifications':['After adjustment','Selected cohort'], 'limitations':[],
            'optional_pending':[],'evidence_quality':'cohort'}
        entry,pending=core.make_entry(card,'2026-11-19','mapper')
        finding=entry['findings'][0]
        self.assertEqual(finding['claim'],card['claim'])
        self.assertIn('After adjustment; Selected cohort.',finding['notes'])
        flags=finding['provenance']['flags']
        for field in ['statistics','sample.n','sample.phase','strength','author_limitations']:
            self.assertIn('not_transcribed:'+field,flags)
        self.assertIn('human_approval_pending',flags)
        self.assertTrue(pending)

if __name__=='__main__':unittest.main()

class CoreConflictTests(unittest.TestCase):
    def test_adjusted_ratio_conflict_is_exposure_specific_and_conservative(self):
        from unittest.mock import patch
        card={'direction':'no_effect','claim':'Age was not independently associated with aphasia.',
              'qualifications':[],'definition':'Age in years'}
        unit={'evidence_ids':['result'],'exposure':{'text':'Age'},'outcome':{'text':'aphasia'}}
        a={'row_path':['Age'],'column_path':['Adjusted OR (95% CI)'],'raw':'3.97 (1.02–15.46)'}
        table={'caption':'Aphasia','table_id':'T1','pdf_page':7,'agreed_readings':[{'reading_A':a,'reading_B':copy.deepcopy(a)}]}
        with patch('source_check_facets.table_context',return_value=[table]):
            self.assertEqual(len(core.ratio_null_conflicts(card,unit,{})),1)
            for field,value in [('row_path',['Gender']),('column_path',['Crude OR (95% CI)']),
                                ('column_path',['Adjusted OR (90% CI)']),('raw','3.97 (1.00–15.46)')]:
                old=a[field];a[field]=value
                self.assertEqual(core.ratio_null_conflicts(card,unit,{}),[])
                a[field]=old
            table['agreed_readings']=[]
            self.assertEqual(core.ratio_null_conflicts(card,unit,{}),[])

    def test_ranking_cannot_drop_a_tie(self):
        card={'direction':'likely','claim':'RS had the best performance.','qualifications':[]}
        unit={'evidence_ids':['result']}
        evidence={'passages':[{'evidence_id':'result','source':{'text':'Three equally optimal models were found.'}}]}
        review={'own_result_source_ids':['result']}
        self.assertEqual(len(core.source_conflicts(card,unit,evidence,review)),1)
        card['qualifications']=['Three models tied for best performance.']
        self.assertEqual(core.source_conflicts(card,unit,evidence,review),[])
