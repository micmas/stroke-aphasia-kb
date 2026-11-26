"""Review evidence must be explicit and must not bypass approval boundaries."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import aphasia_kb as K
import export_webapp as E
from test_schema_v28 import ENTRY

class ReviewEvidence(unittest.TestCase):
    def entry(self):
        e = copy.deepcopy(ENTRY)
        e.update(schema_version='2.9', kind='review', id='review_x')
        e['findings'][0].update(method='narrative_review', relationship='synthesis',
            design='systematic-review', evidence_quality='narrative-review')
        return e

    def write(self, root, name, e):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('---\n' + yaml.safe_dump(e) + '---\n')

    def test_review_roundtrip_and_status_boundary(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            self.write(root, 'drafts/reviews/x.md', self.entry())
            old = self.entry()
            old.update(schema_version='2.4', status='approved', reviewer='human:legacy')
            self.write(root, 'reviews/legacy_summary.md', old)
            kb = K.KnowledgeBase(root, include=('approved', 'draft'))
            self.assertEqual(len(kb.findings), 1)
            self.assertEqual(kb.findings.iloc[0]['source_kind'], 'review')
            self.assertEqual(E.entries(kb)['review_x']['bucket'], 'reviews')
            self.assertEqual(E.findings(kb, root)[0]['source_path'], 'drafts/reviews/x.md')
            self.assertTrue(K.KnowledgeBase(root).findings.empty)
            bad = self.entry()
            bad.update(status='approved', reviewer='human:invented')
            self.write(root, 'drafts/reviews/x.md', bad)
            self.assertTrue(K.KnowledgeBase(root, include=('approved', 'draft')).findings.empty)

    def test_review_cannot_be_presented_as_new_patient_experiment(self):
        e = self.entry()
        issues = []
        K._validate_v2_entry(e, 'x.md', issues)
        self.assertEqual(issues, [])
        e['findings'][0].update(method='clinical_RCT', relationship='treatment_response')
        K._validate_v2_entry(e, 'x.md', issues)
        self.assertTrue(any('review findings require' in i for i in issues))

    def test_fixel_method_is_distinct_from_lesion_mapping(self):
        e = copy.deepcopy(ENTRY)
        e['findings'][0].update(method='FBA', relationship='correlational')
        issues = []
        K._validate_v2_entry(e, 'x.md', issues)
        self.assertFalse(any('method=' in i for i in issues), issues)
        self.assertIsNone(K._lesion_columns(e['findings'][0])['lm_source'])

if __name__ == '__main__':
    unittest.main()
