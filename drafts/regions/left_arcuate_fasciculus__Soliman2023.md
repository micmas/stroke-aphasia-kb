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
  target: form_to_meaning
  target_kind: impairment
  claim: Reduced fractional anisotropy of the left arcuate fasciculus is significantly correlated with
    comprehension impairment in subacute stroke.
  direction: likely
  relationship: correlational
  citation: '@Soliman2023'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 16
    population: subacute left hemispheric stroke aphasia
    time_post_onset: 'mean 3.07 +/- 0.91 weeks (range: 2-4 weeks)'
    phase: early_subacute
    age_range: 'mean 53 +/- 11.7 years (range: 33-68 years)'
    handedness: right handed
    language: native Arabic
  statistics:
    threshold: P-value < 0.0125 (Bonferroni corrected)
    effect_size: r = -0.756
    p_value: '.009'
  confounders_controlled:
  - age
  - lesion volume
  - risk factors
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Dissection of the arcuate fasciculus using a two-ROI approach based on CSD tractography.
  imaging_details:
    field_strength: 1.5T
    reference_space: MNI152
    atlases_used: []
    preprocessing_pipeline: Explore DTI toolbox; Gibbs ringing, motion, and eddy current correction; non-rigid
      registration to T1
    modalities:
    - modality: T1
      sequence: 3D T1-weighted
      voxel_size_mm:
      - 1
      - 1
      - 1
      TR_ms: 7.6
      TE_ms: 3.5
    - modality: DTI
      sequence: EPI
      voxel_size_mm:
      - 2
      - 2
      - 2
      TR_ms: 11700
      TE_ms: 110
      b_values:
      - 0
      - 1000
      n_directions: 32
  author_limitations:
  - Small sample size.
  - Did not dissect different AF segments, relied on the whole AF tract.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 3
    quote: In the left hemisphere, as shown in Table 4, there were strong significant correlations between
      FA of the AF and comprehension (r = -0.756, p = .009).
    supports: claim
  - section: Material and methods
    page: 2
    quote: a total of 17 aphasic patients were enrolled in this study... within the first month post-stroke
    supports: sample
  - section: Material and methods
    page: 2
    quote: CSD based whole brain deterministic tractography was performed... Dissection of dorsal stream
      (AF)... achieved bilaterally, using a two-ROI approach
    supports: method
  - section: Statistical analysis
    page: 3
    quote: Significant threshold was set to (P- value <0.0125) after Bonferroni correction for multiple
      comparisons.
    supports: statistics
  - section: Statistical analysis
    page: 3
    quote: Partial correlations were performed... with elimination the effect of the age, lesion volume
      and the risk factors.
    supports: confounders
  - section: Limitations
    page: 6
    quote: The small sample size is a main limitation of this study... Additionally, we did not dissect
      the different AF segments but rather relied on the whole AF tract.
    supports: limitation
---
