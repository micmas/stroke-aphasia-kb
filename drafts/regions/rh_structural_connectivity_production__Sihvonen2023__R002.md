---
id: rh_structural_connectivity_production
name: right hemisphere structural connectivity cluster
kind: network
findings:
- id: f1
  target: language_production
  target_kind: impairment
  claim: Higher spoken language production t-scores were associated with lower QA
    in segments of the right corticospinal tract, thalamic radiation, and inferior
    longitudinal fasciculus.
  direction: unlikely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: patients with aphasia after a left hemispheric stroke
    phase: not_reported
    time_post_onset: early subacute stage (2-6 weeks poststroke); concurrent association
      between imaging and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (n=22)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient right hemisphere white matter structural connectivity
    measured by QA (quantitative anisotropy) using connectometry analysis of multi-shell
    diffusion-weighted MRI data. Analysis adjusted for lesion volume and age; Results
    corrected for multiple comparisons (pFDR < .0125). Additional metadata has not
    been transcribed; review the pending-field flags before approval.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-25'
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
    - not_transcribed:sample.n
    - proposed_concept:language_production
  citation: '@Sihvonen2023'
  source_passages:
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Higher production t-scores were associated with lower QA in seg-

      ments of the right corticospinal tract, thalamic radiation, and inferior

      longitudinal fasciculus (Figure 1b) (pFDR < .0125).'
    supports: claim
  - section: Original source P3-S1-C3
    page: 3
    quote: 'Inclusion criteria were: first-

      ever left hemisphere stroke with aphasia as measured by an Aphasia

      Quotient of <93.8 using the Western Aphasia Battery—Revised

      (Kertesz, 2007); availability for an initial assessment at 2–6 weeks

      poststroke onset; medically and cognitively able to participate in a

      research intervention; and English as a dominant language prior to

      their stroke.'
    supports: sample
  - section: Original source P3-S1-C11
    page: 3
    quote: 'An overall score for spoken language

      production was derived from the combination of raw scores from the

      object and verb naming, verbal fluency subtests of the CAT.'
    supports: claim
  - section: Original source P3-S2-C11
    page: 3
    quote: 'The restricted diffusion was

      quantified using restricted diffusion imaging (Yeh et al., 2017), and QA

      was extracted as the local connectome fingerprint (Yeh, Vettel,

      et al., 2016) and used in the connectometry analysis.

      2.4

      |

      Connectometry analysis

      Diffusion MRI connectometry (Yeh, Badre, et al., 2016) analysis was

      carried out using DSI Studio.'
    supports: method
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Lesion volume and age

      were included as covariates in all models.'
    supports: confounders
  - section: Original source P2-S3-C1
    page: 2
    quote: 'Badre, et al., 2016) based on multi-shell dMRI data acquired at the

      early subacute stage and language production and comprehension

      assessments at both the early subacute (2–6 weeks) and chronic

      (>6 months) poststroke stages (Table 1).'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Sihvonen2023
  proposal_id: R002
  review_status_sha256: 7258fc9d7d103badf2645bb78c508a4aaa5aca2630715beae44f67bbb948fdb9
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
        A/passages.json: 68aecb48a6636dded7c64ad865cf4f598bf35141e9accd4a36c5644830273e97
        A/raw.json: f7196d288ee3c493ae32855cb65f94cd33b2b28214b64ca98c4b5204b11050ce
        A/source-units.json: cd400d71c5392e705490a568033bcd745efd20cd2d86b5b8e77428f6d4993310
        A/full-source-units.json: 1d24300397dbbb040e679198eadb9eaf610192f7e8345790d8bdf099eb08c883
        A/meta.json: ec0ee7ce7f9d34918ccf96e34b8565886005ee83d7fdf7e452da324f8b3727d1
        A/table-images/TABLE-1-page-2-1.png: d78cb24fcd481ffc32013cabef3f7ff3fed8f0cbee9428b7aa3dc86a5fceb95c
        A/table-images/page-2.png: feb06c216a9deaff3ff98814673af1bf7952a506fbb81631be6441da91da46b3
        A/table-images/manifest.json: 725db2790c0eca16eff383a5e2a0debf5ca5a53adfe6e62d7bf2702698765019
        A/clauses/window-03/raw.json: 8a3654fcbd0dbbcba52cfcc4a4730ece699889f8a117b5a7a4aba2681e398c48
        A/clauses/window-03/prompt.txt: 45231d1e7ac40cc02ee4bd9ee33cc8f26e07a324fd5aaf5b050f5e71675fd25f
        A/clauses/window-03/meta.json: 58ceb3f075deb3671740cf8104fd213a0fb5419f1615e31b97672efd7c984ef2
        A/clauses/window-04/raw.json: 93da7ddd7dbfba4b57a2c6db1f3b71e85ecc2988a04416b129b50f92ea0f4072
        A/clauses/window-04/prompt.txt: 7898b50b4a7c08040ffd92980b76d6b02731c05942642577b7c1a2acb222ebb4
        A/clauses/window-04/meta.json: a1963e4f8a923abb7a486d961e150f2624bddcac3bbd3695ec71c82e10b9f82d
        A/clauses/window-05/raw.json: 1b7f0bc771a305b8004f34b305e8148c64548f2aa5df5bdfc4f04c2178ed52be
        A/clauses/window-05/prompt.txt: 05b8f588027c3fb911803a927160fd6129911b2d720bf3d3271afe9e95e59954
        A/clauses/window-05/meta.json: 4b5cf5c6b834315f485ce50e488d39635846f584a9de7597a2225ac1020fddff
        A/clauses/window-02/raw.json: c56ac388a26bdd613242f290940b4411bf319c65d7506ca594aad713b97d9618
        A/clauses/window-02/prompt.txt: b7ff258e2886b69e78b4733c848bb607b01f71fb705d28cb85993bda3d8cb57b
        A/clauses/window-02/meta.json: 40173fbb9e28eb78057641ac553bb743efd0815de34aab4ee0f95a8a0d5030ed
        A/clauses/window-01/raw.json: e68b7d2783db9642ed14718026388d9c1b4110d4cfb925339e74fe99745446f5
        A/clauses/window-01/prompt.txt: 0664a370c520885612f05538bac7561f7302a3044d203cd8f81f87636561ec1f
        A/clauses/window-01/meta.json: 879d771d917d56dcab14e4978f706088efd870cfc22274380b5edf092a109531
        A/tables/TABLE-1-page-2-1/raw.json: 14f34cb028a4e5f1ea1db643182cd1eafdc80c8040ee164dc5d96efadd84bb9e
        A/tables/TABLE-1-page-2-1/prompt.txt: d0b8fc78c25a4a2618fd834ddca2e18f85609e317b75b95160c358bf76e8776d
        A/tables/TABLE-1-page-2-1/meta.json: 5d6bea17678673f9cf170b5030fc6d69e4c1be4ea49e71fd0ed4440bc10f6942
        B/passages.json: 68aecb48a6636dded7c64ad865cf4f598bf35141e9accd4a36c5644830273e97
        B/raw.json: ea4fc88fd1bc8134b754c1ad9914eaf233ffa1675e76428a1d350a0bba613e45
        B/source-units.json: cd400d71c5392e705490a568033bcd745efd20cd2d86b5b8e77428f6d4993310
        B/full-source-units.json: 1d24300397dbbb040e679198eadb9eaf610192f7e8345790d8bdf099eb08c883
        B/meta.json: 8996e509838763b04296d9fc7aa0a5424408955495203b2b07313411a345b461
        B/table-images/TABLE-1-page-2-1.png: d78cb24fcd481ffc32013cabef3f7ff3fed8f0cbee9428b7aa3dc86a5fceb95c
        B/table-images/page-2.png: feb06c216a9deaff3ff98814673af1bf7952a506fbb81631be6441da91da46b3
        B/table-images/manifest.json: d10fd1bbac17f6c5c0f8e4c1bb9ab4132663af24c779a2ef8fc8b43471cda191
        B/clauses/window-03/raw.json: 34a0e484ea5ff9cd093137b64d231f2508a5b3a6e2d747744c20e233152581ce
        B/clauses/window-03/prompt.txt: 45231d1e7ac40cc02ee4bd9ee33cc8f26e07a324fd5aaf5b050f5e71675fd25f
        B/clauses/window-03/meta.json: 900c3a9774e40827ab9e87427300719db5e85bbc6b66e457f902d0814d7010aa
        B/clauses/window-04/raw.json: 2ca4913f64e26ebc1edf6e43fc95ffb798880c7e6e0e774f77b60eee236add7a
        B/clauses/window-04/prompt.txt: 7898b50b4a7c08040ffd92980b76d6b02731c05942642577b7c1a2acb222ebb4
        B/clauses/window-04/meta.json: ad2710535bcc3ca3cdc3fdd683d7686e6660f3a4b9db82ef3a8b7aa71e9542a1
        B/clauses/window-05/raw.json: dae3c040f2e7dd11e59f83fbd562249f29cf4914b519efbd07ffcc2b4ddfc60c
        B/clauses/window-05/prompt.txt: 05b8f588027c3fb911803a927160fd6129911b2d720bf3d3271afe9e95e59954
        B/clauses/window-05/meta.json: 2e7d3afe6eb6c5a2be19bce379e9ed3e89db65369ad03db965d2ef7e3af7f6be
        B/clauses/window-02/raw.json: 8a0a8c43c0aba4f00ab586e19f1092f7e7fe35a9028b28d6688f512bd3500b8a
        B/clauses/window-02/prompt.txt: b7ff258e2886b69e78b4733c848bb607b01f71fb705d28cb85993bda3d8cb57b
        B/clauses/window-02/meta.json: 035cc21323d878f63e2b33887870ac6d2727381358006b19d20461e01f513539
        B/clauses/window-01/raw.json: 72e5d7207cd97f00bef3bcf5210517e4ffce3a50a3dea263aea15211d3d6b501
        B/clauses/window-01/prompt.txt: 0664a370c520885612f05538bac7561f7302a3044d203cd8f81f87636561ec1f
        B/clauses/window-01/meta.json: 3a15daf28d89d917101113d8a3aa9ee61f3ab97470076a3479a17f7769cd29d2
        B/tables/TABLE-1-page-2-1/raw.json: 14f34cb028a4e5f1ea1db643182cd1eafdc80c8040ee164dc5d96efadd84bb9e
        B/tables/TABLE-1-page-2-1/prompt.txt: d0b8fc78c25a4a2618fd834ddca2e18f85609e317b75b95160c358bf76e8776d
        B/tables/TABLE-1-page-2-1/meta.json: 6a0df39f703e6d34ba4f0fc74dc83720aaf65d6aba41aae2943fc1501fdfb5f0
      code:
        relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
        relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
        ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
        strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
      model: gemma4:26b
      model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
      host: http://localhost:11434
      max_output_tokens: 20000
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
      source_review: _compare/relationships-2026-11-16/review-current/Sihvonen2023
      source_status_sha256: 73b6033d15ff7307822e8ab6361ecafb3491c3b36a76771fd49b15e0e49b6b48
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: early subacute stage right hemisphere structural connectivity (QA)
    outcome:
      text: language production
    analysis_label: Cross-sectional connectometry (early subacute stage)
    relation: association
    evidence_ids:
    - P4-S2-C6
    qualifier_ids:
    - P4-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
      source_review: _compare/relationships-2026-11-16/review-current/Sihvonen2023
      source_status_sha256: 73b6033d15ff7307822e8ab6361ecafb3491c3b36a76771fd49b15e0e49b6b48
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C7
      - 'window 4: invalid/duplicate disposition P5-S1-C6'
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S3-C4
      - Result passage disposed without unit P6-S4-C2
      unattached_null_or_qualifier_ids:
      - P5-S1-C7
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 120
      unselected_timing_passages:
      - P1-S1-C11
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C9
      - P4-S1-C9
      - P4-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P1-S1-C11
        - P1-S2-C2
        - P2-S3-C1
        - P3-S1-C7
        - P4-S1-C2
        - P4-S2-C4
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P3-S3-C11
      table_review_required:
      - TABLE-1-page-2-1
      unlinked_tables:
      - TABLE-1-page-2-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
      source_review: _compare/relationships-2026-11-16/review-current/Sihvonen2023
      source_status_sha256: 73b6033d15ff7307822e8ab6361ecafb3491c3b36a76771fd49b15e0e49b6b48
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Abstract restatement of production associations.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Abstract restatement of comprehension associations.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Abstract restatement regarding interhemispheric connectivity and comprehension.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data collection and linear regression assumptions.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about missing data.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null difference between treatment and usual care groups.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Provides mean lesion load value for interhemispheric tracts.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null correlation between interhemispheric lesion load and language
        scores.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports positive associations between QA in specific right hemisphere
        tracts and comprehension.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports absence of negative associations for comprehension.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports negative associations between QA in specific right hemisphere
        tracts and production.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure caption.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports positive associations between QA in corpus callosum and longitudinal
        comprehension improvement.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports negative associations between QA in specific tracts and longitudinal
        production improvement.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports that results remained largely unchanged after whole-brain analysis
        and additional covariate inclusion.
    - source_id: P5-S2-C9
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of negative associations for production recovery.
    - source_id: P5-S3-C2
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Discussion restatement of tracts connecting to right frontal lobe.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Discussion restatement of tracts connecting to right frontal lobe.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Discussion restatement of negative associations for production.
    - source_id: P6-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Discussion restatement of differential corpus callosum associations.
    - source_id: P6-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Discussion restatement of specific corpus callosum subdivision effects.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological discussion of QA-based connectometry.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about WM tracts outside homologous pathways.
    - source_id: P6-S4-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of treatment group null results.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P4-S1-C8
    - P4-S1-C10
    - P4-S2-C2
    - P4-S2-C5
    - P4-S2-C7
    - P5-S2-C9
    - P5-S3-C2
    - P6-S1-C1
    - P6-S1-C6
    - P6-S2-C4
    - P6-S2-C5
    - P6-S3-C4
    - P6-S3-C6
    - P6-S4-C2
    - P7-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C8
      recruited_sample:
      - P1-S1-C11
      - P3-S1-C5
      eligibility:
      - P3-S1-C3
      - P3-S1-C4
      imaging_provenance:
      - P3-S2-C1
      imaging_timing:
      - P1-S1-C12
      - P2-S3-C1
      - P3-S1-C7
      - P3-S2-C2
      outcome_timing: []
      outcome_definition:
      - P1-S1-C12
      - P1-S2-C2
      - P3-S1-C10
      - P3-S1-C11
      - P4-S1-C2
      - P5-S1-C2
      - P5-S1-C4
      validation: []
      analysis_restrictions:
      - P4-S1-C13
      - P4-S2-C1
      dependent_variable_statement:
      - P1-S2-C2
      - P4-S1-C2
      limitations:
      - P6-S2-C6
      - P6-S3-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C3
      - P5-S1-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C8
      - P3-S1-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P1-S1-C11
      - P1-S2-C2
      - P2-S3-C1
      - P3-S1-C7
      - P4-S1-C2
      - P4-S2-C4
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: core
    scope: Independent model text review of core meaning; not human approval or complete
      PDF verification
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
      review_sha256: 7258fc9d7d103badf2645bb78c508a4aaa5aca2630715beae44f67bbb948fdb9
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: &id001
        - gemma4:31b
        - qwen3.8:27b
        digests: &id002
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P4-S2-C6
      source_result: Higher production t-scores were associated with lower QA in segments
        of the right corticospinal tract, thalamic radiation, and inferior longitudinal
        fasciculus (pFDR < .0125).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the cross-sectional association
            between early subacute right hemisphere structural connectivity and language
            production, as described in P4-S2-C6 and P3-S3-C11.
          source_ids:
          - P4-S2-C6
          - P3-S3-C11
        direction:
          answer: fits
          reason: The source explicitly states that higher production t-scores were
            associated with lower QA, which aligns with the proposed claim of a negative
            association.
          source_ids:
          - P4-S2-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as right hemisphere structural
            connectivity measured via QA connectometry, and the outcome is language
            production measured by the Comprehensive Aphasia Test.
          source_ids:
          - P3-S2-C11
          - P3-S1-C11
        qualifications:
          answer: fits
          reason: The proposed qualifications regarding adjustment for lesion volume
            and age, and correction for multiple comparisons, are consistent with
            the methods described in P4-S1-C3 and P4-S1-C6.
          source_ids:
          - P4-S1-C3
          - P4-S1-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats that would change the interpretation of the
            association are omitted from the proposed core.
          source_ids:
          - P4-S2-C6
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 22
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R002
      exposure:
        text: early subacute stage right hemisphere structural connectivity (QA)
      outcome:
        text: language production
      analysis_label: Cross-sectional connectometry (early subacute stage)
      relation: association
      evidence_ids:
      - P4-S2-C6
      qualifier_ids:
      - P4-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
        source_review: _compare/relationships-2026-11-16/review-current/Sihvonen2023
        source_status_sha256: 73b6033d15ff7307822e8ab6361ecafb3491c3b36a76771fd49b15e0e49b6b48
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: aaab897ab9d07b2387431d61d6c66a900eb8ca34b6ae3b988c48bf1c3611063f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d2c3645a16e66bbfed553fabf3b803b3486b7ca8326ce4d5c785a099892d1324
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C3
          page: 3
          text_layer_sha256: d2c3645a16e66bbfed553fabf3b803b3486b7ca8326ce4d5c785a099892d1324
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Inclusion criteria were: first-

          ever left hemisphere stroke with aphasia as measured by an Aphasia

          Quotient of <93.8 using the Western Aphasia Battery—Revised

          (Kertesz, 2007); availability for an initial assessment at 2–6 weeks

          poststroke onset; medically and cognitively able to participate in a

          research intervention; and English as a dominant language prior to

          their stroke.'
        anchor_text: 'Inclusion criteria were: first-

          ever left hemisphere stroke with aphasia as measured by an Aphasia

          Quotient of <93.8 using the Western Aphasia Battery—Revised

          (Kertesz, 2007); availability for an initial assessment at 2–6 weeks

          poststroke onset; medically and cognitively able to participate in a

          research intervention; and English as a dominant language prior to

          their stroke.'
        excluded_fragments: []
        image_sha256: dd786e61664487391fe30bf8ec3934c41378eb6f0222e2dfcc7a72d0f048a9a5
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Higher production t-scores were associated with lower QA in seg-

    ments of the right corticospinal tract, thalamic radiation, and inferior

    longitudinal fasciculus (Figure 1b) (pFDR < .0125).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
