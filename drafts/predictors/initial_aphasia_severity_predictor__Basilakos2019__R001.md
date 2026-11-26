---
id: initial_aphasia_severity_predictor
name: Initial Aphasia Severity Prediction Model
kind: predictor
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: Lesion volume and time poststroke at initial assessment were the best predictors of initial aphasia severity.
  direction: likely
  relationship: correlational
  method: structural_MRI
  sample:
    n: 35
    population: Individuals in the chronic stage of recovery after a single-event left-hemisphere stroke (middle cerebral artery territory) with aphasia
    phase: not_reported
    time_post_onset: Initial assessment occurred at a mean of 36.3 months poststroke (range 6-202 months); imaging was acquired within 1 week of initial assessment.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Retrospective study
  - Small sample size
  - Male-dominated sample (approximately 3:1 ratio)
  - Mean stroke age (55.5 years) is relatively young compared to national averages
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A regression model using lesion volume (measured via manual tracing on T2-MRIs and normalized via enantiomorphic segmentation-normalization) and time poststroke at initial assessment. Larger lesions were associated with more severe aphasia; Every 1-month increase in time poststroke at assessment was associated with an expected AQ increase of 0.21 points. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified source identity, n=35 and initial-assessment outcome. Initial AQ is the aphasia severity outcome, not the canonical predictor concept initial_aphasia_severity. These are structural-MRI regression analyses (lesion volume or right-hemisphere Fazekas WMH ratings), not voxel-wise LSM or behavioral-only measurement.'
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
  citation: '@Basilakos2019'
  source_passages:
  - section: Original source P6-S2-C4
    page: 6
    quote: "In addressing our first line of inquiry, lesion volume and \ntime poststroke at evaluation were the 2 significant predictors \nof initial aphasia severity, accounting for over one-third of \nthe variance, F(4, 34) = 6.1, P < .001, adjusted R2 = 0.37."
    supports: claim
  - section: Original source P7-S1-C1
    page: 7
    quote: "\n724\t\nNeurorehabilitation and Neural Repair 33(9)\nLarger lesions were associated with more severe aphasia at \ninitial evaluation (t = −4.3, P = .001), and for every 1-month \nincrease in time poststroke at assessment, expected AQ \nincrease was 0.21 points (t = 2.66, P = .01)."
    supports: claim
  - section: Original source P8-S1-C3
    page: 8
    quote: "Our \nresults showed that lesion volume and time post-stroke at \ninitial assessment were the best predictors of initial aphasia \nseverity; leukoaraiosis severity was not a significant predic-\ntor of initial aphasia severity in the chronic stage."
    supports: claim
  - section: Original source P2-S3-C1
    page: 2
    quote: "This is a retrospective study including multi–time point \nassessment of N = 35 participants (9 females; age at stroke: \nM = 55.5 ± 10 years, range = 31-71 years) in the chronic \nstage of recovery after a single-event left hemisphere stroke \n(ie, ≥6 months poststroke; at initial MRI assessment, M = \n36.4 ± 40.8 months poststroke, range = 6-202 months)."
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: "Inclusion criteria for these studies were as follows: \nbetween the ages of 21 and 85 years, premorbidly right-\nhanded individuals in the chronic (≥6 months poststroke) \nstage of recovery following a single-event left hemisphere \nstroke, presence of aphasia (as indicated by a Western \nAphasia Battery24,25 (WAB) Aphasia Quotient (AQ) <93.8), \nand able to undergo neuroimaging on a 3T MRI scanner."
    supports: sample
  - section: Original source P2-S3-C4
    page: 2
    quote: "All \nparticipants presented with left hemisphere stroke to the ter-\nritory of the middle cerebral artery."
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: "Normalization proce-\ndures were as follows: First, stroke lesions were manually \ntraced by a stroke neurologist blind to participant testing \n(author LB) in MRIcron28 on individual T2-MRIs (in \nnative space)."
    supports: method
  - section: Original source P3-S3-C5
    page: 3
    quote: "Lesion volume, obtained from the normalized lesion \nmaps, was used to determine the spatial extent of the \nstroke lesion, where lesion volume (in cm3) was used as a \npredictor variable in regression models."
    supports: method
  - section: Original source P10-S1-C1
    page: 10
    quote: "\nBasilakos et al\t\n727\nLimitations\nBecause of the retrospective nature of this study, there are \nseveral limitations that should be considered."
    supports: limitation
  - section: Original source P10-S1-C2
    page: 10
    quote: "First, the \nsample size was relatively small, and we were unable to \ncontrol for, or identify, factors that may have influenced \nthe presence and severity of leukoaraiosis (eg, diabetes, \natherosclerotic disease, hypertension, age)."
    supports: limitation
  - section: Original source P10-S1-C7
    page: 10
    quote: "Second, the mean stroke age of participants in this sam-\nple was relatively young (mean age at stroke = 55.5 years, \nSD = 10) compared with the United States national aver-\nage, where three-quarters of strokes occur in individuals \nolder than 65 years.53 Though it should be noted that stroke \nrates are on the rise in younger populations (eg, 20- to \n44-year-olds,54 45- to 64-year-olds55)."
    supports: limitation
  - section: Original source P10-S2-C6
    page: 10
    quote: "Third, it should also be noted that the male dominated \nsample in this study (ie, approximately a 3:1 ratio of \nmales:females) is not representative of the fact that when \ncontrolling for age, rates of poststroke aphasia are similar \nbetween males and females.56 However, sex differences \nin leukoaraiosis have been reported, where women have \nbeen shown to demonstrate more severe leukoaraiosis,57,58 \nand that WMH tend to progress more rapidly in deep \nwhite matter regions.59 However, sex differences in leu-\nkoaraiosis are not a unanimous finding.60 Given these \nreported sex differences in leukoaraiosis and its progres-\nsion, further study with a larger sample size should indeed \nexplore the role of sex on leukoaraiosis in poststroke \naphasia, and whether this gives rise to a sex difference in \nrates of decline."
    supports: limitation
predictor_type: imaging_metric
short_definition: A regression model using lesion volume (measured via manual tracing on T2-MRIs and normalized via enantiomorphic segmentation-normalization) and time poststroke at initial assessment.
assessment:
- Western Aphasia Battery Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Basilakos2019
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis evaluates the predictive capacity of lesion volume and time poststroke on initial aphasia severity in a chronic stroke population.
    bucket: predictors
    entity_id: initial_aphasia_severity_predictor
    name: Initial Aphasia Severity Prediction Model
    kind: predictor
    predictor_type: imaging_metric
    definition: A regression model using lesion volume (measured via manual tracing on T2-MRIs and normalized via enantiomorphic segmentation-normalization) and time poststroke at initial assessment.
    assessment:
    - Western Aphasia Battery Aphasia Quotient
    target: initial_aphasia_severity
    target_kind: impairment
    claim: Lesion volume and time poststroke at initial assessment were the best predictors of initial aphasia severity.
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: 35
    population: Individuals in the chronic stage of recovery after a single-event left-hemisphere stroke (middle cerebral artery territory) with aphasia
    timing: Initial assessment occurred at a mean of 36.3 months poststroke (range 6-202 months); imaging was acquired within 1 week of initial assessment.
    qualifications:
    - Larger lesions were associated with more severe aphasia
    - Every 1-month increase in time poststroke at assessment was associated with an expected AQ increase of 0.21 points
    limitations:
    - Retrospective study
    - Small sample size
    - Male-dominated sample (approximately 3:1 ratio)
    - Mean stroke age (55.5 years) is relatively young compared to national averages
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P6-S2-C4
      supports: claim
    - source_id: P7-S1-C1
      supports: claim
    - source_id: P8-S1-C3
      supports: claim
    - source_id: P2-S3-C1
      supports: sample
    - source_id: P2-S3-C3
      supports: sample
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P3-S2-C9
      supports: method
    - source_id: P3-S3-C5
      supports: method
    - source_id: P10-S1-C1
      supports: limitation
    - source_id: P10-S1-C2
      supports: limitation
    - source_id: P10-S1-C7
      supports: limitation
    - source_id: P10-S2-C6
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
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      review_sha256: 792ae8a84920eeb61cc2d6ccf27dca72b3766c3f8f0c80825b514787b1794a28
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
    reason: Target kind conflicts with existing KB concept
    material_issues: []
    seconds_this_run: 0.07825208399663097
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      original_mapping_sha256: f9b4462a3d4b461a8948481f6215bf939e7ff87dcc23eb2e6b3337f9b3861933
      original_status_sha256: 0f7671c5fc063ca3fd1ee0278acdb7a3fd038c59f1db11d444c16a8b3e173995
      evidence_sha256: b0e37a6119e4de5857d4283a8450f6583fe4170536236ee6d72e40696f3658f2
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 3
      - 5
      - 6
      - 7
      - 8
      - 10
      note: Verified source identity, n=35 and initial-assessment outcome. Initial AQ is the aphasia severity outcome, not the canonical predictor concept initial_aphasia_severity. These are structural-MRI regression analyses (lesion volume or right-hemisphere Fazekas WMH ratings), not voxel-wise LSM or behavioral-only measurement.
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
  note: Verified source identity, n=35 and initial-assessment outcome. Initial AQ is the aphasia severity outcome, not the canonical predictor concept initial_aphasia_severity. These are structural-MRI regression analyses (lesion volume or right-hemisphere Fazekas WMH ratings), not voxel-wise LSM or behavioral-only measurement.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
