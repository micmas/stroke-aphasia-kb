---
schema_version: 2.8
id: stroke_severity_sss
name: Neurological stroke severity (Scandinavian Stroke Scale)
kind: predictor
predictor_type: clinical
short_definition: The severity of the initial stroke event, typically measured by the modified Rankin
  Scale (mRS).
assessment:
- modified Rankin Scale (mRS)
units: score
typical_range: 0-6 (higher is worse)
direction_of_severity: higher_is_worse
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: intensive_speech_and_language_therapy
  target_kind: therapy
  claim: Baseline stroke severity is a significant predictor of immediate treatment success in verbal
    communication; patients with milder stroke show greater improvement.
  direction: likely
  relationship: responder
  citation: '@Breitenstein2017'
  method: behavioral_only
  design: RCT
  strength: moderate
  evidence_quality: RCT
  therapy:
    id: intensive_speech_and_language_therapy
    name: intensive speech and language therapy
    dose: 3 weeks, >=10 h per week
  sample:
    n: 156
    population: chronic aphasia after stroke
    time_post_onset: 6 months or more
    phase: chronic
    age_range: 18-70 years
    handedness: not_reported
    language: German
    cohort: FCET2EC
  statistics:
    threshold: p<0.0001
    effect_size: not_reported
    p_value: 0.0001
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: behavioural predictor analysis
  imaging: none
  author_limitations: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 1534
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 1534
    quote: Of all patient-related, stroke-related, aphasia-related, and therapy-related variables (appendix
      p 1), only baseline stroke severity was a significant predictor of immediate treatment success in
      verbal communication (data not shown); patients with less severe stroke at enrolment had greater
      improvement after treatment than those with more severe stroke (p<0.0001).
    supports: claim
---
