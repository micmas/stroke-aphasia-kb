---
schema_version: 2.8
id: right_inferior_frontal_gyrus
name: "Right Inferior Frontal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: right
findings:
  - id: f1
    target: form_to_meaning
    target_kind: impairment
    claim: "In the acute phase, patients with frontal stroke show facilitatory effective connectivity from the right IFG to the left IFG during sentence comprehension."
    direction: likely
    relationship: correlational
    citation: "@Jiang2025"
    method: fMRI_activation
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 17
      population: "patients with left-hemispheric frontal stroke"
      time_post_onset: "<=1 week"
      phase: acute
      language: "German"
    statistics:
      threshold: "posterior probability > 95%"
      effect_size: "0.501"
    confounders_controlled: []
    confounders_not_controlled: ["
      lesion heterogeneity"
    ]
    region_definition:
      kind: peak_coord_sphere
      mni_peak: [42, 35, -10]
      radius_mm: 20
      description: "Sphere around mean group coordinate for auditory speech processing contrast."
    imaging_details:
      field_strength: "3T"
      preprocessing_pipeline: "SPM12 (slice-timing correction, spatial realignment, coregistration, normalization, resampling and smoothing)"
      reference_space: MNI152
      atlases_used: []
      task:
        name: "Auditory sentence comprehension"
        description: "Participants listened to short German sentences and temporally reversed versions."
        contrasts: ["auditory speech > reversed speech"]
        baseline: "reversed speech"
    author_limitations:
      - "Small sample size (n=17 per group)."
      - "Findings may not generalize to speech production."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: ["
        cohort overlaps with @Stockert2022 (same participants)"
      ]
    source_passages:
      - section: "Results"
        page: 5
        quote: "In the acute phase of patients with frontal lesions (Fig. 2B), auditory speech processing significantly facilitated the effective connectivity from rIFG to lIFG (0.501)."
        supports: claim
      - section: "Materials and methods"
        page: 3
        quote: "Two groups of patients with either frontal (n = 17...)"
        supports: sample
      - section: "Materials and methods"
        page: 3
        quote: "We employed two slightly different versions of a passive auditory sentence comprehension paradigm during functional MRI (fMRI)."
        supports: method
      - section: "Statistical analysis"
        page: 5
        quote: "Significant patterns of effective connectivity... were obtained by thresholding the Bayesian Model Average to exclusively retain parameters with a posterior probability larger than 95%"
        supports: statistics
      - section: "Materials and methods"
        page: 3
        quote: "The right IFGorb (42 35 −10) was included as right hemisphere ROI"
        supports: region_definition
      - section: "Limitations"
        page: 11
        quote: "there were ultimately only 17 patients in each group."
        supports: limitation
      - section: "Limitations"
        page: 11
        quote: "our findings may not generalize to speech production."
        supports: limitation
---
