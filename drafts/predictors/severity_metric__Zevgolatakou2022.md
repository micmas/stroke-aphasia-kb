---
schema_version: 2.8
id: severity_metric
name: Aphasia severity metric (instrument-agnostic)
kind: predictor
predictor_type: behavioural
short_definition: Overall measure of aphasia severity.
assessment:
- WAB-AQ
units: score 0-100
typical_range: 0-100 (lower = more severe)
direction_of_severity: lower_is_worse
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Overall aphasia severity is a primary predictor of the length and structural complexity of narrative
    speech production.
  direction: likely
  relationship: correlational
  citation: '@Zevgolatakou2022'
  method: behavioral_only
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 69
    population: chronic left hemisphere stroke
    time_post_onset: at least 3 months post-onset
    phase: chronic
    age_range: 50.0-68.0 (median 58.0)
    handedness: right-handed
    language: native English
  statistics:
    threshold: not_reported
    effect_size: 'RC1: 33.1% of variance'
  confounders_controlled: []
  confounders_not_controlled: []
  instrument: WAB-AQ
  score_band: all severities
  interpretation: General aphasia severity
  author_limitations:
  - Severity distribution skewed toward mild-to-moderate range due to narrative word count requirements.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 9
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 9
    quote: As expected, it [the general factor] had high positive loadings from general severity measures
      (WAB AQ and PNT accuracy). In addition, it contained high positive factor loadings from measures
      of utterance/sentence length... and measures of sentence structural integrity and complexity
    supports: claim
  - section: Materials and methods
    page: 5
    quote: All but five participants were examined at the chronic stage of aphasia (at least 3 months
      post-onset)
    supports: sample
  - section: Materials and methods
    page: 6
    quote: The 21 behavioural measures... were entered into a principal component analysis (PCA) with
      a bifactor rotation.
    supports: method
  - section: Discussion
    page: 13
    quote: This severity distribution is a natural consequence of requiring at least 150 narrative words
      for QPA scoring—very severely impaired participants are often unable to produce that many narrative
      words
    supports: limitation
  region_definition:
    kind: not_reported
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
---
