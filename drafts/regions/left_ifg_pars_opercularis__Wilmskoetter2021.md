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
  target: anomia
  target_kind: impairment
  claim: Preservation of either direct or indirect white matter connections between the left IFG pars
    opercularis and the angular gyrus is associated with greater naming improvement following treatment
    in chronic aphasia.
  direction: likely
  relationship: responder
  citation: '@Wilmskoetter2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: computerized_lexical_semantic_treatment
    name: 3-week-long computerized language treatment focusing on lexical-semantic processing
  sample:
    n: 69
    population: chronic left-hemisphere ischemic stroke and aphasia
    time_post_onset: mean 41.15 months (SD 40.00)
    phase: chronic
    age_range: mean 59.54 (SD 10.26)
    handedness: not_reported
    language: not_reported
    cohort: NCT03416738
  statistics:
    threshold: P = .027 (direct) and P = .039 (indirect)
    effect_size: 23.47 more correct responses (direct) and 20.83 more correct responses (indirect) compared
      to no connection
  confounders_controlled:
  - age
  - years of formal education
  - baseline WAB-AQ
  - treatment type (A-tDCS vs S-tDCS)
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU anatomical atlas
    description: Inferior frontal gyrus opercularis (IFGop)
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: not_reported
    - modality: T2
      sequence: not_reported
    - modality: DTI
      sequence: not_reported
    preprocessing_pipeline: SPM12 normalization into standard space
    reference_space: MNI152
    atlases_used:
    - JHU anatomical atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 350
    confidence: high
    flags:
    - cohort overlaps with @Fridriksson2018JAMA (same phase 2 RCT)
  source_passages:
  - section: Results
    page: 350
    quote: Post hoc tests showed a significant difference in naming improvement between direct and no
      connections (P = .027) and between indirect and no connections (P = .039).
    supports: claim
  - section: Participants
    page: 348
    quote: We included 69 of 74 participants from the clinical trial... individuals with chronic left-hemisphere
      ischemic stroke and aphasia
    supports: sample
  - section: Materials and Methods
    page: 348
    quote: all participants received a 3-week-long computerized language treatment focusing on lexical-semantic
      processing with phonological, semantic, and unrelated foils.
    supports: method
  - section: Statistical Analyses
    page: 349
    quote: we conducted an analysis of covariance (ANCOVA) for each region pair to determine if connection
      type (no connection, indirect, direct) had an effect on change in naming... while controlling for
      age, number of years of formal education, baseline WAB-AQ, treatment type (A-tDCS vs S-tDCS).
    supports: method
  - section: Results
    page: 350
    quote: On average 23.47 more correct responses after treatment were produced by participants with
      a direct connection compared to participants without any connection between the IFGop and AG, and
      on average 20.83 more correct responses after treatment were produced by participants with an indirect
      connection compared to participants without any connection between the IFGop and AG.
    supports: statistics
  - section: Limitations
    page: 353
    quote: We mapped indirect connections based on structural connectomics; thus, we cannot claim that
      these indirect pathways are indeed functionally used.
    supports: limitation
  author_limitations:
  - Structural connectomics does not guarantee functional use of the identified indirect pathways.
  - Binarization of lesion maps may fail to identify existing relationships.
  - Findings may not generalize to other aspects of language beyond naming.
- id: f2
  target: anomia
  target_kind: impairment
  claim: 'The effect of anodal tDCS on naming improvement is moderated by the connection profile between
    the left IFG pars opercularis and the middle temporal gyrus: A-tDCS is most effective for those with
    indirect connections, while sham stimulation is most effective for those with direct connections.'
  direction: likely
  relationship: responder
  citation: '@Wilmskoetter2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: tdcs_aphasia_treatment
    name: anodal transcranial direct current stimulation (A-tDCS)
  sample:
    n: 69
    population: chronic left-hemisphere ischemic stroke and aphasia
    time_post_onset: mean 41.15 months (SD 40.00)
    phase: chronic
    age_range: mean 59.54 (SD 10.26)
    handedness: not_reported
    language: not_reported
    cohort: NCT03416738
  statistics:
    threshold: F[2, 56] = 3.45, P = .039
    effect_size: 'A-tDCS + indirect: 13.44 more correct responses (95% CI = 6.44-20.44); S-tDCS + direct:
      16.28 more correct responses (95% CI = 2.31-30.25)'
  confounders_controlled:
  - age
  - years of formal education
  - baseline WAB-AQ
  - treatment type
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU anatomical atlas
    description: Inferior frontal gyrus opercularis (IFGop)
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: not_reported
    - modality: T2
      sequence: not_reported
    - modality: DTI
      sequence: not_reported
    preprocessing_pipeline: SPM12 normalization into standard space
    reference_space: MNI152
    atlases_used:
    - JHU anatomical atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 350
    confidence: high
    flags:
    - cohort overlaps with @Fridriksson2018JAMA (same phase 2 RCT)
  source_passages:
  - section: Results
    page: 350
    quote: For the IFGop and MTG we revealed a significant interaction between connection type and treatment
      type on change in correct naming (F[2, 56] = 3.45 P = .039).
    supports: claim
  - section: Results
    page: 350
    quote: Participants with direct connections between the IFGop and MTG who received S-tDCS significantly
      improved... Participants with indirect connections between the IFGop and MTG who received A-tDCS
      significantly improved...
    supports: statistics
  - section: Discussion
    page: 352
    quote: Participants who received S-tDCS made the best treatment gains if they had preserved direct
      connections between the IFGop and MTG. However, participants who received A-tDCS made the best treatment
      gains if they had indirect connections.
    supports: claim
  - section: Discussion
    page: 352
    quote: these findings require cautious interpretation because the tDCS type was not randomized according
      to connection type.
    supports: limitation
  author_limitations:
  - tDCS type was not randomized according to connection type, meaning the interaction may reflect other
    group differences.
  - Structural connectomics does not guarantee functional use of the identified indirect pathways.
---
