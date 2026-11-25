---
id: atrial_fibrillation
name: atrial fibrillation
kind: ingredient
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: mortality
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: mortality
  target_kind: prognosis
  claim: In a multivariate analysis including age, aetiology of stroke, degree of
    aphasia, and neurological deficit, increased mortality among aphasic patients
    was related to the presence of atrial fibrillation.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: aphasic patients with acute stroke
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
  - The sample includes both consecutive and non-consecutive acute stroke patients
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Presence of atrial fibrillation registered as part
    of cardiovascular morbidity history upon admission. The finding is specific to
    the subgroup of patients with aphasia. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:mortality
  citation: '@Laska2001'
  source_passages:
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      neurological

      de®cit,

      increased

      mortality

      among

      aphasic patients was related to the presence of atrial

      ®brillation (P < 0.001).'
    supports: claim
  - section: Original source P8-S1-C15
    page: 8
    quote: 'Multivariate

      analysis showed that the only factor with a signi-

      ®cant relationship to the higher mortality among

      aphasic

      patients

      was

      atrial

      ®brillation.'
    supports: claim
  - section: Original source P3-S3-C3
    page: 3
    quote: "In a\nmultivariate analysis including age, aetiology of\nstroke, presence\
      \ of atrial ®brillation and degree of\nAPHASIA IN ACUTE STROKE\n1\n415\nÓ 2001\
      \ Blackwell Science Ltd Journal of Internal Medicine 249: 413±422\n 13652796,\
      \ 2001, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2796.2001.00812.x\
      \ by University of Queensland, Wiley Online Library on [20/10/2026]."
    supports: method
  - section: Original source P2-S1-C10
    page: 2
    quote: 'Among

      these

      non-consecutive

      acute

      stroke patients, another 83 aphasics were identi®ed,

      yielding a total of 119 aphasic patients.'
    supports: sample
  - section: Original source P2-S1-C14
    page: 2
    quote: 'Mortality, however, was registered for all 189

      patients (106 + 83) during the entire 18-month

      follow-up period.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Laska2001
  proposal_id: R002
  review_status_sha256: 6c2d36ff414f8ed91a747a481f48ddbc0b1a611fc4e918af9c85ea6bf166dbe0
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
        A/passages.json: 07fa68e3e0f73df74aaacb49121e7ed7e52e592df8fe6f3b43ec6235a2e30901
        A/raw.json: ed2f6e1ff99e3d5a44a5fb3ef2fb04bae1f5a73571c2f704d15c878bc0b2615d
        A/source-units.json: 7629216b44640d12529936e040603f9e2b78a03b49e7dbabd30e22a4bf384e1f
        A/full-source-units.json: a0c925e712957558a3c00bf52dcfa39e5fcdd8a1efeb2a0869cffae77d439f1f
        A/meta.json: 116174ddfd7d710e1f9a9bc17562141853aefef5be7e2479ed7aa5b5163257c9
        A/table-images/page-7.png: 82e08b4b3add944aaa79bcebbe0f371f2f4af509bec71d5f0096ab0b18de6f52
        A/table-images/page-4.png: f1f7f9a4b9f051d63983f407b305c7055d195c1f83b56a670827f9455f718ad3
        A/table-images/TABLE-1-page-4-1.png: bcfe5d7fed59cedadbffba31c34f32d503cb75ea755785d2cd7198ba473c7985
        A/table-images/manifest.json: c72916a8e1de9a2b0000ca46349421e06c643ca1bbe12cb5072e212b58b37f23
        A/table-images/TABLE-3-page-7-2.png: aa3d41550d05d5d4f46d6a0f59df83c3566213ff1ccccb86dfe706479eb8ed30
        A/table-images/TABLE-2-page-7-1.png: 27029b5421c365b7e70d3b5511d102c133ac32bf9a24c0af04fa3b082aba08c3
        A/clauses/window-03/raw.json: c1f405af4e93b7d9c160724f457c11ae1f36b8764f31b18d440548ba15eb1bd6
        A/clauses/window-03/prompt.txt: a4cf869f244de60ccd24dd7189ccc6870cf60e308609c402daee830f025e25b6
        A/clauses/window-03/meta.json: 013e5e7fb0c5f12491e55b78bee3077c99c2fbe60e9668abd624395eae0b7db8
        A/clauses/window-04/raw.json: 0da107d844f42b1bb0fe9992c35865aa1f3e50228307142dc138cd9b1a1af1c1
        A/clauses/window-04/prompt.txt: c4670f4280a5308802b5afc3d76c1aefd142c18139c6176f34cb4ea7d3e6d656
        A/clauses/window-04/meta.json: aa1fb76bf9ea123b913a10b52e3e7f9237490a3657cfd0d1b06b7956b4cedba7
        A/clauses/window-05/raw.json: d0eb2ce20f9336c930fb6015c995353bce5a83ec79453662ce6ed44afc32c17e
        A/clauses/window-05/prompt.txt: d39e0de7baa540ca1e727ff6ba973d3adcc53bd42f66c8776b778c25b0142efe
        A/clauses/window-05/meta.json: 7d1e2d2602e097fc226ea43c2cd5cfecf6916eac96921e38a514d904b2770337
        A/clauses/window-02/raw.json: 76a51da14e63218e654f63875a1821ae9a1f9ecb7d2b3118d0b2bad22562a870
        A/clauses/window-02/prompt.txt: 67d8914fb4624ab1eafd2192882e9fb89d6ad018d8a9eeae881fc7696a49c9eb
        A/clauses/window-02/meta.json: e339e2d8a02e10e1b2a4eb6ced73f6fcc085228b6dc10d8a9c3ad4bca38a8322
        A/clauses/window-07/raw.json: 014d21a858aac2b3eefc2e84e43c797dca83354f3688735d755bc86e9fdc8971
        A/clauses/window-07/prompt.txt: ca6c3f52f415e4e2095a047361545fbee5c61e044caf27ed6bd97e4cb288f7d9
        A/clauses/window-07/meta.json: e98f13b032f2c1eb84aeecb160b41a0d62483f7826f4a471b6aed6238e047ee4
        A/clauses/window-01/raw.json: d36149b2f71477de756620c6f5d53ad170c94052ae773e750146c65794afbcf4
        A/clauses/window-01/prompt.txt: d7300c49e557e2653ca190660cfb1d9c1f4c57a98865b2af6ce29ca4b0b389a9
        A/clauses/window-01/meta.json: f4e8aea99b3ac1cfdfee95ac1f1c1f8c9a3a7d16f808b6bd6f569abf945e9124
        A/clauses/window-06/raw.json: 3c6b430b56bf6e07e9d451ad0fb6bd7d8b9bcd94c2442e25d9854a9484ed507d
        A/clauses/window-06/prompt.txt: 96f68a0b83f3a3874057273d35d33a8b4d67c5aee86e0f64ae21e6ead9cf0e7f
        A/clauses/window-06/meta.json: 0f8c50194a207b82cb1c26f49fa9bb2747d7b5dcb3a47e9f55f2f12bec5bf0fd
        A/tables/TABLE-3-page-7-3/raw.json: 97788ade148e3e51ea5324b4615cd3e00f2558808f747820e8ea5f1758e90e74
        A/tables/TABLE-3-page-7-3/prompt.txt: 637406c19feef138c004c49b5043e3154ef30a9c7d718e9beaa695c6f993625c
        A/tables/TABLE-3-page-7-3/meta.json: 9a379ea0fe2437788dd22859a80ce810252ec481034463b2303fb78ebeddc0b6
        A/tables/TABLE-2-page-7-2/raw.json: 130e2438234fdc91822d40933b0bf035a391ea2cc48def77c6408279ca6f6e3d
        A/tables/TABLE-2-page-7-2/prompt.txt: 8c7abe86e050e308f2af3981111cff562b130cd898733bb0851c7de646c7e0c7
        A/tables/TABLE-2-page-7-2/meta.json: 9a0f262aaa6af2b22a4e1be255df6149f4b5168414d2562d918cfc96f9462449
        A/tables/TABLE-1-page-4-1/raw.json: 00beaceb3c880c19ad7f9e0253170ad8c659a3949b3d75ce495660ba8bf090c0
        A/tables/TABLE-1-page-4-1/prompt.txt: c14ca57d638209df5290614d7f166a6fc6d33bc59008d81f0938364c756329fe
        A/tables/TABLE-1-page-4-1/meta.json: dd6bee98cbda073eed9f273f5cc3b45e796295a170b0463a9d9f63945b588294
        B/passages.json: 07fa68e3e0f73df74aaacb49121e7ed7e52e592df8fe6f3b43ec6235a2e30901
        B/raw.json: fc5b13b607d617289536cc949d23f0c8ed92d2b61ad047c478fba858610ebc95
        B/source-units.json: 7629216b44640d12529936e040603f9e2b78a03b49e7dbabd30e22a4bf384e1f
        B/full-source-units.json: a0c925e712957558a3c00bf52dcfa39e5fcdd8a1efeb2a0869cffae77d439f1f
        B/meta.json: 1dc15a2f64e5d15f0e4568a412d39ef4538373ef590a0d5f96ea53b608f4d858
        B/table-images/page-7.png: 82e08b4b3add944aaa79bcebbe0f371f2f4af509bec71d5f0096ab0b18de6f52
        B/table-images/page-4.png: f1f7f9a4b9f051d63983f407b305c7055d195c1f83b56a670827f9455f718ad3
        B/table-images/TABLE-1-page-4-1.png: bcfe5d7fed59cedadbffba31c34f32d503cb75ea755785d2cd7198ba473c7985
        B/table-images/manifest.json: d510d2f5085aa089b873eeece641adc9d48a80f0338a925a37407fcd1c50f9c3
        B/table-images/TABLE-3-page-7-2.png: aa3d41550d05d5d4f46d6a0f59df83c3566213ff1ccccb86dfe706479eb8ed30
        B/table-images/TABLE-2-page-7-1.png: 27029b5421c365b7e70d3b5511d102c133ac32bf9a24c0af04fa3b082aba08c3
        B/clauses/window-03/raw.json: e98d09b2ebbea47a218b776400a9d1348e80ed8dd93b49302dda311a9d11c2bd
        B/clauses/window-03/prompt.txt: a4cf869f244de60ccd24dd7189ccc6870cf60e308609c402daee830f025e25b6
        B/clauses/window-03/meta.json: 00a6db365f46d2bbdf26c61deb7bfa7866740080d820cd72442e094362b23c52
        B/clauses/window-04/raw.json: ff01e1f76f9c9ff1b0cb05ce8a0ef3773d0b13961f31c79290c8c32e1cca7871
        B/clauses/window-04/prompt.txt: c4670f4280a5308802b5afc3d76c1aefd142c18139c6176f34cb4ea7d3e6d656
        B/clauses/window-04/meta.json: a60376f106017289112d00a1a836c78f5123e57adcc77bdf4ff04328807e187e
        B/clauses/window-05/raw.json: edc99917d20b3bf3b5bf17684ee5cc9f32bf18d63496e1d1cca7c6e7230e2e7f
        B/clauses/window-05/prompt.txt: d39e0de7baa540ca1e727ff6ba973d3adcc53bd42f66c8776b778c25b0142efe
        B/clauses/window-05/meta.json: 8c76fb63ad21d906a8ab2a78cc1db2c917ce3d4d995d8e0e95bbbd302dee6c7b
        B/clauses/window-02/raw.json: cee242e80c77ff3212a0f8f02b35ab8b4b496082ae6b7fb5475d68c7bb2dd4a2
        B/clauses/window-02/prompt.txt: 67d8914fb4624ab1eafd2192882e9fb89d6ad018d8a9eeae881fc7696a49c9eb
        B/clauses/window-02/meta.json: c1596ce5d6d3b20237377948c03ef116b5ddf60c31343fcef0de41688a232175
        B/clauses/window-07/raw.json: c69f4af4811695b443523f20cd0feeb7b4499d952f9929aacdb5176d1ab3ff63
        B/clauses/window-07/prompt.txt: ca6c3f52f415e4e2095a047361545fbee5c61e044caf27ed6bd97e4cb288f7d9
        B/clauses/window-07/meta.json: 67bcf617ad5e21b05649371fe29e1dfae3bdf2d7a62d0ea6a6d176fa4ad6cabd
        B/clauses/window-01/raw.json: 23d0917810a682cabdcd8d015bca1f2f91146d7dbec925dafe692f08704c3463
        B/clauses/window-01/prompt.txt: d7300c49e557e2653ca190660cfb1d9c1f4c57a98865b2af6ce29ca4b0b389a9
        B/clauses/window-01/meta.json: 420e3900680818cd1a819663f98751b4adf89a293769c28f2e3b1fdc22e1ffaf
        B/clauses/window-06/raw.json: 181ead4e30e1deb129f962d76fe68caeca1eac8a4843e72606fa673bfd83d02a
        B/clauses/window-06/prompt.txt: 96f68a0b83f3a3874057273d35d33a8b4d67c5aee86e0f64ae21e6ead9cf0e7f
        B/clauses/window-06/meta.json: 36589fa08e099c8767d85e484eb1030fe1d283d854b800a4ac7e15bb507fb3f4
        B/tables/TABLE-3-page-7-3/raw.json: c112c2fb174e6716be8996b73dfd4e65b37a22a1bf050b910995d80eae0fc169
        B/tables/TABLE-3-page-7-3/prompt.txt: 637406c19feef138c004c49b5043e3154ef30a9c7d718e9beaa695c6f993625c
        B/tables/TABLE-3-page-7-3/meta.json: 3d05d16e572a5ed27b87b0157e7be996122d3470f7fd1451ae892f4b7a733908
        B/tables/TABLE-2-page-7-2/raw.json: c187d209d10e2ae2459c44401da21e0b2c2a6e5533d34db2fe97e79d4a623c43
        B/tables/TABLE-2-page-7-2/prompt.txt: 8c7abe86e050e308f2af3981111cff562b130cd898733bb0851c7de646c7e0c7
        B/tables/TABLE-2-page-7-2/meta.json: 4cfa8fa64be89222db9e64c4496033a71c89ece22839bfc677c9b9d527b512e2
        B/tables/TABLE-1-page-4-1/raw.json: 33358ec2006a7a9854428cef7720fc97230ad5a90e1d1170f3e89039bd19e175
        B/tables/TABLE-1-page-4-1/prompt.txt: c14ca57d638209df5290614d7f166a6fc6d33bc59008d81f0938364c756329fe
        B/tables/TABLE-1-page-4-1/meta.json: 37a0026532f1d95c1b52b780c1ebfb532793e9f05e708b427dc5a1161dd3f905
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
      pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
      source_review: _compare/relationships-2026-11-16/review-current/Laska2001
      source_status_sha256: b1e272014073d43657e8102c9334e00a30762c491465de7159cb231c38f7a3d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: atrial fibrillation
    outcome:
      text: mortality among aphasic patients
    analysis_label: Multivariate mortality analysis
    relation: association
    evidence_ids:
    - P4-S1-C1
    - P8-S1-C15
    qualifier_ids:
    - P3-S3-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
      source_review: _compare/relationships-2026-11-16/review-current/Laska2001
      source_status_sha256: b1e272014073d43657e8102c9334e00a30762c491465de7159cb231c38f7a3d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C17
      - Accounting without a linked unit P1-S1-C18
      - Accounting without a linked unit P1-S1-C19
      - Accounting without a linked unit P1-S1-C20
      - Accounting without a linked unit P1-S1-C21
      - Accounting without a linked unit P1-S1-C22
      - Accounting without a linked unit P1-S1-C23
      - Unaccounted source passage P1-S1-C23
      - Unaccounted source passage P1-S1-C22
      - Unaccounted source passage P1-S1-C19
      - Unaccounted source passage P1-S1-C17
      - Unaccounted source passage P1-S1-C20
      - Unaccounted source passage P1-S1-C18
      - Unaccounted source passage P1-S1-C21
      - Result passage disposed without unit P3-S2-C11
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P3-S2-C14
      - Result passage disposed without unit P3-S2-C15
      - Result passage disposed without unit P3-S2-C16
      - Result passage disposed without unit P3-S2-C17
      - Result passage disposed without unit P3-S3-C3
      - 'window 6: invalid/duplicate disposition P5-S1-C14'
      - Result passage disposed without unit P5-S1-C14
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C9
      - Result passage disposed without unit P7-S1-C13
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C12
      - Result passage disposed without unit P8-S1-C13
      unattached_null_or_qualifier_ids:
      - P1-S1-C20
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 135
      unselected_timing_passages:
      - P1-S1-C15
      - P2-S1-C5
      - P2-S1-C6
      - P2-S1-C7
      - P2-S1-C9
      - P2-S1-C10
      - P2-S1-C14
      - P2-S2-C12
      - P2-S2-C13
      - P4-S1-C2
      - P4-S1-C7
      - P5-S1-C5
      - P6-S2-C3
      - P8-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P8-S1-C16
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: personal_factors
        source_ids:
        - P2-S2-C1
        - P2-S2-C3
        - P2-S2-C4
        - P3-S2-C14
        - P4-S1-C4
        - P5-S1-C1
        - P6-S1-C9
        - P6-S1-C11
        - P7-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P4-S1-C1
        - P5-S1-C3
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P6-S1-C1
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C9
        - P6-S1-C10
        - P6-S1-C12
        - P7-S1-C11
        - P8-S1-C15
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      unlinked_tables:
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
      source_review: _compare/relationships-2026-11-16/review-current/Laska2001
      source_status_sha256: b1e272014073d43657e8102c9334e00a30762c491465de7159cb231c38f7a3d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes prevalence of aphasia in acute stroke
    - source_id: P1-S1-C18
      disposition: represented
      result_indexes:
      - 0
      reason: establishes mortality difference between aphasics and non-aphasics
    - source_id: P1-S1-C19
      disposition: repeated
      result_indexes:
      - 1
      reason: restatement of atrial fibrillation association with prognosis
    - source_id: P1-S1-C20
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes recovery and mortality counts for aphasic group
    - source_id: P1-S1-C21
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes changes in aphasia type proportions over time
    - source_id: P1-S1-C22
      disposition: represented
      result_indexes:
      - 2
      reason: establishes recovery rate for initial mild aphasia
    - source_id: P1-S1-C23
      disposition: represented
      result_indexes:
      - 3
      reason: establishes improvement for low initial speech function
    - source_id: P1-S1-C24
      disposition: represented
      result_indexes:
      - 3
      reason: establishes age-related recovery
    - source_id: P1-S1-C28
      disposition: background_or_descriptive
      result_indexes: []
      reason: general statement of improvement
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: general statement on recovery potential
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes prevalence of aphasia in consecutive group
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes recurrent stroke counts
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes mean age
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes stroke aetiology
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no significant difference in baseline characteristics
    - source_id: P3-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes total deaths
    - source_id: P3-S2-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes cause of deaths
    - source_id: P3-S2-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes in-hospital mortality trend
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: establishes 18-month mortality difference
    - source_id: P3-S3-C3
      disposition: represented
      result_indexes:
      - 1
      reason: qualifies multivariate analysis for mortality
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: establishes atrial fibrillation as significant factor for mortality
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes recovery and death counts at 18 months
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes missing patients
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes age difference between consecutive and non-consecutive groups
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no differences in gender, aetiology, etc.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 12
      reason: establishes case fatality difference between consecutive and non-consecutive
        groups
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes assessment of patients
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no age difference between aphasia types acutely
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes age trends at 3 months
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes prevalence of fluent vs non-fluent aphasia
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: establishes higher speech function in fluent aphasics
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: general statement of improvement across types
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes common aphasia types
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: references Figure 3
    - source_id: P5-S1-C14
      disposition: repeated
      result_indexes:
      - 6
      reason: restatement of higher speech function in fluent aphasics
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: establishes higher speech function in fluent aphasics
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: qualifies univariate analysis of recovery factors
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: establishes age as significant factor for recovery in multivariate analysis
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: establishes initial severity as factor for recovery
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes characteristics of those who recovered completely
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes recovery rate for mildest aphasia
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes outcomes for those not recovering completely
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes cardiovascular event counts
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: establishes associations between cardiovascular events and age, gender,
        SSSS
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: establishes association between cardiovascular events and acute aphasia
        severity
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no differences in aetiology, volume, or BP
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no difference in recovery by handedness
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes lesion location counts
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes median lesion volume
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes lesion types
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes right-hemisphere lesion demographics
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 8
      reason: establishes relation between lesion volume and aphasia degree
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: states no difference in lesion volume for recovery
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 9
      reason: establishes no difference in mortality by visible lesion presence
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes evolution prevalence
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 10
      reason: establishes no effect of age or gender on evolution
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 10
      reason: establishes Wernicke's aphasia association with evolution
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 11
      reason: establishes no relation between initial degree and evolution
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes incidence of first-ever aphasia
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes testing timeline
    - source_id: P8-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: general statement on test combination
    - source_id: P8-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes hospital mortality
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 1
      reason: establishes atrial fibrillation as the only significant factor for mortality
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes cardiac embolism in deaths
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes global aphasia prevalence
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes global aphasia proportion at 18 months
    - source_id: P8-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes Wernicke's aphasia proportions
    - source_id: P8-S2-C14
      disposition: represented
      result_indexes:
      - 3
      reason: establishes higher recovery rate for younger patients
    - source_id: P8-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: describes improvement in severe speech impairment
    - source_id: P8-S3-C2
      disposition: represented
      result_indexes:
      - 2
      reason: establishes recovery rate for high initial functional communication
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: states lesion location is not helpful for predicting outcome
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: general conclusion on mortality and cardiovascular disease
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 3
      reason: restatement of factors influencing speech recovery
    unresolved_coverage:
    - source_id: P8-S1-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C17
    - P1-S1-C19
    - P1-S1-C20
    - P1-S1-C21
    - P1-S1-C28
    - P1-S2-C2
    - P3-S2-C11
    - P3-S2-C12
    - P3-S2-C13
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C16
    - P3-S2-C17
    - P3-S2-C18
    - P3-S3-C3
    - P4-S1-C3
    - P4-S1-C7
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C11
    - P5-S1-C12
    - P5-S1-C13
    - P5-S1-C14
    - P6-S1-C2
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C11
    - P6-S1-C12
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C9
    - P7-S1-C13
    - P8-S1-C11
    - P8-S1-C12
    - P8-S1-C13
    - P8-S1-C17
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C9
    - P8-S2-C11
    - P8-S2-C15
    - P8-S3-C1
    - P9-S1-C2
    - P9-S1-C6
    - P9-S1-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    - TABLE-3-page-7-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C10
      - P4-S1-C1
      - P4-S1-C2
      recruited_sample:
      - P2-S1-C5
      - P2-S1-C6
      - P2-S1-C7
      eligibility:
      - P2-S1-C5
      imaging_provenance:
      - P2-S2-C5
      imaging_timing:
      - P2-S2-C5
      outcome_timing:
      - P2-S1-C11
      - P3-S2-C2
      - P5-S1-C10
      - P6-S1-C2
      - P7-S1-C9
      outcome_definition:
      - P3-S2-C2
      - P5-S1-C10
      - P6-S1-C2
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations:
      - P8-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C1
      - P5-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C13
      - P4-S1-C4
      - P5-S1-C1
      - P6-S1-C9
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P8-S1-C16
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: personal_factors
      source_ids:
      - P2-S2-C1
      - P2-S2-C3
      - P2-S2-C4
      - P3-S2-C14
      - P4-S1-C4
      - P5-S1-C1
      - P6-S1-C9
      - P6-S1-C11
      - P7-S1-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P4-S1-C1
      - P5-S1-C3
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P6-S1-C1
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C9
      - P6-S1-C10
      - P6-S1-C12
      - P7-S1-C11
      - P8-S1-C15
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
      pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
      review_sha256: 6c2d36ff414f8ed91a747a481f48ddbc0b1a611fc4e918af9c85ea6bf166dbe0
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
      - P4-S1-C1
      - P8-S1-C15
      source_result: In a multivariate analysis including age, aetiology of stroke,
        presence of atrial fibrillation, and degree of neurological deficit, increased
        mortality among aphasic patients was significantly related to the presence
        of atrial fibrillation (P < 0.001).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a multivariate analysis involving
            age, aetiology, atrial fibrillation, and neurological deficit to explain
            mortality differences in aphasic patients. The proposed core correctly
            identifies this specific model and its outcome.
          source_ids:
          - P3-S3-C3
          - P4-S1-C1
          - P8-S1-C15
        direction:
          answer: fits
          reason: The source states that increased mortality was related to the presence
            of atrial fibrillation. The proposed core correctly captures this positive
            association (increased mortality with AF).
          source_ids:
          - P4-S1-C1
          - P8-S1-C15
        construct:
          answer: fits
          reason: The exposure is atrial fibrillation (a clinical history variable),
            and the outcome is mortality. The patient measurement is non-imaging (clinical/registry
            data), which is correct as the analysis relies on clinical variables rather
            than imaging metrics like lesion volume or tractography.
          source_ids:
          - P2-S2-C1
          - P4-S1-C1
        qualifications:
          answer: fits
          reason: The source specifies that this finding applies to the subgroup of
            patients with aphasia (P3-S3-C3, P4-S1-C1). The proposed core includes
            the qualification that the finding is specific to this subgroup.
          source_ids:
          - P3-S3-C3
          - P4-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The core correctly identifies the multivariate nature of the analysis
            and the specific covariates. No material caveats regarding the interpretation
            of the association are omitted. The limitation regarding the mixed consecutive/non-consecutive
            sample is noted in the core's limitations field.
          source_ids:
          - P4-S1-C1
          - P8-S1-C15
      optional_pending:
      - Sample size for the specific multivariate model is not explicitly transcribed
        in the provided snippets, though the total aphasic cohort is 119.
      - Exact P-value is P < 0.001, but specific coefficient or hazard ratio is not
        transcribed.
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
    - Sample size for the specific multivariate model is not explicitly transcribed
      in the provided snippets, though the total aphasic cohort is 119.
    - Exact P-value is P < 0.001, but specific coefficient or hazard ratio is not
      transcribed.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    - field: sample.n
      original: 119
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: 18-month follow-up
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 18'
    analysis_identity:
      id: R002
      exposure:
        text: atrial fibrillation
      outcome:
        text: mortality among aphasic patients
      analysis_label: Multivariate mortality analysis
      relation: association
      evidence_ids:
      - P4-S1-C1
      - P8-S1-C15
      qualifier_ids:
      - P3-S3-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
        source_review: _compare/relationships-2026-11-16/review-current/Laska2001
        source_status_sha256: b1e272014073d43657e8102c9334e00a30762c491465de7159cb231c38f7a3d9
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e519a97befaf70dfa5efdd20234f764d142ee8f45e868837f0f731c925c5992c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C10
          page: 2
          text_layer_sha256: e519a97befaf70dfa5efdd20234f764d142ee8f45e868837f0f731c925c5992c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Among

          these

          non-consecutive

          acute

          stroke patients, another 83 aphasics were identi®ed,

          yielding a total of 119 aphasic patients.'
        anchor_text: 'Among

          these

          non-consecutive

          acute

          stroke patients, another 83 aphasics were identi®ed,

          yielding a total of 119 aphasic patients.'
        excluded_fragments: []
      P2-S1-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 016e702742f8f9705e9afa526de283666822d5b0f402c07833e58f63c921b904
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4ccd96c1dc8b61c9b39f0c176c03a85c4221db654bb89dc7a4a29cbc41701555
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C14
          page: 2
          text_layer_sha256: 4ccd96c1dc8b61c9b39f0c176c03a85c4221db654bb89dc7a4a29cbc41701555
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Mortality, however, was registered for all 189

          patients (106 + 83) during the entire 18-month

          follow-up period.'
        anchor_text: 'Mortality, however, was registered for all 189

          patients (106 + 83) during the entire 18-month

          follow-up period.'
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: '

    neurological

    de®cit,

    increased

    mortality

    among

    aphasic patients was related to the presence of atrial

    ®brillation (P < 0.001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
