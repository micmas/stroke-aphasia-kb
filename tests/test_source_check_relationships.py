"""Safety boundaries for model source checks, not an accuracy benchmark."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_check_relationships as check

class SourceCheckTests(unittest.TestCase):
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
