import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from review_identity import independent
import promote

class Identity(unittest.TestCase):
    def test_real_provenance(self):
        for prefix in ('agent:', 'agent:ollama-extract-cli/', 'agent:ollama-refocus-cli/', 'model:'):
            self.assertFalse(independent(prefix+'gemma4:31b','gemma4:31b'))
            self.assertTrue(independent(prefix+'gemma4:31b','gemma4:26b'))
        self.assertFalse(independent('agent:unknown-tool','gemma4:31b'))
        self.assertTrue(promote.validate_review_args('model:gemma4:31b','A','agent:gemma4:26b',{'created_by':'agent:gemma4:31b'}))
        with self.assertRaises(ValueError): promote.normalize_reviewer('human:')

if __name__=='__main__': unittest.main()
