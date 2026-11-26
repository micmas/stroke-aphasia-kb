---
id: leukoaraiosis_severity
name: leukoaraiosis severity
kind: predictor
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: Leukoaraiosis severity was not a significant predictor of initial aphasia severity in the chronic stage.
  direction: no_effect
  relationship: correlational
  method: structural_MRI
  sample:
    n: 35
    population: Individuals in the chronic stage of recovery after a single-event left-hemisphere stroke (middle cerebral artery territory) with aphasia
    phase: not_reported
    time_post_onset: Initial evaluation at mean 36.4 months poststroke (range 6-202 months)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Retrospective study
  - Unable to control for factors influencing leukoaraiosis such as diabetes, atherosclerotic disease, or hypertension
  - Male-dominated sample (approximately 3:1 ratio)
  - Mean stroke age was relatively young (55.5 years)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Visual rating of periventricular hyperintensities and deep white matter hyperintensities on T2-weighted MRI scans using the Fazekas scale (total score 0-6), rated for the right hemisphere only. Analysis was part of a regression model that also included lesion volume and time poststroke at initial evaluation; Lesion volume and time post-stroke at initial assessment were identified as the best predictors of initial aphasia severity. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified source identity, n=35 and initial-assessment outcome. Initial AQ is the aphasia severity outcome, not the canonical predictor concept initial_aphasia_severity. These are structural-MRI regression analyses (lesion volume or right-hemisphere Fazekas WMH ratings), not voxel-wise LSM or behavioral-only measurement.'
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
  - section: Original source P3-S1-C13
    page: 3
    quote: "Leukoaraiosis was scored on the \nT2-weighted MRI scans using the Fazekas scale,13 a \nvisual rating scale."
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: "Of note, total Fazekas \nscores ≥3 have been considered to reflect severe white \nmatter changes, as these scores correspond to the pres-\nence of early-confluent or confluent WMH.26 Because of \nvariability in left hemisphere lesion size and location, rat-\nings were completed for the right hemisphere only, as per \nprior work in post-stroke individuals23 and the assump-\ntion that leukoaraiotic changes are generally symmetric \nbetween hemispheres.27 Scans were rated by consensus \nby authors AB and LJ, who were blind to all participant \ninformation."
    supports: method
  - section: Original source P5-S1-C1
    page: 5
    quote: "\n722\t\nNeurorehabilitation and Neural Repair 33(9)\nand leukoaraiosis severity were entered as predictors to a \nmodel with initial AQ as the dependent variable."
    supports: method
  - section: Original source P10-S1-C2
    page: 10
    quote: "First, the \nsample size was relatively small, and we were unable to \ncontrol for, or identify, factors that may have influenced \nthe presence and severity of leukoaraiosis (eg, diabetes, \natherosclerotic disease, hypertension, age)."
    supports: limitation
  - section: Original source P10-S2-C6
    page: 10
    quote: "Third, it should also be noted that the male dominated \nsample in this study (ie, approximately a 3:1 ratio of \nmales:females) is not representative of the fact that when \ncontrolling for age, rates of poststroke aphasia are similar \nbetween males and females.56 However, sex differences \nin leukoaraiosis have been reported, where women have \nbeen shown to demonstrate more severe leukoaraiosis,57,58 \nand that WMH tend to progress more rapidly in deep \nwhite matter regions.59 However, sex differences in leu-\nkoaraiosis are not a unanimous finding.60 Given these \nreported sex differences in leukoaraiosis and its progres-\nsion, further study with a larger sample size should indeed \nexplore the role of sex on leukoaraiosis in poststroke \naphasia, and whether this gives rise to a sex difference in \nrates of decline."
    supports: limitation
predictor_type: imaging_metric
short_definition: Visual rating of periventricular hyperintensities and deep white matter hyperintensities on T2-weighted MRI scans using the Fazekas scale (total score 0-6), rated for the right hemisphere only.
assessment:
- Fazekas scale
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Basilakos2019
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study tested leukoaraiosis severity as a predictor for both initial aphasia severity and longitudinal change in aphasia severity. For initial severity, it found no significant effect. For longitudinal change, it found a significant association where higher severity predicted decline.
    bucket: predictors
    entity_id: leukoaraiosis_severity
    name: leukoaraiosis severity
    kind: predictor
    predictor_type: imaging_metric
    definition: Visual rating of periventricular hyperintensities and deep white matter hyperintensities on T2-weighted MRI scans using the Fazekas scale (total score 0-6), rated for the right hemisphere only.
    assessment:
    - Fazekas scale
    target: initial_aphasia_severity
    target_kind: impairment
    claim: Leukoaraiosis severity was not a significant predictor of initial aphasia severity in the chronic stage.
    direction: no_effect
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: 35
    population: Individuals in the chronic stage of recovery after a single-event left-hemisphere stroke (middle cerebral artery territory) with aphasia
    timing: Initial evaluation at mean 36.4 months poststroke (range 6-202 months)
    qualifications:
    - Analysis was part of a regression model that also included lesion volume and time poststroke at initial evaluation
    - Lesion volume and time post-stroke at initial assessment were identified as the best predictors of initial aphasia severity
    limitations:
    - Small sample size
    - Retrospective study
    - Unable to control for factors influencing leukoaraiosis such as diabetes, atherosclerotic disease, or hypertension
    - Male-dominated sample (approximately 3:1 ratio)
    - Mean stroke age was relatively young (55.5 years)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S1-C3
      supports: claim
    - source_id: P2-S3-C1
      supports: sample
    - source_id: P2-S3-C3
      supports: sample
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P3-S1-C13
      supports: method
    - source_id: P3-S2-C2
      supports: method
    - source_id: P5-S1-C1
      supports: method
    - source_id: P10-S1-C2
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
    proposal: R002
    status: failed
    reason: Target kind conflicts with existing KB concept
    material_issues: []
    seconds_this_run: 0.0518714589998126
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      original_mapping_sha256: 812bc0cbbd03baf7698e73c39d107d3b37314bd3d73d5e5c35339abd1d230d78
      original_status_sha256: e5972e34555621e41512b1cd62e5530679fe7f3520512fe1bcbf2ad4b9dcfd73
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
