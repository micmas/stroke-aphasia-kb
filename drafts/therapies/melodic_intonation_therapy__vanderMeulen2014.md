---
schema_version: 2.8
id: melodic_intonation_therapy
name: Melodic Intonation Therapy (MIT)
kind: therapy
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
short_description: A language production treatment for severe nonfluent aphasia involving repetitive singing
  of short sentences combined with rhythmic hand tapping.
targets_impairments:
- fluency
- phonological_production
dosage: 5 h/wk for 6 weeks
findings:
- id: f1
  target: phonological_production
  target_kind: impairment
  claim: Intensive Melodic Intonation Therapy significantly improves the repetition of trained utterances
    in subacute severe nonfluent aphasia compared to a control intervention.
  direction: likely
  relationship: causal
  citation: '@vanderMeulen2014'
  method: clinical_RCT
  design: RCT
  strength: moderate
  evidence_quality: RCT
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
    dose: 5 h/wk for 6 weeks
  sample:
    n: 27
    population: subacute severe nonfluent aphasia
    time_post_onset: 2 to 3 months
    phase: early_subacute
    age_range: 18 to 80 years
    handedness: all right-handed
    language: Dutch
  statistics:
    threshold: p < .01
    effect_size: beta = 15.0
  confounders_controlled:
  - baseline
  - gender
  - aphasia severity
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Behavioural efficacy finding; no specific region targeted.
  author_limitations:
  - The study is too underpowered to obtain significant effects on most of the outcome measures.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 2
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: A significant effect in favor of MIT on language repetition was observed for trained items
    supports: claim
  - section: Participants
    page: 3
    quote: 'Inclusion criteria were: aphasic after left hemisphere stroke, time poststroke 2 to 3 months,
      premorbidly right-handed, age 18 to 80 years, native language Dutch, and MIT candidate.'
    supports: sample
  - section: Design
    page: 2
    quote: A waiting-list randomized controlled design was used... participants in the experimental group
      received intensive MIT (6 weeks; 5 h/wk)
    supports: method
  - section: Results
    page: 4
    quote: The linear regression analysis revealed a significant difference in improvement at T2 between
      the 2 groups for the MIT repetition test (trained items)
    supports: statistics
  - section: Discussion
    page: 6
    quote: The study is too underpowered to obtain significant effects on most of the outcome measures,
      which is a clear limitation of the study.
    supports: limitation
- id: f2
  target: fluency
  target_kind: impairment
  claim: Melodic Intonation Therapy leads to significant improvement in verbal communication in daily
    life for patients with subacute severe nonfluent aphasia.
  direction: likely
  relationship: causal
  citation: '@vanderMeulen2014'
  method: clinical_RCT
  design: RCT
  strength: moderate
  evidence_quality: RCT
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
    dose: 5 h/wk for 6 weeks
  sample:
    n: 27
    population: subacute severe nonfluent aphasia
    time_post_onset: 2 to 3 months
    phase: early_subacute
    age_range: 18 to 80 years
    handedness: all right-handed
    language: Dutch
  statistics:
    threshold: p < .01
    effect_size: mean improvement 6.6 points
  confounders_controlled:
  - baseline
  - gender
  - aphasia severity
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Behavioural efficacy finding; no specific region targeted.
  author_limitations:
  - The study is too underpowered to obtain significant effects on most of the outcome measures.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 2
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: After MIT there was a significant improvement in verbal communication but not after the control
      intervention.
    supports: claim
  - section: Results
    page: 4
    quote: At T2, the MIT group showed significant improvement on all tasks, except for the Sabadel task.
    supports: statistics
  - section: Discussion
    page: 6
    quote: The study is too underpowered to obtain significant effects on most of the outcome measures,
      which is a clear limitation of the study.
    supports: limitation
---
