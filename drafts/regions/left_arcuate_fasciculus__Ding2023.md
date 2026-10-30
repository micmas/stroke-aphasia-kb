---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: discourse_content
  target_kind: impairment
  claim: Damage to the left arcuate fasciculus is associated with impaired quantity and efficiency of
    informative spoken discourse in chronic aphasia.
  direction: likely
  relationship: causal
  citation: '@Ding2023'
  method:
  - MLPA
  - tractography
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 66
    population: participants with aphasia following left hemisphere stroke
    time_post_onset: M = 53, Med = 23 months
    phase: chronic
    age_range: M = 59, Med = 59 (Range 31-79)
    handedness: right-handed
    language: native English speakers
    cohort: not_reported
  statistics:
    threshold: P < 0.05 (MLPA CV correlation)
    effect_size: 'r = -0.26 (for #CIUs), r = -0.40 (for CIUs/min)'
  lesion_mapping:
    analysis: multivariate
    n_analysed: 66
    min_lesion_overlap: '>10% of the participants'
    lesion_volume_correction: covariate
    multiple_comparisons: not_reported
  confounders_controlled:
  - total lesion size
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Left arcuate fasciculus extracted from the HCP1065 atlas.
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - HCP1065
    preprocessing_pipeline: automated symmetric diffeomorphic registration algorithm to Colin27 template
  author_limitations:
  - The present results shed light on persistent impairments in spoken discourse but not on recovery of
    spoken discourse production.
  - The current data did not include any participants with damage in the right hemisphere.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, pages 6-9
    confidence: high
    flags:
    - target_id discourse_content is forward-looking
  source_passages:
  - section: Abstract
    page: 1
    quote: impaired production of relevant information was associated with damage to anterior dorsal white
      matter pathways, specifically the arcuate fasciculus, frontal aslant tract and superior longitudinal
      fasciculus.
    supports: claim
  - section: Materials and methods - Participants
    page: 3
    quote: The data set consisted of behavioural data from 80 participants who had suffered a left hemisphere
      stroke that produced some degree of language impairment.
    supports: sample
  - section: Statistical analyses - Lesion LSM
    page: 5
    quote: To investigate the lesion correlates of CIU impairment, we performed a multivariate voxel-wise
      LSM using the SCCAN algorithm implemented in the R package LESYMAP.
    supports: method
  - section: Statistical analyses - Tract-based LSM
    page: 5
    quote: partial correlations between CIU measures and each tract's lesion percentage were calculated,
      accounting for the effect of total lesion size.
    supports: method
  - section: Results - Tract-wise LSM
    page: 9
    quote: '#CIUs and CIUs/min significantly correlated with the dorsal pathways, including AF, FAT and
      SLF...'
    supports: statistics
  - section: Discussion
    page: 11
    quote: The present results shed light on persistent impairments in spoken discourse but not on recovery
      of spoken discourse production.
    supports: limitation
---
