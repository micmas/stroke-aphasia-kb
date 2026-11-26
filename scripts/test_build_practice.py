import copy,json,unittest
from pathlib import Path
from build_practice import deduplicate,ROOT

def row(doi='',pmid='',n=1,title='Meaningful outcomes'):
    return dict(doi=doi,pmid=pmid,title=title,year='2024',authors=['Smith, A'],journal='Journal',abstract='Abstract',sources=[dict(file='test.ris',record=n)])
class PracticeImportTests(unittest.TestCase):
    def test_duplicates_retain_every_source(self):
        rows=[row(doi='10.1/a',n=1),row(doi='10.1/a',n=2)]
        unique=deduplicate(copy.deepcopy(rows))
        self.assertEqual(len(unique),1)
        self.assertEqual(len(unique[0]['sources']),2)
        self.assertEqual(unique[0]['id'],deduplicate(copy.deepcopy(rows))[0]['id'])
    def test_conflicting_and_ambiguous_identifiers_remain_separate(self):
        self.assertEqual(len(deduplicate([row(doi='10.1/a'),row(doi='10.1/b',n=2),row(n=3)])),3)
        self.assertEqual(len(deduplicate([row(doi='10.1/a',pmid='1'),row(doi='10.1/a',pmid='2',n=2)])),2)
    def test_import_has_complete_provenance_and_no_count_warnings(self):
        base=ROOT/'staging/practice/dist'
        if not (base/'records.json').exists():self.skipTest('Private import unavailable')
        data=json.loads((base/'records.json').read_text())
        rows=[r for chunk in data['chunks'] for r in json.loads((base/chunk).read_text())]
        self.assertEqual(len(rows),data['summary']['unique_records'])
        self.assertEqual(sum(len(r['sources']) for r in rows),data['summary']['raw_records'])
        self.assertEqual(len({r['id'] for r in rows}),len(rows))
        self.assertEqual(data['summary']['warnings'],[])
    def test_public_build_has_no_private_queues(self):
        base=ROOT/'deployment/public-site/dist'
        if not base.exists():self.skipTest('Public build unavailable')
        self.assertEqual(list(base.rglob('records*.json')),[])
        self.assertFalse(any(p.name=='screening' for p in base.rglob('*') if p.is_dir()))
        self.assertTrue((base/'practice/practice.js').exists())
if __name__=='__main__':unittest.main()
