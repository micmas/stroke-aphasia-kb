---
id: left_mca_inferior_division__Hillis2007__R002
name: left MCA inferior division cluster
kind: review
findings:
- id: f1
  target: wernickes_aphasia
  target_kind: impairment
  claim: Hillis2007 reports, based on the historical clinical literature summarized in this 2007 review, that wernicke's aphasia is usually caused by neural dysfunction in regions supplied by the inferior division of the left MCA, including Wernicke's area.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously reported stroke/aphasia studies and methodological literature summarized by Hillis2007; no newly recruited cohort.
    phase: not_reported
    time_post_onset: See cited primary reports; varies across review.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - localization of functions can only be approximate due to individual variability in cytoarchitectural fields, sulci, and gyri
  evidence_quality: narrative-review
  strength: weak
  notes: 'Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending. Source repair (unapproved): Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.'
  imaging_details:
    reference_space: not_applicable
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
    - not_transcribed:sample.n
    - agent_source_repair_pending_human_review
  citation: '@Hillis2007'
  source_passages:
  - section: Original source P4-S1-C6
    page: 4
    quote: 'This

      hypothesis can account for occasional dissociations

      between the typical deficits or anomalous lesion

      sites in patients with Wernicke’s aphasia by the fact

      that there is individual variability in the cerebral

      vasculature and the areas supplied by particular

      arteries.'
    supports: confounders
  - section: Original source P3-S2-C7
    page: 3
    quote: 'There is a great deal of individual

      variability in the boundaries of the cytoarchitectural

      fields identified by Brodmann, as well as in the pat-

      tern of sulci and gyri and general shape of individual

      brains.38,39 Therefore, “localization” of functions

      can only be approximate.'
    supports: limitation
  - section: Original source P4-S1-C5
    page: 4
    quote: 'These deficits

      have been attributed to impaired inhibition of lexi-

      cal activation, so that the person cannot select the

      appropriate word, sound, or meaning from compet-

      ing linguistic units that are also activated.33 Al-

      though such an underlying impairment would

      account for many of the observed language deficits,

      it could not easily account for cases with relatively

      preserved or relatively impaired categories of

      words, such as animals or tools,45 or impaired nouns

      relative to verbs.35 This collection of deficits is usu-

      ally caused by neural dysfunction in regions sup-

      plied by the inferior division of the left MCA,

      including Wernicke’s area (most of Brodmann area

      22, in the posterior, superior temporal gyrus).'
    supports: claim
  - section: Original source P1-S2-C1
    page: 1
    quote: 'well articulated but meaningless.3

      Although localization of functions in the brain lost favor in the early 20th century, these

      early observations provided some of the groundwork for Norman Geschwind’s5 seminal

      writings on aphasia classification and associated sites of lesions, briefly reviewed in this

      article.'
    supports: method
  - section: Original source P1-S2-C1
    page: 1
    quote: 'well articulated but meaningless.3

      Although localization of functions in the brain lost favor in the early 20th century, these

      early observations provided some of the groundwork for Norman Geschwind’s5 seminal

      writings on aphasia classification and associated sites of lesions, briefly reviewed in this

      article.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Hillis2007
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source explicitly links the clinical syndrome of Wernicke's aphasia to neural dysfunction in the territory of the inferior division of the left MCA, including Wernicke's area.
    bucket: regions
    entity_id: left_mca_inferior_division
    name: left MCA inferior division cluster
    kind: network
    predictor_type: imaging_metric
    definition: neural dysfunction in regions supplied by the inferior division of the left middle cerebral artery, including Wernicke's area (Brodmann area 22 in the posterior superior temporal gyrus)
    assessment: []
    target: wernickes_aphasia
    target_kind: impairment
    claim: Wernicke's aphasia is usually caused by neural dysfunction in regions supplied by the inferior division of the left MCA, including Wernicke's area.
    direction: likely
    method: clinical_RCT
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with Wernicke's aphasia
    timing: not_transcribed
    qualifications:
    - individual variability in cerebral vasculature and the areas supplied by particular arteries can account for occasional dissociations between typical deficits and lesion sites
    limitations:
    - localization of functions can only be approximate due to individual variability in cytoarchitectural fields, sulci, and gyri
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P4-S1-C5
      supports: claim
    - source_id: P4-S1-C6
      supports: confounders
    - source_id: P3-S2-C7
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
      pdf_sha256: c801ff6927ade291fadd0f394a819dd9a4b8c2fa2a78e8076224ad6cad6c5efc
      review_sha256: 69e4e8edbc539040cac28425628c6c9491f8c958bdefccefa5dd77a6c06734f3
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
    reason: Claim, population and method source evidence required
    seconds_this_run: 24.522445958005846
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c801ff6927ade291fadd0f394a819dd9a4b8c2fa2a78e8076224ad6cad6c5efc
      original_mapping_sha256: 84000b0f234d874901fc3a55c89c006808d79dee20a0a3f72d97ba81a9e4e3d5
      original_status_sha256: 6a21ec7c7db1259502cb382720c875ae3d593924714e804fd6586092a3dafc59
      evidence_sha256: a32ab4fef8f10e19aaf126cb20d5d3e1c57870606881add2b16e3385f1b6ad9e
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 4
      note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
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
  note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
