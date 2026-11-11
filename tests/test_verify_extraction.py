import json
import sys
from pathlib import Path
import pytest
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import verify_extraction as v


def envelope(citation='@Example2020', claim='original'):
    fm = {'findings': [{'id': 'f1', 'citation': citation, 'claim': claim}]}
    return {'drafts': [{'bucket': 'regions', 'filename': 'example.md',
                        'content': '---\n'+yaml.safe_dump(fm)+'---\n'}]}


def test_diff_records_removed_added_and_changed():
    before = v.finding_inventory(envelope())
    after = v.finding_inventory(envelope(claim='changed'))
    assert v.finding_diff(before, after)['changed']
    assert v.finding_diff(before, {})['dropped']
    assert v.finding_diff({}, after)['added']


def test_refuses_existing_output_without_changing_input(tmp_path):
    source = tmp_path/'input.json'; source.write_text(json.dumps(envelope()))
    original = source.read_bytes()
    with pytest.raises(FileExistsError):
        v.run_verification(source, tmp_path/'pdf', '@Example2020', tmp_path, tmp_path, 'test')
    assert source.read_bytes() == original


def test_failure_is_recorded_and_citation_drift_not_saved(tmp_path, monkeypatch):
    source = tmp_path/'input.json'; source.write_text(json.dumps(envelope()))
    original = source.read_bytes()
    monkeypatch.setattr(v, '_extract_pdf_text', lambda _: ('=== PAGE 1 ===\ntext', 1))
    monkeypatch.setattr(v, '_existing_kb_summary', lambda _: 'definitions')
    monkeypatch.setattr(v, 'call_ollama', lambda *a, **kw: json.dumps(envelope(citation='@Wrong2020')))
    out = tmp_path/'output'
    with pytest.raises(ValueError, match='citation'):
        v.run_verification(source, tmp_path/'pdf', '@Example2020', out, tmp_path, 'test')
    meta = json.loads((out/'meta.json').read_text())
    assert meta['status'] == 'failed'
    assert meta['finding_diff']['changed']
    assert (out/'raw.json').exists()
    assert not (out/'drafts').exists()
    assert source.read_bytes() == original
