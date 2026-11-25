---
id: right_temporal_pole_cluster
name: right temporal pole cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: picture_semantic_judgements
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: picture_semantic_judgements
  target_kind: impairment
  claim: significant activation was found in the right temporal pole for picture judgements
    when participants who performed at chance were removed from the analysis
  direction: likely
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 12
    population: patients with chronic Wernicke's aphasia
    phase: not_reported
    time_post_onset: chronic phase
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - low semantic demands of the animate-inanimate judgement task
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: activation in the right temporal pole during picture
    semantic animate-inanimate judgements, measured via distortion-corrected functional
    MRI. finding emerged only after removing participants who performed at chance
    for the picture or written word judgements. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S1-C3, two-model
    agreement, human verification pending): Materials and methods


    Participant diagnosis and lesions


    Twelve participants with chronic Wernicke''s aphasia [two female, mean age 70.1,
    standard deviation (SD) 8.7] and 12 age- and education-matched control participants
    (one female, mean age 71, SD 6.9) were recruited and provided written informed
    consent as approved by the Multicentre Research Ethics Committee NHS ethics committee
    Original text-layer quotation is preserved below.'
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
    - proposed_concept:picture_semantic_judgements
  citation: '@Robson2014'
  source_passages:
  - section: Original source P8-S1-C7
    page: 8
    quote: 'Removal of the

      participants who performed at chance for the picture or written

      word judgements made no change to signiﬁcance with the excep-

      tion that signiﬁcant activation was additionally found in the right

      temporal pole for the picture judgements [t(9) = 2.1, P = 0.03].'
    supports: claim
  - section: Original source P3-S1-C3
    page: 3
    quote: 'Materials and methods

      Participant diagnosis and lesions

      Twelve participants with chronic Wernicke’s aphasia [two female,

      mean age 70.1, standard deviation (SD) 8.7] and 12 age- and educa-

      tion-matched control participants (one female, mean age 71, SD 6.9)

      were recruited and provided written informed consent as approved by

      the Multicentre Research Ethics Committee NHS ethics committee.'
    supports: sample
  - section: Original source P3-S1-C6
    page: 3
    quote: 'All patients presented with classical symptoms of Wernicke’s aphasia

      after a single left hemisphere stroke; namely impaired single word

      comprehension,

      single

      word

      repetition

      and

      ﬂuent,

      sentence-like

      speech punctuated with phonological or neologistic errors.'
    supports: sample
  - section: Original source P5-S2-C9
    page: 5
    quote: 'Functional magnetic resonance imaging

      acquisition

      This study used distortion-corrected, spin echo EPI functional MRI.'
    supports: method
  - section: Original source P11-S2-C10
    page: 11
    quote: 'However, given the low semantic demands of the animate-inani-

      mate judgement task, this interpretation must be viewed with

      caution.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Robson2014
  proposal_id: R020
  review_status_sha256: b5611394bfedf767579836e4b653e74dbb2e1a9fb19a12af8a267a3dbc631c5a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
    original_review_binding:
      version: relationship-review-v6
      input_hashes:
        pdf: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
        A/passages.json: 86ed03ad98128894519cf24dcf7cbd731c67bb079a008edd63b231f390eebdd2
        A/raw.json: 7d30cb1c3e7004de52ebcbfcdf7e113879c1614238dd31ee0f49e632338a95ed
        A/source-units.json: 9310890d4c6e2ec2d480af1193509dfbc8918855a7ce16aa1b84e3eb732debb9
        A/full-source-units.json: 143a69ce4823df2bfdfcc5e732bfc539c5e79870cf0c2dd8c82d5b93019d4b5c
        A/meta.json: fd21ecbca8e8de32e50bc3407e607e4e8f3b6e02f38576dcc139b1616a170bc9
        A/table-images/TABLE-1-page-3-1.png: efd36c4c8dabb36eddf2a4c19e53db32609d017852cb063b71ace93a13e20659
        A/table-images/TABLE-5-page-8-1.png: 8f028831cd8886743eadea768ff0cdd9158f864460f577e10d39f445dffee499
        A/table-images/page-3.png: bb9f824c1cfe150e11d65a6a1e1a405439176611c779e1369d3203ffe297ce3b
        A/table-images/page-6.png: d9fd099365936161cce3e16cf519a1238da2bfae44fc43b6ee1e6df960e94428
        A/table-images/page-7.png: dcbdfa51beeec8872db9afad0ece01e9e09b50d23b393f0167b84e61318b6d89
        A/table-images/page-4.png: 2ecbbac33be1d1a55dbd7cc58d6e75c398a543fdc48e296c1b129a110c2597f5
        A/table-images/page-9.png: b58fe7a3ea7235b212e1facc0473ad27ffb56fb196e4ea4895d548d5bbcdfd65
        A/table-images/TABLE-3-page-6-1.png: 07fd569f6773466d535afad008d792cbb5a57ba124a47ca2c0f1a17975e8ecf8
        A/table-images/page-8.png: 134eecfd68579d1fcf7d95f208e4d9ce17cac6df2b1eb488ab688cf14e985c10
        A/table-images/TABLE-6-page-8-2.png: 55c6e7a7fb573033a3a41b0b08cc83657dc3623bf206c6bc94ddc5cb030a115a
        A/table-images/manifest.json: 993fc9a0b2ba7830f615ed1a82336230a612926547272e8209b95382ab935b30
        A/table-images/TABLE-2-page-4-1.png: 8d8a8b65ce036f2933347295c74c9f0e11c40dab9d2e14606f423e9a7cec251d
        A/table-images/TABLE-4-page-7-1.png: 2d9e1667e9481ac932906b46cb2ca0bb3df04c78ffdfb4d1c612973b363609d9
        A/table-images/TABLE-7-page-9-1.png: 09d83cd4bf6a13d1f3b2229d1e30f42b35c64eb763f7be4ac200195e7944a982
        A/clauses/window-03/raw.json: ef73aa5065735b5f343aba4a6660fcd996bad2185bdaf5c46e7b2112e0f3ca2d
        A/clauses/window-03/prompt.txt: 1022df533e3d86ade7c7ca08ad5abce0ff98b1f48dcd5df3f005ff0f4be11a1f
        A/clauses/window-03/meta.json: 6c4c6711aece74f9d227908e621ac229633aa51dcef3e916806314a8a5742500
        A/clauses/window-04/raw.json: 410973dacf473130f4eb8b0e03dfdc7566bcb5d4d9c97096d59c1d9f03989c56
        A/clauses/window-04/prompt.txt: 502d66ef881e96e1564b2e62d9f677a3e14d91322e230304d7c99bcb68a26ec1
        A/clauses/window-04/meta.json: 9b91f2c898b62a7821f70fcf0b19e04acb46a1f2b2979225acde81594f2fb2c6
        A/clauses/window-05/raw.json: 7fbe53e2425d81fbb0ba95e25e0e2ab0e66091ac12d7b2cf36750011fbe76976
        A/clauses/window-05/prompt.txt: 9fabc006df77134b00ad483e2d40b42816a0e49b8fb96b37dd03ca2642189358
        A/clauses/window-05/meta.json: e21bac9b603b53bb76f69f5c868849df1c0f6ba326b0fa11fffcd1b2994c782a
        A/clauses/window-02/raw.json: fe50894007e96f68e8ccbccf6fadc55d57855d723ec20f1f9e822396abdf7e00
        A/clauses/window-02/prompt.txt: 36f2c1cd27fa3ac1d91042dfc9f979cb1e72961290219625610a93c6e44e011e
        A/clauses/window-02/meta.json: eef279a10fa34e89d00a1062ddaa491a3adbefb521b988d85ef47084621eee9c
        A/clauses/window-09/raw.json: 7ca28f83ba73ce97f50973f17f977e3fad58d2d866d34ee4240da9162320534d
        A/clauses/window-09/prompt.txt: e4f970271dd79a7cff11351286d5227bb8fbf3a482c7caaf1020efc9fddf079d
        A/clauses/window-09/meta.json: caa44a457892198e58c5fac8cb1a3a5cbe0a0da92f9aecf87baf2d3a46c533ca
        A/clauses/window-07/raw.json: 2f12a32605c10f22e7e8b8dcfebe4f42980a131a64224965ee1c03d0717d3ffc
        A/clauses/window-07/prompt.txt: 4b9ffe3828dd706d4c73b475d0135c70991884c03511dcc0a5fb3cc6fb570d6b
        A/clauses/window-07/meta.json: d930c07216d9ce1eb6a5b759cdbfd5729e311fed4a6b8c6349e3b659fbc7c2de
        A/clauses/window-01/raw.json: 0270a934a87d3a86eadaf2363d500271ec7a9e86866141a2773ea6e99b76e4e6
        A/clauses/window-01/prompt.txt: 2e271edd69bef6f05ea4a095068572d43bf220fe69e85170af83987bee493d19
        A/clauses/window-01/meta.json: 018537e3e1eca32278ac3df7d42f9f839c3019994da9b042becc96b69b777ad1
        A/clauses/window-06/raw.json: 16f6e34f57dfe531c1e737a789412e8b9cc3ea87c0b4e8192665d4a0e432809f
        A/clauses/window-06/prompt.txt: 4cfbb90ef2ad8a3a6682b9bfde97beff38819ca0d50e6a8b3ae013fcaa00d27e
        A/clauses/window-06/meta.json: 49ba2e1dd857873e5c25457ac12e2f0f0b9291379484bef29daa02370e61a1b0
        A/clauses/window-08/raw.json: e541936b60ada609be7fc0e9e28e8b7972703973b3d832243ff0b73c68311585
        A/clauses/window-08/prompt.txt: d335727999a99c5ac67de05b4bb1169934107a1ba25c8a3411708495bd84f3b3
        A/clauses/window-08/meta.json: 531ab4c1eb57887bdb03878df7e5490d2dd9b066792750fcbb1c77aa1f1d7fe0
        A/tables/TABLE-5-page-8-5/raw.json: f65bdf199fc77070e51c952bad84cafe8b4316542fb76266d0454c41c2106860
        A/tables/TABLE-5-page-8-5/prompt.txt: 46abb3955e42cd5bc055d037a39529ce3642adf77ff7f8cd3a6be23669f6505c
        A/tables/TABLE-5-page-8-5/meta.json: 65549d70d396b1aff1f942afb8b59136567d3ad40e88637e4e8b588e27238be0
        A/tables/TABLE-6-page-8-6/raw.json: 9e7ff5186504a99675b65e6dbd74303cbc54a1018d83e221865e907e799fd948
        A/tables/TABLE-6-page-8-6/prompt.txt: 061dbea2c48878e8955ae3271bf17c2a8011f83bc2500179c18fd61e8a648ed7
        A/tables/TABLE-6-page-8-6/meta.json: 9eebc17451304520bb8cb56239e262db6f2c5a4fb6bafe88dd59f8dfef0b6cb0
        A/tables/TABLE-3-page-6-3/raw.json: 5b5836bb2f5e55da6a8b27d2b2201b973e6da3d5784bfeb1f91ea795f9505bd5
        A/tables/TABLE-3-page-6-3/prompt.txt: 58497adab94aac7abec02aab9786921f3dec52c3a7a7bda52d1f5d5e29c15733
        A/tables/TABLE-3-page-6-3/meta.json: 62158ba3657a3c0c281d68b6768c29712de1416d2215d3505c0453957b96c69c
        A/tables/TABLE-1-page-3-1/raw.json: 544a95557f2b2a494f0ea067fa01e21aa3a59bd3e07287efb10da2ce67a87677
        A/tables/TABLE-1-page-3-1/prompt.txt: 4aa8be48c142177b2d6de72732d371988da80ff1d6be6c2a62c13bc6e91a49bd
        A/tables/TABLE-1-page-3-1/meta.json: 4c86bac731c93ac1e5fccbac8b4b8d078c9d596ac93a4e937c15c61e1e6e299c
        A/tables/TABLE-4-page-7-4/raw.json: 304019f7f81885806f5d4d079db0077328d6ccbf86a3ba4df4d1e06bbc3817a9
        A/tables/TABLE-4-page-7-4/prompt.txt: 06a710a187bb6e566426b63ad98f3b99f2f9f34b61978b6edeb014db58595692
        A/tables/TABLE-4-page-7-4/meta.json: 44dc2e40d79cf1a23e0278c939d2cfbec8478df93fc0190fabeec7ff14110a79
        A/tables/TABLE-7-page-9-7/raw.json: 22e1fd2f305f25205ec756f43fdf8307290ac6126d10f88339c1ef6403531552
        A/tables/TABLE-7-page-9-7/prompt.txt: a884b46f14cedf047b3225cb3f12c02068e79e4071176d71c5df45ab3b241209
        A/tables/TABLE-7-page-9-7/meta.json: a4cb12a510f938e0460c8e92be0d8403c50599cc047e64277a2a89c772a5c06f
        A/tables/TABLE-2-page-4-2/raw.json: 9ee47a197236ab270b9407ede5cb1a84fea65a00abd6fbd04145b6eda6fb88ae
        A/tables/TABLE-2-page-4-2/prompt.txt: 25d2adfecc42f4cdb11b2083a56225d241d125f99e2d14c1b7247fe9b70eacab
        A/tables/TABLE-2-page-4-2/meta.json: 4509fc7c95b84e80364130c1c565ca2af9d2ac95cc8d41b7e0378cdd7cb602fa
        B/passages.json: 86ed03ad98128894519cf24dcf7cbd731c67bb079a008edd63b231f390eebdd2
        B/raw.json: 4bb50353aca5723790a7d322d2b33091788a3e6d28df6dae8944bd1715868460
        B/source-units.json: 9310890d4c6e2ec2d480af1193509dfbc8918855a7ce16aa1b84e3eb732debb9
        B/full-source-units.json: 143a69ce4823df2bfdfcc5e732bfc539c5e79870cf0c2dd8c82d5b93019d4b5c
        B/meta.json: a29b84bff6364bb70e6a0a925dbd36be9361c02d191c9ad73e6491ee7f9b1019
        B/table-images/TABLE-1-page-3-1.png: efd36c4c8dabb36eddf2a4c19e53db32609d017852cb063b71ace93a13e20659
        B/table-images/TABLE-5-page-8-1.png: 8f028831cd8886743eadea768ff0cdd9158f864460f577e10d39f445dffee499
        B/table-images/page-3.png: bb9f824c1cfe150e11d65a6a1e1a405439176611c779e1369d3203ffe297ce3b
        B/table-images/page-6.png: d9fd099365936161cce3e16cf519a1238da2bfae44fc43b6ee1e6df960e94428
        B/table-images/page-7.png: dcbdfa51beeec8872db9afad0ece01e9e09b50d23b393f0167b84e61318b6d89
        B/table-images/page-4.png: 2ecbbac33be1d1a55dbd7cc58d6e75c398a543fdc48e296c1b129a110c2597f5
        B/table-images/page-9.png: b58fe7a3ea7235b212e1facc0473ad27ffb56fb196e4ea4895d548d5bbcdfd65
        B/table-images/TABLE-3-page-6-1.png: 07fd569f6773466d535afad008d792cbb5a57ba124a47ca2c0f1a17975e8ecf8
        B/table-images/page-8.png: 134eecfd68579d1fcf7d95f208e4d9ce17cac6df2b1eb488ab688cf14e985c10
        B/table-images/TABLE-6-page-8-2.png: 55c6e7a7fb573033a3a41b0b08cc83657dc3623bf206c6bc94ddc5cb030a115a
        B/table-images/manifest.json: f92eeba38bd6903ac07e4caf1507b7096789cbf7c634908c9cc965b10e717d8b
        B/table-images/TABLE-2-page-4-1.png: 8d8a8b65ce036f2933347295c74c9f0e11c40dab9d2e14606f423e9a7cec251d
        B/table-images/TABLE-4-page-7-1.png: 2d9e1667e9481ac932906b46cb2ca0bb3df04c78ffdfb4d1c612973b363609d9
        B/table-images/TABLE-7-page-9-1.png: 09d83cd4bf6a13d1f3b2229d1e30f42b35c64eb763f7be4ac200195e7944a982
        B/clauses/window-03/raw.json: 2c70c5f4ac7a70fc1ea68ec77d8c2a22e7de9130a8b3261aedde8bf8ef86899e
        B/clauses/window-03/prompt.txt: 1022df533e3d86ade7c7ca08ad5abce0ff98b1f48dcd5df3f005ff0f4be11a1f
        B/clauses/window-03/meta.json: 469c170f9c3a1eb1b554a3a0148e97d5fbeb1d9d590e98633f0110bc6b2b367f
        B/clauses/window-04/raw.json: 9c26eff1aaca1e5feb48446c5a414f6702418c38b461de29b55f651fa99c5fd1
        B/clauses/window-04/prompt.txt: 502d66ef881e96e1564b2e62d9f677a3e14d91322e230304d7c99bcb68a26ec1
        B/clauses/window-04/meta.json: 98a64ef70cd8c34516efc934a0e2ba53f58878b0b0168c3ef43fd8490676336c
        B/clauses/window-05/raw.json: fd006fd6a1ac5d0f98512321a78ff6548d24bec67b7f5965dc0fb94e561e7440
        B/clauses/window-05/prompt.txt: 9fabc006df77134b00ad483e2d40b42816a0e49b8fb96b37dd03ca2642189358
        B/clauses/window-05/meta.json: 02ec08b6c585dcce6b74065665d3aa59bdfd7f4ecb1da2c06ce609bbfc995216
        B/clauses/window-02/raw.json: b1dbbbbdcbe7896039f9736036f37ab37437bad01e8613d5c2727159dc772f53
        B/clauses/window-02/prompt.txt: 36f2c1cd27fa3ac1d91042dfc9f979cb1e72961290219625610a93c6e44e011e
        B/clauses/window-02/meta.json: e1cf8a7f34497edf2a80d0ce3e48fab2e4513985c47d7344b348fb43c61b74e2
        B/clauses/window-09/raw.json: 6ecc56fdb05dfbcab4cfcc482f03cc18382972bd0129031f422e2d6aef9ad465
        B/clauses/window-09/prompt.txt: e4f970271dd79a7cff11351286d5227bb8fbf3a482c7caaf1020efc9fddf079d
        B/clauses/window-09/meta.json: 3bbbef56db55e22be08728fdde86481c7817c15cfa89c5340c982e73127d2596
        B/clauses/window-07/raw.json: 7064304fd3655e3c638d53e4ec43dcfec3ffeae93224fa3191c0b7aa7e935979
        B/clauses/window-07/prompt.txt: 4b9ffe3828dd706d4c73b475d0135c70991884c03511dcc0a5fb3cc6fb570d6b
        B/clauses/window-07/meta.json: 712ada3c95aadd409ffa7993c3f54d816e837a602d6d6685d85df2df5606b6b9
        B/clauses/window-01/raw.json: 1c186705c45c0fc3e94c35e8b4699da5595fa29c19eb44c3cd3f4be5f364f674
        B/clauses/window-01/prompt.txt: 2e271edd69bef6f05ea4a095068572d43bf220fe69e85170af83987bee493d19
        B/clauses/window-01/meta.json: 7afbf907454a1c1900e8a923222962a4c6b5b77bb4328ae551423c2114ba2205
        B/clauses/window-06/raw.json: d1362526ff236fa4441f1df84e112a3d30f54dec1998f2cc833611d50cb24072
        B/clauses/window-06/prompt.txt: 4cfbb90ef2ad8a3a6682b9bfde97beff38819ca0d50e6a8b3ae013fcaa00d27e
        B/clauses/window-06/meta.json: ab0a1f570c0fe60e41a6af72c702c8039a1460f44ab13c28ff1b3ae9537d5174
        B/clauses/window-08/raw.json: fcf1108f9e9f5c9ccd416aee04dc748532905088dbbe3555b8e3525f1a31b24d
        B/clauses/window-08/prompt.txt: d335727999a99c5ac67de05b4bb1169934107a1ba25c8a3411708495bd84f3b3
        B/clauses/window-08/meta.json: 7aa583bdbfa5579c44f9f8c7a9bfa533861122a8d7ffdeecef2b14c631e25596
        B/tables/TABLE-5-page-8-5/raw.json: b7e7d528c741ac50ec3323ecdb983c34e9555ff9538b4610bf18bc6690553d3b
        B/tables/TABLE-5-page-8-5/prompt.txt: 46abb3955e42cd5bc055d037a39529ce3642adf77ff7f8cd3a6be23669f6505c
        B/tables/TABLE-5-page-8-5/meta.json: 79bc2f45d01065e935b2361c44115ef4a9abbc071a445681e2f5a5d3901d9dec
        B/tables/TABLE-6-page-8-6/raw.json: aaf9aeb3423eed0285aa841327bde8b6aaa8a20cf35f564da71b7cecb76f99a9
        B/tables/TABLE-6-page-8-6/prompt.txt: 061dbea2c48878e8955ae3271bf17c2a8011f83bc2500179c18fd61e8a648ed7
        B/tables/TABLE-6-page-8-6/meta.json: 26915aa07078119eae380ad94c5624dec635f66d2bfb19cd2795a126b9d8d39c
        B/tables/TABLE-3-page-6-3/raw.json: 394dd696aa002b0d0212d300cc2b99502b44f70e8fa2536762967595883617ce
        B/tables/TABLE-3-page-6-3/prompt.txt: 58497adab94aac7abec02aab9786921f3dec52c3a7a7bda52d1f5d5e29c15733
        B/tables/TABLE-3-page-6-3/meta.json: ea6f279ad9da667f32cd0ca45bec1887edf01ec42ce27b623ce2f22f33ae5715
        B/tables/TABLE-1-page-3-1/raw.json: 6f29123207cddf4994821f8173c970c97248a15f2eefddec7b2ba6e6fc03c19f
        B/tables/TABLE-1-page-3-1/prompt.txt: 4aa8be48c142177b2d6de72732d371988da80ff1d6be6c2a62c13bc6e91a49bd
        B/tables/TABLE-1-page-3-1/meta.json: b4352970259b5cdec662883f184c5a64d56f788d6d84c682730e618bc01c6706
        B/tables/TABLE-4-page-7-4/raw.json: ff9cd664f46f77f4b2bf9502b3bd39cdd1ddfddd07b002eecff0195ea50a685d
        B/tables/TABLE-4-page-7-4/prompt.txt: 06a710a187bb6e566426b63ad98f3b99f2f9f34b61978b6edeb014db58595692
        B/tables/TABLE-4-page-7-4/meta.json: a3a4bcff4076dfce7750c226a22279aa023d133d992a847f2e36dd8d74fe8a5f
        B/tables/TABLE-7-page-9-7/raw.json: 3a2fa549fbb59621c24b10567fcaf4b3efa31850380cc17fe1175cfdf4e5feb6
        B/tables/TABLE-7-page-9-7/prompt.txt: a884b46f14cedf047b3225cb3f12c02068e79e4071176d71c5df45ab3b241209
        B/tables/TABLE-7-page-9-7/meta.json: 370977a5338b992ab1b8eda5a48f8c2bf6130cde3de963576d0a70f1e7454e6e
        B/tables/TABLE-2-page-4-2/raw.json: 99cf526c886ea51448d806c9677750419e2df229e5f80464fa615788515a6719
        B/tables/TABLE-2-page-4-2/prompt.txt: 25d2adfecc42f4cdb11b2083a56225d241d125f99e2d14c1b7247fe9b70eacab
        B/tables/TABLE-2-page-4-2/meta.json: 6c3ece881a7879a4ec17cfbdf3917157257538eff13c25728b5ff54f21e762c2
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
      pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
      source_review: _compare/relationships-2026-11-16/review-current/Robson2014
      source_status_sha256: 7616af72b19325d10a71e23df1d6a73a2c7ed68fa60d9ddc3316c8bb4d755e90
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R020
    exposure:
      text: picture judgements
    outcome:
      text: activation in the right temporal pole
    analysis_label: Region of interest analysis (sensitivity)
    relation: sensitivity
    evidence_ids:
    - P8-S1-C7
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
      pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
      source_review: _compare/relationships-2026-11-16/review-current/Robson2014
      source_status_sha256: 7616af72b19325d10a71e23df1d6a73a2c7ed68fa60d9ddc3316c8bb4d755e90
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C9
      - Accounting without a linked unit P3-S2-C5
      - Unaccounted source passage P3-S2-C5
      - Accounting without a linked unit P3-S2-C7
      - Accounting without a linked unit P3-S2-C8
      - Accounting without a linked unit P3-S2-C9
      - Unaccounted source passage P3-S2-C9
      - Unaccounted source passage P3-S2-C7
      - Unaccounted source passage P3-S2-C8
      - Accounting without a linked unit P5-S3-C9
      - Unaccounted source passage P5-S3-C9
      - Accounting without a linked unit P6-S1-C13
      - Accounting without a linked unit P6-S2-C1
      - Unaccounted source passage P6-S1-C13
      - Unaccounted source passage P6-S2-C1
      - Result passage disposed without unit P6-S2-C7
      - Unresolved source passage P6-S2-C7
      - Result passage disposed without unit P6-S2-C8
      - Unresolved source passage P6-S2-C8
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C4
      - Accounting without a linked unit P10-S1-C6
      - Accounting without a linked unit P10-S1-C7
      - Accounting without a linked unit P10-S2-C2
      - Unaccounted source passage P10-S1-C7
      - Unaccounted source passage P10-S1-C6
      - Unaccounted source passage P10-S2-C2
      - Accounting without a linked unit P10-S2-C6
      - Unaccounted source passage P10-S2-C6
      - Result passage disposed without unit P10-S3-C9
      - Accounting without a linked unit P10-S4-C2
      - Unaccounted source passage P10-S4-C2
      - Result passage disposed without unit P11-S2-C9
      - Accounting without a linked unit P11-S4-C2
      - Accounting without a linked unit P11-S4-C3
      - Unaccounted source passage P11-S4-C2
      - Unaccounted source passage P11-S4-C3
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C6
      unattached_null_or_qualifier_ids:
      - P8-S1-C2
      - P11-S4-C2
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 183
      unselected_timing_passages:
      - P1-S1-C7
      - P2-S3-C8
      - P3-S1-C3
      - P12-S1-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S4-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P12-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C7
        - P2-S3-C11
        - P3-S1-C1
        - P6-S1-C1
        - P6-S1-C2
        - P6-S1-C12
        - P6-S2-C6
        - P7-S1-C8
        - P8-S1-C4
        - P8-S1-C5
        - P10-S1-C1
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S3-C11
        - P11-S4-C2
        - P11-S4-C3
        - P12-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C7
        - P2-S3-C11
        - P3-S1-C3
        - P3-S2-C12
        - P8-S1-C4
        - P8-S1-C5
        - P10-S1-C1
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S3-C11
        - P11-S4-C2
        - P11-S4-C3
        - P12-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C6
        - P2-S3-C9
        - P3-S1-C2
        - P3-S2-C10
        - P5-S3-C4
        - P6-S1-C6
        - P6-S3-C3
        - P10-S1-C3
        - P11-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C6
        - P1-S1-C8
        - P3-S1-C11
        - P3-S1-C14
        - P3-S2-C3
        - P3-S2-C4
        - P5-S3-C12
        - P5-S4-C8
        - P6-S1-C11
        - P6-S1-C12
        - P6-S2-C10
        - P8-S1-C4
        - P8-S1-C5
        - P10-S1-C1
        - P11-S1-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C7
        - P2-S3-C11
        - P3-S1-C3
        - P3-S1-C4
        - P3-S2-C12
        - P3-S3-C1
        - P3-S3-C2
        - P3-S3-C4
        - P3-S3-C5
        - P4-S2-C8
        - P4-S2-C9
        - P5-S3-C11
        - P10-S1-C4
        - P11-S2-C9
        - P12-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      - TABLE-5-page-8-5
      - TABLE-6-page-8-6
      - TABLE-7-page-9-7
      unlinked_tables:
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      - TABLE-5-page-8-5
      - TABLE-6-page-8-6
      - TABLE-7-page-9-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P6-S2
        - P7-S1
        - P8-S1
        - P9-S1
        - P10-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
      source_review: _compare/relationships-2026-11-16/review-current/Robson2014
      source_status_sha256: 7616af72b19325d10a71e23df1d6a73a2c7ed68fa60d9ddc3316c8bb4d755e90
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Directly states activation in ventral and anterior temporal lobes for
        semantic judgements.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: States over-activation in anterior temporal lobe regions for the aphasia
        group.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: States recruitment of right anterior superior temporal lobe for written
        words.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pre-scan behavioral test accuracy differences.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 2 for behavioral results.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes impairment rates in behavioral tests.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes impairment rates in behavioral tests.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes relationship between semantic association and overall impairment.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap location.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion extension.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion distribution relative to previous studies.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes hemodynamic response function analysis.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces results section.
    - source_id: P6-S2-C1
      disposition: represented
      result_indexes:
      - 3
      reason: States aphasia group was less accurate on semantic and baseline tasks.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports individual performance above chance for picture task.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports individual performance above chance for word condition.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports individual performance above chance for control condition.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that different analysis versions yielded similar results.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Notes a difference between analysis (i) and (ii) in ROI analysis.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 2 for whole brain results.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Tables 5-7 for peak coordinates.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about extensive temporal lobe activation.
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 4
      reason: States bilateral ventral temporal lobe activation for both modalities.
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Details specific regions activated by picture judgements.
    - source_id: P6-S2-C14
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies medial frontal cortex activation for picture judgements.
    - source_id: P6-S2-C15
      disposition: represented
      result_indexes:
      - 7
      reason: Details specific regions activated by written word judgements.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 7
      reason: Continuation of the sentence in P6-S2-C15.
    - source_id: P6-S3-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Continuation of the sentence in P6-S2-C14.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies additional peaks for written word judgements.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group activation patterns.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group additional peaks.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 9
      reason: States greater activation in WA group in ventral and middle temporal
        lobes.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: States greater activation in WA group in right superior temporal sulcus.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 11
      reason: States control group had greater activation in right posterior cingulate.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that main effects of condition were limited.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: States pictures produced greater activation in left ventral temporal
        pole.
    - source_id: P7-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: 'Null finding: no temporal lobe regions more active in controls.'
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 13
      reason: States written words produced greater activation in parahippocampal
        gyri and right IFG.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: 'Null finding: no Group x Condition interactions.'
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Reports control group activation for pictures (L aFuG) and words (L
        aSTG).
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 16
      reason: Reports WA group activation for both modalities in L aFuG, R aFuG, L
        TP, and L vOT.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Reports WA group activation in R aSTG (words) and R vOT (pictures).
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 19
      reason: 'Sensitivity result: removing chance performers added significance to
        R TP for pictures.'
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 20
      reason: Reports WA group activation in aFuG, vOT bilaterally and L lateral polar
        region.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 21
      reason: Reports WA group activation in R aSTG for written words.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 22
      reason: ANOVA results for main effect of group in L vOT, R vOT, and L TP.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 23
      reason: Null finding for effects of condition or interactions in ANOVA.
    - source_id: P10-S4-C2
      disposition: represented
      result_indexes:
      - 24
      reason: Reports WA group activation in R aSTS/STG for written words.
    - source_id: P10-S4-C3
      disposition: represented
      result_indexes:
      - 25
      reason: Reports control group activation in L aSTG/S for written words.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of results regarding R aSTG/S activation.
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 26
      reason: States results did not support prediction of greater reorganization
        for written words.
    - source_id: P11-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for condition effects in ROI and Group x Condition in whole
        brain.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of WA activation to young controls.
    - source_id: P11-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for upregulation of IFG or TPJ.
    - source_id: P11-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about limited large-scale reorganization.
    - source_id: P11-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes behavioral performance differences.
    - source_id: P12-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that removing poor performers did not change results.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restating activation in ATL.
    unresolved_coverage:
    - source_id: P6-S2-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S2-C5
    - P3-S2-C6
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C9
    - P4-S1-C2
    - P4-S1-C3
    - P4-S2-C8
    - P5-S3-C9
    - P6-S1-C13
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C8
    - P6-S2-C9
    - P6-S2-C10
    - P6-S2-C11
    - P6-S3-C2
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C7
    - P7-S1-C14
    - P8-S1-C2
    - P8-S1-C3
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C6
    - P10-S1-C7
    - P10-S2-C2
    - P10-S2-C3
    - P10-S2-C5
    - P10-S2-C6
    - P10-S3-C4
    - P10-S3-C9
    - P11-S1-C6
    - P11-S1-C10
    - P11-S2-C7
    - P11-S2-C8
    - P11-S2-C9
    - P11-S3-C11
    - P11-S4-C2
    - P11-S4-C3
    - P12-S1-C2
    - P12-S1-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    - TABLE-4-page-7-4
    - TABLE-5-page-8-5
    - TABLE-6-page-8-6
    - TABLE-7-page-9-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P2-S1-C2
      - P2-S3-C11
      - P3-S1-C5
      - P3-S1-C6
      imaging_provenance: []
      imaging_timing:
      - P1-S1-C6
      - P3-S2-C10
      outcome_timing:
      - P1-S1-C6
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P6-S1-C2
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C12
      - P8-S1-C7
      - P12-S1-C2
      dependent_variable_statement:
      - P5-S3-C12
      - P5-S4-C8
      - P6-S1-C11
      - P6-S1-C12
      limitations:
      - P11-S2-C10
      - P11-S2-C12
      - P11-S3-C5
      - P11-S3-C6
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S3-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: not_stated
    imaging_vs_outcome: concurrent
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S4-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P12-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C7
      - P2-S3-C11
      - P3-S1-C1
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C12
      - P6-S2-C6
      - P7-S1-C8
      - P8-S1-C4
      - P8-S1-C5
      - P10-S1-C1
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S3-C11
      - P11-S4-C2
      - P11-S4-C3
      - P12-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C7
      - P2-S3-C11
      - P3-S1-C3
      - P3-S2-C12
      - P8-S1-C4
      - P8-S1-C5
      - P10-S1-C1
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S3-C11
      - P11-S4-C2
      - P11-S4-C3
      - P12-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C6
      - P2-S3-C9
      - P3-S1-C2
      - P3-S2-C10
      - P5-S3-C4
      - P6-S1-C6
      - P6-S3-C3
      - P10-S1-C3
      - P11-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C6
      - P1-S1-C8
      - P3-S1-C11
      - P3-S1-C14
      - P3-S2-C3
      - P3-S2-C4
      - P5-S3-C12
      - P5-S4-C8
      - P6-S1-C11
      - P6-S1-C12
      - P6-S2-C10
      - P8-S1-C4
      - P8-S1-C5
      - P10-S1-C1
      - P11-S1-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C7
      - P2-S3-C11
      - P3-S1-C3
      - P3-S1-C4
      - P3-S2-C12
      - P3-S3-C1
      - P3-S3-C2
      - P3-S3-C4
      - P3-S3-C5
      - P4-S2-C8
      - P4-S2-C9
      - P5-S3-C11
      - P10-S1-C4
      - P11-S2-C9
      - P12-S1-C3
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
      pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
      review_sha256: b5611394bfedf767579836e4b653e74dbb2e1a9fb19a12af8a267a3dbc631c5a
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
      source_result: In the region of interest analysis, removal of participants who
        performed at chance for picture or written word judgements resulted in significant
        activation in the right temporal pole for picture judgements (t(9) = 2.1,
        P = 0.03). This finding was not significant in the full sample analysis described
        in P8-S1-C5.
      result_status: detected_only_at_relaxed_threshold
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the sensitivity analysis described
            in P8-S1-C7, which specifically tests the effect of removing chance-performing
            participants on the ROI results. The proposed core correctly identifies
            this as a distinct analysis from the main full-sample ROI analysis.
          source_ids:
          - P8-S1-C7
          - P6-S1-C12
        direction:
          answer: fits
          reason: The source states that significant activation was 'additionally
            found' in the right temporal pole for picture judgements after removing
            chance performers. The proposed core claims 'significant activation was
            found', which preserves the detected direction. The qualifier 'when participants
            who performed at chance were removed' is included, correctly framing the
            condition under which the detection occurred.
          source_ids:
          - P8-S1-C7
        construct:
          answer: fits
          reason: The exposure is 'picture judgements' (semantic animate-inanimate),
            the outcome is 'activation in the right temporal pole', and the method
            is fMRI. The population is patients with chronic Wernicke's aphasia. These
            align with the source text in P8-S1-C7 and the methods in P5-S2-C9.
          source_ids:
          - P8-S1-C7
          - P5-S2-C9
          - P3-S1-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the finding emerged
            only after removing participants who performed at chance. This is a material
            qualifier present in P8-S1-C7 ('Removal of the participants who performed
            at chance... made no change... with the exception that significant activation
            was additionally found...'). The limitation regarding low semantic demands
            (P11-S2-C10) is also included.
          source_ids:
          - P8-S1-C7
          - P11-S2-C10
        missing_material_caveat:
          answer: fits
          reason: The core includes the critical caveat that this is a sensitivity
            analysis (removal of chance performers) and the general limitation of
            low semantic demands. No other material caveats from the provided source
            window appear to be omitted that would change the interpretation of this
            specific ROI finding.
          source_ids:
          - P8-S1-C7
          - P11-S2-C10
      optional_pending:
      - Specific coordinates of the right temporal pole ROI
      - Exact P-value threshold used for the sensitivity analysis (implied P<0.05
        based on t-test output, but not explicitly stated as a threshold change in
        the text snippet)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates of the right temporal pole ROI
    - Exact P-value threshold used for the sensitivity analysis (implied P<0.05 based
      on t-test output, but not explicitly stated as a threshold change in the text
      snippet)
    normalizations: []
    analysis_identity:
      id: R020
      exposure:
        text: picture judgements
      outcome:
        text: activation in the right temporal pole
      analysis_label: Region of interest analysis (sensitivity)
      relation: sensitivity
      evidence_ids:
      - P8-S1-C7
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
        pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
        source_review: _compare/relationships-2026-11-16/review-current/Robson2014
        source_status_sha256: 7616af72b19325d10a71e23df1d6a73a2c7ed68fa60d9ddc3316c8bb4d755e90
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f5d2940614631a63f6b15c3356e69f2d1afcde5d096ea3a180dcccf9f56376ba
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4682d65463025052695772db6b15cd04dec754022a6bc4282b6cc110673945fc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C3
          page: 3
          text_layer_sha256: 4682d65463025052695772db6b15cd04dec754022a6bc4282b6cc110673945fc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and methods

          Participant diagnosis and lesions

          Twelve participants with chronic Wernicke’s aphasia [two female,

          mean age 70.1, standard deviation (SD) 8.7] and 12 age- and educa-

          tion-matched control participants (one female, mean age 71, SD 6.9)

          were recruited and provided written informed consent as approved by

          the Multicentre Research Ethics Committee NHS ethics committee.'
        anchor_text: 'Materials and methods

          Participant diagnosis and lesions

          Twelve participants with chronic Wernicke’s aphasia [two female,

          mean age 70.1, standard deviation (SD) 8.7] and 12 age- and educa-

          tion-matched control participants (one female, mean age 71, SD 6.9)

          were recruited and provided written informed consent as approved by

          the Multicentre Research Ethics Committee NHS ethics committee.'
        excluded_fragments: []
        image_sha256: 9f74772e8fa4e16783b410c10ce5f3fe99a8e69044217da9482e3de5fe6b6ba7
        transcription: 'Materials and methods


          Participant diagnosis and lesions


          Twelve participants with chronic Wernicke''s aphasia [two female, mean age
          70.1, standard deviation (SD) 8.7] and 12 age- and education-matched control
          participants (one female, mean age 71, SD 6.9) were recruited and provided
          written informed consent as approved by the Multicentre Research Ethics
          Committee NHS ethics committee'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'Removal of the

    participants who performed at chance for the picture or written

    word judgements made no change to signiﬁcance with the excep-

    tion that signiﬁcant activation was additionally found in the right

    temporal pole for the picture judgements [t(9) = 2.1, P = 0.03].'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
