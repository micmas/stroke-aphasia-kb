---
schema_version: 2.8
id: age
name: Age at stroke
kind: predictor
predictor_type: demographic
short_definition: Age of the patient at the time of stroke.
units: years
typical_range: not_reported
direction_of_severity: not_applicable
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: prognosis
  target_kind: prognosis
  claim: Age is a significant independent predictor of good functional verbal communication outcome at
    1 year after stroke.
  direction: likely
  relationship: correlational
  citation: '@ElHachioui2013'
  method: behavioral_only
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 130
    population: adult Dutch native/near-native speakers with aphasia due to a first-ever stroke
    time_post_onset: mean of 4 days
    phase: acute
    age_range: mean 67 (SD 15)
    handedness: 86% right-handed
    language: Dutch
  statistics:
    threshold: p <= 0.20 (univariable)
    effect_size: OR 0.94 (0.89 to 0.99)
  confounders_controlled:
  - phonology score
  - Barthel Index score
  - educational level
  - stroke subtype
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: demographic predictor
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
    quote: Age, Barthel Index score, educational level and stroke subtype were the other significant independent
      predictors with a p value <= 0.20 in univariable logistic regression analyses (table 2).
    supports: claim
  - section: Results
    page: 312
    quote: Our final multivariable regression model consisted of the phonology score, Barthel Index score,
      age, educational level and stroke subtype.
    supports: method
  - section: Discussion
    page: 314
    quote: Finally, we were unable to incorporate the role of structural brain damage in our prognostic
      model because as a consequence of the observational design of our study, data from routine CT scanning
      were inadequate.
    supports: limitation
---
