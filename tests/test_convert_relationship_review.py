"""Conversion boundaries using synthetic evidence, not a clinical accuracy test."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import convert_relationship_review as conversion
import promote


class ConversionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.reviews = self.root / 'review'
        self.paper = self.reviews / 'Example2026'
        self.paper.mkdir(parents=True)
        outputs = {
            'proposals.json': {'units': [{'id': 'R1', 'evidence_ids': ['E1'], 'qualifier_ids': []}]},
            'evidence.json': {'passages': [{'evidence_id': 'E1', 'source': {'text': 'Synthetic source quotation.', 'page': 2}}]},
            'audit.json': {'issues': ['Requires source review']},
            'study-frame.json': {'population': 'synthetic fixture'},
        }
        for name, value in outputs.items():
            (self.paper / name).write_text(json.dumps(value))
        (self.paper / 'status.json').write_text(json.dumps({'status': 'requires_revision',
            'binding': {'version': 'fixture'}, 'output_hashes': {
                name: conversion.digest(self.paper / name) for name in outputs}}))
        self.mapping = self.root / 'mapping.json'
        conversion.prepare(self.reviews, self.mapping)
        data = conversion.read(self.mapping)
        data['items'][0].update(bucket='reviews', entry={
            'id': 'example', 'name': 'Synthetic test', 'kind': 'network',
            'status': 'approved', 'reviewer': 'human:fake',
            'findings': [{'id': 'f1', 'target': 'anomia', 'target_kind': 'impairment',
                'claim': 'Synthetic claim', 'direction': 'mixed', 'method': 'narrative_review',
                'relationship': 'synthesis', 'evidence_quality': 'narrative-review',
                'strength': 'weak', 'author_limitations': [],
                'review': {'reviewer': 'human:fake'},
                'provenance': {'extracted_by': 'test', 'extracted_on': '2026-11-17',
                    'paper_section': 'test', 'confidence': 'low', 'flags': []}}]})
        self.mapping.write_text(json.dumps(data))

    def test_preview_execute_idempotence_and_approval_hold(self):
        ready = conversion.convert(self.mapping, self.root)
        path, text = ready[0]
        self.assertFalse(path.exists())
        conversion.convert(self.mapping, self.root, execute=True)
        self.assertEqual(path.read_text(), text)
        self.assertEqual(conversion.convert(self.mapping, self.root, execute=True), [])
        fm = yaml.safe_load(text.split('---')[1])
        self.assertEqual(fm['status'], 'draft')
        self.assertNotIn('reviewer', fm)
        self.assertNotIn('review', fm['findings'][0])
        self.assertEqual(fm['findings'][0]['source_passages'][0]['quote'], 'Synthetic source quotation.')
        with patch.object(promote, 'ROOT', self.root), self.assertRaises(SystemExit):
            promote._approve_locked(SimpleNamespace(approve=str(path)))
        self.assertTrue(path.exists())
        path.write_text('Human edits')
        with self.assertRaises(ValueError):
            conversion.convert(self.mapping, self.root, execute=True)
        self.assertEqual(path.read_text(), 'Human edits')

    def test_changed_review_refused_before_writes(self):
        (self.paper / 'audit.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'changed review hash'):
            conversion.convert(self.mapping, self.root, execute=True)
        self.assertFalse((self.root / 'drafts').exists())

    def test_invalid_mapping_prevents_batch_writes(self):
        data = conversion.read(self.mapping)
        invalid = dict(data['items'][0], entry={'id': '../../escape', 'findings': [{}]})
        data['items'].append(invalid)
        self.mapping.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            conversion.convert(self.mapping, self.root, execute=True)
        self.assertFalse((self.root / 'drafts').exists())


if __name__ == '__main__':
    unittest.main()


class PdfEvidenceTests(unittest.TestCase):
    def test_pdf_support_requires_matching_hash_and_literal_page_text(self):
        import pymupdf
        fixture = ConversionTests('test_changed_review_refused_before_writes')
        fixture.setUp()
        try:
            pdf = fixture.root / 'source.pdf'
            with pymupdf.open() as doc:
                doc.new_page().insert_text((72, 72), 'Table 1: example value 42')
                doc.save(pdf)
            state = conversion.read(fixture.paper / 'status.json')
            state['binding']['input_hashes'] = {'pdf': conversion.digest(pdf)}
            (fixture.paper / 'status.json').write_text(json.dumps(state))
            data = conversion.read(fixture.mapping)
            item = data['items'][0]
            item['review_status_sha256'] = conversion.digest(fixture.paper / 'status.json')
            item['source_pdf'] = str(pdf)
            item['pdf_evidence'] = [{'page': 1, 'section': 'Table 1', 'quote': 'example value 42', 'supports': 'statistics'}]
            fixture.mapping.write_text(json.dumps(data))
            self.assertEqual(len(conversion.convert(fixture.mapping, fixture.root)), 1)
            item['replace_proposal_passages'] = True
            with self.assertRaisesRegex(ValueError, 'requires a source check'):
                conversion.build(item, fixture.reviews)
            item['source_check'] = {'checked_by': 'model:fixture', 'approved': False}
            _, rendered = conversion.build(item, fixture.reviews)
            fm = yaml.safe_load(rendered.split('---')[1])
            self.assertEqual([p['quote'] for p in fm['findings'][0]['source_passages']], ['example value 42'])
            self.assertEqual(fm['reviewer_marks'][0]['page'], 1)
            item['pdf_evidence'][0]['quote'] = 'invented value 43'
            fixture.mapping.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'not found'):
                conversion.convert(fixture.mapping, fixture.root, True)
            self.assertFalse((fixture.root / 'drafts').exists())
        finally:
            fixture.doCleanups()
