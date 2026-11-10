---
schema_version: 2.8
id: left_posterior_stg
name: "Left Posterior Superior Temporal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: fluency
    target_kind: impairment
    claim: "Damage to the left posterior superior temporal gyrus is associated with reduced length and structural complexity of narrative speech production."
    direction: likely
    relationship: causal
    citation: "@Zevgolatakou2022"
    method: MLPA
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 58
      population: "chronic left hemisphere stroke"
      time_post_onset: "at least 3 months post-onset"
      phase: chronic
      age_range: "51.3-68.0 (median 58.5)"
      handedness: "right-handed"
      language: "native English"
    statistics:
      threshold: "P < 0.001"
      effect_size: "CV correlation = 0.603"
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "AAL3"
      description: "Left superior temporal gyrus (posterior portion)"
    lesion_mapping:
      analysis: multivariate
      n_analysed: 58
      min_lesion_overlap: not_reported
      lesion_volume_correction: not_reported
      multiple_comparisons: not_reported
    imaging_details:
      reference_space: MNI152
      atlases_used: ["AAL3"]
      preprocessing_pipeline: "automated symmetric diffeomorphic registration algorithm to Colin27 template"
    author_limitations:
      - "Sample size was moderate relative to other LSM studies."
      - "Severity distribution skewed toward mild-to-moderate range due to narrative word count requirements."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 10"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 10
        quote: "Deficits in complexity of speech output were associated with a large temporo-parietal region (optimal sparseness = 0.576, CV correlation = 0.603, P < 0.001): SMG and postcentral gyrus, posterior superior temporal gyrus and middle temporal gyrus, and Heschl's gyrus"
        supports: claim
      - section: "Materials and methods"
        page: 5
        quote: "All but five participants were examined at the chronic stage of aphasia (at least 3 months post-onset)"
        supports: sample
      - section: "Materials and methods"
        page: 6
        quote: "LSM analyses were performed using SCCAN"
        supports: method
      - section: "Discussion"
        page: 13
        quote: "The participant sample was limited by the availability of narrative speech samples and lesion data. This resulted in a sample size (N = 58) that was moderate relative to other LSM studies"
        supports: limitation
---
