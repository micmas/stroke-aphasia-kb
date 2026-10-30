---
schema_version: 2.8
id: time_post_onset
name: Time post-stroke onset
kind: predictor
predictor_type: clinical
short_definition: The duration of time elapsed between the stroke onset and the start of intervention
  or assessment.
units: months
typical_range: 0-12+ months
direction_of_severity: higher_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Enrollment within one month of stroke onset is associated with the greatest absolute recovery
    across overall language ability, auditory comprehension, naming, and functional communication.
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
    effect_size: +19.1 WAB-AQ points; +5.3 AAT Token Test; +11.1 BNT points; +1.1 AAT Spontaneous-Speech
      Communication
  confounders_controlled:
  - age
  - sex
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
    quote: enrollment <1 month post-onset (+19.1 Western Aphasia Battery Aphasia-Quotient points [CI,
      13.9–24.4]; +5.3 correct on AAT Token Test [CI, 1.7–8.8]; +11.1 Boston Naming Test points [CI, 5.7–16.5];
      and +1.1 AAT Spontaneous-Speech Communication subscale point [CI, 0.7–1.4]) conferred the greatest
      absolute change-from-baseline across each language domain.
    supports: claim
  - section: Methods
    page: 3
    quote: The absolute change in language domain scores from baseline to first follow-up was regressed
      onto stroke, aphasia, and demographic covariates specified a priori...
    supports: method
  - section: Discussion
    page: 7
    quote: We were unable to account for spontaneous recovery in our study.
    supports: limitation
  region_definition:
    kind: not_reported
---
