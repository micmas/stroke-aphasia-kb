---
id: early_language_improvement
name: early language improvement
kind: impairment
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: language_functioning
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_functioning
  target_kind: impairment
  claim: all three subscores (comprehension, repetition and naming) significantly
    improved between the initial assessment and the follow-up
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 20
    population: individuals with aphasia due to a first single ischemic stroke in
      the left middle cerebral artery
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
  - small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: improvement in language functioning measured by a
    composite score consisting of comprehension, repetition, and naming subscores.
    three participants showed a deterioration between the two assessments; the rest
    of the participants showed an improvement in composite scores. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P3-S1-C1, two-model agreement, human verification pending): MATERIALS
    AND METHODS

    Participants

    Twenty participants took part in this study (5 women; mean

    age: 71.6 ± 12.45 years; mean education: 10.05 ± 5.04) Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-25'
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
    - proposed_concept:language_functioning
  citation: '@OsaGarcia2020'
  source_passages:
  - section: Original source P5-S1-C8
    page: 5
    quote: 'All three subscores (i.e., comprehension,

      repetition and naming) signiﬁcantly improved between the initial

      assessment and the follow-up (Comprehension Wilcoxon signed

      ranks test, Z = 3.771, P < 0.001; Repetition Wilcoxon signed

      ranks test, Z = −3.115, P = 0.002; Naming paired-sample t-

      test = −2.329, df = 18, P = 0.031).'
    supports: claim
  - section: Original source P3-S1-C1
    page: 3
    quote: '

      Osa García et al.

      Predicting Early Aphasia Outcome

      MATERIALS AND METHODS

      Participants

      Twenty participants took part in this study (5 women; mean

      age: 71.6 ± 12.45 years; mean education: 10.05 ± 5.04).'
    supports: sample
  - section: Original source P3-S1-C2
    page: 3
    quote: 'Participants presented with aphasia due to a ﬁrst single ischemic

      stroke in the left middle cerebral artery.'
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: 'Initial language assessments took place within the ﬁrst

      72 h (mean = 2.3 days) after stroke onset, and the follow-

      up took place 7–15 days later (mean = 10.55 days).'
    supports: method
  - section: Original source P5-S1-C4
    page: 5
    quote: 'Three participants showed a deterioration between

      the two assessments; the rest of the participants showed an

      improvement in CS scores.'
    supports: claim
  - section: Original source P3-S2-C1
    page: 3
    quote: 'the word-sentence comprehension Task (max = 47 points) of

      the Montreal-Toulouse aphasia battery (MT-86) (39) and the

      revised (short) version of the Token Test (40) (max = 36

      points), which includes oral comprehension of words, sentences

      and sequential commands.'
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: 'The repetition subscore was assessed

      using the repetition task [2 points for each word/non-word (n =

      30) and 5 points for each sentence (n = 3), max = 75 points]

      of the MT-86 (39).'
    supports: method
  - section: Original source P3-S2-C3
    page: 3
    quote: 'Finally, the naming subscore consisted of

      the semantic ﬂuency task (max = 25 points) of the Protocole

      Montréal d’Évaluation de la Communication (41) and a naming

      task.'
    supports: method
  - section: Original source P3-S2-C4
    page: 3
    quote: 'The test Dénomination orale d’images (DO-80) (42) (max

      = 80 points) was used for participants tested in French and the

      Boston Naming Test (BNT) (43) (max = 60 points) was used

      for the one participant who was tested in English, since there

      is no adaptation of this test currently available in English and

      its characteristics as naming test are the same as the BNT.'
    supports: method
  - section: Original source P7-S2-C3
    page: 7
    quote: 'Limitations of this study include the small sample size and

      the analysis that was limited to only one white matter tract.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: OsaGarcia2020
  proposal_id: R002
  review_status_sha256: 8c2734a5d584e66f2b60546c0d73b99074a18e41c571ed0fdfe9e34b694e035f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
        A/passages.json: 80cc3cd09a9bd21a6a655998f904f0161516d638386099b77ce69bd38368258b
        A/raw.json: 1865dbbe085b77b9f5df4314254bf81077a2ba136782e4a06012cba78f202ef8
        A/source-units.json: 11c33da8251a05845c2dc92072dfb550e601bd5590204b56dbb843d50f25def5
        A/full-source-units.json: 0b3408954dacb31cfc151f143615878c61cc6a5a7acd2134adf05cbe044a322c
        A/meta.json: 3805bc5e7aa66c539543084a645423193ebb0714b52374acc9c7305d8bf9607a
        A/table-images/page-6.png: 4b3f153307d583b33a7755a3c5e29ac49f294736c56395e43f5f01a08b90b79d
        A/table-images/page-7.png: f467abcea0e6caa41833e33bc9f7ccc56f16949947272fbbdff63ce4696ef4ea
        A/table-images/page-4.png: ccccc5b9cb5d714d2d9ead82f142fff3bba466cc770fd5b12ea3469490adebe5
        A/table-images/TABLE-1-page-4-1.png: 7d2297fe26a696f040eab96ded49393de458998e6efa7e5a96b9535547f872fe
        A/table-images/TABLE-2-page-6-1.png: e4683a92f27599239cf9b0680f26a71681d4bef37844cf280c9a30a841788837
        A/table-images/manifest.json: 032cdd7a40999acb3fe55e68733e9430b474961b3781cf1e451ab5ced206747d
        A/table-images/TABLE-3-page-7-1.png: f7172106ab1d01c25d9a85b347b11b1707f8306fd38e625269aa5c460fdaa855
        A/clauses/window-03/raw.json: e8878e6039b4ce79374a3593bc0a03799f3a55b4175afdcf05630b806f2a874d
        A/clauses/window-03/prompt.txt: 7f139f181b3892a24cb34450284c9e811d430f39cd6167fbd46fcbfb2e4c4220
        A/clauses/window-03/meta.json: dbf4aeb2ca0739e596f7d81ddd58427d9fe3d26d7ccd1aba984f502171749618
        A/clauses/window-04/raw.json: 25e1337e377d25536b99e1781aba6c7f800d2c79f54fce832cfd168e51847343
        A/clauses/window-04/prompt.txt: dc8a3f75f78d3dbe007395b6d7256fdfa29799e24d3809988982f6f0bd7ba0b2
        A/clauses/window-04/meta.json: 2bb316b3197228bbf5b621c905a29a1df5f7eb3c276c9d2cba544766f841817a
        A/clauses/window-05/raw.json: 1c74fd0a855dc42f91ec09c411a46aaabb0c36870af9d42be5797bfca2cda012
        A/clauses/window-05/prompt.txt: cceb7d5ad990a63aa8515c095ee0f7c84d5a2671d7781c8a7efd981d4dad1e76
        A/clauses/window-05/meta.json: 1f54fd158cfe117950c9126e68a63a5ff7c93bcee70be2a9686d1d22a322938d
        A/clauses/window-02/raw.json: 0bc49aa9246cab2104e02a0bfef3c2d5eeff57854cc0c2ac62c490ff230076cf
        A/clauses/window-02/prompt.txt: ffdc45aed53cb1c0418e660523d66aacc5025c72de3909349e06ff4d15ebff89
        A/clauses/window-02/meta.json: 71686e2340d124b42c7081bf283c33860a5deeebab5362a79a2bb465b8334a56
        A/clauses/window-07/raw.json: 4848e99856e44b6b96674b118cb62ca4a38cfe3faa8093ef282f84fc9a36e236
        A/clauses/window-07/prompt.txt: 16448dca9e96416f9df3472eee7922c678e2b191813bba34facea674b94c1444
        A/clauses/window-07/meta.json: 75ab136c1852571cd59d1a28d4949224c9e4247d0cef2978cf73e6313f9bf28f
        A/clauses/window-01/raw.json: 95049e88ac01d175ce6a8763409ca4f3255ef558089b323de806595fd7bbf77c
        A/clauses/window-01/prompt.txt: f9e7c448a0b534b3fb6e7a4893d036ca59df4d19214e26a00f6acbe9ea16128a
        A/clauses/window-01/meta.json: a79a7a9e64c9a88a473543a3acc2f36513d330f94d6f0a8dbeb38c60e46c2850
        A/clauses/window-06/raw.json: 4fecbbf7510ce4891fc02dbfe3f11a7cf2ebe320540789bcd8b562135634704d
        A/clauses/window-06/prompt.txt: 5d86ecdd2982e5edf8051e5820e96aeb644a4c20b6e793fe2d11d8636dc9407a
        A/clauses/window-06/meta.json: 16ed69bf8cb91c0cb6036c4ded446d9042d8a6782bea9c40dc784ea8cf5d24c6
        A/tables/TABLE-2-page-6-2/raw.json: f18bc408508b23d2d47643a9b02499a3409d5202156ee43af4782e31b7ff4bed
        A/tables/TABLE-2-page-6-2/prompt.txt: 683e68888a869922742863987d8f8ad5ad895a5d66476f339f457c0877c286a6
        A/tables/TABLE-2-page-6-2/meta.json: 27d80e33c0d28c4fc29a32b00de4e62be22907f1115de6ebd4ef68936c2e3704
        A/tables/TABLE-3-page-7-3/raw.json: 0588e0350438e7bf7cff47fecf7577dfcf78640811fd5a0a96c769ded098c4da
        A/tables/TABLE-3-page-7-3/prompt.txt: ff11898ebaf574a3064e7de2cbcd1889c8bf09ee1d74cf867db5fca65d2aa843
        A/tables/TABLE-3-page-7-3/meta.json: 135c906c50c8efa98c70b9ae632593e9593044d78139c24930928278fad7bc5c
        A/tables/TABLE-1-page-4-1/raw.json: 86d339b6b37f363bf3c471667be4c073395b269a5353b4d3e657d000afe71b9e
        A/tables/TABLE-1-page-4-1/prompt.txt: ddbe2933edbcea85eba7b8a9b73d78743cab41c66143ebefd39263e5774c6a2b
        A/tables/TABLE-1-page-4-1/meta.json: 1feac3c8161f66194f9581c1028653be6d4f22b94fc1f24a2a2a824a06a2a739
        B/passages.json: 80cc3cd09a9bd21a6a655998f904f0161516d638386099b77ce69bd38368258b
        B/raw.json: 405b1ac5b286b387cab55b7fc36395ab6cc3142fbf3e7c38dd2511822ea89489
        B/source-units.json: 11c33da8251a05845c2dc92072dfb550e601bd5590204b56dbb843d50f25def5
        B/full-source-units.json: 0b3408954dacb31cfc151f143615878c61cc6a5a7acd2134adf05cbe044a322c
        B/meta.json: e110e35f612f2fc7642f6b7d0459754d19455fa41b390475c2672806ee6a041f
        B/table-images/page-6.png: 4b3f153307d583b33a7755a3c5e29ac49f294736c56395e43f5f01a08b90b79d
        B/table-images/page-7.png: f467abcea0e6caa41833e33bc9f7ccc56f16949947272fbbdff63ce4696ef4ea
        B/table-images/page-4.png: ccccc5b9cb5d714d2d9ead82f142fff3bba466cc770fd5b12ea3469490adebe5
        B/table-images/TABLE-1-page-4-1.png: 7d2297fe26a696f040eab96ded49393de458998e6efa7e5a96b9535547f872fe
        B/table-images/TABLE-2-page-6-1.png: e4683a92f27599239cf9b0680f26a71681d4bef37844cf280c9a30a841788837
        B/table-images/manifest.json: ee3aca46e82734af4929db15ef73c4078ac20dbdbe975debf40ef822b1b490ce
        B/table-images/TABLE-3-page-7-1.png: f7172106ab1d01c25d9a85b347b11b1707f8306fd38e625269aa5c460fdaa855
        B/clauses/window-03/raw.json: d39d1d1cbbc766d1c57581d6d4715221a4f8985427e23a89dbe455c36f7cbe58
        B/clauses/window-03/prompt.txt: 7f139f181b3892a24cb34450284c9e811d430f39cd6167fbd46fcbfb2e4c4220
        B/clauses/window-03/meta.json: c2925dd2291f6d40bef91ae1d274de796f8e7a533323b2880f67f5653f23496e
        B/clauses/window-04/raw.json: e0b67568a64517caa6feeb5df8fe8276434d8f48512ad164346e38f91daf33d6
        B/clauses/window-04/prompt.txt: dc8a3f75f78d3dbe007395b6d7256fdfa29799e24d3809988982f6f0bd7ba0b2
        B/clauses/window-04/meta.json: fe6b667717439f1b75ab417b046321cf526ceb80d9f94a1df8a196caba5af971
        B/clauses/window-05/raw.json: 90aad1ce492a7c0b6a87296ea371d48a99b23af4c97f12c48b95618c4fdc3b3f
        B/clauses/window-05/prompt.txt: cceb7d5ad990a63aa8515c095ee0f7c84d5a2671d7781c8a7efd981d4dad1e76
        B/clauses/window-05/meta.json: 96321fdcbebbc9c7b14e4cfc2fb5980a5d5bf00ee8e79255017fbf34b72c1942
        B/clauses/window-02/raw.json: 104e5182ec6bf5356a985d6b74eb287f1121bd6c5c8afff3c7bbac9b046bc668
        B/clauses/window-02/prompt.txt: ffdc45aed53cb1c0418e660523d66aacc5025c72de3909349e06ff4d15ebff89
        B/clauses/window-02/meta.json: 97460bf71215c9c5fe7178b1c3c02d2e5c32917fc974a419c37b767441974b5d
        B/clauses/window-07/raw.json: ab271f7d155d5a6032a9fbce57e054379e6660fc7e721f34df85488083fb8b9f
        B/clauses/window-07/prompt.txt: 16448dca9e96416f9df3472eee7922c678e2b191813bba34facea674b94c1444
        B/clauses/window-07/meta.json: 8aee33a9ea1daa7eed75036aeeb24d5cd6cd533ede1cd3db27b868ecb4bddc3e
        B/clauses/window-01/raw.json: a50b889bb0eea6c28066aaa59bb7a6063b0ab56083a670584ba1b1bb90be4dcd
        B/clauses/window-01/prompt.txt: f9e7c448a0b534b3fb6e7a4893d036ca59df4d19214e26a00f6acbe9ea16128a
        B/clauses/window-01/meta.json: 9b4a43efb1f27f55bc97d77c1d144256e78ff2bee8b490d516b6ba950f8fef0f
        B/clauses/window-06/raw.json: 2ead7ce1183d77ecb9b36c1a5d3f2404e5879de7ec4222d65b4c514cd2e19534
        B/clauses/window-06/prompt.txt: 5d86ecdd2982e5edf8051e5820e96aeb644a4c20b6e793fe2d11d8636dc9407a
        B/clauses/window-06/meta.json: 008416f7ea091bd85496bb39493c0aca11923e3bda1691dd18e1fcedc58dfdf2
        B/tables/TABLE-2-page-6-2/raw.json: 9e0c49c31f54b23fe937ae3674bbcc9d10c22fe38d68d0e4dbf064cf1049caa7
        B/tables/TABLE-2-page-6-2/prompt.txt: 683e68888a869922742863987d8f8ad5ad895a5d66476f339f457c0877c286a6
        B/tables/TABLE-2-page-6-2/meta.json: f3990209c2d60b619f55819c47791736240af8bc37ed1e0fe763bd633a27d198
        B/tables/TABLE-3-page-7-3/raw.json: e061c35c89defbc768407663bed8967908a02a684e4e419e1cd30252267483c1
        B/tables/TABLE-3-page-7-3/prompt.txt: ff11898ebaf574a3064e7de2cbcd1889c8bf09ee1d74cf867db5fca65d2aa843
        B/tables/TABLE-3-page-7-3/meta.json: ba4643fae513cd4bf849d5df5b54940cda7ebed605faa63d2a9c118d12b6d051
        B/tables/TABLE-1-page-4-1/raw.json: c7aa931cf30004bbd50ae263883d71d5d0031fd7bb88bae85c5da6722d211e76
        B/tables/TABLE-1-page-4-1/prompt.txt: ddbe2933edbcea85eba7b8a9b73d78743cab41c66143ebefd39263e5774c6a2b
        B/tables/TABLE-1-page-4-1/meta.json: 64e691f29223ae9cab73d20c045fff38188944658547c5b5db2f36a7685c676f
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
      pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2020
      source_status_sha256: 1766406ba4c824589c852e5a2053129ed96b29e45ed2255e5f31bd1c2f5135ff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: time (acute to subacute phase)
    outcome:
      text: comprehension, repetition, and naming subscores
    analysis_label: Subscore improvement analysis
    relation: association
    evidence_ids:
    - P5-S1-C8
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
      pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2020
      source_status_sha256: 1766406ba4c824589c852e5a2053129ed96b29e45ed2255e5f31bd1c2f5135ff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C17
      - Accounting without a linked unit P5-S2-C10
      - Accounting without a linked unit P5-S2-C11
      - Accounting without a linked unit P5-S2-C13
      - Accounting without a linked unit P5-S2-C6
      - Accounting without a linked unit P5-S2-C8
      - Accounting without a linked unit P5-S2-C9
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C9
      - Unaccounted source passage P5-S2-C10
      - Unaccounted source passage P5-S2-C11
      - Unaccounted source passage P5-S1-C17
      - Unaccounted source passage P5-S2-C13
      - Unaccounted source passage P5-S2-C8
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C7
      - Result passage disposed without unit P5-S3-C8
      - Result passage disposed without unit P5-S3-C9
      - Result passage disposed without unit P5-S3-C11
      - Result passage disposed without unit P5-S3-C13
      - Accounting without a linked unit P7-S1-C4
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S2-C1
      - Accounting without a linked unit P7-S2-C2
      - Unaccounted source passage P7-S1-C4
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C1
      - Result passage disposed without unit P7-S2-C5
      unattached_null_or_qualifier_ids:
      - P5-S2-C8
      - P5-S2-C10
      - P5-S3-C4
      - P7-S1-C4
      - P7-S2-C2
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 141
      unselected_timing_passages:
      - P1-S2-C5
      - P3-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P1-S2-C1
      - P1-S2-C2
      - P1-S2-C3
      - P1-S2-C4
      - P1-S2-C5
      - P1-S2-C6
      - P1-S2-C7
      - P1-S2-C8
      - P1-S2-C9
      - P1-S2-C10
      - P1-S2-C11
      - P1-S2-C12
      - P1-S2-C13
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2020
      source_status_sha256: 1766406ba4c824589c852e5a2053129ed96b29e45ed2255e5f31bd1c2f5135ff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C9
      disposition: represented
      result_indexes:
      - 3
      reason: States FA from right AF was a significant predictor of early subacute
        aphasia outcome.
    - source_id: P1-S2-C10
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Discusses hierarchical models and the variance accounted for by initial
        aphasia severity.
    - source_id: P1-S2-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Concludes initial aphasia severity was the best predictor.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the statistical test used (Wilcoxon signed rank test).
    - source_id: P4-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes normality test results.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual participant trends (deterioration vs improvement).
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean CS scores.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant overall improvement in language functioning.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean percentage of recovery.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant improvement in all three subscores.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports positive correlation between achieved and potential 1CS.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies the significant model from backwards regression.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies variables in the backwards regression model.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies rFA as the only significant beta coefficient in the backwards
        model.
    - source_id: P5-S1-C15
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates rFA's inclusion in hierarchical regression.
    - source_id: P5-S1-C17
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant correlations of CS initial, lesion load, and lesion
        size with CSsubacute.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports significance and variance for univariate regressions.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports results for the first block of hierarchical analysis.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports effect of adding lesion load to the model.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Reports effect of adding lesion size to the model.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Reports variance change when adding rFA.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 9
      reason: States the rFA variance changes were not significant.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports VIF results for collinearity.
    - source_id: P5-S3-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of improvement in language performance.
    - source_id: P5-S3-C6
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of correlation between achieved and potential
        recovery.
    - source_id: P5-S3-C7
      disposition: repeated
      result_indexes:
      - 10
      - 11
      reason: Discussion restatement of the most successful model combination.
    - source_id: P5-S3-C8
      disposition: repeated
      result_indexes:
      - 10
      - 11
      reason: Discussion restatement of variance prediction.
    - source_id: P5-S3-C9
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement that initial severity was the best predictor.
    - source_id: P5-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about capturing the recovery process.
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about higher initial severity and recovery space.
    - source_id: P5-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about lower initial severity patients.
    - source_id: P5-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Speculative statement on factors contributing to recovery.
    - source_id: P5-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Speculative statement on reasons for recovery variability.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports univariate regression significance.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports hierarchical block 1 results.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports effect of lesion load in hierarchical model.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Reports effect of lesion size in hierarchical model.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Reports rFA variance change.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 9
      reason: Reports non-significance of rFA variance change.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 9
      reason: Restates that rFA involvement is less significant in multivariate models.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 12
      reason: States left AF structural integrity does not account for early outcomes.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Restates left AF does not account for early outcomes.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 13
      reason: States only right AF predicts better outcomes in acute/subacute phase.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Restates that linguistic assessments and lesion measures explain outcomes.
    unresolved_coverage:
    - source_id: P5-S3-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C9
    - P1-S2-C10
    - P1-S2-C11
    - P4-S1-C6
    - P4-S2-C1
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C7
    - P5-S1-C15
    - P5-S2-C9
    - P5-S3-C4
    - P5-S3-C5
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C8
    - P5-S3-C9
    - P5-S3-C11
    - P5-S3-C12
    - P5-S3-C13
    - P7-S1-C4
    - P7-S2-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C1
      recruited_sample:
      - P3-S1-C1
      eligibility:
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C9
      - P3-S1-C10
      imaging_provenance:
      - P3-S2-C8
      - P3-S2-C9
      imaging_timing:
      - P3-S2-C8
      outcome_timing:
      - P3-S1-C5
      outcome_definition:
      - P3-S2-C6
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S2-C8
      - P4-S2-C11
      - P5-S2-C3
      - P5-S2-C4
      limitations:
      - P7-S2-C3
      - P7-S2-C4
      - P7-S2-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C11
      - P5-S2-C4
      - P5-S2-C7
      - P5-S2-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C1
      - P4-S1-C2
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
      review_sha256: 8c2734a5d584e66f2b60546c0d73b99074a18e41c571ed0fdfe9e34b694e035f
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
      - P5-S1-C8
      source_result: All three subscores (comprehension, repetition, and naming) significantly
        improved between the initial assessment (<72h) and the follow-up (10-14 days)
        in 20 patients with post-stroke aphasia, as evidenced by Wilcoxon signed-rank
        tests and a paired-sample t-test.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the paired comparison of language
            subscores between acute and subacute phases, as described in P5-S1-C8
            and P4-S1-C5.
          source_ids:
          - P5-S1-C8
          - P4-S1-C5
        direction:
          answer: fits
          reason: The source explicitly states that all three subscores significantly
            improved, which aligns with the proposed claim of improvement.
          source_ids:
          - P5-S1-C8
        construct:
          answer: fits
          reason: The exposure is time (acute to subacute), the outcome is language
            subscores, and the measurement is behavioral (non-imaging), consistent
            with the source.
          source_ids:
          - P5-S1-C8
          - P3-S1-C13
        qualifications:
          answer: fits
          reason: The draft includes the qualification that three participants deteriorated,
            which is a material caveat from P5-S1-C4.
          source_ids:
          - P5-S1-C4
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing; the small sample size limitation
            is noted, and the deterioration of three participants is included.
          source_ids:
          - P7-S2-C3
          - P5-S1-C4
      optional_pending:
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.time_post_onset
      original: initial assessment <72 hours after stroke onset and follow-up 7-15
        days later
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 15, 7, 72'
    analysis_identity:
      id: R002
      exposure:
        text: time (acute to subacute phase)
      outcome:
        text: comprehension, repetition, and naming subscores
      analysis_label: Subscore improvement analysis
      relation: association
      evidence_ids:
      - P5-S1-C8
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
        pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
        source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2020
        source_status_sha256: 1766406ba4c824589c852e5a2053129ed96b29e45ed2255e5f31bd1c2f5135ff
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0d9178fb5baaad83213476fdae87efd9fa458065f66b3148993dc1ac6ed04669
          exclusions_sha256: 3e51a8bdd09175d3f3e00426c92f9d1c63765cdfcb00bcf16340be83db1cf7dc
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: 6159ecc5d42f2c5f33587345f81e46d37716fb811330d4acf999fca1d2b85f32
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '

          Osa García et al.

          Predicting Early Aphasia Outcome

          MATERIALS AND METHODS

          Participants

          Twenty participants took part in this study (5 women; mean

          age: 71.6 ± 12.45 years; mean education: 10.05 ± 5.04).'
        anchor_text: 'MATERIALS AND METHODS

          Participants

          Twenty participants took part in this study (5 women; mean

          age: 71.6 ± 12.45 years; mean education: 10.05 ± 5.04).'
        excluded_fragments:
        - where: leading
          text: Osa García et al.
          furniture_line: Osa García et al.
          bbox:
          - 44.8
          - 29.5
          - 94.7
          - 36.4
          rule: repeated margin line
        - where: leading
          text: Predicting Early Aphasia Outcome
          furniture_line: Predicting Early Aphasia Outcome
          bbox:
          - 448.3
          - 29.5
          - 550.4
          - 36.4
          rule: repeated margin line
        image_sha256: 475a8987038fe4c1f75fc24751e0e5bd48fe2e31fe96c565d0dc21074721b233
        transcription: 'MATERIALS AND METHODS

          Participants

          Twenty participants took part in this study (5 women; mean

          age: 71.6 ± 12.45 years; mean education: 10.05 ± 5.04)'
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 17a0e2cbfaec8e15ca57cb6cab5934426f6a11205bd0ba2de0489005fb7701e0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0389a95b9d95c0b7074f7df17cb28494fe64bfa37c113ab536bfe3094cd2267d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 0389a95b9d95c0b7074f7df17cb28494fe64bfa37c113ab536bfe3094cd2267d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Initial language assessments took place within the ﬁrst

          72 h (mean = 2.3 days) after stroke onset, and the follow-

          up took place 7–15 days later (mean = 10.55 days).'
        anchor_text: 'Initial language assessments took place within the ﬁrst

          72 h (mean = 2.3 days) after stroke onset, and the follow-

          up took place 7–15 days later (mean = 10.55 days).'
        excluded_fragments: []
        image_sha256: b9a4d1ab4fde58e388a5ff18976fb0237bc6ee0fd3b22693d7a3606c7e699217
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'All three subscores (i.e., comprehension,

    repetition and naming) signiﬁcantly improved between the initial

    assessment and the follow-up (Comprehension Wilcoxon signed

    ranks test, Z = 3.771, P < 0.001; Repetition Wilcoxon signed

    ranks test, Z = −3.115, P = 0.002; Naming paired-sample t-

    test = −2.329, df = 18, P = 0.031).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
