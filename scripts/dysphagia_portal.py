"""Fetch/build the protected Dysphagia screen without changing the Aphasia register."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'portal/.dysphagia-cache'
BUCKET='stroke-aphasia-kb-pdfs'
PREFIX='private/dysphagia-screening/'

def fetch():
    CACHE.mkdir(exist_ok=True)
    def get(name):
        if '/' in name or not name.endswith('.json'):raise ValueError('Invalid asset name')
        subprocess.run(['npx','wrangler','r2','object','get',f'{BUCKET}/{PREFIX}{name}','--file',str(CACHE/name),'--remote'],cwd=ROOT/'portal',check=True)
    get('records.json')
    for name in json.loads((CACHE/'records.json').read_text())['chunks']:get(name)

def attach(dest):
    manifest=json.loads((CACHE/'records.json').read_text())
    target=dest/'dysphagia';target.mkdir(parents=True,exist_ok=True)
    for name in ['records.json']+manifest['chunks']:
        if '/' in name:raise ValueError('Invalid asset path')
        shutil.copy2(CACHE/name,target/name)
    for path in (ROOT/'staging/dysphagia/web').iterdir():
        text=path.read_text().replace(' · screening staging',' · screening').replace('Staging · ','').replace('staging workspace','screening workspace').replace('staging branch','chapter').replace("'/api/decisions'","'/api/dysphagia-decisions'").replace('dysphagia-staging:', 'dysphagia-production:')
        if path.name=='index.html':text=text.replace('<main>', '<p style="padding:0 24px"><a href="/">Aphasia review</a> · <a href="https://stroke-kb.app/dysphagia/">Dysphagia KB</a></p><main>')
        (target/path.name).write_text(text)
    for name in ['project-shell.js','project-shell.css']:shutil.copy2(ROOT/'explorer'/name,target/name)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--fetch',action='store_true');p.add_argument('--out',type=Path);args=p.parse_args()
    if args.fetch:fetch()
    if args.out:attach(args.out)
