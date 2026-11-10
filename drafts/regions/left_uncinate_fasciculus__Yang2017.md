---
schema_version: 2.8
id: left_uncinate_fasciculus
name: "Left Uncinate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-11
hemisphere: left
findings:
  - id: f1
    target: aphasia
    target_kind: impairment
    claim: "Patients with acute aphasia show decreased white matter integrity (FA) in the left uncinate fasciculus compared to healthy controls."
    direction: likely
    relationship: correlational
    citation: "@Yang2017"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 18
      population: "acute aphasia after stroke"
      time_post_onset: "average of 9.7 ± 5.3 days"
      phase: acute
      age_range: "53.67 ± 13.66 years"
      handedness: "all right-handed"
      language: "Chinese native speaker"
    statistics:
      threshold: "P < 0.01, corrected for multiple comparisons"
      effect_size: "T = -5.07"
      p_value: "not_reported"
    confounders_controlled: ["age", "gender", "education"]
    confounders_not_controlled: ["lesion volume"]
    region_definition:
      kind: atlas
      atlas: "JHU DTI-based white-matter atlases"
      description: "Left uncinate fasciculus (UF)"
    imaging_details:
      field_strength: "3.0T"
      acquisition:
        voxel_size_mm: [1, 1, 1]
        TR_ms: 8500
        TE_ms: 93
        sequence: "DTI"
      preprocessing_pipeline: "FSL v5.0, TBSS, non-linear alignment to FMRIB58 FA template"
      reference_space: MNI152
      atlases_used: ["JHU DTI-based white-matter atlases"]
    author_limitations:
      - "The sample size was relatively small for studies involving abnormal WM integrity in aphasia."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 4
        quote: "patients showed decreased FA in the [...] left uncinate fasciculus"
        supports: claim
      - section: "Materials and Methods"
        page: 2
        quote: "Eighteen aphasia patients (all right-handed, six females; age, 53.67 ± 13.66 years) were recruited"
        supports: sample
      - section: "Statistical Analysis"
        page: 4
        quote: "Clusters with a voxel-wise threshold of P < 0.01 as well as voxels[50 were considered statistically significant."
        supports: statistics
      - section: "Discussion"
        page: 6
        quote: "First, the sample size was relatively small for studies involving abnormal WM integrity in aphasia."
        supports: limitation
---
