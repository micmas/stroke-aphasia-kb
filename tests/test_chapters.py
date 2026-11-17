"""Compatibility and chapter isolation, independent of model runs or network."""
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from chapters import membership, select_entry, screening_record
from aphasia_kb import KnowledgeBase
from export_webapp import findings
from screening import stage_of


def test_mixed_paper_has_independent_eligibility():
    candidate = {'chapters': ['aphasia', 'dysphagia'], 'screening': [
        {'stage': 'full_text', 'decision': 'exclude', 'reason': 'not_aphasia'},
        {'chapter': 'dysphagia', 'stage': 'full_text', 'decision': 'include'},
    ]}
    assert stage_of(screening_record(candidate, 'aphasia')) == ('excluded_ft', 'not_aphasia')
    assert stage_of(screening_record(candidate, 'dysphagia')) == ('included', None)
    candidate['screening'].pop()
    assert stage_of(screening_record(candidate, 'dysphagia')) == ('awaiting_ta', None)


@pytest.mark.parametrize('value', [[], None, 'aphasia', ['aphasia', 'aphasia'], ['unknown'], [{}]])
def test_invalid_membership_never_defaults_to_aphasia(value):
    with pytest.raises(ValueError):
        membership({'chapters': value})


def test_legacy_and_override_do_not_mutate_source():
    entry = {'id': 'shared', 'chapters': ['aphasia', 'dysphagia'], 'findings': [
        {'id': 'language', 'chapters': ['aphasia']},
        {'id': 'swallow', 'chapters': ['dysphagia']},
        {'id': 'both'},
    ]}
    assert membership({}) == ['aphasia']
    assert [f['id'] for f in select_entry(entry, 'aphasia')['findings']] == ['language', 'both']
    assert [f['id'] for f in select_entry(entry, 'dysphagia')['findings']] == ['swallow', 'both']
    assert 'chapters' not in entry['findings'][2]


def test_loader_and_export_preserve_ids_and_isolate_findings(tmp_path):
    folder = tmp_path / 'regions'
    folder.mkdir()
    entry = {'schema_version': 2.9, 'id': 'shared_region', 'name': 'Shared region',
             'kind': 'region', 'status': 'approved', 'chapters': ['aphasia', 'dysphagia'],
             'findings': [
                 {'id': 'language', 'chapters': ['aphasia'], 'citation': '@SamePaper'},
                 {'id': 'swallow', 'chapters': ['dysphagia'], 'citation': '@SamePaper'}]}
    path = folder / 'shared.md'
    path.write_text('---\n' + yaml.safe_dump(entry) + '---\n')
    aphasia = KnowledgeBase(tmp_path)
    dysphagia = KnowledgeBase(tmp_path, chapter='dysphagia')
    assert list(aphasia.findings['id']) == ['language']
    assert list(dysphagia.findings['id']) == ['swallow']
    assert list(KnowledgeBase(tmp_path, chapter='all').findings['id']) == ['language', 'swallow']
    exported = findings(aphasia, tmp_path)
    assert exported[0]['chapters'] == ['aphasia']
    assert exported[0]['source_id'] == 'shared_region'
    assert exported[0]['citation'] == '@SamePaper'
    assert len(yaml.safe_load(path.read_text().split('---')[1])['findings']) == 2


def test_legacy_entry_is_not_dysphagia():
    assert select_entry({'id': 'legacy', 'findings': [{'id': 'f'}]}, 'dysphagia') is None
