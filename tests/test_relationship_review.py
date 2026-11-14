"""Review gates prevent unsupported labels and interpretation escaping unflagged."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from relationship_review import gate_unit, worklist, proposal_schema
import jsonschema


def fixture(text, tags=()):
    row = {'evidence_id': 'P1', 'source': {'text': text, 'page': 1},
           'classifications': {'A': 'current_result', 'B': 'current_result'},
           'search_tags': tags}
    unit = {'evidence_ids': ['P1'], 'qualifier_ids': [], 'context_ids': [], 'table_ids': [],
            'exposure': {'text': 'age', 'source_id': 'P1'},
            'outcome': {'text': 'score', 'source_id': 'P1'}, 'roles': [],
            'direction': 'not_stated', 'direction_source_id': '', 'effect_unit': 'individual',
            'relation': 'association', 'origin': 'current_study', 'result_status':'reported_detected',
            'outcome_type':'status_at_assessment'}
    return row, unit


def test_joint_model_statistic_is_not_individual_age_effect():
    row, unit = fixture('The model with age explained score variance (R2 = 0.5).')
    flags, _ = gate_unit(unit, {'P1': row}, {'P1'}, {})
    assert 'possible_joint_as_individual' in flags
    unit['exposure']['text'] = 'education'
    assert 'nonverbatim_or_missing_label' in gate_unit(unit, {'P1': row}, {'P1'}, {})[0]


def test_feature_importance_and_unpublished_claims_remain_flagged():
    row, unit = fixture('Unpublished age feature importance predicted score.', ['model_explanation', 'unpublished_claim'])
    flags, _ = gate_unit(unit, {'P1': row}, {'P1'}, {})
    assert 'model_explanation_not_lesion_effect' in flags
    assert 'interpretation_or_unpublished_only' in flags


def test_held_table_cannot_be_bypassed_via_text_layer():
    row, unit = fixture('age score 0.01 0.03')
    row['classifications'] = {'A': 'table_or_figure', 'B': 'current_result'}
    tables = {'TABLE-3-page-1-1': {'status': 'requires_source_resolution', 'A': {'source': {'pdf_page': 1}}}}
    flags, linked = gate_unit(unit, {'P1': row}, {'P1'}, tables)
    assert 'held_table:TABLE-3-page-1-1' in flags and linked == list(tables)


def test_worklist_never_drops_unclassified_or_long_passages():
    row, _ = fixture('x' * 13000)
    row['classifications'] = {'A': None, 'B': None}
    second = dict(row, evidence_id='P2')
    rows, windows = worklist({'passages': [row, second]})
    assert [r['evidence_id'] for w in windows for r in w] == ['P1', 'P2']


def test_target_evidence_requirement_does_not_force_optional_context_or_tables():
    schema = proposal_schema({'P1'}, {'P1', 'C1'})
    p = schema['properties']['units']['items']['properties']
    jsonschema.validate(['P1'], p['evidence_ids'])
    for key in ['qualifier_ids','context_ids','table_ids']:
        jsonschema.validate([], p[key])
    try:
        jsonschema.validate(['C1'], p['evidence_ids'])
    except jsonschema.ValidationError:
        pass
    else:
        raise AssertionError('Context-only ID accepted as target evidence')


def test_whole_model_p_value_does_not_verify_an_added_variable():
    row, unit = fixture('If age was added, the score model explained 71% (F = 10, P < 0.001).')
    unit.update(relation='incremental_added_set', effect_unit='added_set', result_status='reported_detected')
    assert 'increment_test_not_shown' in gate_unit(unit, {'P1':row}, {'P1'}, {})[0]


def test_context_outcome_and_author_claim_cannot_look_unflagged():
    row, unit = fixture('age was related to the outcome')
    row['contains_author_implication'] = True
    context, _ = fixture('score and change score were measured')
    unit['outcome'] = {'text': 'change score', 'source_id': 'C1'}
    unit['context_ids'] = ['C1']
    flags, _ = gate_unit(unit, {'P1': row, 'C1': context}, {'P1'}, {})
    assert 'outcome_label_from_context_check_analysis' in flags
    assert 'discussion_or_author_claim_check' in flags


def test_separate_univariate_results_cannot_look_like_one_joint_model():
    row, unit = fixture('age and volume predicted score (R2 = .2 and .3, respectively).')
    unit['exposure']['text'] = 'age and volume'
    unit['effect_unit'] = 'whole_model'
    assert 'possible_merged_separate_analyses' in gate_unit(unit, {'P1': row}, {'P1'}, {})[0]
    unit['effect_unit'] = 'individual'
    assert 'possible_merged_separate_analyses' in gate_unit(unit, {'P1': row}, {'P1'}, {})[0]
    unit['outcome'] = {'text': 'accuracy', 'source_id': 'P1'}
    unit['direction'] = 'positive'
    assert 'model_metric_direction_not_clinical_effect' in gate_unit(unit, {'P1': row}, {'P1'}, {})[0]


def test_metric_direction_distinguishes_model_metrics_from_clinical_performance():
    row, unit = fixture('age predicts score')
    unit['direction'] = 'positive'
    for label, expected in [('accuracies', True), ('model performance', True),
                            ('language performance', False), ('naming performance', False)]:
        unit['outcome']['text'] = label
        flags, _ = gate_unit(unit, {'P1': row}, {'P1'}, {})
        assert ('model_metric_direction_not_clinical_effect' in flags) == expected
