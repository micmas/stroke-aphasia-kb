import hashlib
import json
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import batch_dual_extract as b


def manifest(tmp_path):
    pdf = tmp_path / 'paper.pdf'
    pdf.write_bytes(b'original')
    m = tmp_path / 'manifest.json'
    m.write_text(json.dumps({'source_scope': 'main_paper_only', 'papers': [{
        'key': 'Test2026', 'citation': '@Test2026', 'pdf': str(pdf),
        'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'licence_evidence': 'Article notice checked on page 1'}]}))
    return m


def test_preview_no_inference_or_writes(tmp_path, monkeypatch):
    monkeypatch.setattr(b, 'run_pair', lambda *a, **k: pytest.fail('inference'))
    assert b.batch(manifest(tmp_path), tmp_path/'out', ['a', 'b']) == 0
    assert not (tmp_path/'out').exists()


def test_resume_and_settings_change(tmp_path, monkeypatch):
    calls = []
    def run(pdf, citation, out, models, **kwargs):
        calls.append((pdf, citation, models, kwargs))
        out.mkdir()
        (out/'status.json').write_text('{"status":"awaiting_independent_review"}')
        return 0
    monkeypatch.setattr(b, 'run_pair', run)
    m = manifest(tmp_path)
    for _ in range(2):
        assert b.batch(m, tmp_path/'out', ['a', 'b'], execute=True) == 0
    assert len(calls) == 1
    assert calls[0][-1]['max_tokens'] == 20000
    with pytest.raises(ValueError, match='differs'):
        b.batch(m, tmp_path/'out', ['a', 'c'], execute=True)


def test_failed_output_preserved_no_retry(tmp_path, monkeypatch):
    def fail(pdf, citation, out, models, **kwargs):
        out.mkdir()
        (out/'raw.txt').write_text('partial evidence')
        return 1
    monkeypatch.setattr(b, 'run_pair', fail)
    m = manifest(tmp_path)
    assert b.batch(m, tmp_path/'out', ['a', 'b'], execute=True) == 1
    with pytest.raises(ValueError, match='preserved'):
        b.batch(m, tmp_path/'out', ['a', 'b'], execute=True)
    assert (tmp_path/'out/Test2026/raw.txt').read_text() == 'partial evidence'


def test_changed_source_rejected(tmp_path):
    m = manifest(tmp_path)
    (tmp_path/'paper.pdf').write_bytes(b'changed')
    with pytest.raises(ValueError, match='checksum'):
        b.load_manifest(m)


@pytest.mark.parametrize('field,value', [('key', '../escape'), ('licence_evidence', ''), ('citation', '@Wrong')])
def test_invalid_manifest(tmp_path, field, value):
    m = manifest(tmp_path)
    data = json.loads(m.read_text()); data['papers'][0][field] = value
    m.write_text(json.dumps(data))
    with pytest.raises(ValueError):
        b.load_manifest(m)


def test_explicit_retry_archives_failure(tmp_path, monkeypatch):
    def fail(pdf, citation, out, models, **kwargs):
        out.mkdir(); (out/'raw.txt').write_text('old'); return 1
    monkeypatch.setattr(b, 'run_pair', fail)
    m = manifest(tmp_path)
    b.batch(m, tmp_path/'out', ['a', 'b'], execute=True)
    def succeed(pdf, citation, out, models, **kwargs):
        out.mkdir(); (out/'status.json').write_text('{"status":"awaiting_independent_review"}'); return 0
    monkeypatch.setattr(b, 'run_pair', succeed)
    assert b.batch(m, tmp_path/'out', ['a', 'b'], execute=True, retry_failed=True) == 0
    assert (tmp_path/'out/_failed/Test2026/1/raw.txt').read_text() == 'old'


def test_concurrent_batch_rejected(tmp_path):
    import fcntl
    m = manifest(tmp_path)
    with (tmp_path/'out.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(ValueError, match='already running'):
            b.batch(m, tmp_path/'out', ['a', 'b'], execute=True)


def test_continue_runs_other_papers_and_reports_failure(tmp_path, monkeypatch):
    m = manifest(tmp_path)
    data = json.loads(m.read_text())
    second = dict(data['papers'][0], key='Other2026', citation='@Other2026')
    data['papers'].append(second); m.write_text(json.dumps(data))
    calls = []
    def run(pdf, citation, out, models, **kwargs):
        calls.append(citation); out.mkdir()
        if citation == '@Test2026':
            return 1
        (out/'status.json').write_text('{"status":"awaiting_independent_review"}')
        return 0
    monkeypatch.setattr(b, 'run_pair', run)
    assert b.batch(m, tmp_path/'out', ['a','b'], execute=True, continue_on_error=True) == 1
    assert calls == ['@Test2026','@Other2026']
    status = json.loads((tmp_path/'out/batch-status.json').read_text())
    assert status['failed'] == ['Test2026'] and status['approved'] is False
