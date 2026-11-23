import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_dysphagia_staging import records,convert,deduplicate

class ImportTests(unittest.TestCase):
    def test_nbib_book_and_continuation(self):
        parsed=list(records('PMID- 123\nBTI - A book\nAB  - First\n      second\nDP  - 2023\n',True))
        r=convert(parsed[0],True)
        self.assertEqual(r['title'],'A book');self.assertEqual(r['abstract'],'First second')
        self.assertEqual(r['pmid'],'123')
    def test_ris_accession_is_not_pmid(self):
        r=convert(next(records('TY  - JOUR\nTI  - Test\nAN  - 12345678\nER  -\n')),False)
        self.assertEqual(r['pmid'],'')
    def test_incomplete_ris_rejected(self):
        with self.assertRaises(ValueError):list(records('TY  - JOUR\nTI  - Test\n'))
    def row(self,doi='',pmid='',source=1):
        return dict(title='Example study',year=2020,authors=['Smith, A'],doi=doi,pmid=pmid,abstract='',journal='',sources=[dict(file='a.ris',record=source,database='a')])
    def test_sources_kept_and_conflicting_dois_retained(self):
        rows=deduplicate([self.row('10.1/a',source=1),self.row('10.1/a',source=2),self.row('10.1/b',source=3)])
        self.assertEqual(len(rows),2);self.assertEqual(len(rows[0]['sources']),2)
        self.assertNotEqual(rows[0]['id'],rows[1]['id'])
    def test_blank_identifiers_not_matched(self):
        a=self.row();b=self.row(source=2);b['title']='Other study'
        self.assertEqual(len(deduplicate([a,b])),2)
if __name__=='__main__':unittest.main()
