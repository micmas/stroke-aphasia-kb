---
id: fluency_type
name: fluency type
kind: classical
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: There was no significant difference in aphasia severity between the fluent
    and non-fluent groups at 6 months post stroke.
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: Patients with left hemisphere stroke and language impairment
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
  - Small sample size
  - Selected group of patients able to tolerate 45-minute MRI scanning in the acute
    stage
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Categorization into fluent versus non-fluent aphasia
    types based on a cut-off of 4 on the WAB-R fluency scale. The fluent group presented
    with significantly less severe aphasia at baseline compared to the non-fluent
    group. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P11-S2-C4, two-model agreement, human
    verification pending): Also, our observations reflect results derived from a selected
    group of patients that were able to tolerate a 45-min MRI scanning session in
    the acute stage of stroke Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:aphasia_severity
  citation: '@Forkel2014'
  source_passages:
  - section: Original source P8-S1-C1
    page: 8
    quote: "\nlost at 6 months [Aphasia Quotient(ﬂuent) = 88.9 \x02 9.1, Aphasia\n\
      Quotient(non-ﬂuent) = 84.2 \x02 8.1;\nt(14)=\n\x031.03,\nP 4 0.05]."
    supports: claim
  - section: Original source P5-S2-C10
    page: 5
    quote: 'The secondary analysis addressed group differences between sex,

      ﬂuent versus non-ﬂuent aphasia types (deﬁned according to a cut-

      off of 4 on the WAB-R ﬂuency scale), and thrombolysis groups

      (thrombolysed versus non thrombolysed).'
    supports: method
  - section: Original source P7-S3-C3
    page: 7
    quote: "At baseline, the ﬂuent group presented with less severe aphasia (as\n\
      estimated by theAphasiaQuotient score) comparedtothenon-ﬂuent\ngroup [Aphasia\
      \ Quotient(ﬂuent) = 64.4 \x02 25.2, Aphasia Quotient(non-\nﬂuent) = 32.1 \x02\
      \ 21.9; t(14) = \x032.85, P 5 0.01]."
    supports: confounders
  - section: Original source P3-S3-C2
    page: 3
    quote: "Sixteen patients completed\nthe follow-up assessment (10 males; mean age\
      \ 60 \x02 17 years; age\nrange 28–87 years)."
    supports: sample
  - section: Original source P11-S2-C4
    page: 11
    quote: 'Also, our observations reﬂect results derived from a selected group

      of patients that were able to tolerate a 45-min MRI scanning

      session in the acute stage of stroke.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Forkel2014
  proposal_id: R012
  review_status_sha256: e910e9d530c34ff0142f2764eaca68f9c1eb6b6b79900b75c8d765371909b4dd
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
        A/passages.json: 0007e2d892976442e1afc9a24a8db755f6a4bed541bcde2bf4418f33fc0a98fd
        A/raw.json: d95016a311a3383902aeb1fc78ea6fd4814abab29d1173cade2b6d2a7afc6700
        A/source-units.json: d6d63f6a75376914f56ea60cf3d2fac4de5dedbcb24ab7f050bc76270507179a
        A/full-source-units.json: 09b690f8fea132a6f2f71238ca8b95cab084bd4bac513175f1fd96ef748f4172
        A/meta.json: 4a11f551eea0f3779e9ad1af2b6637db8d8beaf005b434d094b320fa7ce852f4
        A/table-images/TABLE-1-page-5-1.png: 7eef748cd7f54adbf6e3e53844c0b3365bf7307051050989577209d16dc96e56
        A/table-images/TABLE-4-page-10-1.png: 3ce20d9043e731c7707f0c850a12e7d6d1250df06161d4b19fffca70d9f54519
        A/table-images/page-10.png: e56766d76be80a508bbf3afb8d9a07bcc6a187938ac0700564e5a8996a48a380
        A/table-images/TABLE-3-page-9-1.png: 860c66822108ac9e48f5146563c896f22e44ccb3a02f2b35a425085962cf401c
        A/table-images/page-7.png: cbb5e2cef7501e5735d2f34698eaea629f4ab302775660d4dbf82b7e9cd3a72f
        A/table-images/page-5.png: 9497587cd8146d836467a1fd949cc81cd42f2f2c46ecf6aa7aaa9cfd2efdfcad
        A/table-images/page-9.png: db1cab1d816fcaa78330abb7dc4abb612c1822bfcf1d1c41c001e29f80450848
        A/table-images/manifest.json: 5b678afc764059de2adf2d9cf501493ca78d4c9a2153c62ca8b48fc7e6124102
        A/table-images/TABLE-2-page-7-1.png: 1d2e89b219d8575db19af9c0d2ea60495bbb94657e44857a622dc51f4c02b0e8
        A/clauses/window-03/raw.json: c9cf4e2424cfafecb44c26fcb2e94f7de4ceae4580e6506b068ce45d86231a56
        A/clauses/window-03/prompt.txt: 28172bc7e1a6b3608704bf3aebaf6e6eec5e906ad06d2f8e268f40c82b4ef1d9
        A/clauses/window-03/meta.json: 5ec97a860a2767d6e44b40c496f9bf18e35f0b76bf85c4dc66a5ace83013fa03
        A/clauses/window-04/raw.json: 9657a254e6bd30a78030d35042c9861584c9e34091bfdb8c3d28f6df550f1472
        A/clauses/window-04/prompt.txt: d6dafbdcd262876317c7097c21b527399d7ecce40376c938e2338fe78bdbb95e
        A/clauses/window-04/meta.json: f53b2ff1a6d08c62cdf073e6f3180611c127fa13cac6df083c484cf829a61944
        A/clauses/window-05/raw.json: 6b8bf9dfb380d96b7a79d031fff34e79c25092dbfc2f8e0e0dadcf693e165b57
        A/clauses/window-05/prompt.txt: 775cbfdaf239218de1cf4837e234c5f33ecac8d70a33a141d7e2b33c100e6591
        A/clauses/window-05/meta.json: 5cefe22cdc4e419364d7167d8d0fbb78406d060d20f18be6fcc1b0c090b883df
        A/clauses/window-02/raw.json: 87ee7307d444df86f672a2e5d1213b2b18aa3a62808f0f268d11ab9adc2a2dcc
        A/clauses/window-02/prompt.txt: 076ceb821fe19197459a461dae34916dcfbd63a0016f9920a599fd6b03920479
        A/clauses/window-02/meta.json: f30b8a389d08587e3b3a8c00e6c6b158522969cc3fda74a2aa89bbc46bd0554b
        A/clauses/window-09/raw.json: 911b5f22fa5e9645a65e6e9637ee60203e1e334e0201b893aab1652b7a74fbc8
        A/clauses/window-09/prompt.txt: 69a440fa6f60d3e20c600d96615a88465a42f276d38f7b33050043120d1c6487
        A/clauses/window-09/meta.json: 1fb5674d142541f1cd17089322e585bb9e63cd6978ee8302ddb6750f2fdce10c
        A/clauses/window-07/raw.json: a71820c5728ab4f421b7795a7b33ac17b254f21584534d502114a9b3924884f1
        A/clauses/window-07/prompt.txt: fb08ad5d9a0b2b4fc50223ac8ae47584533c416897a5cc2ab343f0b8552def8e
        A/clauses/window-07/meta.json: 6d8b5949b900a00edf66cdbf6915a714ba9eb819007e5b38b232c75e8141f9eb
        A/clauses/window-01/raw.json: 9ce0dfe21f28aa00a98dca80ea3995e6aaf3d43b9ab85f14b4afcfc636f48011
        A/clauses/window-01/prompt.txt: 99b1ba4a5c466fa2ffda4e8e0b6a8250324d88e3c962d0dc445610946e5826d4
        A/clauses/window-01/meta.json: 229fd968c3feebcd081379a0a990669eee72d9e5462c66bfcaf527c9e6a740c9
        A/clauses/window-06/raw.json: f119e3b31286bc7243918f1614aee92f9c42f30346b181cb84f3d7f960b9df9e
        A/clauses/window-06/prompt.txt: e01d85ad385a6528d075e8ae3da44eec04a5950d8ab3d0ddf7fa0b1dc48bd345
        A/clauses/window-06/meta.json: b96c88e3d7336583d9c6f19b41ef4b57a986e5f2b082e362e95e6ffb384b81b2
        A/clauses/window-08/raw.json: 8bdcb31ed0a8f51e7d82d195561694145fb00a835cab67a29625377334a0f5ff
        A/clauses/window-08/prompt.txt: 5bee3f6418c74983ca593b903a22f574528683077eedd97321b3d142b79c0e9a
        A/clauses/window-08/meta.json: 7ccdc682abb40d84305247847e4863fe58030c1fa6b2d128b8851bfa5a663627
        A/tables/TABLE-1-page-5-1/raw.json: 98946c4813510b4a1cb257ddd213095fa7f5a2290ca54c103b99764efdc719b4
        A/tables/TABLE-1-page-5-1/prompt.txt: 81a11aea8d1f64778074fc312f6925f64bd763d8f48004662cff016c90b0eeb3
        A/tables/TABLE-1-page-5-1/meta.json: 464f53887e50ccfffeef6a63f4a8308a33ba8aa2303b99d854037e440f5f6789
        A/tables/TABLE-3-page-9-3/raw.json: 02a636aebfcc5afd156f7b7e6c1b40572e68ab423ac0725bfd49310bd2f2340e
        A/tables/TABLE-3-page-9-3/prompt.txt: 0c30b0c7f39812f0b2d90462833cd7615d73c185e9f7138c3afe16bb8fb1c7bc
        A/tables/TABLE-3-page-9-3/meta.json: 31b5e37af07b3ad29c6604e6eab67d69a6542f5d854a5fd03080bca2116bb553
        A/tables/TABLE-2-page-7-2/raw.json: 9d4d6eadc78b4a84753635add11684adb590a40ca47c52eedfcd58eed81bb786
        A/tables/TABLE-2-page-7-2/prompt.txt: d5c4e7118ff80300ea9634f98057ad5e47b21353a53731ffb9bc28dc46bd9fcb
        A/tables/TABLE-2-page-7-2/meta.json: 6cbcec9b271902922ed74264174ae446ffce7b41644c6edb13cdf4a868b713a2
        A/tables/TABLE-4-page-10-4/raw.json: 90c619c8057b9c50cb5ac514c6562b6a581b59ed29bc06bf887411b2dfc8eafd
        A/tables/TABLE-4-page-10-4/prompt.txt: 21259f70994e203c1200dc97f60ef3b1e7a5a34f7baeb4c353d16412e6100a07
        A/tables/TABLE-4-page-10-4/meta.json: 72d99deeccd51ce234941468ae0bc889c26be491ba370cf57972f9747cd7999a
        B/passages.json: 0007e2d892976442e1afc9a24a8db755f6a4bed541bcde2bf4418f33fc0a98fd
        B/raw.json: 93358800254cd2976167d93458e377c4bbc01345603c657f2f7c64fc2e3a9f21
        B/source-units.json: d6d63f6a75376914f56ea60cf3d2fac4de5dedbcb24ab7f050bc76270507179a
        B/full-source-units.json: 09b690f8fea132a6f2f71238ca8b95cab084bd4bac513175f1fd96ef748f4172
        B/meta.json: 08de9b986b708afc79dff5e7522af2f596bcb8b8c305d483d45d894d0c46a50e
        B/table-images/TABLE-1-page-5-1.png: 7eef748cd7f54adbf6e3e53844c0b3365bf7307051050989577209d16dc96e56
        B/table-images/TABLE-4-page-10-1.png: 3ce20d9043e731c7707f0c850a12e7d6d1250df06161d4b19fffca70d9f54519
        B/table-images/page-10.png: e56766d76be80a508bbf3afb8d9a07bcc6a187938ac0700564e5a8996a48a380
        B/table-images/TABLE-3-page-9-1.png: 860c66822108ac9e48f5146563c896f22e44ccb3a02f2b35a425085962cf401c
        B/table-images/page-7.png: cbb5e2cef7501e5735d2f34698eaea629f4ab302775660d4dbf82b7e9cd3a72f
        B/table-images/page-5.png: 9497587cd8146d836467a1fd949cc81cd42f2f2c46ecf6aa7aaa9cfd2efdfcad
        B/table-images/page-9.png: db1cab1d816fcaa78330abb7dc4abb612c1822bfcf1d1c41c001e29f80450848
        B/table-images/manifest.json: 55a97e7d5ec63e048b4be9cbb2449909a0abd556f447bae95e4c705d35fa355b
        B/table-images/TABLE-2-page-7-1.png: 1d2e89b219d8575db19af9c0d2ea60495bbb94657e44857a622dc51f4c02b0e8
        B/clauses/window-03/raw.json: e1103ab3d9a37c8391f50532a47966111e333d50dd784d868180ae2c91147f56
        B/clauses/window-03/prompt.txt: 28172bc7e1a6b3608704bf3aebaf6e6eec5e906ad06d2f8e268f40c82b4ef1d9
        B/clauses/window-03/meta.json: 421ffe22fe54a9f6763c4a5d1dedb77414848d384f21dfff78792df35f84c002
        B/clauses/window-04/raw.json: ee55ccc472117bf46f0309c159cdea8be801bc9afb6be944466f44a46a2af943
        B/clauses/window-04/prompt.txt: d6dafbdcd262876317c7097c21b527399d7ecce40376c938e2338fe78bdbb95e
        B/clauses/window-04/meta.json: a82345eb4b344a2b6cadc623d5ce705b82ceb5924abc7c0c7dc630523793dc44
        B/clauses/window-05/raw.json: 89ec0b43a69808c4a4811aa55ce64ae446c5f985be9fc1fe1b3a76accc548909
        B/clauses/window-05/prompt.txt: 775cbfdaf239218de1cf4837e234c5f33ecac8d70a33a141d7e2b33c100e6591
        B/clauses/window-05/meta.json: b44bf9c456910649aced3540274097a91531247e39cc0548bb5be586f3af3ad9
        B/clauses/window-02/raw.json: 618d966d93814723d54b7d2bf44423725e0f37e7a071ed21bbf19fb3829a487d
        B/clauses/window-02/prompt.txt: 076ceb821fe19197459a461dae34916dcfbd63a0016f9920a599fd6b03920479
        B/clauses/window-02/meta.json: c9c20bb3e4bdf03d5a35bd9ade84a2a68141242aaa678bdcf8a933a35bc11519
        B/clauses/window-09/raw.json: b931b5eed405754cabcfda8408751d3c595e4fc1f0de8f776def98b02b4bfb0f
        B/clauses/window-09/prompt.txt: 69a440fa6f60d3e20c600d96615a88465a42f276d38f7b33050043120d1c6487
        B/clauses/window-09/meta.json: 602271d1c7069d40746ad72e2cd699da03699ad3dee666b107d646928a21859b
        B/clauses/window-07/raw.json: 176930438059ce52c6a335a46c5bddcb1803dee02ea3916a738eae8ea4d1fed0
        B/clauses/window-07/prompt.txt: fb08ad5d9a0b2b4fc50223ac8ae47584533c416897a5cc2ab343f0b8552def8e
        B/clauses/window-07/meta.json: 2b385016d2c4f518ec2a871434251aba0c795ba59b3349e1918d10ee5effdf67
        B/clauses/window-01/raw.json: c5f92aee8503c7b3a5f8b038dfbaf042228c5284a01662e1913c9bacc45d8a06
        B/clauses/window-01/prompt.txt: 99b1ba4a5c466fa2ffda4e8e0b6a8250324d88e3c962d0dc445610946e5826d4
        B/clauses/window-01/meta.json: 267b2d02ed959ad73e9306cc831a48dae3dfaaf1720786ee3de6b0b43662bd2b
        B/clauses/window-06/raw.json: 0a10bf128602e99f5bf188205f32c5ac478f08009aac9525ed62471385ed3e69
        B/clauses/window-06/prompt.txt: e01d85ad385a6528d075e8ae3da44eec04a5950d8ab3d0ddf7fa0b1dc48bd345
        B/clauses/window-06/meta.json: 31aa6277f5f69a9632142a41678985143244c91286a5a971ba3ed6560959f003
        B/clauses/window-08/raw.json: 724529d081e434300f18090c61542262698151b4477cc128e4da09344ccb49f7
        B/clauses/window-08/prompt.txt: 5bee3f6418c74983ca593b903a22f574528683077eedd97321b3d142b79c0e9a
        B/clauses/window-08/meta.json: 047fddba0f5a5f6f4d3abf0d1b8b710c92f3df6edc66853e5deb44dafe04cb58
        B/tables/TABLE-1-page-5-1/raw.json: 095c00f389733638cd8a7681d158d09f5f8ab0a12824ac99adae6620bc65c0bb
        B/tables/TABLE-1-page-5-1/prompt.txt: 81a11aea8d1f64778074fc312f6925f64bd763d8f48004662cff016c90b0eeb3
        B/tables/TABLE-1-page-5-1/meta.json: 5d305cd9ddb2267370e38a5552690bd1201b8f5318dc6a4c212099d7cdc8e0c7
        B/tables/TABLE-3-page-9-3/raw.json: 8faf9d070dc3506feac4b85f72d0b03e0f62a3cea7833b0f4805253f868d07d7
        B/tables/TABLE-3-page-9-3/prompt.txt: 0c30b0c7f39812f0b2d90462833cd7615d73c185e9f7138c3afe16bb8fb1c7bc
        B/tables/TABLE-3-page-9-3/meta.json: 9efd210861b912a75e7b92a533f3d7eee71c8cb26561ba2cbfe32af16d4fa4df
        B/tables/TABLE-2-page-7-2/raw.json: 1b5c0a68288eff829ffbff0c4f7fcaa018d3e0c5f7afd5185b094d7b53c9a72b
        B/tables/TABLE-2-page-7-2/prompt.txt: d5c4e7118ff80300ea9634f98057ad5e47b21353a53731ffb9bc28dc46bd9fcb
        B/tables/TABLE-2-page-7-2/meta.json: 826fae3358cf14dc844083624d0fce342463a9a0b86fce97c4a0d0b4a124c7df
        B/tables/TABLE-4-page-10-4/raw.json: 49482b2caaeb07d4bfeee77bd18a68ba00ca0a3c5254afe74aa55147953f6c53
        B/tables/TABLE-4-page-10-4/prompt.txt: 21259f70994e203c1200dc97f60ef3b1e7a5a34f7baeb4c353d16412e6100a07
        B/tables/TABLE-4-page-10-4/meta.json: 40e4b0a4fea6700ff9155bb5f69b76b3136bf4161961e6a308c9040829a4e161
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
      pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
      source_review: _compare/relationships-2026-11-16/review-current/Forkel2014
      source_status_sha256: 245dfe6f46b10bb3b417d7ef41f9aab494ef1672af15470c2fd855c0255b5805
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: fluency (fluent vs non-fluent)
    outcome:
      text: aphasia severity (6 months)
    analysis_label: Group comparison
    relation: association
    evidence_ids:
    - P8-S1-C1
    qualifier_ids:
    - P9-S1-C5
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
      source_review: _compare/relationships-2026-11-16/review-current/Forkel2014
      source_status_sha256: 245dfe6f46b10bb3b417d7ef41f9aab494ef1672af15470c2fd855c0255b5805
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C17
      - Result passage disposed without unit P4-S1-C6
      - Result passage disposed without unit P6-S1-C12
      - Accounting without a linked unit P6-S1-C9
      - Accounting without a linked unit P6-S2-C2
      - Accounting without a linked unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C5
      - Result passage disposed without unit P6-S2-C6
      - Unaccounted source passage P6-S2-C5
      - Unaccounted source passage P6-S2-C2
      - Unaccounted source passage P6-S2-C3
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P6-S2-C4
      unattached_null_or_qualifier_ids:
      - P6-S1-C12
      - P6-S2-C4
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 196
      unselected_timing_passages:
      - P1-S2-C7
      - P1-S2-C8
      - P3-S2-C7
      - P3-S3-C2
      - P5-S1-C5
      - P5-S2-C14
      - P5-S2-C15
      - P11-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation: []
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-2
      - TABLE-3-page-9-3
      - TABLE-4-page-10-4
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-2
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
        - P7-S3
        - P8-S1
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
      source_review: _compare/relationships-2026-11-16/review-current/Forkel2014
      source_status_sha256: 245dfe6f46b10bb3b417d7ef41f9aab494ef1672af15470c2fd855c0255b5805
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies lesion size as independent predictor in left hemisphere.
    - source_id: P1-S2-C14
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Identifies age and right long segment volume as predictors in right
        hemisphere.
    - source_id: P1-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Describes increase in predictive power when adding right long segment.
    - source_id: P3-S3-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about participant exclusion after inspection.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability of anatomists.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of baseline measure reliability.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 14
      reason: Null correlation between baseline severity and 6-month score.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Initial non-significant model with all variables.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 16
      reason: Significant model with age, sex, and lesion size.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 16
      reason: Restatement of predictors identified in backward elimination.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion overlay map results.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Performance of the first-level left hemisphere model.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Non-significant improvement with left long segment.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Lesion size as independent predictor in left hemisphere.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Non-predictive models for left anterior/posterior segments.
    - source_id: P6-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of left hemisphere variability explanation.
    - source_id: P6-S2-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of 12% increase in predictive value.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Confirmation of lesion size as only independent predictor in left hemisphere.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion overlay map results.
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion overlay map results.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Null correlation between lesion size and left arcuate volumes.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Non-significant model adding sum of three left segments.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Non-predictive first-level right hemisphere model.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Significant improvement with right long segment.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Age and right long segment as independent predictors.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Marginal significance of gender and lesion size in right hemisphere.
    - source_id: P7-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right hemisphere first-level model variance.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Increase in predictive value to 57%.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 15
      reason: AICc values for right hemisphere models.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 15
      reason: Preference for four-predictor model based on AICc.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 15
      reason: Specificity of right long segment to predictive power.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Power calculation result.
    - source_id: P7-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Effect size of hierarchical regression model.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Power analysis conclusion.
    - source_id: P7-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive recovery rates (81.25% aphasic).
    - source_id: P7-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overall group improvement in language functioning.
    - source_id: P7-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of different recovery slopes.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that no patients deteriorated.
    - source_id: P7-S3-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Baseline difference between fluent and non-fluent groups.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Loss of difference between fluent and non-fluent groups at 6 months.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: No sex differences in severity at baseline or 6 months.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 13
      reason: No difference between thrombolysed and non-thrombolysed patients.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Negative correlation between lesion size and baseline severity.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Non-significant correlation between lesion size and follow-up severity.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of patients reaching normal language function.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Null correlations between FA and aphasia severity.
    - source_id: P10-S1-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of right long segment as predictive factor.
    - source_id: P10-S1-C4
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement that other segments were not correlated with recovery.
    - source_id: P10-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Restatement of importance of age, sex, and lesion size.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of lesion size as strongest predictor in left hemisphere.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of right long segment as good predictor.
    - source_id: P10-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of lesion size predictability in left hemisphere.
    - source_id: P10-S1-C13
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right hemisphere model improvement with DTI.
    - source_id: P10-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right hemisphere model variance (60%).
    unresolved_coverage:
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S3-C17
    - P4-S1-C6
    - P5-S1-C5
    - P6-S1-C6
    - P6-S1-C9
    - P6-S1-C12
    - P6-S2-C2
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C11
    - P6-S2-C12
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C9
    - P7-S1-C10
    - P7-S2-C9
    - P7-S2-C11
    - P7-S2-C12
    - P7-S2-C13
    - P7-S2-C14
    - P7-S2-C15
    - P7-S3-C2
    - P9-S1-C4
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C12
    - P10-S1-C13
    - P10-S2-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-7-2
    - TABLE-3-page-9-3
    - TABLE-4-page-10-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C2
      - P5-S2-C14
      recruited_sample:
      - P3-S2-C6
      - P3-S2-C9
      eligibility:
      - P3-S2-C8
      imaging_provenance:
      - P3-S3-C8
      - P3-S3-C10
      - P4-S1-C6
      imaging_timing:
      - P3-S2-C9
      - P3-S3-C9
      outcome_timing:
      - P3-S2-C12
      - P5-S2-C4
      - P7-S2-C14
      outcome_definition:
      - P3-S2-C10
      - P5-S2-C4
      validation:
      - P7-S1-C12
      analysis_restrictions:
      - P5-S1-C2
      - P5-S1-C5
      dependent_variable_statement:
      - P1-S2-C10
      - P5-S2-C4
      limitations:
      - P5-S1-C5
      - P11-S1-C10
      - P11-S2-C2
      - P11-S2-C4
      personal_factors:
      - P6-S1-C2
      tested_personal_effects:
      - P6-S1-C7
      - P7-S1-C8
      adjustment_roles:
      - P1-S2-C9
      - P4-S1-C10
      - P5-S2-C5
      - P6-S2-C2
      - P7-S1-C7
      - P8-S1-C11
      explicitly_not_adjusted:
      - P5-S1-C2
      descriptive_personal_factors:
      - P1-S2-C7
      - P5-S3-C2
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
      review_sha256: e910e9d530c34ff0142f2764eaca68f9c1eb6b6b79900b75c8d765371909b4dd
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
      - P8-S1-C1
      source_result: At 6 months post-stroke, there was no statistically significant
        difference in aphasia severity (Aphasia Quotient) between the fluent and non-fluent
        groups (t(14) = -1.03, P > 0.05), despite a significant difference at baseline.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P8-S1-C1 explicitly reports the comparison of Aphasia
            Quotient at 6 months between fluent and non-fluent groups. The proposed
            core correctly identifies this as a group comparison of aphasia severity
            at 6 months.
          source_ids:
          - P8-S1-C1
          - P5-S2-C10
        direction:
          answer: fits
          reason: The source reports P > 0.05 for the 6-month comparison, indicating
            no significant difference. The proposed core correctly labels this as
            'no_effect' (no statistically detected association/difference).
          source_ids:
          - P8-S1-C1
        construct:
          answer: fits
          reason: The exposure is fluency type (defined in P5-S2-C10) and the outcome
            is aphasia severity (Aphasia Quotient, P3-S2-C10). The measurement is
            behavioral (WAB-R), not imaging-based, so 'non_imaging' is correct. The
            timing is 6 months, matching the source.
          source_ids:
          - P5-S2-C10
          - P3-S2-C10
          - P8-S1-C1
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the fluent group
            had less severe aphasia at baseline (P7-S3-C3), which is a crucial context
            for interpreting the null finding at 6 months (convergence of scores).
            It also includes relevant limitations regarding sample selection (P11-S2-C4).
          source_ids:
          - P7-S3-C3
          - P11-S2-C4
        missing_material_caveat:
          answer: fits
          reason: The core captures the key caveat that baseline differences existed,
            which explains the lack of difference at follow-up. No other material
            caveats that would change the interpretation of this specific null result
            are omitted.
          source_ids:
          - P7-S3-C3
          - P8-S1-C1
      optional_pending:
      - Sample size (n=16) is mentioned in source P3-S3-C2 and P7-S2-C9 but not transcribed
        in the core fields; confirm if required for final draft.
      - Exact t-statistic and P-value details are not transcribed in the core claim,
        only the qualitative result.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=16) is mentioned in source P3-S3-C2 and P7-S2-C9 but not transcribed
      in the core fields; confirm if required for final draft.
    - Exact t-statistic and P-value details are not transcribed in the core claim,
      only the qualitative result.
    normalizations:
    - field: bucket
      original: impairments
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 16
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: 6 months post stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R012
      exposure:
        text: fluency (fluent vs non-fluent)
      outcome:
        text: aphasia severity (6 months)
      analysis_label: Group comparison
      relation: association
      evidence_ids:
      - P8-S1-C1
      qualifier_ids:
      - P9-S1-C5
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
        source_review: _compare/relationships-2026-11-16/review-current/Forkel2014
        source_status_sha256: 245dfe6f46b10bb3b417d7ef41f9aab494ef1672af15470c2fd855c0255b5805
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P8-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c2592b1a9eabbca92e55f38222121bf14db7fcb5ec3039a54c38a9df78c9c2f4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C1
          page: 8
          text_layer_sha256: 684012272e1da3d3fa4410adc96e2d953c99b5092ffe487b4b4ba4f4b548722b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "\nlost at 6 months [Aphasia Quotient(ﬂuent) = 88.9 \x02 9.1,\
          \ Aphasia\nQuotient(non-ﬂuent) = 84.2 \x02 8.1;\nt(14)=\n\x031.03,\nP 4\
          \ 0.05]."
        anchor_text: "lost at 6 months [Aphasia Quotient(ﬂuent) = 88.9 \x02 9.1, Aphasia\n\
          Quotient(non-ﬂuent) = 84.2 \x02 8.1;\nt(14)=\n\x031.03,\nP 4 0.05]."
        excluded_fragments: []
      P7-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9613af1a28773e0fa15d3ec238d8bbeed228436ca86abe3dbd844ab2d66152f9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S3-C3
          page: 7
          text_layer_sha256: 9613af1a28773e0fa15d3ec238d8bbeed228436ca86abe3dbd844ab2d66152f9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "At baseline, the ﬂuent group presented with less severe aphasia\
          \ (as\nestimated by theAphasiaQuotient score) comparedtothenon-ﬂuent\ngroup\
          \ [Aphasia Quotient(ﬂuent) = 64.4 \x02 25.2, Aphasia Quotient(non-\nﬂuent)\
          \ = 32.1 \x02 21.9; t(14) = \x032.85, P 5 0.01]."
        anchor_text: "At baseline, the ﬂuent group presented with less severe aphasia\
          \ (as\nestimated by theAphasiaQuotient score) comparedtothenon-ﬂuent\ngroup\
          \ [Aphasia Quotient(ﬂuent) = 64.4 \x02 25.2, Aphasia Quotient(non-\nﬂuent)\
          \ = 32.1 \x02 21.9; t(14) = \x032.85, P 5 0.01]."
        excluded_fragments: []
      P3-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 393e465b29c455b2dfa16f0e5cdb5cc23fdc859be0ea8ed535e0f71a119abe61
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C2
          page: 3
          text_layer_sha256: 393e465b29c455b2dfa16f0e5cdb5cc23fdc859be0ea8ed535e0f71a119abe61
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Sixteen patients completed\nthe follow-up assessment (10 males;\
          \ mean age 60 \x02 17 years; age\nrange 28–87 years)."
        anchor_text: "Sixteen patients completed\nthe follow-up assessment (10 males;\
          \ mean age 60 \x02 17 years; age\nrange 28–87 years)."
        excluded_fragments: []
      P11-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4042eb126f12858b3530d4676b384a5fc71073a0baaeec926de6737761bbb0f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6be0891cdb60e08c1abbaf104c249399ef34b70e65eec8e5d69ac6ad1f47bd9e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P11-S2-C4
          page: 11
          text_layer_sha256: 6be0891cdb60e08c1abbaf104c249399ef34b70e65eec8e5d69ac6ad1f47bd9e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Also, our observations reﬂect results derived from a selected
          group

          of patients that were able to tolerate a 45-min MRI scanning

          session in the acute stage of stroke.'
        anchor_text: 'Also, our observations reﬂect results derived from a selected
          group

          of patients that were able to tolerate a 45-min MRI scanning

          session in the acute stage of stroke.'
        excluded_fragments: []
        image_sha256: 50ffc598366cff23e3207f8a54a191c51396a7542e83ad2b3370ccbe67b39a62
        transcription: Also, our observations reflect results derived from a selected
          group of patients that were able to tolerate a 45-min MRI scanning session
          in the acute stage of stroke
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: "\nlost at 6 months [Aphasia Quotient(ﬂuent) = 88.9 \x02 9.1, Aphasia\nQuotient(non-ﬂuent)\
    \ = 84.2 \x02 8.1;\nt(14)=\n\x031.03,\nP 4 0.05]."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
