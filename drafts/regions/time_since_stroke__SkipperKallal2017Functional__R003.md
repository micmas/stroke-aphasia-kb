---
id: time_since_stroke
name: time since stroke
kind: classical
findings:
- id: f1
  target: pnt_performance
  target_kind: impairment
  claim: Time since stroke significantly predicted naming performance in a hierarchical
    regression model
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 32
    population: chronic left-hemisphere stroke survivors with a history of aphasia
    phase: not_reported
    time_post_onset: at least 6 months after the stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Time elapsed since the occurrence of the stroke. measured
    in the first step of a hierarchical regression; tested alongside PCAD, lesion
    volume, age, sex, education, and handedness. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P3-S2-C14, two-model agreement, human verification pending): . All participants
    in the

    aphasia group were native English speakers, and testing

    occurred at least 6 months after the stroke Original text-layer quotation is preserved
    below. PDF image reading (P3-S3-C3, two-model agreement, human verification pending):
    . Fourteen participants were then excluded based on fMRI task performance (see
    below), resulting in a final sample of 32 participants in the aphasia group (Table
    I and Supporting Information) Original text-layer quotation is preserved below.'
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
    - not_transcribed:author_limitations
    - proposed_concept:pnt_performance
  citation: '@SkipperKallal2017Functional'
  source_passages:
  - section: Original source P8-S1-C7
    page: 8
    quote: 'Time since stroke was also a signiﬁcant predic-

      tor, t(24) 5 2.13, P < 0.05.'
    supports: claim
  - section: Original source P8-S1-C5
    page: 8
    quote: 'The dependent variable

      was number of correct trials in the PNT, and the predic-

      tors were PCAD, lesion volume, time since stroke, age,

      sex, education and handedness.'
    supports: method
  - section: Original source P3-S2-C13
    page: 3
    quote: 'MATERIALS AND METHODS

      Participants

      Forty-six chronic left-hemisphere stroke survivors with a

      history of aphasia were recruited.'
    supports: sample
  - section: Original source P3-S2-C14
    page: 3
    quote: 'All participants in the

      aphasia group were native English speakers, and testing

      occurred at least 6 months after the stroke.'
    supports: sample
  - section: Original source P3-S3-C3
    page: 3
    quote: 'Fourteen participants were then excluded based on

      fMRI task performance (see below), resulting in a ﬁnal

      sample of 32 participants in the aphasia group (Table I

      and Supporting Information).'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: SkipperKallal2017Functional
  proposal_id: R003
  review_status_sha256: 8c8ff230ddbff92164b3656c407b60fbf38da9b90ac196e0f9572981658485cd
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
        A/passages.json: 5d0005517540112eba60c02b27c5465aac9930dff09fcb029e0f0e40bb485d3e
        A/raw.json: 15e82ac1396dd31c80482f4f09685fe5ee07a8db83a703fef64e123b28bb2515
        A/source-units.json: a1a5d10eefcebaa9170f09d44027b4db76c2d17b41bcda9f78c3b4d5afcc5a72
        A/full-source-units.json: ce276a3effbebc0626447565978dbbe5182fc6c166741b29ef9250f54c902b74
        A/meta.json: c8484f3bd93a78395c0bf5805173453280f60100a98c7bacaff0563ac75f875b
        A/table-images/page-4.png: 642e03d409db0f623303cb5b3a9d673f2874584d606a82e01228343adaffaa53
        A/table-images/TABLE-I-page-4-1.png: 577c9d61cadfeafa845defdc0a5d0ddf0490fe023afbe7e941d2f500aae11cc6
        A/table-images/manifest.json: cc145479f6853efa6ba44527f0b6438da4d547084d9a2dcb64a8667d0193025a
        A/clauses/window-11/raw.json: 079ee37f9da5fbd50c18e07e062bd723d09b8782eea9c78b51d5de7d2496590d
        A/clauses/window-11/prompt.txt: 3c7615c1ec9579eaf46105d86564405f7dfc98f8ed4e20262e49a7956aaa9903
        A/clauses/window-11/meta.json: c7bbf200ecf570534bfb631ca4082dd710c1ba3ae4aa31f32825a333592165a8
        A/clauses/window-10/raw.json: b6a08371c1cd0e6f83bd76889b9a23031c500d3c8864170bd948f0f7f835299b
        A/clauses/window-10/prompt.txt: debac50a65b43af4222214adb3726cd45238ca55dfd558914cf8f78feddd1098
        A/clauses/window-10/meta.json: 4123b70981cd87c7e4673bd433c04e65221b7f2e538474cd53880d1ddf672d9f
        A/clauses/window-03/raw.json: c77634834cb61535ec72e238fc8e863e9e32092d3a192e0bb65708062804431d
        A/clauses/window-03/prompt.txt: d0dadb278ffcf508d4dfb702a07b046d6ea94d394ec14e77950a921b6a49b11d
        A/clauses/window-03/meta.json: 4297751ccf5d4a98fb5acbea929d55a3fc12c53b9f69685afacb26c62b2c9868
        A/clauses/window-04/raw.json: 4916b42e80d3a66c266cdc0f344912e8473993d9cb52fb4a696a632f55c8e0c3
        A/clauses/window-04/prompt.txt: c35d70ed77af7c896e50e08691dc6b889b956ee768045d0587a5b79c2684a279
        A/clauses/window-04/meta.json: 74354a3a2da8ab0aedfc77d6ddd0ba244302ff9c50cf577e899a889397cf875d
        A/clauses/window-05/raw.json: a7c0c5e2c50fee7d3a2ac77657d907365c30b42c2fec1b9e687fc67539f27225
        A/clauses/window-05/prompt.txt: d33eb4457a4703f98221f9b15281b63dedeaf9a7f2a405bcc7ea4a52366d130c
        A/clauses/window-05/meta.json: b127883e129a85f924d0c373598a96be2ba99a4046863dc82ba4ec25de5eef43
        A/clauses/window-02/raw.json: 6abdad64214e2784ccc0e757bc43bb138be4a1609001b34cba67391466921ba1
        A/clauses/window-02/prompt.txt: c2f33b57aad6c8523cd21fd10fdef360475de1ff23efa3c7b4a845293e78fd24
        A/clauses/window-02/meta.json: 0e57cdc6964a6c28b26ec9bfdc3ffc284f7dcd3495ade789e1885c8f050c8a93
        A/clauses/window-09/raw.json: 3e4b5e9c6d96135bd78d033deebac6ed30cb6dfe254c2ae22ab53e0b29a4a6dd
        A/clauses/window-09/prompt.txt: 23821b66e3d4f162412896919b0db7f3008d912ccb92aa9e0007123a2e616ad8
        A/clauses/window-09/meta.json: ca713e943613b0e2f0f6f643ed9f3efb8d263fcdbf4171b46e08a75c5c115c9f
        A/clauses/window-07/raw.json: 327cf8777b90fd0d9d28fd06481b808dc911b8964513644a02231198c64ae2aa
        A/clauses/window-07/prompt.txt: 724d0353b24eb96a494f77028bcfbe3938d8ad6336dfbe20511f3188cd71421a
        A/clauses/window-07/meta.json: 5393c4ba70dac2ee8d222fe25443bae3c842b873b8070c1f5af56dea79130ec7
        A/clauses/window-01/raw.json: a755a5d27a68cdb34fa83f9af3921e82b3c139531f4f48c863d53994e26b0216
        A/clauses/window-01/prompt.txt: 6ae7333d6d16efb5031845b4f2432c06aaa8afe6967686d312fa8e80cc181478
        A/clauses/window-01/meta.json: e237c3a012ebdbf4392d7ffc2a947cf49559aba0d5861e0ded4f0c4a9db573b6
        A/clauses/window-06/raw.json: d639ae649499b5e10e9474c03aabb3f9bd191cd95e42e62f17981950eaf379a9
        A/clauses/window-06/prompt.txt: 45deaa8532d088226cb33aa48cba8f99033c04945791bdabb70edf5313593da2
        A/clauses/window-06/meta.json: 9e72f2c4cb5f0480e00902b01a87f342b681bea12979461dca72ead8f49daf96
        A/clauses/window-08/raw.json: 7caaa5d969d053b47ea76f1153595cb403e7320afc8a2be91c63ba95e534af15
        A/clauses/window-08/prompt.txt: b58cda67f2511a37ca0431ef929bb524426588906d0322c42c9ab5b7909448fc
        A/clauses/window-08/meta.json: 138cb89f41954df5a36e0a69ac8abf4ac7fcd47769d91f045886063853d4b2b5
        A/tables/TABLE-I-page-4-1/raw.json: eebc9878ff49fb863e7fe936632612ca172b0a57c57d4ad5347c553ed4f18fb8
        A/tables/TABLE-I-page-4-1/prompt.txt: 5196bb6f2a7c2317ce82ea6d50f798903030f11b7e0a013e6dd4af66bf380218
        A/tables/TABLE-I-page-4-1/meta.json: c9b0cf3e904f3a656d71c63917cd43dafce88dd6a133b406dbf46b6b5eff2d2a
        B/passages.json: 5d0005517540112eba60c02b27c5465aac9930dff09fcb029e0f0e40bb485d3e
        B/raw.json: 9bfe1512602f1ab8beaba43914369ea62dd8b0925f33fbc26033a82ddcb2ae20
        B/source-units.json: a1a5d10eefcebaa9170f09d44027b4db76c2d17b41bcda9f78c3b4d5afcc5a72
        B/full-source-units.json: ce276a3effbebc0626447565978dbbe5182fc6c166741b29ef9250f54c902b74
        B/meta.json: 83ba151310563d2788f72aeed5685b8fd43c19169185b0a32712659070bd9628
        B/table-images/page-4.png: 642e03d409db0f623303cb5b3a9d673f2874584d606a82e01228343adaffaa53
        B/table-images/TABLE-I-page-4-1.png: 577c9d61cadfeafa845defdc0a5d0ddf0490fe023afbe7e941d2f500aae11cc6
        B/table-images/manifest.json: 4966ed6ab12c4162d861351f17825bc7aa1e87f206179a562cb8ef6c23e9d7f1
        B/clauses/window-11/raw.json: a2f656c933990bd2f99e0d6e4a125bcc9418788b2ccae8ce2f8fde5754c341df
        B/clauses/window-11/prompt.txt: 3c7615c1ec9579eaf46105d86564405f7dfc98f8ed4e20262e49a7956aaa9903
        B/clauses/window-11/meta.json: 27051a66401fdf5e19b842039d7a7689de715dfb5df14a24d31122b961d378cc
        B/clauses/window-10/raw.json: 8e70e40a1b853445f6324f91b7f492895eb6096116039de69643e7cb5942cf20
        B/clauses/window-10/prompt.txt: debac50a65b43af4222214adb3726cd45238ca55dfd558914cf8f78feddd1098
        B/clauses/window-10/meta.json: d801c1a66ea389f62fcc59bb0e1809dd6c76398879258aff65ac0b3b95d1761e
        B/clauses/window-03/raw.json: 7dd93d1c0da3460e7708970a42286a977f711615f13dc304d7bfe37681866aa5
        B/clauses/window-03/prompt.txt: d0dadb278ffcf508d4dfb702a07b046d6ea94d394ec14e77950a921b6a49b11d
        B/clauses/window-03/meta.json: 644d24d4ebea4422f1eee717c9047c0cc901189af58458a54bc0c85c9584ca09
        B/clauses/window-04/raw.json: c5fb3d7fccf589b21b6ef2901247c5dda8e0a8cde9fa2bbaa9687f144d890acc
        B/clauses/window-04/prompt.txt: c35d70ed77af7c896e50e08691dc6b889b956ee768045d0587a5b79c2684a279
        B/clauses/window-04/meta.json: fed9b92e44e09a5340e448966dddd72b74b4867b289d27005765fffc1586361a
        B/clauses/window-05/raw.json: 71d2e033c8751d245c6c221f0d0f01da76854374f028c8953e5bd811964608cf
        B/clauses/window-05/prompt.txt: d33eb4457a4703f98221f9b15281b63dedeaf9a7f2a405bcc7ea4a52366d130c
        B/clauses/window-05/meta.json: dfb33b27e8bca46866ef6cf4a004b1060c832d71d5ac45344a72a0431f676b20
        B/clauses/window-02/raw.json: cb6efbe0ffd59445555fb44228a94031e564c9a2f1d45fb6435c88cf0fcef060
        B/clauses/window-02/prompt.txt: c2f33b57aad6c8523cd21fd10fdef360475de1ff23efa3c7b4a845293e78fd24
        B/clauses/window-02/meta.json: 401fec1c61389ef8954a9b41df1b6f0b4f1cd59f7c8ec07956b8f6112b2649e6
        B/clauses/window-09/raw.json: fbb5ebd64e2b58a4f1deade3c1d5c74b10dd06df5f186b99c663f2d332389fdd
        B/clauses/window-09/prompt.txt: 23821b66e3d4f162412896919b0db7f3008d912ccb92aa9e0007123a2e616ad8
        B/clauses/window-09/meta.json: 59b5cb3b0ac5e8fbc9bed61d8e7b63107eb417d4676e8433fbeb7e6994c6f4b0
        B/clauses/window-07/raw.json: 2d2819ab16df2600a4cb9e190934f53c455592a6fe3c9e5fd1f1b881e3a4a74c
        B/clauses/window-07/prompt.txt: 724d0353b24eb96a494f77028bcfbe3938d8ad6336dfbe20511f3188cd71421a
        B/clauses/window-07/meta.json: 979365101401c9362fdfcfc5b548fa22547e6a00a151ce0e8a28b29c767a2760
        B/clauses/window-01/raw.json: 41bb6ff84486d87d11b0323e06028fd92e0d2f29d0078569d1a46b9e31afc7e0
        B/clauses/window-01/prompt.txt: 6ae7333d6d16efb5031845b4f2432c06aaa8afe6967686d312fa8e80cc181478
        B/clauses/window-01/meta.json: c5d7b6d761e89e2eebe47a2aba2243b2f6266ca6291985c4c3325483bf392b79
        B/clauses/window-06/raw.json: 9a500f6e19de60e44e20474f694551cb0bc9cf371d2abeeaaa59e8ad33870c5d
        B/clauses/window-06/prompt.txt: 45deaa8532d088226cb33aa48cba8f99033c04945791bdabb70edf5313593da2
        B/clauses/window-06/meta.json: 58959ac18fafd7a53e0ec8f2dd625535b5e578568833d550d0b9bce96e988597
        B/clauses/window-08/raw.json: 5059d2df159766cecad17efcdf02323d9060b33389973c83cab603efac9dc3dd
        B/clauses/window-08/prompt.txt: b58cda67f2511a37ca0431ef929bb524426588906d0322c42c9ab5b7909448fc
        B/clauses/window-08/meta.json: 66a08f623d194d30507f6bad2b5fa1a944cfbd0eec257443e5330428a8bbc1ea
        B/tables/TABLE-I-page-4-1/raw.json: d101e6fff89cb66714a11d3be2352d06973b4422aa8faaae8b4a50458879ea8f
        B/tables/TABLE-I-page-4-1/prompt.txt: 5196bb6f2a7c2317ce82ea6d50f798903030f11b7e0a013e6dd4af66bf380218
        B/tables/TABLE-I-page-4-1/meta.json: 7759d6e726dd08ac744e9434fee4596d25d8ed836d9284a62c068bac50214073
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
      pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017Functional
      source_status_sha256: 24c42246830cb936d8ee9ec6b2229940bd5bada7aae7db9699ad2571f8d4e538
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: time since stroke
    outcome:
      text: PNT performance
    analysis_label: Hierarchical regression (Step 1)
    relation: association
    evidence_ids:
    - P8-S1-C7
    qualifier_ids:
    - P8-S1-C5
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017Functional
      source_status_sha256: 24c42246830cb936d8ee9ec6b2229940bd5bada7aae7db9699ad2571f8d4e538
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C4
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P6-S2-C6
      - Unaccounted source passage P6-S2-C6
      - Unaccounted source passage P5-S1-C8
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C6
      - Result passage disposed without unit P6-S3-C7
      - 'window 5: invalid/duplicate disposition P7-S1-C1'
      - Result passage disposed without unit P7-S1-C1
      - 'window 5: invalid/duplicate disposition P7-S1-C2'
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C12
      - Result passage disposed without unit P7-S1-C14
      - Result passage disposed without unit P7-S1-C15
      - Result passage disposed without unit P7-S2-C3
      - Result passage disposed without unit P7-S2-C4
      - Result passage disposed without unit P7-S2-C10
      - Result passage disposed without unit P7-S2-C11
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P7-S2-C8
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P10-S1-C10
      - Accounting without a linked unit P10-S1-C7
      - Accounting without a linked unit P10-S1-C8
      - Accounting without a linked unit P10-S1-C9
      - Accounting without a linked unit P10-S2-C3
      - Accounting without a linked unit P10-S2-C7
      - Unaccounted source passage P10-S2-C3
      - Unaccounted source passage P10-S2-C7
      - Unaccounted source passage P10-S1-C9
      - Unaccounted source passage P10-S1-C7
      - Unaccounted source passage P10-S1-C8
      - 'window 11: invalid/duplicate disposition P10-S2-C11'
      - 'window 11: invalid/duplicate disposition P11-S1-C1'
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S2-C1
      - Result passage disposed without unit P12-S3-C6
      - Result passage disposed without unit P13-S1-C11
      - Result passage disposed without unit P13-S1-C3
      - Accounting without a linked unit P13-S2-C2
      - Result passage disposed without unit P13-S2-C3
      - Unaccounted source passage P13-S2-C2
      - Result passage disposed without unit P13-S2-C10
      - Accounting without a linked unit P13-S2-C11
      - Unaccounted source passage P13-S2-C11
      - Result passage disposed without unit P14-S1-C5
      - Result passage disposed without unit P14-S1-C6
      - Result passage disposed without unit P14-S1-C7
      unattached_null_or_qualifier_ids:
      - P5-S1-C8
      - P7-S1-C14
      - P10-S1-C7
      - P10-S1-C8
      - P10-S1-C9
      - P10-S2-C3
      - P14-S1-C6
      suppressed_nonrepresented_units: 16
      default_disposition_count_requires_completeness_check: 233
      unselected_timing_passages:
      - P3-S2-C2
      - P3-S2-C13
      - P3-S2-C14
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C15
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C17
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S2-C6
        - P4-S2-C8
        - P6-S2-C2
        - P6-S2-C6
        - P8-S1-C5
        - P8-S1-C6
        - P9-S1-C12
        - P10-S1-C2
        - P10-S1-C4
        - P10-S1-C7
        - P10-S1-C9
        - P10-S2-C2
        - P10-S2-C3
        - P10-S2-C4
        - P10-S2-C6
        - P10-S2-C7
        - P10-S2-C9
        - P10-S2-C10
        - P11-S1-C11
        - P11-S1-C12
        - P11-S1-C13
        - P12-S1-C7
        - P12-S1-C10
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        - P13-S2-C2
        - P13-S2-C3
        - P13-S2-C4
        - P13-S2-C5
        - P13-S2-C6
        - P13-S2-C7
        - P13-S2-C8
        - P13-S2-C9
        - P13-S2-C10
        - P13-S2-C11
        - P13-S2-C12
        - P13-S2-C13
        - P13-S2-C14
        - P14-S1-C6
        - P14-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P3-S3-C8
        - P5-S1-C15
        - P5-S2-C2
        - P6-S2-C3
        - P6-S2-C9
        - P8-S1-C5
        - P8-S1-C6
        - P9-S1-C12
        - P10-S1-C4
        - P10-S1-C7
        - P10-S2-C2
        - P10-S2-C4
        - P10-S2-C6
        - P10-S2-C7
        - P10-S2-C9
        - P10-S2-C10
        - P11-S1-C11
        - P11-S1-C12
        - P11-S1-C13
        - P12-S1-C7
        - P12-S1-C10
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        - P13-S2-C2
        - P13-S2-C3
        - P13-S2-C4
        - P13-S2-C5
        - P13-S2-C6
        - P13-S2-C7
        - P13-S2-C8
        - P13-S2-C9
        - P13-S2-C10
        - P13-S2-C11
        - P13-S2-C12
        - P13-S2-C13
        - P13-S2-C14
        - P14-S1-C6
        - P14-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-I-page-4-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S3
        - P5-S2
        - P6-S3
        - P7-S1
        - P7-S2
        - P8-S1
        - P9-S1
        - P10-S1
        - P10-S2
        - P10-S3
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017Functional
      source_status_sha256: 24c42246830cb936d8ee9ec6b2229940bd5bada7aae7db9699ad2571f8d4e538
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 4
      - 14
      reason: Abstract restatement of findings regarding right STS and left dPOp.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: Abstract restatement of lesion-activity relationships.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 4
      - 11
      reason: Abstract summary of activity relating to naming outcomes.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes demographics and exclusion criteria of participants.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group matching for sex.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: States sex was a covariate with no effect.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between PCAD and lesion size.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes normalization accuracy confirmation.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ROI selection thresholding.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports control group accuracy.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports aphasia group accuracy.
    - source_id: P6-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports PNT average scores.
    - source_id: P6-S3-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of SVR-LSM peak area.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies posterior STG as critical area.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies other critical areas (angular gyrus, IPS, PTr).
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCAD score range.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports correlation between PCAD and PNT scores.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overlapping activation during covert naming.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control-specific activation.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes basal ganglia activation.
    - source_id: P7-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group greater activation in occipital lobe.
    - source_id: P7-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia group greater activation in precuneus.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes visual cortex activation.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group map similarity.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia group additional activations.
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes subcortical activation.
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group greater activation in left hemisphere.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists specific regions of control group greater activation.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes bilateral IPS activation.
    - source_id: P7-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia group greater activation in right hemisphere.
    - source_id: P7-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists specific regions of aphasia group over-activation.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P7-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure caption for within-group contrasts.
    - source_id: P7-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Thresholding statement for Figure 2.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes further aphasia group over-activation.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports PCAD as strongest predictor of PNT.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports time since stroke as significant predictor.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports other variables did not significantly predict PNT.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes over/under-activation relative to controls.
    - source_id: P8-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no ROIs from covert naming met threshold.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Counts ROIs surviving from overt naming map.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports negative correlation of left dPOp with PNT.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports left dPOp relationship remained significant in regression.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports positive correlations for right STS and right ventral motor
        cortex.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports only right STS remained significant in regression; right ventral
        motor cortex did not.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 4.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies clusters in covert naming contrast.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Reports left TP significant relationship in regression.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no activity difference in left TP between groups.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      reason: Identifies clusters in overt naming contrast.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Reports left frontal pole significant relationship in regression.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no activity difference in left frontal pole between groups.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Reports right post-central gyrus and right STS significant in regression.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports aphasia group showed more activity in these ROIs.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 11
      reason: Reports no regions differed during successful vs unsuccessful naming.
    - source_id: P10-S2-C12
      disposition: represented
      result_indexes:
      - 12
      reason: Reports right STS activation associated with left dPOp lesions.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 12
      reason: Restatement of right STS and left dPOp findings.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 13
      reason: Reports low right STS activation associated with left STS lesions.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 14
      reason: Reports left dPOp activity related to left STG, white matter, and left
        STS lesions.
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no areas predicted low left dPOp activation.
    - source_id: P12-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right hemisphere activation and post-lexical production.
    - source_id: P12-S1-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 7
      - 8
      - 9
      - 10
      reason: Discussion summary of activation in spared areas relating to outcomes.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 5
      - 10
      reason: Discussion restatement of right hemisphere activity and naming performance.
    - source_id: P12-S1-C9
      disposition: represented
      result_indexes:
      - 10
      reason: Reports that some right hemisphere negative correlations disappeared
        after control.
    - source_id: P12-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no relationship between right IFG activation and naming performance.
    - source_id: P12-S3-C3
      disposition: repeated
      result_indexes:
      - 5
      - 10
      reason: Discussion of right hemisphere compensation.
    - source_id: P12-S3-C4
      disposition: repeated
      result_indexes:
      - 5
      - 10
      reason: Discussion of right STS robustness.
    - source_id: P13-S1-C3
      disposition: repeated
      result_indexes:
      - 11
      reason: Discussion restatement of null results for correct vs incorrect trials.
    - source_id: P13-S2-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of right STS over-activation and performance.
    - source_id: P13-S2-C4
      disposition: repeated
      result_indexes:
      - 13
      reason: Discussion restatement of left STS lesions and right STS failure.
    - source_id: P14-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about lesion location and function.
    - source_id: P14-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about right hemisphere and naming stages.
    - source_id: P14-S1-C6
      disposition: repeated
      result_indexes:
      - 5
      - 10
      reason: Conclusion restatement of right hemisphere activation and predicted
        performance.
    - source_id: P14-S1-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restatement of left dPOp maladaptive activity.
    unresolved_coverage:
    - source_id: P7-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P3-S3-C4
    - P3-S3-C7
    - P3-S3-C8
    - P5-S1-C8
    - P5-S1-C12
    - P6-S1-C7
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C10
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C4
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S1-C14
    - P7-S1-C15
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C9
    - P7-S2-C10
    - P7-S2-C11
    - P8-S1-C1
    - P8-S1-C10
    - P8-S1-C14
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C4
    - P9-S1-C11
    - P10-S1-C3
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C8
    - P10-S1-C10
    - P10-S2-C7
    - P10-S3-C2
    - P11-S1-C1
    - P11-S1-C4
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C12
    - P12-S1-C2
    - P12-S1-C3
    - P12-S1-C4
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S2-C1
    - P12-S2-C11
    - P12-S3-C3
    - P12-S3-C4
    - P12-S3-C6
    - P12-S3-C7
    - P13-S1-C3
    - P13-S1-C11
    - P13-S2-C2
    - P13-S2-C3
    - P13-S2-C4
    - P13-S2-C6
    - P13-S2-C10
    - P13-S2-C11
    - P13-S3-C9
    - P14-S1-C4
    - P14-S1-C5
    - P14-S1-C6
    - P14-S1-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-I-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C3
      - P3-S3-C5
      recruited_sample:
      - P3-S2-C13
      - P3-S3-C2
      - P3-S3-C3
      - P3-S3-C5
      eligibility:
      - P3-S3-C2
      - P3-S3-C3
      - P3-S3-C5
      imaging_provenance:
      - P4-S2-C13
      - P4-S2-C15
      - P5-S1-C11
      imaging_timing:
      - P4-S2-C12
      outcome_timing:
      - P4-S2-C7
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P6-S1-C12
      - P6-S1-C14
      - P6-S1-C16
      - P10-S1-C2
      dependent_variable_statement:
      - P6-S2-C2
      - P6-S2-C4
      - P6-S2-C9
      - P8-S1-C5
      limitations:
      - P6-S1-C7
      - P7-S1-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C6
      - P3-S3-C7
      - P4-S3-C4
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C15
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C17
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S2-C6
      - P4-S2-C8
      - P6-S2-C2
      - P6-S2-C6
      - P8-S1-C5
      - P8-S1-C6
      - P9-S1-C12
      - P10-S1-C2
      - P10-S1-C4
      - P10-S1-C7
      - P10-S1-C9
      - P10-S2-C2
      - P10-S2-C3
      - P10-S2-C4
      - P10-S2-C6
      - P10-S2-C7
      - P10-S2-C9
      - P10-S2-C10
      - P11-S1-C11
      - P11-S1-C12
      - P11-S1-C13
      - P12-S1-C7
      - P12-S1-C10
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      - P13-S2-C2
      - P13-S2-C3
      - P13-S2-C4
      - P13-S2-C5
      - P13-S2-C6
      - P13-S2-C7
      - P13-S2-C8
      - P13-S2-C9
      - P13-S2-C10
      - P13-S2-C11
      - P13-S2-C12
      - P13-S2-C13
      - P13-S2-C14
      - P14-S1-C6
      - P14-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P3-S3-C8
      - P5-S1-C15
      - P5-S2-C2
      - P6-S2-C3
      - P6-S2-C9
      - P8-S1-C5
      - P8-S1-C6
      - P9-S1-C12
      - P10-S1-C4
      - P10-S1-C7
      - P10-S2-C2
      - P10-S2-C4
      - P10-S2-C6
      - P10-S2-C7
      - P10-S2-C9
      - P10-S2-C10
      - P11-S1-C11
      - P11-S1-C12
      - P11-S1-C13
      - P12-S1-C7
      - P12-S1-C10
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      - P13-S2-C2
      - P13-S2-C3
      - P13-S2-C4
      - P13-S2-C5
      - P13-S2-C6
      - P13-S2-C7
      - P13-S2-C8
      - P13-S2-C9
      - P13-S2-C10
      - P13-S2-C11
      - P13-S2-C12
      - P13-S2-C13
      - P13-S2-C14
      - P14-S1-C6
      - P14-S1-C7
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
      pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
      review_sha256: 8c8ff230ddbff92164b3656c407b60fbf38da9b90ac196e0f9572981658485cd
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
      - P8-S1-C7
      source_result: In the first step of a hierarchical regression model predicting
        Philadelphia Naming Test (PNT) performance in the aphasia group, time since
        stroke was a significant predictor (t(24) = 2.13, P < 0.05), alongside PCAD,
        while other demographic and lesion variables were not significant.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P8-S1-C7 explicitly reports the result of the first step
            of the hierarchical regression where time since stroke was a significant
            predictor of PNT performance. The proposed core correctly identifies this
            specific analysis step and outcome.
          source_ids:
          - P8-S1-C7
          - P8-S1-C5
        direction:
          answer: fits
          reason: The source states time since stroke was a 'significant predictor'
            (P8-S1-C7). The proposed core claims it 'significantly predicted' performance.
            While the specific direction (positive/negative) is not explicitly detailed
            in the provided text snippet, the claim of a significant association is
            faithful to the source's report of a detected effect. The direction field
            'likely' is a placeholder for the qualitative draft, but the core claim
            of significance is accurate.
          source_ids:
          - P8-S1-C7
        construct:
          answer: fits
          reason: The exposure is 'time since stroke' and the outcome is 'PNT performance'
            (naming ability). The source confirms PNT was the dependent variable and
            time since stroke was a predictor in the regression (P8-S1-C5, P8-S1-C7).
            The patient measurement is non-imaging (behavioral PNT score), which is
            correct as the outcome is a behavioral test score, not an imaging metric.
          source_ids:
          - P8-S1-C5
          - P8-S1-C7
          - P4-S2-C6
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications that the result was 'measured
            in the first step of a hierarchical regression' and 'tested alongside
            PCAD, lesion volume, age, sex, education, and handedness'. This accurately
            reflects the model structure described in P8-S1-C5 and P8-S1-C4.
          source_ids:
          - P8-S1-C4
          - P8-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The core correctly identifies the analysis as a step in a hierarchical
            model. It does not misrepresent the result as a standalone final conclusion
            or omit the context that it is part of a larger model building process.
            No material caveats regarding the specific finding of time since stroke
            are omitted from the provided source window.
          source_ids:
          - P8-S1-C4
          - P8-S1-C7
      optional_pending:
      - Specific direction of the association (positive/negative) for time since stroke
        is not explicitly stated in the provided text snippet, only that it was significant.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific direction of the association (positive/negative) for time since stroke
      is not explicitly stated in the provided text snippet, only that it was significant.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R003
      exposure:
        text: time since stroke
      outcome:
        text: PNT performance
      analysis_label: Hierarchical regression (Step 1)
      relation: association
      evidence_ids:
      - P8-S1-C7
      qualifier_ids:
      - P8-S1-C5
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
        source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017Functional
        source_status_sha256: 24c42246830cb936d8ee9ec6b2229940bd5bada7aae7db9699ad2571f8d4e538
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4217b353f04e6d0655c235aaae70b39f37b5de9045f7b8c1ff14ee7c2ad32b62
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C14
          page: 3
          text_layer_sha256: 4217b353f04e6d0655c235aaae70b39f37b5de9045f7b8c1ff14ee7c2ad32b62
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants in the

          aphasia group were native English speakers, and testing

          occurred at least 6 months after the stroke.'
        anchor_text: 'All participants in the

          aphasia group were native English speakers, and testing

          occurred at least 6 months after the stroke.'
        excluded_fragments: []
        image_sha256: e2397f7b3920fc340770a1875bdfbeb57405bcdb1da886737a8f315533b8f273
        transcription: '. All participants in the

          aphasia group were native English speakers, and testing

          occurred at least 6 months after the stroke'
      P3-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2cb249a2f6c1b648f3691226b39497d143f0e58358be6b55cad4e4d2f17df453
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2e109f701933b78383b56c0ce96af6699f8cea36a884e8c0afc257e01621fb59
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C3
          page: 3
          text_layer_sha256: 2e109f701933b78383b56c0ce96af6699f8cea36a884e8c0afc257e01621fb59
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Fourteen participants were then excluded based on

          fMRI task performance (see below), resulting in a ﬁnal

          sample of 32 participants in the aphasia group (Table I

          and Supporting Information).'
        anchor_text: 'Fourteen participants were then excluded based on

          fMRI task performance (see below), resulting in a ﬁnal

          sample of 32 participants in the aphasia group (Table I

          and Supporting Information).'
        excluded_fragments: []
        image_sha256: bf3e55a40991b206467ee46b3a7334db914a2cc1798f80f2282c288c95c0a19e
        transcription: . Fourteen participants were then excluded based on fMRI task
          performance (see below), resulting in a final sample of 32 participants
          in the aphasia group (Table I and Supporting Information)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'Time since stroke was also a signiﬁcant predic-

    tor, t(24) 5 2.13, P < 0.05.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
