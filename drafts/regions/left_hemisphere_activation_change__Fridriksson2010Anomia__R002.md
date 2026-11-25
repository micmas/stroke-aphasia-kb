---
id: left_hemisphere_activation_change
name: left hemisphere activation change cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: correct_naming_improvement
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: correct_naming_improvement
  target_kind: prognosis
  claim: A positive relationship was revealed between treatment-assisted increase
    in correct naming and modulation of cortical areas in the left posterior and anterior
    hemisphere; patients whose activation increased in these areas were more likely
    to improve correct naming compared with those with limited change in activation
    or damage to these regions.
  direction: likely
  relationship: correlational
  method: fMRI_FC
  sample:
    n: 19
    population: patients with left hemisphere stroke and chronic aphasia
    phase: not_reported
    time_post_onset: measured before and after 2 weeks of intensive language treatment;
      all patients had sustained stroke at least 8 months before study inclusion
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - the fMRI analysis did not deduce which specific areas within the network are more
    important than others or the dynamics of change needed to support recovery
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Change in cortical activation from pre-treatment to
    post-treatment (calculated as the contrast of parameter estimates between the
    first two and last two fMRI sessions) in the left posterior and anterior hemisphere
    clusters. fMRI analysis included 19 of 26 patients; patients with fewer than five
    correct naming responses in any fMRI session were excluded from the third-level
    analysis; outcome was standardized by each patient''s intra-session variability.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P1-S2-C9, two-model agreement, human verification
    pending): . Twenty-six patients with left hemisphere

    stroke and chronic aphasia underwent fMRI twice before and

    twice after 2 weeks of intensive language treatment targeting ano-

    mia Original text-layer quotation is preserved below. PDF image reading (P1-S3-C4,
    two-model agreement, human verification pending): . All

    had sustained a single event ischemic stroke to the left hemisphere at least

    8 months before study inclusion Original text-layer quotation is preserved below.
    PDF image reading (P4-S1-C11, two-model agreement, human verification pending):
    . Data from

    19 of 26 patients were included in the fMRI analysis. fMRI data

    from one patient were excluded from the analysis due to excessive

    head motion Original text-layer quotation is preserved below.'
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
    - proposed_concept:correct_naming_improvement
  therapy:
    id: cueing_hierarchy_treatment
    name: cueing hierarchy treatment targeting anomia
  citation: '@Fridriksson2010Anomia'
  source_passages:
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Primary outcome: fMRI results

      A positive relationship was revealed between treatment-assisted

      increase in correct naming and modulation of cortical areas in the

      left posterior and anterior hemisphere (Fig. 2).'
    supports: claim
  - section: Original source P4-S1-C4
    page: 4
    quote: 'That is, patients

      whose activation increased in the areas highlighted in Figure 2

      were more likely to improve with respect to correct naming com-

      pared with those with limited change in cortical activation or, as

      importantly, damage to these same regions.'
    supports: claim
  - section: Original source P4-S1-C9
    page: 4
    quote: "A strong relationship\nwas revealed between changes in activation in the\
      \ anterior and\nposterior clusters listed in Table 1 (r(19) \x01 0.90, p \x01\
      \ 0.0001)."
    supports: claim
  - section: Original source P4-S2-C10
    page: 4
    quote: 'Treatment-related increase in correct naming

      was associated with increased cortical activity in the left hemi-

      sphere; specifically in the parietal lobe and the premotor cortex,

      including the superior portion of Broca’s area.'
    supports: claim
  - section: Original source P4-S2-C11
    page: 4
    quote: 'That is, patients

      who showed greater improvement in correct naming also expe-

      rienced greater increase in left hemisphere cortical activation

      compared with their counterparts whose correct naming out-

      come was less favorable.'
    supports: claim
  - section: Original source P6-S1-C4
    page: 6
    quote: 'Although the current data cannot identify the specific neural

      mechanism that mediates recovery from anomia, it is clear that

      improved naming relied on increased brain activation in the left

      hemisphere.'
    supports: claim
  - section: Original source P1-S2-C9
    page: 1
    quote: 'Twenty-six patients with left hemisphere

      stroke and chronic aphasia underwent fMRI twice before and

      twice after 2 weeks of intensive language treatment targeting ano-

      mia.'
    supports: sample
  - section: Original source P1-S3-C4
    page: 1
    quote: 'All

      had sustained a single event ischemic stroke to the left hemisphere at least

      8 months before study inclusion.'
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: 'Data from

      19 of 26 patients were included in the fMRI analysis. fMRI data

      from one patient were excluded from the analysis due to excessive

      head motion.'
    supports: sample
  - section: Original source P2-S5-C4
    page: 2
    quote: 'The third and final level included a regression

      analysis in which data from all participants were combined to predict

      treatment outcome (i.e., change in correct naming).'
    supports: method
  - section: Original source P3-S1-C8
    page: 3
    quote: 'The third and final step involved a regression analysis in which the

      COPE maps created in the second-level analyses were entered to predict

      treatment related change in naming.'
    supports: method
  - section: Original source P5-S2-C4
    page: 5
    quote: 'However,

      the current fMRI analysis did not deduce which of these areas is

      more important than others or the dynamics of change needed to

      support recovery.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2010Anomia
  proposal_id: R002
  review_status_sha256: 0634f8ea926f14200e076851e40d9bd05685b109f151c68e2f682ccf8e55c003
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
        A/passages.json: 22c6c21279f9a5bd84b6d114eaf133cee39f98aab333b606408c35fcbf3b220c
        A/raw.json: 997f473c531ee6f6c4ff00424a48fd755b12375dccf1458aa0a25ed7d1a84b57
        A/source-units.json: 16b245433b8c845f969880901fed9a29d7195af0f28906e3253481488ccc38ac
        A/full-source-units.json: bb8f497e34ecd347f3198a5684985e1ed8ebf575d953fd656f9245711f6cf9c8
        A/meta.json: 5a9bf84e401199b683d38de82fed91a692ba845d64cc74096be314eb1ffdf12c
        A/table-images/page-4.png: 2e262afa33bf34633a5d98b32f2cc8c2bc8b30d7860e7052370426cb8c07c7a6
        A/table-images/TABLE-1-page-4-1.png: f720ec6760732014d6417e9b4ea6ad15bd566f1db88fb79c4d23a885aee15c9c
        A/table-images/manifest.json: 92d264881dfb4097daa28b3a06e2959ec2a28e5be71d850b6e3f0a1251db3b2d
        A/clauses/window-03/raw.json: cc452591770254394b933ee018ddcaba548847812040cb0c7f73f04e7e1579a0
        A/clauses/window-03/prompt.txt: 6acad4eba26144a6a2f9e274997c0ad028263207785e03c8857ea12e93def558
        A/clauses/window-03/meta.json: 0d5143811bf4d926e9318f06604e835a63afd162f53538d200dbcb222c9be069
        A/clauses/window-04/raw.json: 940cc8b1670e532cf59d319c41971b98b556e8b77c50d1e178a18309296a58ee
        A/clauses/window-04/prompt.txt: 8231dced11d828e8f51636d7581745f1e724e8b38f9aa8734cc436531cded670
        A/clauses/window-04/meta.json: 473ec295a7fd528f952aab8b9f1b5c3b8cea86e0565e5cec62ec36014cd3f426
        A/clauses/window-05/raw.json: 550c6b2a2863c58ae1a42bee2fe9f31243a66adb1d44d201301758213d189426
        A/clauses/window-05/prompt.txt: 0ef7490bd56a61b095ade7b040cf2444886e1dc8dd76e6e2d24f8e8090101673
        A/clauses/window-05/meta.json: 4f9a9b0dc287fbca4d82024f650fd17c6d6ff09efeee8c2e4fb7d8bba6e38be9
        A/clauses/window-02/raw.json: 46812412664d92a82d01cc33be3742989ae9f0a5092825905b0dfb65c96e87de
        A/clauses/window-02/prompt.txt: b9a67e3438e7f0264fb70248465b800eceb701e74e67f1f7311b7b3c6bb98343
        A/clauses/window-02/meta.json: d17085aa80d62a516dad37d068cd4b48d06e0583b800a084d53cb3a1fb5fb92d
        A/clauses/window-07/raw.json: 2c06d1b90c61bada3abc3c907c43f2a6b5857ed4e07adc11777e30d32dfca3f3
        A/clauses/window-07/prompt.txt: aa4c0173692c7cc7d88e54355c0cb1c8bf3eac59fa3b3ead59d579989b63a318
        A/clauses/window-07/meta.json: 386542b109ade6e66b0e7cd3a117e773acc21c19930a770feb6bfa2785268b4d
        A/clauses/window-01/raw.json: eb27424464b8482a6519c2cd11e1e4a476f7f411abadd6206f8a22128fce5e40
        A/clauses/window-01/prompt.txt: b486180e361f733f9ee0f98ed712ae290e8a5b491aa763c99ff83503b47a7cef
        A/clauses/window-01/meta.json: 73e68cd1ebc7991bb0ed7eb1140bbf0152a06312a1b704bb2638a62e30d7b2a7
        A/clauses/window-06/raw.json: 58cf1b8131c7c5100a4a4c9bcc9e350fb1d56897771307782fd44e3be7a3bebb
        A/clauses/window-06/prompt.txt: 6b2c19588abe06bd891426792661e34c563c3618c9d51ae2c9f02a3f35d1a788
        A/clauses/window-06/meta.json: 37bdeb47f670a74f7a2b932cccf96a46d2523a823bd842548f0e55fcaf7060ac
        A/tables/TABLE-1-page-4-1/raw.json: 3c0b50158d8bbf1804e94440382c5498533f524197e3df7e7c194f5047d5eca0
        A/tables/TABLE-1-page-4-1/prompt.txt: ebb5128e7dad37e43d29d7ec3ed08e49077d2283a278953ccb4a4d23be108aaf
        A/tables/TABLE-1-page-4-1/meta.json: de7de97da9cf8d73a68114c8987d39e1fbbae21ff9484c385c251af5b8a7ae3f
        B/passages.json: 22c6c21279f9a5bd84b6d114eaf133cee39f98aab333b606408c35fcbf3b220c
        B/raw.json: b31776519b87007313c4557dfda9459f7636c0d98576adfd3c08c11c386d8615
        B/source-units.json: 16b245433b8c845f969880901fed9a29d7195af0f28906e3253481488ccc38ac
        B/full-source-units.json: bb8f497e34ecd347f3198a5684985e1ed8ebf575d953fd656f9245711f6cf9c8
        B/meta.json: ecb39bf651bf99a09398ee5f51e8153632681efe40778072044f76144d890a05
        B/table-images/page-4.png: 2e262afa33bf34633a5d98b32f2cc8c2bc8b30d7860e7052370426cb8c07c7a6
        B/table-images/TABLE-1-page-4-1.png: f720ec6760732014d6417e9b4ea6ad15bd566f1db88fb79c4d23a885aee15c9c
        B/table-images/manifest.json: c44d07cd46f5c30240b33da315c7ad2070f240784e4c81e476e73739caaf59b2
        B/clauses/window-03/raw.json: 2658f07c1af17a0b6aa1374cef80a4e22762f800186b234f38a9693d6cf973a0
        B/clauses/window-03/prompt.txt: 6acad4eba26144a6a2f9e274997c0ad028263207785e03c8857ea12e93def558
        B/clauses/window-03/meta.json: 24d5235894601fed12450e4f39a13426d0fd6921c6b2f1ca7d3b3001643d167a
        B/clauses/window-04/raw.json: c7208cf4a7f99fb484f28448302850c25ba97243e2da62b639162ed3282c9044
        B/clauses/window-04/prompt.txt: 8231dced11d828e8f51636d7581745f1e724e8b38f9aa8734cc436531cded670
        B/clauses/window-04/meta.json: d4e62056160709147bd0ca3f15bb1f158ea02407b8c9439ec08e194fbd940321
        B/clauses/window-05/raw.json: 89403fc56041bccd0c8271febc8ffa8f378c3b3f4d7a766311c4003f75f07d8f
        B/clauses/window-05/prompt.txt: 0ef7490bd56a61b095ade7b040cf2444886e1dc8dd76e6e2d24f8e8090101673
        B/clauses/window-05/meta.json: 31ccc07ec3accf0d24f50eb32a4ce4904a9414968b0899a3662b403769a1b791
        B/clauses/window-02/raw.json: 6f1445a23b33a6d553d85ac5797d588ecf938df0ceaedbc58adb5b9e4eba4cfd
        B/clauses/window-02/prompt.txt: b9a67e3438e7f0264fb70248465b800eceb701e74e67f1f7311b7b3c6bb98343
        B/clauses/window-02/meta.json: 280b3b81d72c7df9a4a1e1d70fdb4fde3fa71b3e9a98d2d260957a2e1d93e5d9
        B/clauses/window-07/raw.json: a550dc4112baf81515a3b58feca72a8122b1eb4a76814a9e5e50595f6b0a2efb
        B/clauses/window-07/prompt.txt: aa4c0173692c7cc7d88e54355c0cb1c8bf3eac59fa3b3ead59d579989b63a318
        B/clauses/window-07/meta.json: 326b3de68b02b6e14ae67242c1d3acf6b75a3cd26d37c3b1e29ad96da9ad255d
        B/clauses/window-01/raw.json: 4e0d7d8d6ff7cc6fc34b8a434854f9a32ad3767053e29fe7e7112ff9506e4c83
        B/clauses/window-01/prompt.txt: b486180e361f733f9ee0f98ed712ae290e8a5b491aa763c99ff83503b47a7cef
        B/clauses/window-01/meta.json: 549b5443b6e6b82758feb6c960969c8ef6edd94e2865d61158c0be97e2169d69
        B/clauses/window-06/raw.json: 9c2425edc1278f283e35f557eab431e523b07f790eccc580a14d364dd6b85ff7
        B/clauses/window-06/prompt.txt: 6b2c19588abe06bd891426792661e34c563c3618c9d51ae2c9f02a3f35d1a788
        B/clauses/window-06/meta.json: 4a4d323e827a68fc120bb42163551535a9664bcae440881ab77aa9b38ba5be74
        B/tables/TABLE-1-page-4-1/raw.json: 3c0b50158d8bbf1804e94440382c5498533f524197e3df7e7c194f5047d5eca0
        B/tables/TABLE-1-page-4-1/prompt.txt: ebb5128e7dad37e43d29d7ec3ed08e49077d2283a278953ccb4a4d23be108aaf
        B/tables/TABLE-1-page-4-1/meta.json: 9c3ed8ee913eda23bbd5ab879aa4e5d4e61f3153e7f1f7ca838cb025863761ad
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
      pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010Anomia
      source_status_sha256: f67e4b6c60e9b69ceaad5c57959ced97a8581f530ea32bd90f83eacc711a73f1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: modulation of cortical areas in the left posterior and anterior hemisphere
    outcome:
      text: treatment-assisted increase in correct naming
    analysis_label: fMRI regression analysis
    relation: association
    evidence_ids:
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C9
    - P4-S2-C10
    - P4-S2-C11
    - P6-S1-C4
    qualifier_ids:
    - P3-S3-C8
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010Anomia
      source_status_sha256: f67e4b6c60e9b69ceaad5c57959ced97a8581f530ea32bd90f83eacc711a73f1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P3-S3-C2
      - Result passage disposed without unit P3-S3-C3
      - Result passage disposed without unit P3-S3-C4
      - Accounting without a linked unit P3-S3-C8
      - Result passage disposed without unit P4-S1-C1
      - Unaccounted source passage P3-S3-C8
      - Unaccounted source passage P3-S3-C2
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C4
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C7
      - Result passage disposed without unit P5-S1-C11
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C7
      - Result passage disposed without unit P5-S2-C2
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P5-S2-C3
      - Accounting without a linked unit P5-S3-C4
      - Accounting without a linked unit P5-S3-C5
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C9
      - Unaccounted source passage P5-S3-C4
      - Unaccounted source passage P5-S3-C5
      - Result passage disposed without unit P6-S3-C2
      - Result passage disposed without unit P6-S3-C3
      unattached_null_or_qualifier_ids:
      - P2-S3-C12
      - P4-S2-C7
      - P5-S2-C4
      - P5-S3-C4
      - P6-S1-C9
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 156
      unselected_timing_passages:
      - P1-S2-C9
      - P1-S2-C13
      - P1-S3-C4
      - P1-S3-C6
      - P2-S1-C14
      - P2-S2-C5
      - P3-S2-C13
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P2-S3-C3
        - P2-S3-C4
        - P2-S5-C3
        - P2-S5-C4
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C6
        - P4-S1-C9
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C13
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S2-C2
        - P5-S2-C3
        - P5-S3-C4
        - P5-S3-C5
        - P6-S1-C4
        - P6-S3-C2
        - P6-S3-C3
        - P6-S3-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P2-S2-C8
        - P2-S2-C10
        - P2-S3-C3
        - P2-S3-C4
        - P2-S3-C8
        - P2-S3-C9
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P3-S2-C7
        - P3-S2-C10
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C6
        - P4-S1-C9
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C13
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S2-C2
        - P5-S2-C3
        - P5-S3-C4
        - P5-S3-C5
        - P6-S1-C4
        - P6-S3-C2
        - P6-S3-C3
        - P6-S3-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010Anomia
      source_status_sha256: f67e4b6c60e9b69ceaad5c57959ced97a8581f530ea32bd90f83eacc711a73f1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes:
      - 1
      - 3
      reason: Reports association between left hemisphere activation and naming improvement,
        and negative effect of posterior temporal/occipital damage.
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies BAs 37 and 39 damage as negative for naming improvement.
    - source_id: P1-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variability in aphasia severity/type in the sample.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides a numerical example of data processing.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides a numerical example of data processing.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides a numerical example of data processing.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides a numerical example of data processing.
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes MRI scanning schedule.
    - source_id: P2-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes fMRI data collection timing.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Confirms all patients completed the study.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports statistically significant increase in correct naming post-treatment.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Notes variability in response to treatment.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia types of the top responders.
    - source_id: P3-S3-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Figure 2 showing brain areas where activation increase associated with
        naming increase.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: States patients responded similarly to semantic and phonological approaches.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports strong correlation between improvement from semantic and phonological
        hierarchies.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports positive relationship between naming increase and left hemisphere
        modulation.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifies that activation increase in specific areas predicts improvement.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports strong relationship between anterior and posterior cluster activation
        changes.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Explains the correlation between anterior and posterior cluster activation.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap in the left insula.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies BAs 37 and 39 as strongest lesion predictors of limited improvement.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Defines the lesion cluster including BAs 37, 39, and 19.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: States patients with damage to these regions were less likely to improve.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides descriptive counts of patients' scores relative to the mean.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Associates naming increase with left hemisphere activity (parietal/premotor/Broca's).
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifies the relationship between naming improvement and activation
        increase.
    - source_id: P4-S2-C13
      disposition: represented
      result_indexes:
      - 3
      reason: States damage to posterior left temporal/occipital regions has negative
        effect on naming.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Restates negative effect of posterior temporal/occipital damage when
        lesion size is factored out.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains fMRI signal in damaged areas.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 1
      - 3
      reason: Synthesizes that response relies on structural integrity (temporal/occipital)
        and recruitment (frontal/parietal).
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: States localized damage predicts treatment outcome.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: States patients with left temporal/occipital damage are less likely
        to benefit.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Links Figure 2 activation increase to improved response.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Provides mean naming improvement for patients with vs without posterior
        lesions.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant difference in naming improvement between the two
        lesion groups.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: States improved naming relied on increased brain activation in the left
        hemisphere.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the study's reliance on linguistic cues compared to other
        studies.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement about combining structural and functional MRI.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Restates that increase in left hemisphere network supports positive
        outcome.
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Restates that preservation of left temporal/occipital regions reflects
        improved naming.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about biomarkers.
    unresolved_coverage:
    - source_id: P5-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S3-C7
    - P2-S3-C5
    - P2-S3-C6
    - P2-S3-C7
    - P2-S3-C8
    - P2-S3-C12
    - P2-S4-C10
    - P3-S2-C13
    - P3-S3-C3
    - P3-S3-C4
    - P3-S3-C8
    - P4-S2-C2
    - P4-S2-C4
    - P4-S2-C7
    - P4-S2-C13
    - P4-S3-C7
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P6-S1-C9
    - P6-S2-C11
    - P6-S3-C2
    - P6-S3-C3
    - P6-S3-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C11
      - P4-S1-C12
      recruited_sample:
      - P1-S2-C9
      - P1-S3-C13
      eligibility:
      - P1-S3-C4
      imaging_provenance:
      - P3-S1-C3
      - P3-S1-C4
      - P4-S3-C9
      imaging_timing:
      - P2-S2-C11
      - P2-S3-C10
      - P2-S3-C13
      - P2-S3-C14
      - P2-S5-C2
      - P2-S5-C3
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P3-S2-C3
      - P3-S2-C4
      dependent_variable_statement:
      - P2-S5-C4
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C7
      limitations:
      - P5-S2-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S2-C13
      - P1-S2-C14
      - P1-S3-C10
      - P1-S3-C11
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S5-C3
      - P2-S5-C4
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C6
      - P4-S1-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C13
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C7
      - P4-S3-C8
      - P4-S3-C9
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C2
      - P5-S2-C3
      - P5-S3-C4
      - P5-S3-C5
      - P6-S1-C4
      - P6-S3-C2
      - P6-S3-C3
      - P6-S3-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P2-S2-C8
      - P2-S2-C10
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C8
      - P2-S3-C9
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C7
      - P3-S2-C10
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C6
      - P4-S1-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C13
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C7
      - P4-S3-C8
      - P4-S3-C9
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C2
      - P5-S2-C3
      - P5-S3-C4
      - P5-S3-C5
      - P6-S1-C4
      - P6-S3-C2
      - P6-S3-C3
      - P6-S3-C4
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
      pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
      review_sha256: 0634f8ea926f14200e076851e40d9bd05685b109f151c68e2f682ccf8e55c003
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
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C9
      - P4-S2-C10
      - P4-S2-C11
      - P6-S1-C4
      source_result: A positive association was detected between the magnitude of
        change in cortical activation (COPE) in left posterior and anterior hemisphere
        clusters and the standardized improvement in correct naming following treatment.
        Patients with greater activation increases in these regions showed greater
        naming improvement. This finding was based on a three-level fMRI analysis
        involving 19 of 26 patients.
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the primary fMRI outcome described
            in the source (P4-S1-C3, P4-S1-C4), which used a three-level regression
            analysis to predict naming change from cortical activation changes. The
            proposed core correctly identifies this as the primary fMRI result, distinct
            from the secondary structural MRI analysis.
          source_ids:
          - P4-S1-C3
          - P4-S1-C4
          - P2-S5-C4
          - P3-S1-C8
        direction:
          answer: fits
          reason: The source explicitly states a 'positive relationship' (P4-S1-C3)
            and that patients with increased activation were 'more likely to improve'
            (P4-S1-C4). The proposed core preserves this directionality (positive
            association between activation change and naming improvement).
          source_ids:
          - P4-S1-C3
          - P4-S1-C4
          - P4-S2-C10
        construct:
          answer: fits
          reason: The exposure is correctly identified as modulation of cortical areas
            in the left hemisphere (P4-S1-C3, P4-S2-C10). The outcome is treatment-assisted
            increase in correct naming (P4-S1-C3). The patient measurement is functional
            imaging (fMRI), specifically the change in activation (COPE maps), not
            lesion overlap or diffusion metrics. The proposed core correctly distinguishes
            this from the structural analysis.
          source_ids:
          - P4-S1-C3
          - P4-S2-C10
          - P3-S1-C7
          - P3-S1-C9
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that the fMRI
            analysis included 19 of 26 patients (P4-S1-C11) and that patients with
            fewer than five correct naming responses were excluded (P3-S2-C3, P4-S1-C12).
            It also notes the standardization of the outcome by intra-session variability
            (P2-S3-C4). These qualifiers are present and accurate.
          source_ids:
          - P4-S1-C11
          - P4-S1-C12
          - P3-S2-C3
          - P2-S3-C4
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes the limitation that the analysis did
            not deduce which specific areas are more important (P5-S2-C4). No other
            material caveats regarding the primary fMRI result appear to be omitted.
            The distinction between the primary fMRI result and the secondary structural
            result is maintained.
          source_ids:
          - P5-S2-C4
          - P4-S1-C13
      optional_pending:
      - Specific coordinates or Brodmann areas for the fMRI clusters are not transcribed
        in the core, but the source mentions BA 37/39 in the context of the structural
        analysis, not the fMRI clusters directly in the provided text snippets for
        the fMRI result itself (Table 1 is referenced but not transcribed).
      - Exact p-values and correlation coefficients for the fMRI regression are not
        transcribed in the core, though P4-S1-C9 mentions r(19)=0.90 for the relationship
        between anterior and posterior clusters, not the main regression against naming.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates or Brodmann areas for the fMRI clusters are not transcribed
      in the core, but the source mentions BA 37/39 in the context of the structural
      analysis, not the fMRI clusters directly in the provided text snippets for the
      fMRI result itself (Table 1 is referenced but not transcribed).
    - Exact p-values and correlation coefficients for the fMRI regression are not
      transcribed in the core, though P4-S1-C9 mentions r(19)=0.90 for the relationship
      between anterior and posterior clusters, not the main regression against naming.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R002
      exposure:
        text: modulation of cortical areas in the left posterior and anterior hemisphere
      outcome:
        text: treatment-assisted increase in correct naming
      analysis_label: fMRI regression analysis
      relation: association
      evidence_ids:
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C9
      - P4-S2-C10
      - P4-S2-C11
      - P6-S1-C4
      qualifier_ids:
      - P3-S3-C8
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010Anomia
        source_status_sha256: f67e4b6c60e9b69ceaad5c57959ced97a8581f530ea32bd90f83eacc711a73f1
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5cf9bc6ae5dca56233bc927f4432d8ca54fcbb1bb03bcd3ed801770daf375bb6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C9
          page: 4
          text_layer_sha256: 5cf9bc6ae5dca56233bc927f4432d8ca54fcbb1bb03bcd3ed801770daf375bb6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "A strong relationship\nwas revealed between changes in activation\
          \ in the anterior and\nposterior clusters listed in Table 1 (r(19) \x01\
          \ 0.90, p \x01 0.0001)."
        anchor_text: "A strong relationship\nwas revealed between changes in activation\
          \ in the anterior and\nposterior clusters listed in Table 1 (r(19) \x01\
          \ 0.90, p \x01 0.0001)."
        excluded_fragments: []
      P1-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 43c0fca79aa7be7b33a14cdae0c15929827c54af7f8c565aefb3dc2ad9cbb648
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C9
          page: 1
          text_layer_sha256: 43c0fca79aa7be7b33a14cdae0c15929827c54af7f8c565aefb3dc2ad9cbb648
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Twenty-six patients with left hemisphere

          stroke and chronic aphasia underwent fMRI twice before and

          twice after 2 weeks of intensive language treatment targeting ano-

          mia.'
        anchor_text: 'Twenty-six patients with left hemisphere

          stroke and chronic aphasia underwent fMRI twice before and

          twice after 2 weeks of intensive language treatment targeting ano-

          mia.'
        excluded_fragments: []
        image_sha256: ff3ce1ee4f93f75d5ade2111f5f86bf697e0b3b346187c24e191b41b3b7d0b63
        transcription: '. Twenty-six patients with left hemisphere

          stroke and chronic aphasia underwent fMRI twice before and

          twice after 2 weeks of intensive language treatment targeting ano-

          mia'
      P1-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f3d69ff572ae50530172170cb333b5fba0b50ba17565e2539542da3a769392e1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C4
          page: 1
          text_layer_sha256: f3d69ff572ae50530172170cb333b5fba0b50ba17565e2539542da3a769392e1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All

          had sustained a single event ischemic stroke to the left hemisphere at least

          8 months before study inclusion.'
        anchor_text: 'All

          had sustained a single event ischemic stroke to the left hemisphere at least

          8 months before study inclusion.'
        excluded_fragments: []
        image_sha256: 80ec572af0c072b2abd9cda985fd613c53c57a1134601f05a33c668b4afb419e
        transcription: '. All

          had sustained a single event ischemic stroke to the left hemisphere at least

          8 months before study inclusion'
      P4-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b7a57029078a0b0d56a92590143399bac0c63cc208a67a80a29d5ca2cad71650
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8cb650333e233ddc3df48d5136a603aa04cf2e27ffd573c63b1de83bdf89a69d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C11
          page: 4
          text_layer_sha256: 8cb650333e233ddc3df48d5136a603aa04cf2e27ffd573c63b1de83bdf89a69d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Data from

          19 of 26 patients were included in the fMRI analysis. fMRI data

          from one patient were excluded from the analysis due to excessive

          head motion.'
        anchor_text: 'Data from

          19 of 26 patients were included in the fMRI analysis. fMRI data

          from one patient were excluded from the analysis due to excessive

          head motion.'
        excluded_fragments: []
        image_sha256: a9a5c6c9e47d9324035ad1963e73d3a46a43336da96f62526b4fb704db05ebf5
        transcription: '. Data from

          19 of 26 patients were included in the fMRI analysis. fMRI data

          from one patient were excluded from the analysis due to excessive

          head motion'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Primary outcome: fMRI results

    A positive relationship was revealed between treatment-assisted

    increase in correct naming and modulation of cortical areas in the

    left posterior and anterior hemisphere (Fig. 2).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
