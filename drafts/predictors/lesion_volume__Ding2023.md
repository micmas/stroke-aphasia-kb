---
schema_version: 2.8
id: lesion_volume
name: Total lesion volume
kind: predictor
predictor_type: imaging_metric
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
short_definition: The total volume of brain tissue damaged by the stroke.
units: cc
typical_range: 5-376 cc
direction_of_severity: higher_is_worse
findings:
- id: f1
  target: discourse_content
  target_kind: impairment
  claim: Total lesion size is significantly correlated with the quantity, efficiency, and informativeness
    of spoken discourse in post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Ding2023'
  method: behavioral_only
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 80
    population: participants with aphasia following left hemisphere stroke
    time_post_onset: M = 53, Med = 23 months
    phase: chronic
    age_range: M = 59, Med = 59 (Range 31-79)
    handedness: right-handed
    language: native English speakers
    cohort: not_reported
  statistics:
    threshold: P < 0.02
    effect_size: r < -0.29
  confounders_controlled: []
  confounders_not_controlled: []
  author_limitations:
  - The present results shed light on persistent impairments in spoken discourse but not on recovery of
    spoken discourse production.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 6
    confidence: high
    flags:
    - target_id discourse_content is forward-looking
  source_passages:
  - section: Results - Behavioural results
    page: 6
    quote: All CIU measures were also significantly correlated with total lesion size (r < -0.29, P <
      0.02), indicating that overall amount of damage within the left middle cerebral artery territory
      predicts quantity, efficiency and informativeness of spoken discourse
    supports: claim
  - section: Materials and methods - Participants
    page: 3
    quote: The data set consisted of behavioural data from 80 participants who had suffered a left hemisphere
      stroke that produced some degree of language impairment.
    supports: sample
  - section: Discussion
    page: 11
    quote: The present results shed light on persistent impairments in spoken discourse but not on recovery
      of spoken discourse production.
    supports: limitation
  region_definition:
    kind: not_reported
---
