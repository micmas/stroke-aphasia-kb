import copy
import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_draft_targets import audit, update_text
from test_schema_v28 import ENTRY, issues


class TargetAuditTests(unittest.TestCase):
    def test_token_test_and_speech_tokens_are_distinct(self):
        a = audit({'target': 'token_test_performance', 'target_kind': 'impairment', 'citation': '@Adezati2022'})
        b = audit({'target': 'token_measure_t', 'target_kind': 'impairment', 'citation': '@Halai2017'})
        self.assertEqual(a[0], 'auditory_sentence_comprehension')
        self.assertEqual(a[1]['instruments'][0]['name'], 'Token Test')
        self.assertEqual(b[0], 'speech_output_quantity')
        self.assertNotEqual(b[1]['instruments'][0]['name'], 'Token Test')

    def test_rules_do_not_guess_other_papers_or_composites(self):
        for target, citation in [('token_test_performance', '@Unknown2026'), ('wab_aphasia_quotient', '@Breier2008'), ('poor_mrs_moca', '@Munsch2016')]:
            result = audit({'target': target, 'target_kind': 'impairment', 'citation': citation})
            self.assertEqual(result[0], target)
            self.assertEqual(result[1]['status'], 'needs_source_review')

    def test_splice_keeps_nested_originals_claims_and_approval(self):
        text = '---\nstatus: draft\nfindings:\n- id: f1\n  target: test_score\n  claim: Original claim\n  source_passages:\n  - quote: Exact quote\nrelationship_review:\n  target: test_score\n---\nBody\n'
        changes = {'target': 'naming', 'outcome_measurement': {'status': 'identified', 'instruments': [{'name': 'Naming test'}]}}
        result = update_text(text, 'f1', changes)
        expected = yaml.safe_load(text.split('---')[1])
        expected['findings'][0].update(changes)
        self.assertEqual(yaml.safe_load(result.split('---')[1]), expected)
        self.assertIn('relationship_review:\n  target: test_score\n---\nBody\n', result)
        self.assertEqual(update_text(result, 'f1', changes), result)

    def test_measurement_is_separate_from_predictor_triplet(self):
        e = copy.deepcopy(ENTRY)
        e['findings'][0]['outcome_measurement'] = {'status': 'identified', 'instruments': [{'name': 'Token Test'}]}
        self.assertFalse(any('outcome_measurement' in i or 'triplet' in i for i in issues(e)))
        e['findings'][0]['outcome_measurement']['instruments'] = []
        self.assertTrue(any('identified outcome_measurement' in i for i in issues(e)))


if __name__ == '__main__':
    unittest.main()
