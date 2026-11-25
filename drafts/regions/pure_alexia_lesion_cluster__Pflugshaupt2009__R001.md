---
id: pure_alexia_lesion_cluster
name: pure alexia cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: pure_alexia
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: pure_alexia
  target_kind: impairment
  claim: Subtracting the lesions of hemianopic dyslexics from those found in pure
    alexics revealed the largest group differences in posterior parts of the left
    fusiform gyrus, occipito-temporal sulcus and inferior temporal gyrus, including
    the coordinate assigned to the centre of the visual word form area in healthy
    adults.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: not_reported
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: Concurrent with neuropsychological assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (n=6 per group) may limit statistical power.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap subtraction analysis comparing
    pure alexia patients against hemianopic dyslexia patients with similar right-sided
    visual field defects. The analysis specifically contrasted pure alexia against
    hemianopic dyslexia to isolate the contribution of the visual field defect. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S3-C5, two-model agreement, human verification pending):
    . During the

    5 years needed to assemble appropriate participants for the present

    study, six patients with pure alexia were identified from the population

    of in-patients at our unit of cognitive and restorative neurology Original text-layer
    quotation is preserved below.'
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
    - not_transcribed:sample.population
    - proposed_concept:pure_alexia
  citation: '@Pflugshaupt2009'
  source_passages:
  - section: Original source P1-S1-C9
    page: 1
    quote: 'In addition, subtracting the lesions of the hemianopic dyslexics from
      those found in pure alexics revealed the largest group

      differences in posterior parts of the left fusiform gyrus, occipito-temporal
      sulcus and inferior temporal gyrus.'
    supports: claim
  - section: Original source P6-S1-C14
    page: 6
    quote: 'The most pro-

      nounced differences between groups were found in posterior

      parts of the left fusiform gyrus, occipito-temporal sulcus and infe-

      rior temporal gyrus.'
    supports: claim
  - section: Original source P1-S2-C3
    page: 1
    quote: 'These regions

      included the coordinate assigned to the centre of the visual word form area
      in healthy adults, which provides further evidence

      for a relation between pure alexia and a damaged visual word form area.'
    supports: claim
  - section: Original source P3-S3-C5
    page: 3
    quote: 'During the

      5 years needed to assemble appropriate participants for the present

      study, six patients with pure alexia were identiﬁed from the population

      of in-patients at our unit of cognitive and restorative neurology.'
    supports: sample
  - section: Original source P3-S3-C10
    page: 3
    quote: 'First, six patients with hemianopic dyslexia due to right-sided

      visual ﬁeld loss participated as a clinical control group.'
    supports: sample
  - section: Original source P5-S1-C12
    page: 5
    quote: 'Furthermore, the MRIcroN software

      (www.mricro.com/mricron; Rorden et al., 2007) was applied to create

      group-speciﬁc lesion overlay plots and a subtraction plot displaying

      voxels more often affected in pure alexia than in hemianopic dyslexia

      and vice versa.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pflugshaupt2009
  proposal_id: R001
  review_status_sha256: 3e26a548d6f52e1651cd7d9cc5666111b27be92ce1339006b9d60eaffd0e52ef
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
        A/passages.json: 57abf5a023a32b8e3a70b622644683289eaa8950fa76db77fcd6c02579790e87
        A/raw.json: 469bffa88048b2c4ff324e9d19c8836436a0bf22f258d2c534af7e5a7eedc07e
        A/source-units.json: f7043b5f7cc7345529053b4a5524e5b45850cae7b17a4ba042fb2db5413818a3
        A/full-source-units.json: 6db555800ace9f9cf720047eda4d251c49609ddf4f84549a4ae773f3003aae14
        A/meta.json: 44d5fe67c08959e4c6c3f9b2dbab8bdf514148226af09657d978c728583f0d61
        A/table-images/page-4.png: fac94b4966da3becd791a3f1ae367e1dd9b9ff01a949fc2662c5cf683e9b87a6
        A/table-images/TABLE-1-page-4-1.png: 9fb6d589ed16c9cabdd1d8a880eb476ede0a7d625034a3011980762b0792e574
        A/table-images/manifest.json: 48cd18205f6b89e331fcb1868b6618da8cb170f3d4fd27f4ba6c5473aadd57cc
        A/clauses/window-03/raw.json: 531b1fae18b3a5bcd6f51a439925c537b34d1c8553870a80d8c268f5a6a3b09f
        A/clauses/window-03/prompt.txt: c02dd1639859f9e0046736b8686bc5c7acf7fa97c659f59df1f9088fa426c149
        A/clauses/window-03/meta.json: cb5a937896727b3f7cc1d88b42647e8b2daa14e7366c5da254636a5bbee42cde
        A/clauses/window-04/raw.json: 60dbdefe30c3d787cd4b299980aa2d83dc2e29c5a29fd4aabb5e7eb7dae288cf
        A/clauses/window-04/prompt.txt: ef4dac23076b80ed3a6af22608a1389b6061a796bd511e975a686f6c9a8df9c3
        A/clauses/window-04/meta.json: ca80dafb33192226fab8a193a2f5ebfcd070b71a77f0160929af1997f0a89d14
        A/clauses/window-05/raw.json: d41077a6cae2bce1f9fc77f681923615d022e1369bfe749ee5def6ed6fac040d
        A/clauses/window-05/prompt.txt: 2d0b52c8d9e7584da8392ef4b2a167b7e365166b890276a8a4b52e11353d9885
        A/clauses/window-05/meta.json: 48d91948976a2e7ee678ead0297c456d06e0f2ad1a2f77436029368dfe290fd4
        A/clauses/window-02/raw.json: 164713fd116bd25e344a2f33774b30783d4518d50c2d9356c2a409b3ced3ee65
        A/clauses/window-02/prompt.txt: 6b8b28a5a185ebdcb1d1d11bdbc30ff0749ef4010e43e2572ce6de2d89b10096
        A/clauses/window-02/meta.json: d2b062ce92da538e03d61e2e6c566cf2d6d92508eded004dd3415f5c1b635c47
        A/clauses/window-09/raw.json: eca66ca11360d13199ed9f2c1049ba2841a9b92b38ba430119fcffc6548a8154
        A/clauses/window-09/prompt.txt: adcb23299bc6763a73b6bc6c5b3a6160ea4224da09a5bdb2a66bebc52f569de2
        A/clauses/window-09/meta.json: 5a910f6c61aaf71684f902260a519370035e34396736915ba2a785833bdd3745
        A/clauses/window-07/raw.json: 9fb7186285f1dbad96c5a52733a7d6ffcc94563a8becdf08133b19430ef687ae
        A/clauses/window-07/prompt.txt: cb3cb232f131d74da9108cb18b15bbfdba7226a8ceace68cdb4dc4692087b8ca
        A/clauses/window-07/meta.json: 128a83a1a678372bdff1a439dcd988a5894374290c30c0ebad8ca6522550d15e
        A/clauses/window-01/raw.json: f33ace62d83b6931adc9c0f89926684e7ccda1906d577fb0b352b11df482020e
        A/clauses/window-01/prompt.txt: fb9bee52492ae70d32071310c288478899c27bfb07c815d8164e63fb26026f04
        A/clauses/window-01/meta.json: 226e362b14d19d724656b1637aceaf04823e951f2fdd421e06ab31e1114f689f
        A/clauses/window-06/raw.json: e449afd26cb1394c1392fcf798109c27e642581b4c6cbefaeb654e64603d34f8
        A/clauses/window-06/prompt.txt: 64cbe9714ffc5563db46eb38efad5722660c5e78b78a348befda1ea2c1f970bb
        A/clauses/window-06/meta.json: d76c84cdd4243232e199897e2e77104493ffd84d74e95f6e4eab60711b911e2d
        A/clauses/window-08/raw.json: c8306e28495962eaf69bf87c464978fec1fad8efa7fe98819e3bd8f51305f453
        A/clauses/window-08/prompt.txt: 4ba142de2f6f2466ba281f3b322b4b556778550bac09cd2da02d0357b4c66417
        A/clauses/window-08/meta.json: 522d264eafef41d7d12ee0c3404fb018c0dbebefb482bce9b801c2aed4e6f74a
        A/tables/TABLE-1-page-4-1/raw.json: 50df65c2e42829018a60e9e51cc4bddfbac2371e5c791dc1ab1de1f8845af919
        A/tables/TABLE-1-page-4-1/prompt.txt: fb65b63c72b21f69a38b5c87627c349ebf281ccaf82648ed127118bfb648a460
        A/tables/TABLE-1-page-4-1/meta.json: 5630861e844ffab6ce74b04df7a36bb41999c111d22228591a88e9d8a6a12d65
        B/passages.json: 57abf5a023a32b8e3a70b622644683289eaa8950fa76db77fcd6c02579790e87
        B/raw.json: 96ef1229d64844dfcc074c75955632066329c240c3c2823448192a9dc0f4bdfb
        B/source-units.json: f7043b5f7cc7345529053b4a5524e5b45850cae7b17a4ba042fb2db5413818a3
        B/full-source-units.json: 6db555800ace9f9cf720047eda4d251c49609ddf4f84549a4ae773f3003aae14
        B/meta.json: b1e7d215fac4ede569489bdceefe2fdfac5733e25dae0c8e1b4916797d241480
        B/table-images/page-4.png: fac94b4966da3becd791a3f1ae367e1dd9b9ff01a949fc2662c5cf683e9b87a6
        B/table-images/TABLE-1-page-4-1.png: 9fb6d589ed16c9cabdd1d8a880eb476ede0a7d625034a3011980762b0792e574
        B/table-images/manifest.json: 7a60e3255c3b03ec4cbd65b5d8972f37d0f42a5ca82e078d72342d7738c86777
        B/clauses/window-03/raw.json: 9f14d44b34e52b8c42174e55522acadd608c3859642759b053651128bcb0907e
        B/clauses/window-03/prompt.txt: c02dd1639859f9e0046736b8686bc5c7acf7fa97c659f59df1f9088fa426c149
        B/clauses/window-03/meta.json: 308042339364162421c6ae5dd89b3873d2c074613a37ea7a268800b801067624
        B/clauses/window-04/raw.json: 76ff3b017a26d4c611aaebb0bfefdc2b8f4bc15840a07a4d55267b9b900200e8
        B/clauses/window-04/prompt.txt: ef4dac23076b80ed3a6af22608a1389b6061a796bd511e975a686f6c9a8df9c3
        B/clauses/window-04/meta.json: 65e06eb35f74230435f88af2da64fffff7ad53c7fd057dc631eae479fd9d91ef
        B/clauses/window-05/raw.json: b61194d145f5f1bb7d1b213a1ed9746bc7f59c32ec187c97184fe49fd3a18b62
        B/clauses/window-05/prompt.txt: 2d0b52c8d9e7584da8392ef4b2a167b7e365166b890276a8a4b52e11353d9885
        B/clauses/window-05/meta.json: 2d47467fc34f8f689b1015813fc2fa7882a32f6143c3e0499cfae5bdf7691b8c
        B/clauses/window-02/raw.json: 1a0600a7601bf5dd99cd27e7a88587f3d56fec0f3dc3f60580b0a27a549ee7ae
        B/clauses/window-02/prompt.txt: 6b8b28a5a185ebdcb1d1d11bdbc30ff0749ef4010e43e2572ce6de2d89b10096
        B/clauses/window-02/meta.json: 58dc65b763d12981ee44b4f19c615c641543c246880cbd65f6365a313fa397d3
        B/clauses/window-09/raw.json: ccad9db8eb8ec23d0f68adfa2541f62b13696a792a395bbbf0e79038cbcaccbd
        B/clauses/window-09/prompt.txt: adcb23299bc6763a73b6bc6c5b3a6160ea4224da09a5bdb2a66bebc52f569de2
        B/clauses/window-09/meta.json: 52738a2a1917651861acbc9e132b30ca4535416cea4ea6f7b45f821c51e047f6
        B/clauses/window-07/raw.json: f048c5bad7f19c8baf1d4c8f682d81eae9088d89cd5393e03f3e7e49ae8014dd
        B/clauses/window-07/prompt.txt: cb3cb232f131d74da9108cb18b15bbfdba7226a8ceace68cdb4dc4692087b8ca
        B/clauses/window-07/meta.json: d2a92ca815919ac71988ea703a10e892e78aa9cbfa2cac1f51a101616ccd37e3
        B/clauses/window-01/raw.json: f4e82c9c5cb1d79a1fa4d2b8da682bfd7fa9b11bc3e0a5582b0bffb8c242beef
        B/clauses/window-01/prompt.txt: fb9bee52492ae70d32071310c288478899c27bfb07c815d8164e63fb26026f04
        B/clauses/window-01/meta.json: 2070475f3453cd2d4091b7fc9c75d6db3ab1cc28dccea1d8b87a059a7c43d039
        B/clauses/window-06/raw.json: 7bde57d354ae35afa32ebb5ccd1baca47d229deb6efb120dfce8a0890dc3a379
        B/clauses/window-06/prompt.txt: 64cbe9714ffc5563db46eb38efad5722660c5e78b78a348befda1ea2c1f970bb
        B/clauses/window-06/meta.json: 696f9a2032e9f7dc0d61fcec14831f24c045df68da640901a639921c57cf8b13
        B/clauses/window-08/raw.json: 5d0e215b410540d6356bbf61679c6010a5bc601a22fddacbbfc560c17b7c688f
        B/clauses/window-08/prompt.txt: 4ba142de2f6f2466ba281f3b322b4b556778550bac09cd2da02d0357b4c66417
        B/clauses/window-08/meta.json: fcfe8fc65092f85570f63b8684b0703ee17a32cf487c72c472fa04fd513e6beb
        B/tables/TABLE-1-page-4-1/raw.json: 37171b5a3ba60b427a8fd6cd612659794d9b06411e362bd6f998409e4168e843
        B/tables/TABLE-1-page-4-1/prompt.txt: fb65b63c72b21f69a38b5c87627c349ebf281ccaf82648ed127118bfb648a460
        B/tables/TABLE-1-page-4-1/meta.json: ef7487bcd1fca6f22b40fba84ac9b1d9162d01c1928188e17924406f16b60190
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
      pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
      source_review: _compare/relationships-2026-11-16/review-current/Pflugshaupt2009
      source_status_sha256: 54959a60b2f216ca7b9b4a9e2a66c2528a4cc443b1a20f4b58382e3e3515a932
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: Pure alexia vs hemianopic dyslexia
    outcome:
      text: Brain lesion location
    analysis_label: Lesion subtraction analysis
    relation: association
    evidence_ids:
    - P1-S1-C9
    - P6-S1-C14
    qualifier_ids:
    - P6-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
      source_review: _compare/relationships-2026-11-16/review-current/Pflugshaupt2009
      source_status_sha256: 54959a60b2f216ca7b9b4a9e2a66c2528a4cc443b1a20f4b58382e3e3515a932
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S4-C2
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C6
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C4
      - Result passage disposed without unit P6-S2-C4
      - 'window 11: invalid/duplicate disposition P7-S1-C1'
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C6
      - Unaccounted source passage P8-S1-C6
      - Unaccounted source passage P8-S1-C4
      - 'window 15: invalid/duplicate disposition P8-S1-C10'
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P9-S2-C6
      - Result passage disposed without unit P9-S2-C8
      - Accounting without a linked unit P9-S2-C9
      - Unaccounted source passage P9-S2-C9
      - Result passage disposed without unit P9-S3-C5
      - Result passage disposed without unit P10-S2-C3
      - Result passage disposed without unit P10-S2-C8
      - Result passage disposed without unit P10-S2-C12
      unattached_null_or_qualifier_ids:
      - P3-S4-C2
      - P5-S1-C4
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 181
      unselected_timing_passages:
      - P3-S3-C5
      - P3-S4-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C6
        - P3-S1-C7
        - P3-S1-C9
        - P3-S2-C10
        - P3-S3-C10
        - P3-S4-C4
        - P5-S1-C8
        - P5-S4-C1
        - P6-S1-C11
        - P6-S2-C4
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C11
        - P7-S2-C5
        - P8-S1-C4
        - P8-S1-C6
        - P9-S2-C3
        - P9-S3-C4
        - P10-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C6
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P3-S3-C5
        - P3-S3-C9
        - P3-S3-C10
        - P3-S4-C4
        - P5-S1-C2
        - P5-S4-C1
        - P9-S1-C8
        - P9-S3-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C9
        - P1-S2-C3
        - P2-S2-C8
        - P4-S2-C4
        - P5-S1-C10
        - P5-S1-C11
        - P5-S1-C12
        - P5-S2-C3
        - P5-S2-C4
        - P6-S2-C2
        - P6-S2-C8
        - P10-S1-C4
        - P10-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C8
        - P3-S1-C9
        - P3-S2-C4
        - P3-S2-C10
        - P3-S2-C11
        - P3-S3-C3
        - P4-S1-C2
        - P5-S1-C7
        - P5-S3-C12
        - P5-S3-C15
        - P7-S1-C6
        - P7-S1-C11
        - P8-S1-C4
        - P9-S2-C4
        - P9-S2-C7
        - P9-S3-C4
        - P9-S3-C8
        - P10-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C6
        - P2-S3-C5
        - P2-S3-C6
        - P3-S1-C2
        - P3-S1-C8
        - P3-S4-C2
        - P4-S1-C1
        - P5-S1-C8
        - P5-S4-C1
        - P7-S1-C7
        - P9-S2-C2
        - P9-S2-C11
        - P9-S3-C1
        - P9-S4-C2
        - P10-S3-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - analysis_restrictions
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P5-S4-C4
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S4
        - P4-S1
        - P4-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P10-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
      source_review: _compare/relationships-2026-11-16/review-current/Pflugshaupt2009
      source_status_sha256: 54959a60b2f216ca7b9b4a9e2a66c2528a4cc443b1a20f4b58382e3e3515a932
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Abstract summary of deficit-specific role of field defect.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Abstract summary of rightward saccades vs other visuo-motor impairments.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Abstract summary of lesion subtraction results.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Abstract summary of VWFA relation.
    - source_id: P3-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes matching of patient groups.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes word frequency control.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports reading accuracy.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes eye tracking accuracy.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes global comprehension check.
    - source_id: P5-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes word frequency control for WLE analysis.
    - source_id: P6-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Detailed results of lesion subtraction.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Links lesion areas to VWFA coordinate.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports VWFA coordinate damage in PA vs HD.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports global text comprehension.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports overall reading speed differences.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports paired reading speed comparisons.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares results to previous studies.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports overall differences in visuo-motor variables.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports null findings for regression/return sweep amplitudes.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports PA vs healthy visuo-motor deficits.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Reports HD vs healthy visuo-motor deficits.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Reports PA vs HD fixation-to-character ratio.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Reports PA vs HD fixation-to-character ratio.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Reports overall differences in WLE visuo-motor variables.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports PA vs HD/Healthy WLE visuo-motor deficits.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null difference between HD and healthy for WLE.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Reports quantitative contribution of field defect.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Reports correlation of rightward saccades with macular sparing.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Reports correlation of rightward saccades with macular sparing.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Reports specific correlation for PA rightward saccades.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Reports correlations for HD macular sparing.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes matching of patient groups.
    - source_id: P9-S2-C5
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of reading speed results.
    - source_id: P9-S2-C9
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 6
      reason: Restatement of visuo-motor and WLE results.
    - source_id: P9-S3-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of quantitative contribution estimates.
    - source_id: P9-S3-C7
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of rightward saccade contribution.
    - source_id: P9-S3-C8
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of macular sparing correlation.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Reports VWFA coordinate damage in PA vs HD.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses cut-off scores for differential diagnosis.
    - source_id: P10-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about eye movement analysis suitability.
    - source_id: P10-S2-C9
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Restatement of variables separating PA from HD.
    - source_id: P10-S2-C12
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Restatement of visuo-motor findings.
    - source_id: P10-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses methodological advantage of eye tracking.
    - source_id: P10-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Proposes diagnostic criteria based on results.
    unresolved_coverage:
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C3
    - P3-S4-C2
    - P5-S1-C4
    - P5-S1-C6
    - P5-S2-C6
    - P5-S3-C9
    - P5-S3-C14
    - P6-S2-C2
    - P6-S2-C4
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C8
    - P7-S1-C11
    - P7-S1-C12
    - P8-S1-C1
    - P8-S1-C4
    - P8-S1-C7
    - P8-S1-C10
    - P9-S1-C1
    - P9-S2-C2
    - P9-S2-C6
    - P9-S2-C8
    - P9-S2-C11
    - P9-S3-C6
    - P10-S2-C3
    - P10-S2-C8
    - P10-S2-C9
    - P10-S2-C12
    - P10-S3-C3
    - P10-S3-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P3-S1-C8
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C11
      - P3-S4-C5
      - P5-S1-C2
      - P9-S1-C8
      - P10-S3-C5
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S1-C9
      - P3-S2-C4
      - P3-S2-C10
      - P3-S2-C11
      limitations:
      - P9-S3-C2
      - P10-S1-C8
      personal_factors:
      - P3-S1-C2
      - P3-S1-C8
      tested_personal_effects:
      - P8-S1-C9
      - P9-S1-C2
      - P9-S1-C3
      - P9-S3-C8
      - P10-S3-C7
      adjustment_roles:
      - P5-S4-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: not_stated
    imaging_vs_outcome: not_stated
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C6
      - P3-S1-C7
      - P3-S1-C9
      - P3-S2-C10
      - P3-S3-C10
      - P3-S4-C4
      - P5-S1-C8
      - P5-S4-C1
      - P6-S1-C11
      - P6-S2-C4
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C11
      - P7-S2-C5
      - P8-S1-C4
      - P8-S1-C6
      - P9-S2-C3
      - P9-S3-C4
      - P10-S2-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C6
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S3-C5
      - P3-S3-C9
      - P3-S3-C10
      - P3-S4-C4
      - P5-S1-C2
      - P5-S4-C1
      - P9-S1-C8
      - P9-S3-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C9
      - P1-S2-C3
      - P2-S2-C8
      - P4-S2-C4
      - P5-S1-C10
      - P5-S1-C11
      - P5-S1-C12
      - P5-S2-C3
      - P5-S2-C4
      - P6-S2-C2
      - P6-S2-C8
      - P10-S1-C4
      - P10-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C8
      - P3-S1-C9
      - P3-S2-C4
      - P3-S2-C10
      - P3-S2-C11
      - P3-S3-C3
      - P4-S1-C2
      - P5-S1-C7
      - P5-S3-C12
      - P5-S3-C15
      - P7-S1-C6
      - P7-S1-C11
      - P8-S1-C4
      - P9-S2-C4
      - P9-S2-C7
      - P9-S3-C4
      - P9-S3-C8
      - P10-S2-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C6
      - P2-S3-C5
      - P2-S3-C6
      - P3-S1-C2
      - P3-S1-C8
      - P3-S4-C2
      - P4-S1-C1
      - P5-S1-C8
      - P5-S4-C1
      - P7-S1-C7
      - P9-S2-C2
      - P9-S2-C11
      - P9-S3-C1
      - P9-S4-C2
      - P10-S3-C5
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
      pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
      review_sha256: 3e26a548d6f52e1651cd7d9cc5666111b27be92ce1339006b9d60eaffd0e52ef
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
      - P1-S1-C9
      - P6-S1-C14
      source_result: Subtracting the lesions of hemianopic dyslexics from those found
        in pure alexics revealed the largest group differences in posterior parts
        of the left fusiform gyrus, occipito-temporal sulcus and inferior temporal
        gyrus. These regions included the coordinate assigned to the centre of the
        visual word form area in healthy adults.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a lesion subtraction analysis (P5-S1-C12)
            comparing pure alexia and hemianopic dyslexia groups, identifying specific
            anatomical regions with the highest frequency of damage in the pure alexia
            group (P1-S1-C9, P6-S1-C14). The proposed core correctly identifies this
            as the specific analysis.
          source_ids:
          - P1-S1-C9
          - P6-S1-C14
          - P5-S1-C12
        direction:
          answer: fits
          reason: The source states that the subtraction revealed differences in specific
            posterior left temporal/occipital regions (P1-S1-C9). The proposed core
            claims these regions were identified as having the largest group differences,
            which aligns with the detected association between pure alexia and damage
            in these areas.
          source_ids:
          - P1-S1-C9
          - P6-S1-C14
        construct:
          answer: fits
          reason: The exposure is the clinical diagnosis (Pure alexia vs hemianopic
            dyslexia), and the outcome is the brain lesion location. The method is
            correctly identified as a lesion subtraction/overlap analysis using template
            maps (CH2 template, P5-S1-C10). The patient measurement is template_lesion_overlap,
            as lesions were drawn onto a template and overlaid/subtracted, not patient-specific
            diffusion tractography.
          source_ids:
          - P5-S1-C10
          - P5-S1-C12
          - P1-S1-C9
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis contrasted
            pure alexia against hemianopic dyslexia to isolate the visual field defect
            contribution. This matches the study's design described in P3-S1-C7 and
            P6-S1-C14 context.
          source_ids:
          - P3-S1-C7
          - P6-S1-C14
        missing_material_caveat:
          answer: fits
          reason: The core captures the main finding. While small sample size is a
            limitation, it is noted in the proposed core's limitations field. No material
            caveat that changes the interpretation of the lesion location finding
            is omitted from the core claim itself.
          source_ids:
          - P9-S3-C2
          - P6-S1-C14
      optional_pending:
      - Specific coordinates of the VWFA center (x=-44, y=-58, z=-16) are mentioned
        in P5-S2-C3 but not transcribed into the core claim, which is acceptable for
        a qualitative draft.
      - Exact lesion volumes or voxel counts are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates of the VWFA center (x=-44, y=-58, z=-16) are mentioned
      in P5-S2-C3 but not transcribed into the core claim, which is acceptable for
      a qualitative draft.
    - Exact lesion volumes or voxel counts are not transcribed.
    normalizations:
    - field: sample.n
      original: 12
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.population
      original: Patients with either pure alexia (n=6) or hemianopic dyslexia (n=6),
        both groups showing similar right-sided visual field defects.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R001
      exposure:
        text: Pure alexia vs hemianopic dyslexia
      outcome:
        text: Brain lesion location
      analysis_label: Lesion subtraction analysis
      relation: association
      evidence_ids:
      - P1-S1-C9
      - P6-S1-C14
      qualifier_ids:
      - P6-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
        source_review: _compare/relationships-2026-11-16/review-current/Pflugshaupt2009
        source_status_sha256: 54959a60b2f216ca7b9b4a9e2a66c2528a4cc443b1a20f4b58382e3e3515a932
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 81f2468c74aef3e132086decb1935010d94bfe50345c7c7dde953f86fdd6d57e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5f158acfda10f5cc22e9b31564869b74efb5c586b231042ae54cf5260be26803
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C5
          page: 3
          text_layer_sha256: 5f158acfda10f5cc22e9b31564869b74efb5c586b231042ae54cf5260be26803
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'During the

          5 years needed to assemble appropriate participants for the present

          study, six patients with pure alexia were identiﬁed from the population

          of in-patients at our unit of cognitive and restorative neurology.'
        anchor_text: 'During the

          5 years needed to assemble appropriate participants for the present

          study, six patients with pure alexia were identiﬁed from the population

          of in-patients at our unit of cognitive and restorative neurology.'
        excluded_fragments: []
        image_sha256: dca5c8f5678d39b30bc941c0dbb30c4cf88fa70ea3c1d153cc2dc4ac3515b082
        transcription: '. During the

          5 years needed to assemble appropriate participants for the present

          study, six patients with pure alexia were identified from the population

          of in-patients at our unit of cognitive and restorative neurology'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'In addition, subtracting the lesions of the hemianopic dyslexics from those
    found in pure alexics revealed the largest group

    differences in posterior parts of the left fusiform gyrus, occipito-temporal sulcus
    and inferior temporal gyrus.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
