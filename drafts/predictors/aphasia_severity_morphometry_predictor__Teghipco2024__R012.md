---
id: aphasia_severity_morphometry_predictor
name: aphasia severity morphometry predictor
kind: predictor
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: For CNN models, Grad-CAM++ saliency was significantly higher in all left hemisphere regions for non-severe compared to severe predictions, while saliency was significantly higher in all right hemisphere regions for severe predictions. For SVM models, SHAP saliency was higher in the lesion for severe predictions, but higher in perilesional and extralesional regions for non-severe predictions.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 213
    population: individuals with chronic left strokes
    phase: not_reported
    time_post_onset: mean 3.2 years post-stroke; imaging collected within 10 days of behavioral evaluation
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - data was downsampled to a lower resolution than typical to make deep learning tractable
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A prediction model using whole-brain morphometry (segmented tissue volumes) and lesion anatomy to discriminate severe aphasia from non-severe aphasia. severe aphasia defined as WAB-AQ below 50; CNN results based on Grad-CAM++ saliency maps; SVM results based on SHAP saliency maps. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Source PDF identity and methods/results checked. Target the measured WAB-R aphasia severity classification (AQ <50), not an aphasia syndrome. This is cross-sectional classifier performance or feature importance, not prospective recovery prediction or causal brain necessity. Use n=213 from Methods; the abstract states N=231, an unresolved source inconsistency explicitly retained here. No human approval.'
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
  - section: Original source P2-S4-C9
    page: 2
    quote: 'Methods

      Participants

      Two-hundred and thirteen individuals (age = 57.98 +/−11.34, 62% male)

      with chronic left strokes (mean years post-stroke = 3.2 +/−3.7) that par-

      ticipated in studies conducted at the Center for the Study of Aphasia

      Recovery (C-STAR) were analyzed retrospectively in the present work.'
    supports: sample
  - section: Original source P14-S3-C5
    page: 14
    quote: 'An important caveat to the results we present is that our data was

      downsampled to a lower resolution than typical to many neuroimaging

      analyses to make deep learning with nested cross-validation tractable.'
    supports: limitation
  - section: Original source P9-S1-C8
    page: 9
    quote: 'Figure 8 shows that Grad-

      CAM++ saliency was signiﬁcantly higher in all left hemisphere regions for

      nonsevere compared to severe predictions based on two-sample t-tests (all

      p < 0.0001; see supplementary Table 2 for exact p-values).'
    supports: claim
  - section: Original source P9-S1-C9
    page: 9
    quote: 'In contrast,

      saliency was signiﬁcantly higher in all right hemisphere regions for severe

      predictions (all p < 0.0001; exact p-values can be found in Supplementary

      Table 2).'
    supports: claim
  - section: Original source P9-S1-C10
    page: 9
    quote: 'SVM SHAP saliency maps demonstrated higher feature impor-

      tance in the lesion for severe prediction, but higher importance in the

      perilesionalandextralesionalROIsfornonseverepredictions(allp < 0.0001;

      exact p-valuescanbe found in SupplementaryTable2).Featuresaliencywas

      low for homolog ROIs across patient class; however, it was relatively higher

      for severe predictions (all p < 0.0001; exact p-values can be found in Sup-

      plementary Table 2).'
    supports: claim
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
    supports: method
  - section: Original source P5-S3-C2
    page: 5
    quote: 'We further explored the impact of data dimensionality on SVM per-

      formance by cross-validating two additional SVM models, one trained on

      feature saliency maps generated by deep Shapley Additive exPlanations

      (SHAP) and another trained on feature maps generated by Gradient-

      weightedClassActivationMapping++(Grad-CAM++).Thiscomparison

      additionally permitted us to evaluate whether it was likely that the CNN

      Fig. 2 | Potential advantages of Convolutional Neural Networks (CNN) for the

      detection of spatially related changes in brain structure. a and e provide examples

      of two patterns of gray matter atrophy in perilesional brain areas (shown in blue) of

      individuals with identical lesions (shown in red).'
    supports: method
predictor_type: imaging_metric
short_definition: A prediction model using whole-brain morphometry (segmented tissue volumes) and lesion anatomy to discriminate severe aphasia from non-severe aphasia.
assessment:
- Western Aphasia Battery-Revised Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Teghipco2024
  proposal_id: R012
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis (R012) examines how the focus of predictive models (CNN and SVM) on different brain regions (lesion, perilesional, extralesional) varies by aphasia severity. The source provides specific findings for both the CNN (via Grad-CAM++) and SVM (via SHAP) models, allowing for a clear description of the association between regional saliency and aphasia severity.
    bucket: predictors
    entity_id: aphasia_severity_morphometry_predictor
    name: aphasia severity morphometry predictor
    kind: predictor
    predictor_type: imaging_metric
    definition: A prediction model using whole-brain morphometry (segmented tissue volumes) and lesion anatomy to discriminate severe aphasia from non-severe aphasia.
    assessment:
    - Western Aphasia Battery-Revised
    target: aphasia_severity
    target_kind: impairment
    claim: For CNN models, Grad-CAM++ saliency was significantly higher in all left hemisphere regions for non-severe compared to severe predictions, while saliency was significantly higher in all right hemisphere regions for severe predictions. For SVM models, SHAP saliency was higher in the lesion for severe predictions, but higher in perilesional and extralesional regions for non-severe predictions.
    direction: likely
    method: MVPA
    relationship: correlational
    therapy: null
    sample_n: 213
    population: individuals with chronic left strokes
    timing: mean 3.2 years post-stroke; imaging collected within 10 days of behavioral evaluation
    qualifications:
    - severe aphasia defined as WAB-AQ below 50
    - CNN results based on Grad-CAM++ saliency maps
    - SVM results based on SHAP saliency maps
    limitations:
    - data was downsampled to a lower resolution than typical to make deep learning tractable
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P2-S4-C9
      supports: sample
    - source_id: P3-S1-C2
      supports: claim
    - source_id: P3-S1-C5
      supports: claim
    - source_id: P9-S1-C8
      supports: claim
    - source_id: P9-S1-C9
      supports: claim
    - source_id: P9-S1-C10
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
    proposal: R012
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 68.47469104200718
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      original_mapping_sha256: 6d6844f3a793bb3b87d5ff129f0022f3eed57ef2814e2ae276db08d4729c7ba8
      original_status_sha256: 5b6594cf4efa91356e104230f0303bdd71f5a4e6262b5ba474e8d6f3701140a3
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
