import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import portal_import as P


def test_progress_is_opt_in_and_never_networks_for_preview(monkeypatch):
    monkeypatch.delenv('PORTAL_APPLY_PROGRESS', raising=False)
    monkeypatch.setattr(P, '_progress_request', lambda *a: (_ for _ in ()).throw(AssertionError('network')))
    assert P.ApplyProgress(3, True).check_id is None
    monkeypatch.setenv('PORTAL_APPLY_PROGRESS', '1')
    assert P.ApplyProgress(3, False).check_id is None


def test_progress_binds_run_attempt_and_published_commit(monkeypatch, tmp_path):
    for key, value in dict(PORTAL_APPLY_PROGRESS='1', GITHUB_TOKEN='test', GITHUB_REPOSITORY='o/r',
                           GITHUB_RUN_ID='123', GITHUB_RUN_ATTEMPT='2', GITHUB_SHA='a'*40,
                           GITHUB_ENV=str(tmp_path/'env')).items():
        monkeypatch.setenv(key, value)
    calls = []
    summary = {}
    def request(method, endpoint, body=None):
        calls.append((method, endpoint, body))
        if body and 'output' in body:
            summary.update(json.loads(body['output']['summary']))
        return {'id': 7, 'output': {'summary': json.dumps(summary)}}
    monkeypatch.setattr(P, '_progress_request', request)
    progress = P.ApplyProgress(9, True)
    progress.update(2, 1)
    assert calls[0][2]['external_id'] == 'portal-apply:123:2'
    assert summary['current'] == 2 and summary['processed'] == 1
    assert (tmp_path/'env').read_text() == 'PORTAL_PROGRESS_ID=7\n'
    monkeypatch.setenv('PORTAL_PROGRESS_ID', '7')
    monkeypatch.setenv('PORTAL_PUBLISHED_SHA', 'b'*40)
    P.publish_apply_progress()
    assert summary['published_sha'] == 'b'*40
    P.finish_apply_progress()
    assert calls[-1][2] == {'status':'completed', 'conclusion':'neutral'}


def test_record_counter_excludes_local_pdf_downloads(monkeypatch, tmp_path):
    inbox = tmp_path/'inbox'; inbox.mkdir()
    for i, kind in enumerate(['screen','pdf','screen']):
        (inbox/f'{i}.json').write_text(json.dumps({'kind':kind, 'id':f'C{i}', 'reviewer':'x@example.org'}))
    for name,value in dict(ROOT=tmp_path, INBOX=inbox, APPLIED=tmp_path/'applied', LOG=tmp_path/'log', LEDGER=None).items():
        monkeypatch.setattr(P,name,value)
    monkeypatch.setattr(P, 'reviewers', lambda: {})
    monkeypatch.setattr(P, 'apply_screen', lambda *a: P.Outcome('applied','applied'))
    updates=[]
    class Progress:
        def __init__(self,total,execute): assert total==2 and execute
        def update(self,current,processed,phase='applying'): updates.append((current,processed,phase))
    monkeypatch.setattr(P,'ApplyProgress',Progress)
    assert P.run(True,False,None,('pdf',)) == 0
    assert updates == [(1,0,'applying'),(2,1,'applying'),(2,2,'checking')]
    assert [p.name for p in inbox.iterdir()] == ['1.json']
