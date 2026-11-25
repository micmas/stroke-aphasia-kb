---
id: event_based_pm_scores
name: event-based PM scores
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: processing_speed
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: processing_speed
  target_kind: impairment
  claim: Higher event-based PM scores correlated with faster processing speed.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 58
    population: acute and early sub-acute stroke patients
    phase: not_reported
    time_post_onset: 2–62 days post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The study sampled stroke patients who were relatively high functioning, likely
    due to self-selection bias.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Event-based prospective memory performance measured
    using the event-based cue subscale of the Memory for Intentions Screening Test
    - Short Form (MIST-SF). The association was specific to event-based PM, whereas
    overall and time-based PM performance were associated with executive functioning
    measures. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P4-S1-C9, two-model agreement, human
    verification pending): . There were 58 stroke patients included in the

    sample (31 % female) Original text-layer quotation is preserved below. PDF image
    reading (P4-S1-C6, two-model agreement, human verification pending): . Participants
    took part 2–62 days post-stroke (M = 19.03, SD =

    14.75) Original text-layer quotation is preserved below. PDF image reading (P3-S2-C6,
    two-model agreement, human verification pending): .

    We administered a short form of the Memory for Intentions

    Screening Test (MIST-SF; Raskin et al., 2016), modified for bedside

    administration, to acute and early sub-acute stroke patients (1 day–3

    months post-stroke) Original text-layer quotation is preserved below.'
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
    - proposed_concept:processing_speed
  citation: '@Gilbert2025'
  source_passages:
  - section: Original source P1-S1-C13
    page: 1
    quote: "Better overall PM performance and time-based PM performance was \nassociated\
      \ with better performance on executive functioning measures, while higher event-based\
      \ PM scores only \ncorrelated with faster processing speed."
    supports: claim
  - section: Original source P4-S1-C9
    page: 4
    quote: "There were 58 stroke patients included in the \nsample (31 % female)."
    supports: sample
  - section: Original source P4-S1-C6
    page: 4
    quote: 'Participants took part 2–62 days post-stroke (M = 19.03, SD =

      14.75).'
    supports: method
  - section: Original source P3-S2-C6
    page: 3
    quote: "We administered a short form of the Memory for Intentions \nScreening\
      \ Test (MIST-SF; Raskin et al., 2016), modified for bedside \nadministration,\
      \ to acute and early sub-acute stroke patients (1 day–3 \nmonths post-stroke)."
    supports: method
  - section: Original source P11-S2-C7
    page: 11
    quote: "Finally, \nour study sampled stroke patients who were relatively high\
      \ functioning \n(likely due to self-selection bias)."
    supports: limitation
predictor_type: behavioural
short_definition: Event-based prospective memory performance measured using the event-based
  cue subscale of the Memory for Intentions Screening Test - Short Form (MIST-SF).
assessment:
- Memory for Intentions Screening Test - Short Form (MIST-SF)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Gilbert2025
  proposal_id: R003
  review_status_sha256: b974cc51e1f2063fdd0d5a180da4bbd7107bec00acf5a2da008fc40595f2a9cf
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
        A/passages.json: 3745e8a5df8444f1ba4de72099265c177eacab8c8b09aa61a1b5f7f196f7d7b3
        A/raw.json: 010915d4fa28094e3bcaff350884afebb061a5be670cbe7725afef21124ff556
        A/source-units.json: e39ee8c5c1d0c0a40bc86b2c5dcea8cbc830d4223b872d542b75c678567c4e20
        A/full-source-units.json: b04c1f5df81a4f036cf70e5db9ebfcd6d73accb74bcd917c7286c3df339f9521
        A/meta.json: 5da90380f5435faaefa8b64204c09823dfc01bd802f87bc320ea1d073411b7f4
        A/table-images/TABLE-1-page-5-1.png: 0f05c7bf59c246d722cb79db513b870f709ab68c555cc886d4498f9785bcb81c
        A/table-images/page-11.png: 115454eecb05beb76f2873663c4e10af0e9466ae79bf614843b4ce9c96a45cd4
        A/table-images/TABLE-5-page-8-1.png: 12a0d794f9c576ebd1aa4c04fa41c3cefad846ac2045a112df5f7bbf0cad8fa6
        A/table-images/page-6.png: d62049a57e81448bd9a4a80bf35d49b78b13ab694a213fb90083fb939a849faf
        A/table-images/page-7.png: 9e54338ffa2227450fdc8069705d3989152b9df1da6af450d719390f1f9a464e
        A/table-images/page-5.png: c7e90e1989847f9a4c479c32538c46cd6ce98e0fae11afbea5652bf39da1dbed
        A/table-images/page-8.png: bf51189a3a36cd20d29c4c2ce2247e1178a9a45d3f5dba11718979aa477c2a18
        A/table-images/TABLE-3-page-6-2.png: 3323f6772d768285eab81e8488b0e9306231d08954640e0d93e48222bb62e7aa
        A/table-images/TABLE-2-page-6-1.png: aee0b9975f69aac8bb4084f5aa7024d2deb153655f1fb678c47811baab67f682
        A/table-images/TABLE-A1-page-11-1.png: 1f39398882639ff94ebcaba37836eaac4f8a9616a204fced0c5a94d3e68a95b4
        A/table-images/manifest.json: 0cc384ae81389de0fb05efe836bb3c34ce7ebc6208b875f7eb58fa64adc0daf7
        A/table-images/TABLE-4-page-7-1.png: e1f2c2a2057716b905aed5de3c8eb2c1f330aa5fb9ade751bbb73bdb57332db2
        A/clauses/window-11/raw.json: 3f8384ff771d46fd32322c935b881c849a61f9ae347a5121755ac5d99f4df74b
        A/clauses/window-11/prompt.txt: ed649f85ce12c282e87043182f3174b99b02af7b0569978f30c08897233fcfd7
        A/clauses/window-11/meta.json: 0cb7021884e4b52fbefe54430ecdaf26a7001f57233c248a99397c17cd22d617
        A/clauses/window-10/raw.json: 331f2786d498572162919e6206761f639b95020625b6f99e33890ada5401052a
        A/clauses/window-10/prompt.txt: db44c59ddd860fab598e10a3342269b7ba121bab3ab3032829ff523243fadf74
        A/clauses/window-10/meta.json: 8a82652c8580276465cc0141edc66bd6308074bda31616e97a4b26527118c706
        A/clauses/window-03/raw.json: 7e566f1605fb4e9edf10a7753015152ae335ed9d1afa1281aa3fea74f56c504e
        A/clauses/window-03/prompt.txt: 506e61d477e909e42e2fb04f2b2ba70de1d299d2bf33e8452368101a4afe7981
        A/clauses/window-03/meta.json: b982a6ebe0e3c9e1a914be624b03078d0862be253de5c8c57d58d54a910e8b95
        A/clauses/window-04/raw.json: 3c7ca966229ab242bd9b965c54003c501987f0447e3a806fefacf5ffa7ed6c05
        A/clauses/window-04/prompt.txt: b19916f45198ea97eedc90aa9067a61ea475445c06e32a9e807837bab593fae8
        A/clauses/window-04/meta.json: e2a40e5464edfbcd30f3ad75e589bbd094d9b50d89c1f8aa47b91d79871a48e4
        A/clauses/window-05/raw.json: e4970912f8cbd8a0db61bec5c940c1474215cd12e27722b931aa4a760b3f2639
        A/clauses/window-05/prompt.txt: 2d18af8c75c11baa874555c7b829bef679965ae27528d2d49639a9841930e272
        A/clauses/window-05/meta.json: 4a3587c6c0b82f124e71c7f1880b8f831b5bc512650fbc9e99f2be83fc41ceb6
        A/clauses/window-02/raw.json: 4aa92e18c73b929cca85bb97ea4648b279275b1e4c3767d866f233ba0aded282
        A/clauses/window-02/prompt.txt: 9fdd3b0820993c5c25bec7fb6597f6f09deebfbbbff4638c5d559f4f57ac47e1
        A/clauses/window-02/meta.json: 099002ba09ce7302343b80c5ad3d6232075d7767a97d731ddabd029758d7d3c4
        A/clauses/window-12/raw.json: cd3482e88aa64b5102643b80e30531b4da50d419c38e05e9be05a5c4a32f6120
        A/clauses/window-12/prompt.txt: 6dce140aa8cbca9b0828a55f200c1b4960a7ce50f1da48621799002803f90058
        A/clauses/window-12/meta.json: bf14a6c9f464ded604c8d835e7b80b62c9d4d43358770c06812965bbdd3c4d96
        A/clauses/window-13/raw.json: a45f0ec11acd3a255593382ab86f073f2864657fec7c00b809cd448804e0d0be
        A/clauses/window-13/prompt.txt: 362c3b4f15cf581180503c7d5c886a47d5bea00923ba6eb5b0659ad2773a9ae1
        A/clauses/window-13/meta.json: 371ca9a4ec4ef21fb5ca6b1f24e69fd11ab2d9db758e72e936be20baa4027a02
        A/clauses/window-09/raw.json: b060aa4dd8dba6ac2b56a7aedd3fd9b7ee13a5b01af2fa18171a3d8b8ae58304
        A/clauses/window-09/prompt.txt: 00956135a4b3f8162f9b56681d015f5ed6b8c4c6824b65b52dd70d8cf19ac4ec
        A/clauses/window-09/meta.json: b0e21761fb21c1b33be26deb5bf59e05d3834d0e0bf70be44ae40537a417eeae
        A/clauses/window-07/raw.json: 898e62ce0858e041fc7f63b4423b69da2be42e273231b78deb71dee7c71b3571
        A/clauses/window-07/prompt.txt: fbd6809a83d431370e33532a9214bec053ad728ed5b11867e60f0d831ba6282c
        A/clauses/window-07/meta.json: ceedd2bc4bf9c64e551fa77db2bcf32e7aa04cf84e23c2d7f6a8d242fc32fc3a
        A/clauses/window-01/raw.json: d2a1e5bbbdd3e54afba3f792e4d8d02024409f7d7e8bee1217061a2ff6349d22
        A/clauses/window-01/prompt.txt: 39487383e4343bafd94ac47dd5d3fbc1065c3de928d534924e467d2b6958903c
        A/clauses/window-01/meta.json: 8a1f64726e008c33ea8cf1e653389894e8b4e1c3a096696c9a5ad40fd6ec0775
        A/clauses/window-06/raw.json: d3847ff3d053a7ec3286f4a3f701dacd30f4c0dc2d8c33392a7e86178fc34b3e
        A/clauses/window-06/prompt.txt: d2044611d9bdb201c29018c6bddb70b03523dec4ed8a9f5a9ffca9cecedf003c
        A/clauses/window-06/meta.json: 0b78965da4cf04a5ae4a0048a2e0df8293cf4a3b9cd703b42e36af58b08017d0
        A/clauses/window-08/raw.json: 2d2cbc6a353f99de36ddc493e75b55d969151191b2000049b3573b493aef5684
        A/clauses/window-08/prompt.txt: 31c11d22ac9f7a2ed394c0965e6d6f4307bc3c1c6f3304ee550afa681c20bad6
        A/clauses/window-08/meta.json: ec718c43f219403e1158e15246b0c6c32aa8ad36765c20c3ebacd2130b96bf1b
        A/tables/TABLE-5-page-8-5/raw.json: cb13e297626723afdf2adb39561f5562808197af5cf330b70188af9cb01bb217
        A/tables/TABLE-5-page-8-5/prompt.txt: acddcf971d64a5833a848b0b1a7a570a743098e29f5d188e151c4e1f735a6041
        A/tables/TABLE-5-page-8-5/meta.json: d7a1c3139dc06b996fb81a3388a93c946488e3729c2829e463863488bf9b97c9
        A/tables/TABLE-1-page-5-1/raw.json: 489b067816d80fa326d97fed3e5d697a566fe70b0695fba9ba9703f1f7c5647f
        A/tables/TABLE-1-page-5-1/prompt.txt: f5957c8b74c6a3418ceab985cf2a7bb34bbfee115669744539a561b7078cd030
        A/tables/TABLE-1-page-5-1/meta.json: 2da6c88e63ab75670a9ab2669e7d60d4bcd7fa7017f41bd67e4cbf930eab70af
        A/tables/TABLE-3-page-6-3/raw.json: 1f66b349de401c63f868e50963d8d02c4a59aa386ed5a5398e955cd22010c1a6
        A/tables/TABLE-3-page-6-3/prompt.txt: 9fcb8d670d62281cabe095bcab3d9520a116a6b8e6a7387aaf3034c3d72661de
        A/tables/TABLE-3-page-6-3/meta.json: 07d958ed9eb13d2673862f271457025a4bdda5880873535dcd9317713cb0dcd6
        A/tables/TABLE-2-page-6-2/raw.json: bfd2979b78288ce400dae5bf0b5675cf298e41409a8775e22b14d61e9e423089
        A/tables/TABLE-2-page-6-2/prompt.txt: c824a2fdc22e38985be5a9dc815aca48a6d91265463277d8246fc3c7079d6e29
        A/tables/TABLE-2-page-6-2/meta.json: 9b57eb88608625f4206b2025771c20341884f16d937152b30e37e701c7cde6ab
        A/tables/TABLE-4-page-7-4/raw.json: 3fced9af15f9994c1039d3b8f405ca4e48fe65703c53a7c68d42d1a6aca1e4a8
        A/tables/TABLE-4-page-7-4/prompt.txt: 9e48034ab0677765a196058318e5d154173d40036bff7dc75c4f0a43fa149a1e
        A/tables/TABLE-4-page-7-4/meta.json: 10a270080618679e5bd918adb9137bf370bcf371b46bf9bfa43b8e21bc311821
        A/tables/TABLE-A1-page-11-6/raw.json: 6a937957d4d696a3732b8cb0f9746289c5f9b47c4c0695964b5ad6fe853fc061
        A/tables/TABLE-A1-page-11-6/prompt.txt: 6a88dd0cdad41c7d40d31b7cac8b14c3998e07a4b4e0b039972ce0ac156b0852
        A/tables/TABLE-A1-page-11-6/meta.json: 3b7e3d2bc333c38fe83056a0284b41867ed2d2917434ea6d6df24bfb503129aa
        B/passages.json: 3745e8a5df8444f1ba4de72099265c177eacab8c8b09aa61a1b5f7f196f7d7b3
        B/raw.json: 48939e02c74cdf8f6fad637ad183ad1f00afb30df41b6cb5a9cfeee6b024b43a
        B/source-units.json: e39ee8c5c1d0c0a40bc86b2c5dcea8cbc830d4223b872d542b75c678567c4e20
        B/full-source-units.json: b04c1f5df81a4f036cf70e5db9ebfcd6d73accb74bcd917c7286c3df339f9521
        B/meta.json: 13512cd1b4047723df9987532075a8186c05e3bda40ceb6d3b73ebf6e922af35
        B/table-images/TABLE-1-page-5-1.png: 0f05c7bf59c246d722cb79db513b870f709ab68c555cc886d4498f9785bcb81c
        B/table-images/page-11.png: 115454eecb05beb76f2873663c4e10af0e9466ae79bf614843b4ce9c96a45cd4
        B/table-images/TABLE-5-page-8-1.png: 12a0d794f9c576ebd1aa4c04fa41c3cefad846ac2045a112df5f7bbf0cad8fa6
        B/table-images/page-6.png: d62049a57e81448bd9a4a80bf35d49b78b13ab694a213fb90083fb939a849faf
        B/table-images/page-7.png: 9e54338ffa2227450fdc8069705d3989152b9df1da6af450d719390f1f9a464e
        B/table-images/page-5.png: c7e90e1989847f9a4c479c32538c46cd6ce98e0fae11afbea5652bf39da1dbed
        B/table-images/page-8.png: bf51189a3a36cd20d29c4c2ce2247e1178a9a45d3f5dba11718979aa477c2a18
        B/table-images/TABLE-3-page-6-2.png: 3323f6772d768285eab81e8488b0e9306231d08954640e0d93e48222bb62e7aa
        B/table-images/TABLE-2-page-6-1.png: aee0b9975f69aac8bb4084f5aa7024d2deb153655f1fb678c47811baab67f682
        B/table-images/TABLE-A1-page-11-1.png: 1f39398882639ff94ebcaba37836eaac4f8a9616a204fced0c5a94d3e68a95b4
        B/table-images/manifest.json: 6b2bb53781f9881609a687e79e7219be0505c30ca7bbaad4c37c4d644fe01074
        B/table-images/TABLE-4-page-7-1.png: e1f2c2a2057716b905aed5de3c8eb2c1f330aa5fb9ade751bbb73bdb57332db2
        B/clauses/window-11/raw.json: 66dac675114c1f445bd295a784ebb9ac89fa0ed1ae7683bb2097c40da254e818
        B/clauses/window-11/prompt.txt: ed649f85ce12c282e87043182f3174b99b02af7b0569978f30c08897233fcfd7
        B/clauses/window-11/meta.json: 4fcfc97803b94c1f600490181ae48d01410254feef0ac2dbd49b5d0169b0c348
        B/clauses/window-10/raw.json: 2a9bf5f94d971bead55c25ca58e7c06298794992604c06b7f5ec8c483a831d0d
        B/clauses/window-10/prompt.txt: db44c59ddd860fab598e10a3342269b7ba121bab3ab3032829ff523243fadf74
        B/clauses/window-10/meta.json: 691e3127d808427e82ad870c364fbba2b9cba5f0a4d788de5837e3a7a084b2b1
        B/clauses/window-03/raw.json: 9e413a8905a85fc5a4d3f99b0007c3a08a2dfd8abc50811a6edaa4ad03be2251
        B/clauses/window-03/prompt.txt: 506e61d477e909e42e2fb04f2b2ba70de1d299d2bf33e8452368101a4afe7981
        B/clauses/window-03/meta.json: 4eb12378212727822891a24444cf68b96b320a42fdf72a74e116a34ac0e62135
        B/clauses/window-04/raw.json: a75468e348afa32302d8a122387fda591c1893ef5ed6d8b7d090aa78593974bd
        B/clauses/window-04/prompt.txt: b19916f45198ea97eedc90aa9067a61ea475445c06e32a9e807837bab593fae8
        B/clauses/window-04/meta.json: 2758be180671d1a5c0c93c124c845ea92a5fda07779824bc127f0136f78b2deb
        B/clauses/window-05/raw.json: 39cac037b0a4c18eeeaedced161be7d6f49d793b9c5682514888895e9c8ff0eb
        B/clauses/window-05/prompt.txt: 2d18af8c75c11baa874555c7b829bef679965ae27528d2d49639a9841930e272
        B/clauses/window-05/meta.json: 6e997adce8e90a5834e97029806fc2ff9fb2e6368e90094658bb6110f947a9f6
        B/clauses/window-02/raw.json: 51120a9db9812964cf3a1669eb8a7357f7585c47d93065255fcdebf177a1d2e6
        B/clauses/window-02/prompt.txt: 9fdd3b0820993c5c25bec7fb6597f6f09deebfbbbff4638c5d559f4f57ac47e1
        B/clauses/window-02/meta.json: 89b1239e2b83792480465390421349e31f24130e6ac73252132ac142b2d2f406
        B/clauses/window-12/raw.json: 9144c91dcc7cad02524620fa4042cefd1022a07db6711f35a7e45b36ea987d1c
        B/clauses/window-12/prompt.txt: 6dce140aa8cbca9b0828a55f200c1b4960a7ce50f1da48621799002803f90058
        B/clauses/window-12/meta.json: d25469ebc96e5daa3408518bdd1262cffa477340d0e42fe5379f380c60f53cfe
        B/clauses/window-13/raw.json: a45f0ec11acd3a255593382ab86f073f2864657fec7c00b809cd448804e0d0be
        B/clauses/window-13/prompt.txt: 362c3b4f15cf581180503c7d5c886a47d5bea00923ba6eb5b0659ad2773a9ae1
        B/clauses/window-13/meta.json: 447a73933954330e3094ede9b2aed76b581d529ca3ade27f3a189e7adfdeaa40
        B/clauses/window-09/raw.json: 0883a1274be8ab1474e1763f29aab3063f4250ca2224a4b5ccd32967a6ba08d2
        B/clauses/window-09/prompt.txt: 00956135a4b3f8162f9b56681d015f5ed6b8c4c6824b65b52dd70d8cf19ac4ec
        B/clauses/window-09/meta.json: 35f66b51b855951a8d9567b78fd8767e859a9e543f13f35e5ce65205feb9d4d9
        B/clauses/window-07/raw.json: 18278fd5dbc48bc6c65c6472cf0ab0e10294b5085084cf5e19b9fd3d77b921a1
        B/clauses/window-07/prompt.txt: fbd6809a83d431370e33532a9214bec053ad728ed5b11867e60f0d831ba6282c
        B/clauses/window-07/meta.json: bc1a79750713c5c24ae8ef1b9d7ab629d9c6d92a178aebddb1476bb4fea5ecf6
        B/clauses/window-01/raw.json: 5c69bf1ad3ce4a70770acfc118d5a4b7ceda8fff4b9d69ee0b3d68739e77704e
        B/clauses/window-01/prompt.txt: 39487383e4343bafd94ac47dd5d3fbc1065c3de928d534924e467d2b6958903c
        B/clauses/window-01/meta.json: 760561e6b05920889d2ec4387b49a4c1bbe5dda3d8e7ad14e0b97cc7908568d7
        B/clauses/window-06/raw.json: 3107444a1b230ec7af2375a9b188f0e1ce75417e28123bb4a546f48122fe2985
        B/clauses/window-06/prompt.txt: d2044611d9bdb201c29018c6bddb70b03523dec4ed8a9f5a9ffca9cecedf003c
        B/clauses/window-06/meta.json: 2f857b7d76db137734397bd660a563083b2e9b420369053c1c1d066684c42135
        B/clauses/window-08/raw.json: e9817e6ec714193ae00dad3d82b0cb77d5fa5e8d144c598e52332389ca5a0c8b
        B/clauses/window-08/prompt.txt: 31c11d22ac9f7a2ed394c0965e6d6f4307bc3c1c6f3304ee550afa681c20bad6
        B/clauses/window-08/meta.json: c281221254a7518f8a7d5c0e0627e04d8f632f162c4b7050e3ad8e59d2f2ff66
        B/tables/TABLE-5-page-8-5/raw.json: efa753768b7389dceca30e61557abda8d41734e7fe8416d6d45d323241c7b202
        B/tables/TABLE-5-page-8-5/prompt.txt: acddcf971d64a5833a848b0b1a7a570a743098e29f5d188e151c4e1f735a6041
        B/tables/TABLE-5-page-8-5/meta.json: 0fb7f1b73b56e02a467aae2c026fceaf313751cde2e96b327604a57fbf9ae944
        B/tables/TABLE-1-page-5-1/raw.json: b814869aab8dc4be56d693bba9db38f6bd85af4642e91363629843923b252418
        B/tables/TABLE-1-page-5-1/prompt.txt: f5957c8b74c6a3418ceab985cf2a7bb34bbfee115669744539a561b7078cd030
        B/tables/TABLE-1-page-5-1/meta.json: 824ee08a908f86dd23aead32434c324cad4249aed372887a657ee8ad315586a6
        B/tables/TABLE-3-page-6-3/raw.json: 5bab722adae3b08ef42896a511dc4826814176e5055b68b7c9e8ec353f7d7ba7
        B/tables/TABLE-3-page-6-3/prompt.txt: 9fcb8d670d62281cabe095bcab3d9520a116a6b8e6a7387aaf3034c3d72661de
        B/tables/TABLE-3-page-6-3/meta.json: dc333b6dc091c94a3c51988131eeeb3d08d9c3662b0aeac1961ed3acf05ff369
        B/tables/TABLE-2-page-6-2/raw.json: 89a0007e0b72e73e719a2acf02f4f987f39adf719f4c2b19fa632d7ab5d597c5
        B/tables/TABLE-2-page-6-2/prompt.txt: c824a2fdc22e38985be5a9dc815aca48a6d91265463277d8246fc3c7079d6e29
        B/tables/TABLE-2-page-6-2/meta.json: cdb5928fc957c0915495c9f0ff5d63f4d6b8545713a896d5743d5dcf7eec82d4
        B/tables/TABLE-4-page-7-4/raw.json: 2526dc901dee2d2dcbccfce38cc7fa495c89601dbb14a33d5fd94d4f5bb0ef7a
        B/tables/TABLE-4-page-7-4/prompt.txt: 9e48034ab0677765a196058318e5d154173d40036bff7dc75c4f0a43fa149a1e
        B/tables/TABLE-4-page-7-4/meta.json: 38140b897894780c0bb4cfd4f9a578f7a05ef77b24deabcbd4d73260843af0b8
        B/tables/TABLE-A1-page-11-6/raw.json: fbf657b38a91bd7099ec422dd67c9691aaed8b1544f52ec62ef3fd9f027bbfee
        B/tables/TABLE-A1-page-11-6/prompt.txt: 6a88dd0cdad41c7d40d31b7cac8b14c3998e07a4b4e0b039972ce0ac156b0852
        B/tables/TABLE-A1-page-11-6/meta.json: 0ba6767e032df6f5be44795a70840b7c53002e029a99b7a0cfc42d4d28b053a0
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
      pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
      source_review: _compare/relationships-2026-11-16/review-current/Gilbert2025
      source_status_sha256: 73bcb3c93826a5b4e386ee2ce3b048f237c324abbc4662161e01dc159950c8ea
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: event-based PM scores
    outcome:
      text: processing speed
    analysis_label: Event-based PM and Processing Speed
    relation: association
    evidence_ids:
    - P1-S1-C13
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
      pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
      source_review: _compare/relationships-2026-11-16/review-current/Gilbert2025
      source_status_sha256: 73bcb3c93826a5b4e386ee2ce3b048f237c324abbc4662161e01dc159950c8ea
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C13
      - Accounting without a linked unit P1-S1-C14
      - Accounting without a linked unit P1-S1-C15
      - Accounting without a linked unit P1-S1-C16
      - Unaccounted source passage P1-S1-C13
      - Unaccounted source passage P1-S1-C14
      - Unaccounted source passage P1-S1-C16
      - Unaccounted source passage P1-S1-C15
      - Accounting without a linked unit P4-S1-C16
      - Accounting without a linked unit P4-S2-C2
      - Accounting without a linked unit P4-S2-C7
      - Accounting without a linked unit P4-S2-C8
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P4-S1-C16
      - Unaccounted source passage P4-S2-C2
      - Result passage disposed without unit P4-S2-C10
      - Result passage disposed without unit P4-S2-C12
      - Result passage disposed without unit P5-S2-C11
      - Result passage disposed without unit P5-S3-C9
      - Accounting without a linked unit P7-S1-C10
      - Accounting without a linked unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C12
      - Result passage disposed without unit P7-S1-C13
      - Result passage disposed without unit P7-S2-C3
      - Result passage disposed without unit P7-S2-C4
      - Unaccounted source passage P7-S1-C10
      - Unaccounted source passage P7-S1-C11
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P8-S1-C9
      - Accounting without a linked unit P8-S2-C1
      - Accounting without a linked unit P8-S2-C3
      - Accounting without a linked unit P8-S2-C4
      - Accounting without a linked unit P8-S2-C7
      - Unaccounted source passage P8-S2-C4
      - Unaccounted source passage P8-S2-C3
      - Unaccounted source passage P8-S2-C7
      - Unaccounted source passage P8-S2-C1
      - Result passage disposed without unit P9-S1-C8
      - Result passage disposed without unit P9-S2-C7
      - Result passage disposed without unit P9-S2-C8
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P9-S2-C10
      - Result passage disposed without unit P9-S2-C9
      - Accounting without a linked unit P9-S3-C3
      - Accounting without a linked unit P9-S3-C6
      - Unaccounted source passage P9-S3-C3
      - Unaccounted source passage P9-S3-C6
      - Result passage disposed without unit P10-S1-C10
      - Accounting without a linked unit P10-S1-C11
      - Accounting without a linked unit P10-S2-C2
      - Accounting without a linked unit P10-S2-C4
      - Result passage disposed without unit P11-S1-C1
      - Accounting without a linked unit P11-S1-C3
      - Unaccounted source passage P10-S1-C11
      - Unaccounted source passage P10-S2-C4
      - Unaccounted source passage P10-S2-C2
      - Unaccounted source passage P11-S1-C3
      unattached_null_or_qualifier_ids:
      - P1-S1-C13
      - P1-S1-C14
      - P1-S1-C15
      - P4-S2-C7
      - P4-S2-C10
      - P4-S2-C12
      - P8-S2-C4
      - P8-S2-C7
      - P9-S2-C9
      - P9-S2-C10
      - P9-S3-C6
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 292
      unselected_timing_passages:
      - P1-S1-C11
      - P3-S2-C6
      - P4-S1-C10
      - P4-S1-C15
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C6
      - P7-S2-C12
      - P8-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P6-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P6-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: limitations
        source_ids:
        - P7-S1-C5
        - P9-S2-C6
        - P10-S1-C3
        - P11-S1-C5
        - P11-S1-C6
        - P11-S1-C9
        - P11-S1-C10
        - P11-S1-C11
        - P11-S1-C12
        - P11-S1-C13
        - P11-S2-C2
        - P11-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P5-S3-C3
        - P5-S3-C4
        - P7-S2-C5
        - P7-S2-C7
        - P7-S2-C8
        - P8-S3-C3
        - P8-S3-C4
        - P9-S3-C7
        - P10-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      - TABLE-5-page-8-5
      - TABLE-A1-page-11-6
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-A1-page-11-6
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S3
        - P8-S4
        - P9-S3
        - P10-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
      source_review: _compare/relationships-2026-11-16/review-current/Gilbert2025
      source_status_sha256: 73bcb3c93826a5b4e386ee2ce3b048f237c324abbc4662161e01dc159950c8ea
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: States PM deficits in acute patients on 7/11 measures.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Links PM performance to executive functioning and processing speed.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: States no significant difference between acute and follow-up PM.
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: States acute PM predicts long-term PM but not other outcomes.
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 6
      reason: States limited conclusions on lesion anatomy due to overlap.
    - source_id: P4-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching of age and education.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of NART-IQ.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of age.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of education and IQ.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of reassessed vs non-reassessed patients.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of imaging subset to total sample.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about non-normal distribution of variables.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about meeting analysis assumptions.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Stroke patients scored lower on 7/11 MIST-SF measures.
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Lists the specific 7 measures showing deficits.
    - source_id: P5-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares effect sizes of time-based vs event-based deficits.
    - source_id: P5-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists measures with no significant differences.
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary materials.
    - source_id: P5-S3-C13
      disposition: represented
      result_indexes:
      - 11
      reason: Association between age and PM scores.
    - source_id: P5-S3-C14
      disposition: represented
      result_indexes:
      - 11
      reason: Association between gender and event-based PM.
    - source_id: P5-S3-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Links TMT-A, TMT-B, Stroop, and semantic fluency to PM Summary Scores.
    - source_id: P5-S3-C16
      disposition: represented
      result_indexes:
      - 1
      reason: Differentiates cognitive predictors for time-based vs event-based PM.
    - source_id: P5-S4-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of cognitive associations.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifies that certain executive processes associate with time-based
        but not event-based PM.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding in control group.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for clinical measures.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for follow-up stroke vs control.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of effect sizes at acute stage.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of effect sizes at follow-up.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: No significant improvement from acute to follow-up.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Acute PM Summary Scores predict follow-up Summary Scores.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Acute PM predicts follow-up anxiety and executive apathy.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlap.
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of impairment across PM types.
    - source_id: P7-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of impairment prevalence.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Formal statistical analysis not possible due to limited overlap.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Visual observation of right parietal regions.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Specifies lesion volume as predictor in regression.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Lesion volume did not predict follow-up measures.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Specifies hierarchical regression steps.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Purpose of adding lesion volume to the model.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on stability of significance.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 10
      reason: Acute PM no longer predicts executive apathy after adjustment.
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 10
      reason: Acute PM no longer predicts anxiety after adjustment.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of hemisphere comparison groups.
    - source_id: P7-S2-C13
      disposition: represented
      result_indexes:
      - 12
      reason: No significant difference in PM Summary Score by hemisphere.
    - source_id: P8-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of acute PM impairment.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of effect size magnitude.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Links executive functioning to PM summary scores.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Links executive functioning to time-based PM.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Links TMT-A to event-based PM.
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for episodic memory.
    - source_id: P8-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for clinical/functional variables.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lack of association with functional outcomes.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Acute PM Summary Score predicts chronic PM Summary Score.
    - source_id: P9-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Acute PM prediction of anxiety/apathy becomes non-significant with lesion
        volume.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Acute PM did not predict other cognitive/clinical variables.
    - source_id: P9-S3-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Lesion volume did not uniquely predict long-term outcomes.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 10
      reason: Anxiety and apathy no longer predicted by acute PM when controlling
        for lesion volume.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: No significant difference in PM scores by hemisphere.
    unresolved_coverage:
    - source_id: P5-S3-C16
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C13
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P4-S1-C16
    - P4-S2-C2
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C10
    - P4-S2-C12
    - P5-S2-C11
    - P5-S2-C15
    - P5-S3-C10
    - P5-S3-C11
    - P5-S3-C12
    - P5-S4-C2
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C12
    - P7-S1-C13
    - P7-S2-C1
    - P7-S2-C4
    - P7-S2-C9
    - P8-S1-C6
    - P8-S1-C9
    - P8-S2-C7
    - P8-S2-C10
    - P9-S1-C1
    - P9-S1-C5
    - P9-S1-C7
    - P9-S1-C8
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    - P9-S2-C10
    - P9-S3-C3
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C11
    - P10-S2-C2
    - P10-S2-C4
    - P11-S1-C1
    - P11-S1-C3
    - P11-S2-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-6-3
    - TABLE-4-page-7-4
    - TABLE-5-page-8-5
    - TABLE-A1-page-11-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C9
      - P4-S1-C14
      - P4-S2-C3
      - P4-S2-C11
      recruited_sample:
      - P4-S1-C2
      - P4-S1-C12
      eligibility:
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C5
      imaging_provenance:
      - P3-S3-C2
      - P5-S1-C7
      imaging_timing:
      - P4-S1-C6
      outcome_timing:
      - P4-S2-C5
      - P7-S1-C9
      outcome_definition:
      - P4-S4-C4
      - P4-S4-C5
      validation: []
      analysis_restrictions:
      - P7-S2-C3
      dependent_variable_statement:
      - P5-S2-C3
      - P5-S2-C14
      - P5-S3-C4
      - P7-S2-C7
      limitations: []
      personal_factors:
      - P4-S1-C10
      - P4-S1-C15
      - P4-S1-C16
      - P4-S2-C8
      - P5-S1-C6
      - P11-S1-C1
      - P11-S1-C3
      tested_personal_effects:
      - P5-S3-C13
      - P5-S3-C14
      - P7-S1-C10
      - P7-S1-C11
      - P9-S2-C2
      - P9-S2-C10
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C14
      - P4-S1-C15
      - P4-S2-C7
      - P4-S2-C8
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S3-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P6-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P6-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: limitations
      source_ids:
      - P7-S1-C5
      - P9-S2-C6
      - P10-S1-C3
      - P11-S1-C5
      - P11-S1-C6
      - P11-S1-C9
      - P11-S1-C10
      - P11-S1-C11
      - P11-S1-C12
      - P11-S1-C13
      - P11-S2-C2
      - P11-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P5-S3-C3
      - P5-S3-C4
      - P7-S2-C5
      - P7-S2-C7
      - P7-S2-C8
      - P8-S3-C3
      - P8-S3-C4
      - P9-S3-C7
      - P10-S1-C1
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
      pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
      review_sha256: b974cc51e1f2063fdd0d5a180da4bbd7107bec00acf5a2da008fc40595f2a9cf
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
      - P1-S1-C13
      source_result: In acute to early sub-acute stroke patients, higher event-based
        prospective memory (PM) scores were associated with faster processing speed.
        This association was specific to event-based PM; overall and time-based PM
        performance were associated with executive functioning measures, not processing
        speed.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the correlational association
            between event-based PM scores and processing speed reported in the abstract
            (P1-S1-C13). The proposed core correctly identifies this as a distinct
            finding from the associations involving overall or time-based PM.
          source_ids:
          - P1-S1-C13
        direction:
          answer: fits
          reason: The source states 'higher event-based PM scores only correlated
            with faster processing speed' (P1-S1-C13). The proposed core claims 'Higher
            event-based PM scores correlated with faster processing speed,' which
            preserves the positive direction of the association.
          source_ids:
          - P1-S1-C13
        construct:
          answer: fits
          reason: The exposure is correctly identified as event-based PM scores measured
            via MIST-SF (P3-S2-C6, P4-S3-C10). The outcome is processing speed. The
            patient measurement is non-imaging (behavioral/cognitive test scores),
            as the association is between two behavioral measures, not imaging data.
            The distinction from time-based/overall PM is correctly captured in the
            qualifications.
          source_ids:
          - P1-S1-C13
          - P3-S2-C6
          - P4-S3-C10
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the association
            was specific to event-based PM, contrasting it with the executive functioning
            associations for overall/time-based PM. This accurately reflects the 'while...
            while...' structure in P1-S1-C13.
          source_ids:
          - P1-S1-C13
        missing_material_caveat:
          answer: fits
          reason: The core includes the limitation regarding self-selection bias (P11-S2-C7).
            No other material caveats that would change the interpretation of this
            specific correlation are omitted. The study's limitations regarding lesion
            overlap (P1-S1-C16) do not apply to this behavioral correlation.
          source_ids:
          - P11-S2-C7
      optional_pending:
      - Specific statistical values (r, p) for the event-based PM and processing speed
        correlation are not transcribed in the provided source window, though Table
        3 readings suggest TMT-A/B may be the processing speed measures used.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values (r, p) for the event-based PM and processing speed
      correlation are not transcribed in the provided source window, though Table
      3 readings suggest TMT-A/B may be the processing speed measures used.
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: event-based PM scores
      outcome:
        text: processing speed
      analysis_label: Event-based PM and Processing Speed
      relation: association
      evidence_ids:
      - P1-S1-C13
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
        pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
        source_review: _compare/relationships-2026-11-16/review-current/Gilbert2025
        source_status_sha256: 73bcb3c93826a5b4e386ee2ce3b048f237c324abbc4662161e01dc159950c8ea
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d46b0c690d5f539a16e89aaf9da3dc1a089ebe7f47db4c0ef1647c7e27bf1166
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C9
          page: 4
          text_layer_sha256: d46b0c690d5f539a16e89aaf9da3dc1a089ebe7f47db4c0ef1647c7e27bf1166
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "There were 58 stroke patients included in the \nsample (31\
          \ % female)."
        anchor_text: "There were 58 stroke patients included in the \nsample (31 %\
          \ female)."
        excluded_fragments: []
        image_sha256: 16f9fad48641b47babd9f8ac2ee22a35ce040aae20057df67c1a5bdd3595fc53
        transcription: '. There were 58 stroke patients included in the

          sample (31 % female)'
      P4-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0a2926c4d445dc8ad2fbf9ff0c054f64e7705c620ebd86d6c885d8a8c832b279
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C6
          page: 4
          text_layer_sha256: 0a2926c4d445dc8ad2fbf9ff0c054f64e7705c620ebd86d6c885d8a8c832b279
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants took part 2–62 days post-stroke (M = 19.03, SD
          =

          14.75).'
        anchor_text: 'Participants took part 2–62 days post-stroke (M = 19.03, SD
          =

          14.75).'
        excluded_fragments: []
        image_sha256: 51a592c44bdb86502022b91d596c25c15b6b0339cfe942d7f853f171e3ea28da
        transcription: '. Participants took part 2–62 days post-stroke (M = 19.03,
          SD =

          14.75)'
      P3-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d59d4244e03d6511de1087e4b8e6f9623244898d6e93fc4aa64d77da86d510d9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cf97febe64700ccb3ce3d44ce081692d47c73ad884101128bfe68c9b90507f28
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C6
          page: 3
          text_layer_sha256: cf97febe64700ccb3ce3d44ce081692d47c73ad884101128bfe68c9b90507f28
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "We administered a short form of the Memory for Intentions\
          \ \nScreening Test (MIST-SF; Raskin et al., 2016), modified for bedside\
          \ \nadministration, to acute and early sub-acute stroke patients (1 day–3\
          \ \nmonths post-stroke)."
        anchor_text: "We administered a short form of the Memory for Intentions \n\
          Screening Test (MIST-SF; Raskin et al., 2016), modified for bedside \nadministration,\
          \ to acute and early sub-acute stroke patients (1 day–3 \nmonths post-stroke)."
        excluded_fragments: []
        image_sha256: e39e2eecedb8a1af37deece95a09bc44e9a8b757c07f74d3e05ddbdeb555894e
        transcription: '.

          We administered a short form of the Memory for Intentions

          Screening Test (MIST-SF; Raskin et al., 2016), modified for bedside

          administration, to acute and early sub-acute stroke patients (1 day–3

          months post-stroke)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Better overall PM performance and time-based PM performance was \nassociated\
    \ with better performance on executive functioning measures, while higher event-based\
    \ PM scores only \ncorrelated with faster processing speed."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
