---
schema_version: 2.8
id: severity_metric
name: Aphasia severity metric (instrument-agnostic)
kind: predictor
predictor_type: clinical
short_definition: Overall aphasia severity as measured by a standardized battery.
assessment:
- WAB-R Aphasia Quotient (WAB-AQ)
units: score 0-100
typical_range: 0-100 (lower = more severe)
direction_of_severity: lower_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Non-linguistic cognitive ability (WAIS Matrices) is associated with less severe aphasia, even
    after controlling for lesion size and location.
  direction: likely
  relationship: correlational
  citation: '@Johnson2022'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  instrument: WAIS Matrices
  score_band: all
  interpretation: Higher non-linguistic cognitive reserve correlates with higher WAB-AQ scores.
  sample:
    n: 147
    population: chronic left-hemisphere stroke
    time_post_onset: '>= 6 months'
    phase: chronic
    age_range: 21-85 years
    handedness: pre-morbidly right-handed
    language: not_reported
  statistics:
    threshold: P = .005
    effect_size: t = 2.9
  confounders_controlled:
  - total lesion volume
  - proportion damage to critical ROIs
  confounders_not_controlled: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 380
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 380
    quote: Three statistically significant predictors (WAIS, age at stroke, and time post-stroke), illustrated
      in Fig. 3, were revealed from our Demographic Model, indicating a relationship between non-linguistic
      cognitive ability (P = .005), age at stroke (P = .02), and time post stroke (P = .001) and aphasia
      severity even when the effect of lesion size (measured in mm3) and location had been factored out
    supports: claim
  - section: Discussion
    page: 386
    quote: Due to the retrospective nature of the present study, there are several limitations that should
      be considered when interpreting the results.
    supports: limitation
  author_limitations:
  - Retrospective nature of the study may lead to unrepresentative samples.
  region_definition:
    kind: not_reported
- id: f2
  target: severity_metric
  target_kind: predictor
  claim: Older age at stroke is associated with more severe aphasia, even after controlling for lesion
    size and location.
  direction: likely
  relationship: correlational
  citation: '@Johnson2022'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  instrument: age at stroke
  score_band: all
  interpretation: Increased age at stroke correlates with lower WAB-AQ scores.
  sample:
    n: 147
    population: chronic left-hemisphere stroke
    time_post_onset: '>= 6 months'
    phase: chronic
    age_range: 21-85 years
    handedness: pre-morbidly right-handed
    language: not_reported
  statistics:
    threshold: P = .02
    effect_size: t = -2.3
  confounders_controlled:
  - total lesion volume
  - proportion damage to critical ROIs
  confounders_not_controlled: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 380
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 380
    quote: Three statistically significant predictors (WAIS, age at stroke, and time post-stroke), illustrated
      in Fig. 3, were revealed from our Demographic Model, indicating a relationship between non-linguistic
      cognitive ability (P = .005), age at stroke (P = .02), and time post stroke (P = .001) and aphasia
      severity even when the effect of lesion size (measured in mm3) and location had been factored out
    supports: claim
  - section: Discussion
    page: 386
    quote: Due to the retrospective nature of the present study, there are several limitations that should
      be considered when interpreting the results.
    supports: limitation
  author_limitations:
  - Retrospective nature of the study may lead to unrepresentative samples.
  region_definition:
    kind: not_reported
- id: f3
  target: severity_metric
  target_kind: predictor
  claim: Greater time post-stroke is associated with less severe aphasia, even after controlling for lesion
    size and location.
  direction: likely
  relationship: correlational
  citation: '@Johnson2022'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  instrument: time post-stroke
  score_band: all
  interpretation: Longer time since stroke onset correlates with higher WAB-AQ scores.
  sample:
    n: 147
    population: chronic left-hemisphere stroke
    time_post_onset: '>= 6 months'
    phase: chronic
    age_range: 21-85 years
    handedness: pre-morbidly right-handed
    language: not_reported
  statistics:
    threshold: P = .001
    effect_size: t = 3.3
  confounders_controlled:
  - total lesion volume
  - proportion damage to critical ROIs
  confounders_not_controlled: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 380
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 380
    quote: Three statistically significant predictors (WAIS, age at stroke, and time post-stroke), illustrated
      in Fig. 3, were revealed from our Demographic Model, indicating a relationship between non-linguistic
      cognitive ability (P = .005), age at stroke (P = .02), and time post stroke (P = .001) and aphasia
      severity even when the effect of lesion size (measured in mm3) and location had been factored out
    supports: claim
  - section: Discussion
    page: 386
    quote: Due to the retrospective nature of the present study, there are several limitations that should
      be considered when interpreting the results.
    supports: limitation
  author_limitations:
  - Retrospective nature of the study may lead to unrepresentative samples.
  region_definition:
    kind: not_reported
- id: f4
  target: severity_metric
  target_kind: predictor
  claim: Greater extent of leukoaraiosis (white matter hyperintensities) is associated with more severe
    aphasia, even after controlling for lesion size and location.
  direction: likely
  relationship: correlational
  citation: '@Johnson2022'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  instrument: Fazekas rating
  score_band: all
  interpretation: Higher Fazekas scores (more severe WMH) correlate with lower WAB-AQ scores.
  sample:
    n: 106
    population: chronic left-hemisphere stroke
    time_post_onset: '>= 6 months'
    phase: chronic
    age_range: 21-85 years
    handedness: pre-morbidly right-handed
    language: not_reported
  statistics:
    threshold: P = .0004
    effect_size: t = -3.7
  confounders_controlled:
  - total lesion volume
  - proportion damage to critical ROIs
  confounders_not_controlled: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 380
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 380
    quote: a second prediction model was constructed, which included available health factors (presence
      of diabetes, exercise rate, BMI, and WMH ratings). ... A statistically significant effect of total
      Fazekas scores (P = .0004) was found in our model
    supports: claim
  - section: Discussion
    page: 386
    quote: Due to the retrospective nature of the present study, there are several limitations that should
      be considered when interpreting the results.
    supports: limitation
  author_limitations:
  - Retrospective nature of the study may lead to unrepresentative samples.
  region_definition:
    kind: not_reported
---
