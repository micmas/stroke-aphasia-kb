---
schema_version: 2.8
id: lesion_volume
name: Total lesion volume
kind: predictor
predictor_type: imaging_metric
short_definition: Total volume of the stroke lesion.
assessment:
- manual T1 tracing
units: cm3
typical_range: 1.44-200.50 cm3
direction_of_severity: higher_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Total lesion volume is significantly negatively related to overall aphasia severity (AQ) in acute
    and subacute post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Yu2022'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: rho = -0.497
    p_value: '0.010'
  confounders_controlled: []
  confounders_not_controlled: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 2
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: Lesion volume was significantly negatively related to spontaneous speech, comprehension, and
      AQ
    supports: claim
  author_limitations: []
  region_definition:
    kind: not_reported
---
