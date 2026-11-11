import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from quote_check import grade_quote, PaperText
from auto_review import check_pdf_quote_match
class Quotes(unittest.TestCase):
    def test_elisions(self):
        a='Participants were examined after their first stroke.'; b='Follow-up measurements were collected after six months.'
        paper=PaperText.from_text(a+' '+b)
        self.assertEqual(grade_quote(a+' [...] '+b,paper),'elided')
        self.assertEqual(grade_quote(a+' [...] cured everyone [...] '+b,paper),'absent')
        self.assertEqual(grade_quote(b+' [...] '+a,paper),'absent')
    def test_numbers_and_typography(self):
        self.assertNotEqual(grade_quote('There were 12 participants.',PaperText.from_text('There were 1–2 participants.')),'exact')
        self.assertEqual(grade_quote('Significant findings in follow-up.',PaperText.from_text('Signiﬁcant ﬁndings in follow-\nup.')),'exact')
        prefix='The study examined participants over several years after their stroke. '
        self.assertEqual(grade_quote(prefix+'invented '*100,PaperText.from_text(prefix+'No change.')),'absent')
    def test_absent_and_missing(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t); (p/'X.txt').write_text('This is the real sentence.')
            fm={'findings':[{'citation':'@X','source_passages':[{'quote':'This is the real sentence.'}]*4+[{'quote':'Unicorns healed everyone.'}]}]}
            self.assertIs(check_pdf_quote_match(fm,p).passed,False)
            fm['findings'][0]['source_passages'].pop()
            fm['findings'].append({'citation':'@Missing','source_passages':[{'quote':'Anything'}]})
            self.assertIsNone(check_pdf_quote_match(fm,p).passed)
if __name__=='__main__': unittest.main()
