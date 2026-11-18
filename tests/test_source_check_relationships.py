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

if __name__=='__main__':unittest.main()
