"""Build the dedicated Dysphagia review site; all search records remain in private R2."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
def build():
 dest=ROOT/'deployment/dysphagia-review/dist'
 if dest.exists():shutil.rmtree(dest)
 dest.mkdir(parents=True)
 for path in (ROOT/'staging/dysphagia/web').iterdir():
  text=path.read_text().replace(' · screening staging',' · screening').replace('Staging · ','').replace('staging workspace','Dysphagia review workspace').replace('staging branch','chapter').replace('dysphagia-staging:','dysphagia-production:')
  if path.name=='index.html':text=text.replace('<main>', '<p style="padding:0 24px"><a href="https://dysphagia-kb.app/">Dysphagia KB</a> · <a href="https://stroke-kb.app/">Stroke KB home</a></p><main>')
  (dest/path.name).write_text(text)
 for name in ['project-shell.js','project-shell.css']:
  text=(ROOT/'explorer'/name).read_text().replace("link('Review portal', 'https://review.aphasia-kb.app/welcome/')","link('Dysphagia review', 'https://review.dysphagia-kb.app/')")
  (dest/name).write_text(text)
 (dest/'_headers').write_text('/*\n  Cache-Control: no-store\n  X-Robots-Tag: noindex, nofollow\n')
 print(dest)
if __name__=='__main__':build()
