---
id: pca_vlsm_component_1
name: PCA of VLSM maps (Component 1)
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: cortical_damage_extent
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: cortical_damage_extent
  target_kind: impairment
  claim: The first principal component of the VLSM maps reflects overall lesion volume
    among participants, as evidenced by its strong correlation with the lesion overlay
    map.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 138
    population: stroke survivors with left hemisphere damage
    phase: not_reported
    time_post_onset: at least 6 months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Vascularly constrained lesion sites
  - Potential diaschisis
  - Cortical reorganization
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The first principal component derived from a data
    matrix of unthresholded univariate VLSM maps relating lesion location to 71 neuropsychological
    speech and language subscores. Component 1 explained approximately 47% of the
    total variance in the VLSM maps. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S4-C8, two-model
    agreement, human verification pending): This study relied on lesion data and neuropsychological
    testing

    in 138 stroke survivors with left hemisphere damage to understand

    whether localized brain damage that predicts different patterns of

    speech impairment loads onto ventral and dorsal streams Original text-layer quotation
    is preserved below. PDF image reading (P5-S1-C9, two-model agreement, human verification
    pending): At the time

    of study inclusion, all participants were at least 6 mo poststroke, with a mean

    age at the time of stroke of 57.31 y old (SD = 11.49) and a mean time post-

    stroke of 36.3 mo (SD = 43.6) Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:cortical_damage_extent
  citation: '@Fridriksson2018'
  source_passages:
  - section: Original source P3-S2-C5
    page: 3
    quote: 'Visual inspection of brain maps representing

      Components 1 and 2 suggested that Component 1 reflected

      overall lesion volume among the study participants, because the

      most negative voxel values were located in central structures, such

      as the insula, but gradually became more positive as the map ex-

      tended to cortical areas farther away from center (Fig. 1, Left).'
    supports: claim
  - section: Original source P3-S2-C8
    page: 3
    quote: 'The correlation between the two

      maps was r = −0.78.'
    supports: claim
  - section: Original source P2-S4-C8
    page: 2
    quote: 'This study relied on lesion data and neuropsychological testing

      in 138 stroke survivors with left hemisphere damage to understand

      whether localized brain damage that predicts different patterns of

      speech impairment loads onto ventral and dorsal streams.'
    supports: sample
  - section: Original source P5-S1-C9
    page: 5
    quote: 'At the time

      of study inclusion, all participants were at least 6 mo poststroke, with a mean

      age at the time of stroke of 57.31 y old (SD = 11.49) and a mean time post-

      stroke of 36.3 mo (SD = 43.6).'
    supports: sample
  - section: Original source P2-S4-C3
    page: 2
    quote: 'In contrast,

      our study initially carried out separate univariate VLSM analyses

      for each behavioral factor and then, applied PCA where the inputs

      consisted of VLSM maps depicting the relationship between lo-

      calized brain damage and speech or language impairment.'
    supports: method
  - section: Original source P2-S3-C8
    page: 2
    quote: 'This study is inherently a lesion-

      symptom mapping study and as such, challenged by the same

      limitations of vascularly constrained lesion sites, potential diaschisis,

      and cortical reorganization as described above.'
    supports: limitation
predictor_type: imaging_metric
short_definition: The first principal component derived from a data matrix of unthresholded
  univariate VLSM maps relating lesion location to 71 neuropsychological speech and
  language subscores.
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2018
  proposal_id: R003
  review_status_sha256: b2026977af807504c55692b75a1f28637d739169462489bdc06681fa9b80aa5a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
        A/passages.json: 95ca38637e14a749fdc171711da209a3d175dae179ee92af201c57cd0eb555b8
        A/raw.json: 7c80811418594f5654df9e55811cf26c9c03723b12cb845c9e037acb697db72c
        A/source-units.json: e68dbee10a88cd7b833072a45014d8cbfb947b0c0d3fe0606698804e6538f0a9
        A/full-source-units.json: e68dbee10a88cd7b833072a45014d8cbfb947b0c0d3fe0606698804e6538f0a9
        A/meta.json: cf8fb9e5522d104cf825e7325d21181455fc46fa09ff3e39fa48c022db49eb33
        A/table-images/manifest.json: 8320f629008ae18a068941a7f4e244334c5ff4e67a3879e62f4a5da83ecdfa76
        A/clauses/window-11/raw.json: f49e7673cee57165d54acd4f825a78ea2baf5eef0ece91da544b056855c2de34
        A/clauses/window-11/prompt.txt: 414b53a041c6595857da1fc1b96201d482212df6fade0bab509e55e961f3e580
        A/clauses/window-11/meta.json: 78fb13731cc7936d149f12da88af08615bfaac5e1e19256aa65102c29e1d49eb
        A/clauses/window-10/raw.json: 6d80e01f4d6c45c9193be032d8007cd9e2ce8cf57c1323ff56dd60635dcae4da
        A/clauses/window-10/prompt.txt: e584be75c9cbf8ee528ec75b00cc0118c05d5b309a2ef45d92a46c42c3539de8
        A/clauses/window-10/meta.json: 63cb986ead5c1bff2aa7ecb825989cb8cfa706e710d9a3e088761de1fd2e2ddd
        A/clauses/window-03/raw.json: 4eadc140373b547027d2bbe1b4f7ae0d960706cba4ff50c2a66849060b842e1c
        A/clauses/window-03/prompt.txt: 1e541c2a0ac689100c7f6f9a17117a956403d7f2f9ae28de9e6766ba98748479
        A/clauses/window-03/meta.json: b3e38ee55df2a33535a205543e2ef6d7359ebc9ed7542f997cd3244268a63a62
        A/clauses/window-04/raw.json: cd0894f5321480e7e588559a69b21024f65901f2aa17432e59041d05d402c245
        A/clauses/window-04/prompt.txt: 4c3f9c17ce075cc597a831c60730cd9c43f2adb1c585de5635ac77ffadee9daf
        A/clauses/window-04/meta.json: a4c42f729daa2c775c845bb65598c79c07f3d4b36a16f2bf9ec9244f32d37146
        A/clauses/window-05/raw.json: f3234a89202bbc304911ffafec5f27ae5d413c016cfc6171d2ac18f274fd460d
        A/clauses/window-05/prompt.txt: e2914cea537d03e73768268be076a82498b2dcf0a0c2af7cf6a2aa6822420cf8
        A/clauses/window-05/meta.json: a8ef1e25554394caf12dd193fa376db70fcd907f2502cfa9a32f94a87f3d8f9d
        A/clauses/window-02/raw.json: 097b1680d497146a0341428fb7eaa72adabcba6240ff194e168b1e96dbecd5fc
        A/clauses/window-02/prompt.txt: 015fab341239f0880b45c87428c376629fd4abf82ec3a74af4bafca2469f8554
        A/clauses/window-02/meta.json: a92d0163cca016bc281272194998367cbcd02a7d6222f24ff56957276879b26b
        A/clauses/window-09/raw.json: 4f09d800cc1a21dbfac586196f351837de8cc201c2eee58fa3de6bb7b1739bd8
        A/clauses/window-09/prompt.txt: 484fae2764b3d633eb581b7d938fe418c6b6bef05fa22174dee3ac040a03f421
        A/clauses/window-09/meta.json: 74bdee9ec4dd2f6b20327dd119c8308da89c8578f50aeb164729479b01eebdca
        A/clauses/window-07/raw.json: a0f599673e74a2c4faeac7c8c4175304a32fd97ccf5dc541ad7021feb217ae58
        A/clauses/window-07/prompt.txt: 1e3bd077196ae4a18f67ed5faefae85479e2ae4a4a3d5b1f390a4314b2f8d8ff
        A/clauses/window-07/meta.json: 1a9e44d6093f3c28b94a08826c3b58e5391492d5653d09346c27817693ae42d8
        A/clauses/window-01/raw.json: 4f34be8e8fd9f391da9485975c1d0ac696ea99b5092b2f2d8e507677f84d46c8
        A/clauses/window-01/prompt.txt: 8e45f707d8cd2be4ecfe0e7252ddd2039c93901dd770de79fb14150a87272736
        A/clauses/window-01/meta.json: b7168d36973650b160174bc51ec12ff8e152f9237527bf4c656191818685af78
        A/clauses/window-06/raw.json: 2306a430b0501820d0a5d387df72791f4da5332a0cea6faf484c5f6492c0cb2f
        A/clauses/window-06/prompt.txt: a0593ba2e7735a71334bc8fe26dda10d2bc31d8639c47abd6bc7f994637a73ca
        A/clauses/window-06/meta.json: ebc7c92b44b017556c3514c09c354f8e26543f688d6325bd91243a0b7a344f7b
        A/clauses/window-08/raw.json: 096af4d49bb43bc6e44b5bbc85f4f12ddfe6e16a878e31046ce6ec88ea612955
        A/clauses/window-08/prompt.txt: 5fd4c7ad8201853d8b23f3f982b011de0c6cdbbff05490b22273263370433ec6
        A/clauses/window-08/meta.json: cc6c1434c22bc3f6126d9f855f4b2c2122f7c1c1704097a77aa8b8f6e12acfc0
        B/passages.json: 95ca38637e14a749fdc171711da209a3d175dae179ee92af201c57cd0eb555b8
        B/raw.json: ab70a60b69645afff4edff3f3ee8c90357186305ac8ff8231f427cfaf28b52c4
        B/source-units.json: e68dbee10a88cd7b833072a45014d8cbfb947b0c0d3fe0606698804e6538f0a9
        B/full-source-units.json: e68dbee10a88cd7b833072a45014d8cbfb947b0c0d3fe0606698804e6538f0a9
        B/meta.json: e4e17c7b6b39bdc4e71ac87f9097151d040f6648243dd08ae3707136cbd3bcfe
        B/table-images/manifest.json: 8320f629008ae18a068941a7f4e244334c5ff4e67a3879e62f4a5da83ecdfa76
        B/clauses/window-11/raw.json: cb3251edf92154b81392b330930242a290ab39e820aecc49247ec64620e4019e
        B/clauses/window-11/prompt.txt: 414b53a041c6595857da1fc1b96201d482212df6fade0bab509e55e961f3e580
        B/clauses/window-11/meta.json: 2a335d8c445800c09895a9b9f561b25669f8c07cf761840b83a1fde88fcac545
        B/clauses/window-10/raw.json: 30d6fac4d5e12f425af6d64414628372e9413587cee4a3bb909a57683f9df5cc
        B/clauses/window-10/prompt.txt: e584be75c9cbf8ee528ec75b00cc0118c05d5b309a2ef45d92a46c42c3539de8
        B/clauses/window-10/meta.json: 7fa8da7fe322514e7f423085258db7fd17ff144db0849189cdb491ab343b6198
        B/clauses/window-03/raw.json: f20af349c09ff4c6e80516519aed93dbea1cea4aff1f14009a907a924ec04d4c
        B/clauses/window-03/prompt.txt: 1e541c2a0ac689100c7f6f9a17117a956403d7f2f9ae28de9e6766ba98748479
        B/clauses/window-03/meta.json: 85700fe6dcfbaa7b1ef31d9669305ce596f03faa6fc7d0b2a596763dbea16a37
        B/clauses/window-04/raw.json: 397df8e8a67ed1117879a85cce022c033bdbd0197f12db34abe30983fa1a7f48
        B/clauses/window-04/prompt.txt: 4c3f9c17ce075cc597a831c60730cd9c43f2adb1c585de5635ac77ffadee9daf
        B/clauses/window-04/meta.json: fb34d805996892a74676f5f091e3081d70c31f048482e9cab6f201162f54385c
        B/clauses/window-05/raw.json: e7c629208fa880d344cc6cf45e1ef608c2e43a7e1724db36d938b77e037aa382
        B/clauses/window-05/prompt.txt: e2914cea537d03e73768268be076a82498b2dcf0a0c2af7cf6a2aa6822420cf8
        B/clauses/window-05/meta.json: d3813eba17fdf3afaab315a16ef19fb3d4fca80140383a013d227a1a304b25dd
        B/clauses/window-02/raw.json: 3d4653a0ab43c8a9494f90d601344b578feb0e989379f01f7c5d11ffb592e524
        B/clauses/window-02/prompt.txt: 015fab341239f0880b45c87428c376629fd4abf82ec3a74af4bafca2469f8554
        B/clauses/window-02/meta.json: 4fc7bab1b6221a6ea2496e2c4e78e02c25e1b979f1cf1f747cfe6e02187638a1
        B/clauses/window-09/raw.json: af2152032d4e30d8475e07007e52969004187e8299c527243483c4a29bd8c696
        B/clauses/window-09/prompt.txt: 484fae2764b3d633eb581b7d938fe418c6b6bef05fa22174dee3ac040a03f421
        B/clauses/window-09/meta.json: cb08f1367966d434368b9fe8a497a3e2d966ecefaaae34253228c72bd2cf8cc6
        B/clauses/window-07/raw.json: a499701f8e715b1828c16b0fcd609e9064a069ff3258e5925af5220beebdfcac
        B/clauses/window-07/prompt.txt: 1e3bd077196ae4a18f67ed5faefae85479e2ae4a4a3d5b1f390a4314b2f8d8ff
        B/clauses/window-07/meta.json: 6fae293b90dd18ec85d326c49d73c8385b43ca9eb6c8aca67ae720ae1d3fe291
        B/clauses/window-01/raw.json: 684b6de52cc792f4d2974515e3e769388cc044c6e5776d44bfa0a4778031e94b
        B/clauses/window-01/prompt.txt: 8e45f707d8cd2be4ecfe0e7252ddd2039c93901dd770de79fb14150a87272736
        B/clauses/window-01/meta.json: 7136e7f8c8f7d4aa6799e4aea2ec1320dd2f7259d21ccf6902d0fe59d4d965c5
        B/clauses/window-06/raw.json: dfb1cb3bca4b5ea7e4ac0017f5b3a711ca38ef6b46b6ae31cd30dcef852c1420
        B/clauses/window-06/prompt.txt: a0593ba2e7735a71334bc8fe26dda10d2bc31d8639c47abd6bc7f994637a73ca
        B/clauses/window-06/meta.json: e54ce3eb7aab13827395911fadea448a719129b7b007a57c4e47c672bca41acf
        B/clauses/window-08/raw.json: b603fb5ccc664c32a5b053d69106df9b2139ad571c35f5bbb31933def00a2cd0
        B/clauses/window-08/prompt.txt: 5fd4c7ad8201853d8b23f3f982b011de0c6cdbbff05490b22273263370433ec6
        B/clauses/window-08/meta.json: 429d64b1b0fead94abfe78e219fea41322f58164621e0efd0da754bf8e6a157a
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
      pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018
      source_status_sha256: a7e9177c96c23a10f709afdb1edeb46aa594bcc6de716b76cf715646c23b16cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: overall lesion volume
    outcome:
      text: cortical damage extent
    analysis_label: PCA of VLSM maps (Component 1)
    relation: association
    evidence_ids:
    - P3-S2-C5
    - P3-S2-C8
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
      pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018
      source_status_sha256: a7e9177c96c23a10f709afdb1edeb46aa594bcc6de716b76cf715646c23b16cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C11
      - Result passage disposed without unit P3-S1-C12
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P3-S1-C14
      - Result passage disposed without unit P3-S1-C15
      - Result passage disposed without unit P3-S1-C16
      - Result passage disposed without unit P3-S1-C9
      - Result passage disposed without unit P3-S3-C5
      - Accounting without a linked unit P4-S1-C10
      - Accounting without a linked unit P4-S1-C3
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S2-C3
      - Accounting without a linked unit P4-S2-C4
      - Unaccounted source passage P4-S1-C10
      - Unaccounted source passage P4-S1-C3
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C5
      - Unaccounted source passage P4-S2-C4
      - Unaccounted source passage P4-S2-C3
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P6-S1-C9
      unattached_null_or_qualifier_ids:
      - P3-S3-C5
      - P4-S2-C4
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 252
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P2-S1-C4
        - P2-S1-C5
        - P2-S2-C5
        - P2-S2-C6
        - P2-S2-C7
        - P2-S2-C8
        - P2-S2-C9
        - P2-S2-C10
        - P2-S2-C12
        - P2-S3-C8
        - P2-S4-C6
        - P4-S3-C7
        - P4-S3-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
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
        - P3-S4
        - P4-S1
        - P4-S2
        - P4-S4
        - P5-S1
        - P5-S5
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018
      source_status_sha256: a7e9177c96c23a10f709afdb1edeb46aa594bcc6de716b76cf715646c23b16cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Establishes anatomical boundaries for dorsal and ventral streams.
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Characterizes the pathways but is a restatement of the findings.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses bias in task support.
    - source_id: P1-S4-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports results of distinct anatomical boundaries for the two pathways.
    - source_id: P1-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance percentages.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance percentages.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance percentages.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings.
    - source_id: P3-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Qualifies the split between positive and negative loadings in Component
        2.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Links negative loadings to motor/phonological and positive to comprehension/naming.
    - source_id: P3-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies negative loadings associated with apraxia and articulation
        errors.
    - source_id: P3-S1-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies positive loadings associated with sentence and auditory comprehension.
    - source_id: P3-S1-C16
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies positive loadings associated with semantic/phonological naming
        errors.
    - source_id: P3-S1-C17
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Suggests negative loadings reflect form-to-articulation and positive
        reflect form-to-meaning.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Links Component 1 to overall lesion volume.
    - source_id: P3-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Provides correlation coefficient for Component 1 and lesion overlay.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation for Component 2 and lesion overlay.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Component 2 spatial pattern.
    - source_id: P3-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies anatomical regions for negative loadings (dorsal stream).
    - source_id: P3-S2-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies anatomical regions for positive loadings (ventral stream).
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies parietal and frontal regions for positive loadings.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of uncinate fasciculus coverage.
    - source_id: P3-S3-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Confirms results were not driven by vascular distribution.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of ventral stream anchors.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with Rauschecker and Scott model.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with Hickok and Poeppel model.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Functional role of pars opercularis/triangularis.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of dorsal stream regions.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Verification that findings were not driven by vascular boundaries.
    - source_id: P4-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Conclusion that Component 2 reflects neuroanatomical divisions.
    - source_id: P4-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of ventral stream and paraphasias.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of ventral stream anatomy.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of dorsal stream anatomy.
    - source_id: P5-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting number of significant univariate VLSM analyses.
    - source_id: P5-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting number of significant univariate VLSM analyses.
    - source_id: P5-S5-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 3 (lesion overlay).
    - source_id: P5-S5-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 3 (lesion overlay).
    - source_id: P5-S5-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 3 (lesion overlay).
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Results of the binary lesion PCA.
    unresolved_coverage:
    - source_id: P3-S1-C17
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P3-S2-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S4-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P1-S4-C4
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S1-C11
    - P3-S1-C12
    - P3-S2-C9
    - P3-S2-C11
    - P3-S3-C3
    - P4-S1-C3
    - P4-S1-C5
    - P4-S1-C8
    - P4-S1-C10
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C10
    - P4-S4-C3
    - P4-S4-C9
    - P5-S1-C1
    - P5-S1-C2
    - P5-S3-C14
    - P5-S4-C3
    - P5-S5-C7
    - P5-S5-C8
    - P5-S5-C9
    - P6-S1-C9
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
      - P2-S4-C8
      - P3-S1-C4
      - P5-S1-C7
      recruited_sample:
      - P5-S1-C6
      - P5-S1-C7
      eligibility:
      - P5-S1-C9
      imaging_provenance:
      - P5-S2-C7
      imaging_timing:
      - P5-S2-C7
      outcome_timing:
      - P5-S1-C9
      outcome_definition:
      - P3-S1-C4
      - P5-S4-C3
      validation: []
      analysis_restrictions:
      - P5-S3-C11
      - P5-S5-C10
      dependent_variable_statement:
      - P3-S1-C4
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S4-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C9
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P2-S1-C4
      - P2-S1-C5
      - P2-S2-C5
      - P2-S2-C6
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C10
      - P2-S2-C12
      - P2-S3-C8
      - P2-S4-C6
      - P4-S3-C7
      - P4-S3-C8
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
      pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
      review_sha256: b2026977af807504c55692b75a1f28637d739169462489bdc06681fa9b80aa5a
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
      - P3-S2-C5
      - P3-S2-C8
      source_result: Component 1 of the PCA of VLSM maps was interpreted as reflecting
        overall lesion volume/cortical damage extent, supported by a strong negative
        correlation (r = -0.78) with the lesion overlay map of all 138 participants.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the PCA of VLSM maps,
            specifically Component 1, and its relationship to the lesion overlap map
            as described in the source.
          source_ids:
          - P3-S2-C5
          - P3-S2-C8
          - P5-S4-C6
        direction:
          answer: fits
          reason: The source states Component 1 reflects overall lesion volume and
            has a strong negative correlation with the lesion overlay map (r = -0.78).
            The draft's claim that it 'reflects overall lesion volume' is consistent
            with this finding.
          source_ids:
          - P3-S2-C5
          - P3-S2-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as overall lesion volume (via
            the correlation with the overlay map) and the outcome as cortical damage
            extent. The method is correctly identified as PCA of VLSM maps. The patient
            measurement is template_lesion_overlap, as the correlation is with a lesion
            overlay map from the participants, not a diffusion-based tract map.
          source_ids:
          - P3-S2-C5
          - P3-S2-C7
          - P3-S2-C8
        qualifications:
          answer: fits
          reason: The draft includes the qualification that Component 1 explained
            ~47% of variance, which is accurate. The limitations listed (vascular
            constraints, diaschisis, reorganization) are general limitations of the
            study mentioned in the source, not specific to this analysis, but are
            not incorrect as general context.
          source_ids:
          - P3-S1-C7
          - P2-S3-C8
        missing_material_caveat:
          answer: fits
          reason: No material caveats specific to the interpretation of Component
            1 as lesion volume are missing. The source explicitly states this interpretation
            and supports it with the correlation.
          source_ids:
          - P3-S2-C5
          - P3-S2-C10
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: overall lesion volume
      outcome:
        text: cortical damage extent
      analysis_label: PCA of VLSM maps (Component 1)
      relation: association
      evidence_ids:
      - P3-S2-C5
      - P3-S2-C8
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
        pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018
        source_status_sha256: a7e9177c96c23a10f709afdb1edeb46aa594bcc6de716b76cf715646c23b16cd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ac54861c630909d4fe8c0a17f1530f2334fdd5d24b029eae844f1bb8f5913e2b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C8
          page: 2
          text_layer_sha256: ac54861c630909d4fe8c0a17f1530f2334fdd5d24b029eae844f1bb8f5913e2b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'This study relied on lesion data and neuropsychological testing

          in 138 stroke survivors with left hemisphere damage to understand

          whether localized brain damage that predicts different patterns of

          speech impairment loads onto ventral and dorsal streams.'
        anchor_text: 'This study relied on lesion data and neuropsychological testing

          in 138 stroke survivors with left hemisphere damage to understand

          whether localized brain damage that predicts different patterns of

          speech impairment loads onto ventral and dorsal streams.'
        excluded_fragments: []
        image_sha256: e84597831b338aecaa797b43ceca1a5d2a145abe9d0864c86221c6b955455370
        transcription: 'This study relied on lesion data and neuropsychological testing

          in 138 stroke survivors with left hemisphere damage to understand

          whether localized brain damage that predicts different patterns of

          speech impairment loads onto ventral and dorsal streams'
      P5-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a853a922808ef950fab87b4ca30132d10ae8ff1023d57cd44cf29f03fc991ca1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 79148e92131960cd5d410d15e4c2cd6b3926c1bdab8facc09ff0b5f30ba62e44
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C9
          page: 5
          text_layer_sha256: 79148e92131960cd5d410d15e4c2cd6b3926c1bdab8facc09ff0b5f30ba62e44
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'At the time

          of study inclusion, all participants were at least 6 mo poststroke, with
          a mean

          age at the time of stroke of 57.31 y old (SD = 11.49) and a mean time post-

          stroke of 36.3 mo (SD = 43.6).'
        anchor_text: 'At the time

          of study inclusion, all participants were at least 6 mo poststroke, with
          a mean

          age at the time of stroke of 57.31 y old (SD = 11.49) and a mean time post-

          stroke of 36.3 mo (SD = 43.6).'
        excluded_fragments: []
        image_sha256: 7ac2aa4972bd058196707508f799a3b7030120c4d2cf791da10bdcd6056ef9aa
        transcription: 'At the time

          of study inclusion, all participants were at least 6 mo poststroke, with
          a mean

          age at the time of stroke of 57.31 y old (SD = 11.49) and a mean time post-

          stroke of 36.3 mo (SD = 43.6)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'Visual inspection of brain maps representing

    Components 1 and 2 suggested that Component 1 reflected

    overall lesion volume among the study participants, because the

    most negative voxel values were located in central structures, such

    as the insula, but gradually became more positive as the map ex-

    tended to cortical areas farther away from center (Fig. 1, Left).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
