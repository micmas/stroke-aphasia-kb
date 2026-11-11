import datetime as dt
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import extract
from extraction_evidence import audit_finding, flag_evidence

TEXT = '\n=== PAGE 1 ===\nAn association was reported in the abstract.\n=== PAGE 2 ===\nAfter adjustment the association was not statistically significant.\n'


def finding(quote, page):
    return {'id': 'f1', 'provenance': {'confidence': 'high', 'flags': []},
            'source_passages': [{'quote': quote, 'page': page, 'supports': 'claim'}]}


def test_real_quote_on_wrong_page_is_flagged_without_relocation():
    f = finding('After adjustment the association was not statistically significant.', 1)
    issues = flag_evidence(f, TEXT)
    assert 'exact text on PDF page(s) [2]' in issues[0]
    assert f['source_passages'][0]['page'] == 1
    assert f['provenance']['confidence'] == 'medium'
    assert audit_finding(finding(f['source_passages'][0]['quote'], 2), TEXT) == []


def test_negation_change_is_not_repaired_or_accepted():
    f = finding('After adjustment the association was statistically significant.', 2)
    assert flag_evidence(f, TEXT)
    assert 'was statistically significant' in f['source_passages'][0]['quote']


def test_missing_malformed_and_boolean_pages_fail_closed():
    for page in [None, True, 0, 3, '2']:
        assert audit_finding(finding('An association was reported in the abstract.', page), TEXT)
    assert audit_finding({'source_passages': []}, TEXT)
    assert audit_finding({'source_passages': ['bad']}, TEXT)


def test_low_confidence_preserved_and_flags_idempotent():
    f = finding('Unknown words.', 1)
    f['provenance']['confidence'] = 'low'
    flag_evidence(f, TEXT)
    flags = f['provenance']['flags'][:]
    flag_evidence(f, TEXT)
    assert f['provenance']['flags'] == flags
    assert f['provenance']['confidence'] == 'low'


def test_cross_page_quote_not_accepted_as_single_page():
    f = finding('An association was reported in the abstract. After adjustment the association was not statistically significant.', 1)
    assert audit_finding(f, TEXT)


def test_saved_extraction_uses_actual_provenance_and_keeps_evidence_flag(tmp_path):
    f = finding('After adjustment the association was not statistically significant.', 1)
    f['provenance'].update(extracted_by='invented', extracted_on='2026-01-01')
    fm = {'schema_version': 2.8, 'id': 'example', 'kind': 'region', 'status': 'approved', 'findings': [f]}
    content = '---\n' + yaml.safe_dump(fm) + '---\n'
    paths = extract.save_drafts([{'bucket': 'regions', 'filename': 'example__Example2020.md', 'content': content}], tmp_path,
                               created_by='agent:test-local-model', citation='@Example2020', paper_text=TEXT)
    saved = yaml.safe_load(paths[0].read_text().split('---')[1])
    p = saved['findings'][0]['provenance']
    assert saved['status'] == 'draft'
    assert p['extracted_by'] == 'agent:test-local-model'
    assert str(p['extracted_on']) == dt.date.today().isoformat()
    assert any('exact text on PDF page(s) [2]' in x for x in p['flags'])


def test_target_context_includes_construct_not_existing_findings(tmp_path):
    bucket = tmp_path / 'impairments'; bucket.mkdir()
    fm = {'id': 'fluency', 'name': 'Speech fluency', 'kind': 'impairment',
          'short_definition': 'Connected speech, distinct from word generation.',
          'assessment': ['Words per minute'], 'findings': [{'claim': 'DO NOT LEAK PRIOR FINDINGS'}]}
    (bucket / 'fluency.md').write_text('---\n' + yaml.safe_dump(fm) + '---\n')
    summary = extract._existing_kb_summary(tmp_path)
    assert 'Connected speech, distinct from word generation.' in summary
    assert 'Words per minute' in summary
    assert 'DO NOT LEAK PRIOR FINDINGS' not in summary


def test_evidence_flags_defer_to_human_review():
    from auto_review import check_no_human_review_flags
    f = finding('After adjustment the association was not statistically significant.', 1)
    flag_evidence(f, TEXT)
    assert check_no_human_review_flags({'findings': [f]}).passed is False


def test_empty_evaluation_is_not_success(tmp_path, monkeypatch):
    import evaluate_extraction_accuracy as evaluator
    pdf = tmp_path / 'source.pdf'; pdf.write_bytes(b'fixture')
    drafts = tmp_path / 'drafts'; drafts.mkdir()
    monkeypatch.setattr(evaluator, '_extract_pdf_text', lambda _: (TEXT, 2))
    report = evaluator.evaluate(drafts, pdf)
    assert report['findings'] == 0
    assert not report['complete_nonempty']


def test_null_provenance_and_flags_are_recoverable_but_wrong_types_fail():
    import pytest
    for provenance in [None, {'flags': None}]:
        f = finding('Unknown words.', 1)
        f['provenance'] = provenance
        assert flag_evidence(f, TEXT)
        assert isinstance(f['provenance']['flags'], list)
        content = '---\n' + yaml.safe_dump({'findings': [{'id': 'f1', 'provenance': provenance}]}) + '---\n'
        normalized, _ = extract._normalize_findings(content, 'regions', None)
        assert isinstance(yaml.safe_load(normalized.split('---')[1])['findings'][0]['provenance']['flags'], list)
    for provenance in ['bad', {'flags': 'bad'}]:
        f = finding('Unknown words.', 1); f['provenance'] = provenance
        with pytest.raises(ValueError):
            flag_evidence(f, TEXT)
        content = '---\n' + yaml.safe_dump({'findings': [f]}) + '---\n'
        with pytest.raises(ValueError):
            extract._normalize_findings(content, 'regions', None)


def test_non_mapping_canonical_entry_is_ignored(tmp_path):
    (tmp_path/'regions').mkdir()
    (tmp_path/'regions/example.md').write_text('---\n- invalid\n---\n')
    assert extract._canonical_entry(tmp_path, 'regions', 'example') == {}
    extract._existing_kb_summary(tmp_path)


def test_malformed_yaml_is_reported_not_abandoned(tmp_path, monkeypatch):
    import evaluate_extraction_accuracy as evaluator
    pdf = tmp_path/'source.pdf'; pdf.write_bytes(b'fixture')
    drafts = tmp_path/'drafts'; drafts.mkdir()
    (drafts/'bad.md').write_text('---\nfindings: [\n---\n')
    monkeypatch.setattr(evaluator, '_extract_pdf_text', lambda _: (TEXT, 2))
    report = evaluator.evaluate(drafts, pdf)
    assert report['schema_issues'] > 0
    assert not report['complete_nonempty']


def test_narrative_review_cannot_claim_primary_causal_evidence():
    from aphasia_kb import _validate_v2_entry
    fm = {'schema_version': 2.8, 'id': 'example', 'kind': 'classical',
          'findings': [{'id': 'f1', 'method': 'narrative_review',
                        'relationship': 'causal', 'evidence_quality': 'cohort'}]}
    issues = []
    _validate_v2_entry(fm, 'fixture.md', issues)
    assert any('requires relationship=synthesis' in x for x in issues)
    assert any('requires evidence_quality=narrative-review' in x for x in issues)
    fm['findings'][0].update(relationship='synthesis', evidence_quality='narrative-review')
    issues = []
    _validate_v2_entry(fm, 'fixture.md', issues)
    assert not any('narrative_review requires' in x for x in issues)
