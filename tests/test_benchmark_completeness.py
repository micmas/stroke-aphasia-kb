import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import benchmark_models as B
import compare_extraction as C
class Benchmark(unittest.TestCase):
    def test_empty_is_ineligible(self):
        r={'model':'x','paper':'P','findings':0,'quotes':0,'absent':0,'schema_issues':0}
        self.assertFalse(B.summarise([r],'x')['x']['eligible'])
    def test_subset_preserves_published_results(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'summary.json'; old='{"papers":[{"key":"Old"}]}' ; p.write_text(old)
            with self.assertRaises(ValueError): B.publish([],{},'x',['New'],None,'test',path=p)
            self.assertEqual(p.read_text(),old)
    def test_all_buckets_and_missing_papers(self):
        self.assertIn('reviews',C.BUCKETS); self.assertIn('ingredients',C.BUCKETS)
        with tempfile.TemporaryDirectory() as t:
            r=C._quote_check([{'citation':'@Missing','source_passages':[{'quote':'X'}]}],Path(t))
            self.assertEqual(r['missing_papers'],['@Missing'])
if __name__=='__main__': unittest.main()
