---
id: adaptive_semantic_matching_paradigm
name: adaptive semantic matching paradigm
kind: predictor
findings:
- id: f1
  target: language_region_mapping
  target_kind: impairment
  claim: The adaptive semantic matching paradigm is feasible for most individuals
    with aphasia and provides more reliable and valid maps of core perisylvian language
    regions (left inferior frontal and left posterior temporal cortex) than narrative
    comprehension or picture naming paradigms.
  direction: likely
  relationship: correlational
  method: fMRI_activation
  sample:
    n: not_reported
    population: individuals with chronic poststroke aphasia (n=16, spanning mild to
      severe) and neurologically normal participants (n=14)
    phase: not_reported
    time_post_onset: chronic poststroke phase; test-retest sessions typically a few
      weeks apart
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Validity was assessed primarily in neurologically normal participants
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A functional MRI language mapping task using an adaptive
    staircase procedure to manipulate linguistic factors (frequency, concreteness,
    age of acquisition, length, and phonological complexity) and presentation rate
    to match individual performance, contrasting semantic matching of word pairs with
    a perceptual symbol-matching control task. One severely impaired patient exhibited
    a floor effect with 59% accuracy, though this remained significantly above chance;
    Reliability was quantified by the Dice coefficient of similarity between two scanning
    sessions. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P5-S1-C8, two-model agreement, human
    verification pending): We assessed the feasibility, reliability, and validity

    of the adaptive semantic matching paradigm in 16 individ-

    uals with chronic poststroke aphasia and 14 neurologically

    normal participants Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:language_region_mapping
  citation: '@Wilson2019'
  source_passages:
  - section: Original source P1-S1-C12
    page: 1
    quote: 'Results: We found that the adaptive semantic matching

      paradigm could be performed by most individuals with aphasia

      and yielded reliable and valid maps of core perisylvian language

      regions in each individual participant.'
    supports: claim
  - section: Original source P5-S1-C13
    page: 5
    quote: 'We found that all 16 individuals with aphasia were

      able to learn the tasks and performed above chance on

      both the language and control conditions.'
    supports: claim
  - section: Original source P5-S2-C8
    page: 5
    quote: 'It can be appreciated that test–retest reproducibility was

      good, and interestingly, in most patients (with the notable

      exception of A12), language processing continued to be

      left lateralized.'
    supports: claim
  - section: Original source P5-S2-C10
    page: 5
    quote: 'The mean Dice coefficient of similarity, quantifying

      test–retest reproducibility of the semantic paradigm across

      the two scanning sessions, was .66 ± .15 (range: .40–.82),

      which significantly exceeded the reliability of the narrative

      comprehension (Dice coefficient = .47) and picture naming

      (Dice coefficient = .43) paradigms.'
    supports: claim
  - section: Original source P5-S3-C4
    page: 5
    quote: 'The adaptive

      semantic matching paradigm robustly demonstrated these

      three known features of normal language organization in

      the control group.'
    supports: claim
  - section: Original source P5-S3-C7
    page: 5
    quote: 'In sum, this study showed the adaptive semantic

      matching paradigm is a feasible, reliable, and valid method

      for mapping language regions in people with aphasia.'
    supports: claim
  - section: Original source P5-S3-C8
    page: 5
    quote: 'In

      particular, the core language regions in the left inferior

      frontal cortex and left posterior temporal cortex were con-

      sistently and reliably identified.'
    supports: claim
  - section: Original source P5-S1-C8
    page: 5
    quote: 'We assessed the feasibility, reliability, and validity

      of the adaptive semantic matching paradigm in 16 individ-

      uals with chronic poststroke aphasia and 14 neurologically

      normal participants.'
    supports: sample
  - section: Original source P5-S1-C9
    page: 5
    quote: 'The participants with aphasia were

      mostly recruited from an outpatient aphasia center and

      spanned a range of severities, approximately evenly distrib-

      uted across mild, moderate, and severe aphasias, charac-

      terized with the Quick Aphasia Battery (Wilson, Eriksson,

      Schneck, & Lucanie, 2018).'
    supports: sample
  - section: Original source P5-S1-C10
    page: 5
    quote: 'The patients were scanned with

      functional MRI on two separate occasions, typically a few

      weeks apart, to quantify test–retest reliability.'
    supports: method
  - section: Original source P4-S1-C10
    page: 4
    quote: 'Therefore, we created a task that

      would be adaptive to each individual’s performance.'
    supports: method
  - section: Original source P4-S1-C15
    page: 4
    quote: 'We use an adaptive staircase procedure and

      control difficulty by simultaneously manipulating a num-

      ber of linguistic factors—frequency, concreteness, age of

      acquisition, length, and phonological complexity—and

      presentation rate.'
    supports: method
  - section: Original source P5-S2-C4
    page: 5
    quote: 'The remaining patient, who was the most

      severely impaired patient in the group, performed with

      59% accuracy, reflecting a floor effect (i.e., the staircase

      procedure called for easier trials than were available to

      present).'
    supports: confounders
predictor_type: imaging_metric
short_definition: A functional MRI language mapping task using an adaptive staircase
  procedure to manipulate linguistic factors (frequency, concreteness, age of acquisition,
  length, and phonological complexity) and presentation rate to match individual performance,
  contrasting semantic matching of word pairs with a perceptual symbol-matching control
  task.
assessment:
- fMRI
- Dice coefficient
- Quick Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Wilson2019
  proposal_id: R002
  review_status_sha256: f2017de538824dd93cf54f5aef9b90d209b1df0d621fbaf3092fef5bab128c9b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
        A/passages.json: c3ed59cdae4ce44e02af259ce53597390b6a5a9d4be4b38b8fcf4b9d3426f8ed
        A/raw.json: a5732c592ca67558e6fe60267a3659fbdce20b5fda676e36e9baaa98c8b3fea5
        A/source-units.json: 1b531c7c279eb463c3c4a8d12ebec0de0c3b76ed05c7ba61b3534ceaa4446a81
        A/full-source-units.json: 4c88a9af84a82509ee2e44278f1262a7fc98f7a5346f81cdb97478fe7112f3b3
        A/meta.json: 388662a8a1a67aa85d79ed72a6be4c8c1cccfbad81afd4b4675d2005ab9763f6
        A/table-images/manifest.json: 8ddc4ec75a9bd70663b5a4460c0c3126efae586b1c1f8b49a057883592dd1a35
        A/clauses/window-03/raw.json: c3c21ec53741fe2acc61f17ab76a754a77a982e7180b403def828ca3c6ee713d
        A/clauses/window-03/prompt.txt: 7c4ddbc6c1f44d2c8deab4a078b6cf3e20530704e658153a8529bbf5afbea294
        A/clauses/window-03/meta.json: 9b7beb90adaec8a910b6280861f562ef79ee686b52d7c2eeb45c308cf5e67465
        A/clauses/window-04/raw.json: 89f31fe1944668af33c75aaf608e557228216c94ba9fed0d44153e63e18b4e94
        A/clauses/window-04/prompt.txt: fcebdd7ed51e2577c4085a727e9f02eb51bbc1247c6e3aa1f6bcf15e09ddd038
        A/clauses/window-04/meta.json: 4ab4a90d1206781ff6f8250532b1b3a7e5f074dc281565a3da890e9267823a1d
        A/clauses/window-05/raw.json: 2d118aaac69574b245fa545c401d9b5c236c00d2b9f2707f19c162e9de1b1ea0
        A/clauses/window-05/prompt.txt: 7a290f1c3a6fb8fb629ce36179361676e272f91a7cec84e784ea9b87f184cbbe
        A/clauses/window-05/meta.json: 32a8cae2484dcdb6a33ca8abb00089c09d24b003c885b59c6c1eb06de05c0b25
        A/clauses/window-02/raw.json: ac63a9ae7561846aa4ff9891eea5eebd354e5f205c194a698a873e8fa9c9f637
        A/clauses/window-02/prompt.txt: 0871550fcaab8583b0027a5a060a5038a7d39268100fe177557643c8cc7a6a70
        A/clauses/window-02/meta.json: b41d5b21162728479d03315085da5a1c8a0668d0ca576c58ccca25bbb5676d85
        A/clauses/window-09/raw.json: 9989312c845b46d39d350db84c49d854dd8b2ee2d1c7f39f7dfdf841a3e31acf
        A/clauses/window-09/prompt.txt: f67c3fcd9dd60ef4ebadb593fdc3390f6486f6186021f9c7c5fd9dae97f9ff1c
        A/clauses/window-09/meta.json: a8fda03482b90884a4c2d60c9e2bf63030d784cfb8268cac322388550e199c62
        A/clauses/window-07/raw.json: a112e2592de6381d731f81788dada414fbc09b8ff2ff18d1afa483d7cb0b98cb
        A/clauses/window-07/prompt.txt: 5a514cd21177067958185bb1f046dfbdfc90735b73547546dfb45242a2de7a3d
        A/clauses/window-07/meta.json: 0657d277251239eb2a2937b28cc78f232a9c3a185758a2c1b724db14c5f57d77
        A/clauses/window-01/raw.json: 96bf17d5fb2c3fabd52e06ff8c56365124fd9827bbdc83010b5bb09b2f616676
        A/clauses/window-01/prompt.txt: 9328990c899f8990f87bc131909afce5056ce2dc6d8a781e22e4f7f2bbb0152d
        A/clauses/window-01/meta.json: f5a03f0069d0bca55c4b0262615c8f0456b2ce3be0d387fb56d5293af40e9421
        A/clauses/window-06/raw.json: 6cdc22cdb6de5395258d95d6ebba1cc8a9b4a4cfdfe84622f8bc3f176408d5a1
        A/clauses/window-06/prompt.txt: db31bb3dbd240addb6b6de9d47b1f2ecb81ffb40b6fc51c2f588ad51c0375d72
        A/clauses/window-06/meta.json: cd46ec1f2d671efd5ae6ccde5be9ee6edc15ef2499e81ad6f67ddc5b59fa8940
        A/clauses/window-08/raw.json: 68ab54ca396d4547a2dd665f2d8136931f9484c2e4553805a99d0ab617ae6c3c
        A/clauses/window-08/prompt.txt: 04eca9e910274c81f9b3985ea90c23c5282fa34e6e31bd5b9c024b9bb3b1de20
        A/clauses/window-08/meta.json: f714441b788e7b76cc7fd95b9d14105c835903fa6a09c1e71c3355141a101ba3
        B/passages.json: c3ed59cdae4ce44e02af259ce53597390b6a5a9d4be4b38b8fcf4b9d3426f8ed
        B/raw.json: ccee4f7a10879e65afb788c0abe2ebf61048fb091136118669d915cc2640725c
        B/source-units.json: 1b531c7c279eb463c3c4a8d12ebec0de0c3b76ed05c7ba61b3534ceaa4446a81
        B/full-source-units.json: 4c88a9af84a82509ee2e44278f1262a7fc98f7a5346f81cdb97478fe7112f3b3
        B/meta.json: 59b3c0e34a9a5b435b19ebb703964fa04b5b9120d187f9377851eb9d5d835ae2
        B/table-images/manifest.json: 8ddc4ec75a9bd70663b5a4460c0c3126efae586b1c1f8b49a057883592dd1a35
        B/clauses/window-03/raw.json: a1355402dcb134ecb7496765e501a564f555182994d803c3b49ee39c5946c45d
        B/clauses/window-03/prompt.txt: 7c4ddbc6c1f44d2c8deab4a078b6cf3e20530704e658153a8529bbf5afbea294
        B/clauses/window-03/meta.json: 4402309a8ef02bfd5c9535f330554236880cd02acbcb61c9558018f4cb60f2e9
        B/clauses/window-04/raw.json: a49440057a83ed36e4778de874276ae0b2f94dcc4963f794b60e07f304f7611a
        B/clauses/window-04/prompt.txt: fcebdd7ed51e2577c4085a727e9f02eb51bbc1247c6e3aa1f6bcf15e09ddd038
        B/clauses/window-04/meta.json: 307127a4d85c56e69770a9d56abe2783b8553a9c12525abf8098311a167c5733
        B/clauses/window-05/raw.json: 12e078df4e22ed2742562035c529c7ea471b7138af0161c44b335acc1e36b5c8
        B/clauses/window-05/prompt.txt: 7a290f1c3a6fb8fb629ce36179361676e272f91a7cec84e784ea9b87f184cbbe
        B/clauses/window-05/meta.json: 55d29c5df5631b4c6e3b5d69dc6ddf52ec500482aa4b1f18b043ac883deaf18a
        B/clauses/window-02/raw.json: 5a0f5b83275c7e0fbb886cac424789b4683d05d0018797bda09f1bcfeda87b1f
        B/clauses/window-02/prompt.txt: 0871550fcaab8583b0027a5a060a5038a7d39268100fe177557643c8cc7a6a70
        B/clauses/window-02/meta.json: 7aa071e92bffa275f3e7c94eb8620495c45adf9b2503abe336562e7b247b0d5c
        B/clauses/window-09/raw.json: 9989312c845b46d39d350db84c49d854dd8b2ee2d1c7f39f7dfdf841a3e31acf
        B/clauses/window-09/prompt.txt: f67c3fcd9dd60ef4ebadb593fdc3390f6486f6186021f9c7c5fd9dae97f9ff1c
        B/clauses/window-09/meta.json: a7de9c83d2de52bb1673b81fc22afe0100528b5cd6b97b80351568c1b75b0ce2
        B/clauses/window-07/raw.json: 07134bfbfeca4d293d1485929b5f96a45bc05997406b085e3bbee890b44ae4d7
        B/clauses/window-07/prompt.txt: 5a514cd21177067958185bb1f046dfbdfc90735b73547546dfb45242a2de7a3d
        B/clauses/window-07/meta.json: ce03a6ed68746f074873dc10895310b98164d07dfc359337f2a1a5f15031093e
        B/clauses/window-01/raw.json: 95060124c0caecbb3e9b3e396a6c3b79c4ec2b4f3fc59db095bf2523368b5e0a
        B/clauses/window-01/prompt.txt: 9328990c899f8990f87bc131909afce5056ce2dc6d8a781e22e4f7f2bbb0152d
        B/clauses/window-01/meta.json: d9d2ac62723cb574128cc7685898597eeab379804c509c8061b71256bb90a184
        B/clauses/window-06/raw.json: 6f9f027bea6e7d926c58307a4fedba61769008cf525d0606543d8431c8ae6b6b
        B/clauses/window-06/prompt.txt: db31bb3dbd240addb6b6de9d47b1f2ecb81ffb40b6fc51c2f588ad51c0375d72
        B/clauses/window-06/meta.json: 0939e1a46adb8290cfcabc78bc61ab2d3c7bde30262f1181e0eb8130ac85142d
        B/clauses/window-08/raw.json: 1abb243da09b42e26f15733ee806214e39e9a45f51b5601e7d3c55f00ed8e3a5
        B/clauses/window-08/prompt.txt: 04eca9e910274c81f9b3985ea90c23c5282fa34e6e31bd5b9c024b9bb3b1de20
        B/clauses/window-08/meta.json: 007a82adf916e6cfe16f2db028682609c8557da038b37ec93062a1873ac0f2dd
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2019
      source_status_sha256: 897543ddfa52603e249f85ef4a5137f3fde58f7fcf37bab059cfeda2a1ed7fbf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: adaptive semantic matching paradigm
    outcome:
      text: task performance, test-retest reproducibility (Dice coefficient), and
        validity (lateralization and localization)
    analysis_label: Feasibility, reliability, and validity of adaptive semantic matching
      paradigm
    relation: association
    evidence_ids:
    - P1-S1-C12
    - P5-S1-C13
    - P5-S2-C8
    - P5-S2-C10
    - P5-S3-C4
    - P5-S3-C7
    - P5-S3-C8
    qualifier_ids:
    - P5-S1-C8
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2019
      source_status_sha256: 897543ddfa52603e249f85ef4a5137f3fde58f7fcf37bab059cfeda2a1ed7fbf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S1-C11
      - Result passage disposed without unit P2-S1-C12
      - Result passage disposed without unit P2-S1-C13
      - Result passage disposed without unit P2-S1-C14
      - Result passage disposed without unit P2-S1-C15
      - Result passage disposed without unit P2-S1-C16
      - Result passage disposed without unit P2-S1-C17
      - Result passage disposed without unit P2-S1-C19
      - Result passage disposed without unit P2-S3-C14
      - Result passage disposed without unit P2-S3-C15
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P3-S3-C2
      - Accounting without a linked unit P3-S3-C3
      - Unaccounted source passage P3-S3-C3
      - Accounting without a linked unit P3-S3-C6
      - Accounting without a linked unit P3-S3-C7
      - Unaccounted source passage P3-S3-C6
      - Unaccounted source passage P3-S3-C7
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C6
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C5
      - Unaccounted source passage P5-S2-C6
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P5-S2-C9
      - Result passage disposed without unit P5-S3-C7
      - Accounting without a linked unit P7-S1-C13
      - Accounting without a linked unit P7-S1-C14
      - Result passage disposed without unit P7-S2-C1
      - Unaccounted source passage P7-S1-C13
      - Unaccounted source passage P7-S1-C14
      - Result passage disposed without unit P7-S2-C13
      - Accounting without a linked unit P7-S2-C3
      - Result passage disposed without unit P7-S2-C7
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P7-S2-C14
      - Result passage disposed without unit P7-S2-C15
      - Result passage disposed without unit P7-S2-C16
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P8-S1-C15
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C5
      - Unaccounted source passage P8-S2-C12
      unattached_null_or_qualifier_ids:
      - P2-S1-C19
      - P5-S2-C5
      - P5-S2-C9
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 163
      unselected_timing_passages:
      - P5-S1-C8
      - P8-S1-C6
      - P8-S1-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P8-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P1-S1-C11
        - P1-S1-C12
        - P2-S3-C4
        - P3-S1-C1
        - P3-S2-C3
        - P5-S1-C8
        - P6-S1-C3
        - P6-S1-C4
        - P7-S1-C9
        - P7-S2-C13
        - P7-S2-C16
        - P8-S1-C1
        - P8-S1-C11
        - P8-S1-C13
        - P8-S2-C7
        - P8-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P1-S1-C11
        - P2-S2-C4
        - P3-S2-C3
        - P5-S1-C8
        - P5-S1-C9
        - P6-S1-C3
        - P6-S1-C4
        - P7-S1-C9
        - P8-S1-C6
        - P8-S1-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P3-S2-C3
        - P5-S1-C9
        - P7-S1-C9
        - P8-S1-C6
        - P8-S1-C13
        - P8-S1-C14
        - P8-S1-C15
        - P8-S2-C4
        - P8-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C12
        - P1-S1-C14
        - P2-S2-C8
        - P5-S1-C10
        - P6-S1-C2
        - P7-S1-C10
        - P7-S3-C2
        - P8-S1-C7
        - P8-S3-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S2-C4
        - P2-S2-C5
        - P2-S2-C10
        - P2-S2-C11
        - P2-S2-C12
        - P2-S3-C9
        - P2-S3-C10
        - P3-S2-C10
        - P3-S2-C12
        - P3-S2-C13
        - P3-S2-C14
        - P3-S3-C1
        - P3-S3-C2
        - P7-S1-C11
        - P7-S1-C12
        - P8-S1-C4
        - P8-S1-C15
        - P8-S2-C4
        - P8-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P2-S3-C14
        - P3-S2-C3
        - P3-S2-C4
        - P4-S1-C17
        - P5-S1-C9
        - P6-S1-C3
        - P6-S1-C4
        - P7-S1-C9
        - P8-S1-C6
        - P8-S2-C4
        - P8-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - eligibility
      - imaging_provenance
      - dependent_variable_statement
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S1
        - P2-S3
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S2
        - P7-S3
        - P8-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2019
      source_status_sha256: 897543ddfa52603e249f85ef4a5137f3fde58f7fcf37bab059cfeda2a1ed7fbf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: States adaptive semantic matching paradigm was feasible and yielded
        reliable/valid maps.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Compares psychometric properties of adaptive semantic matching to other
        paradigms.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: States adaptive rhyme judgment identified fronto-parietal regions.
    - source_id: P2-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual patient history.
    - source_id: P2-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient speech sample.
    - source_id: P2-S1-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient's clinical state.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes structural damage in Mr. L.
    - source_id: P2-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Mr. L's recovery.
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: States four paradigms lacked reliability and validity.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Figure 2.
    - source_id: P3-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports poor to fair test-retest reproducibility.
    - source_id: P3-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Reports striking differences in maps between sessions.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: States validity was limited.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific lateralization of narrative comprehension.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lateralization of other paradigms.
    - source_id: P3-S3-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States none of the four paradigms consistently activated critical regions.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion about the four paradigms.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Reports all 16 individuals with aphasia performed above chance.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports accuracy range for 15 of 16 patients.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports accuracy for the most severely impaired patient.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports accuracy was better than chance.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports performance on control condition.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports good test-retest reproducibility.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes activation of frontal and temporal areas.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Provides mean Dice coefficient and compares it to other paradigms.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: States paradigm demonstrated three known features of normal organization.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Compares lateralization of narrative and picture naming paradigms.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Compares activation of frontal and temporal regions.
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Conclusion on feasibility, reliability, and validity.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports consistent identification of core language regions.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Compares reliability of rhyme judgment and syllable counting.
    - source_id: P7-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Reports activation of supramarginal and ventral precentral gyri.
    - source_id: P7-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Repeats activation of phonological encoding regions.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports activation in the majority of individual participants.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Compares lateralization of rhyme judgment vs syllable counting.
    - source_id: P7-S2-C13
      disposition: represented
      result_indexes:
      - 5
      reason: States Mr. L performed both tasks.
    - source_id: P7-S2-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Reports lack of left frontal activations in Mr. L.
    - source_id: P7-S2-C15
      disposition: represented
      result_indexes:
      - 5
      reason: Reports destruction of Mr. L's left frontal language areas.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Reports specific atypical activations in Mr. L.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 6
      reason: Reports 89% of patients performed adaptive semantic matching above chance.
    - source_id: P8-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports 77% of patients performed adaptive rhyme judgment.
    - source_id: P8-S2-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Conclusion on feasibility of both paradigms.
    unresolved_coverage:
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S1-C10
    - P2-S1-C11
    - P2-S1-C12
    - P2-S1-C13
    - P2-S1-C14
    - P2-S1-C15
    - P2-S1-C16
    - P2-S1-C17
    - P2-S1-C19
    - P2-S3-C14
    - P2-S3-C15
    - P3-S2-C11
    - P3-S2-C13
    - P3-S3-C3
    - P3-S3-C5
    - P3-S3-C7
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C9
    - P7-S2-C1
    - P7-S2-C7
    - P7-S2-C13
    - P7-S2-C14
    - P7-S2-C15
    - P7-S2-C16
    - P7-S3-C3
    - P8-S1-C14
    - P8-S1-C15
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C10
    - P8-S2-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility: []
      imaging_provenance: []
      imaging_timing:
      - P3-S2-C4
      - P5-S1-C10
      - P6-S1-C7
      - P7-S1-C10
      - P8-S1-C7
      - P8-S1-C9
      outcome_timing:
      - P5-S1-C10
      - P6-S1-C7
      - P7-S1-C10
      - P8-S1-C8
      - P8-S2-C10
      outcome_definition:
      - P1-S1-C12
      - P1-S1-C14
      - P5-S2-C10
      - P6-S1-C2
      - P7-S1-C13
      - P7-S2-C3
      - P8-S1-C13
      - P8-S2-C9
      validation:
      - P1-S1-C8
      analysis_restrictions:
      - P6-S1-C5
      dependent_variable_statement: []
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P7-S1-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P8-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P1-S1-C11
      - P1-S1-C12
      - P2-S3-C4
      - P3-S1-C1
      - P3-S2-C3
      - P5-S1-C8
      - P6-S1-C3
      - P6-S1-C4
      - P7-S1-C9
      - P7-S2-C13
      - P7-S2-C16
      - P8-S1-C1
      - P8-S1-C11
      - P8-S1-C13
      - P8-S2-C7
      - P8-S2-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P1-S1-C11
      - P2-S2-C4
      - P3-S2-C3
      - P5-S1-C8
      - P5-S1-C9
      - P6-S1-C3
      - P6-S1-C4
      - P7-S1-C9
      - P8-S1-C6
      - P8-S1-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P3-S2-C3
      - P5-S1-C9
      - P7-S1-C9
      - P8-S1-C6
      - P8-S1-C13
      - P8-S1-C14
      - P8-S1-C15
      - P8-S2-C4
      - P8-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C12
      - P1-S1-C14
      - P2-S2-C8
      - P5-S1-C10
      - P6-S1-C2
      - P7-S1-C10
      - P7-S3-C2
      - P8-S1-C7
      - P8-S3-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C10
      - P2-S2-C11
      - P2-S2-C12
      - P2-S3-C9
      - P2-S3-C10
      - P3-S2-C10
      - P3-S2-C12
      - P3-S2-C13
      - P3-S2-C14
      - P3-S3-C1
      - P3-S3-C2
      - P7-S1-C11
      - P7-S1-C12
      - P8-S1-C4
      - P8-S1-C15
      - P8-S2-C4
      - P8-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P2-S3-C14
      - P3-S2-C3
      - P3-S2-C4
      - P4-S1-C17
      - P5-S1-C9
      - P6-S1-C3
      - P6-S1-C4
      - P7-S1-C9
      - P8-S1-C6
      - P8-S2-C4
      - P8-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
      review_sha256: f2017de538824dd93cf54f5aef9b90d209b1df0d621fbaf3092fef5bab128c9b
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
      - P1-S1-C12
      - P5-S1-C13
      - P5-S2-C10
      - P5-S2-C8
      - P5-S3-C4
      - P5-S3-C7
      - P5-S3-C8
      source_result: The adaptive semantic matching paradigm was feasible for 16 individuals
        with chronic poststroke aphasia (all performed above chance, with one severe
        case showing a floor effect but still above chance). It demonstrated good
        test-retest reliability (mean Dice coefficient .66, significantly higher than
        narrative comprehension and picture naming) and validity in neurologically
        normal participants (robustly demonstrating left lateralization and activation
        of left inferior frontal and posterior temporal regions).
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the study of the adaptive
            semantic matching paradigm's feasibility, reliability, and validity. The
            source confirms this was the second study reviewed (Wilson, Yen, & Eriksson,
            2018), involving 16 aphasia patients and 14 controls.
          source_ids:
          - P1-S1-C10
          - P5-S1-C8
          - P5-S3-C7
        direction:
          answer: fits
          reason: The claim that the paradigm is feasible, reliable, and valid aligns
            with the source findings. The source explicitly states the paradigm yielded
            reliable and valid maps and had superior psychometric properties compared
            to other paradigms.
          source_ids:
          - P1-S1-C12
          - P1-S1-C13
          - P5-S3-C7
        construct:
          answer: fits
          reason: The exposure is the adaptive semantic matching paradigm. The outcome
            is task performance (feasibility), test-retest reproducibility (reliability
            via Dice coefficient), and validity (lateralization/localization). The
            patient measurement is functional imaging (fMRI activation maps), not
            lesion overlap or diffusion tractography. The source confirms fMRI was
            used to identify language regions.
          source_ids:
          - P2-S2-C8
          - P5-S1-C8
          - P5-S2-C10
          - P5-S3-C3
        qualifications:
          answer: fits
          reason: The draft includes the qualification that validity was assessed
            primarily in neurologically normal participants, which is a material caveat
            found in the source (P5-S1-C11, P5-S3-C3). It also notes the floor effect
            for one patient, which is accurate.
          source_ids:
          - P5-S1-C11
          - P5-S3-C3
          - P5-S2-C4
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly limits the
            validity claim to the control group and notes the feasibility exception
            for the most severe patient. The source does not present conflicting results
            that would require a 'conflict' status.
          source_ids:
          - P5-S1-C11
          - P5-S3-C3
      optional_pending:
      - Specific Dice coefficient values for individual patients are not transcribed,
        only the mean and range.
      - Exact anatomical coordinates of the identified regions are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific Dice coefficient values for individual patients are not transcribed,
      only the mean and range.
    - Exact anatomical coordinates of the identified regions are not transcribed.
    normalizations:
    - field: sample.n
      original: 30
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R002
      exposure:
        text: adaptive semantic matching paradigm
      outcome:
        text: task performance, test-retest reproducibility (Dice coefficient), and
          validity (lateralization and localization)
      analysis_label: Feasibility, reliability, and validity of adaptive semantic
        matching paradigm
      relation: association
      evidence_ids:
      - P1-S1-C12
      - P5-S1-C13
      - P5-S2-C8
      - P5-S2-C10
      - P5-S3-C4
      - P5-S3-C7
      - P5-S3-C8
      qualifier_ids:
      - P5-S1-C8
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
        source_review: _compare/relationships-2026-11-16/review-current/Wilson2019
        source_status_sha256: 897543ddfa52603e249f85ef4a5137f3fde58f7fcf37bab059cfeda2a1ed7fbf
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a366bb7a8f73cd498254f43eb2c149fbb2be81ab275f883ff816020b407fb6e5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C8
          page: 5
          text_layer_sha256: a366bb7a8f73cd498254f43eb2c149fbb2be81ab275f883ff816020b407fb6e5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We assessed the feasibility, reliability, and validity

          of the adaptive semantic matching paradigm in 16 individ-

          uals with chronic poststroke aphasia and 14 neurologically

          normal participants.'
        anchor_text: 'We assessed the feasibility, reliability, and validity

          of the adaptive semantic matching paradigm in 16 individ-

          uals with chronic poststroke aphasia and 14 neurologically

          normal participants.'
        excluded_fragments: []
        image_sha256: 2597f5f9a2ff612a75847f237d197f9ee410ba031adc5a29be5839ce4cb40ae2
        transcription: 'We assessed the feasibility, reliability, and validity

          of the adaptive semantic matching paradigm in 16 individ-

          uals with chronic poststroke aphasia and 14 neurologically

          normal participants'
      P5-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 64a85a4f2681f70fc59d5da1b107376747efc8981528915272ec6635f0035f9e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 969fbd6c1dd0151f9eb34ad8ee1d06caa04d2d2f8e0b497a5a69fb78ae81a4d3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C9
          page: 5
          text_layer_sha256: 969fbd6c1dd0151f9eb34ad8ee1d06caa04d2d2f8e0b497a5a69fb78ae81a4d3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The participants with aphasia were

          mostly recruited from an outpatient aphasia center and

          spanned a range of severities, approximately evenly distrib-

          uted across mild, moderate, and severe aphasias, charac-

          terized with the Quick Aphasia Battery (Wilson, Eriksson,

          Schneck, & Lucanie, 2018).'
        anchor_text: 'The participants with aphasia were

          mostly recruited from an outpatient aphasia center and

          spanned a range of severities, approximately evenly distrib-

          uted across mild, moderate, and severe aphasias, charac-

          terized with the Quick Aphasia Battery (Wilson, Eriksson,

          Schneck, & Lucanie, 2018).'
        excluded_fragments: []
        image_sha256: 948a238b9ee0b261f0a573dcab83591e6fa456d91ef11513916723fffe3645b1
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Results: We found that the adaptive semantic matching

    paradigm could be performed by most individuals with aphasia

    and yielded reliable and valid maps of core perisylvian language

    regions in each individual participant.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
