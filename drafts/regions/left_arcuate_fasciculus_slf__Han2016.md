---
schema_version: 2.8
id: left_arcuate_fasciculus_slf
name: Left Arcuate Fasciculus and Superior Longitudinal Fascicle (Dorsal Language Pathway)
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
members: []
networks: []
tracts_adjacent: []
findings:
- id: f1
  target: phonological_production
  target_kind: impairment
  claim: Damage to the left superior longitudinal fasciculus (SLF) is associated with impaired phonological
    encoding in speech production, as measured by nonword errors in naming and word reading accuracy.
  direction: likely
  relationship: causal
  citation: '@Han2016'
  method:
  - DTI
  - LSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 69
    population: patients with brain damage (stroke and traumatic brain injury)
    time_post_onset: 'at least one-month post-onset [disease duration: mean = 7 months; standard deviation
      (SD) = 12; range 1–86]'
    phase: chronic
    age_range: mean 46 years (SD = 13; range 20–76)
    handedness: all right-handed
    language: native Chinese speakers
    cohort: not_reported
  statistics:
    threshold: Bonferroni corrected p < 0.01
    effect_size: lesion percentage partial r = -0.52; mean FA partial r = 0.52 (naming); lesion percentage
      partial r = -0.57; mean FA partial r = 0.55 (reading)
    p_value: p < 0.01
  lesion_mapping:
    analysis: univariate
    n_analysed: 69
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: bonferroni
  confounders_controlled:
  - total lesion volume
  - age
  - gender
  - education level
  - grey matter lesions in premotor/precentral/postcentral/supramarginal gyrus
  - auditory lexical decision score
  - picture associative matching score
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU white-matter tractography atlas (25 % probability map)
    description: Left superior longitudinal fasciculus (SLF) as defined by the JHU WM template.
  imaging_details:
    field_strength: 1.5T
    reference_space: MNI152
    atlases_used:
    - JHU white-matter tractography atlas
    preprocessing_pipeline: SPM5 co-registration, BrainVoyager QX v2.0 registration to Talairach, ANTs
      transformation to MNI; PANDA pipeline (BET, Eddycorrect, DTIFIT) for DTI
    modalities:
    - modality: T1
      sequence: 3D T1-weighted
      voxel_size_mm:
      - 0.49
      - 0.49
      - 0.7
    - modality: T2
      sequence: FLAIR
      voxel_size_mm:
      - 0.49
      - 0.49
      - 5
    - modality: DTI
      voxel_size_mm:
      - 1.95
      - 1.95
      - 2.6
      n_directions: 32
      b_values:
      - 0
      - 1000
  author_limitations:
  - The current study is constrained by the spatial scale of the John Hopkins University white-matter
    template and can only be interpreted with the template tract.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, pages 8-11
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: the integrity of the left SLF in both the structural and diffusion tensor imaging measures
      consistently predicted the severity of phonological encoding impairment in the two phonological
      production tasks.
    supports: claim
  - section: Materials and methods - Participants
    page: 3
    quote: The mean age of the remaining 69 patients (55 males) was 46 years (SD = 13; range 20–76)...
      all patients were right-handed.
    supports: sample
  - section: Materials and methods - Participants
    page: 3
    quote: 'at least one-month post-onset [disease duration: mean = 7 months; standard deviation (SD)
      = 12; range 1–86]'
    supports: sample
  - section: Brain-behavior mapping analysis
    page: 5
    quote: The results were adjusted for the 17 tracts using the Bonferroni correction method (p < 0.0006,
      corrected p < 0.01).
    supports: statistics
  - section: Brain-behavior mapping analysis
    page: 5
    quote: correlate the lesion percentage and the mean FA value of each tract and phonological encoding
      index, with whole-brain total lesion volume as a covariate.
    supports: method
  - section: Imaging data - Preprocessing
    page: 5
    quote: registered into Talairach space via BrainVoyager QX v2.0... the lesion description was transformed
      into the Montreal Neurological Institute (MNI) space.
    supports: imaging_details
  - section: Discussion
    page: 12
    quote: The current study is constrained by the spatial scale of the John Hopkins University white-matter
      template and can only be interpreted with the template tract
    supports: limitation
---
