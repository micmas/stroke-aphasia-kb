import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_stroke_staging import prepare_public
class PublicBuild(unittest.TestCase):
 def test_private_records_refused(self):
  with tempfile.TemporaryDirectory() as path:
   p=Path(path);(p/'records-000.json').write_text('[]')
   with self.assertRaises(ValueError):prepare_public(p)
 def test_screening_redirects_to_authenticated_host(self):
  with tempfile.TemporaryDirectory() as path:
   p=Path(path);(p/'index.html').write_text('<a href="/dysphagia/screening/">screen</a> STAGING · Stroke KB')
   prepare_public(p)
   self.assertIn('https://review.dysphagia-kb.app/',(p/'index.html').read_text())
   self.assertNotIn('STAGING',(p/'index.html').read_text())
