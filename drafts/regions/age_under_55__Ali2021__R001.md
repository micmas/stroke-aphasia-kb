---
id: age_under_55
name: age <55 years
kind: classical
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: overall_language_ability
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: overall_language_ability
  target_kind: prognosis
  claim: Within RCT datasets, the largest mean absolute change in overall-language-ability
    was seen in those aged <55 years.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: 136
    population: people with poststroke aphasia in randomized controlled trials
    phase: not_reported
    time_post_onset: from baseline (median 43.6 weeks poststroke) to first follow-up
      (median 10 weeks from baseline)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - participants were limited to those who had access to speech and language therapy
    during the study intervention period
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Age of the participant was categorized as less than
    55 years. analysis based on RCT datasets; outcome measured as mean absolute change
    in points. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P1-S2-C5, two-model agreement, human
    verification pending): RESULTS: Assessments at baseline (median=43.6 weeks poststroke;
    interquartile range [4–165.1]) and first-follow-up (median=10 weeks from baseline;
    interquartile range [3–26]) were available for n=943 on overall-language ability,
    n=1056 on auditory comprehension, n=791 on naming and n=974 on functional-communication
    Original text-layer quotation is preserved below. PDF image reading (P4-S1-C6,
    two-model agreement, human verification pending): . Data at baseline

    (median=43.6 weeks since stroke; IQR [4–165.1])

    and first follow-up (median=10 weeks since baseline;

    IQR [3–26]) were available for overall-language-ability

    (n=943; 24 datasets, represented by the Western Apha-

    sia Battery-AQ), auditory comprehension (n=1056; 29

    datasets, represented by the Aachen Aphasia Test [AAT]

    Token Test), naming (n=791, 27 datasets, by Boston

    Naming Test), and functional-communication (n=974,

    23 datasets, represented by the AAT Spontaneous-

    Speech Communication subscale, Figure 1) Original text-layer quotation is preserved
    below. Reconcile this new analysis with earlier drafts and source-review decisions
    for the paper; new candidate IDs do not carry earlier decisions forward.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:overall_language_ability
  citation: '@Ali2021'
  source_passages:
  - section: Original source P4-S2-C7
    page: 4
    quote: "Predictors of Language Recovery\nOverall-Language-Ability\nWithin the\
      \ RCT datasets, the largest mean absolute \nchange in overall-language-ability\
      \ (presented as West-\nern Aphasia Battery-AQ points) was seen in those aged\
      \ \n<55 years (+15.4 points CI [10–20.9] IPD=136, 11 \nRCTs)."
    supports: claim
  - section: Original source P1-S1-C11
    page: 1
    quote: "METHODS: Individual participant data meta-analysis of systematically sourced\
      \ aphasia datasets described overall-language \nability using the Western Aphasia\
      \ Battery Aphasia-Quotient; auditory comprehension by Aachen Aphasia Test (AAT)\
      \ Token \nTest; naming by Boston Naming Test and functional-communication by\
      \ AAT Spontaneous-Speech Communication subscale."
    supports: method
  - section: Original source P1-S2-C5
    page: 1
    quote: "RESULTS: Assessments at baseline (median=43.6 weeks poststroke; interquartile\
      \ range [4–165.1]) and first-follow-up \n(median=10 weeks from baseline; interquartile\
      \ range [3–26]) were available for n=943 on overall-language ability, \nn=1056\
      \ on auditory comprehension, n=791 on naming and n=974 on functional-communication."
    supports: sample
  - section: Original source P4-S1-C6
    page: 4
    quote: "Data at baseline \n(median=43.6 weeks since stroke; IQR [4–165.1]) \n\
      and first follow-up (median=10 weeks since baseline; \nIQR [3–26]) were available\
      \ for overall-language-ability \n(n=943; 24 datasets, represented by the Western\
      \ Apha-\nsia Battery-AQ), auditory comprehension (n=1056; 29 \ndatasets, represented\
      \ by the Aachen Aphasia Test [AAT] \nToken Test), naming (n=791, 27 datasets,\
      \ by Boston \nNaming Test), and functional-communication (n=974, \n23 datasets,\
      \ represented by the AAT Spontaneous-\nSpeech Communication subscale, Figure 1)."
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: "Data \nare therefore presented on those who had access to SLT \nduring\
      \ the study intervention period."
    supports: limitation
  - section: Original source P3-S1-C2
    page: 3
    quote: "DOI: 10.1161/STROKEAHA.120.031162\nCLINICAL AND POPULATION \nSCIENCES\n\
      Statistical Analysis\nA one-stage meta-analysis approach combined available\
      \ IPD \nfrom eligible datasets with analyses preserving the clustering of \n\
      participants within each study and were generated using SAS/\nSTAT software,\
      \ Version 9.4 of the SAS System for Windows."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Ali2021
  proposal_id: R001
  review_status_sha256: 3c48f7bfc5e59eb45eb807bf4f6f9a072a593ccf6a8c92079e18d9eb02705bd7
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
        A/passages.json: e2aedd1f6f8d7760bcb4e75fb745467ba944988043c714be35ff281faab62aa3
        A/raw.json: eac7a90a194d03bcfd0ef882babbbcb153bea62226a44cd54c667655e0598abe
        A/source-units.json: 7fd786971429746e5c7463d07eaa9a33006112dcb2add198c54cb51a4eceab0b
        A/full-source-units.json: 647a2f1605e85b055578d85b3c47824fbbea7eaad39c10029228f50834060f4a
        A/meta.json: e3737ea5abe15967404a263a4f3f28f7f069b045d3411bc849aa1f978d2075b8
        A/table-images/manifest.json: 958387f4ced803ad14156b407a280f70a0a71f9ab30f3cbceb860001b5f4d1c1
        A/clauses/window-03/raw.json: cd9abe972d3ce84a8d19e4fa86ab3235174a0613889db6bc1285f07087e44192
        A/clauses/window-03/prompt.txt: c2eceb91a2154f66406280757f80e14c63c77c76e86d665241fcd64ae4cc88e4
        A/clauses/window-03/meta.json: 7a77fec04e3a07dcb6a20da21bf4973c523fb2252b957aed3767c1d33cd4ae59
        A/clauses/window-04/raw.json: 0ae40fe2776ceba2fa8978f680033aeceea6e92b8202e511893ffc1c18841a0f
        A/clauses/window-04/prompt.txt: dad01644df4abfddb809140e96a7132e29907ff9ee184d1b1b5d994101af84cc
        A/clauses/window-04/meta.json: 048f53bc0111785a8857d1c0587f0be8035ee0a3ab13e618e4fdfd113e4ab925
        A/clauses/window-05/raw.json: 8fec8eba8902338ae2dc02bc0155f920e5b676b8ce2f6d094e4480518d07ef58
        A/clauses/window-05/prompt.txt: ae7e74cb71ba28d8ebf689e56df5b1765402e3df73482325fb18598ae000044b
        A/clauses/window-05/meta.json: e90818b2fc2bc3b5670d0b64069c4c34867e537577275cfafa111734c1fdaaf0
        A/clauses/window-02/raw.json: 589217bcf35c9ef19df6de6baefd71c2326e4444f5aa478bdd91c88af931995e
        A/clauses/window-02/prompt.txt: 8c61c60a22dc2acb49228d8502157cdb1d5f72ff0bb47ee033aa0f7d1750f851
        A/clauses/window-02/meta.json: 85109ca4ade77a0d2ba9e2e0fba4f75672d2135e967b539ed56e26b59bf93163
        A/clauses/window-07/raw.json: f7ec666f0f6533313569cd969777d43a2098bef97fcf17a8ae463d982a4057c1
        A/clauses/window-07/prompt.txt: ad81ec1f70c7481a0c615efebe80b65b399918c70f704e08d49929ee4c230754
        A/clauses/window-07/meta.json: 1cf4044a77949391120dd569d184b978624a32f59b09e4322742dea73a1e0407
        A/clauses/window-01/raw.json: 916ac02a8f051980bdf848ca71917de2a690e4264b7c84eaa2b35d6509133453
        A/clauses/window-01/prompt.txt: abcb6c9675a08b5b3af45a4963a5383788b9f40e6bcc7f2a71db3bd6f2948c7a
        A/clauses/window-01/meta.json: 55d1c5f118818f287609f7570332cd2f3d595664361cbfd6536dca0214ba0b2a
        A/clauses/window-06/raw.json: b436046953be570df4a5cdf414561af1bfb2ac1d8a4eeef5aa1f4a7041eb4828
        A/clauses/window-06/prompt.txt: 590a31e9cc026aa97acf51cf736e1d789fe1a98d088c84c14038c04798422a8e
        A/clauses/window-06/meta.json: 467e04f15a045be85b6bd014e9d3adf700cdc02e12a407a698cb99f4c3b09fc6
        B/passages.json: e2aedd1f6f8d7760bcb4e75fb745467ba944988043c714be35ff281faab62aa3
        B/raw.json: 471b8cfa714bdcfc8ba53070b21ea72868538f92e2f3ff69b64bc04f175c14e6
        B/source-units.json: 7fd786971429746e5c7463d07eaa9a33006112dcb2add198c54cb51a4eceab0b
        B/full-source-units.json: 647a2f1605e85b055578d85b3c47824fbbea7eaad39c10029228f50834060f4a
        B/meta.json: 7500e1307d5f44aca5ac4c5e17b6ac578113a822b55a398bfeae8d2a44dbf30f
        B/table-images/manifest.json: 958387f4ced803ad14156b407a280f70a0a71f9ab30f3cbceb860001b5f4d1c1
        B/clauses/window-03/raw.json: 4f9bdb5eef120cda6ab9e3545772710505ec54fe3884dae9c1babefff71910eb
        B/clauses/window-03/prompt.txt: c2eceb91a2154f66406280757f80e14c63c77c76e86d665241fcd64ae4cc88e4
        B/clauses/window-03/meta.json: 66525ae42d13d4400ecd2e01ec4037b5f3d46a01fd788294e7a50f686cc23dda
        B/clauses/window-04/raw.json: 5fc5ef9ee65ce54e20b44f3abfd42b919be1d0ca9d12b7d51067f437f1d65bba
        B/clauses/window-04/prompt.txt: dad01644df4abfddb809140e96a7132e29907ff9ee184d1b1b5d994101af84cc
        B/clauses/window-04/meta.json: 72c1c3c13f3aa3121b8b85a21d6619ae6363be44cbc02d8072d2a1bfcf505c02
        B/clauses/window-05/raw.json: cb05bbc61cc9e4012ee476e26ae06759993bcf3414bdbd583a7e4e69c30f2cd4
        B/clauses/window-05/prompt.txt: ae7e74cb71ba28d8ebf689e56df5b1765402e3df73482325fb18598ae000044b
        B/clauses/window-05/meta.json: c96a2f7399111d743cabca3adeb572bf75d53fcb63518f4b83be4a01b211eae8
        B/clauses/window-02/raw.json: d9b6cc77f787e9503c24dabd2202bedf0c4397d3ad7d666c4a694883d0515c4f
        B/clauses/window-02/prompt.txt: 8c61c60a22dc2acb49228d8502157cdb1d5f72ff0bb47ee033aa0f7d1750f851
        B/clauses/window-02/meta.json: ecd3fd2ba7e24d198a120116ebf06c07b73cf6f37a9bcb81588176e1e27e69a4
        B/clauses/window-07/raw.json: 44be998e9ba0d2bcaa691e5c0acfa879314c58ae42746680fc91c64ff215c4dd
        B/clauses/window-07/prompt.txt: ad81ec1f70c7481a0c615efebe80b65b399918c70f704e08d49929ee4c230754
        B/clauses/window-07/meta.json: 52be48fc1259e2cec6f31812322ce4c2cf3e62f0cb0c0b6a9c47ea3adeff79c1
        B/clauses/window-01/raw.json: c06dfb7da06d00e478d18d04aacda63b46a9d1e792837235e221517fe2d01183
        B/clauses/window-01/prompt.txt: abcb6c9675a08b5b3af45a4963a5383788b9f40e6bcc7f2a71db3bd6f2948c7a
        B/clauses/window-01/meta.json: d70ea733692bfb7b5d69f6266685244a28c9fb42aad5419997fe2bc17ebce723
        B/clauses/window-06/raw.json: f9dfa2dc8b2a6bb106764b3b28f70a83c8dbeb3fdb33b81716962ac9333933ef
        B/clauses/window-06/prompt.txt: 590a31e9cc026aa97acf51cf736e1d789fe1a98d088c84c14038c04798422a8e
        B/clauses/window-06/meta.json: f56c81c096ac08bae7ffb4641297537512cd702f34c3073a31d69c0f91616a83
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
      pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
      source_review: _compare/relationships-2026-11-16/review-current/Ali2021
      source_status_sha256: 8fc6ca658a72b20239e8003166457c0b00c12576da6db184efcc2ac7e420f295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: age <55 years
    outcome:
      text: overall-language-ability
    analysis_label: Predictors of Overall-Language-Ability (RCT)
    relation: association
    evidence_ids:
    - P4-S2-C7
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
      pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
      source_review: _compare/relationships-2026-11-16/review-current/Ali2021
      source_status_sha256: 8fc6ca658a72b20239e8003166457c0b00c12576da6db184efcc2ac7e420f295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S2-C9
      - Result passage disposed without unit P4-S1-C4
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C7
      - Result passage disposed without unit P4-S2-C8
      - 'window 5: invalid/duplicate disposition P4-S3-C1'
      - Result passage disposed without unit P4-S3-C1
      - Result passage disposed without unit P4-S3-C2
      - Result passage disposed without unit P4-S3-C5
      - Result passage disposed without unit P4-S3-C10
      - Accounting without a linked unit P4-S3-C6
      - Accounting without a linked unit P4-S3-C7
      - Accounting without a linked unit P4-S3-C8
      - Accounting without a linked unit P4-S3-C9
      - Accounting without a linked unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P4-S3-C8
      - Unaccounted source passage P4-S3-C6
      - Unaccounted source passage P5-S1-C2
      - Unaccounted source passage P4-S3-C9
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P4-S3-C7
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S2-C4
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P7-S1-C2
      - Accounting without a linked unit P7-S1-C4
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Unaccounted source passage P7-S1-C4
      - Unaccounted source passage P7-S1-C2
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C3
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C8
      unattached_null_or_qualifier_ids:
      - P4-S1-C8
      - P4-S2-C5
      - P7-S1-C2
      - P7-S1-C7
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 123
      unselected_timing_passages:
      - P2-S2-C8
      - P3-S1-C4
      - P3-S1-C6
      - P4-S1-C2
      - P4-S1-C10
      - P4-S2-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S2
        - P3-S3
        - P4-S1
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
      source_review: _compare/relationships-2026-11-16/review-current/Ali2021
      source_status_sha256: 8fc6ca658a72b20239e8003166457c0b00c12576da6db184efcc2ac7e420f295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 3
      - 4
      - 6
      - 7
      - 9
      reason: Abstract summary of specific results detailed in the results section.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 14
      reason: States the general relationship between age/chronicity and score improvement.
    - source_id: P1-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical heterogeneity.
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes risk of bias.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes screening counts.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes dataset inclusion counts.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes types of studies included.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant demographics.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data checks and validity.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sample sizes for language domains.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data extraction for other domains.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains why certain results are not presented.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data inadequacy for handedness.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data formats for SES and education.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains why certain covariates hindered adjustment.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes insufficient data for No SLT group.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes limited data for historical SLT group.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Provides absolute change for <55 years in overall-language-ability.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Provides absolute change for other age groups in overall-language-ability.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Provides absolute change for <1 month enrollment in overall-language-ability.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Provides absolute change for other chronicity windows in overall-language-ability.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Compares gains between women and men in overall-language-ability.
    - source_id: P4-S3-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Confidence interval for sex difference in overall-language-ability.
    - source_id: P4-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States consistency across study types.
    - source_id: P4-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Provides absolute change for <55 years in auditory comprehension.
    - source_id: P4-S3-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Provides absolute change for <1 month enrollment in auditory comprehension.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: States consistency across study types.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Provides absolute change for <55 years in naming.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Provides absolute change for other age groups in naming.
    - source_id: P4-S3-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Provides absolute change for <1 month enrollment in naming.
    - source_id: P4-S3-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Provides absolute change for other chronicity windows in naming.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: States consistency across study types.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Provides absolute change for <55 years in functional communication.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Provides absolute change for other age groups in functional communication.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Provides absolute change for <1 month enrollment in functional communication.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Provides absolute change for other chronicity windows in functional
        communication.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Compares gains between women and men in functional communication.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: States consistency across study types.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports absolute and relative proportions of change across domains.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Reports proportions of change for <1 month enrollment.
    - source_id: P5-S2-C1
      disposition: repeated
      result_indexes:
      - 12
      reason: Relative proportion of change for <1 month enrollment.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sample sizes for all study designs.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Reports absolute and relative proportions of change for all study designs.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical heterogeneity.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline comparability of groups.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes risk of bias (blinding).
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes attrition and selection bias.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes level of evidence and publication bias.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missingness analysis.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data transformation and synthesis methods.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes validation of RCT observations in all study types.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses operational definition of recovery and timing of therapy.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: States inability to account for spontaneous recovery.
    unresolved_coverage:
    - source_id: P5-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C6
    - P1-S2-C8
    - P1-S2-C9
    - P3-S2-C9
    - P3-S2-C10
    - P3-S2-C11
    - P4-S1-C2
    - P4-S1-C4
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C8
    - P4-S1-C9
    - P4-S1-C10
    - P4-S2-C2
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C8
    - P4-S2-C10
    - P4-S3-C1
    - P4-S3-C2
    - P4-S3-C5
    - P4-S3-C7
    - P4-S3-C9
    - P4-S3-C10
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C7
    - P5-S2-C1
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C9
    - P5-S3-C2
    - P5-S3-C3
    - P5-S3-C5
    - P5-S3-C6
    - P6-S1-C3
    - P7-S1-C2
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C8
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
      analysed_sample:
      - P3-S2-C10
      - P4-S1-C6
      - P5-S2-C2
      recruited_sample:
      - P2-S2-C8
      eligibility:
      - P2-S2-C8
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S2-C5
      - P4-S1-C6
      - P7-S2-C4
      outcome_definition:
      - P2-S3-C8
      - P2-S3-C9
      - P3-S2-C5
      - P5-S1-C8
      - P7-S1-C7
      validation:
      - P7-S1-C4
      analysis_restrictions:
      - P4-S1-C8
      - P4-S2-C4
      - P4-S2-C5
      - P7-S2-C3
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S3-C8
      - P3-S1-C8
      limitations:
      - P7-S2-C2
      - P7-S2-C3
      - P7-S2-C4
      personal_factors:
      - P2-S2-C9
      - P3-S1-C8
      - P4-S1-C10
      - P4-S2-C3
      - P7-S2-C2
      tested_personal_effects:
      - P1-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C11
      - P5-S1-C2
      - P5-S1-C4
      - P5-S1-C6
      adjustment_roles:
      - P3-S1-C8
      - P3-S1-C10
      explicitly_not_adjusted:
      - P4-S2-C3
      descriptive_personal_factors:
      - P2-S2-C9
      - P4-S1-C2
      - P4-S1-C10
    outcome_type: change_from_baseline
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections: []
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
      pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
      review_sha256: 3c48f7bfc5e59eb45eb807bf4f6f9a072a593ccf6a8c92079e18d9eb02705bd7
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
      - P4-S2-C7
      source_result: Within RCT datasets, the largest mean absolute change in overall-language-ability
        (measured by Western Aphasia Battery-AQ) was observed in participants aged
        <55 years (+15.4 points, 95% CI [10–20.9], IPD=136, 11 RCTs).
      result_status: ranking_with_tie
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the RCT-specific subgroup analysis
            of overall-language-ability predictors, specifically the age <55 years
            group, as described in P4-S2-C7. The proposed core correctly identifies
            this as a ranking within the RCT population.
          source_ids:
          - P4-S2-C7
          - P2-S3-C6
        direction:
          answer: fits
          reason: The source states that the 'largest mean absolute change' was seen
            in the <55 years group. The proposed core uses 'likely' direction, which
            is a conservative representation of a ranking result where the group had
            the highest observed effect size, though it does not explicitly claim
            statistical superiority over other groups in the text provided (though
            implied by 'largest'). The direction of association (younger age associated
            with greater recovery) is preserved.
          source_ids:
          - P4-S2-C7
        construct:
          answer: fits
          reason: Exposure is age <55 years. Outcome is overall-language-ability.
            Measurement is Western Aphasia Battery-AQ (non-imaging clinical assessment).
            The proposed core correctly identifies these elements. The patient measurement
            is non_imaging as it relies on standardized language test scores, not
            neuroimaging data.
          source_ids:
          - P4-S2-C7
          - P1-S1-C11
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis is
            based on RCT datasets and notes the limitation regarding SLT access. It
            correctly restricts the claim to the RCT population as per the source
            text 'Within the RCT datasets'.
          source_ids:
          - P4-S2-C7
          - P4-S2-C6
        missing_material_caveat:
          answer: fits
          reason: The core captures the primary caveat that this is an RCT-specific
            finding. While the source notes that observations were consistent in all
            study types (P4-S3-C2), the selected analysis is specifically the RCT
            one. The limitation regarding SLT access (P4-S2-C6) is included. No material
            caveats that change the interpretation of the RCT ranking are omitted.
          source_ids:
          - P4-S2-C7
          - P4-S2-C6
      optional_pending:
      - Specific confidence interval values for the <55 group are not transcribed
        in the core fields but are present in source P4-S2-C7
      - Comparison with other age groups (56-65, 66-75, >75) is not detailed in the
        core claim but is part of the ranking context in P4-S2-C8
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific confidence interval values for the <55 group are not transcribed in
      the core fields but are present in source P4-S2-C7
    - Comparison with other age groups (56-65, 66-75, >75) is not detailed in the
      core claim but is part of the ranking context in P4-S2-C8
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R001
      exposure:
        text: age <55 years
      outcome:
        text: overall-language-ability
      analysis_label: Predictors of Overall-Language-Ability (RCT)
      relation: association
      evidence_ids:
      - P4-S2-C7
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
        pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
        source_review: _compare/relationships-2026-11-16/review-current/Ali2021
        source_status_sha256: 8fc6ca658a72b20239e8003166457c0b00c12576da6db184efcc2ac7e420f295
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6d34bdec3d86d5d81978b87434aca3aaece6db58037438ec91b85e5c951e73a0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C5
          page: 1
          text_layer_sha256: 6d34bdec3d86d5d81978b87434aca3aaece6db58037438ec91b85e5c951e73a0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "RESULTS: Assessments at baseline (median=43.6 weeks poststroke;\
          \ interquartile range [4–165.1]) and first-follow-up \n(median=10 weeks\
          \ from baseline; interquartile range [3–26]) were available for n=943 on\
          \ overall-language ability, \nn=1056 on auditory comprehension, n=791 on\
          \ naming and n=974 on functional-communication."
        anchor_text: "RESULTS: Assessments at baseline (median=43.6 weeks poststroke;\
          \ interquartile range [4–165.1]) and first-follow-up \n(median=10 weeks\
          \ from baseline; interquartile range [3–26]) were available for n=943 on\
          \ overall-language ability, \nn=1056 on auditory comprehension, n=791 on\
          \ naming and n=974 on functional-communication."
        excluded_fragments: []
        image_sha256: f118c96e0b17e51862994b620cd679ddd55fd8fde6038ef85db25c768e5a7c61
        transcription: 'RESULTS: Assessments at baseline (median=43.6 weeks poststroke;
          interquartile range [4–165.1]) and first-follow-up (median=10 weeks from
          baseline; interquartile range [3–26]) were available for n=943 on overall-language
          ability, n=1056 on auditory comprehension, n=791 on naming and n=974 on
          functional-communication'
      P4-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: afa6ff72b9e07a4a4ddbf41e871bd6ddd37eb738495e654ce6c93b830ae3e7b9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C6
          page: 4
          text_layer_sha256: afa6ff72b9e07a4a4ddbf41e871bd6ddd37eb738495e654ce6c93b830ae3e7b9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Data at baseline \n(median=43.6 weeks since stroke; IQR [4–165.1])\
          \ \nand first follow-up (median=10 weeks since baseline; \nIQR [3–26]) were\
          \ available for overall-language-ability \n(n=943; 24 datasets, represented\
          \ by the Western Apha-\nsia Battery-AQ), auditory comprehension (n=1056;\
          \ 29 \ndatasets, represented by the Aachen Aphasia Test [AAT] \nToken Test),\
          \ naming (n=791, 27 datasets, by Boston \nNaming Test), and functional-communication\
          \ (n=974, \n23 datasets, represented by the AAT Spontaneous-\nSpeech Communication\
          \ subscale, Figure 1)."
        anchor_text: "Data at baseline \n(median=43.6 weeks since stroke; IQR [4–165.1])\
          \ \nand first follow-up (median=10 weeks since baseline; \nIQR [3–26]) were\
          \ available for overall-language-ability \n(n=943; 24 datasets, represented\
          \ by the Western Apha-\nsia Battery-AQ), auditory comprehension (n=1056;\
          \ 29 \ndatasets, represented by the Aachen Aphasia Test [AAT] \nToken Test),\
          \ naming (n=791, 27 datasets, by Boston \nNaming Test), and functional-communication\
          \ (n=974, \n23 datasets, represented by the AAT Spontaneous-\nSpeech Communication\
          \ subscale, Figure 1)."
        excluded_fragments: []
        image_sha256: 4cdc8f7ae229b4364530ea97b624201907dd02026997c490560d0ad74f283b89
        transcription: '. Data at baseline

          (median=43.6 weeks since stroke; IQR [4–165.1])

          and first follow-up (median=10 weeks since baseline;

          IQR [3–26]) were available for overall-language-ability

          (n=943; 24 datasets, represented by the Western Apha-

          sia Battery-AQ), auditory comprehension (n=1056; 29

          datasets, represented by the Aachen Aphasia Test [AAT]

          Token Test), naming (n=791, 27 datasets, by Boston

          Naming Test), and functional-communication (n=974,

          23 datasets, represented by the AAT Spontaneous-

          Speech Communication subscale, Figure 1)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "Predictors of Language Recovery\nOverall-Language-Ability\nWithin the RCT\
    \ datasets, the largest mean absolute \nchange in overall-language-ability (presented\
    \ as West-\nern Aphasia Battery-AQ points) was seen in those aged \n<55 years\
    \ (+15.4 points CI [10–20.9] IPD=136, 11 \nRCTs)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
