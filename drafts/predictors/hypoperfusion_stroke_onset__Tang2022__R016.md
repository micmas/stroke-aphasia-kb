---
id: hypoperfusion_stroke_onset
name: hypoperfusion at stroke onset
kind: predictor
findings:
- id: f1
  target: language_related_cortical_thickness
  target_kind: impairment
  claim: the mean cortical thickness of individual clusters identified as relating to language performance was not different between patients with and without hypoperfusion at stroke onset
  direction: no_effect
  relationship: correlational
  method: structural_MRI
  sample:
    n: 32
    population: patients with chronic left subcortical stroke and aphasia
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
  - small number of patients with different perfusion status in subgroup analyses
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: presence of hypoperfusion at stroke onset as measured by perfusion computer tomography or perfusion weighted images. controlled for key variables; post hoc analysis of clusters previously identified as relating to language performance. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Perfusion status was assessed with perfusion CT or perfusion-weighted imaging at stroke onset; the outcome was later FreeSurfer cortical thickness. Correct the exposure type to imaging_metric and method to structural_MRI. Distinguish whole left-hemisphere comparison (R015) from prespecified language-related clusters (R016); n=32, cross-sectional association.'
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
  - section: Original source P7-S2-C2
    page: 7
    quote: 'Comparisons of cortical thickness in

      subgroups with different perfusion

      status

      To explore the impacts of perfusion status on cortical

      thickness, we further compared the diﬀerences in cortical

      thickness between patients without hypoperfusion (NHP) and

      with HP according to perfusion computer tomography or

      perfusion weighted images at stroke onset.'
    supports: method
  - section: Original source P7-S2-C7
    page: 7
    quote: 'A post hoc analysis was performed to

      compare cortical thickness in each cluster identiﬁed as above to

      relate to language performance by controlling for key variables.'
    supports: method
  - section: Original source P7-S2-C8
    page: 7
    quote: 'The results showed that the mean cortical thickness of the

      individual clusters was not diﬀerent between the two subgroups

      (all p > 0.11).'
    supports: claim
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
  - section: Original source P10-S2-C8
    page: 10
    quote: 'Thirdly, the

      number of patients with diﬀerent perfusion status was relatively

      small in the subgroup analyses, which also restricted the

      generalization of the conclusions.'
    supports: limitation
predictor_type: imaging_metric
short_definition: presence of hypoperfusion at stroke onset as measured by perfusion computer tomography or perfusion weighted images
assessment:
- Perfusion CT or perfusion-weighted imaging at stroke onset
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Tang2022
  proposal_id: R016
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis compares cortical thickness in language-related clusters between patients with and without hypoperfusion at stroke onset, finding no significant difference.
    bucket: predictors
    entity_id: hypoperfusion_stroke_onset
    name: hypoperfusion at stroke onset
    kind: predictor
    predictor_type: clinical
    definition: presence of hypoperfusion at stroke onset as measured by perfusion computer tomography or perfusion weighted images
    assessment: []
    target: language_related_cortical_thickness
    target_kind: impairment
    claim: the mean cortical thickness of individual clusters identified as relating to language performance was not different between patients with and without hypoperfusion at stroke onset
    direction: no_effect
    method: VBM
    relationship: correlational
    therapy: null
    sample_n: 32
    population: patients with chronic left subcortical stroke and aphasia
    timing: over 6 months after stroke
    qualifications:
    - controlled for key variables
    - post hoc analysis of clusters previously identified as relating to language performance
    limitations:
    - small number of patients with different perfusion status in subgroup analyses
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S2-C2
      supports: method
    - source_id: P7-S2-C7
      supports: method
    - source_id: P7-S2-C8
      supports: claim
    - source_id: P2-S2-C11
      supports: sample
    - source_id: P10-S2-C8
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
    proposal: R016
    status: failed
    reason: 'Tang2022: predictor_type=''clinical'' requires assessment (non-empty list of test names)'
    material_issues: []
    seconds_this_run: 66.91522225001245
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      original_mapping_sha256: eec6361583048bf5110c9efc671d1b6cbcf82e8c759f53f19bfab2b9dac661dc
      original_status_sha256: 93a274fba683695f30e8d9c831e7816953f3d1c1a2387e70b76e2fd61adbcef1
      evidence_sha256: 5cb0d53826e6994543e881497cc8f6c9b8d54198b90f7bddefb41e14edee776e
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 4
      - 7
      - 10
      note: Perfusion status was assessed with perfusion CT or perfusion-weighted imaging at stroke onset; the outcome was later FreeSurfer cortical thickness. Correct the exposure type to imaging_metric and method to structural_MRI. Distinguish whole left-hemisphere comparison (R015) from prespecified language-related clusters (R016); n=32, cross-sectional association.
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
  note: Perfusion status was assessed with perfusion CT or perfusion-weighted imaging at stroke onset; the outcome was later FreeSurfer cortical thickness. Correct the exposure type to imaging_metric and method to structural_MRI. Distinguish whole left-hemisphere comparison (R015) from prespecified language-related clusters (R016); n=32, cross-sectional association.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
