---
id: ba22_necrosis_disconnection_model
name: BA 22 necrosis and disconnection model
kind: predictor
findings:
- id: f1
  target: comprehension_of_sequential_commands
  target_kind: impairment
  claim: The authors report a BA22 necrosis/disconnection model associated with sequential-command comprehension (F=3.05, p=.047); disconnection p=.01 and necrosis p=.43. Methods mention Bonferroni adjustment, but the main text does not establish how this nominal p=.047 met that adjusted threshold.
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 39
    population: Right-handed individuals with chronic aphasia following a left hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: At least six months post-stroke; behavioral testing and MRI scanning performed concurrently at enrollment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The method does not account for physiological asymmetries between hemispheres
  - Results are subject to the technical limitations of MRI tractography
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A combined model consisting of the percentage of necrotic damage to Brodmann area 22 and the percentage of fiber reduction (disconnection) of BA 22, measured via T1-weighted MRI and deterministic fiber tractography. The association was determined using multiple linear regression with a stepwise approach; Necrosis was not an independent predictor of comprehension within the model. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified patient-specific MRI/DTI-space connectome reconstruction and deterministic tractography, with left/right connectivity comparison. Reference labels define cortical ROIs; they are not substitutes for patient diffusion measurements. Models combine regional necrosis and connectivity, with physiological hemispheric-asymmetry limitations. The article reports n=39 despite sex counts summing to 38. Nominal reported P values are retained; the precise multiplicity-adjustment
    implementation is not resolved from the main text.'
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
  citation: '@Bonilha2014'
  source_passages:
  - section: Original source P5-S1-C9
    page: 5
    quote: "We also \nobserved a significant relationship between comprehension and a model composed by BA \n22 necrosis and BA 22 disconnection (F=3.05, p=0.047; necrosis: β=−0.35; p=0.43; \ndisconnection β=47; p=0.01)."
    supports: claim
  - section: Original source P5-S1-C10
    page: 5
    quote: "However, in this model, necrosis was not independently \nassociated with comprehension."
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: "Methods\nSubjects\nWe studied thirty-nine individuals (mean age 62.7 ±12.8 years, 22 male, 16 female) who \nsuffered a left hemisphere ischemic stroke at least six months prior to enrolling in this study \n(Table I in the Online Data Supplement)."
    supports: sample
  - section: Original source P1-S1-C6
    page: 1
    quote: "Deterministic fiber tractography was employed to assess \nconnectivity between each possible pair of cortical Brodmann areas (BA)."
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: "Statistical Analyses\nWe performed multiple linear regression analyses with the performance on naming measures \ndefined as the dependent variable, with the following independent variables: 1) percentage \nof damage to each BA area, 2) percentage number of fibers of each BA area."
    supports: method
  - section: Original source P4-S1-C2
    page: 4
    quote: "It should be noted that this method does not take into consideration physiological \nasymmetries between hemispheres."
    supports: limitation
  - section: Original source P6-S2-C3
    page: 6
    quote: "Nevertheless, the results should be interpreted in the context of limitations of MRI \ntractography.\n2) Cortical disconnection and naming performance\nWe demonstrated that naming performance is associated with preservation of cortical \nintegrity and cortical connectivity of BA 45."
    supports: limitation
predictor_type: imaging_metric
short_definition: A combined model consisting of the percentage of necrotic damage to Brodmann area 22 and the percentage of fiber reduction (disconnection) of BA 22, measured via T1-weighted MRI and deterministic fiber tractography.
assessment:
- Western Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Bonilha2014
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis evaluates the relationship between a combined model of BA 22 necrosis and disconnection and the comprehension of sequential commands in chronic stroke patients.
    bucket: predictors
    entity_id: ba22_necrosis_disconnection_model
    name: BA 22 necrosis and disconnection model
    kind: predictor
    predictor_type: imaging_metric
    definition: A combined model consisting of the percentage of necrotic damage to Brodmann area 22 and the percentage of fiber reduction (disconnection) of BA 22, measured via T1-weighted MRI and deterministic fiber tractography.
    assessment:
    - Western Aphasia Battery
    target: comprehension_of_sequential_commands
    target_kind: impairment
    claim: A model composed of BA 22 necrosis and BA 22 disconnection was significantly associated with the comprehension of sequential commands, although necrosis alone was not independently associated with this outcome.
    direction: likely
    method: tractography
    relationship: correlational
    therapy: null
    sample_n: 39
    population: Right-handed individuals with chronic aphasia following a left hemisphere ischemic stroke
    timing: At least six months post-stroke; behavioral testing and MRI scanning performed concurrently at enrollment
    qualifications:
    - The association was determined using multiple linear regression with a stepwise approach
    - Necrosis was not an independent predictor of comprehension within the model
    limitations:
    - The method does not account for physiological asymmetries between hemispheres
    - Results are subject to the technical limitations of MRI tractography
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S1-C9
      supports: claim
    - source_id: P5-S1-C10
      supports: claim
    - source_id: P2-S2-C5
      supports: sample
    - source_id: P1-S1-C6
      supports: method
    - source_id: P4-S1-C7
      supports: method
    - source_id: P4-S1-C2
      supports: limitation
    - source_id: P6-S2-C3
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
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      review_sha256: 79aef69c5137295615c00df451eafe7866bae6eda751eb63b2031edf5d888210
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
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P5-S1-C9
    seconds_this_run: 0.007966041001054691
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      original_mapping_sha256: 74cfce57fd993c78aafa938926a034aed024fc75b7202c53f156316bf3208332
      original_status_sha256: e1a748c9fd6ead59d767a75e034fee6c77f27e22d22a00fce367166b36aa72b1
      evidence_sha256: 5f982698067ca57372749c457eab482e4e80e81dff21e4362d2a0bcddeb15247
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
      note: Verified patient-specific MRI/DTI-space connectome reconstruction and deterministic tractography, with left/right connectivity comparison. Reference labels define cortical ROIs; they are not substitutes for patient diffusion measurements. Models combine regional necrosis and connectivity, with physiological hemispheric-asymmetry limitations. The article reports n=39 despite sex counts summing to 38. Nominal reported P values are retained; the precise multiplicity-adjustment implementation is not resolved from the main text.
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
  note: Verified patient-specific MRI/DTI-space connectome reconstruction and deterministic tractography, with left/right connectivity comparison. Reference labels define cortical ROIs; they are not substitutes for patient diffusion measurements. Models combine regional necrosis and connectivity, with physiological hemispheric-asymmetry limitations. The article reports n=39 despite sex counts summing to 38. Nominal reported P values are retained; the precise multiplicity-adjustment implementation is not resolved from the main text.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
