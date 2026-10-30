---
schema_version: 2.8
id: left_superior_temporal_gyrus
name: Left Superior Temporal Gyrus (Dorsal Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: brocas_aphasia
  target_kind: impairment
  claim: In patients with damage to the pars opercularis, additional damage to the left superior temporal
    gyrus (Wernicke's area) distinguishes those with Broca's aphasia from those with other aphasia types.
  direction: likely
  relationship: causal
  citation: '@Fridriksson2015'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 70
    population: chronic left hemispheric stroke
    time_post_onset: at least 6 months post-stroke
    phase: chronic
    age_range: mean 61.04 (SD 12.14)
    handedness: not_reported
    language: not_reported
  statistics:
    threshold: P < 0.01 (for >50% BAC damage group)
    effect_size: Zmax = 10.18 (for >50% BAC damage group)
  lesion_mapping:
    analysis: univariate
    n_analysed: 70
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: fwe
  confounders_controlled: []
  confounders_not_controlled:
  - lesion volume
  region_definition:
    kind: data_driven_cluster
    description: Area mostly confined within the superior temporal gyrus (STG) and inferior parietal cortex,
      referred to as the Wernicke's area cluster (WAC).
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: T1-MRI images segmented and normalized to the 2-mm3 ICBM standard brain template
      using cost function masking of the lesion
    reference_space: MNI152
    atlases_used:
    - Automatic Anatomical Labeling
  author_limitations:
  - The WAB does not specifically test for grammatical processing problems.
  - The fluency rating scale on the WAB suffers from somewhat poor interrater reliability.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 4691
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 4691
    quote: These analyses revealed that individuals with Broca's aphasia are more likely to have damage
      in an area that is mostly confined within the superior temporal gyrus (STG) and, to a lesser extent,
      inferior parietal cortex than participants who also have considerable damage to the portion of the
      pars opercularis... but do not have Broca's aphasia
    supports: claim
  - section: Participants
    page: 4690
    quote: The study sample was selected from a database that includes 76 patients with chronic left hemispheric
      stroke. All patients were at least 6 months post-stroke...
    supports: sample
  - section: VLSM Analyses
    page: 4690
    quote: Lesion comparisons between participants with or without Broca's aphasia were implemented using
      non-parametric mapping (NPM; Rorden et al. 2007)
    supports: method
  - section: Results
    page: 4691
    quote: '''Damage >50%'' Zthresh = 5.97, P < 0.01, Zmax = 10.18'
    supports: statistics
  - section: Image Acquisition and Image Preprocessing
    page: 4690
    quote: each participant underwent MRI using a Siemens 3-T system... T1-MRI images were segmented and
      normalized to the 2-mm3 ICBM standard brain template
    supports: imaging_details
  - section: Discussion
    page: 4694
    quote: It is a caveat that the WAB does not specifically test for grammatical processing problems
    supports: limitation
---

Finding f1 describes the secondary VLSM result showing that Broca's aphasia typically involves both the pars opercularis and the STG.
