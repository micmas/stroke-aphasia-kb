---
schema_version: 2.8
id: left_angular_gyrus
name: "Left Angular Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Fewer propagation steps along indirect white matter connections between the angular gyrus and the middle temporal gyrus significantly predict greater naming improvement after treatment in chronic aphasia."
    direction: likely
    relationship: responder
    citation: "@Wilmskoetter2021"
    method: tractography
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 69
      population: "chronic left-hemisphere ischemic stroke and aphasia"
      time_post_onset: "6 to 202 months"
      phase: chronic
      age_range: "mean 59.54 (SD 10.26)"
      handedness: not_reported
      language: not_reported
      cohort: "NCT01927302"
    statistics:
      threshold: "P < .05"
      effect_size: "standardized beta = -0.517"
      p_value: ".012"
    confounders_controlled: ["age", "education", "baseline WAB-AQ", "treatment type (A-tDCS vs S-tDCS)"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "JHU anatomical atlas"
      description: "angular gyrus (AG)"
    therapy:
      id: computerized_lexical_semantic_treatment
      name: "computerized language treatment focusing on lexical-semantic processing"
      dose: "3-week-long"
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["JHU anatomical atlas"]
      preprocessing_pipeline: "SPM12 normalization"
    author_limitations:
      - "Indirect pathways were mapped based on structural connectomics; functional use is not confirmed."
      - "Binarization of lesion maps may fail to identify existing relationships."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 351"
      confidence: high
      flags: ["cohort overlaps with @Fridriksson2018JAMA (same NCT01927302 trial)"]
    source_passages:
      - section: "Results"
        page: 351
        quote: "fewer steps along the indirect connection between the AG and MTG significantly predicted an increase in correct naming responses after treatment (standardized beta = -0.517, P = .012)."
        supports: claim
      - section: "Materials and Methods"
        page: 349
        quote: "We calculated indirect pairwise connections by computing the shortest path length (ie, the minimal number of steps) between each pair of gray matter regions."
        supports: method
      - section: "Discussion"
        page: 353
        quote: "Fewer steps along indirect connections between the AG and MTG was predictive of more correct responses at follow-up compared to baseline."
        supports: claim
---

Notes: This finding suggests that the efficiency (shorter path length) of indirect connections between the AG and MTG is a predictor of naming recovery.
