---
id: speech_fluency_cluster
name: speech fluency cluster
kind: network
findings:
- id: f1
  target: speech_fluency
  target_kind: impairment
  claim: Impaired speech fluency is associated with damage involving the Rolandic
    operculum, pars opercularis, pars triangularis, insula, precentral gyrus, middle
    frontal gyrus, and the white matter underlying Broca's area and surrounding structures.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 64
    population: patients with chronic left hemisphere stroke
    phase: not_reported
    time_post_onset: chronic phase (>6 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The WAB fluency scale is noted by the authors to be a flawed shorthand that plots
    qualitative data on an interval scale and lacks careful reliability assessment.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Voxel-by-voxel image intensity (represented as Z-scores
    normalized to the intact right hemisphere) on T1-MRI scans. The association remained
    approximately the same when auditory word-picture matching, diadochokinetic rate,
    and matrix reasoning scores were included as cofactors, although overall Z-scores
    were lower. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P3-S1-C3, two-model agreement, human
    verification pending): . Out of 76 patients included in

    the database, data from 64 patients (29 females) who had incurred a

    single left hemisphere stroke (60 ischaemic; four haemorrhagic) result-

    ing in chronic aphasia (>6 months post-stroke) were included in this

    research (Supplementary material) Original text-layer quotation is preserved below.'
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
    - proposed_concept:speech_fluency
  citation: '@Fridriksson2013'
  source_passages:
  - section: Original source P7-S1-C8
    page: 7
    quote: 'Impaired speech ﬂu-

      ency is associated with damage mostly involving the Rolandic

      operculum, pars opercularis, pars triangularis, insula, precentral

      gyrus, middle frontal gyrus, and the white matter underlying

      Broca’s area and surrounding structures (Fig. 5A).'
    supports: claim
  - section: Original source P3-S1-C3
    page: 3
    quote: 'Out of 76 patients included in

      the database, data from 64 patients (29 females) who had incurred a

      single left hemisphere stroke (60 ischaemic; four haemorrhagic) result-

      ing in chronic aphasia (46 months post-stroke) were included in this

      research (Supplementary material).'
    supports: sample
  - section: Original source P4-S1-C5
    page: 4
    quote: 'We made one modiﬁcation to the methods proposed by

      Tyler et al. (2005): instead of including the mean image intensity value

      as a co-factor, Z-scores were calculated on voxel-by-voxel basis for

      each patients’ T1-MRI based on the mean and standard deviation of

      the structurally intact (right) hemisphere.'
    supports: method
  - section: Original source P7-S1-C10
    page: 7
    quote: 'Subsequent analyses that separ-

      ately included auditory word-picture matching, diadochokinetic

      rate, and scores from the Matrix Reasoning test as cofactors

      revealed approximately the same lesion location as when no

      cofactors were included; albeit, with lower overall Z-scores.'
    supports: confounders
  - section: Original source P2-S4-C4
    page: 2
    quote: 'There are many criticisms of this scale, including

      the plotting of essentially qualitative data on an interval scale,

      lack of careful reliability assessment, and failure to take features

      such as articulatory agility and prosody into account [see Gordon

      (1998), for a discussion of these issues].'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2013
  proposal_id: R015
  review_status_sha256: 1c9116c6c31c9d6a7ed28d6d946c53c60d6bb415233f00f2a5c2c8d765180a92
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
        A/passages.json: 4ccc0c36dfb641b5e7f369328267e83632f6f65450e73b2c766f7d991900d262
        A/raw.json: b997db2184d92781459a10472d6fc1d549a73aeb37b06689b6708cfd5a2ecb37
        A/source-units.json: c7ad8d49769e136009c82dbaec7a2e6bf2eace3131b3aa9ba44df781d598a486
        A/full-source-units.json: 92c72bc6ec60a77d7dd040847423c3c929843080081f324d1a1e6a2d0d34c0ba
        A/meta.json: 2f0459a73d9d6492303ebe81fcc584461cf6ab775f5acfb24bf334b9523ae195
        A/table-images/TABLE-1-page-6-1.png: c5eed8caebcc5b593b9a49fa498b03e0718d91df92532470006d7fcd5ac7e774
        A/table-images/page-6.png: 54c1f7be424efe3888ac2f23ed62531e3e8ad491b9452cddefb3472bea002525
        A/table-images/manifest.json: f531d4f6fc54e0d1f011343867269d65f77286178682a812636b6c6f7652425a
        A/clauses/window-03/raw.json: d1171a1996529843e2b2a7f1a17c0a6e2d8070ba3a8f778f482a8afd563520e7
        A/clauses/window-03/prompt.txt: 5e78d677802011739d2d4f737020ad48be09127559f67f94357ae4ac44757903
        A/clauses/window-03/meta.json: 8444fc4378182952e2738897394a124bb2d1c371b2c044cfd70d1015235a9691
        A/clauses/window-04/raw.json: 993409e30fd29b8cbfaf059bbaa7e114cb9724d1dc2fcea5b1cfa3d90b8b201f
        A/clauses/window-04/prompt.txt: 04fd7c6e49a6c0a434b5e50deedad1f20bcd306dce36c3e4a2324dabf7c01766
        A/clauses/window-04/meta.json: aa6629bdb2250a148fe9d2e4e0367668573d640ab2c5e6773447cc80a53dc891
        A/clauses/window-05/raw.json: 5a06cec99db44b4dea18a92f48ee94eb848f69ca769ed15b96225e441da1dab2
        A/clauses/window-05/prompt.txt: cf4ded0070e9c3a4b03569c854dc1b2c66ff3bfcec7a1dbf06aa17dda7a1dafc
        A/clauses/window-05/meta.json: 1609ee8c8cc095b89f13f73fb82b6909e29ef19ee35665779ba0ede7c5bbc2b1
        A/clauses/window-02/raw.json: 4d82ad59be7ce04fb03d0c401a66d46ae9fb2c9ea96ca0ed94eea6b05343eef8
        A/clauses/window-02/prompt.txt: bc8930f491f9e8e25891efd6f0b0e71f83951224248738807e7e9a59fa91c381
        A/clauses/window-02/meta.json: 4a0ef3f3ca423c2f2ca02e1566fc26fdfe194919582bd11f2d066181bff8e800
        A/clauses/window-07/raw.json: a774963e020fb9a525c8f604b0a10b289317f575350be977a35cd82ee10e3bec
        A/clauses/window-07/prompt.txt: 2cdaef328f1607d4b92d1ded198ba6f1f6bff43374136ef8c68ee85ed927bdbb
        A/clauses/window-07/meta.json: 69037944386fb175ce6e4b35f1adf11bc8c8746dd995775408601b553b7d2af8
        A/clauses/window-01/raw.json: 0327f8a83571ffaadbcca7d90af1127494f62878a7c6d4828f02574ed0b5d720
        A/clauses/window-01/prompt.txt: 668369decc452f7031dbc274bed19936cd717e27ad7a1dcbc63f5c7a6ecffc0d
        A/clauses/window-01/meta.json: daf988c201e9fbe8c53a8d7855c9b61aaa94caca12eec7de251f125d76edc4e1
        A/clauses/window-06/raw.json: b0c593e8297120c4fb9e52cf66da3e4b4b4aaeff24bd4fa033ee6e1dbe1aacec
        A/clauses/window-06/prompt.txt: 059512ab1338466ca0f13fecb2d17d1460fbc25ab477f1185188d38abcc30b06
        A/clauses/window-06/meta.json: 0e33e3f4f73ffe0aebb06a7c7b4c1e939385bbac023fca70e2e89bc3121d0c87
        A/tables/TABLE-1-page-6-1/raw.json: b8e664f89c5577cf42ce42fb4755b427b2eb8944391c73a97c9db8f5ef921a33
        A/tables/TABLE-1-page-6-1/prompt.txt: 2785485affcf2b7bcb3569bff6fca6d024808f1f02dcedb3be881af25a7b2e76
        A/tables/TABLE-1-page-6-1/meta.json: 23ad833da74a842400d07ce422b96effe55a753bc8d4b60b016597ee11e4d924
        B/passages.json: 4ccc0c36dfb641b5e7f369328267e83632f6f65450e73b2c766f7d991900d262
        B/raw.json: ee6451b3ad7f2333898e0ed3bb5dd6e68b031efeadb3e42f11f7757211c0ab2b
        B/source-units.json: c7ad8d49769e136009c82dbaec7a2e6bf2eace3131b3aa9ba44df781d598a486
        B/full-source-units.json: 92c72bc6ec60a77d7dd040847423c3c929843080081f324d1a1e6a2d0d34c0ba
        B/meta.json: 65a6e876d9b8450e1450d164c2237c9f730b6b0c811dca4b9187cf4f950b7406
        B/table-images/TABLE-1-page-6-1.png: c5eed8caebcc5b593b9a49fa498b03e0718d91df92532470006d7fcd5ac7e774
        B/table-images/page-6.png: 54c1f7be424efe3888ac2f23ed62531e3e8ad491b9452cddefb3472bea002525
        B/table-images/manifest.json: 73b189b29762960240082bfb68846421c043988765b6b575243cc83143db6218
        B/clauses/window-03/raw.json: bba19aaaa62c7809199aad5c5a6e2e202f842868456da80bab9b7233ddfa9d77
        B/clauses/window-03/prompt.txt: 5e78d677802011739d2d4f737020ad48be09127559f67f94357ae4ac44757903
        B/clauses/window-03/meta.json: 4ac7ae9d2d31e1d0b7534e0cb2d9599ed452bb48e99248d7bfa557dd20cb3584
        B/clauses/window-04/raw.json: 72ff0fc4331ef87a30e17ceb00d56f5a538f193b26ecdbf5bf0e4107be125413
        B/clauses/window-04/prompt.txt: 04fd7c6e49a6c0a434b5e50deedad1f20bcd306dce36c3e4a2324dabf7c01766
        B/clauses/window-04/meta.json: b683afd0ac9b41ef618f8d7d60c0be97395c77f59fa01456496e5415738475e8
        B/clauses/window-05/raw.json: a6c6583c78005650426b8aac94d47b4c30d8155d815207fbee2f3d402fe85c32
        B/clauses/window-05/prompt.txt: cf4ded0070e9c3a4b03569c854dc1b2c66ff3bfcec7a1dbf06aa17dda7a1dafc
        B/clauses/window-05/meta.json: ea1fe77c07d4410aef8e912b4195ca81b789505494ba6aaa9b1e23176c3b39d5
        B/clauses/window-02/raw.json: ec97ff547c42393b9c1b5d37ada9f4dfb12b0be1833e5cccad229b4b66f96e25
        B/clauses/window-02/prompt.txt: bc8930f491f9e8e25891efd6f0b0e71f83951224248738807e7e9a59fa91c381
        B/clauses/window-02/meta.json: 2dabbc96771bc08457bf5dc55b9ba231a49877c1dd4b3e44bdd59aae8232a340
        B/clauses/window-07/raw.json: c2093b43265355fa1975e0c372db8da2dbf87767865c853c891b94b988e90d78
        B/clauses/window-07/prompt.txt: 2cdaef328f1607d4b92d1ded198ba6f1f6bff43374136ef8c68ee85ed927bdbb
        B/clauses/window-07/meta.json: 3d716b47281b1ed68b01b85e104ea922abfba8ce6c697adc165cf662531e1178
        B/clauses/window-01/raw.json: 3594673bdc02f9bda74c869fc53382ad300c4f97be1b01c0a5a5c615141c2561
        B/clauses/window-01/prompt.txt: 668369decc452f7031dbc274bed19936cd717e27ad7a1dcbc63f5c7a6ecffc0d
        B/clauses/window-01/meta.json: f9f4349e69e59c38171d2361d020206f0e156b0953d4ce1de749e0ed55eacb74
        B/clauses/window-06/raw.json: db76914af3eca732fc8b0ae7115570ad766df7b7fafbd6a198dbe5e81d9fe264
        B/clauses/window-06/prompt.txt: 059512ab1338466ca0f13fecb2d17d1460fbc25ab477f1185188d38abcc30b06
        B/clauses/window-06/meta.json: cb8b56f84ffafd8d8852f763f2dd144c9026ff48eaaa24c2a940cdcb32902bba
        B/tables/TABLE-1-page-6-1/raw.json: 6dc4ceaeb2ccf681e9e0f0045e8ef1c077c1e2bd7bb6562982f74c9b6338aaf0
        B/tables/TABLE-1-page-6-1/prompt.txt: 2785485affcf2b7bcb3569bff6fca6d024808f1f02dcedb3be881af25a7b2e76
        B/tables/TABLE-1-page-6-1/meta.json: bbe02448d5137fa7e227fb8bf4d9e1de82d1fb92aabde5a912e116174320292c
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
      pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2013
      source_status_sha256: be5d34fc805d5174ae5e5836c84fa1a30e8400db4491eedddf5954083f6de160
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R015
    exposure:
      text: Rolandic operculum, pars opercularis, pars triangularis, insula, precentral
        gyrus, middle frontal gyrus, and white matter underlying Broca's area
    outcome:
      text: speech fluency
    analysis_label: Whole brain VLSM (no cofactor)
    relation: association
    evidence_ids:
    - P7-S1-C8
    qualifier_ids:
    - P7-S1-C9
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2013
      source_status_sha256: be5d34fc805d5174ae5e5836c84fa1a30e8400db4491eedddf5954083f6de160
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S2-C2
      - Accounting without a linked unit P1-S2-C3
      - Result passage disposed without unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C5
      - Result passage disposed without unit P1-S2-C6
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S2-C5
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S2-C2
      - Result passage disposed without unit P3-S1-C11
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C12
      - Accounting without a linked unit P3-S3-C11
      - Unaccounted source passage P3-S3-C11
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S3-C4
      - Result passage disposed without unit P8-S3-C5
      - 'window 9: invalid/duplicate disposition P8-S3-C7'
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 139
      unselected_timing_passages:
      - P1-S1-C7
      - P3-S1-C1
      - P3-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S3-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P5-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C6
        - P1-S2-C3
        - P1-S2-C6
        - P2-S3-C4
        - P2-S3-C5
        - P3-S3-C4
        - P4-S1-C4
        - P4-S3-C5
        - P4-S3-C7
        - P4-S4-C4
        - P5-S1-C1
        - P5-S1-C3
        - P5-S1-C5
        - P5-S1-C6
        - P7-S1-C10
        - P8-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      unlinked_tables:
      - TABLE-1-page-6-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S3
        - P4-S3
        - P4-S4
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2013
      source_status_sha256: be5d34fc805d5174ae5e5836c84fa1a30e8400db4491eedddf5954083f6de160
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the general relationship being tested and the sample size.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Abstract statement of the primary ROI finding.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Abstract statement of the improved prediction model.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      - 6
      reason: Abstract summary of results controlling for cofactors.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Abstract statement that whole brain analyses corroborated ROI findings.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Abstract statement regarding uncinate fasciculus and aphasia type.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      - 4
      - 6
      reason: Summary statement of robustness across cofactors.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap map (Figure 1).
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean Aphasia Quotient.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports distribution of aphasia types.
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap in the insula.
    - source_id: P4-S4-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Primary ROI result for speech fluency.
    - source_id: P4-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 1.
    - source_id: P4-S4-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Second ROI model result for speech fluency.
    - source_id: P4-S4-C9
      disposition: represented
      result_indexes:
      - 1
      reason: F-change test for the second model.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: ROI results with picture-word recognition cofactor.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: ROI result with diadochokinetic rate cofactor (Model 1).
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: ROI result with diadochokinetic rate cofactor (Model 2).
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 7
      reason: ROI result with matrix reasoning cofactor.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: ROI results for auditory word-picture recognition.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: ROI result for diadochokinetic rate.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Qualification of significance for diadochokinetic rate model.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Null result for matrix reasoning ROI analysis.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 13
      reason: Exploratory ROI difference between Broca's and global aphasia.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes global aphasia group image intensity.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Levene's test for variance.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of lesion volume between groups.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of time post-stroke between groups.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Linear regression for auditory comprehension in Broca's vs global aphasia.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on whole brain analysis significance.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 14
      reason: Whole brain association for speech fluency.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 14
      reason: Highest Z-score location for speech fluency.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 15
      reason: Sensitivity of whole brain results to cofactors.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 16
      reason: Whole brain association for auditory word-picture matching.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 16
      reason: Highest Z-score location for auditory word-picture matching.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 17
      reason: Null whole brain results for diadochokinetic rate and matrix reasoning.
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 17
      reason: Restatement of null whole brain results.
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of uncinate fasciculus contribution.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      - 4
      - 6
      reason: Discussion restatement of ASAF robustness.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 8
      - 9
      - 16
      reason: Discussion restatement of auditory word-picture recognition results.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of diadochokinetic rate results.
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 11
      - 17
      reason: Discussion restatement of null matrix reasoning results.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Figure 5B.
    - source_id: P8-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 10
      - 14
      reason: Discussion summary of non-fluent aphasia markers.
    - source_id: P8-S3-C3
      disposition: repeated
      result_indexes:
      - 13
      reason: Discussion restatement of uncinate fasciculus/temporal pole difference.
    - source_id: P8-S4-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of ASAF effect.
    - source_id: P8-S4-C2
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      - 4
      - 6
      reason: Conclusion restatement of ASAF robustness.
    unresolved_coverage:
    - source_id: P7-S1-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C2
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P3-S1-C4
    - P3-S1-C11
    - P3-S1-C12
    - P3-S3-C11
    - P4-S4-C7
    - P4-S4-C9
    - P5-S1-C8
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C9
    - P7-S1-C12
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P8-S1-C2
    - P8-S1-C11
    - P8-S3-C3
    - P8-S3-C4
    - P8-S3-C5
    - P8-S3-C10
    - P8-S4-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C3
      recruited_sample:
      - P3-S1-C1
      - P3-S1-C5
      eligibility:
      - P3-S1-C2
      imaging_provenance:
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
      - P4-S1-C5
      - P4-S1-C11
      imaging_timing:
      - P3-S1-C3
      outcome_timing:
      - P3-S1-C3
      outcome_definition:
      - P2-S3-C10
      - P2-S3-C11
      - P2-S4-C3
      - P3-S2-C3
      validation: []
      analysis_restrictions:
      - P4-S3-C7
      - P4-S4-C5
      dependent_variable_statement:
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P4-S1-C12
      limitations:
      - P2-S4-C4
      - P2-S4-C5
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C7
      - P8-S2-C8
      - P8-S3-C7
      personal_factors: []
      tested_personal_effects:
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P7-S1-C6
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C3
      - P3-S1-C6
      - P3-S1-C11
      - P3-S1-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S3-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P5-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C6
      - P1-S2-C3
      - P1-S2-C6
      - P2-S3-C4
      - P2-S3-C5
      - P3-S3-C4
      - P4-S1-C4
      - P4-S3-C5
      - P4-S3-C7
      - P4-S4-C4
      - P5-S1-C1
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      - P7-S1-C10
      - P8-S1-C4
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
      pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
      review_sha256: 1c9116c6c31c9d6a7ed28d6d946c53c60d6bb415233f00f2a5c2c8d765180a92
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
      - P7-S1-C8
      source_result: The source reports that impaired speech fluency is associated
        with damage involving the Rolandic operculum, pars opercularis, pars triangularis,
        insula, precentral gyrus, middle frontal gyrus, and white matter underlying
        Broca's area. This association was identified using whole-brain VLSM (voxel-wise
        lesion-symptom mapping) based on T1-MRI intensity (Z-scores) in 64 patients
        with chronic left hemisphere stroke. The association remained approximately
        the same when cofactors (auditory word-picture matching, diadochokinetic rate,
        matrix reasoning) were included, though with lower Z-scores.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the whole-brain VLSM analysis
            for speech fluency without cofactors, as described in P7-S1-C8 and P4-S3-C12.
            The proposed core correctly identifies this as the primary analysis yielding
            the specific anatomical cluster.
          source_ids:
          - P7-S1-C8
          - P4-S3-C12
        direction:
          answer: fits
          reason: The source states 'Impaired speech fluency is associated with damage...',
            which aligns with the proposed claim of association between damage and
            impaired fluency. The direction is consistent with the detection of a
            significant relationship.
          source_ids:
          - P7-S1-C8
        construct:
          answer: fits
          reason: The exposure (anatomical regions) and outcome (speech fluency via
            WAB) are correctly identified. The method is correctly described as VLSM
            using T1-MRI intensity. The patient measurement is template_lesion_overlap
            because the analysis relates image intensity (Z-scores) in normalized
            space to behavior, which is the core of the VLSM method described in P3-S3-C9
            and P4-S1-C2, rather than patient-specific tractography or raw diffusion
            data.
          source_ids:
          - P7-S1-C8
          - P3-S3-C9
          - P4-S1-C2
        qualifications:
          answer: fits
          reason: The qualification regarding the robustness of the association when
            cofactors are included is correctly captured from P7-S1-C10. The limitation
            regarding the WAB scale is correctly captured from P2-S4-C4. The draft
            correctly treats the cofactor analysis as a qualification/robustness check
            rather than a separate primary finding.
          source_ids:
          - P7-S1-C10
          - P2-S4-C4
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft includes the key limitation
            about the WAB scale and the robustness qualification. The small sample
            size for the Broca's vs Global comparison is not relevant to this specific
            whole-brain fluency analysis.
          source_ids:
          - P7-S1-C8
          - P7-S1-C10
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
      id: R015
      exposure:
        text: Rolandic operculum, pars opercularis, pars triangularis, insula, precentral
          gyrus, middle frontal gyrus, and white matter underlying Broca's area
      outcome:
        text: speech fluency
      analysis_label: Whole brain VLSM (no cofactor)
      relation: association
      evidence_ids:
      - P7-S1-C8
      qualifier_ids:
      - P7-S1-C9
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2013
        source_status_sha256: be5d34fc805d5174ae5e5836c84fa1a30e8400db4491eedddf5954083f6de160
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7e14fb39c463a67c5398298527ca83c246df802c0a17afd9f725fd1a42ad34c7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f711d513456462bf920661253951ff870fec4ffa8299552d187b24b0da0873e4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C3
          page: 3
          text_layer_sha256: f711d513456462bf920661253951ff870fec4ffa8299552d187b24b0da0873e4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Out of 76 patients included in

          the database, data from 64 patients (29 females) who had incurred a

          single left hemisphere stroke (60 ischaemic; four haemorrhagic) result-

          ing in chronic aphasia (46 months post-stroke) were included in this

          research (Supplementary material).'
        anchor_text: 'Out of 76 patients included in

          the database, data from 64 patients (29 females) who had incurred a

          single left hemisphere stroke (60 ischaemic; four haemorrhagic) result-

          ing in chronic aphasia (46 months post-stroke) were included in this

          research (Supplementary material).'
        excluded_fragments: []
        image_sha256: f3c20bb04046151425687c39145d3f84ea877e9e186a8a0d54e35034a9dc79c0
        transcription: '. Out of 76 patients included in

          the database, data from 64 patients (29 females) who had incurred a

          single left hemisphere stroke (60 ischaemic; four haemorrhagic) result-

          ing in chronic aphasia (>6 months post-stroke) were included in this

          research (Supplementary material)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'Impaired speech ﬂu-

    ency is associated with damage mostly involving the Rolandic

    operculum, pars opercularis, pars triangularis, insula, precentral

    gyrus, middle frontal gyrus, and the white matter underlying

    Broca’s area and surrounding structures (Fig. 5A).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
