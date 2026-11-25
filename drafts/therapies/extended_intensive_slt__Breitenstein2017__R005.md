---
id: extended_intensive_slt
name: extended intensive speech and language therapy
kind: therapy
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: verbal_communication_effectiveness
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Amsterdam-Nijmegen Everyday Language Test
      subtest: A-scale
    metric: Effectiveness of verbal communication in ten everyday situations
    definition_source:
      citation: '@Breitenstein2017'
      page: 4
      quote: "Outcomes\nThe centrally assessed primary outcome measure was \neffectiveness of verbal communication\
        \ in ten everyday \nlife situations, assessed using the two parallel versions \nof the Amsterdam-Nijmegen\
        \ Everyday Language Test \n(ANELT) A-scale.23 We randomly selected which of the \ntwo ANELT versions\
        \ was to be given to a patient at their \nfirst assessment; versions were then alternated across\
        \ \nsubsequent assessments in an individual patient (eg, if a \npatient had four assessments and\
        \ started with version I, \nthe sequence would have been: I, II, I, II)."
      basis: Published source passage
    note: Measurement metadata identified from source evidence; finding remains unapproved.
  target: verbal_communication_effectiveness
  target_kind: impairment
  claim: In a subgroup of patients receiving 5 weeks or more of intensive speech and
    language therapy, the mean change in verbal communication effectiveness from baseline
    was larger after the extended therapy period (median 6 weeks) than after the initial
    3 weeks of therapy.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: 34
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: assessment performed within 3 working days of completion of the
      intensive treatment period
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - subgroup analysis
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: intensive speech and language therapy (≥10 h per week)
    provided for 5 weeks or more. subgroup analysis of patients from both the intervention
    and control groups; the extended therapy group did not differ from the 3-week
    therapy group in age, sex, education, initial stroke severity, aphasia severity,
    or aphasia syndrome distribution. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - not_transcribed:sample.population
    - proposed_concept:verbal_communication_effectiveness
  therapy:
    id: intensive_slt
    name: intensive speech and language therapy
  citation: '@Breitenstein2017'
  source_passages:
  - section: Original source P7-S1-C4
    page: 7
    quote: "Subgroup analysis of 34 patients (19 in the intervention \ngroup and 15\
      \ in the control group) who received 5 weeks \nor more of intensive speech and\
      \ language therapy \nshowed that the mean change in ANELT A-scale score \nfrom\
      \ baseline was roughly 1 point larger (4·23 points \n[SD 4·28], 95% CI 2·74–5·73)\
      \ after a median of 6 weeks \n(IQR 5–7) of intensive therapy than after the\
      \ initial \n3 weeks of intensive therapy (3·32 points [5·64], \n1·35–5·29; appendix\
      \ p 12)."
    supports: claim
  - section: Original source P7-S1-C5
    page: 7
    quote: "Patients who had intensive \nspeech and language therapy limited to 3\
      \ weeks versus \nthose who had at least 5 weeks of therapy did not differ \n\
      with respect to age, sex, years of education, initial stroke \nseverity, \n\
      aphasia \nseverity, \nor \naphasia \nsyndrome \ndistribution (data not shown;\
      \ all p>0·13)."
    supports: confounders
  - section: Original source P4-S2-C8
    page: 4
    quote: "We \nalso did additional outcome assessments in the subgroup \nof patients\
      \ from both groups who had 5 weeks or more of \nintensive speech and language\
      \ therapy; assessments \nwere done within 3 working days of completion of the\
      \ \nintensive treatment period."
    supports: method
  - section: Original source P3-S1-C5
    page: 3
    quote: "Participants\nInclusion criteria, which aimed to replicate realistic \n\
      routine health-care conditions, were chronic aphasia \n(confirmed using the\
      \ Aachen Aphasia Test [AAT])22 lasting \n6 months or more after an ischaemic\
      \ or haemorrhagic \nstroke, age 18–70 years, German as first language, basic\
      \ \ncomprehension abilities and at least rudimentary attempts \nto verbally\
      \ communicate (communication score >0 on the \nAAT spontaneous speech scale),\
      \ and the ability to follow \nsimple instructions (at least one correct response\
      \ on the \nfirst ten items of the AAT Token Test)."
    supports: sample
  - section: Original source P9-S2-C4
    page: 9
    quote: "Therapy \nduration might also be an important determinant of \ntreatment\
      \ effects: the subsample of 34 patients in our \nstudy who had 5 weeks or more\
      \ of intensive speech and \nlanguage therapy had mean increases of more than\
      \ \n4 points from baseline to after therapy."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Breitenstein2017
  proposal_id: R005
  review_status_sha256: 39bdf7f698e2d17411ff9ddd64bdace028506d60374fcd704603e6cfa833a930
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
        A/passages.json: 3110323fa620ba4459fa81ba8a37965362f9952b131c30df41c8d797ae317261
        A/raw.json: cb8dc08c4e747081bf8d4164a930cb6f7d467539327df5d4d258628e44aa3295
        A/source-units.json: 871d2c5884606e4aa0e4d27394ad65a5c5868dbe1d6cf123a2e47722e98538e2
        A/full-source-units.json: db5befb6a765227d7f339d0b07b6f240d86922a45659e48fe1bbda277f9ae893
        A/meta.json: e116609367ddb6d37a76758cebcf8289b8e425ea87e45998f7abd446d35b6d4a
        A/table-images/TABLE-1-page-7-1.png: a6cc5b88f7c16d12807b4ee64c4196fcc730a8e7dc5c8576d69120bdd2dbd3f5
        A/table-images/TABLE-2-page-8-1.png: fbb953a5d7424f884b6c8cd0a71d5e92318826e8f32597162e8e72799791cd18
        A/table-images/page-7.png: 2dd2f25168f55763cbab8076a4283d1b53a4f98696417ab4d407b2818ee56c04
        A/table-images/page-8.png: 6d4f2eb41186f44aedd3e5de58e6a7142c6659e0e0d83d14d46c20a5a785d61a
        A/table-images/manifest.json: 18056f51ecf25ba660de1083fa9df1ca2c09c9ad7eee53babbb9d0561420ba9a
        A/clauses/window-03/raw.json: 3e99ae57fc2d6e4dec5051354579e36bc77ebe3ecf543b4f65a881995318f95b
        A/clauses/window-03/prompt.txt: f6eac5f167327fded1228db60b3d331f7823636b8ea04af75894bb699d788a16
        A/clauses/window-03/meta.json: 59b35d2702f3f08cebcc4f93e4ef7d03454420e37baa163e9c2b2363cd1633f9
        A/clauses/window-04/raw.json: eda32be90b2ece5328a6acca48cd13417d60350d5b6579d586360d85c137dd31
        A/clauses/window-04/prompt.txt: c16b452a60b376061079fd8c2c550f263ddb5d2d5f31254d472beb4eb38369a9
        A/clauses/window-04/meta.json: a5f8617899e0b666e563b25e48f90573e7b56dcc644546c3cc9de6941e7d0788
        A/clauses/window-05/raw.json: b2b826444d883e61dc6966fc02958a7204aab517994e70499da5a0db8337d755
        A/clauses/window-05/prompt.txt: 30acb4d84d1fa9b1e1449d060b3293d47e6c156873b206fce96fa201a86a3330
        A/clauses/window-05/meta.json: cd6f6932fe97b94eef42b4d2679b4f4725a6e5790e152b801c818c5d2e54763e
        A/clauses/window-02/raw.json: 16826c6411b1f6cd26032f730f7a555ae23812b6b5d7d35af9b4f1f439dd8f5e
        A/clauses/window-02/prompt.txt: eced275939f552670d41c7270be3527b428ebefe89dacc6cbc75854cfdaa37c9
        A/clauses/window-02/meta.json: 3299033dad946101eb2a5c15c439c56809a6cd51155ea56dd22ec2b018ae694e
        A/clauses/window-07/raw.json: 51aa79321762ebfd2ebfeaada884fee8110b25767e8c66fb8ed175bb4964d764
        A/clauses/window-07/prompt.txt: dbac2c12a09bb0960d3741c567acffe0f6ca0a77565ec68587ba0462a4ebd898
        A/clauses/window-07/meta.json: e288c211a2d58bcbf753da502ef27777c58dffcf7677bcf0198e6540bfda0b37
        A/clauses/window-01/raw.json: 640cda5eb6e16a8b16f5167aac22693659fbc158f93438deaeb48606184666e9
        A/clauses/window-01/prompt.txt: 9224c2ad57a71dd588749aac080782c6c58f6a47bd6babe6fdd33f85a6fc6f4a
        A/clauses/window-01/meta.json: 21b6350baa56cfa6467f9d044fbd05abbd36de4e5ebe624343c17db05c3fd239
        A/clauses/window-06/raw.json: abed49038152310cb9543f8c55f8ef983ebf9e7b1fd08c7c046d3635e203f7c9
        A/clauses/window-06/prompt.txt: 59bfa6e5651b0abcdb04b940886d24c9ca530428eaf19d3092a3df2be7942abc
        A/clauses/window-06/meta.json: ce09bb06cc484ab71f05cac1b848c31403ab9d5a8a8cb3fa0fe924596b7d77b0
        A/clauses/window-08/raw.json: d720614c6c6aae7521316689ace71c8ae8a73e4408cd4180149ad98c696e4ef8
        A/clauses/window-08/prompt.txt: 50e93b4c2ddd5a48fc87fada8818c5ebeb4a9f6ac7a7878df2d4f15f7797760a
        A/clauses/window-08/meta.json: 3aae005449abe70721a9879f37000a8c6cc7a14721a137bb3b7e253942915599
        A/tables/TABLE-2-page-8-2/raw.json: d5d93d3bd1f6c339cf914de05b5f27f955ee059fda45c3bc1ade5dc401a191d9
        A/tables/TABLE-2-page-8-2/prompt.txt: c4b2da992696ffefb27b134dd1e69f81792a733704421308cabf89ffbdc86ea8
        A/tables/TABLE-2-page-8-2/meta.json: 6ce52b14585b43b09dbe6c7ff1f96512b2a246f60308749cc7057b06e5a88660
        A/tables/TABLE-1-page-7-1/raw.json: a00f1ee5b9b0d6183c97f56b0cc75c32bef1c181fe17fa167fdf576593b14f52
        A/tables/TABLE-1-page-7-1/prompt.txt: ba038ad695521c89544e3420843381a15b1564e362ba86aa3719ad62b163ab6e
        A/tables/TABLE-1-page-7-1/meta.json: fc6ce6c31c6067736ae0518cf6026afd175538ed9806dbc44c83a829b021f163
        B/passages.json: 3110323fa620ba4459fa81ba8a37965362f9952b131c30df41c8d797ae317261
        B/raw.json: 62f2aa069a5b5b62d094374513932fa94d8bced2eda67a5eda3b77572cc9d526
        B/source-units.json: 871d2c5884606e4aa0e4d27394ad65a5c5868dbe1d6cf123a2e47722e98538e2
        B/full-source-units.json: db5befb6a765227d7f339d0b07b6f240d86922a45659e48fe1bbda277f9ae893
        B/meta.json: e3733bcde329fc000c0919441fc68af9c80093e2df91f79d73df7c57adfec962
        B/table-images/TABLE-1-page-7-1.png: a6cc5b88f7c16d12807b4ee64c4196fcc730a8e7dc5c8576d69120bdd2dbd3f5
        B/table-images/TABLE-2-page-8-1.png: fbb953a5d7424f884b6c8cd0a71d5e92318826e8f32597162e8e72799791cd18
        B/table-images/page-7.png: 2dd2f25168f55763cbab8076a4283d1b53a4f98696417ab4d407b2818ee56c04
        B/table-images/page-8.png: 6d4f2eb41186f44aedd3e5de58e6a7142c6659e0e0d83d14d46c20a5a785d61a
        B/table-images/manifest.json: 8ec80406c37396387ff967368118f2d74dde8ba8f4cd956625ce25e27c578ca4
        B/clauses/window-03/raw.json: b4a0dad4ba75aad15d68899f739530ba9b43d61298ed00679315630566fb0080
        B/clauses/window-03/prompt.txt: f6eac5f167327fded1228db60b3d331f7823636b8ea04af75894bb699d788a16
        B/clauses/window-03/meta.json: 527cf8ab08e9a700b1df812f6b1f2c501ed9f2607ea0ad3216c0b463dbf488a9
        B/clauses/window-04/raw.json: e12d5ce067506631eca52cff9bb7495e94b90d92b2efec61db766874d3849a87
        B/clauses/window-04/prompt.txt: c16b452a60b376061079fd8c2c550f263ddb5d2d5f31254d472beb4eb38369a9
        B/clauses/window-04/meta.json: 3d20560975025b6b82e5f009ba887ba5204f648e686d97c8968c0f11fdd345ad
        B/clauses/window-05/raw.json: 638abe87bb302b9c05bc6687ae845d0ffcb73e413486297c787753ee1002ab33
        B/clauses/window-05/prompt.txt: 30acb4d84d1fa9b1e1449d060b3293d47e6c156873b206fce96fa201a86a3330
        B/clauses/window-05/meta.json: a788a17e5d8fffa9a6823c4f8a69a5a8af14c91246e72c50ddfcac94deb9fd6e
        B/clauses/window-02/raw.json: c36c09a3c048e96ed8506921089fef7805c4598fc54e76d801aa75a49f8895c2
        B/clauses/window-02/prompt.txt: eced275939f552670d41c7270be3527b428ebefe89dacc6cbc75854cfdaa37c9
        B/clauses/window-02/meta.json: ee22c17aede999772ab27904290688f628333f87645b7020f4ca4340f0e0e9b1
        B/clauses/window-07/raw.json: 34a34dcd8727265b0b5c1b8f6553985eaae85f2d27f632c51d92461423923937
        B/clauses/window-07/prompt.txt: dbac2c12a09bb0960d3741c567acffe0f6ca0a77565ec68587ba0462a4ebd898
        B/clauses/window-07/meta.json: 98713ddcfcf3601f778e21062d0aca7ad9d31b20b93e6d377364d637b468768b
        B/clauses/window-01/raw.json: 74bb0da6894aa8e5f97177530b9c936221efdfa69cdf5d933076b82f0084370d
        B/clauses/window-01/prompt.txt: 9224c2ad57a71dd588749aac080782c6c58f6a47bd6babe6fdd33f85a6fc6f4a
        B/clauses/window-01/meta.json: 8aece3bbbe1ab34d405ce1c35b00b2e9e4d46f3c0ae2582e5af0bc7c06b97421
        B/clauses/window-06/raw.json: c30d95af1c8471707e78630779972414c9bbb75efc8bc99e209cc4d99c6a68cd
        B/clauses/window-06/prompt.txt: 59bfa6e5651b0abcdb04b940886d24c9ca530428eaf19d3092a3df2be7942abc
        B/clauses/window-06/meta.json: 4327b3d6ee4de903377e8cb69ca055ce54305f08ab8ba20308d5ac7cdec0af24
        B/clauses/window-08/raw.json: a3f7aa44c16213fd93fe072beddc5b551365f20d66a01f65d54009d866561502
        B/clauses/window-08/prompt.txt: 50e93b4c2ddd5a48fc87fada8818c5ebeb4a9f6ac7a7878df2d4f15f7797760a
        B/clauses/window-08/meta.json: 1a2c5392e00fa4036c0b620b8b9d478ead34ed10853a8e3e4fcb29fcf1e8f55d
        B/tables/TABLE-2-page-8-2/raw.json: 5a2cd519a41b91f127b38b7c8bccd5f33b21d3d614579ba4d843365c21e265f8
        B/tables/TABLE-2-page-8-2/prompt.txt: c4b2da992696ffefb27b134dd1e69f81792a733704421308cabf89ffbdc86ea8
        B/tables/TABLE-2-page-8-2/meta.json: 1856852b8a8f1bfd49ca9ae41187fddd427e2d00816db4d8cc20d2c2a906959b
        B/tables/TABLE-1-page-7-1/raw.json: a00f1ee5b9b0d6183c97f56b0cc75c32bef1c181fe17fa167fdf576593b14f52
        B/tables/TABLE-1-page-7-1/prompt.txt: ba038ad695521c89544e3420843381a15b1564e362ba86aa3719ad62b163ab6e
        B/tables/TABLE-1-page-7-1/meta.json: a32b147324189bfaeccd9ffedd6913e0912137a69970e5249568c0d67dc406d6
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
      pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
      source_review: _compare/relationships-2026-11-16/review-current/Breitenstein2017
      source_status_sha256: d1a2bc101a3ad1c168ad384a94e550c8fb3073de23dff4a5b39e1e197493039f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: 5 weeks or more of intensive speech and language therapy
    outcome:
      text: verbal communication effectiveness in everyday life scenarios (ANELT A-scale)
    analysis_label: Subgroup analysis (extended therapy)
    relation: treatment_effect
    evidence_ids:
    - P7-S1-C4
    - P9-S2-C4
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
      pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
      source_review: _compare/relationships-2026-11-16/review-current/Breitenstein2017
      source_status_sha256: d1a2bc101a3ad1c168ad384a94e550c8fb3073de23dff4a5b39e1e197493039f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C7
      - Result passage disposed without unit P2-S4-C3
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P6-S2-C5
      - Result passage disposed without unit P7-S1-C5
      - Accounting without a linked unit P7-S1-C6
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C1
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C4
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C1
      - Unaccounted source passage P7-S1-C6
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C8
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P7-S2-C8
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P10-S1-C8
      unattached_null_or_qualifier_ids:
      - P6-S2-C2
      - P7-S1-C5
      - P7-S2-C2
      - P7-S2-C3
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 151
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S4-C2
      - P3-S1-C5
      - P3-S1-C6
      - P4-S2-C4
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P6-S1-C9
      - P7-S3-C7
      - P10-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P5-S2-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S2-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P1-S1-C5
        - P4-S2-C4
        - P4-S2-C6
        - P5-S1-C1
        - P7-S1-C6
        - P7-S2-C2
        - P8-S2-C1
        - P9-S3-C1
        - P9-S3-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C5
        - P4-S2-C10
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P5-S1-C1
        - P7-S1-C6
        - P7-S2-C2
        - P8-S2-C1
        - P9-S3-C1
        - P9-S3-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      - TABLE-2-page-8-2
      unlinked_tables:
      - TABLE-1-page-7-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P5-S3
        - P9-S2
        - P9-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
      source_review: _compare/relationships-2026-11-16/review-current/Breitenstein2017
      source_status_sha256: d1a2bc101a3ad1c168ad384a94e550c8fb3073de23dff4a5b39e1e197493039f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports primary endpoint and control group results.
    - source_id: P1-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes adverse events unrelated to study participation.
    - source_id: P2-S3-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of superiority of intensive therapy.
    - source_id: P2-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: States treatment effects remained stable after 6 months.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to previous underpowered studies.
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses feasibility of intervention.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about missing data imputation.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports protocol deviations.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports therapy duration and intensity.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports therapy intensity during deferral and follow-up.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports baseline differences (thrombolysis).
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports baseline difference in time since stroke.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater agreement and ANELT version distribution.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports ANELT version distribution in control group.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports primary endpoint and control group results.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: States group difference was independent of moderator variables.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: States group difference was independent of moderator variables.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Reports control group improvements after therapy.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: States treatment effects remained stable after 6 months.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports results for subgroup with 5+ weeks of therapy.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of difference in baseline characteristics for subgroup.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports improvements in SAPS and SAQOL-39.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of correlation between SAPS gains and moderators.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null findings for ANELT B, SAPS phonology, NVLT, TMT, mRS.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null findings for ANELT B, SAPS phonology, NVLT, TMT, mRS.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Reports stability of CETI gains over 6 months.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies baseline stroke severity as a predictor of success.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no significant predictors of long-term stability.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about per-protocol population results.
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports adverse events during therapy.
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports recurrent stroke before randomisation.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on adverse events being unrelated to study.
    - source_id: P7-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of primary result in discussion.
    - source_id: P7-S2-C10
      disposition: repeated
      result_indexes:
      - 5
      - 7
      reason: Restatement of linguistic and quality-of-life improvements.
    - source_id: P7-S3-C1
      disposition: repeated
      result_indexes:
      - 5
      - 7
      reason: Restatement of linguistic and quality-of-life improvements.
    - source_id: P7-S3-C2
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement that no moderators were noted.
    - source_id: P7-S3-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of null findings for non-targeted cognitive functions.
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 1 data on therapy duration and intensity.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of VAMS.
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of AAT.
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of SLT and AAT profile height.
    - source_id: P7-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 1 caption.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Reports control group replication of treatment effect.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of the distribution of treatment effect (outliers).
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null effect of low-intensity therapy during deferral.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 13
      reason: Reports null effect of low-intensity therapy during follow-up.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about lack of dropouts during therapy.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of dropout rates compared to Cochrane review.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on feasibility of intensive therapy.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of health-care cost as a barrier.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 5
      - 6
      reason: Table 2 providing primary and secondary outcome data.
    - source_id: P8-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 data (flattened cells).
    - source_id: P8-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of ANELT.
    - source_id: P8-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of SAPS.
    - source_id: P8-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of QoL.
    - source_id: P8-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of SAQOL-39.
    - source_id: P8-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of CETI.
    - source_id: P8-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of NVLT.
    - source_id: P8-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of TMT and mRS.
    - source_id: P8-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 caption.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies stroke severity as the only significant predictor.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Specifies that milder stroke severity predicts greater improvement.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of persistence of treatment gains.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of mean gain in points.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports mean increases for subgroup with 5+ weeks of therapy.
    - source_id: P9-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 3 labels.
    - source_id: P10-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 5
      reason: Restatement of significant improvements in communication and linguistic
        abilities.
    unresolved_coverage:
    - source_id: P7-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
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
    - source_id: P8-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C7
    - P2-S3-C5
    - P2-S3-C7
    - P2-S4-C3
    - P5-S2-C2
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C12
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C5
    - P7-S1-C5
    - P7-S1-C7
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C9
    - P7-S2-C10
    - P7-S3-C1
    - P7-S3-C2
    - P7-S3-C3
    - P8-S1-C2
    - P8-S1-C5
    - P9-S1-C4
    - P9-S2-C3
    - P10-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    - TABLE-2-page-8-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S2-C5
      - P5-S1-C7
      - P6-S1-C10
      recruited_sample:
      - P1-S2-C4
      - P5-S3-C1
      eligibility:
      - P1-S1-C3
      - P3-S1-C5
      - P3-S1-C6
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S1-C7
      - P5-S1-C8
      dependent_variable_statement:
      - P1-S1-C5
      - P4-S3-C7
      - P4-S3-C8
      - P4-S3-C9
      limitations:
      - P10-S1-C9
      - P10-S1-C10
      - P10-S1-C11
      - P10-S2-C2
      - P10-S2-C3
      - P10-S2-C6
      personal_factors: []
      tested_personal_effects:
      - P7-S1-C7
      - P7-S2-C3
      adjustment_roles:
      - P5-S2-C5
      explicitly_not_adjusted:
      - P5-S2-C9
      descriptive_personal_factors:
      - P6-S2-C2
      - P6-S2-C3
      - P6-S3-C1
      - P7-S3-C8
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P5-S2-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S2-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P1-S1-C5
      - P4-S2-C4
      - P4-S2-C6
      - P5-S1-C1
      - P7-S1-C6
      - P7-S2-C2
      - P8-S2-C1
      - P9-S3-C1
      - P9-S3-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C5
      - P4-S2-C10
      - P4-S3-C7
      - P4-S3-C8
      - P4-S3-C9
      - P5-S1-C1
      - P7-S1-C6
      - P7-S2-C2
      - P8-S2-C1
      - P9-S3-C1
      - P9-S3-C2
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
      pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
      review_sha256: 39bdf7f698e2d17411ff9ddd64bdace028506d60374fcd704603e6cfa833a930
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
      - P7-S1-C4
      - P9-S2-C4
      source_result: In a subgroup of 34 patients (19 intervention, 15 control) who
        received 5 weeks or more of intensive speech and language therapy, the mean
        change in ANELT A-scale score from baseline was roughly 1 point larger after
        the extended therapy period (median 6 weeks) compared to the initial 3 weeks
        of therapy. The source describes this as a numerical increase in the mean
        change score, not a statistically significant between-group difference or
        a formal test of the extended duration effect.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the subgroup analysis of patients receiving
            5+ weeks of therapy, comparing the outcome after the extended period to
            the initial 3-week period. This matches the source description in P7-S1-C4
            and P9-S2-C4.
          source_ids:
          - P7-S1-C4
          - P9-S2-C4
        direction:
          answer: fits
          reason: The source states the mean change was 'roughly 1 point larger' after
            the extended therapy. The draft claim that the change was 'larger' preserves
            the direction of the observed effect. The source does not provide a p-value
            for this specific comparison, so the draft's qualitative description is
            faithful to the available text.
          source_ids:
          - P7-S1-C4
          - P9-S2-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as 5+ weeks of intensive speech
            and language therapy. The outcome is verbal communication effectiveness
            measured by the ANELT A-scale. The patient measurement is non-imaging
            (behavioral/clinical assessment), which is correct as the ANELT is a standardized
            test, not an imaging modality.
          source_ids:
          - P7-S1-C4
          - P4-S2-C10
        qualifications:
          answer: fits
          reason: The draft correctly identifies this as a subgroup analysis. It also
            includes the qualification that the extended therapy group did not differ
            from the 3-week group in key baseline characteristics (age, sex, etc.),
            which is supported by P7-S1-C5. This is a material qualifier that supports
            the validity of the subgroup comparison.
          source_ids:
          - P7-S1-C4
          - P7-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes the necessary caveat that this is a subgroup
            analysis. It does not overstate the result as a primary finding or a statistically
            significant difference between the 3-week and 5-week groups, which is
            appropriate given the source text only reports the mean difference without
            a p-value for this specific comparison.
          source_ids:
          - P7-S1-C4
          - P9-S2-C4
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: patients with chronic aphasia (lasting 6 months or more) after stroke,
        aged 18-70 years
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 18, 7E+1'
    analysis_identity:
      id: R005
      exposure:
        text: 5 weeks or more of intensive speech and language therapy
      outcome:
        text: verbal communication effectiveness in everyday life scenarios (ANELT
          A-scale)
      analysis_label: Subgroup analysis (extended therapy)
      relation: treatment_effect
      evidence_ids:
      - P7-S1-C4
      - P9-S2-C4
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
        pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
        source_review: _compare/relationships-2026-11-16/review-current/Breitenstein2017
        source_status_sha256: d1a2bc101a3ad1c168ad384a94e550c8fb3073de23dff4a5b39e1e197493039f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d2773bfed486a49933d5f92a002f1ba9793522abed152513c57aa8f647eb3115
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C8
          page: 4
          text_layer_sha256: d2773bfed486a49933d5f92a002f1ba9793522abed152513c57aa8f647eb3115
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "We \nalso did additional outcome assessments in the subgroup\
          \ \nof patients from both groups who had 5 weeks or more of \nintensive\
          \ speech and language therapy; assessments \nwere done within 3 working\
          \ days of completion of the \nintensive treatment period."
        anchor_text: "We \nalso did additional outcome assessments in the subgroup\
          \ \nof patients from both groups who had 5 weeks or more of \nintensive\
          \ speech and language therapy; assessments \nwere done within 3 working\
          \ days of completion of the \nintensive treatment period."
        excluded_fragments: []
        image_sha256: b7052b583ebd83e8a58e5617ca63f5480287ac73304aecf43981c125214ff5b9
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1a84e18965df4f21df445b9bb4325c05e53feffca4065ea25808bc909024befc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 60b41a366c1c90de5f4d49c6756ab7081af15af5ab698a5d42791f690c603b52
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 60b41a366c1c90de5f4d49c6756ab7081af15af5ab698a5d42791f690c603b52
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Participants\nInclusion criteria, which aimed to replicate\
          \ realistic \nroutine health-care conditions, were chronic aphasia \n(confirmed\
          \ using the Aachen Aphasia Test [AAT])22 lasting \n6 months or more after\
          \ an ischaemic or haemorrhagic \nstroke, age 18–70 years, German as first\
          \ language, basic \ncomprehension abilities and at least rudimentary attempts\
          \ \nto verbally communicate (communication score >0 on the \nAAT spontaneous\
          \ speech scale), and the ability to follow \nsimple instructions (at least\
          \ one correct response on the \nfirst ten items of the AAT Token Test)."
        anchor_text: "Participants\nInclusion criteria, which aimed to replicate realistic\
          \ \nroutine health-care conditions, were chronic aphasia \n(confirmed using\
          \ the Aachen Aphasia Test [AAT])22 lasting \n6 months or more after an ischaemic\
          \ or haemorrhagic \nstroke, age 18–70 years, German as first language, basic\
          \ \ncomprehension abilities and at least rudimentary attempts \nto verbally\
          \ communicate (communication score >0 on the \nAAT spontaneous speech scale),\
          \ and the ability to follow \nsimple instructions (at least one correct\
          \ response on the \nfirst ten items of the AAT Token Test)."
        excluded_fragments: []
        image_sha256: 9443524458f0c66b9884876214d16f19ac78448e9b74e1d9ebc9614cdf32aa23
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "Subgroup analysis of 34 patients (19 in the intervention \ngroup and 15\
    \ in the control group) who received 5 weeks \nor more of intensive speech and\
    \ language therapy \nshowed that the mean change in ANELT A-scale score \nfrom\
    \ baseline was roughly 1 point larger (4·23 points \n[SD 4·28], 95% CI 2·74–5·73)\
    \ after a median of 6 weeks \n(IQR 5–7) of intensive therapy than after the initial\
    \ \n3 weeks of intensive therapy (3·32 points [5·64], \n1·35–5·29; appendix p\
    \ 12)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
