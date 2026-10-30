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
    claim: "Tissue concentration in the left anterior temporal lobe, including the temporal pole and anterior MTG, is uniquely related to semantic processing in chronic stroke aphasia."
    direction: likely
    relationship: causal
    citation: "@Woollams2018"
    method: VBCM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 43
      population: "chronic stroke aphasic patients"
      time_post_onset: "at least 12 months post-stroke"
      phase: chronic
      language: "native English speakers"
    statistics:
      threshold: "p < 0.005 voxel level, p ≤ 0.05 family wise error (FWE)-corrected cluster level"
      effect_size: "T = 4.93"
    lesion_mapping:
      analysis: univariate
      n_analysed: 43
      min_lesion_overlap: not_reported
      lesion_volume_correction: none
      multiple_comparisons: fwe
    confounders_controlled: []
    confounders_not_controlled: ["lesion volume"]
    region_definition:
      kind: data_driven_cluster
      description: "Cluster centred on the white matter in the left anterior temporal lobe (ATL), extending to the temporal pole, planum polare, anterior and posterior MTG, and inferior temporal gyrus (ITG), and the anterior fusiform."
    imaging_details:
      field_strength: "3.0 T"
      acquisition:
        sequence: "T1-weighted inversion recovery"
        voxel_size_mm: [1.0, 1.0, 1.0]
      preprocessing_pipeline: "SPM8 modified unified segmentation–normalisation procedure"
      reference_space: MNI152
      atlases_used: ["Harvard–Oxford cortical", "NatBrain-Lab white-matter"]
      coordinates_reported:
        - region: "Middle temporal gyrus ant"
          mni: [-56, -8, -26]
    author_limitations:
      - "Significant results within areas correlated with lesion volume must be interpreted with caution with respect to the specificity of their involvement in a particular behaviour."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 9"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 9
        quote: "Performance on the semantic factor was uniquely related to a cluster of voxels centred on the white matter in the left anterior temporal lobe (ATL), extending to the temporal pole, planum polare, anterior and posterior MTG, and inferior temporal gyrus (ITG), and the anterior fusiform."
        supports: claim
      - section: "Materials and methods"
        page: 3
        quote: "Forty-three chronic stroke patients (either ischaemic or haemorrhagic) were recruited... All patients were at least 12 months post-stroke at the time of scanning and assessment"
        supports: sample
      - section: "Neuroimaging data analysis"
        page: 6
        quote: "Brain regions where tissue concentration... were related to behavioural measures were identified using voxel-based correlational methodology (VBCM) (Tyler et al. 2005)"
        supports: method
      - section: "Neuroimaging data analysis"
        page: 7
        quote: "All results are thresholded at p < 0.005 voxel level, p ≤ 0.05 family wise error (FWE)-corrected cluster level."
        supports: statistics
      - section: "Neuroimaging data analysis"
        page: 8
        quote: "For this reason, we did not control for lesion volume in our main analyses"
        supports: method
      - section: "Discussion"
        page: 15
        quote: "significant results within areas correlated with lesion volume must be interpreted with caution with respect to the specificity of their involvement in a particular behaviour."
        supports: limitation
---
