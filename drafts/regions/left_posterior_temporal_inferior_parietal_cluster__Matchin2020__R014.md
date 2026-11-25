---
id: left_posterior_temporal_inferior_parietal_cluster
name: left posterior temporal and inferior parietal cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: paragrammatism
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: paragrammatism
  target_kind: impairment
  claim: paragrammatism was associated with damage to the left posterior temporal
    and inferior parietal cortex, centered on the posterior superior temporal gyrus
    and middle temporal gyrus, including the inferior and posterior parts of the supramarginal
    gyrus
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 53
    population: right-handed patients with aphasia following chronic left-hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: at least six months poststroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - analysis excluded patients with severely limited speech output or reduced intelligibility
    due to motor speech problems or severe aphasia
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: patient lesion overlap with a voxel-based cluster
    centered on the left posterior superior temporal gyrus and middle temporal gyrus,
    including the inferior and posterior parts of the supramarginal gyrus. association
    remained when regressing out the effects of lesion volume and speech rate (words
    per minute). Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P4-S2-C5, two-model agreement, human
    verification pending): Of the 100 original subjects, we successfully rated 53,
    and these were included in the following analyses Original text-layer quotation
    is preserved below. PDF image reading (P4-S2-C6, two-model agreement, human verification
    pending): . Forty-seven subjects were unable to be rated due to audio quality
    issues (N = 2) or severely limited speech output or reduced intelligibility as
    a result of concomitant motor speech problems (apraxia of speech and/or dysarthria)
    or severe aphasia (N = 45) Original text-layer quotation is preserved below. PDF
    image reading (P1-S1-C6, two-model agreement, human verification pending): . Four
    expert raters assessed videos of 53 right-handed patients with aphasia following
    chronic left-hemisphere stroke retelling the Cinderella story Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:paragrammatism
  citation: '@Matchin2020'
  source_passages:
  - section: Original source P11-S1-C4
    page: 11
    quote: 'PARAGRAMMATISM (Figure 4, cool colors) was associated with

      damage to left posterior temporal and inferior parietal cortex, centered on
      the posterior supe-

      rior temporal gyrus and middle temporal gyrus, including the inferior and posterior
      parts of

      the SMG.'
    supports: claim
  - section: Original source P11-S1-C5
    page: 11
    quote: 'Overall, regressing out the effect of speech rate (WPM) reduced the strength
      and

      the spatial extent of the damage associated with AGRAMMATISM and PARAGRAMMATISM
      while

      maintaining essentially the same spatial location.'
    supports: confounders
  - section: Original source P3-S2-C6
    page: 3
    quote: 'All subjects had a single ischemic stroke to the left

      hemisphere at least six months prior to study inclusion and were also premorbidly
      right-

      handed (self-disclosed).'
    supports: sample
  - section: Original source P4-S2-C5
    page: 4
    quote: 'Of the 100 original subjects, we successfully rated 53, and these were
      included in the fol-

      lowing analyses.'
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Forty-seven subjects were unable to be rated due to audio quality issues
      (N =

      2) or severely limited speech output or reduced intelligibility as a result
      of concomitant motor

      speech problems (apraxia of speech and/or dysarthria) or severe aphasia (N =
      45).'
    supports: limitation
  - section: Original source P9-S1-C10
    page: 9
    quote: 'Whole-Brain Analyses

      We performed corresponding whole-brain analyses in NiiStat (https://www.nitrc.org/projects/

      niistat/), using binary logistic regression to remove effects of (i) lesion
      volume only and (ii) le-

      sion volume and speech rate (WPM) from the behavioral classifications.'
    supports: method
  - section: Original source P1-S1-C6
    page: 1
    quote: 'Four expert raters assessed videos of 53 right-handed patients with

      aphasia following chronic left-hemisphere stroke retelling the Cinderella story.'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Matchin2020
  proposal_id: R014
  review_status_sha256: 24c8abf02b3428f1402b01cbb49e25bbf67a80ef4b78d2165e2f86dd13a849d4
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
        A/passages.json: c6b8def78994f7306972f00e7a6ea88c36b5bd0672eab657fa816da23803e534
        A/raw.json: 04af200d581b308b514198635d543440da0623c926a969c47f6fc378cffda28d
        A/source-units.json: 2f78ad22b26509347f473df2be0c3f9e394d32ee951ebbbf78444725d74c5d23
        A/full-source-units.json: 15be2f3f191b4adc676d591478757c19c8b05b415910dd979eab9fc7d71b65b4
        A/meta.json: 856aa35e37f8a0a19de2a949460450efb226750ed1b3e64ec93568d3f9428818
        A/table-images/TABLE-1-page-5-1.png: aa87e258dbcad57f87f50bd1e4c9e574b0a71d060359293c49294256cea9cb11
        A/table-images/page-12.png: 19b178d6afa05c766f95b2dc9ff4c94fc05f4fe13c042e834aa38ba6570dcb5e
        A/table-images/page-5.png: 6df7a6c2532422343bbb8f9f8d1fb1d9cdee76f3f35daa0b27b91f425fdefbb9
        A/table-images/manifest.json: fdd5a1181f9b914e51a6feeddb32d63b9f3a1427aeff5307e41e10831cd1603d
        A/table-images/TABLE-2-page-12-1.png: b4568ec60a362db28c27f426293bda04cff2796ed994a35328a90067d71478ea
        A/clauses/window-03/raw.json: 18e65a221412a4d74f8b22a84f3d92477b595c1dcabfa55c6d543d6b6baab07f
        A/clauses/window-03/prompt.txt: 1a2090d571641d14351a0a4c0587ce4a6b9339d5610d6072f7aff60bfe5e3e5d
        A/clauses/window-03/meta.json: 8f67d13f5e41d524aae4d91d58b0194e7bd4a56e14f18ba758cb7d35efca280c
        A/clauses/window-04/raw.json: cc9f64ddee99d04f103ca4618b9b4604b16f68ae9c6284542769d0408f355b3e
        A/clauses/window-04/prompt.txt: 16e9a051261ae963b321491279f1a5cdbf7ef7e9d5ff0a3d3d800d96d6b75c02
        A/clauses/window-04/meta.json: 2d258e5713f48c287017331a7929105f9e3b00eae74e0adcd513489453c19caf
        A/clauses/window-05/raw.json: 04819fe0942222967c8f8e8a723c04d7d5c2e8e91e047eb14dca6c285b33f1bd
        A/clauses/window-05/prompt.txt: c2f66ca3121898401ae8a9a32378524d8b5026fc06bf4b7ae1d8011d86590a87
        A/clauses/window-05/meta.json: 9b3c9003057601f97da4d69dd64b9fe1dea1902cc57f62756242edef8cf8cec8
        A/clauses/window-02/raw.json: 2df7a986af16dbdeb4043d7b928717a64f3adb79afcfd0a0a07e63e35cdd2b9e
        A/clauses/window-02/prompt.txt: bd377be0516759010171a82cdbdc0501844651b5269c1f42c05a7bb501672f37
        A/clauses/window-02/meta.json: b0a3214ff2e5b100f92fadb3d92e9e4ac608e1ea49427687e2990e41b5bdf078
        A/clauses/window-07/raw.json: 6b6b727afa0cf56f217354fe0fc4d592baa589d4c89449088b1eeb74fbbb9bf3
        A/clauses/window-07/prompt.txt: a47baddcde4af2d3c92c968fc13bba90ef872bcfac76de08b2aa58d2064f83e9
        A/clauses/window-07/meta.json: 78d871055ea15d3b2bf389372db34d3e581138e38c3afcfc287c4720a50eca5d
        A/clauses/window-01/raw.json: e2f4fb059e311d977d51425b473bb32f792979e97a5681102e82f54328331874
        A/clauses/window-01/prompt.txt: 253e3844d6a1857a4f897c426d3eff34266e59a58991b0fdf8482887db90189f
        A/clauses/window-01/meta.json: 4ffa2a42f8bf7165419475c86793d2ef56b6a7a267738f8880440bddb011919f
        A/clauses/window-06/raw.json: ad5ef7659ef3133dd2dedf8be6ad2f2f677992317ded7633d2d3c110aa877245
        A/clauses/window-06/prompt.txt: f4d6fa7fd7b0cfdbcfb3d8422dca3d5d9171c1324a93af1bd8c11d3f38c064ff
        A/clauses/window-06/meta.json: 2be57caf8259a1b74b10f677527e55509a6532db40a24cef32a7d51f16e5433e
        A/clauses/window-08/raw.json: 3e6026f5374196a3f3dbb9a5d3c511d3962e3903887711430e4dbc8c41fcf067
        A/clauses/window-08/prompt.txt: bc3b837bec676d07b5664faff14d760188b3f61df28f9767e569f1b1f5c968cb
        A/clauses/window-08/meta.json: 7d4e7e7d73f30873d23a1a844da83fa996e6e71c206171fa578c315fef240292
        A/tables/TABLE-1-page-5-1/raw.json: 2502dfc169831aa454250062157c34290f9dee65dce5498d6bfed3a273b38995
        A/tables/TABLE-1-page-5-1/prompt.txt: 02db2d9f9fea8ad5c0089af317d0b27142e8a73dc3079c8443391f181ced0b61
        A/tables/TABLE-1-page-5-1/meta.json: 172944afbcc347db33a6a1d2f92df1340afa9810a30493f160b86fd0ee101daf
        A/tables/TABLE-2-page-12-2/raw.json: 53273099ba499604c3a2ca50ff91be0dd3ee1a0f56e4c2455d42d7d52aa92c1c
        A/tables/TABLE-2-page-12-2/prompt.txt: 3aea92d93b510f26f0d18b01a255b81cdb3a307647036dff7f594c6c3706ac61
        A/tables/TABLE-2-page-12-2/meta.json: 3adca51798eed564020fd55db74681a44f09392893a648e408a70f259070d567
        B/passages.json: c6b8def78994f7306972f00e7a6ea88c36b5bd0672eab657fa816da23803e534
        B/raw.json: 76fef0d72e9af7fdf0eeb96569a8c0a8e3d221ba1b61b3d4bf42edd57d5cefe7
        B/source-units.json: 2f78ad22b26509347f473df2be0c3f9e394d32ee951ebbbf78444725d74c5d23
        B/full-source-units.json: 15be2f3f191b4adc676d591478757c19c8b05b415910dd979eab9fc7d71b65b4
        B/meta.json: 7ca19717f8a09fcf0b30a02e16334a0410b7e2a794a13143d3951b2fc5d1c8c7
        B/table-images/TABLE-1-page-5-1.png: aa87e258dbcad57f87f50bd1e4c9e574b0a71d060359293c49294256cea9cb11
        B/table-images/page-12.png: 19b178d6afa05c766f95b2dc9ff4c94fc05f4fe13c042e834aa38ba6570dcb5e
        B/table-images/page-5.png: 6df7a6c2532422343bbb8f9f8d1fb1d9cdee76f3f35daa0b27b91f425fdefbb9
        B/table-images/manifest.json: ba46e732a7a3c184f8ca564de021b734edd810a0f4b526fa5cd8c40168af7500
        B/table-images/TABLE-2-page-12-1.png: b4568ec60a362db28c27f426293bda04cff2796ed994a35328a90067d71478ea
        B/clauses/window-03/raw.json: d816de1778178868a6fda07ccba3fce93238d9d245c1810616e5cce82d675bef
        B/clauses/window-03/prompt.txt: 1a2090d571641d14351a0a4c0587ce4a6b9339d5610d6072f7aff60bfe5e3e5d
        B/clauses/window-03/meta.json: 2d01d92d171833d4b8cf6887d3f8397b88ff4971a202c6c4937a8a8896973440
        B/clauses/window-04/raw.json: 4506317c84def27c528771ebbea7a32100dcf7d4120773eb11fa6cccb7365bd4
        B/clauses/window-04/prompt.txt: 16e9a051261ae963b321491279f1a5cdbf7ef7e9d5ff0a3d3d800d96d6b75c02
        B/clauses/window-04/meta.json: 42cf19a82e55f5696c5bace1f399f482c3d8cc13e0b46e110c69e5830e45d94a
        B/clauses/window-05/raw.json: 04af1c022612e9c5945063418755c4a8397edfacc9bdf9d46a1358577d5c59be
        B/clauses/window-05/prompt.txt: c2f66ca3121898401ae8a9a32378524d8b5026fc06bf4b7ae1d8011d86590a87
        B/clauses/window-05/meta.json: f31cb1b7074149f62cd98f04366256aedb41bae31663a0a171e4eff9c99acd44
        B/clauses/window-02/raw.json: ddcd2ceaffe398b3c8147b349f3c73af9b7727970b55bfaba7b6025710e576a1
        B/clauses/window-02/prompt.txt: bd377be0516759010171a82cdbdc0501844651b5269c1f42c05a7bb501672f37
        B/clauses/window-02/meta.json: 7398e441f19ff7e580f7442766092ea7c73cad5b33d991e1df4b53afa9e545e1
        B/clauses/window-07/raw.json: e90e416e836074a3fa0ed0ab2314b087b82612a3c31d671a78544cde53b4cb7c
        B/clauses/window-07/prompt.txt: a47baddcde4af2d3c92c968fc13bba90ef872bcfac76de08b2aa58d2064f83e9
        B/clauses/window-07/meta.json: 7cf7ed3b880d67b910db47c1d0d086966a2994dea55fadbf1b8d22f88b02e0e6
        B/clauses/window-01/raw.json: 90be316e6127ac10a972ecc43814849d755f53d09fcdbe1729c52b59cf3dbfe5
        B/clauses/window-01/prompt.txt: 253e3844d6a1857a4f897c426d3eff34266e59a58991b0fdf8482887db90189f
        B/clauses/window-01/meta.json: 2042b12327e4e9144e808e546204f85da97631c8b6711d7982c9acd206f3cb2c
        B/clauses/window-06/raw.json: 6cd103f94c7a170df93ee5d380f834709c5c00a1fa2c9d8898a71a740be2489f
        B/clauses/window-06/prompt.txt: f4d6fa7fd7b0cfdbcfb3d8422dca3d5d9171c1324a93af1bd8c11d3f38c064ff
        B/clauses/window-06/meta.json: 952a762242c3a44893531485ae243cf59f2dd7a027c8b5015d6805ffd0a05c30
        B/clauses/window-08/raw.json: 67e0fa26738bc933c97540e600ac0c6dd0f75b4d25014674bc2d07decfb83817
        B/clauses/window-08/prompt.txt: bc3b837bec676d07b5664faff14d760188b3f61df28f9767e569f1b1f5c968cb
        B/clauses/window-08/meta.json: c23426619d9d90849d2458cacce1b9b431805cfedce490b7e591dd8884fd7ea0
        B/tables/TABLE-1-page-5-1/raw.json: 938fd1122a1ef0368b08547a27ccd966e5856ce35a5c9bd0070b223be6971f1a
        B/tables/TABLE-1-page-5-1/prompt.txt: 02db2d9f9fea8ad5c0089af317d0b27142e8a73dc3079c8443391f181ced0b61
        B/tables/TABLE-1-page-5-1/meta.json: 5f8201f368f0e755e63e7492351c4a568329abf388e3c8fd927bfda7f7fc6f39
        B/tables/TABLE-2-page-12-2/raw.json: 4b52dad1faa8203e7657cdec287825944d7323d77989e1c22f8238483ec04195
        B/tables/TABLE-2-page-12-2/prompt.txt: 3aea92d93b510f26f0d18b01a255b81cdb3a307647036dff7f594c6c3706ac61
        B/tables/TABLE-2-page-12-2/meta.json: 4ea947f6de7ec458c04707219741cbecc41f1b9d34a42ec70f1bba88bde82c92
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
      pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2020
      source_status_sha256: 64905e6a9f43fdd7a526c11a6f1022377deedd6e949d24520c9506489eb8e34a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R014
    exposure:
      text: damage to left posterior temporal and inferior parietal cortex (pSTG,
        MTG, inferior and posterior SMG)
    outcome:
      text: PARAGRAMMATISM
    analysis_label: Whole-brain analysis (lesion volume and speech rate covariates)
    relation: sensitivity
    evidence_ids:
    - P11-S1-C4
    - P11-S1-C5
    qualifier_ids:
    - P9-S1-C10
    - P11-S1-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2020
      source_status_sha256: 64905e6a9f43fdd7a526c11a6f1022377deedd6e949d24520c9506489eb8e34a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S2-C10
      - Result passage disposed without unit P4-S2-C11
      - 'window 4: invalid/duplicate disposition P7-S1-C1'
      - Accounting without a linked unit P9-S1-C7
      - Accounting without a linked unit P9-S2-C10
      - Accounting without a linked unit P9-S2-C6
      - Unaccounted source passage P9-S2-C6
      - Unaccounted source passage P9-S1-C7
      - Unaccounted source passage P9-S2-C10
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C11
      - Result passage disposed without unit P11-S2-C1
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P13-S1-C2
      - Result passage disposed without unit P13-S2-C3
      - Result passage disposed without unit P13-S2-C7
      - Result passage disposed without unit P13-S2-C9
      - Result passage disposed without unit P14-S1-C7
      - Accounting without a linked unit P14-S2-C10
      - Result passage disposed without unit P14-S2-C7
      - Unaccounted source passage P14-S2-C10
      - Result passage disposed without unit P15-S1-C1
      - Accounting without a linked unit P15-S1-C10
      - Result passage disposed without unit P15-S1-C4
      - Accounting without a linked unit P15-S1-C6
      - Unaccounted source passage P15-S1-C10
      - Unaccounted source passage P15-S1-C6
      - Result passage disposed without unit P15-S2-C6
      unattached_null_or_qualifier_ids:
      - P4-S2-C12
      - P5-S1-C1
      - P9-S2-C10
      - P11-S1-C11
      - P11-S2-C2
      - P14-S2-C10
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 176
      unselected_timing_passages:
      - P1-S1-C6
      - P3-S2-C3
      - P3-S2-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P11-S1-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P3-S1-C9
        - P4-S2-C11
        - P9-S1-C4
        - P9-S1-C10
        - P10-S1-C1
        - P11-S1-C3
        - P14-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-12-2
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-12-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P8-S1
        - P9-S2
        - P10-S1
        - P11-S1
        - P11-S2
        - P12-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2020
      source_status_sha256: 64905e6a9f43fdd7a526c11a6f1022377deedd6e949d24520c9506489eb8e34a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Reports ROI double dissociation results.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: States results held when regressing out speech rate.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides group counts.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides group counts.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general aphasia subtype associations.
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes covariate selection.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides qualitative examples.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides qualitative examples.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group inclusion.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides qualitative examples.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides qualitative examples.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater reliability kappa.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater reliability kappa.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater reliability kappa.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater reliability kappa.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes fluency trends.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes fluency trends.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes fluency trends.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports homogeneity of variance test.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports homogeneity of variance test.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Reports ROI double dissociation results.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: Reports ROI results with speech rate covariate.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 4.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 8
      - 12
      reason: Reports whole-brain associations for AGRAMMATISM.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 9
      - 13
      reason: Reports whole-brain association for AGRAMMATISM and its loss after WPM
        covariate.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 10
      - 14
      reason: Reports whole-brain associations for PARAGRAMMATISM.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 12
      - 14
      reason: Describes effect of WPM covariate on whole-brain results.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of spatial overlap.
    - source_id: P11-S1-C10
      disposition: represented
      result_indexes:
      - 15
      reason: Reports association of reduced WPM with brain damage.
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 16
      reason: Reports overlap between reduced WPM and AGRAMMATISM.
    - source_id: P11-S2-C1
      disposition: repeated
      result_indexes:
      - 16
      reason: Repeats overlap finding.
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Reports results after regressing WPM.
    - source_id: P11-S2-C3
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Specifies brain regions for reduced WPM and AGRAMMATISM after regression.
    - source_id: P13-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Restatement of ROI results in discussion.
    - source_id: P13-S1-C2
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: Restatement of ROI results with WPM covariate.
    - source_id: P13-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: Restatement of ROI results with WPM covariate.
    - source_id: P13-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses nature of paragrammatic errors.
    - source_id: P13-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates interrater agreement.
    - source_id: P14-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      reason: Restatement of double dissociation in discussion.
    - source_id: P14-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Restatement of agrammatism association.
    - source_id: P14-S2-C10
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      reason: Restatement of agrammatism association with WPM covariate.
    - source_id: P14-S2-C11
      disposition: repeated
      result_indexes:
      - 17
      reason: Restatement of reduced WPM association.
    - source_id: P15-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 1.
    - source_id: P15-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides group diagnosis counts.
    - source_id: P15-S1-C6
      disposition: represented
      result_indexes:
      - 19
      reason: Reports null association with ATL.
    - source_id: P15-S1-C10
      disposition: represented
      result_indexes:
      - 18
      reason: Reports association with ATL without lesion volume covariate.
    - source_id: P15-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      reason: Summary restatement of double dissociation.
    unresolved_coverage:
    - source_id: P13-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C10
    - P4-S2-C11
    - P4-S2-C12
    - P5-S1-C1
    - P5-S1-C4
    - P6-S1-C1
    - P7-S1-C1
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C7
    - P7-S2-C3
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P9-S1-C7
    - P9-S2-C6
    - P11-S1-C1
    - P11-S1-C6
    - P11-S2-C1
    - P11-S2-C2
    - P13-S1-C1
    - P13-S1-C2
    - P13-S1-C3
    - P13-S1-C4
    - P13-S2-C3
    - P13-S2-C7
    - P13-S2-C9
    - P14-S1-C7
    - P14-S2-C7
    - P14-S2-C10
    - P14-S2-C11
    - P15-S1-C1
    - P15-S1-C4
    - P15-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-12-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C6
      - P4-S2-C5
      - P8-S1-C19
      recruited_sample:
      - P3-S2-C3
      eligibility:
      - P3-S2-C6
      imaging_provenance:
      - P1-S1-C8
      - P8-S1-C11
      imaging_timing:
      - P3-S2-C6
      outcome_timing:
      - P3-S1-C4
      outcome_definition:
      - P1-S1-C7
      - P4-S1-C8
      - P4-S1-C11
      - P9-S1-C5
      validation: []
      analysis_restrictions:
      - P4-S2-C6
      - P15-S2-C2
      - P15-S2-C3
      - P15-S2-C4
      dependent_variable_statement:
      - P9-S1-C4
      - P9-S1-C5
      - P9-S1-C10
      - P11-S1-C9
      limitations:
      - P15-S2-C2
      - P15-S2-C3
      - P15-S2-C4
      personal_factors:
      - P5-S1-C2
      - P8-S1-C4
      - P15-S1-C4
      tested_personal_effects:
      - P11-S1-C10
      - P11-S1-C11
      - P14-S2-C10
      - P14-S2-C11
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C7
      - P5-S1-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P11-S1-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P3-S1-C9
      - P4-S2-C11
      - P9-S1-C4
      - P9-S1-C10
      - P10-S1-C1
      - P11-S1-C3
      - P14-S2-C10
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
      pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
      review_sha256: 24c8abf02b3428f1402b01cbb49e25bbf67a80ef4b78d2165e2f86dd13a849d4
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
      - P11-S1-C4
      - P11-S1-C5
      source_result: The source reports that paragrammatism was associated with damage
        to the left posterior temporal and inferior parietal cortex, specifically
        centered on the posterior superior temporal gyrus (pSTG) and middle temporal
        gyrus (MTG), including the inferior and posterior parts of the supramarginal
        gyrus (SMG). This association was identified in whole-brain voxel-based lesion-symptom
        mapping (VLSM) analyses. The association remained significant when regressing
        out the effects of lesion volume and speech rate (words per minute), although
        the spatial extent was reduced. The analysis involved 53 right-handed patients
        with chronic left-hemisphere stroke.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the whole-brain VLSM analysis
            for paragrammatism described in P11-S1-C4 and P11-S1-C5. The proposed
            core correctly identifies the outcome (paragrammatism) and the anatomical
            region (left posterior temporal/inferior parietal). The inclusion of covariates
            (lesion volume and speech rate) is consistent with the 'Whole-brain analysis
            (lesion volume and speech rate covariates)' label, as P11-S1-C5 confirms
            the pattern held after regressing out speech rate.
          source_ids:
          - P11-S1-C4
          - P11-S1-C5
          - P9-S1-C10
        direction:
          answer: fits
          reason: The source explicitly states that paragrammatism was 'associated
            with damage' to the specified regions (P11-S1-C4). The proposed core uses
            the direction 'likely' and the claim 'paragrammatism was associated with
            damage', which faithfully preserves the detected association without overclaiming
            causality or zero effect.
          source_ids:
          - P11-S1-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to the left posterior
            temporal and inferior parietal cortex (pSTG, MTG, SMG). The outcome is
            paragrammatism. The patient measurement is correctly classified as template_lesion_overlap,
            as the study uses VLSM where patient lesions are overlaid on standard
            space/voxel maps, rather than patient-specific diffusion tractography
            or functional imaging. The method is VLSM.
          source_ids:
          - P11-S1-C4
          - P9-S1-C10
          - P1-S1-C8
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the association
            remained when regressing out lesion volume and speech rate. This is supported
            by P11-S1-C5, which states that regressing out speech rate maintained
            the spatial location while reducing extent. The limitation regarding exclusion
            of patients with limited speech output is also correctly included, supported
            by P4-S2-C6.
          source_ids:
          - P11-S1-C5
          - P4-S2-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly notes the robustness
            to covariates and the sample restriction. The use of uncorrected thresholds
            (p < 0.05) is a methodological detail that does not change the qualitative
            nature of the detected association in this context, and the core is a
            qualitative draft. The distinction between ROI and whole-brain is handled
            by the analysis label.
          source_ids:
          - P9-S1-C11
          - P11-S1-C4
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
      id: R014
      exposure:
        text: damage to left posterior temporal and inferior parietal cortex (pSTG,
          MTG, inferior and posterior SMG)
      outcome:
        text: PARAGRAMMATISM
      analysis_label: Whole-brain analysis (lesion volume and speech rate covariates)
      relation: sensitivity
      evidence_ids:
      - P11-S1-C4
      - P11-S1-C5
      qualifier_ids:
      - P9-S1-C10
      - P11-S1-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
        source_review: _compare/relationships-2026-11-16/review-current/Matchin2020
        source_status_sha256: 64905e6a9f43fdd7a526c11a6f1022377deedd6e949d24520c9506489eb8e34a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0f56cf504301f7759f16c37124367665d916527150c814097aab338410151b8b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C5
          page: 4
          text_layer_sha256: 0f56cf504301f7759f16c37124367665d916527150c814097aab338410151b8b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Of the 100 original subjects, we successfully rated 53, and
          these were included in the fol-

          lowing analyses.'
        anchor_text: 'Of the 100 original subjects, we successfully rated 53, and
          these were included in the fol-

          lowing analyses.'
        excluded_fragments: []
        image_sha256: a7821f75516862d3d9c0a0190ea4583f70c605bdab96dc13238c4cacef2f4344
        transcription: Of the 100 original subjects, we successfully rated 53, and
          these were included in the following analyses
      P4-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2b47f9a18baae3b87cf8d7ca72f53616a094b3c061e008d1758053479cc1ed41
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C6
          page: 4
          text_layer_sha256: 2b47f9a18baae3b87cf8d7ca72f53616a094b3c061e008d1758053479cc1ed41
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Forty-seven subjects were unable to be rated due to audio
          quality issues (N =

          2) or severely limited speech output or reduced intelligibility as a result
          of concomitant motor

          speech problems (apraxia of speech and/or dysarthria) or severe aphasia
          (N = 45).'
        anchor_text: 'Forty-seven subjects were unable to be rated due to audio quality
          issues (N =

          2) or severely limited speech output or reduced intelligibility as a result
          of concomitant motor

          speech problems (apraxia of speech and/or dysarthria) or severe aphasia
          (N = 45).'
        excluded_fragments: []
        image_sha256: 3064e72c12915dd8354023702f9ce459f6c4c4df3ace850fb4452aef297cd92e
        transcription: . Forty-seven subjects were unable to be rated due to audio
          quality issues (N = 2) or severely limited speech output or reduced intelligibility
          as a result of concomitant motor speech problems (apraxia of speech and/or
          dysarthria) or severe aphasia (N = 45)
      P1-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3597baecfccf38759ec4f57b272f7ab62989e2514ba0001c94149a8ba2729973
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8121e61da7994899870b76d5dcafde88fbb70b4d5e6d57c19ff7cd13c2b0b62f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C6
          page: 1
          text_layer_sha256: 8121e61da7994899870b76d5dcafde88fbb70b4d5e6d57c19ff7cd13c2b0b62f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Four expert raters assessed videos of 53 right-handed patients
          with

          aphasia following chronic left-hemisphere stroke retelling the Cinderella
          story.'
        anchor_text: 'Four expert raters assessed videos of 53 right-handed patients
          with

          aphasia following chronic left-hemisphere stroke retelling the Cinderella
          story.'
        excluded_fragments: []
        image_sha256: c6cc9d2c3a31c05691ee05e5f70d5700f87d96a9eee64c67c908272f7405a373
        transcription: . Four expert raters assessed videos of 53 right-handed patients
          with aphasia following chronic left-hemisphere stroke retelling the Cinderella
          story
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'PARAGRAMMATISM (Figure 4, cool colors) was associated with

    damage to left posterior temporal and inferior parietal cortex, centered on the
    posterior supe-

    rior temporal gyrus and middle temporal gyrus, including the inferior and posterior
    parts of

    the SMG.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
