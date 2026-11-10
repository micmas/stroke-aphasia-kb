---
schema_version: 2.8
id: sex
name: Patient sex
kind: predictor
predictor_type: demographic
short_definition: Biological sex of the patient.
assessment: []
units: not_reported
typical_range: not_reported
direction_of_severity: not_applicable
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: crossed_aphasia
  target_kind: impairment
  claim: Male crossed aphasia patients are significantly more likely than female patients to have a positive
    history of familial sinistrality.
  direction: likely
  relationship: correlational
  citation: '@Coppens2002'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 165
    population: crossed aphasia patients
    time_post_onset: not_reported
    phase: not_reported
    age_range: not_reported
    handedness: not_reported
    language: not_reported
  statistics:
    threshold: p = .025
    effect_size: Yates corrected v2 = 5.021
  confounders_controlled: []
  confounders_not_controlled: []
  author_limitations:
  - Familial sinistrality is difficult to establish in most cases and may be influenced by family size.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Discussion
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: However, male were significantly more likely than female CA subjects to show a positive history
      of familial sinistrality.
    supports: claim
  - section: Results
    page: 18
    quote: However, there was a signiﬁcant diﬀerence between the frequency of familial sinistrality (Yates
      corrected v2 = 5.021, df = 1, p = .025). A history of familial sinistrality was signiﬁcantly more
      frequent in male than in female CA subjects.
    supports: statistics
  - section: Discussion
    page: 28
    quote: As a caveat, we would strongly underscore that familial sinistrality is rather diﬃcult to establish
      in most CA cases.
    supports: limitation
  region_definition:
    kind: not_reported
---
