"""Build Dysphagia from the shared Aphasia review UI, with an empty findings export.

Screening records, decisions and PDFs remain in Dysphagia's private storage.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import shutil
ROOT=Path(__file__).resolve().parents[1]
def build():
 dest=ROOT/'deployment/dysphagia-review/dist'
 if dest.exists():shutil.rmtree(dest)
 dest.mkdir(parents=True)
 for path in (ROOT/'portal/web').iterdir():
  if path.is_file():shutil.copy2(path,dest/path.name)
 page=dest/'index.html'
 page.write_text(page.read_text().replace('<html lang="en">','<html lang="en" data-chapter="dysphagia">').replace('Stroke aphasia KB','Stroke dysphagia KB').replace('https://aphasia-kb.app/','https://dysphagia-kb.app/'))
 for source,target in [('styles.css','explorer-styles.css'),('load-export.js','load-export.js'),('project-shell.js','project-shell.js'),('project-shell.css','project-shell.css')]:
  shutil.copy2(ROOT/'explorer'/source,dest/target)
 (dest/'_headers').write_text('/*\n  Cache-Control: no-store\n  X-Robots-Tag: noindex, nofollow\n')
 vendor=ROOT/'portal/node_modules/pdfjs-dist/build'
 (dest/'vendor').mkdir()
 for name in ['pdf.min.mjs','pdf.worker.min.mjs']:shutil.copy2(vendor/name,dest/'vendor'/name)
 (dest/'manifest.json').write_text(json.dumps({'chapter':'dysphagia','built':dt.datetime.now(dt.timezone.utc).isoformat(),'papers':{},'fulltext':{},'sources':{'keys':[]},'counts':{'private':0,'public':0,'sources':0},'config':{'explorerUrl':'https://dysphagia-kb.app/'}}))
 print(dest)
if __name__=='__main__':build()
