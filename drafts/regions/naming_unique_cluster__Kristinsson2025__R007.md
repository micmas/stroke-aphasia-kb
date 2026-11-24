---
id: naming_unique_cluster
name: naming unique cluster
kind: network
findings:
- id: f1
  target: naming
  target_kind: impairment
  claim: Bilateral superior frontal and parietal lobes, as well as subcortical regions
    including the caudate nucleus and putamen, were uniquely associated with naming
    performance, with these associations predominantly revealed in connectivity-based
    models.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 86
    population: participants with chronic (>12-month post-stroke) aphasia after left
      hemisphere strokes
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Language impairment quantified using only the WAB-R, which is described as a fairly
    coarse measure
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Brain regions identified as uniquely associated with
    naming performance (defined as having high beta coefficients for naming but low/negligible
    coefficients for other WAB-R subtests) across at least two modality-specific PLSR
    models, including connectivity-based models. Unique association defined by beta
    coefficients exceeding ±0.2 for naming and remaining below that threshold for
    other subtests; Findings reported only for regions identified in two or more modality-specific
    PLSR models. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P4-S1-C7, two-model agreement, human
    verification pending): . Therefore, the resulting cohort was com-

    posed of 86 participants and subsequent analyses refer to

    these 86 participants Original text-layer quotation is preserved below. PDF image
    reading (P1-S1-C6, two-model agreement, human verification pending): . A total
    of 86 participants with chronic (>12-month post-stroke) aphasia after left hemisphere
    strokes were examined Original text-layer quotation is preserved below.'
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
    - proposed_concept:naming
  citation: '@Kristinsson2025'
  source_passages:
  - section: Original source P10-S3-C7
    page: 10
    quote: "Several re­\ngions in the bilateral superior frontal and parietal lobes,\
      \ as \nwell as subcortical regions (e.g. caudate nucleus, putamen) \nwere uniquely\
      \ associated with naming performance."
    supports: claim
  - section: Original source P10-S3-C8
    page: 10
    quote: "These \nassociations were predominantly revealed in connectivity- \nbased\
      \ models."
    supports: claim
  - section: Original source P10-S3-C3
    page: 10
    quote: "In \norder to prevent spurious findings, we report regional task \nassociations\
      \ identified in two or more modality-specific \nPLSR models."
    supports: method
  - section: Original source P10-S2-C10
    page: 10
    quote: "Following the PLSR model fit­\nting for each neuroimaging modality, regions\
      \ with high beta \nvalues for one subtest but low or negligible coefficient\
      \ for \nothers were classified as uniquely contributing to that specif­\nic\
      \ subtest."
    supports: method
  - section: Original source P14-S1-C5
    page: 14
    quote: "Unique regional involvement was determined based on a \nthreshold of averaged\
      \ ß=±0.2 for a given WAB-R subtest and lower coefficient for other subtests\
      \ (overall N = 86)."
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: "Therefore, the resulting cohort was com­\nposed of 86 participants and\
      \ subsequent analyses refer to \nthese 86 participants."
    supports: sample
  - section: Original source P1-S1-C6
    page: 1
    quote: "A total of 86 \nparticipants with chronic (>12-month post-stroke) aphasia\
      \ after left hemisphere strokes were examined."
    supports: sample
  - section: Original source P16-S1-C9
    page: 16
    quote: "Second, lan­\nguage impairment was quantified based on the WAB-R only,\
      \ \nwhich is a fairly coarse measure of language processing."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kristinsson2025
  proposal_id: R007
  review_status_sha256: 774c9fa39abbc23b4f70273589afaa6d732d9afa9404a4593cfd6939e43d3298
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
        A/passages.json: 9aee8a026de0a32febf6ae1c91123c238c5545a5d096a72f578dbdc6f7e14ee0
        A/raw.json: 5517a8579c17583863d0a7951c9baa4e3b277e2c5945aff606b982742f1da8f9
        A/source-units.json: 8f7852446d44e000b31cd0467581a90f78c297a8d4178a8b8e05fa745aec2bc8
        A/full-source-units.json: a0bff97e7a7aa41a78b46a5762565816aee56acae0875d7a2927d7e8a05f0fd8
        A/meta.json: 1c9c298461329c9a68fb3e813c4de632264b6247032975207a106da1f19b7778
        A/table-images/TABLE-2-page-8-1.png: f08be7a0df1e116cf55569afcbec9282986d2cc6ce7c62c80c5bf541ccf82934
        A/table-images/page-4.png: 382a0b64214b370827ea7a0a001922c035c383254524689b7ef72a62c25334d9
        A/table-images/TABLE-1-page-4-1.png: f41dfcaa63211f7cdd62a9b4ad2721200c47fabf12c601e0432df62f673ff137
        A/table-images/page-8.png: b23d2f624944020e4126a845e7abb8577e1619389111197fa96c9cace467a7c4
        A/table-images/manifest.json: 29d5cc4ba3878f2e60ed3df7adc80387c5ecc32380d0e0b2f2d39a74464769c0
        A/clauses/window-03/raw.json: f515091e2ac9495ce4b7f3858c47562b2c0773021aaeddbb386e6dddf75d6ddd
        A/clauses/window-03/prompt.txt: dc182ed0d940ee94af8628eb8efc6f9133133eea4dbe5b60a3e09eeefae7a9f1
        A/clauses/window-03/meta.json: a3ca1df6436ef6143cd1a9d0518a07dc70b161f8c5a3e47732ffe52a566fd4af
        A/clauses/window-04/raw.json: 8fd2761a3c1ab9524949a314b953817081dd2136964ebb571a410f1c8ab1cc80
        A/clauses/window-04/prompt.txt: 2693c74ce87160aa0acf70ed753295a4366869df4e90736fd1283f1d0d32ce98
        A/clauses/window-04/meta.json: 9545e3d680fff67d6b08ce50b3f52f8bc29704f0133e0168a8abae9bc895ea4c
        A/clauses/window-05/raw.json: 23e633d365a4a4de3ef25414f748fb67a9a50b4d71f98b4d14d6f7d6ae23cacc
        A/clauses/window-05/prompt.txt: 1d1c523703b5f3eccccc93e76988685998d4c8ea837d090e66576a37c6851153
        A/clauses/window-05/meta.json: 7a3ccec3c513c604a61b491212c1c225728710deeccd67bb3b3905ea67c23c6b
        A/clauses/window-02/raw.json: 73851dc28e54d801d40b5ff19a3b52eb2d2f1f46b48232a799fc932c249866d1
        A/clauses/window-02/prompt.txt: f0b9d40586cb48f0450c5c1d641d71724506b28d888a2fc1c8dd86105cc2ed29
        A/clauses/window-02/meta.json: bc1f8c01d389aa65472d921f4f4e73ed23e85d54c4b9b42f0476c03d72f14e91
        A/clauses/window-09/raw.json: 24213dc407ab088d4353816a76449a67d3568caadbbb178a3698365a4e690380
        A/clauses/window-09/prompt.txt: c4df2d0badc504787fbdfd46372736b019221baa2911bf1c5fd6796919724509
        A/clauses/window-09/meta.json: c6b4a31e856a18a0fc9dceb9820c10c0bdc89bd7d7af7a64b06daa967d3a7f13
        A/clauses/window-07/raw.json: 2cfa86a3eae3353729031a9b4c1711ed7a2034585b876fe1cd35b9f516ec49e2
        A/clauses/window-07/prompt.txt: db85f01c5c4c0c06e1774715124856ee95701c836530ce7d52234748903018f2
        A/clauses/window-07/meta.json: d424373675b4caa735f960f893aca87e934fbb35eebdbdfef4a36087e8c19ee0
        A/clauses/window-01/raw.json: de5816963386f405281e908427ad212e81b9a5fc5f6897f4dd1b8f8de0727011
        A/clauses/window-01/prompt.txt: 78d30ffd1020cf9c0b78b33a43fc60aee9c972a843aa36330a13bed79ae41b02
        A/clauses/window-01/meta.json: 5c49a07f80d72b0c6b086f68a29c5b37ed59d0bfa5a89cea6dab33e73bfb8780
        A/clauses/window-06/raw.json: 78122fdbb04c9c35c80fbb5df0c26d807af81e53c5203135ff93b8036eddb595
        A/clauses/window-06/prompt.txt: 75f01018a074d0b5955b5c384b7e67393d1d93617af1feca3053d516916b1b15
        A/clauses/window-06/meta.json: 5255901e8d5367c1bd0a3b3d7cab239cb823b1618874b23668bb46047e47f750
        A/clauses/window-08/raw.json: dfbcc0cc3a42e9c5a2a52e0b1a23eea20b822ad555fb0a383addfa0d35f44259
        A/clauses/window-08/prompt.txt: 34a06843319fcc4be403b3fda95aeac6c74841d770465cb5958dfa069b1cdf0b
        A/clauses/window-08/meta.json: a6d5add12babbd8908c0c4e711aa5c3e65910c9667af6eaf4ff56dd647825f96
        A/tables/TABLE-2-page-8-2/raw.json: b78aae68c5f6f4c8f33c3c4cbbb8270d4c584425505755923d7dbd3a924305ad
        A/tables/TABLE-2-page-8-2/prompt.txt: 617ece01e525c33f26377178d6c589e167491ea6b5e88561808e0855b12d717d
        A/tables/TABLE-2-page-8-2/meta.json: 5e17d156c0f4bc024dcc7d5d750e69831d043d974aa17f8e34c052ef7c058722
        A/tables/TABLE-1-page-4-1/raw.json: 585d978292c29f21ba17a991b279db911e66ca7985cad24d72152a5c01393996
        A/tables/TABLE-1-page-4-1/prompt.txt: 4a64a74aa131e04181f10b0d3ef9ec0358de7ca1ea7f8461092397ad97a70c2b
        A/tables/TABLE-1-page-4-1/meta.json: d004e1bfd80ee34e517d012112a5281992e49926b6e45b414d09e7eab67570b5
        B/passages.json: 9aee8a026de0a32febf6ae1c91123c238c5545a5d096a72f578dbdc6f7e14ee0
        B/raw.json: 98923e777888f9985c968c24bdb97d0b0cb32d39289db02093db7a7e35e9cd4c
        B/source-units.json: 8f7852446d44e000b31cd0467581a90f78c297a8d4178a8b8e05fa745aec2bc8
        B/full-source-units.json: a0bff97e7a7aa41a78b46a5762565816aee56acae0875d7a2927d7e8a05f0fd8
        B/meta.json: 17bb71694a95ac796d59c15933e308e6406eca796da4021308f54fd6ead3cb3d
        B/table-images/TABLE-2-page-8-1.png: f08be7a0df1e116cf55569afcbec9282986d2cc6ce7c62c80c5bf541ccf82934
        B/table-images/page-4.png: 382a0b64214b370827ea7a0a001922c035c383254524689b7ef72a62c25334d9
        B/table-images/TABLE-1-page-4-1.png: f41dfcaa63211f7cdd62a9b4ad2721200c47fabf12c601e0432df62f673ff137
        B/table-images/page-8.png: b23d2f624944020e4126a845e7abb8577e1619389111197fa96c9cace467a7c4
        B/table-images/manifest.json: a49973f6a85fde80005053b2745daf7faefc14561e1b1acb531ebbfeda2ab340
        B/clauses/window-03/raw.json: 94e03ba38a36c9ad01ba251acfb5f22d8e714ba1c7db9d7bb8fa35244aac2018
        B/clauses/window-03/prompt.txt: dc182ed0d940ee94af8628eb8efc6f9133133eea4dbe5b60a3e09eeefae7a9f1
        B/clauses/window-03/meta.json: 36426040320ad6d7e4002cb77e7cfe7c5de76b3a7e00f7760441f69b7de14008
        B/clauses/window-04/raw.json: 938a646ce46bf3115ea4ea5eb60f64ba66255e5df26cc6322d256bdc774a6156
        B/clauses/window-04/prompt.txt: 2693c74ce87160aa0acf70ed753295a4366869df4e90736fd1283f1d0d32ce98
        B/clauses/window-04/meta.json: cebc027782ca4105261592c4d54ea8579ad088cf58b60c9b799cf951bea2433e
        B/clauses/window-05/raw.json: baf69dc4c90f77ffa4fafc5a254419163d82db595a55a2d7e339fee607659a79
        B/clauses/window-05/prompt.txt: 1d1c523703b5f3eccccc93e76988685998d4c8ea837d090e66576a37c6851153
        B/clauses/window-05/meta.json: 1c400953b0d9953443ca55a1a2cefb0e6f3e1a264b9d26e697c8df41c887f8ba
        B/clauses/window-02/raw.json: 784ee8aa36a28059c1407083de6bd43017dbc8d4fec858efc4c9e40b72421fd7
        B/clauses/window-02/prompt.txt: f0b9d40586cb48f0450c5c1d641d71724506b28d888a2fc1c8dd86105cc2ed29
        B/clauses/window-02/meta.json: 08ff9183afaef4693669022173ffc329fb40c137e10dd989696b62bf38c573da
        B/clauses/window-09/raw.json: efaca0c75d9a20aebec914c20e9c483e92539c399500c27e2d2b88ae07460dc2
        B/clauses/window-09/prompt.txt: c4df2d0badc504787fbdfd46372736b019221baa2911bf1c5fd6796919724509
        B/clauses/window-09/meta.json: 56f3e0962fe120d0c960e4eb81b380f214cb9ccac7decdf67dc934ea132bd6d1
        B/clauses/window-07/raw.json: eab5841215ce0f79bcc64a300d1b0330844d7e6b1386e6b61e203913735f40c8
        B/clauses/window-07/prompt.txt: db85f01c5c4c0c06e1774715124856ee95701c836530ce7d52234748903018f2
        B/clauses/window-07/meta.json: b9c9d585843fa744c8ed03d41be0ef6705fbb25a612709323e7465e5c0f8d553
        B/clauses/window-01/raw.json: 008cd7b53a125a84c52fccba27625a205d3579f4968284ba425038c18c82ae4c
        B/clauses/window-01/prompt.txt: 78d30ffd1020cf9c0b78b33a43fc60aee9c972a843aa36330a13bed79ae41b02
        B/clauses/window-01/meta.json: 0d2411f15e898dec83005a5897d7c77831103e0029b462003faf5d0e577c7305
        B/clauses/window-06/raw.json: 69e767250091d8350c260d5d5f513910f19110b947614122dafbccaee4621719
        B/clauses/window-06/prompt.txt: 75f01018a074d0b5955b5c384b7e67393d1d93617af1feca3053d516916b1b15
        B/clauses/window-06/meta.json: 2aa5f0f2a072dd569630c195905684edee98a9e0b42e3458bbfb0caeeab37299
        B/clauses/window-08/raw.json: e8193179a02fe06c38293000d11bf42567146a442aad7fe7d37a1a5088f722ab
        B/clauses/window-08/prompt.txt: 34a06843319fcc4be403b3fda95aeac6c74841d770465cb5958dfa069b1cdf0b
        B/clauses/window-08/meta.json: e6327a01d934f72e7712d235a5d968e240fb99a6cf29f543f23f3ba614691798
        B/tables/TABLE-2-page-8-2/raw.json: 46d68d95d4dafba1e9472e28588cd8eeb4f5ac51ad8bef752e957449ec6617cc
        B/tables/TABLE-2-page-8-2/prompt.txt: 617ece01e525c33f26377178d6c589e167491ea6b5e88561808e0855b12d717d
        B/tables/TABLE-2-page-8-2/meta.json: 5157a1a1219309917907dd44bd3e8764080f15c4477cbd4cf017fe6b8182aa6c
        B/tables/TABLE-1-page-4-1/raw.json: e2fbfce7301229db5bb2365efb9f10bb5e5bddea7f66376874d1dba7c3b0ac28
        B/tables/TABLE-1-page-4-1/prompt.txt: 4a64a74aa131e04181f10b0d3ef9ec0358de7ca1ea7f8461092397ad97a70c2b
        B/tables/TABLE-1-page-4-1/meta.json: 74e75ded4cba004b455759a7bd1443f669764c9d27d7f88a83813f05a8b220a6
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
      pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2025
      source_status_sha256: c50f63ebd5c85065d9ce869e006b2e7771d0ae66be2e0a0a75f6bc3ead5cd4f0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: brain regions (beta coefficients)
    outcome:
      text: naming
    analysis_label: Unique neural architecture association
    relation: association
    evidence_ids:
    - P10-S3-C7
    - P10-S3-C8
    qualifier_ids:
    - P10-S2-C10
    - P10-S3-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2025
      source_status_sha256: c50f63ebd5c85065d9ce869e006b2e7771d0ae66be2e0a0a75f6bc3ead5cd4f0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C9
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S3-C2
      - Accounting without a linked unit P7-S3-C3
      - Accounting without a linked unit P7-S3-C5
      - Accounting without a linked unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C5
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S3-C3
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P8-S1-C1
      - Result passage disposed without unit P10-S1-C8
      - Result passage disposed without unit P10-S1-C9
      - Accounting without a linked unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Accounting without a linked unit P10-S2-C6
      - Result passage disposed without unit P10-S2-C7
      - Accounting without a linked unit P10-S2-C8
      - Unaccounted source passage P10-S2-C5
      - Unaccounted source passage P10-S2-C4
      - Unaccounted source passage P10-S2-C6
      - Unaccounted source passage P10-S2-C8
      - 'window 7: invalid/duplicate disposition P10-S3-C5'
      - Result passage disposed without unit P10-S3-C5
      - 'window 7: invalid/duplicate disposition P10-S3-C6'
      - Result passage disposed without unit P10-S3-C6
      - 'window 7: invalid/duplicate disposition P10-S3-C8'
      - Result passage disposed without unit P10-S3-C8
      - Result passage disposed without unit P15-S1-C2
      - Accounting without a linked unit P16-S2-C3
      - Unaccounted source passage P16-S2-C3
      unattached_null_or_qualifier_ids:
      - P10-S2-C5
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 192
      unselected_timing_passages:
      - P1-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C1
        - P5-S1-C11
        - P5-S2-C2
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C7
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C8
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C5
        - P6-S2-C6
        - P6-S2-C7
        - P6-S2-C8
        - P6-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-8-2
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P5-S3
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S1
        - P9-S1
        - P10-S1
        - P10-S2
        - P11-S1
        - P12-S1
        - P12-S2
        - P13-S1
        - P14-S1
        - P15-S1
        - P15-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2025
      source_status_sha256: c50f63ebd5c85065d9ce869e006b2e7771d0ae66be2e0a0a75f6bc3ead5cd4f0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Describes covariance explained by latent variables.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies spontaneous speech as most influential and perisylvian regions
        as shared variance.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Provides prediction accuracy for language measures.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Reports unique variance accounted for by distributed regions.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 6
      reason: Discusses shared perisylvian and unique distributed regions.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to participant characteristics and lesion overlap figure.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variability in outcomes and lesions.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average language scores.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-correlation of language scores.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies spontaneous speech as dominant component.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Compares loadings of naming, repetition, and other subtests across models.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies auditory comprehension as having lowest loading weight.
    - source_id: P7-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: States covariance explained by LVs varied across models.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports models explaining over 50% covariance with first two LVs.
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Describes network-wide patterns of disconnections.
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies number of LVs required for other modalities.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of common patterns emerging across modalities.
    - source_id: P7-S3-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies first LV highlighting left perisylvian area.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap in superior longitudinal fasciculus.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies right hemisphere homologous regions in perfusion/connectivity
        models.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies second LV delineating ventral and dorsal streams.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies third LV accentuating AP distinction.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on commonalities and distinctions.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Contrasts structural connectivity and functional connectivity findings.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure caption describing brain renderings.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies left rolandic operculum as most frequently implicated region.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies superior and inferior temporal gyri in six modalities.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies putamen and thalamus as critical in four to five modalities.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Contrasts structural connectivity and lesion-based modalities.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies functional activity and perfusion modalities highlighting
        bilateral regions.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant correlation in 26/44 models.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies modalities with significant results for all four functions
        and those without.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports highest correlation coefficients for specific subtests by modality.
    - source_id: P10-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on shared variability.
    - source_id: P10-S2-C10
      disposition: represented
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      reason: Defines classification of unique contributing regions.
    - source_id: P10-S3-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies regions uniquely associated with auditory comprehension.
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies right hemisphere associations for auditory comprehension.
    - source_id: P10-S3-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Contrasts modality-specific identification of right vs left hemisphere
        regions.
    - source_id: P10-S3-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies regions uniquely associated with naming.
    - source_id: P10-S3-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Notes naming associations were predominantly in connectivity models.
    - source_id: P10-S3-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies regions uniquely associated with repetition.
    - source_id: P10-S3-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies regions uniquely associated with spontaneous speech.
    - source_id: P10-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to supplementary table.
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Reports variance explained by shared and unique models.
    - source_id: P12-S1-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Identifies strongest unique predictors for naming, repetition, and auditory
        comprehension.
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Reports no independent effects for spontaneous speech.
    - source_id: P15-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 5
      - 6
      - 7
      - 8
      reason: Restatement of shared and unique variance findings.
    - source_id: P15-S2-C2
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      reason: Restatement of unique associations for auditory comprehension and others.
    - source_id: P15-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General comparison of modalities.
    - source_id: P15-S2-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies right hemisphere recruitment in auditory comprehension via
        rsfMRI.
    - source_id: P15-S3-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies hypoperfusion in left hemisphere regions as shared variance.
    - source_id: P16-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P16-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage:
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C6
    - P7-S1-C9
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C9
    - P7-S2-C11
    - P7-S3-C2
    - P7-S3-C5
    - P8-S1-C5
    - P8-S1-C6
    - P9-S1-C2
    - P10-S1-C8
    - P10-S1-C9
    - P10-S2-C7
    - P10-S2-C8
    - P10-S3-C11
    - P15-S1-C2
    - P15-S1-C3
    - P15-S1-C4
    - P15-S1-C6
    - P15-S2-C2
    - P15-S2-C6
    - P15-S2-C7
    - P15-S3-C1
    - P16-S2-C2
    - P16-S2-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-8-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C7
      recruited_sample:
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C4
      eligibility:
      - P4-S1-C6
      imaging_provenance: []
      imaging_timing:
      - P4-S1-C1
      outcome_timing:
      - P4-S1-C9
      outcome_definition:
      - P1-S1-C7
      - P3-S3-C2
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      - P4-S1-C14
      validation:
      - P1-S1-C9
      - P6-S2-C11
      analysis_restrictions:
      - P10-S1-C3
      dependent_variable_statement:
      - P3-S3-C5
      - P3-S4-C1
      - P6-S3-C3
      - P6-S3-C5
      limitations:
      - P16-S1-C5
      - P16-S1-C6
      - P16-S1-C8
      - P16-S1-C9
      - P16-S1-C10
      - P16-S1-C11
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P6-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C1
      - P5-S1-C11
      - P5-S2-C2
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C8
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C5
      - P6-S2-C6
      - P6-S2-C7
      - P6-S2-C8
      - P6-S2-C9
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
      pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
      review_sha256: 774c9fa39abbc23b4f70273589afaa6d732d9afa9404a4593cfd6939e43d3298
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
      - P10-S3-C7
      - P10-S3-C8
      source_result: The study identified brain regions uniquely associated with naming
        performance using a multivariate PLSR approach. Specifically, bilateral superior
        frontal and parietal lobes, as well as subcortical regions (caudate nucleus,
        putamen), were found to have high beta coefficients for naming but low/negligible
        coefficients for other WAB-R subtests. These associations were predominantly
        revealed in connectivity-based models and required identification in at least
        two modality-specific PLSR models to be reported.
      result_status: detected
      patient_measurement: multiple
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the 'Unique neural architecture
            association' for naming, defined by beta coefficients from PLSR models.
            The source explicitly describes this analysis in P10-S3-C7 and P10-S3-C8,
            distinguishing it from shared variance analyses (VIP scores).
          source_ids:
          - P10-S3-C7
          - P10-S3-C8
          - P6-S3-C8
        direction:
          answer: fits
          reason: The source states that regions were 'uniquely associated' with naming.
            The proposed draft uses 'likely' direction, which is appropriate given
            the correlational nature of the PLSR beta coefficients and the lack of
            a specified sign (positive/negative) in the specific result passage, though
            P10-S3-C2 notes that significant effects indicate involvement rather than
            direction. The draft does not claim a specific causal direction or sign,
            preserving the detected association status.
          source_ids:
          - P10-S3-C7
          - P10-S3-C8
          - P10-S3-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as brain regions (beta coefficients)
            and the outcome as naming performance. The patient measurement is 'multiple'
            because the result is a synthesis across modality-specific PLSR models
            (including connectivity, lesion, etc.), not a single modality like patient_diffusion
            or template_lesion_overlap alone. The definition correctly captures the
            'unique' aspect (high beta for naming, low for others).
          source_ids:
          - P10-S3-C7
          - P10-S3-C8
          - P6-S3-C8
          - P10-S2-C10
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that findings are
            reported only for regions identified in two or more modality-specific
            PLSR models (P10-S3-C3). It also correctly notes the beta coefficient
            threshold (±0.2) from P14-S1-C5/P6-S3-C9. The limitation regarding WAB-R
            coarseness is included.
          source_ids:
          - P10-S3-C3
          - P14-S1-C5
          - P16-S1-C9
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly reflects the
            multimodal nature and the specific thresholding criteria. The 'new_model_candidate_not_verified'
            flag is a system status, not a source caveat. The source does not present
            a conflicting null result for this specific unique association claim.
          source_ids:
          - P10-S3-C3
          - P10-S3-C7
          - P10-S3-C8
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
      id: R007
      exposure:
        text: brain regions (beta coefficients)
      outcome:
        text: naming
      analysis_label: Unique neural architecture association
      relation: association
      evidence_ids:
      - P10-S3-C7
      - P10-S3-C8
      qualifier_ids:
      - P10-S2-C10
      - P10-S3-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
        source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2025
        source_status_sha256: c50f63ebd5c85065d9ce869e006b2e7771d0ae66be2e0a0a75f6bc3ead5cd4f0
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d20db1f29b505067b76fce14c907baf0eac6f4d9fdd19a54aa7771318635b181
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C7
          page: 4
          text_layer_sha256: d20db1f29b505067b76fce14c907baf0eac6f4d9fdd19a54aa7771318635b181
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Therefore, the resulting cohort was com­\nposed of 86 participants\
          \ and subsequent analyses refer to \nthese 86 participants."
        anchor_text: "Therefore, the resulting cohort was com­\nposed of 86 participants\
          \ and subsequent analyses refer to \nthese 86 participants."
        excluded_fragments: []
        image_sha256: 85ecfc6d4ef5e053da5311ca363564c3e06ff6c36069b86ba0e7e40d1df5e5e8
        transcription: '. Therefore, the resulting cohort was com-

          posed of 86 participants and subsequent analyses refer to

          these 86 participants'
      P1-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ec4f598d3ad8d426d1f766bafcdb6ddf6a7f2a256e4d5d35c3c739e33f1ea286
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f3859038c33d70479b878d1b591cc818cb7ea0e9c360f9ca86c11e72a9c04649
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C6
          page: 1
          text_layer_sha256: f3859038c33d70479b878d1b591cc818cb7ea0e9c360f9ca86c11e72a9c04649
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A total of 86 \nparticipants with chronic (>12-month post-stroke)\
          \ aphasia after left hemisphere strokes were examined."
        anchor_text: "A total of 86 \nparticipants with chronic (>12-month post-stroke)\
          \ aphasia after left hemisphere strokes were examined."
        excluded_fragments: []
        image_sha256: d5de65c044b36a61e8c0562879553d8aac789c3f2c6252dbf5788156f68d1732
        transcription: . A total of 86 participants with chronic (>12-month post-stroke)
          aphasia after left hemisphere strokes were examined
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "Several re­\ngions in the bilateral superior frontal and parietal lobes,\
    \ as \nwell as subcortical regions (e.g. caudate nucleus, putamen) \nwere uniquely\
    \ associated with naming performance."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
