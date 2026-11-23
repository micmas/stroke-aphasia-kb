---
id: brocas_area
name: Broca's area cluster
kind: network
findings:
- id: f1
  target: speech_repetition_impairment
  target_kind: impairment
  claim: Structural damage in Broca's area is associated with impaired speech repetition.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 39
    population: Acute ischemic stroke patients with single left-hemisphere events
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
  - The study did not specifically examine the relationship between localized damage
    and the clinical diagnosis of conduction aphasia
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a voxel-wise structural
    lesion map (DWI) analyzed via logistic regression. Analysis controlled for auditory
    comprehension performance as a cofactor; The sample included patients with various
    aphasia types and those without aphasia, meaning repetition deficits may have
    been due to factors other than primary repetition impairment (e.g., apraxia of
    speech or nonfluent aphasia). Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S1-C4, two-model
    agreement, human verification pending): . Therefore, data from 39

    patients were included in the final statistical analyses described below Original
    text-layer quotation is preserved below. PDF image reading (P2-S1-C6, two-model
    agreement, human verification pending): . For most

    participants, behavioral and MRI examination were completed within

    3 d of hospital admission, but in a few cases participants were examined

    as late as 20 d following stroke due to factors such as fatigue or other

    stroke sequelae Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:speech_repetition_impairment
  citation: '@Fridriksson2010'
  source_passages:
  - section: Original source P3-S1-C5
    page: 3
    quote: "Additional structural damage associated with impaired\nspeech repetition\
      \ was noted in Broca’s area (\x0341, 36, 10)."
    supports: claim
  - section: Original source P2-S3-C4
    page: 2
    quote: 'The DWI lesion data consisted of binary

      voxelwise maps (lesion versus nonlesioned) and were submitted to vox-

      elwise lesion–behavior mapping (VLBM) (Bates et al., 2003).'
    supports: method
  - section: Original source P2-S3-C5
    page: 2
    quote: 'VLBM was

      performed using NPM (nonparametric mapping) (Rorden et al., 2007)

      (a software package available from www.mricro.com), via a voxel-by-

      voxel logistic regression.'
    supports: method
  - section: Original source P2-S3-C9
    page: 2
    quote: 'Spe-

      cifically, an independent Z-score was computed for each voxel,

      computing whether speech repetition performance was correlated with

      injury to that voxel, using the level of auditory comprehension perfor-

      mance as a regressor.'
    supports: method
  - section: Original source P2-S1-C12
    page: 2
    quote: 'The BEST-2’s Repetition

      subtest served to quantify the severity of repetition impairment.'
    supports: claim
  - section: Original source P2-S1-C4
    page: 2
    quote: 'Therefore, data from 39

      patients were included in the final statistical analyses described below.'
    supports: sample
  - section: Original source P2-S1-C6
    page: 2
    quote: 'For most

      participants, behavioral and MRI examination were completed within

      3 d of hospital admission, but in a few cases participants were examined

      as late as 20 d following stroke due to factors such as fatigue or other

      stroke sequelae.'
    supports: sample
  - section: Original source P2-S1-C7
    page: 2
    quote: "Behavioral and MRI examinations were always com-\npleted with \x0224 h\
      \ separating them."
    supports: sample
  - section: Original source P1-S3-C11
    page: 1
    quote: 'All participants had incurred a single event ischemic stroke

      to the left hemisphere and provided informed consent for study inclu-

      Received March 4, 2010; revised June 25, 2010; accepted July 6, 2010.'
    supports: sample
  - section: Original source P4-S2-C5
    page: 4
    quote: 'It is important to point out that the present study did not

      examine a direct relationship between localized brain damage

      and conduction aphasia, an aphasic disorder marked by a distinct

      impairment in speech repetition with relatively spared language

      comprehension and speech production.'
    supports: limitation
  - section: Original source P4-S2-C7
    page: 4
    quote: 'Thus, the study sample in-

      cluded some patients who had difficulty repeating due to factors

      such as apraxia of speech, nonfluent aphasia, or auditory com-

      prehension impairment rather than the primary repetition im-

      pairment seen in conduction aphasia.'
    supports: confounders
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2010
  proposal_id: R002
  review_status_sha256: de4fed9c6c3d71630dc733bd13bf69db2b17c6d8089daa006f88d3f4bcf1eb46
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
        A/passages.json: 74694dbe00089b1aceca815d32075af3eae413c27e5b2e204fc50e143431e4e5
        A/raw.json: e3f70aefb44d9d43f1435390a004e04f78c83454baaef3a7200f03a68e03afd5
        A/source-units.json: d3e784c5255aaf5f48e1f4f1dbac1e5e703d096e130a2565e0d7f7111f9b51f0
        A/full-source-units.json: fa20376b389cd295d77740fb1d533b2c64bfbbb70b9da01a1a0f51875eb1aba9
        A/meta.json: 0e35a25710d8ce276b6e8d31c37e5249d6ffe6edbd18c7bdff6e59dab044910c
        A/table-images/TABLE-1-page-2-1.png: 48f43d3a4dfecf2d83b7b0f71d8d8de47e79e24747a4229fe6f270ad68ce858f
        A/table-images/page-2.png: 79d41faff4fffaacba1977f6b508d4d4eb234a3aa4bbf15fc9cdfc1774da49be
        A/table-images/manifest.json: bfe3827da2d70a2a829cd826a4c77167f654d9058722debc49168080ae0722e8
        A/clauses/window-03/raw.json: 293724f7348dfc8deb3c541003fbaac95805003363fc58495959685f3e65ad89
        A/clauses/window-03/prompt.txt: 41c0891b6e1e2619a20ed81d841c8be33d2f3a3eb0f6bead9020352d2fb0a2a5
        A/clauses/window-03/meta.json: e37c843ecc618bbac232b757c9427b4aff446d67d22ee4680d5fba5318696230
        A/clauses/window-04/raw.json: 2eabc9b0661df82846e11365abd58edfe8654747cd50a0e63fac97b387d29750
        A/clauses/window-04/prompt.txt: 0d6355a793111f80e647e943dc5311e18f3dc5f47823ce12363e018a45abfef9
        A/clauses/window-04/meta.json: 516cedfa9dc562c0e056c10a953d4e553741b4d3711411ebe78d843a3f674c95
        A/clauses/window-05/raw.json: fbd5a9878aa2afe3e5615d8a677f761f4d348a708fb987e8a14cc190e275ab28
        A/clauses/window-05/prompt.txt: f2a725760dc8a91e75631540dbde63bf0c66cbcf486a3dd4dba0b123b5528163
        A/clauses/window-05/meta.json: a6882ff2ec94d83d56188b3379c2c1d24ba502a5f85413e5d2ccefb86191db48
        A/clauses/window-02/raw.json: 07163f23fb8afc7b63577fcdbe4ce8efec7fdc237dbeb5e7d61b0858d4cccddf
        A/clauses/window-02/prompt.txt: b77e1356884d0a8687c7ddb53cdb6c94b2c82ea563e94075518752c3ae0d75f9
        A/clauses/window-02/meta.json: 36b50e08ef447921034244596aeec847a6776f68b2decdd8dd43e84d1fa4b4cd
        A/clauses/window-01/raw.json: 923fa7e1c2d34b44c549a582cdf7b34eab1ea3003417406347b461ee718af356
        A/clauses/window-01/prompt.txt: 7fb48d1638d959a194f84c69a34236cc6002822d12ed3d94ea4e113c09677c3e
        A/clauses/window-01/meta.json: 424917ff2589264e42702674660649dc9f2f56393766861d9836ad96a5a71782
        A/tables/TABLE-1-page-2-1/raw.json: 51ec74940293dbb273b46eb9b1e06125da22723b9f3090a4746f7a01671ca384
        A/tables/TABLE-1-page-2-1/prompt.txt: f5234be35215a7053953b6c724e0b2a40a09daf57b08be26a201132d671e96f2
        A/tables/TABLE-1-page-2-1/meta.json: aa2c918ec83bf0d76011ff69ce1e9ed24a24abf89839e8c46697f26851c55ef5
        B/passages.json: 74694dbe00089b1aceca815d32075af3eae413c27e5b2e204fc50e143431e4e5
        B/raw.json: 3e832c91810110f812f2ab78262b06297713a02a3b0e6b7012cf6054a0ef214e
        B/source-units.json: d3e784c5255aaf5f48e1f4f1dbac1e5e703d096e130a2565e0d7f7111f9b51f0
        B/full-source-units.json: fa20376b389cd295d77740fb1d533b2c64bfbbb70b9da01a1a0f51875eb1aba9
        B/meta.json: 214fffadfcd643bee1826ab80f5a573cc690f4bc8e562b779ea5d7bf6b4f2262
        B/table-images/TABLE-1-page-2-1.png: 48f43d3a4dfecf2d83b7b0f71d8d8de47e79e24747a4229fe6f270ad68ce858f
        B/table-images/page-2.png: 79d41faff4fffaacba1977f6b508d4d4eb234a3aa4bbf15fc9cdfc1774da49be
        B/table-images/manifest.json: f994d6d6d09013ec5056bc50ab515b15b432f22711ee1a7084fb1a0665710f42
        B/clauses/window-03/raw.json: 8b3a94b28f2a138a8d0da0a2e680d14cb4a9d4c0382796bc2397060f8234dcb1
        B/clauses/window-03/prompt.txt: 41c0891b6e1e2619a20ed81d841c8be33d2f3a3eb0f6bead9020352d2fb0a2a5
        B/clauses/window-03/meta.json: 396003064e93454392116073642d306ec9b36d369e5ebd9351319b71319cb85a
        B/clauses/window-04/raw.json: f7aca6c5dc5b4d7cbe907e8a20f18bfb3d390fe27ec0e96ea26a4260e4603272
        B/clauses/window-04/prompt.txt: 0d6355a793111f80e647e943dc5311e18f3dc5f47823ce12363e018a45abfef9
        B/clauses/window-04/meta.json: b34483deb8edabd4aa1bdd709e707ae1342b37ba176138afd0a069f4f1bf7a4c
        B/clauses/window-05/raw.json: 15ce15565005fffc54ede144ced8eff0ab3fa8ed9d7e297d39a4e2100de8fc31
        B/clauses/window-05/prompt.txt: f2a725760dc8a91e75631540dbde63bf0c66cbcf486a3dd4dba0b123b5528163
        B/clauses/window-05/meta.json: 016cbbb80e34e1fa95d2a4368f481a4ae5d1c3a2b4d5ed2bf98cedc51d7059d8
        B/clauses/window-02/raw.json: 8c3b4c4eb894a504511eccfd6b5893e4648deaf147a3ec8df599928b630ad1c8
        B/clauses/window-02/prompt.txt: b77e1356884d0a8687c7ddb53cdb6c94b2c82ea563e94075518752c3ae0d75f9
        B/clauses/window-02/meta.json: a6ecd7c10eed44146384c39fb940e22a68ea675d7aba128dea69605d556ba9a3
        B/clauses/window-01/raw.json: 11c82fc6de86f46f8ac232b3ba23ade6f1fc310396ccaf8e6bb3455345e24923
        B/clauses/window-01/prompt.txt: 7fb48d1638d959a194f84c69a34236cc6002822d12ed3d94ea4e113c09677c3e
        B/clauses/window-01/meta.json: b06bab3174d5d513e8317bbaf76bd17e1550823599a162a3e9dc813c965da3d0
        B/tables/TABLE-1-page-2-1/raw.json: 5cf183d33553a8f0bb3f78098046609612e02cf47df3e1a4cc0c622522c5048d
        B/tables/TABLE-1-page-2-1/prompt.txt: f5234be35215a7053953b6c724e0b2a40a09daf57b08be26a201132d671e96f2
        B/tables/TABLE-1-page-2-1/meta.json: 9ca0eb1a3cf0a39fee7c864fd7247d1e5ace4115259b7f876bd30a2624bc791b
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
      pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010
      source_status_sha256: f07b605fbea93faf2b535b69a2d41ca96291e26c6cb9ce4159ad3d9aa40fd9a6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: structural damage in Broca’s area
    outcome:
      text: impaired speech repetition
    analysis_label: VLBM analysis of structural lesion data
    relation: association
    evidence_ids:
    - P3-S1-C5
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
      pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010
      source_status_sha256: f07b605fbea93faf2b535b69a2d41ca96291e26c6cb9ce4159ad3d9aa40fd9a6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S1-C15
      - Accounting without a linked unit P2-S3-C16
      - Accounting without a linked unit P3-S1-C1
      - Accounting without a linked unit P3-S1-C2
      - Accounting without a linked unit P3-S1-C3
      - Accounting without a linked unit P3-S1-C5
      - Accounting without a linked unit P3-S1-C6
      - Unaccounted source passage P3-S1-C2
      - Unaccounted source passage P3-S1-C5
      - Unaccounted source passage P2-S3-C16
      - Unaccounted source passage P3-S1-C3
      - Unaccounted source passage P3-S1-C1
      - Unaccounted source passage P3-S1-C6
      - 'window 3: invalid/duplicate disposition P3-S1-C12'
      - Result passage disposed without unit P3-S2-C10
      - Accounting without a linked unit P4-S1-C1
      - Accounting without a linked unit P4-S1-C2
      - Unaccounted source passage P4-S1-C1
      - Unaccounted source passage P4-S1-C2
      - Result passage disposed without unit P4-S2-C4
      unattached_null_or_qualifier_ids:
      - P4-S1-C2
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 111
      unselected_timing_passages:
      - P1-S2-C10
      - P2-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      unlinked_tables:
      - TABLE-1-page-2-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S1
        - P2-S3
        - P3-S1
        - P3-S2
        - P3-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010
      source_status_sha256: f07b605fbea93faf2b535b69a2d41ca96291e26c6cb9ce4159ad3d9aa40fd9a6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of structural lesion result.
    - source_id: P1-S1-C5
      disposition: repeated
      result_indexes:
      - 2
      reason: Abstract restatement of PWI result.
    - source_id: P2-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general lesion overlap, not a relationship with a clinical
        outcome.
    - source_id: P2-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/clinical distribution of aphasia severity.
    - source_id: P2-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general lesion overlap in the insula.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Directly states the association between white matter damage and impaired
        repetition.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Provides coordinates for the structural lesion result.
    - source_id: P3-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies the lesion location as being within the arcuate fasciculus.
    - source_id: P3-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Directly states association with Broca's area.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Directly states the PWI predictor in the left supramarginal gyrus.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Clarifies the relationship as hypoperfusion (high TTP) leading to low
        repetition scores.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Directly states the PWI cluster in the TPJ.
    - source_id: P3-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of the arcuate fasciculus result.
    - source_id: P3-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of the arcuate fasciculus result.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: States the null association between the ventral pathway and impaired
        repetition.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the comparison between PWI and structural data.
    - source_id: P4-S1-C1
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of PWI results (supramarginal gyrus and TPJ).
    - source_id: P4-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of structural lesion result.
    - source_id: P4-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of TPJ association.
    - source_id: P4-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion summary of PWI results.
    - source_id: P4-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      reason: Discussion summary of both structural and perfusion results.
    - source_id: P4-S3-C8
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      reason: Final summary restatement of the main findings.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C5
    - P2-S1-C9
    - P2-S1-C15
    - P2-S3-C16
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C12
    - P3-S2-C1
    - P3-S2-C10
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C10
    - P4-S2-C4
    - P4-S2-C9
    - P4-S3-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C4
      recruited_sample:
      - P1-S3-C10
      eligibility:
      - P2-S1-C2
      - P2-S1-C3
      imaging_provenance:
      - P2-S1-C18
      - P2-S2-C14
      - P3-S1-C4
      imaging_timing:
      - P2-S1-C6
      outcome_timing:
      - P2-S1-C6
      outcome_definition:
      - P2-S1-C12
      - P2-S3-C13
      validation: []
      analysis_restrictions:
      - P4-S2-C5
      - P4-S2-C8
      dependent_variable_statement:
      - P2-S3-C5
      - P2-S3-C9
      - P2-S3-C13
      limitations:
      - P4-S2-C5
      - P4-S2-C7
      - P4-S2-C8
      - P4-S3-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S3-C8
      - P2-S3-C9
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C4
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
      pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
      review_sha256: de4fed9c6c3d71630dc733bd13bf69db2b17c6d8089daa006f88d3f4bcf1eb46
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
      - P3-S1-C5
      source_result: The VLBM analysis of structural lesion data revealed that additional
        structural damage associated with impaired speech repetition was noted in
        Broca's area (coordinates approx. -41, 36, 10). This finding was derived from
        a voxelwise logistic regression of binary lesion maps (DWI) against speech
        repetition performance, controlling for auditory comprehension.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VLBM analysis of structural
            lesion data described in P3-S1-C5 and P2-S3-C4/C5. The proposed core correctly
            identifies this as a voxelwise analysis of structural lesions (DWI) rather
            than the separate PWI analysis or the arcuate fasciculus finding.
          source_ids:
          - P3-S1-C5
          - P2-S3-C4
          - P2-S3-C5
        direction:
          answer: fits
          reason: The source states that damage in Broca's area was 'associated with
            impaired speech repetition' (P3-S1-C5). The proposed core claims 'Structural
            damage in Broca's area is associated with impaired speech repetition,'
            which preserves the detected association direction.
          source_ids:
          - P3-S1-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as structural damage in Broca's
            area. The outcome is impaired speech repetition. The patient measurement
            is correctly classified as template_lesion_overlap, as the study overlaid
            patient lesions on a standard template (SPM5) for voxelwise analysis,
            rather than using patient-specific diffusion tractography for the primary
            lesion mapping (DTI was used for a separate probabilistic map overlay
            in P3-S1-C3/C4, not the primary VLBM statistic).
          source_ids:
          - P3-S1-C5
          - P2-S3-C4
          - P2-S2-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis controlled
            for auditory comprehension (P2-S3-C8/C9) and notes the limitation regarding
            the heterogeneous sample (P4-S2-C5/C7). These are material qualifiers
            present in the source.
          source_ids:
          - P2-S3-C8
          - P2-S3-C9
          - P4-S2-C5
          - P4-S2-C7
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly reflects that
            this is a secondary finding ('Additional structural damage...') and includes
            the necessary context about the sample composition and statistical controls.
          source_ids:
          - P3-S1-C5
          - P4-S2-C5
      optional_pending:
      - sample.time_post_onset
      - coordinates.brocas_area
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - sample.time_post_onset
    - coordinates.brocas_area
    normalizations:
    - field: sample.time_post_onset
      original: Behavioral and MRI examinations completed between 3 and 20 days following
        stroke, with less than 24 hours separating the two assessments
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 24'
    analysis_identity:
      id: R002
      exposure:
        text: structural damage in Broca’s area
      outcome:
        text: impaired speech repetition
      analysis_label: VLBM analysis of structural lesion data
      relation: association
      evidence_ids:
      - P3-S1-C5
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
        pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2010
        source_status_sha256: f07b605fbea93faf2b535b69a2d41ca96291e26c6cb9ce4159ad3d9aa40fd9a6
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 490bbf58be0333fc36cb660b83945b89ef5f83bbd65ecce65843c8ff5f057f2a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 490bbf58be0333fc36cb660b83945b89ef5f83bbd65ecce65843c8ff5f057f2a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Additional structural damage associated with impaired\nspeech\
          \ repetition was noted in Broca’s area (\x0341, 36, 10)."
        anchor_text: "Additional structural damage associated with impaired\nspeech\
          \ repetition was noted in Broca’s area (\x0341, 36, 10)."
        excluded_fragments: []
      P2-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 10628b1a9b4cb46553ae929d12af48baafc4f67cfb50d5229142d7d94433a9b9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C4
          page: 2
          text_layer_sha256: 10628b1a9b4cb46553ae929d12af48baafc4f67cfb50d5229142d7d94433a9b9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Therefore, data from 39

          patients were included in the final statistical analyses described below.'
        anchor_text: 'Therefore, data from 39

          patients were included in the final statistical analyses described below.'
        excluded_fragments: []
        image_sha256: 4c908a2d84e92b512f2f89f1def5d4580e1f6e54dab837ea7a3dba3b2ee10103
        transcription: '. Therefore, data from 39

          patients were included in the final statistical analyses described below'
      P2-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 55b5fc8cd571c22b4e71e4e8d28992cb36b6438919b6e493f2106582573a17c1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C6
          page: 2
          text_layer_sha256: 55b5fc8cd571c22b4e71e4e8d28992cb36b6438919b6e493f2106582573a17c1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'For most

          participants, behavioral and MRI examination were completed within

          3 d of hospital admission, but in a few cases participants were examined

          as late as 20 d following stroke due to factors such as fatigue or other

          stroke sequelae.'
        anchor_text: 'For most

          participants, behavioral and MRI examination were completed within

          3 d of hospital admission, but in a few cases participants were examined

          as late as 20 d following stroke due to factors such as fatigue or other

          stroke sequelae.'
        excluded_fragments: []
        image_sha256: a72a9deb086031037333fca8bb5784775c57688b137118e9139bbe87d8f5e374
        transcription: '. For most

          participants, behavioral and MRI examination were completed within

          3 d of hospital admission, but in a few cases participants were examined

          as late as 20 d following stroke due to factors such as fatigue or other

          stroke sequelae'
      P2-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b253dbc61548f8f7b0bdd8c1c22a33afef04563de99232461a620e7d61f5626b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C7
          page: 2
          text_layer_sha256: b253dbc61548f8f7b0bdd8c1c22a33afef04563de99232461a620e7d61f5626b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Behavioral and MRI examinations were always com-\npleted with\
          \ \x0224 h separating them."
        anchor_text: "Behavioral and MRI examinations were always com-\npleted with\
          \ \x0224 h separating them."
        excluded_fragments: []
      P1-S3-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb5ff723ce58a93806f4c1d5a20dc06c1c8ff65db9aa1622bdb0df7c5b2394da
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ecad44c69de0c104984cce02861eb0945b6a702b00c83aa9048907bdce46413e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C11
          page: 1
          text_layer_sha256: ecad44c69de0c104984cce02861eb0945b6a702b00c83aa9048907bdce46413e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'All participants had incurred a single event ischemic stroke

          to the left hemisphere and provided informed consent for study inclu-

          Received March 4, 2010; revised June 25, 2010; accepted July 6, 2010.'
        anchor_text: 'All participants had incurred a single event ischemic stroke

          to the left hemisphere and provided informed consent for study inclu-

          Received March 4, 2010; revised June 25, 2010; accepted July 6, 2010.'
        excluded_fragments: []
        image_sha256: 683e7d19acc81b75bf8868a3a5de00a343d2eb8543cdcfffd1d2b66057fdafbe
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "Additional structural damage associated with impaired\nspeech repetition\
    \ was noted in Broca’s area (\x0341, 36, 10)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
