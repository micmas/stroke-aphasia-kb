---
schema_version: 2.8
id: left_ifg_pars_opercularis
name: Left IFG Pars Opercularis (Broca's area, dorsal stream hub)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: phonological_production
  target_kind: impairment
  claim: Tissue concentration in the left inferior frontal gyrus pars opercularis is uniquely related
    to phonological processing in chronic stroke aphasia.
  direction: likely
  relationship: causal
  citation: '@Woollams2018'
  method: VBCM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 43
    population: chronic stroke aphasic patients
    time_post_onset: at least 12 months post-stroke
    phase: chronic
    language: native English speakers
  statistics:
    threshold: p < 0.005 voxel level, p ≤ 0.05 family wise error (FWE)-corrected cluster level
    effect_size: T = 5.98
  lesion_mapping:
    analysis: univariate
    n_analysed: 43
    min_lesion_overlap: not_reported
    lesion_volume_correction: none
    multiple_comparisons: fwe
  confounders_controlled: []
  confounders_not_controlled:
  - lesion volume
  region_definition:
    kind: data_driven_cluster
    description: Large cluster including IFG (triangularis and orbitalis), frontal and central opercular
      cortex, and other perisylvian regions.
  imaging_details:
    field_strength: 3.0 T
    acquisition:
      sequence: T1-weighted inversion recovery
      voxel_size_mm:
      - 1.0
      - 1.0
      - 1.0
    preprocessing_pipeline: SPM8 modified unified segmentation–normalisation procedure
    reference_space: MNI152
    atlases_used:
    - Harvard–Oxford cortical
    - NatBrain-Lab white-matter
  author_limitations:
  - Significant results within areas correlated with lesion volume must be interpreted with caution with
    respect to the specificity of their involvement in a particular behaviour.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 9
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 9
    quote: 'Performance on the phonological factor was uniquely correlated with a large cluster of a number
      of left hemisphere regions: ... inferior frontal gyrus (IFG) (triangularis and orbitalis), frontal
      and central opercular cortex...'
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Forty-three chronic stroke patients (either ischaemic or haemorrhagic) were recruited... All
      patients were at least 12 months post-stroke at the time of scanning and assessment
    supports: sample
  - section: Neuroimaging data analysis
    page: 6
    quote: Brain regions where tissue concentration... were related to behavioural measures were identified
      using voxel-based correlational methodology (VBCM) (Tyler et al. 2005)
    supports: method
  - section: Neuroimaging data analysis
    page: 7
    quote: All results are thresholded at p < 0.005 voxel level, p ≤ 0.05 family wise error (FWE)-corrected
      cluster level.
    supports: statistics
  - section: Neuroimaging data analysis
    page: 8
    quote: For this reason, we did not control for lesion volume in our main analyses
    supports: method
  - section: Discussion
    page: 15
    quote: significant results within areas correlated with lesion volume must be interpreted with caution
      with respect to the specificity of their involvement in a particular behaviour.
    supports: limitation
---
