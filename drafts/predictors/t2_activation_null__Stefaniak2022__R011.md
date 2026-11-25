---
id: t2_activation_null
name: T2 brain activation
kind: predictor
findings:
- id: f1
  target: t2_language_pcs
  target_kind: impairment
  claim: No brain regions were identified in which T2 activation was associated with
    T2 PC1, PC2, or PC3 scores.
  direction: no_effect
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 26
    population: individuals with mild-moderate aphasia following left hemispheric
      infarct
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and
      timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Exclusion of lesion-affected voxels may have missed positive associations between
    language performance and left hemisphere activation
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Mean regional brain activation during overt speech
    production (summation of ''Speech and Count'' over ''Rest'') measured via functional
    MRI at 4 months post-stroke. Analyses were restricted to grey matter voxels in
    which no patient had a lesion to minimize confounding effects of lesion morphology.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:t2_language_pcs
  citation: '@Stefaniak2022'
  source_passages:
  - section: Original source P8-S3-C2
    page: 8
    quote: 'We did not identify any clusters in which T2 activation was

      associated with T2 PC1, PC2 or PC3 score.'
    supports: claim
  - section: Original source P3-S2-C3
    page: 3
    quote: 'Twenty-six

      patients had a full battery of language test data available and were

      included in this analysis.'
    supports: sample
  - section: Original source P4-S1-C5
    page: 4
    quote: 'The contrast of interest was the summation of ‘Speech and

      Count’ over ‘Rest’, which represents the combined activation dur-

      ing overt speech production over the course of the scan.'
    supports: method
  - section: Original source P4-S2-C6
    page: 4
    quote: 'To minim-

      ize the confounding effect of variable lesion morphology, analyses

      were restricted to grey matter voxels in which no patient had a le-

      sion.'
    supports: confounders
  - section: Original source P11-S3-C4
    page: 11
    quote: 'Consequently,

      we might have missed positive associations between language

      performance and left hemisphere activation, as has been shown

      previously.12 However, most previous studies reporting such a

      compensatory role for left hemisphere language activation have

      tended to overlook variable lesion morphology as a confounding

      factor,21,80–82 or analysed restricted subgroups of patients with

      lesions confined to certain locations12,16 which does not complete-

      ly account for voxel-wise variability in lesion location throughout

      the entire left hemisphere.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Mean regional brain activation during overt speech production (summation
  of 'Speech and Count' over 'Rest') measured via functional MRI at 4 months post-stroke.
assessment:
- fMRI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Stefaniak2022
  proposal_id: R011
  review_status_sha256: 43a046f4ecf8593b8c0b1238adb333ff1d7421706bf23d2026b6ee08df55e5a2
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
    original_review_binding:
      version: relationship-review-v6
      input_hashes:
        pdf: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
        A/passages.json: b5eec70a29bd4fa361da4317721ad17df38fcd8668bf7cdac77bf22c53992b10
        A/raw.json: 2e09c05273d6d32986f824d03a6f88d3c90f2ef618f703614f969bde76293da8
        A/source-units.json: b61057cb4ffc778ac020b6d4f31680ca4d4a75392f01307902555c5f20c2b2d1
        A/full-source-units.json: 3e5cd0e26a4fff6589e7b16f46def3f1c3bc31ff9f24b91b7471f08e2af620a3
        A/meta.json: b6d0df1cc48eb50dfad87ee39e3eab46fe78bb054bd49309962d0ed7a8109a1c
        A/table-images/TABLE-1-page-5-1.png: 8e8530f58fa39331f9d07760593b73f65e3347821f4ac00dc6ae1e69bfa1d665
        A/table-images/page-5.png: 1b686f7e2edadfd7f1178a36a0ef7b4aa106161be8180d1dfb2606cc1a71cd83
        A/table-images/manifest.json: 6f8c7067698a7403b6b83e3a3242b41c3c11e45310007da0389208f0cda7fb2b
        A/clauses/window-03/raw.json: 39466f133f8e0727f4cf161f171d554bc608e73bb8ec1b55969f9eca8d722863
        A/clauses/window-03/prompt.txt: 3a6a18363c77d872727e1182ce28bc382811300820c3294e422ac11c951c21f0
        A/clauses/window-03/meta.json: 8815468a9ccdf5577f01bba6c9b62c4c881edc9a98b9cae5ce0601956f65020f
        A/clauses/window-04/raw.json: 83f217f0b4c60531705e58c05519e06fc3b152b0e14fb3cc261c5c75bdeeb9ef
        A/clauses/window-04/prompt.txt: 4891a90ef584f6388ac159e316cf8f24decd9b5a9cb918acfc2d24843ffedcf4
        A/clauses/window-04/meta.json: f6ceb1880a3f159239cf049c8b340cd14ddfed117ba15aab10aa1486e00c8dd1
        A/clauses/window-05/raw.json: fbfe1b952e9f44de328e754082999564c8f7f735ca722a8295745d2014e59eb5
        A/clauses/window-05/prompt.txt: bb52db155d65b5f4be54f95f5b903e3ec5a93343753ce6002ac4a1ba4c3c843d
        A/clauses/window-05/meta.json: 840f563dd27649e060cd427c6b6058f967075171b785dd30363a60c214ec00a4
        A/clauses/window-02/raw.json: 06d287659400af45ab67dfbb7320c12a33767ecb1b141dba320bb36413fe26cb
        A/clauses/window-02/prompt.txt: cb87938a28501cac2c0ed3456cb2fe5adf65a1906a85f1b1f5204125f2af84c1
        A/clauses/window-02/meta.json: 6624ec3e6ce8351024f380e74917404ea2ccf08e69e83d1194909976df0fdf5e
        A/clauses/window-07/raw.json: 35090578957f0c4f6038f06026069bddda2191d3b6405539136c1db7b94618eb
        A/clauses/window-07/prompt.txt: f611a78143a73bd149efe99a04bb68ed5a8345196f70f2f30eabb93e876e8bef
        A/clauses/window-07/meta.json: 3a4a6e7b32d3ec378c96274eacfe0a273a7486eddfbd25e065f5c1adf20252b9
        A/clauses/window-01/raw.json: ac0e3e10c88df5caf94bb5d8c5d5b71b942c34fe1ba3cfed0976f700e143fc90
        A/clauses/window-01/prompt.txt: 90e18428bdf738f8212d17080ed89189f2caa776b131db81b9e72478f3d266d8
        A/clauses/window-01/meta.json: 2e34d2dfd262c8e650f8b8b5bafb1ec860a28d8e7b71bed183aa34f2be7584e1
        A/clauses/window-06/raw.json: fe182f56afb30d2b9c4a5230f61177ee9f81ca6307651dea4b0fc96451e2d8b8
        A/clauses/window-06/prompt.txt: 73785d9f1c59666c434963424dd97a5d561abcc3aed6af41928c4d2887d792f4
        A/clauses/window-06/meta.json: a5fa681bc65165894edb1f5814eef98758a89d0b45a4d4b3269c7fec2c4f01b6
        A/clauses/window-08/raw.json: 77feb60b4d7c7daf7cccc74a9133d0e97aaa13edc9eedb0680e7104af0353d78
        A/clauses/window-08/prompt.txt: 82385704a54aa24f484077a9d17ffbf710c9204b2f7560096c98805359461ef5
        A/clauses/window-08/meta.json: eac266268d22f9f0091e0cf1eb831ffd49e2b03e3b8bcd2a88d4502f82cb4425
        A/tables/TABLE-1-page-5-1/raw.json: 8fcc0aa12b0923a5fadf4b4519dd47e5f20a6fa7dadd1564c940b4d9bdba1faf
        A/tables/TABLE-1-page-5-1/prompt.txt: fe6af7c480329c5e7abf99833fa57a35e04badac11805835accf761a78ccb04d
        A/tables/TABLE-1-page-5-1/meta.json: d6907e3779a32f6f5e63ac76cd52ca73d0b362f8ee3bede540ee3599b7980922
        B/passages.json: b5eec70a29bd4fa361da4317721ad17df38fcd8668bf7cdac77bf22c53992b10
        B/raw.json: 5c4b07e3a8e9ad7a34865fa9735b70ce0e1d964e8a0a7707dcd0cc7ef0ef0b10
        B/source-units.json: b61057cb4ffc778ac020b6d4f31680ca4d4a75392f01307902555c5f20c2b2d1
        B/full-source-units.json: 3e5cd0e26a4fff6589e7b16f46def3f1c3bc31ff9f24b91b7471f08e2af620a3
        B/meta.json: 25c13c54565efcbf78a823e11f1af34ae46ffd2756f2ce7c35d0685b2d7e92de
        B/table-images/TABLE-1-page-5-1.png: 8e8530f58fa39331f9d07760593b73f65e3347821f4ac00dc6ae1e69bfa1d665
        B/table-images/page-5.png: 1b686f7e2edadfd7f1178a36a0ef7b4aa106161be8180d1dfb2606cc1a71cd83
        B/table-images/manifest.json: 76c7a8d845d5af7f089bd2f605e95237be924a6df450c4735ff196959143acb6
        B/clauses/window-03/raw.json: 1614b19f9ef2a8808a79883f05ec62c38eefbe5038bf26b75d574814e030d525
        B/clauses/window-03/prompt.txt: 3a6a18363c77d872727e1182ce28bc382811300820c3294e422ac11c951c21f0
        B/clauses/window-03/meta.json: d163de1f82eac5a37a98046024d268587968ef5d4df8d52a0a3b1679afe4932a
        B/clauses/window-04/raw.json: c2861765b17ee9e228993804c503d024c0d745b384537a043dda7dce218a45c3
        B/clauses/window-04/prompt.txt: 4891a90ef584f6388ac159e316cf8f24decd9b5a9cb918acfc2d24843ffedcf4
        B/clauses/window-04/meta.json: bd725d65c3e9567c9bc2f89b8babeea8457af2fd06820e0b3483c378e380b932
        B/clauses/window-05/raw.json: 62f2432fb5408ba73da1c73c7ac1ea1f469efaa7dddeebfb922094636634b243
        B/clauses/window-05/prompt.txt: bb52db155d65b5f4be54f95f5b903e3ec5a93343753ce6002ac4a1ba4c3c843d
        B/clauses/window-05/meta.json: 3b82b8f251a1b8b8281903a8a88f9ca3e8a85ab670b2b62a3ab68809d1dc5641
        B/clauses/window-02/raw.json: 5f1b9ac4bd4be8d4a81b8f7db992e66e0185d2a5c388d65a35695bae2beecd86
        B/clauses/window-02/prompt.txt: cb87938a28501cac2c0ed3456cb2fe5adf65a1906a85f1b1f5204125f2af84c1
        B/clauses/window-02/meta.json: 67dbe2b1707ea223b9b73d41f953dcb2327a41c38e9b2b31c11d7fb691ab6de0
        B/clauses/window-07/raw.json: af9cbf3eaf6f8d5e9ab5cdea5c1075e36bd40166be0d040171d4c3dda8777de3
        B/clauses/window-07/prompt.txt: f611a78143a73bd149efe99a04bb68ed5a8345196f70f2f30eabb93e876e8bef
        B/clauses/window-07/meta.json: 98a24ceaa26ff623e5f4f88f700cad4aab1f81899908cf2076a1e0fbeea7fe2a
        B/clauses/window-01/raw.json: 03d40f508461456475d935fcf3a3cf382336e1bd7c9d289877bb013a81ee27b0
        B/clauses/window-01/prompt.txt: 90e18428bdf738f8212d17080ed89189f2caa776b131db81b9e72478f3d266d8
        B/clauses/window-01/meta.json: cc3e98a0b5b76a49909bf7259b58bd8a39f2f1236b38e80ed3fa716ee50200d1
        B/clauses/window-06/raw.json: 79a1074e40e4240a2ceed2bac93c3be6aeb8396b5745f810945abc8b770a08b8
        B/clauses/window-06/prompt.txt: 73785d9f1c59666c434963424dd97a5d561abcc3aed6af41928c4d2887d792f4
        B/clauses/window-06/meta.json: bb19d946f4082b9a3fdbee23daa875748d4048b8d4345845ad3252902425026b
        B/clauses/window-08/raw.json: 9ed30ed1fa48220b105a360d0aefc29ef773857d67d3b2bd047fecfce04a7017
        B/clauses/window-08/prompt.txt: 82385704a54aa24f484077a9d17ffbf710c9204b2f7560096c98805359461ef5
        B/clauses/window-08/meta.json: e075bf3ff58aea94b116c81f816cb9c11f28855ba1c0436bc33666c6ecc2cccb
        B/tables/TABLE-1-page-5-1/raw.json: 42ec7d31f489da17e2e9bcbdef19bc47d497381ee1c263fc158d9df0ccdf1a4d
        B/tables/TABLE-1-page-5-1/prompt.txt: fe6af7c480329c5e7abf99833fa57a35e04badac11805835accf761a78ccb04d
        B/tables/TABLE-1-page-5-1/meta.json: 353f611833c7c73f1e7c4d85e2d67dc6438a3c85e501616a6290261af771ab45
      code:
        relationship_review.py: ab52eac5603e2f4080aa82e51ec2d579714fe7aeecc6cc376f345c9001157135
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
      pdf_sha256: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
      source_review: _compare/relationships-2026-11-16/review-current/Stefaniak2022
      source_status_sha256: f44dcdf8a115e12ab7d64b08c8f1ee647bfd3e77a82beeaad8c736dc923b27bf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R011
    exposure:
      text: T2 brain activation
    outcome:
      text: T2 PC1, PC2 or PC3 scores
    analysis_label: T2 Activation Association
    relation: association
    evidence_ids:
    - P8-S3-C2
    qualifier_ids: []
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
      source_review: _compare/relationships-2026-11-16/review-current/Stefaniak2022
      source_status_sha256: f44dcdf8a115e12ab7d64b08c8f1ee647bfd3e77a82beeaad8c736dc923b27bf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C8
      - Accounting without a linked unit P1-S2-C2
      - Unaccounted source passage P1-S2-C2
      - Result passage disposed without unit P3-S2-C6
      - 'window 6: invalid/duplicate disposition P5-S1-C11'
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C8
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C5
      - Accounting without a linked unit P6-S2-C6
      - Unaccounted source passage P6-S2-C6
      - Unaccounted source passage P6-S2-C5
      - Unaccounted source passage P6-S2-C4
      - Result passage disposed without unit P6-S2-C10
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P8-S2-C8
      - Result passage disposed without unit P8-S3-C4
      - Result passage disposed without unit P8-S3-C7
      - Result passage disposed without unit P8-S4-C3
      - Result passage disposed without unit P8-S4-C9
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C8
      - Result passage disposed without unit P11-S1-C3
      - Accounting without a linked unit P11-S2-C1
      - Accounting without a linked unit P11-S2-C5
      - Accounting without a linked unit P11-S2-C6
      - Unaccounted source passage P11-S2-C1
      - Unaccounted source passage P11-S2-C6
      - Unaccounted source passage P11-S2-C5
      - Result passage disposed without unit P11-S3-C6
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P5-S3-C4
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P8-S1-C1
      - P8-S1-C3
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 146
      unselected_timing_passages:
      - P8-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C6
        - P3-S2-C3
        - P3-S2-C8
        - P4-S2-C8
        - P5-S1-C7
        - P5-S3-C2
        - P6-S3-C2
        - P7-S1-C2
        - P7-S1-C5
        - P7-S1-C6
        - P8-S1-C6
        - P8-S2-C2
        - P8-S3-C3
        - P9-S2-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P1-S1-C6
        - P2-S2-C4
        - P3-S1-C9
        - P3-S2-C8
        - P4-S2-C2
        - P4-S3-C1
        - P4-S3-C2
        - P4-S3-C3
        - P5-S1-C1
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C6
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C7
        - P6-S1-C9
        - P6-S2-C1
        - P6-S2-C4
        - P6-S3-C2
        - P7-S1-C2
        - P7-S1-C8
        - P8-S1-C6
        - P9-S2-C7
        - P10-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C7
        - P1-S1-C9
        - P1-S1-C10
        - P2-S3-C5
        - P2-S4-C2
        - P3-S2-C10
        - P3-S2-C11
        - P3-S3-C1
        - P3-S3-C2
        - P4-S1-C5
        - P4-S2-C8
        - P4-S2-C10
        - P4-S3-C4
        - P4-S3-C5
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C7
        - P6-S1-C9
        - P6-S2-C1
        - P6-S2-C4
        - P6-S2-C8
        - P6-S3-C2
        - P7-S1-C2
        - P7-S1-C5
        - P7-S1-C6
        - P8-S1-C3
        - P8-S1-C4
        - P8-S1-C6
        - P9-S2-C7
        - P9-S2-C10
        - P9-S3-C4
        - P10-S1-C2
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C10
        - P3-S1-C5
        - P4-S1-C3
        - P4-S2-C3
        - P4-S3-C3
        - P5-S1-C3
        - P6-S1-C6
        - P6-S1-C9
        - P6-S2-C4
        - P6-S2-C8
        - P6-S2-C11
        - P6-S3-C2
        - P7-S1-C3
        - P7-S1-C6
        - P8-S1-C1
        - P8-S1-C6
        - P8-S2-C2
        - P8-S2-C5
        - P8-S2-C7
        - P8-S2-C9
        - P8-S4-C10
        - P9-S1-C6
        - P9-S1-C7
        - P9-S1-C9
        - P9-S2-C8
        - P9-S3-C4
        - P10-S1-C3
        - P10-S1-C6
        - P10-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - outcome_timing
      - outcome_definition
      - validation
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S3
        - P5-S3
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P8-S2
        - P8-S3
        - P9-S2
        - P10-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
      source_review: _compare/relationships-2026-11-16/review-current/Stefaniak2022
      source_status_sha256: f44dcdf8a115e12ab7d64b08c8f1ee647bfd3e77a82beeaad8c736dc923b27bf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes the three orthogonal PCs of language profiles.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: States that components did not recover in a homogeneous manner.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary statement of findings.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of specific regional associations.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of overlapping cluster associations.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic age-matching information.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlap map.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of analysis restriction to grey matter.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of impairment and improvement.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Defines the interpretation of PC1, PC2, and PC3.
    - source_id: P5-S1-C11
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of PC1 improvement.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Significant improvement in PC1 scores at T2.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Significant improvement in PC2 scores at T2.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Lack of significant improvement in PC3 scores at T2.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about IQR size.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline PC score correlations with change.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Correlations between PC changes (PC1 vs PC2, PC2 vs PC3, PC1 vs PC3).
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of PCA space movement.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of general activation patterns.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Non-significant group x time interaction.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 11
      reason: No regions of significantly greater activation in patients than controls.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 11
      reason: Less activation in patients in three clusters.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Null association for T1 PC2 and PC3.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Positive association of T1 activation in specific cluster with T1 PC1.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Robust regression confirming T1 PC1 association.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Unadjusted activation change associated with PC1 improvement.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies clusters for PC1 improvement (unadjusted).
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Robust regression for unadjusted PC1 improvement.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies clusters for PC1 improvement after baseline control.
    - source_id: P6-S2-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of adjusted PC1 clusters.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies bilateral ventromedial PFC cluster for PC1.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies right temporo-occipital MTG cluster for PC1.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Robust regression for adjusted PC1 improvement.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for negative association with PC1 change.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for positive association with PC2 change.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Null finding for PC2 change before baseline control.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies clusters for PC2 change after baseline control.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies left temporal pole/frontal pole cluster for PC2.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies right temporal pole/MTG cluster for PC2.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Null association for PC2 before baseline control.
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 7
      reason: Significant negative association for PC2 after baseline control.
    - source_id: P6-S3-C1
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of null association for PC2 before control.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of negative association for PC2 after control.
    - source_id: P7-S1-C2
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: General statement of PC1 association.
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Restatement of cluster counts for PC1.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Robust regression for adjusted PC2 change.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for positive association with PC3 change.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Unadjusted negative association for PC3 change.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies bilateral precentral gyrus/MFG cluster for PC3.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Robust regression for unadjusted PC3 change.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Null association for PC3 after baseline control (cluster 2).
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies left frontal pole cluster for PC3.
    - source_id: P8-S2-C1
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of left frontal pole cluster.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Null association for PC3 after baseline control (cluster 3).
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies clusters for PC3 change after baseline control.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies bilateral frontal poles/superior frontal gyrus cluster for
        PC3.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Robust regression for adjusted PC3 change (cluster 1).
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies ventromedial PFC cluster for PC3.
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Robust regression for adjusted PC3 change (cluster 2).
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies precuneus cluster for PC3.
    - source_id: P8-S2-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Robust regression for adjusted PC3 change (cluster 3).
    - source_id: P8-S3-C1
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of PC3 interaction.
    - source_id: P8-S3-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Null association for T2 activation and T2 PC scores.
    - source_id: P8-S3-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of multidimensional recovery.
    - source_id: P8-S4-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of uncorrelated/anticorrelated recovery.
    - source_id: P8-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of non-overlapping regions.
    - source_id: P8-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of adjusted regional associations.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological statement on false positives.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological statement on false negatives.
    - source_id: P9-S1-C9
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of ATL clusters for PC2.
    - source_id: P9-S2-C1
      disposition: repeated
      result_indexes:
      - 12
      reason: Restatement of lack of group-level activation changes.
    - source_id: P9-S2-C4
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of hypoactivation in specific regions.
    - source_id: P9-S2-C7
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of PC2 association.
    - source_id: P9-S3-C1
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of PC2 null before control.
    - source_id: P9-S3-C4
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of PC2 adjusted association.
    - source_id: P10-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: General statement of PC3 negative association.
    - source_id: P10-S1-C3
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Restatement of cluster counts for PC3.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of bilateral recovery.
    - source_id: P11-S1-C5
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of negative correlation for PC3.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of task-negative regions.
    - source_id: P11-S2-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of bilateral MFG and fluency recovery.
    - source_id: P11-S2-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of bilateral ATL and semantic recovery.
    unresolved_coverage:
    - source_id: P6-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S4-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P1-S2-C2
    - P1-S2-C3
    - P3-S2-C6
    - P3-S3-C9
    - P4-S2-C7
    - P5-S1-C7
    - P5-S1-C11
    - P5-S2-C5
    - P5-S2-C6
    - P5-S3-C4
    - P5-S3-C5
    - P6-S2-C5
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C11
    - P6-S3-C2
    - P7-S1-C2
    - P7-S1-C3
    - P8-S2-C2
    - P8-S3-C4
    - P8-S3-C7
    - P8-S3-C8
    - P8-S4-C3
    - P8-S4-C8
    - P8-S4-C9
    - P8-S4-C10
    - P9-S1-C1
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C9
    - P9-S2-C1
    - P9-S2-C4
    - P9-S2-C5
    - P11-S1-C3
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S2-C1
    - P11-S2-C5
    - P11-S3-C5
    - P11-S3-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C6
      - P3-S1-C9
      - P3-S2-C5
      - P3-S2-C8
      - P4-S3-C8
      - P5-S3-C2
      - P6-S3-C2
      - P11-S4-C3
      eligibility:
      - P1-S1-C6
      - P3-S2-C2
      imaging_provenance:
      - P1-S1-C6
      - P3-S3-C9
      - P4-S3-C8
      - P5-S1-C5
      imaging_timing:
      - P1-S1-C6
      - P2-S2-C4
      - P3-S1-C9
      - P4-S3-C8
      - P9-S2-C1
      - P9-S2-C4
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S2-C6
      - P4-S2-C7
      - P11-S3-C3
      dependent_variable_statement:
      - P1-S1-C9
      - P1-S1-C10
      - P2-S3-C5
      - P2-S4-C2
      limitations:
      - P2-S2-C5
      - P11-S3-C4
      - P11-S3-C5
      personal_factors:
      - P8-S1-C1
      - P8-S2-C2
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P11-S3-C3
      descriptive_personal_factors:
      - P1-S1-C6
      - P3-S2-C4
      - P3-S2-C6
      - P4-S3-C8
      - P5-S1-C3
      - P8-S2-C7
      - P9-S2-C1
      - P11-S4-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C6
      - P3-S2-C3
      - P3-S2-C8
      - P4-S2-C8
      - P5-S1-C7
      - P5-S3-C2
      - P6-S3-C2
      - P7-S1-C2
      - P7-S1-C5
      - P7-S1-C6
      - P8-S1-C6
      - P8-S2-C2
      - P8-S3-C3
      - P9-S2-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P1-S1-C6
      - P2-S2-C4
      - P3-S1-C9
      - P3-S2-C8
      - P4-S2-C2
      - P4-S3-C1
      - P4-S3-C2
      - P4-S3-C3
      - P5-S1-C1
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C6
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C7
      - P6-S1-C9
      - P6-S2-C1
      - P6-S2-C4
      - P6-S3-C2
      - P7-S1-C2
      - P7-S1-C8
      - P8-S1-C6
      - P9-S2-C7
      - P10-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C7
      - P1-S1-C9
      - P1-S1-C10
      - P2-S3-C5
      - P2-S4-C2
      - P3-S2-C10
      - P3-S2-C11
      - P3-S3-C1
      - P3-S3-C2
      - P4-S1-C5
      - P4-S2-C8
      - P4-S2-C10
      - P4-S3-C4
      - P4-S3-C5
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C7
      - P6-S1-C9
      - P6-S2-C1
      - P6-S2-C4
      - P6-S2-C8
      - P6-S3-C2
      - P7-S1-C2
      - P7-S1-C5
      - P7-S1-C6
      - P8-S1-C3
      - P8-S1-C4
      - P8-S1-C6
      - P9-S2-C7
      - P9-S2-C10
      - P9-S3-C4
      - P10-S1-C2
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C10
      - P3-S1-C5
      - P4-S1-C3
      - P4-S2-C3
      - P4-S3-C3
      - P5-S1-C3
      - P6-S1-C6
      - P6-S1-C9
      - P6-S2-C4
      - P6-S2-C8
      - P6-S2-C11
      - P6-S3-C2
      - P7-S1-C3
      - P7-S1-C6
      - P8-S1-C1
      - P8-S1-C6
      - P8-S2-C2
      - P8-S2-C5
      - P8-S2-C7
      - P8-S2-C9
      - P8-S4-C10
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C9
      - P9-S2-C8
      - P9-S3-C4
      - P10-S1-C3
      - P10-S1-C6
      - P10-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
      review_sha256: 43a046f4ecf8593b8c0b1238adb333ff1d7421706bf23d2026b6ee08df55e5a2
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
    approved: false
    core_review:
      own_result_source_ids:
      - P8-S3-C2
      source_result: The study reports that no clusters were identified in which T2
        brain activation was significantly associated with T2 PC1, PC2, or PC3 scores.
        This is a null finding for the cross-sectional association at the 4-month
        time point.
      result_status: not_detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P8-S3-C2 explicitly states 'We did not identify any clusters
            in which T2 activation was associated with T2 PC1, PC2 or PC3 score.'
            This matches the proposed analysis identity of T2 activation associated
            with T2 PC scores.
          source_ids:
          - P8-S3-C2
          - P4-S3-C1
        direction:
          answer: fits
          reason: The source reports a null result ('did not identify any clusters'),
            which corresponds to the 'no_effect' direction in the draft, meaning no
            statistically detected association. The draft correctly does not claim
            a specific positive or negative direction.
          source_ids:
          - P8-S3-C2
        construct:
          answer: fits
          reason: The exposure is T2 brain activation (fMRI), and the outcome is T2
            PC scores (behavioral). The source confirms T2 activation was related
            to T2 PC scores in separate analyses (P4-S3-C1) and that no clusters were
            found (P8-S3-C2). The patient measurement is functional imaging (fMRI
            activation), not lesion overlap or diffusion.
          source_ids:
          - P8-S3-C2
          - P4-S3-C1
          - P4-S1-C5
        qualifications:
          answer: fits
          reason: The draft includes the qualification that analyses were restricted
            to unlesioned grey matter voxels. This is supported by P4-S2-C6 and P11-S3-C3,
            which state that analyses were restricted to voxels in which no patient
            had a lesion to minimize confounding. This is a material qualifier for
            the null result, as it limits the anatomical scope of the finding.
          source_ids:
          - P4-S2-C6
          - P11-S3-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that exclusion of lesion-affected
            voxels may have missed positive associations with left hemisphere activation
            (P11-S3-C4). This is a material caveat for the null result. No other material
            caveats appear to be missing for this specific null finding.
          source_ids:
          - P11-S3-C4
      optional_pending:
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.time_post_onset
      original: 4 months post-stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 4'
    analysis_identity:
      id: R011
      exposure:
        text: T2 brain activation
      outcome:
        text: T2 PC1, PC2 or PC3 scores
      analysis_label: T2 Activation Association
      relation: association
      evidence_ids:
      - P8-S3-C2
      qualifier_ids: []
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: ed4b49737344893abdc3f801c15ea80ecddedf6a181ab82902bf1790bc944aa8
        source_review: _compare/relationships-2026-11-16/review-current/Stefaniak2022
        source_status_sha256: f44dcdf8a115e12ab7d64b08c8f1ee647bfd3e77a82beeaad8c736dc923b27bf
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'We did not identify any clusters in which T2 activation was

    associated with T2 PC1, PC2 or PC3 score.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
