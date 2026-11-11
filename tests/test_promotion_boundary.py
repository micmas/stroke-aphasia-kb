import copy,sys,tempfile,unittest,yaml
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import promote as P
import auto_review as A
from test_schema_v28 import ENTRY
class Promotion(unittest.TestCase):
    def test_false_tier_cannot_promote(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); p=root/'drafts/therapies/x.md'; p.parent.mkdir(parents=True)
            fm=copy.deepcopy(ENTRY); fm['created_by']='agent:gemma4:31b'; fm['findings'][0]['therapy']={'id':'test','name':'Test'}
            p.write_text('---\n'+yaml.safe_dump(fm)+'---\n')
            with patch.object(P,'ROOT',root),patch.object(P,'LOG',root/'log.md'):
                with self.assertRaises(ValueError): P.cmd_approve(SimpleNamespace(approve=str(p),reviewer='model:gemma4:26b',tier='A',extractor=None))
                self.assertTrue(p.exists()); self.assertFalse((root/'therapies').exists())
                with self.assertRaises(ValueError): P._bucket_for(root/'drafts/_backup/regions/x.md')
    def test_backup_not_selected(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); (root/'_backup').mkdir(); (root/'_backup/x.md').write_text('bad')
            (root/'regions').mkdir(); (root/'regions/x.md').write_text('live')
            with patch.object(A,'DRAFTS_DIR',root): self.assertEqual(A.select_drafts(all_drafts=True),[root/'regions/x.md'])
if __name__=='__main__': unittest.main()


def test_model_report_is_bound_to_current_draft(tmp_path, monkeypatch):
    import hashlib
    fm = copy.deepcopy(ENTRY)
    fm['created_by'] = 'agent:ollama-extract-cli/gemma4:31b'
    fm['findings'][0]['relationship'] = 'correlational'
    fm['findings'][0]['provenance']['extracted_by'] = fm['created_by']
    draft = tmp_path / 'drafts/regions/test.md'
    draft.parent.mkdir(parents=True)
    draft.write_text('---\n' + yaml.safe_dump(fm) + '---\n')
    monkeypatch.setattr(P, 'ROOT', tmp_path)
    monkeypatch.setattr(P, 'LOG', tmp_path / 'logs/audit.md')
    monkeypatch.setattr(A, 'run_deterministic_checks', lambda *a, **kw: [])
    monkeypatch.setattr(A, 'classify_tier', lambda *a, **kw: ('A', []))
    report = tmp_path / 'logs/auto_review/regions/test.yaml'
    report.parent.mkdir(parents=True)
    run = {'draft_sha256': hashlib.sha256(draft.read_bytes()).hexdigest(),
           'verdict': A.Verdict.APPROVE, 'review_tier': 'A',
           'llm_review': {'model': 'gemma4:26b', 'independent': True, 'unanimous': True}}
    report.write_text(yaml.safe_dump({'runs': [run]}))
    args = SimpleNamespace(approve=str(draft), reviewer='model:gemma4:26b', tier='A', extractor=None)
    original = draft.read_text()
    draft.write_text(original + '\nchanged\n')
    import pytest
    with pytest.raises(ValueError, match='current, unanimous'):
        P.cmd_approve(args)
    draft.write_text(original)
    P.cmd_approve(args)
    assert not draft.exists()
    assert 'MODEL-APPROVED' in P.LOG.read_text()
    assert len(list((tmp_path / 'regions').glob('*.md'))) == 1
