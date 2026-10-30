---
schema_version: 2.8
id: melodic_intonation_therapy
name: Melodic Intonation Therapy (MIT)
kind: therapy
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
targets_impairments:
- fluency
- anomia
short_description: An intonation-based treatment for nonfluent aphasia using melodic contours and rhythmic
  left-hand tapping.
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Intense melodic intonation therapy leads to significant improvements in spontaneous speech production
    that generalize to untrained language structures.
  direction: likely
  relationship: causal
  citation: '@Schlaug2010'
  method: behavioral_only
  design: case-series
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 6
    population: patients treated with MIT
    time_post_onset: not_reported
    phase: chronic
    age_range: not_reported
    handedness: not_reported
    language: not_reported
  statistics:
    threshold: not_reported
    effect_size: more than 200% improvement in correct information units (CIUs)
    p_value: not_reported
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: behavioural-only treatment-efficacy finding
  author_limitations:
  - The efficacy of this therapy has yet to be substantiated in a randomized controlled trial.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 659
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 659
    quote: Another case series of six patients treated with MIT showed a more than 200% improvement in
      a measure of spontaneous speech, correct information units (CIUs).
    supports: claim
  - section: Introduction
    page: 657
    quote: the efficacy of this therapy has yet to be substantiated in a randomized controlled trial.
    supports: limitation
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
    dose: up to 1.5 h/day, 5 days/week over a period of several months
- id: f2
  target: right_inferior_frontal_gyrus
  target_kind: region
  claim: Melodic intonation therapy induces increased activation in the right inferior frontal gyrus,
    right temporal, and premotor regions.
  direction: likely
  relationship: treatment_response
  citation: '@Schlaug2010'
  method: fMRI_activation
  design: case-series
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 1
    population: patient treated with MIT
    time_post_onset: not_reported
    phase: chronic
    age_range: not_reported
    handedness: not_reported
    language: not_reported
  statistics:
    threshold: p < 0.05 family-wise error
    effect_size: not_reported
    p_value: not_reported
  confounders_controlled:
  - rate of production
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: Right temporal, premotor and posterior inferior frontal region
  imaging_details:
    reference_space: MNI152
    atlases_used: []
    preprocessing_pipeline: spatially-standardized normal brain
    task:
      name: Overt speaking
      description: Overt speaking versus silence and vowel production
      contrasts:
      - Speak > Sil
      - Speak > Phon
      baseline: Silence
  author_limitations:
  - Pilot imaging data suggest that functional and structural imaging changes occur...
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 659
    confidence: high
    flags:
    - n=1 for imaging finding
  source_passages:
  - section: Results
    page: 659
    quote: The pronounced differences in activation observed in the post- versus pre-therapy comparison
      shows that there is more activation in the right temporal, premotor and posterior inferior frontal
      region after therapy.
    supports: claim
  - section: Results
    page: 661
    quote: the rate of speaking/singing remains the same for all assessments, so true treatment-induced
      changes in the brain network can be detected rather than changes in the rate of production.
    supports: confounders
  - section: Executive summary
    page: 662
    quote: Pilot imaging data suggest that functional and structural imaging changes occur in a right
      fronto-temporal network in patients undergoing an intense course of MIT.
    supports: limitation
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
    dose: up to 1.5 h/day, 5 days/week over a period of several months
- id: f3
  target: right_arcuate_fasciculus
  target_kind: region
  claim: Intense melodic intonation therapy is associated with an increase in the size and fiber length
    of the right arcuate fasciculus.
  direction: likely
  relationship: treatment_response
  citation: '@Schlaug2010'
  method: DTI
  design: case-series
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 1
    population: patient treated with MIT
    time_post_onset: not_reported
    phase: chronic
    age_range: not_reported
    handedness: not_reported
    language: not_reported
  statistics:
    threshold: not_reported
    effect_size: not_reported
    p_value: not_reported
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Right arcuate fasciculus (AF)
  imaging_details:
    reference_space: not_reported
    atlases_used: []
    preprocessing_pipeline: not_reported
  author_limitations:
  - The most likely explanation for these imaging results are changes in myelination... however, changes
    in axon diameter... are also possible.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 659
    confidence: high
    flags:
    - n=1 for DTI finding
  source_passages:
  - section: Results
    page: 659
    quote: There is a visible increase in the size (number of fibers and volume of tract) and length of
      fibers of the right arcuate fasciculus when the acquisition before therapy (A) is compared with
      the acquisition after therapy (B).
    supports: claim
  - section: Results
    page: 659
    quote: The most likely explanation for these imaging results are changes in myelination [48-50]; however,
      changes in axon diameter owing to changes in myelin or axon density, themselves owing to axonal
      sprouting, are also possible [51-53].
    supports: limitation
  therapy:
    id: melodic_intonation_therapy
    name: Melodic Intonation Therapy
    dose: up to 1.5 h/day, 5 days/week over a period of several months
---

This paper discusses the mechanisms and neural correlates of Melodic Intonation Therapy (MIT), specifically highlighting its ability to engage right-hemisphere homologous regions in patients with large left-hemisphere lesions.
