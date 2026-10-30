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
  target: tool_use
  target_kind: impairment
  claim: Damage to left hemisphere tracts overlapping with the superior longitudinal fasciculus, specifically
    those connecting the left IFG to the left IPL and the left DLPMC to the left IFG/VPMC, is associated
    with deficits in tool use.
  direction: likely
  relationship: causal
  citation: '@Bi2015'
  method:
  - tractography
  - VLSM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 86
    population: brain-damaged patients
    time_post_onset: mean 6 months, SD 11, range 1-86
    phase: chronic
    age_range: mean 45 years (SD 13, range 19-76)
    handedness: all right handed
    language: native Chinese speakers
  statistics:
    threshold: FDR q <= 0.05
    effect_size: 'partial r: -0.47 to -0.29'
  lesion_mapping:
    analysis: univariate
    n_analysed: 86
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: fdr
  confounders_controlled:
  - total lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Tracts connecting left IFG-lIPL, lDLPMC-lIFG, and lDLPMC-lVPMC, overlapping with the
      left SLF of the JHU template.
  imaging_details:
    field_strength: 1.5T
    modalities:
    - modality: T1
      sequence: MP-RAGE
      voxel_size_mm:
      - 0.49
      - 0.49
      - 0.7
    - modality: DTI
      voxel_size_mm:
      - 1.95
      - 1.95
      - 2.6
      n_directions: 32
      b_values:
      - 0
      - 1000
    preprocessing_pipeline: SPM5 coregistration + ANTs normalization to Talairach/MNI space; PANDA pipeline
      for DTI (BET, Eddycorrect, DTIFIT)
    reference_space: MNI152
    atlases_used:
    - AAL
    - JHU WM tractography atlas
  author_limitations:
  - Statistical power for each tract varied due to unequal numbers of patients having a lesion in a given
    tract.
  - DTI is an indirect measure of real fiber connections and is prone to errors in resolving fiber crossings.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, pages 8-9
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: three left hemisphere tracts connecting frontoparietal and intrafrontal areas overlapping with
      left superior longitudinal fasciculus are crucial for tool use such that larger lesion and lower
      mean FA values on these tracts were associated with more severe tool use deficits.
    supports: claim
  - section: Participants
    page: 3
    quote: Eighty-six brain-damaged patients (65 males) were recruited for this study... was at least
      1 month post-onset (mean 6 months, SD 11, range 1-86)
    supports: sample
  - section: Testing the effects of observed tracts in tool processing with patients
    page: 6
    quote: we performed partial correlation analyses between the lesion percentages or mean FA values
      with tool behavioral scores across patients, with each patient's whole lesion volume as covariate.
    supports: method
  - section: Results
    page: 8
    quote: 'For tool use, the lesion percentage analysis revealed 11 tracts with lesion percentages that
      were significantly negatively correlated with tool use scores (partial r: -0.47 to -0.29, FDR q
      <= 0.05)'
    supports: statistics
  - section: Discussion
    page: 13
    quote: In the patient analyses the statistical power for each tract varied due to the unequal numbers
      of patients having a lesion in a given tract.
    supports: limitation
  - section: Discussion
    page: 13
    quote: DTI is an indirect measure of real fiber connections and is especially prone to errors in resolving
      fiber crossings
    supports: limitation
- id: f2
  target: tool_concept
  target_kind: impairment
  claim: Damage to left hemisphere tracts connecting frontal and temporal/parietal regions, including
    those overlapping with the left SLF, IFOF, UF, and ATR, is associated with deficits in tool conceptual
    processing.
  direction: likely
  relationship: causal
  citation: '@Bi2015'
  method:
  - tractography
  - VLSM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 86
    population: brain-damaged patients
    time_post_onset: mean 6 months, SD 11, range 1-86
    phase: chronic
    age_range: mean 45 years (SD 13, range 19-76)
    handedness: all right handed
    language: native Chinese speakers
  statistics:
    threshold: FDR q <= 0.05
    effect_size: 'partial r: -0.54 to -0.40'
  lesion_mapping:
    analysis: univariate
    n_analysed: 86
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: fdr
  confounders_controlled:
  - total lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Eight left hemisphere tracts connecting frontal and temporal/parietal regions, overlapping
      with lSLF, lIFOF, lUF, and lATR.
  imaging_details:
    field_strength: 1.5T
    modalities:
    - modality: T1
      sequence: MP-RAGE
      voxel_size_mm:
      - 0.49
      - 0.49
      - 0.7
    - modality: DTI
      voxel_size_mm:
      - 1.95
      - 1.95
      - 2.6
      n_directions: 32
      b_values:
      - 0
      - 1000
    preprocessing_pipeline: SPM5 coregistration + ANTs normalization to Talairach/MNI space; PANDA pipeline
      for DTI (BET, Eddycorrect, DTIFIT)
    reference_space: MNI152
    atlases_used:
    - AAL
    - JHU WM tractography atlas
  author_limitations:
  - Statistical power for each tract varied due to unequal numbers of patients having a lesion in a given
    tract.
  - DTI is an indirect measure of real fiber connections and is prone to errors in resolving fiber crossings.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 9
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: These tracts and five additional left hemisphere tracts connecting frontal and temporal/parietal
      regions, mainly overlapping with left superior longitudinal fasciculus, inferior frontooccipital
      fasciculus, uncinate fasciculus, and anterior thalamic radiation, are crucial for tool concept processing.
    supports: claim
  - section: Results
    page: 9
    quote: 'For tool concept processing, the integrity of eight tracts was correlated significantly negatively
      with tool concept composite scores in the lesion analysis... (partial r: -0.54 to -0.40, FDR q <=
      0.01)'
    supports: statistics
---
