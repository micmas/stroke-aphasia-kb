---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: syntactic_processing
  target_kind: impairment
  claim: Disconnection of the left arcuate fasciculus is associated with impaired comprehension of sentences
    containing object extraction.
  direction: likely
  relationship: causal
  citation: '@Biondo2024'
  method: disconnectome
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 131
    population: left hemisphere stroke survivors
    time_post_onset: at least 6 months
    phase: chronic
    age_range: 31-86 years
    handedness: all right handed
    language: native-like proficiency in English
  statistics:
    threshold: Bonferroni corrected... alpha = 0.0038
    effect_size: not_reported
  lesion_mapping:
    analysis: network
    n_analysed: 131
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: bonferroni
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: indirect structural disconnection mapping using HCP-842 atlas
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - HCP-842 atlas
    preprocessing_pipeline: Lesion Quantification Toolkit
  author_limitations:
  - our disconnection analyses relied on indirect measures of structural disconnection, as diffusion tensor
    imaging data were only available for a subset of participants.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 10
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 10
    quote: the disconnection of both the SLF and the AF affected the comprehension of sentences containing
      object extraction.
    supports: claim
  - section: Materials and methods
    page: 5
    quote: Participants included 131 individuals... who sustained a single left hemisphere stroke at least
      6 months before being tested and scanned.
    supports: sample
  - section: Statistical analysis
    page: 7
    quote: To evaluate the impact of tract-level disconnection severity on auditory sentence comprehension,
      we performed Pearson correlations analyses, Bonferroni corrected for the number of tracts (alpha
      = 0.0038).
    supports: statistics
  - section: Limitations and future directions
    page: 13
    quote: Another limitation is that our disconnection analyses relied on indirect measures of structural
      disconnection, as diffusion tensor imaging data were only available for a subset of participants.
    supports: limitation
---
