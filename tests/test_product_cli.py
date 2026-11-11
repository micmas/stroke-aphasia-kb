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
    args=['--manifest','a path; $(no shell).json','--run']
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
