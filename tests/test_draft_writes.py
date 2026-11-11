import sys,tempfile,unittest,yaml
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from extract import save_drafts
class Drafts(unittest.TestCase):
    def test_boundary_and_validation(self):
        fm={'id':'x','status':'approved','reviewer':'human:fake','findings':[{'id':'f1','review':{'reviewer':'human:fake'}}]}
        def d(name,content=None): return {'bucket':'regions','filename':name,'content':content or '---\n'+yaml.safe_dump(fm)+'---\n'}
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)
            for name in ('../../regions/x.md','/tmp/escape.md'):
                with self.assertRaises(ValueError): save_drafts([d(name)],root)
            with self.assertRaises(yaml.YAMLError): save_drafts([d('x.md','---\na: [""x""]\n---\n')],root)
            self.assertFalse((root/'drafts/regions/x.md').exists())
            paths=save_drafts([d('x.md')],root)
            text=paths[0].read_text(); self.assertIn('status: draft',text); self.assertNotIn('reviewer:',text)
            with self.assertRaises(ValueError): save_drafts([d('x.md')],root)
            self.assertEqual(paths[0].read_text(),text)
if __name__=='__main__': unittest.main()
