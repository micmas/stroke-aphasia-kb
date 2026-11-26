---
id: left_ifof_fd
name: left IFOF FD
kind: tract
findings:
- id: f1
  target: color_naming
  target_kind: impairment
  claim: Mean fiber density (FD) of the left IFOF had a positive, trend-level association with color naming (r=0.542, p=0.007), which did not meet the study’s Bonferroni-corrected significance threshold.
  direction: mixed
  relationship: correlational
  method: FBA
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
  - template-based tractography may not capture inter-individual variability
  - heterogeneity of aphasia profiles
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient diffusion-derived fixel metrics FD, FC and/or FDC, at the fixel or tract level specified in the claim. Reference masks define measurement locations; lesion overlap is not the exposure. Within-patient language association; preserve corrected versus trend-level inference. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Reconstructed the selected analysis from original Results and Methods. Corrected the actual patient measurement, group/within-patient denominator, statistical interpretation and evidence links; original failed mapping retained. No independent model or human approval is asserted.'
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
  - section: Original source P9-S1-C13
    page: 9
    quote: "Despite above promising \nadvantages, the present study was limited by the heterogeneity of the \nsymptoms of aphasia profiles."
    supports: limitation
  - section: Original source P5-S3-C15
    page: 5
    quote: "In addition, the mean FD of the IFOF was \nalso correlated with responsive naming subdomain (r = 0.600, p =\n0.002), and exhibited trend-level positive correlation with a color \n"
    supports: claim
  - section: Original source P5-S4-C2
    page: 5
    quote: "In addition, the mean FD of the IFOF was \nalso correlated with responsive naming subdomain (r = 0.600, p =\n0.002), and exhibited trend-level positive correlation with a color \nnaming (r = 0.542, p = 0.007)."
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
  proposal_id: R024
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis examines the correlation between the mean fiber density (FD) of the left inferior fronto-occipital fasciculus (IFOF) and color naming performance in subacute stroke patients. The source explicitly reports a 'trend-level positive correlation' for this specific subdomain.
    bucket: predictors
    entity_id: left_ifof_fd
    name: left IFOF FD
    kind: tract
    predictor_type: imaging_metric
    definition: patient lesion overlap with a population/reference tract template (XTRACT) to calculate mean fiber density (FD) using fixel-based analysis
    assessment:
    - Aphasia Battery of Chinese
    target: color_naming
    target_kind: impairment
    claim: the mean FD of the left IFOF exhibited a trend-level positive correlation with the color naming subdomain
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: 29
    population: patients with post-stroke aphasia
    timing: subacute stage (7 days to 1 month post-stroke)
    qualifications:
    - trend-level correlation
    - Spearman's partial correlation used
    - adjusted for age, sex, education level, whole-brain averaged values, lesion volume, and cortical involvement of lesion
    limitations:
    - small sample size
    - template-based tractography may not capture inter-individual variability
    - heterogeneity of aphasia profiles
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S4-C2
      supports: claim
    - source_id: P4-S1-C13
      supports: method
    - source_id: P2-S4-C3
      supports: sample
    - source_id: P5-S1-C2
      supports: method
    - source_id: P5-S1-C4
      supports: confounders
    - source_id: P9-S2-C3
      supports: limitation
    - source_id: P9-S2-C4
      supports: limitation
    - source_id: P9-S1-C13
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
    proposal: R024
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 51.85343370802002
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      original_mapping_sha256: 134a6c969e1b93bffee3ffcefca82463ca4ca11998165c9c00efc81ddbe722aa
      original_status_sha256: c81f7f4e0328a0a548a33e10e57f6b0653ff70c8ab8a946c0dac09b955348769
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
