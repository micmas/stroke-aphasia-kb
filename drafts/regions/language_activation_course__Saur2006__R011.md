---
id: language_activation_course
name: language activation course cluster
kind: network
findings:
- id: f1
  target: language_recovery_dynamics
  target_kind: prognosis
  claim: 'Language-specific activation follows different temporal courses across regions: the left IFG and left posterior middle temporal gyrus show a monophasic course with continuous increase of activation, while the right insular cortex, right IFG, and SMA show a biphasic curve with an early increase followed by a later decrease.'
  direction: mixed
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 14
    population: patients with aphasia due to an embolic first-ever infarction of the left middle cerebral artery territory
    phase: not_reported
    time_post_onset: Scans at mean 1.8 days, 12.1 days and 321 days after stroke.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Results are limited to a highly selected group of less severely impaired patients who were able to cooperate with fMRI in the first days after stroke
  evidence_quality: cohort
  strength: weak
  notes: 'Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Source repair (unapproved): Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval.'
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
  citation: '@Saur2006'
  source_passages:
  - section: Original source P7-S1-C3
    page: 7
    quote: 'Plots of the

      parameter estimates (speech > reversed speech) for each of

      the six identiﬁed areas revealed different language recovery

      curves: left IFG and left posterior middle temporal gyrus

      showed a monophasic course with continuous increase of

      activation, whereas right insular cortex, right IFG and

      SMA showed a biphasic curve with an early increase and

      later decrease of activation.'
    supports: claim
  - section: Original source P7-S1-C4
    page: 7
    quote: 'A two-factorial repeated-mea-

      sures ANOVA with the factors time (Ex1-3) · region revealed

      that the course of activation over time was heterogeneous in

      the six tested regions (signiﬁcant interaction effect region ·

      time; F(10, 130) = 5.21, P < 0.001).'
    supports: method
  - section: Original source P2-S4-C1
    page: 2
    quote: "Study design\nPatients were ﬁrst scanned 0–4 days post-stroke (dps) (Ex1, mean:\n1.8 dps) and again \x022 weeks later before discharge or transfer to a\nrehabilitation facility (Ex2, mean: 12.1 dps)."
    supports: sample
  - section: Original source P2-S4-C2
    page: 2
    quote: "A follow-up examina-\ntion in the chronic stage was carried out \x024–12 months post-stroke\n(Ex3, mean: 321 dps)."
    supports: sample
  - section: Original source P4-S2-C5
    page: 4
    quote: 'From a total of 198 consecutively screened aphasic

      stroke patients, 14 met our inclusion criteria and were

      recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

      11 male and three female].'
    supports: sample
  - section: Original source P12-S3-C7
    page: 12
    quote: 'Thus, the

      results are limited to somewhat less severely impaired patients

      who were clearly aphasic at the ﬁrst exam but were able to

      understand the task.'
    supports: limitation
  - section: Original source P7-S1-C7
    page: 7
    quote: 'Post hoc paired t-tests

      (two-tailed) showed that the early increase of activation (Ex1

      versus Ex2) was signiﬁcant in all identiﬁed regions except for

      the pars triangularis of the left IFG.'
    supports: claim
  - section: Original source P7-S1-C8
    page: 7
    quote: 'The late increase (Ex1

      versus Ex3) was signiﬁcant in all left-hemisphere regions and

      the right insular cortex.'
    supports: claim
  - section: Original source P7-S1-C9
    page: 7
    quote: 'The decrease of activation (Ex2 ver-

      sus Ex3) was signiﬁcant only in the right insular cortex and

      right IFG.'
    supports: claim
  design: longitudinal
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Saur2006
  proposal_id: R011
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a heterogeneous course of language-specific activation across six regions over three phases of recovery (acute, subacute, chronic), with specific monophasic and biphasic patterns identified.
    bucket: regions
    entity_id: language_activation_course
    name: language activation course cluster
    kind: network
    predictor_type: imaging_metric
    definition: 'Language-specific activation (intelligible speech > reversed speech) measured via fMRI at three time points: acute (mean 1.8 dps), subacute (mean 12.1 dps), and chronic (mean 321 dps).'
    assessment:
    - fMRI
    target: language_recovery_dynamics
    target_kind: prognosis
    claim: 'Language-specific activation follows different temporal courses across regions: the left IFG and left posterior middle temporal gyrus show a monophasic course with continuous increase of activation, while the right insular cortex, right IFG, and SMA show a biphasic curve with an early increase followed by a later decrease.'
    direction: likely
    method: fMRI_activation
    relationship: correlational
    therapy: null
    sample_n: 14
    population: patients with aphasia due to an embolic first-ever infarction of the left middle cerebral artery territory
    timing: concurrently measured at acute (0-4 days), subacute (~2 weeks), and chronic (4-12 months) stages
    qualifications:
    - The early increase of activation (Ex1 vs Ex2) was significant in all identified regions except for the pars triangularis of the left IFG
    - The late increase (Ex1 vs Ex3) was significant in all left-hemisphere regions and the right insular cortex
    - The decrease of activation (Ex2 vs Ex3) was significant only in the right insular cortex and right IFG
    limitations:
    - Results are limited to a highly selected group of less severely impaired patients who were able to cooperate with fMRI in the first days after stroke
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S1-C3
      supports: claim
    - source_id: P7-S1-C4
      supports: method
    - source_id: P2-S4-C1
      supports: sample
    - source_id: P2-S4-C2
      supports: sample
    - source_id: P4-S2-C5
      supports: sample
    - source_id: P12-S3-C7
      supports: limitation
    - source_id: P7-S1-C7
      supports: claim
    - source_id: P7-S1-C8
      supports: claim
    - source_id: P7-S1-C9
      supports: claim
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      review_sha256: 62f2029b8c3c7c439c1d6c00c11eb6280d30f7de8dde5ca4a7dcdcc0940f79bb
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
    proposal: R011
    status: failed
    reason: Truncated output held
    seconds_this_run: 170.26835091601242
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      original_mapping_sha256: 979b6afc201cde830acec3d6178f3b031608f3171caddb30017f2d6f43e88a4c
      original_status_sha256: 328e7a1e125637f7b91217d875a6c803d68c35e196f82062ad92778c0011457a
      evidence_sha256: 49bacac36f08b81933cef517c8bd27c086e53f4de07e6959346cf7e5632bf1e3
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 2
      - 4
      - 7
      note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
