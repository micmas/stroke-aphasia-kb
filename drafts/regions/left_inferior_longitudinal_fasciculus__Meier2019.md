---
schema_version: 2.8
id: left_inferior_longitudinal_fasciculus
name: "Left Inferior Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Integrity of the left inferior longitudinal fasciculus (ILF), as reflected by fractional anisotropy, is associated with naming skills independently of lesion volume."
    direction: likely
    relationship: correlational
    citation: "@Meier2019"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 34
      population: "chronic left hemisphere stroke"
      time_post_onset: ">=six months post-onset"
      phase: chronic
      age_range: "mean 61.91 +/- 10.84 years"
      handedness: "mixed"
      language: "English"
    statistics:
      threshold: "FDR corrected"
      effect_size: "partial r = 0.507"
      p_value: "0.025"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      atlas: "Johns Hopkins University White Matter Tractography atlas"
      description: "left inferior longitudinal fasciculus (ILF)"
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["Johns Hopkins University White Matter Tractography atlas"]
      preprocessing_pipeline: "enantiomorphic warping of intact RH into damaged LH, normalized to mni_icbm152_T1_2009 template"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 9"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 9
        quote: "When controlling for lesion volume, relationships between BNTtotal and FAmean in the left IFOF (partial r = 0.441, p = 0.046) and FAmean in the left ILF (partial r = 0.507, p = 0.025) remained significant"
        supports: claim
      - section: "Materials and methods"
        page: 3
        quote: "we extracted tract masks from the Johns Hopkins University White Matter Tractography atlas (Wakana et al. 2004) that corresponded to the bilateral arcuate (AF), inferior fronto-occipital (IFOF), inferior longitudinal (ILF) and uncinate (UF) fasciculi"
        supports: region_definition
    author_limitations:
      - "The variance in naming and treatment outcomes explained by the lesion classification systems was low."
    source_passages_limitation:
      - section: "Discussion"
        page: 13
        quote: "the variance in naming and treatment outcomes explained by the lesion classification systems was low"
        supports: limitation
  - id: f2
    target: anomia
    target_kind: therapy
    claim: "Integrity of the left inferior longitudinal fasciculus (ILF), as reflected by fractional anisotropy, predicts success in naming treatment independently of lesion volume."
    direction: likely
    relationship: responder
    citation: "@Meier2019"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 34
      population: "chronic left hemisphere stroke"
      time_post_onset: ">=six months post-onset"
      phase: chronic
      age_range: "mean 61.91 +/- 10.84 years"
      handedness: "mixed"
      language: "English"
    statistics:
      threshold: "FDR corrected"
      effect_size: "partial r = 0.658"
      p_value: "< 0.001"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      atlas: "Johns Hopkins University White Matter Tractography atlas"
      description: "left inferior longitudinal fasciculus (ILF)"
    therapy:
      id: semantic_feature_analysis
      name: "modified semantic feature analysis-based treatment for anomia"
      dose: "four hours per week for up to 12 weeks"
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["Johns Hopkins University White Matter Tractography atlas"]
      preprocessing_pipeline: "enantiomorphic warping of intact RH into damaged LH, normalized to mni_icbm152_T1_2009 template"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 9"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 9
        quote: "Similarly, partial correlations with lesion volume revealed remaining significant associations between PMG and FAmean in the left IFOF (partial r = 0.560, p = 0.006) and FAmean in the left ILF (partial r = 0.658, p < 0.001)"
        supports: claim
      - section: "Treatment protocol"
        page: 3
        quote: "Ultimately, 30 participants received modified semantic feature analysis-based treatment for anomia (Boyle 2010; Kiran and Thompson 2003) for four hours per week for up to 12 weeks"
        supports: method
    author_limitations:
      - "The variance in naming and treatment outcomes explained by the lesion classification systems was low."
    source_passages_limitation:
      - section: "Discussion"
        page: 13
        quote: "the variance in naming and treatment outcomes explained by the lesion classification systems was low"
        supports: limitation
---
