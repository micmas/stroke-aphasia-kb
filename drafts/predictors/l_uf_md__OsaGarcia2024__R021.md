---
id: l_uf_md
name: left uncinate fasciculus mean diffusivity
kind: predictor
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: chronic_change_scores
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    metric: Composite score change from subacute to chronic phase (ΔCS2–3)
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: language_recovery
  target_kind: prognosis
  claim: left uncinate fasciculus mean diffusivity correlated with chronic change
    scores.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 24
    population: participants with poststroke aphasia resulting from a first ischemic
      stroke in the left middle cerebral artery territory
    phase: not_reported
    time_post_onset: imaging performed within 3 days poststroke; chronic change scores
      measured at least 6 months poststroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - absence of specific cortical measures
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: mean diffusivity extracted from the left uncinate
    fasciculus using the Tractoflow automated pipeline (version 2.3.0) with atlas-based
    segmentation in within-subject template space, measured during the acute phase
    (within 3 days poststroke). chronic change scores (ΔCS2-3) represent the difference
    between subacute and chronic composite scores. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S2-C10, two-model agreement, human verification pending): . Thus, a total
    sample of 24 participants

    (mean age, 70 years; SD, 3; 8 women) completed the initial MRI

    and all 3 language assessments Original text-layer quotation is preserved below.
    PDF image reading (P2-S2-C6, two-model agreement, human verification pending):
    METHODS


    Participant Recruitment and Procedure


    We recruited 39 participants with aphasia resulting from a first ischemic stroke
    in the left middle cerebral artery territory at an acute care hospital Original
    text-layer quotation is preserved below. PDF image reading (P2-S2-C8, two-model
    agreement, human verification pending): . Following the protocol out-

    lined by Saur et al,¹³ language assessments and MRI scans were

    conducted within 3 days (acute, T₁), 7 to 15 days (subacute,

    T₂), and at least 6 months (chronic, T₃) poststroke Original text-layer quotation
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
    - proposed_concept:chronic_change_scores
  citation: '@OsaGarcia2024'
  source_passages:
  - section: Original source P5-S1-C14
    page: 5
    quote: "In addition, R-IFOFAD correlated \npositively with chronic change scores,\
      \ and L-UFMD cor-\nrelated with both subacute performance scores and \nchronic\
      \ change scores."
    supports: claim
  - section: Original source P2-S2-C10
    page: 2
    quote: "Thus, a total sample of 24 participants \n(mean age, 70 years; SD, 3;\
      \ 8 women) completed the initial MRI \nand all 3 language assessments."
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: "METHODS\nParticipant Recruitment and Procedure\nWe recruited 39 participants\
      \ with aphasia resulting from a \nfirst ischemic stroke in the left middle cerebral\
      \ artery territory \nat an acute care hospital."
    supports: sample
  - section: Original source P3-S2-C1
    page: 3
    quote: "used the Atlas-based segmentation profile of Tractoflow, ver-\nsion 2.3.0,\
      \ using Freesurfer anatomic images in the within- \nsubject template space,\
      \ which is recommended for pathological \ndata.32 Once the tractogram was reconstructed,\
      \ diffusion mea-\nsures—namely fractional anisotropy, mean diffusivity and axial\
      \ \ndiffusivity, were extracted from ventral stream bundles (IFOF, \nUF, and\
      \ inferior longitudinal fasciculus) and dorsal stream bun-\ndles (AF and superior\
      \ longitudinal fasciculus) bilaterally."
    supports: method
  - section: Original source P2-S2-C8
    page: 2
    quote: "Following the protocol out-\nlined by Saur et al,13 language assessments\
      \ and MRI scans were \nconducted within 3 days (acute, T1), 7 to 15 days (subacute,\
      \ \nT2), and at least 6 months (chronic, T3) poststroke."
    supports: method
  - section: Original source P2-S3-C6
    page: 2
    quote: "Language Assessment and Variable Creation\nBased on previous studies,23,26\
      \ we calculated composite scores \n(CSs) consisting of 3 subscores: comprehension,\
      \ repetition, \nand naming."
    supports: method
  - section: Original source P8-S1-C11
    page: 8
    quote: "Nevertheless, \nwe consider this study valuable because it reports on\
      \ \n>2 time points in the same cohort, including early acute \nmeasures, which\
      \ has yielded important evidence about \nrecovery in recent literature.2,13,45\
      \ Another limitation is \nthe absence of specific cortical measures, although\
      \ lit-\nerature has extensively shown the utility of both white \nand gray matter\
      \ measures in predicting recovery.15,41 The \n"
    supports: limitation
predictor_type: imaging_metric
short_definition: mean diffusivity extracted from the left uncinate fasciculus using
  the Tractoflow automated pipeline (version 2.3.0) with atlas-based segmentation
  in within-subject template space, measured during the acute phase (within 3 days
  poststroke).
assessment:
- composite score (comprehension, repetition, and naming)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: OsaGarcia2024
  proposal_id: R021
  review_status_sha256: cd9b6000c4c6eb033c3560061d7263ad03f593d6a7f6dae34a2489fd1aabf2cb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
        A/passages.json: a8cd00c4a6e245cd751f674c25fd86d02380d716132a8b7e8fc82f8664f4c672
        A/raw.json: d34d81b43ac4fae8fc077831f5895a29f16b1e6cd084ef03d9c3bd4d50f7ae09
        A/source-units.json: f5f1812cf9fbc7376910f9548530dc54e6efce737226e445a379667f59173094
        A/full-source-units.json: 80e4c48bfcdcbe4f0dc85187592bb64b0bc5f5dc8a4a3f1f6d516bfb308b5dd1
        A/meta.json: 18cd9b4a17998956a510fbb5a89710a20fb63cc92b5c2677b4a0dbade991899c
        A/table-images/TABLE-S1-page-8-1.png: 2ac2982178b906ada3802517140001ad5b300bc2574dab627ab5b0516bd1a674
        A/table-images/TABLE-1-page-5-1.png: c22aa53c89d638ac1eeb52c770f720b5afce1992ea9b4e0b4e59adacaf9853f5
        A/table-images/page-7.png: 5e7b2053bce7574cdc6d0a5fb21eb5a5a394225cee3d263f7f29880b39b17e8d
        A/table-images/page-5.png: d2d002e2e78f1150145bba18cb533bd84ffd2180151568775dd0df9a8a66e382
        A/table-images/page-8.png: 7aa48f6eaa3e5c5b5a851252e1b8420e6af7e44b15d6c7135a4b1ca3676e31db
        A/table-images/manifest.json: f4eb35cdbcf658cc3f0534bf0a996a8748fd5f685f3d8aa07c56de3ffe18f69f
        A/table-images/TABLE-3-page-7-2.png: 3d1236ee047638d9ebaa8eb1f2ddb4a88fd581ca088a3374e6bb260ac478dc04
        A/table-images/TABLE-2-page-7-1.png: 69df46dee60caba8976d4e6d1721a7f835295f1a0237cf2c64f453f1d7a308bb
        A/clauses/window-03/raw.json: bacca7c7f791dbe607695cb15b8fb2b59de1a9ba039def56a1e7976553a1ab85
        A/clauses/window-03/prompt.txt: fd25eb1bdedf94f5f333a04d447f8b3ed053e52f2435bad17397e53edd0f17f6
        A/clauses/window-03/meta.json: 06267e7fe88cd269781e42620b1baf16dc70c4f720b8212d4a6a4de62cd97230
        A/clauses/window-04/raw.json: 57ddfee88bbb987424b18f9c960d9a847db5bc2e384c0e5c6dc389fb4592ed37
        A/clauses/window-04/prompt.txt: 5e2ed5622e2eda8a052b08d2015ae7f884c2755e667f611e2557a8408e884b76
        A/clauses/window-04/meta.json: 80928d5408b0b9b94c6e1a8bf8a13a92bf2edd06b22da0ccda57487c99872a05
        A/clauses/window-05/raw.json: cf1e7e107c0ba2034bad255a017c3824e1285b9dc9bce1da8e59b3ae22c0d5bd
        A/clauses/window-05/prompt.txt: ed4e8b6ba2675e2c91288d20b2c9ce677529aba5e19c3db2c642175e11fcb261
        A/clauses/window-05/meta.json: 0e4c98c7f4575b11daf33add3702073f89f03f54df5b56dd9e39fc2939868969
        A/clauses/window-02/raw.json: c4576a2be346bb1f49f1c62a3d70cc530ce6d28e8eca53f0e5c72fb210db4418
        A/clauses/window-02/prompt.txt: 287f8f31df12aa8d6ecbc274198367521fc7b9a53e8a75097282bd2e8155286c
        A/clauses/window-02/meta.json: f09e9b8020076cc7394ff06e81591e1ba288c1ae44da95269c1088dca22df340
        A/clauses/window-01/raw.json: 60d27b62197d81d45b3a51179b8629b6cb7df9894e3f070cb43d61c6e2703fec
        A/clauses/window-01/prompt.txt: 5182c6273456852d0a96b481d2b1395353dac9793abc5506850082a9899d26eb
        A/clauses/window-01/meta.json: 2623943566e7c10fd292452025e4a46a7686da08f9c65a04b14af94b51f8b3f0
        A/clauses/window-06/raw.json: d863d9fe7e9043392ebd90a740e77eb66c5f517543252dd788c9df275cde97a5
        A/clauses/window-06/prompt.txt: c6f99f390ce762c147fce3c986ce04cc0feb52e84e4a0f2d96fa2f3f226fcfeb
        A/clauses/window-06/meta.json: 3573f2f252acc259f2c5a2980d0798a1655a6e98babc520e04761f428ee1a989
        A/tables/TABLE-1-page-5-1/raw.json: c95df73b8a6956d51f81f3a1112ccf5bf1ff087df5d17f9802bf3b9b3420f0c1
        A/tables/TABLE-1-page-5-1/prompt.txt: bd7691e6abd302943935e1a8368ca1c258b1437701e90a914cc6ee4f5a115531
        A/tables/TABLE-1-page-5-1/meta.json: 135b67f134cd39d9e5f4667c53e91e7efffe871ed74493e5cc71447a46cca719
        A/tables/TABLE-S1-page-8-4/raw.json: 7715c12b889ba61d8c49f2d7081bffe56c0614b981801b1a5ae0c11fe293a6c4
        A/tables/TABLE-S1-page-8-4/prompt.txt: 9fef35e6b0e5d03ee15d865fafba7bbafb2c5108fbcb3a037a942b6a0b5fd359
        A/tables/TABLE-S1-page-8-4/meta.json: 82b985e1170f4ac0f09fe0762afecab15f5e77984df6b977a351c0caa2eff153
        A/tables/TABLE-3-page-7-3/raw.json: 263bb4353dab5b8c91cfa111c0d4e412eada3cf4cc49c9fa0f91c14bdf8b1089
        A/tables/TABLE-3-page-7-3/prompt.txt: 8d4858c3a34cf6a3449b7775d51a1dec0aa7dfd0b81b1882963fbf1668355192
        A/tables/TABLE-3-page-7-3/meta.json: bbbb764af8586773098385019315ca2445792e0faccf20a26a30b5dcc257d401
        A/tables/TABLE-2-page-7-2/raw.json: 555277bb96c41a9e53725c7e5c064a531e48a17e93ef9f1c6629dfb8b09b7e21
        A/tables/TABLE-2-page-7-2/prompt.txt: 59d57146d84a76e74264d7c70d4c1c89842b749c4edeaf825c013d9f638b4167
        A/tables/TABLE-2-page-7-2/meta.json: beced33b0e73077d2a1b4b8073551b1ce7de3440d077d711763b7a2358026764
        B/passages.json: a8cd00c4a6e245cd751f674c25fd86d02380d716132a8b7e8fc82f8664f4c672
        B/raw.json: abab489f717ef5a5f9241042b96cd1dcc5ffd364f9f294fbcdf183b26ebf8422
        B/source-units.json: f5f1812cf9fbc7376910f9548530dc54e6efce737226e445a379667f59173094
        B/full-source-units.json: 80e4c48bfcdcbe4f0dc85187592bb64b0bc5f5dc8a4a3f1f6d516bfb308b5dd1
        B/meta.json: cebd70ee070cd010d02b3200cd30e7639eb6bf8b9c008c66f2c488acc8683b2a
        B/table-images/TABLE-S1-page-8-1.png: 2ac2982178b906ada3802517140001ad5b300bc2574dab627ab5b0516bd1a674
        B/table-images/TABLE-1-page-5-1.png: c22aa53c89d638ac1eeb52c770f720b5afce1992ea9b4e0b4e59adacaf9853f5
        B/table-images/page-7.png: 5e7b2053bce7574cdc6d0a5fb21eb5a5a394225cee3d263f7f29880b39b17e8d
        B/table-images/page-5.png: d2d002e2e78f1150145bba18cb533bd84ffd2180151568775dd0df9a8a66e382
        B/table-images/page-8.png: 7aa48f6eaa3e5c5b5a851252e1b8420e6af7e44b15d6c7135a4b1ca3676e31db
        B/table-images/manifest.json: 4c04775c87e322601cdb0a6fa3597321af0864ac84a9bfa127883827077fb678
        B/table-images/TABLE-3-page-7-2.png: 3d1236ee047638d9ebaa8eb1f2ddb4a88fd581ca088a3374e6bb260ac478dc04
        B/table-images/TABLE-2-page-7-1.png: 69df46dee60caba8976d4e6d1721a7f835295f1a0237cf2c64f453f1d7a308bb
        B/clauses/window-03/raw.json: f29ddab0adad372dfe9e32b25295d214ca4023f364f861754b5c8f72e05e1dd4
        B/clauses/window-03/prompt.txt: fd25eb1bdedf94f5f333a04d447f8b3ed053e52f2435bad17397e53edd0f17f6
        B/clauses/window-03/meta.json: 52a65e3c69121e836e971e61e8e13c8cf44de7bde1dc1d712a4bb25d6acbd0f8
        B/clauses/window-04/raw.json: 5353f99197bbf889c9c0542e23d098a5848e1e63f24ba11b9eb6b6222a142a75
        B/clauses/window-04/prompt.txt: 5e2ed5622e2eda8a052b08d2015ae7f884c2755e667f611e2557a8408e884b76
        B/clauses/window-04/meta.json: cb129929c49281548c79ccfbbdbb901824552f7190f760408698ae3d32794453
        B/clauses/window-05/raw.json: d3012e7b19861d60328b52f4f9c648c3f6e58cd45fd3ba7ef502f44da99add00
        B/clauses/window-05/prompt.txt: ed4e8b6ba2675e2c91288d20b2c9ce677529aba5e19c3db2c642175e11fcb261
        B/clauses/window-05/meta.json: dcf84bcaa711469c061e71132eab1bc71a1b791cab67734730ac2887f37530d6
        B/clauses/window-02/raw.json: 7e7612bff31196e7335eb0879780d45eeaa0bff60e63b7aad6182306ec6c9070
        B/clauses/window-02/prompt.txt: 287f8f31df12aa8d6ecbc274198367521fc7b9a53e8a75097282bd2e8155286c
        B/clauses/window-02/meta.json: fc308a110ee306e7bb32f188424021b0ee4ff1c34f70e4e6ebee5601c4ed1de5
        B/clauses/window-01/raw.json: 570a8449d53fe982c7d9731a04b62373bd2016b0c4c6b74b575ae62f64fd5929
        B/clauses/window-01/prompt.txt: 5182c6273456852d0a96b481d2b1395353dac9793abc5506850082a9899d26eb
        B/clauses/window-01/meta.json: eb4d8c22957c1b45fc7a3b64762cb57eb49b90fc11f59a41158625ef83becea3
        B/clauses/window-06/raw.json: 1591b38f2ca66669e0126054c02247d21cfa7dcf4d1e354383e155f7e5c6e2cf
        B/clauses/window-06/prompt.txt: c6f99f390ce762c147fce3c986ce04cc0feb52e84e4a0f2d96fa2f3f226fcfeb
        B/clauses/window-06/meta.json: 4f5de45bbd691708a5a0184eed71588a9845406e7b110e8dfd0616f8836b874e
        B/tables/TABLE-1-page-5-1/raw.json: f9e17e8c79a58e98f12500e9e568005821cebffffa8893a57d300f2a5dfa97dc
        B/tables/TABLE-1-page-5-1/prompt.txt: bd7691e6abd302943935e1a8368ca1c258b1437701e90a914cc6ee4f5a115531
        B/tables/TABLE-1-page-5-1/meta.json: 2335aba0ddf6a513f6d51a2e5fcff1682d427b6db6e2d7fe7992e35c8fdb6ff5
        B/tables/TABLE-S1-page-8-4/raw.json: 7c59c06af6812371cefbcb0660bf6d4eb610962109233d9d1a78e9dc378dbc3a
        B/tables/TABLE-S1-page-8-4/prompt.txt: 9fef35e6b0e5d03ee15d865fafba7bbafb2c5108fbcb3a037a942b6a0b5fd359
        B/tables/TABLE-S1-page-8-4/meta.json: cbb08da8730f105f37c15018643bf3036abba11fdf02cd0c293ed0ce58ce7546
        B/tables/TABLE-3-page-7-3/raw.json: 8f0186064549e1bd813f573b38bae4edd44e85d5e5a6dc14af44bef9693a8e8a
        B/tables/TABLE-3-page-7-3/prompt.txt: 8d4858c3a34cf6a3449b7775d51a1dec0aa7dfd0b81b1882963fbf1668355192
        B/tables/TABLE-3-page-7-3/meta.json: 6bbff8bbf3098178a60de5d7a2212e9eb818bbfa68db3058d5c0588775af170d
        B/tables/TABLE-2-page-7-2/raw.json: 0b230e0160f241285a47b3403f8d832d9f985a7b0e7c2a8b730e5c9fd33ae808
        B/tables/TABLE-2-page-7-2/prompt.txt: 59d57146d84a76e74264d7c70d4c1c89842b749c4edeaf825c013d9f638b4167
        B/tables/TABLE-2-page-7-2/meta.json: 30d786dd75cec34f648b56f8290763f518b46345f0c25eb9eb5ac4721c10494f
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
      pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2024
      source_status_sha256: 17ce8445f0cd5bb683fcb90133d4bdff31d158caafff47a61d9f9f20937ae6e4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R021
    exposure:
      text: mean diffusivity from the left uncinate fasciculus
    outcome:
      text: chronic change scores
    analysis_label: Chronic change correlation (UF)
    relation: association
    evidence_ids:
    - P5-S1-C14
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
      pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2024
      source_status_sha256: 17ce8445f0cd5bb683fcb90133d4bdff31d158caafff47a61d9f9f20937ae6e4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C6
      - Accounting without a linked unit P3-S3-C18
      - Unaccounted source passage P3-S3-C18
      - Result passage disposed without unit P3-S4-C2
      - Result passage disposed without unit P3-S4-C3
      - Result passage disposed without unit P4-S1-C2
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C4
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C13
      - Result passage disposed without unit P5-S1-C14
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P6-S1-C3
      - 'window 7: invalid/duplicate disposition P7-S1-C2'
      - Result passage disposed without unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C1
      - Accounting without a linked unit P7-S2-C2
      - Result passage disposed without unit P7-S2-C4
      - Result passage disposed without unit P7-S2-C5
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C1
      - 'window 9: invalid/duplicate disposition P8-S1-C2'
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C4
      unattached_null_or_qualifier_ids:
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S2-C4
      - P5-S1-C5
      - P5-S2-C2
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 117
      unselected_timing_passages:
      - P1-S2-C2
      - P2-S2-C6
      - P2-S2-C10
      - P5-S2-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S2-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      - TABLE-S1-page-8-4
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      - TABLE-S1-page-8-4
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
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
      source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2024
      source_status_sha256: 17ce8445f0cd5bb683fcb90133d4bdff31d158caafff47a61d9f9f20937ae6e4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports R2 for L-AFAD predicting subacute and chronic performance.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Reports L-IFOFAD and R-IFOFAD predicting subacute and chronic change
        scores.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports mediation of L-AF lesion load on chronic performance.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Conclusion restating results of L-AF and L-IFOF predictions.
    - source_id: P3-S3-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports general ANOVA significance across time points, not a specific
        relationship between exposure and outcome.
    - source_id: P3-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc comparisons of time points (T1 vs T2, T2 vs T3) are descriptive
        of recovery trajectory.
    - source_id: P3-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of change scores between phases is descriptive.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of change scores between phases is descriptive.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for relative change score comparisons.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports r-tPA effect on CS1, CS2, CS3 and null effect on change scores.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Identifies L-AF measurements as significant predictors for CS2 and CS3.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Identifies L-UFMD as significant predictor for CS2.
    - source_id: P4-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: General statement that only ventral stream measures predicted change
        scores.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Specifies L-IFOFAD for ΔCS1–2 and L-IFOFAD, R-IFOFAD, L-UFMD for ΔCS2–3.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for diffusion predictors of ΔCS1–3.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports L-IFOFAD for rΔCS1–2 and L-UFFA for rΔCS1–3.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for diffusion predictors of rΔCS2–3.
    - source_id: P4-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about model improvement with covariates.
    - source_id: P4-S1-C17
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates L-AFAD significance in CS3 model.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Identifies L-IFOFAD and lesion size as robust predictors in nested change
        models.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Reports significance and coefficient change of L-IFOFAD after adding
        baseline CS.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for diffusion measures in nested relative change models.
    - source_id: P4-S2-C5
      disposition: repeated
      result_indexes:
      - 15
      reason: Restates CS1 as robust predictor for rΔCS1–2.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 15
      - 16
      reason: Reports CS1 and lesion size as robust predictors for relative change
        models.
    - source_id: P5-S1-C3
      disposition: repeated
      result_indexes:
      - 16
      reason: Reports R2 for the rΔCS1–3 model.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 17
      reason: Reports CS1 as significant predictor for ΔCS1–3.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 18
      reason: Null mediation effect for L-IFOFAD on change scores.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 19
      reason: Null mediation effect for L-AFAD on CS2.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant mediation of L-AF lesion load on CS3.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Qualifies the mediation effect by showing L-AFAD becomes non-significant
        when lesion load is present.
    - source_id: P5-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Discussion restatement of L-AFAD and L-IFOFAD predictions.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 20
      - 21
      reason: Reports correlations of R-IFOFAD and L-UFMD with change scores.
    - source_id: P5-S1-C15
      disposition: repeated
      result_indexes:
      - 7
      reason: Restates rΔCS1–3 prediction.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about sensitivity to baseline and covariates.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 23
      reason: Identifies L-IFOFAD and L-AFAD as remaining significant after covariates.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 4
      reason: Restates that lesion load only influenced L-AF and chronic outcomes.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports L-UF MD association was not retained after covariates.
    - source_id: P7-S1-C14
      disposition: represented
      result_indexes:
      - 20
      reason: Reports R-IFOFAD positive correlation with later changes.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 20
      reason: Qualifies R-IFOFAD correlation as a compensatory role.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 22
      reason: Reports negative correlation of L-UFFA and L-AFFA with relative overall
        change.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 15
      - 16
      reason: Restates language baseline as a reliable predictor.
    - source_id: P8-S1-C7
      disposition: repeated
      result_indexes:
      - 12
      - 16
      reason: Restates lesion size as a significant predictor.
    unresolved_coverage:
    - source_id: P5-S1-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P7-S1-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C6
    - P3-S3-C18
    - P3-S4-C2
    - P3-S4-C3
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C9
    - P4-S1-C11
    - P4-S1-C13
    - P4-S1-C15
    - P4-S1-C17
    - P4-S2-C4
    - P5-S1-C3
    - P5-S1-C10
    - P5-S1-C12
    - P5-S1-C13
    - P5-S2-C2
    - P6-S1-C3
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P7-S1-C4
    - P7-S1-C6
    - P7-S1-C8
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C1
    - P7-S2-C4
    - P7-S2-C5
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C7
    - P8-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-7-2
    - TABLE-3-page-7-3
    - TABLE-S1-page-8-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S2-C2
      - P2-S2-C10
      recruited_sample:
      - P1-S2-C2
      - P2-S2-C6
      eligibility:
      - P2-S2-C7
      imaging_provenance:
      - P3-S1-C3
      - P3-S2-C1
      imaging_timing:
      - P1-S1-C9
      - P2-S2-C8
      - P3-S1-C3
      outcome_timing:
      - P1-S1-C9
      - P2-S1-C7
      - P2-S2-C8
      - P3-S2-C11
      - P3-S2-C12
      - P3-S3-C4
      outcome_definition:
      - P2-S1-C7
      - P2-S3-C11
      - P3-S1-C2
      validation: []
      analysis_restrictions:
      - P3-S3-C11
      - P3-S3-C12
      - P3-S3-C13
      - P3-S3-C14
      dependent_variable_statement:
      - P1-S1-C10
      - P3-S2-C11
      - P3-S2-C12
      - P3-S3-C4
      limitations:
      - P8-S1-C10
      - P8-S1-C11
      - P8-S2-C1
      personal_factors:
      - P1-S1-C10
      - P3-S3-C11
      - P4-S1-C15
      - P6-S1-C4
      - P7-S2-C5
      tested_personal_effects:
      - P4-S1-C4
      adjustment_roles:
      - P1-S1-C10
      - P3-S3-C11
      - P4-S1-C15
      - P6-S1-C4
      - P7-S2-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S2-C2
      - P2-S2-C10
      - P5-S2-C3
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S2-C9
      reason: No current-result classification; a covariate description is not an
        individual test
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
      pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
      review_sha256: cd9b6000c4c6eb033c3560061d7263ad03f593d6a7f6dae34a2489fd1aabf2cb
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
      - P5-S1-C14
      source_result: The source reports that left uncinate fasciculus mean diffusivity
        (L-UFMD) correlated with chronic change scores (specifically late change,
        ΔCS2-3, as per P4-S1-C10). This is a detected association in the regression/correlation
        analysis.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R021 targets the association between L-UFMD
            and chronic change scores. The source P5-S1-C14 explicitly states 'L-UFMD
            correlated with... chronic change scores'. P4-S1-C10 specifies that L-UFMD
            was significant in predicting ΔCS2-3 (late change), which is a component
            of chronic change. The analysis identity is consistent.
          source_ids:
          - P5-S1-C14
          - P4-S1-C10
        direction:
          answer: fits
          reason: The source confirms a significant correlation/association. The proposed
            draft uses 'likely' for direction, which is acceptable for a qualitative
            draft where the specific sign (positive/negative) might not be explicitly
            detailed in the summary text P5-S1-C14, though P4-S1-C10 implies significance.
            The core claim of association is preserved.
          source_ids:
          - P5-S1-C14
          - P4-S1-C10
        construct:
          answer: fits
          reason: Exposure is L-UFMD (mean diffusivity from left uncinate fasciculus).
            Outcome is chronic change scores. The source P3-S2-C1 confirms MD extraction
            from UF. P2-S3-C11 defines change scores. The construct is accurate.
          source_ids:
          - P3-S2-C1
          - P2-S3-C11
          - P5-S1-C14
        qualifications:
          answer: fits
          reason: The draft includes the qualification that chronic change scores
            represent the difference between subacute and chronic composite scores.
            This aligns with the definition of ΔCS2-3 in P2-S3-C11. No material qualifiers
            are lost.
          source_ids:
          - P2-S3-C11
          - P5-S1-C14
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the absence of cortical
            measures. The source P8-S1-C11 mentions this. No other material caveats
            (like the specific model type or collinearity exclusions) are omitted
            that would change the interpretation of the core association claim.
          source_ids:
          - P8-S1-C11
      optional_pending:
      - Specific direction (positive/negative) of the correlation
      - Exact statistical values (p-value, beta) for L-UFMD vs chronic change
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific direction (positive/negative) of the correlation
    - Exact statistical values (p-value, beta) for L-UFMD vs chronic change
    normalizations: []
    analysis_identity:
      id: R021
      exposure:
        text: mean diffusivity from the left uncinate fasciculus
      outcome:
        text: chronic change scores
      analysis_label: Chronic change correlation (UF)
      relation: association
      evidence_ids:
      - P5-S1-C14
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
        pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
        source_review: _compare/relationships-2026-11-16/review-current/OsaGarcia2024
        source_status_sha256: 17ce8445f0cd5bb683fcb90133d4bdff31d158caafff47a61d9f9f20937ae6e4
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9a779a314705e00e9017388832829465cd5c0419048b26366666735a98b6e098
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C10
          page: 2
          text_layer_sha256: 9a779a314705e00e9017388832829465cd5c0419048b26366666735a98b6e098
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Thus, a total sample of 24 participants \n(mean age, 70 years;\
          \ SD, 3; 8 women) completed the initial MRI \nand all 3 language assessments."
        anchor_text: "Thus, a total sample of 24 participants \n(mean age, 70 years;\
          \ SD, 3; 8 women) completed the initial MRI \nand all 3 language assessments."
        excluded_fragments: []
        image_sha256: 9ae35574fcf2a5498316f0a5f4331925914385f0fd2a30cbaf71f915d48e1664
        transcription: '. Thus, a total sample of 24 participants

          (mean age, 70 years; SD, 3; 8 women) completed the initial MRI

          and all 3 language assessments'
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1acf9edcf998adb26344d96b68ebb8350745c836c6dd29cf5d1da51244c7c252
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 1acf9edcf998adb26344d96b68ebb8350745c836c6dd29cf5d1da51244c7c252
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "METHODS\nParticipant Recruitment and Procedure\nWe recruited\
          \ 39 participants with aphasia resulting from a \nfirst ischemic stroke\
          \ in the left middle cerebral artery territory \nat an acute care hospital."
        anchor_text: "METHODS\nParticipant Recruitment and Procedure\nWe recruited\
          \ 39 participants with aphasia resulting from a \nfirst ischemic stroke\
          \ in the left middle cerebral artery territory \nat an acute care hospital."
        excluded_fragments: []
        image_sha256: ef725caf4b3a985a420f447c08a1c70bbc5aca64f4aed7d64dc1f529eb2dd740
        transcription: 'METHODS


          Participant Recruitment and Procedure


          We recruited 39 participants with aphasia resulting from a first ischemic
          stroke in the left middle cerebral artery territory at an acute care hospital'
      P2-S2-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 97879f7958c0ed026714653549c73608c5240d1562ec101c151d0b9631e19637
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: eaacadcfca6a230ba6ab28ec15aa90bf7be5606ca57b216d34d03c8cd2f5262a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C8
          page: 2
          text_layer_sha256: eaacadcfca6a230ba6ab28ec15aa90bf7be5606ca57b216d34d03c8cd2f5262a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Following the protocol out-\nlined by Saur et al,13 language\
          \ assessments and MRI scans were \nconducted within 3 days (acute, T1),\
          \ 7 to 15 days (subacute, \nT2), and at least 6 months (chronic, T3) poststroke."
        anchor_text: "Following the protocol out-\nlined by Saur et al,13 language\
          \ assessments and MRI scans were \nconducted within 3 days (acute, T1),\
          \ 7 to 15 days (subacute, \nT2), and at least 6 months (chronic, T3) poststroke."
        excluded_fragments: []
        image_sha256: fbeda9074f4e953c2b92b92d63d160fb33ea6fcaab35702123761120db06d619
        transcription: '. Following the protocol out-

          lined by Saur et al,¹³ language assessments and MRI scans were

          conducted within 3 days (acute, T₁), 7 to 15 days (subacute,

          T₂), and at least 6 months (chronic, T₃) poststroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "In addition, R-IFOFAD correlated \npositively with chronic change scores,\
    \ and L-UFMD cor-\nrelated with both subacute performance scores and \nchronic\
    \ change scores."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
