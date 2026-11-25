#!/usr/bin/env python3
"""Build the shared Stroke KB staging hub; production files are never rewritten."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from build_dysphagia_staging import build as build_screening
from package_export import package_export
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'staging/stroke/dist'
WEB=ROOT/'staging/stroke/web'

def build(exports=None, public=False, reuse_exports=False):
    global DEST
    DEST = ROOT / ('deployment/public-site/dist' if public else 'staging/stroke/dist')
    if not public:
        if not exports: raise ValueError('Staging requires --exports')
        build_screening(exports)
    DEST.mkdir(parents=True,exist_ok=True)
    for path in WEB.iterdir():shutil.copy2(path,DEST/path.name)
    for name in ['styles.css','project-shell.css','project-shell.js','licensing.html','LICENSE.txt']:
        shutil.copy2(ROOT/'explorer'/name,DEST/name)
    shell=(DEST/'project-shell.js').read_text().replace('new URL(url)', 'new URL(url, location.origin)').replace("link('Review portal', 'https://review.aphasia-kb.app/welcome/')", "link('Stroke KB staging', '/')")
    (DEST/'project-shell.js').write_text(shell)
    (DEST/'js').mkdir(exist_ok=True)
    shutil.copy2(ROOT/'js/kb-evidence.js',DEST/'js/kb-evidence.js')
    if not public:
        screening=DEST/'dysphagia/screening';shutil.copytree(ROOT/'staging/dysphagia/dist',screening,dirs_exist_ok=True)
        page=(screening/'index.html').read_text().replace('</head>','<link rel="stylesheet" href="/chapter.css"><script src="/chapter-bar.js"></script></head>')
        (screening/'index.html').write_text(page)
        shutil.copy2(DEST/'project-shell.js',screening/'project-shell.js')
    search=DEST/'dysphagia/search';shutil.copytree(ROOT/'explorer/dysphagia-search',search,dirs_exist_ok=True)
    # Search page uses parent-relative shared assets.
    for name in ['project-shell.css','project-shell.js','styles.css']:shutil.copy2(DEST/name,DEST/'dysphagia'/name)
    page=(search/'index.html').read_text().replace('</head>','<link rel="stylesheet" href="/chapter.css"><script src="/chapter-bar.js"></script></head>')
    (search/'index.html').write_text(page)
    summary=json.loads((ROOT/'screening/dysphagia/import-manifest.json').read_text())
    nav=[('Overview',''),('Findings','findings'),('Matrix','matrix'),('Papers','papers'),('Coverage','coverage'),('Searches','searches'),('Paper licences','licences'),('Methods','models'),('Get involved','involve'),('Review','review')]
    for chapter in ['aphasia','dysphagia']:
        dest=DEST/chapter;dest.mkdir(exist_ok=True)
        for path in (ROOT/'explorer').iterdir():
            if path.is_file():shutil.copy2(path,dest/path.name)
        for name in ['chapter-empty.js', 'dysphagia-coverage.js']:
            shutil.copy2(WEB/name,dest/name)
        shutil.copy2(DEST/'project-shell.js',dest/'project-shell.js')
        html=(dest/'index.html').read_text()
        html=html.replace('Stroke aphasia KB',f'{chapter.capitalize()} KB')
        html=re.sub(r'<meta name="description"[^>]*>',f'<meta name="description" content="Stroke KB staging: {chapter.capitalize()} chapter.">',html)
        html=re.sub(r'<nav class="nav".*?</nav>','<nav class="nav" aria-label="Views">'+''.join(f'<a href="#/{route}">{label}</a>' for label,route in nav)+'</nav>',html,flags=re.S)
        if chapter=='dysphagia':html=re.sub(r'<aside.*?</aside>','',html,flags=re.S)
        else:html=html.replace('https://review.aphasia-kb.app/#/drafts','?kb=drafts#/findings')
        html=html.replace('</head>','<meta name="robots" content="noindex,nofollow"><link rel="stylesheet" href="/chapter.css"><script src="/chapter-bar.js"></script></head>')
        if chapter=='dysphagia':html=html.replace('</head>',f'<script>window.DYSPHAGIA_IMPORT={json.dumps(summary)};</script></head>')
        (dest/'index.html').write_text(html)
        app=(dest/'app.js').read_text()
        app="import {initEmptyChapter,renderChapterExtra} from './chapter-empty.js';\n"+app
        app=app.replace("'../export/", "'/aphasia/export/")
        app=app.replace('function init() {',"function init() {\n  if(window.STROKE_CHAPTER==='dysphagia'){initEmptyChapter({prismaDiagram});return;}")
        app=app.replace('function render() {',"function render() {\n  if(renderChapterExtra(window.STROKE_CHAPTER,{prismaDiagram}))return;")
        app=app.replace('portalNav(state.index.kb.portal);','// Staging uses the chapter Review hub rather than a silent production link.')
        (dest/'app.js').write_text(app)
    export=DEST/'aphasia/export';export.mkdir(exist_ok=True)
    for name,statuses in [('stroke-aphasia-kb.json','approved'),('stroke-aphasia-kb-drafts.json','approved,in_review,draft')]:
        if reuse_exports: shutil.copy2(ROOT/'export'/name,export/name)
        else: subprocess.run([sys.executable,str(ROOT/'scripts/export_webapp.py'),'--include',statuses,'--out',str(export/name)],cwd=ROOT,check=True)
        package_export(export/name)
    shutil.copy2(ROOT/'export/model-benchmark.json',export/'model-benchmark.json')
    # No data export is created for Dysphagia. Its evidence sections cannot load Aphasia data.
    (DEST/'_headers').write_text('/*\n  Cache-Control: no-store\n  X-Robots-Tag: noindex, nofollow\n')
    if public:
        prepare_public(DEST)
    print(f'Stroke KB site built at {DEST}')

def prepare_public(dest):
    # Only public templates and evidence exports are present; never copy screening data.
    forbidden = list(dest.rglob('records*.json'))
    if forbidden or (dest/'dysphagia/screening').exists():
        raise ValueError('Private screening assets found in public output')
    for p in dest.rglob('*'):
        if p.suffix not in ('.html','.js','.css'): continue
        text=p.read_text()
        text=text.replace('STAGING · Stroke KB','Stroke KB').replace(' · staging','').replace('Stroke KB staging','Stroke KB')
        text=text.replace('staging explorer','explorer').replace('staging workspace','screening workspace')
        text=text.replace('Aphasia review portal (production)','Aphasia review portal')
        text=text.replace('<meta name="robots" content="noindex,nofollow">','')
        text=text.replace('/dysphagia/screening/', 'https://review.dysphagia-kb.app/')
        if p.name=='project-shell.js':text=text.replace("link('Stroke KB', '/')","link('Review portal', 'https://review.aphasia-kb.app/welcome/')")
        if p.name=='chapter-bar.js':
            text=text.replace("['Stroke KB home','/',null]", "['Stroke KB home','https://stroke-kb.app/',null]").replace("['Aphasia','/aphasia/','aphasia']","['Aphasia','https://stroke-kb.app/aphasia/','aphasia']").replace("['Dysphagia','/dysphagia/','dysphagia']","['Dysphagia','https://dysphagia-kb.app/','dysphagia']")
            text=text.replace("window.STROKE_CHAPTER=chapter;", "window.STROKE_CHAPTER=chapter;\nif(location.hostname==='dysphagia-kb.app' && location.pathname==='/') location.replace('/dysphagia/'+location.search+location.hash);")
        p.write_text(text)
    (dest/'_headers').write_text('/*\n  Cache-Control: no-cache\n  X-Content-Type-Options: nosniff\n')
    (dest/'_redirects').write_text('/dysphagia/screening/* https://review.dysphagia-kb.app/:splat 302\n')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--exports',type=Path);p.add_argument('--public',action='store_true');p.add_argument('--reuse-exports',action='store_true');args=p.parse_args();build(args.exports,args.public,args.reuse_exports)
