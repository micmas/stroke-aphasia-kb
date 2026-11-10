---
schema_version: 2.8
id: left_ifg_pars_opercularis
name: Left IFG Pars Opercularis (Broca's area, dorsal stream hub)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Preservation of either direct or indirect white matter connections between the left IFG pars
    opercularis and the angular gyrus is associated with greater naming improvement following treatment
    in chronic aphasia.
  direction: likely
  relationship: responder
  citation: '@Wilmskoetter2021'
  method: tractography
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 69
    population: chronic left-hemisphere ischemic stroke and aphasia
    time_post_onset: 6 to 202 months
    phase: chronic
    age_range: mean 59.54 (SD 10.26)
    handedness: not_reported
    language: not_reported
    cohort: NCT01927302
  statistics:
    threshold: P < .05
    effect_size: P = .027 (direct), P = .039 (indirect)
    p_value: '.027'
  confounders_controlled:
  - age
  - education
  - baseline WAB-AQ
  - treatment type (A-tDCS vs S-tDCS)
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU anatomical atlas
    description: inferior frontal gyrus opercularis (IFGop)
  therapy:
    id: computerized_lexical_semantic_treatment
    name: computerized language treatment focusing on lexical-semantic processing
    dose: 3-week-long
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - JHU anatomical atlas
    preprocessing_pipeline: SPM12 normalization
  author_limitations:
  - Indirect pathways were mapped based on structural connectomics; functional use of these pathways is
    not confirmed.
  - Binarization of lesion maps may fail to identify existing relationships.
  - Findings may not generalize to other aspects of language beyond naming.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 350
    confidence: high
    flags:
    - cohort overlaps with @Fridriksson2018JAMA (same NCT01927302 trial)
  source_passages:
  - section: Results
    page: 350
    quote: Post hoc tests showed a significant difference in naming improvement between direct and no
      connections (P = .027) and between indirect and no connections (P = .039).
    supports: claim
  - section: Materials and Methods
    page: 348
    quote: We included 69 of 74 participants from the clinical trial... all participants received a 3-week-long
      computerized language treatment focusing on lexical-semantic processing
    supports: sample
  - section: Materials and Methods
    page: 349
    quote: We performed whole-brain probabilistic tractography but spared the lesion for tractography.
    supports: method
  - section: Materials and Methods
    page: 350
    quote: Treated naming recovery... while controlling for age, number of years of formal education,
      baseline WAB-AQ, treatment type (A-tDCS vs S-tDCS).
    supports: confounders
  - section: Discussion
    page: 354
    quote: We mapped indirect connections based on structural connectomics; thus, we cannot claim that
      these indirect pathways are indeed functionally used.
    supports: limitation
---

Notes: This finding relates to the predictive value of structural connectivity (direct and indirect) for treatment response in anomia.
