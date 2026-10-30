---
schema_version: 2.8
id: left_ifg_pars_opercularis
name: Left IFG Pars Opercularis (Broca's area, dorsal stream hub)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: brocas_aphasia
  target_kind: impairment
  claim: Damage to the left inferior frontal gyrus pars opercularis is associated with Broca's aphasia,
    although it is not sufficient on its own to cause the syndrome.
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
    threshold: Z = 4.79 (corrected, P < 0.01)
    effect_size: Zmax = 8.67
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
    description: Posterior portion of Broca's area, the pars opercularis (referred to as the Broca's area
      cluster or BAC).
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
    quote: A whole-brain NPM analysis revealed that individuals with Broca's aphasia are more likely to
      have damage to the left inferior frontal gyrus compared with those who have other kinds of aphasia
      (Fig. 2). Specifically, most of the damage that predicts Broca's aphasia is located in the posterior
      portion of Broca's area, the pars opercularis.
    supports: claim
  - section: Participants
    page: 4690
    quote: The study sample was selected from a database that includes 76 patients with chronic left hemispheric
      stroke. All patients were at least 6 months post-stroke...
    supports: sample
  - section: VLSM Analyses
    page: 4690
    quote: Lesion comparisons between participants with or without Broca's aphasia were implemented using
      non-parametric mapping (NPM; Rorden et al. 2007) with which independent group t-tests compared the
      presence or absence of a lesion in a given cortical area on a voxel-by-voxel basis between the 2
      groups.
    supports: method
  - section: Results
    page: 4691
    quote: The threshold for statistical significance was Z = 4.79 (corrected, P < 0.01) and the maximum
      voxel value was Z = 8.67.
    supports: statistics
  - section: Image Acquisition and Image Preprocessing
    page: 4690
    quote: each participant underwent MRI using a Siemens 3-T system... T1-MRI images were segmented and
      normalized to the 2-mm3 ICBM standard brain template using cost function masking of the lesion
    supports: imaging_details
  - section: Discussion
    page: 4694
    quote: It is a caveat that the WAB does not specifically test for grammatical processing problems...
      Moreover, a difference in one point on this scale could, for example, distinguish a given patient
      being classified as having Broca's aphasia as opposed to conduction aphasia
    supports: limitation
---

Finding f1 describes the primary VLSM result linking the pars opercularis to Broca's aphasia.
