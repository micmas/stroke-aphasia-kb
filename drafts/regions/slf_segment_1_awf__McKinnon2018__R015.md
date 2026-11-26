---
id: slf_segment_1_awf
name: SLF segment 1 cluster
kind: network
findings:
- id: f1
  target: smg_necrosis
  target_kind: impairment
  claim: Patient axonal water fraction in posterior SLF segment 1 was negatively associated with supramarginal gyrus necrosis (r=-.55, P<.05).
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 32
    population: right-handed native English speakers with chronic post-stroke aphasia following a single left-hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: chronic phase (at least 6 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The SLF tract likely includes fibers from both the SLF and the arcuate fasciculus due to the lack of a fiber curvature filtering algorithm
  - AWF is based on simplifying assumptions about axonal coplanarity which may affect accuracy in regions with complex fiber crossings
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Axonal water fraction (AWF) calculated from the most posterior segment (segment 1) of the superior longitudinal fasciculus (SLF) using kurtosis-based white matter tractography. SMG necrosis versus phonemic paraphasias is a separate nonsignificant association (r=.31, P=.21). Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified patient-specific diffusion kurtosis tractography and AWF, rather than a normative template. Selected association is posterior SLF AWF versus SMG necrosis (r=-.55, P<.05); the separate weak nonsignificant SMG-paraphasia relationship must not be attributed to AWF.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
    extracted_on: '2026-11-26'
    paper_section: Main paper; qualitative core draft
    confidence: low
    flags:
    - core_profile_machine_prepared
    - human_approval_pending
    - core_text_check_only
    - paper_completeness_pending
    - pdf_visual_review_pending
    - not_transcribed:statistics
    - not_transcribed:confounders_controlled
    - not_transcribed:confounders_not_controlled
    - not_transcribed:region_definition
    - not_transcribed:imaging_details.reference_space
    - not_transcribed:imaging_details.atlases_used
    - not_transcribed:lesion_mapping
    - not_transcribed:sample.phase
    - not_transcribed:strength
    - agent_source_repair_pending_human_review
  citation: '@McKinnon2018'
  source_passages:
  - section: Original source P2-S3-C10
    page: 2
    quote: "We studied 32 participants with chronic post-stroke aphasia (age: 57 ± 11 y, time post-stroke: \n35 ± 30 mos, gender: 8 women)."
    supports: sample
  - section: Original source P2-S3-C12
    page: 2
    quote: "They were right-handed native English speakers with a history of a single previous ischemic \nstroke in the left hemisphere at least 6 months before enrollment."
    supports: sample
  - section: Original source P3-S2-C4
    page: 3
    quote: "In this study, we employed three novel forms of structural \nwhite matter analyses: (a) patient specific white matter tractography was performed using DKI, a technique that \nrequires a multi-shell diffusion acquisition and dedicated post-processing procedures to improve upon tractog-\nraphy through the delineation of fiber crossings23,24; (b) the integrity of individual fibers was described using \nmicrostructural modeling metrics (i.e. AWF) derived from DKI15, which provide a more specific description of \nthe underlying microstructure than conventional dMRI metrics (i.e. FA); and (c) AWF and FA- were assessed in \na fine grained pattern along specific tracts, enabling a detailed assessment of where and how post-stroke integrity \ncan affect language."
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: "AWF and FA values were quantified at each point, but to facilitate statistical analysis, we assigned the average \nmetric to each point along the fiber bundle’s geometric mean resulting in 100 values along the length of the ILF \nand SLF sections that were ultimately binned into 4 segments containing 25 nodes each (Fig. 2, right)."
    supports: method
  - section: Original source P9-S2-C10
    page: 9
    quote: "The SLF, \nhowever, likely includes fibers from both the SLF and the arcuate fasciculus, since no filtering algorithm based \non fiber curvature was implemented."
    supports: limitation
  - section: Original source P9-S3-C5
    page: 9
    quote: "For example, \nthe WMTI model assumes that in a voxel all axons lie in the same plane, which might be more or less accurate \nin different locations15."
    supports: limitation
  - section: Original source P7-S2-C6
    page: 7
    quote: "Note that the AWF calcu-\nlated from SLF’s segment 1 was associated with supra-marginal gyrus (SMG) necrosis (−0.55, p < 0.05); however, \nSMG necrosis only weakly related to the percentage of phonemic paraphasias (r = 0.31, p = 0.21)."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: McKinnon2018
  proposal_id: R015
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis describes a statistically significant association between the axonal water fraction (AWF) of the posterior segment of the superior longitudinal fasciculus (SLF) and the necrosis of the supramarginal gyrus (SMG) in chronic stroke patients.
    bucket: regions
    entity_id: slf_segment_1_awf
    name: SLF segment 1 cluster
    kind: network
    predictor_type: imaging_metric
    definition: Axonal water fraction (AWF) calculated from the most posterior segment (segment 1) of the superior longitudinal fasciculus (SLF) using kurtosis-based white matter tractography.
    assessment: []
    target: smg_necrosis
    target_kind: impairment
    claim: The AWF calculated from SLF segment 1 was associated with supra-marginal gyrus (SMG) necrosis.
    direction: likely
    method: tractography
    relationship: correlational
    therapy: null
    sample_n: 32
    population: right-handed native English speakers with chronic post-stroke aphasia following a single left-hemisphere ischemic stroke
    timing: chronic phase (at least 6 months post-stroke)
    qualifications:
    - The association with SMG necrosis did not translate to a significant relationship with the percentage of phonemic paraphasias (r = 0.31, p = 0.21)
    limitations:
    - The SLF tract likely includes fibers from both the SLF and the arcuate fasciculus due to the lack of a fiber curvature filtering algorithm
    - AWF is based on simplifying assumptions about axonal coplanarity which may affect accuracy in regions with complex fiber crossings
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S2-C6
      supports: claim
    - source_id: P2-S3-C10
      supports: sample
    - source_id: P2-S3-C12
      supports: sample
    - source_id: P3-S2-C4
      supports: method
    - source_id: P5-S1-C5
      supports: method
    - source_id: P9-S2-C10
      supports: limitation
    - source_id: P9-S3-C5
      supports: limitation
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      review_sha256: 769f9dfe804092fcb0c19e5644eda528e69ca3cf1acfb97910f04c99003b1bbb
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    proposal: R015
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P7-S2-C6
    seconds_this_run: 106.63476499999524
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      original_mapping_sha256: 8c379e334fa7c5d1483178236a58df825024d31c3f002df7fff8a2817e6342f4
      original_status_sha256: f155cc350c859298c99fe2188b6cef738f2086b776f498261c17115cccb6b4be
      evidence_sha256: 8a2cbb1d26859a84386ded4bf1e1dce4a9ef4a5dfb9520d605c96740c6b1c851
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 3
      - 5
      - 7
      - 9
      note: Verified patient-specific diffusion kurtosis tractography and AWF, rather than a normative template. Selected association is posterior SLF AWF versus SMG necrosis (r=-.55, P<.05); the separate weak nonsignificant SMG-paraphasia relationship must not be attributed to AWF.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round3.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round3
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Verified patient-specific diffusion kurtosis tractography and AWF, rather than a normative template. Selected association is posterior SLF AWF versus SMG necrosis (r=-.55, P<.05); the separate weak nonsignificant SMG-paraphasia relationship must not be attributed to AWF.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
