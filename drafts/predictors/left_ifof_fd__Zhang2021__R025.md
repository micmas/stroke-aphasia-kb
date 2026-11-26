---
id: left_ifof_fd
name: left IFOF FD
kind: tract
findings:
- id: f1
  target: naming_performance
  target_kind: impairment
  claim: Mean fractional anisotropy (FA), rather than fiber density, in the left IFOF was positively associated with total naming (r=0.680, p<0.001) and picture naming (r=0.673, p<0.001).
  direction: likely
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
  - Small sample size
  - Template-based tractography may not fully capture inter-individual variability in tract morphology
  - Heterogeneity of aphasia symptom profiles
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
  - section: Original source P5-S4-C3
    page: 5
    quote: "Compared to the mean FD, the signifi­\ncant correlations with tract-wise mean FA of the left IFOF were found \nwithin naming domain (total naming score: r = 0.680, p < 0.001; picture \nTable 1 \nDemographic characteristics and medical information of participants (n = 62).   \nAphasia \nPatients \nHealthy \nControls \nStatistic  \nn = 29 \nn = 33  \nSex, male (%) \n21 (72.4) \n19 (57.6) \nχ2(1) = 1.484, P \n= 0.223 \nAge, years (SD) \n59.2 (12.3) \n54.6 (13.1) \nt(60) = 1.442, P \n= 0.155 \nEducation, years (SD) \n10.0 (3.7) \n10.4 (4.2) \nZ = -0.512*, P =\n0.609 \nTime post-stroke, days (SD) \n13.2 (7.3) \n– \n– \nHandedness, right (%) \n29 (100) \n33 (100) \n– \nICV, cm3 (SD) \n1549.5 \n(155.0) \n1482.2 \n(136.2) \nt(60) = 1.822, P \n= 0.073 \nLesion volume, mL (SD) \n52.7 (48.8) \n– \n– \nCortical involvement of \nlesion, % (SD) \n53.8 (26.4) \n– \n– \nNotes: Data are shown as mean (SD) or number (%). Reported P-values from two- \nsample independent t-test for age and intracranial\
      \ volume, Mann-Whitney U test \nfor the non-normal variable education year, and chi-squared test for male pro­\nportion and handedness. ICV = intracranial volume; SD = standard deviation. *: \nZ value was reported for Mann-Whitney U test. \nJ. Zhang et al.                                                                                                                                                                                                                                   \n\n"
    supports: claim
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
  proposal_id: R025
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis of tract-wise mean fiber density (FD) in the left IFOF shows a significant positive correlation with total naming and picture naming scores in subacute stroke patients.
    bucket: predictors
    entity_id: left_ifof_fd
    name: left IFOF FD
    kind: tract
    predictor_type: imaging_metric
    definition: Patient lesion overlap with a population/reference tract template (XTRACT) to extract the mean fiber density (FD) of the left inferior fronto-occipital fasciculus.
    assessment:
    - Aphasia Battery of Chinese
    target: naming_performance
    target_kind: impairment
    claim: The mean fiber density (FD) of the left inferior fronto-occipital fasciculus (IFOF) is significantly and positively associated with the total naming score and the picture naming subdomain.
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: 29
    population: patients with post-stroke aphasia
    timing: subacute stage (7 days to 1 month post-stroke)
    qualifications:
    - Analysis used Spearman's partial correlation
    - Significance threshold adjusted by Bonferroni correction
    - Adjusted for age, sex, education level, whole-brain averaged values, lesion volume, and cortical involvement of lesion
    limitations:
    - Small sample size
    - Template-based tractography may not fully capture inter-individual variability in tract morphology
    - Heterogeneity of aphasia symptom profiles
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S3-C14
      supports: claim
    - source_id: P2-S4-C3
      supports: sample
    - source_id: P4-S1-C13
      supports: method
    - source_id: P5-S1-C2
      supports: method
    - source_id: P5-S1-C4
      supports: confounders
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
    proposal: R025
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 55.76497954101069
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      original_mapping_sha256: a310e19e6f68256b08d4be0fe5dd13c498e8731bcfebc2eea421bbccd2b807cf
      original_status_sha256: da254d9bcc82b7dd3f2e0ef806aa8d1946918b6652d2b3f50e2f273f1fba323c
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
