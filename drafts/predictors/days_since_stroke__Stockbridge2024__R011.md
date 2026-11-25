---
id: days_since_stroke
name: days since stroke
kind: predictor
findings:
- id: f1
  target: discourse_efficiency_improvement
  target_kind: prognosis
  claim: days since stroke did not significantly contribute to the prediction of long-term
    recovery of discourse efficiency
  direction: no_effect
  relationship: correlational
  method: MVPA
  sample:
    n: 22
    population: right-handed adult English speakers within three months of ischemic
      left hemisphere stroke diagnosed with aphasia
    phase: not_reported
    time_post_onset: long-term recovery measured by combining performance five- and
      twenty-weeks post-treatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - heterogenous aphasia subtypes
  - active tDCS and sham tDCS participants analyzed together
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: number of days from stroke onset to the start of the
    study/therapy. measured as a contributor to a prediction model; model also included
    age and mean diffusivity of various white matter regions. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P4-S1-C1, two-model agreement, human verification pending): Results


    Participant description


    Twenty-two participants completed diffusion tensor imaging, summarized in Tables
    1, 2 and 3. Original text-layer quotation is preserved below. PDF image reading
    (P2-S3-C2, two-model agreement, human verification pending): . Included individu-

    als were right-handed, adult English speakers within three

    months of ischemic left hemisphere stroke who were diag-

    nosed with aphasia using the Western Aphasia Battery-

    Revised (WAB-R; Kertesz 2007) Original text-layer quotation is preserved below.'
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
    - proposed_concept:discourse_efficiency_improvement
  therapy:
    id: tdcs_slt
    name: anodal transcranial direct current stimulation combined with computer-delivered
      speech and language naming therapy
  citation: '@Stockbridge2024'
  source_passages:
  - section: Original source P6-S2-C8
    page: 6
    quote: 'Days since stroke was no longer a sig­

      nificant contributor to the model.'
    supports: claim
  - section: Original source P4-S2-C3
    page: 4
    quote: "For each behavioral outcome mea­\nsure (PNT, CU, and Syllables/CU), a\
      \ separate regression \nwas calculated to predict change in that variable sub-acutely\
      \ \n(one week after treatment) and chronically (combining per­\nformance five-\
      \ and twenty-weeks post-treatment to maxi­\nmize the data available for analysis)."
    supports: method
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      Brain Structure and Function (2024) 229:2207–2217

      Results

      Participant description

      Twenty-two participants completed diffusion tensor imag­

      ing, summarized in Tables 1, 2 and 3.'
    supports: sample
  - section: Original source P2-S3-C2
    page: 2
    quote: "Included individu­\nals were right-handed, adult English speakers within\
      \ three \nmonths of ischemic left hemisphere stroke who were diag­\nnosed with\
      \ aphasia using the Western Aphasia Battery-\nRevised (WAB-R; Kertesz 2007)."
    supports: sample
  - section: Original source P9-S2-C12
    page: 9
    quote: 'Days: Days from stroke to start of therapy

      1 3

      2215


      '
    supports: claim
  - section: Original source P9-S2-C2
    page: 9
    quote: 'Limitations

      One of the main limitations is small sample size with het­

      erogenous aphasia subtypes.'
    supports: limitation
  - section: Original source P9-S2-C3
    page: 9
    quote: "Another limitation is we have \nanalyzed together patients who received\
      \ active tDCS and \nthose who received sham tDCS due to small sample size."
    supports: limitation
predictor_type: demographic
short_definition: number of days from stroke onset to the start of the study/therapy
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Stockbridge2024
  proposal_id: R011
  review_status_sha256: 01ee30b75663c276f40282f4eae59ba41fd1bf921642665edca50810faa0759f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
        A/passages.json: b4bf6bdc64acba409362714c451eb61733e697ffb77eba9c838bd0d4db5ebc92
        A/raw.json: 691f4959803ebd821553cbf55cbf5f211fa9908a95ac4b3b4234dfa6d51347cb
        A/source-units.json: be489f9624d7357a73a156847404cbe88f0a580482ba7dfa7ff69644de6287c2
        A/full-source-units.json: a31d2491e4d3fdef30d05917c97de3596c459e57c0c167623e4c96421845dca0
        A/meta.json: 14431464161394b54f614b8477c6f9bc0184828a18eb87cca8c6ab2e2ad45e62
        A/table-images/TABLE-1-page-5-1.png: 984e65b66a0ed3d84e046184ac445c21028bd3ebaaff6f832a2f4790adfd26e8
        A/table-images/TABLE-4-page-9-1.png: f279608cd7e0d4ff78c1738b201856d548968c00dab6a86e48176417471bef2c
        A/table-images/page-6.png: 085cbe778faf2f3767dd426455fd31ac6336c3c4857d6f65df02a062f516cac3
        A/table-images/page-7.png: 8b80a8602c79708cf993cf1652d956482c64e38651b54cdc3badbac78c24bdea
        A/table-images/page-5.png: acc21cad2b7f95e25947a4c9b58de525f4d8d9cdab10c0c4838b3877785f8e4b
        A/table-images/page-9.png: 78da80b2899c3220c03dde88a84f8646d3df40da8de637b772cd603b0d360c3d
        A/table-images/TABLE-2-page-6-1.png: 57708fb136dbc6f20a0032a29a8fc86f733feb5bfe15894dae1236c744190d3f
        A/table-images/manifest.json: c2b1b83b0e52dcb097a0fe4162b364751852b2014ec5fcfea97d2484319e9fd6
        A/table-images/TABLE-3-page-7-1.png: e2be8b8688c61323db16552f30efe3c0fc7ed0f09afd386f8af2e3608e2fb28b
        A/clauses/window-03/raw.json: ad4f15ffd24ebdaf6ef2ac990cc4a2b7ac207d987cdb65cbcc1fdd21b3f38c95
        A/clauses/window-03/prompt.txt: 11b8a67ff42e0f65b7da676ce03fa62f21072680c1b95092a4965c2dc70a9d8d
        A/clauses/window-03/meta.json: e880adc47d17e29d2dfa2790e0955b7bcfd349dc94ebb350b9005bb81f3147cd
        A/clauses/window-04/raw.json: a85b12e317e3fcbf8fc8a01393e44387c46475efede6989e1561339b4a9219b0
        A/clauses/window-04/prompt.txt: d1b94ab048de9c73b561f7e38ee10e9d36b0cf73cf64b2b401cd74e359af0775
        A/clauses/window-04/meta.json: 34c4918cb5d44b6ae92305607c1f3ae2837422515ecd016e5fa0ae3dbecfc1c6
        A/clauses/window-05/raw.json: 74940e2b265014519b6ac7c2d5f5133a5c794592b44cbad57466534e62486fcf
        A/clauses/window-05/prompt.txt: 74394b9c81711fd802786aa3755d8208f7dc0c82a1beb438d1af30d3c9e9c8c8
        A/clauses/window-05/meta.json: fecf50449f9743f14a24caf3b29210e9cf2be5212b93f4bfd4ce3660fd9a6198
        A/clauses/window-02/raw.json: 0dc37f0d8d8b7eea4d64e8bb8d1c288ea4af3468997dd80a9af6476141eb1717
        A/clauses/window-02/prompt.txt: 9bd07994749067969389adf5315ea388028e67d7199dd7d015bc96176002d6b0
        A/clauses/window-02/meta.json: 98f44a7538ee27a8ff0ea462c627821f790f88cfaa7b80cb5d89268e92ecb171
        A/clauses/window-01/raw.json: 49e12be179e016e162e14e7a4511e714f96003f0a5de1b700907909c2f06caac
        A/clauses/window-01/prompt.txt: 43e3afba1cfc144de6a14025d7936d71fd17f0f9a631e55229a5157f03cb637e
        A/clauses/window-01/meta.json: bc60dcf7a5bc1ad22904ce3b775d5beca7043067fe38e3c7864a75d13ed0f101
        A/clauses/window-06/raw.json: dbd13e6cad0661cbc52fe84a8e1a28a2e76f34642b2f94c289fa227cf91409b4
        A/clauses/window-06/prompt.txt: 118907f13aeb19f0e5172a27b0e9fd68547c0bcec48501206d4702ac2d4dd883
        A/clauses/window-06/meta.json: ef13134c53487a5dac07d8de423723a4700f739fc7ab534aef2a19bae76e0706
        A/tables/TABLE-1-page-5-1/raw.json: 068a889478fb592813e4861451c9760076939898790d479c17f46ea8a8e0dc7f
        A/tables/TABLE-1-page-5-1/prompt.txt: 7faa0bfb52be97ee3d7d442e7f82ed5649e71dfa95ef5d17b40d52c1854bb172
        A/tables/TABLE-1-page-5-1/meta.json: 529d4a6a3fa02ff395d1860604cc656552d5897e12a113c155d4c34d063403e8
        A/tables/TABLE-2-page-6-2/raw.json: 234d3c9737f3b1b35e7328059f278eb33e28ee8bf0d77693306694e3e4097975
        A/tables/TABLE-2-page-6-2/prompt.txt: 3e34cdfe714d0c11477e47c3030344cfb3db21c97c7a21547b3458cc7710d04e
        A/tables/TABLE-2-page-6-2/meta.json: 7a1fe1e5fcb18c12a1d8dd5a7e6d32aeec2ccef31225e27b54ef81c675831b35
        A/tables/TABLE-3-page-7-3/raw.json: 6d818425091aebaf8489b1d219056be10d5bc8d71c96198968c92cee568889f4
        A/tables/TABLE-3-page-7-3/prompt.txt: 172e47d124a8bb225a64d297e2a02ef7ea84d42b6351409ae38086520a14f4b2
        A/tables/TABLE-3-page-7-3/meta.json: 607787d78d22011288f41227efa7cb0844f3b6a8b48b4846f59c67691adf8522
        A/tables/TABLE-4-page-9-4/raw.json: 39bc4c92ffac1eeac9018086cb7a11bcc7c38aba33b814a63f8877b41eb926e2
        A/tables/TABLE-4-page-9-4/prompt.txt: 7a2cac64933e6087a4b73fc36e407c28318cd1d20e5ae66df70007945afc9c68
        A/tables/TABLE-4-page-9-4/meta.json: 250632e0fe678d16b8cb96d45653e447778dabe238e46d5a0ee7193d0d6e01eb
        B/passages.json: b4bf6bdc64acba409362714c451eb61733e697ffb77eba9c838bd0d4db5ebc92
        B/raw.json: 10df3a5f7768652c4d0756a829fa0bcef181e21e0e37af9ed5a616b970b35cea
        B/source-units.json: be489f9624d7357a73a156847404cbe88f0a580482ba7dfa7ff69644de6287c2
        B/full-source-units.json: a31d2491e4d3fdef30d05917c97de3596c459e57c0c167623e4c96421845dca0
        B/meta.json: 508d8dea85928790594104b7c74f64734bdbf78275f0560b06749b076e9402d9
        B/table-images/TABLE-1-page-5-1.png: 984e65b66a0ed3d84e046184ac445c21028bd3ebaaff6f832a2f4790adfd26e8
        B/table-images/TABLE-4-page-9-1.png: f279608cd7e0d4ff78c1738b201856d548968c00dab6a86e48176417471bef2c
        B/table-images/page-6.png: 085cbe778faf2f3767dd426455fd31ac6336c3c4857d6f65df02a062f516cac3
        B/table-images/page-7.png: 8b80a8602c79708cf993cf1652d956482c64e38651b54cdc3badbac78c24bdea
        B/table-images/page-5.png: acc21cad2b7f95e25947a4c9b58de525f4d8d9cdab10c0c4838b3877785f8e4b
        B/table-images/page-9.png: 78da80b2899c3220c03dde88a84f8646d3df40da8de637b772cd603b0d360c3d
        B/table-images/TABLE-2-page-6-1.png: 57708fb136dbc6f20a0032a29a8fc86f733feb5bfe15894dae1236c744190d3f
        B/table-images/manifest.json: d9019bfdc8ebb1ad9e6320561ff68940df397610e6ab0494bd0d935d29aa68e6
        B/table-images/TABLE-3-page-7-1.png: e2be8b8688c61323db16552f30efe3c0fc7ed0f09afd386f8af2e3608e2fb28b
        B/clauses/window-03/raw.json: c7c152a7852623fc2b8a47a7e2bc0c2f98abde1728c9a2b959b3c6eec79126c4
        B/clauses/window-03/prompt.txt: 11b8a67ff42e0f65b7da676ce03fa62f21072680c1b95092a4965c2dc70a9d8d
        B/clauses/window-03/meta.json: 467f24b550898ee71c70081e58a80accfda5a38823256d0232d02385e8a8cab9
        B/clauses/window-04/raw.json: 87f6c236d7397ef7a729cb81c010200de7413a048ce0de08a5f71c8139bca16a
        B/clauses/window-04/prompt.txt: d1b94ab048de9c73b561f7e38ee10e9d36b0cf73cf64b2b401cd74e359af0775
        B/clauses/window-04/meta.json: 607c96b8e96c09bc0fd4542db81fa3be96bef0058b57bcd11d7e0d45dddcdab4
        B/clauses/window-05/raw.json: 4752a25197a78bb10af0ec73e7fdae4681d16b369796d26e9a6c775638e4a86d
        B/clauses/window-05/prompt.txt: 74394b9c81711fd802786aa3755d8208f7dc0c82a1beb438d1af30d3c9e9c8c8
        B/clauses/window-05/meta.json: 2ff10a2345718eded9a0ac28c73512337edce026697164b393014854a00bb8c7
        B/clauses/window-02/raw.json: b07c7d433e7fa6351d01440fe84638fb5b1f92957234252d4fa35a9e02395135
        B/clauses/window-02/prompt.txt: 9bd07994749067969389adf5315ea388028e67d7199dd7d015bc96176002d6b0
        B/clauses/window-02/meta.json: 8ff1f0e8e952d299a250e6a09e5512474e7c7b222785c632dac07f7e964990d0
        B/clauses/window-01/raw.json: 2a2e2db9813c41a77ce7bab5293bc15e7479927e67e9065195b99022d955fd87
        B/clauses/window-01/prompt.txt: 43e3afba1cfc144de6a14025d7936d71fd17f0f9a631e55229a5157f03cb637e
        B/clauses/window-01/meta.json: 9cacb23ec005719a6e90678b63f8886eea2d8fe33ff8e03c89fc4e044477e5e1
        B/clauses/window-06/raw.json: 515cabb58af966a38595c9102bd19b652ed5868f2b8cf12e31228c2983245762
        B/clauses/window-06/prompt.txt: 118907f13aeb19f0e5172a27b0e9fd68547c0bcec48501206d4702ac2d4dd883
        B/clauses/window-06/meta.json: 279132cd66e20a5ba9d8c76bab02f6c600d793db0da29e734761624174318117
        B/tables/TABLE-1-page-5-1/raw.json: 6e3ddef262e8a28108fcc3f408a552e6bc984add0f4ffb1d0d0d683ff2541af7
        B/tables/TABLE-1-page-5-1/prompt.txt: 7faa0bfb52be97ee3d7d442e7f82ed5649e71dfa95ef5d17b40d52c1854bb172
        B/tables/TABLE-1-page-5-1/meta.json: 07d504f061d485da2b98d63d89f67776f1d6fae927e263a758378477fe40ed80
        B/tables/TABLE-2-page-6-2/raw.json: 19cd278c6ee948c0b5b84c8311e8457caa886117c1950317b6bde42c8a90e1a0
        B/tables/TABLE-2-page-6-2/prompt.txt: 3e34cdfe714d0c11477e47c3030344cfb3db21c97c7a21547b3458cc7710d04e
        B/tables/TABLE-2-page-6-2/meta.json: ef69878d24aa475b873949d66e94c934d9dc867d32a21c9d49a681dc6871ec44
        B/tables/TABLE-3-page-7-3/raw.json: 6f7fa69845f554e943c9bef2f615c6dd962c22bc8e06901074215104a447dc7c
        B/tables/TABLE-3-page-7-3/prompt.txt: 172e47d124a8bb225a64d297e2a02ef7ea84d42b6351409ae38086520a14f4b2
        B/tables/TABLE-3-page-7-3/meta.json: a2010dfaf4095accd2a4f80ed3c944310d109ad41db09b025834783c716dd9b6
        B/tables/TABLE-4-page-9-4/raw.json: 4b5bc73aa3447422921ba0cf5a2ea6776fbb87a40b44469c8e7c2abe0543871b
        B/tables/TABLE-4-page-9-4/prompt.txt: 7a2cac64933e6087a4b73fc36e407c28318cd1d20e5ae66df70007945afc9c68
        B/tables/TABLE-4-page-9-4/meta.json: 46b40bec3d82159fba2bfd16d2a70a5f5fa363ea9884590435f88816965ba848
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
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      source_review: _compare/relationships-2026-11-16/review-current/Stockbridge2024
      source_status_sha256: 09f02c54b11a21800459ff9cf579ef0b656af9442e9b3b3ea2078d148b57f968
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R011
    exposure:
      text: days since stroke
    outcome:
      text: discourse efficiency improvement
    analysis_label: Long-term recovery prediction (5- and 20-weeks post-treatment)
    relation: performance
    evidence_ids:
    - P6-S2-C8
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
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      source_review: _compare/relationships-2026-11-16/review-current/Stockbridge2024
      source_status_sha256: 09f02c54b11a21800459ff9cf579ef0b656af9442e9b3b3ea2078d148b57f968
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C6
      - Result passage disposed without unit P3-S1-C2
      - Unresolved source passage P3-S2-C14
      - Result passage disposed without unit P4-S1-C2
      - Result passage disposed without unit P5-S1-C1
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P9-S1-C1
      - Accounting without a linked unit P9-S1-C15
      - Accounting without a linked unit P9-S1-C2
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P9-S1-C15
      - Unaccounted source passage P9-S1-C2
      - Unaccounted source passage P9-S1-C1
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 128
      unselected_timing_passages:
      - P2-S2-C4
      - P2-S2-C7
      - P2-S3-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P9-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S2-C3
        - P5-S1-C8
        - P5-S1-C10
        - P5-S1-C11
        - P5-S1-C13
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C6
        - P9-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      - TABLE-4-page-9-4
      unlinked_tables:
      - TABLE-3-page-7-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P4-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      source_review: _compare/relationships-2026-11-16/review-current/Stockbridge2024
      source_status_sha256: 09f02c54b11a21800459ff9cf579ef0b656af9442e9b3b3ea2078d148b57f968
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sample size for DTI subset.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: States correlation between naming and pITG integrity.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: States predictors for naming recovery.
    - source_id: P1-S2-C9
      disposition: represented
      result_indexes:
      - 4
      reason: States predictors for discourse efficiency recovery.
    - source_id: P1-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      - 4
      reason: Abstract conclusion restating associations.
    - source_id: P1-S2-C11
      disposition: repeated
      result_indexes:
      - 2
      - 4
      - 7
      - 8
      reason: Abstract conclusion restating predictive value.
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses analysis constraints due to sample size.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: References prior study results (Stockbridge et al. 2023a).
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes DTI delineation success.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general improvement in language (ANOVA) without specific exposure.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general lack of improvement in content/syllables (ANOVA) without
        specific exposure.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: States correlation between naming and pITG MD.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: States null correlation for discourse measures.
    - source_id: P4-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      - 4
      - 7
      - 8
      reason: General statement that baseline MD predicts recovery.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes thresholding to avoid lesion overlap.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about long-term vs short-term patterns.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Specifies direction of MD predictors for efficiency.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses influence of days since stroke on PNT vs efficiency.
    - source_id: P5-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of pITG correlation.
    - source_id: P5-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of null discourse correlation.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies predictors and variance for PNT recovery.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies direction of MD predictors for PNT.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: States non-significance of content recovery model.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: States significance and variance for efficiency recovery.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Specifies predictors for efficiency recovery.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: States significance of long-term models for PNT and efficiency.
    - source_id: P5-S1-C14
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of long-term PNT prediction.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Specifies predictors for long-term PNT recovery.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Specifies predictors for long-term PNT recovery.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: References prior study results.
    - source_id: P6-S1-C12
      disposition: repeated
      result_indexes:
      - 2
      - 4
      reason: Restatement of variance explained by models.
    - source_id: P6-S1-C13
      disposition: repeated
      result_indexes:
      - 2
      - 4
      reason: Restatement of predictors for naming and efficiency.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 2
      - 4
      reason: Specifies contributors to naming and efficiency models.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: States short-term content recovery was not predicted.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: States long-term PNT recovery relied on similar factors.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Specifies predictors for long-term PNT recovery.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about long-term vs short-term efficiency prediction.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Specifies significance of AG, IFOF, and ILF for long-term efficiency.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 10
      reason: States days since stroke was not a significant contributor to long-term
        efficiency.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References prior study on pMTG.
    - source_id: P8-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of pMTG as predictor.
    - source_id: P9-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 4
      reason: Conclusion restating associations.
    - source_id: P9-S1-C2
      disposition: repeated
      result_indexes:
      - 2
      - 4
      - 7
      - 8
      reason: Conclusion restating predictive value.
    - source_id: P9-S2-C9
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      reason: Table 4 providing all regression coefficients and significance.
    unresolved_coverage:
    - source_id: P5-S1-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C6
    - P1-S2-C10
    - P1-S2-C11
    - P3-S1-C1
    - P3-S1-C2
    - P4-S1-C2
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C9
    - P4-S2-C6
    - P5-S1-C1
    - P5-S1-C3
    - P5-S1-C6
    - P5-S1-C7
    - P6-S1-C1
    - P6-S1-C10
    - P6-S1-C12
    - P6-S2-C6
    - P6-S2-C9
    - P8-S1-C2
    - P8-S1-C7
    - P8-S1-C8
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C15
    - P9-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    - TABLE-4-page-9-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C1
      recruited_sample:
      - P2-S2-C4
      eligibility:
      - P2-S3-C2
      - P2-S3-C3
      imaging_provenance:
      - P3-S2-C13
      imaging_timing:
      - P1-S2-C3
      outcome_timing:
      - P3-S1-C11
      - P4-S2-C3
      - P5-S1-C13
      - P6-S1-C11
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P3-S1-C1
      dependent_variable_statement:
      - P4-S2-C3
      limitations:
      - P9-S2-C2
      - P9-S2-C3
      - P9-S2-C5
      - P9-S2-C6
      - P9-S2-C8
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C2
      - P5-S1-C12
      - P6-S2-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S2-C4
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P9-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S2-C3
      - P5-S1-C8
      - P5-S1-C10
      - P5-S1-C11
      - P5-S1-C13
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C6
      - P9-S2-C10
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
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      review_sha256: 01ee30b75663c276f40282f4eae59ba41fd1bf921642665edca50810faa0759f
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
      - P6-S2-C8
      source_result: For the prediction of long-term recovery of discourse efficiency
        (combining 5- and 20-weeks post-treatment), days since stroke was no longer
        a significant contributor to the model, whereas integrity of IFOF and ILF
        reached significance.
      result_status: lost_after_adjustment
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the long-term recovery
            prediction model for discourse efficiency (Syllables/CU) as described
            in P6-S2-C6 and P6-S2-C8. The timing (5- and 20-weeks combined) and outcome
            (efficiency) match the source.
          source_ids:
          - P6-S2-C6
          - P6-S2-C8
          - P4-S2-C3
        direction:
          answer: fits
          reason: The source explicitly states 'Days since stroke was no longer a
            significant contributor to the model' (P6-S2-C8). The draft's claim of
            'no_effect' (interpreted as no statistically detected association in this
            specific model) is faithful to the source text. This is a legitimate adjusted
            null result, not a robustness check of a previous finding.
          source_ids:
          - P6-S2-C8
        construct:
          answer: fits
          reason: The exposure is 'days since stroke' (defined in P9-S2-C12 as days
            from stroke to start of therapy). The outcome is 'discourse efficiency
            improvement' (Syllables/CU change). The method is regression (P4-S2-C2).
            The patient measurement involves DTI metrics (MD) derived from atlas-based
            segmentation (P3-S2-C13), which corresponds to template_lesion_overlap
            in the context of the provided enum options (as opposed to patient_diffusion
            which implies individual tractography, or functional_imaging). The draft
            correctly identifies the construct.
          source_ids:
          - P9-S2-C12
          - P3-S1-C9
          - P3-S2-C13
        qualifications:
          answer: fits
          reason: The draft includes relevant limitations such as small sample size
            (P9-S2-C2) and the combination of active/sham tDCS groups (P9-S2-C3).
            It correctly notes that the model included other predictors (age, MDs).
          source_ids:
          - P9-S2-C2
          - P9-S2-C3
          - P6-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key context that this is a long-term model
            where days since stroke lost significance, unlike the short-term model
            where it was significant (implied by the contrast in P6-S2-C6/C8). No
            material caveat changing the interpretation of the null result is omitted.
          source_ids:
          - P6-S2-C8
          - P6-S2-C6
      optional_pending:
      - Specific p-values or confidence intervals for the 'days since stroke' coefficient
        in the long-term efficiency model are not transcribed.
      - Exact standardized coefficients for the significant predictors (IFOF, ILF)
        in this specific model are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values or confidence intervals for the 'days since stroke' coefficient
      in the long-term efficiency model are not transcribed.
    - Exact standardized coefficients for the significant predictors (IFOF, ILF) in
      this specific model are not transcribed.
    normalizations: []
    analysis_identity:
      id: R011
      exposure:
        text: days since stroke
      outcome:
        text: discourse efficiency improvement
      analysis_label: Long-term recovery prediction (5- and 20-weeks post-treatment)
      relation: performance
      evidence_ids:
      - P6-S2-C8
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
        pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
        source_review: _compare/relationships-2026-11-16/review-current/Stockbridge2024
        source_status_sha256: 09f02c54b11a21800459ff9cf579ef0b656af9442e9b3b3ea2078d148b57f968
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4f505752ed7abf8f3c56839bfe283c100f2274da678e3e41daae011e6860a747
          exclusions_sha256: 35de5f6e2e01b696591d6fb783feb1c4018f49e94e59de888dd9eddaa72472c9
          source_id: P4-S1-C1
          page: 4
          text_layer_sha256: f8b50d0ef8175edb5084c829b71a831f47493b6387ad418fede758fd37d90802
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '

          Brain Structure and Function (2024) 229:2207–2217

          Results

          Participant description

          Twenty-two participants completed diffusion tensor imag­

          ing, summarized in Tables 1, 2 and 3.'
        anchor_text: 'Results

          Participant description

          Twenty-two participants completed diffusion tensor imag­

          ing, summarized in Tables 1, 2 and 3.'
        excluded_fragments:
        - where: leading
          text: Brain Structure and Function (2024) 229:2207–2217
          furniture_line: Brain Structure and Function (2024) 229:2207–2217
          bbox:
          - 374.0
          - 32.3
          - 544.3
          - 42.5
          rule: repeated margin line
        image_sha256: 9e0838fbda763fcc4c0d2b9963190fc83909bd93796f511149a82b75719f1ec6
        transcription: 'Results


          Participant description


          Twenty-two participants completed diffusion tensor imaging, summarized in
          Tables 1, 2 and 3.'
      P2-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e98e66d52f63af9612213f352de84874881a10af9764e5a094e924c31e88b174
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C2
          page: 2
          text_layer_sha256: e98e66d52f63af9612213f352de84874881a10af9764e5a094e924c31e88b174
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Included individu­\nals were right-handed, adult English speakers\
          \ within three \nmonths of ischemic left hemisphere stroke who were diag­\n\
          nosed with aphasia using the Western Aphasia Battery-\nRevised (WAB-R; Kertesz\
          \ 2007)."
        anchor_text: "Included individu­\nals were right-handed, adult English speakers\
          \ within three \nmonths of ischemic left hemisphere stroke who were diag­\n\
          nosed with aphasia using the Western Aphasia Battery-\nRevised (WAB-R; Kertesz\
          \ 2007)."
        excluded_fragments: []
        image_sha256: 60c99015093a22a1ad3decde62e6dbdd30e91cc334e978720f17e5669bc9cc2d
        transcription: '. Included individu-

          als were right-handed, adult English speakers within three

          months of ischemic left hemisphere stroke who were diag-

          nosed with aphasia using the Western Aphasia Battery-

          Revised (WAB-R; Kertesz 2007)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'Days since stroke was no longer a sig­

    nificant contributor to the model.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
