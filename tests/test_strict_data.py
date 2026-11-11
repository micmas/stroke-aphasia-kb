import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from strict_data import DuplicateKeyError,load_yaml,load_json
import extract
from aphasia_kb import parse_markdown


def test_duplicate_passages_are_not_silently_discarded(tmp_path):
    content='---\nid: example\nfindings:\n- id: f1\n  source_passages: [{quote: first}]\n  source_passages: [{quote: second}]\n---\n'
    path=tmp_path/'source.md';path.write_text(content)
    with pytest.raises(DuplicateKeyError,match='source_passages'):parse_markdown(path)
    draft={'bucket':'regions','filename':'example.md','content':content}
    with pytest.raises(DuplicateKeyError):extract.save_drafts([draft],tmp_path/'out')
    assert not (tmp_path/'out/drafts').exists()
    assert path.read_text()==content


def test_duplicate_json_model_fields_fail():
    with pytest.raises(DuplicateKeyError):
        extract.parse_response('{"drafts": [], "drafts": [{"content":"lost"}]}')
    with pytest.raises(DuplicateKeyError):load_json('{"a":{"value":1,"value":2}}')


def test_distinct_findings_and_explicit_merge_remain_valid():
    assert load_yaml('findings:\n- id: f1\n- id: f2')['findings'][1]['id']=='f2'
    assert load_yaml('base: &b {name: old}\nentry: {<<: *b, name: new}')['entry']['name']=='new'
