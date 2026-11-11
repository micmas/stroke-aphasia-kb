import sys
from pathlib import Path
from unittest.mock import patch
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import promotion_transaction as T


def test_retry_after_canonical_write_does_not_duplicate(tmp_path):
    draft = tmp_path / 'drafts/regions/x.md'
    draft.parent.mkdir(parents=True)
    draft.write_text('draft')
    canonical = tmp_path / 'regions/x.md'
    log = tmp_path / 'logs/audit.md'
    write = T.atomic_write
    def fail_log(path, text):
        if path == log:
            raise OSError('disk failure')
        write(path, text)
    with patch.object(T, 'atomic_write', fail_log), pytest.raises(OSError):
        T.commit(tmp_path, draft, canonical, 'one finding', log, 'approved\n')
    assert draft.exists() and canonical.read_text() == 'one finding'
    assert T.recover_pending(tmp_path, draft)
    assert not draft.exists() and canonical.read_text() == 'one finding'
    assert log.read_text().count('approved') == 1
    assert not T.recover_pending(tmp_path, draft)
    draft.write_text('draft')
    with pytest.raises(ValueError, match='already promoted'):
        T.commit(tmp_path, draft, canonical, 'duplicate', log, 'approved\n')
