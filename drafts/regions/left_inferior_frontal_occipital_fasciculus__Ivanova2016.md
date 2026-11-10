---
schema_version: 2.8
id: left_inferior_frontal_occipital_fasciculus
name: "Left Inferior Frontal-Occipital Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: form_to_meaning
    target_kind: impairment
    claim: "Integrity of the left inferior frontal-occipital fasciculus is associated with language comprehension in chronic aphasia."
    direction: likely
    relationship: correlational
    citation: "@Ivanova2016"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 37
      population: "individuals with aphasia due to left hemisphere stroke"
      time_post_onset: "M = 26.38, SD = 21.40 months post-onset"
      phase: chronic
      age_range: "34-78 years"
      handedness: "all right-handed"
      language: "native speakers of Russian"
    statistics:
      threshold: "p < .01"
      effect_size: "r = .504 (p = .002) for single word comprehension"
    confounders_controlled: ["age", "time post-onset", "lesion size"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "John Hopkins University White Matter Tractography atlas"
      description: "Tract masks thresholded with probability value of .25 in MNI space"
    imaging_details:
      field_strength: "1.5T"
      acquisition:
        voxel_size_mm: [2.7, 2.7, 2.7]
        TR_ms: 6000
        TE_ms: 95
        sequence: "spin echo, single shot EPI"
      preprocessing_pipeline: "FSL eddy_correct, BET, DTIFIT; cost function masking for co-registration"
      reference_space: MNI152
      atlases_used: ["John Hopkins University White Matter Tractography atlas"]
    author_limitations:
      - "The extent to which language deficits are directly a result of white or grey matter involvement cannot be definitively determined as only lesion size (but not location) was used as a covariate."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 10"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 2
        quote: "Language comprehension was predominantly related to integrity of the left IFOF and left ILF"
        supports: claim
      - section: "Materials and methods"
        page: 5
        quote: "Thirty-seven individuals (18 males, 19 females; Mage = 54 years, SD = 10.53, age range: 34-78 years) with various types of aphasia were recruited"
        supports: sample
      - section: "Materials and methods"
        page: 7
        quote: "partial correlations were used... factoring out effects of age, time post-onset and lesion size."
        supports: confounders
      - section: "Discussion"
        page: 12
        quote: "the extent to which language deficits are directly a result of white or grey matter involvement cannot be definitively determined here, as only lesion size (but not location) was used as a covariate in the correlational analyses."
        supports: limitation
---
