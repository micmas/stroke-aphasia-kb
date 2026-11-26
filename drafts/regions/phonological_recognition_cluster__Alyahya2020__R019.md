---
id: phonological_recognition_cluster
name: phonological recognition cluster
kind: network
findings:
- id: f1
  target: phonological_recognition
  target_kind: impairment
  claim: The phonological recognition component correlated with Heschl's gyrus and planum temporale.
  direction: likely
  relationship: correlational
  method: VBCM
  sample:
    n: 46
    population: patients with chronic post-stroke aphasia following a single left haemorrhagic or ischaemic stroke
    phase: not_reported
    time_post_onset: chronic stage (4-12 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - white matter tract labels are descriptive based on atlas overlap rather than direct DTI measurement
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Continuous voxel signal intensity associated with the phonological-recognition PCA component (word/nonword minimal-pair discrimination), using VBCM with the other components and demographic covariates. analysis performed without lesion volume as a covariate; component was identified within a unified PCA model including other language and cognitive domains. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): The selected evidence was split across adjacent text segments: P8-S2-C8 continues into P8-S3-C1. Verified Heschl''s gyrus/planum temporale component result in the PDF. VBCM measured continuous voxel signal intensity, not binary lesion overlap; this result is from the model without lesion-volume covariate, with other components and demographic factors included.'
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
  citation: '@Alyahya2020'
  source_passages:
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Analysis of neuroimaging data

      The unified PCA model was mapped onto brain lesions using a

      voxel-based correlational methodology (VBCM) (Tyler et al.,

      2005).'
    supports: method
  - section: Original source P3-S1-C8
    page: 3
    quote: 'Materials and methods

      Participants

      Forty-six patients who had developed aphasia following a single

      left haemorrhagic or ischaemic stroke were tested in the chronic

      stage (412 months post-stroke).'
    supports: sample
  - section: Original source P8-S1-C9
    page: 8
    quote: 'Neural correlates of connected

      speech alongside other language

      and cognitive domains

      For clarity, results without lesion volume as a covariate are

      discussed first.'
    supports: confounders
  - section: Original source P8-S2-C8
    page: 8
    quote: 'On the other hand, parietal

      regions involving the angular gyrus and posterior supramar-

      ginal gyrus, and tracts corresponding to the posterior seg-

      ment

      of

      the

      arcuate

      fasciculus

      correlated

      with

      both

      ‘phonological recognition’ and ‘phonological production’

      components. ‘Phonological recognition’ further correlated

      '
    supports: claim
  - section: Original source P8-S3-C1
    page: 8
    quote: 'both

      ‘phonological recognition’ and ‘phonological production’

      components. ‘Phonological recognition’ further correlated

      with Heschl’s gyrus and planum temporale. ‘Phonological

      production’ also related to the parietal operculum cortex,

      and tracts corresponding to the anterior and long segments

      of the arcuate fasciculus, the inferior longitudinal fasciculus

      and the cortico-spinal tract.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Alyahya2020
  proposal_id: R019
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study used VBCM to map a PCA-derived 'phonological recognition' component onto brain lesions, identifying a significant correlation with Heschl's gyrus and the planum temporale in chronic stroke patients.
    bucket: regions
    entity_id: phonological_recognition_cluster
    name: phonological recognition cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with a voxel-based correlational mapping of a PCA component derived from phonemic discrimination tests (word and non-word minimal pairs).
    assessment:
    - word minimal pairs
    - non-word minimal pairs
    target: phonological_recognition
    target_kind: impairment
    claim: The phonological recognition component correlated with Heschl's gyrus and planum temporale.
    direction: likely
    method: VBCM
    relationship: correlational
    therapy: null
    sample_n: 46
    population: patients with chronic post-stroke aphasia following a single left haemorrhagic or ischaemic stroke
    timing: chronic stage (4-12 months post-stroke)
    qualifications:
    - analysis performed without lesion volume as a covariate
    - component was identified within a unified PCA model including other language and cognitive domains
    limitations:
    - white matter tract labels are descriptive based on atlas overlap rather than direct DTI measurement
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S1-C6
      supports: claim
    - source_id: P8-S3-C1
      supports: claim
    - source_id: P4-S2-C3
      supports: method
    - source_id: P3-S1-C8
      supports: sample
    - source_id: P8-S1-C9
      supports: confounders
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      review_sha256: 2568f8e8fd3fcb3e46c5c0ec673c4dd1ad443886b7107e9ca56082c087a0b526
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
    proposal: R019
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 0.003387415999895893
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      original_mapping_sha256: 605a3729abdc02d2fb75e7eac7071c3163f1101fdf5dc32bce130f8f72f10bc5
      original_status_sha256: 50b13c7777cbae62fcd580f5838c2e3c8b5f9f57781f50fe37e17edc4ec2e3e7
      evidence_sha256: a2f912878162dac82e68d84efa653429115f42ccf7cfac587314b44b12a04c64
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 3
      - 4
      - 8
      note: 'The selected evidence was split across adjacent text segments: P8-S2-C8 continues into P8-S3-C1. Verified Heschl''s gyrus/planum temporale component result in the PDF. VBCM measured continuous voxel signal intensity, not binary lesion overlap; this result is from the model without lesion-volume covariate, with other components and demographic factors included.'
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
  note: 'The selected evidence was split across adjacent text segments: P8-S2-C8 continues into P8-S3-C1. Verified Heschl''s gyrus/planum temporale component result in the PDF. VBCM measured continuous voxel signal intensity, not binary lesion overlap; this result is from the model without lesion-volume covariate, with other components and demographic factors included.'
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
