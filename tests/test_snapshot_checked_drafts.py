"""Publication repairs must survive later recovery output without duplication."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from snapshot_checked_drafts import snapshot


class SnapshotRepairTests(unittest.TestCase):
    def test_recovery_cannot_duplicate_or_overwrite_manual_repair(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run, source, dest = (root / name for name in ('run', 'source', 'dest'))
            repair = 'drafts/regions/repaired__Paper__R001.md'
            original = dest / repair
            original.parent.mkdir(parents=True)
            original.write_text('Preserved corrected publication copy')
            ledger = dest / 'logs/publication/current-drafts.json'
            ledger.parent.mkdir(parents=True)
            ledger.write_text(json.dumps({'files': {repair: {
                'source_sha256': None, 'paper': 'Paper', 'candidate': 'R001',
                'manual_repair': True,
            }}}))
            for candidate in ('R001', 'R002'):
                rel = f'drafts/regions/regenerated__Paper__{candidate}.md'
                path = source / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('---\nstatus: draft\nfindings: [{id: f1}]\n---\n')
                status = run / 'Paper' / candidate / 'status.json'
                status.parent.mkdir(parents=True)
                status.write_text(json.dumps({'status': 'draft', 'path': rel}))
            result = snapshot(run, source, dest)
            self.assertEqual(result['added'], 1)
            self.assertEqual(original.read_text(), 'Preserved corrected publication copy')
            self.assertFalse((dest / 'drafts/regions/regenerated__Paper__R001.md').exists())
            self.assertTrue((dest / 'drafts/regions/regenerated__Paper__R002.md').exists())
            self.assertEqual(snapshot(run, source, dest)['added'], 0)


if __name__ == '__main__':
    unittest.main()
