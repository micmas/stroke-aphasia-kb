---
id: slf_segment_1_fa
name: SLF segment 1 AWF
kind: predictor
findings:
- id: f1
  target: phonemic_paraphasias
  target_kind: impairment
  claim: Fractional anisotropy of posterior SLF segment 1 was weakly negatively associated with phonemic paraphasias (r=-.46), but the association did not survive correction for multiple comparisons (reported P>.05).
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 32
    population: right-handed native English speakers with chronic post-stroke aphasia (single left hemisphere ischemic stroke)
    phase: not_reported
    time_post_onset: chronic phase (at least 6 months post-stroke; mean 35 ± 30 months)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The SLF tract likely includes fibers from the arcuate fasciculus due to the lack of a curvature filtering algorithm.
  - AWF is based on simplifying assumptions about axonal coplanarity which may vary by location.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient fractional anisotropy in posterior SLF segment 1, delineated using patient-specific diffusion kurtosis tractography. r=-.46; did not survive correction for multiple comparisons (reported corrected P>.05); SLF may include arcuate fibers. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Restore selected FA analysis; original mapping incorrectly substituted the stronger AWF analysis. Patient-specific DKI tractography verified. Report negative nominal association and failure of multiple-comparison correction together.'
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
  - section: Original source P2-S4-C6
    page: 2
    quote: "The Pyramids and Palm Trees Test \n(PPT)21 was used to determine semantic knowledge, and the Philadelphia Naming Test (PNT)22 was used to \ntest confrontational naming."
    supports: method
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
  - section: Original source P7-S1-C4
    page: 7
    quote: "The FA of segment \n1 was weakly associated with phonemic paraphasias, albeit not surviving correction for multiple comparisons \n(r = −0.46, p > 0.05)."
    supports: claim
predictor_type: imaging_metric
short_definition: Patient fractional anisotropy in posterior SLF segment 1, delineated using patient-specific diffusion kurtosis tractography.
assessment:
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: McKinnon2018
  proposal_id: R005
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis identifies a significant association between the axonal water fraction (AWF) of the posterior segment of the SLF and the percentage of phonemic paraphasias, which persists after controlling for lesion overlap.
    bucket: predictors
    entity_id: slf_segment_1_awf
    name: SLF segment 1 AWF
    kind: predictor
    predictor_type: imaging_metric
    definition: Axonal water fraction (AWF) measured via DKI-based tractography in the most posterior segment (segment 1) of the superior longitudinal fasciculus (SLF).
    assessment:
    - Philadelphia Naming Test
    target: phonemic_paraphasias
    target_kind: impairment
    claim: The average AWF in segment 1 of the SLF is associated with the percentage of phonemic paraphasias, and this relationship remains significant when controlling for white matter lesion overlap.
    direction: likely
    method: tractography
    relationship: correlational
    therapy: null
    sample_n: 32
    population: right-handed native English speakers with chronic post-stroke aphasia (single left hemisphere ischemic stroke)
    timing: chronic phase (at least 6 months post-stroke; mean 35 ± 30 months)
    qualifications:
    - The association was found to be more significant for AWF than for FA (which did not survive multiple comparison correction).
    - The relationship remained significant after controlling for white matter lesion overlap with the SLF and ILF.
    - The relationship remained significant when adjusting for supra-Sylvian gray matter necrosis.
    limitations:
    - The SLF tract likely includes fibers from the arcuate fasciculus due to the lack of a curvature filtering algorithm.
    - AWF is based on simplifying assumptions about axonal coplanarity which may vary by location.
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S1-C2
      supports: claim
    - source_id: P7-S1-C9
      supports: claim
    - source_id: P2-S3-C10
      supports: sample
    - source_id: P2-S3-C12
      supports: sample
    - source_id: P2-S4-C6
      supports: method
    - source_id: P3-S2-C4
      supports: method
    - source_id: P5-S1-C5
      supports: method
    - source_id: P7-S2-C5
      supports: claim
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
    proposal: R005
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 55.79347837500973
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      original_mapping_sha256: c519f1e8b8dd9d6517fd7b66e7742be452cec26de48940ba0df1c5e311a86c0b
      original_status_sha256: cfdee22d668c18e3965808b75135231c82d6459ed7b88b5dc5200602a153cf01
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
      note: Restore selected FA analysis; original mapping incorrectly substituted the stronger AWF analysis. Patient-specific DKI tractography verified. Report negative nominal association and failure of multiple-comparison correction together.
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
  note: Restore selected FA analysis; original mapping incorrectly substituted the stronger AWF analysis. Patient-specific DKI tractography verified. Report negative nominal association and failure of multiple-comparison correction together.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
