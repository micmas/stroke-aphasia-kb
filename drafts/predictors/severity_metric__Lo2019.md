---
schema_version: 2.8
id: severity_metric
name: Aphasia severity metric (instrument-agnostic)
kind: predictor
predictor_type: behavioural
short_definition: A standardized measure of overall cognitive or language impairment following stroke.
assessment:
- Standardized z-scores (T-scores)
units: z-score (SD)
typical_range: z-score (lower = more severe)
direction_of_severity: higher_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Diabetes mellitus is strongly associated with poorer global cognitive function after stroke.
  direction: likely
  relationship: correlational
  citation: '@Lo2019'
  method: meta-analysis
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  instrument: Standardized global cognition z-score
  score_band: all severities
  interpretation: Diabetes mellitus acts as a significant risk factor for lower global cognitive performance.
  sample:
    n: 2698
    population: hospital-based stroke or TIA patients
    time_post_onset: 2 to 6 months
    phase: early_subacute
    age_range: mean 67.0 (SD 11.1)
    handedness: not_reported
    language: not_reported
    cohort: STROKOG
  statistics:
    threshold: p < 0.001
    effect_size: -0.47 SD
    p_value: <0.001
  confounders_controlled:
  - sex
  - age
  - education
  - hypertension
  - smoking
  - atrial fibrillation
  - past stroke
  confounders_not_controlled:
  - APOE
  region_definition:
    kind: not_reported
    description: Global cognitive function derived from 5 domains (attention, memory, language, perceptual
      motor, executive function).
  author_limitations:
  - 'Selection bias: patients with severe language impairment or those very ill were generally excluded.'
  - Lack of consensus on the allocation of neuropsychological tests into domains.
  - Standardization relies on the assumption that comparison groups were representative.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 9
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 9
    quote: Diabetes mellitus was strongly associated with poorer performance in global cognition and in
      all domains when examined independently (table 5) and after adjustment for other risk factors (-0.47
      SD; p < 0.001 in global cognition...)
    supports: claim
  - section: Methods
    page: 6
    quote: In the second step and main set of analyses, risk factors (hypertension, diabetes mellitus,
      smoking, AF, smoking, past stroke) were included together in a single multivariable model.
    supports: method
  - section: Results
    page: 6
    quote: For the combined sample (n = 2,698), mean z scores for the 5 domains were similar at approximately
      -1 SD, and mean global cognition was -1.5 SDs
    supports: sample
  - section: Discussion
    page: 13
    quote: individuals with severe language impairment or those who are very ill are generally excluded,
      leading to some selection bias.
    supports: limitation
---

# Notes
This finding targets the general cognitive severity metric as the paper focuses on poststroke cognitive impairment (PSCI) rather than aphasia specifically, though language is one of the measured domains.
