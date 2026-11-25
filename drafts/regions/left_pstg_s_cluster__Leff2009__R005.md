---
id: left_pstg_s_cluster
name: left posterior superior temporal gyrus and sulcus cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: spoken_sentence_comprehension
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: spoken_sentence_comprehension
  target_kind: impairment
  claim: structural integrity of the left posterior superior temporal gyrus and sulcus
    cluster is significantly correlated with spoken sentence comprehension scores
  direction: likely
  relationship: correlational
  method: VBM
  sample:
    n: 210
    population: stroke patients with a digit span of at least two
    phase: not_reported
    time_post_onset: median 35 months post-stroke (range >1 month); imaging and testing
      occurred within one week of each other
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - structural MRI limitations for white-matter labels
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: grey matter density within a cluster in the left posterior
    superior temporal gyrus and sulcus, identified via voxel-based morphometry as
    covarying with auditory short-term memory capacity. analysis controlled for auditory
    word repetition, auditory non-word repetition, verbal fluency, picture naming,
    and stroke volume; the correlation was not significant for single word comprehension
    or written sentence comprehension. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S1-C11,
    two-model agreement, human verification pending): . One

    hundred and twenty-eight (61%) were male and 186 (89%) were

    right-handed, with a mean age of 59 years (SD = 14) Original text-layer quotation
    is preserved below. PDF image reading (P3-S2-C4, two-model agreement, human verification
    pending): . The median time after stroke

    upon testing was 35 months (interquartile range=12–74 months),

    with a skew towards relatively recent stroke (26% ≤ 12 months)

    The minimum time since stroke was >1 month to avoid testing

    patients in the acute and subacute phases Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:spoken_sentence_comprehension
  citation: '@Leff2009'
  source_passages:
  - section: Original source P6-S1-C2
    page: 6
    quote: 'The

      right panel of Fig. 4 illustrates the signiﬁcant correlation between

      the structural

      integrity

      of this

      region

      and spoken

      sentence

      comprehension

      score,

      r(199) = 0.22,

      P = 0.002

      (right

      panel

      Fig. 4), but not single word comprehension, r(199) = -0.03,

      P = 0.66 or written sentences, r(199) = 0.05, P = 0.45.'
    supports: claim
  - section: Original source P5-S3-C5
    page: 5
    quote: 'This region forms part of the left posterior

      superior temporal gyrus and sulcus (Fig. 3 lower panel and

      Table 1).'
    supports: method
  - section: Original source P5-S1-C8
    page: 5
    quote: 'Statistical analysis

      All statistical analyses used voxel-based morphometry; that is a whole-

      brain, unbiased, semi-automated technique for characterizing regional

      differences in structural magnetic resonance images (Ashburner and

      Friston, 2000).'
    supports: method
  - section: Original source P3-S1-C11
    page: 3
    quote: 'One

      hundred and twenty-eight (61%) were male and 186 (89%) were

      right-handed, with a mean age of 59 years (SD = 14).'
    supports: sample
  - section: Original source P3-S2-C4
    page: 3
    quote: 'The median time after stroke

      upon testing was 35 months (interquartile range = 12–74 months),

      with a skew towards relatively recent stroke (26% 4 12 months)

      The minimum time since stroke was 41 month to avoid testing

      patients in the acute and subacute phases.'
    supports: sample
  - section: Original source P4-S3-C8
    page: 4
    quote: 'MRI data acquisition

      All subjects were scanned either on the same day or within one week

      of their behavioural testing.'
    supports: sample
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      To conﬁrm the relationship between the structural integrity

      of this region of cortex and language comprehension, we used

      the values from the principal eigenvariate extracted from the sig-

      niﬁcant cluster identiﬁed in Analysis 2 (see above) and performed

      partial regression against each of the measures of language

      comprehension (controlled variables were as Analysis 2).'
    supports: method
  - section: Original source P3-S2-C6
    page: 3
    quote: 'Behavioural assessments

      All 210 patients’ language abilities were assessed using the compre-

      hensive aphasia test (Swinburn et al., 2004).'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Leff2009
  proposal_id: R005
  review_status_sha256: f28921f4b0c7063f00337df363d113c68b0f72d34df933303d6b3fbef7719037
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
        A/passages.json: 7d7466f187aa6bd8886074890442d4fe83ec6cc6c52b2c602209f572035d2d28
        A/raw.json: f4177c64900dbd1a02e70e7dd8323bc1aa1a57395b7e1adea1a66ce8442c7dda
        A/source-units.json: 79bc7bafa309e76e13651d188a5f4c73bece776db558c9f26220288b8c893a42
        A/full-source-units.json: f69d7329812dc824388d76062d7a9f501a607c669ff7ed9440880431364aa6b2
        A/meta.json: b620ac1a27be4bbb01f18905d5c0eda18ba93a37b130629b8d19299a0790c842
        A/table-images/TABLE-1-page-8-1.png: fa00c611c537454833dee6fa3f828b80facde3a3e55a17a9cbbe69cbe655e041
        A/table-images/page-8.png: 36758993895380ed596874ff4b7b68f8036e795b14cd4e9eca8c4a1471e5c231
        A/table-images/manifest.json: 90ab8158047b0c43cb9218f104f854920011173edf65af361dd625443325d542
        A/clauses/window-03/raw.json: 668fed20b016856da3682b6617eee067a84db7fe0a3b175ea70d75d2230a3dd9
        A/clauses/window-03/prompt.txt: f0ec483046eaa38b630b657322928fd8b13c191783732099f2808463317abc55
        A/clauses/window-03/meta.json: 72b546e5200f72a01d9625def99695a012515aad66a25f293bc1edf37c5c5a51
        A/clauses/window-04/raw.json: 0735e888661fcf680a628b97dce27cb287969dcc41e82ebdfe12d79f58802d18
        A/clauses/window-04/prompt.txt: 8a5d22846b0f7e609f1a84c0ba3a78307c875b048fc4b2915bf0f1a5a79fb140
        A/clauses/window-04/meta.json: 508810722e71427bbe662bf4d3a78da94647fc4ad0f16e0be90978f5b9ab819f
        A/clauses/window-05/raw.json: 7079183b97bcc6780e7686dcef507d3a1e2b4367265249e04d5751f7d26229c1
        A/clauses/window-05/prompt.txt: 5810716fda7e07b63aac838e39f998d1a37f55d5135fa6d833dbad7d9dfb5d7c
        A/clauses/window-05/meta.json: ea0a23958d81587cd7f9ae77076c6d3b0c1ce1a954f19f9dd65ba81d86c84d44
        A/clauses/window-02/raw.json: 8736c5ec201fd974391750249b23205721a1ca5fbd03e5576e085765c2f44c3f
        A/clauses/window-02/prompt.txt: d867d755c3836ec1fde2055fa611f2833e7cbee9baa8efe6bfa7a74f826a84a0
        A/clauses/window-02/meta.json: 3b9f2cb223ab573b8582e486ac92a381ee56491af299f7cf52f1f88367e384a1
        A/clauses/window-09/raw.json: c44df1a26f4ea51b3056ebf2f776ca9902bfcded4facf7996510c6ce51bda833
        A/clauses/window-09/prompt.txt: cb03e05b6c73d38906134809a4a4ff718e5cd21fff2bfaf5882dd3658dcd7272
        A/clauses/window-09/meta.json: 4e66e19982ad351b20e0e205b9849de8c3c8bdef104e8fd1fcbea4f1da26af70
        A/clauses/window-07/raw.json: 375264410ea58f8d38a6756f9dd7678ad4dfbed4621c59bfe2bbe3169165c378
        A/clauses/window-07/prompt.txt: a1d1beb0928b4e5f0b6fb877a4c0221fdbc36fe6f75aecf9e1e654a9fc87280b
        A/clauses/window-07/meta.json: 80deee569674db5d751ce3955c32dd011855f3117ce2a2e9b8dd4363f31be1fc
        A/clauses/window-01/raw.json: 253ae24fabbb9daee2c3fa6076f29283b40910b4a684b4501e693d2eedeb7ca6
        A/clauses/window-01/prompt.txt: 2dc7981b81d4b34877532de8d8b045f872c71be2d740671cc39767b4465aa3bb
        A/clauses/window-01/meta.json: f4389165b376cf795d2c49212f6fe6b692cfe4bee11c32319d828b7f26175566
        A/clauses/window-06/raw.json: 2097616c0b38bd2fca94f056a81d900bab9fcf8c450ada7a02373c7a3dfe0ad4
        A/clauses/window-06/prompt.txt: 884e14aae16f061486fdbe045ecde9c88cfd87f4f3d5fb05113c6ca6a9fb1139
        A/clauses/window-06/meta.json: f04223d1bcf03b73a014bcda9700d547a815acb461ab359b1cdb2d6e4bafcc1f
        A/clauses/window-08/raw.json: 007c56413c50caca1e74fa32885683c216bd9887da32079842af606582ae2344
        A/clauses/window-08/prompt.txt: e78e668d14a3543c8e1ffe63e03acbb4c4b9eb168178eade8735fdcb2124f812
        A/clauses/window-08/meta.json: 8ef8a498cefa1f9b06ed433101cf1507f987ab67505b8d8addd11fad5d79cca5
        A/tables/TABLE-1-page-8-1/raw.json: 1139b9f0c3818064b99a7c8d9a6674e1819738edfb1c9d90a999ed93c28dfeab
        A/tables/TABLE-1-page-8-1/prompt.txt: ff03b86d878ccd35ea16875451f8eb9dad22a4282a18101457c08cfcfbd547da
        A/tables/TABLE-1-page-8-1/meta.json: 95bbcb7b237235f73ed55dce075a1deded5b707659ab76ee0570a28eb4275e93
        B/passages.json: 7d7466f187aa6bd8886074890442d4fe83ec6cc6c52b2c602209f572035d2d28
        B/raw.json: 00f3bdf4ab9e4de6934870195a75497faee4064ba2f0091a3f5c20c620713af6
        B/source-units.json: 79bc7bafa309e76e13651d188a5f4c73bece776db558c9f26220288b8c893a42
        B/full-source-units.json: f69d7329812dc824388d76062d7a9f501a607c669ff7ed9440880431364aa6b2
        B/meta.json: 2def871f6f0fa99478ee438ee3edf8ce015c0c402b3665b81dda7f6a8a7bc201
        B/table-images/TABLE-1-page-8-1.png: fa00c611c537454833dee6fa3f828b80facde3a3e55a17a9cbbe69cbe655e041
        B/table-images/page-8.png: 36758993895380ed596874ff4b7b68f8036e795b14cd4e9eca8c4a1471e5c231
        B/table-images/manifest.json: 582f3b4a260606920b08bdb98376fc3571e91cc7f156549a174456faa865e607
        B/clauses/window-03/raw.json: 8428811e6ea1e67fdeef4863e7f561181a5d064b6be69cb89c466aad5e6917a7
        B/clauses/window-03/prompt.txt: f0ec483046eaa38b630b657322928fd8b13c191783732099f2808463317abc55
        B/clauses/window-03/meta.json: fc982c4cdad37288fd444438dc4a06554298f293b1730bc0077ba1329630fdcf
        B/clauses/window-04/raw.json: 9b782070c3a5ce3d4c98273bf8581d23e0925b0217388708811d7b5f927c8fd0
        B/clauses/window-04/prompt.txt: 8a5d22846b0f7e609f1a84c0ba3a78307c875b048fc4b2915bf0f1a5a79fb140
        B/clauses/window-04/meta.json: 382431b544ff30ac9946996e434d8bc665b565a6297b43e67ecc8e3cfdc35887
        B/clauses/window-05/raw.json: f0d4b0c01e5787f952411ad90bada7d6e49108b2592a50dd34ffd8b199474ac6
        B/clauses/window-05/prompt.txt: 5810716fda7e07b63aac838e39f998d1a37f55d5135fa6d833dbad7d9dfb5d7c
        B/clauses/window-05/meta.json: 8203973108185f6b3f29d9e1bd13e06dacd4ebdffa8a1a4aec1a176b56a523a3
        B/clauses/window-02/raw.json: 117c535189e2b3ea68432a4821597602f72c428772090cb2f27404de16f5cac3
        B/clauses/window-02/prompt.txt: d867d755c3836ec1fde2055fa611f2833e7cbee9baa8efe6bfa7a74f826a84a0
        B/clauses/window-02/meta.json: eb9046738b2536774b0424f608fac41f61bad411b9c387ee26b5c7f0bc77c2c7
        B/clauses/window-09/raw.json: c44df1a26f4ea51b3056ebf2f776ca9902bfcded4facf7996510c6ce51bda833
        B/clauses/window-09/prompt.txt: cb03e05b6c73d38906134809a4a4ff718e5cd21fff2bfaf5882dd3658dcd7272
        B/clauses/window-09/meta.json: 6e4468c333305cb7ec9131383df507dc0dcf86f5c4bddf861ce1b160b0881df2
        B/clauses/window-07/raw.json: 802c3b5913d101bdaf920ab2daf1c417747ead27b63d42623cccada664ae45c8
        B/clauses/window-07/prompt.txt: a1d1beb0928b4e5f0b6fb877a4c0221fdbc36fe6f75aecf9e1e654a9fc87280b
        B/clauses/window-07/meta.json: f5235702783e38627380bf16c6793ffa3c036dfadf8a72699eb423d45874ca4f
        B/clauses/window-01/raw.json: 485a37f5973884b7234531a96f08119552ae5b68d3ed12d08f9846f4b2b91a41
        B/clauses/window-01/prompt.txt: 2dc7981b81d4b34877532de8d8b045f872c71be2d740671cc39767b4465aa3bb
        B/clauses/window-01/meta.json: f3212119fbc83fcf06a81b4dfbe72c6446f80b5ee1f3da8556b0091401b0ed44
        B/clauses/window-06/raw.json: d1ce3a0e65eb327f8ac3ed0c75a2e5464233106822327aedd5c7b866b4e3d5cc
        B/clauses/window-06/prompt.txt: 884e14aae16f061486fdbe045ecde9c88cfd87f4f3d5fb05113c6ca6a9fb1139
        B/clauses/window-06/meta.json: 3be8bc3fc9325688252392f2f47883e529cd935a62b2f3f548a28623812d5ea8
        B/clauses/window-08/raw.json: d2396ccc3ba51f4672b2bfa7405ad9d03ce18c26dd2821ad5942d1603948eaaf
        B/clauses/window-08/prompt.txt: e78e668d14a3543c8e1ffe63e03acbb4c4b9eb168178eade8735fdcb2124f812
        B/clauses/window-08/meta.json: 7943b96cee48ae19cf4095a06841c4e53d430c9941c79bdc421d4d1c7a04b627
        B/tables/TABLE-1-page-8-1/raw.json: 591d83b31bb2378099134c8e8d38bddbc56242d84fd6f9161dac7830ef1435c3
        B/tables/TABLE-1-page-8-1/prompt.txt: ff03b86d878ccd35ea16875451f8eb9dad22a4282a18101457c08cfcfbd547da
        B/tables/TABLE-1-page-8-1/meta.json: 21d980ae563cb4839e790e060b8ec6e3985297b0ac0c5fd0df5e56c70c0c553d
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
      pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
      source_review: _compare/relationships-2026-11-16/review-current/Leff2009
      source_status_sha256: 934f45000f22b22008f14293cc84906186bf25545cf50d6c764200830ad447aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: structural integrity of left posterior superior temporal gyrus and sulcus
    outcome:
      text: spoken sentence comprehension
    analysis_label: Partial Regression (from Analysis 2 cluster)
    relation: association
    evidence_ids:
    - P6-S1-C2
    qualifier_ids:
    - P6-S1-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
      source_review: _compare/relationships-2026-11-16/review-current/Leff2009
      source_status_sha256: 934f45000f22b22008f14293cc84906186bf25545cf50d6c764200830ad447aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C17
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P5-S2-C12
      - Result passage disposed without unit P5-S2-C13
      - Result passage disposed without unit P5-S2-C14
      - 'window 4: invalid/duplicate disposition P5-S3-C3'
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C9
      - Accounting without a linked unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C5
      - Unaccounted source passage P6-S1-C2
      - 'window 6: invalid/duplicate disposition P6-S1-C9'
      - Result passage disposed without unit P6-S2-C1
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P9-S1-C4
      - Accounting without a linked unit P9-S1-C5
      - Result passage disposed without unit P9-S1-C6
      - Unaccounted source passage P9-S1-C5
      - Result passage disposed without unit P9-S2-C7
      - Accounting without a linked unit P9-S2-C8
      - Unaccounted source passage P9-S2-C8
      unattached_null_or_qualifier_ids:
      - P9-S1-C5
      suppressed_nonrepresented_units: 3
      default_disposition_count_requires_completeness_check: 189
      unselected_timing_passages:
      - P3-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P2-S1-C7
        - P2-S1-C8
        - P2-S1-C9
        - P3-S2-C7
        - P3-S2-C8
        - P3-S2-C9
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C13
        - P4-S2-C15
        - P4-S2-C16
        - P4-S2-C17
        - P4-S2-C20
        - P4-S2-C21
        - P4-S2-C22
        - P4-S3-C3
        - P4-S3-C5
        - P4-S3-C6
        - P4-S3-C7
        - P5-S2-C9
        - P6-S1-C2
        - P8-S2-C2
        - P8-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P2-S2-C7
        - P4-S1-C1
        - P4-S1-C2
        - P4-S1-C10
        - P4-S1-C12
        - P4-S1-C14
        - P4-S1-C19
        - P4-S2-C3
        - P4-S2-C9
        - P4-S2-C14
        - P4-S2-C22
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S2-C7
        - P5-S2-C9
        - P6-S2-C5
        - P6-S2-C7
        - P6-S2-C8
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P3-S1-C13
      table_review_required:
      - TABLE-1-page-8-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P3-S3
        - P5-S2
        - P5-S3
        - P6-S1
        - P6-S2
        - P7-S2
        - P8-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
      source_review: _compare/relationships-2026-11-16/review-current/Leff2009
      source_status_sha256: 934f45000f22b22008f14293cc84906186bf25545cf50d6c764200830ad447aa
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Abstract statement of Analysis 2 result.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Abstract statement of the relationship between the region and spoken
        sentence comprehension.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion volume variability.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes subject inclusion criteria.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes test scores.
    - source_id: P4-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes test scores.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap map figure.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Results of Analysis 1.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Results of Analysis 1.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Results of Analysis 2.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Results of Analysis 2.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Results of Analysis 3.
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Results of Analysis 4.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      reason: Partial regression results for spoken sentences, single words, and written
        sentences.
    - source_id: P6-S1-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      reason: Restatement of partial regression results.
    - source_id: P6-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of Analysis 2.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of partial regression result.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Discussion of Analysis 1 results.
    - source_id: P6-S2-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies Analysis 1 results as potentially generic functions.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Figure 2.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes model variance.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes speech perception/production.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes caudate nucleus function.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Discussion of Analysis 2 result.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of the region.
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of Analysis 2.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological comment.
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of partial regression result.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of partial regression result.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Discussion of null result for written sentences.
    - source_id: P9-S1-C6
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion of anatomical dissociation.
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of Analysis 1.
    - source_id: P9-S2-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Conclusion restatement of Analysis 2.
    - source_id: P9-S2-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restatement of partial regression result.
    - source_id: P9-S2-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restatement of shared substrate.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P3-S2-C2
    - P3-S2-C10
    - P4-S1-C7
    - P4-S1-C17
    - P5-S2-C12
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S2-C1
    - P6-S2-C2
    - P6-S2-C9
    - P7-S1-C1
    - P7-S1-C4
    - P8-S1-C2
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C9
    - P9-S1-C4
    - P9-S1-C6
    - P9-S1-C7
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-8-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C8
      recruited_sample:
      - P3-S1-C8
      eligibility:
      - P2-S3-C11
      - P3-S1-C9
      - P3-S1-C10
      - P3-S2-C10
      - P3-S2-C11
      imaging_provenance:
      - P4-S3-C9
      - P5-S1-C4
      imaging_timing:
      - P4-S3-C8
      - P3-S2-C4
      outcome_timing:
      - P3-S2-C4
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S2-C11
      dependent_variable_statement:
      - P5-S2-C4
      - P5-S2-C6
      - P5-S2-C7
      - P5-S2-C9
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C11
      - P3-S2-C3
      - P3-S2-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P2-S1-C7
      - P2-S1-C8
      - P2-S1-C9
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C13
      - P4-S2-C15
      - P4-S2-C16
      - P4-S2-C17
      - P4-S2-C20
      - P4-S2-C21
      - P4-S2-C22
      - P4-S3-C3
      - P4-S3-C5
      - P4-S3-C6
      - P4-S3-C7
      - P5-S2-C9
      - P6-S1-C2
      - P8-S2-C2
      - P8-S2-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P2-S2-C7
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C10
      - P4-S1-C12
      - P4-S1-C14
      - P4-S1-C19
      - P4-S2-C3
      - P4-S2-C9
      - P4-S2-C14
      - P4-S2-C22
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P5-S2-C7
      - P5-S2-C9
      - P6-S2-C5
      - P6-S2-C7
      - P6-S2-C8
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
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
      pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
      review_sha256: f28921f4b0c7063f00337df363d113c68b0f72d34df933303d6b3fbef7719037
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
      - P6-S1-C2
      source_result: A significant positive correlation (r=0.22, P=0.002) was found
        between the structural integrity (grey matter density) of the left posterior
        superior temporal gyrus and sulcus cluster and spoken sentence comprehension
        scores. This association was not significant for single word comprehension
        or written sentence comprehension. The analysis used partial regression on
        the principal eigenvariate of the cluster identified in Analysis 2, controlling
        for auditory word repetition, auditory non-word repetition, verbal fluency,
        picture naming, and stroke volume.
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the partial regression described
            in P6-S1-C1 and P6-S1-C2, which uses the eigenvariate from the Analysis
            2 cluster to test associations with comprehension measures. The proposed
            core correctly identifies this as a partial regression analysis.
          source_ids:
          - P6-S1-C1
          - P6-S1-C2
          - P5-S3-C5
        direction:
          answer: fits
          reason: The source reports a significant positive correlation (r=0.22) for
            spoken sentence comprehension. The proposed core states a significant
            correlation, which is faithful. The direction is positive, implying higher
            structural integrity is associated with better comprehension.
          source_ids:
          - P6-S1-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as the structural integrity
            of the left posterior superior temporal gyrus and sulcus. The outcome
            is spoken sentence comprehension. The method is VBM/partial regression.
            The patient measurement is voxel_tissue (grey matter density), not template_lesion_overlap,
            as the statistical analysis used continuous grey matter values (P5-S1-C7,
            P5-S1-C8), while lesion overlap was only for illustration.
          source_ids:
          - P6-S1-C2
          - P5-S1-C7
          - P5-S1-C8
          - P5-S3-C5
        qualifications:
          answer: fits
          reason: The proposed core includes the necessary controls (auditory word/non-word
            repetition, verbal fluency, picture naming, stroke volume) as stated in
            P6-S1-C1 and P5-S2-C7. It also correctly notes the lack of significance
            for single word and written sentence comprehension, which is a key qualification
            of the specificity of the finding.
          source_ids:
          - P6-S1-C1
          - P6-S1-C2
          - P5-S2-C7
        missing_material_caveat:
          answer: fits
          reason: 'The core captures the main caveats: the specific controls used
            and the specificity of the result to spoken sentence comprehension. No
            material caveats regarding the interpretation of this specific association
            are omitted.'
          source_ids:
          - P6-S1-C2
          - P6-S1-C3
      optional_pending:
      - Exact coordinates of the peak voxel
      - Cluster size in voxels
      - Specific P-value threshold details beyond P<0.05
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact coordinates of the peak voxel
    - Cluster size in voxels
    - Specific P-value threshold details beyond P<0.05
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: structural integrity of left posterior superior temporal gyrus and sulcus
      outcome:
        text: spoken sentence comprehension
      analysis_label: Partial Regression (from Analysis 2 cluster)
      relation: association
      evidence_ids:
      - P6-S1-C2
      qualifier_ids:
      - P6-S1-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
        source_review: _compare/relationships-2026-11-16/review-current/Leff2009
        source_status_sha256: 934f45000f22b22008f14293cc84906186bf25545cf50d6c764200830ad447aa
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9f9bb4ba44cf99c7737e55c457b650093c5846849d7fffd8a8763a5f4f0ad291
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C11
          page: 3
          text_layer_sha256: 9f9bb4ba44cf99c7737e55c457b650093c5846849d7fffd8a8763a5f4f0ad291
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'One

          hundred and twenty-eight (61%) were male and 186 (89%) were

          right-handed, with a mean age of 59 years (SD = 14).'
        anchor_text: 'One

          hundred and twenty-eight (61%) were male and 186 (89%) were

          right-handed, with a mean age of 59 years (SD = 14).'
        excluded_fragments: []
        image_sha256: 6fe0f1ff443a94d43362a0e5a33c7b2e5adb3246614686304dfcd2325bdd2f54
        transcription: '. One

          hundred and twenty-eight (61%) were male and 186 (89%) were

          right-handed, with a mean age of 59 years (SD = 14)'
      P3-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 452cac9e92f45f34aa7b1f1d31739c3fafff9ff7347b17a6bd88c6315e3f3c83
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d1915e80ef3149532777078ac0dc19de1ad0868bb30451edbced096afe9a3598
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C4
          page: 3
          text_layer_sha256: d1915e80ef3149532777078ac0dc19de1ad0868bb30451edbced096afe9a3598
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The median time after stroke

          upon testing was 35 months (interquartile range = 12–74 months),

          with a skew towards relatively recent stroke (26% 4 12 months)

          The minimum time since stroke was 41 month to avoid testing

          patients in the acute and subacute phases.'
        anchor_text: 'The median time after stroke

          upon testing was 35 months (interquartile range = 12–74 months),

          with a skew towards relatively recent stroke (26% 4 12 months)

          The minimum time since stroke was 41 month to avoid testing

          patients in the acute and subacute phases.'
        excluded_fragments: []
        image_sha256: fb26f89ba16fea241e41be6cf197eab1015ef205b2474477c063dbff88ea443b
        transcription: '. The median time after stroke

          upon testing was 35 months (interquartile range=12–74 months),

          with a skew towards relatively recent stroke (26% ≤ 12 months)

          The minimum time since stroke was >1 month to avoid testing

          patients in the acute and subacute phases'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'The

    right panel of Fig. 4 illustrates the signiﬁcant correlation between

    the structural

    integrity

    of this

    region

    and spoken

    sentence

    comprehension

    score,

    r(199) = 0.22,

    P = 0.002

    (right

    panel

    Fig. 4), but not single word comprehension, r(199) = -0.03,

    P = 0.66 or written sentences, r(199) = 0.05, P = 0.45.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
