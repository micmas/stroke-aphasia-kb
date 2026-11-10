---
schema_version: 2.8
id: severity_metric
name: Aphasia severity metric (instrument-agnostic)
kind: predictor
predictor_type: behavioural
short_definition: A measure of overall aphasia severity or functional communication ability.
assessment:
- ScreeLing
- ASRS
units: score
typical_range: ScreeLing 0-24 per component; ASRS 0-5
direction_of_severity: lower_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: prognosis
  target_kind: prognosis
  claim: Initial severity of phonological impairment is the strongest linguistic predictor of good functional
    verbal communication outcome at 1 year after stroke.
  direction: likely
  relationship: correlational
  citation: '@ElHachioui2013'
  method: behavioral_only
  design: longitudinal
  strength: strong
  evidence_quality: cohort
  instrument: ScreeLing
  score_band: baseline phonology score
  interpretation: Higher initial phonology scores predict better functional outcome.
  sample:
    n: 130
    population: adult Dutch native/near-native speakers with aphasia due to a first-ever stroke
    time_post_onset: mean of 4 days
    phase: acute
    age_range: mean 67 (SD 15)
    handedness: 86% right-handed
    language: Dutch
  statistics:
    threshold: p=0.003
    effect_size: OR 1.31 (95% CI 1.15 to 1.51)
  confounders_controlled:
  - age
  - Barthel Index score
  - educational level
  - stroke subtype
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: behavioural predictor based on ScreeLing phonology score
  author_limitations:
  - The three core linguistic components were not examined extensively but with a screening tool.
  - Unable to incorporate the role of structural brain damage because routine CT scanning data were inadequate.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 312
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 312
    quote: In multivariable analysis, these variables explained 46.5% of the variance, with phonology
      being the only significant predictor (p=0.003).
    supports: statistics
  - section: Discussion
    page: 313
    quote: Phonology score proved to be the strongest linguistic predictor, which emphasises the importance
      of investigating the core linguistic components in the acute stage.
    supports: claim
  - section: Methods
    page: 310
    quote: Adult Dutch native/near-native speakers who could complete language tests between 2 and 14
      days after stroke were eligible for inclusion.
    supports: sample
  - section: Discussion
    page: 314
    quote: Second, the three core linguistic components were not examined extensively but with a screening
      tool.
    supports: limitation
  - section: Discussion
    page: 314
    quote: Finally, we were unable to incorporate the role of structural brain damage in our prognostic
      model because as a consequence of the observational design of our study, data from routine CT scanning
      were inadequate.
    supports: limitation
---
