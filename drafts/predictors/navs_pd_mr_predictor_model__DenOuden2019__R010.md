---
id: navs_pd_mr_predictor_model
name: NAVS PD-MR prediction model
kind: predictor
findings:
- id: f1
  target: pd_mr
  target_kind: impairment
  claim: A model using ASPT-G and SCT-NC-C scores predicted membership of the morphosyntactically
    reduced speech group (PD-MR) with 87.3% success, 75% sensitivity, and 90.2% specificity.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: Right-handed native English speakers who suffered a left-hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: Mean 52.8 months since first stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The PD-MR group was defined by clinical judgment of descriptive-speech samples
    (Cookie-Theft picture from WAB-R)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A linear discriminant analysis model using the ASPT-G
    (grammatically well-formed responses in the Action Sentence Production Test) and
    SCT-NC-C (difference score between noncanonical and canonical sentence comprehension
    in the Sentence Comprehension Test) scores. The model was a secondary LDA conducted
    for comparison to the primary analysis; Three participants were excluded from
    this specific analysis due to missing data. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - not_transcribed:sample.n
    - proposed_concept:pd_mr
  citation: '@DenOuden2019'
  source_passages:
  - section: Original source P10-S1-C1
    page: 10
    quote: '

      improve classification (87.3% success), but the independently predic-

      tive variables were now identified as ASPT-G and SCT-NC-C, and only

      three participants had to be excluded.'
    supports: claim
  - section: Original source P10-S1-C2
    page: 10
    quote: 'Together these variables cor-

      rectly categorized 9/12 PD-MR participants (sensitivity 75%) and

      46/51 PD-Other participants (specificity 90.2%).'
    supports: claim
  - section: Original source P4-S1-C8
    page: 4
    quote: 'We therefore start our analysis with an investigation of corre-

      lations between NAVS subtests, and between these tests and general

      aphasia severity and lesion size.

      2

      |

      MATERIALS AND METHODS

      2.1

      | Participants

      Participants were 71 right-handed native speakers of English (mean

      age 59.6 years, SD 10.1, range 37–80 years; 23 females) who had

      suffered a left-hemisphere ischemic stroke (63 single and 8 multiple

      strokes; mean number of months since first stroke 52.8, SD 52.5,

      range 8–290 months; mean lesion size 93.5 cc, SD 86.0 cc, range

      0.16–365.4 cc).'
    supports: sample
  - section: Original source P6-S2-C3
    page: 6
    quote: 'Agrammatic pattern of morphosyntactic reduction (PD-MR):

      Omission and/or substitution of grammatical morphemes (verb

      inflection [tense and agreement errors]; plural markers), articles,

      and prepositions.

      2.'
    supports: claim
  - section: Original source P5-S1-C10
    page: 5
    quote: 'For this reason, we added a custom

      category to the scoring, ASPT-Code G (ASPT-G), which was only given

      in case the response sentence was grammatically well-formed, includ-

      ing appropriate inflection and morphology, but still not penalizing pho-

      nemic paraphasias.'
    supports: method
  - section: Original source P5-S3-C6
    page: 5
    quote: 'This yielded

      the SPPT-noncanonical minus canonical (NC-C) score and the SCT-NC-

      C score, respectively, that we used for our behavioral classification

      analysis.'
    supports: method
predictor_type: behavioural
short_definition: A linear discriminant analysis model using the ASPT-G (grammatically
  well-formed responses in the Action Sentence Production Test) and SCT-NC-C (difference
  score between noncanonical and canonical sentence comprehension in the Sentence
  Comprehension Test) scores.
assessment:
- Northwestern Assessment of Verbs and Sentences (NAVS)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: DenOuden2019
  proposal_id: R010
  review_status_sha256: 1fa4339f1c413311473eb3627ad12b70e43a8aba591777b2ab19664626778624
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
        A/passages.json: e885bf7c41be673f2385f82aaf038eb3fe18ab80a8bb39c56954eccfaeaa66e6
        A/raw.json: 696d01b539fa6a94e8e14a507e7f8995e1087498b8716f1cf881109fa3df81d6
        A/source-units.json: ab42b1e399957757d10d47eb074622dcdcca1aaa739a988d50244c9e64b0679d
        A/full-source-units.json: bdd9274bdfbe1ed4f5bfe068de6717596d333790c73e92a5ce5bb6dcf01dfd0a
        A/meta.json: 26c7aba50a6f4dd5fec0b39f9fc8218234762c14331878e4e59748a122760617
        A/table-images/page-14.png: a97dd737060eb325fdf0fa8c8f1978d76dd4208344167410ac2a54abb8987960
        A/table-images/TABLE-1-page-5-1.png: 0854c7e19b999c829c9eb9f334912c5b213e5c24c27fa6dae2cf89a15b017ee2
        A/table-images/page-12.png: 923a4835664acb4c57339c1b64f5b746dbd9e21315bdf4eab14d8f0218eadb1c
        A/table-images/TABLE-4-page-9-1.png: 6cc441c4109c977df9b5fc8a234bd04ef75a4fb518a0891c15cd83c0e9b1cb64
        A/table-images/page-10.png: f33b7b2cb34854f97f13eeec22364f3caf1d4fc6af7e24a540855b5812f35b2f
        A/table-images/page-11.png: a35bd2c8d8dc1767df3fa22a6398f2e5d8a891be089f4b77c0f4999ba06667f0
        A/table-images/TABLE-7-page-11-1.png: e92d49af269ec467cc3cf20b7e7feab43460612e05413257d33dd15de337b135
        A/table-images/TABLE-9-page-14-1.png: b086a3efe09ee304e081b67a2ff06122f05ebae8cd680056e9f3c3d7fdc957cb
        A/table-images/page-6.png: df5470c1747c4d94bf7b63462829bd401cb2b3dab55c58db1e8b3260e90bf657
        A/table-images/TABLE-3-page-8-1.png: 2f93902b1abf938ea0bc3288d3bb0a76db11103da43ec2e715a59e1e80e2b884
        A/table-images/page-5.png: c3e94a2f0affae16bcd91a36e08734c507f53351961118f615404fb8b117af26
        A/table-images/page-9.png: db7317cbee2fafe3788d72aaa44af926d2828a1038678a17d05d1bfe396a9d22
        A/table-images/page-8.png: d0c0bc0c8489e1abe6b79c8f0c474783e9683d6233ef2c2dfc8eb5ab3f20157a
        A/table-images/TABLE-8-page-12-1.png: bdb62c172aabbb4c9c05b5f207a88c5b2f9a9d0b2281a242ea8e6cbc00b7673d
        A/table-images/TABLE-2-page-6-1.png: 8964d037f8612d5548abb8e0c650fdef49601acda2b6c351ed4e1fb60ec70dae
        A/table-images/manifest.json: 6c99ecc23fa02e6dee56a52e084dc777910b0ba0a2f19ebc9a81fc953a3d3d8a
        A/table-images/TABLE-5-page-10-1.png: 93a392a73ab063afa16ae52a2de832190dee1da0efec1717d1594f78d0caec1a
        A/table-images/TABLE-6-page-10-2.png: 93a392a73ab063afa16ae52a2de832190dee1da0efec1717d1594f78d0caec1a
        A/clauses/window-11/raw.json: 92b4bf2d68ff06392a6236635bb42f54a09d128ebf74f7788fafafc48bce0c90
        A/clauses/window-11/prompt.txt: c704f3fd19518149f67613dc04295cacf080a5227c514de9215446c099d5ac28
        A/clauses/window-11/meta.json: 88e7496b3d295e585ef95e7da11a3de89058728d3266095265e31e4bc88bbacc
        A/clauses/window-10/raw.json: a54e0c1fb2dac21ade906201967aa70e356a413cd1853530dab4ea71a903ac1e
        A/clauses/window-10/prompt.txt: aeb5d149f5714099892b282c3b95cfbbdd56050a2c4a8f896359d3e8c7962741
        A/clauses/window-10/meta.json: d958b69ca34d7f3f3d7978da1817e84f81b9c489d620b424856d4357898557b6
        A/clauses/window-03/raw.json: 79703d05531e8de3e72058cea7b556ac55a82ffc04d8c6cbaa011cbbcdecc2ef
        A/clauses/window-03/prompt.txt: 527a5cf6db61ab79e5a3255f53b4c6f0d7fa25cf6e6563a71b50b5b131e303e1
        A/clauses/window-03/meta.json: 7f5b7d1018b116c869ba0d102963d1a32952474484993c5aa9b0b28fc4db8af1
        A/clauses/window-04/raw.json: 11fa5c74f5b19225091d68cea8dbdadd1a7025469c8759959feb66764c636669
        A/clauses/window-04/prompt.txt: 48493ce0212a3ebb756f9134e257585a84975a04cf3d19fca66b33ee9baa7478
        A/clauses/window-04/meta.json: 74ec05640f17f7100b9405dbf0732b166af9c5ba1a6ec7a5383d07771d079c38
        A/clauses/window-05/raw.json: 5a6643591f3389f6fc099a1078de3008c8d3b35258e90f64c144fce5fca95eb1
        A/clauses/window-05/prompt.txt: 7ae1f79e81fcb55e7a92ce2b409b0e4b30554e48cfc9f27e993d76d8d6f542c8
        A/clauses/window-05/meta.json: a663f56e21d3c29f1e86bd05c0fe51741aaf04bffd1092f0ac188a2f67aa88be
        A/clauses/window-02/raw.json: f88437e8bf82d88b94f4f09bfc8dec2542d2d1db679eec34a1e01c46cbd68747
        A/clauses/window-02/prompt.txt: 7482a6af607b14bff940543030ce084662517fb6dca5392df51a63dc0680a3f5
        A/clauses/window-02/meta.json: 1a558e733ef27ab944b29c635672c0d2d8f396c2d42b37ec8a880824dea746e4
        A/clauses/window-12/raw.json: b12cef98b3d798ce95192f2cc533f7d5e7c25119364ad5798fa98fafbd5ac956
        A/clauses/window-12/prompt.txt: 20c60259bf2016e5712cb166f9c86c2608961262f947f797c1373a8bece22507
        A/clauses/window-12/meta.json: e6dbb52ebe4228fe798906fb2ea7d47709210a16a9b20bf5e5274c941f70688f
        A/clauses/window-13/raw.json: 7d5f4f910cb463eae842ad9ff2b1994f75853bf29b8dcff3ac1dc1b31636b2d3
        A/clauses/window-13/prompt.txt: e66d222dd814cc9e49cec837156b18d1708999c9bd563b7730baeade0da0f361
        A/clauses/window-13/meta.json: 70648ab9da9954ade07210ad48f25f63ea668143da653e2c49de25d75e028e1b
        A/clauses/window-14/raw.json: c25db6f7f002b87bdbe056dbb2fa0f976398e069800bb82002240a42507d819c
        A/clauses/window-14/prompt.txt: e6370bc19eb1c1fb8a6d53b5673d378650c84374c96e588a3478dd36d43e50f1
        A/clauses/window-14/meta.json: a9d1fa314bcf065951b3590146d944908e297e9ecb70fd4543c77df6e49ad966
        A/clauses/window-09/raw.json: bf7f00c687417e15af31b76273423ea9dab26dcb386bff566b71dabb9fb65218
        A/clauses/window-09/prompt.txt: 064186549727cba265a1c242287819d5717b4b4278897c5a3294a3c1407d6877
        A/clauses/window-09/meta.json: 36150d9ea54810ecb5ab82fd6c1954f00e2d2b316b1aadb0a058955ba8378980
        A/clauses/window-07/raw.json: e2efc4c60303ac83543dad0e3c3e64dace80d86dd2e9a087f990366bb0d6923a
        A/clauses/window-07/prompt.txt: a91eb6f4359bd64052003e7c7cb343257ce1fa240dd495ccb94da345ce6fda56
        A/clauses/window-07/meta.json: c31280974ab0acfd8f46683ee7ccb4ee2d51578ef79cbaad669da66acdda17d0
        A/clauses/window-01/raw.json: 6d8b10be1affb6c432ad6c10c6d247fa29331c40fc0e58ada237ae776b4e6153
        A/clauses/window-01/prompt.txt: d0d7954b569415decd402ae6e1009f648399e9f05974db7c4c27ca36daf3b4b3
        A/clauses/window-01/meta.json: a385fc62cc6f13788b60be388098009ed330e7e125b6bc46610202ba943fd0e9
        A/clauses/window-06/raw.json: 42c5e194a78a9eb42c65d3758273482707c5d2fc0273c21f57d3018edd18a3eb
        A/clauses/window-06/prompt.txt: 5a663a832cc7b580dec63b7039d5fcd360d09ad44bf6765638cab8cd6cb9b427
        A/clauses/window-06/meta.json: 2e568b060afc0a027a0ef3b7104a99b9bdaf1db3e800f96e01379eaa65a581b3
        A/clauses/window-08/raw.json: 5d4a7ff954d9153354b04391c034e6b5087b35042b5a622c785b0633e7447e80
        A/clauses/window-08/prompt.txt: 9265d5c77b1a40c736b47fb4ea67d8c52288baf410e7de3787b961ee2ff71e81
        A/clauses/window-08/meta.json: 7fce29ce353782ed7b51fffc32bda5cc5c5a37b7e296c912fcadc4b1a0ace5ad
        A/tables/TABLE-1-page-5-1/raw.json: 2520088ca2cb33bf8033d1f18832a8c6ef6828ef4f365889c44259c9b7924540
        A/tables/TABLE-1-page-5-1/prompt.txt: 9096dc3ae51c1e2049b729960aacb25e8835e8980cc46447a3b0e2a3f3ee99ba
        A/tables/TABLE-1-page-5-1/meta.json: 5450d4d71e7857c476f64cce936d33cb96740ecd73872ea4740a8817ca187688
        A/tables/TABLE-3-page-8-3/raw.json: 23a0636e7b4d56614b80ef82d51b2ea1f7847b5d770ef58775112c2f1e92d1c5
        A/tables/TABLE-3-page-8-3/prompt.txt: f9ca52323a65baac5e4ab9aa39065ad1f1ee785ebc9a72032e77203336aeb553
        A/tables/TABLE-3-page-8-3/meta.json: 2d28962d2a0fae4ad7f57e278808de510a155c7d2b29a391acdfb2935018245b
        A/tables/TABLE-2-page-6-2/raw.json: 4fafc1f271f1bdf6c3accc4b336771cf99222f2751b5bd85fb45e9b9587f3b73
        A/tables/TABLE-2-page-6-2/prompt.txt: eb91318655cd7a86d4241cfbec7b8be23a2b9b3f09162cad20564b4ebb74ee3c
        A/tables/TABLE-2-page-6-2/meta.json: 6b1657a3189635071a81117211d319cbe657fae888a7f84f9a05ac9ea7ea4710
        A/tables/TABLE-9-page-14-9/raw.json: 6c965ec6644c810abf594ae33efa96deebf9048fd378d55ce769b3c29a10882f
        A/tables/TABLE-9-page-14-9/prompt.txt: df6b9a92b2e33038e435c891753e49065279f0bfdc0b5c67e835301b1bda6d6d
        A/tables/TABLE-9-page-14-9/meta.json: 0211e51f441311c20546b204280111005f531d57fa37fee5857515c3b5f6f37d
        A/tables/TABLE-7-page-11-7/raw.json: b666c2f41d17f81075a41e86e2b014d35002824e68cb97c2b57f8ac8b8875a3c
        A/tables/TABLE-7-page-11-7/prompt.txt: a14e0523b3b22c2641e66cc119216559e62a035dee7bf6cb57df0e7937abb04f
        A/tables/TABLE-7-page-11-7/meta.json: 6b8c0566fad07d70efc005cf79106b006dbc93a4c825fe596faecb37b889a974
        A/tables/TABLE-5-page-10-5/raw.json: 56b04efb186a2b6167ac3303a20cb4848ba7ae278437dcc721eb13056d6a4d0d
        A/tables/TABLE-5-page-10-5/prompt.txt: 003dffb8259b7143fc01c89b85f2209c02c2c4c7164c215057280f20191b38b0
        A/tables/TABLE-5-page-10-5/meta.json: 2c58bd94a723c684d010695a4a406f5816cbf4c7b7a93c4b91b0c37beb36d251
        A/tables/TABLE-8-page-12-8/raw.json: 5af0a5f2cc67ecff05c1d04e4e9ae211155848bfddb40f4b04ecff271781935a
        A/tables/TABLE-8-page-12-8/prompt.txt: 932c11a10aa070adf1f97e95bfad1bea8068383e169e869c94b75b072f65dad8
        A/tables/TABLE-8-page-12-8/meta.json: b0ad202802993c4ae47608ab1df980ef33f5cba31edb92639497b60fbb19a1eb
        A/tables/TABLE-4-page-9-4/raw.json: 7a3c3e7cb39a7fed3032468b22738048432a60717723117c519feaf731d322d8
        A/tables/TABLE-4-page-9-4/prompt.txt: cf0a5727de6cf3dd0f1878eff4155810500ab3f27195e7684d9b22d7291621fc
        A/tables/TABLE-4-page-9-4/meta.json: 435bc0d2996bb6be6b17edddea0ccb49ce712b53887ff4422771fdebdf262a9c
        A/tables/TABLE-6-page-10-6/raw.json: 2f34661c345e83f531c588a19d57f18e74efca79dcf9b3703284694e34f8e3e1
        A/tables/TABLE-6-page-10-6/prompt.txt: ffc10332a6bde1cec68f45447b8e0cc135192a8e829cc5b1be13e1d953caea9f
        A/tables/TABLE-6-page-10-6/meta.json: 5ce2e6a8a7f390624fc544e86c0e71b00f7cfc02815f767bcc0fdd187057fefe
        B/passages.json: e885bf7c41be673f2385f82aaf038eb3fe18ab80a8bb39c56954eccfaeaa66e6
        B/raw.json: db5aa5c01b3162268d8c672295a571afe3cd36ed3eebc419a349ff891d6f1650
        B/source-units.json: ab42b1e399957757d10d47eb074622dcdcca1aaa739a988d50244c9e64b0679d
        B/full-source-units.json: bdd9274bdfbe1ed4f5bfe068de6717596d333790c73e92a5ce5bb6dcf01dfd0a
        B/meta.json: 82e17c385e869fb0d0990711f05fa84bafe1362629102dddb59dae32c1e41831
        B/table-images/page-14.png: a97dd737060eb325fdf0fa8c8f1978d76dd4208344167410ac2a54abb8987960
        B/table-images/TABLE-1-page-5-1.png: 0854c7e19b999c829c9eb9f334912c5b213e5c24c27fa6dae2cf89a15b017ee2
        B/table-images/page-12.png: 923a4835664acb4c57339c1b64f5b746dbd9e21315bdf4eab14d8f0218eadb1c
        B/table-images/TABLE-4-page-9-1.png: 6cc441c4109c977df9b5fc8a234bd04ef75a4fb518a0891c15cd83c0e9b1cb64
        B/table-images/page-10.png: f33b7b2cb34854f97f13eeec22364f3caf1d4fc6af7e24a540855b5812f35b2f
        B/table-images/page-11.png: a35bd2c8d8dc1767df3fa22a6398f2e5d8a891be089f4b77c0f4999ba06667f0
        B/table-images/TABLE-7-page-11-1.png: e92d49af269ec467cc3cf20b7e7feab43460612e05413257d33dd15de337b135
        B/table-images/TABLE-9-page-14-1.png: b086a3efe09ee304e081b67a2ff06122f05ebae8cd680056e9f3c3d7fdc957cb
        B/table-images/page-6.png: df5470c1747c4d94bf7b63462829bd401cb2b3dab55c58db1e8b3260e90bf657
        B/table-images/TABLE-3-page-8-1.png: 2f93902b1abf938ea0bc3288d3bb0a76db11103da43ec2e715a59e1e80e2b884
        B/table-images/page-5.png: c3e94a2f0affae16bcd91a36e08734c507f53351961118f615404fb8b117af26
        B/table-images/page-9.png: db7317cbee2fafe3788d72aaa44af926d2828a1038678a17d05d1bfe396a9d22
        B/table-images/page-8.png: d0c0bc0c8489e1abe6b79c8f0c474783e9683d6233ef2c2dfc8eb5ab3f20157a
        B/table-images/TABLE-8-page-12-1.png: bdb62c172aabbb4c9c05b5f207a88c5b2f9a9d0b2281a242ea8e6cbc00b7673d
        B/table-images/TABLE-2-page-6-1.png: 8964d037f8612d5548abb8e0c650fdef49601acda2b6c351ed4e1fb60ec70dae
        B/table-images/manifest.json: 2fbe36d275ccbbb48efe1487030d80b12874553bdc326bb28a83b01cab80c0fb
        B/table-images/TABLE-5-page-10-1.png: 93a392a73ab063afa16ae52a2de832190dee1da0efec1717d1594f78d0caec1a
        B/table-images/TABLE-6-page-10-2.png: 93a392a73ab063afa16ae52a2de832190dee1da0efec1717d1594f78d0caec1a
        B/clauses/window-11/raw.json: 75700bf1cf344c12a36c69e8d8a4cc8d9dbd1cb690ec56ec008d70e52813c242
        B/clauses/window-11/prompt.txt: c704f3fd19518149f67613dc04295cacf080a5227c514de9215446c099d5ac28
        B/clauses/window-11/meta.json: d1e18b47e48c11962d55c189d1198f94247dcd8de9875f1940b8af2b0b82cceb
        B/clauses/window-10/raw.json: 7759018dde2434db1c4aa516cb40e283a4de92000d35f3e15a3354a4f7453417
        B/clauses/window-10/prompt.txt: aeb5d149f5714099892b282c3b95cfbbdd56050a2c4a8f896359d3e8c7962741
        B/clauses/window-10/meta.json: d8c56fa5819057fdcc1fc06225bdfcd0fd252c7f11dc393cbd2afdd3f53c3aee
        B/clauses/window-03/raw.json: 9b3c1f8a0cb361e4120e1599eddeb15094a07c2fbfac92afe3c84d9ddaa56add
        B/clauses/window-03/prompt.txt: 527a5cf6db61ab79e5a3255f53b4c6f0d7fa25cf6e6563a71b50b5b131e303e1
        B/clauses/window-03/meta.json: eebd7465817695ecf9f5eecad706c29d025e2b41bf78eb15f4e8e8f8f99270af
        B/clauses/window-04/raw.json: 9183becbd25887dacad7fe17487b4895020d717cdbaf32158028e3274b899ee5
        B/clauses/window-04/prompt.txt: 48493ce0212a3ebb756f9134e257585a84975a04cf3d19fca66b33ee9baa7478
        B/clauses/window-04/meta.json: 8ada5bf6e7146e2154c44df374211db36ff593b160bffd0543447015a2d39c45
        B/clauses/window-05/raw.json: a55004ad5513236f811d7c8913fd4ed2a177be4a8bce2d6cab3baeb53f3cd3d3
        B/clauses/window-05/prompt.txt: 7ae1f79e81fcb55e7a92ce2b409b0e4b30554e48cfc9f27e993d76d8d6f542c8
        B/clauses/window-05/meta.json: 394c5f4d06986a9f42cb92bb6f4bea92950e50010d95972ba5916957e30e14a5
        B/clauses/window-02/raw.json: cb3e8e793fc3cc40c2a365862b16ae2aa28f12aa6e087c2aeb825dbb36820ac2
        B/clauses/window-02/prompt.txt: 7482a6af607b14bff940543030ce084662517fb6dca5392df51a63dc0680a3f5
        B/clauses/window-02/meta.json: f50f83a717970e4b41299954900909e9632fb5ab69e6726c7d0c082589eb46e1
        B/clauses/window-12/raw.json: 81c15615362313fbe5f4de65f22b769b45c21acc5069d4c1e2d0ecc571dbcd75
        B/clauses/window-12/prompt.txt: 20c60259bf2016e5712cb166f9c86c2608961262f947f797c1373a8bece22507
        B/clauses/window-12/meta.json: 882d9e10bce4a50134fb20955109f1de3b9be36bd09dfd07235d1d96091fe496
        B/clauses/window-13/raw.json: fa9fa23787fe049419d89a11bf0f493b1995deff994c00adca499a6b0ff39d04
        B/clauses/window-13/prompt.txt: e66d222dd814cc9e49cec837156b18d1708999c9bd563b7730baeade0da0f361
        B/clauses/window-13/meta.json: a4f7a6a0f3a6b326890c15fe3893ef3b53c9ee852d9de865db27f74f33e662b1
        B/clauses/window-14/raw.json: c25db6f7f002b87bdbe056dbb2fa0f976398e069800bb82002240a42507d819c
        B/clauses/window-14/prompt.txt: e6370bc19eb1c1fb8a6d53b5673d378650c84374c96e588a3478dd36d43e50f1
        B/clauses/window-14/meta.json: a4e923a034bce5b35b81e064c5e3e6ef5624c843e85499e7a6d2f6de91b3b755
        B/clauses/window-09/raw.json: 3336733902ff91794f73ffc6d3bf0b75fc2d519158b6d97160eb0148307e23bd
        B/clauses/window-09/prompt.txt: 064186549727cba265a1c242287819d5717b4b4278897c5a3294a3c1407d6877
        B/clauses/window-09/meta.json: 471ea12c1d6337460bb02fe60f6c14d6881cb8ea7c9b592458e891b6c7ad9eba
        B/clauses/window-07/raw.json: b1bd73d55a2dfb091cfb9b74e5cd672e4b73de3c9967d700629c28628353294e
        B/clauses/window-07/prompt.txt: a91eb6f4359bd64052003e7c7cb343257ce1fa240dd495ccb94da345ce6fda56
        B/clauses/window-07/meta.json: 4d622549ee8df0e8be2364f241b739cbe5ec0ede61252f66354a51d0acdaec81
        B/clauses/window-01/raw.json: 6ff12085e82f78355daf700a9fc40a2d608128eeeef1b065d4a9e1e14ca01fff
        B/clauses/window-01/prompt.txt: d0d7954b569415decd402ae6e1009f648399e9f05974db7c4c27ca36daf3b4b3
        B/clauses/window-01/meta.json: fb2ae61e50d446c7e0ce21c53000ab96f3a18ac2bdcf030e38969c9b9e2a42c2
        B/clauses/window-06/raw.json: 9d0b853c22166f65b3186146c1f9d014c5ec53eac8a9a68be89a4df8503a1107
        B/clauses/window-06/prompt.txt: 5a663a832cc7b580dec63b7039d5fcd360d09ad44bf6765638cab8cd6cb9b427
        B/clauses/window-06/meta.json: 30b484b85358263f9048016d3cd339f3e6d496b7abd01d010e6758e56a6abe14
        B/clauses/window-08/raw.json: 1c9cc19bd800d9db2401d2243f329811cca269eec45b9f871d36b0f84224599b
        B/clauses/window-08/prompt.txt: 9265d5c77b1a40c736b47fb4ea67d8c52288baf410e7de3787b961ee2ff71e81
        B/clauses/window-08/meta.json: 065c9264d75a02f2321226f8050b3e49641fca0c79d78a76033ac75f70926a9d
        B/tables/TABLE-1-page-5-1/raw.json: 2520088ca2cb33bf8033d1f18832a8c6ef6828ef4f365889c44259c9b7924540
        B/tables/TABLE-1-page-5-1/prompt.txt: 9096dc3ae51c1e2049b729960aacb25e8835e8980cc46447a3b0e2a3f3ee99ba
        B/tables/TABLE-1-page-5-1/meta.json: fdcd10a7b8ecd3cc8b46718ee1d06750a31ffa42f22d7de695ed3eb670e16c53
        B/tables/TABLE-3-page-8-3/raw.json: 1d157220d92bb28776ca4c30b8c90b37efe84b2562c6ccbea3f22b728d2f1997
        B/tables/TABLE-3-page-8-3/prompt.txt: f9ca52323a65baac5e4ab9aa39065ad1f1ee785ebc9a72032e77203336aeb553
        B/tables/TABLE-3-page-8-3/meta.json: 80a0162501a029d564266052bf30b7fad6824b7c40b0849a8e6f152d36b07dd8
        B/tables/TABLE-2-page-6-2/raw.json: 666a1269425bc02ab7c450b752b2b1e5a9fe2d1aa3fe0a7f68b1e9e35f2e4fe2
        B/tables/TABLE-2-page-6-2/prompt.txt: eb91318655cd7a86d4241cfbec7b8be23a2b9b3f09162cad20564b4ebb74ee3c
        B/tables/TABLE-2-page-6-2/meta.json: e107c9ea01544f76ca604c31ab525ae94f4994874925b2c7661555759329d8cd
        B/tables/TABLE-9-page-14-9/raw.json: 1db603a21f33bd34b274689a586625aa2b5a6c7da0eb849930eb9b4dc738dab1
        B/tables/TABLE-9-page-14-9/prompt.txt: df6b9a92b2e33038e435c891753e49065279f0bfdc0b5c67e835301b1bda6d6d
        B/tables/TABLE-9-page-14-9/meta.json: 78078aa073a1abdd38d6806c95509804603dfa1133c192c482ebbc764c38af1a
        B/tables/TABLE-7-page-11-7/raw.json: c769c8cf3f2ebafc3bc9d1349071ea671e9baff8d8f077491c77b22c1d2a74d9
        B/tables/TABLE-7-page-11-7/prompt.txt: a14e0523b3b22c2641e66cc119216559e62a035dee7bf6cb57df0e7937abb04f
        B/tables/TABLE-7-page-11-7/meta.json: 04f5b06c7e73ffa30285a66f19b6a0c5b16b47a0979bd7aefe0b4550db411f10
        B/tables/TABLE-5-page-10-5/raw.json: 6d5fe1d0eb165a8134d4ad8822e32f2e04ed36c34b22f8ac21f4bb99632090a7
        B/tables/TABLE-5-page-10-5/prompt.txt: 003dffb8259b7143fc01c89b85f2209c02c2c4c7164c215057280f20191b38b0
        B/tables/TABLE-5-page-10-5/meta.json: 96063246f9deee2fac1af7aaa93a55bdfa16c1ffab58ccadfe9e82a28f7ddb0d
        B/tables/TABLE-8-page-12-8/raw.json: 5af0a5f2cc67ecff05c1d04e4e9ae211155848bfddb40f4b04ecff271781935a
        B/tables/TABLE-8-page-12-8/prompt.txt: 932c11a10aa070adf1f97e95bfad1bea8068383e169e869c94b75b072f65dad8
        B/tables/TABLE-8-page-12-8/meta.json: e08d2d76166806091afa0a1283fe8a6a4da3114b0487bc858e2aa03eafe97a6e
        B/tables/TABLE-4-page-9-4/raw.json: caa1a497ee57d4b7f4018abc4ea421acc3bb82cd1e8c409f28e9379093168b35
        B/tables/TABLE-4-page-9-4/prompt.txt: cf0a5727de6cf3dd0f1878eff4155810500ab3f27195e7684d9b22d7291621fc
        B/tables/TABLE-4-page-9-4/meta.json: 8cf99ad303f5d34d6407e80549fc3b922618b0f92264640f827440ce45438f60
        B/tables/TABLE-6-page-10-6/raw.json: 2f34661c345e83f531c588a19d57f18e74efca79dcf9b3703284694e34f8e3e1
        B/tables/TABLE-6-page-10-6/prompt.txt: ffc10332a6bde1cec68f45447b8e0cc135192a8e829cc5b1be13e1d953caea9f
        B/tables/TABLE-6-page-10-6/meta.json: 42871f686761d541f6bc29f9986c8317bcc495f1d7e9abadc93e81c846b6e0ed
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
      pdf_sha256: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
      source_review: _compare/relationships-2026-11-16/review-current/DenOuden2019
      source_status_sha256: fa4cc1608338da5bdf2c3b2075b762215754fce05d2dc97e45591a7fbeff94ca
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: ASPT-G and SCT-NC-C scores
    outcome:
      text: morphosyntactically reduced speech (PD-MR group membership)
    analysis_label: Linear Discriminant Analysis (PD-MR with ASPT-G)
    relation: performance
    evidence_ids:
    - P10-S1-C1
    - P10-S1-C2
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
      pdf_sha256: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
      source_review: _compare/relationships-2026-11-16/review-current/DenOuden2019
      source_status_sha256: fa4cc1608338da5bdf2c3b2075b762215754fce05d2dc97e45591a7fbeff94ca
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C5
      - Accounting without a linked unit P1-S2-C6
      - Unaccounted source passage P1-S2-C5
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S2-C6
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Result passage disposed without unit P6-S2-C8
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P7-S1-C1
      - Accounting without a linked unit P7-S1-C2
      - Accounting without a linked unit P7-S1-C3
      - Unaccounted source passage P7-S1-C3
      - Unaccounted source passage P7-S1-C2
      - Result passage disposed without unit P9-S1-C4
      - Result passage disposed without unit P9-S2-C8
      - Result passage disposed without unit P11-S1-C5
      - Accounting without a linked unit P11-S1-C6
      - Accounting without a linked unit P11-S1-C7
      - Accounting without a linked unit P11-S1-C8
      - Unaccounted source passage P11-S1-C8
      - Unaccounted source passage P11-S1-C6
      - Unaccounted source passage P11-S1-C7
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P13-S1-C3
      - Result passage disposed without unit P14-S1-C1
      - Result passage disposed without unit P14-S1-C4
      - Result passage disposed without unit P14-S1-C5
      - Accounting without a linked unit P14-S1-C7
      - Accounting without a linked unit P14-S1-C8
      - Accounting without a linked unit P14-S1-C9
      - Accounting without a linked unit P14-S2-C3
      - Accounting without a linked unit P14-S2-C4
      - Accounting without a linked unit P14-S2-C5
      - Accounting without a linked unit P16-S1-C3
      - Unaccounted source passage P14-S2-C4
      - Unaccounted source passage P14-S1-C9
      - Unaccounted source passage P14-S2-C5
      - Unaccounted source passage P14-S2-C3
      - Unaccounted source passage P14-S1-C7
      - Unaccounted source passage P16-S1-C3
      - Unaccounted source passage P14-S1-C8
      - Result passage disposed without unit P17-S1-C12
      - Result passage disposed without unit P17-S2-C10
      - Accounting without a linked unit P17-S2-C11
      - Accounting without a linked unit P17-S2-C7
      - Accounting without a linked unit P17-S2-C9
      - Unaccounted source passage P17-S2-C11
      - Unaccounted source passage P17-S2-C9
      - Unaccounted source passage P17-S2-C7
      - Result passage disposed without unit P18-S1-C10
      - Result passage disposed without unit P18-S1-C6
      - Accounting without a linked unit P18-S1-C8
      - Accounting without a linked unit P18-S2-C2
      - Result passage disposed without unit P18-S2-C4
      - Result passage disposed without unit P18-S2-C6
      - Accounting without a linked unit P18-S2-C8
      - Unaccounted source passage P18-S2-C8
      - Unaccounted source passage P18-S2-C2
      - Unaccounted source passage P18-S1-C8
      - Result passage disposed without unit P18-S2-C9
      - Result passage disposed without unit P18-S3-C1
      - Result passage disposed without unit P18-S3-C6
      - Result passage disposed without unit P19-S1-C12
      - Result passage disposed without unit P19-S1-C13
      - Result passage disposed without unit P19-S2-C4
      - Result passage disposed without unit P19-S2-C5
      - Result passage disposed without unit P19-S2-C6
      - Result passage disposed without unit P19-S2-C7
      unattached_null_or_qualifier_ids:
      - P7-S1-C2
      - P9-S1-C4
      - P14-S1-C9
      - P18-S1-C10
      - P19-S1-C12
      suppressed_nonrepresented_units: 23
      default_disposition_count_requires_completeness_check: 238
      unselected_timing_passages:
      - P18-S4-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
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
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
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
      - slot: dependent_variable_statement
        source_id: P13-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C5
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
      - slot: dependent_variable_statement
        source_id: P14-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P18-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P18-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P18-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P18-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysis_restrictions
        source_ids:
        - P8-S2-C4
        - P8-S2-C6
        - P8-S2-C7
        - P8-S2-C8
        - P9-S1-C4
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C8
        - P12-S1-C9
        - P18-S1-C3
        - P18-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P18-S4-C2
        - P18-S4-C3
        - P18-S4-C4
        - P18-S4-C5
        - P19-S1-C4
        - P19-S1-C5
        - P19-S1-C6
        - P19-S1-C7
        - P19-S1-C8
        - P19-S1-C9
        - P19-S1-C10
        - P19-S1-C11
        - P19-S1-C12
        - P19-S1-C13
        - P19-S1-C14
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P3-S1-C7
        - P8-S2-C4
        - P8-S2-C6
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C8
        - P12-S1-C9
        - P14-S1-C4
        - P14-S1-C5
        - P14-S1-C6
        - P14-S1-C7
        - P14-S1-C8
        - P14-S1-C9
        - P18-S1-C3
        - P18-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-8-3
      - TABLE-4-page-9-4
      - TABLE-5-page-10-5
      - TABLE-6-page-10-6
      - TABLE-7-page-11-7
      - TABLE-8-page-12-8
      - TABLE-9-page-14-9
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-3-page-8-3
      - TABLE-6-page-10-6
      - TABLE-7-page-11-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P8-S2
        - P10-S2
        - P11-S1
        - P11-S2
        - P12-S1
        - P13-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
      source_review: _compare/relationships-2026-11-16/review-current/DenOuden2019
      source_status_sha256: fa4cc1608338da5bdf2c3b2075b762215754fce05d2dc97e45591a7fbeff94ca
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general variation in syntactic processing patterns.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings.
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings.
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data handling for missing responses.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes rater agreement.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes final group counts.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: References supporting information table.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes differences in aphasia/apraxia severity between groups.
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general differences in fluency and grammatical content.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes differences in fluency and grammatical content.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes non-significant differences in type/token ratio.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes noun/verb ratio differences.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the purpose of discourse analysis.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical methodology (regression of lesion size).
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general effects of canonicity.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general effects of verb argument complexity.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Correlation between NAVS subtests, severity, and lesion size.
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between aphasia severity and lesion size.
    - source_id: P9-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Null correlation between derived measures and severity/lesion size.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between specific verb complexity patterns.
    - source_id: P9-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group sizes for clustering.
    - source_id: P9-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group membership distribution.
    - source_id: P9-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Chi-square test of group distribution.
    - source_id: P9-S3-C2
      disposition: represented
      result_indexes:
      - 8
      reason: LDA performance for PD-MR group.
    - source_id: P9-S3-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Sensitivity and specificity for PD-MR LDA.
    - source_id: P9-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Effect of adding ASPT-G to first LDA.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: LDA performance for PD-MR with ASPT-G.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Sensitivity and specificity for PD-MR LDA with ASPT-G.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: T-test differences between PD-MR and PD-Other.
    - source_id: P10-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: T-test for noncanonical production in PD-MR.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: LDA performance for NAVS-Low group.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Predictive variables for NAVS-Low LDA.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Correct classification counts for NAVS-Low LDA.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 11
      reason: LDA performance for NAVS-Low with ASPT-G.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Predictive variables for NAVS-Low LDA with ASPT-G.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: T-test differences between NAVS-Low and NAVS-Other.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: References supporting information Figure S1.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General regional damage for NAVS grouping.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General regional damage for PD-MR grouping.
    - source_id: P10-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of proportional damage between groups.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Voxel associated with NAVS-Low after lesion size regression.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Location of voxel predicting NAVS-Low.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of the voxel.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Voxel associated with PD-MR group.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 2 and Table 7.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Dorsal and ventral connectivity predicting group membership.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General regional damage for subscores (Figure S2).
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Regional damage correlated with overall NAVS subscores after regression.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of NAVS-Low voxel result.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Damage to angular gyrus correlated with ASPT-A.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for regional damage in 3-place/2-place verbs.
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Connectivity between MTG and insula predicting 3-place verbs.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for regional damage in noncanonical SPPT.
    - source_id: P12-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Regional damage in posterior temporal/inferior parietal for noncanonical
        SCT.
    - source_id: P12-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on connectivity predicting noncanonical SPPT.
    - source_id: P13-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Connectivity predicting noncanonical SPPT.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Null correlation between derived measures and severity/lesion size.
    - source_id: P16-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of predictors for morphosyntactic reduction.
    - source_id: P17-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Discussion of triangular IFG lesions and PD-MR.
    - source_id: P17-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Discussion of medial pSTG damage and NAVS-Low.
    - source_id: P18-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Discussion of angular gyrus damage and ASPT-A.
    - source_id: P18-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Discussion of MTG-insula connectivity and 3-place verbs.
    - source_id: P18-S3-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Discussion of ventral connections to IFG and noncanonical SPPT.
    - source_id: P19-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Conclusion on Broca's area and agrammatic output.
    unresolved_coverage:
    - source_id: P7-S1-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P4-S2-C9
    - P6-S2-C8
    - P6-S2-C9
    - P6-S2-C10
    - P6-S2-C11
    - P6-S2-C12
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P9-S1-C4
    - P9-S1-C7
    - P9-S1-C8
    - P9-S2-C3
    - P9-S2-C4
    - P9-S2-C6
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    - P9-S3-C5
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C11
    - P10-S2-C2
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C5
    - P10-S2-C6
    - P10-S2-C8
    - P11-S1-C1
    - P11-S1-C3
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S2-C2
    - P12-S1-C1
    - P12-S1-C4
    - P12-S1-C5
    - P12-S1-C7
    - P12-S1-C9
    - P12-S2-C1
    - P13-S1-C3
    - P13-S1-C4
    - P14-S1-C1
    - P14-S1-C4
    - P14-S1-C5
    - P14-S1-C7
    - P14-S1-C8
    - P14-S1-C9
    - P14-S2-C3
    - P14-S2-C4
    - P14-S2-C5
    - P16-S1-C3
    - P16-S1-C4
    - P16-S1-C5
    - P16-S2-C2
    - P17-S1-C2
    - P17-S1-C7
    - P17-S1-C10
    - P17-S1-C11
    - P17-S2-C10
    - P18-S1-C3
    - P18-S1-C6
    - P18-S1-C10
    - P18-S2-C4
    - P18-S2-C8
    - P18-S2-C9
    - P18-S3-C1
    - P18-S3-C3
    - P18-S3-C6
    - P19-S1-C2
    - P19-S1-C12
    - P19-S1-C13
    - P19-S2-C5
    - P19-S2-C6
    - P19-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-8-3
    - TABLE-4-page-9-4
    - TABLE-5-page-10-5
    - TABLE-6-page-10-6
    - TABLE-7-page-11-7
    - TABLE-8-page-12-8
    - TABLE-9-page-14-9
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C9
      - P4-S2-C2
      recruited_sample:
      - P4-S1-C9
      eligibility:
      - P4-S1-C9
      imaging_provenance:
      - P7-S2-C6
      - P7-S2-C9
      - P7-S3-C2
      imaging_timing:
      - P7-S1-C5
      outcome_timing:
      - P19-S1-C2
      outcome_definition:
      - P5-S3-C6
      - P6-S1-C3
      validation:
      - P6-S2-C10
      analysis_restrictions: []
      dependent_variable_statement:
      - P8-S2-C4
      - P8-S2-C5
      - P12-S1-C3
      - P13-S1-C5
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C9
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
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
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
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
    - slot: dependent_variable_statement
      source_id: P13-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C5
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
    - slot: dependent_variable_statement
      source_id: P14-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P18-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P18-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P18-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P18-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysis_restrictions
      source_ids:
      - P8-S2-C4
      - P8-S2-C6
      - P8-S2-C7
      - P8-S2-C8
      - P9-S1-C4
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      - P18-S1-C3
      - P18-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P18-S4-C2
      - P18-S4-C3
      - P18-S4-C4
      - P18-S4-C5
      - P19-S1-C4
      - P19-S1-C5
      - P19-S1-C6
      - P19-S1-C7
      - P19-S1-C8
      - P19-S1-C9
      - P19-S1-C10
      - P19-S1-C11
      - P19-S1-C12
      - P19-S1-C13
      - P19-S1-C14
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P3-S1-C7
      - P8-S2-C4
      - P8-S2-C6
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      - P14-S1-C4
      - P14-S1-C5
      - P14-S1-C6
      - P14-S1-C7
      - P14-S1-C8
      - P14-S1-C9
      - P18-S1-C3
      - P18-S1-C6
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
      pdf_sha256: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
      review_sha256: 1fa4339f1c413311473eb3627ad12b70e43a8aba591777b2ab19664626778624
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
      - P10-S1-C1
      - P10-S1-C2
      source_result: A secondary linear discriminant analysis (LDA) using ASPT-G and
        SCT-NC-C scores predicted membership in the morphosyntactically reduced speech
        group (PD-MR) with 87.3% success, 75% sensitivity, and 90.2% specificity.
        This analysis was conducted for comparison to the primary LDA, which did not
        include ASPT-G.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a secondary LDA including ASPT-G
            (P8-S2-C2) and reports the specific variables (ASPT-G, SCT-NC-C) and performance
            metrics (87.3% success, 75% sensitivity, 90.2% specificity) in P10-S1-C1
            and P10-S1-C2. The draft correctly identifies this as the specific analysis.
          source_ids:
          - P8-S2-C2
          - P10-S1-C1
          - P10-S1-C2
        direction:
          answer: fits
          reason: The source states that the variables 'correctly categorized' the
            groups, implying a detected association between the scores and group membership.
            The draft's claim of prediction aligns with this detected relationship.
          source_ids:
          - P10-S1-C1
          - P10-S1-C2
        construct:
          answer: fits
          reason: The exposure (ASPT-G and SCT-NC-C scores) and outcome (PD-MR group
            membership) are correctly identified from the source. The patient measurement
            is behavioral (NAVS scores), not imaging-based, so 'non_imaging' is the
            correct classification.
          source_ids:
          - P10-S1-C1
          - P10-S1-C2
          - P5-S1-C10
          - P5-S3-C6
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that this was a secondary
            analysis conducted for comparison (P8-S2-C2) and notes the exclusion of
            three participants (P10-S1-C1). These are material qualifiers present
            in the source.
          source_ids:
          - P8-S2-C2
          - P10-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveat that the PD-MR group was defined
            by clinical judgment of descriptive speech (Cookie-Theft picture), which
            is a material limitation of the outcome measure. No other material caveats
            appear to be missing for this specific analysis.
          source_ids:
          - P6-S1-C9
          - P6-S2-C3
      optional_pending:
      - Sample size for this specific LDA (N=54 implied by 9/12 + 46/51, but not explicitly
        stated as a single N in the source text for this specific model, only the
        exclusions are mentioned).
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific LDA (N=54 implied by 9/12 + 46/51, but not explicitly
      stated as a single N in the source text for this specific model, only the exclusions
      are mentioned).
    normalizations:
    - field: sample.n
      original: 65
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R010
      exposure:
        text: ASPT-G and SCT-NC-C scores
      outcome:
        text: morphosyntactically reduced speech (PD-MR group membership)
      analysis_label: Linear Discriminant Analysis (PD-MR with ASPT-G)
      relation: performance
      evidence_ids:
      - P10-S1-C1
      - P10-S1-C2
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
        pdf_sha256: fbb400130534ae269095835a935821c414dadf8d3de984656d207bb241edfc20
        source_review: _compare/relationships-2026-11-16/review-current/DenOuden2019
        source_status_sha256: fa4cc1608338da5bdf2c3b2075b762215754fce05d2dc97e45591a7fbeff94ca
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
  page: 10
  quote: '

    improve classification (87.3% success), but the independently predic-

    tive variables were now identified as ASPT-G and SCT-NC-C, and only

    three participants had to be excluded.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
