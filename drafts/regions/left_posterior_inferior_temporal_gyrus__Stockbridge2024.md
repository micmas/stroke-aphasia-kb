---
schema_version: 2.8
id: left_posterior_inferior_temporal_gyrus
name: "Left Posterior Inferior Temporal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Microstructural integrity of the left posterior inferior temporal gyrus is positively associated with picture naming accuracy in subacute aphasia."
    direction: likely
    relationship: correlational
    citation: "@Stockbridge2024"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 22
      population: "subacute post-stroke aphasia"
      time_post_onset: "within three months"
      phase: early_subacute
      age_range: "mean 69 (SD 13)"
      handedness: "right-handed"
      language: "English"
    statistics:
      threshold: "p < 0.05"
      effect_size: not_reported
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Brainnectome (merged regions ITG 7_2, 7_5)"
      description: "Left posterior inferior temporal gyrus (pITG) defined via Brainnectome map and DSI studio atlas-based segmentation."
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["Brainnectome"]
      preprocessing_pipeline: "DSI studio with FSL eddy tool for motion/eddy current correction; resampled to 1mm isotropic"
      modalities:
        - modality: DTI
          sequence: "32 direction DWI"
          voxel_size_mm: [0.82, 0.82, 2.2]
          TR_ms: 7013
          TE_ms: 71
          b_values: [700]
    author_limitations:
      - "Small sample size with heterogeneous aphasia subtypes."
      - "Atlas-based segmentation performed in native diffusion space rather than coregistering with T1w or T2w maps."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 4
        quote: "Picture naming performance demonstrated a significant but weak correlation with lower mean diffusivity (higher microstructural integrity) in the left pITG."
        supports: claim
      - section: "Methods"
        page: 2
        quote: "Included individuals were right-handed, adult English speakers within three months of ischemic left hemisphere stroke who were diagnosed with aphasia using the Western Aphasia Battery-Revised (WAB-R; Kertesz 2007)."
        supports: sample
      - section: "Methods"
        page: 3
        quote: "The MRI protocol included... Diffusion-weighted imaging (DWI), and data were acquired on a Philips 3T scanner... 32 direction DWI data were acquired axially with no gaps. TR/TE:7013/71... the b-value = 700s mm2, slice thickness = 2.2 mm/in-plane resolution = 0.82 mm."
        supports: imaging_details
      - section: "Methods"
        page: 3
        quote: "we used embedded maps Brainnectome... to generate regions... pITG (merged regions ITG 7_2, 7_5; Brainnectome map)"
        supports: region_definition
      - section: "Limitations"
        page: 9
        quote: "One of the main limitations is small sample size with heterogeneous aphasia subtypes."
        supports: limitation
---
