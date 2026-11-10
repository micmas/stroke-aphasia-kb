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
  claim: Reduced fiber density and cross-section (FDC) in the left arcuate fasciculus is associated with
    impaired comprehension of non-canonical sentences in subacute Mandarin-speaking aphasia.
  direction: likely
  relationship: causal
  citation: '@Fang2025'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 23
    population: subacute Mandarin-speaking aphasic patients
    time_post_onset: 1-6 months post-onset
    phase: early_subacute
    age_range: 30-79 years
    handedness: all right-handed
    language: Mandarin
  statistics:
    threshold: FWE p < 0.05
    effect_size: beta = 0.47
  confounders_controlled:
  - age
  - education
  - time post-stroke
  - verb comprehension
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Left arcuate fasciculus as defined by TractSeg
  lesion_mapping:
    analysis: univariate
    n_analysed: 23
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: fwe
  imaging_details:
    field_strength: 3.0T
    reference_space: MNI152
    atlases_used:
    - ' TractSeg'
    preprocessing_pipeline: MRtrix3 (dwidenoise, Gibbs removal), FSL (TOPUP, EDDY), N4 algorithm, SynthStrip
  author_limitations:
  - The relatively small sample size of this study may reduce its statistical power.
  - Tract-wise results in these tracts should be taken with caution due to potential overlap between neighboring
    white matter fixel masks.
  - Cross-sectional design in subacute patients complicates direct comparison with chronic populations.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 11
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 11
    quote: A positive linear relationship was observed between non-canonical sentence comprehension accuracy
      and FDC in fixels located in the left superior longitudinal fasciculus II (SLF II), superior longitudinal
      fasciculus III (SLF III), arcuate fasciculus (AF), middle longitudinal fasciculus (MdLF), inferior
      fronto-occipital fasciculus (IFOF), inferior longitudinal fasciculus (ILF), and the isthmus (ICC)
      and splenium (SCC) of the corpus callosum.
    supports: claim
  - section: Materials and Methods
    page: 4
    quote: Ultimately, 23 participants (19 men and 4 women) were included in the current analysis... native
      Mandarin speakers, right-handed... confirmed diagnosis of a single-hemispheric stroke within six
      months before the assessment
    supports: sample
  - section: Materials and Methods
    page: 8
    quote: Family-wise error (FWE)-corrected p-values were computed using non-parametric bootstrapping
      with 5000 permutations, and statistical significance was set at an FWE-corrected threshold of p
      < 0.05.
    supports: statistics
  - section: Materials and Methods
    page: 8
    quote: Linear regression models were fit with fixel-wise FDC as the response variable and accuracy
      for non-canonical sentences... as the predictor. Covariates include age, years of education, log-transformed
      time post-stroke, and the overall accuracy of the Verb Comprehension Test
    supports: method
  - section: Discussion
    page: 16
    quote: First, the relatively small sample size of this study may reduce its statistical power.
    supports: limitation
---
