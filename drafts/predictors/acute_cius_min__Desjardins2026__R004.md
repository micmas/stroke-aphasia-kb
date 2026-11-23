---
id: acute_cius_min
name: acute connected speech fluency and efficiency
kind: predictor
findings:
- id: f1
  target: subacute_connected_speech
  target_kind: prognosis
  claim: Acute connected speech performance (CIUs/min) is positively correlated with
    subacute connected speech performance.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 28
    population: people with aphasia due to a first ischemic stroke in the left middle
      cerebral artery territory
    phase: not_reported
    time_post_onset: acute (0-5 days) to subacute (7-15 days) post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: connected speech fluency and efficiency measured as
    correct information units per minute (CIUs/min) during the acute phase (0-5 days
    post-stroke). the association survived FDR correction. Additional metadata has
    not been transcribed; review the pending-field flags before approval. PDF image
    reading (P1-S2-C3, two-model agreement, human verification pending): . Naming
    and connected speech (quantified using correct information

    units per minute, CIUs/min) were assessed across the acute (0–5 days), subacute
    (7–15

    days), and chronic (>6 months) phases Original text-layer quotation is preserved
    below. PDF image reading (P3-S3-C8, two-model agreement, human verification pending):
    Participants


    Twenty-eight participants took part in this study (12 women; mean age: 70 ± 13
    years; mean education: 12 ± 4 years) Original text-layer quotation is preserved
    below. PDF image reading (P4-S1-C4, two-model agreement, human verification pending):
    Language assessment


    Initial assessment (acute phase) generally occurred within the first 72 h post-stroke
    (mean = 2 ± 1 days), a follow-up assessment (subacute phase) took place approximately
    ten days post-stroke (mean = 11 ± 2 days), and a third (chronic phase) was carried
    out at least 6 months post-stroke (mean = 306 ± 109 days or 10.0 ± 3.5 months)
    Original text-layer quotation is preserved below.'
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
    - proposed_concept:subacute_connected_speech
  citation: '@Desjardins2026'
  source_passages:
  - section: Original source P1-S2-C6
    page: 1
    quote: "Subacute connected speech was correlated \npositively to acute CIUs/min\
      \ and negatively to IFOF-lesion load."
    supports: claim
  - section: Original source P7-S1-C2
    page: 7
    quote: "Only \nIFOF-lesion load and acute CIUs/min survived the FDR correc-\n\
      tion."
    supports: claim
  - section: Original source P1-S2-C3
    page: 1
    quote: "Naming and connected speech (quantified using correct information \nunits\
      \ per minute, CIUs/min) were assessed across the acute (0—5 days), subacute\
      \ (7—15 \ndays), and chronic (>6 months) phases."
    supports: method
  - section: Original source P3-S3-C8
    page: 3
    quote: "Participants\nTwenty-eight participants took part in this study (12 women;\
      \ \nmean age: 70 ± 13 years; mean education: 12 ± 4 years)."
    supports: sample
  - section: Original source P3-S3-C10
    page: 3
    quote: "All participants were diagnosed with aphasia due to an \nischemic stroke\
      \ by a neurologist and screened for eligibility by \na licensed speech-language\
      \ pathologist."
    supports: sample
  - section: Original source P3-S4-C1
    page: 3
    quote: "were the following: experiencing a first ischemic stroke in the \nleft\
      \ middle cerebral artery territory, presenting language def-\nicits following\
      \ this stroke, speaking French, and being right-\nhanded."
    supports: sample
  - section: Original source P4-S1-C8
    page: 4
    quote: "To evaluate the impact of word-finding diffi-\nculties on fluency and\
      \ efficiency, connected speech samples \nwere elicited by the Picnic scene picture\
      \ description task from \nthe Western Aphasia Battery — Revised (Kertesz, 2006)."
    supports: method
  - section: Original source P4-S1-C4
    page: 4
    quote: "Language assessment\nInitial assessment (acute phase) generally occurred\
      \ within the \nfirst 72 h post-stroke (mean = 2 ± 1 days), a follow-up \nassessment\
      \ (subacute phase) took place approximately ten \ndays post-stroke (mean = 11\
      \ ± 2 days), and a third (chronic \nphase) was carried out at least 6 months\
      \ post-stroke \n(mean = 306 ± 109 days or 10.0 ± 3.5 months)."
    supports: method
predictor_type: behavioural
short_definition: connected speech fluency and efficiency measured as correct information
  units per minute (CIUs/min) during the acute phase (0-5 days post-stroke)
assessment:
- Picnic scene picture description task from the Western Aphasia Battery — Revised
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Desjardins2026
  proposal_id: R004
  review_status_sha256: 40ab15fef4f6643cdfe699b643ead825b78661ae8acd2d904a89bfd59e7d8e0f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
        A/passages.json: a696ee6a5ecf35e6200df5161ff4e2da264f1cb7a812eafe7a324dafd8d544b9
        A/raw.json: 89b5ba73e68bd5f96c34f45dfee5b29c3e3d71e3e55fe0ac8894ff6359ddcfdc
        A/source-units.json: 882b68babb34c6138c81a14848f945ce8bf3843524feb18fbcbf0330c044399c
        A/full-source-units.json: 882b68babb34c6138c81a14848f945ce8bf3843524feb18fbcbf0330c044399c
        A/meta.json: 85d4212156f71deff16461942104751cd56aca9ba314d7769dbece417402b921
        A/table-images/TABLE-1-page-5-1.png: 25c51362497522e832274e3707cec0733edef1448271d5491886985c1a6cddc1
        A/table-images/TABLE-3-page-9-1.png: 74e25119e5ecfc0fefd2e1d2fdcf20771fd5a510759281c4c03d0b6208854b29
        A/table-images/page-11.png: 090e234c504791f893536ff69493dde7e4e8d34d0249480ca26346f80c3a5da4
        A/table-images/TABLE-2-page-8-1.png: de9a2f1b7b4c04cdfe71c7902ee3b91b36a887bd0e2b16fc298f35c2e9bbaa38
        A/table-images/page-5.png: c0acf2d8816e7d3a1c2d2e2cea59ae2c678c885f2f3bf2a42741c0290c0eae58
        A/table-images/TABLE-4-page-11-1.png: c8be79965d1e6ca8f2b170f19a23805f82e61acd8362f0216eaf99b4d7061432
        A/table-images/page-9.png: e8900238e9ed3d017bf9a2c1fd56de8d68f632ccef504a83a8d49c18a8c081ff
        A/table-images/page-8.png: 4e8bcd4516c04f333aab66eff2070a8cc564de61fa9104cc422195760ba01270
        A/table-images/manifest.json: e9c2a09e57d79967de883e4f8c87d072217d4a02d7e8a5fbb2cb16286ef55480
        A/clauses/window-11/raw.json: 23a724482ec24ae90586bd9f03c5a9cc81a8be446b9bb4d60cef2895eb20b801
        A/clauses/window-11/prompt.txt: 560f77a1d75237cb94fdc49fadca00057704f8a8b5248997d61c65cadf65ed4b
        A/clauses/window-11/meta.json: e276488c679f9c6fd35aa898ca6ee5a4e0901213f2b821c4e7b0327288a43068
        A/clauses/window-16/raw.json: e062a98540a1aec45652db6b47eb9f257779bde062e92e76e5af116d42bc11d8
        A/clauses/window-16/prompt.txt: 3922fc925e9b01b0c70795cd3784cb84e44db4fd13d6880270f2bada2be60c75
        A/clauses/window-16/meta.json: 3301802d862eabb10e163c705ca30cdf23a90502555b0fa3e9e0d77314c71282
        A/clauses/window-20/raw.json: 04c43446c1d6bc412a99928744cf7a8a6bb8b67526a20cc521df3075838927bf
        A/clauses/window-20/prompt.txt: ab6e1ea7127d6dcb92ab95f97fdcb06dd2fcc285c58129f22b4b199403dbe158
        A/clauses/window-20/meta.json: 5f490fb80960bd5f44b45dd720bbb17fbdc68da2268948b6cee85a01576797f4
        A/clauses/window-18/raw.json: 602dc500ee570d2e2ea70f999780b0df1d904570cc3b297c74496f4fc394ee35
        A/clauses/window-18/prompt.txt: 22748b7261d800a993f0b510a51e93aded6ad327f2f0d047f0e64475226c0fd9
        A/clauses/window-18/meta.json: 9aa0f7c4aaa68346dd0585bbd85e420bb70679191f05bc017d3d580f81483829
        A/clauses/window-19/raw.json: 0fd2430d0015cb669274848d7b086428a16e7cf7bbebadf8b9d3556fa19a439b
        A/clauses/window-19/prompt.txt: 27f11ac3ada958411e7933dd766396aa972a6a2627183575e58678251479c0ad
        A/clauses/window-19/meta.json: c0c7c95140b9415674c587d481ad0f51d94a167a2bf1139e7710e59f1c0219dd
        A/clauses/window-17/raw.json: 76e757377c12e54c1a91d0071a8701ffcdb783a52e2f930fec9c5646ba897c11
        A/clauses/window-17/prompt.txt: 086511dd572468449f57df4850681361568f271e57e4e4e83335bfe30ebafd15
        A/clauses/window-17/meta.json: eba7bb142168a30a1497b3e51d4f9f347bb413dac6063e72bb8b2e10313d008d
        A/clauses/window-10/raw.json: a69a9c2475810ba83b2b85a9cade2d74e21538dcc91a3304c70fa30061cabc60
        A/clauses/window-10/prompt.txt: 8f697725cc4ab77ddd47fc2b619b7af7549360020ac414f2e6bbfdeb25f54571
        A/clauses/window-10/meta.json: ce8011aaa6e8b9cb74489ede775adc518780988415a5896ca83860c1ea065aa8
        A/clauses/window-03/raw.json: 0b0c42a9be569f92ca9393a14cb642bffb6eca6d37bd54336afb7bcc36462b27
        A/clauses/window-03/prompt.txt: 59fff884a6a7a5a588ac5dd10880a10d0d8ebd558ee10d8a36b42983659a1a82
        A/clauses/window-03/meta.json: ad5526c884f8e95f270d8613e87cc3b6b6d1ec188671cc6be08594de248023dd
        A/clauses/window-04/raw.json: 9becfa79539a3fedc96c2f6114f1cdec4da632af159511e4eb4a8ddff840ca2b
        A/clauses/window-04/prompt.txt: 973378248be198cda7cec7bf0659b4c6a22246708db282be3dcaf870e2131f3b
        A/clauses/window-04/meta.json: 8e1f2b9aad2cc510b6e5a064f220e5a4a13f3d212e78a0979970484406dac805
        A/clauses/window-05/raw.json: d54396e54b02ecdc0a59b96cac68f10433724866dbf278b87a93b985fe16a111
        A/clauses/window-05/prompt.txt: edc7228dda495fb5d274659b9d6f61596d0b71aeb6263e7c64fbf07dd069d42e
        A/clauses/window-05/meta.json: 5a930007e329fc787e9d220d0921f28412ad6f6df7e1832cfe823d980caddae3
        A/clauses/window-02/raw.json: d704d0622cd606f98cf46bfafc4e014e30bccac0e7891ebba7c182a54036b472
        A/clauses/window-02/prompt.txt: c74cffec0e7d88730f59450d5f9cd68462ade28a9616982139cdb2ae4d3b61f9
        A/clauses/window-02/meta.json: c81498c03bf2d5b76eb1e61ea578aa1721e564263218ee6ab3785c1162701775
        A/clauses/window-15/raw.json: 847bcfbf1d9a9312cc0172e44ae8f3abb39332d405177a641b62a55abdc06d10
        A/clauses/window-15/prompt.txt: 3fc2c55fd223ad1c1e45f87a6bffab6afc2c990c1eebae8fbd4217b9076d90e8
        A/clauses/window-15/meta.json: 333dea2d8ff4d8f8657909d6f1f0fd591ad30740bfa6cb960dfaa15c0d0d5603
        A/clauses/window-12/raw.json: 0f6352023cf7c2757f8b4e38c1f5651c4a977588a7757ee7fa3fbc834d0aa867
        A/clauses/window-12/prompt.txt: c7bf1a8570a63db2713125b589901be2d34247fcde99dca4e7587199edd1d8a1
        A/clauses/window-12/meta.json: 09d4103f37f02ee621dcccaf05d2242d9cd05a2519859e13b03fc3deeec2b4d4
        A/clauses/window-13/raw.json: 0e4ccf07531798812bfbd78b7dd876d1e6e931ded1523780fb0f570965b4c232
        A/clauses/window-13/prompt.txt: 075fb8c4682d162029e471003b85844d8c3daf2402c26d8f87954c856c00d7d4
        A/clauses/window-13/meta.json: 79b886c2d4f9286521fdbdf24643e0b4d2d20a85f60563ee6953509fdda6ca68
        A/clauses/window-14/raw.json: 9c72ad6d0cf54b4976cf93555158c441ce529f6046b4b9db79af03f9932076c0
        A/clauses/window-14/prompt.txt: 1364ba547ab4e6f5ba3f5f5b08bd538a63f4648de7eae1b879278cd8749ce0d4
        A/clauses/window-14/meta.json: aae8af6aac2d57fa3b08a19d62177027270324fcfd0df843f328cac8ef2d1fd4
        A/clauses/window-09/raw.json: d222972824efe3ac046b9fdec8d07bc023eefc50a0932199307a88f60c39efec
        A/clauses/window-09/prompt.txt: e8f012dd605c940a296279f0fc40414fea4a5f7dfdc4dd6b33714098feb918ee
        A/clauses/window-09/meta.json: 5cdb8b55e8425e9e07945a82bceb266ec92e1055156c70aa3e5164907d1841e1
        A/clauses/window-07/raw.json: 1930519e94007101af2988e0787463b642b382bfe381e5f07e9e7a427c1a10ce
        A/clauses/window-07/prompt.txt: 7c4560338d48cfa46890605ee4b4712f4d72b52df7805498b964dda8fd2e1521
        A/clauses/window-07/meta.json: 413e41ca9309bb06991beb69342daa4d9cb77542d2e448ad3500d6acb5e36e2b
        A/clauses/window-01/raw.json: 559f9846503b22a80ba489e8de2029bdb1268a85ebad858e9c3215dc6818107d
        A/clauses/window-01/prompt.txt: 61229a753bca1e1945abe6170fbdaed358dc7b8d4dd971c23161acbda561e2e8
        A/clauses/window-01/meta.json: 1fd1aaf0865bfa1ebc4943a4b0766f66d5ff45e40262d9aa145cffc262a9dc4f
        A/clauses/window-06/raw.json: d8d9a65d1b066da7c6e6c2a7df6ed86e4e247cb35e1ba04419668c252133df9e
        A/clauses/window-06/prompt.txt: b51fbe3ca06b815bcd65bb0a87d2cbcf3bf81b10d05b617209c7a9a527333b5c
        A/clauses/window-06/meta.json: bc3a7945a3fbb7b2ff75441aa41b8bf37143b8a31295f372c8f790167cfcdcec
        A/clauses/window-08/raw.json: e27cc23c58dd8030232981167144c104717ace6bf4763366e1c1d35ee979365c
        A/clauses/window-08/prompt.txt: 9a4f7c430505877981485c38f4952e1bffd387a110641901e7b053d674c4c401
        A/clauses/window-08/meta.json: 6f6b084f5905fbea4b394349c3b6998b7daba2c1117dad13d9f3254e30f42522
        A/tables/TABLE-1-page-5-1/raw.json: 6fe33626b602e3ebef59b0bad5caad1a6afaf7558c5a7dcb80a840566ad81814
        A/tables/TABLE-1-page-5-1/prompt.txt: 4d3eaa65d9a7a84f2e0613293a8fb6b6beae263d7a0e4f8db54f8c553728c9c6
        A/tables/TABLE-1-page-5-1/meta.json: c4428f5d950c2eb8ebf8e2eb9f1d0715791b5f5c558aeb34c1850c42b2cbcbef
        A/tables/TABLE-4-page-11-4/raw.json: ef8867cb56c6d20221750171adf5c41b4cbf41a8f46ea38d21a8c29c53102bf4
        A/tables/TABLE-4-page-11-4/prompt.txt: 503af274c815abdde3974afc57eecac9a4d5d2353985a59aaeff595929c80df7
        A/tables/TABLE-4-page-11-4/meta.json: 947298e1b6788c11825c014766b6877e5d06f7ec1bebfdb73af4461a84b49121
        A/tables/TABLE-2-page-8-2/raw.json: 2c65ad8aee2970dcc20ecab5c9a264ec6994edb2c2066f5a69dba3fcaac59b8d
        A/tables/TABLE-2-page-8-2/prompt.txt: d4537a835b1f3ec24aa77f75893d8867f12bcf355f1cdc55813dbabe01b6c2bc
        A/tables/TABLE-2-page-8-2/meta.json: 020a44dfa0da8375142a328139d01bfb0da65d40b872166e0b05da80279e4f9b
        A/tables/TABLE-3-page-9-3/raw.json: af85f58769b80487e41e8b82bd542daa16b02bd61a6d33a8e967db50cd2a4c4d
        A/tables/TABLE-3-page-9-3/prompt.txt: 61fea270565a951d1cc8a8a70a9f14add69ee549326a30980e8902584107992f
        A/tables/TABLE-3-page-9-3/meta.json: 214326fda9d296155a5defb1cd9eae302dae972348efadeb661c9040b719b681
        B/passages.json: a696ee6a5ecf35e6200df5161ff4e2da264f1cb7a812eafe7a324dafd8d544b9
        B/raw.json: 99f229ac4130a90ec17c884139f6b480b79881446e7c06cd19e879dd25a5ea07
        B/source-units.json: 882b68babb34c6138c81a14848f945ce8bf3843524feb18fbcbf0330c044399c
        B/full-source-units.json: 882b68babb34c6138c81a14848f945ce8bf3843524feb18fbcbf0330c044399c
        B/meta.json: 208394391ee8db8c7dfd214d689afa35d3634de8ee3aa5ebc4cc3654558a554e
        B/table-images/TABLE-1-page-5-1.png: 25c51362497522e832274e3707cec0733edef1448271d5491886985c1a6cddc1
        B/table-images/TABLE-3-page-9-1.png: 74e25119e5ecfc0fefd2e1d2fdcf20771fd5a510759281c4c03d0b6208854b29
        B/table-images/page-11.png: 090e234c504791f893536ff69493dde7e4e8d34d0249480ca26346f80c3a5da4
        B/table-images/TABLE-2-page-8-1.png: de9a2f1b7b4c04cdfe71c7902ee3b91b36a887bd0e2b16fc298f35c2e9bbaa38
        B/table-images/page-5.png: c0acf2d8816e7d3a1c2d2e2cea59ae2c678c885f2f3bf2a42741c0290c0eae58
        B/table-images/TABLE-4-page-11-1.png: c8be79965d1e6ca8f2b170f19a23805f82e61acd8362f0216eaf99b4d7061432
        B/table-images/page-9.png: e8900238e9ed3d017bf9a2c1fd56de8d68f632ccef504a83a8d49c18a8c081ff
        B/table-images/page-8.png: 4e8bcd4516c04f333aab66eff2070a8cc564de61fa9104cc422195760ba01270
        B/table-images/manifest.json: 118296d222df5b9981e335cb04d9601dafaa706de3d6ce6d4b9a7960809f30db
        B/clauses/window-11/raw.json: bfe5b09d30bfb3210fe9f76a23bd6af3e456ed86dc22b7107bf3a4d145fc5400
        B/clauses/window-11/prompt.txt: 560f77a1d75237cb94fdc49fadca00057704f8a8b5248997d61c65cadf65ed4b
        B/clauses/window-11/meta.json: 25823149254121ed649a62adbd4a5deb343029536d9696157938701b16d8f4b6
        B/clauses/window-16/raw.json: 0a43dbd93145bbdf29f9e62cc59cf128a5ebb36a7105ecc83c3fa99e1cce049a
        B/clauses/window-16/prompt.txt: 3922fc925e9b01b0c70795cd3784cb84e44db4fd13d6880270f2bada2be60c75
        B/clauses/window-16/meta.json: 9b2702eb91a2b63f320ff7d84edf376dcea446e84320a892b245e688feb1b41c
        B/clauses/window-20/raw.json: adf95e4bc83a11f53818c5e597c88ac6670843ea035a121d1449bfd82c7a4aa5
        B/clauses/window-20/prompt.txt: ab6e1ea7127d6dcb92ab95f97fdcb06dd2fcc285c58129f22b4b199403dbe158
        B/clauses/window-20/meta.json: 344aee21fbc93ad559d6ebb8d908df05da3f18d5d5f1edb3c45a71640edcbf5b
        B/clauses/window-18/raw.json: d6d5001baef08cff8cc5716770d0256629718465939f303cf972626f2d7f601c
        B/clauses/window-18/prompt.txt: 22748b7261d800a993f0b510a51e93aded6ad327f2f0d047f0e64475226c0fd9
        B/clauses/window-18/meta.json: da4edf454b29ffb02f352bb517e15a8553a9a1a19f5abe1b162c924a4db01636
        B/clauses/window-19/raw.json: d73a469813ea1d31f865212ee43b7d361cfa4ea40c64102e6a1b307a308a7c33
        B/clauses/window-19/prompt.txt: 27f11ac3ada958411e7933dd766396aa972a6a2627183575e58678251479c0ad
        B/clauses/window-19/meta.json: 1b51297d8923896d525a91d0b1286bad0e2a28b50323e89677cac89e455140f4
        B/clauses/window-17/raw.json: 0824779fefaab48c0a3894417cb29c2b134435d0031175b8f17da2f1dc7d64de
        B/clauses/window-17/prompt.txt: 086511dd572468449f57df4850681361568f271e57e4e4e83335bfe30ebafd15
        B/clauses/window-17/meta.json: 93a879e767c280aeb4fa0d7666c45d6cbfd13846224119029b138531aee14499
        B/clauses/window-10/raw.json: 6425729518175368fc273a0e7a660b0e8c520a2d5900bc95f68268c46c89f7a3
        B/clauses/window-10/prompt.txt: 8f697725cc4ab77ddd47fc2b619b7af7549360020ac414f2e6bbfdeb25f54571
        B/clauses/window-10/meta.json: 897f965ae7c5fee9896967a8beda4d7706d5cbbcd7b70058335cee09f26ebe6e
        B/clauses/window-03/raw.json: 62af4a51e521b9b2c33d12dfb5fea3f58ed917c199bbe568dc94440f2025c40d
        B/clauses/window-03/prompt.txt: 59fff884a6a7a5a588ac5dd10880a10d0d8ebd558ee10d8a36b42983659a1a82
        B/clauses/window-03/meta.json: f644f942a7fc6e936af1460e62e584d87a9240624ca243cf2bca54a7154e4a63
        B/clauses/window-04/raw.json: d59c5aa8d7f35f77f41d6ff24e101fd4b0fc2fc84868dce24721af32dabdd594
        B/clauses/window-04/prompt.txt: 973378248be198cda7cec7bf0659b4c6a22246708db282be3dcaf870e2131f3b
        B/clauses/window-04/meta.json: e66d95a91f658a037530df45822111fc199b39e1dbd6813bc4b9af59076ce138
        B/clauses/window-05/raw.json: fadafbdc72d2ddb1da7d8bdbb438e49d9e14c6346b7129f366ac69f5f7997ea5
        B/clauses/window-05/prompt.txt: edc7228dda495fb5d274659b9d6f61596d0b71aeb6263e7c64fbf07dd069d42e
        B/clauses/window-05/meta.json: f8f62151541e16c1f1c669b098b618ffb840fe2e8ee0855b9202f794bc5790b8
        B/clauses/window-02/raw.json: b079d1c7b7f4c0ca759ca4a5918274e40eae81ba9d39cfe9fbb0bab55476e1c6
        B/clauses/window-02/prompt.txt: c74cffec0e7d88730f59450d5f9cd68462ade28a9616982139cdb2ae4d3b61f9
        B/clauses/window-02/meta.json: 1424b21128926d677716b5f163f9117475cb7fd4b56e04e49d95e65cba4fb258
        B/clauses/window-15/raw.json: 938bec1b3293f5100540b28b2ca24c4a50232aebd73c12732fadca51449e37bd
        B/clauses/window-15/prompt.txt: 3fc2c55fd223ad1c1e45f87a6bffab6afc2c990c1eebae8fbd4217b9076d90e8
        B/clauses/window-15/meta.json: 7cf92ce6e907b2c0dd2934b858a917121ea71ed5e58f91f3c3fafe7d0ddee344
        B/clauses/window-12/raw.json: f6d42baba874e7232b22f4f86cf5825e6c0e2d217ce1e1a726b98c031a5227e6
        B/clauses/window-12/prompt.txt: c7bf1a8570a63db2713125b589901be2d34247fcde99dca4e7587199edd1d8a1
        B/clauses/window-12/meta.json: 5966c3c5007621093ec4d779a8fc3f9c636f7846ddfd2eb11aaa8d3447995435
        B/clauses/window-13/raw.json: 23e21eb83050847fd80539da42aa57d8c1dd291b263dde383743e5c0d859ba8f
        B/clauses/window-13/prompt.txt: 075fb8c4682d162029e471003b85844d8c3daf2402c26d8f87954c856c00d7d4
        B/clauses/window-13/meta.json: 5754e332d74562fb38a1989743eae057e301654c1d2e70fde4574616d3c1e50c
        B/clauses/window-14/raw.json: 3a901e3e12370cc5c8728502559f7ee1aabcdffc75091e163cc724b6821f8f44
        B/clauses/window-14/prompt.txt: 1364ba547ab4e6f5ba3f5f5b08bd538a63f4648de7eae1b879278cd8749ce0d4
        B/clauses/window-14/meta.json: 85715ef7f6e36c88324d62a2b26188995e1342bfaa14236fb6a4b6c4f6a1d0de
        B/clauses/window-09/raw.json: fd815eb4d0d71a89a4a61cf140178453201a8a1607f124ec908b7ac724a4af55
        B/clauses/window-09/prompt.txt: e8f012dd605c940a296279f0fc40414fea4a5f7dfdc4dd6b33714098feb918ee
        B/clauses/window-09/meta.json: 8271a5002749d1ae50926678f9a2d3df3af2f2372fb63e908c3e0b0b761f7320
        B/clauses/window-07/raw.json: 7c53f00e75b6df1206f9d71ba494ec4fcb77dbc308a4cfc584bba6f35fbcd17e
        B/clauses/window-07/prompt.txt: 7c4560338d48cfa46890605ee4b4712f4d72b52df7805498b964dda8fd2e1521
        B/clauses/window-07/meta.json: 5a1531034a0be78d07b25105f9cd59cae123aece40215f493dc06d6536c6c628
        B/clauses/window-01/raw.json: e820c0cfe3526390ccff26eba9a2c34c91b110fb7bf9c1a97839f17fa17cef50
        B/clauses/window-01/prompt.txt: 61229a753bca1e1945abe6170fbdaed358dc7b8d4dd971c23161acbda561e2e8
        B/clauses/window-01/meta.json: 8e61bc7757d026319dcb350ad060049fccf02047706be3360e5ad96400250401
        B/clauses/window-06/raw.json: b5697ab8f84115434531ea6f4ee313ec1d6f7b276a5d0d5d58c4f27238e0e4cd
        B/clauses/window-06/prompt.txt: b51fbe3ca06b815bcd65bb0a87d2cbcf3bf81b10d05b617209c7a9a527333b5c
        B/clauses/window-06/meta.json: 97847b3d3cfc533b9a61f5783acf0d827e7f5f46fd940773f40936ebdf097dfb
        B/clauses/window-08/raw.json: 01000edafff635f36b3550bba3b642930b4d70f1a74c6be7ff25e26e22b3a062
        B/clauses/window-08/prompt.txt: 9a4f7c430505877981485c38f4952e1bffd387a110641901e7b053d674c4c401
        B/clauses/window-08/meta.json: 056f90a900b6d50e48e6130ab5fcef3ae5b5eae3111566d06e4e4f82c37b1f5d
        B/tables/TABLE-1-page-5-1/raw.json: 6fe33626b602e3ebef59b0bad5caad1a6afaf7558c5a7dcb80a840566ad81814
        B/tables/TABLE-1-page-5-1/prompt.txt: 4d3eaa65d9a7a84f2e0613293a8fb6b6beae263d7a0e4f8db54f8c553728c9c6
        B/tables/TABLE-1-page-5-1/meta.json: d70080838aef4dbd10c9889815ecc554882b9c067b9e750b5f776195a9d76f2a
        B/tables/TABLE-4-page-11-4/raw.json: 07fca5f783fffdf7ccfa483364dda19d73cae7c4f7589e485525c52ea6cbf20d
        B/tables/TABLE-4-page-11-4/prompt.txt: 503af274c815abdde3974afc57eecac9a4d5d2353985a59aaeff595929c80df7
        B/tables/TABLE-4-page-11-4/meta.json: d2775fb7ad4d68ce946210fa8e891a21cc62336c0b1e994fe370aafa9fe2ea53
        B/tables/TABLE-2-page-8-2/raw.json: dc56c9816a2d2dc5a942815a768a17392dc2d319984bff3912de0326c3fc19b1
        B/tables/TABLE-2-page-8-2/prompt.txt: d4537a835b1f3ec24aa77f75893d8867f12bcf355f1cdc55813dbabe01b6c2bc
        B/tables/TABLE-2-page-8-2/meta.json: 8f1e28cb065365f9294d8e410d314dac69a3937f3d74168df0794bfee4acaa25
        B/tables/TABLE-3-page-9-3/raw.json: e7456328a7ee1522cce7b3d46d0e3fa95458ed357f488d39fd7f300d8b5a18ea
        B/tables/TABLE-3-page-9-3/prompt.txt: 61fea270565a951d1cc8a8a70a9f14add69ee549326a30980e8902584107992f
        B/tables/TABLE-3-page-9-3/meta.json: 5ed647b654813d44cc57a657fff9c7fde06fc19ed864f9810802f49e37bb09a9
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
      pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
      source_review: _compare/relationships-2026-11-16/review-current/Desjardins2026
      source_status_sha256: 0d13a7a791fec80a93733ae695556ff78938a6fdc39202cc0a15a83c6dc48e2f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: acute CIUs/min
    outcome:
      text: subacute connected speech
    analysis_label: Pearson correlation
    relation: association
    evidence_ids:
    - P1-S2-C6
    - P7-S1-C2
    - P9-S2-C4
    qualifier_ids:
    - P7-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
      source_review: _compare/relationships-2026-11-16/review-current/Desjardins2026
      source_status_sha256: 0d13a7a791fec80a93733ae695556ff78938a6fdc39202cc0a15a83c6dc48e2f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P4-S2-C7
      - Unaccounted source passage P4-S2-C7
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P6-S3-C8
      - 'window 9: invalid/duplicate disposition P7-S1-C5'
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C13
      - Accounting without a linked unit P8-S1-C14
      - Result passage disposed without unit P8-S1-C15
      - Accounting without a linked unit P8-S2-C2
      - Unaccounted source passage P8-S1-C14
      - Unaccounted source passage P8-S2-C2
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P8-S2-C9
      - Accounting without a linked unit P8-S2-C12
      - Accounting without a linked unit P8-S3-C1
      - Accounting without a linked unit P8-S3-C2
      - Unaccounted source passage P8-S2-C12
      - Unaccounted source passage P8-S3-C2
      - Unaccounted source passage P8-S3-C1
      - 'window 15: invalid/duplicate disposition P9-S1-C10'
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P9-S1-C11
      - Result passage disposed without unit P9-S2-C2
      - 'window 17: invalid/duplicate disposition P10-S1-C5'
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Accounting without a linked unit P11-S1-C7
      - Unaccounted source passage P11-S1-C7
      - 'window 19: invalid/duplicate disposition P11-S1-C12'
      - Result passage disposed without unit P11-S1-C12
      - 'window 21: invalid/duplicate disposition P11-S2-C10'
      - Result passage disposed without unit P11-S2-C10
      - Result passage disposed without unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C11
      - Result passage disposed without unit P12-S2-C5
      - Result passage disposed without unit P12-S3-C6
      - Result passage disposed without unit P12-S3-C8
      - Result passage disposed without unit P12-S3-C9
      unattached_null_or_qualifier_ids:
      - P4-S2-C7
      - P8-S1-C1
      - P8-S2-C2
      - P8-S2-C3
      - P8-S2-C12
      - P8-S3-C1
      - P9-S1-C1
      - P9-S1-C11
      - P10-S1-C2
      suppressed_nonrepresented_units: 33
      default_disposition_count_requires_completeness_check: 272
      unselected_timing_passages:
      - P1-S2-C3
      - P3-S3-C8
      - P4-S1-C1
      - P4-S1-C4
      - P8-S1-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S4-C1
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
        source_id: P12-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S4-C19
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C23
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P3-S3-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S2-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P1-S2-C3
        - P3-S2-C8
        - P3-S3-C1
        - P3-S3-C4
        - P3-S3-C5
        - P4-S1-C4
        - P8-S2-C8
        - P8-S2-C9
        - P8-S3-C5
        - P9-S1-C2
        - P12-S1-C7
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C6
        - P12-S3-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S2-C3
        - P2-S2-C11
        - P2-S2-C12
        - P3-S3-C1
        - P3-S3-C3
        - P3-S3-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S2-C3
        - P4-S2-C5
        - P6-S1-C5
        - P8-S2-C7
        - P8-S2-C8
        - P8-S2-C10
        - P8-S3-C1
        - P9-S1-C2
        - P9-S1-C8
        - P12-S1-C7
        - P12-S1-C8
        - P12-S1-C9
        - P12-S1-C11
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C6
        - P12-S3-C8
        - P12-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C11
        - P6-S3-C2
        - P6-S3-C3
        - P8-S1-C9
        - P8-S1-C11
        - P8-S2-C4
        - P8-S2-C5
        - P9-S1-C11
        - P12-S2-C7
        - P12-S2-C10
        - P12-S2-C11
        - P12-S2-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S1-C9
        - P3-S2-C1
        - P3-S2-C2
        - P3-S2-C3
        - P3-S2-C4
        - P3-S2-C5
        - P3-S2-C6
        - P3-S2-C7
        - P4-S1-C1
        - P8-S1-C2
        - P8-S1-C15
        - P8-S2-C3
        - P8-S2-C4
        - P8-S2-C5
        - P9-S1-C1
        - P9-S1-C10
        - P9-S1-C11
        - P9-S1-C12
        - P10-S1-C2
        - P10-S1-C5
        - P11-S1-C1
        - P11-S1-C12
        - P11-S2-C3
        - P11-S2-C10
        - P12-S1-C13
        - P12-S1-C14
        - P12-S2-C3
        - P12-S2-C5
        - P12-S2-C7
        - P12-S2-C9
        - P12-S2-C10
        - P12-S2-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C4
        - P3-S2-C9
        - P6-S1-C3
        - P6-S1-C9
        - P6-S1-C10
        - P8-S1-C12
        - P8-S1-C13
        - P8-S1-C14
        - P9-S2-C4
        - P12-S3-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S2-C4
        - P3-S3-C8
        - P3-S4-C3
        - P5-S1-C6
        - P5-S2-C1
        - P6-S2-C8
        - P8-S1-C3
        - P8-S3-C5
        - P9-S2-C4
        - P12-S3-C11
        - P14-S3-C6
        - P15-S3-C36
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - outcome_definition
      - validation
      - analysis_restrictions
      - limitations
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P2-S3-C1
      - P2-S4-C1
      - P12-S2-C15
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-8-2
      - TABLE-3-page-9-3
      - TABLE-4-page-11-4
      unlinked_tables:
      - TABLE-1-page-5-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P8-S3
        - P10-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
      source_review: _compare/relationships-2026-11-16/review-current/Desjardins2026
      source_status_sha256: 0d13a7a791fec80a93733ae695556ff78938a6fdc39202cc0a15a83c6dc48e2f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Correlations for subacute naming.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Correlations for subacute connected speech.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Regression models for subacute naming and connected speech.
    - source_id: P1-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about predictors.
    - source_id: P2-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about outcomes.
    - source_id: P2-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about white matter tracts.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reliability metrics for CIUs/min.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Tract exclusion statistics.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Tract exclusion details.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Tract reconstruction failure statistics.
    - source_id: P6-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion segmentation success rate.
    - source_id: P6-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Uncorrected correlation count.
    - source_id: P6-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Strongest uncorrected correlations for subacute naming.
    - source_id: P6-S3-C15
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: FDR corrected correlations for subacute naming.
    - source_id: P6-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Uncorrected correlations for subacute CIUs/min.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Strongest uncorrected correlations for subacute CIUs/min.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: FDR corrected correlations for subacute CIUs/min.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Uncorrected correlations for chronic naming.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: FDR corrected correlation for chronic naming.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Outlier observation.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Outlier verification.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Null result for chronic naming after outlier removal.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Uncorrected correlations for chronic CIUs/min.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Null result for chronic CIUs/min after FDR correction.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 7
      reason: Regression model for subacute naming.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 8
      reason: Regression model for subacute CIUs/min.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Regression model for chronic CIUs/min.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Null result for chronic CIUs/min model after Bonferroni correction.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Correlation for chronic naming.
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Outlier observation for chronic naming.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Null result for chronic naming after outlier removal.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about right UF volume.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      reason: Pearson correlation table.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Right UF volume as predictor of chronic connected speech.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Right UF volume did not survive multiple comparisons correction.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: UF lesion load variability.
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on acute assessment.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on white matter characteristics.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on lesion-related variables.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Total lesion volume correlation.
    - source_id: P11-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on lesion load.
    - source_id: P11-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: AF-lesion load and naming.
    - source_id: P11-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Null result for FAT and ILF lesion load and naming after FDR correction.
    - source_id: P11-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of naming vs connected speech associations.
    - source_id: P11-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: IFOF-lesion load importance.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on short-term prognosis.
    - source_id: P11-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on language lateralization.
    - source_id: P11-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on TMS and lateralization.
    - source_id: P11-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Right UF and FAT correlations.
    - source_id: P11-S3-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Negative association between right ILF volume and chronic DO-80.
    - source_id: P12-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Negative association between right ILF volume and chronic DO-80.
    - source_id: P12-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on acute aphasia severity.
    - source_id: P12-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on lesion influence.
    - source_id: P12-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on AF, ILF, FAT vs IFOF.
    - source_id: P12-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on white matter predictors.
    - source_id: P12-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on clinical variables.
    - source_id: P12-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on future predictors.
    - source_id: P12-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on patients.
    - source_id: P12-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Author contribution statement.
    - source_id: P11-S4-C1
      disposition: represented
      result_indexes:
      - 7
      - 8
      - 9
      reason: Regression results table.
    unresolved_coverage:
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S4-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C8
    - P2-S1-C1
    - P2-S1-C2
    - P4-S2-C7
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C4
    - P6-S3-C8
    - P6-S3-C13
    - P6-S3-C14
    - P6-S3-C16
    - P7-S1-C1
    - P7-S1-C3
    - P7-S1-C5
    - P7-S1-C6
    - P8-S1-C1
    - P8-S1-C4
    - P8-S1-C13
    - P8-S1-C15
    - P8-S2-C3
    - P8-S2-C5
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C10
    - P8-S2-C12
    - P8-S3-C1
    - P8-S3-C2
    - P9-S1-C1
    - P9-S1-C10
    - P9-S1-C11
    - P9-S2-C2
    - P10-S1-C2
    - P10-S1-C4
    - P10-S1-C5
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C11
    - P11-S1-C12
    - P11-S2-C3
    - P11-S2-C4
    - P11-S2-C5
    - P11-S2-C7
    - P11-S2-C9
    - P11-S2-C10
    - P11-S3-C5
    - P11-S3-C6
    - P12-S1-C1
    - P12-S1-C10
    - P12-S1-C11
    - P12-S2-C5
    - P12-S2-C10
    - P12-S3-C6
    - P12-S3-C7
    - P12-S3-C8
    - P12-S3-C9
    - P12-S3-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-8-2
    - TABLE-3-page-9-3
    - TABLE-4-page-11-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C1
      - P6-S2-C3
      - P6-S3-C8
      - P8-S1-C10
      - P12-S2-C3
      - P12-S2-C4
      - P15-S3-C36
      recruited_sample:
      - P1-S1-C5
      - P3-S3-C8
      - P3-S3-C9
      - P5-S1-C6
      - P5-S2-C1
      - P6-S3-C8
      - P12-S2-C3
      - P15-S3-C36
      eligibility:
      - P3-S3-C10
      - P3-S3-C11
      - P3-S4-C1
      - P3-S4-C2
      imaging_provenance:
      - P1-S1-C4
      - P3-S3-C1
      - P4-S3-C1
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C7
      - P6-S1-C4
      - P7-S1-C7
      imaging_timing:
      - P1-S1-C5
      - P3-S3-C1
      - P4-S3-C1
      - P4-S3-C2
      - P5-S1-C3
      - P12-S1-C5
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S2-C12
      - P3-S3-C1
      - P3-S3-C3
      - P3-S3-C6
      limitations: []
      personal_factors:
      - P3-S2-C9
      - P3-S3-C4
      - P8-S1-C3
      - P8-S1-C16
      - P8-S2-C2
      - P14-S3-C6
      - P15-S3-C36
      tested_personal_effects:
      - P8-S1-C3
      - P8-S2-C2
      - P11-S3-C5
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
      source_id: P1-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S4-C1
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
      source_id: P12-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S4-C19
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C23
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P3-S3-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S2-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P1-S2-C3
      - P3-S2-C8
      - P3-S3-C1
      - P3-S3-C4
      - P3-S3-C5
      - P4-S1-C4
      - P8-S2-C8
      - P8-S2-C9
      - P8-S3-C5
      - P9-S1-C2
      - P12-S1-C7
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C6
      - P12-S3-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S2-C3
      - P2-S2-C11
      - P2-S2-C12
      - P3-S3-C1
      - P3-S3-C3
      - P3-S3-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S2-C3
      - P4-S2-C5
      - P6-S1-C5
      - P8-S2-C7
      - P8-S2-C8
      - P8-S2-C10
      - P8-S3-C1
      - P9-S1-C2
      - P9-S1-C8
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      - P12-S1-C11
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C6
      - P12-S3-C8
      - P12-S3-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: analysis_restrictions
      source_ids:
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C11
      - P6-S3-C2
      - P6-S3-C3
      - P8-S1-C9
      - P8-S1-C11
      - P8-S2-C4
      - P8-S2-C5
      - P9-S1-C11
      - P12-S2-C7
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C13
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S1-C9
      - P3-S2-C1
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C7
      - P4-S1-C1
      - P8-S1-C2
      - P8-S1-C15
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C5
      - P9-S1-C1
      - P9-S1-C10
      - P9-S1-C11
      - P9-S1-C12
      - P10-S1-C2
      - P10-S1-C5
      - P11-S1-C1
      - P11-S1-C12
      - P11-S2-C3
      - P11-S2-C10
      - P12-S1-C13
      - P12-S1-C14
      - P12-S2-C3
      - P12-S2-C5
      - P12-S2-C7
      - P12-S2-C9
      - P12-S2-C10
      - P12-S2-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C4
      - P3-S2-C9
      - P6-S1-C3
      - P6-S1-C9
      - P6-S1-C10
      - P8-S1-C12
      - P8-S1-C13
      - P8-S1-C14
      - P9-S2-C4
      - P12-S3-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S2-C4
      - P3-S3-C8
      - P3-S4-C3
      - P5-S1-C6
      - P5-S2-C1
      - P6-S2-C8
      - P8-S1-C3
      - P8-S3-C5
      - P9-S2-C4
      - P12-S3-C11
      - P14-S3-C6
      - P15-S3-C36
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
      pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
      review_sha256: 40ab15fef4f6643cdfe699b643ead825b78661ae8acd2d904a89bfd59e7d8e0f
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
      - P1-S2-C6
      - P7-S1-C2
      source_result: Subacute connected speech (CIUs/min) was positively correlated
        with acute CIUs/min. This association survived FDR correction, as did the
        negative correlation with IFOF-lesion load. The source explicitly states that
        'Only IFOF-lesion load and acute CIUs/min survived the FDR correction' for
        subacute CIUs/min.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is a Pearson correlation between acute CIUs/min
            and subacute CIUs/min. The source confirms this specific correlation was
            performed and survived FDR correction (P7-S1-C2). The draft correctly
            identifies this as the core relationship.
          source_ids:
          - P1-S2-C6
          - P7-S1-C2
          - P6-S2-C7
        direction:
          answer: fits
          reason: The source states 'Subacute connected speech was correlated positively
            to acute CIUs/min' (P1-S2-C6). The draft claims a positive correlation.
            The direction is preserved.
          source_ids:
          - P1-S2-C6
        construct:
          answer: fits
          reason: Exposure is acute CIUs/min (behavioral measure of connected speech
            fluency/efficiency). Outcome is subacute CIUs/min. The draft correctly
            identifies these as behavioral measures. The patient measurement is non_imaging
            because the correlation is between two behavioral scores (CIUs/min), not
            between a behavioral score and an imaging metric (like lesion load or
            FA). Although the paper involves imaging, this specific relationship is
            behavioral-behavioral.
          source_ids:
          - P1-S2-C3
          - P4-S1-C8
          - P1-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the association survived
            FDR correction. This is a material qualifier supported by P7-S1-C2. The
            draft also notes small sample size as a limitation, which is supported
            by P12-S1-C14 and P12-S2-C3.
          source_ids:
          - P7-S1-C2
          - P12-S1-C14
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly identifies
            the FDR survival. The fact that this was part of a regression model is
            context, but the core relationship is the correlation. The draft does
            not omit any critical limitation that would change the interpretation
            of the correlation itself.
          source_ids:
          - P7-S1-C2
          - P8-S1-C14
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
      id: R004
      exposure:
        text: acute CIUs/min
      outcome:
        text: subacute connected speech
      analysis_label: Pearson correlation
      relation: association
      evidence_ids:
      - P1-S2-C6
      - P7-S1-C2
      - P9-S2-C4
      qualifier_ids:
      - P7-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
        source_review: _compare/relationships-2026-11-16/review-current/Desjardins2026
        source_status_sha256: 0d13a7a791fec80a93733ae695556ff78938a6fdc39202cc0a15a83c6dc48e2f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0bfadcecf6579d11d3823d9c81865c443f16e8d0cbce0b8571eabb79c7cf5d08
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C3
          page: 1
          text_layer_sha256: 0bfadcecf6579d11d3823d9c81865c443f16e8d0cbce0b8571eabb79c7cf5d08
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Naming and connected speech (quantified using correct information\
          \ \nunits per minute, CIUs/min) were assessed across the acute (0—5 days),\
          \ subacute (7—15 \ndays), and chronic (>6 months) phases."
        anchor_text: "Naming and connected speech (quantified using correct information\
          \ \nunits per minute, CIUs/min) were assessed across the acute (0—5 days),\
          \ subacute (7—15 \ndays), and chronic (>6 months) phases."
        excluded_fragments: []
        image_sha256: 026ac2e51c036352be58e01de96e91d69069aae719d45eae814df2abbe60f247
        transcription: '. Naming and connected speech (quantified using correct information

          units per minute, CIUs/min) were assessed across the acute (0–5 days), subacute
          (7–15

          days), and chronic (>6 months) phases'
      P3-S3-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 455a9ea33744caf742894877f4cc0f6dea3855afeb38db60b520d18a8b020537
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C8
          page: 3
          text_layer_sha256: 455a9ea33744caf742894877f4cc0f6dea3855afeb38db60b520d18a8b020537
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants\nTwenty-eight participants took part in this\
          \ study (12 women; \nmean age: 70 ± 13 years; mean education: 12 ± 4 years)."
        anchor_text: "Participants\nTwenty-eight participants took part in this study\
          \ (12 women; \nmean age: 70 ± 13 years; mean education: 12 ± 4 years)."
        excluded_fragments: []
        image_sha256: 5703d9dbf1f77f3086a61558ebaa75e387ad21dbd91e19343eabae15d0df47ac
        transcription: 'Participants


          Twenty-eight participants took part in this study (12 women; mean age: 70
          ± 13 years; mean education: 12 ± 4 years)'
      P4-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2c1d28ff533909a20384f77996388de881e8e29e32b050b13703c7875af43b08
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 943c2a9bd0ca47ddf32517c31de03ace53b269b6351a11cb1bc7ccaeee15049f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C4
          page: 4
          text_layer_sha256: 943c2a9bd0ca47ddf32517c31de03ace53b269b6351a11cb1bc7ccaeee15049f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Language assessment\nInitial assessment (acute phase) generally\
          \ occurred within the \nfirst 72 h post-stroke (mean = 2 ± 1 days), a follow-up\
          \ \nassessment (subacute phase) took place approximately ten \ndays post-stroke\
          \ (mean = 11 ± 2 days), and a third (chronic \nphase) was carried out at\
          \ least 6 months post-stroke \n(mean = 306 ± 109 days or 10.0 ± 3.5 months)."
        anchor_text: "Language assessment\nInitial assessment (acute phase) generally\
          \ occurred within the \nfirst 72 h post-stroke (mean = 2 ± 1 days), a follow-up\
          \ \nassessment (subacute phase) took place approximately ten \ndays post-stroke\
          \ (mean = 11 ± 2 days), and a third (chronic \nphase) was carried out at\
          \ least 6 months post-stroke \n(mean = 306 ± 109 days or 10.0 ± 3.5 months)."
        excluded_fragments: []
        image_sha256: d955ce3cd77ab5ef595b9bfcd042e22a3bf4539008f83172a7cd385f4e4479fd
        transcription: 'Language assessment


          Initial assessment (acute phase) generally occurred within the first 72
          h post-stroke (mean = 2 ± 1 days), a follow-up assessment (subacute phase)
          took place approximately ten days post-stroke (mean = 11 ± 2 days), and
          a third (chronic phase) was carried out at least 6 months post-stroke (mean
          = 306 ± 109 days or 10.0 ± 3.5 months)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Subacute connected speech was correlated \npositively to acute CIUs/min\
    \ and negatively to IFOF-lesion load."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
