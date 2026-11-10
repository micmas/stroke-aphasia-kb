---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: form_to_meaning
  target_kind: impairment
  claim: Integrity of the left arcuate fasciculus posterior segment is strongly associated with auditory
    comprehension in acute and subacute post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Yu2022'
  method: DTI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: r = 0.686
    p_value: '0.000'
  confounders_controlled:
  - lesion load of cortical language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Posterior segment of the left arcuate fasciculus (PSAF) defined by streamlines passing
      through parietal and temporal ROIs but not the frontal ROI.
  imaging_details:
    field_strength: 3T
    acquisition:
      voxel_size_mm:
      - 1
      - 1
      - 1
      TR_ms: 2300
      TE_ms: 2.98
      sequence: MPRAGE
    modalities:
    - modality: T1
      sequence: MPRAGE
      voxel_size_mm:
      - 1
      - 1
      - 1
    - modality: DTI
      sequence: EPI
      voxel_size_mm:
      - 2.5
      - 2.5
      - 2.5
      TR_ms: 7200
      TE_ms: 104
      gradient_directions: 64
      b_values:
      - 0
      - 1000
    preprocessing_pipeline: FSL 5.0.9 (Eddy_correct, BET v2.1, FLIRT registration to MNI152)
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: when lesion load was set as a controlled variable, partial correlations revealed that the PSAF
      was significantly strongly related to comprehension, repetition, naming, and AQ
    supports: claim
  - section: Materials and Methods
    page: 2
    quote: Twenty-six right-handed patients... mean time post-stroke = 39.46 days, SD = 32.02
    supports: sample
  - section: Materials and Methods
    page: 4
    quote: MRI data were acquired using a 3-Tesla Siemens Skyra scanner
    supports: imaging_details
  - section: Materials and Methods
    page: 5
    quote: the streamlines passing through both the ROI 2 and ROI 3 but not ROI 1 formed the PSAF
    supports: region_definition
  - section: Discussion
    page: 16
    quote: the number of patients was somewhat limited... the method of language assessment applied in
      this study may be insufficient to fully reflect the real language ability of our patients
    supports: limitation
  author_limitations:
  - Small sample size (n=26).
  - Language assessment may not fully reflect real ability, especially for fluency and naming.
  - Deterministic fiber-tracking algorithm may affect reconstruction in crossed fibers.
- id: f2
  target: phonological_production
  target_kind: impairment
  claim: Integrity of the left arcuate fasciculus posterior segment is strongly associated with speech
    repetition in acute and subacute post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Yu2022'
  method: DTI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: r = 0.708
    p_value: '0.000'
  confounders_controlled:
  - lesion load of cortical language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Posterior segment of the left arcuate fasciculus (PSAF).
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: when lesion load was set as a controlled variable, partial correlations revealed that the PSAF
      was significantly strongly related to comprehension, repetition, naming, and AQ
    supports: claim
  - section: Discussion
    page: 15
    quote: our results support the relationship between damage to the left PSAF and comprehension and
      repetition deficits in acute/subacute PSA
    supports: claim
  author_limitations:
  - Small sample size (n=26).
  - Deterministic fiber-tracking algorithm may affect reconstruction in crossed fibers.
- id: f3
  target: anomia
  target_kind: impairment
  claim: Integrity of the left arcuate fasciculus posterior segment is associated with naming performance
    in acute and subacute post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Yu2022'
  method: DTI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: r = 0.488
    p_value: '0.013'
  confounders_controlled:
  - lesion load of cortical language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Posterior segment of the left arcuate fasciculus (PSAF).
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: when lesion load was set as a controlled variable, partial correlations revealed that the PSAF
      was significantly strongly related to comprehension, repetition, naming, and AQ
    supports: claim
  author_limitations:
  - Small sample size (n=26).
  - The method of language assessment applied in this study may be insufficient to fully reflect the real
    language ability of our patients, particularly in terms of... naming
- id: f4
  target: severity_metric
  target_kind: predictor
  claim: Integrity of the left arcuate fasciculus posterior segment is strongly associated with overall
    aphasia severity (AQ) in acute and subacute post-stroke aphasia.
  direction: likely
  relationship: correlational
  citation: '@Yu2022'
  method: DTI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: r = 0.695
    p_value: '0.000'
  confounders_controlled:
  - lesion load of cortical language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Posterior segment of the left arcuate fasciculus (PSAF).
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: when lesion load was set as a controlled variable, partial correlations revealed that the PSAF
      was significantly strongly related to comprehension, repetition, naming, and AQ
    supports: claim
  author_limitations:
  - Small sample size (n=26).
- id: f5
  target: fluency
  target_kind: impairment
  claim: No significant correlation was found between the anterior segment of the left arcuate fasciculus
    and language performance, including fluency.
  direction: no_effect
  relationship: correlational
  citation: '@Yu2022'
  method: DTI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 26
    population: acute/subacute post-stroke aphasia
    time_post_onset: mean 39.46 days (SD 32.02)
    phase: early_subacute
    age_range: mean 54.50 years (SD 11.30)
    handedness: all right-handed
    language: Chinese
  statistics:
    threshold: alpha = 0.05
    effect_size: r = 0.231
    p_value: '0.267'
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Anterior segment of the left arcuate fasciculus (ASAF).
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 7
    quote: No significant correlation was found between the ASAF and language measures.
    supports: claim
  author_limitations:
  - Small sample size (n=26).
  - the 10-point rating scale within the WAB to evaluate verbal fluency... might insufficiently reflect
    the multidimensional nature of verbal fluency
---
