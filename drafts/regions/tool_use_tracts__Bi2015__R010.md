---
id: tool_use_tracts
name: tool use tracts
kind: network
findings:
- id: f1
  target: tool_use_scores
  target_kind: impairment
  claim: Tool use scores significantly correlated with the lesion percentages and
    mean FA values of all 3 tool use tracts after controlling for performance on an
    intransitive action imitation task.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 86
    population: brain-damaged patients (majority stroke, some traumatic brain injury)
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
  - statistical power for each tract varied due to unequal numbers of patients having
    a lesion in a given tract
  - DTI is an indirect measure of real fiber connections and prone to errors in resolving
    fiber crossings
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap (percentage of damaged voxels)
    and mean fractional anisotropy (FA) of three white matter tracts identified via
    deterministic fiber tracking between tool-relevant cortical regions in healthy
    participants. analysis controlled for intransitive action imitation scores. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S2-C14, two-model agreement, human verification pending):
    . Eighty-six brain-damaged patients (65 males) were recruited

    for this study from the China Rehabilitation Research Center Original text-layer
    quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - proposed_concept:tool_use_scores
  citation: '@Bi2015'
  source_passages:
  - section: Original source P10-S4-C6
    page: 10
    quote: "After controlling for intransitive action imitation\nscores, tool use\
      \ scores still significantly correlated with the lesion\npercentages (partial\
      \ r: \x040.45 to \x040.35, p \x02 0.0009) and the mean\nFA values (partial r:\
      \ 0.26–0.30, p \x02 0.02) of all 3 tracts (Table 4)."
    supports: claim
  - section: Original source P10-S4-C5
    page: 10
    quote: 'Dissociation between tool use action and non-tool-use action

      To investigate whether the effects of the 3 tool use-related tracts

      were fully explained by their participation in action processing in

      general, we correlated tool use scores and tract integrity values,

      with patients’ scores on the intransitive action imitation task as a

      covariate.'
    supports: method
  - section: Original source P3-S2-C14
    page: 3
    quote: 'Eighty-six brain-damaged patients (65 males) were recruited

      for this study from the China Rehabilitation Research Center.'
    supports: sample
  - section: Original source P3-S2-C15
    page: 3
    quote: "We ad-\nopted the following inclusion criteria: had no previous brain\
      \ injury; had\nno other neurological or psychiatric disease such as alcohol\
      \ abuse or\nsevere depression; was at least 1 month post-onset (mean \x03 6\
      \ months,\nSD \x03 11, range: 1–86); and had enough language comprehension ability\n\
      to understand task instructions."
    supports: sample
  - section: Original source P3-S2-C17
    page: 3
    quote: "The majority\nsuffered from stroke (n \x03 74) and the others from traumatic\
      \ brain injury\n(n \x03 12)."
    supports: sample
  - section: Original source P5-S2-C13
    page: 5
    quote: 'For tract

      integrity, we used two types of measures based on structural imaging and

      diffusion imaging, respectively: with structural imaging, we measured

      the percentage of damaged voxels (number of voxels with lesion divided

      by total number of voxels on the tract); with diffusion imaging, we cal-

      culated the mean FA value (averaging the FA values of all voxels in the

      tract).'
    supports: method
  - section: Original source P13-S1-C4
    page: 13
    quote: 'An important caveat to consider is that in the patient analyses

      the statistical power for each tract varied due to the unequal

      numbers of patients having a lesion in a given tract.'
    supports: limitation
  - section: Original source P13-S1-C8
    page: 13
    quote: 'Finally, DTI is an indirect

      measure of real fiber connections and is especially prone to errors

      in resolving fiber crossings (Mori and van Zijl, 2002); therefore,

      convergent evidence from other imaging techniques is war-

      ranted.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Bi2015
  proposal_id: R010
  review_status_sha256: 8bb6f9974c9d26316055a116664d7621e774881210022a5c5a2c015af28d7695
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
        A/passages.json: 3a1a76aa8c9f3d7475606ac4e519b4252dcbb581bf844d5b0f2862337649585e
        A/raw.json: 7dfd2f9e8426b784dc9ed80aae7582c89196559182b74fea4e85740f46fdc68e
        A/source-units.json: 4576e890cbc3f5afe5a1946f0895f4d1c80e84243de1468bdf3bc51550bd5106
        A/full-source-units.json: a83a7839722da8593fcf12344cb92e18acc565a7c1d63ec139b70397abbee58e
        A/meta.json: bf2d27bef9ea4ee510dbcedeb12d83084494374658c5ad1e04aad08502e44ae1
        A/table-images/TABLE-1-page-5-1.png: f4c79f657c7e77c2a906a5e617705702c85d57b0ddbfd5a396b1fb5a7c280330
        A/table-images/page-11.png: 84d467add911d320e190d6d5a9d3f13fbe9f9428b979163a16523ec6977ba332
        A/table-images/page-6.png: 3ec881fe6e77a36dee588f6c63baf9c9798f033d186d90b094a51b65de9c8165
        A/table-images/TABLE-3-page-8-1.png: 02e95455401a87068605a4ea708d98ad2f4b532b171e5d6e07f041fdb2c933ea
        A/table-images/page-5.png: e673780cbd7ec6a69ecc011da766191e836d9a73f70df8a1243d018645830af0
        A/table-images/TABLE-4-page-11-1.png: 2a723189fc650a206f7883d548d02a74b24e4bc65d7ed7c50dfef29f2719a08b
        A/table-images/page-8.png: 0d953f11e713340534978396b488a350dc388dd4918f307121c723ceaa014df2
        A/table-images/TABLE-2-page-6-1.png: cb927958cb99dae6337f024ea7c7eee339361f30a54d0bae38b1bb85a6a5c4f7
        A/table-images/manifest.json: b63264efb4420ee88d2f981c8e9602be72e5333b9e45f60dc02d650c2d934a2a
        A/clauses/window-11/raw.json: a25bef249d972a3ac0e056dbd4e4f9adcf6fa0190d2e5e49d1e62ed9d9b338ac
        A/clauses/window-11/prompt.txt: bb60c7d982bc3583fab62e09a601654648967340b9e91bf1c14fd5ef57aa3093
        A/clauses/window-11/meta.json: 53c108b43e581f52b98054dd27a7da647e8d5e90e816795f011e9365be7a646d
        A/clauses/window-10/raw.json: 0bce7db80d473001d64c5104ca5d5a5385d94ce5e98fc2eaed8a20fa52be592b
        A/clauses/window-10/prompt.txt: 73997d2ab7e5a6bebe94e1e5b388a38c33baecbe46319d7d384f36e72668f908
        A/clauses/window-10/meta.json: 44dcde1d59fd51df08cc955243e13dd6ac0e1f890ad0b10c96ec84b97e5d9abe
        A/clauses/window-03/raw.json: 1e588b303eded431cbc82a09b71bba69f737901f382ae160076d39e97b67c2ee
        A/clauses/window-03/prompt.txt: 0ac8979f23b2b43c2e8f2a223652bfea61d9dae8b19fff336771951dda416c5a
        A/clauses/window-03/meta.json: d68dfd97d96ede146e55045077030e157278bfefaf170f5144264f63f5bd9cc7
        A/clauses/window-04/raw.json: da534917ffe49d5c9d555cd1ca1c87ac8838e7aad4236ebc4c6568c2e63f8b1b
        A/clauses/window-04/prompt.txt: 49d3b452bcd699d859ef289d6b9c9b9eeeb331de2afc8bbe0e53d0e2a65b02d6
        A/clauses/window-04/meta.json: 82521140d90e1d07e0c5c0612b216b99ca74684e689b2932140d2a2eb12bd6d4
        A/clauses/window-05/raw.json: 56c81b066c45b99221d5742a164cef0d3de0fe7950b98d4021188d38796729e1
        A/clauses/window-05/prompt.txt: fda53ca9bb44150c0cfea1a9623956dc7912a889695cfbf519e1437d48d1e766
        A/clauses/window-05/meta.json: 8340f2829ad9484bd2f3b2c8d5b4732eea64270e737acbfb65d1849492e21e53
        A/clauses/window-02/raw.json: 49a1f6a72923218d1ce2fbf63d5eb3fc862944bc2e1cb268047afc707603bd8a
        A/clauses/window-02/prompt.txt: fec4cd55bb131281f8fe94ca1990dba61a2d316d290df130ab1e0771b84b66ef
        A/clauses/window-02/meta.json: 1407f06f6d14e1b46166029a07e1280fb5a25ef6d572586cc55c68e2dd0f4b4e
        A/clauses/window-12/raw.json: daf84a585a4d73c6787c5ac13f041ef64c9296554526d83cacca6d3660766515
        A/clauses/window-12/prompt.txt: c550f37f5abd36c4ea63d376fada75cce01d98c73a3f21bd35b87156e69badf7
        A/clauses/window-12/meta.json: d2a953a7c9987b9c39e358a0f8617b2bdd3e1445ea690b5132f387cfda7b469e
        A/clauses/window-13/raw.json: f5604dd21179c438692bac819703eb14a62213fe8db70a6ef39f370c30ee8d2b
        A/clauses/window-13/prompt.txt: e2b2ebbd80286b681329fdb3cefb2194839ff3741839935dd84c246e155f0278
        A/clauses/window-13/meta.json: ddd68dbdd69d1999bb2d8b9794b23e71049a51605240e09830611c13e0936b0f
        A/clauses/window-09/raw.json: 419bcffb418d82f538d27ca81a9f40643c2e3d2fb0fa6ef8dd388a3587a9a6b4
        A/clauses/window-09/prompt.txt: e5e9039e9e3643fc0742f2fabe5e3af6ec564321ae79b6ba31d9a0f2d22baa73
        A/clauses/window-09/meta.json: 6de5df56fa2ef9df654cc6a06a5e61947b1e1a9244c303eec72eb9e88543aa29
        A/clauses/window-07/raw.json: d60cf1a8471d711da1a6d9a4bc30242a761d2272677f65745a462757dc460390
        A/clauses/window-07/prompt.txt: 460580ae1e1198060ec2e6cd35cee8967c4a0718be53bc856820ed50b4533e9f
        A/clauses/window-07/meta.json: db8228708661b08a64237399126ad3415f3e0037b9ad559053fbfbc0864b0b59
        A/clauses/window-01/raw.json: 1b5281f19fa7e3d5798e51aeb08546d81a4c359af1f7723de632dc27630c4e4d
        A/clauses/window-01/prompt.txt: 0eb6b170eb44d465e78bc79aec8ebcca4eb91bf4c083bfa49858a81ff768c91b
        A/clauses/window-01/meta.json: e0bc6da2f16a7b2815f4db9c7034b24639441b1782c0798c49cbed35b0188415
        A/clauses/window-06/raw.json: 2154c92dde75e65b232c24297861505cf1f8f3eb14d71899238c3ffc6cd8f10d
        A/clauses/window-06/prompt.txt: caacf1ea06cf103ec6787c8807994979ef553262d1dc2732ffeba006fa393f45
        A/clauses/window-06/meta.json: 57cfd13af75ab5b0c01db94d6d941a381a8132b599bd21a84e6aca1dd48656a2
        A/clauses/window-08/raw.json: 1ee39ff19dbe224f6cc693b9f89325ae6740aff97e25440fbd95ef1a897a75d4
        A/clauses/window-08/prompt.txt: 7780b02cf8a5f69f66df002e36b5af38ab52b1cf4f4c5c369a0f275e588c6d87
        A/clauses/window-08/meta.json: ada695faa179b1ca8311d924d174256556f77c23e49ce391cbe9d47674575d3d
        A/tables/TABLE-1-page-5-1/raw.json: b932dac4c3e0e469b03501f6c981be397c8baa8b07d1089fd9988f8ecb5ede31
        A/tables/TABLE-1-page-5-1/prompt.txt: 41ec817375ee74db35a0af5e6d6b66e9ed2b4faf3b3a77ebbd38f463751febcc
        A/tables/TABLE-1-page-5-1/meta.json: d971ba3b05cfe4d3958ff5d8b10dc1f4ecd8fd4fe9a343f62d3707c218c5549a
        A/tables/TABLE-4-page-11-4/raw.json: bcc16d2fd440414b67d48271faab2861a7411cce3caafc2a4902583d23b51d27
        A/tables/TABLE-4-page-11-4/prompt.txt: 7a5156859f04ef911fdb948cfd3c080e1f5655a553e5c3348b72a1645c952fab
        A/tables/TABLE-4-page-11-4/meta.json: e42003aa77b7042f6fd45a591b4fadc0b6b6af7127de3b4691200d135d7fd1d7
        A/tables/TABLE-3-page-8-3/raw.json: 7994dffe34c08e90080e8457d7843571b2838a2097983b830722f2072c433e08
        A/tables/TABLE-3-page-8-3/prompt.txt: ef7427c52b45f1d9b2dd0a593e7dc7f23de923fbf3ee6df60ef2fa500a3e180a
        A/tables/TABLE-3-page-8-3/meta.json: 11da552c14bc83de917e1ce38439dac3b85b559bb5949eccb3c174227062c148
        A/tables/TABLE-2-page-6-2/raw.json: ae382eb5f3608d9ce289f2957864896648f0c5f8b43961cd89a89cd6f4cba38d
        A/tables/TABLE-2-page-6-2/prompt.txt: d9444c698755adf8028bd90bdafc5c76fdf7b5e8b19eef7ea19d37bff38def36
        A/tables/TABLE-2-page-6-2/meta.json: 2f63ea254e650c10b2b21df92824e3b143b253bc10ae5b59aff5b9823c0d527f
        B/passages.json: 3a1a76aa8c9f3d7475606ac4e519b4252dcbb581bf844d5b0f2862337649585e
        B/raw.json: 69ebf38513f0911fc5625bfb4f62bbd88ae25d8fba2ddd5f01b949b45f54465d
        B/source-units.json: 4576e890cbc3f5afe5a1946f0895f4d1c80e84243de1468bdf3bc51550bd5106
        B/full-source-units.json: a83a7839722da8593fcf12344cb92e18acc565a7c1d63ec139b70397abbee58e
        B/meta.json: 7b843e2398cdb9b7b8900cd1c4ed8d0185d6be0d1b2d9fdf8818ac9a87f1ec51
        B/table-images/TABLE-1-page-5-1.png: f4c79f657c7e77c2a906a5e617705702c85d57b0ddbfd5a396b1fb5a7c280330
        B/table-images/page-11.png: 84d467add911d320e190d6d5a9d3f13fbe9f9428b979163a16523ec6977ba332
        B/table-images/page-6.png: 3ec881fe6e77a36dee588f6c63baf9c9798f033d186d90b094a51b65de9c8165
        B/table-images/TABLE-3-page-8-1.png: 02e95455401a87068605a4ea708d98ad2f4b532b171e5d6e07f041fdb2c933ea
        B/table-images/page-5.png: e673780cbd7ec6a69ecc011da766191e836d9a73f70df8a1243d018645830af0
        B/table-images/TABLE-4-page-11-1.png: 2a723189fc650a206f7883d548d02a74b24e4bc65d7ed7c50dfef29f2719a08b
        B/table-images/page-8.png: 0d953f11e713340534978396b488a350dc388dd4918f307121c723ceaa014df2
        B/table-images/TABLE-2-page-6-1.png: cb927958cb99dae6337f024ea7c7eee339361f30a54d0bae38b1bb85a6a5c4f7
        B/table-images/manifest.json: 65e91bfec04eaf8364d67e03aa1242e6998d5472729641a38a519ed9431f4faf
        B/clauses/window-11/raw.json: 8143e32de85a57cab59e2150a429a6d9d807f87efb39d53094039b2236dfbde2
        B/clauses/window-11/prompt.txt: bb60c7d982bc3583fab62e09a601654648967340b9e91bf1c14fd5ef57aa3093
        B/clauses/window-11/meta.json: bc4b71186b4d6927974a0c5838fc92f2821dec4b97e33b5a910eb184daa159c9
        B/clauses/window-10/raw.json: aff06dbd465277151a03522aa326f0e482002103c1fcb712c6d0faafa0ee84e7
        B/clauses/window-10/prompt.txt: 73997d2ab7e5a6bebe94e1e5b388a38c33baecbe46319d7d384f36e72668f908
        B/clauses/window-10/meta.json: f1751979101ac39b5f6a5a872201930dda8dfc494da29fb07b1d2e160a28652f
        B/clauses/window-03/raw.json: 7c3af5b131788e3ca3443b87b06746f7d2adc3558d7744604d600bbe1905b852
        B/clauses/window-03/prompt.txt: 0ac8979f23b2b43c2e8f2a223652bfea61d9dae8b19fff336771951dda416c5a
        B/clauses/window-03/meta.json: a3fbed9adc09d15aafb721176fb180eb3b085cceb804c687d6cf04b56429e814
        B/clauses/window-04/raw.json: a03bb009046ed529980bfcbcc04ce884325ffbd0363fa1e011c046f1b4af4e59
        B/clauses/window-04/prompt.txt: 49d3b452bcd699d859ef289d6b9c9b9eeeb331de2afc8bbe0e53d0e2a65b02d6
        B/clauses/window-04/meta.json: 033c868e4f84444b22ebdf4c2974a8619621c98bf4328ecead891369cb9ecee9
        B/clauses/window-05/raw.json: 9e024e87bcfbf10e45be8f61816d297acc204d28a4e41c0ae5f2a62707a07f0a
        B/clauses/window-05/prompt.txt: fda53ca9bb44150c0cfea1a9623956dc7912a889695cfbf519e1437d48d1e766
        B/clauses/window-05/meta.json: e76886dc043af782f3b6cf6fff2ffc0e7c493004d2c0d41a98fe873101a6ea56
        B/clauses/window-02/raw.json: 86ed0f2c4a6c9d5ae2949b49fee39628f6652d6adf079d9d9f6b229bdd2fb817
        B/clauses/window-02/prompt.txt: fec4cd55bb131281f8fe94ca1990dba61a2d316d290df130ab1e0771b84b66ef
        B/clauses/window-02/meta.json: b69f720c7ff71f0ed8e04c2482aaa7a3c0f3a64cb24af9da60d54284196479e2
        B/clauses/window-12/raw.json: eb80249c1b2c066c877d06b013689e8c13c1d1541a719968a04a10650448fa26
        B/clauses/window-12/prompt.txt: c550f37f5abd36c4ea63d376fada75cce01d98c73a3f21bd35b87156e69badf7
        B/clauses/window-12/meta.json: 049f768e1326dd1764b62d9b117602856797efb353acf3cba094b9b284e66d28
        B/clauses/window-13/raw.json: 41c6c0cb8bb4b19f933a09d8b0adc4fce4959351f885922e1062971c8a2f2cc8
        B/clauses/window-13/prompt.txt: e2b2ebbd80286b681329fdb3cefb2194839ff3741839935dd84c246e155f0278
        B/clauses/window-13/meta.json: 0a0c32c78fbacd51d32dad932d10bf2e3c0568843771e72717e7ccd1a2ca27bf
        B/clauses/window-09/raw.json: bed83b15706cd82d47f3cde5d8e1cd673224bcf5955dadbfcb5d24c43001b628
        B/clauses/window-09/prompt.txt: e5e9039e9e3643fc0742f2fabe5e3af6ec564321ae79b6ba31d9a0f2d22baa73
        B/clauses/window-09/meta.json: b6c00c9c74d762fc364aee511d4cf69746a697078196b425d8f98ee290bcfe35
        B/clauses/window-07/raw.json: eb129a68012c848d5c52f8a19339014fc9df19c321b4b47fcf115741d65d0c18
        B/clauses/window-07/prompt.txt: 460580ae1e1198060ec2e6cd35cee8967c4a0718be53bc856820ed50b4533e9f
        B/clauses/window-07/meta.json: 3be581168c46af956eef85f1917ca9ec680c75f37ec188cc37d0acfa77b223ef
        B/clauses/window-01/raw.json: 6d9dc0d63ad9a19ab9e3543976cf775637cd87db611ccb4126ad1c80de525946
        B/clauses/window-01/prompt.txt: 0eb6b170eb44d465e78bc79aec8ebcca4eb91bf4c083bfa49858a81ff768c91b
        B/clauses/window-01/meta.json: a4f6f7ea5dceb28de6f085a7bc12655417fd43a34dd6c4063e0dbd7aff20d0ca
        B/clauses/window-06/raw.json: 1b0bf7ec7bad5e61e35624bd6bbf7ee55a3209dabe128b799102878f8ae65028
        B/clauses/window-06/prompt.txt: caacf1ea06cf103ec6787c8807994979ef553262d1dc2732ffeba006fa393f45
        B/clauses/window-06/meta.json: cad2b37f9a96cfb5fd4803e745e2c487201e93966acb2760e51a6a583ef42dbb
        B/clauses/window-08/raw.json: 5d513eca629ff44378fcd8badf019364a7a040e44bfd91d314dcf7543e07ba03
        B/clauses/window-08/prompt.txt: 7780b02cf8a5f69f66df002e36b5af38ab52b1cf4f4c5c369a0f275e588c6d87
        B/clauses/window-08/meta.json: a5d8b65099f89ccabab23ccff876905f4d19caaad3379726266415dfea30d765
        B/tables/TABLE-1-page-5-1/raw.json: 52dbe82efae7b8fb5cc0665271da2fb77ed98741cbefaf5b16d64a83f4dba04a
        B/tables/TABLE-1-page-5-1/prompt.txt: 41ec817375ee74db35a0af5e6d6b66e9ed2b4faf3b3a77ebbd38f463751febcc
        B/tables/TABLE-1-page-5-1/meta.json: 13dc98294f0eb02a8ba4416a57b0491f312b345245399c556b22695793d41908
        B/tables/TABLE-4-page-11-4/raw.json: 56358fea08c2825a4be9a18ec8337816b9a0e3c97d40bd85e7c644bc5974cb81
        B/tables/TABLE-4-page-11-4/prompt.txt: 7a5156859f04ef911fdb948cfd3c080e1f5655a553e5c3348b72a1645c952fab
        B/tables/TABLE-4-page-11-4/meta.json: 0275be378c0e52748380f76f34807ec0ab9260944d32df6680a9811760e2b69b
        B/tables/TABLE-3-page-8-3/raw.json: 7c60bc8e44601b2d89a926a2c9a001ccddd6a6c2306696c2a31ee0c6dbe3d169
        B/tables/TABLE-3-page-8-3/prompt.txt: ef7427c52b45f1d9b2dd0a593e7dc7f23de923fbf3ee6df60ef2fa500a3e180a
        B/tables/TABLE-3-page-8-3/meta.json: 9ce41ec6d13dc7c5e5ab082b7de0051b5db4c1201b375f25a1569e5aee5ce71d
        B/tables/TABLE-2-page-6-2/raw.json: eca4aa4b237b6e76e95896027470db56e08e113e9bd4a3991dea6a15984dece1
        B/tables/TABLE-2-page-6-2/prompt.txt: d9444c698755adf8028bd90bdafc5c76fdf7b5e8b19eef7ea19d37bff38def36
        B/tables/TABLE-2-page-6-2/meta.json: 36ab55526492969315b8f8ab381fe4c9d1047494580ee63fe31600fcc59455d3
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
      pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
      source_review: _compare/relationships-2026-11-16/review-current/Bi2015
      source_status_sha256: de75f02b07c74aaf0b018461fbb45617227705e0bc8ee6454490fa11b57d2e5b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: Integrity of 3 tool use tracts
    outcome:
      text: Tool use scores
    analysis_label: Dissociation Analysis (Use vs General Action)
    relation: sensitivity
    evidence_ids:
    - P10-S4-C6
    qualifier_ids:
    - P10-S4-C5
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
      source_review: _compare/relationships-2026-11-16/review-current/Bi2015
      source_status_sha256: de75f02b07c74aaf0b018461fbb45617227705e0bc8ee6454490fa11b57d2e5b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C3
      - Result passage disposed without unit P5-S2-C10
      - Accounting without a linked unit P6-S2-C7
      - Accounting without a linked unit P6-S2-C8
      - Unaccounted source passage P6-S2-C8
      - Unaccounted source passage P6-S2-C7
      - Result passage disposed without unit P6-S2-C10
      - Result passage disposed without unit P6-S3-C3
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C6
      - Result passage disposed without unit P6-S3-C8
      - Result passage disposed without unit P6-S4-C2
      - Result passage disposed without unit P6-S4-C4
      - Result passage disposed without unit P6-S4-C5
      - Result passage disposed without unit P6-S4-C6
      - Result passage disposed without unit P6-S4-C7
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C6
      - Accounting without a linked unit P8-S1-C10
      - Accounting without a linked unit P8-S1-C11
      - Accounting without a linked unit P8-S2-C5
      - Result passage disposed without unit P9-S1-C1
      - Unaccounted source passage P8-S1-C11
      - Unaccounted source passage P8-S2-C5
      - Unaccounted source passage P8-S1-C10
      - Result passage disposed without unit P10-S2-C3
      - Result passage disposed without unit P10-S2-C4
      - Result passage disposed without unit P10-S2-C6
      - Result passage disposed without unit P10-S4-C3
      - Accounting without a linked unit P10-S4-C6
      - Accounting without a linked unit P11-S1-C3
      - Accounting without a linked unit P11-S1-C4
      - Accounting without a linked unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C5
      - Unaccounted source passage P10-S4-C6
      - Unaccounted source passage P12-S1-C1
      - Unaccounted source passage P11-S1-C3
      - Unaccounted source passage P11-S1-C4
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C11
      - Accounting without a linked unit P12-S1-C12
      - Result passage disposed without unit P12-S1-C6
      - Accounting without a linked unit P12-S1-C7
      - Result passage disposed without unit P12-S2-C3
      - Unaccounted source passage P12-S1-C12
      - Unaccounted source passage P12-S1-C7
      - Result passage disposed without unit P12-S3-C1
      - Result passage disposed without unit P12-S3-C12
      - Result passage disposed without unit P12-S3-C13
      - Result passage disposed without unit P12-S3-C4
      - Result passage disposed without unit P12-S3-C6
      - Result passage disposed without unit P12-S3-C7
      - Result passage disposed without unit P12-S3-C8
      - Result passage disposed without unit P12-S4-C1
      - Accounting without a linked unit P12-S4-C6
      - Accounting without a linked unit P12-S4-C7
      - Accounting without a linked unit P13-S1-C1
      - Accounting without a linked unit P13-S1-C11
      - Accounting without a linked unit P13-S1-C8
      - Accounting without a linked unit P13-S2-C1
      - Accounting without a linked unit P13-S2-C2
      - Unaccounted source passage P13-S1-C11
      - Unaccounted source passage P13-S2-C2
      - Unaccounted source passage P13-S2-C1
      - Unaccounted source passage P12-S4-C6
      - Unaccounted source passage P13-S1-C8
      - Unaccounted source passage P13-S1-C1
      - Unaccounted source passage P12-S4-C7
      unattached_null_or_qualifier_ids:
      - P6-S3-C3
      - P10-S4-C3
      - P10-S4-C6
      - P11-S1-C3
      - P11-S1-C4
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 274
      unselected_timing_passages:
      - P3-S2-C9
      - P3-S2-C15
      - P3-S2-C19
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C13
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
        source_id: P8-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
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
        source_id: P10-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C5
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
        source_id: P10-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S4-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S4-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S4-C14
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S4-C15
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P3-S1-C6
        - P3-S1-C8
        - P3-S4-C11
        - P3-S4-C13
        - P4-S1-C11
        - P4-S1-C12
        - P6-S2-C7
        - P6-S2-C8
        - P6-S2-C9
        - P6-S3-C4
        - P6-S3-C5
        - P6-S3-C6
        - P6-S3-C8
        - P6-S3-C9
        - P6-S4-C9
        - P8-S1-C10
        - P8-S1-C11
        - P8-S2-C5
        - P8-S2-C6
        - P9-S1-C1
        - P9-S1-C3
        - P9-S1-C4
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C8
        - P10-S1-C9
        - P10-S2-C7
        - P10-S2-C8
        - P10-S2-C10
        - P11-S1-C2
        - P11-S1-C3
        - P11-S1-C4
        - P12-S1-C12
        - P12-S1-C13
        - P13-S1-C2
        - P13-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P5-S3-C6
        - P5-S3-C7
        - P5-S3-C12
        - P5-S4-C3
        - P5-S4-C4
        - P6-S1-C13
        - P6-S1-C15
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C6
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S1-C8
        - P10-S1-C9
        - P10-S3-C5
        - P10-S3-C6
        - P10-S3-C7
        - P10-S3-C9
        - P10-S3-C10
        - P11-S1-C1
        - P11-S1-C2
        - P11-S1-C3
        - P11-S1-C4
        - P12-S1-C1
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C11
        - P12-S1-C12
        - P12-S1-C13
        - P13-S1-C1
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S1-C4
        - P3-S5-C4
        - P4-S5-C4
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P3-S2-C9
        - P3-S2-C11
        - P3-S2-C14
        - P3-S2-C15
        - P3-S2-C17
        - P3-S2-C18
        - P3-S2-C19
        - P3-S3-C3
        - P3-S3-C4
        - P4-S1-C16
        - P4-S2-C3
        - P4-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P2-S3-C2
        - P2-S3-C3
        - P3-S1-C7
        - P4-S2-C3
        - P4-S2-C7
        - P5-S3-C2
        - P5-S3-C6
        - P5-S3-C7
        - P5-S3-C12
        - P5-S4-C3
        - P5-S4-C4
        - P6-S1-C5
        - P6-S1-C13
        - P6-S1-C15
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C6
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C8
        - P10-S1-C9
        - P10-S2-C5
        - P10-S2-C6
        - P10-S2-C7
        - P10-S2-C8
        - P10-S2-C10
        - P10-S3-C6
        - P10-S3-C7
        - P10-S3-C9
        - P10-S3-C10
        - P11-S1-C1
        - P11-S1-C2
        - P11-S1-C3
        - P11-S1-C4
        - P12-S1-C6
        - P12-S1-C7
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S2-C9
        - P3-S2-C11
        - P3-S2-C14
        - P3-S2-C15
        - P3-S2-C17
        - P3-S2-C18
        - P3-S2-C19
        - P3-S3-C3
        - P3-S3-C4
        - P4-S1-C16
        - P4-S2-C3
        - P4-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-8-3
      - TABLE-4-page-11-4
      unlinked_tables:
      - TABLE-2-page-6-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S1
        - P2-S2
        - P4-S4
        - P4-S5
        - P5-S4
        - P6-S1
        - P6-S3
        - P6-S4
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S2
        - P11-S1
        - P12-S1
        - P12-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
      source_review: _compare/relationships-2026-11-16/review-current/Bi2015
      source_status_sha256: de75f02b07c74aaf0b018461fbb45617227705e0bc8ee6454490fa11b57d2e5b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Introduces the association between left hemisphere tracts and tool use
        deficits.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Introduces the association between left hemisphere tracts and tool concept
        processing.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about consistency with voxel-based mapping.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient aphasia classification demographics.
    - source_id: P3-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interrater agreement for tool use scoring.
    - source_id: P3-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interrater reliability for analytic scoring.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Tractography seed overlap details.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Number of node mask pairs determined.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Tract mask thresholding methodology.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of tracts passing thresholds.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2 for behavioral performance.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of patients vs healthy subjects (demographics/general performance).
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Error type percentages (descriptive).
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between scoring methods (reliability).
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance and loadings.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between PCA score and composite score.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance and loadings for 5 tasks.
    - source_id: P6-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between PCA score and composite score.
    - source_id: P6-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Number of effective tracts reaching threshold.
    - source_id: P6-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Average size of tracts.
    - source_id: P6-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Symmetry of tracts.
    - source_id: P6-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of intrahemisphere tracts.
    - source_id: P6-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: List of symmetric tracts.
    - source_id: P6-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: List of non-symmetric intrahemisphere tracts.
    - source_id: P6-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of interhemisphere tracts.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: List of homologous interhemisphere tracts.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: List of non-homologous interhemisphere tracts.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Voxel count variation in ROI spheres.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of WM size between ROI pairs (null result for demographics).
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between ROI WM size and tract size (null result).
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion distribution description.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of FA values between patients and healthy adults.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count per tract.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count per tract.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count per tract.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between tract size and lesion chance (null result).
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies 11 tracts negatively correlated with tool use scores in lesion
        analysis.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies 3 tracts with significant effects in FA analysis for tool
        use.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies the convergence of 3 tracts across lesion and FA analyses
        for tool use.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Association between lIFG-lIPL tract and kinematic scores.
    - source_id: P8-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P8-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 3 legend/notes.
    - source_id: P8-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P8-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Page footer.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Association between lIFG-lIPL tract and postural scores (marginal).
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Association between intrafrontal tracts and postural scores.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies 8 tracts negatively correlated with tool concept scores in
        lesion analysis.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies 9 tracts positively correlated with tool concept scores in
        FA analysis.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Summary of crucial tracts for tool use and tool conceptual processing.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Sensitivity result for tool use tracts controlling for whole brain GM.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Sensitivity result for tool concept tracts controlling for whole brain
        GM.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Sensitivity result for tool use tracts controlling for specific GM seeds.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Sensitivity result for tool concept tracts controlling for specific
        GM seeds.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Sensitivity result for tool use and concept tracts controlling for etiology.
    - source_id: P10-S2-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Sensitivity result for tool use and concept tracts in stroke patients
        only.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 12
      reason: VLSM association between left insula/putamen and tool use deficits.
    - source_id: P10-S2-C8
      disposition: represented
      result_indexes:
      - 13
      reason: VFSM association between left putamen and frontal lobe and tool use
        deficits.
    - source_id: P10-S2-C9
      disposition: represented
      result_indexes:
      - 14
      reason: Combined VLSM/VFSM overlap with left SLF for tool use.
    - source_id: P10-S3-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Combined VLSM/VFSM overlap with lATR, lIFOF, lSLF, and lUF for tool
        concepts.
    - source_id: P10-S3-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Sensitivity result for tool use tracts partialling out tool concept
        scores.
    - source_id: P10-S3-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Sensitivity result for tool concept tracts partialling out tool use
        scores.
    - source_id: P10-S4-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Sensitivity result for tool use tracts controlling for intransitive
        action imitation.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Sensitivity result for tool concept tracts controlling for animal and
        person concepts (lesion analysis).
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Sensitivity result for tool concept tracts controlling for animal and
        person concepts (FA analysis).
    unresolved_coverage:
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C9
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P10-S3-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S2-C3
    - P3-S3-C4
    - P3-S3-C12
    - P3-S4-C4
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C7
    - P5-S2-C10
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C8
    - P6-S2-C10
    - P6-S3-C3
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C8
    - P6-S4-C2
    - P6-S4-C3
    - P6-S4-C4
    - P6-S4-C5
    - P6-S4-C6
    - P6-S4-C7
    - P6-S4-C8
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C7
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C11
    - P8-S2-C2
    - P10-S1-C9
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C6
    - P10-S2-C10
    - P10-S3-C3
    - P10-S4-C3
    - P12-S1-C1
    - P12-S1-C3
    - P12-S1-C4
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C10
    - P12-S1-C11
    - P12-S1-C12
    - P12-S1-C13
    - P12-S2-C3
    - P12-S3-C1
    - P12-S3-C4
    - P12-S3-C6
    - P12-S3-C7
    - P12-S3-C8
    - P12-S3-C12
    - P12-S3-C13
    - P12-S4-C1
    - P12-S4-C5
    - P12-S4-C6
    - P12-S4-C7
    - P13-S1-C1
    - P13-S2-C1
    - P13-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-8-3
    - TABLE-4-page-11-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C8
      - P3-S2-C14
      recruited_sample:
      - P3-S2-C8
      - P3-S2-C14
      eligibility:
      - P3-S2-C15
      imaging_provenance:
      - P2-S2-C3
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      - P5-S1-C9
      - P7-S1-C13
      imaging_timing:
      - P3-S1-C3
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      outcome_timing:
      - P3-S1-C8
      - P5-S2-C11
      - P5-S2-C12
      - P5-S2-C13
      outcome_definition: []
      validation:
      - P2-S2-C4
      - P2-S3-C2
      - P3-S1-C8
      - P10-S2-C5
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C4
      - P2-S1-C11
      - P3-S1-C2
      - P3-S1-C7
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C13
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
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
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
      source_id: P10-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C5
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
      source_id: P10-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S4-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S4-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S4-C14
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S4-C15
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P3-S1-C6
      - P3-S1-C8
      - P3-S4-C11
      - P3-S4-C13
      - P4-S1-C11
      - P4-S1-C12
      - P6-S2-C7
      - P6-S2-C8
      - P6-S2-C9
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C8
      - P6-S3-C9
      - P6-S4-C9
      - P8-S1-C10
      - P8-S1-C11
      - P8-S2-C5
      - P8-S2-C6
      - P9-S1-C1
      - P9-S1-C3
      - P9-S1-C4
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C8
      - P10-S1-C9
      - P10-S2-C7
      - P10-S2-C8
      - P10-S2-C10
      - P11-S1-C2
      - P11-S1-C3
      - P11-S1-C4
      - P12-S1-C12
      - P12-S1-C13
      - P13-S1-C2
      - P13-S1-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: analysis_restrictions
      source_ids:
      - P5-S3-C6
      - P5-S3-C7
      - P5-S3-C12
      - P5-S4-C3
      - P5-S4-C4
      - P6-S1-C13
      - P6-S1-C15
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S1-C8
      - P10-S1-C9
      - P10-S3-C5
      - P10-S3-C6
      - P10-S3-C7
      - P10-S3-C9
      - P10-S3-C10
      - P11-S1-C1
      - P11-S1-C2
      - P11-S1-C3
      - P11-S1-C4
      - P12-S1-C1
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C11
      - P12-S1-C12
      - P12-S1-C13
      - P13-S1-C1
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S1-C4
      - P3-S5-C4
      - P4-S5-C4
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P3-S2-C9
      - P3-S2-C11
      - P3-S2-C14
      - P3-S2-C15
      - P3-S2-C17
      - P3-S2-C18
      - P3-S2-C19
      - P3-S3-C3
      - P3-S3-C4
      - P4-S1-C16
      - P4-S2-C3
      - P4-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P2-S3-C2
      - P2-S3-C3
      - P3-S1-C7
      - P4-S2-C3
      - P4-S2-C7
      - P5-S3-C2
      - P5-S3-C6
      - P5-S3-C7
      - P5-S3-C12
      - P5-S4-C3
      - P5-S4-C4
      - P6-S1-C5
      - P6-S1-C13
      - P6-S1-C15
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C8
      - P10-S1-C9
      - P10-S2-C5
      - P10-S2-C6
      - P10-S2-C7
      - P10-S2-C8
      - P10-S2-C10
      - P10-S3-C6
      - P10-S3-C7
      - P10-S3-C9
      - P10-S3-C10
      - P11-S1-C1
      - P11-S1-C2
      - P11-S1-C3
      - P11-S1-C4
      - P12-S1-C6
      - P12-S1-C7
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S2-C9
      - P3-S2-C11
      - P3-S2-C14
      - P3-S2-C15
      - P3-S2-C17
      - P3-S2-C18
      - P3-S2-C19
      - P3-S3-C3
      - P3-S3-C4
      - P4-S1-C16
      - P4-S2-C3
      - P4-S2-C7
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
      pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
      review_sha256: 8bb6f9974c9d26316055a116664d7621e774881210022a5c5a2c015af28d7695
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
      - P10-S4-C6
      source_result: 'After controlling for intransitive action imitation scores,
        tool use scores significantly correlated with the lesion percentages (partial
        r: -0.45 to -0.35, p < 0.0009) and the mean FA values (partial r: 0.26–0.30,
        p < 0.02) of all 3 tool use tracts.'
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R010) corresponds to the dissociation between
            tool use and non-tool-use action imitation described in P10-S4-C5 and
            P10-S4-C6. The proposed core correctly identifies the exposure (3 tool
            use tracts), outcome (tool use scores), and the specific covariate (intransitive
            action imitation).
          source_ids:
          - P10-S4-C5
          - P10-S4-C6
        direction:
          answer: fits
          reason: The source reports significant correlations (p < 0.0009 for lesion,
            p < 0.02 for FA) after adjustment. The proposed core states 'significantly
            correlated', which preserves the detected association. The direction of
            the relationship (integrity vs impairment) is consistent with the source's
            negative partial r for lesion percentage and positive for FA (where higher
            FA implies better integrity, though the source text in P10-S4-C6 lists
            positive r for FA, implying a positive correlation with performance scores,
            or potentially a sign convention difference, but the statistical significance
            is the key direction of 'association' vs 'no association'). The core correctly
            identifies a significant association.
          source_ids:
          - P10-S4-C6
        construct:
          answer: fits
          reason: 'The exposure is correctly identified as the integrity of 3 tool
            use tracts. The outcome is tool use scores. The patient measurement is
            correctly identified as template_lesion_overlap (lesion percentage on
            tracts) and diffusion (FA). The source P10-S4-C6 explicitly mentions ''lesion
            percentages'' and ''mean FA values''. The proposed core''s definition
            mentions ''Patient lesion overlap... and mean fractional anisotropy'',
            which is accurate. The method is described as LSM in the core, but the
            source describes it as partial correlation of tract integrity (lesion/FA)
            with behavior. While ''LSM'' might be a shorthand for Lesion-Symptom Mapping,
            the specific analysis here is a tract-level partial correlation, not a
            voxel-wise VLSM. However, the core''s ''definition'' field accurately
            describes the metric. The ''method'' field ''LSM'' is slightly imprecise
            as it usually refers to voxel-wise analysis, but the ''definition'' and
            ''claim'' are faithful to the tract-level analysis. Given the qualitative
            nature, the core captures the essential construct: tract integrity (lesion/FA)
            vs tool use performance, adjusted for non-tool action.'
          source_ids:
          - P10-S4-C6
          - P5-S2-C13
        qualifications:
          answer: fits
          reason: The core includes the qualification that the analysis controlled
            for intransitive action imitation scores. This is the critical qualifier
            for this specific 'dissociation' analysis. The limitations regarding statistical
            power and DTI limitations are also included.
          source_ids:
          - P10-S4-C5
          - P13-S1-C4
          - P13-S1-C8
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core includes the specific
            covariate used in this analysis (intransitive action imitation) and the
            general limitations of the study (power, DTI).
          source_ids:
          - P10-S4-C6
          - P13-S1-C4
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
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: at least 1 month post-onset
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1'
    analysis_identity:
      id: R010
      exposure:
        text: Integrity of 3 tool use tracts
      outcome:
        text: Tool use scores
      analysis_label: Dissociation Analysis (Use vs General Action)
      relation: sensitivity
      evidence_ids:
      - P10-S4-C6
      qualifier_ids:
      - P10-S4-C5
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
        source_review: _compare/relationships-2026-11-16/review-current/Bi2015
        source_status_sha256: de75f02b07c74aaf0b018461fbb45617227705e0bc8ee6454490fa11b57d2e5b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P10-S4-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2fe66d44eb6ee19fc4386358979cf173185f1041da7a882431cdf693f50a37dd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S4-C6
          page: 10
          text_layer_sha256: 2fe66d44eb6ee19fc4386358979cf173185f1041da7a882431cdf693f50a37dd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "After controlling for intransitive action imitation\nscores,\
          \ tool use scores still significantly correlated with the lesion\npercentages\
          \ (partial r: \x040.45 to \x040.35, p \x02 0.0009) and the mean\nFA values\
          \ (partial r: 0.26–0.30, p \x02 0.02) of all 3 tracts (Table 4)."
        anchor_text: "After controlling for intransitive action imitation\nscores,\
          \ tool use scores still significantly correlated with the lesion\npercentages\
          \ (partial r: \x040.45 to \x040.35, p \x02 0.0009) and the mean\nFA values\
          \ (partial r: 0.26–0.30, p \x02 0.02) of all 3 tracts (Table 4)."
        excluded_fragments: []
      P3-S2-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e6775b45ef248a69c72a362b4f8e9d927fc068a65b2ba7fc795f42f1a5999ed9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C14
          page: 3
          text_layer_sha256: e6775b45ef248a69c72a362b4f8e9d927fc068a65b2ba7fc795f42f1a5999ed9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Eighty-six brain-damaged patients (65 males) were recruited

          for this study from the China Rehabilitation Research Center.'
        anchor_text: 'Eighty-six brain-damaged patients (65 males) were recruited

          for this study from the China Rehabilitation Research Center.'
        excluded_fragments: []
        image_sha256: c6a702a3ae383796656add0dec0b581534c1dfcff01dc8d72df92593fceaeb7f
        transcription: '. Eighty-six brain-damaged patients (65 males) were recruited

          for this study from the China Rehabilitation Research Center'
      P3-S2-C15:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4e1cf8f74fa7c0507c453e833e03524179baae2af73286ac54c47554e8a5694b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C15
          page: 3
          text_layer_sha256: 4e1cf8f74fa7c0507c453e833e03524179baae2af73286ac54c47554e8a5694b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "We ad-\nopted the following inclusion criteria: had no previous\
          \ brain injury; had\nno other neurological or psychiatric disease such as\
          \ alcohol abuse or\nsevere depression; was at least 1 month post-onset (mean\
          \ \x03 6 months,\nSD \x03 11, range: 1–86); and had enough language comprehension\
          \ ability\nto understand task instructions."
        anchor_text: "We ad-\nopted the following inclusion criteria: had no previous\
          \ brain injury; had\nno other neurological or psychiatric disease such as\
          \ alcohol abuse or\nsevere depression; was at least 1 month post-onset (mean\
          \ \x03 6 months,\nSD \x03 11, range: 1–86); and had enough language comprehension\
          \ ability\nto understand task instructions."
        excluded_fragments: []
      P3-S2-C17:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 92c23d34ea64d5609408e5a75436fbcc74ac925ddac69889346f5203dcb50e27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1e58d9048af248b052691649f7d272092939f1cd415e643412403d0317a8320a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C17
          page: 3
          text_layer_sha256: 1e58d9048af248b052691649f7d272092939f1cd415e643412403d0317a8320a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The majority\nsuffered from stroke (n \x03 74) and the others\
          \ from traumatic brain injury\n(n \x03 12)."
        anchor_text: "The majority\nsuffered from stroke (n \x03 74) and the others\
          \ from traumatic brain injury\n(n \x03 12)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "After controlling for intransitive action imitation\nscores, tool use scores\
    \ still significantly correlated with the lesion\npercentages (partial r: \x04\
    0.45 to \x040.35, p \x02 0.0009) and the mean\nFA values (partial r: 0.26–0.30,\
    \ p \x02 0.02) of all 3 tracts (Table 4)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
