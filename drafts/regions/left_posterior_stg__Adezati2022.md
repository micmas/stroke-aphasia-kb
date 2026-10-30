---
schema_version: 2.8
id: left_posterior_stg
name: "Left Posterior Superior Temporal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the posterior superior temporal lobe is associated with auditory sentence comprehension deficits."
    direction: likely
    relationship: causal
    citation: "@Adezati2022"
    method: [VLSM, MLPA]
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 50
      population: "aphasia secondary to a single left hemisphere stroke"
      time_post_onset: "2 months - 14 years"
      phase: chronic
      age_range: "mean 52.14 (SD 15.12)"
      handedness: "44:4:2 (R:L:A)"
      language: not_reported
    statistics:
      threshold: "continuous permutation-based Family Wise Error Rate (FWER) at p < 0.05"
      effect_size: not_reported
    lesion_mapping:
      analysis: univariate
      n_analysed: 50
      min_lesion_overlap: ">= 10% of the participants (minimum n = 5)"
      lesion_volume_correction: direct
      multiple_comparisons: permutation_fwe
    confounders_controlled:
      - "lesion size"
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "Suprathreshold voxels identified via VLSM and SCCAN in the posterior superior temporal lobe (STG, MTG, and Heschl's gyrus)."
    imaging_details:
      field_strength: "3T"
      preprocessing_pipeline: "LINDA package in R; symmetric normalization to Colin27 space"
      reference_space: other
      atlases_used: ["AAL"]
    author_limitations:
      - "The sample size (N=50) is smaller than some prior studies (e.g., Lwi et al., N=168)."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: ["reference_space is Colin27, not MNI152"]
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "The key findings were that lesions in the posterior superior temporal lobe and inferior frontal gyrus (pars triangularis) were associated with sentence comprehension deficits, which was observed in both mass univariate and multivariate lesion-symptom mapping."
        supports: claim
      - section: "Methods - Data"
        page: 2
        quote: "Prospectively collected Magnetic Resonance Imaging (MRI) and psycholinguistic data from 50 participants with aphasia secondary to a single left hemisphere stroke were analysed."
        supports: sample
      - section: "Statistical analysis"
        page: 4
        quote: "All analyses were also corrected for lesion size using direct total lesion volume control (dTLVC) (Mirman et al., 2015)."
        supports: confounders
      - section: "Statistical analysis"
        page: 4
        quote: "Mass-univariate LSM results were corrected for multiple comparisons using continuous permutation-based Family Wise Error Rate (FWER) at p < 0.05"
        supports: statistics
      - section: "Discussion"
        page: 4
        quote: "Note that Lwi et al. had a much larger sample size (N = 168) than the present study (N = 50)."
        supports: limitation
---

Finding f1 reports that damage to the posterior superior temporal lobe (including STG and MTG) is associated with deficits in auditory sentence comprehension as measured by the Token Test.
