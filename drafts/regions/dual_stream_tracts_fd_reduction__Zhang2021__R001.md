---
id: dual_stream_tracts_fd_reduction
name: dual-stream tracts cluster
kind: network
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: In the comparison of participants classified as having post-stroke aphasia with healthy controls, patients with post-stroke aphasia exhibited significant fixel-wise fiber density (FD) reductions in dual-stream tracts, including the left inferior fronto-occipital fasciculus (IFOF), arcuate fasciculus, and superior longitudinal fasciculus (SLF) III. This is a between-group imaging contrast, not a correlation with language severity. Adding motor dysfunction as a covariate mainly restricted the FD reductions to dual-stream tracts.
  direction: likely
  relationship: correlational
  method: FBA
  sample:
    n: 62
    population: 29 participants classified as having post-stroke aphasia and 33 healthy controls
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
  - Heterogeneity of aphasia symptom profiles
  - Template-based tractography may not fully capture inter-individual variability in stroke patients
  - Cross-sectional design without chronic stage follow-up
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient diffusion-derived fixel metrics FD, FC and/or FDC, at the fixel or tract level specified in the claim. Reference masks define measurement locations; lesion overlap is not the exposure. Between-group imaging comparisons do not establish a correlation with symptom severity. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Reconstructed the selected analysis from original Results and Methods. Corrected the actual patient measurement, group/within-patient denominator, statistical interpretation and evidence links; original failed mapping retained. No independent model or human approval is asserted.'
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
  - section: Original source P5-S1-C15
    page: 5
    quote: "By adding motor dysfunction level as a covariate, the \nsensitivity analysis showed that reduced FD was mainly confined to \ndual-stream tracts (Supplemental Fig. 1)."
    supports: confounders
  - section: Original source P9-S2-C3
    page: 9
    quote: "The relatively small sample size reduced \nstatistical power and precluded the investigation of subgroup differ­\nences."
    supports: limitation
  - section: Original source P9-S1-C13
    page: 9
    quote: "Despite above promising \nadvantages, the present study was limited by the heterogeneity of the \nsymptoms of aphasia profiles."
    supports: limitation
  - section: Original source P9-S2-C4
    page: 9
    quote: "Template-based tractography may lead to insufficient capture of \ninter-individual variability in tract morphology for the patients with \nstroke."
    supports: limitation
  - section: Original source P9-S2-C6
    page: 9
    quote: "Finally, this study did not include follow-up evaluations at the chronic \nstage, and longitudinal changes were not addressed. \n4.5."
    supports: limitation
  - section: Original source P1-S2-C4
    page: 1
    quote: "Results: The aphasic group exhibited significant fixel-wise FD reductions in the dual-stream tracts, including the \nleft inferior fronto-occipital fasciculus (IFOF), arcuate fasciculus, and superior longitudinal fasciculus (SLF) III \n(family-wise-error-corrected p < 0.05)."
    supports: claim
  - section: Original source P5-S1-C13
    page: 5
    quote: "Group-wise comparisons \nWhole-brain FBA revealed reduced FD in aphasia patients compared \nto the controls."
    supports: claim
  - section: Original source P5-S1-C14
    page: 5
    quote: "As shown in Fig. 3A, most regions with fixels showing \nsignificant FD reductions were located within dual-stream tracts (the left \nSLF III, AF, IFOF, MdLF, and ILF), as well as the left anterior thalamic \nradiation, splenium, and radiations of the corpus callosum (FWE-cor­\nrected p < 0.05)."
    supports: claim
  - section: Original source P5-S1-C15
    page: 5
    quote: "By adding motor dysfunction level as a covariate, the \nsensitivity analysis showed that reduced FD was mainly confined to \ndual-stream tracts (Supplemental Fig. 1)."
    supports: claim
  - section: Original source P3-S1-C11
    page: 3
    quote: "DWI pre-processing and CSD modelling \nThe DWI data were processed using a single-tissue CSD pipeline \n(Tournier et al., 2007) that included multiple pre-processing steps in \nMRtrix3 (v3.0.0) (www.mrtrix.org) (Tournier et al., 2019)."
    supports: method
  - section: Original source P3-S2-C11
    page: 3
    quote: "FD, FC, and FDC were then obtained to detect fiber-specific white \nmatter pathologies in crossing-fiber regions with greater sensitivity and \ninterpretability than tensor-derived metrics (Raffelt et al., 2017). \n2.5.2."
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
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a significant reduction in fiber density (FD) within specific dual-stream tracts in patients with post-stroke aphasia compared to healthy controls using fixel-based analysis (FBA).
    bucket: regions
    entity_id: dual_stream_tracts_fd_reduction
    name: dual-stream tracts cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with a population/reference tract template was not the primary analysis; instead, whole-brain fixel-based analysis (FBA) was used to measure fiber density (FD) in the left inferior fronto-occipital fasciculus (IFOF), arcuate fasciculus (AF), superior longitudinal fasciculus (SLF) III, middle longitudinal fasciculus (MdLF), and inferior longitudinal fasciculus (ILF).
    assessment: []
    target: post_stroke_aphasia
    target_kind: impairment
    claim: Patients with post-stroke aphasia exhibited significant fixel-wise fiber density (FD) reductions in dual-stream tracts, including the left inferior fronto-occipital fasciculus (IFOF), arcuate fasciculus, and superior longitudinal fasciculus (SLF) III.
    direction: likely
    method: VBCM
    relationship: correlational
    therapy: null
    sample_n: 62
    population: Participants with post-stroke aphasia and age- and sex-matched healthy controls
    timing: Subacute stage (7 days to 1 month post-stroke; mean 13.2 days)
    qualifications:
    - Analysis adjusted for age, sex, education level, whole-brain averaged values, lesion volume, and cortical involvement of lesion
    - Sensitivity analysis including motor dysfunction level as a covariate showed reduced FD was mainly confined to dual-stream tracts
    limitations:
    - Small sample size
    - Heterogeneity of aphasia symptom profiles
    - Template-based tractography may not fully capture inter-individual variability in stroke patients
    - Cross-sectional design without chronic stage follow-up
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S2-C4
      supports: claim
    - source_id: P5-S1-C13
      supports: claim
    - source_id: P5-S1-C14
      supports: claim
    - source_id: P2-S4-C9
      supports: sample
    - source_id: P2-S4-C3
      supports: sample
    - source_id: P5-S1-C9
      supports: sample
    - source_id: P5-S1-C4
      supports: confounders
    - source_id: P5-S1-C15
      supports: confounders
    - source_id: P2-S2-C11
      supports: method
    - source_id: P9-S2-C3
      supports: limitation
    - source_id: P9-S1-C13
      supports: limitation
    - source_id: P9-S2-C4
      supports: limitation
    - source_id: P9-S2-C6
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
    proposal: R001
    status: failed
    reason: 'Zhang2021: finding[0] (id=f1): target ''post_stroke_aphasia'' is an aphasia syndrome but the claim is about a symptom; target the symptom entry (anomia, fluency, …) unless the paper classifies by syndrome'
    material_issues: []
    seconds_this_run: 151.1514999580104
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      original_mapping_sha256: fc4047a53506987e0ba021b7e6f6cf6f949052c3f9c4a4238874235752e2cc7b
      original_status_sha256: 3d291e2ad187a4e113498b1332570949f1827cb46c48a3cacbbb3ceca7646410
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
