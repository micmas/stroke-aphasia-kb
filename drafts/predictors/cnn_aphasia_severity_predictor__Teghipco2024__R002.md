---
id: cnn_aphasia_severity_predictor
name: CNN aphasia severity predictor
kind: predictor
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: The CNN achieved significantly higher predictive accuracy (median balanced accuracy of 0.77 and median F1 score of 0.7) than linear Support Vector Machines (SVMs) in identifying individuals with severe aphasia.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 213
    population: individuals with chronic left strokes
    phase: not_reported
    time_post_onset: chronic stage (mean 3.2 +/- 3.7 years post-stroke); imaging collected within 10 days of behavioral assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Data was downsampled to 8 mm voxel size to make nested cross-validation tractable
  - The study does not definitively rule out the possibility that other classical learning implementations could compete with the CNN
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A 3D Convolutional Neural Network (CNN) trained on ordinal morphometric maps (combining segmented white matter, gray matter, and cerebrospinal fluid volumes with manually segmented lesion masks) to discriminate severe aphasia from non-severe aphasia. Severe aphasia defined as WAB-R aphasia quotient below 50; CNN performance was significantly better than chance; SVM performance was evaluated using linear and nonlinear kernels, as well as with PCA and ICA dimensionality reduction, which did not significantly improve SVM F1 scores; Model fusion (stacking or averaging) did not substantially outperform the CNN alone. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Source PDF identity and methods/results checked. Target the measured WAB-R aphasia severity classification (AQ <50), not an aphasia syndrome. This is cross-sectional classifier performance or feature importance, not prospective
    recovery prediction or causal brain necessity. Use n=213 from Methods; the abstract states N=231, an unresolved source inconsistency explicitly retained here. No human approval.'
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
  citation: '@Teghipco2024'
  source_passages:
  - section: Original source P1-S1-C4
    page: 1
    quote: 'Methods Here, we test whether deep learning with Convolutional Neural Networks (CNNs)

      on whole brain morphometry (i.e., segmented tissue volumes) and lesion anatomy better

      predicts chronic stroke individuals with severe aphasia (N = 231) than classical machine

      learning (Support Vector Machines; SVMs), evaluating whether encoding spatial

      dependencies identiﬁes uniquely predictive patterns.'
    supports: method
  - section: Original source P1-S1-C5
    page: 1
    quote: 'Results CNNs achieve higher balanced accuracy and F1 scores, even when SVMs are

      nonlinear or integrate linear or nonlinear dimensionality reduction.'
    supports: claim
  - section: Original source P2-S4-C9
    page: 2
    quote: 'Methods

      Participants

      Two-hundred and thirteen individuals (age = 57.98 +/−11.34, 62% male)

      with chronic left strokes (mean years post-stroke = 3.2 +/−3.7) that par-

      ticipated in studies conducted at the Center for the Study of Aphasia

      Recovery (C-STAR) were analyzed retrospectively in the present work.'
    supports: sample
  - section: Original source P3-S1-C2
    page: 3
    quote: 'In

      the present study, we aimed to identify patients with severe aphasia (WAB-

      AQ below 50), who comprise 35% of the participant cohort and fall under

      the very severe or severe WAB-R categories.'
    supports: claim
  - section: Original source P3-S1-C5
    page: 3
    quote: 'Neuroimaging data was

      collected within 10 days of evaluation on the WAB-R.'
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: 'Segmented

      tissue and lesion maps were transformed to template space using k-nearest

      neighborinterpolationandmergedtogenerateordinalmorphometricmaps

      with voxels inside the lesion being assigned a 4th tissue value.'
    supports: method
  - section: Original source P4-S1-C9
    page: 4
    quote: 'The maps were then downsampled to 8 mm voxel size to

      make our comprehensive cross-validation scheme tractable with deep

      learning and the ﬁeld of view was cropped to remove any empty space

      present across all study participants.'
    supports: limitation
  - section: Original source P7-S1-C7
    page: 7
    quote: 'Paired t-tests comparing

      model performance across repeats revealed that linear SVMs had sig-

      niﬁcantly worse F1 scores (M = 0.65, SD = 0.02) compared to CNNs

      (M = 0.7, SD = 0.01), t(19) = −10, p = 5.26e−9, Cohen’s d = −2.24.'
    supports: claim
  - section: Original source P7-S1-C8
    page: 7
    quote: 'Overall,

      SVMs mean accuracy was worse (M = 0.73, SD = 0.01) than CNNs

      (M = 0.77, SD = 0.01), t(19) = −9.8, p = 7.28e−9, Cohen’s d = −2.2.'
    supports: claim
  - section: Original source P11-S1-C4
    page: 11
    quote: 'The current study

      leveraged deep and classical machine learning to understand how well brain

      morphometry and lesion anatomy can predict aphasia severity in chronic

      stroke, testing whether Convolutional Neural Networks’ (CNNs) unique

      sensitivity tospatialproperties would identifydistinct predictive patterns.In

      arepeated,nested,cross-validationscheme,wefoundthatCNNsperformed

      wellonthistask,achievingamedianbalancedaccuracyof77%andamedian

      F1 score of 0.7.'
    supports: claim
  - section: Original source P14-S3-C5
    page: 14
    quote: 'An important caveat to the results we present is that our data was

      downsampled to a lower resolution than typical to many neuroimaging

      analyses to make deep learning with nested cross-validation tractable.'
    supports: limitation
predictor_type: imaging_metric
short_definition: A 3D Convolutional Neural Network (CNN) trained on ordinal morphometric maps (combining segmented white matter, gray matter, and cerebrospinal fluid volumes with manually segmented lesion masks) to discriminate severe aphasia from non-severe aphasia.
assessment:
- Western Aphasia Battery-Revised Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Teghipco2024
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study directly compares the performance of a 3D CNN against SVMs in predicting severe aphasia using whole-brain morphometry and lesion anatomy, finding the CNN significantly more accurate.
    bucket: predictors
    entity_id: cnn_aphasia_severity_predictor
    name: CNN aphasia severity predictor
    kind: predictor
    predictor_type: imaging_metric
    definition: A 3D Convolutional Neural Network (CNN) trained on ordinal morphometric maps (combining segmented white matter, gray matter, and cerebrospinal fluid volumes with manually segmented lesion masks) to discriminate severe aphasia from non-severe aphasia.
    assessment:
    - Western Aphasia Battery-Revised (WAB-R)
    target: severe_aphasia
    target_kind: impairment
    claim: The CNN achieved significantly higher predictive accuracy (median balanced accuracy of 0.77 and median F1 score of 0.7) than linear Support Vector Machines (SVMs) in identifying individuals with severe aphasia.
    direction: likely
    method: MVPA
    relationship: correlational
    therapy: null
    sample_n: 213
    population: individuals with chronic left strokes
    timing: chronic stage (mean 3.2 +/- 3.7 years post-stroke); imaging collected within 10 days of behavioral assessment
    qualifications:
    - Severe aphasia defined as WAB-R aphasia quotient below 50
    - CNN performance was significantly better than chance
    - SVM performance was evaluated using linear and nonlinear kernels, as well as with PCA and ICA dimensionality reduction, which did not significantly improve SVM F1 scores
    - Model fusion (stacking or averaging) did not substantially outperform the CNN alone
    limitations:
    - Data was downsampled to 8 mm voxel size to make nested cross-validation tractable
    - The study does not definitively rule out the possibility that other classical learning implementations could compete with the CNN
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S1-C4
      supports: method
    - source_id: P1-S1-C5
      supports: claim
    - source_id: P2-S4-C9
      supports: sample
    - source_id: P3-S1-C2
      supports: claim
    - source_id: P3-S1-C5
      supports: method
    - source_id: P4-S1-C7
      supports: method
    - source_id: P4-S1-C9
      supports: limitation
    - source_id: P7-S1-C7
      supports: claim
    - source_id: P7-S1-C8
      supports: claim
    - source_id: P11-S1-C4
      supports: claim
    - source_id: P14-S3-C5
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
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      review_sha256: 8d7a558e52be5e3f0e45ec8e054dd1acdc5ec2f388b22878efa73fb39271f0a0
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
    reason: 'Teghipco2024: finding[0] (id=f1): target ''severe_aphasia'' is an aphasia syndrome but the claim is about a symptom; target the symptom entry (anomia, fluency, …) unless the paper classifies by syndrome'
    material_issues: []
    seconds_this_run: 178.9772822499799
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      original_mapping_sha256: 7e5e408b2f2eb4154c907851e342323335630d66eeb6ae0a0fa7389549f5e2fd
      original_status_sha256: d35e3cfa775e04cb72ad044b301f98236de3747b0341c5d362cf1b48aef5e914
      evidence_sha256: cfd39318c3e7f6cb42bd0141294dbdde925a2ccef2209954bea14af3b2d4c1c0
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      - 14
      note: Source PDF identity and methods/results checked. Target the measured WAB-R aphasia severity classification (AQ <50), not an aphasia syndrome. This is cross-sectional classifier performance or feature importance, not prospective recovery prediction or causal brain necessity. Use n=213 from Methods; the abstract states N=231, an unresolved source inconsistency explicitly retained here. No human approval.
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
  note: Source PDF identity and methods/results checked. Target the measured WAB-R aphasia severity classification (AQ <50), not an aphasia syndrome. This is cross-sectional classifier performance or feature importance, not prospective recovery prediction or causal brain necessity. Use n=213 from Methods; the abstract states N=231, an unresolved source inconsistency explicitly retained here. No human approval.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
