---
id: gender__Coppens2002__R003
name: gender
kind: review
findings:
- id: f1
  target: ca_symptomatology
  target_kind: impairment
  claim: Coppens2002 reports from its analysis of published cases that there were no significant differences between males and females in terms of crossed aphasia symptomatology, including CA subtype, frequency of oral/written language skill discrepancy, apraxia distribution, or presence of neglect.
  direction: no_effect
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously published crossed-aphasia cases analysed by the review; analysis-specific denominators differ.
    phase: not_reported
    time_post_onset: diagnosis preferentially taken from the subacute period (3 weeks to 2 months postonset)
  statistics:
    threshold: See source passages for the review’s case-level statistical analysis; not a new cohort.
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - nonstandardized character of published case descriptions
  - variation in level of detail and time post onset across reports
  - some aphasia labels based on text interpretation of older case studies
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators. Source repair (unapproved): Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.'
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
  citation: '@Coppens2002'
  source_passages:
  - section: Original source P17-S2-C15
    page: 17
    quote: 'There were no diﬀerences between males and females for the CA

      subtype (Yates corrected v2: 1.56, df ¼ 1, p ¼ :212), the frequency of a discrepancy

      P.'
    supports: claim
  - section: Original source P18-S1-C1
    page: 18
    quote: '

      between oral and written skills (Pearson v2 ¼ 0.27, df ¼ 2, p ¼ :874), the apraxia

      distribution (Pearson v2 ¼ 1.274, df ¼ 4, p ¼ :866), or the presence of neglect (Yates

      corrected v2 ¼ 0.78, df ¼ 1, p ¼ :377).'
    supports: claim
  - section: Original source P27-S2-C6
    page: 27
    quote: 'The results of the gender

      analyses have shown that there are no signiﬁcant diﬀerences between males and

      females in terms of CA symptomatology (refer to Table 2).'
    supports: claim
  - section: Original source P29-S1-C11
    page: 29
    quote: 'The limitations of this review are inherent to the nonstandardized character of

      published CA case descriptions.'
    supports: limitation
  - section: Original source P17-S2-C12
    page: 17
    quote: 'The overall data set was statistically analyzed based on several deﬁning features:

      gender, familial sinistrality, CA subtype (i.e., mirror-image vs. anomalous), and

      aphasia type.'
    supports: method
  - section: Original source P17-S1-C11
    page: 17
    quote: 'Male subjects accounted for 66.1% of the cases and females for

      33.9% (n ¼ 165).'
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Coppens2002
  proposal_id: R003
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study analyzed the relationship between gender and various symptoms of crossed aphasia (CA) in a review of 165 cases, finding no significant differences in symptom distribution between males and females.
    bucket: predictors
    entity_id: gender
    name: gender
    kind: classical
    predictor_type: demographic
    definition: patient gender (male vs female)
    assessment: []
    target: ca_symptomatology
    target_kind: impairment
    claim: There were no significant differences between males and females in terms of crossed aphasia symptomatology, including CA subtype, frequency of oral/written language skill discrepancy, apraxia distribution, or presence of neglect.
    direction: no_effect
    method: meta-analysis
    relationship: correlational
    therapy: null
    sample_n: 165
    population: patients with crossed aphasia (CA)
    timing: diagnosis preferentially taken from the subacute period (3 weeks to 2 months postonset)
    qualifications:
    - analysis included CA subtype (mirror-image vs anomalous)
    - analysis included discrepancy between oral and written language skills
    - analysis included apraxia distribution
    - analysis included presence of neglect
    limitations:
    - nonstandardized character of published case descriptions
    - variation in level of detail and time post onset across reports
    - some aphasia labels based on text interpretation of older case studies
    optional_pending: []
    evidence_quality: meta-analysis
    passages:
    - source_id: P17-S2-C12
      supports: method
    - source_id: P17-S2-C15
      supports: claim
    - source_id: P18-S1-C1
      supports: claim
    - source_id: P27-S2-C6
      supports: claim
    - source_id: P5-S2-C3
      supports: method
    - source_id: P17-S1-C11
      supports: sample
    - source_id: P29-S1-C11
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      review_sha256: 3d3639b15bf67edde5fd481a6aacd66b70c50bd9fcec6baabfc53381f1004181
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
    reason: Truncated output held
    seconds_this_run: 237.64465716599807
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      original_mapping_sha256: 272d870b4ab551a8871795c20004e590e624bc4ac62def267d11060353a750eb
      original_status_sha256: 6c2ac41891ba176b8025ab46ac65cefacbddbd9373e2806d666abd47b52f77b0
      evidence_sha256: 92a0eb9069615cc78286bcf11df00e37aeb7ec79819a55a9fda1e490a5970671
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 5
      - 17
      - 18
      - 27
      note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
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
  note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
