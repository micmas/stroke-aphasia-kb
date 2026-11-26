---
id: anterior_dorsal_stream_cluster
name: anterior dorsal stream cluster
kind: network
findings:
- id: f1
  target: phonological_errors_in_naming
  target_kind: impairment
  claim: Voxels in which lesion status correlated with phonological error rates in object naming were strongly concentrated in frontal and parietal cortices of the anterior dorsal stream, specifically the postcentral gyrus, supramarginal gyrus, and precentral gyrus, with no significant clusters in the posterior superior temporal gyrus or posterior superior temporal sulcus.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 106
    population: individuals with diverse profiles of aphasia secondary to stroke
    phase: not_reported
    time_post_onset: at least 1 month post-onset of aphasia
  statistics:
    threshold: FDR q=.01; critical t=3.51; main phonological-error VLSM.
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - structural MRI limitations for white-matter labels
  - potential underestimation of functional tissue damage by lesion characterization
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
  citation: '@Schwartz2012'
  source_passages:
  - section: Original source P1-S1-C7
    page: 1
    quote: 'Voxels in which lesion status correlated with phonological error rates localized to dorsal stream areas, in keeping with

      classical and contemporary brain-language models.'
    supports: claim
  - section: Original source P6-S2-C10
    page: 6
    quote: 'Anatomical ﬁndings: phonological

      errors

      In the VLSM of phonological errors with FDR-controlled threshold

      (q = 0.01; critical t-value 3.51), a total of 14 372 signiﬁcant voxels

      were identiﬁed (Fig. 2).'
    supports: claim
  - section: Original source P6-S2-C11
    page: 6
    quote: 'The largest concentration was located in

      the postcentral gyrus (5331 voxels; 37% of total), in a region

      extending from the cortex abutting the Sylvian ﬁssure inferiorly,

      to approximate MNI z-value 64, superiorly.'
    supports: claim
  - section: Original source P6-S2-C12
    page: 6
    quote: "The voxel with the\nhighest t-value (t = 5.17) was located in the inferior portion of\nthe precentral gyrus (MNI x = \x0462, y = \x0416, z = 11)."
    supports: claim
  - section: Original source P6-S2-C15
    page: 6
    quote: 'There were 1419

      signiﬁcant voxels in this region.'
    supports: claim
  - section: Original source P6-S3-C5
    page: 6
    quote: "A large number of signiﬁcant voxels (2275 voxels; 16% of total)\noccupied the supramarginal gyrus; the maximal t-value in this\ncluster (t = 4.82) was at MNI coordinates x = \x0445, y = \x0430,\nz = 26."
    supports: claim
  - section: Original source P6-S3-C6
    page: 6
    quote: "A smaller cluster of signiﬁcant voxels occupied the mid-\nportion of the central sulcus of the insula (1010 voxels; 7% of\ntotal); the maximal t-value (t = 4.63) was at MNI coordinates\nx = \x0439, y = 2, z = \x041."
    supports: claim
  - section: Original source P6-S3-C7
    page: 6
    quote: "Additionally, there was a small cluster in\nthe inferior frontal gyrus pars opercularis and rare voxels in pars\ntriangularis; the peak t-value (t = 4.46) in inferior frontal gyrus was\nat MNI coordinates x = \x0461, y = \x043, z = 4."
    supports: claim
  - section: Original source P6-S3-C10
    page: 6
    quote: 'Critical to the study hypotheses, there were no

      voxel

      clusters

      in

      the

      posterior

      superior

      temporal

      gyrus

      or

      posterior superior temporal sulcus.'
    supports: claim
  - section: Original source P6-S3-C12
    page: 6
    quote: 'Only 39 voxels in the Spt mask corre-

      lated signiﬁcantly with phonological errors—1% of the 3636

      voxels in Spt mask and a negligible fraction of the 14 372 total

      voxels.'
    supports: claim
  - section: Original source P7-S1-C3
    page: 7
    quote: 'To summarize, in this, the main VLSM of phonological errors,

      we found that voxels carrying a statistically signiﬁcant correlation

      with phonological errors were strongly concentrated in frontal and

      parietal cortices, i.e. the anterior dorsal stream.'
    supports: claim
  - section: Original source P3-S3-C1
    page: 3
    quote: 'The inclusion criteria were as follows: at least 1 month post-onset of

      aphasia secondary to stroke, living at home, medically stable without

      major psychiatric or neurological co-morbidities, premorbid right hand-

      edness, English as primary language, adequate vision and hearing

      (with or without correction) and CT or MRI conﬁrmed left hemisphere

      cortical lesion.'
    supports: sample
  - section: Original source P3-S3-C2
    page: 3
    quote: 'Of the 142 individuals enrolled, 106 qualiﬁed for the

      current study.'
    supports: sample
  - section: Original source P4-S2-C11
    page: 4
    quote: 'In short, the analysis of phonological errors involved all and only

      Philadelphia Naming Test non-word errors.'
    supports: claim
  - section: Original source P5-S2-C11
    page: 5
    quote: 'For analyses

      with one dependent variable (e.g. phonological errors) and one inde-

      pendent variable (lesion status), a t-test was performed at each voxel

      comparing scores on the dependent variable between patients with

      and without lesions in that voxel.'
    supports: method
  - section: Original source P7-S1-C10
    page: 7
    quote: 'Both secondary analyses

      again produced anterior-centred phonological errors-lesion corre-

      lation maps.'
    supports: claim
  - section: Original source P14-S1-C1
    page: 14
    quote: '

      The characterization of the lesions in this study likely underes-

      timates the extent of functional tissue damage.'
    supports: limitation
  design: cross-sectional
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Schwartz2012
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study used VLSM to identify brain regions where lesion status correlated with phonological error rates in object naming. The results localized these voxels to the anterior dorsal stream (specifically postcentral gyrus, supramarginal gyrus, and precentral gyrus), while finding no significant clusters in the posterior superior temporal gyrus or sulcus.
    bucket: regions
    entity_id: anterior_dorsal_stream_cluster
    name: anterior dorsal stream cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with voxels where lesion status correlated with phonological error rates in object naming
    assessment:
    - Philadelphia Naming Test
    target: phonological_errors_in_naming
    target_kind: impairment
    claim: Voxels in which lesion status correlated with phonological error rates in object naming were strongly concentrated in frontal and parietal cortices of the anterior dorsal stream, specifically the postcentral gyrus, supramarginal gyrus, and precentral gyrus, with no significant clusters in the posterior superior temporal gyrus or posterior superior temporal sulcus.
    direction: likely
    method: VLSM
    relationship: correlational
    therapy: null
    sample_n: 106
    population: individuals with diverse profiles of aphasia secondary to stroke
    timing: at least 1 month post-onset of aphasia
    qualifications:
    - phonological errors were defined as all non-word errors in the Philadelphia Naming Test regardless of phonemic overlap with the target
    - analysis included patients with and without apraxia of speech
    - results were consistent when regressing out lesion size
    limitations:
    - structural MRI limitations for white-matter labels
    - potential underestimation of functional tissue damage by lesion characterization
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S1-C7
      supports: claim
    - source_id: P6-S2-C10
      supports: claim
    - source_id: P6-S2-C11
      supports: claim
    - source_id: P6-S2-C12
      supports: claim
    - source_id: P6-S2-C15
      supports: claim
    - source_id: P6-S3-C5
      supports: claim
    - source_id: P6-S3-C6
      supports: claim
    - source_id: P6-S3-C7
      supports: claim
    - source_id: P6-S3-C10
      supports: claim
    - source_id: P6-S3-C12
      supports: claim
    - source_id: P7-S1-C3
      supports: claim
    - source_id: P3-S3-C1
      supports: sample
    - source_id: P3-S3-C2
      supports: sample
    - source_id: P4-S2-C11
      supports: claim
    - source_id: P5-S2-C11
      supports: method
    - source_id: P7-S1-C10
      supports: claim
    - source_id: P14-S1-C1
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
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      review_sha256: fe3f6b3213144baf063144c24d628a2d2bbff829e01ad23f846dfc458380b042
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
    proposal: R001
    status: failed
    reason: Truncated output held
    seconds_this_run: 154.1323017500108
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      original_mapping_sha256: 643a73d0ae58762cb135034aba500a5356a31d7efa7e5ef72d0ade2e2262de38
      original_status_sha256: f2d979d94489b8216ced07e2e4edc79ecccfd89db8f35d39bfef3be025fd49b5
      evidence_sha256: d564c3ba5c480d168d91eb41cfff390996db366c5e013ac6efbe5d993ab16080
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
      - 4
      - 5
      - 6
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
