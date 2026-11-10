---
schema_version: 2.8
id: right_superior_temporal_sulcus
name: "Right Superior Temporal Sulcus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: right
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Increased activation of the right superior temporal sulcus during overt naming is associated with better naming performance, independent of lesion size and damage to critical left hemisphere naming areas."
    direction: likely
    relationship: correlational
    citation: "@SkipperKallal2017Functional"
    method: fMRI_activation
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 32
      population: "chronic left-hemisphere stroke survivors with aphasia"
      time_post_onset: "at least 6 months"
      phase: chronic
      age_range: "mean 58.78 (8.61)"
      handedness: "26 right, 3 left, 2 ambidextrous"
      language: "native English speakers"
    statistics:
      threshold: "z = 3.5 for ROI selection; cluster-corrected P < 0.05"
      effect_size: "t(23) = 2.80"
      p_value: "0.01"
    confounders_controlled: ["lesion size", "PCAD (proportion of critical area damaged)", "age", "sex", "education", "handedness", "time since stroke"]
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "ROI identified from aphasia > control contrast during overt naming, threshold z = 3.5, size > 500 mm3"
    imaging_details:
      field_strength: "3.0 T"
      acquisition:
        voxel_size_mm: [3.2, 3.2, 3.2]
        TR_ms: 2000
        TE_ms: 30
        sequence: "gradient-echo echo-planar pulse sequence"
      preprocessing_pipeline: "FSL 5.0.6; high pass temporal filter, MCFLIRT motion correction, slice timing correction, intensity normalization, 5mm FWHM smoothing, normalization to older adult MNI template"
      reference_space: MNI152
      atlases_used: []
      coordinates_reported: [{region: "right STS", mni: [46, 239, 23]}]
    task:
      name: "Overt Naming"
      description: "Participants produced the name of a line drawing aloud after a covert retrieval phase."
      contrasts: ["overt naming > fixation"]
      baseline: "fixation"
    author_limitations:
      - "The study is cross-sectional, limiting causal inferences about reorganization."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 9"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 9
        quote: "In the regression analyses, only the positive relationship between right STS activity and PNT remained significant (t(23) = 2.80, P = 0.01)."
        supports: claim
      - section: "Materials and Methods"
        page: 3
        quote: "Forty-six chronic left-hemisphere stroke survivors with a history of aphasia were recruited. [...] resulting in a final sample of 32 participants in the aphasia group"
        supports: sample
      - section: "Materials and Methods"
        page: 5
        quote: "Mean contrast parameter estimates were extracted from each ROI [...] we then tested whether activation of each ROI during a naming task could predict naming performance as measured by the 60-item PNT"
        supports: method
      - section: "Materials and Methods"
        page: 4
        quote: "MRI data were collected on a 3.0 T Siemens Trio Scanner"
        supports: imaging_details
      - section: "Discussion"
        page: 12
        quote: "The experiment described here is a cross-sectional study of naming in chronic aphasia"
        supports: limitation
---
