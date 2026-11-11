"""Recoverable, serialized promotion writes. Journals survive process interruption."""
import hashlib
import json
from pathlib import Path
from pipeline_files import atomic_write, BUCKETS


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def recover(root, journal):
    record = json.loads(journal.read_text())
    if record['done']:
        return
    draft, canonical, log = (root / record[k] for k in ('draft', 'canonical', 'log'))
    # A journal must never be a route outside this repository.
    for path in (draft, canonical, log):
        path.resolve().relative_to(root.resolve())
    if draft.relative_to(root).parts[:1] != ('drafts',) or canonical.relative_to(root).parts[0] not in BUCKETS:
        raise ValueError('Invalid promotion journal destination')
    if digest(draft) not in (record['draft_sha'], None):
        raise ValueError('Draft changed during pending promotion; preserve it for manual recovery')
    current = digest(canonical)
    if current not in (record['before'], record['after']):
        raise ValueError('Canonical changed during pending promotion; manual recovery required')
    if current != record['after']:
        atomic_write(canonical, record['text'])
    old_log = log.read_text() if log.exists() else ''
    marker = f" | operation: {journal.stem}"
    if marker not in old_log:
        atomic_write(log, old_log + record['line'].rstrip('\n') + marker + '\n')
    if draft.exists():
        draft.unlink()
    record['done'] = True
    record.pop('text')
    atomic_write(journal, json.dumps(record, indent=2) + '\n')


def commit(root, draft, canonical, text, log, line):
    original = digest(draft)
    operation = hashlib.sha256((str(draft.relative_to(root)) + ':' + original).encode()).hexdigest()
    journal = root / 'logs/promotion_transactions' / (operation + '.json')
    record = dict(draft=str(draft.relative_to(root)), canonical=str(canonical.relative_to(root)),
                  log=str(log.relative_to(root)), draft_sha=original, before=digest(canonical),
                  after=hashlib.sha256(text.encode()).hexdigest(), text=text, line=line, done=False)
    if journal.exists():
        saved = json.loads(journal.read_text())
        if saved['done']:
            raise ValueError('This exact draft was already promoted; refusing duplicate evidence')
    else:
        atomic_write(journal, json.dumps(record, indent=2) + '\n')
    recover(root, journal)


def recover_pending(root, draft):
    resumed = False
    for journal in sorted((root / 'logs/promotion_transactions').glob('*.json')):
        record = json.loads(journal.read_text())
        if not record['done']:
            recover(root, journal)
            resumed |= record['draft'] == str(draft.relative_to(root))
    return resumed
