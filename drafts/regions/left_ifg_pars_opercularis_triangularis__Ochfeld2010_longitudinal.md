---
schema_version: 2.8
id: left_ifg_pars_opercularis_triangularis
name: "Left Inferior Frontal Gyrus (Broca Area)"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left

findings:
  - id: f1
    target: brocas_aphasia
    target_kind: impairment
    claim: "In a longitudinal sample, ischemia involving Broca area was significantly associated with Broca or global aphasia acutely, but not chronically."
    direction: likely
    relationship: causal
    citation: "@Ochfeld2010"
    method: LSM
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 20
      population: "right-hand-dominant patients with left hemisphere ischemic stroke"
      time_post_onset: "<= 48 hours and >= 6 months"
      phase: longitudinal
      age_range: "39 to 80 years"
      handedness: "right-hand-dominant"
      language: "English"
    statistics:
      threshold: "P <= 0.0125"
      effect_size: "chi-square = 20 (acute) vs 0 (chronic) for part of Broca area"
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "probabilistic cytoarchitectural map"
      description: "Brodmann areas 44 and 45"
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["probabilistic cytoarchitectural map"]
      modalities:
        - modality: T2
        - modality: DWI
        - modality: PWI
    author_limitations:
      - "relatively small sample size of our study"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 326"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 326
        quote: "In the 20 patients studied longitudinally, the association between ischemia involving part of Broca area and Broca or global aphasia was significant only acutely (chi2=20; df1; P<=0.0001), not chronically (chi2=0; df1; p=1; not significant)."
        supports: claim
      - section: "Results"
        page: 326
        quote: "The subset of 20 patients studied at both time periods was similar to the entire group: age 39 to 80 (mean, 56.6; SD, 11.9)..."
        supports: sample
      - section: "Conclusion"
        page: 5
        quote: "Recognizing the limitations of WAB-R classification and the relatively small sample size of our study..."
        supports: limitation
---
