import sys,tempfile,unittest,yaml
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import refocus as R
class Marks(unittest.TestCase):
    def test_same_local_id_gets_distinct_prompt_identity(self):
        with tempfile.TemporaryDirectory() as t:
            paths=[]
            for name in ('left','right'):
                p=Path(t)/(name+'.md'); p.write_text('---\n'+yaml.safe_dump({'reviewer_marks':[{'id':'m1','quote':name}]})+'---\n'); paths.append(p)
            marks=R.pending_marks(paths)
            self.assertEqual(len({m['id'] for _,m in marks}),2)
            self.assertTrue(all(m['_local_id']=='m1' for _,m in marks))
            self.assertEqual(R.pending_marks(paths),marks)
if __name__=='__main__': unittest.main()
