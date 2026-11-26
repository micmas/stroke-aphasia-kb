---
id: lrs_ex1_activation_correlation
name: Acute phase LRS-activation correlation
kind: predictor
findings:
- id: f1
  target: overall_language_recovery_score
  target_kind: impairment
  claim: In the acute phase, better initial language performance (as measured by LRSEx1) was strongly positively correlated with higher language activation in the left IFG, SMA, and a small cluster in the pars triangularis of the right IFG.
  direction: likely
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 14
    population: Patients with aphasia due to an embolic first-ever stroke of the left MCA territory
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
  - The patient group was highly selected, requiring the ability to understand the task and cooperate during a 20-minute fMRI session in the first days after stroke.
  - Results are limited to somewhat less severely impaired patients who were clearly aphasic but able to understand the task.
  - In three patients, the identified peak in the left IFG was located within the infarct, resulting in low effect sizes for those individuals.
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
  - section: Original source P7-S2-C4
    page: 7
    quote: 'In the acute phase, there was a strong

      positive linear correlation of LRSEx1 with language activation

      with two large clusters in the left IFG (r = 0.93, P < 0.001) and

      SMA (r = 0.88, P < 0.001), and a small cluster in the pars

      triangularis of the right IFG (r = 0.79, P < 0.001, Tab. 4A).'
    supports: claim
  - section: Original source P11-S1-C12
    page: 11
    quote: 'The correlation of initial language impair-

      ment and language activation revealed that better language

      performance was linked to higher activation in the left IFG.'
    supports: claim
  - section: Original source P4-S2-C5
    page: 4
    quote: 'From a total of 198 consecutively screened aphasic

      stroke patients, 14 met our inclusion criteria and were

      recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

      11 male and three female].'
    supports: sample
  - section: Original source P2-S4-C1
    page: 2
    quote: "Study design\nPatients were ﬁrst scanned 0–4 days post-stroke (dps) (Ex1, mean:\n1.8 dps) and again \x022 weeks later before discharge or transfer to a\nrehabilitation facility (Ex2, mean: 12.1 dps)."
    supports: method
  - section: Original source P2-S3-C10
    page: 2
    quote: 'These

      scores were normalized to a range of 0–1 (scorenor) and averaged

      into a composite score labelled the ‘overall language recovery score’

      {LRS = [AABTnor + AAT (without TT and SPSnor) + TTnor + SPSnor +

      CETInor + Tasknor]/6} with a resulting range between 0 and 1.'
    supports: method
  - section: Original source P12-S3-C7
    page: 12
    quote: 'Thus, the

      results are limited to somewhat less severely impaired patients

      who were clearly aphasic at the ﬁrst exam but were able to

      understand the task.'
    supports: limitation
  - section: Original source P8-S1-C2
    page: 8
    quote: 'In three patients, the

      identiﬁed peak in the left IFG was located in the infarct; there-

      fore, the corresponding effect sizes were low (marked black in

      the plot).'
    supports: limitation
  design: longitudinal
predictor_type: imaging_metric
short_definition: Task-related language activation (intelligible speech > reversed speech) measured by fMRI during the acute phase (0-4 days post-stroke).
assessment:
- fMRI
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Saur2006
  proposal_id: R015
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study reports a significant positive correlation between the overall language recovery score (LRS) at the first examination (acute phase) and task-related language activation in specific brain regions (left IFG, SMA, and right IFG).
    bucket: predictors
    entity_id: lrs_ex1_activation_correlation
    name: Acute phase LRS-activation correlation
    kind: predictor
    predictor_type: imaging_metric
    definition: Task-related language activation (intelligible speech > reversed speech) measured by fMRI during the acute phase (0-4 days post-stroke).
    assessment:
    - fMRI
    target: overall_language_recovery_score
    target_kind: impairment
    claim: In the acute phase, better initial language performance (as measured by LRSEx1) was strongly positively correlated with higher language activation in the left IFG, SMA, and a small cluster in the pars triangularis of the right IFG.
    direction: likely
    method: fMRI_activation
    relationship: correlational
    therapy: null
    sample_n: 14
    population: Patients with aphasia due to an embolic first-ever stroke of the left MCA territory
    timing: Acute phase (0-4 days post-stroke; mean 1.8 days)
    qualifications:
    - The correlation was measured using simple linear regression between the LRS of each patient and the respective language activation contrast image.
    - The LRS is a composite score averaging normalized results from AABT, AAT, Token Test, spontaneous speech analysis, CETI, and scanner task performance.
    limitations:
    - The patient group was highly selected, requiring the ability to understand the task and cooperate during a 20-minute fMRI session in the first days after stroke.
    - Results are limited to somewhat less severely impaired patients who were clearly aphasic but able to understand the task.
    - In three patients, the identified peak in the left IFG was located within the infarct, resulting in low effect sizes for those individuals.
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S2-C4
      supports: claim
    - source_id: P11-S1-C12
      supports: claim
    - source_id: P4-S2-C5
      supports: sample
    - source_id: P2-S4-C1
      supports: method
    - source_id: P2-S3-C10
      supports: method
    - source_id: P12-S3-C7
      supports: limitation
    - source_id: P8-S1-C2
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
    proposal: R015
    status: failed
    reason: Truncated output held
    seconds_this_run: 178.37686862499686
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      original_mapping_sha256: 5c003215b9995ceb1ef4420ce14d2f64b49c0b702c1236e623520b7522dd87fa
      original_status_sha256: c0bece330e6501ff97a84350f0da8a09e9c373ae8177e80056060ee71548f911
      evidence_sha256: 49bacac36f08b81933cef517c8bd27c086e53f4de07e6959346cf7e5632bf1e3
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 2
      - 4
      - 7
      - 11
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
