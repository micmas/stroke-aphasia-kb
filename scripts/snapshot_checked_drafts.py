"""Copy completed source-checked drafts into a publishing checkout without overwriting reviews."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import yaml

def snapshot(run_dir, source_repo, destination):
    audit = destination / 'logs/publication/current-drafts.json'
    previous = json.loads(audit.read_text()) if audit.exists() else {'files': {}}
    records = previous['files']
    added = []
    changed = []
    for status_path in sorted(run_dir.glob('*/*/status.json')):
        try:
            status = json.loads(status_path.read_text())
        except (OSError, ValueError):
            continue  # A writer may be replacing this file.
        if status.get('status') != 'draft' or not status.get('path'):
            continue
        rel = Path(status['path'])
        if rel.is_absolute() or '..' in rel.parts or rel.parts[0] != 'drafts':
            raise ValueError(f'Unsafe draft path: {rel}')
        src = source_repo / rel
        if not src.is_file():
            continue
        content = src.read_bytes()
        sha = hashlib.sha256(content).hexdigest()
        key = rel.as_posix()
        # Published versions may have been edited, rejected or promoted by a person.
        # Never re-import or overwrite them, even if the draft was moved.
        if key in records:
            if records[key]['source_sha256'] != sha:
                changed.append(key)
            continue
        dest = destination / rel
        if dest.exists():
            raise ValueError(f'Unregistered destination already exists: {key}')
        fm = yaml.safe_load(content.decode().split('---', 2)[1])
        if fm.get('status') != 'draft' or len(fm.get('findings', [])) != 1:
            raise ValueError(f'Expected one unapproved finding: {key}')
        # Re-read the status and content to avoid capturing an in-progress replacement.
        if src.read_bytes() != content or json.loads(status_path.read_text()) != status:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
        records[key] = {'source_sha256': sha, 'paper': status_path.parent.parent.name,
                        'candidate': status_path.parent.name}
        added.append(key)
    if added or not audit.exists():
        audit.parent.mkdir(parents=True, exist_ok=True)
        audit.write_text(json.dumps({
            'snapshot_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'archive_tag': 'archive/pre-core-drafts-2026-11-20',
            'approved_by_snapshot': False,
            'files': records,
        }, indent=2) + '\n')
    return {'added': len(added), 'published_source_records': len(records),
            'papers': len({v['paper'] for v in records.values()}),
            'changed_source_versions_not_overwritten': changed}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-dir', type=Path, required=True)
    p.add_argument('--source-repo', type=Path, required=True)
    p.add_argument('--destination', type=Path, default=Path(__file__).resolve().parents[1])
    a = p.parse_args()
    if a.source_repo.resolve() == a.destination.resolve():
        p.error('Use a separate publishing checkout; never snapshot into the running output repository.')
    print(json.dumps(snapshot(a.run_dir, a.source_repo, a.destination), indent=2))
