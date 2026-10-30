---
schema_version: 2.8
id: left_uncinate_fasciculus
name: "Left Uncinate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: tool_concept
    target_kind: impairment
    claim: "Damage to the left uncinate fasciculus (lUF) is associated with deficits in tool conceptual processing."
    direction: likely
    relationship: causal
    citation: "@Bi2015"
    method: [tractography, VLSM]
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 86
      population: "brain-damaged patients"
      time_post_onset: "mean 6 months, SD 11, range 1-86"
      phase: chronic
      age_range: "mean 45 years (SD 13, range 19-76)"
      handedness: "all right handed"
      language: "native Chinese speakers"
    statistics:
      threshold: "FDR q <= 0.05"
      effect_size: "not_reported"
    lesion_mapping:
      analysis: univariate
      n_analysed: 86
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: fdr
    confounders_controlled:
      - "total lesion volume"
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Left UF as defined by the JHU WM tractography atlas."
    imaging_details:
      field_strength: "1.5T"
      modalities:
        - modality: T1
          sequence: MP-RAGE
          voxel_size_mm: [0.49, 0.49, 0.7]
        - modality: DTI
          voxel_size_mm: [1.95, 1.95, 2.6]
          n_directions: 32
          b_values: [0, 1000]
      preprocessing_pipeline: "SPM5 coregistration + ANTs normalization to Talairach/MNI space; PANDA pipeline for DTI (BET, Eddycorrect, DTIFIT)"
      reference_space: MNI152
      atlases_used: ["AAL", "JHU WM tractography atlas"]
    author_limitations:
      - "Statistical power for each tract varied due to unequal numbers of patients having a lesion in a given tract."
      - "DTI is an indirect measure of real fiber connections and is prone to errors in resolving fiber crossings."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 10"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 10
        quote: "The common voxels of VLSM and VFSM results... overlapped with four left tracts of the JHU template, including lATR (11%), lIFOF (11%), lSLF (2%), and lUF (15%)."
        supports: claim
---
