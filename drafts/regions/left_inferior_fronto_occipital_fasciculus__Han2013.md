---
schema_version: 2.8
id: left_inferior_fronto_occipital_fasciculus
name: "Left Inferior Fronto-Occipital Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: semantics
    target_kind: impairment
    claim: "Damage to the left inferior fronto-occipital fasciculus is associated with semantic processing deficits across multiple input and output modalities."
    direction: likely
    relationship: causal
    citation: "@Han2013"
    method: [LSM, DTI]
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 76
      population: "right-handed brain-damaged patients"
      time_post_onset: "at least 1 month post-onset"
      phase: early_subacute
      age_range: "mean 47 (SD 13; range 20-76 years)"
      handedness: "all right-handed"
      language: "native Chinese speakers"
    statistics:
      threshold: "Bonferroni corrected (P = 0.00294 for lesion analysis, P = 0.0025 for FA analysis; corrected P = 0.05)"
      effect_size: "lesion correlation r = -0.56 (composite); FA correlation r = 0.63 (composite)"
    lesion_mapping:
      analysis: univariate
      n_analysed: 76
      min_lesion_overlap: ">= 5 patients"
      lesion_volume_correction: covariate
      multiple_comparisons: bonferroni
    confounders_controlled: ["overall cognitive state (MMSE)", "whole lesion volume", "type of brain damage", "grey matter lesions", "non-semantic control tasks"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "JHU white-matter tractography atlas (25%-threshold sub-template)"
      description: "Left inferior fronto-occipital fasciculus as defined by the JHU-WM-Tracts atlas."
    imaging_details:
      field_strength: "1.5T"
      reference_space: "MNI152"
      atlases_used: ["JHU white-matter tractography atlas"]
      preprocessing_pipeline: "SPM5 co-registration, manual lesion tracing, BrainVoyager QX v2.0 registration to Talairach, then transformed to MNI; DTI via PANDA pipeline (BET, Eddycorrect, DTIFIT) and ANTs registration to FMRIB FA template"
    author_limitations:
      - "Results are constrained by the lesion distribution in the patient group, with a bias toward the middle cerebral artery territory."
      - "Individual tracts may not have specific functions; the overall pattern of multiple tracts might be what matters for semantic processing."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, pages 8-10"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 8
        quote: "the lesion percentages of the following three tracts significantly correlated negatively with all three semantic tasks: left IFOF, left ATR, left uncinate fasciculus (corrected P-values = 0.05)."
        supports: claim
      - section: "Materials and methods"
        page: 2
        quote: "Eighty-three patients with brain damage... at least 1 month post-onset... right-handed... Seven patients were not included in the analyses... remaining 76 patients"
        supports: sample
      - section: "Materials and methods"
        page: 5
        quote: "we adopted a widely used human brain white-matter template, the 'JHU white-matter tractography atlas' from FSL... We chose to use the 25%-threshold sub-template"
        supports: region_definition
      - section: "Materials and methods"
        page: 5
        quote: "The results were adjusted for the 17 tracts with the Bonferroni correction method (P = 0.00294, corrected P = 0.05)."
        supports: statistics
      - section: "Discussion"
        page: 12
        quote: "our analyses here were constrained by the lesion distribution in the patient groups... our patients tended to have lesions in the territory of the middle cerebral artery"
        supports: limitation
---
