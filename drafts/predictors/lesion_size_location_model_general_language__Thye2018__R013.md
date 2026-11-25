---
id: lesion_size_location_model_general_language
name: lesion size and location model for general language deficits
kind: predictor
findings:
- id: f1
  target: general_language_impairment
  target_kind: impairment
  claim: For general measures of spoken language performance, such as the Philadelphia
    Naming Test and the WAB Aphasia Quotient, lesion location did not significantly
    improve prediction accuracy above and beyond lesion size.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 128
    population: individuals with aphasia secondary to left hemisphere stroke (not
      bilateral or solely subcortical)
    phase: not_reported
    time_post_onset: chronic stage (> 6 months post onset) for imaging; at least 1
      month post onset for inclusion
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The modest amount of variance explained represents a lower bound as other factors
    (demographics, multimodal imaging) were excluded
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A predictive model comparing lesion size alone against
    a model combining lesion size and template lesion load (the proportion of overlap
    between a participant''s lesion and an independently-generated LSM-based template
    of critical regions). The finding held regardless of whether critical lesion locations
    were defined by mass-univariate VLSM or multivariate SCCAN; Lesion size alone
    was a significant predictor for these measures. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S3-C3, two-model agreement, human verification pending): The participants
    were 128 individuals with aphasia secondary to left hemisphere stroke (not bilateral
    or solely subcortical) Original text-layer quotation is preserved below. PDF image
    reading (P2-S3-C9, two-model agreement, human verification pending): Lesion location
    was assessed based on MRI (n = 75) or CT (n = 53)

    brain scans collected during the chronic stage (> 6 months post onset)

    and following the same procedures as previous studies of this data set

    (or sub-sets of these data) Original text-layer quotation is preserved below.'
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
    - proposed_concept:general_language_impairment
  citation: '@Thye2018'
  source_passages:
  - section: Original source P6-S3-C8
    page: 6
    quote: 'For general measures of spoken language perfor-

      mance, such as the Philadelphia Naming Test and the WAB Aphasia

      Quotient, overall lesion size and lesion location (overlap with a “cri-

      tical” location template) were signiﬁcant predictors of deﬁcit severity,

      but lesion location did not signiﬁcantly improve prediction accuracy

      above and beyond lesion size.'
    supports: claim
  - section: Original source P7-S1-C7
    page: 7
    quote: 'In the case of the broad deﬁcit scores, the fact that lesion location

      does not improve prediction accuracy beyond that obtained with lesion

      size alone is essentially failing to reject the null hypothesis that the

      language deﬁcit is a result of lesion size.'
    supports: claim
  - section: Original source P7-S2-C5
    page: 7
    quote: 'In contrast, aphasia severity (WAB AQ) and naming deﬁcits (PNT)

      were predictable from overall lesion size, but lesion location provided

      no additional predictive utility.'
    supports: claim
  - section: Original source P9-S1-C1
    page: 9
    quote: '

      were (1) Speech Production and Speech Recognition deﬁcits were

      better predicted by a model containing both lesion size and lesion lo-

      cation, whereas general language deﬁcits (aphasia severity and naming

      deﬁcits) were predicted by lesion size and lesion location did not im-

      prove these predictions; and (2) SCCAN LSM inherently captured this

      by choosing a large optimal sparseness value for WAB AQ and PNT,

      which produced very large lesion location “templates”, whereas for

      VLSM, the size of the lesion location templates was determined by the

      multiple comparisons correction and the (lack of) predictive utility of

      lesion location only emerged in a subsequent cross-validation predictive

      analysis.'
    supports: claim
  - section: Original source P2-S3-C3
    page: 2
    quote: 'The participants were 128 individuals with aphasia secondary to left

      hemisphere stroke (not bilateral or solely subcortical).'
    supports: sample
  - section: Original source P2-S3-C9
    page: 2
    quote: 'Lesion location was assessed based on MRI (n = 75) or CT (n = 53)

      brain scans collected during the chronic stage (> 6 months post onset)

      and following the same procedures as previous studies of this data set

      (or sub-sets of these data).'
    supports: method
  - section: Original source P6-S2-C3
    page: 6
    quote: 'Repeating this pro-

      cedure for each of the 8 folds produced the two critical predictors –

      overall lesion size and template lesion load – for each participant.'
    supports: method
predictor_type: imaging_metric
short_definition: A predictive model comparing lesion size alone against a model combining
  lesion size and template lesion load (the proportion of overlap between a participant's
  lesion and an independently-generated LSM-based template of critical regions).
assessment:
- Philadelphia Naming Test
- Western Aphasia Battery Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Thye2018
  proposal_id: R013
  review_status_sha256: 210f47b18baffc5b23a0815d1a453438e6b1773b49b8be9932af42831e5bedda
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
        A/passages.json: 61424e77bb4685f5e5c3717400e1be8cf193fc5ad20d571703241b4f5cebecfb
        A/raw.json: fd5d6f606e6a5b7d2b52bc0ca8ef9212232f5510ac5f7a0f248ee29ac96e324e
        A/source-units.json: 89545954b5416d4cec0ae64a7353c1230d6673f0cb8970343a8e351c8339635b
        A/full-source-units.json: 9e219be7280f677050ecc60d2e8d169048b8b865dc39cc4c18a46c07abfb2ade
        A/meta.json: 26ac8136646bd01230a2623788b589fd747127aae19c95c0cf31383d5a0e964f
        A/table-images/TABLE-1-page-2-1.png: b048c226fcd23a9931300d9b4ec100a4561436598a2ea23fe4c61913e1cff532
        A/table-images/page-2.png: cd3b204072774e3f0d948d79956a8092b4de558e4dd354f79933359573b83be4
        A/table-images/page-5.png: 6b8aaca826c3ab43ff6707c5c1c056165b49a35e03f9fb5a20efe64500d51c66
        A/table-images/manifest.json: 73e2c8399bf15875a78c47bf5f80bc44d559a19482a3ce77e1ea216bf4e86269
        A/table-images/TABLE-2-page-5-1.png: 7618eb389ce00ffcf8b0e35704d8779cbc8ab4db19e714acf4d15bad2aa7c815
        A/clauses/window-03/raw.json: 1dd8655aac8738abcff6043b25ac59919a0b7258bc50a666a3f0d7b6a49895a3
        A/clauses/window-03/prompt.txt: 95eccea50ecc270b2acf9f1d70761d856c3717d0f1dc589f8659aba016574a88
        A/clauses/window-03/meta.json: 3ee688dc215234e47673d813659aacf4bb33b8cd7b564e7e06a501ca2eec3794
        A/clauses/window-04/raw.json: 369a6dfec437cbadb17c99a2fde98da25275b51fe57e4208e8e7536ad6c7227d
        A/clauses/window-04/prompt.txt: 51a61629ce4fde84760978ea6c5a7a9dacae0d5ad618775ea37cfda297948bdf
        A/clauses/window-04/meta.json: 2ce041294b848508ddbf6f68611f03b4d2a0862c9f01f66506eadda0144dff43
        A/clauses/window-05/raw.json: f7daca1df7113696356a0afb3c63636afdef07692ed2ea2e40d762186edc79ea
        A/clauses/window-05/prompt.txt: 8375cb2f85d00442b9e696a03dafb30422a3fc0a03096a9fc33869aba6fec458
        A/clauses/window-05/meta.json: 4ef6d3b37943abdbc9620a49f0fb27f7f11e6e5ccedc1d25f130a5cdca2bd335
        A/clauses/window-02/raw.json: 162a435d7ef9d3a661142b76b9e8152e6e8a4fdd55c8d6da9d2dc86a9d484086
        A/clauses/window-02/prompt.txt: 12a85651c281a73284ca264c0470ddd6725c7483e0c5667f09a182f5130508e8
        A/clauses/window-02/meta.json: 34d4e959aeb21a38b70b0e9272650d368554277efc0140fa69bc6034b306c19c
        A/clauses/window-07/raw.json: a66b3c650e6dd1fef6353fca6d059918cf0c05c9b6b27ed8a10134a9dffb7ceb
        A/clauses/window-07/prompt.txt: 0a3addf74b56505d9327c1fe7642328401cd3140a3ec119876802008523aabc7
        A/clauses/window-07/meta.json: 9796e282f0b94c227ec6ce9d20d5c04d4d6c769547c6d708e1c7ecd89417131f
        A/clauses/window-01/raw.json: 79ca0809e694cd3581c6053916a5cbee78c64823b308ed0e78f59b3c63104e2c
        A/clauses/window-01/prompt.txt: a9757f1e64f22f38548ccac537f7beccde8f09d004bcfaeaf547ca5ebfd850bc
        A/clauses/window-01/meta.json: 37a9d1207572265222a071dc87b1a4be457fff6789093446802e45c7e2ed9ff5
        A/clauses/window-06/raw.json: cb6e25d983dfcc53aac83e8bc7c1bc84c251be17b5cb34fb31ca42719249a174
        A/clauses/window-06/prompt.txt: ab3edf985755f948fda0a2c5c6f9da1ab62e4e97f3706586240c8933922adf14
        A/clauses/window-06/meta.json: 78cf741be1ef8be59a608fa61d14e6d7a38a034d68d719c2ed2fa6135ddc00fa
        A/clauses/window-08/raw.json: 480aecc6afefbcef54aca7fc5bf367d0d95fe5b6d3b0d99f6d48e9beff7ac24b
        A/clauses/window-08/prompt.txt: a1427237be2911a8abad1a8527aeeddb200331806441f5921b7e9f658d73aac8
        A/clauses/window-08/meta.json: 865f8c6070abcd47f98816ccfe63182b8beade8190636a5edc3cd9117d65b133
        A/tables/TABLE-2-page-5-2/raw.json: c8f088ccd58b3ae52d64d0d72c844a2b0142f21dc99d342a12ddeef7462c7b11
        A/tables/TABLE-2-page-5-2/prompt.txt: a20130063fceaa6042804a669a973dcbaf954ffaf98b73e0a2267fc5f2639dda
        A/tables/TABLE-2-page-5-2/meta.json: 349a39317bad610bca624969db2e0712b7ad6421556f47ca02adc06698f5c00c
        A/tables/TABLE-1-page-2-1/raw.json: 476905249f335cdc291ccbe0932c61feddd74f6b88b3256f980d234226066cb3
        A/tables/TABLE-1-page-2-1/prompt.txt: 254a46d70ef892b6b4b8298b584b7303541e04aa5d9d369002306a73fc9c76f2
        A/tables/TABLE-1-page-2-1/meta.json: 9050017d2d9f9910e30543e7eb4798efd952a93aa9611a047550700886a5d6e7
        B/passages.json: 61424e77bb4685f5e5c3717400e1be8cf193fc5ad20d571703241b4f5cebecfb
        B/raw.json: ec7303289a72e3d19d0eea0ef8544c8fc84c9d44e89badbd022c64fc83852a48
        B/source-units.json: 89545954b5416d4cec0ae64a7353c1230d6673f0cb8970343a8e351c8339635b
        B/full-source-units.json: 9e219be7280f677050ecc60d2e8d169048b8b865dc39cc4c18a46c07abfb2ade
        B/meta.json: c98450e18bd3a8031cafa053fe4e838d0414b0dff983a67c5d9cc4af1c126ced
        B/table-images/TABLE-1-page-2-1.png: b048c226fcd23a9931300d9b4ec100a4561436598a2ea23fe4c61913e1cff532
        B/table-images/page-2.png: cd3b204072774e3f0d948d79956a8092b4de558e4dd354f79933359573b83be4
        B/table-images/page-5.png: 6b8aaca826c3ab43ff6707c5c1c056165b49a35e03f9fb5a20efe64500d51c66
        B/table-images/manifest.json: ef6c70901eb5f146fc16664145ebf06117bd7ab7d5710978284766300c2f5971
        B/table-images/TABLE-2-page-5-1.png: 7618eb389ce00ffcf8b0e35704d8779cbc8ab4db19e714acf4d15bad2aa7c815
        B/clauses/window-03/raw.json: ea9689741a09aa29f97ee9a8d7e15c7a35af9e50aea2078feb8625532eec17b3
        B/clauses/window-03/prompt.txt: 95eccea50ecc270b2acf9f1d70761d856c3717d0f1dc589f8659aba016574a88
        B/clauses/window-03/meta.json: 9023306ee560ec27826da11306ff631dabfb49a19be84f7ee678747e5c2d5655
        B/clauses/window-04/raw.json: 18fcca047392f1b6bdc43f60817921e72336d5e2ebb4b21816a48b410832894e
        B/clauses/window-04/prompt.txt: 51a61629ce4fde84760978ea6c5a7a9dacae0d5ad618775ea37cfda297948bdf
        B/clauses/window-04/meta.json: a0213753f54d8dfa5de30c165fff4fcd641c349a8f488863f95113ea54b80add
        B/clauses/window-05/raw.json: 32cbb38e32dd6c68a2df0869a289eec9860d2686bcd4a692aa46f677ecc07c60
        B/clauses/window-05/prompt.txt: 8375cb2f85d00442b9e696a03dafb30422a3fc0a03096a9fc33869aba6fec458
        B/clauses/window-05/meta.json: 57ecfbfd9e39a683f198390e45087d1b7451ecb03e7717695d4083bb6839b649
        B/clauses/window-02/raw.json: ea22ea30cb7ee36469fc1837bdcf3b4c5872e02e865704605d98975bd440ae51
        B/clauses/window-02/prompt.txt: 12a85651c281a73284ca264c0470ddd6725c7483e0c5667f09a182f5130508e8
        B/clauses/window-02/meta.json: 6281069c216116691f950cb1c2afe29ffce6885ce6f7fc1e72de44e216971303
        B/clauses/window-07/raw.json: 0cc784263adb2c307771b2ffa59667dd8ff3d0d5b2efe4ffe7e524d95fbb35ee
        B/clauses/window-07/prompt.txt: 0a3addf74b56505d9327c1fe7642328401cd3140a3ec119876802008523aabc7
        B/clauses/window-07/meta.json: 10b5f82a21d7b0b4abe57fc7a5549429d46f47973465d85d54e581d49c24f5aa
        B/clauses/window-01/raw.json: 56f37a5b0c627bad87db36d4d34e2b6c654f621e92bbbc92dc3fba2443739411
        B/clauses/window-01/prompt.txt: a9757f1e64f22f38548ccac537f7beccde8f09d004bcfaeaf547ca5ebfd850bc
        B/clauses/window-01/meta.json: 6dd2b88bf1ecafe47e79c36ad62c4282ef5d750d2414c4add20c9a3a3ee53b5f
        B/clauses/window-06/raw.json: 8e88ac8d3f18205959ca4badba09b24dadbb77b51410790a8d7dd4e107a26500
        B/clauses/window-06/prompt.txt: ab3edf985755f948fda0a2c5c6f9da1ab62e4e97f3706586240c8933922adf14
        B/clauses/window-06/meta.json: 75ff2928353e8dca85c4650f4ca7ed400d77e85b07d7ea01689495a1636ea5c2
        B/clauses/window-08/raw.json: dc6fa93e34762bd9cf4c2e9d42fb66f0a72c8bda4a9b4274ba2f0549ef7690db
        B/clauses/window-08/prompt.txt: a1427237be2911a8abad1a8527aeeddb200331806441f5921b7e9f658d73aac8
        B/clauses/window-08/meta.json: 1deb9f8fa8bda8b95f894c3c7a72e30efa555fa9a46d9c6efd4edd083cc1ea15
        B/tables/TABLE-2-page-5-2/raw.json: 6e6b52faed6fbdbae48363f69d90925dcd30e1d7d1034a3fcc35dc646494934a
        B/tables/TABLE-2-page-5-2/prompt.txt: a20130063fceaa6042804a669a973dcbaf954ffaf98b73e0a2267fc5f2639dda
        B/tables/TABLE-2-page-5-2/meta.json: 1ef3979fd21eacfa161c0507ef0bdeb485a55fd057ae286cbd3ed32bce3a900b
        B/tables/TABLE-1-page-2-1/raw.json: 33c84b1ce2f6deed35769530181995e1926cf9744ef56c1e4d8274746e6bf0ec
        B/tables/TABLE-1-page-2-1/prompt.txt: 254a46d70ef892b6b4b8298b584b7303541e04aa5d9d369002306a73fc9c76f2
        B/tables/TABLE-1-page-2-1/meta.json: 24a7a3bd3158d641a04edf0f012908ab45081238017349101ae21a4756a6c54c
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
      pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
      source_review: _compare/relationships-2026-11-16/review-current/Thye2018
      source_status_sha256: 30336a546ad79951fd977f73f87584d5ba5a74ed529196012a398fb928fb66aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: lesion size + lesion location vs lesion size alone
    outcome:
      text: PNT and WAB AQ
    analysis_label: Model Comparison (Study 2)
    relation: model_comparison
    evidence_ids:
    - P6-S3-C8
    - P7-S1-C7
    - P7-S2-C5
    - P9-S1-C1
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
      pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
      source_review: _compare/relationships-2026-11-16/review-current/Thye2018
      source_status_sha256: 30336a546ad79951fd977f73f87584d5ba5a74ed529196012a398fb928fb66aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S4-C8
      - Result passage disposed without unit P3-S1-C4
      - Accounting without a linked unit P3-S1-C5
      - Accounting without a linked unit P4-S1-C6
      - Result passage disposed without unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C3
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P3-S1-C5
      - Unaccounted source passage P4-S1-C6
      - Result passage disposed without unit P5-S2-C8
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S3-C3
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C6
      - Result passage disposed without unit P6-S3-C7
      - Result passage disposed without unit P6-S3-C8
      - Result passage disposed without unit P6-S3-C9
      - Result passage disposed without unit P6-S4-C5
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S1-C7
      unattached_null_or_qualifier_ids:
      - P2-S4-C8
      - P6-S3-C3
      - P6-S3-C7
      - P6-S3-C8
      - P6-S4-C5
      - P7-S1-C6
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 174
      unselected_timing_passages:
      - P2-S3-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C13
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
        source_id: P7-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C14
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C15
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-5-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S4
        - P3-S1
        - P3-S2
        - P4-S1
        - P5-S1
        - P6-S2
        - P6-S3
        - P7-S2
        - P7-S3
        - P8-S1
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
      source_review: _compare/relationships-2026-11-16/review-current/Thye2018
      source_status_sha256: 30336a546ad79951fd977f73f87584d5ba5a74ed529196012a398fb928fb66aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes: []
      reason: Abstract summary of findings represented in detailed results.
    - source_id: P2-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes exclusion of non-chronic participants.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA variance loadings.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes exclusion of a PCA factor based on eigenvalue.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA variance explained.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to PCA factor loadings figure.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports optimization parameters and CV correlations for model setup.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Supports speech recognition localization.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 3.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes PNT association.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes WAB AQ association.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes semantic deficit association.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes semantic deficit association (white matter).
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes speech production association.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes speech recognition association.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Supports speech recognition localization.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of semantic results.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of PNT/WAB AQ breadth.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General comparison of SCCAN and VLSM.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of SCCAN behavior for speech recognition.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of WAB AQ result.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Reports correlations between lesion size and deficits.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of correspondence between methods.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports lesion size as significant predictor.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports variance explained by lesion size.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports variance explained by lesion size for PCA measures.
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 7
      reason: Reports template lesion load as significant predictor.
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 8
      reason: Reports template lesion load for semantics.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Reports effects of template lesion load after controlling for size.
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Conclusion on improved prediction for speech production/recognition.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of correlation.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of correlation in SCCAN.
    - source_id: P6-S3-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Conclusion on improved prediction for speech production/recognition.
    - source_id: P6-S3-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Conclusion on lack of improvement for PNT/WAB AQ.
    - source_id: P6-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on method consistency.
    - source_id: P6-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of semantic prediction accuracy.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Discussion of broad measures and lesion size.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Discussion of broad measures and lesion size.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 12
      reason: Null hypothesis for broad measures.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Model comparison for specific scores.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Lack of additional utility for PNT/WAB AQ.
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion size as primary predictor.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Additional power for speech recognition/production.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Additional power for speech recognition/production.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between template load and size.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of VLSM and SCCAN results.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: No unique predictive value for PNT, WAB AQ, Semantics.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Summary of model comparison results.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sparseness values.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sparseness values.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 3.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sparseness values.
    - source_id: P9-S3-C10
      disposition: represented
      result_indexes:
      - 13
      reason: Behavior-side control eliminated PNT/WAB AQ effects.
    - source_id: P9-S3-C11
      disposition: represented
      result_indexes:
      - 14
      reason: Behavior-side control for speech production/recognition.
    - source_id: P9-S4-C1
      disposition: represented
      result_indexes:
      - 14
      reason: Behavior-side control for speech production/recognition.
    - source_id: P9-S4-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Summary of prediction for functional systems.
    unresolved_coverage:
    - source_id: P1-S1-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P2-S4-C8
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S2-C6
    - P4-S1-C6
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C11
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C7
    - P5-S2-C8
    - P5-S3-C6
    - P6-S1-C1
    - P6-S2-C8
    - P6-S2-C10
    - P6-S2-C11
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C9
    - P6-S4-C5
    - P7-S1-C5
    - P7-S1-C6
    - P7-S2-C7
    - P7-S2-C8
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C6
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S2-C2
    - P9-S2-C4
    - P9-S2-C5
    - P9-S3-C7
    - P9-S4-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C3
      - P2-S3-C3
      - P2-S3-C9
      recruited_sample:
      - P2-S3-C3
      eligibility:
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C7
      imaging_provenance:
      - P2-S3-C5
      - P2-S3-C9
      - P2-S3-C10
      - P2-S4-C2
      imaging_timing:
      - P2-S3-C9
      outcome_timing:
      - P2-S3-C9
      outcome_definition:
      - P3-S1-C3
      - P3-S1-C6
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C7
      - P5-S1-C8
      validation:
      - P3-S1-C10
      - P6-S1-C7
      - P6-S1-C13
      - P7-S2-C13
      analysis_restrictions:
      - P4-S1-C4
      - P6-S1-C11
      - P9-S3-C7
      dependent_variable_statement:
      - P2-S2-C8
      - P3-S1-C8
      - P6-S1-C5
      - P6-S2-C4
      limitations:
      - P2-S1-C13
      - P5-S1-C9
      - P9-S3-C8
      - P9-S3-C11
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C4
      - P6-S1-C11
      - P6-S2-C4
      - P6-S3-C2
      - P7-S2-C7
      - P9-S3-C7
      - P9-S3-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C13
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
      source_id: P7-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C14
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C15
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
      pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
      review_sha256: 210f47b18baffc5b23a0815d1a453438e6b1773b49b8be9932af42831e5bedda
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
      - P6-S3-C8
      - P7-S1-C7
      - P7-S2-C5
      - P9-S1-C1
      source_result: For general language measures (PNT and WAB AQ), lesion location
        (template lesion load) did not significantly improve prediction accuracy beyond
        lesion size alone. This pattern was consistent across both VLSM and SCCAN
        methods.
      result_status: model_comparison
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the comparison of lesion
            size alone versus lesion size plus location for PNT and WAB AQ in Study
            2, as described in the source passages.
          source_ids:
          - P6-S1-C5
          - P6-S3-C8
          - P9-S1-C1
        direction:
          answer: fits
          reason: The claim that lesion location did not significantly improve prediction
            accuracy aligns with the source statements that lesion location was not
            a significant predictor beyond lesion size for these general measures.
          source_ids:
          - P6-S3-C8
          - P7-S1-C7
          - P7-S2-C5
        construct:
          answer: fits
          reason: The exposure (lesion size vs. size+location) and outcome (PNT, WAB
            AQ) are correctly identified. The patient measurement is template lesion
            overlap, which is the specific metric used in the model comparison.
          source_ids:
          - P6-S2-C4
          - P6-S3-C8
          - P3-S1-C6
        qualifications:
          answer: fits
          reason: The qualifications regarding the consistency across VLSM and SCCAN
            methods and the significant predictive power of lesion size alone are
            accurately reflected in the draft.
          source_ids:
          - P6-S3-C9
          - P6-S2-C9
          - P9-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that the variance explained is
            a lower bound due to the exclusion of other factors, which is a material
            caveat mentioned in the source.
          source_ids:
          - P9-S3-C3
          - P9-S2-C8
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
      id: R013
      exposure:
        text: lesion size + lesion location vs lesion size alone
      outcome:
        text: PNT and WAB AQ
      analysis_label: Model Comparison (Study 2)
      relation: model_comparison
      evidence_ids:
      - P6-S3-C8
      - P7-S1-C7
      - P7-S2-C5
      - P9-S1-C1
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
        pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
        source_review: _compare/relationships-2026-11-16/review-current/Thye2018
        source_status_sha256: 30336a546ad79951fd977f73f87584d5ba5a74ed529196012a398fb928fb66aa
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7d06f871954f9e428ee316479553fa6c4616257cc902600f0520538ba990e51a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C3
          page: 2
          text_layer_sha256: 7d06f871954f9e428ee316479553fa6c4616257cc902600f0520538ba990e51a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The participants were 128 individuals with aphasia secondary
          to left

          hemisphere stroke (not bilateral or solely subcortical).'
        anchor_text: 'The participants were 128 individuals with aphasia secondary
          to left

          hemisphere stroke (not bilateral or solely subcortical).'
        excluded_fragments: []
        image_sha256: ef2a03a29a6068bc862566461e40b9e4fc3c62214d6512f1c083858db6dece7d
        transcription: The participants were 128 individuals with aphasia secondary
          to left hemisphere stroke (not bilateral or solely subcortical)
      P2-S3-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: aba317a56678ed522e11955ab8e7b5a38d2c49dd5a090732dda241ae142204c9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2365b3f6da1f7d25ccdd06bd9b79a638c33a5fd3d8ba55484250ad1ae528e010
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C9
          page: 2
          text_layer_sha256: 2365b3f6da1f7d25ccdd06bd9b79a638c33a5fd3d8ba55484250ad1ae528e010
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Lesion location was assessed based on MRI (n = 75) or CT (n
          = 53)

          brain scans collected during the chronic stage (> 6 months post onset)

          and following the same procedures as previous studies of this data set

          (or sub-sets of these data).'
        anchor_text: 'Lesion location was assessed based on MRI (n = 75) or CT (n
          = 53)

          brain scans collected during the chronic stage (> 6 months post onset)

          and following the same procedures as previous studies of this data set

          (or sub-sets of these data).'
        excluded_fragments: []
        image_sha256: fd9176c3f8d289eec0b966f748a4e15c006277a66d9b24adb820a40393ab0170
        transcription: 'Lesion location was assessed based on MRI (n = 75) or CT (n
          = 53)

          brain scans collected during the chronic stage (> 6 months post onset)

          and following the same procedures as previous studies of this data set

          (or sub-sets of these data)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'For general measures of spoken language perfor-

    mance, such as the Philadelphia Naming Test and the WAB Aphasia

    Quotient, overall lesion size and lesion location (overlap with a “cri-

    tical” location template) were signiﬁcant predictors of deﬁcit severity,

    but lesion location did not signiﬁcantly improve prediction accuracy

    above and beyond lesion size.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
