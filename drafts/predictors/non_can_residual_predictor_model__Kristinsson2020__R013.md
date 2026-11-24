---
id: non_can_residual_predictor_model
name: non-CAN residual score predictor model
kind: predictor
findings:
- id: f1
  target: non_can_residual_scores
  target_kind: impairment
  claim: In a post hoc analysis contrasting subject versus object gaps, a model including
    proportional damage to pSTG, SMG, IFGop, and STG predicted non-CAN residual scores,
    with pSTG identified as the strongest predictor.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: individuals with acute left-hemisphere stroke
    phase: not_reported
    time_post_onset: acute phase (<20 days poststroke); MRI and behavioral testing
      conducted within a day of each other
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - ROI-based approach represents each region by a single proportional damage value,
    compromising spatial resolution
  - behavioral performance was only examined in relation to structural cortical damage
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A stepwise regression model using proportional damage
    to predefined language ROIs (pSTG, SMG, IFGop, and STG) to predict non-CAN residual
    scores. non-CAN residual scores were calculated by including proportional accuracy
    on canonical sentences as a covariate to isolate the effect of non-canonical structures;
    the post hoc analysis specifically contrasted cleft sentences and referential
    wh-questions with subject gaps versus those with object gaps. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P1-S1-C5, two-model agreement, human verification pending): . One
    hundred four individuals with acute aphasia (<20 days poststroke) were included
    in the study Original text-layer quotation is preserved below. PDF image reading
    (P4-S1-C11, two-model agreement, human verification pending): In most cases, MRI
    and behavioral examinations were conducted within 3 days of hospital admission,
    although a handful of patients underwent examination up to 20 days after stroke
    because of complications secondary to the stroke Original text-layer quotation
    is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:non_can_residual_scores
  citation: '@Kristinsson2020'
  source_passages:
  - section: Original source P13-S2-C2
    page: 13
    quote: 'Thus, we performed a

      post hoc analysis contrasting performance on cleft sen-

      tences with subject gaps and referential wh-questions with

      subject gap and main verbs (canonical sentences) to the

      same sentence structures but with object gaps rather than

      subject gaps (noncanonical sentences).'
    supports: method
  - section: Original source P13-S2-C4
    page: 13
    quote: 'For non-CAN resid-

      ual scores, the analysis revealed a similar model explaining

      41.1% of the variance in scores.'
    supports: claim
  - section: Original source P13-S2-C5
    page: 13
    quote: 'The pSTG was identified

      as the strongest predictor, accounting for 26.2%.'
    supports: claim
  - section: Original source P13-S2-C6
    page: 13
    quote: 'Other

      ROIs included in the model were SMG (+4.1%), IFGop

      (+5.6%), and STG (+6.7%).'
    supports: claim
  - section: Original source P1-S1-C5
    page: 1
    quote: 'One hundred four individuals with acute aphasia

      (<20 days poststroke) were included in the study.'
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: 'In most cases, MRI and behavioral examinations were

      conducted within 3 days of hospital admission, although a

      handful of patients underwent examination up to 20 days

      after stroke because of complications secondary to the

      stroke.'
    supports: sample
  - section: Original source P4-S1-C12
    page: 4
    quote: 'MRI and behavioral testing were always completed

      within a day of each other.'
    supports: sample
  - section: Original source P14-S2-C4
    page: 14
    quote: 'Each ROI treated as an independent variable in our

      models is represented by a single number (proportional

      damage), regardless of the size of the ROI.'
    supports: limitation
  - section: Original source P14-S3-C9
    page: 14
    quote: 'Finally, behavioral performance

      was only examined in relation to structural damage in

      cortical brain areas, although the inclusion of cerebral per-

      fusion imaging could provide additional information

      (Fridriksson, Richardson, Fillmore, & Cai, 2012; Hillis

      et al., 2001, 2002, 2004).'
    supports: limitation
predictor_type: imaging_metric
short_definition: A stepwise regression model using proportional damage to predefined
  language ROIs (pSTG, SMG, IFGop, and STG) to predict non-CAN residual scores.
assessment:
- sentence–picture matching task
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kristinsson2020
  proposal_id: R013
  review_status_sha256: 1e241ab8336d59d73548c8d7119140f841b7b570e3b37e5fe5d1de6bbc4cb52e
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
        A/passages.json: c7cc9d34e1bb7801f0cf13bf0793d3b004c84c5ff3f88e81db61996b2243d096
        A/raw.json: db684820d5b238351a75c573076365301950fcd3f4e4b1931cec33b475889258
        A/source-units.json: 93d54d386e09b15399a5247eaf57e75643e6203adbda07e60581235f922f5bae
        A/full-source-units.json: 3ff49242f8ac10c580591ea93414515d533af93efb4e7b3df61b400bf4bea5cd
        A/meta.json: 76b18796a893d8dac96ab9ae2235266f740d4b667b1c1638084749a76846d387
        A/table-images/page-10.png: 8f01985052c9b0861f920d2439f9d470a27da6685cc7c3459986e0af5a5f3cc4
        A/table-images/page-11.png: b947f7db39432d3a9213855e98639c99392f93110e679bc530934787257d4922
        A/table-images/page-6.png: 0a6e1a9de931439b3582b280d415fdb5d4f78fc3afbce6dc1a84f928587f81c3
        A/table-images/TABLE-4-page-8-1.png: 50f7c42154867c02b618c453d86977a77ec9909e37e7bfceab2ac26d9751204b
        A/table-images/page-5.png: cea89503261c8ac81a38cfc4625a50ce74b5cad90fec2c354c20f4eefda5739d
        A/table-images/page-4.png: 1f6ab499c9a9d4de6f620a263178f82d5eea85139e418901c4e58469a30fa7a0
        A/table-images/TABLE-1-page-4-1.png: 33d4663378292f88918a427adf100075bb975ec932819677be5b16566fbb3e65
        A/table-images/TABLE-3-page-6-1.png: de0a3ecae633927f67ed581f42f5b78ea16d55e71719039e3ba9ba501da44ff4
        A/table-images/page-8.png: a6974e8d3eb374740b80931e91d6aad454ab1c3432d115f9a725ec38f09c9ab7
        A/table-images/TABLE-6-page-11-1.png: 614b6d3da5c4dcc2e3137b1ace4c56ca359a56741202fbe82712dee0c9d449f6
        A/table-images/manifest.json: 70d09038371b44fd164eca0d1e6e804488e0a570c659c85db12ce467485649e5
        A/table-images/TABLE-5-page-10-1.png: 1a25f0504be4d8dbfbc01c4b04c3fa0c428c63350a1e4c18b9acb28010dddc8d
        A/table-images/TABLE-2-page-5-1.png: 46d13b2963ff8d45cccd4caf0707b5b91684556e4b6ad07c0a085240ed99cf1d
        A/clauses/window-11/raw.json: 25eaa0296da90bc7d189be6d7e5d6f8bada145e75556625f8243eeced67bb21c
        A/clauses/window-11/prompt.txt: fd04e97b3d49e15bbb7364a59d78fd2944803e8a8ef4460a8f95fe51658a3c24
        A/clauses/window-11/meta.json: aa007631d2a4bf7cf560ef5e8218074ff5b963bb30d66d136a6680d80b7fb7d2
        A/clauses/window-10/raw.json: e858554cdc41d0a5c508b78cee0ef1b26912e8806bcc64d30262fc9a42b5b266
        A/clauses/window-10/prompt.txt: 2a13ff6ec40a32ca4179d3ba5560c6b4e55a20b000312de1636e29819019ddec
        A/clauses/window-10/meta.json: 14e027ccde6af45c646f4b732859677b96bed17cafae807740d9182832e03237
        A/clauses/window-03/raw.json: 8b2cfba37315dc2cab5f46113e4c99f0a32ba565d3e9fbd2c39960c0fc7b1834
        A/clauses/window-03/prompt.txt: 35c173d6ab4f0839149c9bb00a158e5dcbfa937fada9a3494be959656691d75b
        A/clauses/window-03/meta.json: 5be2586eab9ff049d9fad5a89e71ab282f29baca068bc225facb6c26487aeba9
        A/clauses/window-04/raw.json: 560c5989092c959723fb94dd7ff388e60eb7d0cfc2ec3b5d7b09364f93d0768d
        A/clauses/window-04/prompt.txt: c79bcac9d0445de1a52d2b3ff175e7ac85318d4d3926e3cbcbaede5035950895
        A/clauses/window-04/meta.json: 2f5eb0d8d4d2753f3d5b903ceba05c2d4d6017b84655513421724fe029cf9442
        A/clauses/window-05/raw.json: 210fe4484c5b8121c3a71903fad56584ec5b93859fa8e4a14b655285351c0d9b
        A/clauses/window-05/prompt.txt: 435b7c406ce2be798b2869c5d90f8d67e42e8f7497f9f6319bf7cd8353314798
        A/clauses/window-05/meta.json: 04ff694a9d3e05764cc12344546a6356afc6817c4443f927cdda086074463968
        A/clauses/window-02/raw.json: 101f2e8689ce199c4c39ddb8a09ac27ab4cc423d00ff021f0cdb0db7baf33b50
        A/clauses/window-02/prompt.txt: f546c986c3e1a2b5133734f3c0b43b1e6bf4ecf399229ca22ffdd1ac1f2f4e21
        A/clauses/window-02/meta.json: 5dd03fa33d678259e7aac588b2fdb8b327e5421a83bd662a41340299deff991e
        A/clauses/window-12/raw.json: 9b5adaaec59ad4cdc68862fda25a41341636c4c80e134cf7474ddc78a227cc94
        A/clauses/window-12/prompt.txt: ffae4fae74261952e82648da710d7eddac3d1b3db0b3f205185423f1e7f0c8dc
        A/clauses/window-12/meta.json: 9def621ce520d1d887ee930cfdfea917c54e22a926b1b345a9c297878b13888b
        A/clauses/window-09/raw.json: 59c9b60d9767266095450ef3ff249a7e3e546213f34b0fbc700b3f0eabbb932d
        A/clauses/window-09/prompt.txt: 3e7bd9421c96548ce7db611fa9411e50ec4842fb6fe137ae1075ea7c8113796d
        A/clauses/window-09/meta.json: b259abbb0b7581c6807897166ebfe069a0969138b013d93402d0040c7be332e2
        A/clauses/window-07/raw.json: 73dc98adf97246f5a1ce49d29a7ec05c62338d59d12e71acc8db0f4a1ff202c1
        A/clauses/window-07/prompt.txt: 9bb40e26fcc11c4baa00c046b5eab6dedc2de599019f19051d47779b2a88c83b
        A/clauses/window-07/meta.json: 1a9c68c22d82bf2ea01f219482dbb197a104979ea143da51f968266717cb1e70
        A/clauses/window-01/raw.json: f8814e64d0b74f23cd721324081a36c652e68e10d47c513c93d50b2f0671ed1a
        A/clauses/window-01/prompt.txt: 8db0b983944240a8d22373584c579050cbc5b7f934938d18b4e8b47372bfcbb9
        A/clauses/window-01/meta.json: b4e19b9771d32861fdf58ef1b6e2a32dae5f2b4a3ac047c6d52b66cec6061f20
        A/clauses/window-06/raw.json: 3cae87e522fe43aa274665b26980c9f5c3ef020f9dfe6acba5c4c04fced42b89
        A/clauses/window-06/prompt.txt: 0eb1ce8f0361b812fc4170bd84ead0900e2feba27179a86c57150cf3b3e9ff10
        A/clauses/window-06/meta.json: 4cd286c3b8b1361e8492e25923ab4c184f8d8d9d7378220404c279f6fb9955ee
        A/clauses/window-08/raw.json: 600e1ca7da54752859fc8789de76e38012c6501ea28e9e04948d7506f7877ca6
        A/clauses/window-08/prompt.txt: de5723ea2c60244da11924da87198575f4ea770d976c374cc34dcdfe7160a675
        A/clauses/window-08/meta.json: b25d970b28997cbbfc54ccac59711b98e116ec357aee41d7cab44e700f98b938
        A/tables/TABLE-4-page-8-4/raw.json: afb604815dbaa31c659db91974d68bfc9c112dbcd52712f5e573840a48ee1bb3
        A/tables/TABLE-4-page-8-4/prompt.txt: 03cfaa8b187d4d5f402a44c62b1883f309ba54700b9f8de42f27ca1e5d23ddd0
        A/tables/TABLE-4-page-8-4/meta.json: d7ac130b3ab7d7573d36b0c7d6caef0a2b5d368583ca2c4c4ea079638a986206
        A/tables/TABLE-6-page-11-6/raw.json: bd82d68f541a2a679456b923a140d4331f945623d187a0f6e60d968914608f84
        A/tables/TABLE-6-page-11-6/prompt.txt: 98dcc3fb171329643ecd0473dfa4c41a3fd7b3ee2c7639db15d1be2ec66b292c
        A/tables/TABLE-6-page-11-6/meta.json: d574f747001adfff33640254eae1556cbcb3f2502977f6f502fb839a41b166f1
        A/tables/TABLE-2-page-5-2/raw.json: 9d4a2b0a6f77d8ca4f9d0b695e7c32dfe17cd26ddc262d4aa6dd9179ea319673
        A/tables/TABLE-2-page-5-2/prompt.txt: 9a109c54d7617aa15414a975150cf0947e70d6ca293880e7393a17e069a0ce72
        A/tables/TABLE-2-page-5-2/meta.json: 347fa9619a22c270b62d67f8d4ee97edad4d6f77fac69fa786eaa1ec7c16ad78
        A/tables/TABLE-3-page-6-3/raw.json: b9ad01ca3b7729c422925f923b12ebe4ca4c49b23c502132d1613d7eebc33456
        A/tables/TABLE-3-page-6-3/prompt.txt: cc712c6702d94e96180dd7ec761bb81fc3c2a3094b5ed0e1d4d353a67985fd7d
        A/tables/TABLE-3-page-6-3/meta.json: bb1beca8ebb934ac201ab28abe9f00c969c2732b50e125f8440e6144cfd84010
        A/tables/TABLE-5-page-10-5/raw.json: f495a751a0738124869de7bdaf417174deeca20b342746b678205f8e17876c59
        A/tables/TABLE-5-page-10-5/prompt.txt: a557dcef65d652ec27366220c3edce254b1d5458ea35f1ea732a08ff184781c1
        A/tables/TABLE-5-page-10-5/meta.json: 9ba059581de06dbb2a0ae96335679cf596fba71e1df52e8a734e5efb87da782c
        A/tables/TABLE-1-page-4-1/raw.json: 8b874a09ad6fd8d4edb560d6358aef99e0be3e03ec1c6ea09aa7107487918e14
        A/tables/TABLE-1-page-4-1/prompt.txt: 93c21cb4895cade1a3d6ce8b9a5cb3fd315a7a729c2fb7c0b3059958167674f7
        A/tables/TABLE-1-page-4-1/meta.json: b25c6372af2693ddcb870afc5de6de7a3343bb86ed1bff227264fa18424b7bd8
        B/passages.json: c7cc9d34e1bb7801f0cf13bf0793d3b004c84c5ff3f88e81db61996b2243d096
        B/raw.json: 639a7e0eb76db113133f7e7bf3ce150e249cc6782195c12e42ab5799df6e5c24
        B/source-units.json: 93d54d386e09b15399a5247eaf57e75643e6203adbda07e60581235f922f5bae
        B/full-source-units.json: 3ff49242f8ac10c580591ea93414515d533af93efb4e7b3df61b400bf4bea5cd
        B/meta.json: 8ad37b3e3ef2652b5cefa913fcb0c3bc2e7e03c67b2c38b1f8b987a3f698e654
        B/table-images/page-10.png: 8f01985052c9b0861f920d2439f9d470a27da6685cc7c3459986e0af5a5f3cc4
        B/table-images/page-11.png: b947f7db39432d3a9213855e98639c99392f93110e679bc530934787257d4922
        B/table-images/page-6.png: 0a6e1a9de931439b3582b280d415fdb5d4f78fc3afbce6dc1a84f928587f81c3
        B/table-images/TABLE-4-page-8-1.png: 50f7c42154867c02b618c453d86977a77ec9909e37e7bfceab2ac26d9751204b
        B/table-images/page-5.png: cea89503261c8ac81a38cfc4625a50ce74b5cad90fec2c354c20f4eefda5739d
        B/table-images/page-4.png: 1f6ab499c9a9d4de6f620a263178f82d5eea85139e418901c4e58469a30fa7a0
        B/table-images/TABLE-1-page-4-1.png: 33d4663378292f88918a427adf100075bb975ec932819677be5b16566fbb3e65
        B/table-images/TABLE-3-page-6-1.png: de0a3ecae633927f67ed581f42f5b78ea16d55e71719039e3ba9ba501da44ff4
        B/table-images/page-8.png: a6974e8d3eb374740b80931e91d6aad454ab1c3432d115f9a725ec38f09c9ab7
        B/table-images/TABLE-6-page-11-1.png: 614b6d3da5c4dcc2e3137b1ace4c56ca359a56741202fbe82712dee0c9d449f6
        B/table-images/manifest.json: 6644dcf33d21587ac05bd3e847754de060867f6f4fd0f9e592b987a0251a7ef1
        B/table-images/TABLE-5-page-10-1.png: 1a25f0504be4d8dbfbc01c4b04c3fa0c428c63350a1e4c18b9acb28010dddc8d
        B/table-images/TABLE-2-page-5-1.png: 46d13b2963ff8d45cccd4caf0707b5b91684556e4b6ad07c0a085240ed99cf1d
        B/clauses/window-11/raw.json: fbbda70e7b150005d461fafe641179c1c2fc75bcc83d658beebd0742d71c287b
        B/clauses/window-11/prompt.txt: fd04e97b3d49e15bbb7364a59d78fd2944803e8a8ef4460a8f95fe51658a3c24
        B/clauses/window-11/meta.json: eeedc6a21898bd7299dbf87b5e5ca1ab0cc3e71e5725eefaa20c6bf3ff532863
        B/clauses/window-10/raw.json: 784dded78e3a2f8a78f40b1d00c17ae1c75d3e561f793ed07d287235a5d61520
        B/clauses/window-10/prompt.txt: 2a13ff6ec40a32ca4179d3ba5560c6b4e55a20b000312de1636e29819019ddec
        B/clauses/window-10/meta.json: 3ea262dc877e458c4c8e81e1814580621e54461cdd4f2bdbe5e379dd3bb5156b
        B/clauses/window-03/raw.json: 0208e78c407e12fcde3a2a7862ac7c9963e7923d4d164cd78df34948fd1e1952
        B/clauses/window-03/prompt.txt: 35c173d6ab4f0839149c9bb00a158e5dcbfa937fada9a3494be959656691d75b
        B/clauses/window-03/meta.json: 9b72bb41fd61b1fb741ff636edf3193c85dde3299c9e9b1ffd52cd492a5fd107
        B/clauses/window-04/raw.json: aaa5145d31d0b24b7260bbb57624f06d7095bf90f8a8fecbc20a7d9f77114cf3
        B/clauses/window-04/prompt.txt: c79bcac9d0445de1a52d2b3ff175e7ac85318d4d3926e3cbcbaede5035950895
        B/clauses/window-04/meta.json: b1d5e0c9cf8a4efff63e230e8979808c308322c749f8df97b685118bc5e0cf63
        B/clauses/window-05/raw.json: 7d878987f5272ebf098e84fd86b4a0b6a16ec7e576a41ec7d2ada5e9bbda8676
        B/clauses/window-05/prompt.txt: 435b7c406ce2be798b2869c5d90f8d67e42e8f7497f9f6319bf7cd8353314798
        B/clauses/window-05/meta.json: c2497eeacf27e9b5c0f3bd77a7fc59069e65c3d3e1433cb695795bf8b79bf72c
        B/clauses/window-02/raw.json: 75f7f269292f9bd5297b185e258ddf16d136861efd852c3e4d41196b139ffbf0
        B/clauses/window-02/prompt.txt: f546c986c3e1a2b5133734f3c0b43b1e6bf4ecf399229ca22ffdd1ac1f2f4e21
        B/clauses/window-02/meta.json: 602e15421ef253c938045223aded8cdf1e5be9e022adea34c9ea7ead9647bdb0
        B/clauses/window-12/raw.json: 6e809f2f273e4c6f772c0003d32499cd9022609611dd4fb6b9de51afabd8a7d8
        B/clauses/window-12/prompt.txt: ffae4fae74261952e82648da710d7eddac3d1b3db0b3f205185423f1e7f0c8dc
        B/clauses/window-12/meta.json: bba3b4ef853d87918bcd0f720628f74633acd34277690d1f3d7e75234e3846be
        B/clauses/window-09/raw.json: e7cc12d7b9aa7713288285f15c57c036f98b1803511c15fac41eeae0300f7aba
        B/clauses/window-09/prompt.txt: 3e7bd9421c96548ce7db611fa9411e50ec4842fb6fe137ae1075ea7c8113796d
        B/clauses/window-09/meta.json: 20077324beb8d8249df552dccec266106dcce9415eb9b154fa52d8831c8582cf
        B/clauses/window-07/raw.json: 990e870ceb86880f034618806e1a364170c1df24710cdd9f8a8214e7c5b5dc24
        B/clauses/window-07/prompt.txt: 9bb40e26fcc11c4baa00c046b5eab6dedc2de599019f19051d47779b2a88c83b
        B/clauses/window-07/meta.json: 149fc92f290378565e604957481a718a7b17e6739a5788c32aeae7d495a702ff
        B/clauses/window-01/raw.json: 3e37359f4c72cd8bceaa1fc2d2c65912d3ea9f50018139de64079acd5629a34e
        B/clauses/window-01/prompt.txt: 8db0b983944240a8d22373584c579050cbc5b7f934938d18b4e8b47372bfcbb9
        B/clauses/window-01/meta.json: cfcba2fbeba5bb1f74c7193c09b9766bebc7415d5cdda3da8fa8dc36c991f578
        B/clauses/window-06/raw.json: 53b601a8f506ae76c73fcd3862a2833244988c17c2c2d66f576a96f792afbb0a
        B/clauses/window-06/prompt.txt: 0eb1ce8f0361b812fc4170bd84ead0900e2feba27179a86c57150cf3b3e9ff10
        B/clauses/window-06/meta.json: 230aca6de463b149daa852f7de278d8c53a099b3261ad3d94029f1dec66cd48a
        B/clauses/window-08/raw.json: 96b53e9aa85d32718ee7d9122fcee5ec031fa547a08158aa2f205e3522dea411
        B/clauses/window-08/prompt.txt: de5723ea2c60244da11924da87198575f4ea770d976c374cc34dcdfe7160a675
        B/clauses/window-08/meta.json: bd922d4ed265684ada08ece61dbbcf23b326cef9f6afe35353afb83a47c23c3a
        B/tables/TABLE-4-page-8-4/raw.json: b1ae354c06c256265ec69133128fdce9bf62507e7f76327563b427de63b97539
        B/tables/TABLE-4-page-8-4/prompt.txt: 03cfaa8b187d4d5f402a44c62b1883f309ba54700b9f8de42f27ca1e5d23ddd0
        B/tables/TABLE-4-page-8-4/meta.json: f6506b59cba97de7f1831ce2243a718ae9608c00f5e146bf3b72ca535296c32f
        B/tables/TABLE-6-page-11-6/raw.json: cc6755f91b320da1ce590f799f4f35a3119ce7a9e3f1abc21bd1c423b271f46b
        B/tables/TABLE-6-page-11-6/prompt.txt: 98dcc3fb171329643ecd0473dfa4c41a3fd7b3ee2c7639db15d1be2ec66b292c
        B/tables/TABLE-6-page-11-6/meta.json: ee34b9fb66182c5543175a5f86ca01b937ab34308734c34a40fcab24b1f1d0b0
        B/tables/TABLE-2-page-5-2/raw.json: 41e5e1236c24280531900a2523a7c077af26a0f994848309b6160ee9d7034a1b
        B/tables/TABLE-2-page-5-2/prompt.txt: 9a109c54d7617aa15414a975150cf0947e70d6ca293880e7393a17e069a0ce72
        B/tables/TABLE-2-page-5-2/meta.json: 730429f27897022feb5d5db19f6beec48ed4bf902fe6fee753fbadc901c508f1
        B/tables/TABLE-3-page-6-3/raw.json: f3c1dcaeb9c5000d7622823990f830f9a242293bf04a978002724706847e6cb6
        B/tables/TABLE-3-page-6-3/prompt.txt: cc712c6702d94e96180dd7ec761bb81fc3c2a3094b5ed0e1d4d353a67985fd7d
        B/tables/TABLE-3-page-6-3/meta.json: 32d03203d53ae8393c3e26eab5596fb3736c896c571936b906937c6f89b54c55
        B/tables/TABLE-5-page-10-5/raw.json: ebf53d17376bf7205731861d57e82a758db014db8af054a462d49b656f4b61e5
        B/tables/TABLE-5-page-10-5/prompt.txt: a557dcef65d652ec27366220c3edce254b1d5458ea35f1ea732a08ff184781c1
        B/tables/TABLE-5-page-10-5/meta.json: 89632a137c98e86bdd590911ca28492eb17cd18c6b0d2f84b1c44aca8222cfaf
        B/tables/TABLE-1-page-4-1/raw.json: 532059b38ab052fb1783c9ee893bcbb52e65d66e8cfc63ecd38d0d1ead214446
        B/tables/TABLE-1-page-4-1/prompt.txt: 93c21cb4895cade1a3d6ce8b9a5cb3fd315a7a729c2fb7c0b3059958167674f7
        B/tables/TABLE-1-page-4-1/meta.json: 8a279098567ffa337c3841a3ea98062be83eaec52b7eb3781e4e3ba5b4def8e3
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
      pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2020
      source_status_sha256: e68563ebfaa8737671999420adab9960bdb5eb3568ab7326c0650c491074b5a7
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: proportional damage to pSTG, SMG, IFGop, and STG
    outcome:
      text: non-CAN residual scores (subject vs object gaps)
    analysis_label: Post hoc analysis (Cleft/Wh-questions)
    relation: association
    evidence_ids:
    - P13-S2-C4
    - P13-S2-C5
    - P13-S2-C6
    qualifier_ids:
    - P13-S1-C11
    - P13-S1-C12
    - P13-S1-C13
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2020
      source_status_sha256: e68563ebfaa8737671999420adab9960bdb5eb3568ab7326c0650c491074b5a7
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C3
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C9
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C12
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C9
      - Result passage disposed without unit P7-S1-C13
      - Result passage disposed without unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C4
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S1-C9
      - Result passage disposed without unit P9-S1-C16
      - Result passage disposed without unit P9-S2-C2
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C7
      - Accounting without a linked unit P12-S1-C8
      - Accounting without a linked unit P12-S1-C9
      - Result passage disposed without unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C6
      - Unaccounted source passage P12-S1-C9
      - Unaccounted source passage P12-S1-C8
      - Unaccounted source passage P12-S2-C6
      - Result passage disposed without unit P12-S2-C8
      - Result passage disposed without unit P12-S3-C2
      - Result passage disposed without unit P12-S3-C3
      - Result passage disposed without unit P12-S3-C4
      - Result passage disposed without unit P12-S3-C7
      - Result passage disposed without unit P12-S3-C8
      - Result passage disposed without unit P12-S3-C10
      - Result passage disposed without unit P12-S3-C11
      - Result passage disposed without unit P12-S3-C12
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P13-S1-C2
      - Result passage disposed without unit P13-S1-C3
      - Result passage disposed without unit P13-S1-C4
      - Result passage disposed without unit P13-S1-C12
      - Result passage disposed without unit P13-S2-C3
      - Result passage disposed without unit P13-S2-C4
      - Accounting without a linked unit P13-S2-C5
      - Accounting without a linked unit P13-S2-C6
      - Unaccounted source passage P13-S2-C5
      - Unaccounted source passage P13-S2-C6
      - Accounting without a linked unit P13-S3-C3
      - Accounting without a linked unit P13-S3-C6
      - Unaccounted source passage P13-S3-C3
      - Unaccounted source passage P13-S3-C6
      - Result passage disposed without unit P14-S2-C7
      - Result passage disposed without unit P14-S3-C11
      - Result passage disposed without unit P14-S3-C6
      unattached_null_or_qualifier_ids:
      - P4-S1-C9
      - P9-S1-C16
      - P9-S2-C2
      - P9-S2-C3
      - P11-S1-C2
      - P13-S1-C2
      suppressed_nonrepresented_units: 33
      default_disposition_count_requires_completeness_check: 240
      unselected_timing_passages:
      - P1-S1-C5
      - P2-S3-C2
      - P3-S3-C6
      - P4-S1-C3
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
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
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: limitations
        source_ids:
        - P14-S2-C2
        - P14-S2-C3
        - P14-S2-C4
        - P14-S2-C5
        - P14-S2-C6
        - P14-S2-C7
        - P14-S2-C14
        - P14-S2-C15
        - P14-S3-C7
        - P14-S3-C8
        - P14-S3-C9
        - P14-S3-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-4-page-8-4
      - TABLE-5-page-10-5
      - TABLE-6-page-11-6
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-5-page-10-5
      - TABLE-6-page-11-6
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S2
        - P8-S1
        - P9-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2020
      source_status_sha256: e68563ebfaa8737671999420adab9960bdb5eb3568ab7326c0650c491074b5a7
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of pMTG as strongest predictor for total and non-CAN scores.
    - source_id: P1-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Restatement of AG and pSTG predictors for CAN and non-CAN scores.
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: General summary of temporo-parietal and posterior temporal associations.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes prior study by Magnusdottir et al. (2013).
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion volume data.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of covariate inclusion (lesion volume).
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia scores.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of aphasia scores between groups.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: T-test for comparability of samples.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: ANOVA for language effect.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive score frequency.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean total score.
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive CAN and non-CAN scores.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive score range.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of CAN vs non-CAN scores.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Chi-square test for ceiling effects.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of participants with damage to specific ROIs.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about model significance.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result for total score model.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Direction of beta values for total score model.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Variance explained by pMTG for total score.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Variance explained by AG and IFGtri for total score.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result for CAN score model.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Beta values and variance for AG and MTG in CAN model.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Beta value and variance for SMG in CAN model.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Positive beta values for MTGpole and STG in CAN model.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result for non-CAN score model.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Variance explained by pMTG for non-CAN score.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Variance explained by AG, IFGop, STG, and MTG for non-CAN score.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 2
      reason: Beta values for non-CAN score model.
    - source_id: P8-S1-C15
      disposition: unresolved
      result_indexes: []
      reason: Reference to Table 4.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Direct result for non-CAN residual model.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Variance explained by pSTG for non-CAN residuals.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Exclusion of AG from final non-CAN residual model.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Variance explained by IFGop, SMG, and IFGtri for non-CAN residuals.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Beta values for non-CAN residual model.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Interpretation of lesion profile for non-CAN residuals.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Variance comparison for total score (posterior vs frontal).
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Significance of pMTG in posterior total score model.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Non-significance of frontal predictors for total score.
    - source_id: P9-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Variance and significance of pMTG in posterior CAN model.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Non-significance of frontal CAN model.
    - source_id: P9-S1-C14
      disposition: represented
      result_indexes:
      - 6
      reason: Variance for posterior non-CAN model.
    - source_id: P9-S1-C15
      disposition: represented
      result_indexes:
      - 6
      reason: Significance of pMTG in posterior non-CAN model.
    - source_id: P9-S1-C16
      disposition: represented
      result_indexes:
      - 6
      reason: Variance and significance of IFGop in frontal non-CAN model.
    - source_id: P9-S1-C17
      disposition: represented
      result_indexes:
      - 7
      reason: Variance for posterior non-CAN residual model.
    - source_id: P9-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Significance of pSTG in posterior non-CAN residual model.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Variance and significance of frontal non-CAN residual model.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Direct result for logit total score model.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Direction of coefficients for logit total score model.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Direct result for logit CAN score model.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Direct result for logit non-CAN score model.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Significance of pMTG in logit non-CAN model.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Direct result for logit non-CAN residual model.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Interpretation of pMTG as strongest predictor in logit non-CAN residual
        model.
    - source_id: P12-S3-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Positive beta weight for STG in non-CAN model.
    - source_id: P12-S3-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Negative correlation of STG damage with non-CAN scores.
    - source_id: P12-S3-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Positive beta weights for SMG and IFGtri in non-CAN residual model.
    - source_id: P13-S2-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Variance for post hoc non-CAN residual model.
    - source_id: P13-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Variance explained by pSTG in post hoc model.
    - source_id: P13-S2-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Variance explained by SMG, IFGop, and STG in post hoc model.
    unresolved_coverage:
    - source_id: P8-S1-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P2-S3-C7
    - P4-S1-C8
    - P4-S1-C9
    - P4-S2-C2
    - P4-S2-C3
    - P5-S1-C6
    - P5-S1-C9
    - P7-S1-C11
    - P7-S1-C12
    - P7-S1-C13
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P8-S1-C1
    - P8-S1-C2
    - P9-S1-C3
    - P9-S2-C16
    - P9-S3-C1
    - P10-S1-C2
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    - P11-S2-C2
    - P11-S2-C3
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S2-C5
    - P12-S2-C6
    - P12-S2-C8
    - P12-S3-C2
    - P12-S3-C3
    - P12-S3-C4
    - P12-S3-C5
    - P12-S3-C7
    - P12-S3-C8
    - P12-S3-C9
    - P12-S3-C10
    - P12-S3-C11
    - P12-S3-C12
    - P13-S1-C1
    - P13-S1-C2
    - P13-S1-C3
    - P13-S1-C4
    - P13-S1-C5
    - P13-S1-C12
    - P13-S2-C3
    - P13-S2-C11
    - P13-S3-C3
    - P13-S3-C6
    - P14-S2-C7
    - P14-S3-C6
    - P14-S3-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    - TABLE-4-page-8-4
    - TABLE-5-page-10-5
    - TABLE-6-page-11-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C7
      recruited_sample:
      - P4-S1-C1
      - P4-S1-C5
      - P4-S1-C6
      eligibility:
      - P4-S1-C3
      imaging_provenance:
      - P6-S1-C4
      imaging_timing:
      - P4-S1-C11
      outcome_timing:
      - P4-S1-C11
      outcome_definition:
      - P5-S1-C12
      validation:
      - P11-S1-C7
      analysis_restrictions:
      - P5-S1-C13
      - P7-S1-C1
      - P7-S1-C6
      - P9-S2-C7
      dependent_variable_statement:
      - P7-S1-C1
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C9
      - P5-S1-C8
      - P7-S1-C9
      - P14-S1-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S2-C14
      - P4-S3-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
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
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: limitations
      source_ids:
      - P14-S2-C2
      - P14-S2-C3
      - P14-S2-C4
      - P14-S2-C5
      - P14-S2-C6
      - P14-S2-C7
      - P14-S2-C14
      - P14-S2-C15
      - P14-S3-C7
      - P14-S3-C8
      - P14-S3-C9
      - P14-S3-C10
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
      pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
      review_sha256: 1e241ab8336d59d73548c8d7119140f841b7b570e3b37e5fe5d1de6bbc4cb52e
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
      - P13-S2-C4
      - P13-S2-C5
      - P13-S2-C6
      source_result: In a post hoc analysis contrasting cleft sentences and referential
        wh-questions with subject gaps versus object gaps, a stepwise regression model
        using proportional damage to pSTG, SMG, IFGop, and STG predicted non-CAN residual
        scores, explaining 41.1% of the variance, with pSTG identified as the strongest
        predictor (26.2%).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a post hoc analysis (P13-S2-C2)
            contrasting specific sentence types (clefts/wh-questions) to examine subject
            vs object gaps. The proposed core correctly identifies this as a distinct
            analysis from the main stepwise regression, targeting non-CAN residual
            scores.
          source_ids:
          - P13-S2-C2
          - P13-S2-C4
        direction:
          answer: fits
          reason: The source states the model 'revealed a similar model' and 'supported
            our main analysis' (P13-S2-C3), identifying pSTG as the strongest predictor.
            The proposed core correctly characterizes this as a detected association
            where pSTG is the strongest predictor, preserving the direction of the
            finding (damage associated with impairment/prediction of residual scores).
          source_ids:
          - P13-S2-C3
          - P13-S2-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as proportional damage to specific
            ROIs (pSTG, SMG, IFGop, STG) based on P13-S2-C5 and P13-S2-C6. The outcome
            is non-CAN residual scores. The patient measurement is template_lesion_overlap,
            as the study uses predefined ROIs from an atlas (Faria et al., 2012) to
            calculate proportional damage, rather than patient-specific tractography
            or voxelwise tissue analysis.
          source_ids:
          - P13-S2-C5
          - P13-S2-C6
          - P5-S1-C11
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that this
            is a post hoc analysis contrasting specific sentence types (clefts/wh-questions)
            and that non-CAN residual scores were calculated by covarying canonical
            performance. This accurately reflects the source's description of the
            analysis method and purpose.
          source_ids:
          - P13-S2-C2
          - P7-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core includes limitations regarding the ROI-based approach (spatial
            resolution) and the restriction to structural cortical damage. No material
            caveats that would change the interpretation of this specific post hoc
            finding are omitted. The distinction between this post hoc analysis and
            the main analysis is preserved.
          source_ids:
          - P14-S2-C4
          - P14-S3-C9
      optional_pending:
      - Specific p-values for the post hoc model predictors are not transcribed in
        the provided source window, only variance explained percentages.
      - Sample size for this specific post hoc subset is not explicitly stated, though
        the main study N=104 is noted.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values for the post hoc model predictors are not transcribed in the
      provided source window, only variance explained percentages.
    - Sample size for this specific post hoc subset is not explicitly stated, though
      the main study N=104 is noted.
    normalizations:
    - field: sample.n
      original: 104
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R013
      exposure:
        text: proportional damage to pSTG, SMG, IFGop, and STG
      outcome:
        text: non-CAN residual scores (subject vs object gaps)
      analysis_label: Post hoc analysis (Cleft/Wh-questions)
      relation: association
      evidence_ids:
      - P13-S2-C4
      - P13-S2-C5
      - P13-S2-C6
      qualifier_ids:
      - P13-S1-C11
      - P13-S1-C12
      - P13-S1-C13
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
        source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2020
        source_status_sha256: e68563ebfaa8737671999420adab9960bdb5eb3568ab7326c0650c491074b5a7
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8c6cd48539b0274c877209401776053b387fcf66ca504ba3f80cac101e98d342
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C5
          page: 1
          text_layer_sha256: 8c6cd48539b0274c877209401776053b387fcf66ca504ba3f80cac101e98d342
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'One hundred four individuals with acute aphasia

          (<20 days poststroke) were included in the study.'
        anchor_text: 'One hundred four individuals with acute aphasia

          (<20 days poststroke) were included in the study.'
        excluded_fragments: []
        image_sha256: 773125353101cdad2969e7808ec7722c4c9ecc34d81b3ac204de8e5e636d8d6e
        transcription: . One hundred four individuals with acute aphasia (<20 days
          poststroke) were included in the study
      P4-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6642e2ac7e0dd79d165f97aeca5853be6a017fe10805ec2b891ce39290ac0fbd
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 34281d0f296518cfba9ab7cb277b485266fda79cb74a86c611d3de65acccb3eb
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C11
          page: 4
          text_layer_sha256: 34281d0f296518cfba9ab7cb277b485266fda79cb74a86c611d3de65acccb3eb
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In most cases, MRI and behavioral examinations were

          conducted within 3 days of hospital admission, although a

          handful of patients underwent examination up to 20 days

          after stroke because of complications secondary to the

          stroke.'
        anchor_text: 'In most cases, MRI and behavioral examinations were

          conducted within 3 days of hospital admission, although a

          handful of patients underwent examination up to 20 days

          after stroke because of complications secondary to the

          stroke.'
        excluded_fragments: []
        image_sha256: 186db3a06b66d60a8e041652435e02f00cde05c43fe54279b2790cd99c0489f5
        transcription: In most cases, MRI and behavioral examinations were conducted
          within 3 days of hospital admission, although a handful of patients underwent
          examination up to 20 days after stroke because of complications secondary
          to the stroke
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 13
  quote: 'Thus, we performed a

    post hoc analysis contrasting performance on cleft sen-

    tences with subject gaps and referential wh-questions with

    subject gap and main verbs (canonical sentences) to the

    same sentence structures but with object gaps rather than

    subject gaps (noncanonical sentences).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
