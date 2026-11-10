---
schema_version: 2.8
id: right_inferior_longitudinal_fasciculus
name: "Right Inferior Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: right
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Increase in the microstructural integrity (FA) of the right inferior longitudinal fasciculus is associated with improved naming accuracy in subacute post-stroke aphasia."
    direction: likely
    relationship: correlational
    citation: "@BlomSmink2020"
    method: tractography
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 10
      population: "aphasia after left-hemisphere stroke"
      time_post_onset: "within 3 months post onset"
      phase: early_subacute
      age_range: "mean 61.8 +/- 7.8 years"
      handedness: "right-handed"
      language: "Dutch"
    statistics:
      threshold: "P < .001 (Bonferroni-corrected)"
      effect_size: "r = 0.91"
    confounders_controlled: []
    confounders_not_controlled: ["lesion volume", "lesion site", "tDCS condition"]
    region_definition:
      kind: tract
      description: "Reconstructed using deterministic tractography based on ROI protocols of Wakana et al."
    imaging_details:
      field_strength: "3.0-T"
      reference_space: "native"
      atlases_used: []
      preprocessing_pipeline: "ExploreDTI: subject motion and eddy current correction"
      modalities:
        - modality: DTI
          sequence: "single-shot spin-echo echo-planar imaging"
          voxel_size_mm: [1.9, 1.9, 2.5]
          TR_ms: 7925
          TE_ms: 81.9
          n_directions: 32
          b_values: [0, 1000]
    author_limitations:
      - "Small sample size (n=10)."
      - "Predominantly male sample (7 men, 3 women), potentially introducing sex bias."
      - "Variability in timing of data collection across individuals."
      - "DTI provides only indirect measures of white matter tissue properties."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 788"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 788
        quote: "A strong positive correlation was found between FA change in the ILF and change in BNT score (r = 0.91, P < .001; Figure 5); an increase in FA was associated with a considerable improvement on the BNT"
        supports: claim
      - section: "Methods - Participants"
        page: 785
        quote: "Ten participants (7 men; mean age: 61.8 +/- 7.8 years) with aphasia due to first-ever left-hemisphere stroke completed the study."
        supports: sample
      - section: "Methods - Participants"
        page: 785
        quote: "All participants were within 3 months post onset at the time of the study"
        supports: sample
      - section: "Methods - Image Acquisition and Processing"
        page: 786
        quote: "Deterministic tractography was used to reconstruct the dorsal and ventral tracts for both hemispheres in native space."
        supports: method
      - section: "Statistical Analysis"
        page: 788
        quote: "probability values calculated for Pearson's correlations were corrected for multiple comparisons (10x)."
        supports: statistics
      - section: "Discussion"
        page: 792
        quote: "This study has several limitations. A first limitation is the small sample size."
        supports: limitation
---
