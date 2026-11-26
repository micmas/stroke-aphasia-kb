---
id: pitch_accuracy
name: pitch accuracy
kind: predictor
findings:
- id: f1
  target: articulatory_quality
  target_kind: impairment
  claim: Pitch accuracy of sung syllables was not significantly correlated with relative articulatory quality (reported r(16)=0.29, nonsignificant) in the 17-person non-fluent aphasia sample.
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 17
    population: non-fluent aphasics (Broca's or global aphasia with prevailing expressive deficits)
    phase: not_reported
    time_post_onset: at least 3 months post-infarction (except one case)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Pitch accuracy of each sung syllable assessed separately for each lyric type. finding was independent of whether all or only left hemisphere lesion patients were included; finding was independent of whether all or specific lyric types were considered. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified the task-specific assessment: pitch accuracy for each sung syllable and relative articulatory quality. This is a concurrent correlation, not a singing treatment effect. Retain reported r=.29, nonsignificant, rather than infer a zero association.'
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
  citation: '@Stahl2011'
  source_passages:
  - section: Original source P7-S2-C12
    page: 7
    quote: 'A correlation analysis of pitch accuracy with relative

      articulatory quality did not yield signiﬁcant results [r(16) = 0.29,

      NS].'
    supports: claim
  - section: Original source P7-S2-C13
    page: 7
    quote: 'Notably, this ﬁnding was independent of whether all or

      only left hemisphere lesion patients were included.'
    supports: confounders
  - section: Original source P7-S3-C6
    page: 7
    quote: 'It should therefore be

      noted that pitch accuracy and articulatory quality were found to

      be unrelated in our data.'
    supports: claim
  - section: Original source P3-S2-C2
    page: 3
    quote: 'Seventeen stroke patients were

      included in the study.'
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: 'All patients were classiﬁed as non-ﬂuent aphasics, diagnosed with

      Broca’s aphasia (n = 10) or global aphasia with prevailing expressive

      deﬁcits (n = 7).'
    supports: sample
  - section: Original source P3-S2-C6
    page: 3
    quote: 'At

      the time of testing, all patients were at least 3 months post-infarction,

      except in one case (Patient HS).'
    supports: sample
  - section: Original source P6-S3-C10
    page: 6
    quote: 'Pitch accuracy of each sung syllable was assessed separately for

      each lyric type.'
    supports: method
predictor_type: behavioural
short_definition: Pitch accuracy of each sung syllable assessed separately for each lyric type
assessment:
- Task-specific sung-syllable pitch accuracy rating
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Stahl2011
  proposal_id: R003
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study explicitly tested the correlation between pitch accuracy in sung conditions and articulatory quality in non-fluent aphasics and found no significant association.
    bucket: predictors
    entity_id: pitch_accuracy
    name: pitch accuracy
    kind: predictor
    predictor_type: behavioural
    definition: Pitch accuracy of each sung syllable assessed separately for each lyric type
    assessment: []
    target: articulatory_quality
    target_kind: impairment
    claim: Pitch accuracy in the sung conditions had no significant impact on articulatory quality.
    direction: no_effect
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: 17
    population: non-fluent aphasics (Broca's or global aphasia with prevailing expressive deficits)
    timing: at least 3 months post-infarction (except one case)
    qualifications:
    - finding was independent of whether all or only left hemisphere lesion patients were included
    - finding was independent of whether all or specific lyric types were considered
    limitations:
    - small sample size
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S2-C12
      supports: claim
    - source_id: P7-S2-C13
      supports: confounders
    - source_id: P7-S3-C6
      supports: claim
    - source_id: P3-S2-C2
      supports: sample
    - source_id: P3-S2-C9
      supports: sample
    - source_id: P3-S2-C6
      supports: sample
    - source_id: P6-S3-C10
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      review_sha256: 553002c43d943cc341de539abd58bf654c8468fb7efda1ffdcdb58eca7953c2d
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
    proposal: R003
    status: failed
    reason: 'Stahl2011: predictor_type=''behavioural'' requires assessment (non-empty list of test names)'
    material_issues: []
    seconds_this_run: 94.28946541700861
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      original_mapping_sha256: 33863bfdb51f3cc84e5d4bde79cc600e7c8c5c5c4952cacf6afbdef553bc28bd
      original_status_sha256: ce3464a3f7f26195f5f4856da043d0677a709c264b3f078deb902188f6dc35cc
      evidence_sha256: 369d6f72c8781b0b42ff3caa9223a416ed7fc9516af3eb19f35b4e8199246968
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 3
      - 6
      - 7
      note: 'Verified the task-specific assessment: pitch accuracy for each sung syllable and relative articulatory quality. This is a concurrent correlation, not a singing treatment effect. Retain reported r=.29, nonsignificant, rather than infer a zero association.'
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
  note: 'Verified the task-specific assessment: pitch accuracy for each sung syllable and relative articulatory quality. This is a concurrent correlation, not a singing treatment effect. Retain reported r=.29, nonsignificant, rather than infer a zero association.'
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
