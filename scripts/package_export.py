#!/usr/bin/env python3
"""Split deployment copies of large exports; keep repository exports intact."""
import argparse
import hashlib
import json
from pathlib import Path

LIMIT = 20 * 1024 * 1024  # Leave headroom below the hosting per-file limit.
PART_BYTES = 4 * 1024 * 1024


def package_export(path, limit=LIMIT, part_bytes=PART_BYTES):
    path = Path(path)
    raw = path.read_bytes()
    if len(raw) <= limit:
        return False
    # Validate before replacing the deployment copy. Parts hold exact UTF-8 bytes.
    parsed = json.loads(raw)
    if isinstance(parsed, dict) and parsed.get('_kb_json_parts') == 1:
        return False
    digest = hashlib.sha256(raw).hexdigest()
    parts = []
    start = 0
    while start < len(raw):
        end = min(start + part_bytes, len(raw))
        while end < len(raw) and raw[end] & 0xC0 == 0x80:
            end -= 1
        if end == start:
            raise ValueError('Part size cannot contain one UTF-8 character')
        name = f'{path.name}.{digest}.{len(parts):03d}.txt'
        (path.parent / name).write_bytes(raw[start:end])
        parts.append(name)
        start = end
    path.write_text(json.dumps({'_kb_json_parts': 1, 'parts': parts,
                               'bytes': len(raw), 'sha256': digest}), encoding='utf-8')
    for old in path.parent.glob(f'{path.name}.*.txt'):
        if old.name not in parts:
            old.unlink()
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='+', type=Path)
    for path in parser.parse_args().paths:
        if package_export(path):
            print(f'Packaged {path} into bounded download parts')
