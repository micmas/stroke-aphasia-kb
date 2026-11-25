---
id: semantic_fluency_sccan_cluster
name: semantic fluency cluster
kind: network
findings:
- id: f1
  target: semantic_fluency
  target_kind: impairment
  claim: A broad network of cortical and white matter regions, including frontal and
    posterior temporal areas, is associated with semantic fluency deficits.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 55
    population: participants with aphasia secondary to a single left hemisphere stroke
    phase: not_reported
    time_post_onset: mean 39.80 months since stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - results are based on a single-center prospective collection of MRI and psycholinguistic
    data
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a distributed network
    of cortical and white matter regions identified via sparse canonical correlation
    analysis (SCCAN), including the inferior parietal lobule, superior and middle
    temporal gyri, temporal pole, inferior frontal gyrus, middle and superior frontal
    gyri, anterior corona radiata, external capsule, anterior limb of the internal
    capsule, superior longitudinal fasciculus, and posterior thalamic radiation. analysis
    controlled for total direct lesion volume; voxels were excluded if fewer than
    10% of participants had lesions in that voxel. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S2-C4, two-model agreement, human verification pending): Methods

    Participants

    Prospectively collected MRI and psycholinguistic data from 55 participants with
    aphasia secondary to a single left hemisphere stroke were analysed Original text-layer
    quotation is preserved below. PDF image reading (P3-S2-C4, two-model agreement,
    human verification pending): Participant demographic information


    Mean (SD) Range

    Age (years) 52.82 (15.66) 22.65–90.76

    Time since stroke (months) 39.80 (37.88) 2.24–167.93

    Lesion volume (cc) 113 (69) 2–251

    SFT 18.07 (15.63) 0–62

    COWAT 8.15 (8.38) 0–36

    BNT 33.18 (20.13) 0–60


    Number of participants

    Gender (M:F) 32:23

    Handedness (R:L:A) 49:4:2


    Note Original text-layer quotation is preserved below.'
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
    - proposed_concept:semantic_fluency
  citation: '@Thye2021'
  source_passages:
  - section: Original source P5-S1-C3
    page: 5
    quote: 'In addition, SCCAN

      identiﬁed a broad network of cortical regions extending from the inferior parietal
      lobule

      into superior and middle temporal gyri and temporal pole and in frontal regions
      including

      inferior frontal and middle and superior frontal gyri (optimized sparseness
      = 0.83, CV

      correlation = .52, p < .001).'
    supports: claim
  - section: Original source P5-S1-C2
    page: 5
    quote: 'The SCCAN results included these white matter tracts, as well as portions
      of the

      superior longitudinal fasciculus and posterior thalamic radiation.'
    supports: claim
  - section: Original source P2-S2-C4
    page: 2
    quote: 'Methods

      Participants

      Prospectively collected MRI and psycholinguistic data from 55 participants with
      aphasia

      secondary to a single left hemisphere stroke were analysed.'
    supports: sample
  - section: Original source P3-S2-C4
    page: 3
    quote: 'Participant demographic information

      Mean (SD)

      Range

      Age (years)

      52.82 (15.66)

      22.65–90.76

      Time since stroke (months)

      39.80 (37.88)

      2.24–167.93

      Lesion volume (cc)

      113 (69)

      2–251

      SFT

      18.07 (15.63)

      0–62

      COWAT

      8.15 (8.38)

      0–36

      BNT

      33.18 (20.13)

      0–60

      Number of participants

      Gender (M:F)

      32:23

      Handedness (R:L:A)

      49:4:2

      Note.'
    supports: sample
  - section: Original source P3-S1-C11
    page: 3
    quote: 'All of the LSM analyses controlled for lesion size

      using total direct lesion volume control (Mirman et al., 2015).'
    supports: method
  - section: Original source P3-S1-C12
    page: 3
    quote: "Each LSM analysis excluded\nvoxels where at least 10% (N \x01 6) of participants\
      \ did not have lesions."
    supports: method
  - section: Original source P2-S2-C2
    page: 2
    quote: 'These include adoptinga reproducible lesion segmentation method,controlling

      for overall lesion volume, appropriately correcting for multiple comparisons,
      limiting

      analysis to regions with sufﬁcient lesion involvement and running both mass-univariate

      LSM and a multivariate alternative: sparse canonical correlation analysis (SCCAN),
      to

      better capture the distributed ﬂuency network (Pustina, Avants, Faseyitan, Medaglia,
      &

      Coslett, 2018).'
    supports: method
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Fluency was assessed with the Semantic Fluency Test

      and the Controlled Oral Word Association Test.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Thye2021
  proposal_id: R003
  review_status_sha256: 97f8d7b4ff76b2108201f5ff99b1ec8e6d2ff09297ae8f28f6cb866255ca5b7c
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
        A/passages.json: 0a34a2622f143c7f2b0fc8c85d373f7620a9eadb8cfdeb47c1c42d6430bd38f3
        A/raw.json: bc17f8ba0f168abf9af53ea4b7c175996d29ba924f526b4be926c0ad1992621b
        A/source-units.json: dcccfcaa8830694e3251721120e00cc784823720af73b9dca2beb366638a49d7
        A/full-source-units.json: 6e9cdae15fba834a5ef15ea3302367d6bd64cd66d979e477903883dd5e716093
        A/meta.json: da1b74d542a6ef71fb218be001af84c2362912dad43dcb324b3a601ef44b5fec
        A/table-images/TABLE-1-page-3-1.png: 377af781c2cc606d59096ab0e21ba737296691610041f4a766432b1fa5355f84
        A/table-images/page-3.png: 290db76e30b9e2dc5a346ce87e1786225fd94327cb4762aa140d5dffbb58aab8
        A/table-images/manifest.json: 27a6be247db425a0a55ff72b6b0720fc91d69a2276352d25eaf455257bb9acd8
        A/clauses/window-03/raw.json: 8b9013d1640dd6155e887af7784697039e988aec82feabb74c47ec38dff297f6
        A/clauses/window-03/prompt.txt: 5c539d6cb1a11d607e42592f7f98e45aea9a83c23980798d0c91f3f69187166c
        A/clauses/window-03/meta.json: 6b5352de1b7e32027bfd88010a4ce5f0239dac6e60a723181b462c783910489f
        A/clauses/window-04/raw.json: 61af00151acbe3deabd3385ee87147324061b03fc7466a0714146c78cec8ccb6
        A/clauses/window-04/prompt.txt: d5cc55a76985de1be0bc3db1fdd7362c69a03950c95b3c71e7e21c85bc78f691
        A/clauses/window-04/meta.json: f046736d04cee2b069b62914fe8417a010d1330a3c52bbd3bd2e97b969104988
        A/clauses/window-02/raw.json: dc196c1d527283d094e71c958a3f99d493b95a9f8b33fd5d5de03a4afcf2e7b8
        A/clauses/window-02/prompt.txt: 4ea3dea32194b4fcf68f3165c7f6f8db0f5045cf856c7192257f92c785ee7557
        A/clauses/window-02/meta.json: af94b459551e0af2f5a12f028271beb9408a5e50585415a59dd0232ed3c400e3
        A/clauses/window-01/raw.json: 43991bbf023f06471e55bca9dd62c277daa5325db548e96b3c3fc40837d7968d
        A/clauses/window-01/prompt.txt: 5f1335c402465c0c423f7d62f0e9b0ed0b8183583931d94ce5195ed8d1225cb4
        A/clauses/window-01/meta.json: b0e809e187fc768d99cbb582cf88e0bd8e2f36821323d64cf948c61c2b5406c3
        A/tables/TABLE-1-page-3-1/raw.json: 6116f88c9cd38b84f019509180986a9636f0a2b25c7a90dc5a4f6ea216b73d4a
        A/tables/TABLE-1-page-3-1/prompt.txt: 3653a1499c8ef9a5fcef58dc8841bd6b73360bd8a3a5b77859935094ee2289d2
        A/tables/TABLE-1-page-3-1/meta.json: e02b64f22d82f47bdabcd064e33b3da1a6b4985222cbe9af0ab77abb6bdec21c
        B/passages.json: 0a34a2622f143c7f2b0fc8c85d373f7620a9eadb8cfdeb47c1c42d6430bd38f3
        B/raw.json: 052b56987b5c233fc42b5c05e213fa9c677870c06706c5d9ece13cdebc23a101
        B/source-units.json: dcccfcaa8830694e3251721120e00cc784823720af73b9dca2beb366638a49d7
        B/full-source-units.json: 6e9cdae15fba834a5ef15ea3302367d6bd64cd66d979e477903883dd5e716093
        B/meta.json: 115fd16f16a89de69d14bab450e8e29cdc608e6851a948249644ebe3756ee0a6
        B/table-images/TABLE-1-page-3-1.png: 377af781c2cc606d59096ab0e21ba737296691610041f4a766432b1fa5355f84
        B/table-images/page-3.png: 290db76e30b9e2dc5a346ce87e1786225fd94327cb4762aa140d5dffbb58aab8
        B/table-images/manifest.json: 6c63d677dcbf579b36d713b1f484e897a4d89f0892d3c6a5a49d8ca040c12af5
        B/clauses/window-03/raw.json: 31fef936d3e6e06b521babfb8af2a0aa89880a9d8ca3fc59294448fcc3342168
        B/clauses/window-03/prompt.txt: 5c539d6cb1a11d607e42592f7f98e45aea9a83c23980798d0c91f3f69187166c
        B/clauses/window-03/meta.json: 693e6c00e54e079897538dd599ed1487111aff94911ed321a1d074aaf2965c2d
        B/clauses/window-04/raw.json: 61af00151acbe3deabd3385ee87147324061b03fc7466a0714146c78cec8ccb6
        B/clauses/window-04/prompt.txt: d5cc55a76985de1be0bc3db1fdd7362c69a03950c95b3c71e7e21c85bc78f691
        B/clauses/window-04/meta.json: f065d9d785bb1a774309fd0e0e341d4198d195e69c8f386355b23fb219d27654
        B/clauses/window-02/raw.json: 15ca739411a4f0f8fcaf9f37a564a6f9e8c95044c59ad42c7dbcf24e487ee86c
        B/clauses/window-02/prompt.txt: 4ea3dea32194b4fcf68f3165c7f6f8db0f5045cf856c7192257f92c785ee7557
        B/clauses/window-02/meta.json: 854bae5451b9bb5749e875e6a313c4053da3910f5becc980176b43962d842175
        B/clauses/window-01/raw.json: 4bcbc7b5160b8b7e2af3de75fab57f454dc1b9339829d119d219dd6200968e76
        B/clauses/window-01/prompt.txt: 5f1335c402465c0c423f7d62f0e9b0ed0b8183583931d94ce5195ed8d1225cb4
        B/clauses/window-01/meta.json: ba8d583df3c368e656f71f1c61f7db6d757a6202bec3322cba6ed2d74848b521
        B/tables/TABLE-1-page-3-1/raw.json: 27d0daa3fdf8e2a9d17410884eb1424d14806916039f56912b391ccbc2533080
        B/tables/TABLE-1-page-3-1/prompt.txt: 3653a1499c8ef9a5fcef58dc8841bd6b73360bd8a3a5b77859935094ee2289d2
        B/tables/TABLE-1-page-3-1/meta.json: d0222c22a09777b4cf91974fa829dfbd2dcd552877277077e66c3db31f48d2a5
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
      pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
      source_review: _compare/relationships-2026-11-16/review-current/Thye2021
      source_status_sha256: fbf4915a08ef6fce6eceff350b4cefb17079869d28d7c4234f53c53d40f0df0e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: lesion in distributed network
    outcome:
      text: semantic fluency
    analysis_label: SCCAN
    relation: performance
    evidence_ids:
    - P5-S1-C3
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
      pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
      source_review: _compare/relationships-2026-11-16/review-current/Thye2021
      source_status_sha256: fbf4915a08ef6fce6eceff350b4cefb17079869d28d7c4234f53c53d40f0df0e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P3-S1-C14
      - Result passage disposed without unit P3-S2-C2
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S2-C7
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 67
      unselected_timing_passages:
      - P3-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P4-S1
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
      source_review: _compare/relationships-2026-11-16/review-current/Thye2021
      source_status_sha256: fbf4915a08ef6fce6eceff350b4cefb17079869d28d7c4234f53c53d40f0df0e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: repeated
      result_indexes: []
      reason: Abstract restatement of findings
    - source_id: P3-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the results section
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 3
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Directly reports VLSM results for semantic fluency
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Directly reports SCCAN white matter results for semantic fluency
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports SCCAN cortical network and performance metrics for semantic
        fluency
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Directly reports VLSM results for letter fluency
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports SCCAN results for letter fluency
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports SCCAN posterior cluster and performance metrics for letter fluency
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null result for residuals analysis
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null result for SVR-LSM
    - source_id: P6-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of shared network
    - source_id: P6-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Discussion restatement of VLSM white matter findings
    - source_id: P6-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      - 4
      reason: Discussion restatement of SCCAN distributed network
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 4
      reason: Discussion restatement of frontal/temporal involvement
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      - 4
      reason: Discussion detailing differences in SCCAN networks
    - source_id: P6-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      - 4
      reason: Discussion detailing differences in SCCAN networks
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Behavioral correlation is a descriptive finding, not a lesion-symptom
        relationship
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of correlation strength to other studies
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological discussion on focal results
    - source_id: P6-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 3
      - 4
      reason: Discussion restating overlap between VLSM and SCCAN
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on multivariate LSM effectiveness
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Conclusion summarizing the shared network findings
    unresolved_coverage:
    - source_id: P1-S1-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    pending_source_ids:
    - P1-S1-C5
    - P3-S1-C14
    - P3-S2-C2
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C10
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C4
      recruited_sample:
      - P2-S2-C4
      eligibility:
      - P2-S2-C4
      imaging_provenance:
      - P2-S2-C4
      imaging_timing:
      - P2-S2-C4
      outcome_timing:
      - P2-S2-C4
      outcome_definition:
      - P2-S2-C6
      - P2-S2-C7
      - P3-S1-C5
      validation:
      - P3-S1-C10
      analysis_restrictions:
      - P3-S1-C12
      dependent_variable_statement:
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C7
      limitations:
      - P6-S2-C5
      - P6-S2-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C6
      - P3-S1-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
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
      pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
      review_sha256: 97f8d7b4ff76b2108201f5ff99b1ec8e6d2ff09297ae8f28f6cb866255ca5b7c
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
      - P5-S1-C3
      source_result: SCCAN identified a broad network of cortical and white matter
        regions (including inferior parietal lobule, superior/middle temporal gyri,
        temporal pole, and frontal regions) associated with semantic fluency deficits,
        with a CV correlation of .52 and p < .001.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is SCCAN for semantic fluency, matching the
            source description in P5-S1-C3 and P2-S2-C2.
          source_ids:
          - P5-S1-C3
          - P2-S2-C2
        direction:
          answer: fits
          reason: The source reports a significant association (p < .001) between
            the identified network and semantic fluency deficits, consistent with
            the draft's claim of association.
          source_ids:
          - P5-S1-C3
        construct:
          answer: fits
          reason: The exposure is lesion overlap with the identified network (template_lesion_overlap
            via SCCAN), and the outcome is semantic fluency performance (Semantic
            Fluency Test), matching the source.
          source_ids:
          - P5-S1-C3
          - P2-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the control for lesion volume and the voxel exclusion
            threshold (10%), which are stated in P3-S1-C11 and P3-S1-C12.
          source_ids:
          - P3-S1-C11
          - P3-S1-C12
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing; the draft correctly reflects the
            single-center nature and the specific analysis type.
          source_ids:
          - P2-S2-C4
      optional_pending:
      - Specific coordinates of the identified clusters
      - Exact sparseness parameter value (0.83) and CV correlation (.52) details
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates of the identified clusters
    - Exact sparseness parameter value (0.83) and CV correlation (.52) details
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: lesion in distributed network
      outcome:
        text: semantic fluency
      analysis_label: SCCAN
      relation: performance
      evidence_ids:
      - P5-S1-C3
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
        pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
        source_review: _compare/relationships-2026-11-16/review-current/Thye2021
        source_status_sha256: fbf4915a08ef6fce6eceff350b4cefb17079869d28d7c4234f53c53d40f0df0e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9c8b02ae37f78cabf65b71d39b7c5c0d489f685c0a76855e76d0288c6d31390f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: 9c8b02ae37f78cabf65b71d39b7c5c0d489f685c0a76855e76d0288c6d31390f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Participants

          Prospectively collected MRI and psycholinguistic data from 55 participants
          with aphasia

          secondary to a single left hemisphere stroke were analysed.'
        anchor_text: 'Methods

          Participants

          Prospectively collected MRI and psycholinguistic data from 55 participants
          with aphasia

          secondary to a single left hemisphere stroke were analysed.'
        excluded_fragments: []
        image_sha256: 2ca80303ad2b07bdcd354d4147e0c73869aedc264abf495749fb17cc77ae229b
        transcription: 'Methods

          Participants

          Prospectively collected MRI and psycholinguistic data from 55 participants
          with aphasia secondary to a single left hemisphere stroke were analysed'
      P3-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 41fb5514f9838a1dbe9e3137bf55e3319f8ebadf0cdde7600e0e94251ff974bc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C4
          page: 3
          text_layer_sha256: 41fb5514f9838a1dbe9e3137bf55e3319f8ebadf0cdde7600e0e94251ff974bc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participant demographic information

          Mean (SD)

          Range

          Age (years)

          52.82 (15.66)

          22.65–90.76

          Time since stroke (months)

          39.80 (37.88)

          2.24–167.93

          Lesion volume (cc)

          113 (69)

          2–251

          SFT

          18.07 (15.63)

          0–62

          COWAT

          8.15 (8.38)

          0–36

          BNT

          33.18 (20.13)

          0–60

          Number of participants

          Gender (M:F)

          32:23

          Handedness (R:L:A)

          49:4:2

          Note.'
        anchor_text: 'Participant demographic information

          Mean (SD)

          Range

          Age (years)

          52.82 (15.66)

          22.65–90.76

          Time since stroke (months)

          39.80 (37.88)

          2.24–167.93

          Lesion volume (cc)

          113 (69)

          2–251

          SFT

          18.07 (15.63)

          0–62

          COWAT

          8.15 (8.38)

          0–36

          BNT

          33.18 (20.13)

          0–60

          Number of participants

          Gender (M:F)

          32:23

          Handedness (R:L:A)

          49:4:2

          Note.'
        excluded_fragments: []
        image_sha256: 12bbbb4e64586241d4bb87a89ef8b9cabd5a5191d0a9be543b31332c62149327
        transcription: 'Participant demographic information


          Mean (SD) Range

          Age (years) 52.82 (15.66) 22.65–90.76

          Time since stroke (months) 39.80 (37.88) 2.24–167.93

          Lesion volume (cc) 113 (69) 2–251

          SFT 18.07 (15.63) 0–62

          COWAT 8.15 (8.38) 0–36

          BNT 33.18 (20.13) 0–60


          Number of participants

          Gender (M:F) 32:23

          Handedness (R:L:A) 49:4:2


          Note'
      P3-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ad68c8b2ad667f4743d4ee38abf3d4398ed15769af423e150ab1d1a9d6761109
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: eb0b5aff6d8ba103908106d56d6f85a954939759124f0e044c534f797d5b8e1f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C12
          page: 3
          text_layer_sha256: eb0b5aff6d8ba103908106d56d6f85a954939759124f0e044c534f797d5b8e1f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Each LSM analysis excluded\nvoxels where at least 10% (N \x01\
          \ 6) of participants did not have lesions."
        anchor_text: "Each LSM analysis excluded\nvoxels where at least 10% (N \x01\
          \ 6) of participants did not have lesions."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'In addition, SCCAN

    identiﬁed a broad network of cortical regions extending from the inferior parietal
    lobule

    into superior and middle temporal gyri and temporal pole and in frontal regions
    including

    inferior frontal and middle and superior frontal gyri (optimized sparseness =
    0.83, CV

    correlation = .52, p < .001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
