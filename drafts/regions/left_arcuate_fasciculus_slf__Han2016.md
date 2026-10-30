---
schema_version: 2.8
id: left_arcuate_fasciculus_slf
name: Left Arcuate Fasciculus and Superior Longitudinal Fascicle (Dorsal Language Pathway)
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: phonological_production
  target_kind: impairment
  claim: Damage to the left superior longitudinal fasciculus (SLF) is associated with impaired phonological
    encoding in speech production, as evidenced by increased nonword errors in naming and reduced accuracy
    in word reading aloud.
  direction: likely
  relationship: causal
  citation: '@Han2016'
  method:
  - LSM
  - DTI
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 69
    population: patients with brain damage (majority stroke)
    time_post_onset: mean = 7 months; standard deviation (SD) = 12; range 1-86
    phase: chronic
    age_range: mean 46 years (SD = 13; range 20-76)
    handedness: all right-handed
    language: native Chinese speakers
  statistics:
    threshold: Bonferroni corrected p < 0.01
    effect_size: lesion percentage partial r = -0.52 to -0.57; FA partial r = 0.52 to 0.55
  lesion_mapping:
    analysis: univariate
    n_analysed: 69
    min_lesion_overlap: '>= 5 patients'
    lesion_volume_correction: covariate
    multiple_comparisons: bonferroni
  confounders_controlled:
  - total lesion volume
  - age
  - gender
  - education level
  - gray matter lesions in phonological-relevant regions
  - auditory lexical decision score
  - picture associative matching score
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU white-matter tractography atlas (25 % probability map)
    description: Left superior longitudinal fasciculus (SLF) as defined by the JHU WM template.
  imaging_details:
    field_strength: 1.5T
    modalities:
    - modality: T1
      sequence: 3D T1-weighted
      voxel_size_mm:
      - 0.49
      - 0.49
      - 0.7
    - modality: DTI
      voxel_size_mm:
      - 1.95
      - 1.95
      - 2.6
      b_values:
      - 0
      - 1000
    preprocessing_pipeline: SPM5 co-registration + BrainVoyager QX v2.0 registration to Talairach/MNI
      + PANDA (FSL 4.1.7) for DTI
    reference_space: MNI152
    atlases_used:
    - JHU white-matter tractography atlas
  author_limitations:
  - The current study is constrained by the spatial scale of the John Hopkins University white-matter
    template.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, pages 583-586
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: the integrity of the left SLF in both the structural and diffusion tensor imaging measures
      consistently predicted the severity of phonological encoding impairment in the two phonological
      production tasks.
    supports: claim
  - section: Participants
    page: 3
    quote: The mean age of the remaining 69 patients (55 males) was 46 years (SD = 13; range 20-76)...
      all patients were right-handed.
    supports: sample
  - section: Brain-behavior mapping analysis
    page: 5
    quote: For the lesion percentage measure... the lesion percentage... was correlated with the patients'
      phonological encoding scores... partialing out total lesion volume. The results were adjusted for
      the 17 tracts using the Bonferroni correction method (p < 0.0006, corrected p < 0.01).
    supports: method
  - section: Results
    page: 8
    quote: the lesion percentages of the left SLF were significantly negatively correlated with phonological
      encoding scores in both the oral picture naming and word reading tasks, with total lesion volume
      as a covariate (Bonferroni corrected ps < 0.01).
    supports: statistics
  - section: Imaging data - Acquisition
    page: 4
    quote: Patients were scanned... with a 1.5T GE SIGNA EXCITE scanner... high resolution three-dimensional
      T1-weighted images... diffusion-weighted images (DWI).
    supports: imaging_details
  - section: Discussion
    page: 12
    quote: The current study is constrained by the spatial scale of the John Hopkins University white-matter
      template and can only be interpreted with the template tract.
    supports: limitation
---
