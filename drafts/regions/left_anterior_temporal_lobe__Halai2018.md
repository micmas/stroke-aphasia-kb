---
schema_version: 2.8
id: left_anterior_temporal_lobe
name: "Left Anterior Temporal Lobe"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: semantics
    target_kind: impairment
    claim: "Damage to the left anterior temporal region is associated with impaired semantic ability in chronic stroke."
    direction: likely
    relationship: causal
    citation: "@Halai2018"
    method: VBCM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 46
      population: "chronic stroke patients"
      time_post_onset: "at least 12 months post-stroke"
      phase: chronic
      age_range: "mean 65.46 years (SD = 11.49)"
      handedness: "pre-morbidly right-handed"
      language: "native English speakers"
    statistics:
      threshold: "p < 0.005 voxel height, FWE-cluster corrected p < 0.05"
      effect_size: not_reported
    lesion_mapping:
      analysis: univariate
      n_analysed: 46
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: fwe
    confounders_controlled:
      - "lesion volume"
      - "age"
      - "years of education"
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "cluster located in the anterior MTG bordering between TP, ITG, TFG and PHG"
    imaging_details:
      field_strength: "3.0 Tesla"
      acquisition:
        voxel_size_mm: [1.0, 1.0, 1.0]
        TR_ms: 9.0
        TE_ms: 3.93
        sequence: "T1-weighted inversion recovery"
      preprocessing_pipeline: "SPM8 modified unified segmentation-normalisation procedure optimized for focal lesioned brains"
      reference_space: MNI152
      atlases_used: []
    author_limitations:
      - "The PCA model includes the effect of all errors simultaneously, making it harder to detect effects unique to a given factor."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 5
        quote: "The semantic ability cluster was located in the anterior MTG bordering between TP, inferior temporal gyrus (ITG), temporal fusiform gyrus (TFG) and PHG."
        supports: claim
      - section: "Materials and methods"
        page: 2
        quote: "All patients were at least 12 months post-stroke at the time of scanning and assessment... there were 33 males and 13 females with a mean age of 65.46 years (SD = 11.49)."
        supports: sample
      - section: "Analysis of neuroimaging data"
        page: 3
        quote: "The normalised and bias-corrected T1-weighted images were used to determine the brain regions where tissue concentration correlated with individual measures or PCA factor scores using a voxel-based correlational methodology (VBCM) (Tyler et al., 2005)"
        supports: method
      - section: "Results"
        page: 5
        quote: "Fig. 2 shows the signiﬁcant clusters thresholded at p < 0.005 voxel height, FWE-cluster corrected p < 0.05"
        supports: statistics
      - section: "Analysis of neuroimaging data"
        page: 4
        quote: "The participants' lesion volume, age and years of education were entered as covariates in each VBCM."
        supports: confounders
      - section: "Discussion"
        page: 8
        quote: "as the PCA model includes the eﬀect of all errors simultaneously (as a multiple regression), it is much harder to detect eﬀects unique to a given factor."
        supports: limitation
---
