---
id: executive_cognition_factor
name: executive-cognition factor
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: neural_tissue_concentration
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: neural_tissue_concentration
  target_kind: impairment
  claim: There were no clusters of neural tissue concentration that correlated uniquely
    with the executive-cognition factor score and survived correction for multiple
    comparisons.
  direction: no_effect
  relationship: correlational
  method: VBCM
  sample:
    n: 31
    population: individuals with chronic stroke aphasia (at least 12 months post-stroke)
      with a single left hemisphere stroke
    phase: not_reported
    time_post_onset: at least 12 months post-stroke at time of scanning and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - the test battery was not designed to extensively assess executive capacities
  - patient lesions may not have encompassed key regions for executive capacity
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A behavioral factor extracted via principal components
    analysis (PCA) with varimax rotation from a battery of assessments including forward
    and backward digit span, the Brixton Spatial Rule Anticipation Task, and Raven’s
    Coloured Progressive Matrices. analysis controlled for variation in phonological
    and semantic PCA factors; analysis controlled for lesion volume. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P3-S2-C4, two-model agreement, human verification pending): . Participants
    were included if they had chronic stroke aphasia, i.e. they had an enduring impairment
    in producing and/or understanding spoken language and were at least 12 months
    post-stroke at time of scanning and assessment (n = 31) Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:neural_tissue_concentration
  citation: '@Butler2014'
  source_passages:
  - section: Original source P8-S2-C6
    page: 8
    quote: 'In contrast to the phonological and

      semantic factors, there were no clusters that correlated uniquely

      with the cognitive factor score and survived correction for multiple

      comparisons.'
    supports: claim
  - section: Original source P13-S1-C11
    page: 13
    quote: 'The third factor, ‘executive’ cognition, which ex-

      plained the least variance, did not uniquely covary with any brain

      regions in our analysis.'
    supports: claim
  - section: Original source P3-S2-C4
    page: 3
    quote: 'Participants were included if they had chronic stroke aphasia,

      i.e. they had an enduring impairment in producing and/or understand-

      ing spoken language and were at least 12 months post-stroke at time

      of scanning and assessment (n = 31).'
    supports: sample
  - section: Original source P3-S2-C5
    page: 3
    quote: 'All participants were recruited

      on the basis that they reported one left hemisphere stroke, either

      ischaemic or haemorrhagic.'
    supports: sample
  - section: Original source P5-S4-C2
    page: 5
    quote: 'Principle component analysis factors and test scores

      The VBCM analyses of PCA factors and individual test scores were

      conducted in SPM8 running on Matlab 2009a and 2012a, respectively,

      with sets of factors or scores entered simultaneously as continuous

      behavioural

      covariates.'
    supports: method
  - section: Original source P10-S2-C2
    page: 10
    quote: 'Lesion

      volume was included in each VBCM model with results thresh-

      olded at P 5 0.005 voxel-level, P 4 0.01 FWE corrected cluster-

      level.'
    supports: confounders
  - section: Original source P16-S4-C3
    page: 16
    quote: 'In terms of the absence of correlates of executive-

      cognitive function, it is worth noting that our test battery was not

      designed to extensively assess these capacities, nor did the lesions

      of the aphasic patients that were considered encompass many

      regions thought to be key for this capacity.'
    supports: limitation
  - section: Original source P3-S4-C2
    page: 3
    quote: 'The additional cognitive tests included

      forward and backward digit span (Wechsler, 1987), the Brixton Spatial

      Rule Anticipation Task (Burgess and Shallice, 1997), and Raven’s

      Coloured Progressive Matrices (Raven, 1962).'
    supports: method
predictor_type: behavioural
short_definition: A behavioral factor extracted via principal components analysis
  (PCA) with varimax rotation from a battery of assessments including forward and
  backward digit span, the Brixton Spatial Rule Anticipation Task, and Raven’s Coloured
  Progressive Matrices.
assessment:
- forward digit span
- backward digit span
- Brixton Spatial Rule Anticipation Task
- Raven’s Coloured Progressive Matrices
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Butler2014
  proposal_id: R003
  review_status_sha256: 85bed5e1bfe702750c9730868f99dbab994031393652dd9018982905cf093bb2
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
        A/passages.json: 34ddf91d4b12893f318f2c56f202a53f79a86d008dfe46bafc258c5c51b8b5d1
        A/raw.json: 01c66903f2b161216eac884beb05a4de4246fe1a26d5de64c7251239c9318903
        A/source-units.json: f34ea0a0f4f5173524fa018fde7747421d95db547fe1a8170e22fa4f16700d99
        A/full-source-units.json: 02bf85d3bde687e15b844fe072ce6902cc510e0652ddf454f23412aefbbff858
        A/meta.json: 41c75dd95df6f2bba6133fbe8826bf9dd6ed652eb6cfc3be420460f149b13a6c
        A/table-images/TABLE-3-page-8-1.png: 50ab7d63b252480a2cccccf03d432030e9ffdb9ed15b071df04e5e0db463b701
        A/table-images/page-7.png: 1b6d201658f80548cef25f1a16b31850055204306e9f90fd3a3840cc463c166b
        A/table-images/page-4.png: 8330448c9f17c436d98e41a60d1f1fad02ea9a1ba7e132f4bf829a2f0d479d18
        A/table-images/TABLE-1-page-4-1.png: beec29328459ae2cfc4d174cdf7f55e2c0df1404eb4bdc5179f61496d8dff766
        A/table-images/page-8.png: 1d7d3cd30db710421cc5e202095764a3565b39f4bc4ca0ec49fc7891a21a2ab9
        A/table-images/manifest.json: ab1097a565996f1dfac4d7847973f0432dba3969b6c836f6aaad5c0c4cb1f438
        A/table-images/TABLE-2-page-7-1.png: cd8c7d381c3cc53a5f2d752f32580977b5f61190fb0fe0abfb4614260cd07977
        A/clauses/window-11/raw.json: 578fb2bccf42cc95cff670685ef09d59fbabc305f30d54582e19f0d0ec8093d9
        A/clauses/window-11/prompt.txt: 5880e3a0d078961003f67d919cde137df9e175ef61d3227034f20aa0403af2fa
        A/clauses/window-11/meta.json: 3b48a82f77c6c54381027fbe5643c4642a67ac36c8524042f36000d997ef1d3d
        A/clauses/window-10/raw.json: 9c53504cbcc241fa71b7af65b6ca944dbccb9dd1f59d50602c701261dc27347a
        A/clauses/window-10/prompt.txt: 5ad6a18bf0f66f3ac06181cdeebb27c9325fbecf65a6cdae1954152d4fd0f5b0
        A/clauses/window-10/meta.json: efa47b70db44f3471b017b47b58bb9473be5856643e79c154e7bdcb0963ae085
        A/clauses/window-03/raw.json: 44de2a8a550bd5709878a205dd1097fb61c98c0724fbc271fce958c5a7d404c8
        A/clauses/window-03/prompt.txt: f83208b971b1e21eb5c8f22101f1383f12c276223f766207c25323ffdf59675a
        A/clauses/window-03/meta.json: bae474845392902d5530b93a009e96504a5c6080c9416e992b52c843cdf8bbfe
        A/clauses/window-04/raw.json: 9ea8f85659b74329a21cffee723337bbe22c84e998142416d37a4c72f63bc3af
        A/clauses/window-04/prompt.txt: 4ce76bf13de3dfd74284a0d2b4a52e3f66b3fc00dce4fa5094e322c35639d565
        A/clauses/window-04/meta.json: 290987335ebaf0c91fcc313a26eb2ccc447e14136f012e5861e042449a49bdee
        A/clauses/window-05/raw.json: 278374ff9fcc6a3ddd35e182a59330b3df9d4d063bf7a8ffc6b7aa487cfb2aaa
        A/clauses/window-05/prompt.txt: 942c78fc212bc4dd07c791f221c512956e8edb0bcbdeab606e77e12aca94f5f0
        A/clauses/window-05/meta.json: 65d139fc6ba994e4e25aa58e5471bc46ec1c7259df5bb35a7d4be260aebb5671
        A/clauses/window-02/raw.json: da200a37243292776136012b88e0c883c06b9da9b1b3fe04d4ca99fbceddb496
        A/clauses/window-02/prompt.txt: a1fa7363493d28771998deb170e58cf6f772550d30fb335584bf486175dfb3b4
        A/clauses/window-02/meta.json: c06f0ca8bdc7cda2ad9de08a8102cabdd1defbb4f39c35ee904c56a8c669c53b
        A/clauses/window-09/raw.json: c4f911e748bada5a03985c0eefaaf3d945e2c73db713bb27ce3b2eb7337c9f67
        A/clauses/window-09/prompt.txt: 79682989f67bc016070f9804346d3ca9457632657129659ebc16ef4ece228a34
        A/clauses/window-09/meta.json: 30df58fe41eb2aebe32c0fc340a66a1dc44a14e571ad25a9355cd1243dad4759
        A/clauses/window-07/raw.json: 9b7c62d867c550ac35755f7a508af6d2661923e70e8a48949f811f08ada825bc
        A/clauses/window-07/prompt.txt: 3884358ebd86cfff95444c0f5fd84ada30d876d6ab1d4678e5cf555b918b5b5a
        A/clauses/window-07/meta.json: dfa89c55bd987f315b020ddca4841a0db0db817ef6277fe2eab1a44ab0cea9e1
        A/clauses/window-01/raw.json: 4ce410f2786ba9ff1ed8ce3946087e5852d96230cf92f07a0d0b8e81547a9e7e
        A/clauses/window-01/prompt.txt: 0cf0b34d9cf70b4f18571434754c717bae5f20c73d53445a00d271caa8b6bf03
        A/clauses/window-01/meta.json: 5bada19a7d634bddfed4ba4f3dbb6ecda2db69c018947deb8a9435e9301f5be3
        A/clauses/window-06/raw.json: b6cf66bf8bf3740c8c8fc4a6b0bba91eac1e3161ac9e39587ab8d6b7d2caf2d1
        A/clauses/window-06/prompt.txt: 365256ee58306d999c5cd6575711608f6ff9f20bae52648229722168496fd050
        A/clauses/window-06/meta.json: d0e2000bee3dee9431d4424adc252e68bb7b5f00e5f4a130c3719a0f9a585497
        A/clauses/window-08/raw.json: f9fc680d96c2cf518dceb4e0f9ad4236592cb8a68d387a815ca934c92cde334f
        A/clauses/window-08/prompt.txt: 310241a9c0684ae94ff8555189c5eb256f9b56c466bfd25d4a6c49550103e95b
        A/clauses/window-08/meta.json: b3bf3e0c453dce9baedd62e4974d185022200c9c872d45f634020e4ce37dd2a7
        A/tables/TABLE-3-page-8-3/raw.json: 113cc767134644dae3f88694192fc7be35981d0fa5ecd315952f81834677474e
        A/tables/TABLE-3-page-8-3/prompt.txt: 949320f2a057e1582cce439fed0b76abf1c66512936013e9322d5070dfa1c530
        A/tables/TABLE-3-page-8-3/meta.json: 88ce470df619c86991f9621d56edb9801bfb72ff998ab899923f626d4813c3ee
        A/tables/TABLE-2-page-7-2/raw.json: 7496baeada31a081961efe46d6f2448f96e0c980ba7655a51f88064b77615d07
        A/tables/TABLE-2-page-7-2/prompt.txt: 1159f689daf0589fdd59a5e705cf93e26b785716dc860c53f146e752d847ab95
        A/tables/TABLE-2-page-7-2/meta.json: be892dfbeda2cd2b444cd35925744293a1bbba46505815a9e6b26a43ab0de90c
        A/tables/TABLE-1-page-4-1/raw.json: dd367cc5c414f646c57a95ff6e90f696d56568792b3c54c665f3d3b29e8729eb
        A/tables/TABLE-1-page-4-1/prompt.txt: 388eed7fc57a9b2b3348851787824a1b58f2058e451aa2ca4dc4cd1f7de5619c
        A/tables/TABLE-1-page-4-1/meta.json: c19f0b3eda381468f34a5bc68ea58cadade896eb90e0509a5575668130fc4712
        B/passages.json: 34ddf91d4b12893f318f2c56f202a53f79a86d008dfe46bafc258c5c51b8b5d1
        B/raw.json: 6553a3eebadbd95c6f59c388361c058bb71543162116aa4ae74654498494aee1
        B/source-units.json: f34ea0a0f4f5173524fa018fde7747421d95db547fe1a8170e22fa4f16700d99
        B/full-source-units.json: 02bf85d3bde687e15b844fe072ce6902cc510e0652ddf454f23412aefbbff858
        B/meta.json: 97fc8531944ec7a0848806cdf92536482869c8830a3f3908fa70b84f9fab984e
        B/table-images/TABLE-3-page-8-1.png: 50ab7d63b252480a2cccccf03d432030e9ffdb9ed15b071df04e5e0db463b701
        B/table-images/page-7.png: 1b6d201658f80548cef25f1a16b31850055204306e9f90fd3a3840cc463c166b
        B/table-images/page-4.png: 8330448c9f17c436d98e41a60d1f1fad02ea9a1ba7e132f4bf829a2f0d479d18
        B/table-images/TABLE-1-page-4-1.png: beec29328459ae2cfc4d174cdf7f55e2c0df1404eb4bdc5179f61496d8dff766
        B/table-images/page-8.png: 1d7d3cd30db710421cc5e202095764a3565b39f4bc4ca0ec49fc7891a21a2ab9
        B/table-images/manifest.json: 554a0e80e0b809431fef660593734bfcebea80d4695b9befc9332ccf5d1cc9ff
        B/table-images/TABLE-2-page-7-1.png: cd8c7d381c3cc53a5f2d752f32580977b5f61190fb0fe0abfb4614260cd07977
        B/clauses/window-11/raw.json: adcadc7c2c24b4d731f55be014365d1f3684d294f8179cea55139b99d790b4f4
        B/clauses/window-11/prompt.txt: 5880e3a0d078961003f67d919cde137df9e175ef61d3227034f20aa0403af2fa
        B/clauses/window-11/meta.json: 7f15386d939e59eac791cef3350fea1ea03f4ee5d09c2e14d7cedbf4a3700b4f
        B/clauses/window-10/raw.json: 1d90d567d9ab6e4429aa70d81eb30bc6dca92fc4d39f90a41646a1c4dcebe39b
        B/clauses/window-10/prompt.txt: 5ad6a18bf0f66f3ac06181cdeebb27c9325fbecf65a6cdae1954152d4fd0f5b0
        B/clauses/window-10/meta.json: 820a2ebfc758a42da69cc5e5ecbd05a38ee85f993df07e1318450a160be48f18
        B/clauses/window-03/raw.json: bf767280bc3f4db42d22190032f780ac2a78652b06f8103eca6b56b97a3c6e9e
        B/clauses/window-03/prompt.txt: f83208b971b1e21eb5c8f22101f1383f12c276223f766207c25323ffdf59675a
        B/clauses/window-03/meta.json: 563032e5f038eeba2269a744141da455d898574b580d49bf8383a563ffe8f157
        B/clauses/window-04/raw.json: 45712c7c647a4f66da38c2b05e8cb2454c25306c3300d1fe668e1915b925b17e
        B/clauses/window-04/prompt.txt: 4ce76bf13de3dfd74284a0d2b4a52e3f66b3fc00dce4fa5094e322c35639d565
        B/clauses/window-04/meta.json: e97579c275f3a8a2a830f588e7e7b6ae79db618934c2c9e3ad214817fe17bbc4
        B/clauses/window-05/raw.json: 6dec462d140d2148d1ed3675d19a4aec79f88b08413b8513c7ee149914035885
        B/clauses/window-05/prompt.txt: 942c78fc212bc4dd07c791f221c512956e8edb0bcbdeab606e77e12aca94f5f0
        B/clauses/window-05/meta.json: b079f9c1aae7b3384207aefd648327e83dd6b716e5cf75bb6d0e11efb8781664
        B/clauses/window-02/raw.json: 4dde185d904fc09823321fc842c46b285b38410585244f12600e42fac6a24636
        B/clauses/window-02/prompt.txt: a1fa7363493d28771998deb170e58cf6f772550d30fb335584bf486175dfb3b4
        B/clauses/window-02/meta.json: a23b02afd38e6e59ff70e8bf078fb2fbe3cf151fbcdb52dc82453212313aa723
        B/clauses/window-09/raw.json: 9c55bba86eceb14be5e55f25bdb799c18d0668ea7c2b22364f222210bc60f19c
        B/clauses/window-09/prompt.txt: 79682989f67bc016070f9804346d3ca9457632657129659ebc16ef4ece228a34
        B/clauses/window-09/meta.json: 49b9a006b1ea1727aa8fa42c110266881af1c8f662cbb41b25cfeffb42d035d1
        B/clauses/window-07/raw.json: e73c2f8fe47fab598a295b6320b8aef871ee7661379c08171c9ca8d5292a318c
        B/clauses/window-07/prompt.txt: 3884358ebd86cfff95444c0f5fd84ada30d876d6ab1d4678e5cf555b918b5b5a
        B/clauses/window-07/meta.json: f6f979262018928745407e212c06408972bdc246213c6ea8c90c5241b30b9512
        B/clauses/window-01/raw.json: 00f71569e8fbdd33cd09518fc7f928338eec758acdaf9ee037caf5bc1d61d409
        B/clauses/window-01/prompt.txt: 0cf0b34d9cf70b4f18571434754c717bae5f20c73d53445a00d271caa8b6bf03
        B/clauses/window-01/meta.json: adaa83c017e7bccba6191e977df617e1ff9f7bce4aba4df9f99aec3c10471261
        B/clauses/window-06/raw.json: deb66a32bb98f77b17a994a0544c3f45eea5263c9c5ad777985d1d515e5d1b4c
        B/clauses/window-06/prompt.txt: 365256ee58306d999c5cd6575711608f6ff9f20bae52648229722168496fd050
        B/clauses/window-06/meta.json: 561619040e0cb5d20bbf2229a69a12d9788c1a16e308fa35c6904b9920961017
        B/clauses/window-08/raw.json: c0e36d85122f2f5038f79d913e6cd78c78e3fb3c463091055fdd33518f4d0ae7
        B/clauses/window-08/prompt.txt: 310241a9c0684ae94ff8555189c5eb256f9b56c466bfd25d4a6c49550103e95b
        B/clauses/window-08/meta.json: a09fbdc8005ddc3e132d9c6968b2c6ab204bc9e8d7829e80746765aef89737cc
        B/tables/TABLE-3-page-8-3/raw.json: 17eebf9decd4972708a2eec5c6b2dda177b599da68c2888271bf9e11e1062714
        B/tables/TABLE-3-page-8-3/prompt.txt: 949320f2a057e1582cce439fed0b76abf1c66512936013e9322d5070dfa1c530
        B/tables/TABLE-3-page-8-3/meta.json: a750135e130eb627a432b63180f59b97373b2a184a782c180d0af95324d77a9b
        B/tables/TABLE-2-page-7-2/raw.json: d5b6e07cd32e05601570aeaeca4a4036262e9417cd38b5924b750d9136f62e77
        B/tables/TABLE-2-page-7-2/prompt.txt: 1159f689daf0589fdd59a5e705cf93e26b785716dc860c53f146e752d847ab95
        B/tables/TABLE-2-page-7-2/meta.json: ef11a5ceb7c44316baec9595aa66c20f15d76707b76b155db8f86c6e3f6c3004
        B/tables/TABLE-1-page-4-1/raw.json: 911329ebca812bc6d6a64ebaf7492d5d82b5e54a8251abe748d9b9ca80bad360
        B/tables/TABLE-1-page-4-1/prompt.txt: 388eed7fc57a9b2b3348851787824a1b58f2058e451aa2ca4dc4cd1f7de5619c
        B/tables/TABLE-1-page-4-1/meta.json: f1aa2c0c4cc2b5f5b7a73c64cfcdf52ce6099e7eb44ef93a773f4e20b16cef8f
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
      pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
      source_review: _compare/relationships-2026-11-16/review-current/Butler2014
      source_status_sha256: 17bb6508c1ef2ab7edea160094315a508c16aa05dad75c628e601912bd39ac74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: executive-cognition factor
    outcome:
      text: neural tissue concentration
    analysis_label: VBCM of PCA factors
    relation: association
    evidence_ids:
    - P8-S2-C6
    - P13-S1-C11
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
      pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
      source_review: _compare/relationships-2026-11-16/review-current/Butler2014
      source_status_sha256: 17bb6508c1ef2ab7edea160094315a508c16aa05dad75c628e601912bd39ac74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C13
      - Accounting without a linked unit P1-S1-C14
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S1-C13
      - Unaccounted source passage P1-S1-C14
      - Unaccounted source passage P1-S2-C3
      - Result passage disposed without unit P2-S3-C4
      - Accounting without a linked unit P5-S3-C9
      - Unaccounted source passage P5-S3-C9
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P6-S2-C1
      - Accounting without a linked unit P6-S2-C3
      - Result passage disposed without unit P6-S2-C4
      - Unaccounted source passage P6-S2-C3
      - Result passage disposed without unit P6-S2-C10
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P6-S3-C4
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C6
      - Result passage disposed without unit P6-S3-C11
      - Result passage disposed without unit P8-S2-C10
      - Result passage disposed without unit P8-S2-C11
      - Result passage disposed without unit P8-S2-C12
      - Result passage disposed without unit P8-S2-C2
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C6
      - Accounting without a linked unit P10-S1-C2
      - Accounting without a linked unit P10-S1-C3
      - Accounting without a linked unit P10-S1-C7
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P9-S1-C5
      - Unaccounted source passage P10-S1-C2
      - Unaccounted source passage P10-S1-C3
      - Unaccounted source passage P10-S1-C7
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C3
      - Result passage disposed without unit P13-S1-C4
      - Accounting without a linked unit P13-S1-C5
      - Accounting without a linked unit P13-S1-C7
      - Unaccounted source passage P13-S1-C7
      - Unaccounted source passage P13-S1-C5
      - Result passage disposed without unit P14-S1-C4
      - Result passage disposed without unit P14-S1-C6
      - Result passage disposed without unit P15-S1-C10
      - Result passage disposed without unit P15-S1-C9
      - Result passage disposed without unit P15-S2-C4
      - Result passage disposed without unit P15-S2-C6
      - Result passage disposed without unit P15-S2-C7
      - Result passage disposed without unit P16-S1-C3
      - Accounting without a linked unit P16-S2-C4
      - Accounting without a linked unit P16-S2-C6
      - Accounting without a linked unit P16-S2-C8
      - Result passage disposed without unit P16-S3-C1
      - Accounting without a linked unit P16-S4-C2
      - Accounting without a linked unit P16-S4-C3
      - Unaccounted source passage P16-S4-C2
      - Unaccounted source passage P16-S2-C8
      - Unaccounted source passage P16-S2-C4
      - Unaccounted source passage P16-S4-C3
      - Unaccounted source passage P16-S2-C6
      unattached_null_or_qualifier_ids:
      - P6-S1-C3
      - P6-S2-C10
      - P8-S2-C6
      - P9-S1-C5
      - P10-S1-C10
      - P15-S1-C10
      - P16-S4-C2
      suppressed_nonrepresented_units: 40
      default_disposition_count_requires_completeness_check: 218
      unselected_timing_passages:
      - P1-S1-C9
      - P3-S1-C9
      - P3-S2-C11
      - P3-S2-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C1
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
        source_id: P16-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P2-S3-C4
        - P5-S3-C4
        - P6-S3-C12
        - P8-S1-C11
        - P8-S1-C12
        - P10-S1-C1
        - P10-S1-C10
        - P13-S1-C8
        - P13-S1-C10
        - P16-S1-C6
        - P16-S1-C1
        - P16-S2-C2
        - P16-S2-C3
        - P16-S2-C4
        - P16-S2-C5
        - P16-S2-C6
        - P16-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      - TABLE-3-page-8-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P5-S1
        - P6-S2
        - P6-S3
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S1
        - P10-S2
        - P10-S3
        - P11-S1
        - P12-S1
        - P13-S2
        - P14-S1
        - P14-S2
        - P15-S2
        - P15-S3
        - P16-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
      source_review: _compare/relationships-2026-11-16/review-current/Butler2014
      source_status_sha256: 17bb6508c1ef2ab7edea160094315a508c16aa05dad75c628e601912bd39ac74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the PCA factor labels based on loadings, not a measured relationship.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variance explained by PCA factors.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P1-S1-C14
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of semantic factor results.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of executive-cognition factor null result.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the general outcome of the methodology.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes threshold adjustment for lesion identification.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the selection of participants for symptom analysis.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohort heterogeneity.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes range of participant performance.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA variance explained.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to tables of loadings and scores.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the interpretation of Factor 1.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the interpretation of Factor 2.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes naming test loadings.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 3 loadings.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific test loadings on Factor 3.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Camel and Cactus Test loading.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes semantic control deficits in stroke aphasia.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the interpretation of the executive-cognition factor.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes unrotated PCA results.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation between severity and PCA factors.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets the correlation between severity and phonology.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Figure 1.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient positions in PCA space.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient positions in PCA space.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the ability of factor scores to capture graded patterns.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Broca's aphasia performance variation.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mixed non-fluent case positions.
    - source_id: P6-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the lesion overlap map.
    - source_id: P6-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes maximum lesion overlap in a specific voxel.
    - source_id: P6-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical thresholding.
    - source_id: P6-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical thresholding.
    - source_id: P6-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the software used for analysis.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Figure 3.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Finding regarding large lesion overlap between subtypes.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 14
      reason: Finding regarding larger overlaps in symptom-level analysis.
    - source_id: P8-S1-C7
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: Restatement of overlap findings.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Phonology factor association with left hemisphere regions.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Phonology factor association with left inferior prefrontal region.
    - source_id: P8-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Refers to Figure 5A.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Phonology factor association with white matter/arcuate fasciculus.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Semantic factor association with left anterior temporal lobe.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Semantic factor association with anterior middle temporal gyrus and
        temporal stem.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Semantic factor association with ventral language route white matter.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Null result for cognitive factor unique correlation.
    - source_id: P8-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports intercorrelations between non-PCA selected tests.
    - source_id: P8-S2-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Null result for non-word minimal pairs in non-PCA analysis.
    - source_id: P8-S2-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Synonym judgement association with subcortical/frontal clusters.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Delayed non-word repetition association with STG, MTG, and insula.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Spoken word-to-picture matching association with left anterior temporal
        lobe.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Null result for Raven's progressive matrices in PCA-guided analysis.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: PCA factors results unchanged by lesion volume inclusion.
    - source_id: P10-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlations between lesion volume and individual tests.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Lesion volume inclusion removed synonym judgement cluster.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: PCA-selected tests results survived lesion volume covariation.
    - source_id: P13-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P13-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P13-S1-C10
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of semantic factor results.
    - source_id: P13-S1-C11
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of executive-cognition null result.
    - source_id: P15-S1-C10
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of PCA-selected tests survival of lesion volume covariation.
    - source_id: P15-S2-C7
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of PCA factor results survival of lesion volume covariation.
    - source_id: P16-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P16-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P16-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of phonology factor results.
    - source_id: P16-S2-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of semantic factor results.
    unresolved_coverage:
    - source_id: P6-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S4-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S1-C7
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C13
    - P1-S1-C14
    - P1-S2-C3
    - P2-S3-C4
    - P5-S1-C4
    - P5-S3-C9
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P6-S1-C11
    - P6-S2-C1
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C9
    - P6-S2-C10
    - P6-S3-C4
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C9
    - P6-S3-C11
    - P8-S1-C1
    - P8-S1-C7
    - P8-S2-C2
    - P8-S2-C10
    - P9-S1-C5
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S2-C1
    - P11-S1-C1
    - P11-S1-C3
    - P11-S1-C5
    - P12-S1-C1
    - P12-S1-C2
    - P12-S1-C3
    - P13-S1-C4
    - P13-S1-C5
    - P13-S1-C7
    - P14-S1-C4
    - P14-S1-C6
    - P15-S1-C6
    - P15-S1-C9
    - P15-S2-C4
    - P15-S2-C5
    - P15-S2-C6
    - P15-S2-C8
    - P16-S1-C1
    - P16-S1-C3
    - P16-S2-C2
    - P16-S3-C1
    - P16-S4-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    - TABLE-3-page-8-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C11
      recruited_sample:
      - P3-S2-C4
      eligibility:
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C7
      imaging_provenance:
      - P4-S1-C12
      imaging_timing:
      - P3-S2-C4
      outcome_timing:
      - P3-S2-C4
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S4-C3
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S3-C3
      - P5-S4-C2
      - P5-S4-C3
      limitations:
      - P5-S2-C3
      - P16-S1-C4
      - P16-S4-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C11
      - P10-S1-C10
      - P15-S1-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C11
      - P4-S2-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C1
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
      source_id: P16-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P2-S3-C4
      - P5-S3-C4
      - P6-S3-C12
      - P8-S1-C11
      - P8-S1-C12
      - P10-S1-C1
      - P10-S1-C10
      - P13-S1-C8
      - P13-S1-C10
      - P16-S1-C6
      - P16-S1-C1
      - P16-S2-C2
      - P16-S2-C3
      - P16-S2-C4
      - P16-S2-C5
      - P16-S2-C6
      - P16-S2-C8
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
      pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
      review_sha256: 85bed5e1bfe702750c9730868f99dbab994031393652dd9018982905cf093bb2
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
      - P8-S2-C6
      - P13-S1-C11
      source_result: The study performed Voxel-Based Cortical Morphometry (VBCM) using
        three orthogonal PCA factors (phonological, semantic, executive-cognition)
        as continuous predictors of neural tissue concentration in 31 patients with
        chronic stroke aphasia. While the phonological and semantic factors showed
        significant unique associations with specific brain regions, the executive-cognition
        factor did not uniquely covary with any brain regions; no clusters survived
        correction for multiple comparisons.
      result_status: not_detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the VBCM analysis of
            PCA factors. The source (P8-S1-C8, P8-S2-C6) confirms that VBCM was used
            to relate PCA factor scores to tissue concentration, and specifically
            that the executive-cognition factor was one of the three factors analyzed.
          source_ids:
          - P8-S1-C8
          - P8-S2-C6
          - P5-S4-C2
        direction:
          answer: fits
          reason: The source explicitly states that 'there were no clusters that correlated
            uniquely with the cognitive factor score and survived correction for multiple
            comparisons' (P8-S2-C6) and that the factor 'did not uniquely covary with
            any brain regions' (P13-S1-C11). The draft's 'no_effect' direction accurately
            reflects this null finding.
          source_ids:
          - P8-S2-C6
          - P13-S1-C11
        construct:
          answer: fits
          reason: The exposure is correctly identified as the 'executive-cognition
            factor' derived from PCA. The outcome is 'neural tissue concentration'
            via VBCM. The source confirms the use of VBCM to index neural integrity
            (P5-S2-C10) and the extraction of an executive-cognition factor (P13-S1-C4).
            The patient measurement is voxel tissue concentration, not template lesion
            overlap or patient diffusion.
          source_ids:
          - P13-S1-C4
          - P5-S2-C10
          - P8-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the analysis controlled
            for phonological and semantic factors. This is supported by P5-S4-C3 and
            P8-S1-C9, which state that the factors are orthogonal and entered simultaneously,
            meaning the result denotes unique variance. The draft also includes the
            limitation that the test battery was not designed to extensively assess
            executive capacities (P16-S4-C3), which is a material caveat for interpreting
            the null result.
          source_ids:
          - P5-S4-C3
          - P8-S1-C9
          - P16-S4-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitation from P16-S4-C3 regarding the
            test battery's design and lesion distribution. It also correctly notes
            the control for lesion volume (P10-S2-C2). No other material caveats that
            would change the interpretation of the null result appear to be missing
            from the provided source window.
          source_ids:
          - P16-S4-C3
          - P10-S2-C2
      optional_pending:
      - Specific threshold values for the null result (P < 0.001 voxel, P < 0.001
        FWE cluster) are not transcribed in the draft but are present in source P8-S1-C10.
      - Exact list of tests loading on the executive factor is not fully detailed
        in the draft, though P3-S4-C2 lists the cognitive tests used.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific threshold values for the null result (P < 0.001 voxel, P < 0.001 FWE
      cluster) are not transcribed in the draft but are present in source P8-S1-C10.
    - Exact list of tests loading on the executive factor is not fully detailed in
      the draft, though P3-S4-C2 lists the cognitive tests used.
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: executive-cognition factor
      outcome:
        text: neural tissue concentration
      analysis_label: VBCM of PCA factors
      relation: association
      evidence_ids:
      - P8-S2-C6
      - P13-S1-C11
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
        pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
        source_review: _compare/relationships-2026-11-16/review-current/Butler2014
        source_status_sha256: 17bb6508c1ef2ab7edea160094315a508c16aa05dad75c628e601912bd39ac74
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fb176d1523eecf090f780a6bc19acd153705d386e5b28f344cb0b99d39ce4520
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C4
          page: 3
          text_layer_sha256: fb176d1523eecf090f780a6bc19acd153705d386e5b28f344cb0b99d39ce4520
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants were included if they had chronic stroke aphasia,

          i.e. they had an enduring impairment in producing and/or understand-

          ing spoken language and were at least 12 months post-stroke at time

          of scanning and assessment (n = 31).'
        anchor_text: 'Participants were included if they had chronic stroke aphasia,

          i.e. they had an enduring impairment in producing and/or understand-

          ing spoken language and were at least 12 months post-stroke at time

          of scanning and assessment (n = 31).'
        excluded_fragments: []
        image_sha256: 4bbdab8f45557b938276d00f0d072c05bacc9d5ef57df7d19922201c204d6c23
        transcription: . Participants were included if they had chronic stroke aphasia,
          i.e. they had an enduring impairment in producing and/or understanding spoken
          language and were at least 12 months post-stroke at time of scanning and
          assessment (n = 31)
      P10-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1917dd467147c4eee35cec2dade1187d21e6eff812a01b3fe2096f7b11b70cc8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 521e023209c5c8613920d41f8ef1f6d022793f46b5ca142ac962bf0d044df828
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S2-C2
          page: 10
          text_layer_sha256: 521e023209c5c8613920d41f8ef1f6d022793f46b5ca142ac962bf0d044df828
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Lesion

          volume was included in each VBCM model with results thresh-

          olded at P 5 0.005 voxel-level, P 4 0.01 FWE corrected cluster-

          level.'
        anchor_text: 'Lesion

          volume was included in each VBCM model with results thresh-

          olded at P 5 0.005 voxel-level, P 4 0.01 FWE corrected cluster-

          level.'
        excluded_fragments: []
        image_sha256: 55d99efd07ee6687007d7c597cd873c42187ab470e2788a36934cd8776674aec
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'In contrast to the phonological and

    semantic factors, there were no clusters that correlated uniquely

    with the cognitive factor score and survived correction for multiple

    comparisons.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
