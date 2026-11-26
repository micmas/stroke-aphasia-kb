---
id: left_naming_cortical_cluster
name: left naming cortical cluster
kind: network
findings:
- id: f1
  target: naming_word_finding
  target_kind: impairment
  claim: In 32 patients with chronic left subcortical stroke and history of aphasia, cortical thickness in left inferior precentral/frontal and posterior cingulate clusters was positively associated with naming/word-finding after demographic and lesion-size adjustment. The prose names pars orbitalis; Table 2 names pars opercularis for the left frontal extension.
  direction: likely
  relationship: correlational
  method: structural_MRI
  sample:
    n: 32
    population: patients with chronic left subcortical stroke (ischemic or hemorrhagic) and history of aphasia
    phase: not_reported
    time_post_onset: over 6 months after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - cross-sectional investigation
  - type and dose of speech therapy were not quantified as confounding factors
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: FreeSurfer cortical thickness in left inferior precentral/frontal-opercular and posterior cingulate clusters; the prose and Table 2 disagree about the frontal pars label. analysis controlled for age, education level, time from stroke onset, and lesion size; when cortical thickness measures were added to a hierarchical regression model, this left hemisphere cluster was a significant predictor for naming/word finding. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Adjacent segments complete the selected naming association. Correct method to structural-MRI surface-based cortical thickness regression. Prose says pars orbitalis whereas Table 2 labels the left cluster as inferior precentral extending to pars opercularis; preserve this anatomical source conflict rather than choose silently.'
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
  citation: '@Tang2022'
  source_passages:
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Materials and methods

      Participants

      Thirty-two patients with chronic left subcortical stroke

      (ischemic or hemorrhagic) and history of aphasia were recruited

      with the following inclusion criteria: (i) Native Chinese speakers;

      (ii) over 6 months after stroke; (iii) unilateral subcortical

      lesion; (iv) ability to perform tests; and (v) absence of prior

      diagnosis of neurological disease.'
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: 'Statistical analysis

      To determine cortical thickness association with language

      measures, cortical thickness maps were entered into separate

      multiple

      regression

      analyses

      using

      spontaneous

      speech,

      naming/word

      ﬁnding,

      repetition,

      and

      auditory-verbal

      comprehension as explanatory variables controlling for key

      demographic factors and lesion size as confounding variables.'
    supports: method
  - section: Original source P5-S1-C10
    page: 5
    quote: 'Considering

      the possible impacts of age and time from stroke onset on

      cerebral volume (Nitkunan et al., 2011; Walhovd et al., 2011;

      Brodtmann et al., 2012; Takao et al., 2012), we included age,

      education level, time from stroke onset and lesion size as the

      key nuisances in the separate regression model.'
    supports: confounders
  - section: Original source P10-S2-C2
    page: 10
    quote: 'First,

      this is a cross-sectional investigation that might preclude

      the empirical evidence of remote cortical atrophy mediated

      by neurodegeneration of the connecting ﬁber tracts.'
    supports: limitation
  - section: Original source P10-S2-C11
    page: 10
    quote: 'However, the type and dose of speech therapy are not easily

      quantiﬁable as a confounding factor in the current regression

      analyses.'
    supports: limitation
  - section: Original source P5-S1-C13
    page: 5
    quote: 'As for naming ability,

      cortical thickness in the left inferior precentral gyrus, pars

      orbitalis, and left posterior cingulum was positively related to

      '
    supports: claim
  - section: Original source P5-S2-C2
    page: 5
    quote: 'As for naming ability,

      cortical thickness in the left inferior precentral gyrus, pars

      orbitalis, and left posterior cingulum was positively related to

      the naming/word ﬁnding score (Figures 2Ca,Cd and Table 2).'
    supports: claim
  - section: Original source P7-S1-C2
    page: 7
    quote: 'Tests

      Cluster size

      (mm2)

      Pmax

      Talairach coordinates (mm)

      Anatomical regions

      x

      y

      z

      Multiple regression, Auditory-Verbal Comprehension as predictor (nuisance variables*)

      LH

      803.25

      0.009

      –40.4

      –66.1

      35.3

      Inferior Parietal Gyrus extending to

      Posterior Superior Temporal Gyrus

      Multiple regression, Spontaneous Speech as predictor (nuisance variables*)

      LH

      907.41

      0.004

      –6.2

      54.3

      –16.5

      Medial Orbitofrontal Gyrus extending to

      Lateral Orbitofrontal Gyrus

      Multiple regression, naming/word-ﬁnding as predictor (nuisance variables*)

      LH

      659.04

      0.029

      –37.6

      2.9

      24.4

      Inferior Precentral Gyrus extending to

      Pars Opercularis Gyrus

      641.38

      0.032

      –11.8

      –18.6

      37.4

      Posterior Cingulate Gyrus

      RH

      576.24

      0.045

      41.5

      30.5

      –12.6

      Lateral Orbitofrontal Gyrus extending to

      Pars Orbitalis and Triangularis

      Signiﬁcant clusters in each hemisphere are presented (corrected at vertex-wise P < 0.005 and cluster-wise P < 0.05).'
    supports: claim
  - section: Original source P7-S1-C3
    page: 7
    quote: 'LH, left hemisphere; RH, right hemisphere.

      *Nuisance variables include age, education level, time post stroke and lesion size.

      each cluster as a dependent variable.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Tang2022
  proposal_id: R003
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identified a specific left-hemisphere cortical cluster (inferior precentral gyrus, pars orbitalis, and posterior cingulum) where cortical thickness was positively associated with naming/word finding scores in patients with chronic left subcortical stroke, controlling for age, education, time since stroke, and lesion size.
    bucket: regions
    entity_id: left_naming_cortical_cluster
    name: left naming cortical cluster
    kind: network
    predictor_type: imaging_metric
    definition: cortical thickness in the left inferior precentral gyrus, pars orbitalis, and left posterior cingulum measured by FreeSurfer
    assessment:
    - Western Aphasia Battery-Revised
    target: naming_word_finding
    target_kind: impairment
    claim: cortical thickness in the left inferior precentral gyrus, pars orbitalis, and left posterior cingulum was positively related to the naming/word finding score
    direction: likely
    method: VBM
    relationship: correlational
    therapy: null
    sample_n: 32
    population: patients with chronic left subcortical stroke (ischemic or hemorrhagic) and history of aphasia
    timing: over 6 months after stroke
    qualifications:
    - analysis controlled for age, education level, time from stroke onset, and lesion size
    - when cortical thickness measures were added to a hierarchical regression model, this left hemisphere cluster was a significant predictor for naming/word finding
    limitations:
    - cross-sectional investigation
    - type and dose of speech therapy were not quantified as confounding factors
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S2-C2
      supports: claim
    - source_id: P2-S2-C11
      supports: sample
    - source_id: P4-S1-C11
      supports: method
    - source_id: P5-S1-C10
      supports: confounders
    - source_id: P5-S2-C8
      supports: claim
    - source_id: P10-S2-C2
      supports: limitation
    - source_id: P10-S2-C11
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
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      review_sha256: 31adbe281ea00eb7ba313dc37b9789f34a6b2f52ed43da11ad670c7faba52750
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
    reason: No primary evidence for the selected analysis
    seconds_this_run: 43.02029833299457
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      original_mapping_sha256: ba19cdc51fe5d6c9a23ad519fcd23a0bb6afb4bb5262e04fa200aec3e25613f8
      original_status_sha256: 4f0e5ff7e551243c1170002fea6b8ad3d81b7b41c189d67ab86716609d14d37b
      evidence_sha256: 5cb0d53826e6994543e881497cc8f6c9b8d54198b90f7bddefb41e14edee776e
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 4
      - 5
      - 7
      - 10
      note: Adjacent segments complete the selected naming association. Correct method to structural-MRI surface-based cortical thickness regression. Prose says pars orbitalis whereas Table 2 labels the left cluster as inferior precentral extending to pars opercularis; preserve this anatomical source conflict rather than choose silently.
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
  note: Adjacent segments complete the selected naming association. Correct method to structural-MRI surface-based cortical thickness regression. Prose says pars orbitalis whereas Table 2 labels the left cluster as inferior precentral extending to pars opercularis; preserve this anatomical source conflict rather than choose silently.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
