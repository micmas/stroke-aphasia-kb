import json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import ollama_client as O
import recheck_drafts as R
from test_recheck import draft
class Recovery(unittest.TestCase):
    def test_loop_raises_recoverable_exception(self):
        class Resp:
            def __enter__(self): return self
            def __exit__(self,*a): pass
            def __iter__(self):
                for _ in range(128): yield json.dumps({'message':{'content':'x'*40}}).encode()
        with patch.object(O,'model_capabilities',return_value=[]),patch.object(O.urllib.request,'urlopen',return_value=Resp()):
            with self.assertRaises(O.RepetitionLoop) as cm: O.chat('fake',verbose=False)
            self.assertTrue(cm.exception.partial)
    def test_exception_restores_drafts(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); p=root/'drafts/regions/x__X.md'; draft(p,'X','test')
            before=p.read_bytes(); row={'key':'X','paths':[p],'pdf':root/'papers/X.pdf'}
            def fail(*a): raise OSError('fake disk failure')
            with self.assertRaises(OSError): R.rewrite(row,'test',None,1,extract=fail,drafts=root/'drafts',papers=root/'papers',backup=root/'backup')
            self.assertEqual(p.read_bytes(),before)
if __name__=='__main__': unittest.main()
