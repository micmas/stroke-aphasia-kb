---
schema_version: 2.8
id: right_posterior_perisylvian_cortex
name: "Right Posterior Perisylvian Cortex"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: right

findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "In patients with more fluent aphasias, greater treatment gains in category member generation are associated with a rightward shift in posterior perisylvian activity."
    direction: likely
    relationship: correlational
    citation: "@Benjamin2014"
    method: fMRI_activation
    design: RCT
    strength: weak
    evidence_quality: cohort
    therapy:
      id: intention_treatment
      name: "Intention treatment"
      dose: "3 phases, 10 sessions per week per phase"
    sample:
      n: 7
      population: "chronic left-hemisphere stroke aphasia (predominantly conduction aphasia)"
      time_post_onset: ">6 months"
      phase: chronic
      age_range: "mean 72.1 (SD 10.5)"
      handedness: "premorbidly right-handed"
      language: "English"
    statistics:
      threshold: "P < .01"
      effect_size: "r = -0.86"
    confounders_controlled: ["
      design-matched control treatment (CT)"
    ]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford"
      description: "Posterior perisylvian ROI constructed from Harvard-Oxford atlas."
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: fMRI
          sequence: "gradient echo-echo planar"
          voxel_size_mm: [null, null, 4]
          TR_ms: 1700
          TE_ms: 30
          volumes: 60
      preprocessing_pipeline: "T1 masks warped into MNI-152 atlas space using nonlinear FNIRT algorithm from FSL"
      reference_space: MNI152
      atlases_used: ["Harvard-Oxford"]
    author_limitations:
      - "Small sample size; correlation may be influenced by a few subjects."
      - "The role of this region may vary by aphasia type and lesion location."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 550"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 550
        quote: "rightward shifts in posterior persylvian activity showed a significant correlation with treatment gains for IT (r = -0.86, n = 7, P < .01)"
        supports: claim
      - section: "Discussion"
        page: 552
        quote: "greater treatment improvement in patients with more fluent aphasias was associated with a rightward shift in posterior perisylvian laterality."
        supports: claim
      - section: "Discussion"
        page: 552
        quote: "the removal of one subject at either end of the regression line for the CT group could alter the regression line, leaving some doubt that this correlation is real."
        supports: limitation
      - section: "Discussion"
        page: 552
        quote: "Hence, type of aphasia and lesion location may affect roles of left and right posterior perisylvian cortex in the Intention treatment."
        supports: limitation
---
