---
id: svm_dimensionality_reduction
name: SVM dimensionality reduction (PCA/ICA)
kind: predictor
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: Dimensionality reduction using PCA or ICA did not significantly improve SVM performance in discriminating participants with severe aphasia (WAB-AQ < 50) from those with moderate or mild aphasia, and there was no significant performance difference between the use of PCA versus ICA.
  direction: no_effect
  relationship: correlational
  method: MVPA
  sample:
    n: 213
    population: individuals with chronic left strokes
    phase: not_reported
    time_post_onset: cross-sectional; imaging collected within 10 days of behavioral evaluation; mean years post-stroke = 3.2 +/- 3.7
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - data was downsampled to 8 mm voxel size to make cross-validation tractable
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Support Vector Machine (SVM) models trained on brain morphometry and lesion anatomy, where data was preprocessed using either Principal Component Analysis (PCA) or Independent Component Analysis (ICA) to reduce the number of features (retaining between 1 and 75 components). performance assessed using F1 score and mean accuracy; dimensionality reduction was folded into the cross-validation process. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Source PDF identity and methods/results checked. Target the measured WAB-R aphasia severity classification (AQ <50), not an aphasia syndrome. This is cross-sectional classifier performance or feature importance, not prospective recovery prediction or causal brain necessity. Use n=213 from Methods; the abstract states N=231, an unresolved source inconsistency explicitly retained here. No human approval.'
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
  - section: Original source P5-S1-C11
    page: 5
    quote: 'We addressed the possibility that poorer SVM performance relative to

      CNNreﬂectsoptimizationfailureinhighdimensionalfeaturespacebycross

      validating two additional SVMs independently, one which used Principal

      Component Analysis (PCA) as a data preprocessing step and another that

      '
    supports: method
  - section: Original source P5-S2-C1
    page: 5
    quote: 'CNNreﬂectsoptimizationfailureinhighdimensionalfeaturespacebycross

      validating two additional SVMs independently, one which used Principal

      Component Analysis (PCA) as a data preprocessing step and another that

      relaxed component orthogonality constraints by applying Independent

      Component Analysis (ICA) to the components.'
    supports: method
  - section: Original source P5-S2-C3
    page: 5
    quote: 'For both dimensionality reduction techniques, model

      order selection was expressed as a hyperparameter that was tuned in the

      inner folds by validating SVM models trained on lower dimensional spaces

      that retained between 1 and 75 components (i.e., 75 total values tested).'
    supports: method
  - section: Original source P7-S1-C12
    page: 7
    quote: 'Paired t-tests revealed usage of PCA

      (F1:M = 0.65,SD = 0.02; mean accuracy: M = 0.72, SD = 0.02) versus ICA

      (F1:M = 0.65, SD = 0.02; mean accuracy: M = 0.72, SD = 0.02) conferred no

      signiﬁcant performance beneﬁt on F1 scores, t(19) = 0.67, p = 0.51, Cohen’s

      D = 0.18 or mean accuracy, t(19) = 0.61, p = 0.55, Cohen’s D = 0.16, sug-

      gesting ICA did not capture considerable nonlinearities.'
    supports: claim
  - section: Original source P7-S2-C2
    page: 7
    quote: 'Further, dimen-

      sionality reduction did not improve SVM performance according to F1,

      whether using PCA, t(19) = 0.47, p = 0.65, Cohen’s D = 0.13, or ICA,

      t(19) = 0.95,p = 0.35,Cohen’sD = 0.3.Thesamewastrueformeanaccuracy

      with PCA, t(19) = 0.1.51, p = 0.26, Cohen’s D = 0.33, and ICA, t(19) = 1.42,

      p = 0.17, Cohen’s D = 0.45.'
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
  - section: Original source P14-S3-C5
    page: 14
    quote: 'An important caveat to the results we present is that our data was

      downsampled to a lower resolution than typical to many neuroimaging

      analyses to make deep learning with nested cross-validation tractable.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Support Vector Machine (SVM) models trained on brain morphometry and lesion anatomy, where data was preprocessed using either Principal Component Analysis (PCA) or Independent Component Analysis (ICA) to reduce the number of features (retaining between 1 and 75 components).
assessment:
- Western Aphasia Battery-Revised Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Teghipco2024
  proposal_id: R006
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis tests whether dimensionality reduction (PCA or ICA) improves the performance of SVMs in predicting severe aphasia. The results explicitly state that neither PCA nor ICA provided a significant performance benefit over the baseline SVM, nor was there a significant difference between the two techniques.
    bucket: predictors
    entity_id: svm_dimensionality_reduction
    name: SVM dimensionality reduction (PCA/ICA)
    kind: predictor
    predictor_type: imaging_metric
    definition: Support Vector Machine (SVM) models trained on brain morphometry and lesion anatomy, where data was preprocessed using either Principal Component Analysis (PCA) or Independent Component Analysis (ICA) to reduce the number of features (retaining between 1 and 75 components).
    assessment:
    - Western Aphasia Battery-Revised (WAB-R)
    target: severe_aphasia
    target_kind: impairment
    claim: Dimensionality reduction using PCA or ICA did not significantly improve SVM performance in discriminating participants with severe aphasia (WAB-AQ < 50) from those with moderate or mild aphasia, and there was no significant performance difference between the use of PCA versus ICA.
    direction: no_effect
    method: MVPA
    relationship: correlational
    therapy: null
    sample_n: 213
    population: individuals with chronic left strokes
    timing: cross-sectional; imaging collected within 10 days of behavioral evaluation; mean years post-stroke = 3.2 +/- 3.7
    qualifications:
    - performance assessed using F1 score and mean accuracy
    - dimensionality reduction was folded into the cross-validation process
    limitations:
    - data was downsampled to 8 mm voxel size to make cross-validation tractable
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S1-C11
      supports: method
    - source_id: P5-S2-C1
      supports: method
    - source_id: P5-S2-C3
      supports: method
    - source_id: P7-S1-C12
      supports: claim
    - source_id: P7-S2-C2
      supports: claim
    - source_id: P2-S4-C9
      supports: sample
    - source_id: P3-S1-C2
      supports: claim
    - source_id: P3-S1-C5
      supports: method
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
    proposal: R006
    status: failed
    reason: 'Teghipco2024: finding[0] (id=f1): target ''severe_aphasia'' is an aphasia syndrome but the claim is about a symptom; target the symptom entry (anomia, fluency, …) unless the paper classifies by syndrome'
    material_issues: []
    seconds_this_run: 148.33134270799928
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      original_mapping_sha256: 46304f3d728dc049c147c1ef3c825d000db72483ecbb671c37583c6a763d6d0e
      original_status_sha256: f728a8c69f0bd7fc9af2c310c44e35b0bcb5ec8cf7986c5cfcb903c9711a26ad
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
