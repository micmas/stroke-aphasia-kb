---
id: insula_arcuate_slf_fluency_cluster
name: insula and arcuate/superior longitudinal fasciculus cluster
kind: network
findings:
- id: f1
  target: speech_fluency
  target_kind: impairment
  claim: Lesions in the insula and the arcuate/superior longitudinal fasciculus in parietal white matter were most strongly associated with deficits in speech fluency.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 101
    population: left-hemisphere-injured stroke patients with some degree of speech or language impairment
    phase: not_reported
    time_post_onset: at least one year after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The apparent role of the insula could be an indirect consequence of lesions to Broca's area, although ANCOVA analysis suggested independence
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with voxels in the insula and the arcuate/superior longitudinal fasciculus in parietal white matter, analyzed via voxel-based lesion-symptom mapping. The anterior insula was found to be critical for fluency independent of Broca''s area. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
    - original_mapper_failed_method_evidence_binding
    - agent_repaired_unapproved
  citation: '@Bates2003'
  design: cross-sectional
  source_passages:
  - section: Original source P2-S1-C11
    page: 2
    quote: 'We analyzed data on speech fluency and language comprehen-

      sion for 101 left-hemisphere-injured stroke patients who showed

      some degree of speech or language impairment.'
    supports: sample
  - section: Original source P2-S1-C13
    page: 2
    quote: 'For this reason, we focused on

      the fluency and auditory comprehension subtests of a standard

      assessment tool, the Western Aphasia Battery (WAB)6.'
    supports: claim
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Patients were tested

      at least one year after stroke.'
    supports: sample
  - section: Original source P2-S2-C10
    page: 2
    quote: 'Fluency was most affected

      by lesions in the insula (Fig. 1b) and in the arcuate/superior lon-

      gitudinal fasciculus in parietal white matter (Fig. 1c).'
    supports: claim
  - section: Original source P2-S3-C11
    page: 2
    quote: 'Lesions within the insula (b) and deep parietal

      white matter (c) had the most impact on fluency, whereas injury to the

      middle temporal gyrus (d) produced the largest effect on measures of audi-

      tory comprehension.'
    supports: claim
  - section: Original source P3-S1-C6
    page: 3
    quote: 'These maps

      showed that the anterior insula is critical for fluency, independent

      of Broca’s area (Fig. 2a), whereas Broca’s area is not especially

      important for fluency once lesions to the insula have been

      accounted for (Fig. 2b).'
    supports: claim
  - section: Original source P2-S2-C4
    page: 2
    quote: 'Patients’

      lesions were reconstructed onto templates by a board-certified neu-

      rologist (R.T.K.) who was blind to the clinical status of each

      patient2,5.'
    supports: method
  - section: Original source P2-S2-C8
    page: 2
    quote: 'For each voxel, patients were divided into two groups according

      to whether they did or did not have a lesion affecting that voxel.'
    supports: method
  - section: Original source P2-S2-C9
    page: 2
    quote: 'Behavioral scores were then compared for these two groups, yield-

      ing a t-statistic for each voxel (Fig. 1).'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
reviewer_marks:
- id: failed-draft-repair
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Agent checked article identity, result, population and method against the original PDF. Original mapper failed because no method evidence was tagged. No new independent model check or human approval has occurred.
relationship_review:
  paper: Bates2003
  proposal_id: R008
  approved: false
  original_mapping:
    decision: draft
    reason: The study uses VLSM to identify brain regions most strongly associated with speech fluency deficits in a cohort of stroke patients, specifically highlighting the insula and the arcuate/superior longitudinal fasciculus.
    bucket: regions
    entity_id: insula_arcuate_slf_fluency_cluster
    name: insula and arcuate/superior longitudinal fasciculus cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with voxels in the insula and the arcuate/superior longitudinal fasciculus in parietal white matter, analyzed via voxel-based lesion-symptom mapping.
    assessment:
    - Western Aphasia Battery (WAB)
    target: speech_fluency
    target_kind: impairment
    claim: Lesions in the insula and the arcuate/superior longitudinal fasciculus in parietal white matter were most strongly associated with deficits in speech fluency.
    direction: likely
    method: VLSM
    relationship: correlational
    therapy: null
    sample_n: 101
    population: left-hemisphere-injured stroke patients with some degree of speech or language impairment
    timing: at least one year after stroke
    qualifications:
    - The anterior insula was found to be critical for fluency independent of Broca's area
    limitations:
    - The apparent role of the insula could be an indirect consequence of lesions to Broca's area, although ANCOVA analysis suggested independence
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P2-S1-C11
      supports: sample
    - source_id: P2-S1-C13
      supports: claim
    - source_id: P2-S2-C6
      supports: sample
    - source_id: P2-S2-C10
      supports: claim
    - source_id: P2-S3-C11
      supports: claim
    - source_id: P3-S1-C6
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
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      review_sha256: 122eb2239d758cf4fd30a7b0161cd5230c041b310b08b626103af44fcc986ef7
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
    proposal: R008
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 0.005227583002124447
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Added the actual lesion-reconstruction and voxelwise t-test method passages on PDF page 2; retained the directly supported relationship and population. Pages 1 and 3 contain adjacent articles, whose results are excluded.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      original_mapping_sha256: 323a07ee04347b43c207917e106ffca7024416ec9528ce8f8828a8de9d139bde
      original_status_sha256: 840307d38e2ab5032bea21a515e243cd7673689189fa125296a5b4456ec2ea09
      evidence_sha256: b0e254808c8080f5aebf191b5fd4e8c9b64a1641c700b0ada3b92091888aec18
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    remaining:
    - Human PDF review and approval
    - Main Results, figures and tables completeness check
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T00:25:36.604288+00:00'
      approved: false
      pdf_pages:
      - 2
      - 3
      note: Added the actual lesion-reconstruction and voxelwise t-test method passages on PDF page 2; retained the directly supported relationship and population. Pages 1 and 3 contain adjacent articles, whose results are excluded.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Added the actual lesion-reconstruction and voxelwise t-test method passages on PDF page 2; retained the directly supported relationship and population. Pages 1 and 3 contain adjacent articles, whose results are excluded.
    original_scope: Agent source inspection and missing-method-evidence repair of a failed mapping; not an independent model pass or human approval.
---

# Source review required

This repaired draft is unapproved. Its original failed attempt is preserved in the frontmatter.
