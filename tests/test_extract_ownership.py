import sys
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import extract_ready as E

def test_dirty_managed_paths_stop_before_any_work(tmp_path):
    (tmp_path / 'papers').mkdir()
    with patch.object(E, 'ROOT', tmp_path), patch.object(E.subprocess, 'run', return_value=SimpleNamespace(stdout=' M drafts/regions/human.md\n')) as git, patch.object(E, '_run') as run:
        assert E.execute(None, None, True, False) == 2
        run.assert_not_called()
        assert git.call_count == 1
