---
schema_version: 2.8
id: melodic_intonation_therapy
name: Melodic Intonation Therapy (MIT)
kind: therapy
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
short_description: A rehabilitation programme including melodic intoning, rhythmic speech and the use
  of common phrases.
targets_impairments:
- fluency
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Melodic intoning does not significantly improve articulatory quality compared to rhythmic speech
    in non-fluent aphasics.
  direction: no_effect
  relationship: causal
  citation: '@Stahl2011'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: melodic_intonation_therapy
    name: melodic intonation therapy
  sample:
    n: 17
    population: non-fluent aphasics
    time_post_onset: at least 3 months post-infarction
    phase: chronic
    age_range: 27-80 years
    handedness: right-handed
    language: German native-speakers
  statistics:
    threshold: NS
    effect_size: F(1) = 0.55
  confounders_controlled:
  - patients' age
  - composite basal ganglia lesion scale
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: behavioural-only treatment-efficacy finding — no specific brain region
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  author_limitations:
  - The study was limited to a small sample of 17 patients.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: 'Results, Part 1: Melodic intoning'
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: A repeated-measures ANOVA based on articulatory quality did not indicate an effect of melodic
      intoning as contrasted with the spoken conditions [F(1) = 0.55, NS]
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Seventeen stroke patients were included in the study.
    supports: sample
  - section: Introduction
    page: 1
    quote: 'This therapy consists of a rehabilitation programme with various elements, including three
      main components: melodic intoning, rhythmic speech and the use of common phrases.'
    supports: method
  - section: Discussion
    page: 10
    quote: Contrary to some opinion, our results suggest that singing may not be decisive for speech production
      in non-fluent aphasics.
    supports: claim
---
