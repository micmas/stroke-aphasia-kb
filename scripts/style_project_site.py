#!/usr/bin/env python3
"""Add shared navigation and themes to generated HTML, without changing results."""
import argparse
import os
from pathlib import Path
import shutil


def style_site(site: Path) -> int:
    source = Path(__file__).resolve().parents[1] / 'explorer'
    for name in ('project-shell.css', 'project-shell.js'):
        shutil.copy2(source / name, site / name)
    count = 0
    for page in site.rglob('*.html'):
        text = page.read_text(encoding='utf-8')
        if 'project-shell.js' in text or '</head>' not in text:
            continue
        prefix = Path(os.path.relpath(site, page.parent)).as_posix()
        assets = f'<link rel="stylesheet" href="{prefix}/project-shell.css">\n<script src="{prefix}/project-shell.js"></script>\n'
        page.write_text(text.replace('</head>', assets + '</head>', 1), encoding='utf-8')
        count += 1
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    args = parser.parse_args()
    print(f'Added shared navigation and themes to {style_site(args.site)} HTML pages.')
