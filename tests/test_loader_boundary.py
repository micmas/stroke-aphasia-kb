import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import aphasia_kb as K
from test_schema_v28 import ENTRY

class Boundary(unittest.TestCase):
    def test_draft_cannot_self_approve(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'drafts/regions/x.md'; p.parent.mkdir(parents=True)
            fm=copy.deepcopy(ENTRY); fm.update(status='approved',reviewer='human:invented',reviewed_on='2026-11-11')
            fm['findings'][0]['therapy']={'id':'test','name':'Test'}
            p.write_text('---\n'+yaml.safe_dump(fm)+'---\n')
            self.assertTrue(K.KnowledgeBase(Path(t)).findings.empty)
            self.assertTrue(K.KnowledgeBase(Path(t),include=('approved','draft')).findings.empty)
    def test_dispatch(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'regions/x.md'; p.parent.mkdir(); p.write_text('---\n'+yaml.safe_dump(ENTRY)+'---\n')
            with patch.object(K,'_validate_v2_entry',wraps=K._validate_v2_entry) as v2:
                kb=K.KnowledgeBase(Path(t)); self.assertEqual(v2.call_count,1)
                self.assertTrue(any('therapy' in i for i in kb.issues))
if __name__=='__main__': unittest.main()


def test_malformed_findings_are_reported_without_crashing(tmp_path):
    from aphasia_kb import KnowledgeBase
    directory = tmp_path / 'regions'
    directory.mkdir()
    (directory / 'bad.md').write_text('---\nschema_version: 2.8\nid: bad\nstatus: approved\nfindings: [not-a-mapping]\n---\n')
    kb = KnowledgeBase(tmp_path)
    assert kb.findings.empty
    assert any('findings must be a list' in x for x in kb.issues)
