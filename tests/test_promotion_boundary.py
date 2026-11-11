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
