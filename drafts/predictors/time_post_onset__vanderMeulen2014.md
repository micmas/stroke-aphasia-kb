---
schema_version: 2.8
id: time_post_onset
name: Time post-stroke onset
kind: predictor
predictor_type: clinical
short_definition: The duration of time elapsed since the onset of the stroke.
units: weeks/months
typical_range: not_reported
direction_of_severity: not_applicable
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: melodic_intonation_therapy
  target_kind: therapy
  claim: Earlier initiation of Melodic Intonation Therapy in the subacute phase predicts greater improvement
    in language repetition and verbal communication.
  direction: likely_responder
  relationship: responder
  citation: '@vanderMeulen2014'
  method: behavioral_only
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
  sample:
    n: 27
    population: subacute severe nonfluent aphasia
    time_post_onset: 2 to 3 months
    phase: early_subacute
    age_range: 18 to 80 years
    handedness: all right-handed
    language: Dutch
  statistics:
    threshold: p < .05
    effect_size: beta = -0.68 (untrained items), beta = -1.54 (AAT repetition), beta = -0.46 (ANELT)
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Predictor analysis of timing; no specific region involved.
  author_limitations:
  - Lesion characteristics were not documented in detail.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Determinants for Therapy Outcome
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 5
    quote: Time poststroke at the start of MIT predicted outcome on untrained items, MIT task (beta =
      -.68, p = .01), on AAT repetition (beta = -1.54, p = .02), and on the ANELT (beta = -.46, p = .04).
      The earlier MIT was started, the greater the improvement on these outcome measures.
    supports: claim
  - section: Discussion
    page: 7
    quote: A limitation of the present study is that lesion characteristics were not documented in detail.
    supports: limitation
---
