---
schema_version: 2.8
id: age
name: Age at stroke
kind: predictor
predictor_type: demographic
short_definition: The age of the patient at the time of stroke or assessment.
units: years
typical_range: 18-90+ years
direction_of_severity: not_applicable
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Younger age (under 55 years) is associated with greater absolute recovery in overall language
    ability, auditory comprehension, and naming compared to older age groups.
  direction: likely
  relationship: correlational
  citation: '@Ali2021'
  method: meta-analysis
  design: meta-analysis
  strength: strong
  evidence_quality: cohort
  sample:
    n: 943
    population: multilingual, international aphasia dataset
    time_post_onset: median=43.6 weeks poststroke
    phase: chronic
    age_range: median 63 (IQR, 53-72)
    handedness: not_reported
    language: multilingual
    cohort: RELEASE
  statistics:
    threshold: 95% CI
    effect_size: +15.4 WAB-AQ points; +6.1 AAT Token Test; +9.3 BNT points
  confounders_controlled:
  - sex
  - time since stroke
  - baseline language impairment score
  confounders_not_controlled:
  - education level
  - socioeconomic status
  - initial stroke severity
  author_limitations:
  - Unable to account for spontaneous recovery.
  - Many potentially important covariates... were inconsistently available across the datasets.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 1781
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 1
    quote: Younger age (<55 years, +15.4 Western Aphasia Battery Aphasia-Quotient points [CI, 10.0–20.9],
      +6.1 correct on AAT Token Test [CI, 3.2–8.9]; +9.3 Boston Naming Test points [CI, 4.7–13.9]... conferred
      the greatest absolute change-from-baseline across each language domain.
    supports: claim
  - section: Methods
    page: 3
    quote: The absolute change in language domain scores from baseline to first follow-up was regressed
      onto stroke, aphasia, and demographic covariates specified a priori...
    supports: method
  - section: Results
    page: 4
    quote: median age was 63 (IQR, 53–72)
    supports: sample
  - section: Discussion
    page: 7
    quote: We were unable to account for spontaneous recovery in our study.
    supports: limitation
  region_definition:
    kind: not_reported
---
