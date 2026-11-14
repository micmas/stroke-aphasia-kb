"""Safety boundaries for literal evidence, not model-accuracy tests."""
import copy
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import relationship_evidence as evidence


def test_missing_and_duplicate_classifications_never_become_accepted_labels():
    labels, issues = evidence.classify_rows({'items': [
        {'id': 'a', 'kind': 'current_result'}, {'id': 'a', 'kind': 'methods'},
        {'id': 'b', 'kind': 'population_or_timing'},
        {'id': 'invented', 'kind': 'current_result'}]}, {'a', 'b', 'c'})
    assert labels == {'b': 'population_or_timing'}
    assert any('a: duplicate' in x for x in issues)
    assert any('c: unclassified' in x for x in issues)


def test_original_offsets_and_full_qualifiers_survive_pairing():
    full = 'The effect was positive, but not after adjustment.'
    short = 'The effect was positive, but'
    units = {'P1-S1': {'page': 1, 'text': short}, 'P1-S2': {'page': 1, 'text': full}}
    arm = {'schema_version': 'source-evidence-v1', 'tables': [], 'passages': [
        {'id': k+'-C1', 'source_id': k, 'page': 1, 'text': u['text'],
         'source_start': 0, 'source_end': len(u['text']), 'classification': 'current_result'}
        for k,u in units.items()]}
    packet = evidence.pair_evidence(arm, copy.deepcopy(arm), units)
    a,b = packet['passages']
    assert a['hidden_by_default'] and a['superseded_by'] == b['evidence_id']
    assert b['source']['text'] == full and not b['hidden_by_default']
    changed = copy.deepcopy(arm)
    changed['passages'][1]['text'] = 'The effect was positive.'
    with pytest.raises(ValueError, match='differ'):
        evidence.pair_evidence(arm, changed, units)


def test_repeated_roi_rows_keep_laterality_and_unresolved_headers():
    table = {'columns': [{'path': ['Side']}, {'path': ['Fraction']}], 'rows': [
        {'path': ['Naming', 'SLF'], 'cells': ['L', '4.2']},
        {'path': ['Naming', 'SLF'], 'cells': ['R', '1.1']}], 'notes': []}
    same = evidence.table_packet(table, table, 'T1', 'Caption', 1)
    assert len(same['facts']) == 4
    assert all(f['status'] == 'literal_agreement' and not f['approved'] for f in same['facts'])
    swapped = copy.deepcopy(table)
    swapped['rows'].reverse()
    mismatch = evidence.table_packet(table, swapped, 'T1', 'Caption', 1)
    assert all(f['status'] != 'literal_agreement' for f in mismatch['facts'])
    changed = copy.deepcopy(table)
    for row in changed['rows']:
        row['path'][0] = 'Repetition'
    mismatch = evidence.table_packet(table, changed, 'T1', 'Caption', 1)
    assert all(f['status'] != 'literal_agreement' for f in mismatch['facts'])


@pytest.mark.parametrize('text', [
    'Over-ﬁtting may affect this estimate (p b 0.001).',
    'Potential 1CS may be limited. Significant predictors are highlighted in bold. of the main hypotheses was confirmed.',
])
def test_damaged_glyphs_and_ligature_limitations_are_flagged_not_rewritten(text):
    units = {'P1-S1': {'page': 1, 'text': text}}
    rows = [{'evidence_id': 'x', 'source': {'source_id': 'P1-S1', 'source_start': 0, 'page': 1,
             'source_end': len(text), 'text': text}, 'classifications': {'A':'methods','B':'methods'}}]
    evidence.annotate_passages(rows, units)
    assert rows[0]['display_requires_pdf_check']
    if 'Over-ﬁtting' in text:
        assert rows[0]['contains_limitation'] and rows[0]['review_backstop']
    else:
        assert rows[0]['contains_caption_boundary'] and rows[0]['context_review_required']
    assert rows[0]['source']['text'] == text
