---
id: semantic_category_access_generalization
name: semantic category access and generalization
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: generalization_to_untrained_items
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: generalization_to_untrained_items
  target_kind: impairment
  claim: generalization to untrained items was not merely the result of repeatedly
    accessing specific semantic categories
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 2
    population: persons with fluent aphasia (one with anomic aphasia and one with
      Wernicke's aphasia)
    phase: not_reported
    time_post_onset: post-treatment probe sessions
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - single-subject design
  - small sample size (N=2)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: accessing specific semantic categories during semantic
    feature analysis (SFA) treatment. post hoc analysis; improved naming of a specific
    item was operationally defined as accuracy during at least three of the four probe
    sessions in a treatment condition. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S2-C5, two-model
    agreement, human verification pending): . The present experiment

    sought to determine whether similar positive outcomes

    could be demonstrated for 2 persons with classical syn-

    dromes of fluent aphasia, one with anomic aphasia and one

    with Wernicke’s aphasia, who appeared to experience

    breakdowns at different levels of lexical processing Original text-layer quotation
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
    - proposed_concept:generalization_to_untrained_items
  therapy:
    id: sfa
    name: semantic feature analysis
  citation: '@Boyle2004'
  source_passages:
  - section: Original source P11-S1-C2
    page: 11
    quote: "Generalization to untreated items might occur in at least \ntwo ways as\
      \ a result of SFA treatment: Only items from \nsemantic categories that were\
      \ accessed during treatment \nmight benefit as a result of repeated stimulation\
      \ of those \ncategories, or repeated stimulation of the semantic system \nin\
      \ a methodical way might make access to the system \neasier in general, regardless\
      \ of specific semantic categories \nused in treatment."
    supports: claim
  - section: Original source P11-S1-C10
    page: 11
    quote: "This suggests that for Participant 1, improved naming was \nnot confined\
      \ to semantic categories that were accessed \nduring treatment."
    supports: claim
  - section: Original source P11-S2-C9
    page: 11
    quote: "Thus, data from \nParticipant 2 show that umproved naming of specific\
      \ items \nwas not confined to semantic categories accessed during \ntreatment."
    supports: claim
  - section: Original source P11-S3-C1
    page: 11
    quote: "This post hoc analysis suggests that for both partici- \npants, the generalization\
      \ to untrained items was not merely \nthe result of repeatedly accessing specific\
      \ semantic \ncategories."
    supports: claim
  - section: Original source P2-S3-C10
    page: 2
    quote: "Method \nParticipants \nTwo right-handed men with aphasia participated\
      \ in the \nstudy."
    supports: sample
  - section: Original source P2-S2-C5
    page: 2
    quote: "The present experiment \nsought to determine whether similar positive\
      \ outcomes \ncould be demonstrated for 2 persons with classical syn- \ndromes\
      \ of fluent aphasia, one with anomic aphasia and one \nwith Wernicke’s aphasia,\
      \ who appeared to experience \nbreakdowns at different levels of lexical processing."
    supports: sample
  - section: Original source P11-S1-C5
    page: 11
    quote: "For this purpose, improved \nnaming of a specific item was operationally\
      \ defined as \naccuracy during at least three of the four probe sessions in\
      \ \na treatment condition, \nTable Al in the Appendix shows the probe and treat-\
      \ \nment nouns for Participant 1, separated into semantic \ncategories, and\
      \ the number of baseline and probe sessions \nduring which he named the item\
      \ accurately."
    supports: method
predictor_type: behavioural
short_definition: accessing specific semantic categories during semantic feature analysis
  (SFA) treatment
assessment:
- confrontation naming
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Boyle2004
  proposal_id: R012
  review_status_sha256: 156a6f8a148af999113d1d3db358ebd6f7833ed6a3b3e3f61b12de98a01c797a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
        A/passages.json: 25361424a13ca4cbdaa33b2160abe40b3559822bfe1fed54606d5b4d1ee0af68
        A/raw.json: 566d9ffa4517d656c03746c1f207d8c87e57e5c53c70b7183fa04c39eb972173
        A/source-units.json: af8f53bcc35f48d0d0ae377248003cf3d80ecbf6432493ab0be60f3cfafea74d
        A/full-source-units.json: 08d6922565632c9dd22205bc31201a225a5b74b373529b05ebb228e21f3c4dce
        A/meta.json: 087414903fcb8bf9cf7d488d984b0f23ad183a9aa00e378ab46112198c455213
        A/table-images/page-14.png: df6dc9021f3178318421c5f4c0997d3258eb124decc61012095789ab01151940
        A/table-images/TABLE-1-page-3-1.png: c2398ef83d51860ff9e4491163ba01c3d444f3fef66b279929c2c6b597e2467c
        A/table-images/page-13.png: d8fe43e14a7b7d3fa24a9ae6c8c029841889e3e3d473d38d42c0e4e760df4bd0
        A/table-images/TABLE-3-page-9-1.png: 8204428a1e58c9ca838986b8362a1f06a18736a40f182186055d5cf2c7a4aa15
        A/table-images/page-3.png: d90bfeccb740c7c9bffc71d6d98a142ee1acb7e4d3d683a0293dc77894264f8d
        A/table-images/page-9.png: 0e0476618f666644168e923637183d2b64d7e1dcb08cb8b2e44c5d476a602108
        A/table-images/manifest.json: c68cbbc93f8aeb82146912e4ffcb71ca1a9a7cbb834e4f99cff934f14169585b
        A/table-images/TABLE-A1-page-13-1.png: 7f09aa8f5bcae5ffa2475b432b61fc5182da1af0847b4dbe7f7ede6393246e05
        A/table-images/TABLE-2-page-3-2.png: c2398ef83d51860ff9e4491163ba01c3d444f3fef66b279929c2c6b597e2467c
        A/table-images/TABLE-A2-page-14-1.png: add65f848c27b339fb5e32a9b1f3a68e931b9c8ad0a83ead181b14b12e86981b
        A/clauses/window-11/raw.json: 772f289c37d82453201bfeb692588232a96694396e8e589aa4d166dddc8a653b
        A/clauses/window-11/prompt.txt: 6fb3276fafd09b8041b7fb06e4b2dfb9035748ba33febe0c6d3072f1b5f0946b
        A/clauses/window-11/meta.json: a3e68c70a0f0414c38ccf1da63984e4af0da5d6ad5ca893e88e5be5a9d6f1362
        A/clauses/window-10/raw.json: 962eec22718220dc01d38d6b0be82758e4cf133670985618656d061b25c9ae25
        A/clauses/window-10/prompt.txt: b4bcbfd0e7cac5fa47366fbf7bf9445d8117bc7ad4521f1a2e80ac8b20457e97
        A/clauses/window-10/meta.json: 4186f010c3cd63ba4cd8cc5226d5617d7739e308bc068e686ae399778dde285f
        A/clauses/window-03/raw.json: 2d3db5f0fa9d05a0223611d3fae0ef917629ce313358b4b80ad22ee18c2b48fa
        A/clauses/window-03/prompt.txt: 453b575c3e93bd57dd8ed8104cfcb340d6373e07c9206d0fa88558c2094cb94b
        A/clauses/window-03/meta.json: 1c80e5ba00b685f0acf981cf54f26fb1ce4d400251375865be7c17a1341b323e
        A/clauses/window-04/raw.json: aa45fe6e4327619ea4f4260a326d945c22b8e3b7576d1eb47411d59b1cb56af2
        A/clauses/window-04/prompt.txt: da800e65b7aacd6dc561bee612c29491d4903f5576a161ccdaa3da1ded4c4c31
        A/clauses/window-04/meta.json: 5a93329a16e6a4009fda9abe854d08e6e57c0cce890a99a90242da1f2e2642c0
        A/clauses/window-05/raw.json: f6b241281b4cb52daf2eee5f77574a35223f4c0b59e3de42293f0e73bfe7aed5
        A/clauses/window-05/prompt.txt: 6a61fd451b9f684bafcf9ca69aaa3e29cef0111af9d5e9d50a35669f3fdd54ad
        A/clauses/window-05/meta.json: 88815e62600d6505a410530b7d1c0af87022ea6af78ba09370799d883816209e
        A/clauses/window-02/raw.json: cda238ff02fa21582aa5c168a1a4095163cfaf061e2bedac04e735403223ce4a
        A/clauses/window-02/prompt.txt: 255705a59453fccd258edfad62d3a6d584b7174b6cefcefbb285a1caad42332e
        A/clauses/window-02/meta.json: af9c8f1f0a5ea04e7a1025b0332470f3c89f897bd7cba3ad75d5da0dd9a648d1
        A/clauses/window-12/raw.json: 9a4a64726026e16fba894c49941f7548322bbdf9086da9e7f8b5f193257d990a
        A/clauses/window-12/prompt.txt: 05d09a05aa95ef97554a71d658c01ad7ee222914d877d2d251d2a4f9327cc106
        A/clauses/window-12/meta.json: bbfcc0520a144b8bdd3e629ee64244ec2bb556acc966826a832fb9fd090e2085
        A/clauses/window-13/raw.json: 22ddc90902d041117cbb32ed3aad7769ec372fc260d248dac34e178081445168
        A/clauses/window-13/prompt.txt: 60cbd6f5b23ee02ea6e04d16850557e388b4ce43fcbdaa8f92604b3e115804fa
        A/clauses/window-13/meta.json: 91754a07ac6dcc5972f384d272d3bca324a9464a1e373d4c344c45289228d1e5
        A/clauses/window-09/raw.json: 0f770badb5015dd9d2951ccd8f232f9bf35d8152de9211220e864ba3e243f9d2
        A/clauses/window-09/prompt.txt: 779736f9e0a05a4e8f3f3fc7bcf13eb6981f313f7ca9d734dea519f4731e1ec3
        A/clauses/window-09/meta.json: af5508a1d3f32119d5c198de18b5f92bf09a96410dc3ccf3dc6becc6cb3f1981
        A/clauses/window-07/raw.json: 8dc709f6820bd8777e7128c5d38bc28c3a3367a239acf9db99eea5d04364309e
        A/clauses/window-07/prompt.txt: f0082c7f4bf03a6076983982d0207098036f7de2ba8ba0344702edc930bb6ef1
        A/clauses/window-07/meta.json: 9c80b1060e8a5e3a3c4a03c2f9433619c1b080122235f70c7da73e461b458526
        A/clauses/window-01/raw.json: 8137bca8be0cda55b97690697ac1f96e7db2e9dbc9173f0a6223eb08294b5677
        A/clauses/window-01/prompt.txt: c24c439823adf4b926ab1ed3c994533706c9ecfb769df411aba22fec9a73ff47
        A/clauses/window-01/meta.json: 415c0f4b806a17391856becace07a53038821489b6fbc3098c5da5faf17c21d0
        A/clauses/window-06/raw.json: 30bc93a14fc4de27afefe5b8a723513a23a65af7232618ac1eeec44df02af082
        A/clauses/window-06/prompt.txt: 7538e9b99203c987e697b17789dd5a634cf3573db0bc3c0c19a7b65f5400655a
        A/clauses/window-06/meta.json: fa043e0aae54d7f814fdfb6e2deace96ab90bc51acc54d2efb49c83c1f8e9495
        A/clauses/window-08/raw.json: 29d8fc078ffe4cb7f46b8ce92540339083f0a1d82c8421e1e9b487ecac2110c2
        A/clauses/window-08/prompt.txt: 56c159ef5787c0ed57f3e5aa593494402079ba3a850cac701dd9b00018427543
        A/clauses/window-08/meta.json: dda35ca29969284d77d46764313227fcef898b07db0bd32fd57070612709d719
        A/tables/TABLE-A2-page-14-5/raw.json: ce9489c6853ad8d94f20d59938f6c746064f863906b147eb8180cbf1b868601b
        A/tables/TABLE-A2-page-14-5/prompt.txt: 543ee1378418edb44f4716e0f8cf376137bcc14a5138752fb448cd4b7ff7eee3
        A/tables/TABLE-A2-page-14-5/meta.json: ddab040bd7eb61e838ed5a2434280abe6e16c315fbafd47980455880508b9da4
        A/tables/TABLE-1-page-3-1/raw.json: 6cdec46c1ba195b1aeca656b4060e94b7541b2af7689cdb610a3c6317df0db79
        A/tables/TABLE-1-page-3-1/prompt.txt: 630ea2aeb888008868f98394cb8f83f506c930e422a754b0fb2c4138e64d9369
        A/tables/TABLE-1-page-3-1/meta.json: 7556d3b869e4b228b0e364d1a40cbde47d52a14354b1475bdbe86408d3f10e46
        A/tables/TABLE-2-page-3-2/raw.json: 39d37aedaf8a1bcfb78faae80302e29b74704861de36e6552b2bb372681ddd33
        A/tables/TABLE-2-page-3-2/prompt.txt: 99fb91ab89e82b04626c77f188bb44c7502e08527fe34d5e6b7f501dd91ad055
        A/tables/TABLE-2-page-3-2/meta.json: c1a1c9cc5ea01a59f51b4aeb853507a5a05577eedd539fe362db858c985708d8
        A/tables/TABLE-3-page-9-3/raw.json: 097f583f858b572abb739c60fcf26628b2044f25478a74bbb70b4dc58302a524
        A/tables/TABLE-3-page-9-3/prompt.txt: 264e22939581c021e1e486c967c72307a30a24b67d37b3857a1cb8989425202f
        A/tables/TABLE-3-page-9-3/meta.json: e743727cef389b5d780cfd3f01a45908ef8ea63ad7bba11dcbe5dbf553ec4f86
        A/tables/TABLE-A1-page-13-4/raw.json: cc9ffbfb71dafea341fbdb6b0441a5a767185cf93cc9484115ed1209d1ef5922
        A/tables/TABLE-A1-page-13-4/prompt.txt: f67521ab74d787df5c071893b060a48862e6aa753ec36bb81acf59b09febcabe
        A/tables/TABLE-A1-page-13-4/meta.json: e65d5bff0c46401a38fd37a1d46ac9ac4ff0678763743a048a1e0a9db0db9102
        B/passages.json: 25361424a13ca4cbdaa33b2160abe40b3559822bfe1fed54606d5b4d1ee0af68
        B/raw.json: 9ebec35c4b5cc9b7f5667590a9c80190de9d0807ad8757a265c6ee951cda3956
        B/source-units.json: af8f53bcc35f48d0d0ae377248003cf3d80ecbf6432493ab0be60f3cfafea74d
        B/full-source-units.json: 08d6922565632c9dd22205bc31201a225a5b74b373529b05ebb228e21f3c4dce
        B/meta.json: 154e39fa0bef9f9683d1216c106eed5fcc1108b7f7ac295216fe6f615627119c
        B/table-images/page-14.png: df6dc9021f3178318421c5f4c0997d3258eb124decc61012095789ab01151940
        B/table-images/TABLE-1-page-3-1.png: c2398ef83d51860ff9e4491163ba01c3d444f3fef66b279929c2c6b597e2467c
        B/table-images/page-13.png: d8fe43e14a7b7d3fa24a9ae6c8c029841889e3e3d473d38d42c0e4e760df4bd0
        B/table-images/TABLE-3-page-9-1.png: 8204428a1e58c9ca838986b8362a1f06a18736a40f182186055d5cf2c7a4aa15
        B/table-images/page-3.png: d90bfeccb740c7c9bffc71d6d98a142ee1acb7e4d3d683a0293dc77894264f8d
        B/table-images/page-9.png: 0e0476618f666644168e923637183d2b64d7e1dcb08cb8b2e44c5d476a602108
        B/table-images/manifest.json: f75a9db6c8d68e91baffbbb5cd6c58ddaffda4d0d75c2764f65275d7c22d8e82
        B/table-images/TABLE-A1-page-13-1.png: 7f09aa8f5bcae5ffa2475b432b61fc5182da1af0847b4dbe7f7ede6393246e05
        B/table-images/TABLE-2-page-3-2.png: c2398ef83d51860ff9e4491163ba01c3d444f3fef66b279929c2c6b597e2467c
        B/table-images/TABLE-A2-page-14-1.png: add65f848c27b339fb5e32a9b1f3a68e931b9c8ad0a83ead181b14b12e86981b
        B/clauses/window-11/raw.json: 2a75a81e626754b7a20daffe31cfd3fc192008ed2028b5bd9ebd374461e7d033
        B/clauses/window-11/prompt.txt: 6fb3276fafd09b8041b7fb06e4b2dfb9035748ba33febe0c6d3072f1b5f0946b
        B/clauses/window-11/meta.json: 73990fbcf72ef1f2cd1f4860450dad5780260c5edbad253e193e2a4e24bc6e93
        B/clauses/window-10/raw.json: b38623f6e0615d47351921d76a60358f834bef3885cdb4f4a2db6d1c8bec8566
        B/clauses/window-10/prompt.txt: b4bcbfd0e7cac5fa47366fbf7bf9445d8117bc7ad4521f1a2e80ac8b20457e97
        B/clauses/window-10/meta.json: 889e08a86e6fab7100941dd28624cd66b500d1ec89fffde550cc881332534027
        B/clauses/window-03/raw.json: e15ef0c54cd1ac49bce501e5fdd934f553409593d8750fbb2921d48b87d054fc
        B/clauses/window-03/prompt.txt: 453b575c3e93bd57dd8ed8104cfcb340d6373e07c9206d0fa88558c2094cb94b
        B/clauses/window-03/meta.json: f7c5f1093fb3237f793e55e294f4e01915b544266da2e80f20a025e630a3b224
        B/clauses/window-04/raw.json: 1e4923c3582605b695fccc3cd39ba5de187f35fc32a6a476600d273f708c0436
        B/clauses/window-04/prompt.txt: da800e65b7aacd6dc561bee612c29491d4903f5576a161ccdaa3da1ded4c4c31
        B/clauses/window-04/meta.json: a56fc2a2c046b6f2f3c16a8c1c484fcfc37b2db50d134d07850e08e16e61a73c
        B/clauses/window-05/raw.json: 5a964119b07b3301e8d03d22f2fb7e548708b6566f9efa7b648049407a780d91
        B/clauses/window-05/prompt.txt: 6a61fd451b9f684bafcf9ca69aaa3e29cef0111af9d5e9d50a35669f3fdd54ad
        B/clauses/window-05/meta.json: 835e36a8ef5f2ada5ee0e4d56f962c6ba8bb632aa824d1f650eb277f8268c03d
        B/clauses/window-02/raw.json: e85e5bc6bd9a1b9d56d0549f61cfdb0f8ae715d58f162829b3e4dd94fa5b8b7d
        B/clauses/window-02/prompt.txt: 255705a59453fccd258edfad62d3a6d584b7174b6cefcefbb285a1caad42332e
        B/clauses/window-02/meta.json: 94d9aaedda6cd72fa3686e12108402caa5d381f9d69c69c1834b053cab77a63c
        B/clauses/window-12/raw.json: 327ec6e200ac0bb7107576d1c14ca31d624580784d59d25eb22ab9b60ee29366
        B/clauses/window-12/prompt.txt: 05d09a05aa95ef97554a71d658c01ad7ee222914d877d2d251d2a4f9327cc106
        B/clauses/window-12/meta.json: e87c490889e58581a3491b94536d0fb9d634a0113329d5204517e010007499d0
        B/clauses/window-13/raw.json: 7a3199e58df326a235ad59f506123575ab0ca258c562a353cbb88730e95a81a8
        B/clauses/window-13/prompt.txt: 60cbd6f5b23ee02ea6e04d16850557e388b4ce43fcbdaa8f92604b3e115804fa
        B/clauses/window-13/meta.json: 106a6070bd66f71b7f4de8642165862b26a119dcbc1831154d4ba79696a979ee
        B/clauses/window-09/raw.json: b3ff4338bd50611baf12c5040ad246e874f7896bf9068bcdeff60bbc1750d531
        B/clauses/window-09/prompt.txt: 779736f9e0a05a4e8f3f3fc7bcf13eb6981f313f7ca9d734dea519f4731e1ec3
        B/clauses/window-09/meta.json: c6501e0b092ade3b90765413b815affcb5665e56dfe609a0169c97ae9f363336
        B/clauses/window-07/raw.json: 2b5a1df393a9e8ee530ffa25241b47573761cdc81f0f706e8f75ee9aac316200
        B/clauses/window-07/prompt.txt: f0082c7f4bf03a6076983982d0207098036f7de2ba8ba0344702edc930bb6ef1
        B/clauses/window-07/meta.json: 643365416afa4bc5353708b71e3f91a065bb7f64f33df52342c37afec621a406
        B/clauses/window-01/raw.json: ab2b1fd89afb99ebcfb99b6ce120d3e2b3daa477f6d687468dc46480ca948cf4
        B/clauses/window-01/prompt.txt: c24c439823adf4b926ab1ed3c994533706c9ecfb769df411aba22fec9a73ff47
        B/clauses/window-01/meta.json: b7b18af8a64f004ac33557e4906b3294d6013d65b80c95665092130ba5ebb5df
        B/clauses/window-06/raw.json: baecafebc9ac7d0fe55ea1cd8959ea99aec1fb328b78042c14b96ab6f5010e6d
        B/clauses/window-06/prompt.txt: 7538e9b99203c987e697b17789dd5a634cf3573db0bc3c0c19a7b65f5400655a
        B/clauses/window-06/meta.json: 8f02ed7ecd0279687cb482e4bd63566d6bfaa8d681c5adc35d4f80f95ec65215
        B/clauses/window-08/raw.json: 6ed95901e34ab5338efe6c21a2f0c45d10571a35add221b97169f61072813e53
        B/clauses/window-08/prompt.txt: 56c159ef5787c0ed57f3e5aa593494402079ba3a850cac701dd9b00018427543
        B/clauses/window-08/meta.json: 68d15dddf7aadf38320abcb40980d1b2ebdea9ffe2fb1c04d46151f049b9575f
        B/tables/TABLE-A2-page-14-5/raw.json: b6c5952faab8efbdeb908e4c4fba45a54ba67ea5adf410e08a2c303257ccbb19
        B/tables/TABLE-A2-page-14-5/prompt.txt: 543ee1378418edb44f4716e0f8cf376137bcc14a5138752fb448cd4b7ff7eee3
        B/tables/TABLE-A2-page-14-5/meta.json: 2831f9649d912b6b580d794f12d2e52b2fdf65b0fd28da1bbc1545bea869652b
        B/tables/TABLE-1-page-3-1/raw.json: 7682ec9bce469b526cec04958efcf289ab0aee44b429ebbc24374557b175d631
        B/tables/TABLE-1-page-3-1/prompt.txt: 630ea2aeb888008868f98394cb8f83f506c930e422a754b0fb2c4138e64d9369
        B/tables/TABLE-1-page-3-1/meta.json: 1b3de6bd0a1c1d7729dfe13d9c35f56c21d3505fc78ecee9a79cd6b0a603d69d
        B/tables/TABLE-2-page-3-2/raw.json: 4f7b2e5f355ec45a01fd087d32693a28864fb39d69c7b7bc7639ac96a1786ce7
        B/tables/TABLE-2-page-3-2/prompt.txt: 99fb91ab89e82b04626c77f188bb44c7502e08527fe34d5e6b7f501dd91ad055
        B/tables/TABLE-2-page-3-2/meta.json: 1f460dbd6c91a66bde9b4facf51a3403282681ffdfd8db804088cb9f95ce734e
        B/tables/TABLE-3-page-9-3/raw.json: 097f583f858b572abb739c60fcf26628b2044f25478a74bbb70b4dc58302a524
        B/tables/TABLE-3-page-9-3/prompt.txt: 264e22939581c021e1e486c967c72307a30a24b67d37b3857a1cb8989425202f
        B/tables/TABLE-3-page-9-3/meta.json: 4be7f0869cf41338d591ffac0f8f2542e6d69f5ec0a5e34a009d88bae4b80d72
        B/tables/TABLE-A1-page-13-4/raw.json: b7cbe8ef472fb622dc0aa43bf423500a7d0bd761b46087d0768067a528fef363
        B/tables/TABLE-A1-page-13-4/prompt.txt: f67521ab74d787df5c071893b060a48862e6aa753ec36bb81acf59b09febcabe
        B/tables/TABLE-A1-page-13-4/meta.json: 24a7d2cf6d27b39296682eac4a315a25fad611f43c1accbb1ac18dab40823af9
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
      pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
      source_review: _compare/relationships-2026-11-16/review-current/Boyle2004
      source_status_sha256: 6b91e3f684f8df7fbf3c2530959fb89616ff712222b4d98532d9b53b2c38401e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: accessing specific semantic categories during treatment
    outcome:
      text: generalization to untrained items
    analysis_label: Semantic category access and generalization
    relation: sensitivity
    evidence_ids:
    - P11-S2-C10
    - P11-S2-C11
    - P11-S3-C1
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
      pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
      source_review: _compare/relationships-2026-11-16/review-current/Boyle2004
      source_status_sha256: 6b91e3f684f8df7fbf3c2530959fb89616ff712222b4d98532d9b53b2c38401e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S1-C6
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P3-S2-C9
      - Result passage disposed without unit P3-S3-C1
      - Result passage disposed without unit P3-S3-C2
      - Result passage disposed without unit P3-S3-C3
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S1-C8
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S2-C8
      - Unaccounted source passage P6-S2-C8
      - Unaccounted source passage P6-S1-C6
      - Result passage disposed without unit P6-S2-C11
      - Result passage disposed without unit P6-S2-C13
      - Accounting without a linked unit P6-S2-C14
      - Accounting without a linked unit P6-S2-C15
      - Accounting without a linked unit P6-S3-C2
      - Accounting without a linked unit P6-S3-C3
      - Unaccounted source passage P6-S2-C15
      - Unaccounted source passage P6-S3-C3
      - Unaccounted source passage P6-S2-C14
      - Unaccounted source passage P6-S3-C2
      - Accounting without a linked unit P6-S3-C10
      - Accounting without a linked unit P6-S3-C11
      - Accounting without a linked unit P6-S3-C12
      - Accounting without a linked unit P6-S3-C5
      - Accounting without a linked unit P6-S3-C6
      - Accounting without a linked unit P6-S3-C7
      - Accounting without a linked unit P6-S3-C8
      - Unaccounted source passage P6-S3-C5
      - Unaccounted source passage P6-S3-C12
      - Unaccounted source passage P6-S3-C6
      - Unaccounted source passage P6-S3-C8
      - Unaccounted source passage P6-S3-C10
      - Unaccounted source passage P6-S3-C11
      - Unaccounted source passage P6-S3-C7
      - Result passage disposed without unit P9-S1-C15
      - Result passage disposed without unit P9-S2-C10
      - Result passage disposed without unit P9-S2-C3
      - Accounting without a linked unit P9-S2-C4
      - Result passage disposed without unit P9-S2-C5
      - Accounting without a linked unit P9-S2-C6
      - Result passage disposed without unit P9-S2-C7
      - Unaccounted source passage P9-S2-C6
      - Unaccounted source passage P9-S2-C4
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S1-C9
      - Result passage disposed without unit P11-S2-C10
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C6
      - Result passage disposed without unit P11-S2-C7
      - Result passage disposed without unit P11-S2-C8
      - Result passage disposed without unit P11-S3-C11
      - Result passage disposed without unit P11-S3-C12
      - Accounting without a linked unit P11-S3-C9
      - Accounting without a linked unit P11-S4-C2
      - Accounting without a linked unit P11-S4-C3
      - Accounting without a linked unit P11-S4-C4
      - Unaccounted source passage P11-S4-C4
      - Unaccounted source passage P11-S4-C2
      - Unaccounted source passage P11-S3-C9
      - Unaccounted source passage P11-S4-C3
      - Accounting without a linked unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C4
      - Accounting without a linked unit P12-S1-C5
      - Accounting without a linked unit P12-S2-C4
      - Unaccounted source passage P12-S1-C4
      - Unaccounted source passage P12-S2-C4
      - Unaccounted source passage P12-S1-C5
      - Unaccounted source passage P12-S1-C1
      unattached_null_or_qualifier_ids:
      - P4-S1-C5
      - P6-S2-C15
      - P9-S2-C4
      - P9-S2-C6
      - P11-S1-C7
      - P11-S1-C8
      - P11-S2-C2
      - P11-S2-C10
      - P11-S3-C11
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 248
      unselected_timing_passages:
      - P4-S3-C20
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-3-2
      - TABLE-3-page-9-3
      - TABLE-A1-page-13-4
      - TABLE-A2-page-14-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-3-2
      - TABLE-A1-page-13-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P9-S1
        - P10-S1
        - P11-S3
        - P11-S4
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
      source_review: _compare/relationships-2026-11-16/review-current/Boyle2004
      source_status_sha256: 6b91e3f684f8df7fbf3c2530959fb89616ff712222b4d98532d9b53b2c38401e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports improvement in treated and generalized naming.
    - source_id: P1-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of improvement in discourse without specific measure.
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of no change in discourse.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification information.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of spontaneous speech.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of strategies.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification information.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of spontaneous speech.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of severity.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline error description.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline performance description.
    - source_id: P3-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline error description.
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline performance description.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline performance description.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Stimulus selection detail.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Stimulus selection detail.
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Treatment procedure detail.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Treatment procedure detail.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Treatment procedure detail.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Operational definition detail.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reliability result.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reliability result.
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Data location description.
    - source_id: P6-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline stability description.
    - source_id: P6-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Reports improvement in treated nouns for Participant 1.
    - source_id: P6-S2-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Provides accuracy data for treated nouns.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports maintenance of naming accuracy.
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports improvement in treated nouns for Participant 2.
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports continued improvement in treated nouns.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Provides accuracy data for treated nouns.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline stability description.
    - source_id: P6-S3-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports improvement in treated nouns for many-exemplar condition.
    - source_id: P6-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Data location description.
    - source_id: P6-S3-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports generalized naming for Participant 1.
    - source_id: P6-S3-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports generalized naming for Participant 2.
    - source_id: P6-S3-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Provides accuracy data for probe nouns.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports no further improvement in probe items for Participant 2 in many-exemplar
        condition.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Provides accuracy data for probe nouns.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports increased efficiency (CIUs/min) for Participant 1.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Provides specific CIUs/min data for Participant 1.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no change in mean CIUs or %CIUs for Participant 1.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports increase in mean CIUs for Participant 2.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports increase in CIUs for Participant 2 after few-exemplar condition.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports continued increase in CIUs during many-exemplar condition.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Provides specific mean CIU data for Participant 2.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Reports modest increase in CIUs/min for Participant 2, not functionally
        significant.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Reports stable %CIUs for Participant 2.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Reports no difference in global lexical retrieval difficulty for either
        participant.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes apparent differences before statistical testing.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 8
      reason: Reports significant reduction in delays for Participant 1.
    - source_id: P9-S2-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Reports non-significant differences in specific word-finding behaviors
        for Participant 2.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of naming improvements.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports that many exemplars did not enhance generalization.
    - source_id: P9-S2-C5
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 6
      reason: Restatement of mixed discourse results.
    - source_id: P9-S2-C6
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Restatement of global retrieval and delay results.
    - source_id: P9-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table title.
    - source_id: P9-S3-C4
      disposition: unresolved
      result_indexes: []
      reason: Table 3 contains raw data that requires transcription/analysis.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S1-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Reports improved naming not confined to treated categories for Participant
        1.
    - source_id: P11-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc analysis detail.
    - source_id: P11-S2-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Reports improved naming not confined to treated categories for Participant
        2.
    - source_id: P11-S2-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Suggests improved access to semantic system for Participant 2.
    - source_id: P11-S3-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reports that adding 60 items did not improve generalization.
    - source_id: P11-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study.
    - source_id: P11-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Participant 2's performance variability.
    - source_id: P11-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Participant 1's performance.
    - source_id: P11-S3-C12
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 6
      reason: Restatement of discourse improvements.
    - source_id: P11-S4-C2
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of efficiency increase for Participant 1.
    - source_id: P11-S4-C3
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of reduction in delays.
    - source_id: P11-S4-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of no change in CIUs or %CIUs.
    - source_id: P11-S4-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of no reduction in global retrieval difficulty.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Restatement of no reduction in retrieval difficulty or specific behaviors.
    - source_id: P12-S1-C4
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      reason: Restatement of Participant 2's discourse results.
    unresolved_coverage:
    - source_id: P9-S3-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C3
    - P1-S1-C4
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C6
    - P3-S1-C7
    - P3-S1-C8
    - P3-S2-C9
    - P3-S2-C10
    - P3-S3-C1
    - P3-S3-C2
    - P3-S3-C3
    - P4-S1-C5
    - P4-S1-C8
    - P5-S1-C13
    - P5-S2-C5
    - P5-S2-C7
    - P6-S1-C6
    - P6-S2-C8
    - P6-S2-C11
    - P6-S2-C12
    - P6-S2-C13
    - P6-S2-C15
    - P6-S3-C2
    - P6-S3-C4
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C8
    - P6-S3-C12
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C10
    - P7-S2-C3
    - P9-S1-C3
    - P9-S1-C11
    - P9-S1-C14
    - P9-S1-C15
    - P9-S2-C3
    - P9-S2-C5
    - P9-S2-C6
    - P9-S2-C7
    - P9-S2-C10
    - P9-S3-C2
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S1-C10
    - P11-S2-C2
    - P11-S2-C6
    - P11-S2-C7
    - P11-S2-C8
    - P11-S2-C9
    - P11-S3-C7
    - P11-S3-C9
    - P11-S3-C11
    - P11-S3-C12
    - P11-S4-C2
    - P11-S4-C3
    - P11-S4-C4
    - P11-S4-C5
    - P12-S1-C1
    - P12-S1-C4
    - P12-S2-C4
    - P13-S3-C5
    - P14-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-3-2
    - TABLE-3-page-9-3
    - TABLE-A1-page-13-4
    - TABLE-A2-page-14-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P3-S1-C13
      - P3-S1-C14
      recruited_sample:
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      eligibility:
      - P2-S3-C12
      - P2-S4-C2
      - P2-S4-C3
      - P2-S4-C4
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P4-S3-C17
      outcome_definition:
      - P2-S3-C9
      - P5-S3-C11
      - P5-S3-C13
      - P5-S3-C14
      - P6-S1-C13
      - P6-S2-C10
      - P6-S2-C11
      - P9-S3-C3
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C1
      - P2-S3-C9
      - P5-S2-C11
      - P5-S3-C6
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C13
      - P3-S1-C14
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
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
      pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
      review_sha256: 156a6f8a148af999113d1d3db358ebd6f7833ed6a3b3e3f61b12de98a01c797a
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
      - P11-S2-C10
      - P11-S2-C11
      - P11-S3-C1
      source_result: The post hoc analysis found that for both participants, improved
        naming of untrained items was not confined to semantic categories accessed
        during treatment. For Participant 1, items from unshared categories improved
        (P11-S1-C9), and for Participant 2, an item from an untargeted category improved
        (P11-S2-C7). The authors conclude that generalization was not merely the result
        of repeatedly accessing specific semantic categories, but rather involved
        improved access to the semantic system in general (P11-S3-C1, P11-S3-C2).
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the post hoc examination of
            whether generalization to untrained items was restricted to semantic categories
            accessed during treatment, as described in P11-S1-C4 and P11-S3-C1.
          source_ids:
          - P11-S1-C4
          - P11-S3-C1
        direction:
          answer: fits
          reason: The claim that generalization was 'not merely the result of repeatedly
            accessing specific semantic categories' aligns with the source finding
            that improved naming occurred in unshared categories, indicating that
            the specific category access was not the sole driver (i.e., no exclusive
            effect of category access on generalization).
          source_ids:
          - P11-S1-C10
          - P11-S2-C9
          - P11-S3-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as accessing semantic categories
            during SFA treatment, and the outcome is generalization to untrained items.
            The measurement is behavioral (confrontation naming accuracy), not imaging-based.
          source_ids:
          - P11-S1-C2
          - P11-S1-C5
          - P5-S3-C6
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that this was a post
            hoc analysis and specifies the operational definition for improved naming
            (accuracy in at least 3 of 4 probe sessions).
          source_ids:
          - P11-S1-C4
          - P11-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitations of the single-subject design
            and small sample size (N=2), which are material to the interpretation
            of the generalization findings.
          source_ids:
          - P2-S3-C10
          - P2-S2-C5
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
      id: R012
      exposure:
        text: accessing specific semantic categories during treatment
      outcome:
        text: generalization to untrained items
      analysis_label: Semantic category access and generalization
      relation: sensitivity
      evidence_ids:
      - P11-S2-C10
      - P11-S2-C11
      - P11-S3-C1
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
        pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
        source_review: _compare/relationships-2026-11-16/review-current/Boyle2004
        source_status_sha256: 6b91e3f684f8df7fbf3c2530959fb89616ff712222b4d98532d9b53b2c38401e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 51e801ffde0a85dc0b6a9bdee2668ec0b53a7b00e5cc9750f0c839ebfeecd5df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9fdc422ad95cdefaba2a3cd2da2eb6fac5b5a412148008603993a98488f20574
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 9fdc422ad95cdefaba2a3cd2da2eb6fac5b5a412148008603993a98488f20574
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The present experiment \nsought to determine whether similar\
          \ positive outcomes \ncould be demonstrated for 2 persons with classical\
          \ syn- \ndromes of fluent aphasia, one with anomic aphasia and one \nwith\
          \ Wernicke’s aphasia, who appeared to experience \nbreakdowns at different\
          \ levels of lexical processing."
        anchor_text: "The present experiment \nsought to determine whether similar\
          \ positive outcomes \ncould be demonstrated for 2 persons with classical\
          \ syn- \ndromes of fluent aphasia, one with anomic aphasia and one \nwith\
          \ Wernicke’s aphasia, who appeared to experience \nbreakdowns at different\
          \ levels of lexical processing."
        excluded_fragments: []
        image_sha256: 65f7f163fd191dda5bc18f9dbae7c88b793180a535881ab7296f5a4da7c79960
        transcription: '. The present experiment

          sought to determine whether similar positive outcomes

          could be demonstrated for 2 persons with classical syn-

          dromes of fluent aphasia, one with anomic aphasia and one

          with Wernicke’s aphasia, who appeared to experience

          breakdowns at different levels of lexical processing'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: "Generalization to untreated items might occur in at least \ntwo ways as\
    \ a result of SFA treatment: Only items from \nsemantic categories that were accessed\
    \ during treatment \nmight benefit as a result of repeated stimulation of those\
    \ \ncategories, or repeated stimulation of the semantic system \nin a methodical\
    \ way might make access to the system \neasier in general, regardless of specific\
    \ semantic categories \nused in treatment."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
