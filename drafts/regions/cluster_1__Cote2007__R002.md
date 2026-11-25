---
id: cluster_1
name: Cluster 1 cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: communication_abilities
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: communication_abilities
  target_kind: impairment
  claim: Participants in the first cluster showed impairments in all four language
    components evaluated by the Protocole MEC, specifically reduced verbal fluency,
    poor story recall, reduced comprehension of non-literal language, major difficulty
    in adapting speech to the communication partner, and prosodic impairments.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 28
    population: French-speaking individuals with a single right-hemisphere vascular
      brain lesion
    phase: not_reported
    time_post_onset: 3 to 14 weeks post-onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size restricting generalisation
  - A posteriori exploration
  - Protocole MEC does not provide exhaustive evaluation of all communication components
    (e.g., humor and sarcasm are not evaluated)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Membership in a subgroup identified by hierarchical
    cluster analysis based on z-scored performance on 14 tasks of the Protocole MEC.
    Cluster 1 is one of three identified subgroups; Impairment for the subgroup was
    defined as a mean z score below -1.5 and more than 50% of members having a z score
    below -2. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P4-S1-C8, two-model agreement, human
    verification pending): METHOD


    Participants


    A total of 28 French-speaking volunteer participants (15 men and 13 women) were
    evaluated Original text-layer quotation is preserved below. PDF image reading
    (P4-S1-C12, two-model agreement, human verification pending): . All were 3 to
    14 weeks post-onset (with an average of 6 weeks post-

    onset) Original text-layer quotation is preserved below.'
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
    - proposed_concept:communication_abilities
  citation: '@Cote2007'
  source_passages:
  - section: Original source P8-S1-C1
    page: 8
    quote: '

      N Participants in the first cluster showed impairments in all four language

      components evaluated by the Protocole MEC.'
    supports: claim
  - section: Original source P8-S1-C2
    page: 8
    quote: 'A qualitative analysis of these

      participants’ results showed reduced verbal fluency, poor story recall, reduced

      comprehension of non-literal language, major difficulty in adapting their speech

      to their communication partner, and prosodic impairments.'
    supports: claim
  - section: Original source P4-S1-C8
    page: 4
    quote: 'METHOD

      Participants

      A total of 28 French-speaking volunteer participants (15 men and 13 women) were

      evaluated.'
    supports: sample
  - section: Original source P4-S1-C12
    page: 4
    quote: 'All were 3 to 14 weeks post-onset (with an average of 6 weeks post-

      onset).'
    supports: sample
  - section: Original source P6-S2-C4
    page: 6
    quote: 'The performance of all participants with RHD for all tasks was submitted
      to a

      hierarchical cluster analysis (Aldenderfer & Blashfield, 1985) to allow for
      the

      identification of subgroups of participants with RHD characterised by distinctive

      communication impairment profiles.'
    supports: method
  - section: Original source P6-S2-C10
    page: 6
    quote: 'In order to

      achieve this characterisation, the result for each task was considered impaired
      for a

      given subgroup under the following two conditions: (1) the overall mean z score
      of

      the cluster was below 21.5; and (2) more than 50% of the members of the cluster
      had

      a z score below 22 (see Table 3).

      744

      COˆ TE´ ET AL.


      '
    supports: method
  - section: Original source P10-S1-C6
    page: 10
    quote: 'The main limitation of the present study is surely the small number of
      participants

      evaluated, restricting the generalisation of results to the population of RHD.'
    supports: limitation
  - section: Original source P3-S1-C6
    page: 3
    quote: 'This first attempt had a number of

      limitations; one being that it was an a posteriori exploration, and another
      that it was

      based on the evaluation of only a limited number of communication components.'
    supports: limitation
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      humour and sarcasm is not evaluated, and only a limited number of tasks assess
      the

      semantic processing of words.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Cote2007
  proposal_id: R002
  review_status_sha256: 96f13823ca6473ca34b0ee1e2c78faa99f2097755d5cf0ddde211ce26724f4fc
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
        A/passages.json: 03fa8ff2339858c2855ac89ccce3c15f62ab2f70a939a68ecfff9dfd4fb1725b
        A/raw.json: 788a7699453a6d1c8471b59dfecab2a4fce1ab73f16874acdee5d803b4a92355
        A/source-units.json: 83eada0c7082f818f12438f081b1b8ca5df80636b2812c0e4119bcf1bbf590ad
        A/full-source-units.json: 82cf9f7dca522351764859526bc7404dfbc0c1ba907c83da7cdd27898066542c
        A/meta.json: d4161df53611f61a23eed22cba898db690fffdbc885f25da1890780e90acafd4
        A/table-images/TABLE-1-page-5-1.png: 8f13a25bc722d3d7823c0c8c5d6715906f3ab3a2ada92fd96f5b04328f9b646d
        A/table-images/page-7.png: ba00628c1d417e91fdcb17996814df28e740ca1694bd139a45ebdb15c08a089a
        A/table-images/page-5.png: b845c15068af3f5e8ee59b2968e6297215afc58eddf0a1f42895c61340f6ecde
        A/table-images/manifest.json: a75c9e27b2fc611f3e449a5118960978e9176f120967e14f43c1448dffdb1fb6
        A/table-images/TABLE-3-page-7-1.png: 79e1f6865011e189e83c9df9c234c1374d5a1a50a4a321a53d18b5bbb47ddbe9
        A/table-images/TABLE-2-page-7-2.png: 79e1f6865011e189e83c9df9c234c1374d5a1a50a4a321a53d18b5bbb47ddbe9
        A/clauses/window-03/raw.json: f3ab964bd1908cd02a2c221959775598fb6ead71e44c5a3b567ed14ed1247265
        A/clauses/window-03/prompt.txt: 8efccad2dc5a4e7d5eb8cb070e33c90ad93fc22029c44a38200a4a3624b23b63
        A/clauses/window-03/meta.json: b12ac39fd4fb58d73e7e79e837169ce2184ea7001afd7b0842b8a8817ce66251
        A/clauses/window-04/raw.json: 8fdec888e1bbd2c6fc675a8e88c8ec88400cdc2341a292f4b3efb6161417bc83
        A/clauses/window-04/prompt.txt: 3bc2150e7bcbc3073566a2e3b582d3e74f8459a6805c1464d9fbaf6ff8b02443
        A/clauses/window-04/meta.json: eeed59933befd9cf3a969f1a220d7035191a005069efd9d766e6e3539dab5435
        A/clauses/window-05/raw.json: f040de4b532f38380e13e474a96297077097c7c7ec88da8040150373c218b5bf
        A/clauses/window-05/prompt.txt: 5455bdf975286230eba5f664a232d626909b84082252fa2aa17f080966f2019d
        A/clauses/window-05/meta.json: 9ef843b6e67c2cad7e4066776622294893c43fcdc9cfccebfa9cba75bab4c8c7
        A/clauses/window-02/raw.json: 29ac4c010c9ce168f775e19bc476016ea1c1a2935e6c0e3abdfe37f1f446914a
        A/clauses/window-02/prompt.txt: 96fe77f62f8942f97cc4ff5a5f5265c6d1bdb201c40a561e938c80f5c0acda04
        A/clauses/window-02/meta.json: 1210e41c69fd0805f06e2fbcf089c4100d82fc68564aa7b4762d0296badfb32e
        A/clauses/window-01/raw.json: 343eada9f6bc202e132d791f6bfd9ce6646636789c0c7c86217f2daa80129fba
        A/clauses/window-01/prompt.txt: a48ced5f123ff8595ad7d281cc4cde7e8184133aeb25e3dd71e9fa3d3207d510
        A/clauses/window-01/meta.json: 06d55941ae2f024a3ba4ea03724a7d379c8036bd7cffce5fb09b033583c06c1d
        A/tables/TABLE-1-page-5-1/raw.json: 89a31f142dd1ea47818ae4e9d8a506eb005db29fe8e4fe17d43d558303666217
        A/tables/TABLE-1-page-5-1/prompt.txt: b705e0bc0a058c0bd3ed7ade221c3b93290f82c5c1827e165c7c7347076fbc5e
        A/tables/TABLE-1-page-5-1/meta.json: c7d0c47c38b3da178a76396bfb41b6c6ddf0a2a589456bcd76f62fdc948f3e73
        A/tables/TABLE-2-page-7-3/raw.json: c4ca673bea468b30cbdd25df6a78ca0149b3b1702b24a57e745c8f847751c256
        A/tables/TABLE-2-page-7-3/prompt.txt: bdfea9f6ed74a515f728fea53e25ebac43c897b38f1669affeea255c43683a1e
        A/tables/TABLE-2-page-7-3/meta.json: 22c9e9afd15a9a149fae4cab5b6e6dcb035569289b747e8b15ad3394c09a714e
        A/tables/TABLE-3-page-7-2/raw.json: 8b8d488f1847c131d52f6560f2fd4b79389864512b74e7d9b75a336729f6cc8c
        A/tables/TABLE-3-page-7-2/prompt.txt: e64e5705be309fe0be689b28503961a945c5c0629e2a4d6c6da21507e4faf9b4
        A/tables/TABLE-3-page-7-2/meta.json: 2d65a4b5fd42a79dc1accec6ddaa1bbb7fbde258fd3c86c177a5be0edaef0a22
        B/passages.json: 03fa8ff2339858c2855ac89ccce3c15f62ab2f70a939a68ecfff9dfd4fb1725b
        B/raw.json: 0e4156b999fb2a4e3302b866dad92b73376daeb80437b22045bcf89a96b5311f
        B/source-units.json: 83eada0c7082f818f12438f081b1b8ca5df80636b2812c0e4119bcf1bbf590ad
        B/full-source-units.json: 82cf9f7dca522351764859526bc7404dfbc0c1ba907c83da7cdd27898066542c
        B/meta.json: da544f5c097a666a2c2083afe142dad484b97453dd00e003adb345d34f31195d
        B/table-images/TABLE-1-page-5-1.png: 8f13a25bc722d3d7823c0c8c5d6715906f3ab3a2ada92fd96f5b04328f9b646d
        B/table-images/page-7.png: ba00628c1d417e91fdcb17996814df28e740ca1694bd139a45ebdb15c08a089a
        B/table-images/page-5.png: b845c15068af3f5e8ee59b2968e6297215afc58eddf0a1f42895c61340f6ecde
        B/table-images/manifest.json: c2a76eb4bd02b45e78418361fbbc87c9441373cf681d6af7b1d6eeb19c8762dd
        B/table-images/TABLE-3-page-7-1.png: 79e1f6865011e189e83c9df9c234c1374d5a1a50a4a321a53d18b5bbb47ddbe9
        B/table-images/TABLE-2-page-7-2.png: 79e1f6865011e189e83c9df9c234c1374d5a1a50a4a321a53d18b5bbb47ddbe9
        B/clauses/window-03/raw.json: 8e9e9d55f5b017e8439dfa2a92eb7979662a4f01009a38e7a18f55d8262d81e4
        B/clauses/window-03/prompt.txt: 8efccad2dc5a4e7d5eb8cb070e33c90ad93fc22029c44a38200a4a3624b23b63
        B/clauses/window-03/meta.json: fc0f816ca5d0ba36cd40de7303921c9c440c2fa0891c1890a9c7e7d454b1e680
        B/clauses/window-04/raw.json: 7fdb900b67feff1fa8f81e643d99c3faaef9fe8f927c1ca269d4c59b54b7a475
        B/clauses/window-04/prompt.txt: 3bc2150e7bcbc3073566a2e3b582d3e74f8459a6805c1464d9fbaf6ff8b02443
        B/clauses/window-04/meta.json: dedde3ccbc02f05a00f61f98656a8f353257d62782883597dab4461af88d08bc
        B/clauses/window-05/raw.json: 4b63578e1e4b6b54ee448d2c01c4da55780f4bc25dcf239e07f95bd79b6ba25c
        B/clauses/window-05/prompt.txt: 5455bdf975286230eba5f664a232d626909b84082252fa2aa17f080966f2019d
        B/clauses/window-05/meta.json: 5a99c227470b81bb78f6c0d6588d84da424b765419387b0f7bec2ae21e702c0b
        B/clauses/window-02/raw.json: 7e59e12a793b2b45739d72f2b234519d4e9e22a01921d1185337ea507b0c6f53
        B/clauses/window-02/prompt.txt: 96fe77f62f8942f97cc4ff5a5f5265c6d1bdb201c40a561e938c80f5c0acda04
        B/clauses/window-02/meta.json: c6c3ecd8f2b71b3220e3ef6d153a0bde0743f8b73810fd7557e446b0a92173ce
        B/clauses/window-01/raw.json: f80eff33da23a1218263c99af7e17c5f2ac192202be2c7b5bad6c4b8ed6c1542
        B/clauses/window-01/prompt.txt: a48ced5f123ff8595ad7d281cc4cde7e8184133aeb25e3dd71e9fa3d3207d510
        B/clauses/window-01/meta.json: 530840e1e0a061bf5106698fa4b4fec36254cf6b6f1f42bffd59abc18c34e209
        B/tables/TABLE-1-page-5-1/raw.json: 73f7957c3e4b6eaf3355e6e413ec400f319feace9953d712a5c0d4122e801408
        B/tables/TABLE-1-page-5-1/prompt.txt: b705e0bc0a058c0bd3ed7ade221c3b93290f82c5c1827e165c7c7347076fbc5e
        B/tables/TABLE-1-page-5-1/meta.json: 09b398540ac6ed8f1e307ad530bb883f9493d8802f3d89bc3465bdc964509fb0
        B/tables/TABLE-2-page-7-3/raw.json: 5b9cd54aceb004b6d70cb957f5da1e78117ce1a1d90c7188eb1e524a18a69921
        B/tables/TABLE-2-page-7-3/prompt.txt: bdfea9f6ed74a515f728fea53e25ebac43c897b38f1669affeea255c43683a1e
        B/tables/TABLE-2-page-7-3/meta.json: 9a802759e0103680d05b16b48a5c97801937763cd3a0e5cf703b18b90658903c
        B/tables/TABLE-3-page-7-2/raw.json: 4f91ada0e5da3f476c4895da8361ebe230d15a25bb14a5d6f9f0ad33886383e6
        B/tables/TABLE-3-page-7-2/prompt.txt: e64e5705be309fe0be689b28503961a945c5c0629e2a4d6c6da21507e4faf9b4
        B/tables/TABLE-3-page-7-2/meta.json: 0d748cd995015f7c66f739caf5edc789e464f75398fbd66aecfc0b5df15fa4ec
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
      pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
      source_review: _compare/relationships-2026-11-16/review-current/Cote2007
      source_status_sha256: 69ee24a86a5547b76b8eecd473be4a6eeff726ff6417ad6830d7e516d0e64287
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: Cluster 1 membership
    outcome:
      text: prosodic, lexical-semantic, discourse, and pragmatic abilities
    analysis_label: Cluster 1 characterization
    relation: association
    evidence_ids:
    - P8-S1-C1
    - P8-S1-C2
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
      pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
      source_review: _compare/relationships-2026-11-16/review-current/Cote2007
      source_status_sha256: 69ee24a86a5547b76b8eecd473be4a6eeff726ff6417ad6830d7e516d0e64287
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P1-S2-C5
      - Result passage disposed without unit P2-S1-C1
      - Result passage disposed without unit P2-S1-C2
      - Result passage disposed without unit P6-S2-C7
      - Accounting without a linked unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Unaccounted source passage P8-S1-C1
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C3
      - Result passage disposed without unit P8-S1-C12
      - Result passage disposed without unit P8-S1-C13
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P8-S1-C15
      - Result passage disposed without unit P8-S1-C16
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P8-S2-C7
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P9-S2-C5
      - Result passage disposed without unit P9-S2-C6
      - Result passage disposed without unit P10-S1-C9
      unattached_null_or_qualifier_ids:
      - P8-S1-C16
      - P8-S2-C5
      - P9-S2-C6
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 110
      unselected_timing_passages:
      - P3-S2-C9
      - P4-S1-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P3-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-3
      - TABLE-3-page-7-2
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-3
      - TABLE-3-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
      source_review: _compare/relationships-2026-11-16/review-current/Cote2007
      source_status_sha256: 69ee24a86a5547b76b8eecd473be4a6eeff726ff6417ad6830d7e516d0e64287
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies the identification of four subgroups based on Protocole MEC.
    - source_id: P1-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of cluster findings in the abstract.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of cluster findings in the abstract.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of cluster findings in the abstract.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about lack of clear relationship with factors.
    - source_id: P2-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information.
    - source_id: P2-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: States higher incidence in rehabilitation settings.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes validity/reliability of the tool, not a current-study relationship.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies three clusters via hierarchical analysis.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Describes Cluster 1 impairments.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Qualitative details of Cluster 1 impairments.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual patient observation (anosognosia).
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      - 2
      reason: Describes Cluster 2 preservation of discourse.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Describes Cluster 2 impairments.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual patient observation (anosognosia).
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 0
      - 3
      reason: Describes Cluster 3 normal abilities.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical impression of specific patients.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical impression of specific patients.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Qualifies Cluster 3 results relative to norms.
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual patient awareness.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 4
      reason: Identifies outliers.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Describes outlier deficits.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 4
      reason: Qualitative details of outlier deficits.
    - source_id: P8-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual patient awareness.
    - source_id: P8-S1-C16
      disposition: represented
      result_indexes:
      - 6
      reason: Null finding for specific lesion site association with clusters.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Observation of frontal lesions in Cluster 2.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Observation of subcortical lesions in Cluster 3.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Distribution of age and education across subgroups.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Gender distribution (demographics).
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about factors.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of heterogeneity.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of cluster implications.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of Cluster 3 findings.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of Cluster 3 findings.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of clinical impression vs quantitative results.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of Cluster 3 findings.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Incidence of communication disorders in rehabilitation settings.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Incidence estimate (>80%) in rehabilitation settings.
    - source_id: P9-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of combination of impairments.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of need for larger samples.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Association between subcortical lesions and preserved language abilities.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion restatement.
    unresolved_coverage:
    - source_id: P9-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C1
    - P1-S2-C2
    - P1-S2-C3
    - P1-S2-C5
    - P2-S1-C1
    - P3-S2-C10
    - P6-S2-C7
    - P7-S1-C1
    - P8-S1-C3
    - P8-S1-C6
    - P8-S1-C8
    - P8-S1-C9
    - P8-S1-C10
    - P8-S1-C11
    - P8-S1-C14
    - P8-S1-C15
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C6
    - P8-S2-C7
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C7
    - P9-S2-C5
    - P9-S2-C6
    - P10-S1-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-7-3
    - TABLE-3-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C8
      recruited_sample:
      - P4-S1-C14
      - P4-S2-C1
      eligibility:
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      imaging_provenance:
      - P4-S1-C10
      imaging_timing:
      - P4-S1-C12
      outcome_timing:
      - P4-S1-C12
      outcome_definition:
      - P6-S1-C12
      - P6-S1-C13
      - P7-S1-C3
      validation: []
      analysis_restrictions:
      - P6-S2-C10
      dependent_variable_statement:
      - P6-S1-C12
      limitations:
      - P3-S2-C11
      - P3-S2-C12
      - P4-S1-C1
      - P4-S1-C2
      - P9-S2-C6
      - P10-S1-C6
      personal_factors:
      - P1-S2-C5
      - P6-S2-C3
      - P8-S2-C5
      - P9-S2-C6
      tested_personal_effects: []
      adjustment_roles:
      - P6-S2-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C9
      - P8-S2-C5
      - P8-S2-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: validation
      source_id: P3-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C3
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
      pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
      review_sha256: 96f13823ca6473ca34b0ee1e2c78faa99f2097755d5cf0ddde211ce26724f4fc
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
      - P8-S1-C1
      - P8-S1-C2
      source_result: Cluster 1 membership was associated with impairments in all four
        language components evaluated by the Protocole MEC (prosodic, lexical-semantic,
        discourse, and pragmatic), characterized by reduced verbal fluency, poor story
        recall, reduced comprehension of non-literal language, major difficulty in
        adapting speech to the communication partner, and prosodic impairments.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the characterization
            of Cluster 1 from the hierarchical cluster analysis described in the source.
            The source explicitly links Cluster 1 to the specific impairment profile
            described in P8-S1-C1 and P8-S1-C2.
          source_ids:
          - P8-S1-C1
          - P8-S1-C2
          - P6-S2-C4
        direction:
          answer: fits
          reason: The direction of the association is correctly captured as 'likely'
            or positive association between Cluster 1 membership and the presence
            of impairments. The source states that participants in this cluster 'showed
            impairments', which aligns with the proposed claim.
          source_ids:
          - P8-S1-C1
          - P8-S1-C2
        construct:
          answer: fits
          reason: The exposure (Cluster 1 membership) and outcome (impairments in
            prosodic, lexical-semantic, discourse, and pragmatic abilities) are correctly
            identified. The patient measurement is correctly classified as non_imaging,
            as the study relies on the Protocole MEC behavioral battery, not imaging
            metrics for the outcome characterization, although lesion data was collected
            for descriptive purposes.
          source_ids:
          - P8-S1-C1
          - P8-S1-C2
          - P4-S1-C3
        qualifications:
          answer: fits
          reason: The qualifications regarding the definition of impairment (mean
            z-score below -1.5 and >50% below -2) are accurate based on P6-S2-C10.
            The limitation regarding the small sample size and a posteriori nature
            of the exploration are also correctly included.
          source_ids:
          - P6-S2-C10
          - P10-S1-C6
          - P3-S1-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft includes the key limitations
            regarding sample size, the a posteriori nature of the analysis, and the
            non-exhaustive nature of the Protocole MEC. The unresolved image reading
            in P1-S1-C5 does not affect the core result of Cluster 1 characterization.
          source_ids:
          - P10-S1-C6
          - P3-S1-C6
          - P4-S1-C1
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
      id: R002
      exposure:
        text: Cluster 1 membership
      outcome:
        text: prosodic, lexical-semantic, discourse, and pragmatic abilities
      analysis_label: Cluster 1 characterization
      relation: association
      evidence_ids:
      - P8-S1-C1
      - P8-S1-C2
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
        pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
        source_review: _compare/relationships-2026-11-16/review-current/Cote2007
        source_status_sha256: 69ee24a86a5547b76b8eecd473be4a6eeff726ff6417ad6830d7e516d0e64287
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 792f43a2d4cf6ee11bfee57ad68539d44ef1aa5d6fb38b2161a40a41a2b68189
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C8
          page: 4
          text_layer_sha256: 792f43a2d4cf6ee11bfee57ad68539d44ef1aa5d6fb38b2161a40a41a2b68189
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'METHOD

          Participants

          A total of 28 French-speaking volunteer participants (15 men and 13 women)
          were

          evaluated.'
        anchor_text: 'METHOD

          Participants

          A total of 28 French-speaking volunteer participants (15 men and 13 women)
          were

          evaluated.'
        excluded_fragments: []
        image_sha256: 27de309931e96c47a05a747f35a8c49836aef2b8328c93cbee7c6e89dc483cb8
        transcription: 'METHOD


          Participants


          A total of 28 French-speaking volunteer participants (15 men and 13 women)
          were evaluated'
      P4-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6b0e7e6129086c0dc212619ba1f9435e77218880f7ba5732d548fc6e80d65f98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 393cb871281a6566accbffa2af7e5a39651caecbd4a9185c0b51137d25a20473
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C12
          page: 4
          text_layer_sha256: 393cb871281a6566accbffa2af7e5a39651caecbd4a9185c0b51137d25a20473
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All were 3 to 14 weeks post-onset (with an average of 6 weeks
          post-

          onset).'
        anchor_text: 'All were 3 to 14 weeks post-onset (with an average of 6 weeks
          post-

          onset).'
        excluded_fragments: []
        image_sha256: 987c0dac1e73f7a8f9a2bba60439039b288a95cad1adf15b0feae21cf8eb2ab0
        transcription: '. All were 3 to 14 weeks post-onset (with an average of 6
          weeks post-

          onset)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: '

    N Participants in the first cluster showed impairments in all four language

    components evaluated by the Protocole MEC.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
