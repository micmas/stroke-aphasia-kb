---
schema_version: 2.8
id: right_lateral_frontal_cortex
name: "Right Lateral Frontal Cortex"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: right

findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Intention treatment, involving left-hand movements, induces a rightward shift in lateral frontal activity during word production that persists for 3 months."
    direction: likely
    relationship: treatment_response
    citation: "@Benjamin2014"
    method: fMRI_activation
    design: RCT
    strength: moderate
    evidence_quality: cohort
    therapy:
      id: intention_treatment
      name: "Intention treatment"
      dose: "3 phases, 10 sessions per week per phase"
    sample:
      n: 7
      population: "chronic left-hemisphere stroke aphasia"
      time_post_onset: ">6 months"
      phase: chronic
      age_range: "mean 72.1 (SD 10.5)"
      handedness: "premorbidly right-handed"
      language: "English"
    statistics:
      threshold: "P < .05"
      effect_size: "t = -2.602 (posttreatment), t = -2.332 (3-month follow-up)"
    confounders_controlled: ["
design-matched control treatment (CT)"
    ]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford"
      description: "Lateral frontal ROI constructed from Harvard-Oxford atlas, excluding the anterior most portion of frontal polar cortex."
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: fMRI
          sequence: "gradient echo-echo planar"
          voxel_size_mm: [null, null, 4]
          TR_ms: 1700
          TE_ms: 30
          volumes: 60
        - modality: T1
          sequence: "turbo field echo"
          voxel_size_mm: [null, null, 1.0]
          TR_ms: 8.1
          TE_ms: 3.7
      preprocessing_pipeline: "T1 masks warped into MNI-152 atlas space using nonlinear FNIRT algorithm from FSL"
      reference_space: MNI152
      atlases_used: ["Harvard-Oxford"]
    author_limitations:
      - "Small sample size may limit generalizability."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 548"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 548
        quote: "One-tailed t tests indicated that IT patients demonstrated a significant rightward shift in lateral frontal activity from pretreatment to both posttreatment (t = -2.602, df = 6, P < .05) and 3-month follow-up (t = -2.332, df = 5, P < .05)."
        supports: claim
      - section: "Method"
        page: 547
        quote: "Fourteen chronic (>6 months) aphasia patients participated."
        supports: sample
      - section: "Method"
        page: 548
        quote: "Three regions of interest (ROIs; medial frontal, lateral frontal, and posterior perisylvian) were constructed for each hemisphere by combining regions from the Harvard-Oxford atlas distributed with FSL"
        supports: region_definition
      - section: "Method"
        page: 548
        quote: "the whole brain was imaged in 1.70 seconds using a gradient echo-echo planar sequence... (repetition time [TR] = 1700 ms; echo time [TE] = 30 ms)"
        supports: imaging_details
      - section: "Discussion"
        page: 551
        quote: "engagement of right relative to left lateral frontal cortex during word generation increased immediately posttreatment. This laterality shift persisted for 3 months posttreatment."
        supports: claim
      - section: "Discussion"
        page: 552
        quote: "Because of the small number of subjects in the groups..."
        supports: limitation
---
