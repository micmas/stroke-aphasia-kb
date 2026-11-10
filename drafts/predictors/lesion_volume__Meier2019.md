---
schema_version: 2.8
id: lesion_volume
name: Total lesion volume
kind: predictor
predictor_type: imaging_metric
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
short_definition: The total volume of the brain lesion, typically measured in cubic centimeters (cc).
units: cc
typical_range: not_reported
direction_of_severity: higher_is_worse
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Total lesion volume is a sufficient predictor of overall aphasia severity in patients with chronic
    stroke.
  direction: likely
  relationship: correlational
  citation: '@Meier2019'
  method: behavioral_only
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 34
    population: chronic left hemisphere stroke
    time_post_onset: '>=six months post-onset'
    phase: chronic
    age_range: mean 61.91 +/- 10.84 years
    handedness: mixed
    language: English
  statistics:
    threshold: not_reported
    effect_size: not_reported
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: total lesion volume
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Conclusions, page 14
    confidence: high
    flags: []
  source_passages:
  - section: Conclusions
    page: 14
    quote: it can be inferred that total lesion volume also adequately captured overall aphasia severity
      in our patient sample.
    supports: claim
  - section: Participants
    page: 2
    quote: Thirty-four individuals (24 males; mean age = 61.91 +/- 10.84 years) with chronic stroke-induced
      aphasia (i.e., >=six months post-onset...)
    supports: sample
  author_limitations:
  - The variance in naming and treatment outcomes explained by the lesion classification systems was low.
  source_passages_limitation:
  - section: Discussion
    page: 13
    quote: the variance in naming and treatment outcomes explained by the lesion classification systems
      was low
    supports: limitation
---
