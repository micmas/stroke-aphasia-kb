---
id: nonlinguistic_cognitive_predictors_naming_pmg
name: nonlinguistic cognitive predictors of naming PMG
kind: predictor
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: naming_pmg
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    metric: Proportion of potential maximal gain (PMG)
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: naming_improvement
  target_kind: prognosis
  claim: When controlling for pretreatment apraxia of speech and auditory comprehension
    impairment, pretreatment executive function, visual short-term memory, and auditory
    comprehension were significant predictors of the proportion of potential maximal
    gain (PMG) immediately following naming therapy.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 27
    population: persons with poststroke aphasia
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
  - Small sample size may have resulted in an under-powered analysis
  - Nonlinguistic cognitive assessments in aphasia may be influenced by speech, language,
    or motor impairments
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Pretreatment scores on principal components representing
    executive function, visual short-term memory, and verbal short-term memory, measured
    via a battery including the Cognitive-Linguistic Quick Test, Wechsler Adult Intelligence
    Scale Digit Span, Doors and People Test, and Corsi block-tapping test. Analysis
    used a backward stepwise regression controlling for pretreatment apraxia of speech
    (measured by diadochokinetic productions) and auditory comprehension impairment
    (measured by WAB-R auditory verbal comprehension sub-scores). Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S1-C10, two-model agreement, human verification pending): Sixty-seven
    persons with poststroke aphasia (44 men; mean

    age=60.90; mean months post onset=53.58) were included in

    this study (table 1) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:naming_pmg
  therapy:
    id: semantic_based_naming_treatment
    name: semantic-based naming treatment
  citation: '@Gilmore2019'
  source_passages:
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      auditory comprehension were signiﬁcant predictors, with 1-unit

      increases in each ability predicting .29 (P<.05), .30 (P<.05),

      and .41 (P<.05) increases in PMG, respectively.'
    supports: claim
  - section: Original source P5-S2-C7
    page: 5
    quote: 'Thus, 2 additional backward stepwise regression

      analyses were conducted to predict PMG and PMGM using

      executive function, visual short-term memory, and verbal short-

      term memory, while controlling for pretreatment apraxia of

      speech and auditory comprehension impairment.'
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: 'The model pre-

      dicting PMG (nZ27) explained 57% of the variance (adjusted R2),

      F4,22Z9.7, P<.001.'
    supports: method
  - section: Original source P3-S2-C5
    page: 3
    quote: 'In addition to study 1’s assessments, these participants

      were given the following nonlinguistic cognitive assessments

      before treatment: the Wechsler Adult Intelligence Scale Digit

      Span Forward24 and Backward to measure verbal short-term

      memory; the Visual Recognition subtest of the Doors and Peo-

      ple Test25 and the Corsi block-tapping test26 to measure visual

      short-term memory; and 2 visuospatial tasks (ie, Geometric

      Matching and Inclusion).'
    supports: method
  - section: Original source P2-S1-C10
    page: 2
    quote: 'Sixty-seven persons with poststroke aphasia (44 men; mean

      ageZ60.90; mean months post onsetZ53.58) were included in

      this study (table 1).'
    supports: sample
  - section: Original source P3-S3-C3
    page: 3
    quote: Data from 27 participants in study 1 who had undergone naming therapy were
      used in study 2.
    supports: sample
  - section: Original source P5-S1-C3
    page: 5
    quote: 'The participant-to-variable ratio of 1.93 may have

      resulted in an under-powered analysis; thus, 2 alternative analyses

      were conducted to compensate for this potential limitation.'
    supports: limitation
  - section: Original source P7-S1-C3
    page: 7
    quote: 'Furthermore, there are currently no gold

      standard assessments for assessing nonlinguistic cognition in

      aphasia.29 Thus, participants’ performance on some nonlinguistic

      cognitive assessments used in the present study may have been

      negatively affected by speech (eg, apraxia of speech may have

      inﬂuenced accurate production on digit span tasks), language (eg,

      auditory

      comprehension

      may

      have

      hindered

      understanding

      instructions), or motor impairment (eg, hemiplegia may have

      affected pen and paper timed tasks).'
    supports: limitation
predictor_type: behavioural
short_definition: Pretreatment scores on principal components representing executive
  function, visual short-term memory, and verbal short-term memory, measured via a
  battery including the Cognitive-Linguistic Quick Test, Wechsler Adult Intelligence
  Scale Digit Span, Doors and People Test, and Corsi block-tapping test.
assessment:
- Cognitive-Linguistic Quick Test
- Wechsler Adult Intelligence Scale Digit Span Forward
- Wechsler Adult Intelligence Scale Digit Span Backward
- Doors and People Test Visual Recognition subtest
- Corsi block-tapping test
- Geometric Matching
- Inclusion
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Gilmore2019
  proposal_id: R005
  review_status_sha256: 7001af961c08c596f74251ba1bb1b4c1d9ade92b813171eb4c32d150ba662573
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
        A/passages.json: 5e95504eb79f73241e889437bd0c3e82996bff995f0e87ba69a572069da8fdba
        A/raw.json: 584680b802ccb622c6969a7b3e1ac84b326282b27978d7b703ac4b9b81855334
        A/source-units.json: 38ec334e8ac984801fde44f3420fa0f1b6852f81cccfd45cb0efa2dd89936033
        A/full-source-units.json: c0cf686a3d8cfe41517aaa26442f13fc7e80dffa280bc11a2357de830930459b
        A/meta.json: 1181fd74d7e4c61a71d25d3729541172b2976a2376538ed7e76546b4d2b8590c
        A/table-images/TABLE-1-page-5-1.png: 1dc3933a32115e6089537f174d7757fb73670b28389675d49e1022e9b2276290
        A/table-images/page-6.png: d65f0a41d4285f25b5d7c3d69798ea60abe585b2747ad07d490cac5dad461210
        A/table-images/page-7.png: 6d95b0ad0f00933ca117b59335cf5e77c7df66620cf775eb382811213d5941d2
        A/table-images/page-5.png: 8edfeaa2626540498d0c176e0916f5350768ea3040b4072c60966ff31ced372f
        A/table-images/page-4.png: 28de588648ed496c616a140940c0d00d4ab3f4c05e455b25d0e5ca3206785b2d
        A/table-images/TABLE-1-page-4-1.png: 1705fb7a795f925bfd7ade693cd48d48dd0649b108f46142249a9114024554b8
        A/table-images/TABLE-2-page-6-1.png: 19c00b3b01759cb3871b9bd8d82eacfdd3dc63788906363e8e1581e05df325d8
        A/table-images/manifest.json: e73f33b8662417c23e62367a2ec983200e58013cdf1b475b69fd4118d5475153
        A/table-images/TABLE-3-page-7-1.png: 6e8b11fe93b7a6c40e3372fffe54c8cdcdf65a42b7c1402bae19657074f427b3
        A/clauses/window-03/raw.json: 5fac75134172c6f9da426e1b5e044817f56b53152469f2c4c1a1ea462b6ea64d
        A/clauses/window-03/prompt.txt: 33829d2622c8d9770856e43f2ec688a3115bdd59625428de563ccf8dd3bc2098
        A/clauses/window-03/meta.json: 98b66d311e15024d3272b638af682c5afaeea0dc2a419396a0b2ddec7bbfdf50
        A/clauses/window-04/raw.json: 17e41c988c35e417d562f096ed90d66cb42c4f033a6df47f630a76869fb2d25c
        A/clauses/window-04/prompt.txt: 06dad175f4a1d078cff8fa6a45be607b304934d1c2a19b4546b435d36d6fac88
        A/clauses/window-04/meta.json: e50d1a4588691f20959513e333bb3be69a78a8bc97c2eda99204a8d05b48e723
        A/clauses/window-05/raw.json: 61482795c22f4bf11948cf53b46ce360ed9bd679635126401e5ceb5c54106a08
        A/clauses/window-05/prompt.txt: 06109112fcd5babd687e9232baacde5c684d3a00a3784cfec20b6895447c60d0
        A/clauses/window-05/meta.json: 2313010879cb5aea2dd3485b0198027006fed1f34fc494a19660ff8187843886
        A/clauses/window-02/raw.json: ecb25dbc31cd5f448b384e92219eed9a0c74a6953e9c8c9a84d267a7ba4ca329
        A/clauses/window-02/prompt.txt: bb2d703cd623b860a4477a5affadd5c0301aa8f6b12f4ab04bd61a885a5eb490
        A/clauses/window-02/meta.json: a11575d6cda26a117f101a52f4c4861068bf115cc2d37f43cf14fe88c09515ea
        A/clauses/window-01/raw.json: c936f576b636afa1a06548cd8976d6434884410b60922c305a671a430914e1e1
        A/clauses/window-01/prompt.txt: 733ea9462cddc6e2189ced7259994310c56f955ae023eaa7c761cbce819f7bb5
        A/clauses/window-01/meta.json: 8ba4bdbe4afb24e6c88199de3f1724409423866098267a8d83afe27cd4e63bf5
        A/tables/TABLE-2-page-6-3/raw.json: fe1862cbf220237568483a10c573530d1174be8d149b6adea9b543db31acc3c0
        A/tables/TABLE-2-page-6-3/prompt.txt: 496f47d5c220beeee53373e26f6d1e4e705302ebd0321debb3549daa8a18dc23
        A/tables/TABLE-2-page-6-3/meta.json: d74e0b091735e7a5e2121696f1c448360281648f3f62fdaa9b57523789742842
        A/tables/TABLE-1-page-5-2/raw.json: c5346e4f11a45c80b9ab43d95b8f5a8d926ab168cbca2e5123d49ecd89f98446
        A/tables/TABLE-1-page-5-2/prompt.txt: aa383f2922a15518570c560433767cff16a4064f06b56cff25d57ba188601533
        A/tables/TABLE-1-page-5-2/meta.json: 181f92fb43cc187586cd10fddf2950531127d765d01cea8ec0f252001b8f5019
        A/tables/TABLE-3-page-7-4/raw.json: eeb77d62b7479ab260ffdc221270d75d60996dd14bb0bcb543eba83d1faada27
        A/tables/TABLE-3-page-7-4/prompt.txt: 026e23cc968b926dd71c00ac96e7c3b1b72fa23545530e39da356aa34f0bd828
        A/tables/TABLE-3-page-7-4/meta.json: 544e50018aeda90e116472bce4f52c7fc7799411557a4d03827e118cc9f66dc2
        A/tables/TABLE-1-page-4-1/raw.json: 2d9ef0fe10f471dd374f7ba7b252af49eaed6b93fa05f9ad31dc3dc54c3713ee
        A/tables/TABLE-1-page-4-1/prompt.txt: b01be8884a352de95bfd1629dd8aae2a198f3367d6b223c89bb7be94e6a0e162
        A/tables/TABLE-1-page-4-1/meta.json: ffd2db641057ac2537a3a69c4ba7a8655d0bbc962cc6aa85308766afe8ae526d
        B/passages.json: 5e95504eb79f73241e889437bd0c3e82996bff995f0e87ba69a572069da8fdba
        B/raw.json: b6368666da9d7b8c2f6d3b3282db8fa5fe840d94f46147161a077c6626f99d22
        B/source-units.json: 38ec334e8ac984801fde44f3420fa0f1b6852f81cccfd45cb0efa2dd89936033
        B/full-source-units.json: c0cf686a3d8cfe41517aaa26442f13fc7e80dffa280bc11a2357de830930459b
        B/meta.json: d507c97990e44e0c19bf33c350950c941e790c21dbcdb918312cb322d4440d80
        B/table-images/TABLE-1-page-5-1.png: 1dc3933a32115e6089537f174d7757fb73670b28389675d49e1022e9b2276290
        B/table-images/page-6.png: d65f0a41d4285f25b5d7c3d69798ea60abe585b2747ad07d490cac5dad461210
        B/table-images/page-7.png: 6d95b0ad0f00933ca117b59335cf5e77c7df66620cf775eb382811213d5941d2
        B/table-images/page-5.png: 8edfeaa2626540498d0c176e0916f5350768ea3040b4072c60966ff31ced372f
        B/table-images/page-4.png: 28de588648ed496c616a140940c0d00d4ab3f4c05e455b25d0e5ca3206785b2d
        B/table-images/TABLE-1-page-4-1.png: 1705fb7a795f925bfd7ade693cd48d48dd0649b108f46142249a9114024554b8
        B/table-images/TABLE-2-page-6-1.png: 19c00b3b01759cb3871b9bd8d82eacfdd3dc63788906363e8e1581e05df325d8
        B/table-images/manifest.json: 23f8b5b43dac6a3284cbef1af79c37cb6ecb3e07dcccf425d81d7912eac9c9c9
        B/table-images/TABLE-3-page-7-1.png: 6e8b11fe93b7a6c40e3372fffe54c8cdcdf65a42b7c1402bae19657074f427b3
        B/clauses/window-03/raw.json: 5629b1135d7f125206bd55b739680875d20eb9ec3f2966c2ae4ee3303c142699
        B/clauses/window-03/prompt.txt: 33829d2622c8d9770856e43f2ec688a3115bdd59625428de563ccf8dd3bc2098
        B/clauses/window-03/meta.json: ea51c1798327f7e3ee657f27e26666390c7c8d86da4977415cb400c97fb047e5
        B/clauses/window-04/raw.json: d6b90caf358da16c11695101b77b23e93e66a93dfe7953953695ab67576e3305
        B/clauses/window-04/prompt.txt: 06dad175f4a1d078cff8fa6a45be607b304934d1c2a19b4546b435d36d6fac88
        B/clauses/window-04/meta.json: 4e9690d09970c905260c8478a347e341c5ac1faf028027299bf60166b5fe29c3
        B/clauses/window-05/raw.json: c66191c1d13b5e4269413008f94fa80ebc7a3bd7cf366581a38b3f4e73d3234b
        B/clauses/window-05/prompt.txt: 06109112fcd5babd687e9232baacde5c684d3a00a3784cfec20b6895447c60d0
        B/clauses/window-05/meta.json: afcc9647d01b64852ebeae3099fb911b60c525f2f337d85fe680577e47726395
        B/clauses/window-02/raw.json: e6aa99b2bed57f993a781eb1b333fecda178e104cc0cf0694698273ea8bbbceb
        B/clauses/window-02/prompt.txt: bb2d703cd623b860a4477a5affadd5c0301aa8f6b12f4ab04bd61a885a5eb490
        B/clauses/window-02/meta.json: 85f898853fde80bdc6ec81f75f89fea0928f8090581248b442d9df6e861a1038
        B/clauses/window-01/raw.json: 01cb81fb6f40ab46341ef2fa4f7f3d1eb366ac040dd37c91ad3ebea026a2d95b
        B/clauses/window-01/prompt.txt: 733ea9462cddc6e2189ced7259994310c56f955ae023eaa7c761cbce819f7bb5
        B/clauses/window-01/meta.json: 81a090deecdac152c55be1705900614aa59d1c18ce43df34edd78e0be289dc81
        B/tables/TABLE-2-page-6-3/raw.json: 034a29e7d01f95e9284b6748a89671dd115ce46a9b3b26b948a1023c6da62f7e
        B/tables/TABLE-2-page-6-3/prompt.txt: 496f47d5c220beeee53373e26f6d1e4e705302ebd0321debb3549daa8a18dc23
        B/tables/TABLE-2-page-6-3/meta.json: c39524ce880c41b3c47e7a704349f6f301c320801e2da6bacd576b93e59b4a37
        B/tables/TABLE-1-page-5-2/raw.json: 1d177cd951a54aa69bf4f46cb8fdbafb1fcc83e6853f9f8398d4c5d2fab4bd8c
        B/tables/TABLE-1-page-5-2/prompt.txt: aa383f2922a15518570c560433767cff16a4064f06b56cff25d57ba188601533
        B/tables/TABLE-1-page-5-2/meta.json: 0bad4d6e7d93c943fa504bc94ab1d0f35333f51cb0a3a064e81c99d3bbf7f33a
        B/tables/TABLE-3-page-7-4/raw.json: 5f7d40c4ea95a7923cb44de2e3733e8fae1b8169c10d0f37ad514b742e074fc3
        B/tables/TABLE-3-page-7-4/prompt.txt: 026e23cc968b926dd71c00ac96e7c3b1b72fa23545530e39da356aa34f0bd828
        B/tables/TABLE-3-page-7-4/meta.json: aca8ed902ca037731e74a1b247fadc707384985232f9a1ae9b8099ceaf17300b
        B/tables/TABLE-1-page-4-1/raw.json: 2438aa5dcb3ff0e7dfd1415c67972db2b560cea2054096742ce5ecdbb4e5a718
        B/tables/TABLE-1-page-4-1/prompt.txt: b01be8884a352de95bfd1629dd8aae2a198f3367d6b223c89bb7be94e6a0e162
        B/tables/TABLE-1-page-4-1/meta.json: 87777ea7aa0bd5ddc0463379039b0107606a634c7e16b26836b37dea2e9c73e2
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
      pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
      source_review: _compare/relationships-2026-11-16/review-current/Gilmore2019
      source_status_sha256: e10eacdf20bc19220e6c9eae4c0134fc06df717043ec129f01aff3a619c07da9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: executive function, visual short-term memory, and auditory comprehension
    outcome:
      text: proportion of potential maximal gain (PMG) after naming therapy
    analysis_label: Study 2 Adjusted Backward Stepwise Regression
    relation: sensitivity
    evidence_ids:
    - P6-S1-C1
    qualifier_ids:
    - P5-S2-C7
    - P5-S2-C8
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
      source_review: _compare/relationships-2026-11-16/review-current/Gilmore2019
      source_status_sha256: e10eacdf20bc19220e6c9eae4c0134fc06df717043ec129f01aff3a619c07da9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C12
      - Accounting without a linked unit P1-S1-C13
      - Result passage disposed without unit P1-S1-C14
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C13
      - Result passage disposed without unit P3-S1-C10
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P5-S1-C4
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S2-C9
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C5
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P6-S2-C12
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C5
      - Accounting without a linked unit P7-S1-C6
      - Unaccounted source passage P7-S1-C6
      unattached_null_or_qualifier_ids:
      - P1-S1-C14
      - P1-S2-C3
      - P3-S1-C10
      - P5-S1-C4
      - P5-S2-C9
      - P6-S1-C3
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 78
      unselected_timing_passages:
      - P2-S1-C10
      - P5-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C7
        - P1-S1-C8
        - P2-S1-C10
        - P3-S3-C3
        - P5-S1-C1
        - P5-S1-C5
        - P5-S1-C8
        - P5-S1-C13
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C8
        - P5-S2-C9
        - P6-S1-C2
        - P6-S1-C10
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        - P6-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-6-3
      - TABLE-3-page-7-4
      unlinked_tables:
      - TABLE-3-page-7-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
      source_review: _compare/relationships-2026-11-16/review-current/Gilmore2019
      source_status_sha256: e10eacdf20bc19220e6c9eae4c0134fc06df717043ec129f01aff3a619c07da9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports prevalence of deficits, not a relationship between exposure
        and outcome.
    - source_id: P1-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA dimensionality reduction.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of Study 1 regression results.
    - source_id: P1-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA dimensionality reduction for Study 2.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Abstract restatement of Study 2 findings.
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports prevalence of deficits.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean PMG score.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance explanation.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA component loading description.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA component loading description.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA component summary.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Specific test loading detail.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Model fit statistics (variance explained).
    - source_id: P3-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies variables in the best-fit model for Study 1.
    - source_id: P3-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant predictors for PMG in Study 1.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant interaction effect.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Interprets the interaction effect.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplemental appendix.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean PMG for Study 2.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean PMGM for Study 2.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance explanation.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA component characterization.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Model fit statistics for PMG in Study 2.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant predictors for PMG in Study 2.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Model fit statistics for PMGM in Study 2.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant predictors for PMGM in Study 2.
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Summary interpretation of Study 2 results.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Model fit statistics for adjusted PMG model.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement that all variables were retained in the model.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant predictors for adjusted PMG model.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Model fit statistics for adjusted PMGM model.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports significant predictors for adjusted PMGM model.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Discussion summary of adjusted findings.
    - source_id: P6-S2-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      reason: Discussion restatement of Study 2 findings.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      reason: Discussion restatement of Study 2 findings.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about supplemental support.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports prevalence of deficits.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of Study 1.
    - source_id: P7-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      reason: Conclusion restatement of Study 2.
    unresolved_coverage:
    - source_id: P6-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P1-S1-C14
    - P1-S2-C3
    - P2-S3-C9
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C6
    - P3-S1-C7
    - P3-S1-C9
    - P3-S1-C10
    - P5-S1-C4
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C10
    - P5-S1-C11
    - P5-S1-C13
    - P5-S2-C3
    - P5-S2-C5
    - P5-S2-C8
    - P5-S2-C9
    - P6-S1-C2
    - P6-S1-C5
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C6
    - P6-S2-C12
    - P6-S3-C2
    - P6-S4-C2
    - P7-S1-C2
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-1-page-5-2
    - TABLE-2-page-6-3
    - TABLE-3-page-7-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P2-S1-C6
      eligibility:
      - P2-S2-C2
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C10
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
      - P5-S1-C6
      - P5-S3-C6
      - P5-S3-C7
      outcome_definition:
      - P1-S1-C10
      - P2-S2-C6
      - P3-S2-C9
      - P3-S2-C10
      - P5-S3-C6
      - P5-S3-C7
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S3-C6
      - P5-S1-C5
      limitations:
      - P5-S1-C3
      - P7-S1-C1
      - P7-S1-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S2-C3
      - P3-S1-C10
      - P5-S1-C6
      - P5-S2-C7
      - P5-S2-C7
      - P5-S2-C9
      - P6-S1-C1
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C10
      - P4-S1-C1
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: not_stated
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C7
      - P1-S1-C8
      - P2-S1-C10
      - P3-S3-C3
      - P5-S1-C1
      - P5-S1-C5
      - P5-S1-C8
      - P5-S1-C13
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C8
      - P5-S2-C9
      - P6-S1-C2
      - P6-S1-C10
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
      - P6-S1-C11
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
      pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
      review_sha256: 7001af961c08c596f74251ba1bb1b4c1d9ade92b813171eb4c32d150ba662573
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
      - P6-S1-C1
      source_result: In the adjusted backward stepwise regression model predicting
        PMG (n=27), executive function, visual short-term memory, and auditory comprehension
        were significant predictors, with 1-unit increases predicting .29, .30, and
        .41 increases in PMG, respectively (P<.05).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the adjusted backward stepwise
            regression for PMG described in P5-S2-C7 and P5-S2-C8, with results in
            P6-S1-C1. The model includes executive function, visual short-term memory,
            and auditory comprehension as predictors.
          source_ids:
          - P5-S2-C7
          - P5-S2-C8
          - P6-S1-C1
        direction:
          answer: fits
          reason: The source states that 1-unit increases in executive function, visual
            short-term memory, and auditory comprehension predicted increases in PMG.
            The draft claim correctly reflects this positive association.
          source_ids:
          - P6-S1-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as pretreatment nonlinguistic
            cognitive skills (executive function, visual short-term memory) and auditory
            comprehension. The outcome is PMG after naming therapy. The method is
            behavioral regression, not imaging-based.
          source_ids:
          - P3-S2-C5
          - P5-S1-C6
          - P6-S1-C1
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the analysis
            controlled for apraxia of speech and auditory comprehension impairment,
            as stated in P5-S2-C7 and P5-S2-C8.
          source_ids:
          - P5-S2-C7
          - P5-S2-C8
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitations regarding sample size and
            potential confounding of nonlinguistic assessments by speech/language/motor
            impairments, as noted in P5-S1-C3 and P7-S1-C3. No material caveats are
            omitted.
          source_ids:
          - P5-S1-C3
          - P7-S1-C3
      optional_pending:
      - sample.time_post_onset
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
    - sample.time_post_onset
    normalizations:
    - field: sample.time_post_onset
      original: pretreatment predictors of immediate post-treatment outcome (10-12
        weeks)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 12, 1E+1'
    analysis_identity:
      id: R005
      exposure:
        text: executive function, visual short-term memory, and auditory comprehension
      outcome:
        text: proportion of potential maximal gain (PMG) after naming therapy
      analysis_label: Study 2 Adjusted Backward Stepwise Regression
      relation: sensitivity
      evidence_ids:
      - P6-S1-C1
      qualifier_ids:
      - P5-S2-C7
      - P5-S2-C8
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
        source_review: _compare/relationships-2026-11-16/review-current/Gilmore2019
        source_status_sha256: e10eacdf20bc19220e6c9eae4c0134fc06df717043ec129f01aff3a619c07da9
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: aecbf667437b923f7d2bff01add1d250272fd4ac792cd81be45f50506565c11b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C10
          page: 2
          text_layer_sha256: aecbf667437b923f7d2bff01add1d250272fd4ac792cd81be45f50506565c11b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Sixty-seven persons with poststroke aphasia (44 men; mean

          ageZ60.90; mean months post onsetZ53.58) were included in

          this study (table 1).'
        anchor_text: 'Sixty-seven persons with poststroke aphasia (44 men; mean

          ageZ60.90; mean months post onsetZ53.58) were included in

          this study (table 1).'
        excluded_fragments: []
        image_sha256: a339ebe5c11ad21e5e9eb97336cba8057a07df46b7f67b05c34c25d4297edede
        transcription: 'Sixty-seven persons with poststroke aphasia (44 men; mean

          age=60.90; mean months post onset=53.58) were included in

          this study (table 1)'
      P3-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6245ce962feb99ec0499f8e3850727037bd2d8afbfdb3a7f6550710bdbf310e2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fa92ae3ce4c8b466fcf28c5a616df134747d07cceb69b0ea31097e805bd6415f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C3
          page: 3
          text_layer_sha256: fa92ae3ce4c8b466fcf28c5a616df134747d07cceb69b0ea31097e805bd6415f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: Data from 27 participants in study 1 who had undergone naming
          therapy were used in study 2.
        anchor_text: Data from 27 participants in study 1 who had undergone naming
          therapy were used in study 2.
        excluded_fragments: []
        image_sha256: bf4624df393aeeb1202a1cdc14ea4e92df0d9209a6d4a9c2506c2a1a95d46331
        transcription: Data from 27 participants in study 1 who had undergone naming
          therapy were used in study 2.
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: '

    auditory comprehension were signiﬁcant predictors, with 1-unit

    increases in each ability predicting .29 (P<.05), .30 (P<.05),

    and .41 (P<.05) increases in PMG, respectively.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
