---
id: left_ifof_fd
name: left IFOF fiber density
kind: tract
findings:
- id: f1
  target: word_level_comprehension
  target_kind: impairment
  claim: Mean fractional anisotropy (FA) of the left IFOF showed only a trend-level positive correlation with word-level comprehension (r=0.540, p=0.007), which did not meet the study’s Bonferroni-corrected significance threshold.
  direction: mixed
  relationship: correlational
  method: DTI
  sample:
    n: 29
    population: 29 participants with early subacute post-stroke aphasia
    phase: not_reported
    time_post_onset: Early subacute stage; mean 13.2 days after stroke.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - heterogeneity of aphasia symptom profiles
  - template-based tractography may not fully capture inter-individual variability in tract morphology
  - relatively small number of diffusion directions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient diffusion-derived tensor FA extracted within tract masks. Reference masks define measurement locations; lesion overlap is not the exposure. Within-patient language association; preserve corrected versus trend-level inference. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Reconstructed the selected analysis from original Results and Methods. Corrected the actual patient measurement, group/within-patient denominator, statistical interpretation and evidence links; original failed mapping retained. No independent model or human approval is asserted.'
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
  citation: '@Zhang2021'
  source_passages:
  - section: Original source P5-S1-C4
    page: 5
    quote: "Age, sex, education level, whole-brain averaged values, lesion vol­\nume, and cortical involvement of lesion were considered as nuisance \ncovariates for the results."
    supports: confounders
  - section: Original source P9-S2-C3
    page: 9
    quote: "The relatively small sample size reduced \nstatistical power and precluded the investigation of subgroup differ­\nences."
    supports: limitation
  - section: Original source P9-S2-C4
    page: 9
    quote: "Template-based tractography may lead to insufficient capture of \ninter-individual variability in tract morphology for the patients with \nstroke."
    supports: limitation
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      NeuroImage: Clinical 31 (2021) 102774

      6

      naming subdomain: r = 0.673, p < 0.001), and only a trend-level cor­

      relation was reported with word-level comprehension (r = 0.540, p =

      0.007).'
    supports: claim
  - section: Original source P4-S1-C8
    page: 4
    quote: "Tract-wise metrics \nGiven that most tracts in the language network consist of long-range \nfibers, atlas-based tract-wise metrics were extracted to measure the \naverage features along the whole course of specific tracts of interest \n(TOIs) and complement whole-brain analyses."
    supports: method
  - section: Original source P4-S1-C13
    page: 4
    quote: "We chose seven dual- \nstream tracts (the SLF III, AF, IFOF, UF, ILF, MdLF, and frontal aslant \ntract) as TOIs defined by XTRACT, a novel automated tractography \nprotocol (see detailed techniques in Supplemental Method 2) (War­\nrington et al., 2020)."
    supports: method
  - section: Original source P4-S1-C15
    page: 4
    quote: "For complementary information, we also extracted average \ntensor-derived metric FA from voxel masks of TOIs for between-group \ncomparisons."
    supports: method
  - section: Original source P2-S4-C3
    page: 2
    quote: "Eligibility criteria included a history \nof initial left-hemisphere ischemic stroke during the early subacute stage \n(7 days to 1 month), aphasia confirmed by the language scale, age \n18–80 years, right-handedness, Chinese as a first language, and educa­\ntion experience ≥6 years."
    supports: sample
  - section: Original source P2-S4-C9
    page: 2
    quote: "The final cohort \nconsisted of 62 participants (29 patients, 33 healthy controls)."
    supports: sample
  design: cross-sectional
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2021
  proposal_id: R026
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study found a significant positive correlation between the mean fiber density (FD) of the left IFOF and word-level comprehension in subacute stroke patients. The analysis used a specific fiber-based metric (FD) extracted from a tract-based mask (IFOF) defined by the XTRACT protocol.
    bucket: predictors
    entity_id: left_ifof_fd
    name: left IFOF fiber density
    kind: tract
    predictor_type: imaging_metric
    definition: mean fiber density (FD) extracted from the left inferior fronto-occipital fasciculus (IFOF) using a mask defined by the XTRACT automated tractography protocol
    assessment:
    - Aphasia Battery of Chinese
    target: word_level_comprehension
    target_kind: impairment
    claim: the mean fiber density of the left IFOF significantly positively correlated with word-level comprehension
    direction: likely
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 29
    population: patients with post-stroke aphasia
    timing: subacute stage (7 days to 1 month post-stroke)
    qualifications:
    - Spearman's partial correlation analysis was used
    - adjusted for nuisance covariates including age, sex, education level, whole-brain averaged values, lesion volume, and cortical involvement of lesion
    - significance threshold adjusted by Bonferroni correction
    limitations:
    - small sample size
    - heterogeneity of aphasia symptom profiles
    - template-based tractography may not fully capture inter-individual variability in tract morphology
    - relatively small number of diffusion directions
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S3-C12
      supports: claim
    - source_id: P4-S1-C13
      supports: method
    - source_id: P2-S4-C3
      supports: sample
    - source_id: P5-S1-C2
      supports: method
    - source_id: P5-S1-C4
      supports: confounders
    - source_id: P2-S4-C9
      supports: sample
    - source_id: P9-S2-C3
      supports: limitation
    - source_id: P9-S2-C4
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
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      review_sha256: 8efc3be14543c82d88880d3628246940c8e3eac12b049709f9762e1be5b31371
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
    proposal: R026
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 48.891388415999245
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      original_mapping_sha256: 7ea4c083a3f74ff8f6bb0bf4481c539f143848fd4989ead789608b6defd417f8
      original_status_sha256: b6b79ef98296090ac8ec59cb1ee15caff07791c31bb668d92d7038dd8a6db10b
      evidence_sha256: 65a019b43630701d56116193a78d33cedb3d08b15eee6269ebdd455df7bae894
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
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
      note: Reconstructed the selected analysis from original Results and Methods. Corrected the actual patient measurement, group/within-patient denominator, statistical interpretation and evidence links; original failed mapping retained. No independent model or human approval is asserted.
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
  note: Reconstructed the selected analysis from original Results and Methods. Corrected the actual patient measurement, group/within-patient denominator, statistical interpretation and evidence links; original failed mapping retained. No independent model or human approval is asserted.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
