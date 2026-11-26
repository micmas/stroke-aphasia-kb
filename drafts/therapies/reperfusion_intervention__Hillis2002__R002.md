---
id: reperfusion_intervention
name: Reperfusion intervention
kind: therapy
findings:
- id: f1
  target: aphasia
  target_kind: impairment
  claim: Six selected patients with subcortical infarction and cortical hypoperfusion underwent interventions to restore perfusion and showed at least partial cortical reperfusion. Repeat testing at about 3 days after symptom onset showed substantial language improvement, with full recovery in most cases; one untreated comparison patient had persistent hypoperfusion and aphasia. This was not a randomized trial.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 6
    population: Six intervention recipients with subcortical infarction and cortical hypoperfusion; a seventh untreated patient is described separately as a comparison.
    phase: not_reported
    time_post_onset: Repeat MRI and cognitive testing at approximately 3 days after stroke symptom onset.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (n=6)
  evidence_quality: case-study
  strength: weak
  notes: 'Used the detailed Results description instead of the abstract’s blanket 100% immediate-resolution wording. Four patients received induced blood-pressure elevation, one endarterectomy and one a stent. Observational selected case series; intervention effectiveness cannot be isolated from this uncontrolled comparison. Source repair (unapproved): Used the detailed Results description instead of the abstract’s blanket 100% immediate-resolution wording. Four patients received induced blood-pressure elevation, one endarterectomy and one a stent. Observational selected case series; intervention effectiveness cannot be isolated from this uncontrolled comparison.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - proposed_concept:aphasia
    - agent_source_repair_pending_human_review
  therapy:
    id: reperfusion_intervention
    name: Reperfusion intervention
  citation: '@Hillis2002'
  source_passages:
  - section: Original source P1-S2-C3
    page: 1
    quote: 'Among

      the

      patients

      who

      received intervention that successfully restored cortical

      perfusion, 100% (six out of six) showed immediate reso-

      lution of aphasia.'
    supports: claim
  - section: Original source P4-S1-C10
    page: 4
    quote: 'Intervention

      A subset of six subjects with subcortical infarcts and cortical

      hypoperfusion

      had

      intervention

      to

      restore

      perfusion.'
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: 'Intervention consisted of induced blood pressure elevation

      with intravenous phenylephrine (n = 4) (for discussion of the

      rationale and evidence for this intervention, see Wise et al.,

      1972; Rordorf et al., 1997; Hillis et al., 2001a, b), urgent

      carotid endarterectomy (n = 1) or carotid stenting (n = 1).'
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: 'Repeat cognitive testing at 3 days after symptom

      onset showed substantial improvement of language, with full

      recovery in most cases, as shown in Fig. 4.'
    supports: claim
  design: case-series
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hillis2002
  proposal_id: R002
  approved: false
  original_core_review:
    paper: Hillis2002
    proposal_id: R002
    review_status_sha256: e6bc89384582914e9ac4cfb0e968aa4a7a9918500a383a181737c523ab05a033
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
      original_review_binding:
        version: relationship-review-v4
        input_hashes:
          pdf: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          A/passages.json: cd3b9f234822466e2f6dc1a645f6eb1bd335f9c00672a1c4b115c20ee055f298
          A/raw.json: 738a2c70e7e668706dbc82bc8df15eb90207c88f29443ef5b0f87f975abb245c
          A/source-units.json: d6fe443414d69dc74560d143eed61136b77b611836043ece20377a75d686e5d4
          A/full-source-units.json: d40f98b3125eb66aae3849da421ecb04c304aea797bfb2971f4ed110a40e08d8
          A/meta.json: cd8edada5d82edf4b3a1c36ce717b9fb16c0cbfdd73aeb9f264e8831bd36b434
          A/table-images/TABLE-3-page-9-1.png: 33f02b9c200dbc70966297afb67c3c292f0b75b926adc5567a0457599d2311d7
          A/table-images/TABLE-2-page-8-2.png: b6b815c98a659015b8e060e288b83debf9a32d2709106f0ac27c42f591ad41b9
          A/table-images/page-5.png: 0816abc7fe305e3a6123ad4371822e32e01b0224c1ee7eb180d6f20e4e624390
          A/table-images/TABLE-1-page-8-1.png: f3b9387d114fc48266f40648a9b2ba2640018a54d93566a55f1612b180a7a284
          A/table-images/page-9.png: 3853830cf59685eabf33de7bc54838963a78216b5bb8217f85c218e0e354cbc3
          A/table-images/page-8.png: bf1c51f2429e48d2f83b78c746d14ae5c40ed2ce04400db60351ea39a89ab8c3
          A/table-images/manifest.json: eb3458755799d4a57dccdfb0eb45f65fae8ca0c1b0224e294f42d54b7646507c
          A/table-images/TABLE-2-page-5-1.png: d53f590cbe24f40962c8174fdb632c06900c69b085c89ddfbb4aabb6f7db16ca
          A/clauses/window-03/raw.json: 2e316b85f18529061582fce4e49131dda9624f6cb4880f40593488b026e332b7
          A/clauses/window-03/prompt.txt: b66d184c64940cc00f52e48e29584a731bec3970b75126fd83d88dbb947b5c2e
          A/clauses/window-03/meta.json: 248d236c54655a02e1938ee9f464adb2993e8080e6c7e1127f83fe1ad1cd280d
          A/clauses/window-04/raw.json: e86b1cc3c642e2c1def99f2f33d0248fbd72b216d25b0468aa8a17fa1c983b5a
          A/clauses/window-04/prompt.txt: f8fef89739ea66bc14d358d2e6abffddba305df46cac1dc693149820bd5f6d5b
          A/clauses/window-04/meta.json: b6fd49d391c26e6fc817332decf72de38f09104d3f60aff36e40101e5000919b
          A/clauses/window-05/raw.json: 69f1644f504959198a4242d4696ea1bc02ce5b06425efa5fa81e6636fa15328d
          A/clauses/window-05/prompt.txt: 92ef2a71afd96b563ba69c7abb423e86704b5294261fdee8df23cc293beee342
          A/clauses/window-05/meta.json: 927b7a1b0b07e01094bc3190dd1f9f3874e16f262c7ee4002835d112ef6c2313
          A/clauses/window-02/raw.json: 426b107b647e6139c36d4333182063854e0c76bd5abc8f4bdbd16c8a6ea15330
          A/clauses/window-02/prompt.txt: 1cfca70437f1445f606f79450c093aa2a5619f33290bae58a16ba8445a3b6cb9
          A/clauses/window-02/meta.json: f95c3330be2094ceab8dd0c3899d63de52bbfb4be3f03a5b144c12b24d7f7cbc
          A/clauses/window-07/raw.json: efe119e64510a6b6c4d019072c19ecb18d4d9e62718e7192874736adac61d6bd
          A/clauses/window-07/prompt.txt: ee6a17f007db9a0b78d4fa670d50c68886b1a15fe47dc17582030bb91a52eefd
          A/clauses/window-07/meta.json: c00ea2b4fd65cfff7839b840e43cc684defcc38f890203201c6c3e02a15a3745
          A/clauses/window-01/raw.json: a7296fadf7fe0cb00602c2b17bdc50ea19d56fb21696bfb0192a3cd9e40e3f2b
          A/clauses/window-01/prompt.txt: cd12463ae8a9db1eeb381111d0c46aac3f2c0315a7061b75f56e4855bb7238b1
          A/clauses/window-01/meta.json: 4ee5e5638737e8be7f0bc1e2004785e335175f9be29e914196afa6706b1545ce
          A/clauses/window-06/raw.json: 753a76bc0a413509d1919dab0907dbd39a530d3ec473c8116e1c1db0d78c9cc2
          A/clauses/window-06/prompt.txt: bfe8f310eced23e5b6cea7b341aa9db0e879e19128730ed7c5738087a75b0482
          A/clauses/window-06/meta.json: e4d5fb85970539ae4c8039a417e4c5683c0060cfe8837c4350e3641ed8718ea5
          A/tables/TABLE-2-page-8-3/raw.json: 3fa34009f1b75c4c8c80a6090ebe21de1c19324deb6136b82b621a434f113ddf
          A/tables/TABLE-2-page-8-3/prompt.txt: 0af81b6bd2d6fdae3565f2f6d9200524f29a152a966311d6ff4af24f255571ad
          A/tables/TABLE-2-page-8-3/meta.json: dde0518d40a94d9d11d245f043ab9092cac3ec2f30a54d89348f94148cb1ae60
          A/tables/TABLE-3-page-9-4/raw.json: 794f6c9e18f36c96047d696e423f7a70a05e49557cb7ce945aff5b4fef3f486b
          A/tables/TABLE-3-page-9-4/prompt.txt: 781f9a6313f8842b13caff442d4d0fd9f682bddb733805e1eb480df91b38a030
          A/tables/TABLE-3-page-9-4/meta.json: 28965008586309dc5e7e8d533c99dba6e58ef9d1ce4302afb713e788eaa23ee3
          A/tables/TABLE-2-page-5-1/raw.json: 1c9b4cea569fe000a10b7435a52ffadc0349ef9b4f8fab95ed123f65b88c5a1f
          A/tables/TABLE-2-page-5-1/prompt.txt: cca19119f6c6f0c55e778843ef6e8822f2e99764bc07f0935bc31d615d4f5a60
          A/tables/TABLE-2-page-5-1/meta.json: 9621924977ae6f311448dfd2ca059d917c28b62563ad0171155ea5806b3fa9ca
          A/tables/TABLE-1-page-8-2/raw.json: 950dfa4808bbcf4132bb86c0be6dfb8ae4ad152eb6bc31679bca4b44ff997a33
          A/tables/TABLE-1-page-8-2/prompt.txt: 2396ded08ac6f9ab53878d7981bab940954febd92fc1e29a0692bfecb0db5d28
          A/tables/TABLE-1-page-8-2/meta.json: 8cd5611d0b5caef0d444804a183d105a5a08fd258528f0f7083a62da1a77e74a
          B/passages.json: cd3b9f234822466e2f6dc1a645f6eb1bd335f9c00672a1c4b115c20ee055f298
          B/raw.json: 8e762e58078ed434b9c9dea2e769a9bef4b2ebf0ea6c4cf28c833da74a2777a7
          B/source-units.json: d6fe443414d69dc74560d143eed61136b77b611836043ece20377a75d686e5d4
          B/full-source-units.json: d40f98b3125eb66aae3849da421ecb04c304aea797bfb2971f4ed110a40e08d8
          B/meta.json: dac7c9ffd652bfdeb486b1bd3c752736ce5fb30ad38c889cd462cde12f28ea29
          B/table-images/TABLE-3-page-9-1.png: 33f02b9c200dbc70966297afb67c3c292f0b75b926adc5567a0457599d2311d7
          B/table-images/TABLE-2-page-8-2.png: b6b815c98a659015b8e060e288b83debf9a32d2709106f0ac27c42f591ad41b9
          B/table-images/page-5.png: 0816abc7fe305e3a6123ad4371822e32e01b0224c1ee7eb180d6f20e4e624390
          B/table-images/TABLE-1-page-8-1.png: f3b9387d114fc48266f40648a9b2ba2640018a54d93566a55f1612b180a7a284
          B/table-images/page-9.png: 3853830cf59685eabf33de7bc54838963a78216b5bb8217f85c218e0e354cbc3
          B/table-images/page-8.png: bf1c51f2429e48d2f83b78c746d14ae5c40ed2ce04400db60351ea39a89ab8c3
          B/table-images/manifest.json: 0292b9d00cb92070e9bc61c1dd51ae3c323eb2b3ab2c23a950b8c1de0bca271d
          B/table-images/TABLE-2-page-5-1.png: d53f590cbe24f40962c8174fdb632c06900c69b085c89ddfbb4aabb6f7db16ca
          B/clauses/window-03/raw.json: 198b2b6a517f80757dfad9c5beb40422b686631498480fbedd969a15ed568476
          B/clauses/window-03/prompt.txt: b66d184c64940cc00f52e48e29584a731bec3970b75126fd83d88dbb947b5c2e
          B/clauses/window-03/meta.json: c1fdb90a77713707ba599dd72f7f457989d1453bc4774da6b984289c2e27618b
          B/clauses/window-04/raw.json: ff7510fca44d4e54a1608fb1f9aaa30214765c4687bbf2ea0a48937bc63713e4
          B/clauses/window-04/prompt.txt: f8fef89739ea66bc14d358d2e6abffddba305df46cac1dc693149820bd5f6d5b
          B/clauses/window-04/meta.json: aae6448a541ee008b9a616009f4635238c8fab1123d1498d920bd75d702960f9
          B/clauses/window-05/raw.json: b47af121c4fa9c8a28aeb82a84cd31d0ef40fe7a92510d5077cae9030b73fb4c
          B/clauses/window-05/prompt.txt: 92ef2a71afd96b563ba69c7abb423e86704b5294261fdee8df23cc293beee342
          B/clauses/window-05/meta.json: e928aa13affc72f3bb6c6b46c2a865b2cc68c1c77a8fde8686134ab315532ab3
          B/clauses/window-02/raw.json: bbc77f9eddd342e83b2c03f097252fa178c2157c63215b54d5fec99d6c5ee0a6
          B/clauses/window-02/prompt.txt: 1cfca70437f1445f606f79450c093aa2a5619f33290bae58a16ba8445a3b6cb9
          B/clauses/window-02/meta.json: ddedbd54b9110aa1ae13ff6d7db5668021e0717798074fda82f28da21d9a8904
          B/clauses/window-07/raw.json: 4575df16afa65fd7c2218d31fff0e3feccac6a41059f3c25d54b3f1c209170b3
          B/clauses/window-07/prompt.txt: ee6a17f007db9a0b78d4fa670d50c68886b1a15fe47dc17582030bb91a52eefd
          B/clauses/window-07/meta.json: 00c00b2b3ed9c972ff0b7a4df1539cefa0fa751e60674986618083a5e05a69ca
          B/clauses/window-01/raw.json: 6e5c38eeeda845a20a4ea1e56303de46c295855a97464056f96f7f32bef11022
          B/clauses/window-01/prompt.txt: cd12463ae8a9db1eeb381111d0c46aac3f2c0315a7061b75f56e4855bb7238b1
          B/clauses/window-01/meta.json: fec96604d5c186ea570a8ffa1be8c933756eb2095cfa7880c1861cb058a33df7
          B/clauses/window-06/raw.json: c6879ead9247b1455ed185ff68840615dfde598c8faa3cac4290c9e7e2192cac
          B/clauses/window-06/prompt.txt: bfe8f310eced23e5b6cea7b341aa9db0e879e19128730ed7c5738087a75b0482
          B/clauses/window-06/meta.json: e8187e4bf4aa2eecbbeb3cae2c70234f7c80aee0c8df23f080a312b76adc59c7
          B/tables/TABLE-2-page-8-3/raw.json: fcfdbe9b83034599687c2e3e7685f28538ab323c1ab4c855525366fdc0061a36
          B/tables/TABLE-2-page-8-3/prompt.txt: 0af81b6bd2d6fdae3565f2f6d9200524f29a152a966311d6ff4af24f255571ad
          B/tables/TABLE-2-page-8-3/meta.json: 86503444cfca0020dcee15278bea6f8f5fe1f3417c167d9d7366545acd74acfd
          B/tables/TABLE-3-page-9-4/raw.json: a45df8f0ef0ced3cc1a0004e569dc67f8ad4ad9e6ce006ce42f81f54383174ae
          B/tables/TABLE-3-page-9-4/prompt.txt: 781f9a6313f8842b13caff442d4d0fd9f682bddb733805e1eb480df91b38a030
          B/tables/TABLE-3-page-9-4/meta.json: 7ffbb02fd82d97293765b11fef5e3a587ad1a23872232f3a85c318c9c2fe8fa8
          B/tables/TABLE-2-page-5-1/raw.json: 9392d8c31787e49792926d91d55a78146e2c835d30b21f088bf84e900ac8a2e0
          B/tables/TABLE-2-page-5-1/prompt.txt: cca19119f6c6f0c55e778843ef6e8822f2e99764bc07f0935bc31d615d4f5a60
          B/tables/TABLE-2-page-5-1/meta.json: de55b5d3b89faffe71ce54fc39bf3e51fbc3f40e32524a08989817a597f3c4b2
          B/tables/TABLE-1-page-8-2/raw.json: de26fbdefbbd0afa091fd6734cba9025bd558e63cec33e310d99855118fc12cb
          B/tables/TABLE-1-page-8-2/prompt.txt: 2396ded08ac6f9ab53878d7981bab940954febd92fc1e29a0692bfecb0db5d28
          B/tables/TABLE-1-page-8-2/meta.json: 9c2658e30fff9b40dcc5154e15b5a9054e89c345f1982df8d348fa0aea78068f
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
        pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
        source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R002
      exposure:
        text: intervention to restore cortical perfusion
      outcome:
        text: aphasia
      analysis_label: Reperfusion intervention
      relation: treatment_effect
      evidence_ids:
      - P1-S2-C3
      - P5-S1-C5
      qualifier_ids:
      - P4-S1-C10
      - P4-S1-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
        source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Accounting without a linked unit P1-S2-C2
        - Accounting without a linked unit P1-S2-C3
        - Accounting without a linked unit P1-S2-C4
        - Accounting without a linked unit P1-S2-C5
        - Accounting without a linked unit P2-S1-C1
        - Unaccounted source passage P1-S2-C5
        - Unaccounted source passage P1-S2-C2
        - Unaccounted source passage P2-S1-C1
        - Unaccounted source passage P1-S2-C4
        - Unaccounted source passage P1-S2-C3
        - Result passage disposed without unit P3-S1-C9
        - Result passage disposed without unit P3-S3-C2
        - Result passage disposed without unit P3-S3-C5
        - Result passage disposed without unit P3-S3-C8
        - Result passage disposed without unit P4-S1-C4
        - 'window 3: invalid/duplicate disposition P4-S2-C4'
        - Result passage disposed without unit P4-S2-C10
        - Result passage disposed without unit P4-S2-C7
        - Result passage disposed without unit P4-S3-C3
        - Result passage disposed without unit P5-S1-C11
        - Result passage disposed without unit P5-S1-C12
        - Result passage disposed without unit P5-S1-C13
        - Result passage disposed without unit P5-S1-C5
        - Result passage disposed without unit P5-S1-C8
        - Result passage disposed without unit P6-S1-C1
        - Result passage disposed without unit P6-S1-C2
        - Result passage disposed without unit P6-S1-C3
        - Accounting without a linked unit P6-S1-C4
        - Accounting without a linked unit P6-S1-C5
        - Accounting without a linked unit P6-S1-C6
        - Accounting without a linked unit P7-S1-C1
        - Accounting without a linked unit P7-S1-C2
        - Unaccounted source passage P7-S1-C2
        - Unaccounted source passage P6-S1-C4
        - Unaccounted source passage P7-S1-C1
        - Unaccounted source passage P6-S1-C5
        - Unaccounted source passage P6-S1-C6
        - Accounting without a linked unit P7-S1-C12
        - Result passage disposed without unit P7-S1-C4
        - Result passage disposed without unit P7-S1-C5
        - Accounting without a linked unit P7-S2-C2
        - Unaccounted source passage P7-S1-C12
        - Unaccounted source passage P7-S2-C2
        - Result passage disposed without unit P10-S1-C5
        unattached_null_or_qualifier_ids:
        - P1-S2-C2
        - P5-S1-C12
        - P5-S1-C14
        - P7-S1-C4
        suppressed_nonrepresented_units: 13
        default_disposition_count_requires_completeness_check: 148
        unselected_timing_passages:
        - P2-S2-C9
        - P2-S3-C6
        - P3-S2-C9
        - P4-S2-C3
        - P5-S1-C7
        - P9-S1-C6
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P1-S2-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P1-S2-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S1-C8
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S1-C9
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P5-S1-C13
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S1-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S1-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P3-S3-C2
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: analysed_sample
          source_ids:
          - P1-S1-C18
          - P1-S1-C21
          - P1-S2-C2
          - P1-S2-C4
          - P1-S2-C5
          - P2-S2-C6
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P4-S2-C14
          - P4-S3-C7
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C11
          - P5-S1-C9
          - P5-S1-C11
          - P5-S1-C12
          - P5-S1-C13
          - P5-S1-C14
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P7-S1-C12
          - P8-S1-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P1-S1-C19
          - P1-S2-C4
          - P1-S2-C5
          - P2-S2-C8
          - P4-S1-C6
          - P4-S1-C7
          - P4-S1-C8
          - P4-S1-C9
          - P5-S1-C13
          - P6-S1-C5
          - P6-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: analysis_restrictions
          source_ids:
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P4-S2-C14
          - P4-S3-C7
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C11
          - P5-S1-C11
          - P5-S1-C12
          - P5-S1-C13
          - P5-S1-C14
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P7-S1-C12
          - P8-S1-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - analysed_sample
        - outcome_definition
        - validation
        - analysis_restrictions
        - personal_factors
        - tested_personal_effects
        - adjustment_roles
        - explicitly_not_adjusted
        unclassified_extraction_ids: []
        table_review_required:
        - TABLE-1-page-8-2
        - TABLE-2-page-5-1
        - TABLE-2-page-8-3
        - TABLE-3-page-9-4
        unlinked_tables:
        - TABLE-1-page-8-2
        - TABLE-2-page-5-1
        - TABLE-2-page-8-3
        - TABLE-3-page-9-4
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P4-S2
          - P4-S3
          - P5-S1
          - P6-S1
          - P7-S2
          - P8-S1
          - P9-S2
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
        source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P1-S2-C2
        disposition: represented
        result_indexes:
        - 0
        reason: States all subjects with only subcortical lesions who had aphasia or neglect showed cortical hypoperfusion.
      - source_id: P1-S2-C3
        disposition: represented
        result_indexes:
        - 1
        reason: Reports 100% resolution of aphasia after successful restoration of cortical perfusion.
      - source_id: P1-S2-C4
        disposition: represented
        result_indexes:
        - 2
        reason: Compares association strength of aphasia/neglect with PWI vs DWI.
      - source_id: P1-S2-C5
        disposition: represented
        result_indexes:
        - 3
        reason: Provides PPV percentages for PWI vs DWI.
      - source_id: P3-S1-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: States no patients met a specific description for spontaneous speech aphasia.
      - source_id: P3-S3-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports mean scores for subtests.
      - source_id: P3-S3-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports control subject performance.
      - source_id: P3-S3-C8
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports inter-rater reliability.
      - source_id: P4-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports agreement between neuroradiologist and technician.
      - source_id: P4-S2-C6
        disposition: represented
        result_indexes:
        - 4
        reason: Reports 25/37 left subcortical lesion patients had aphasia and all had cortical hypoperfusion.
      - source_id: P4-S2-C7
        disposition: represented
        result_indexes:
        - 4
        reason: Specifies hypoperfusion was in the left MCA territory.
      - source_id: P4-S2-C8
        disposition: represented
        result_indexes:
        - 4
        reason: Concludes 100% of language deficits with isolated subcortical lesions were accounted for by hypoperfusion.
      - source_id: P4-S2-C9
        disposition: represented
        result_indexes:
        - 4
        reason: Reports only one non-aphasic subject with left subcortical lesions had hypoperfusion (occipital).
      - source_id: P4-S2-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Lists common sites of subcortical infarct.
      - source_id: P4-S2-C12
        disposition: represented
        result_indexes:
        - 5
        reason: Reports association between left corona radiata lesions, aphasia, and hypoperfusion.
      - source_id: P4-S2-C14
        disposition: represented
        result_indexes:
        - 6
        reason: Reports association between left caudate infarcts, language deficits, and hypoperfusion.
      - source_id: P4-S3-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Illustrative case description of Fig 1.
      - source_id: P4-S3-C4
        disposition: represented
        result_indexes:
        - 7
        reason: Reports no language impairments in five subjects with isolated left thalamic infarcts.
      - source_id: P4-S3-C6
        disposition: represented
        result_indexes:
        - 7
        reason: Reports one thalamic lesion subject had occipital hypoperfusion and visual deficits.
      - source_id: P4-S3-C8
        disposition: represented
        result_indexes:
        - 8
        reason: Reports 7/14 right subcortical lesion patients had neglect.
      - source_id: P4-S3-C9
        disposition: represented
        result_indexes:
        - 8
        reason: Reports all 7 neglect patients had hypoperfusion and 7 without neglect had none.
      - source_id: P4-S3-C11
        disposition: represented
        result_indexes:
        - 9
        reason: Reports neglect associated with right caudate/capsular and corona radiata sites.
      - source_id: P5-S1-C1
        disposition: represented
        result_indexes:
        - 9
        reason: Provides p-value for right subcortical site associations.
      - source_id: P5-S1-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Illustrative case description of Fig 2.
      - source_id: P5-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports partial reperfusion of cortex in treated subjects.
      - source_id: P5-S1-C5
        disposition: represented
        result_indexes:
        - 1
        reason: Reports substantial improvement/full recovery of language after intervention.
      - source_id: P5-S1-C8
        disposition: represented
        result_indexes:
        - 1
        reason: Reports persistent aphasia in non-intervention control.
      - source_id: P5-S1-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports prevalence of language deficits in left hemisphere stroke.
      - source_id: P5-S1-C12
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports DWI findings in aphasic subjects.
      - source_id: P5-S1-C13
        disposition: represented
        result_indexes:
        - 10
        reason: Reports 95% of subjects with lexical deficits had cortical hypoperfusion on PWI.
      - source_id: P6-S1-C4
        disposition: represented
        result_indexes:
        - 11
        reason: Reports all 27 right hemisphere stroke patients with neglect had cortical hypoperfusion.
      - source_id: P6-S1-C5
        disposition: represented
        result_indexes:
        - 2
        reason: Reports aphasia association with infarct (DWI) vs hypoperfusion (PWI).
      - source_id: P6-S1-C6
        disposition: represented
        result_indexes:
        - 2
        reason: Reports neglect association with infarct (DWI) vs hypoperfusion (PWI).
      - source_id: P7-S1-C1
        disposition: repeated
        result_indexes:
        - 0
        - 4
        - 8
        reason: Restatement of findings regarding subcortical infarctions and hypoperfusion.
      - source_id: P7-S1-C2
        disposition: repeated
        result_indexes:
        - 1
        reason: Restatement of resolution of aphasia after reversal of hypoperfusion.
      - source_id: P7-S2-C2
        disposition: repeated
        result_indexes:
        - 0
        - 4
        - 8
        reason: Restatement that 100% of subjects with aphasia/neglect showed hypoperfusion.
      - source_id: P8-S1-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports CT findings of chronic aphasic subjects.
      - source_id: P9-S1-C8
        disposition: repeated
        result_indexes:
        - 1
        reason: Restatement that reperfusion led to improvement of language function.
      - source_id: P9-S2-C2
        disposition: repeated
        result_indexes:
        - 0
        - 4
        - 8
        reason: Restatement that hypoperfusion could account for all cases.
      - source_id: P9-S2-C3
        disposition: represented
        result_indexes:
        - 0
        reason: States no support was found for the hypothesis that subcortical lesions directly cause deficits.
      - source_id: P9-S2-C7
        disposition: represented
        result_indexes:
        - 2
        - 10
        - 11
        reason: Table 3 provides the raw counts and chi-squared values for the associations.
      - source_id: P10-S1-C5
        disposition: repeated
        result_indexes:
        - 0
        - 4
        - 8
        reason: Concluding statement that hypoperfusion is an important contributor.
      unresolved_coverage:
      - source_id: P9-S2-C7
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P5-S1-C14
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P6-S1-C1
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P6-S1-C2
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P6-S1-C3
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P6-S1-C8
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P7-S1-C3
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P7-S1-C4
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P7-S1-C5
        disposition: unresolved
        reason: Discovery omitted this passage
      - source_id: P7-S1-C12
        disposition: unresolved
        reason: Discovery omitted this passage
      pending_source_ids:
      - P3-S1-C9
      - P3-S3-C2
      - P3-S3-C5
      - P3-S3-C8
      - P4-S1-C4
      - P4-S2-C7
      - P4-S2-C9
      - P4-S2-C10
      - P4-S3-C3
      - P4-S3-C6
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C8
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C14
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C3
      - P6-S1-C8
      - P7-S1-C1
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C12
      - P7-S2-C2
      - P8-S1-C2
      - P9-S1-C8
      - P9-S2-C2
      - P9-S2-C3
      - P10-S1-C5
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review:
      - TABLE-1-page-8-2
      - TABLE-2-page-5-1
      - TABLE-2-page-8-3
      - TABLE-3-page-9-4
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample: []
        recruited_sample:
        - P1-S1-C18
        eligibility:
        - P2-S2-C10
        - P2-S3-C2
        - P2-S3-C5
        - P2-S3-C6
        - P2-S3-C7
        - P2-S3-C8
        imaging_provenance:
        - P3-S3-C9
        - P3-S3-C10
        - P3-S3-C11
        - P3-S3-C12
        - P3-S3-C14
        - P3-S3-C15
        - P4-S1-C5
        imaging_timing:
        - P1-S1-C18
        - P2-S2-C6
        - P2-S3-C7
        - P4-S2-C2
        - P5-S1-C5
        outcome_timing:
        - P1-S1-C18
        - P1-S1-C22
        - P2-S2-C7
        - P3-S1-C12
        - P4-S2-C2
        - P5-S1-C4
        - P5-S1-C5
        outcome_definition: []
        validation: []
        analysis_restrictions: []
        dependent_variable_statement:
        - P1-S1-C19
        - P2-S2-C8
        - P4-S1-C6
        - P4-S1-C7
        limitations:
        - P9-S2-C2
        - P9-S2-C3
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles: []
        explicitly_not_adjusted: []
        descriptive_personal_factors:
        - P2-S3-C6
        - P2-S3-C7
        - P2-S3-C8
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: none_described
      held_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P3-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C18
        - P1-S1-C21
        - P1-S2-C2
        - P1-S2-C4
        - P1-S2-C5
        - P2-S2-C6
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C12
        - P4-S2-C14
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P4-S3-C11
        - P5-S1-C9
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P7-S1-C12
        - P8-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C19
        - P1-S2-C4
        - P1-S2-C5
        - P2-S2-C8
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P5-S1-C13
        - P6-S1-C5
        - P6-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C12
        - P4-S2-C14
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P4-S3-C11
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P7-S1-C12
        - P8-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
        review_sha256: e6bc89384582914e9ac4cfb0e968aa4a7a9918500a383a181737c523ab05a033
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
        - P1-S2-C3
        - P5-S1-C5
        source_result: In a subset of six patients with subcortical infarcts and cortical hypoperfusion who received intervention to restore perfusion (phenylephrine, endarterectomy, or stenting), 100% showed immediate resolution of aphasia. Repeat cognitive testing at 3 days showed substantial improvement with full recovery in most cases. This finding is based on a very small sample (n=6) and the authors note that they cannot rule out that cortical reperfusion sometimes occurs without resolution of aphasia in other cases.
        result_status: detected
        patient_measurement: non_imaging
        checks:
          analysis_identity:
            answer: fits
            reason: The selected analysis correctly identifies the specific subset of 6 patients who received reperfusion intervention and the outcome of aphasia resolution. The source (P1-S2-C3, P5-S1-C5) confirms this specific analysis distinct from the broader association studies.
            source_ids:
            - P1-S2-C3
            - P5-S1-C5
            - P4-S1-C10
          direction:
            answer: fits
            reason: The claim that intervention was associated with resolution of aphasia preserves the detected positive association (improvement/resolution) reported in the source. The direction 'likely' is appropriate given the observational nature and small sample size, avoiding causal overstatement while reflecting the observed outcome.
            source_ids:
            - P1-S2-C3
            - P5-S1-C5
          construct:
            answer: fits
            reason: The exposure (reperfusion intervention) and outcome (aphasia) are correctly identified. The patient measurement is non-imaging (cognitive testing battery), which is the actual measure of the outcome. The source confirms that cognitive testing was used to assess aphasia resolution, not imaging alone.
            source_ids:
            - P1-S2-C3
            - P5-S1-C5
            - P3-S1-C12
          qualifications:
            answer: fits
            reason: The draft includes the qualification that the finding is based on a small subset (n=6). This is a material caveat present in the source (P9-S1-C9) regarding the generalizability of the reperfusion finding.
            source_ids:
            - P4-S1-C10
            - P9-S1-C9
          missing_material_caveat:
            answer: fits
            reason: The draft captures the small sample size limitation. While the source notes that reperfusion might not always resolve aphasia (P9-S1-C9), the draft's qualification regarding the small subset implicitly covers the limited evidence base. No other material caveats that change the interpretation of this specific n=6 result are omitted.
            source_ids:
            - P9-S1-C9
        optional_pending: []
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      normalizations: []
      analysis_identity:
        id: R002
        exposure:
          text: intervention to restore cortical perfusion
        outcome:
          text: aphasia
        analysis_label: Reperfusion intervention
        relation: treatment_effect
        evidence_ids:
        - P1-S2-C3
        - P5-S1-C5
        qualifier_ids:
        - P4-S1-C10
        - P4-S1-C11
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
          source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: reperfusion_intervention
    name: Reperfusion intervention
    kind: therapy
    findings:
    - id: f1
      target: aphasia
      target_kind: impairment
      claim: Among patients who received intervention that successfully restored cortical perfusion, 100% (six out of six) showed immediate resolution of aphasia.
      direction: likely
      relationship: treatment_response
      method: clinical_RCT
      sample:
        n: 6
        population: Patients with subcortical infarcts and cortical hypoperfusion
        phase: not_reported
        time_post_onset: Repeat cognitive testing and imaging performed the morning after intervention, which was 3 days after initial assessment (initial assessment within 24h of onset)
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - Small sample size (n=6)
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: Intervention to restore cortical perfusion, consisting of induced blood pressure elevation with intravenous phenylephrine, urgent carotid endarterectomy, or carotid stenting. Finding is based on a small subset of the total study population. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - proposed_concept:aphasia
      therapy:
        id: reperfusion_intervention
        name: Reperfusion intervention
      citation: '@Hillis2002'
      source_passages:
      - section: Original source P1-S2-C3
        page: 1
        quote: 'Among

          the

          patients

          who

          received intervention that successfully restored cortical

          perfusion, 100% (six out of six) showed immediate reso-

          lution of aphasia.'
        supports: claim
      - section: Original source P4-S1-C10
        page: 4
        quote: 'Intervention

          A subset of six subjects with subcortical infarcts and cortical

          hypoperfusion

          had

          intervention

          to

          restore

          perfusion.'
        supports: sample
      - section: Original source P4-S1-C11
        page: 4
        quote: 'Intervention consisted of induced blood pressure elevation

          with intravenous phenylephrine (n = 4) (for discussion of the

          rationale and evidence for this intervention, see Wise et al.,

          1972; Rordorf et al., 1997; Hillis et al., 2001a, b), urgent

          carotid endarterectomy (n = 1) or carotid stenting (n = 1).'
        supports: method
      - section: Original source P5-S1-C5
        page: 5
        quote: 'Repeat cognitive testing at 3 days after symptom

          onset showed substantial improvement of language, with full

          recovery in most cases, as shown in Fig. 4.'
        supports: claim
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-24'
    relationship_review:
      paper: Hillis2002
      proposal_id: R002
      review_status_sha256: e6bc89384582914e9ac4cfb0e968aa4a7a9918500a383a181737c523ab05a033
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
        original_review_binding:
          version: relationship-review-v4
          input_hashes:
            pdf: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
            A/passages.json: cd3b9f234822466e2f6dc1a645f6eb1bd335f9c00672a1c4b115c20ee055f298
            A/raw.json: 738a2c70e7e668706dbc82bc8df15eb90207c88f29443ef5b0f87f975abb245c
            A/source-units.json: d6fe443414d69dc74560d143eed61136b77b611836043ece20377a75d686e5d4
            A/full-source-units.json: d40f98b3125eb66aae3849da421ecb04c304aea797bfb2971f4ed110a40e08d8
            A/meta.json: cd8edada5d82edf4b3a1c36ce717b9fb16c0cbfdd73aeb9f264e8831bd36b434
            A/table-images/TABLE-3-page-9-1.png: 33f02b9c200dbc70966297afb67c3c292f0b75b926adc5567a0457599d2311d7
            A/table-images/TABLE-2-page-8-2.png: b6b815c98a659015b8e060e288b83debf9a32d2709106f0ac27c42f591ad41b9
            A/table-images/page-5.png: 0816abc7fe305e3a6123ad4371822e32e01b0224c1ee7eb180d6f20e4e624390
            A/table-images/TABLE-1-page-8-1.png: f3b9387d114fc48266f40648a9b2ba2640018a54d93566a55f1612b180a7a284
            A/table-images/page-9.png: 3853830cf59685eabf33de7bc54838963a78216b5bb8217f85c218e0e354cbc3
            A/table-images/page-8.png: bf1c51f2429e48d2f83b78c746d14ae5c40ed2ce04400db60351ea39a89ab8c3
            A/table-images/manifest.json: eb3458755799d4a57dccdfb0eb45f65fae8ca0c1b0224e294f42d54b7646507c
            A/table-images/TABLE-2-page-5-1.png: d53f590cbe24f40962c8174fdb632c06900c69b085c89ddfbb4aabb6f7db16ca
            A/clauses/window-03/raw.json: 2e316b85f18529061582fce4e49131dda9624f6cb4880f40593488b026e332b7
            A/clauses/window-03/prompt.txt: b66d184c64940cc00f52e48e29584a731bec3970b75126fd83d88dbb947b5c2e
            A/clauses/window-03/meta.json: 248d236c54655a02e1938ee9f464adb2993e8080e6c7e1127f83fe1ad1cd280d
            A/clauses/window-04/raw.json: e86b1cc3c642e2c1def99f2f33d0248fbd72b216d25b0468aa8a17fa1c983b5a
            A/clauses/window-04/prompt.txt: f8fef89739ea66bc14d358d2e6abffddba305df46cac1dc693149820bd5f6d5b
            A/clauses/window-04/meta.json: b6fd49d391c26e6fc817332decf72de38f09104d3f60aff36e40101e5000919b
            A/clauses/window-05/raw.json: 69f1644f504959198a4242d4696ea1bc02ce5b06425efa5fa81e6636fa15328d
            A/clauses/window-05/prompt.txt: 92ef2a71afd96b563ba69c7abb423e86704b5294261fdee8df23cc293beee342
            A/clauses/window-05/meta.json: 927b7a1b0b07e01094bc3190dd1f9f3874e16f262c7ee4002835d112ef6c2313
            A/clauses/window-02/raw.json: 426b107b647e6139c36d4333182063854e0c76bd5abc8f4bdbd16c8a6ea15330
            A/clauses/window-02/prompt.txt: 1cfca70437f1445f606f79450c093aa2a5619f33290bae58a16ba8445a3b6cb9
            A/clauses/window-02/meta.json: f95c3330be2094ceab8dd0c3899d63de52bbfb4be3f03a5b144c12b24d7f7cbc
            A/clauses/window-07/raw.json: efe119e64510a6b6c4d019072c19ecb18d4d9e62718e7192874736adac61d6bd
            A/clauses/window-07/prompt.txt: ee6a17f007db9a0b78d4fa670d50c68886b1a15fe47dc17582030bb91a52eefd
            A/clauses/window-07/meta.json: c00ea2b4fd65cfff7839b840e43cc684defcc38f890203201c6c3e02a15a3745
            A/clauses/window-01/raw.json: a7296fadf7fe0cb00602c2b17bdc50ea19d56fb21696bfb0192a3cd9e40e3f2b
            A/clauses/window-01/prompt.txt: cd12463ae8a9db1eeb381111d0c46aac3f2c0315a7061b75f56e4855bb7238b1
            A/clauses/window-01/meta.json: 4ee5e5638737e8be7f0bc1e2004785e335175f9be29e914196afa6706b1545ce
            A/clauses/window-06/raw.json: 753a76bc0a413509d1919dab0907dbd39a530d3ec473c8116e1c1db0d78c9cc2
            A/clauses/window-06/prompt.txt: bfe8f310eced23e5b6cea7b341aa9db0e879e19128730ed7c5738087a75b0482
            A/clauses/window-06/meta.json: e4d5fb85970539ae4c8039a417e4c5683c0060cfe8837c4350e3641ed8718ea5
            A/tables/TABLE-2-page-8-3/raw.json: 3fa34009f1b75c4c8c80a6090ebe21de1c19324deb6136b82b621a434f113ddf
            A/tables/TABLE-2-page-8-3/prompt.txt: 0af81b6bd2d6fdae3565f2f6d9200524f29a152a966311d6ff4af24f255571ad
            A/tables/TABLE-2-page-8-3/meta.json: dde0518d40a94d9d11d245f043ab9092cac3ec2f30a54d89348f94148cb1ae60
            A/tables/TABLE-3-page-9-4/raw.json: 794f6c9e18f36c96047d696e423f7a70a05e49557cb7ce945aff5b4fef3f486b
            A/tables/TABLE-3-page-9-4/prompt.txt: 781f9a6313f8842b13caff442d4d0fd9f682bddb733805e1eb480df91b38a030
            A/tables/TABLE-3-page-9-4/meta.json: 28965008586309dc5e7e8d533c99dba6e58ef9d1ce4302afb713e788eaa23ee3
            A/tables/TABLE-2-page-5-1/raw.json: 1c9b4cea569fe000a10b7435a52ffadc0349ef9b4f8fab95ed123f65b88c5a1f
            A/tables/TABLE-2-page-5-1/prompt.txt: cca19119f6c6f0c55e778843ef6e8822f2e99764bc07f0935bc31d615d4f5a60
            A/tables/TABLE-2-page-5-1/meta.json: 9621924977ae6f311448dfd2ca059d917c28b62563ad0171155ea5806b3fa9ca
            A/tables/TABLE-1-page-8-2/raw.json: 950dfa4808bbcf4132bb86c0be6dfb8ae4ad152eb6bc31679bca4b44ff997a33
            A/tables/TABLE-1-page-8-2/prompt.txt: 2396ded08ac6f9ab53878d7981bab940954febd92fc1e29a0692bfecb0db5d28
            A/tables/TABLE-1-page-8-2/meta.json: 8cd5611d0b5caef0d444804a183d105a5a08fd258528f0f7083a62da1a77e74a
            B/passages.json: cd3b9f234822466e2f6dc1a645f6eb1bd335f9c00672a1c4b115c20ee055f298
            B/raw.json: 8e762e58078ed434b9c9dea2e769a9bef4b2ebf0ea6c4cf28c833da74a2777a7
            B/source-units.json: d6fe443414d69dc74560d143eed61136b77b611836043ece20377a75d686e5d4
            B/full-source-units.json: d40f98b3125eb66aae3849da421ecb04c304aea797bfb2971f4ed110a40e08d8
            B/meta.json: dac7c9ffd652bfdeb486b1bd3c752736ce5fb30ad38c889cd462cde12f28ea29
            B/table-images/TABLE-3-page-9-1.png: 33f02b9c200dbc70966297afb67c3c292f0b75b926adc5567a0457599d2311d7
            B/table-images/TABLE-2-page-8-2.png: b6b815c98a659015b8e060e288b83debf9a32d2709106f0ac27c42f591ad41b9
            B/table-images/page-5.png: 0816abc7fe305e3a6123ad4371822e32e01b0224c1ee7eb180d6f20e4e624390
            B/table-images/TABLE-1-page-8-1.png: f3b9387d114fc48266f40648a9b2ba2640018a54d93566a55f1612b180a7a284
            B/table-images/page-9.png: 3853830cf59685eabf33de7bc54838963a78216b5bb8217f85c218e0e354cbc3
            B/table-images/page-8.png: bf1c51f2429e48d2f83b78c746d14ae5c40ed2ce04400db60351ea39a89ab8c3
            B/table-images/manifest.json: 0292b9d00cb92070e9bc61c1dd51ae3c323eb2b3ab2c23a950b8c1de0bca271d
            B/table-images/TABLE-2-page-5-1.png: d53f590cbe24f40962c8174fdb632c06900c69b085c89ddfbb4aabb6f7db16ca
            B/clauses/window-03/raw.json: 198b2b6a517f80757dfad9c5beb40422b686631498480fbedd969a15ed568476
            B/clauses/window-03/prompt.txt: b66d184c64940cc00f52e48e29584a731bec3970b75126fd83d88dbb947b5c2e
            B/clauses/window-03/meta.json: c1fdb90a77713707ba599dd72f7f457989d1453bc4774da6b984289c2e27618b
            B/clauses/window-04/raw.json: ff7510fca44d4e54a1608fb1f9aaa30214765c4687bbf2ea0a48937bc63713e4
            B/clauses/window-04/prompt.txt: f8fef89739ea66bc14d358d2e6abffddba305df46cac1dc693149820bd5f6d5b
            B/clauses/window-04/meta.json: aae6448a541ee008b9a616009f4635238c8fab1123d1498d920bd75d702960f9
            B/clauses/window-05/raw.json: b47af121c4fa9c8a28aeb82a84cd31d0ef40fe7a92510d5077cae9030b73fb4c
            B/clauses/window-05/prompt.txt: 92ef2a71afd96b563ba69c7abb423e86704b5294261fdee8df23cc293beee342
            B/clauses/window-05/meta.json: e928aa13affc72f3bb6c6b46c2a865b2cc68c1c77a8fde8686134ab315532ab3
            B/clauses/window-02/raw.json: bbc77f9eddd342e83b2c03f097252fa178c2157c63215b54d5fec99d6c5ee0a6
            B/clauses/window-02/prompt.txt: 1cfca70437f1445f606f79450c093aa2a5619f33290bae58a16ba8445a3b6cb9
            B/clauses/window-02/meta.json: ddedbd54b9110aa1ae13ff6d7db5668021e0717798074fda82f28da21d9a8904
            B/clauses/window-07/raw.json: 4575df16afa65fd7c2218d31fff0e3feccac6a41059f3c25d54b3f1c209170b3
            B/clauses/window-07/prompt.txt: ee6a17f007db9a0b78d4fa670d50c68886b1a15fe47dc17582030bb91a52eefd
            B/clauses/window-07/meta.json: 00c00b2b3ed9c972ff0b7a4df1539cefa0fa751e60674986618083a5e05a69ca
            B/clauses/window-01/raw.json: 6e5c38eeeda845a20a4ea1e56303de46c295855a97464056f96f7f32bef11022
            B/clauses/window-01/prompt.txt: cd12463ae8a9db1eeb381111d0c46aac3f2c0315a7061b75f56e4855bb7238b1
            B/clauses/window-01/meta.json: fec96604d5c186ea570a8ffa1be8c933756eb2095cfa7880c1861cb058a33df7
            B/clauses/window-06/raw.json: c6879ead9247b1455ed185ff68840615dfde598c8faa3cac4290c9e7e2192cac
            B/clauses/window-06/prompt.txt: bfe8f310eced23e5b6cea7b341aa9db0e879e19128730ed7c5738087a75b0482
            B/clauses/window-06/meta.json: e8187e4bf4aa2eecbbeb3cae2c70234f7c80aee0c8df23f080a312b76adc59c7
            B/tables/TABLE-2-page-8-3/raw.json: fcfdbe9b83034599687c2e3e7685f28538ab323c1ab4c855525366fdc0061a36
            B/tables/TABLE-2-page-8-3/prompt.txt: 0af81b6bd2d6fdae3565f2f6d9200524f29a152a966311d6ff4af24f255571ad
            B/tables/TABLE-2-page-8-3/meta.json: 86503444cfca0020dcee15278bea6f8f5fe1f3417c167d9d7366545acd74acfd
            B/tables/TABLE-3-page-9-4/raw.json: a45df8f0ef0ced3cc1a0004e569dc67f8ad4ad9e6ce006ce42f81f54383174ae
            B/tables/TABLE-3-page-9-4/prompt.txt: 781f9a6313f8842b13caff442d4d0fd9f682bddb733805e1eb480df91b38a030
            B/tables/TABLE-3-page-9-4/meta.json: 7ffbb02fd82d97293765b11fef5e3a587ad1a23872232f3a85c318c9c2fe8fa8
            B/tables/TABLE-2-page-5-1/raw.json: 9392d8c31787e49792926d91d55a78146e2c835d30b21f088bf84e900ac8a2e0
            B/tables/TABLE-2-page-5-1/prompt.txt: cca19119f6c6f0c55e778843ef6e8822f2e99764bc07f0935bc31d615d4f5a60
            B/tables/TABLE-2-page-5-1/meta.json: de55b5d3b89faffe71ce54fc39bf3e51fbc3f40e32524a08989817a597f3c4b2
            B/tables/TABLE-1-page-8-2/raw.json: de26fbdefbbd0afa091fd6734cba9025bd558e63cec33e310d99855118fc12cb
            B/tables/TABLE-1-page-8-2/prompt.txt: 2396ded08ac6f9ab53878d7981bab940954febd92fc1e29a0692bfecb0db5d28
            B/tables/TABLE-1-page-8-2/meta.json: 9c2658e30fff9b40dcc5154e15b5a9054e89c345f1982df8d348fa0aea78068f
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
          pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
          source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R002
        exposure:
          text: intervention to restore cortical perfusion
        outcome:
          text: aphasia
        analysis_label: Reperfusion intervention
        relation: treatment_effect
        evidence_ids:
        - P1-S2-C3
        - P5-S1-C5
        qualifier_ids:
        - P4-S1-C10
        - P4-S1-C11
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
          source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Accounting without a linked unit P1-S2-C2
          - Accounting without a linked unit P1-S2-C3
          - Accounting without a linked unit P1-S2-C4
          - Accounting without a linked unit P1-S2-C5
          - Accounting without a linked unit P2-S1-C1
          - Unaccounted source passage P1-S2-C5
          - Unaccounted source passage P1-S2-C2
          - Unaccounted source passage P2-S1-C1
          - Unaccounted source passage P1-S2-C4
          - Unaccounted source passage P1-S2-C3
          - Result passage disposed without unit P3-S1-C9
          - Result passage disposed without unit P3-S3-C2
          - Result passage disposed without unit P3-S3-C5
          - Result passage disposed without unit P3-S3-C8
          - Result passage disposed without unit P4-S1-C4
          - 'window 3: invalid/duplicate disposition P4-S2-C4'
          - Result passage disposed without unit P4-S2-C10
          - Result passage disposed without unit P4-S2-C7
          - Result passage disposed without unit P4-S3-C3
          - Result passage disposed without unit P5-S1-C11
          - Result passage disposed without unit P5-S1-C12
          - Result passage disposed without unit P5-S1-C13
          - Result passage disposed without unit P5-S1-C5
          - Result passage disposed without unit P5-S1-C8
          - Result passage disposed without unit P6-S1-C1
          - Result passage disposed without unit P6-S1-C2
          - Result passage disposed without unit P6-S1-C3
          - Accounting without a linked unit P6-S1-C4
          - Accounting without a linked unit P6-S1-C5
          - Accounting without a linked unit P6-S1-C6
          - Accounting without a linked unit P7-S1-C1
          - Accounting without a linked unit P7-S1-C2
          - Unaccounted source passage P7-S1-C2
          - Unaccounted source passage P6-S1-C4
          - Unaccounted source passage P7-S1-C1
          - Unaccounted source passage P6-S1-C5
          - Unaccounted source passage P6-S1-C6
          - Accounting without a linked unit P7-S1-C12
          - Result passage disposed without unit P7-S1-C4
          - Result passage disposed without unit P7-S1-C5
          - Accounting without a linked unit P7-S2-C2
          - Unaccounted source passage P7-S1-C12
          - Unaccounted source passage P7-S2-C2
          - Result passage disposed without unit P10-S1-C5
          unattached_null_or_qualifier_ids:
          - P1-S2-C2
          - P5-S1-C12
          - P5-S1-C14
          - P7-S1-C4
          suppressed_nonrepresented_units: 13
          default_disposition_count_requires_completeness_check: 148
          unselected_timing_passages:
          - P2-S2-C9
          - P2-S3-C6
          - P3-S2-C9
          - P4-S2-C3
          - P5-S1-C7
          - P9-S1-C6
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P1-S2-C4
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P1-S2-C5
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P4-S1-C8
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P4-S1-C9
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P5-S1-C13
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P6-S1-C5
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P6-S1-C6
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: validation
            source_id: P3-S3-C2
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: analysed_sample
            source_ids:
            - P1-S1-C18
            - P1-S1-C21
            - P1-S2-C2
            - P1-S2-C4
            - P1-S2-C5
            - P2-S2-C6
            - P4-S2-C5
            - P4-S2-C6
            - P4-S2-C12
            - P4-S2-C14
            - P4-S3-C7
            - P4-S3-C8
            - P4-S3-C9
            - P4-S3-C11
            - P5-S1-C9
            - P5-S1-C11
            - P5-S1-C12
            - P5-S1-C13
            - P5-S1-C14
            - P6-S1-C4
            - P6-S1-C5
            - P6-S1-C6
            - P7-S1-C12
            - P8-S1-C7
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: outcome_definition
            source_ids:
            - P1-S1-C19
            - P1-S2-C4
            - P1-S2-C5
            - P2-S2-C8
            - P4-S1-C6
            - P4-S1-C7
            - P4-S1-C8
            - P4-S1-C9
            - P5-S1-C13
            - P6-S1-C5
            - P6-S1-C6
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: analysis_restrictions
            source_ids:
            - P4-S2-C5
            - P4-S2-C6
            - P4-S2-C12
            - P4-S2-C14
            - P4-S3-C7
            - P4-S3-C8
            - P4-S3-C9
            - P4-S3-C11
            - P5-S1-C11
            - P5-S1-C12
            - P5-S1-C13
            - P5-S1-C14
            - P6-S1-C4
            - P6-S1-C5
            - P6-S1-C6
            - P7-S1-C12
            - P8-S1-C7
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - analysed_sample
          - outcome_definition
          - validation
          - analysis_restrictions
          - personal_factors
          - tested_personal_effects
          - adjustment_roles
          - explicitly_not_adjusted
          unclassified_extraction_ids: []
          table_review_required:
          - TABLE-1-page-8-2
          - TABLE-2-page-5-1
          - TABLE-2-page-8-3
          - TABLE-3-page-9-4
          unlinked_tables:
          - TABLE-1-page-8-2
          - TABLE-2-page-5-1
          - TABLE-2-page-8-3
          - TABLE-3-page-9-4
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P4-S2
            - P4-S3
            - P5-S1
            - P6-S1
            - P7-S2
            - P8-S1
            - P9-S2
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
          source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P1-S2-C2
          disposition: represented
          result_indexes:
          - 0
          reason: States all subjects with only subcortical lesions who had aphasia or neglect showed cortical hypoperfusion.
        - source_id: P1-S2-C3
          disposition: represented
          result_indexes:
          - 1
          reason: Reports 100% resolution of aphasia after successful restoration of cortical perfusion.
        - source_id: P1-S2-C4
          disposition: represented
          result_indexes:
          - 2
          reason: Compares association strength of aphasia/neglect with PWI vs DWI.
        - source_id: P1-S2-C5
          disposition: represented
          result_indexes:
          - 3
          reason: Provides PPV percentages for PWI vs DWI.
        - source_id: P3-S1-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: States no patients met a specific description for spontaneous speech aphasia.
        - source_id: P3-S3-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports mean scores for subtests.
        - source_id: P3-S3-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports control subject performance.
        - source_id: P3-S3-C8
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports inter-rater reliability.
        - source_id: P4-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports agreement between neuroradiologist and technician.
        - source_id: P4-S2-C6
          disposition: represented
          result_indexes:
          - 4
          reason: Reports 25/37 left subcortical lesion patients had aphasia and all had cortical hypoperfusion.
        - source_id: P4-S2-C7
          disposition: represented
          result_indexes:
          - 4
          reason: Specifies hypoperfusion was in the left MCA territory.
        - source_id: P4-S2-C8
          disposition: represented
          result_indexes:
          - 4
          reason: Concludes 100% of language deficits with isolated subcortical lesions were accounted for by hypoperfusion.
        - source_id: P4-S2-C9
          disposition: represented
          result_indexes:
          - 4
          reason: Reports only one non-aphasic subject with left subcortical lesions had hypoperfusion (occipital).
        - source_id: P4-S2-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Lists common sites of subcortical infarct.
        - source_id: P4-S2-C12
          disposition: represented
          result_indexes:
          - 5
          reason: Reports association between left corona radiata lesions, aphasia, and hypoperfusion.
        - source_id: P4-S2-C14
          disposition: represented
          result_indexes:
          - 6
          reason: Reports association between left caudate infarcts, language deficits, and hypoperfusion.
        - source_id: P4-S3-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Illustrative case description of Fig 1.
        - source_id: P4-S3-C4
          disposition: represented
          result_indexes:
          - 7
          reason: Reports no language impairments in five subjects with isolated left thalamic infarcts.
        - source_id: P4-S3-C6
          disposition: represented
          result_indexes:
          - 7
          reason: Reports one thalamic lesion subject had occipital hypoperfusion and visual deficits.
        - source_id: P4-S3-C8
          disposition: represented
          result_indexes:
          - 8
          reason: Reports 7/14 right subcortical lesion patients had neglect.
        - source_id: P4-S3-C9
          disposition: represented
          result_indexes:
          - 8
          reason: Reports all 7 neglect patients had hypoperfusion and 7 without neglect had none.
        - source_id: P4-S3-C11
          disposition: represented
          result_indexes:
          - 9
          reason: Reports neglect associated with right caudate/capsular and corona radiata sites.
        - source_id: P5-S1-C1
          disposition: represented
          result_indexes:
          - 9
          reason: Provides p-value for right subcortical site associations.
        - source_id: P5-S1-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Illustrative case description of Fig 2.
        - source_id: P5-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports partial reperfusion of cortex in treated subjects.
        - source_id: P5-S1-C5
          disposition: represented
          result_indexes:
          - 1
          reason: Reports substantial improvement/full recovery of language after intervention.
        - source_id: P5-S1-C8
          disposition: represented
          result_indexes:
          - 1
          reason: Reports persistent aphasia in non-intervention control.
        - source_id: P5-S1-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports prevalence of language deficits in left hemisphere stroke.
        - source_id: P5-S1-C12
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports DWI findings in aphasic subjects.
        - source_id: P5-S1-C13
          disposition: represented
          result_indexes:
          - 10
          reason: Reports 95% of subjects with lexical deficits had cortical hypoperfusion on PWI.
        - source_id: P6-S1-C4
          disposition: represented
          result_indexes:
          - 11
          reason: Reports all 27 right hemisphere stroke patients with neglect had cortical hypoperfusion.
        - source_id: P6-S1-C5
          disposition: represented
          result_indexes:
          - 2
          reason: Reports aphasia association with infarct (DWI) vs hypoperfusion (PWI).
        - source_id: P6-S1-C6
          disposition: represented
          result_indexes:
          - 2
          reason: Reports neglect association with infarct (DWI) vs hypoperfusion (PWI).
        - source_id: P7-S1-C1
          disposition: repeated
          result_indexes:
          - 0
          - 4
          - 8
          reason: Restatement of findings regarding subcortical infarctions and hypoperfusion.
        - source_id: P7-S1-C2
          disposition: repeated
          result_indexes:
          - 1
          reason: Restatement of resolution of aphasia after reversal of hypoperfusion.
        - source_id: P7-S2-C2
          disposition: repeated
          result_indexes:
          - 0
          - 4
          - 8
          reason: Restatement that 100% of subjects with aphasia/neglect showed hypoperfusion.
        - source_id: P8-S1-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports CT findings of chronic aphasic subjects.
        - source_id: P9-S1-C8
          disposition: repeated
          result_indexes:
          - 1
          reason: Restatement that reperfusion led to improvement of language function.
        - source_id: P9-S2-C2
          disposition: repeated
          result_indexes:
          - 0
          - 4
          - 8
          reason: Restatement that hypoperfusion could account for all cases.
        - source_id: P9-S2-C3
          disposition: represented
          result_indexes:
          - 0
          reason: States no support was found for the hypothesis that subcortical lesions directly cause deficits.
        - source_id: P9-S2-C7
          disposition: represented
          result_indexes:
          - 2
          - 10
          - 11
          reason: Table 3 provides the raw counts and chi-squared values for the associations.
        - source_id: P10-S1-C5
          disposition: repeated
          result_indexes:
          - 0
          - 4
          - 8
          reason: Concluding statement that hypoperfusion is an important contributor.
        unresolved_coverage:
        - source_id: P9-S2-C7
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P5-S1-C14
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P6-S1-C1
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P6-S1-C2
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P6-S1-C3
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P6-S1-C8
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P7-S1-C3
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P7-S1-C4
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P7-S1-C5
          disposition: unresolved
          reason: Discovery omitted this passage
        - source_id: P7-S1-C12
          disposition: unresolved
          reason: Discovery omitted this passage
        pending_source_ids:
        - P3-S1-C9
        - P3-S3-C2
        - P3-S3-C5
        - P3-S3-C8
        - P4-S1-C4
        - P4-S2-C7
        - P4-S2-C9
        - P4-S2-C10
        - P4-S3-C3
        - P4-S3-C6
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C8
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C14
        - P6-S1-C1
        - P6-S1-C2
        - P6-S1-C3
        - P6-S1-C8
        - P7-S1-C1
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C12
        - P7-S2-C2
        - P8-S1-C2
        - P9-S1-C8
        - P9-S2-C2
        - P9-S2-C3
        - P10-S1-C5
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review:
        - TABLE-1-page-8-2
        - TABLE-2-page-5-1
        - TABLE-2-page-8-3
        - TABLE-3-page-9-4
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample: []
          recruited_sample:
          - P1-S1-C18
          eligibility:
          - P2-S2-C10
          - P2-S3-C2
          - P2-S3-C5
          - P2-S3-C6
          - P2-S3-C7
          - P2-S3-C8
          imaging_provenance:
          - P3-S3-C9
          - P3-S3-C10
          - P3-S3-C11
          - P3-S3-C12
          - P3-S3-C14
          - P3-S3-C15
          - P4-S1-C5
          imaging_timing:
          - P1-S1-C18
          - P2-S2-C6
          - P2-S3-C7
          - P4-S2-C2
          - P5-S1-C5
          outcome_timing:
          - P1-S1-C18
          - P1-S1-C22
          - P2-S2-C7
          - P3-S1-C12
          - P4-S2-C2
          - P5-S1-C4
          - P5-S1-C5
          outcome_definition: []
          validation: []
          analysis_restrictions: []
          dependent_variable_statement:
          - P1-S1-C19
          - P2-S2-C8
          - P4-S1-C6
          - P4-S1-C7
          limitations:
          - P9-S2-C2
          - P9-S2-C3
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles: []
          explicitly_not_adjusted: []
          descriptive_personal_factors:
          - P2-S3-C6
          - P2-S3-C7
          - P2-S3-C8
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: none_described
        held_selections:
        - slot: dependent_variable_statement
          source_id: P1-S2-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P1-S2-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S1-C8
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S1-C9
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P5-S1-C13
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S1-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S1-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P3-S3-C2
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: analysed_sample
          source_ids:
          - P1-S1-C18
          - P1-S1-C21
          - P1-S2-C2
          - P1-S2-C4
          - P1-S2-C5
          - P2-S2-C6
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P4-S2-C14
          - P4-S3-C7
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C11
          - P5-S1-C9
          - P5-S1-C11
          - P5-S1-C12
          - P5-S1-C13
          - P5-S1-C14
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P7-S1-C12
          - P8-S1-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P1-S1-C19
          - P1-S2-C4
          - P1-S2-C5
          - P2-S2-C8
          - P4-S1-C6
          - P4-S1-C7
          - P4-S1-C8
          - P4-S1-C9
          - P5-S1-C13
          - P6-S1-C5
          - P6-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: analysis_restrictions
          source_ids:
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P4-S2-C14
          - P4-S3-C7
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C11
          - P5-S1-C11
          - P5-S1-C12
          - P5-S1-C13
          - P5-S1-C14
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P7-S1-C12
          - P8-S1-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
          review_sha256: e6bc89384582914e9ac4cfb0e968aa4a7a9918500a383a181737c523ab05a033
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
          - P1-S2-C3
          - P5-S1-C5
          source_result: In a subset of six patients with subcortical infarcts and cortical hypoperfusion who received intervention to restore perfusion (phenylephrine, endarterectomy, or stenting), 100% showed immediate resolution of aphasia. Repeat cognitive testing at 3 days showed substantial improvement with full recovery in most cases. This finding is based on a very small sample (n=6) and the authors note that they cannot rule out that cortical reperfusion sometimes occurs without resolution of aphasia in other cases.
          result_status: detected
          patient_measurement: non_imaging
          checks:
            analysis_identity:
              answer: fits
              reason: The selected analysis correctly identifies the specific subset of 6 patients who received reperfusion intervention and the outcome of aphasia resolution. The source (P1-S2-C3, P5-S1-C5) confirms this specific analysis distinct from the broader association studies.
              source_ids:
              - P1-S2-C3
              - P5-S1-C5
              - P4-S1-C10
            direction:
              answer: fits
              reason: The claim that intervention was associated with resolution of aphasia preserves the detected positive association (improvement/resolution) reported in the source. The direction 'likely' is appropriate given the observational nature and small sample size, avoiding causal overstatement while reflecting the observed outcome.
              source_ids:
              - P1-S2-C3
              - P5-S1-C5
            construct:
              answer: fits
              reason: The exposure (reperfusion intervention) and outcome (aphasia) are correctly identified. The patient measurement is non-imaging (cognitive testing battery), which is the actual measure of the outcome. The source confirms that cognitive testing was used to assess aphasia resolution, not imaging alone.
              source_ids:
              - P1-S2-C3
              - P5-S1-C5
              - P3-S1-C12
            qualifications:
              answer: fits
              reason: The draft includes the qualification that the finding is based on a small subset (n=6). This is a material caveat present in the source (P9-S1-C9) regarding the generalizability of the reperfusion finding.
              source_ids:
              - P4-S1-C10
              - P9-S1-C9
            missing_material_caveat:
              answer: fits
              reason: The draft captures the small sample size limitation. While the source notes that reperfusion might not always resolve aphasia (P9-S1-C9), the draft's qualification regarding the small subset implicitly covers the limited evidence base. No other material caveats that change the interpretation of this specific n=6 result are omitted.
              source_ids:
              - P9-S1-C9
          optional_pending: []
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        normalizations: []
        analysis_identity:
          id: R002
          exposure:
            text: intervention to restore cortical perfusion
          outcome:
            text: aphasia
          analysis_label: Reperfusion intervention
          relation: treatment_effect
          evidence_ids:
          - P1-S2-C3
          - P5-S1-C5
          qualifier_ids:
          - P4-S1-C10
          - P4-S1-C11
          context_ids: []
          table_ids: []
          approved: false
          status: requires_source_review
          flags:
          - new_model_candidate_not_verified
          candidate_discovery:
            model: gemma4:31b
            model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
            source_review: _compare/relationships-2026-11-16/review-current/Hillis2002
            source_status_sha256: 208f5f106ca70b44414797ed6ea0cbc2e06da6048ca2a4e38a4f7f0ca07efedb
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
      page: 1
      quote: 'Among

        the

        patients

        who

        received intervention that successfully restored cortical

        perfusion, 100% (six out of six) showed immediate reso-

        lution of aphasia.'
      status: pending
      by: agent:relationship-converter
      date: '2026-11-24'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The study reports that in a subset of patients with subcortical infarcts and cortical hypoperfusion, interventions to restore perfusion (e.g., phenylephrine, endarterectomy, stenting) were associated with the immediate resolution of aphasia.
    bucket: therapies
    entity_id: reperfusion_intervention
    name: Reperfusion intervention
    kind: therapy
    predictor_type: clinical
    definition: Intervention to restore cortical perfusion, consisting of induced blood pressure elevation with intravenous phenylephrine, urgent carotid endarterectomy, or carotid stenting.
    assessment:
    - bedside battery for lexical tasks (auditory and reading comprehension, picture naming, tactile naming, oral reading and repetition)
    - spoken yes/no questions
    - description of the 'cookie theft' picture from the Boston Diagnostic Aphasia Examination
    target: aphasia
    target_kind: impairment
    claim: Among patients who received intervention that successfully restored cortical perfusion, 100% (six out of six) showed immediate resolution of aphasia.
    direction: likely
    method: clinical_RCT
    relationship: treatment_response
    therapy:
      id: reperfusion_intervention
      name: Reperfusion intervention
    sample_n: 6
    population: Patients with subcortical infarcts and cortical hypoperfusion
    timing: Repeat cognitive testing and imaging performed the morning after intervention, which was 3 days after initial assessment (initial assessment within 24h of onset)
    qualifications:
    - Finding is based on a small subset of the total study population
    limitations:
    - Small sample size (n=6)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S2-C3
      supports: claim
    - source_id: P4-S1-C10
      supports: sample
    - source_id: P4-S1-C11
      supports: method
    - source_id: P5-S1-C5
      supports: claim
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
      review_sha256: e6bc89384582914e9ac4cfb0e968aa4a7a9918500a383a181737c523ab05a033
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
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/therapies/reperfusion_intervention__Hillis2002__R002.md
    seconds_this_run: 107.98642087500775
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 4113b06a0caa9c8be9da035d0a308bb233084f7c662f71e6e32f3a42c5549963
      original_mapping_sha256: fbf598ae3eadda7d4a12b949fab6490c6974321ca5b109e97fe2e5ae98738a6c
      original_status_sha256: 4edf5d6cb437bd1bb51e64329816a00c61cc21d27eae2daabdbbec74c4fdd9be
      evidence_sha256: 2f81d08a1b481f955e501d30518c0ed7f47eaa39b62d79f0ed518fb35b74a6b5
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 4
      - 5
      - 6
      note: Used the detailed Results description instead of the abstract’s blanket 100% immediate-resolution wording. Four patients received induced blood-pressure elevation, one endarterectomy and one a stent. Observational selected case series; intervention effectiveness cannot be isolated from this uncontrolled comparison.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Among

    the

    patients

    who

    received intervention that successfully restored cortical

    perfusion, 100% (six out of six) showed immediate reso-

    lution of aphasia.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Used the detailed Results description instead of the abstract’s blanket 100% immediate-resolution wording. Four patients received induced blood-pressure elevation, one endarterectomy and one a stent. Observational selected case series; intervention effectiveness cannot be isolated from this uncontrolled comparison.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
