---
id: atrial_fibrillation
name: atrial fibrillation
kind: ingredient
findings:
- id: f1
  target: poststroke_cognitive_impairment
  target_kind: impairment
  claim: Patients with atrial fibrillation had poorer global cognition, attention,
    and executive function after adjustment for other risk factors, although this
    effect was fully mediated by stroke subtype (cardioembolic vs other subtypes).
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: 2 to 6 months after the index event
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - risk factor history was generally based on medical record review
  - some studies had only 1 test per domain
  - standardization relies on the representativeness of comparison groups
  - potential selection bias as patients with severe impairment may be less able to
    participate
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: presence of atrial fibrillation as noted in medical
    records. adjusted for sex, age, education, and other risk factors (hypertension,
    diabetes mellitus, smoking, past stroke); the association with global cognition
    became non-significant after further adjustment for stroke subtype. Additional
    metadata has not been transcribed; review the pending-field flags before approval.'
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
    - not_transcribed:sample.population
    - proposed_concept:poststroke_cognitive_impairment
  citation: '@Lo2019'
  source_passages:
  - section: Original source P10-S1-C3
    page: 10
    quote: 'Patients with AF had poorer global cognition, atten-

      tion, and executive function after adjustment (−0.26 SD; p =

      0.005 for global).'
    supports: claim
  - section: Original source P10-S1-C7
    page: 10
    quote: 'After further adjustment for stroke subtype, the results for

      all risk factors remained unchanged except for AF, the eﬀect

      of which on global cognition changed from −0.26 SD (p =

      0.005) to nearly zero (0.02; p = 0.90; results available from

      Dryad, appendix T17, doi.org/10.5061/dryad.m517990).'
    supports: claim
  - section: Original source P10-S1-C9
    page: 10
    quote: 'Results showed that conditions for full mediation

      were met, with the eﬀect of AF on cognition reduced

      to nearly zero (−0.03; p = 0.84; the steps and results of

      the mediation analysis are available from Dryad, appen-

      dix A4.1).'
    supports: claim
  - section: Original source P2-S1-C17
    page: 2
    quote: 'Results

      In a combined sample of 3,146 participants admitted to hospital for stroke (97%)
      or TIA (3%),

      44% were impaired in global cognition and 30% to 35% were impaired in individual
      domains 2

      to 6 months after the index event.'
    supports: sample
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      and main set of analyses, risk factors (hypertension, di-

      abetes mellitus, smoking, AF, smoking, past stroke) were

      included together in a single multivariable model.'
    supports: method
  - section: Original source P6-S1-C9
    page: 6
    quote: 'Therefore, for all patients in the combined sample, neuro-

      psychological assessments were performed 2 to 6 months

      after stroke (refer to the ﬂowchart in appendix F1 available

      from Dryad, doi.org/10.5061/dryad.m517990).'
    supports: method
  - section: Original source P14-S1-C4
    page: 14
    quote: 'Fifth, risk factor history was generally based on medical

      record review, and there could have been diﬀerences in how it

      was recorded across studies.'
    supports: limitation
  - section: Original source P14-S1-C6
    page: 14
    quote: 'Finally, 3 studies in our combined analyses

      did not attempt to exclude patients with known dementia, but

      all studies may have included some patients with preexisting

      dementia because no clinical assessments were performed

      until after the index stroke and patient recruitment, which

      could have led to overestimation of the frequency of cognitive

      impairment.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lo2019
  proposal_id: R005
  review_status_sha256: 19fb6ee339d2a66b735de610d4825422c7c0a75aa3062193dfed8d8341890fe1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
        A/passages.json: d698bbadcedc9cf576ca15b4fb23d02fa4eae1d573d2c1a1ae7f08e9f6fff258
        A/raw.json: 0ba25918f59621869995594346c4c6013ff53e5e79a7471b371feb151513a586
        A/source-units.json: aa1686a4ee0b3d1bf813393e37ef2081511a02f160d03f5a8a4d8e60c9c60432
        A/full-source-units.json: aa1686a4ee0b3d1bf813393e37ef2081511a02f160d03f5a8a4d8e60c9c60432
        A/meta.json: fd493287ae177d2cc80d2e39c10a04f0a150dd40ff7120bb44016840fe7cba70
        A/table-images/TABLE-4-page-9-1.png: 7c89b43326a94b42d0350cdb0c8307088b3789b8bb02d9b076ad1e98ca382013
        A/table-images/page-11.png: 14e183fedbaca13a8442ab68f35ee2c9892f242af74afcb008d5f4469df4ec6e
        A/table-images/TABLE-3-page-8-1.png: 7450c4124b64cdd05eaa2e1e62e625fc18680600ba49b53c0bd8a16350567e92
        A/table-images/page-7.png: ca3eb09d1b457cf4072e4913333c0b42e7ab1cfd0f72672eb5959f537fa53d84
        A/table-images/page-4.png: fcc21bfd8044e2cafbefbb1701419128db8fdb105bac8f35f7e88e4e253db937
        A/table-images/TABLE-1-page-4-1.png: 3c3b19b0f18299a1ea1f6b7e63dcce89a6deb1ba7317909b0834aedc9524d488
        A/table-images/page-9.png: e5289cdc79edffd32266a3626fa163039d2fbe74963b8b73f8d1afb1dc41d50b
        A/table-images/page-8.png: 8d6989423ca7af4401c2a85ba062b268eea1bd9d75539c64066694a954d4a764
        A/table-images/TABLE-5-page-11-1.png: ef1977ffd20c38eb53cd83c3ec2f4b98674068b0746f7b7b5aa7f388bbec1db7
        A/table-images/manifest.json: 60f6863ea27f7b1318085278414d08d085bd8ccf025ea09d28dde1e9def10295
        A/table-images/TABLE-2-page-7-1.png: 7e33161cd42c1bd194396d0e8d65cd2a05def2b4100988075d7bc26faabb7027
        A/clauses/window-11/raw.json: b09685d3c78601382bf71e9bd1290d5a0f18417d9969f2c7d9af68d1b7a89500
        A/clauses/window-11/prompt.txt: 974343efb51c7578289d9c3615098d5b0ca7cc677dc1d7297e15e129b5908130
        A/clauses/window-11/meta.json: d4029f63a50a6833c7dea42cd39821c60fe9314e5286b6b364f27656f79a3b9c
        A/clauses/window-10/raw.json: 473678c2770b638b99804cef0b634f7ed30fcd46d06cb1f36a6e880848422282
        A/clauses/window-10/prompt.txt: 433bb6a89c27cf5abf2c832f2b0593dd215e73dc100e4cc1239e5daba2434ff0
        A/clauses/window-10/meta.json: d32e1153d2412537b17898fcb650bcd9280e6bc65ce3b8a234b125f63d5ee844
        A/clauses/window-03/raw.json: 0ac6bf391ee66f980ebe382425899abfddfa1bad785710e9dece143be4951f79
        A/clauses/window-03/prompt.txt: a900279c6c6511dbcaaed4770d1581d1fd9dac672f27fa507c3074fa0cfffa41
        A/clauses/window-03/meta.json: 8c3e6874921cc66d188eb194754663126450d9e2100ee02b8cbffab110c653f0
        A/clauses/window-04/raw.json: 1978520d5862fc808bbdf5e773c21bb0ea904eeb8ef571487d739ceece7012d2
        A/clauses/window-04/prompt.txt: cfc1b9b112eb60881d91c51401f8fbc781ed891a32c18acf1bbf87388a46ac14
        A/clauses/window-04/meta.json: a01f290f0e6aac1130f9f3557a26bc0f36897cab2bac62e570f4a2c88d3e5d2e
        A/clauses/window-05/raw.json: f9f9380e99689a0130a6faf4c290a0dd008cf1b9d0efcb59e3e45c67b3671d44
        A/clauses/window-05/prompt.txt: 10b1ddb663204b5c3df49ba0a6e1322a270195c9a36ae9469099a0aa0109399a
        A/clauses/window-05/meta.json: 11daeb56b12f70550154eab2a24bb63a93dcb5aaebcafcab546299a0422e9086
        A/clauses/window-02/raw.json: e8fde0699baedb6c09eae2b0b4329a86c0bdbe2ba5124359e2a57db98f0d47dc
        A/clauses/window-02/prompt.txt: 3ea14f66a0882e2a4666baa14e20ff5b7c0ecd1a628b444db221fb596c59bfc2
        A/clauses/window-02/meta.json: 444f2e525bf663b47d79d9914f7ed4608284d6804363314eac430c1ea5655b6e
        A/clauses/window-09/raw.json: 0dbabd677b2ee813226d22265bced8244a283486eddb1b51afa7c8c16258be70
        A/clauses/window-09/prompt.txt: 5828a861c8454e4e58c8244eb2cb4f0716a7a119fb332ddcde3cc4ac56525dd1
        A/clauses/window-09/meta.json: 817a664ca8dbed7dc79599708df5251741c5d41824af2a0f2923c133429a0619
        A/clauses/window-07/raw.json: 33d21d367e652117e2c9d8c981c1653633809ff9479ee66962658fa81f489aa6
        A/clauses/window-07/prompt.txt: 92d644623a62751f95201b86d9b49c49db84fac5e8a23da81c6f9227c859d264
        A/clauses/window-07/meta.json: 67ec8cbe69b7732013794ca789ab530a1f85dd8fb4fbbb40719304b888245136
        A/clauses/window-01/raw.json: cf9519c7b080b062b5798e27083cc53c47d61569348111a2a74150884e0fc1de
        A/clauses/window-01/prompt.txt: 8119fbf926685a2cb42ec5f01852a8ee61766d72f0fef125daa0e4ec8c5db435
        A/clauses/window-01/meta.json: 772eff7d199754457cb275f9ab598886c9a827657f5696e2a2ad51463a1b778a
        A/clauses/window-06/raw.json: 456e97c8672b3ba00300805573c1725be0ea15321548376a8c02dc674c77f5ce
        A/clauses/window-06/prompt.txt: a811e2043dc00c4110708fdc633984eed372cd280ff45420cb90acdca0db18f3
        A/clauses/window-06/meta.json: 5258531b95f4cc46ce6c11bba89c5e3eb45831398fb671246432e01ffabb7299
        A/clauses/window-08/raw.json: 6f09565f28c933b67a24f3dda8974770c9cf2bf722f16432d12783d91cf9000e
        A/clauses/window-08/prompt.txt: e51199043f35f9ac4d5b7df846954c738fbf47cb4fc40f7186ccb5b8e69db781
        A/clauses/window-08/meta.json: ff09f6bdb4ed3a5e3cb76d47529ad7a79740fd5a34d367e6b8ecb875f8a35306
        A/tables/TABLE-5-page-11-5/raw.json: 8b06f284633f5f4b63ecc28359ce80ffb9120bfb5de514e6ffad340148f2ff00
        A/tables/TABLE-5-page-11-5/prompt.txt: b9d4f53d769302b245c200ad6e9b57d1cfda3bef60a2c8b400c51c8b9b5063f4
        A/tables/TABLE-5-page-11-5/meta.json: 74ba8b69ca910fdebd8f7bcfea9a64d9adb37f2c381d5e36a2a19095c330ba3b
        A/tables/TABLE-3-page-8-3/raw.json: f7bf521a50edea8cf28b423a7acd77876b5ff9cdef97e30143745a15a9357d6e
        A/tables/TABLE-3-page-8-3/prompt.txt: c333ea808ed9c4f90eea7cb041bd63eed148c8fb52e450236a51285967cfc661
        A/tables/TABLE-3-page-8-3/meta.json: 83f3e9cce0014052f1a141ca967463ac08d9212fa80be04c47dc7c91a17dae65
        A/tables/TABLE-2-page-7-2/raw.json: ec53d99bc79c4a7e5ca99b6c8ddcf78541f37f548a585c67de128a21f3ada73d
        A/tables/TABLE-2-page-7-2/prompt.txt: af07ec512cacee4ef470cd412275b5af5e37e869c525a700c9066a4939fdf08a
        A/tables/TABLE-2-page-7-2/meta.json: 17e3db51e5c7cce14a42a6766ec3441be946ff568bfa9d9d43d17d11ebf0c61d
        A/tables/TABLE-1-page-4-1/raw.json: 98a4d45dbcb815da5f212827a514a44e6f57b45f36695cd8d3d4451f5e674ee6
        A/tables/TABLE-1-page-4-1/prompt.txt: 1467f11e9f7850d82a5f9fb4dee7e550bc88e25d2415f3ad6d823b408bd6c9d8
        A/tables/TABLE-1-page-4-1/meta.json: cf222c15ddc551de7917b1b2708794a23e57e55d71ea9c7af855907b919ca701
        A/tables/TABLE-4-page-9-4/raw.json: e79a0b9ec2d6f3235acc27747331775470a3f7af7448b02f47f781e46586e795
        A/tables/TABLE-4-page-9-4/prompt.txt: a57e85a9a3c9a37bb2590be335d7c8b0870f2fd1aefaef9f4a3a87fe113b21bd
        A/tables/TABLE-4-page-9-4/meta.json: a301450c36ffc14d2c137d26f8dad33b6a08c7c302082c6ed032110cb8f54f3a
        B/passages.json: d698bbadcedc9cf576ca15b4fb23d02fa4eae1d573d2c1a1ae7f08e9f6fff258
        B/raw.json: 987f36da4ab5dc263c011fe2818770fc191af501686485874d93ef13a0132c2e
        B/source-units.json: aa1686a4ee0b3d1bf813393e37ef2081511a02f160d03f5a8a4d8e60c9c60432
        B/full-source-units.json: aa1686a4ee0b3d1bf813393e37ef2081511a02f160d03f5a8a4d8e60c9c60432
        B/meta.json: ca8b47efb58910ca40c41a7a8744a88e35ad2157a5247a3684b96c476919d64d
        B/table-images/TABLE-4-page-9-1.png: 7c89b43326a94b42d0350cdb0c8307088b3789b8bb02d9b076ad1e98ca382013
        B/table-images/page-11.png: 14e183fedbaca13a8442ab68f35ee2c9892f242af74afcb008d5f4469df4ec6e
        B/table-images/TABLE-3-page-8-1.png: 7450c4124b64cdd05eaa2e1e62e625fc18680600ba49b53c0bd8a16350567e92
        B/table-images/page-7.png: ca3eb09d1b457cf4072e4913333c0b42e7ab1cfd0f72672eb5959f537fa53d84
        B/table-images/page-4.png: fcc21bfd8044e2cafbefbb1701419128db8fdb105bac8f35f7e88e4e253db937
        B/table-images/TABLE-1-page-4-1.png: 3c3b19b0f18299a1ea1f6b7e63dcce89a6deb1ba7317909b0834aedc9524d488
        B/table-images/page-9.png: e5289cdc79edffd32266a3626fa163039d2fbe74963b8b73f8d1afb1dc41d50b
        B/table-images/page-8.png: 8d6989423ca7af4401c2a85ba062b268eea1bd9d75539c64066694a954d4a764
        B/table-images/TABLE-5-page-11-1.png: ef1977ffd20c38eb53cd83c3ec2f4b98674068b0746f7b7b5aa7f388bbec1db7
        B/table-images/manifest.json: 7304439a0126cb80123f3684f8ed238efeef6fee2908bf2bef387932a150f220
        B/table-images/TABLE-2-page-7-1.png: 7e33161cd42c1bd194396d0e8d65cd2a05def2b4100988075d7bc26faabb7027
        B/clauses/window-11/raw.json: 6d0b7f1ec48c8e58617808ee6657490ce2787462403f20b6f50fd0c98750d0f8
        B/clauses/window-11/prompt.txt: 974343efb51c7578289d9c3615098d5b0ca7cc677dc1d7297e15e129b5908130
        B/clauses/window-11/meta.json: 94c336125c383187745a176b975278573cd532f17c05c5663ac71fd90165649f
        B/clauses/window-10/raw.json: e5d1b5fac91614dc0d1e57f4360218e2fe39c5fa8019230a2e8d2f01b4ce1b69
        B/clauses/window-10/prompt.txt: 433bb6a89c27cf5abf2c832f2b0593dd215e73dc100e4cc1239e5daba2434ff0
        B/clauses/window-10/meta.json: f36bcc544102acafa5c07b8ad50a5928888f5a70a30a2e43fb9d1b8f88692b32
        B/clauses/window-03/raw.json: c129afb89f83f10f9636106ddbf5852852833e49f8149267cb5282d57cc5a3ee
        B/clauses/window-03/prompt.txt: a900279c6c6511dbcaaed4770d1581d1fd9dac672f27fa507c3074fa0cfffa41
        B/clauses/window-03/meta.json: 2c9ab490fa03dfc9ecf260781740b6729cfa133ef0659d89fe6c9008bae3ecf3
        B/clauses/window-04/raw.json: 0ba6be69ab024bdb92609c66a7a803c0423d3bf0305b3e0e7310bf65c2f35578
        B/clauses/window-04/prompt.txt: cfc1b9b112eb60881d91c51401f8fbc781ed891a32c18acf1bbf87388a46ac14
        B/clauses/window-04/meta.json: e802ea7cc7c895f4b95780c1022468bbecfe45f6a1eb8dece30b5aaf8b174010
        B/clauses/window-05/raw.json: e8c2c8f1b4074cd26f74d3174751b41f8ca5638fc5d4cdbd4a37fcea0eb990e2
        B/clauses/window-05/prompt.txt: 10b1ddb663204b5c3df49ba0a6e1322a270195c9a36ae9469099a0aa0109399a
        B/clauses/window-05/meta.json: 96b385bd529eec263bfe7dbf6bc1f4e61ff8e8f38e887dfab022f39ff1620cfd
        B/clauses/window-02/raw.json: 1121e44184744650e855d0849f3d384bb96f6ac6f1c17923992e6d54fa23f4e9
        B/clauses/window-02/prompt.txt: 3ea14f66a0882e2a4666baa14e20ff5b7c0ecd1a628b444db221fb596c59bfc2
        B/clauses/window-02/meta.json: d370bf13950dd4e79aac1aabd277340e58973b16cd40e75eafe8f5370ac83834
        B/clauses/window-09/raw.json: 0dbabd677b2ee813226d22265bced8244a283486eddb1b51afa7c8c16258be70
        B/clauses/window-09/prompt.txt: 5828a861c8454e4e58c8244eb2cb4f0716a7a119fb332ddcde3cc4ac56525dd1
        B/clauses/window-09/meta.json: e150261b3b973b30979470c1dc659928c3b46331fa79949d1784562f4c853dfb
        B/clauses/window-07/raw.json: 499736bfed5f349177c855cba65684964b6d506cdc6bee98cad11ef74a732afe
        B/clauses/window-07/prompt.txt: 92d644623a62751f95201b86d9b49c49db84fac5e8a23da81c6f9227c859d264
        B/clauses/window-07/meta.json: a74b035fc70dc15fb8b2535415456d56317856d1dd82236c047d004d00dd5c0a
        B/clauses/window-01/raw.json: f8efd820cc22ac0248dea898fc0dbc62fecd83c32c874def5af2b5263f888909
        B/clauses/window-01/prompt.txt: 8119fbf926685a2cb42ec5f01852a8ee61766d72f0fef125daa0e4ec8c5db435
        B/clauses/window-01/meta.json: 4703bb6d558573a656f673d2e987981592977f7f3dcb0a9d87e9da98f1ca5813
        B/clauses/window-06/raw.json: f3f2d7525a4dc128e04f80d1dc64e8d19ccbe787a1bb8ee4f5fa645a66bdf930
        B/clauses/window-06/prompt.txt: a811e2043dc00c4110708fdc633984eed372cd280ff45420cb90acdca0db18f3
        B/clauses/window-06/meta.json: 70d6fc4febbddc79d08c4ddd36a4c8d9eea2a55f6e8b69ac7ec9ee9a13ca0453
        B/clauses/window-08/raw.json: 3daf81a8257bac3427cab27eaa84faef79c1bff308e80e6a472f03f38bc05828
        B/clauses/window-08/prompt.txt: e51199043f35f9ac4d5b7df846954c738fbf47cb4fc40f7186ccb5b8e69db781
        B/clauses/window-08/meta.json: e784f7d49209b47a624156a8f7086611c2c40c3e428be585277da236fa08b1bf
        B/tables/TABLE-5-page-11-5/raw.json: 4620ce91863cd062b83ac945c21bd0e1b3134e87331e77855b0bc9613acdb18e
        B/tables/TABLE-5-page-11-5/prompt.txt: b9d4f53d769302b245c200ad6e9b57d1cfda3bef60a2c8b400c51c8b9b5063f4
        B/tables/TABLE-5-page-11-5/meta.json: 36a8defbce96843d345a71f678ee7edb509c26a17aab98d82572e852c379d580
        B/tables/TABLE-3-page-8-3/raw.json: 7d20a955d872690a2b423023965d0295e1e12f92875a5cd1278026c7494e7eaf
        B/tables/TABLE-3-page-8-3/prompt.txt: c333ea808ed9c4f90eea7cb041bd63eed148c8fb52e450236a51285967cfc661
        B/tables/TABLE-3-page-8-3/meta.json: bb8ebab1aad4698abefe63fda8451402860720ef902b8a49c53c88a8f6cb7395
        B/tables/TABLE-2-page-7-2/raw.json: 3b532afb8e9dba483c5d48725d3b43806d5756e6818eb6edbc821e74b83eb492
        B/tables/TABLE-2-page-7-2/prompt.txt: af07ec512cacee4ef470cd412275b5af5e37e869c525a700c9066a4939fdf08a
        B/tables/TABLE-2-page-7-2/meta.json: db41b98f553fc78e9f05d7caf96d26cf9ffb362e06ebccce063388745e7f940a
        B/tables/TABLE-1-page-4-1/raw.json: 4d8b0f620c193a42d53ca69df3cea8d71c108a4e890ee967bb246a3184a2b3c2
        B/tables/TABLE-1-page-4-1/prompt.txt: 1467f11e9f7850d82a5f9fb4dee7e550bc88e25d2415f3ad6d823b408bd6c9d8
        B/tables/TABLE-1-page-4-1/meta.json: d4a7181fdb499af8a06e3bf396658fd3761dc8f4f90045f47675d7cbac475405
        B/tables/TABLE-4-page-9-4/raw.json: a879104d7bbd1e4fbc2a1076355c4cf8719b380eabdbd73b488732a1648a2e2f
        B/tables/TABLE-4-page-9-4/prompt.txt: a57e85a9a3c9a37bb2590be335d7c8b0870f2fd1aefaef9f4a3a87fe113b21bd
        B/tables/TABLE-4-page-9-4/meta.json: 0364e09fb5fe1b4a49ee6411fa8b1e6e97b06a3e19759f49c2a7df7bc0b39646
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
      pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
      source_review: _compare/relationships-2026-11-16/review-current/Lo2019
      source_status_sha256: a5d717bf996133335071616548f2af9e791e66a79e892ab223ad2c289b50fdbb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: atrial fibrillation
    outcome:
      text: global cognition, attention, and executive function
    analysis_label: Multivariable risk factor analysis
    relation: association
    evidence_ids:
    - P2-S1-C18
    - P10-S1-C3
    - P11-S1-C1
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
      pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
      source_review: _compare/relationships-2026-11-16/review-current/Lo2019
      source_status_sha256: a5d717bf996133335071616548f2af9e791e66a79e892ab223ad2c289b50fdbb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S1-C17
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C10
      - 'window 9: invalid/duplicate disposition P10-S2-C10'
      - Result passage disposed without unit P13-S2-C7
      - Unresolved source passage P13-S2-C7
      unattached_null_or_qualifier_ids:
      - P10-S1-C1
      - P10-S1-C10
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 201
      unselected_timing_passages:
      - P4-S1-C9
      - P6-S2-C4
      - P7-S2-C4
      - P9-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P9-S1-C6
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
        source_id: P10-S1-C4
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
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P5-S3-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P6-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P6-S1-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P13-S1-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_ids:
        - P2-S1-C18
        - P9-S1-C6
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S1-C11
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C7
        - P13-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P2-S1-C18
        - P5-S2-C7
        - P5-S2-C9
        - P5-S3-C7
        - P5-S3-C10
        - P6-S1-C1
        - P6-S1-C2
        - P6-S1-C5
        - P6-S1-C7
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C5
        - P10-S1-C7
        - P11-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_timing
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      - TABLE-3-page-8-3
      - TABLE-4-page-9-4
      - TABLE-5-page-11-5
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S2
        - P9-S1
        - P12-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
      source_review: _compare/relationships-2026-11-16/review-current/Lo2019
      source_status_sha256: a5d717bf996133335071616548f2af9e791e66a79e892ab223ad2c289b50fdbb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P2-S1-C17
      disposition: represented
      result_indexes:
      - 0
      reason: Reports prevalence of global and domain impairment in combined sample.
    - source_id: P2-S1-C18
      disposition: represented
      result_indexes:
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Reports associations of diabetes, past stroke, hypertension, AF, and
        smoking with cognition.
    - source_id: P2-S2-C3
      disposition: represented
      result_indexes:
      - 14
      reason: States no significant differences in domain impairment among ethnoracial
        groups.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sample characteristics (stroke types).
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports mean z scores and impairment percentages for combined sample.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 1 for domain impairment percentages.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes impairment proportions in excluded studies.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes effect of using a more stringent impairment criterion.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes impairment proportions when excluding patients without preexisting
        dementia exclusion.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports proportions of dementia and MCI diagnoses.
    - source_id: P6-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References appendixes for dementia criteria.
    - source_id: P6-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports proportions of patients impaired in multiple domains.
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares clinical diagnosis to domain impairment proportions.
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Reports higher impairment in left hemisphere stroke for global, memory,
        language, and executive function.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Reports higher impairment in right hemisphere stroke for perceptual
        motor function.
    - source_id: P6-S3-C6
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports impairment proportions by stroke subtype (small vessel and cardioembolic).
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes undetermined stroke types in CogFAST-Nigeria.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes unknown stroke mechanisms in PROSPER.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports total number of patients with unknown stroke type.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 23
      reason: Reports no significant difference between ischemic and hemorrhagic strokes
        for global cognition.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports proportions of global impairment by ethnoracial group.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions pairwise differences between ethnoracial groups in certain
        domains.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 15
      reason: States mixed models showed no significant relationship between ethnoracial
        groups and impairment.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports strong association of diabetes with global cognition and all
        domains.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports association of history of stroke with global cognition and most
        domains.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Reports history of stroke associated with impairment in all domains
        except memory.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports hypertension associated with global cognition, language, and
        executive function.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports AF associated with global cognition, attention, and executive
        function.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports smoking associated with perceptual motor impairment but not
        global cognition.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Reports CHF associated with cognition independently but not after adjustment.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no significant association between angina or MI and cognition.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 21
      reason: Reports AF effect on global cognition changed to nearly zero after stroke
        subtype adjustment.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 21
      reason: Reports full mediation of AF effect by cardioembolic stroke.
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 16
      - 17
      - 18
      reason: Reports interactions of diabetes, past stroke, and smoking with Korean
        ethnicity.
    - source_id: P10-S2-C1
      disposition: represented
      result_indexes:
      - 16
      - 17
      - 18
      reason: Provides effect size for diabetes interaction in Koreans.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Reports interactions of smoking and AF with Chinese ethnicity.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 22
      reason: Reports no significant interaction terms between risk factors and stroke
        status.
    - source_id: P13-S1-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Restates no significant differences in domain impairment among ethnoracial
        groups.
    - source_id: P13-S2-C10
      disposition: represented
      result_indexes:
      - 22
      reason: Restates that risk factor associations were not different in participants
        without stroke.
    - source_id: P13-S3-C1
      disposition: represented
      result_indexes:
      - 22
      reason: Restates that risk factor associations were not different in participants
        without stroke.
    - source_id: P10-S3-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Restates small vessel disease etiology associated with less impairment.
    - source_id: P10-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Restates greater impairment in left hemisphere stroke for language domain.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 7
      - 9
      reason: Table 5 provides effect sizes and p-values for all risk factors across
        domains.
    unresolved_coverage:
    - source_id: P13-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C10
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
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
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
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C8
    - P6-S2-C9
    - P6-S2-C10
    - P6-S2-C11
    - P6-S3-C1
    - P6-S3-C2
    - P6-S3-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    - P9-S1-C3
    - P9-S1-C4
    - P10-S1-C10
    - P10-S2-C3
    - P10-S2-C5
    - P10-S2-C6
    - P10-S2-C8
    - P10-S2-C11
    - P10-S3-C2
    - P12-S1-C2
    - P13-S1-C4
    - P13-S1-C5
    - P13-S1-C7
    - P13-S1-C8
    - P13-S2-C1
    - P13-S2-C3
    - P13-S2-C4
    - P13-S2-C6
    - P13-S2-C7
    - P13-S2-C8
    - P13-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    - TABLE-3-page-8-3
    - TABLE-4-page-9-4
    - TABLE-5-page-11-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P6-S1-C8
      - P6-S1-C9
      recruited_sample:
      - P4-S1-C3
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C10
      - P5-S1-C3
      eligibility:
      - P4-S1-C3
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P6-S1-C10
      imaging_provenance:
      - P5-S1-C10
      imaging_timing: []
      outcome_timing:
      - P2-S1-C15
      - P3-S2-C1
      - P4-S1-C3
      - P6-S1-C9
      outcome_definition:
      - P2-S1-C16
      - P5-S3-C4
      - P5-S3-C5
      - P6-S2-C6
      validation: []
      analysis_restrictions:
      - P6-S1-C3
      - P6-S1-C8
      - P6-S1-C10
      dependent_variable_statement:
      - P5-S3-C10
      - P6-S1-C11
      limitations:
      - P13-S3-C6
      - P13-S3-C7
      - P13-S3-C8
      - P14-S1-C3
      - P14-S1-C4
      - P14-S1-C5
      - P14-S1-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P6-S1-C3
      descriptive_personal_factors:
      - P5-S1-C6
      - P5-S1-C7
      - P7-S1-C1
      - P8-S1-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P9-S1-C6
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
      source_id: P10-S1-C4
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
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P5-S3-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P6-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P6-S1-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P13-S1-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_ids:
      - P2-S1-C18
      - P9-S1-C6
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S1-C11
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C7
      - P13-S2-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P2-S1-C18
      - P5-S2-C7
      - P5-S2-C9
      - P5-S3-C7
      - P5-S3-C10
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C5
      - P6-S1-C7
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C5
      - P10-S1-C7
      - P11-S1-C2
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
      pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
      review_sha256: 19fb6ee339d2a66b735de610d4825422c7c0a75aa3062193dfed8d8341890fe1
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
      - P10-S1-C3
      - P2-S1-C18
      source_result: Atrial fibrillation was associated with poorer global cognition,
        attention, and executive function after adjustment for other risk factors
        (hypertension, diabetes, smoking, past stroke). However, after further adjustment
        for stroke subtype, the association with global cognition became non-significant
        (effect size changed from -0.26 SD to 0.02 SD), and full mediation by stroke
        subtype was observed.
      result_status: lost_after_adjustment
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the multivariable risk factor
            analysis described in the source, specifically the step where AF is adjusted
            for other risk factors and then stroke subtype. The source explicitly
            details this progression in P10-S1-C3 and P10-S1-C7.
          source_ids:
          - P10-S1-C3
          - P10-S1-C7
          - P6-S1-C1
        direction:
          answer: fits
          reason: The draft correctly captures the direction of the association (poorer
            cognition) and the change in significance (loss of significance/mediation)
            after adding stroke subtype. It does not incorrectly claim a null effect
            at the initial multivariable stage.
          source_ids:
          - P10-S1-C3
          - P10-S1-C7
          - P10-S1-C9
        construct:
          answer: fits
          reason: The exposure (AF) and outcome (cognitive domains) are correctly
            identified. The patient measurement is non-imaging (neuropsychological
            tests), not diffusion or lesion overlap, as the study uses standardized
            test scores. The draft correctly identifies the mediation by stroke subtype.
          source_ids:
          - P10-S1-C3
          - P10-S1-C8
          - P5-S3-C2
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the effect is
            mediated by stroke subtype, which is a material caveat found in P10-S1-C7
            and P10-S1-C9. It also correctly notes the adjustment for other risk factors.
          source_ids:
          - P10-S1-C7
          - P10-S1-C9
          - P6-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes the mediation caveat. While there are other limitations
            (e.g., selection bias, single test per domain), the most material caveat
            regarding the specific AF finding is the mediation by stroke subtype,
            which is included. The draft is a qualitative summary and does not need
            to list every minor limitation if the core interpretation is preserved.
          source_ids:
          - P10-S1-C7
          - P14-S1-C4
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    - field: sample.n
      original: 3146
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.population
      original: patients admitted to hospital for stroke (97%) or TIA (3%) from 13
        international cohorts
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 13'
    analysis_identity:
      id: R005
      exposure:
        text: atrial fibrillation
      outcome:
        text: global cognition, attention, and executive function
      analysis_label: Multivariable risk factor analysis
      relation: association
      evidence_ids:
      - P2-S1-C18
      - P10-S1-C3
      - P11-S1-C1
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
        pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
        source_review: _compare/relationships-2026-11-16/review-current/Lo2019
        source_status_sha256: a5d717bf996133335071616548f2af9e791e66a79e892ab223ad2c289b50fdbb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 67d3456f3c1b3061897712f9c14093c9a15c7b65df1e430fe1fe447e758626a4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c583a21d70abed79bb9c47ad2975a01e781435dbf82471d5ce9bd074b0afdc17
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C9
          page: 6
          text_layer_sha256: c583a21d70abed79bb9c47ad2975a01e781435dbf82471d5ce9bd074b0afdc17
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Therefore, for all patients in the combined sample, neuro-

          psychological assessments were performed 2 to 6 months

          after stroke (refer to the ﬂowchart in appendix F1 available

          from Dryad, doi.org/10.5061/dryad.m517990).'
        anchor_text: 'Therefore, for all patients in the combined sample, neuro-

          psychological assessments were performed 2 to 6 months

          after stroke (refer to the ﬂowchart in appendix F1 available

          from Dryad, doi.org/10.5061/dryad.m517990).'
        excluded_fragments: []
        image_sha256: dcda41989450c20ce56c466b5a7eb6cdbedf68446c19572ea256bfe8be2b88fc
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'Patients with AF had poorer global cognition, atten-

    tion, and executive function after adjustment (−0.26 SD; p =

    0.005 for global).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
