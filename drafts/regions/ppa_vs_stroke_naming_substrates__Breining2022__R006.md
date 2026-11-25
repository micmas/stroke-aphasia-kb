---
id: ppa_vs_stroke_naming_substrates
name: PPA vs acute stroke naming substrates
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: naming_performance
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: naming_performance
  target_kind: impairment
  claim: No single brain region was associated with both object and action naming
    in both PPA and acute stroke; regions identified as associated with naming were
    specific to either the PPA or the acute stroke group.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: individuals with aphasia due to primary progressive aphasia (n=31)
      or acute left hemisphere stroke (n=37)
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size for neuroimaging analysis
  - Potential for LASSO model overfitting
  - Different imaging metrics used for PPA (volume) vs stroke (lesion percentage),
    preventing direct comparison within a single statistical model
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Comparison of regional brain metrics (normalized ROI
    volume for PPA; percentage of ROI lesion for acute stroke) associated with naming
    performance. PPA imaging was within 5 months of assessment; Acute stroke assessment
    was within 5 days of hospital admission. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P1-S2-C4, two-model
    agreement, human verification pending): . A subset of participants (N = 31 PPA,
    N = 37 acute stroke) provided neuroimaging data Original text-layer quotation
    is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:naming_performance
  citation: '@Breining2022'
  source_passages:
  - section: Original source P19-S1-C1
    page: 19
    quote: "\neight regions associated with object naming in either aetiology, none\
      \ were identiHed in \nboth stroke and PPA."
    supports: claim
  - section: Original source P19-S1-C2
    page: 19
    quote: "Likewise, of the seven regions associated with action naming in \neither\
      \ aetiology, none were identiHed for both stroke and PPA."
    supports: claim
  - section: Original source P19-S1-C3
    page: 19
    quote: "The regions that were \nassociated with both object and action naming\
      \ in PPA were distinct from those that were \nassociated with both types of\
      \ naming in stroke."
    supports: claim
  - section: Original source P21-S1-C9
    page: 21
    quote: "No single region was associated with both object and action naming in\
      \ \nboth PPA and acute stroke."
    supports: claim
  - section: Original source P21-S2-C3
    page: 21
    quote: "Rather, all regions identiHed in the analyses were associated \nwith naming\
      \ only for participants with PPA or only for participants with acute stroke."
    supports: claim
  - section: Original source P1-S2-C4
    page: 1
    quote: "A subset of participants (N = 31 PPA, N = 37 acute stroke) \nprovided\
      \ neuroimaging data."
    supports: sample
  - section: Original source P13-S1-C4
    page: 13
    quote: "Relating neuroimaging and behavioural data\nLeast Absolute Shrinkage and\
      \ Selection Operator (LASSO) regression (Tibshirani, 1996) \nwas used to evaluate\
      \ which ROIs were related to behaviour on object and action naming."
    supports: method
  - section: Original source P22-S1-C10
    page: 22
    quote: "Another important limitation is the sample size that was included in the\
      \ neuroimaging \nanalysis."
    supports: limitation
  - section: Original source P22-S1-C13
    page: 22
    quote: It is possible that the results were overHtted by the LASSO model.
    supports: limitation
  - section: Original source P22-S1-C3
    page: 22
    quote: "Next, it was not possible to directly compare the participants with PPA\
      \ and acute stroke \nusing exactly the same neuroimaging measures and thus we\
      \ could not directly compare the \ntwo groups within the same statistical model."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Breining2022
  proposal_id: R006
  review_status_sha256: 09bed46b3d09e82a0bb78bf2e55f4416ce05f724829f8e14bccb9c795ab021f4
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
        A/passages.json: 10b1e18d8e14b75d18690ebbafed518e696f77f93061cb630084689ee0f001c4
        A/raw.json: 033b8d694f53185d307342d9c9bbe6c60761aa9e4354a5248391f631f6e9bcbc
        A/source-units.json: 2702be3156d46d14069ee4070c01c3124f1c6523b15a8968933e680296aef457
        A/full-source-units.json: 52dc7129296e82a8b1532434cd80a0e3cbb3aa0ec435a26269dc756f38d2e3c1
        A/meta.json: f2ed4eb2ae185a877a57adb9d517ae8a44214b0f6e9e07009fd4342adb2540c1
        A/table-images/TABLE-5-page-18-1.png: 50048f9601394011b7fbcd2bae070512a5c97cf69c0ca6c86461ae99240ec200
        A/table-images/TABLE-3-page-10-1.png: 12e3f76d66206cc4ca8cafe091a586f3d460739e8075215bbb46fb0ff6fa6982
        A/table-images/TABLE-2-page-9-1.png: 2f494a642278bc999dc884b7aff42f2f1de6a0935db7730235ca042f4016fe54
        A/table-images/page-17.png: 29ef52d9ebd0011101091e2b367c5ea04fd61b3e24f697dda225c1b3a2355860
        A/table-images/TABLE-1-page-5-1.png: 659e9dd3c32d0a3c4e3bd464fa7548c727032bf4e18a190624a3f8cb8ae4fb44
        A/table-images/page-10.png: 388082ce1282126729ddf584da7fad0fd4c75e6c7046614fba59797343136c6a
        A/table-images/TABLE-2-page-8-1.png: 13fceb4767b15bc0503778247c041669c50a3cc0029f82c44204ee72ee907793
        A/table-images/TABLE-4-page-17-1.png: 13bc1306c411c5fa76085a2dc9d91b0775dcb06581216fe6ca54d96c028e5d40
        A/table-images/page-7.png: cc40eb053ff9adf70da73af2c0084d2c34e7197ff152dbe122df95eb012e969d
        A/table-images/page-5.png: 7b87a9d60dec381870bdc092d086959c3362c7635f8d4613659625721e73c072
        A/table-images/page-4.png: 8c198ea78768c86414d21fe45ff0c1f5f604919a235a5a39d13916324d842d3d
        A/table-images/TABLE-1-page-4-1.png: c36f480266db727c983f0bef661f801e1e5e6662b393cb5835c8abad94587129
        A/table-images/page-9.png: 203c0c6754dd0600320ce89beff111df28eed64ea8ec6e824991e43271e827da
        A/table-images/page-8.png: f2dae5a128069f659c64e718a9aadbd24c47f66cfb5c38997d422cfc155d64d4
        A/table-images/manifest.json: 0772560bedf152293ec1bb7b110f0cb80d28e4f1e81b635276b8e3f87fd02782
        A/table-images/TABLE-2-page-7-1.png: a4038108d75a2305b02f1e630d702ea0eeb9ed71e65fd3d1a7466a4143489329
        A/table-images/page-18.png: 4d48e8f08c3a6842132ece85ca93c023c0f0feb96f399319b5b7225c51bb3bf2
        A/clauses/window-11/raw.json: 3141a11996a1d0cdddfdd976ff65a4bd91cf5351057e36eb4ad17495b83fe0a4
        A/clauses/window-11/prompt.txt: fe99a7f5bdc67a1158a93cf961688f09d4d38d2226079dc45dafefd81f049eea
        A/clauses/window-11/meta.json: 526f29e9f3ae46ca6e1868d07b9ecdf14495b2af2d5ee7f84659bc959c59b2e9
        A/clauses/window-10/raw.json: 2d3f67aef39284462e699a46c41c679f3ccde84727b6fc6cbe92cc2eaaed0ccc
        A/clauses/window-10/prompt.txt: 18477cf9f8f3fe00edb86df7613c548c397c1552a00558e342b79022808bb554
        A/clauses/window-10/meta.json: 9ef57b6411e2db8272c062d9fabd308d7059c9f9332183d356b38f002aee2b9d
        A/clauses/window-03/raw.json: 5e832eb73c12ce69cd07b47f4487f2ca8c5c9a5135cc32d4e7d929f3d8aae924
        A/clauses/window-03/prompt.txt: a735cdc5aa61b9c56956b17ff01c409fb88f1530fcdffe4965e1dc106ef924ec
        A/clauses/window-03/meta.json: b50a835cc4f655c06b03473aac27da2151d290a6c8fc75136c74979bbdaecb77
        A/clauses/window-04/raw.json: 908fb0c3091149bcce211c87ca0d3351026c411c3f167440acd69b999fa2a1c5
        A/clauses/window-04/prompt.txt: fc31adab68eb74f2c4ff002e026b39457c6e87b207aeb277f6ab69e1167cf14c
        A/clauses/window-04/meta.json: 68cb385e6f4b1bf41812c3e2dd6b37515eecee380a676fedc78bab4131cec30c
        A/clauses/window-05/raw.json: 6212c8eb5ee876b8cb403ad85691a1e1c2543a4d55618e53c9f581a596496bb5
        A/clauses/window-05/prompt.txt: cb39508384a558d60369f7fae8273e32fbba4e0cbcdb9b755daab8d05b011426
        A/clauses/window-05/meta.json: b099380d1c3d25812b74a35062abb7aab4c8c1f8f74a1c08c86ecc8cee547724
        A/clauses/window-02/raw.json: e3b9e23b4a22e5dbb1137abce19b6a7ac4efb98e9167e90bd5f44c8af1767d7a
        A/clauses/window-02/prompt.txt: ee60b5cae2b7ddf27b95712d9695a73a53aef7ca783526ac488999712a684e87
        A/clauses/window-02/meta.json: 2f7d978fd330b2d63739206a4f107f30cb80692bb95559ac3e668310c9d92b61
        A/clauses/window-09/raw.json: 1c5e8f4343ee972ea09c9e014c40b8f8d8ca18ded63f49d81193a928f5253cb9
        A/clauses/window-09/prompt.txt: 7b30f411c0b5b3f829897993f7e78c333d85c67c143ff8a6a09b1d9efb517877
        A/clauses/window-09/meta.json: 9e0d766d24c9efe2b091db0366557cd4ef710edcacac2dd5c2e5974164ae5083
        A/clauses/window-07/raw.json: ab7ff688d961cc72da8a3777d4132a7ee98d71f63c87861906f815ac98b72548
        A/clauses/window-07/prompt.txt: 1b245d7864fd52c52d1c5fe7ba42b266c3e03413e3d90e2134c3b784c6845441
        A/clauses/window-07/meta.json: a0214ae085623da8c60eb48c1ab8f9420a184aeb20412b2e99587e74fc9068b6
        A/clauses/window-01/raw.json: 0dc65a6cbaede6810f32b9faf0b1f95523692a5635566c1ec40e86eedf31771a
        A/clauses/window-01/prompt.txt: fb7eaf2cc78ee10097fdcce715152c3ab46a0afbf8f22867277ce9981f4651b1
        A/clauses/window-01/meta.json: b262a721870a67ee2451cd6bcc67c60deff346b68bad7d79d6f494ff6c8b53c1
        A/clauses/window-06/raw.json: 400d3cc05bc454be53fe11cbf7f7bc2e5330276ec0b307e0de64b8f285b34af2
        A/clauses/window-06/prompt.txt: f494913e7db51657e24aaa2901861e21c32cb8b70d7da41a71aa471d304e5b7e
        A/clauses/window-06/meta.json: 0a3048824c41700028662349a75ae1a8ba05de5fe9002e4ddfc6fc9726ff1075
        A/clauses/window-08/raw.json: 5ae7dd13e95d56dfd6e8bcd3eca9841b8c82f28b3e3e3950a600fd55074cf05b
        A/clauses/window-08/prompt.txt: d4a681027f58ec398a804d256be8f5dc1c5661e528d3b28ba77619614f108f70
        A/clauses/window-08/meta.json: b52a1e6b8d9b937b2817c000f3c75d14f25034cb2da2c016eb39ff3ac8e6a5b0
        A/tables/TABLE-3-page-10-6/raw.json: c2e14831f90823043b29cc95fc797fc669ea252e52c261fbe3c6803fa18614a5
        A/tables/TABLE-3-page-10-6/prompt.txt: 7f17e9ad385a4f935223797c1cf0b9e39e58f340f2a78501e178b21a00e85f6d
        A/tables/TABLE-3-page-10-6/meta.json: 55a2cb95238d235e1baa08b3f2dfb531cba59a24ad14bb214453f1b4969ca0f7
        A/tables/TABLE-4-page-17-7/raw.json: 4bdfbc07173f4dcfabdc2ee61c9839685e2148515f4bfaf5dd558ca8dd8fd747
        A/tables/TABLE-4-page-17-7/prompt.txt: d755a4530df7cdfa2c9e73ae2544962f3bfb1c80c0e28eb79e62315d8f1d4ca6
        A/tables/TABLE-4-page-17-7/meta.json: 374d2849aedb223f6c326e5a4a1c66dbab1a8ff8c19acaf671b000968af0a2d8
        A/tables/TABLE-2-page-8-4/raw.json: cd2311cb6ecac853496051a68e52dc10d90375e49d35cc37c97417047532499e
        A/tables/TABLE-2-page-8-4/prompt.txt: 05982f7b988979d15dec80c3c54c5e4a6c7a970099224ee09cc702febb5658a4
        A/tables/TABLE-2-page-8-4/meta.json: 584265885e6ad37325e7c7c0a3cbab97e75a7867803c33540e17fabba4557fe0
        A/tables/TABLE-1-page-5-2/raw.json: b251c972381bddfa48dbdfdf6286e123ac43148da680d2a8444ef6b0ae23b800
        A/tables/TABLE-1-page-5-2/prompt.txt: dce9ebef6d1e1e00778f9b4d1513d9e0075085b32fb0e8672e589de1d329bce0
        A/tables/TABLE-1-page-5-2/meta.json: 285114e5a5600d31180389028816b2bce2973914cee578885606d3d1209bd580
        A/tables/TABLE-2-page-9-5/raw.json: 02f09e1c61eeb4147b37da85c83a01f5b32708fa9d78aaff1cc641d9a52aec51
        A/tables/TABLE-2-page-9-5/prompt.txt: 2f6ee31ed754e6c7e6ad4e8146b4ccf7a0cc534e69c48cd9354cdaacbcb331c6
        A/tables/TABLE-2-page-9-5/meta.json: 77dfd3478851082278e141fde440619cc439a5518d0d77a70ef7fe9a714f1494
        A/tables/TABLE-2-page-7-3/raw.json: 17ca0819fe9c4bf30696da661a2ac0b26e7547b0389d68c27ec6c0c8584ab080
        A/tables/TABLE-2-page-7-3/prompt.txt: 679e838a1a64d4c96c1affdbe5f9de3d3350a3ef6e87583657ee7dc84d0f1a87
        A/tables/TABLE-2-page-7-3/meta.json: d77caf7329275294aa98cba683afac1b43a93519d422d2c5984735df8a947812
        A/tables/TABLE-5-page-18-8/raw.json: bd8b6c6c9576e4c65ea978296774e1e765fcbaf13c30459bac867744e501abe6
        A/tables/TABLE-5-page-18-8/prompt.txt: 81d42487a2843450717af141e350eaac3bfb890ef978d221bc16326711269a30
        A/tables/TABLE-5-page-18-8/meta.json: 09368c164b413fcdc26531fc617da2f3d03ce53461c6ab7fdc3f06ce2ff608a6
        A/tables/TABLE-1-page-4-1/raw.json: feb00b473f82767c4a036e13a2f856f1c2d3ad4f1e2bb16df38478a91eb795b6
        A/tables/TABLE-1-page-4-1/prompt.txt: b4ca5040bcad9a65d56cd9c640777ad15df661efc1af03a4f8cf27c2c0c24759
        A/tables/TABLE-1-page-4-1/meta.json: 8a4cc9b5cfb923edc97178f68a750f3a1a2d7f4588e1de3cc7bce4e3b0f689f7
        B/passages.json: 10b1e18d8e14b75d18690ebbafed518e696f77f93061cb630084689ee0f001c4
        B/raw.json: 6b434b31eabafb62a775b8ac8403cd9971ceca7ad76c6d857fd6f830681c3a40
        B/source-units.json: 2702be3156d46d14069ee4070c01c3124f1c6523b15a8968933e680296aef457
        B/full-source-units.json: 52dc7129296e82a8b1532434cd80a0e3cbb3aa0ec435a26269dc756f38d2e3c1
        B/meta.json: bfd554232c7e5b02a719b217e85b036b09582c011786f77c623f329699720855
        B/table-images/TABLE-5-page-18-1.png: 50048f9601394011b7fbcd2bae070512a5c97cf69c0ca6c86461ae99240ec200
        B/table-images/TABLE-3-page-10-1.png: 12e3f76d66206cc4ca8cafe091a586f3d460739e8075215bbb46fb0ff6fa6982
        B/table-images/TABLE-2-page-9-1.png: 2f494a642278bc999dc884b7aff42f2f1de6a0935db7730235ca042f4016fe54
        B/table-images/page-17.png: 29ef52d9ebd0011101091e2b367c5ea04fd61b3e24f697dda225c1b3a2355860
        B/table-images/TABLE-1-page-5-1.png: 659e9dd3c32d0a3c4e3bd464fa7548c727032bf4e18a190624a3f8cb8ae4fb44
        B/table-images/page-10.png: 388082ce1282126729ddf584da7fad0fd4c75e6c7046614fba59797343136c6a
        B/table-images/TABLE-2-page-8-1.png: 13fceb4767b15bc0503778247c041669c50a3cc0029f82c44204ee72ee907793
        B/table-images/TABLE-4-page-17-1.png: 13bc1306c411c5fa76085a2dc9d91b0775dcb06581216fe6ca54d96c028e5d40
        B/table-images/page-7.png: cc40eb053ff9adf70da73af2c0084d2c34e7197ff152dbe122df95eb012e969d
        B/table-images/page-5.png: 7b87a9d60dec381870bdc092d086959c3362c7635f8d4613659625721e73c072
        B/table-images/page-4.png: 8c198ea78768c86414d21fe45ff0c1f5f604919a235a5a39d13916324d842d3d
        B/table-images/TABLE-1-page-4-1.png: c36f480266db727c983f0bef661f801e1e5e6662b393cb5835c8abad94587129
        B/table-images/page-9.png: 203c0c6754dd0600320ce89beff111df28eed64ea8ec6e824991e43271e827da
        B/table-images/page-8.png: f2dae5a128069f659c64e718a9aadbd24c47f66cfb5c38997d422cfc155d64d4
        B/table-images/manifest.json: 7e48d60b3b37f36f8c6bbdf073e7a2a626472e175e1e42af2bb8c9f076e8a830
        B/table-images/TABLE-2-page-7-1.png: a4038108d75a2305b02f1e630d702ea0eeb9ed71e65fd3d1a7466a4143489329
        B/table-images/page-18.png: 4d48e8f08c3a6842132ece85ca93c023c0f0feb96f399319b5b7225c51bb3bf2
        B/clauses/window-11/raw.json: 0b45591916bec52e76582636a01a67b2ef18996a5d9688b274c5fa05a584c956
        B/clauses/window-11/prompt.txt: fe99a7f5bdc67a1158a93cf961688f09d4d38d2226079dc45dafefd81f049eea
        B/clauses/window-11/meta.json: 5390620900a456bdad7de6b3a00aec4de1f5605a01d16ee9b1091243ad564b61
        B/clauses/window-10/raw.json: f662d4b2dc512318febf2c7e00e6903876360108deca7639bbc1b795c42cb35c
        B/clauses/window-10/prompt.txt: 18477cf9f8f3fe00edb86df7613c548c397c1552a00558e342b79022808bb554
        B/clauses/window-10/meta.json: 29d78fa16615ddf54fb2b675277a900c921149b6ef75ea20cec09eb0a7c1b929
        B/clauses/window-03/raw.json: 3381f35d4ccb531f62469a1621d267959cb11349e4b9e4f27fe50a90a257bae0
        B/clauses/window-03/prompt.txt: a735cdc5aa61b9c56956b17ff01c409fb88f1530fcdffe4965e1dc106ef924ec
        B/clauses/window-03/meta.json: cc876f6c0529fba6d52079ba51a85ab622d85354b2bee14caa047397b6098742
        B/clauses/window-04/raw.json: 2fd8bfca123469537ef541f6475cca5c3750d22a6200e931c289e831f2a5d66e
        B/clauses/window-04/prompt.txt: fc31adab68eb74f2c4ff002e026b39457c6e87b207aeb277f6ab69e1167cf14c
        B/clauses/window-04/meta.json: 3655daee198148c039d27def696483ca2797f0f0a85b5723e870e5356ab866fc
        B/clauses/window-05/raw.json: 9cc74a8ff55e56f9e242458c213a117762301425df9099cb3ed5380e134a1c49
        B/clauses/window-05/prompt.txt: cb39508384a558d60369f7fae8273e32fbba4e0cbcdb9b755daab8d05b011426
        B/clauses/window-05/meta.json: 8764b06c51c8af1f0f7e49178153679ad8a43bc7919236ef2f3222419ed184c3
        B/clauses/window-02/raw.json: 629e9fdebcdb44aa87a2acb776caf37d3f57ac4e1be9670d543dae2585b88c45
        B/clauses/window-02/prompt.txt: ee60b5cae2b7ddf27b95712d9695a73a53aef7ca783526ac488999712a684e87
        B/clauses/window-02/meta.json: 8aef610df829dc6ec3335de59956bb7fa13ae668e33acdd42a8ee372feab14a2
        B/clauses/window-09/raw.json: 1949386cc2e32f04436d0a7d40654d2d2f0d478efd6b3f4c0fd08a137373591b
        B/clauses/window-09/prompt.txt: 7b30f411c0b5b3f829897993f7e78c333d85c67c143ff8a6a09b1d9efb517877
        B/clauses/window-09/meta.json: 62a855523e04b9130da4a0fa22b57a6b3493198bc70bb0ddf8a037cbef861e99
        B/clauses/window-07/raw.json: ba15978c64db3cdb0e08b8c9134e9fa10137932210a3cde6b837c255236ab1ae
        B/clauses/window-07/prompt.txt: 1b245d7864fd52c52d1c5fe7ba42b266c3e03413e3d90e2134c3b784c6845441
        B/clauses/window-07/meta.json: 510402d05f1536bde0dedc198fde040d740fa0e14c2a4d3eb5d7673b7d999e18
        B/clauses/window-01/raw.json: 700e2c4677680b69b4b9d500a11654700f6f7dc82fe467a21ba3e2a1077f243e
        B/clauses/window-01/prompt.txt: fb7eaf2cc78ee10097fdcce715152c3ab46a0afbf8f22867277ce9981f4651b1
        B/clauses/window-01/meta.json: bf9fb8a5425a2f82aaa53debf0a0a14e4806ff7c233af7ce38d63d4fd680ce55
        B/clauses/window-06/raw.json: 47ea22feeed2e641f0ac80d82de3bcd182bd8767d49f440fc0d610bc93221e93
        B/clauses/window-06/prompt.txt: f494913e7db51657e24aaa2901861e21c32cb8b70d7da41a71aa471d304e5b7e
        B/clauses/window-06/meta.json: 8a434b38ae7675c24faea68275e68c2a47d89c372b662b176f0a792c040bf049
        B/clauses/window-08/raw.json: 8f665c52241b7dcfcb7b55bdd991da0d00d75cf49a70cc2e987f9787f1814d74
        B/clauses/window-08/prompt.txt: d4a681027f58ec398a804d256be8f5dc1c5661e528d3b28ba77619614f108f70
        B/clauses/window-08/meta.json: 3242020cd812e65301478996c05af348ae7984e82d51b62b17913851dd9448a5
        B/tables/TABLE-3-page-10-6/raw.json: 1ab4f02562c7b097b482f03227ea9a23b286812c857a0abbed6aabf3950f68da
        B/tables/TABLE-3-page-10-6/prompt.txt: 7f17e9ad385a4f935223797c1cf0b9e39e58f340f2a78501e178b21a00e85f6d
        B/tables/TABLE-3-page-10-6/meta.json: 22446087235bfd2a6526e7f9a302c242c0561bcee0437e9528c0b40ad172c8df
        B/tables/TABLE-4-page-17-7/raw.json: 5bc0b5c0fe2607d20a3aa02dfdb75e811f0a42ea3511ae185ae085adddf320fc
        B/tables/TABLE-4-page-17-7/prompt.txt: d755a4530df7cdfa2c9e73ae2544962f3bfb1c80c0e28eb79e62315d8f1d4ca6
        B/tables/TABLE-4-page-17-7/meta.json: 314f0a445d657feda35516a94c37b8cb3010b17902477714269a5f44d4ac4d7e
        B/tables/TABLE-2-page-8-4/raw.json: f468857ff32a664f559eb57e00c34d2ddcc1594a557c8dc08276c0a0725d9140
        B/tables/TABLE-2-page-8-4/prompt.txt: 05982f7b988979d15dec80c3c54c5e4a6c7a970099224ee09cc702febb5658a4
        B/tables/TABLE-2-page-8-4/meta.json: 30243bb02bcf5e5e2e4af02464b4a76f0f5ca2c36ad879dfe9e3ce34872fce94
        B/tables/TABLE-1-page-5-2/raw.json: 27446b13d09b895210eb0e188daa0dbe0e4d93171a5987df3f3f7c7efbb43a17
        B/tables/TABLE-1-page-5-2/prompt.txt: dce9ebef6d1e1e00778f9b4d1513d9e0075085b32fb0e8672e589de1d329bce0
        B/tables/TABLE-1-page-5-2/meta.json: 6556dba84feb891a44d2524a4fc0ea7c4c6506c3104852e8f30966c150e99993
        B/tables/TABLE-2-page-9-5/raw.json: 2794c912984c037ba43e6e25295ac6431ec9d74a83f88eac4e39ef91151b53c6
        B/tables/TABLE-2-page-9-5/prompt.txt: 2f6ee31ed754e6c7e6ad4e8146b4ccf7a0cc534e69c48cd9354cdaacbcb331c6
        B/tables/TABLE-2-page-9-5/meta.json: 6b8800d026885ed0d8500e265c75878ff0823baffce99b62caba3fb588761b33
        B/tables/TABLE-2-page-7-3/raw.json: 548e46a498d2ed46c9d6c339121a612cec2eb6320ca84eeaead37a7263c10465
        B/tables/TABLE-2-page-7-3/prompt.txt: 679e838a1a64d4c96c1affdbe5f9de3d3350a3ef6e87583657ee7dc84d0f1a87
        B/tables/TABLE-2-page-7-3/meta.json: 3fde362e7146b2f4e95d16962e536c07ddf4c44a330e313f7960b236c1e6755c
        B/tables/TABLE-5-page-18-8/raw.json: 7b5856c0b0bae41fa978b985ebca79e5961ed0c36e951ef180ae9ec402f7a4cb
        B/tables/TABLE-5-page-18-8/prompt.txt: 81d42487a2843450717af141e350eaac3bfb890ef978d221bc16326711269a30
        B/tables/TABLE-5-page-18-8/meta.json: ad24638435de40ab37bccc184f27c62a13f45215576fc48cb264e2261759afa4
        B/tables/TABLE-1-page-4-1/raw.json: 91f26a68e587191c7dbf7a534eb24a787ba0e77da3638b59390f2e5c017a8c48
        B/tables/TABLE-1-page-4-1/prompt.txt: b4ca5040bcad9a65d56cd9c640777ad15df661efc1af03a4f8cf27c2c0c24759
        B/tables/TABLE-1-page-4-1/meta.json: 47c67b28b86832bdc1d1b45013deecd1410bcce366fe95269a7a12b3505d06dc
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
      pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
      source_review: _compare/relationships-2026-11-16/review-current/Breining2022
      source_status_sha256: f3490ba35556c35fd1fe9df1e458f0531c89d29299b9b2789e55a9b9b5d13f0b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: aetiology (PPA vs. acute stroke)
    outcome:
      text: naming-associated neural regions
    analysis_label: Cross-aetiology neural substrate comparison
    relation: association
    evidence_ids:
    - P19-S1-C1
    - P19-S1-C2
    - P19-S1-C3
    - P21-S1-C9
    - P21-S1-C10
    qualifier_ids:
    - P19-S1-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
      source_review: _compare/relationships-2026-11-16/review-current/Breining2022
      source_status_sha256: f3490ba35556c35fd1fe9df1e458f0531c89d29299b9b2789e55a9b9b5d13f0b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S1-C1
      - Result passage disposed without unit P2-S1-C3
      - Result passage disposed without unit P2-S1-C4
      - Result passage disposed without unit P9-S1-C4
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Accounting without a linked unit P14-S1-C3
      - Accounting without a linked unit P14-S1-C4
      - Accounting without a linked unit P14-S1-C6
      - Accounting without a linked unit P15-S1-C4
      - Accounting without a linked unit P15-S1-C5
      - Unaccounted source passage P15-S1-C5
      - Unaccounted source passage P14-S1-C4
      - Unaccounted source passage P14-S1-C3
      - Unaccounted source passage P15-S1-C4
      - Unaccounted source passage P14-S1-C6
      - Result passage disposed without unit P15-S1-C6
      - Result passage disposed without unit P16-S1-C3
      - Result passage disposed without unit P16-S1-C5
      - Result passage disposed without unit P16-S2-C5
      - Result passage disposed without unit P16-S2-C6
      - Result passage disposed without unit P16-S2-C7
      - Accounting without a linked unit P18-S1-C3
      - Accounting without a linked unit P18-S1-C4
      - Accounting without a linked unit P18-S1-C5
      - Accounting without a linked unit P18-S1-C6
      - Accounting without a linked unit P18-S2-C6
      - Unaccounted source passage P18-S1-C3
      - Unaccounted source passage P18-S1-C5
      - Unaccounted source passage P18-S2-C6
      - Unaccounted source passage P18-S1-C6
      - Unaccounted source passage P18-S1-C4
      - Result passage disposed without unit P19-S1-C10
      - Accounting without a linked unit P19-S1-C2
      - Accounting without a linked unit P19-S1-C3
      - Result passage disposed without unit P19-S1-C9
      - Unaccounted source passage P19-S1-C3
      - Unaccounted source passage P19-S1-C2
      - Result passage disposed without unit P19-S1-C11
      - Accounting without a linked unit P19-S1-C12
      - Accounting without a linked unit P19-S2-C2
      - Accounting without a linked unit P19-S2-C6
      - Accounting without a linked unit P19-S2-C7
      - Accounting without a linked unit P20-S1-C1
      - Accounting without a linked unit P20-S1-C4
      - Unaccounted source passage P19-S2-C6
      - Unaccounted source passage P19-S2-C2
      - Unaccounted source passage P19-S1-C12
      - Unaccounted source passage P20-S1-C1
      - Unaccounted source passage P20-S1-C4
      - Unaccounted source passage P19-S2-C7
      - Result passage disposed without unit P20-S1-C11
      - Result passage disposed without unit P20-S1-C13
      - Result passage disposed without unit P20-S1-C17
      - Result passage disposed without unit P20-S1-C7
      - Result passage disposed without unit P21-S1-C8
      - Result passage disposed without unit P21-S2-C5
      - Accounting without a linked unit P22-S1-C1
      - Unaccounted source passage P22-S1-C1
      - Accounting without a linked unit P22-S2-C8
      - Accounting without a linked unit P23-S1-C8
      - Unaccounted source passage P23-S1-C8
      - Unaccounted source passage P22-S2-C8
      unattached_null_or_qualifier_ids:
      - P2-S1-C4
      - P11-S1-C4
      - P18-S1-C3
      - P18-S1-C4
      - P18-S1-C5
      - P20-S1-C17
      - P22-S1-C1
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 237
      unselected_timing_passages:
      - P1-S1-C13
      - P1-S1-C16
      - P1-S2-C4
      - P5-S1-C1
      - P5-S1-C5
      - P5-S1-C11
      - P6-S2-C3
      - P6-S2-C7
      - P6-S2-C10
      - P19-S1-C7
      - P22-S1-C12
      - P23-S1-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: limitations
        source_ids:
        - P21-S2-C12
        - P21-S2-C13
        - P21-S2-C14
        - P21-S2-C15
        - P21-S2-C16
        - P22-S1-C13
        - P22-S2-C4
        - P22-S2-C5
        - P22-S2-C6
        - P22-S2-C7
        - P22-S2-C8
        - P22-S2-C9
        - P22-S2-C10
        - P22-S2-C11
        - P22-S2-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      - TABLE-2-page-8-4
      - TABLE-2-page-9-5
      - TABLE-3-page-10-6
      - TABLE-4-page-17-7
      - TABLE-5-page-18-8
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      - TABLE-2-page-8-4
      - TABLE-2-page-9-5
      - TABLE-3-page-10-6
      - TABLE-4-page-17-7
      - TABLE-5-page-18-8
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P14-S1
        - P15-S1
        - P16-S2
        - P17-S1
        - P17-S2
        - P18-S1
        - P18-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
      source_review: _compare/relationships-2026-11-16/review-current/Breining2022
      source_status_sha256: f3490ba35556c35fd1fe9df1e458f0531c89d29299b9b2789e55a9b9b5d13f0b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P2-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Reports double dissociation in behavioral performance.
    - source_id: P2-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of neuroimaging results.
    - source_id: P2-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of aetiology differences.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of symptom duration.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of age and education.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group performance data.
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Validation of assessment item matching.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot testing name agreement.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group performance data.
    - source_id: P12-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of ROI selection/exclusion.
    - source_id: P13-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological description of LASSO.
    - source_id: P13-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of ROIs used in stroke analysis.
    - source_id: P14-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of impairment in PPA group.
    - source_id: P14-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of impairment in stroke group.
    - source_id: P14-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of impairment on HANA.
    - source_id: P15-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies participants with impaired BNT but intact HANA.
    - source_id: P15-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies participants with impaired HANA but intact BNT.
    - source_id: P15-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Concludes these patterns constitute a double dissociation.
    - source_id: P16-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant performance differences between tasks.
    - source_id: P16-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports individuals meeting both impairment and significance criteria.
    - source_id: P16-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Lists ROIs associated with BNT performance in PPA.
    - source_id: P16-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null independent significance for PPA object naming predictors.
    - source_id: P16-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Lists ROIs associated with HANA performance in PPA.
    - source_id: P16-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports null independent significance for PPA action naming predictors.
    - source_id: P17-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Lists ROIs associated with BNT performance in stroke.
    - source_id: P17-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant independent predictor (angular gyrus) for BNT in
        stroke.
    - source_id: P17-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Lists ROIs associated with HANA performance in stroke.
    - source_id: P17-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports null independent significance for HANA predictors in stroke.
    - source_id: P17-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 5/Figure 4.
    - source_id: P17-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend description.
    - source_id: P18-S1-C2
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Identifies common regions for both naming types in PPA.
    - source_id: P18-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies regions associated with object naming only in PPA.
    - source_id: P18-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies regions associated with action naming only in PPA.
    - source_id: P18-S1-C5
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Identifies common region (angular gyrus) for both naming types in stroke.
    - source_id: P18-S1-C6
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Identifies distinct regions for object vs action naming in stroke.
    - source_id: P18-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend description.
    - source_id: P18-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend description.
    - source_id: P19-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Reports no overlap in object naming regions between PPA and stroke.
    - source_id: P19-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Reports no overlap in action naming regions between PPA and stroke.
    - source_id: P19-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports distinct common regions for PPA vs stroke.
    - source_id: P19-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Concludes different neural substrates for PPA and stroke.
    - source_id: P19-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General confirmation of hypotheses.
    - source_id: P19-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of double dissociation.
    - source_id: P20-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of double dissociation.
    - source_id: P20-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about different regions.
    - source_id: P20-S2-C3
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of PPA-specific naming regions.
    - source_id: P20-S2-C6
      disposition: repeated
      result_indexes:
      - 3
      - 4
      reason: Restatement of stroke-specific naming regions.
    - source_id: P20-S2-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of total lesion volume association with action naming.
    - source_id: P21-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 3
      - 4
      reason: Restatement of common regions.
    - source_id: P21-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of PPA common regions.
    - source_id: P21-S1-C6
      disposition: repeated
      result_indexes:
      - 3
      - 4
      reason: Restatement of stroke common region (angular gyrus).
    - source_id: P21-S1-C8
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of different regions for different aetiologies.
    - source_id: P21-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports no single region associated with both naming types across both
        aetiologies.
    - source_id: P21-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Reports all identified regions were aetiology-specific.
    - source_id: P21-S2-C3
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of aetiology-specific associations.
    - source_id: P22-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of double dissociation.
    unresolved_coverage:
    - source_id: P21-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P17-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S1-C3
    - P2-S1-C4
    - P6-S1-C6
    - P6-S1-C7
    - P9-S1-C4
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    - P12-S2-C10
    - P13-S1-C1
    - P13-S1-C2
    - P14-S1-C3
    - P14-S1-C4
    - P14-S1-C6
    - P15-S1-C6
    - P16-S2-C6
    - P16-S2-C8
    - P17-S1-C5
    - P17-S1-C7
    - P17-S1-C8
    - P17-S1-C13
    - P17-S2-C4
    - P18-S1-C2
    - P18-S1-C5
    - P18-S1-C13
    - P18-S1-C14
    - P18-S2-C6
    - P19-S1-C4
    - P19-S1-C9
    - P19-S1-C10
    - P19-S1-C11
    - P19-S1-C12
    - P19-S2-C2
    - P19-S2-C6
    - P19-S2-C7
    - P20-S1-C1
    - P20-S1-C4
    - P20-S1-C5
    - P20-S1-C6
    - P20-S1-C7
    - P20-S1-C10
    - P20-S1-C11
    - P20-S1-C13
    - P20-S1-C17
    - P20-S2-C3
    - P20-S2-C6
    - P20-S2-C8
    - P21-S1-C4
    - P21-S1-C5
    - P21-S1-C6
    - P21-S1-C8
    - P21-S2-C3
    - P21-S2-C5
    - P22-S1-C1
    - P22-S2-C8
    - P23-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-1-page-5-2
    - TABLE-2-page-7-3
    - TABLE-2-page-8-4
    - TABLE-2-page-9-5
    - TABLE-3-page-10-6
    - TABLE-4-page-17-7
    - TABLE-5-page-18-8
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S1-C5
      - P6-S1-C9
      - P6-S2-C8
      recruited_sample:
      - P5-S1-C1
      - P5-S1-C11
      - P6-S2-C3
      - P6-S2-C10
      eligibility:
      - P6-S1-C4
      - P6-S1-C5
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      imaging_provenance:
      - P11-S1-C14
      - P11-S2-C2
      - P11-S2-C3
      - P12-S2-C2
      - P12-S2-C3
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      imaging_timing:
      - P6-S1-C9
      - P11-S1-C15
      outcome_timing:
      - P11-S1-C15
      outcome_definition:
      - P11-S1-C10
      - P14-S1-C1
      - P14-S1-C5
      - P14-S1-C12
      validation:
      - P13-S1-C9
      analysis_restrictions:
      - P13-S2-C5
      - P13-S2-C7
      dependent_variable_statement:
      - P13-S2-C3
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P12-S1-C5
      - P12-S1-C6
      - P13-S1-C3
      - P13-S2-C4
      - P13-S2-C6
      - P16-S2-C3
      - P17-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C11
      - P6-S1-C3
      - P6-S1-C7
      - P6-S2-C3
      - P6-S2-C5
      - P6-S2-C9
      - P10-S1-C2
      - P10-S1-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: limitations
      source_ids:
      - P21-S2-C12
      - P21-S2-C13
      - P21-S2-C14
      - P21-S2-C15
      - P21-S2-C16
      - P22-S1-C13
      - P22-S2-C4
      - P22-S2-C5
      - P22-S2-C6
      - P22-S2-C7
      - P22-S2-C8
      - P22-S2-C9
      - P22-S2-C10
      - P22-S2-C11
      - P22-S2-C12
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
      pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
      review_sha256: 09bed46b3d09e82a0bb78bf2e55f4416ce05f724829f8e14bccb9c795ab021f4
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
      - P19-S1-C1
      - P19-S1-C2
      - P19-S1-C3
      - P21-S1-C9
      - P21-S1-C10
      source_result: The study found that distinct neural substrates were identified
        for PPA and acute stroke. Specifically, no single brain region was associated
        with both object and action naming in both PPA and acute stroke; regions identified
        as associated with naming were specific to either the PPA or the acute stroke
        group.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the cross-aetiology comparison
            of neural substrates for naming. The source explicitly states that different
            regions were identified for PPA vs. stroke (P19-S1-C4, P21-S1-C8) and
            that no single region was associated with both object and action naming
            in both groups (P21-S1-C9).
          source_ids:
          - P19-S1-C1
          - P19-S1-C2
          - P19-S1-C3
          - P21-S1-C9
          - P21-S1-C10
        direction:
          answer: fits
          reason: The claim that 'no single brain region was associated with both
            object and action naming in both PPA and acute stroke' accurately reflects
            the source's finding of distinct substrates (P19-S1-C1, P19-S1-C2, P21-S1-C9).
            The direction of the finding (distinctness/lack of overlap) is preserved.
          source_ids:
          - P19-S1-C1
          - P19-S1-C2
          - P21-S1-C9
        construct:
          answer: fits
          reason: 'The exposure (aetiology: PPA vs. acute stroke) and outcome (naming-associated
            neural regions) are correctly identified. The patient measurement is correctly
            classified as template_lesion_overlap, as the study uses atlas-based segmentation
            (MRI Cloud) to calculate ROI volumes for PPA and lesion percentages for
            stroke, rather than patient-specific diffusion tractography.'
          source_ids:
          - P11-S2-C2
          - P12-S2-C6
          - P13-S1-C4
        qualifications:
          answer: fits
          reason: The proposed core includes relevant qualifications regarding timing
            (PPA imaging within 5 months, stroke assessment within 5 days) and limitations
            (small sample size, LASSO overfitting risk, inability to directly compare
            groups in a single model due to different metrics). These align with the
            source passages P6-S1-C9, P6-S2-C7, P22-S1-C10, P22-S1-C13, and P22-S1-C3.
          source_ids:
          - P6-S1-C9
          - P6-S2-C7
          - P22-S1-C3
          - P22-S1-C10
          - P22-S1-C13
        missing_material_caveat:
          answer: fits
          reason: The core includes the critical limitation that different imaging
            metrics (volume vs. lesion %) prevented direct statistical comparison
            within a single model (P22-S1-C3). It also notes the small sample size
            and potential overfitting (P22-S1-C10, P22-S1-C13). No material caveats
            that change the interpretation of the 'distinct substrates' finding are
            omitted.
          source_ids:
          - P22-S1-C3
          - P22-S1-C10
          - P22-S1-C13
      optional_pending:
      - Specific p-values and effect sizes for individual regions are not transcribed
        in the core, as this is a qualitative draft.
      - Exact sample sizes for the neuroimaging subset (N=31 PPA, N=37 stroke) are
        mentioned in source but not explicitly in the core's sample_n field, though
        population field mentions them.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values and effect sizes for individual regions are not transcribed
      in the core, as this is a qualitative draft.
    - Exact sample sizes for the neuroimaging subset (N=31 PPA, N=37 stroke) are mentioned
      in source but not explicitly in the core's sample_n field, though population
      field mentions them.
    normalizations:
    - field: sample.n
      original: 68
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R006
      exposure:
        text: aetiology (PPA vs. acute stroke)
      outcome:
        text: naming-associated neural regions
      analysis_label: Cross-aetiology neural substrate comparison
      relation: association
      evidence_ids:
      - P19-S1-C1
      - P19-S1-C2
      - P19-S1-C3
      - P21-S1-C9
      - P21-S1-C10
      qualifier_ids:
      - P19-S1-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
        source_review: _compare/relationships-2026-11-16/review-current/Breining2022
        source_status_sha256: f3490ba35556c35fd1fe9df1e458f0531c89d29299b9b2789e55a9b9b5d13f0b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb7041c5e30bdccf3937563b12e9e92e005cd88a30573f071de3cd5d840e9710
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5c9f7a685df0af7187fc3263ddad4cd12cf9b6bcd95f5c46516c62257a331df1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C4
          page: 1
          text_layer_sha256: 5c9f7a685df0af7187fc3263ddad4cd12cf9b6bcd95f5c46516c62257a331df1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A subset of participants (N = 31 PPA, N = 37 acute stroke)\
          \ \nprovided neuroimaging data."
        anchor_text: "A subset of participants (N = 31 PPA, N = 37 acute stroke) \n\
          provided neuroimaging data."
        excluded_fragments: []
        image_sha256: 25018412475c0b1c8f4e27b84f1a4c3004122a99e90a4b336b694e5f3b0a87c5
        transcription: . A subset of participants (N = 31 PPA, N = 37 acute stroke)
          provided neuroimaging data
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 19
  quote: "\neight regions associated with object naming in either aetiology, none\
    \ were identiHed in \nboth stroke and PPA."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
