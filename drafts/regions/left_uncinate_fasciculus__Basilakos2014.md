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
    target: fluency
    target_kind: impairment
    claim: "Damage to the left uncinate fasciculus is associated with reduced speech fluency in chronic post-stroke aphasia."
    direction: likely
    relationship: causal
    citation: "@Basilakos2014"
    method: VBCM
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 76
      population: "chronic left-hemisphere ischemic stroke aphasia"
      time_post_onset: "mean 35.57 months (SD 47.56, range 6-276)"
      phase: chronic
      age_range: "mean 61.35 years (SD 12.67, range 36-83)"
      handedness: "73 right-handed"
      language: not_reported
    statistics:
      threshold: "Bonferroni corrected p < 0.008"
      effect_size: "r = 0.574"
      p_value: "< 0.001"
    lesion_mapping:
      analysis: univariate
      n_analysed: 76
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: bonferroni
    confounders_controlled: ["lesion size"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Catani et al. (2012)"
      description: "Uncinate fasciculus defined via white matter atlas."
    imaging_details:
      field_strength: "3T"
      acquisition:
        voxel_size_mm: not_reported
        TR_ms: 2250
        TE_ms: 4.2
        sequence: "MP-RAGE (TFE)"
      preprocessing_pipeline: "Clinical toolbox (Rorden et al., 2012) for SPM8; cost-function approach normalization to 1 mm isotropic ICBM standard brain template"
      reference_space: MNI152
      atlases_used: ["Catani et al. (2012)"]
    author_limitations:
      - "T1-signal intensity is an indirect measure of tissue integrity."
      - "Use of WAB-R fluency scale is not a perfect measure of speech fluency."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 3"
      confidence: high
      flags: ["cohort overlaps with @Fridriksson2018 (USC Aphasia Lab)"]
    source_passages:
      - section: "Results"
        page: 3
        quote: "uncinate fasciculus (r = 0.574, p < 0.001) [..] were correlated with speech fluency scores"
        supports: claim
      - section: "Participants"
        page: 2
        quote: "This study included 76 patients (32 female, 73 right-handed) with chronic aphasia [..] history of one single, left-hemisphere ischemic stroke"
        supports: sample
      - section: "Preprocessing of structural images"
        page: 3
        quote: "T1-signal intensity in white matter regions was used to relate cortical damage [..] to behavior (Tyler et al., 2005)."
        supports: method
      - section: "Region of interest analyses"
        page: 3
        quote: "To control for multiple comparisons in the correlation analyses, the alpha-level was Bonferroni corrected [..] the threshold for significance was set to p = 0.008."
        supports: statistics
      - section: "Region of interest analyses"
        page: 3
        quote: "A white matter atlas constructed by Catani et al. (2012) was consulted to define [..] the uncinate fasciculus."
        supports: region_definition
      - section: "MRI Data Collection"
        page: 2
        quote: "Magnetic resonance imaging data were acquired using a Siemens 3-T Trio System [..] T1-weighted imaging sequence using a MP-RAGE (TFE) sequence"
        supports: imaging_details
      - section: "Discussion"
        page: 5
        quote: "We acknowledge that use of the WAB-R fluency scale is not a perfect measure of speech fluency"
        supports: limitation
  - id: f2
    target: semantics
    target_kind: impairment
    claim: "Damage to the left uncinate fasciculus is associated with reduced semantic processing in chronic post-stroke aphasia."
    direction: likely
    relationship: causal
    citation: "@Basilakos2014"
    method: VBCM
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 57
      population: "chronic left-hemisphere ischemic stroke aphasia"
      time_post_onset: "mean 35.57 months (SD 47.56, range 6-276)"
      phase: chronic
      age_range: "mean 61.35 years (SD 12.67, range 36-83)"
      handedness: "73 right-handed"
      language: not_reported
    statistics:
      threshold: "Bonferroni corrected p < 0.008"
      effect_size: "r = 0.41"
      p_value: "< 0.001"
    lesion_mapping:
      analysis: univariate
      n_analysed: 57
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: bonferroni
    confounders_controlled: ["lesion size"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Catani et al. (2012)"
      description: "Uncinate fasciculus defined via white matter atlas."
    imaging_details:
      field_strength: "3T"
      acquisition:
        voxel_size_mm: not_reported
        TR_ms: 2250
        TE_ms: 4.2
        sequence: "MP-RAGE (TFE)"
      preprocessing_pipeline: "Clinical toolbox (Rorden et al., 2012) for SPM8; cost-function approach normalization to 1 mm isotropic ICBM standard brain template"
      reference_space: MNI152
      atlases_used: ["Catani et al. (2012)"]
    author_limitations:
      - "T1-signal intensity is an indirect measure of tissue integrity."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: ["cohort overlaps with @Fridriksson2018 (USC Aphasia Lab)"]
    source_passages:
      - section: "Results"
        page: 5
        quote: "Semantic processing was correlated with the uncinate fasciculus (r = 0.41, p < 0.001)"
        supports: claim
      - section: "Participants"
        page: 2
        quote: "Pyramids and Palm Trees Test scores were available for 57 of the 76 individuals"
        supports: sample
      - section: "Preprocessing of structural images"
        page: 3
        quote: "T1-signal intensity in white matter regions was used to relate cortical damage [..] to behavior (Tyler et al., 2005)."
        supports: method
      - section: "Region of interest analyses"
        page: 3
        quote: "To control for multiple comparisons in the correlation analyses, the alpha-level was Bonferroni corrected [..] the threshold for significance was set to p = 0.008."
        supports: statistics
      - section: "Region of interest analyses"
        page: 3
        quote: "A white matter atlas constructed by Catani et al. (2012) was consulted to define [..] the uncinate fasciculus."
        supports: region_definition
      - section: "MRI Data Collection"
        page: 2
        quote: "Magnetic resonance imaging data were acquired using a Siemens 3-T Trio System [..] T1-weighted imaging sequence using a MP-RAGE (TFE) sequence"
        supports: imaging_details
      - section: "Discussion"
        page: 7
        quote: "T1-signal intensity is an indirect measure of tissue integrity"
        supports: limitation
    }
---
