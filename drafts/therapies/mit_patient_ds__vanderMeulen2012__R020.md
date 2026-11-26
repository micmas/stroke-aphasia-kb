---
id: mit_patient_ds
name: Melodic Intonation Therapy (Patient DS)
kind: therapy
findings:
- id: f1
  target: language_improvement
  target_kind: prognosis
  claim: No language improvement was found for patient DS, including in the repetition
    of trained utterances, despite the patient showing a facilitating effect of the
    MIT technique during treatment sessions.
  direction: no_effect
  relationship: treatment_response
  method: behavioral_only
  sample:
    n: not_reported
    population: Young Dutch-speaking woman with severe nonfluent aphasia and relatively
      good language comprehension following a left hemorrhagic cerebrovascular accident
    phase: not_reported
    time_post_onset: MIT started at 8-months poststroke; assessed pre- and post-6
      weeks of intensive therapy
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Case study of a single individual
  evidence_quality: case-study
  strength: weak
  notes: 'Exposure measurement: Intensive Melodic Intonation Therapy (3–5h/wk) for
    6 weeks, consisting of training verbal production by repeating melodically intoned
    phrases while rhythmically tapping the patient''s hand, with a gradual decrease
    in support from the speech-language pathologist until independent production and
    the final replacement of singing by speaking. Patient fit the classical profile
    of MIT candidates (nonfluent aphasia, poorly articulated speech, severe disorders
    in language repetition, and relatively good auditory language comprehension);
    Patient showed a facilitating effect (ability to sing short utterances and produce
    trained utterances more fluently) during the therapy sessions. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P4-S4-C9, two-model agreement, human verification pending): MIT
    was started at 8-months poststroke Original text-layer quotation is preserved
    below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
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
    - not_transcribed:sample.n
    - proposed_concept:language_improvement
  therapy:
    id: mit
    name: Melodic Intonation Therapy
  citation: '@vanderMeulen2012'
  source_passages:
  - section: Original source P5-S2-C11
    page: 5
    quote: 'No language improvement was found for patient DS, not even

      in repeating trained utterances.'
    supports: claim
  - section: Original source P5-S1-C12
    page: 5
    quote: 'They received intensive MIT (3–5h/wk) for

      6 weeks.'
    supports: method
  - section: Original source P4-S4-C9
    page: 4
    quote: MIT was started at 8-months poststroke.
    supports: sample
  - section: Original source P5-S1-C14
    page: 5
    quote: 'Pre- and posttreatment the following tests

      were administered: repetition of trained and untrained phrases,

      the subtests repetition, action naming, and auditory language

      comprehension of the Aachen Aphasia Test (AAT),47 the Am-

      sterdam-Nijmegen Everyday Language Test (ANELT),48 and

      the Sabadel story retell task.49 The latter tasks examine the

      effect of MIT on patients’ functional communication.'
    supports: method
  - section: Original source P5-S2-C6
    page: 5
    quote: 'From the start, MIT facilitated speech production in both

      patients.'
    supports: confounders
  - section: Original source P5-S1-C8
    page: 5
    quote: 'Neverthe-

      less, they both ﬁt the classical proﬁle of MIT candidates,

      deﬁned in the literature as meeting at least 3 of the following

      criteria: nonﬂuent aphasia, poorly articulated speech, severe

      disorders in language repetition, and relatively good auditory

      language comprehension.11,12 Despite their severe language

      production deﬁcits, both patients were eager to communicate.'
    supports: confounders
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: vanderMeulen2012
  proposal_id: R020
  review_status_sha256: 2668efd9d361ad19f3d2022a34a123fee2044f4c6037324a3ed871b718569c82
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
        A/passages.json: 30fad166320ad7eed25bdef70653c8886c3b463b92e3028b8ca61d1746de2888
        A/raw.json: 7325bbfe4bdbaa2ed0fa0298d6cbae6a6c95e3f41209507de878064e24031f3d
        A/source-units.json: 2d5381ae2dcfbfdc1f85c6d0467eb398f4af5c3165185372a6406f48065af945
        A/full-source-units.json: 9510214d9330f4835c901481de4c6d1af9da211cf21de767a1606ce40e26d10f
        A/meta.json: 7f7708bf3fcb4575c26ba283c979cc29888e8956769e750f85335af8891a1201
        A/table-images/TABLE-1-page-3-1.png: 82b4e4464d3bd63e03e4769c176e0f59e1ab941ebcd624e2fe3eca6812151f8a
        A/table-images/page-3.png: b6142c6de13cfd30c896f072ab07e3117b7eed2a22f3f6e38e22d3b271f7061b
        A/table-images/page-5.png: db8efcfa9c645f0cd57a88217e8a7019747db2b64d11faebfde4677691b6345c
        A/table-images/manifest.json: 0100dd877f6e3789318308b22c85aec4219834df8765291e21ab97327f3825f0
        A/table-images/TABLE-2-page-5-1.png: 97fa886a42e4cda4af0943722aea6227ca9da1c74d4aec78d6fcdc386d3d41d6
        A/clauses/window-03/raw.json: 16123ad9d1fd80cbc052050970aaed0097971ffa96954e2c06cf38049aae3a6f
        A/clauses/window-03/prompt.txt: a6f4c0392870b5aad37be4e60da724eaeb8d5777274b02aa615eed501027f8fd
        A/clauses/window-03/meta.json: cef8d4d6822ad694f69a56951382c857d0250c3bc1f5aa9f7492aebceb7d770c
        A/clauses/window-04/raw.json: 34eb9d6809a2b50a7c14b889cfaef523eecb7e6f9037f9f185c4c0fc659c43ab
        A/clauses/window-04/prompt.txt: 667275bd0c11403c3607d38525c5af64e85e4d21eb3886dbe4911dac4e0e3020
        A/clauses/window-04/meta.json: 53a0b3ccf688cdc54c1d995a8b996556001978fef8658e5fae0fac7b2f90e3ad
        A/clauses/window-05/raw.json: f808ad2d82d83aab05e09482e85a775c4c9a9baa482022d43b937adfeeb3bd66
        A/clauses/window-05/prompt.txt: 25de80e3f8bd3327aae51e6a1b5479ecf79eea43280319ecaf2866c72b55714e
        A/clauses/window-05/meta.json: 40dbec4e07bb82ea3fae790a4d81e879b58b2ba6ae05a4453829f98d3dfedb98
        A/clauses/window-02/raw.json: 86ea0c48df04983aa4db3126b2709b013de8f17a0f2e52017fc6143392431429
        A/clauses/window-02/prompt.txt: 83194f7ae7f6b45fffe915207b6e55b1cf25de896e47b6f148d79bbcd9c06d39
        A/clauses/window-02/meta.json: e97478dd98a7fbf5eef331808d4175943663c9d4abc7c7caa4771630fa991964
        A/clauses/window-07/raw.json: 43410a16fa78387ecefa64c26cffdeec14723f454a3b48a4069fa1e7c799afc2
        A/clauses/window-07/prompt.txt: a6fcb0e24063b2cdda565919446e3e474ce24691654a0a1fbbe5d33b592fb82c
        A/clauses/window-07/meta.json: 8c006fcbcdcb84c4706447fb5e0b76de004ce975291266afec4a33432f4ba496
        A/clauses/window-01/raw.json: 897fb1a314dc52249f8100cce60d4617a474178351a2bf0413886680320ff0c8
        A/clauses/window-01/prompt.txt: f0d1a32d61c9ad066fce9b8bd3dbe1c033f11aeb5809ebb599d530277fdc5459
        A/clauses/window-01/meta.json: 40a111299f2e5efc8b2931953bd246e902836df31599dc91019c271cf6d7e19f
        A/clauses/window-06/raw.json: ad7844549677fa6a791a0dd2343eb4708a113a7d31c18334e0e4a00f1e16da85
        A/clauses/window-06/prompt.txt: f53e49106ea0084fc0108d8581d3c33a09a8ec696297fd5d2f3ccbe155f82262
        A/clauses/window-06/meta.json: 6354250b9155a8b5fb1da9872547693d477e49315b9256b04f2d7abad4cb6d7f
        A/tables/TABLE-2-page-5-2/raw.json: 79cb65ae7c1b17b742f8cdc9a42b96751f9d365ef703ff6831f61a5faa003388
        A/tables/TABLE-2-page-5-2/prompt.txt: 390f8dace939f5ded296170376e33ee3ccd95d3752a7edb01fac93cb7609761e
        A/tables/TABLE-2-page-5-2/meta.json: 28ffad826e51af00c229a4519e2bf8f21c27945b223afd7e9edac1b64e789fb7
        A/tables/TABLE-1-page-3-1/raw.json: 67f1f785d60a6d7089b52db30477387a94d03e31a4ce0bebf476755d2c2388a4
        A/tables/TABLE-1-page-3-1/prompt.txt: ddd95aaf08459a9e101b0b23d9e4cd736eb88ec1e89275e95aa4786157c3a099
        A/tables/TABLE-1-page-3-1/meta.json: b860990b34f7187c0526ead4ca520fe7de24fce6635c3fe82f6022e8f1050704
        B/passages.json: 30fad166320ad7eed25bdef70653c8886c3b463b92e3028b8ca61d1746de2888
        B/raw.json: 5bb8d08332eda94362933fd8837c34c668ac15135d395133f40e9b45ca899eca
        B/source-units.json: 2d5381ae2dcfbfdc1f85c6d0467eb398f4af5c3165185372a6406f48065af945
        B/full-source-units.json: 9510214d9330f4835c901481de4c6d1af9da211cf21de767a1606ce40e26d10f
        B/meta.json: 236907df9ee6f4a13d020163842d174d82e774f39b7cd7e56978c87b51f90121
        B/table-images/TABLE-1-page-3-1.png: 82b4e4464d3bd63e03e4769c176e0f59e1ab941ebcd624e2fe3eca6812151f8a
        B/table-images/page-3.png: b6142c6de13cfd30c896f072ab07e3117b7eed2a22f3f6e38e22d3b271f7061b
        B/table-images/page-5.png: db8efcfa9c645f0cd57a88217e8a7019747db2b64d11faebfde4677691b6345c
        B/table-images/manifest.json: d70d4abf12da1d936304a9f47641ca0ac8f632a24a54e0f530429a24b68e5d8c
        B/table-images/TABLE-2-page-5-1.png: 97fa886a42e4cda4af0943722aea6227ca9da1c74d4aec78d6fcdc386d3d41d6
        B/clauses/window-03/raw.json: 3498ae024e5872409ebe4ee5a0a72f9603f8630f5783887fa270e10e4687abb3
        B/clauses/window-03/prompt.txt: a6f4c0392870b5aad37be4e60da724eaeb8d5777274b02aa615eed501027f8fd
        B/clauses/window-03/meta.json: 245f87c6f316e79c8bf1655d88979c771a825e8c3bfc96a38d31b6db41d242c4
        B/clauses/window-04/raw.json: 470bf2061968e87ded79d7e75565c2e2eeabf24511cfad18ebb4d58cf8b26748
        B/clauses/window-04/prompt.txt: 667275bd0c11403c3607d38525c5af64e85e4d21eb3886dbe4911dac4e0e3020
        B/clauses/window-04/meta.json: 3e50ca703c66299f29ce51300bcf5f6ce718e1577da852d16431f5e625e1c562
        B/clauses/window-05/raw.json: e0ff5d9cba2dcedc312b0499df7972ebe64ae8aa6ff22df636a373b5de6bfa83
        B/clauses/window-05/prompt.txt: 25de80e3f8bd3327aae51e6a1b5479ecf79eea43280319ecaf2866c72b55714e
        B/clauses/window-05/meta.json: 535dd0b0e4a071fdf0de18c79227c00e380fa78fddc5be2c29c14fe1082eae32
        B/clauses/window-02/raw.json: 7deeeeffe7f33a0fc87372827c33272702958432f3040c2b63f1a69d8a9905e6
        B/clauses/window-02/prompt.txt: 83194f7ae7f6b45fffe915207b6e55b1cf25de896e47b6f148d79bbcd9c06d39
        B/clauses/window-02/meta.json: f6209678ede556768b302110023257391530e22be43164167994047fdc3ad632
        B/clauses/window-07/raw.json: 65026438af7d189a788f16b954c1ed38456d90a502bdc7ae6cd96e723ac5bf6d
        B/clauses/window-07/prompt.txt: a6fcb0e24063b2cdda565919446e3e474ce24691654a0a1fbbe5d33b592fb82c
        B/clauses/window-07/meta.json: 0e4517d678e307dbc4a0277a4ed199281c967be00eef37d1686fa23166243a77
        B/clauses/window-01/raw.json: b03ff80e26157a9d2f642e5d845690c7b708f8a5710137c69b888bad9e63d3e9
        B/clauses/window-01/prompt.txt: f0d1a32d61c9ad066fce9b8bd3dbe1c033f11aeb5809ebb599d530277fdc5459
        B/clauses/window-01/meta.json: e754ca63b162a29b4452711fdd693d5642e69a7387441022a4ecd616f19543ba
        B/clauses/window-06/raw.json: 720da7e331a2aa796d9b745545fe30c33181a1b4ec00a75d10a08fff7f2097e2
        B/clauses/window-06/prompt.txt: f53e49106ea0084fc0108d8581d3c33a09a8ec696297fd5d2f3ccbe155f82262
        B/clauses/window-06/meta.json: 0f170922766e6fc6e94fc9809e77b17a2f2a212e4d4059077cb2ce60aac41f2a
        B/tables/TABLE-2-page-5-2/raw.json: 79cb65ae7c1b17b742f8cdc9a42b96751f9d365ef703ff6831f61a5faa003388
        B/tables/TABLE-2-page-5-2/prompt.txt: 390f8dace939f5ded296170376e33ee3ccd95d3752a7edb01fac93cb7609761e
        B/tables/TABLE-2-page-5-2/meta.json: ab3d840a5e476b17b497a996ceccfdae9dae1580c1ade5998c46087ee564a630
        B/tables/TABLE-1-page-3-1/raw.json: 4c1208dd5d6ded5e56397fd9a4015a0b81e919405b2e56662b685366947c8dc1
        B/tables/TABLE-1-page-3-1/prompt.txt: ddd95aaf08459a9e101b0b23d9e4cd736eb88ec1e89275e95aa4786157c3a099
        B/tables/TABLE-1-page-3-1/meta.json: b940b906d8c7911ad4dd5c44b7c6cb42870ed2cd9a5c159b2f0fc07d6f354aec
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2012
      source_status_sha256: 5e28599aa14e457634c5850db9823ea5d100b351d6fe9e109126f44b782cc792
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R020
    exposure:
      text: MIT
    outcome:
      text: language improvement (including repeating trained utterances)
    analysis_label: Patient DS case study
    relation: association
    evidence_ids:
    - P5-S2-C11
    - P5-S3-C17
    qualifier_ids:
    - P5-S1-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2012
      source_status_sha256: 5e28599aa14e457634c5850db9823ea5d100b351d6fe9e109126f44b782cc792
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P2-S2-C3
      - Result passage disposed without unit P2-S2-C4
      - 'window 4: invalid/duplicate disposition P2-S2-C5'
      - Result passage disposed without unit P2-S2-C10
      - Result passage disposed without unit P2-S2-C9
      - 'window 6: invalid/duplicate disposition P2-S2-C14'
      - Result passage disposed without unit P2-S3-C5
      - Result passage disposed without unit P4-S4-C4
      - Result passage disposed without unit P4-S4-C5
      - Result passage disposed without unit P4-S4-C12
      - Result passage disposed without unit P4-S4-C7
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C17
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P5-S3-C5
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P2-S1-C5
      - P2-S2-C5
      - P2-S2-C10
      - P5-S1-C3
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 143
      unselected_timing_passages:
      - P2-S1-C4
      - P2-S2-C15
      - P2-S3-C17
      - P2-S4-C1
      - P4-S4-C2
      - P4-S4-C9
      - P4-S4-C10
      - P5-S1-C7
      - P5-S1-C11
      - P5-S3-C16
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P2-S1-C2
        - P2-S2-C10
        - P2-S2-C11
        - P2-S2-C14
        - P2-S2-C15
        - P2-S3-C7
        - P3-S1-C1
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C4
        - P3-S1-C5
        - P3-S1-C6
        - P3-S2-C1
        - P3-S2-C2
        - P4-S1-C7
        - P4-S1-C10
        - P4-S1-C11
        - P4-S2-C2
        - P4-S2-C3
        - P4-S3-C10
        - P4-S4-C1
        - P4-S4-C8
        - P5-S1-C7
        - P5-S1-C8
        - P5-S2-C15
        - P5-S3-C4
        - P5-S3-C9
        - P5-S3-C11
        - P5-S3-C17
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S2-C16
        - P1-S3-C5
        - P2-S1-C3
        - P2-S2-C11
        - P2-S2-C14
        - P2-S2-C15
        - P2-S3-C7
        - P2-S3-C15
        - P4-S1-C7
        - P4-S1-C10
        - P4-S1-C11
        - P4-S2-C2
        - P4-S2-C3
        - P4-S3-C10
        - P5-S1-C11
        - P5-S2-C15
        - P5-S3-C4
        - P5-S3-C9
        - P5-S3-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P1-S3-C3
        - P1-S3-C5
        - P1-S3-C8
        - P2-S1-C1
        - P2-S1-C5
        - P2-S2-C14
        - P2-S3-C7
        - P5-S1-C11
        - P5-S2-C15
        - P5-S3-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P2-S2-C5
        - P2-S2-C6
        - P2-S3-C9
        - P2-S3-C10
        - P3-S1-C1
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C4
        - P3-S1-C5
        - P3-S1-C6
        - P3-S2-C1
        - P3-S2-C2
        - P5-S2-C6
        - P5-S2-C8
        - P5-S2-C10
        - P5-S2-C11
        - P5-S2-C12
        - P5-S3-C15
        - P5-S3-C16
        - P5-S3-C17
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P2-S1-C6
        - P2-S1-C7
        - P2-S2-C2
        - P2-S2-C7
        - P2-S3-C8
        - P3-S1-C1
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C4
        - P3-S1-C5
        - P3-S1-C6
        - P3-S2-C1
        - P3-S2-C2
        - P4-S2-C3
        - P5-S1-C14
        - P5-S1-C15
        - P5-S1-C16
        - P5-S1-C17
        - P5-S1-C18
        - P5-S2-C14
        - P5-S2-C21
        - P5-S3-C17
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S2-C8
        - P2-S2-C9
        - P2-S2-C12
        - P2-S3-C6
        - P4-S2-C5
        - P4-S2-C6
        - P5-S3-C10
        - P5-S3-C12
        - P5-S3-C17
        - P6-S1-C1
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C11
        - P6-S1-C14
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P2-S1-C4
        - P2-S2-C14
        - P2-S3-C7
        - P4-S1-C4
        - P4-S2-C6
        - P4-S3-C11
        - P4-S4-C1
        - P4-S4-C8
        - P5-S1-C2
        - P5-S1-C7
        - P5-S1-C8
        - P5-S3-C9
        - P5-S3-C11
        - P6-S1-C18
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - eligibility
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2012
      source_status_sha256: 5e28599aa14e457634c5850db9823ea5d100b351d6fe9e109126f44b782cc792
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: States lack of well-designed group studies in general.
    - source_id: P2-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of articles included in review.
    - source_id: P2-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes total number of individuals reported.
    - source_id: P2-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of MIT onset.
    - source_id: P2-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes candidacy criteria.
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes common outcome measures used in studies.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on focus of studies.
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on lack of functional outcome measures.
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Identifies studies using functional outcome measures.
    - source_id: P2-S2-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Supports increase of CIUs after MIT.
    - source_id: P2-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports positive effects overall.
    - source_id: P2-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies evidence as limited by design.
    - source_id: P2-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies evidence as mostly single case/series.
    - source_id: P2-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Identifies group data studies.
    - source_id: P2-S2-C11
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Qualifies Popovici study as combining MIT with reading/writing.
    - source_id: P2-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes classic MIT approach.
    - source_id: P2-S2-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Reports higher improvement on verbal output in MIT patients.
    - source_id: P2-S2-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Describes Springer et al study design.
    - source_id: P2-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Describes Springer et al group sizes.
    - source_id: P2-S2-C16
      disposition: represented
      result_indexes:
      - 3
      reason: Describes Springer et al crossover timing.
    - source_id: P2-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of Springer et al comparison.
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of Springer et al crossover.
    - source_id: P2-S3-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports larger improvement after linguistic approach than MIT.
    - source_id: P2-S3-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports improvement most if linguistic therapy preceded by MIT.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on crossover design.
    - source_id: P2-S3-C7
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Describes Bonakdapour et al study population.
    - source_id: P2-S3-C8
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Describes Bonakdapour et al outcome measures.
    - source_id: P2-S3-C9
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports significant improvement on therapy-related measures and null
        on unrelated.
    - source_id: P2-S3-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports stability of improvement for 1 month.
    - source_id: P2-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites AAN classification.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on quality of evidence.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of need for RCTs.
    - source_id: P2-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists ongoing RCTs.
    - source_id: P2-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ongoing RCT methods.
    - source_id: P2-S3-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of studies.
    - source_id: P4-S4-C4
      disposition: represented
      result_indexes:
      - 19
      reason: Describes Patient VD baseline inability to convey message.
    - source_id: P4-S4-C5
      disposition: represented
      result_indexes:
      - 19
      reason: Describes Patient VD baseline repetition deficit.
    - source_id: P4-S4-C6
      disposition: represented
      result_indexes:
      - 19
      reason: Describes Patient VD baseline naming deficit.
    - source_id: P4-S4-C7
      disposition: represented
      result_indexes:
      - 19
      reason: Describes Patient VD baseline comprehension.
    - source_id: P4-S4-C12
      disposition: represented
      result_indexes:
      - 20
      reason: Describes Patient DS lack of improvement from prior broad therapy.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS diagnosis.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS speech description.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS naming deficit.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS comprehension description.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of patients.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Candidacy profile check.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient nonverbal strategies.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Facilitation during treatment.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Ability to sing utterances.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Transition from singing to speaking.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Difference in therapeutic effect.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 20
      reason: Reports no language improvement for Patient DS.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 19
      reason: Reports improvement in repeating trained utterances for Patient VD.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 19
      reason: Reports significant improvement on AAT verbal production for Patient
        VD.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 19
      reason: Reports improvement in ANELT and Sabadel for Patient VD.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Candidacy profile check.
    - source_id: P5-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Response to technique during therapy.
    - source_id: P5-S2-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on effectiveness.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS enjoyment of therapy.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS experience of producing utterances.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of auditory comprehension between patients.
    - source_id: P5-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient DS profile check.
    - source_id: P5-S3-C17
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Table 2 data for Patient DS and VD.
    unresolved_coverage:
    - source_id: P2-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S2-C16
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C16
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P2-S3-C17
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S4-C12
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S2-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S3-C17
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S1-C8
    - P2-S1-C2
    - P2-S1-C3
    - P2-S1-C4
    - P2-S1-C5
    - P2-S2-C2
    - P2-S2-C3
    - P2-S2-C4
    - P2-S2-C5
    - P2-S2-C6
    - P2-S2-C8
    - P2-S2-C9
    - P2-S2-C10
    - P2-S2-C11
    - P2-S2-C14
    - P2-S2-C15
    - P2-S3-C1
    - P2-S3-C3
    - P4-S4-C4
    - P4-S4-C5
    - P4-S4-C6
    - P4-S4-C7
    - P4-S4-C12
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C9
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C10
    - P5-S2-C15
    - P5-S2-C16
    - P5-S2-C17
    - P5-S3-C4
    - P5-S3-C5
    - P5-S3-C9
    - P5-S3-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility: []
      imaging_provenance:
      - P2-S1-C5
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C6
      - P3-S2-C1
      - P3-S2-C2
      - P4-S1-C4
      - P4-S2-C2
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P1-S3-C6
      - P2-S1-C1
      dependent_variable_statement:
      - P2-S3-C9
      - P4-S2-C3
      - P5-S2-C21
      - P5-S3-C17
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P2-S1-C2
      - P2-S2-C10
      - P2-S2-C11
      - P2-S2-C14
      - P2-S2-C15
      - P2-S3-C7
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P3-S2-C1
      - P3-S2-C2
      - P4-S1-C7
      - P4-S1-C10
      - P4-S1-C11
      - P4-S2-C2
      - P4-S2-C3
      - P4-S3-C10
      - P4-S4-C1
      - P4-S4-C8
      - P5-S1-C7
      - P5-S1-C8
      - P5-S2-C15
      - P5-S3-C4
      - P5-S3-C9
      - P5-S3-C11
      - P5-S3-C17
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S2-C16
      - P1-S3-C5
      - P2-S1-C3
      - P2-S2-C11
      - P2-S2-C14
      - P2-S2-C15
      - P2-S3-C7
      - P2-S3-C15
      - P4-S1-C7
      - P4-S1-C10
      - P4-S1-C11
      - P4-S2-C2
      - P4-S2-C3
      - P4-S3-C10
      - P5-S1-C11
      - P5-S2-C15
      - P5-S3-C4
      - P5-S3-C9
      - P5-S3-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S3-C3
      - P1-S3-C5
      - P1-S3-C8
      - P2-S1-C1
      - P2-S1-C5
      - P2-S2-C14
      - P2-S3-C7
      - P5-S1-C11
      - P5-S2-C15
      - P5-S3-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P2-S2-C5
      - P2-S2-C6
      - P2-S3-C9
      - P2-S3-C10
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P3-S2-C1
      - P3-S2-C2
      - P5-S2-C6
      - P5-S2-C8
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P5-S3-C15
      - P5-S3-C16
      - P5-S3-C17
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P2-S1-C6
      - P2-S1-C7
      - P2-S2-C2
      - P2-S2-C7
      - P2-S3-C8
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P3-S2-C1
      - P3-S2-C2
      - P4-S2-C3
      - P5-S1-C14
      - P5-S1-C15
      - P5-S1-C16
      - P5-S1-C17
      - P5-S1-C18
      - P5-S2-C14
      - P5-S2-C21
      - P5-S3-C17
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C12
      - P2-S3-C6
      - P4-S2-C5
      - P4-S2-C6
      - P5-S3-C10
      - P5-S3-C12
      - P5-S3-C17
      - P6-S1-C1
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C11
      - P6-S1-C14
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P2-S1-C4
      - P2-S2-C14
      - P2-S3-C7
      - P4-S1-C4
      - P4-S2-C6
      - P4-S3-C11
      - P4-S4-C1
      - P4-S4-C8
      - P5-S1-C2
      - P5-S1-C7
      - P5-S1-C8
      - P5-S3-C9
      - P5-S3-C11
      - P6-S1-C18
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
      pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
      review_sha256: 2668efd9d361ad19f3d2022a34a123fee2044f4c6037324a3ed871b718569c82
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
      - P5-S2-C11
      - P5-S3-C17
      source_result: For patient DS, no language improvement was found, not even in
        repeating trained utterances, despite a facilitating effect during therapy
        sessions. This null finding is contrasted with patient VD, who showed improvement.
        The source explicitly states that it is unclear whether the lack of success
        in DS is due to timing (8 months poststroke vs 2 weeks for VD) or other factors,
        and that the effect of MIT in early phases is unknown.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the specific outcome
            for patient DS (no improvement) as distinct from patient VD (improvement).
            The source explicitly contrasts the two cases (P5-S2-C10, P5-S2-C11, P5-S2-C12).
            The analysis is a case study comparison, not a statistical model with
            covariates, so 'robustness' or 'adjustment' concepts do not apply in the
            statistical sense, but the qualitative distinction between the two patients
            is preserved.
          source_ids:
          - P5-S2-C10
          - P5-S2-C11
          - P5-S2-C12
        direction:
          answer: fits
          reason: The claim 'No language improvement was found for patient DS' accurately
            reflects the source statement 'No language improvement was found for patient
            DS, not even in repeating trained utterances' (P5-S2-C11). The direction
            is a null finding (no_effect) for this specific patient, which is correctly
            distinguished from the positive finding for patient VD.
          source_ids:
          - P5-S2-C11
        construct:
          answer: fits
          reason: The exposure is MIT (defined in P1-S1-C12, P5-S1-C12). The outcome
            is language improvement, specifically including repetition of trained
            utterances (P5-S2-C11). The measurement is behavioral (AAT, ANELT, Sabadel,
            repetition tasks) as described in P5-S1-C14 and Table 2 (P5-S3-C17). The
            patient measurement is non_imaging (behavioral tests), not diffusion or
            template overlap.
          source_ids:
          - P1-S1-C12
          - P5-S1-C12
          - P5-S1-C14
          - P5-S3-C17
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the patient showed a facilitating
            effect during sessions (P5-S2-C6, P5-S2-C8, P5-S3-C4) and fit the classical
            profile (P5-S1-C8, P5-S2-C15). It also notes the timing (8 months poststroke,
            P4-S4-C9). The source explicitly states that facilitation does not guarantee
            success (P5-S2-C20), which supports the qualification that the null result
            occurred despite in-session facilitation.
          source_ids:
          - P5-S2-C6
          - P5-S2-C8
          - P5-S3-C4
          - P5-S2-C20
          - P4-S4-C9
        missing_material_caveat:
          answer: fits
          reason: The draft correctly identifies this as a case study (single individual).
            It does not overgeneralize to a population. It does not claim that MIT
            is ineffective for all patients, only for this specific case. The source's
            uncertainty about whether the null result is due to timing or other factors
            (P5-S3-C10, P6-S1-C1) is a limitation of the case study design, but the
            core finding (no improvement for DS) is faithfully represented. The draft
            does not omit a material caveat that changes the interpretation of the
            null result for this patient.
          source_ids:
          - P5-S3-C10
          - P6-S1-C1
      optional_pending:
      - Detailed statistics/coordinates/atlas metadata have NOT been transcribed.
      - Sample size is 1 (case study), not transcribed as a numeric field but implied
        by 'case study'.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Detailed statistics/coordinates/atlas metadata have NOT been transcribed.
    - Sample size is 1 (case study), not transcribed as a numeric field but implied
      by 'case study'.
    normalizations:
    - field: sample.n
      original: 1
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R020
      exposure:
        text: MIT
      outcome:
        text: language improvement (including repeating trained utterances)
      analysis_label: Patient DS case study
      relation: association
      evidence_ids:
      - P5-S2-C11
      - P5-S3-C17
      qualifier_ids:
      - P5-S1-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
        source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2012
        source_status_sha256: 5e28599aa14e457634c5850db9823ea5d100b351d6fe9e109126f44b782cc792
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S4-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fe0249adb6fb1e611bac8b6ca9a5c6e40721415f74e96c9c79f8f9bf32ae48e7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e126effeb80d98913c3b48c152b4c9b9c1fc30386dea7a3c8949766bad26efc5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S4-C9
          page: 4
          text_layer_sha256: e126effeb80d98913c3b48c152b4c9b9c1fc30386dea7a3c8949766bad26efc5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: MIT was started at 8-months poststroke.
        anchor_text: MIT was started at 8-months poststroke.
        excluded_fragments: []
        image_sha256: 4c44b6e464a202917dc7c0171268534869562b8f321996adf49f7e5dd307a227
        transcription: MIT was started at 8-months poststroke
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'No language improvement was found for patient DS, not even

    in repeating trained utterances.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
