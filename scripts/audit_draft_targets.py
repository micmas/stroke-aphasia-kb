#!/usr/bin/env python3
"""Audit a fixed published draft export; never read or change active extraction outputs.

The reviewed rules distinguish constructs from scores. Unresolved targets remain
unchanged and explicitly queued for source review. This is NOT scientific approval.
Run without --apply to inspect counts. Existing audit metadata makes reruns stable.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RULES = {}


def rule(old, target, papers, name=None, metric=None):
    for key in old.split():
        RULES[key] = {"target": target, "papers": papers.split(), "name": name, "metric": metric}


# Each rule is restricted to the papers inspected in the 2026-11-25 audit.
# A score retains its original label in metric; change, residual and follow-up
# qualifiers remain in the claim and original_target, never silently discarded.
rule('token_test_performance', 'auditory_sentence_comprehension', 'Adezati2022', 'Token Test', 'Token Test performance')
rule('bnt_naming_performance bnt_performance bnt_total boston_naming_test boston_naming_test_score', 'picture_naming', 'Baldo2013 Meier2019 Maher2006 Marchina2011', 'Boston Naming Test')
rule('adn_impairment adn_performance', 'auditory_description_naming', 'Pillay2017', 'Auditory description naming task')
rule('asc_impairment', 'auditory_sentence_comprehension', 'Pillay2017', 'Auditory sentence comprehension task')
rule('can_score can_score_accuracy', 'canonical_sentence_comprehension', 'Kristinsson2020', 'Sentence comprehension task', 'Canonical sentence accuracy')
rule('non_can_performance non_can_score_accuracy', 'noncanonical_sentence_comprehension', 'Kristinsson2020', 'Sentence comprehension task', 'Noncanonical sentence accuracy')
rule('non_can_residual_score non_can_residual_scores noncanonical_residual_accuracy', 'noncanonical_sentence_comprehension', 'Kristinsson2020', 'Sentence comprehension task', 'Residual noncanonical sentence accuracy; adjustment retained in claim')
rule('total_score sentence_processing_total_score', 'sentence_comprehension', 'Kristinsson2020', 'Sentence comprehension task', 'Total score across sentence conditions')
rule('cycle_r_performance cycle_r_comprehension cycle_r_sentence_comprehension cycle_r_subtests', 'sentence_comprehension', 'Dronkers2004', 'CYCLE-R', 'Scores for the sentence conditions named in the claim')
rule('cycle_r_complex_comprehension', 'complex_sentence_comprehension', 'Dronkers2004', 'CYCLE-R', 'Double Embedding, Object Relatives and Subject Relatives subtests')
rule('cycle_r_double_embedding_agentless_passive', 'double_embedding_and_agentless_passive_comprehension', 'Dronkers2004', 'CYCLE-R', 'Double Embedding and Agentless Passive subtests')
rule('anelt_a_score', 'everyday_verbal_communication', 'Nouwens2017', 'Amsterdam-Nijmegen Everyday Language Test', 'A-score: understandability / adequacy of verbal communication')
rule('fcp_improvement', 'functional_communication_change', 'Bhogal2003', 'Functional Communication Profile', 'Ratio of improvement')
rule('bdae_phrase_length', 'connected_speech_phrase_length', 'Naeser2005', 'Boston Diagnostic Aphasia Examination', 'Words per longest phrase in elicited propositional speech')
rule('wab_aq', 'overall_aphasia_severity', 'Johnson2019 Johnson2022 Kristinsson2021 Maher2006', 'Western Aphasia Battery', 'Aphasia Quotient')
rule('wab_r_aq aphasia_quotient', 'overall_aphasia_severity', 'Hu2025 Meier2019 Fridriksson2018JAMA', 'Western Aphasia Battery–Revised', 'Aphasia Quotient')
rule('initial_aq', 'baseline_aphasia_severity', 'Pedersen2004', 'Western Aphasia Battery', 'Initial Aphasia Quotient')
rule('aq_1yr', 'overall_aphasia_severity', 'Pedersen2004', 'Western Aphasia Battery', 'Aphasia Quotient at one year')
rule('aq_improvement', 'aphasia_severity_change', 'Pedersen2004', 'Western Aphasia Battery', 'Change in Aphasia Quotient over one year')
rule('aq_change aphasia_quotient_change', 'aphasia_severity_change', 'Basilakos2019', 'Western Aphasia Battery–Revised', 'Follow-up minus initial Aphasia Quotient')
rule('wab_aq_change', 'aphasia_severity_change', 'Johnson2019', 'Western Aphasia Battery', 'Change in Aphasia Quotient between first and last assessments')
rule('wab_r_aq_change', 'aphasia_severity_change', 'Harvey2022', 'Western Aphasia Battery–Revised', 'Change in Aphasia Quotient')
rule('wab_r_aq_proportion_change', 'aphasia_severity_change', 'Harvey2022', 'Western Aphasia Battery–Revised', 'Proportion change in Aphasia Quotient')
rule('wab_initial', 'baseline_language_function', 'Lazar2010', 'Western Aphasia Battery', 'Baseline composite score; study-specific selection of subtests')
rule('achieved_delta_wab achieved_wab_change', 'language_recovery', 'Lazar2010', 'Western Aphasia Battery', 'Change in study-specific WAB score from baseline to 90 days')
rule('wab_fluency', 'speech_fluency', 'Ding2023', 'Western Aphasia Battery', 'Fluency rating')
rule('wab_fluency_score', 'speech_fluency', 'Basilakos2014', 'Western Aphasia Battery–Revised', 'Fluency rating')
rule('moca moca_score', 'global_cognitive_function', 'Munsch2016', 'Montreal Cognitive Assessment', 'MoCA total score')
rule('smo_ca smoca_outcome', 'global_cognitive_function', 'Munsch2016', 'Short Montreal Cognitive Assessment', 'sMoCA; thresholds retained in claim')
rule('ocs_semantics_performance', 'semantic_processing', 'Moore2024', 'Oxford Cognitive Screen', 'Semantics task')
rule('ocs_praxis_performance', 'praxis', 'Hobden2024', 'Oxford Cognitive Screen', 'Praxis task')
rule('pm_impairment pm_summary_score long_term_pm mist_sf_performance', 'prospective_memory', 'Gilbert2025', 'Memory for Intentions Screening Test–Short Form', 'Summary score or subscales specified in the claim; timing retained')
rule('matrix_reasoning_scores', 'nonverbal_reasoning', 'Fridriksson2013', 'Matrix Reasoning test')
rule('palpa_rhymejudge', 'rhyme_judgment', 'Matchin2024', 'Psycholinguistic Assessments of Language Processing in Aphasia', 'RhymeJudge task')
rule('pnt_improvement', 'naming_improvement', 'Bonilha2016', 'Philadelphia Naming Test', 'Treatment-related change in naming performance')
rule('naming_pmg potential_maximal_gain', 'naming_improvement', 'Gilmore2019', None, 'Proportion of potential maximal gain (PMG)')
rule('pmgm', 'maintenance_of_naming_improvement', 'Gilmore2019', None, 'Proportion of potential maximal gain maintained (PMGM)')
rule('token_measure_t', 'speech_output_quantity', 'Halai2017', 'Connected speech analysis', 'Token count (T); not the Token Test')
rule('type_token_ratio', 'lexical_diversity', 'Halai2017', 'Connected speech analysis', 'Type-token ratio')
rule('ci_quantity ciu_quantity cius_quantity number_of_cius mean_cius', 'discourse_information_quantity', 'Ding2023 Boyle2004', 'Correct information unit analysis', 'Number of correct information units; aggregation retained in claim')
rule('cius_min', 'discourse_information_rate', 'Ding2023', 'Correct information unit analysis', 'Correct information units per minute')
rule('percent_cius', 'discourse_informativeness', 'Ding2023 Boyle2004', 'Correct information unit analysis', 'Percentage of correct information units')
rule('logopenia_dimension_score', 'logopenia', 'Casilio2025', 'APROCSA', 'Logopenia dimension score')
rule('agrammatism_dimension_score', 'agrammatism', 'Casilio2025', 'APROCSA', 'Agrammatism dimension score')
rule('paraphasia_dimension_score', 'paraphasia', 'Casilio2025', 'APROCSA', 'Paraphasia dimension score')
rule('repetition_test', 'speech_repetition', 'Pulvermuller2001', 'Repetition task', 'Repetition of spoken sounds, words, compound words and sentences')
rule('digit_span', 'auditory_short_term_memory_capacity', 'Leff2009', 'Forward digit span task', 'Maximum length of a spoken digit sequence repeated in the original order')
rule('aspt_a_score', 'verb_argument_structure_production', 'DenOuden2019', 'Northwestern Assessment of Verbs and Sentences', 'Argument Structure Production Test, Code A: verb and all required arguments in correct order')
rule('sat_verbal_score', 'verbal_semantic_processing', 'Nouwens2017', 'Semantic Association Test', 'Verbal version')
rule('cat_word_comprehension', 'word_comprehension', 'Nouwens2017', 'Comprehensive Aphasia Test', 'Word comprehension subtest; modality requires verification')
rule('composite_score cs_subacute', 'overall_language_function', 'OsaGarcia2020', None, 'Study-specific language composite; phase retained in claim')
rule('chronic_change_score chronic_change_scores late_raw_change_score', 'language_recovery', 'OsaGarcia2024', None, 'Composite score change from subacute to chronic phase (ΔCS2–3)')
rule('early_raw_change_score subacute_change_score', 'language_recovery', 'OsaGarcia2024', None, 'Composite score change from acute to subacute phase (ΔCS1–2)')
rule('overall_change_scores_delta_cs1_3', 'language_recovery', 'OsaGarcia2024', None, 'Composite score change from acute to chronic phase (ΔCS1–3)')

# These are real non-behaviour endpoints or methodological findings. Do not
# invent a behavioural construct, or silently put imaging outcomes in impairment.
NON_BEHAVIOUR = set('''adverse_events mild_nonserious_adverse_events serious_adverse_events
scalp_erythema undesirable_side_effects brain_activation brain_lesion_clusters brain_lesion_location
auditory_comprehension_map auditory_speech_processing_connectivity auditory_speech_processing_modulation
connectivity_disruption cortical_abnormality_pwi_dwi cortical_damage_extent cortical_hypoperfusion
effective_connectivity fa_values fazekas_rating functional_imaging_data grey_matter_activity
healthy_vs_aphasia_activity hippocampal_wm_integrity language_lateralization lateral_frontal_activity_laterality
left_hemisphere_fa_reduction left_hippocampus_volume_reduction lesion_distribution lesion_regions
medial_frontal_activity_laterality neural_correlates neural_reorganization_degree neural_tissue_concentration
noun_verb_processing_neural_correlates posterior_cluster_activation rdlpfc_to_lptl_facilitation rsfc_connectivity
salience_and_central_executive_networks salience_network_activity semantic_activation semantic_processing_activation
session_effect structural_markers task_activity therapy_induced_rsfc_changes therapy_intensity time_to_first_therapy
tissue_concentration white_matter_hyperintensities white_matter_integrity white_matter_tract_integrity
aprocsa_dimension_scores aprocsa_dimensions aprocsa_feature_ratings ciu_consistency ciu_measure_consistency
agrammatism_motor_speech_bias logopenia_agrammatism_bias long_term_mortality mortality
reduced_wpm_and_agrammatism_overlap'''.split())

# These labels do not establish a specific construct by themselves. Keep them
# visible in a source-review queue rather than guessing from a test acronym.
AMBIGUOUS = set('''absolute_proportion_of_change relative_proportion_of_change relative_early_change
relative_overall_change recovery_ratio recovery_ratio_difference cumulative_clinical_change
behavioral_deficits behavioral_impairment_variance behavioral_variance behavioural_deficits
behavioural_performance behavioural_recovery behavioural_variance chronic_behavioural_outcome
complete_recovery degree_of_recovery domain_impairment good_outcome_3m impairment_level individual_clinical_tests
language_measures language_tasks long_term_outcomes pd_mr pd_mr_group_membership recovery
secondary_outcomes_12_weeks secondary_outcomes_null task_accuracy treatment_outcome treatment_response
treatment_responsiveness rehabilitation_responsiveness navs_low_group navs_overall_scores
aspt_a_score cat_word_comprehension cat_language_scores ocs_performance wab_r_subtests wab_aphasia_quotient
token_test_change_score pica_score_change sat_verbal_score digit_span modified_rankin_scale poor_mrs_and_moca
poor_mrs_moca comprehensive_aphasia_test_batteries communication_rating_scales general_aphasia_severity_and_lesion_size
three_month_behavioural_score three_month_behavioural_scores ciu_measures ciu_production'''.split())


def audit(f):
    old = f.get('target_audit', {}).get('original_target', f['target'])
    target = old
    measure = {'status': 'needs_source_review', 'instruments': [],
               'note': 'Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor or a paper-wide test list.'}
    status, category = 'behaviour_label_present', 'behaviour_or_language_construct'
    reason = 'Label names a behaviour or language construct; its exact operational definition and measurement still need source review.'
    if old in NON_BEHAVIOUR or f['target_kind'] in ('region', 'predictor'):
        status, category = 'needs_source_review', 'non_behaviour_or_methodological'
        reason = 'This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural deficit.'
    elif old in AMBIGUOUS or re.search(r'(^|_)(score|scores|test|aq|cs)(_|$)', old):
        status, category = 'needs_source_review', 'ambiguous_or_composite'
        reason = 'A score, generic outcome or composite label does not uniquely identify a behaviour. Check the task, subtests and analysis before retargeting.'
    r = RULES.get(old)
    if r and f['citation'].lstrip('@') in r['papers']:
        target = r['target']
        status = 'construct_separated'
        category = 'behaviour_or_language_construct'
        reason = 'Separated the construct from the score/task using the published claim and linked source passages. This is metadata correction, not scientific approval.'
        measure = {'status': 'identified' if r['name'] else 'needs_source_review',
                   'instruments': [{'name': r['name']}] if r['name'] else [],
                   'metric': r['metric'] or old.replace('_', ' '),
                   'note': 'Task conditions, covariates, change metric and timing remain in the claim and source passages. Instrument version/subtests require final source verification.'}
    if f['citation'] == '@Adezati2022' and target in ('sentence_comprehension', 'sentence_comprehension_deficits', 'auditory_sentence_comprehension', 'sentence_comprehension_deficit'):
        measure = {'status': 'identified', 'instruments': [{'name': 'Token Test'}],
                   'metric': 'Sentence comprehension performance',
                   'definition_source': {'citation': '@Adezati2022', 'page': 2,
                       'quote': 'First, sentence comprehension was measured using the Token Test'},
                   'note': 'Methods, page 2: sentences avoid non-canonical structures and complex embeddings. This is not a measure of all syntactic abilities.'}
    record = {'status': status, 'category': category, 'original_target': old,
              'reason': reason, 'audited_on': '2026-11-25',
              'scope': 'Published metadata and linked excerpts; no new model pass or human approval'}
    return target, measure, record


def update_text(text, finding_id, changes):
    """Splice only top-level finding fields. Preserve original extraction/audit YAML byte-for-byte."""
    front = text.split('---', 2)[1]
    node = yaml.compose(front)
    findings = next(v for k, v in node.value if k.value == 'findings')
    offset = text.index(front)
    edits = []
    for finding in findings.value:
        values = {k.value: (k, v) for k, v in finding.value}
        if values['id'][1].value != finding_id:
            continue
        for key, value in changes.items():
            rendered = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True, width=100).rstrip()
            rendered = '\n'.join('  ' + line for line in rendered.splitlines()) + '\n'
            if key in values:
                k, v = values[key]
                start = front.rfind('\n', 0, k.start_mark.index) + 1
                next_keys = [kk.start_mark.index for kk, _ in finding.value if kk.start_mark.index > k.start_mark.index]
                end = front.rfind('\n', 0, min(next_keys)) + 1 if next_keys else finding.end_mark.index
                edits.append((offset + start, offset + end, rendered))
            else:
                # Inserting before target is safe for both flow scalars and block values.
                start = front.rfind('\n', 0, values['target'][0].start_mark.index) + 1
                edits.append((offset + start, offset + start, rendered))
        break
    else:
        raise ValueError(f'Finding not found: {finding_id}')
    for start, end, replacement in sorted(edits, key=lambda e: (e[0], e[1]), reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    export = json.loads((ROOT / 'export/stroke-aphasia-kb-drafts.json').read_text())
    rows, counts = [], Counter()
    for f in export['findings']:
        if f['source_status'] != 'draft':
            continue  # Never rewrite reviewed or approved entries.
        target, measurement, audit_record = audit(f)
        counts[audit_record['status']] += 1
        path = ROOT / f['source_path']
        original = path.read_text()
        before = yaml.safe_load(original.split('---', 2)[1])
        assert before['status'] == 'draft'
        stored = next(x for x in before['findings'] if x['id'] == f['id'])
        assert stored['target'] in (f['target'], target), f['source_path']
        changes = {'target': target, 'outcome_measurement': measurement, 'target_audit': audit_record}
        updated = update_text(original, f['id'], changes)
        after = yaml.safe_load(updated.split('---', 2)[1])
        expected = copy.deepcopy(before)
        next(x for x in expected['findings'] if x['id'] == f['id']).update(changes)
        assert after == expected, f"Unexpected mutation: {path}"
        if args.apply and updated != original:
            path.write_text(updated)
        rows.append({'path': f['source_path'], 'finding': f['id'], 'citation': f['citation'],
                     'before_target': audit_record['original_target'], 'target': target,
                     'status': audit_record['status'], 'category': audit_record['category'],
                     'measurement_status': measurement['status']})
    report = {'audited_on': '2026-11-25', 'input_export_digest': export.get('version', {}).get('contentDigest'),
              'scope': 'All published draft findings in the captured export. Labels and linked excerpts, not full-PDF scientific approval.',
              'counts': dict(counts), 'findings': len(rows), 'papers': len({r['citation'] for r in rows}),
              'retargeted': sum(r['before_target'] != r['target'] for r in rows),
              'measurement_identified': sum(r['measurement_status'] == 'identified' for r in rows),
              'approved': 0, 'records': rows}
    if args.apply:
        (ROOT / 'logs/publication/target-audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    main()
