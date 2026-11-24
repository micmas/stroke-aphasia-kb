---
id: extreme_capsule_lesion_load
name: extreme capsule lesion load
kind: tract
findings:
- id: f1
  target: words_per_minute
  target_kind: impairment
  claim: When used in a regression model with arcuate fasciculus lesion load, uncinate
    fasciculus lesion load, and total lesion size, extreme capsule lesion load was
    a nonsignificant predictor of words per minute (WPM).
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 30
    population: Right-handed patients with left-hemispheric strokes in the middle
      cerebral artery territory and residual impairments in speech production.
    phase: not_reported
    time_post_onset: At least 11 months post stroke at the time of testing.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a probabilistic reference
    tract template of the extreme capsule derived from diffusion tensor imaging of
    10 age-matched healthy subjects. Measured as part of a regression analysis where
    arcuate fasciculus lesion load was the best predictor. Additional metadata has
    not been transcribed; review the pending-field flags before approval. PDF image
    reading (P2-S2-C4, two-model agreement, human verification pending): Methods


    Subjects

    The study group consisted of 30 right-handed patients, all of whom had left-hemispheric
    strokes in the middle cerebral artery territory and were at least 11 months post
    stroke at the time of testing (6 females and 24 males; mean age 58.5 years [SD
    10.0]; mean time poststroke 35.0 months [SD 28.7]) Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-24'
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
    - proposed_concept:words_per_minute
  citation: '@Marchina2011'
  source_passages:
  - section: Original source P3-S3-C2
    page: 3
    quote: "AF\nlesion load proved to be the best variable (partial R2\x040.175,\n\
      P\x040.030; Figure 2A), whereas EmC lesion load (partial\nR2\x040.087, P\x04\
      0.135), UF lesion load (partial R2\x040.098,\nP\x040.112), and lesion size (partial\
      \ R2\x040.002, P\x040.829) were\nshown to be nonsignificant predictors."
    supports: claim
  - section: Original source P1-S1-C7
    page: 1
    quote: 'To quantitatively analyze the

      relationship between impairment scores and lesion load along the 3 fiber tracts,
      we calculated tract–lesion overlap volumes

      for each patient using probabilistic maps of the tracts derived from diffusion
      tensor images of 10 age-matched healthy subjects.'
    supports: method
  - section: Original source P2-S2-C4
    page: 2
    quote: 'Methods

      Subjects

      The study group consisted of 30 right-handed patients, all of whom

      had left-hemispheric strokes in the middle cerebral artery territory

      and were at least 11 months post stroke at the time of testing (6

      females and 24 males; mean age 58.5 years [SD 10.0]; mean time

      poststroke 35.0 months [SD 28.7]).'
    supports: sample
  - section: Original source P2-S1-C4
    page: 2
    quote: 'Lesion loads (ie, volume of tract affected

      by a patient’s lesion) of these tracts were then calculated and

      related to 3 functional measures of speech production: words

      per minute (WPM), number of correct information units

      (CIUs) per total words uttered (%CIUs), and CIUs per

      minute.16 WPM reflects the rate of speech but includes

      uninformative “filler” words, circumlocutions, and incorrect

      words.'
    supports: claim
  - section: Original source P3-S2-C12
    page: 3
    quote: "Results\nRate of Speech\nA regression analysis was first conducted using\
      \ lesion size\nand lesion loads of all 3 tracts (ie, AF, EmC, and UF) as\npredictors\
      \ of words/min (adjusted R2\x040.301, P\x040.011)."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Marchina2011
  proposal_id: R002
  review_status_sha256: 423e5507176daee930a80d64fcda5ef76dcff455ab744da299172589cfd092ee
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
        A/passages.json: ec9c68a9b9f1b493b613e5cc47b6d6d986319a9399b4d2598fb686788a4fa886
        A/raw.json: 5958f84fc8f35ca7b04f121012d28749c2603910585a0094642fec334fd6e712
        A/source-units.json: 76f500a85d124800d8fae70a3f6ac6ab39adb02bb81fbae041afe1ce77b9caaa
        A/full-source-units.json: c902f1bff001d62ec21bf3c21179e441b3f276864d6fbc6015d7539caac643b7
        A/meta.json: 16c4b1043a80d491cd4df6754da4b4b0ce391fd3e4d639aeec9c291a57e09a73
        A/table-images/manifest.json: 61e44b6110aba550f3c2b293cfd88b2049a7e8ba2d48f3cf26446a20383a0b49
        A/clauses/window-03/raw.json: 47aff445cca74c7ab39fc7b1404ce89dd1b251f1d2b4bc0eaed4665f7f83e6c1
        A/clauses/window-03/prompt.txt: 1a8b6878bab9ef414426610525b056bd0bfc94cc1d28d5d9454dd74add7f66ee
        A/clauses/window-03/meta.json: 1075dcba25507498a69d8ffdb537581ae65b564d6b1cf7c5bca9d06fb4df8f07
        A/clauses/window-04/raw.json: a4d792860712def3fdb27b8633864421698241d5ae1eeab23e428aa164239819
        A/clauses/window-04/prompt.txt: 8a723009ae0834abf1f774855bf1b1c33de1beb6cffa13f080d4352de716bb94
        A/clauses/window-04/meta.json: 592fb9c119ac578b8ba2d86c3dee798cc686bedc8f34e89c709c038e2d32ca9a
        A/clauses/window-02/raw.json: 7ed7a3f2f62a85d5ff39880fa2348eb1212c2022b882880c6529c5563e35155d
        A/clauses/window-02/prompt.txt: ca401d297580161a0466d10d323d35061b89f443bc49ef97c3b2e44799734a28
        A/clauses/window-02/meta.json: d32c2c22c39cf7304ca2c500aebdfb127fa54b2e96d7094fb04b188af13954c8
        A/clauses/window-01/raw.json: 9b1ce9f68b9bbf14e27d5444795e228694f8c44e34f37a7863bccf235afd0fc5
        A/clauses/window-01/prompt.txt: 8c1428a4881696f9101f0628cdc304db7ee9b46370a519df8798709670ef9854
        A/clauses/window-01/meta.json: d52b807557186af53ad68f309a1a18bcd2170af95991c215ef91d7c20574f906
        B/passages.json: ec9c68a9b9f1b493b613e5cc47b6d6d986319a9399b4d2598fb686788a4fa886
        B/raw.json: 7b9ab765566e227d6b2a4209eb0910c5943c71f1ea32d5c4cc86274d82f1150c
        B/source-units.json: 76f500a85d124800d8fae70a3f6ac6ab39adb02bb81fbae041afe1ce77b9caaa
        B/full-source-units.json: c902f1bff001d62ec21bf3c21179e441b3f276864d6fbc6015d7539caac643b7
        B/meta.json: 9f49cb2f7aa5da8ab3cab1d8cda17e80d2ffd5e30a3ba177e3c5bc789e91a07d
        B/table-images/manifest.json: 61e44b6110aba550f3c2b293cfd88b2049a7e8ba2d48f3cf26446a20383a0b49
        B/clauses/window-03/raw.json: 743f02a3062e9f464506af4d08f05cfbc2d849c36e5fc7d21b5fe3ab01fe0099
        B/clauses/window-03/prompt.txt: 1a8b6878bab9ef414426610525b056bd0bfc94cc1d28d5d9454dd74add7f66ee
        B/clauses/window-03/meta.json: ba3d138ad1aac6247f8ccb48a3dcd406606e7779113bf4718543c46892105bd2
        B/clauses/window-04/raw.json: 23de8ed5697ac627a133029000ccc1ff2ba0c9f24147dd69ce7ff330d92e6bdf
        B/clauses/window-04/prompt.txt: 8a723009ae0834abf1f774855bf1b1c33de1beb6cffa13f080d4352de716bb94
        B/clauses/window-04/meta.json: 50c0ec743916feb8e8bf665352f3d651e299c76870466dcfba18641db70bf37c
        B/clauses/window-02/raw.json: e2b9e077260b263c921588eb5d1547977998a095303101c4c0877af9cd0a2c69
        B/clauses/window-02/prompt.txt: ca401d297580161a0466d10d323d35061b89f443bc49ef97c3b2e44799734a28
        B/clauses/window-02/meta.json: 643f802d109593571bd3c6a999c066b7577e134bfcdb317a06e5db7fefa83833
        B/clauses/window-01/raw.json: 68aa622c5cbc25071913dbe8569f9d5d86aa8c200292388b3ba6e0666ff0e524
        B/clauses/window-01/prompt.txt: 8c1428a4881696f9101f0628cdc304db7ee9b46370a519df8798709670ef9854
        B/clauses/window-01/meta.json: 92b029a1dae663863895086ac09a6972e89ac1b72df492d577be8212d2958981
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
      pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
      source_review: _compare/relationships-2026-11-16/review-current/Marchina2011
      source_status_sha256: 93e948a4960cdfcdbad0d26b284568ed8fff2a89ddb28e55e4793680e1e095fd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: extreme capsule lesion load
    outcome:
      text: words per minute (WPM)
    analysis_label: Regression analysis for rate of speech
    relation: association
    evidence_ids:
    - P3-S3-C2
    qualifier_ids:
    - P3-S2-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
      source_review: _compare/relationships-2026-11-16/review-current/Marchina2011
      source_status_sha256: 93e948a4960cdfcdbad0d26b284568ed8fff2a89ddb28e55e4793680e1e095fd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C8
      - Unaccounted source passage P1-S1-C8
      - Result passage disposed without unit P4-S1-C6
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 0
      default_disposition_count_requires_completeness_check: 84
      unselected_timing_passages:
      - P1-S1-C5
      - P2-S3-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
      source_review: _compare/relationships-2026-11-16/review-current/Marchina2011
      source_status_sha256: 93e948a4960cdfcdbad0d26b284568ed8fff2a89ddb28e55e4793680e1e095fd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      - 14
      - 15
      reason: Abstract summary of regression results.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes interobserver reliability of CIU scoring.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ventricular dilatation in lesion mapping.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes interobserver reliability of lesion volume.
    - source_id: P3-S2-C12
      disposition: represented
      result_indexes:
      - 0
      - 16
      reason: Provides model performance and qualifier for WPM regression.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Provides individual predictor results for WPM.
    - source_id: P3-S3-C3
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      - 17
      reason: Provides model performance and qualifier for %CIUs regression.
    - source_id: P3-S3-C4
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: Provides individual predictor results for %CIUs.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the third regression analysis.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      - 11
      - 18
      reason: Provides model performance and qualifier for CIUs/min regression.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      - 11
      reason: Provides individual predictor results for CIUs/min.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 12
      - 13
      - 14
      - 15
      - 19
      reason: Provides model performance and qualifier for naming ability regression.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 12
      - 13
      reason: Provides predictor results for AF and UF on naming.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Provides predictor results for EmC and lesion size on naming.
    - source_id: P4-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      - 4
      - 8
      reason: Discussion restatement of AF significance.
    - source_id: P4-S1-C7
      disposition: repeated
      result_indexes:
      - 3
      - 7
      - 11
      reason: Discussion restatement of lesion size non-significance.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 4
      - 8
      reason: Discussion restatement of AF significance across measures.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative comparison of specific patients in Figure 3.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative comparison of specific patients in Figure 3.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C8
    - P2-S3-C7
    - P3-S2-C3
    - P3-S2-C6
    - P3-S3-C5
    - P4-S1-C6
    - P4-S1-C7
    - P5-S1-C5
    - P5-S2-C8
    - P5-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C4
      recruited_sample:
      - P2-S2-C4
      eligibility:
      - P2-S2-C4
      - P2-S2-C6
      imaging_provenance:
      - P2-S1-C3
      - P3-S1-C2
      - P3-S2-C8
      imaging_timing:
      - P2-S2-C4
      outcome_timing:
      - P2-S2-C5
      outcome_definition:
      - P2-S1-C4
      - P2-S1-C6
      - P2-S2-C2
      - P2-S3-C6
      - P2-S3-C8
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C4
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
      review_sha256: 423e5507176daee930a80d64fcda5ef76dcff455ab744da299172589cfd092ee
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
      - P3-S3-C2
      source_result: In a regression analysis predicting words per minute (WPM) using
        lesion size and lesion loads of the arcuate fasciculus (AF), extreme capsule
        (EmC), and uncinate fasciculus (UF), EmC lesion load was a nonsignificant
        predictor (partial R2=0.087, P=0.135), whereas AF lesion load was significant.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the regression model for WPM
            described in P3-S2-C12 and P3-S3-C2, which included AF, EmC, UF, and lesion
            size as predictors.
          source_ids:
          - P3-S2-C12
          - P3-S3-C2
        direction:
          answer: fits
          reason: The source explicitly states that EmC lesion load was a nonsignificant
            predictor (P=0.135), which aligns with the 'no_effect' direction (no statistically
            detected association) in the draft.
          source_ids:
          - P3-S3-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as extreme capsule lesion load,
            and the outcome is WPM. The patient measurement is correctly identified
            as template_lesion_overlap, as the study overlaid patient lesions on probabilistic
            tract maps derived from healthy controls (P1-S1-C7, P3-S2-C8), rather
            than using patient diffusion data.
          source_ids:
          - P1-S1-C7
          - P3-S2-C8
          - P3-S3-C2
        qualifications:
          answer: fits
          reason: The draft correctly qualifies the null result by noting it was part
            of a regression analysis where AF was the best predictor, which is supported
            by P3-S3-C2.
          source_ids:
          - P3-S3-C2
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly identifies
            the null result and the context of the model. The small sample size is
            noted as a limitation, which is appropriate given the N=30.
          source_ids:
          - P2-S2-C4
          - P3-S3-C2
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R002
      exposure:
        text: extreme capsule lesion load
      outcome:
        text: words per minute (WPM)
      analysis_label: Regression analysis for rate of speech
      relation: association
      evidence_ids:
      - P3-S3-C2
      qualifier_ids:
      - P3-S2-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
        source_review: _compare/relationships-2026-11-16/review-current/Marchina2011
        source_status_sha256: 93e948a4960cdfcdbad0d26b284568ed8fff2a89ddb28e55e4793680e1e095fd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 690e344d9f66437c64872bf17908afa0b05c1d807b2102aaec07ef9a4413c555
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C2
          page: 3
          text_layer_sha256: 690e344d9f66437c64872bf17908afa0b05c1d807b2102aaec07ef9a4413c555
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "AF\nlesion load proved to be the best variable (partial R2\x04\
          0.175,\nP\x040.030; Figure 2A), whereas EmC lesion load (partial\nR2\x04\
          0.087, P\x040.135), UF lesion load (partial R2\x040.098,\nP\x040.112), and\
          \ lesion size (partial R2\x040.002, P\x040.829) were\nshown to be nonsignificant\
          \ predictors."
        anchor_text: "AF\nlesion load proved to be the best variable (partial R2\x04\
          0.175,\nP\x040.030; Figure 2A), whereas EmC lesion load (partial\nR2\x04\
          0.087, P\x040.135), UF lesion load (partial R2\x040.098,\nP\x040.112), and\
          \ lesion size (partial R2\x040.002, P\x040.829) were\nshown to be nonsignificant\
          \ predictors."
        excluded_fragments: []
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 02be2a2d003c0acf3c87b0ab67d79cba816bb3c0ca04528899c4bf18c5bcd5f8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: 02be2a2d003c0acf3c87b0ab67d79cba816bb3c0ca04528899c4bf18c5bcd5f8
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Subjects

          The study group consisted of 30 right-handed patients, all of whom

          had left-hemispheric strokes in the middle cerebral artery territory

          and were at least 11 months post stroke at the time of testing (6

          females and 24 males; mean age 58.5 years [SD 10.0]; mean time

          poststroke 35.0 months [SD 28.7]).'
        anchor_text: 'Methods

          Subjects

          The study group consisted of 30 right-handed patients, all of whom

          had left-hemispheric strokes in the middle cerebral artery territory

          and were at least 11 months post stroke at the time of testing (6

          females and 24 males; mean age 58.5 years [SD 10.0]; mean time

          poststroke 35.0 months [SD 28.7]).'
        excluded_fragments: []
        image_sha256: 5f38bdf034171b3572f7a9c132ff72a1f25247dc6e35ab517d66bcfba0d24147
        transcription: 'Methods


          Subjects

          The study group consisted of 30 right-handed patients, all of whom had left-hemispheric
          strokes in the middle cerebral artery territory and were at least 11 months
          post stroke at the time of testing (6 females and 24 males; mean age 58.5
          years [SD 10.0]; mean time poststroke 35.0 months [SD 28.7])'
      P3-S2-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8b6527f9452aea5cfab9ee7cf8399f0fa97aadfd6d2095a12039ffceac8770fa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3d867b90810211244c2c6ecf2940cd29aa41ace5c6d665e0728683265bccf0ce
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C12
          page: 3
          text_layer_sha256: 3d867b90810211244c2c6ecf2940cd29aa41ace5c6d665e0728683265bccf0ce
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Results\nRate of Speech\nA regression analysis was first conducted\
          \ using lesion size\nand lesion loads of all 3 tracts (ie, AF, EmC, and\
          \ UF) as\npredictors of words/min (adjusted R2\x040.301, P\x040.011)."
        anchor_text: "Results\nRate of Speech\nA regression analysis was first conducted\
          \ using lesion size\nand lesion loads of all 3 tracts (ie, AF, EmC, and\
          \ UF) as\npredictors of words/min (adjusted R2\x040.301, P\x040.011)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "AF\nlesion load proved to be the best variable (partial R2\x040.175,\nP\x04\
    0.030; Figure 2A), whereas EmC lesion load (partial\nR2\x040.087, P\x040.135),\
    \ UF lesion load (partial R2\x040.098,\nP\x040.112), and lesion size (partial\
    \ R2\x040.002, P\x040.829) were\nshown to be nonsignificant predictors."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
