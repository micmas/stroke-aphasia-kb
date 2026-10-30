---
schema_version: 2.8
id: left_temporoparietal_white_matter_crossroad
name: "Left Temporoparietal White Matter Crossroad"
kind: network
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
members: ["left_arcuate_fasciculus", "left_inferior_fronto_occipital_fasciculus"]
notes: "New region ID for the combined dorsal/ventral disconnection area identified by Rosso et al. 2015."

findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Damage to a white matter region at the intersection of the arcuate and inferior fronto-occipital fasciculi is strongly associated with global aphasia severity in chronic stroke."
    direction: likely
    relationship: causal
    citation: "@Rosso2015"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 23
      population: "chronic poststroke aphasic patients"
      time_post_onset: "mean +/- SD time poststroke = 16 +/- 21 months"
      phase: chronic
      age_range: "mean +/- SD age = 57 +/- 19 years"
      handedness: "all right-handed"
      language: "French native speaker"
    statistics:
      threshold: "height threshold of 0.001 (uncorrected) and corrected at the cluster level by a familywise error threshold at P < .05"
      effect_size: "correlation coefficient = -0.833"
      p_value: "P < .0001"
    lesion_mapping:
      analysis: univariate
      n_analysed: 23
      min_lesion_overlap: not_reported
      lesion_volume_correction: not_reported
      multiple_comparisons: fwe
    confounders_controlled: ["age", "time poststroke"]
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "A single cluster (1922 voxels) including the posterior arm of internal capsule, posterior portion of the external capsule, white matter underlying the supramarginalis cortex, and posterior portion of the superior temporal gyrus."
    imaging_details:
      field_strength: not_reported
      modalities:
        - modality: T1
          sequence: MPRAGE
          voxel_size_mm: [1, 1, 1]
          TR_ms: 2300
          TE_ms: 4.18
        - modality: DTI
          sequence: spin-echo echo-planar
          voxel_size_mm: [2, 2, 2]
          n_directions: 60
          b_values: [1500]
      preprocessing_pipeline: "FSL 3.3 eddy current correction + FDT FA maps + SPM8 normalization to MNI space + 6mm Gaussian smoothing"
      reference_space: MNI152
      atlases_used: ["Jülich Atlas"]
      coordinates_reported:
        - region: "Left Inferior fronto-occipital F."
          mni: [-32, -30, 2]
        - region: "Left arcuate F. Left supramarginalis"
          mni: [-48, -46, 18]
        - region: "Left arcuate F. Left pSTG"
          mni: [-38, -44, 8]
    author_limitations:
      - "The number of subjects was relatively low, limiting the subgroup analysis."
      - "The role of Wallerian degeneration cannot be totally dismissed."
      - "The simultaneous lesion of the dorsal and ventral language pathway explained only 60% of the variance of aphasia severity."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, pages 290-291"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 290
        quote: "The voxel-based regression analysis between normalized FA maps and ART scores at the time of MRI showed that regions associated with greater aphasia severity were located in a single cluster (n = 1922 voxels, P < .0001)"
        supports: claim
      - section: "Methods"
        page: 288
        quote: "Twenty-three right-handed patients (14 males, mean +/- standard deviation [SD] age = 57 +/- 19 years, mean +/- SD time poststroke = 16 +/- 21 months) participated in the study."
        supports: sample
      - section: "Methods"
        page: 289
        quote: "We then performed a voxel-based multiple regression analysis using SPM8 with the smoothed and normalized FA maps and the language scores as variables of interest (ART scores)."
        supports: method
      - section: "Results"
        page: 291
        quote: "The FA values extracted from each subject from the area determined by the voxel-based analysis correlated well with the ART scores (correlation coefficient = -0.833, 95% CI = -0.927 to -0.641, P < .001; adjusted R2 = 0.680)."
        supports: statistics
      - section: "Methods"
        page: 289
        quote: "In the general linear model, age and time poststroke were entered as confounding covariates."
        supports: confounders
      - section: "Results"
        page: 290
        quote: "including the posterior arm of internal capsule, the posterior portion of the external capsule and the white matter underlying the supra-marginalis cortex, and the posterior portion of the superior temporal gyrus, that is, the temporoparietal junction"
        supports: region_definition
      - section: "Methods"
        page: 288
        quote: "anatomical 3-dimensional T1-weighted MPRAGE images (TR = 2.3 seconds; TE = 4.18 ms... voxel size = 1 x 1 x 1 mm3); spin-echo echo-planar diffusion tensor imaging (TR = 10 seconds, TE = 87 ms, voxel size = 2 x 2 x 2 mm3, 60 slices, 60 gradient encoded directions with a b value of 1500 s/mm2)"
        supports: imaging_details
      - section: "Discussion"
        page: 293
        quote: "First, although the total sample size was in the higher range of published DTI studies, the number of subjects was relatively low, limiting the subgroup analysis"
        supports: limitation
---
