---
id: gender_familial_sinistrality__Coppens2002__R002
name: gender and familial sinistrality association
kind: review
findings:
- id: f1
  target: familial_sinistrality
  target_kind: impairment
  claim: Coppens2002 reports from its analysis of published cases that male subjects with crossed aphasia were significantly more likely than female subjects to have a positive history of familial sinistrality.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously published crossed-aphasia cases analysed by the review; analysis-specific denominators differ.
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: See source passages for the review’s case-level statistical analysis; not a new cohort.
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - measurement of familial sinistrality lacks accuracy
  - familial sinistrality is difficult to establish in most cases
  - probability of familial sinistrality increases with family size
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators. Source repair (unapproved): Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.'
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
  citation: '@Coppens2002'
  source_passages:
  - section: Original source P1-S1-C4
    page: 1
    quote: 'However, male were signiﬁcantly more likely than female CA

      subjects to show a positive history of familial sinistrality.'
    supports: claim
  - section: Original source P18-S1-C2
    page: 18
    quote: 'However, there was a signiﬁcant diﬀerence

      between the frequency of familial sinistrality (Yates corrected v2 ¼ 5.021, df ¼ 1,

      p ¼ :025).'
    supports: claim
  - section: Original source P18-S1-C3
    page: 18
    quote: 'A history of familial sinistrality was signiﬁcantly more frequent in male

      than in female CA subjects.'
    supports: claim
  - section: Original source P27-S2-C8
    page: 27
    quote: 'However, the only statistically signiﬁ-

      cant result in this review suggested that more males than females had a history of

      familial sinistrality.'
    supports: claim
  - section: Original source P29-S1-C8
    page: 29
    quote: 'The only signiﬁcant result suggests that males

      have a signiﬁcantly higher probability to have a positive familial sinistrality, which in

      turn suggests that the language lateralization mechanism in males may be more likely

      to be inﬂuenced by genetic handedness factors.'
    supports: claim
  - section: Original source P29-S1-C9
    page: 29
    quote: 'However, the measurement of fa-

      milial sinistrality lacks accuracy.'
    supports: limitation
  - section: Original source P28-S1-C1
    page: 28
    quote: '

      caveat, we would strongly underscore that familial sinistrality is rather diﬃcult to

      establish in most CA cases.'
    supports: limitation
  - section: Original source P28-S1-C3
    page: 28
    quote: 'Furthermore, the probability of familial sinistrality clearly increases with family size

      (Bishop, 1980).'
    supports: limitation
  - section: Original source P17-S2-C12
    page: 17
    quote: 'The overall data set was statistically analyzed based on several deﬁning features:

      gender, familial sinistrality, CA subtype (i.e., mirror-image vs. anomalous), and

      aphasia type.'
    supports: method
  - section: Original source P17-S1-C11
    page: 17
    quote: 'Male subjects accounted for 66.1% of the cases and females for

      33.9% (n ¼ 165).'
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Coppens2002
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a statistically significant association between gender and familial sinistrality in patients with crossed aphasia, noting that males were more likely to have a positive history of familial sinistrality.
    bucket: predictors
    entity_id: gender_familial_sinistrality
    name: gender and familial sinistrality association
    kind: predictor
    predictor_type: demographic
    definition: Gender (male vs female) in patients with crossed aphasia.
    assessment: []
    target: familial_sinistrality
    target_kind: impairment
    claim: Male subjects with crossed aphasia were significantly more likely than female subjects to have a positive history of familial sinistrality.
    direction: likely
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: 165
    population: patients with crossed aphasia
    timing: concurrent
    qualifications:
    - familial sinistrality was recorded as any mention of one or more left-handed family members, including descendants or relatives two generations removed
    limitations:
    - measurement of familial sinistrality lacks accuracy
    - familial sinistrality is difficult to establish in most cases
    - probability of familial sinistrality increases with family size
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S1-C4
      supports: claim
    - source_id: P18-S1-C2
      supports: claim
    - source_id: P18-S1-C3
      supports: claim
    - source_id: P27-S2-C8
      supports: claim
    - source_id: P29-S1-C8
      supports: claim
    - source_id: P17-S1-C11
      supports: sample
    - source_id: P16-S1-C2
      supports: method
    - source_id: P29-S1-C9
      supports: limitation
    - source_id: P28-S1-C1
      supports: limitation
    - source_id: P28-S1-C3
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      review_sha256: 3d3639b15bf67edde5fd481a6aacd66b70c50bd9fcec6baabfc53381f1004181
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
    proposal: R002
    status: failed
    reason: Truncated output held
    seconds_this_run: 436.721573625
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      original_mapping_sha256: 96bfef5cbed3fdac9ed5dee8b5bafa41882d2dbebe99da0b121a68c96ca52ebb
      original_status_sha256: a33499a8b91ddc1897b9fdd4d117f6f97cd64d23f36a2f1a2ce29350f0533ab6
      evidence_sha256: 92a0eb9069615cc78286bcf11df00e37aeb7ec79819a55a9fda1e490a5970671
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 16
      - 17
      - 18
      - 27
      - 29
      note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
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
  note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
