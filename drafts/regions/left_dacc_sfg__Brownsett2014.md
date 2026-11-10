---
schema_version: 2.8
id: left_dacc_sfg
name: "Left Dorsal Anterior Cingulate Cortex / Superior Frontal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: executive_functions
    target_kind: impairment
    claim: "Activation of the dorsal anterior cingulate cortex and adjacent superior frontal gyrus during a listening-and-prepare-to-repeat task predicts better performance on picture description in chronic aphasia."
    direction: likely
    relationship: correlational
    citation: "@Brownsett2014"
    method: fMRI_activation
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 16
      population: "chronic post-stroke aphasia"
      time_post_onset: "at least 6 months (mean 4 years, range 6 months to 11 years)"
      phase: chronic
      age_range: "mean 60 years; range 37-84 years"
      handedness: "all right-handed"
      language: "English"
    statistics:
      threshold: "Z >= 2.3, corrected P <= 0.05"
      effect_size: "r = 0.63"
      p_value: "0.01"
    confounders_controlled: ["lesion volume", "age"]
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "ROI defined by multiplying probabilistic anatomical masks from the FSL Harvard-Oxford Cortical Structural Atlas with functional activity observed in healthy participants during noise-vocoded speech perception."
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["Harvard-Oxford Cortical Structural Atlas"]
      preprocessing_pipeline: "FSL FEAT 5.98: MCFLIRT realignment, BET non-brain removal, 6mm FWHM Gaussian smoothing, grand-mean intensity normalization, high pass temporal filtering (sigma=50s), FLIRT registration with cost-function masking"
      task:
        name: "Listen-and-prepare-to-repeat"
        description: "Participants heard simple sentences, with each listening trial followed immediately by a trial in which they repeated back the previous sentence."
        contrasts: ["ListNorm vs ListWhite"]
        baseline: "segmented broadband noise bursts (white noise)"
    author_limitations:
      - "The study was not designed to determine why the dACC/SFG had such variable function across the group."
      - "Microscopic effects of disease predisposing to stroke and biological ageing are probable factors influencing dACC/SFG function."
      - "Conventional univariate statistical analyses may be too insensitive to reveal training-induced functional changes."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, pages 249-250"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 250
        quote: "The mean performance on the picture description test across the three sessions was then correlated with the mean dACC/SFG activation across three sessions. There was a significant positive correlation (r = 0.63, P = 0.01), with better picture description scores associated with greater dACC/SFG activation (Fig. 8)."
        supports: claim
      - section: "Materials and methods"
        page: 243
        quote: "All patients were at least 6 months post-stroke (mean 4 years, range 6 months to 11 years)... All patients had a lesion involving the left temporal and parietal lobes"
        supports: sample
      - section: "Materials and methods"
        page: 244
        quote: "Univariate whole-brain analyses were carried out within the framework of the general linear model using FEAT (FMRI Expert Analysis Tool) Version 5.98, part of FSL"
        supports: method
      - section: "Results"
        page: 250
        quote: "The results of the regression indicated that the model was statistically significant and accounted for 50% of the variance [R2 = 0.501, F(3,12) = 4.02, P = 0.03]. It was found that dACC/SFG activation predicted picture description score (beta = 0.56, P = 0.03), but age (beta = 0.16, P = 0.46) and lesion volume did not (beta = -0.28, P = 0.22)"
        supports: statistics
      - section: "Materials and methods"
        page: 245
        quote: "the theoretically motivated region of interest was defined by multiplying probabilistic anatomical masks from the FSL Harvard-Oxford Cortical Structural Atlas with functional activity observed in healthy participants."
        supports: region_definition
      - section: "Discussion"
        page: 252
        quote: "This study was not designed to determine why the dACC/SFG had such variable function across the group."
        supports: limitation
---
