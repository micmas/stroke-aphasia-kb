import importlib.util
from pathlib import Path
import pytest
spec=importlib.util.spec_from_file_location('product_cli',Path(__file__).resolve().parents[1]/'kb.py')
cli=importlib.util.module_from_spec(spec);spec.loader.exec_module(cli)


def test_help_has_one_current_path(capsys):
    assert cli.main([])==0
    out=capsys.readouterr().out
    assert 'extract' in out and 'review' in out and 'provisional' in out


@pytest.mark.parametrize('command,script',[('extract','batch_dual_extract.py'),('review','review_dual_extract.py')])
def test_exact_arguments_and_interpreter_preserved(monkeypatch,command,script):
    calls=[];monkeypatch.setattr(cli.os,'execv',lambda exe,args:calls.append((exe,args)))
    args=['--manifest','a path; $(no shell).json']
    cli.main([command,*args])
    assert calls[0][0]==cli.sys.executable
    assert calls[0][1][1]==str(cli.ROOT/'scripts'/script)
    assert calls[0][1][2:]==args


def test_prepare_defaults_repo_and_respects_override(monkeypatch):
    calls=[];monkeypatch.setattr(cli.os,'execv',lambda exe,args:calls.append(args))
    cli.main(['prepare','--output','manifest.json'])
    assert calls[-1][2:4]==['--repo',str(cli.ROOT)]
    cli.main(['prepare','--repo=/tmp/example','--output','manifest.json'])
    assert calls[-1][2:]==['--repo=/tmp/example','--output','manifest.json']


def test_no_accidental_mutation_from_list_commands(monkeypatch):
    monkeypatch.setattr(cli.os,'execv',lambda *a:pytest.fail('must not execute'))
    assert cli.main(['status','--tag-legacy'])==2
    assert cli.main(['drafts','--approve','a.md'])==2
    assert cli.main(['does-not-exist'])==2


def test_busy_processing_does_not_start(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(cli, 'git', lambda *a, **k: str(tmp_path))
    monkeypatch.setattr(cli, 'active_jobs', lambda: ['123 python batch_dual_extract.py'])
    monkeypatch.setattr(cli.subprocess, 'Popen', lambda *a, **k: pytest.fail('busy'))
    assert cli.main(['extract', '--run']) == 2
    assert 'No work started' in capsys.readouterr().out


def test_wait_starts_only_when_idle(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, 'git', lambda *a, **k: str(tmp_path))
    states = iter([['busy'], []])
    monkeypatch.setattr(cli, 'active_jobs', lambda: next(states))
    sleeps = []; calls = []
    monkeypatch.setattr(cli.time, 'sleep', lambda n: sleeps.append(n))
    class Child:
        def wait(self): return 7
    monkeypatch.setattr(cli.subprocess, 'Popen', lambda args, **k: (calls.append(args) or Child()))
    assert cli.main(['review', '--run', '--wait']) == 7
    assert sleeps == [5] and len(calls) == 1 and '--wait' not in calls[0]


def test_sync_refuses_to_publish_unrelated_staged_work(monkeypatch, tmp_path):
    calls = []
    def fake_git(*args, **kwargs):
        calls.append(args)
        if args[0] == 'rev-parse': return str(tmp_path)
        if args[0] == 'branch': return 'main'
        if args[:2] == ('diff', '--cached'): return 'regions/user-edit.md'
        pytest.fail('must stop before fetch, download, or publishing')
    monkeypatch.setattr(cli, 'git', fake_git)
    assert cli.main(['sync']) == 1
    assert not any(c[0] == 'push' for c in calls)


def test_process_detection_ignores_shell_and_current_process(monkeypatch):
    from types import SimpleNamespace
    monkeypatch.setattr(cli.subprocess, 'run', lambda *a, **k: SimpleNamespace(stdout=
        f'{cli.os.getpid()} python scripts/batch_dual_extract.py\n'
        '99 /bin/zsh -lc python scripts/batch_dual_extract.py\n'
        '100 /path/Python scripts/review_dual_extract.py --run\n'))
    assert cli.active_jobs() == ['100 /path/Python scripts/review_dual_extract.py --run']


def test_sync_only_publishes_import_paths_and_never_runs_intake(monkeypatch, tmp_path):
    from types import SimpleNamespace
    inbox = tmp_path / 'inbox'; inbox.mkdir()
    calls = []; imports = []; staged_checks = iter(['', 'logs/portal/ledger.jsonl'])
    def fake_git(*args, **kwargs):
        calls.append(args)
        if args[0] == 'rev-parse': return str(tmp_path)
        if args[0] == 'branch': return 'main'
        if args[:2] == ('diff', '--cached'): return next(staged_checks)
        return ''
    monkeypatch.setattr(cli, 'git', fake_git)
    monkeypatch.setattr(cli, 'active_jobs', lambda: ['existing extraction'])
    monkeypatch.setitem(cli.sys.modules, 'portal_import', SimpleNamespace(
        INBOX=inbox, run=lambda *a, **k: imports.append((a, k))))
    assert cli.main(['sync']) == 0
    assert imports == [((True, False, 'pdf'), {'intake': False})]
    added = next(c for c in calls if c[0] == 'add')
    assert '.' not in added and 'drafts' not in added and 'papers' not in added
    assert ('push', 'origin', 'main') in calls


def test_sync_does_not_update_code_under_active_job(monkeypatch, tmp_path):
    calls = []
    def fake_git(*args, **kwargs):
        calls.append(args)
        if args[0] == 'rev-parse': return str(tmp_path)
        if args[0] == 'branch': return 'main'
        if args[:3] == ('diff', 'HEAD', 'origin/main'): return 'changed extraction code'
        return ''
    monkeypatch.setattr(cli, 'git', fake_git)
    monkeypatch.setattr(cli, 'active_jobs', lambda: ['existing extraction'])
    assert cli.main(['sync']) == 1
    assert not any(c[0] in ('merge', 'add', 'push') for c in calls)
