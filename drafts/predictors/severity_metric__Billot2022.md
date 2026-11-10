---
schema_version: 2.8
id: severity_metric
name: Aphasia severity metric (instrument-agnostic)
kind: predictor
predictor_type: behavioural
short_definition: A quantitative measure of overall aphasia severity, typically derived from a standardized
  battery.
assessment:
- WAB-R Aphasia Quotient (AQ)
units: score 0-100
typical_range: 0-100 (lower = more severe)
direction_of_severity: lower_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: language_rehabilitation_response
  target_kind: therapy
  claim: Baseline aphasia severity (WAB-AQ) is an independent predictor of responsiveness to language
    rehabilitation in chronic post-stroke aphasia.
  direction: likely
  relationship: responder
  citation: '@Billot2022'
  method: MLPA
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 55
    population: chronic post-stroke aphasia due to a single left-hemisphere stroke
    time_post_onset: mean 59.0 months
    phase: chronic
    age_range: mean 58.8 years
    handedness: not_reported
    language: not_reported
    cohort: CNLR
  statistics:
    threshold: P < 0.001
    effect_size: F1 = 0.842
  confounders_controlled:
  - demographics
  - structural integrity
  - functional connectivity
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: behavioural predictor
  therapy:
    id: language_rehabilitation
    name: language rehabilitation
    dose: 12 weeks
  author_limitations:
  - Small sample size can lead to less accurate results when using machine learning models on neuroimaging
    data to predict behavior.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 1610
    confidence: high
    flags:
    - lesion_mapping (v2.7 design) not extracted by the model — filled from statistics.threshold / confounders
      where the text says; check the Methods
    - imaging_details.reference_space not extracted by the model — set to not_reported; verify against
      the paper
  source_passages:
  - section: Results
    page: 1610
    quote: Notably, among SVM models trained on an individual feature set, aphasia severity (ie, AQ) and
      rs-fMRI connectivity (ie, RS) independently provided the best prediction performance scores...
    supports: claim
  - section: Methods
    page: 1607
    quote: Participants were 55 individuals (37 male) with chronic post-stroke aphasia due to a single
      left-hemisphere stroke (mean age =58.8 years, mean time poststroke onset =59.0 months, mean education
      =15.8 years).
    supports: sample
  - section: Methods
    page: 1609
    quote: SVM and RF models were trained, tuned, and tested using a leave-one-out cross-validation procedure
      on all possible combinations of feature sets...
    supports: method
  - section: Results
    page: 1610
    quote: Notably, among SVM models trained on an individual feature set, aphasia severity (ie, AQ) and
      rs-fMRI connectivity (ie, RS) independently provided the best prediction performance scores, with
      an accuracy of 0.782 and 0.764 and an F1 score of 0.842 and 0.812, respectively.
    supports: statistics
  - section: Limitations
    page: 1612
    quote: Previous studies demonstrated that small sample sizes can lead to less accurate results when
      using machine learning models on neuroimaging data to predict behavior.
    supports: limitation
  instrument: WAB-R Aphasia Quotient (AQ)
  score_band: all severities
  interpretation: Baseline severity used as a predictor of treatment response
  lesion_mapping:
    analysis: multivariate
    n_analysed: 55
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: not_reported
  imaging_details:
    reference_space: not_reported
    atlases_used: []
---
