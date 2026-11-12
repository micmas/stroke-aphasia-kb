import sys
from pathlib import Path
from unittest.mock import patch
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import ollama_client as O

def test_locality_and_remote_prompt_refusal():
    for host in ('http://localhost:11434', 'http://127.0.0.1:11434', 'http://[::1]:11434'):
        assert O.is_local(host)
    for host in ('https://localhost.example.invalid', 'https://example.invalid/127.0.0.1', 'http://0.0.0.0:11434'):
        assert not O.is_local(host)
        with patch.object(O.urllib.request, 'urlopen') as request, pytest.raises(O.OllamaError):
            O.chat('restricted paper text', host=host)
        request.assert_not_called()
    with pytest.raises(O.OllamaError):
        O.chat('restricted paper text', model='example:cloud')
