---
id: bac_wac_damage_25_model
name: BAC and WAC proportional damage model (>25%)
kind: predictor
findings:
- id: f1
  target: brocas_aphasia
  target_kind: impairment
  claim: A model based on at least 25% damage to both the BAC and WAC clusters classified
    individuals with Broca's aphasia with 90% accuracy.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: not_reported
    population: patients with chronic left hemispheric stroke
    phase: not_reported
    time_post_onset: at least 6 months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Aphasia types were classified using the Western Aphasia Battery, which the authors
    note has limitations and is not a gold standard
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Leave-one-out cross-validation classification based
    on whether patients had at least 25% damage to both the Broca''s area cluster
    (BAC) and the Wernicke''s area cluster (WAC), where these clusters were defined
    by data-driven voxel-wise lesion-symptom mapping (VLSM). The model classified
    Broca''s aphasia against other types of aphasia; The analysis grouped participants
    who had at least 25% damage to both BAC and WAC versus those who had <25% damage
    to either BAC, WAC, or both. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S1-C7, two-model
    agreement, human verification pending): Methods


    Participants

    The study sample was selected from a database that includes 76 patients with chronic
    left hemispheric stroke Original text-layer quotation is preserved below. PDF
    image reading (P2-S1-C8, two-model agreement, human verification pending): . All
    patients were at least

    6 months post-stroke and the mean time since stroke onset was 36.7

    months (SD=45.51; range=6–276) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
  citation: '@Fridriksson2015'
  source_passages:
  - section: Original source P4-S1-C3
    page: 4
    quote: 'For the “damage >25%” analysis, the overall classiﬁcation ac-

      curacy was 91.4% (Fig. 4).'
    supports: claim
  - section: Original source P4-S1-C4
    page: 4
    quote: 'Broca’s aphasia was classiﬁed with

      90% accuracy (18/20 correctly classiﬁed) and those with other

      types of aphasia with 92% accuracy (46/50 correctly classiﬁed).'
    supports: claim
  - section: Original source P4-S1-C2
    page: 4
    quote: 'For example, the

      ﬁrst classiﬁcation analysis grouped participants together who

      had at least 25% damage to both BAC and WAC versus those

      who had <25% damage to either BAC, WAC, or both.'
    supports: method
  - section: Original source P2-S1-C7
    page: 2
    quote: 'Methods

      Participants

      The study sample was selected from a database that includes 76 pa-

      tients with chronic left hemispheric stroke.'
    supports: sample
  - section: Original source P2-S1-C8
    page: 2
    quote: 'All patients were at least

      6 months post-stroke and the mean time since stroke onset was 36.7

      months (SD = 45.51; range = 6–276).'
    supports: sample
  - section: Original source P2-S1-C10
    page: 2
    quote: 'Aphasia

      types were classiﬁed according to the Western Aphasia Battery (WAB;

      Kertesz 1982).'
    supports: method
  - section: Original source P6-S3-C12
    page: 6
    quote: 'Accordingly, it is crucial to

      emphasize that the current results should be interpreted in re-

      lation to WAB limitations.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Leave-one-out cross-validation classification based on whether patients
  had at least 25% damage to both the Broca's area cluster (BAC) and the Wernicke's
  area cluster (WAC), where these clusters were defined by data-driven voxel-wise
  lesion-symptom mapping (VLSM).
assessment:
- Western Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2015
  proposal_id: R003
  review_status_sha256: c8a4c98e2d5942b62e90b07481888678b6ae85256453f17a446e6416dd13919a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
        A/passages.json: 5e7a7c94052222f6e79c1e338f3567928f5d47951e79a65ce773aaded83de449
        A/raw.json: 957e977da6f7e63fd0c4754750d1c45d110e8bb4bed09cecb47207259f825190
        A/source-units.json: 23c2fa07b5157e1f57275bf01240012f1fa647524f87b344abbe31380f151789
        A/full-source-units.json: 9e3e836dacc87a1996ab137442cc81cf609623477ce5d47a737bd44334412366
        A/meta.json: e52670569ddc6810219e1a591b4fa03d458abbac2538d8a989a453a979fdc339
        A/table-images/manifest.json: 017db2bcea7ec09bb79a3bcaf459d0160e0a4a9086f133fe8659d4e5b38e97ee
        A/clauses/window-03/raw.json: 60b8803323bc86911688987efbbf5e5a6f1933913adc75746cf378c777b9fb76
        A/clauses/window-03/prompt.txt: b50e0a8099923349b363c77f8639b70eb9451edaa1a95e51a87dd43f782bc809
        A/clauses/window-03/meta.json: b3f51d9dad33c5422c23de719116f6dff76543920c9ce4b61fc2e93d18d2e116
        A/clauses/window-04/raw.json: 907d1748349320cdf2a6aaebe3a62737670975a32f270f9666895af9167502bc
        A/clauses/window-04/prompt.txt: a2fdc9b3e309b22976e6dec3c17e4896ed74d4767ed640eb90cfcd9908fb92f9
        A/clauses/window-04/meta.json: 115c7479750f511e023b078ba70e35a54953cb163e61b93c77d62479ad295ad3
        A/clauses/window-05/raw.json: f62bc2470bb3a5ce708eaeb77ddac5eb513ba7b08f411ffe0115c45b70d9a53d
        A/clauses/window-05/prompt.txt: 2c2214606fae91aa8eb22e2be9cb7afa5a01f796dbf60dc06e7d5b55929ca076
        A/clauses/window-05/meta.json: 2450a033d38f77ec4761a3bd1b38c58881804b538e490ecf5f7c951f97cdf557
        A/clauses/window-02/raw.json: f070aa1685a2488a6187d073b1b50b2dfc39d4e3b56e25d0ebec95d2799c477d
        A/clauses/window-02/prompt.txt: 0ee2abd6c5322dd37a7a2a3bac7ca130090e62a9cc4ec9dc8420ab4b0010202c
        A/clauses/window-02/meta.json: 2be05676b277dc01d3943a4339ffa3c0e9839a814d181f0efff648e276f6cf40
        A/clauses/window-07/raw.json: 038aa860bee9209cfb0cd3a36ac960f8b557bcfd07816475ebe380bd78fcb7ef
        A/clauses/window-07/prompt.txt: 430689b6ba7673edd79fdbfd8c76e8cb16b16e519965dd5daebe43b11bfd198a
        A/clauses/window-07/meta.json: 4dbd9073760e45da0a2419b8697f24515b2fa855a61f8092c2ac7ca9b22654a5
        A/clauses/window-01/raw.json: 5f9deba380d70bfbc324b4dc714d581592a136107befc61465f9007ac8388248
        A/clauses/window-01/prompt.txt: 26aeabc0e10745365ac4e067e1548b43d1332a6f776ad4626652c5304bbeea7c
        A/clauses/window-01/meta.json: 3292f12e62f6520445c53f04d111c220cccc2a8422b6975722d30feb3ef3daf1
        A/clauses/window-06/raw.json: c74e87beaeb113dae29abb32cac8a7a6be5471c489d5ced05c82eaaf04291ec7
        A/clauses/window-06/prompt.txt: a11e789d9dd29cddfc8c19a3774aaad5fbc96fcd6ad11e399cab1591fe856a87
        A/clauses/window-06/meta.json: ffbdf0a5375f651d04e69e648a6f31deb636c75871745aecaa42269cb5362c5c
        B/passages.json: 5e7a7c94052222f6e79c1e338f3567928f5d47951e79a65ce773aaded83de449
        B/raw.json: 462bc33f792fc893db8e264d9dce1d20ec29de0ac65c19c52c93b917c802cd0a
        B/source-units.json: 23c2fa07b5157e1f57275bf01240012f1fa647524f87b344abbe31380f151789
        B/full-source-units.json: 9e3e836dacc87a1996ab137442cc81cf609623477ce5d47a737bd44334412366
        B/meta.json: 029e881ff9316ae6cf459f7b1f056172616bf838a8db3531985d832c35f08561
        B/table-images/manifest.json: 017db2bcea7ec09bb79a3bcaf459d0160e0a4a9086f133fe8659d4e5b38e97ee
        B/clauses/window-03/raw.json: c42492fe5c9eb254867986492f2ef5e8289ab5cdf793ae57321140ede331293a
        B/clauses/window-03/prompt.txt: b50e0a8099923349b363c77f8639b70eb9451edaa1a95e51a87dd43f782bc809
        B/clauses/window-03/meta.json: 2c6efad5696a08617f9ebf3415809266f1113e8582a6c9c33fc443d3ddab2637
        B/clauses/window-04/raw.json: 1a078689688666fb3a710bf43967db150567e253446adf09b4261cbfe7c2b8a7
        B/clauses/window-04/prompt.txt: a2fdc9b3e309b22976e6dec3c17e4896ed74d4767ed640eb90cfcd9908fb92f9
        B/clauses/window-04/meta.json: 34986f83a636abc33c177444a7c6c56b0a0e8fa7ba054d42a4d638c6fe440164
        B/clauses/window-05/raw.json: 14cc8c639c05d610f3d57e74eb75317adf2b841b07b449e8826d02f25999bf96
        B/clauses/window-05/prompt.txt: 2c2214606fae91aa8eb22e2be9cb7afa5a01f796dbf60dc06e7d5b55929ca076
        B/clauses/window-05/meta.json: 3a9ed02595316d6cb0ae83fa21ee674984d929ed0b59051b00ae765d45ce5b40
        B/clauses/window-02/raw.json: 18a229523ffd7359c9a796ddf44a2f2c3f37216b225309ac64d118d0849df2b0
        B/clauses/window-02/prompt.txt: 0ee2abd6c5322dd37a7a2a3bac7ca130090e62a9cc4ec9dc8420ab4b0010202c
        B/clauses/window-02/meta.json: f937d3c4295a9d078885e794c5cea377ab4829185543b20a4e2c4f803c532d8e
        B/clauses/window-07/raw.json: 60525a6a8dc4296138114dbefa5064054abbb93637f9c3f5dbb4b00ebe41915d
        B/clauses/window-07/prompt.txt: 430689b6ba7673edd79fdbfd8c76e8cb16b16e519965dd5daebe43b11bfd198a
        B/clauses/window-07/meta.json: 6356f9d846fefd4d239ac98a64d92a1cab86578fd2fe7312de7e3478e129fa3f
        B/clauses/window-01/raw.json: e22fdb7d14a974e5c81af63cfece4eb66f0721adcbb35688d463c38e120f998f
        B/clauses/window-01/prompt.txt: 26aeabc0e10745365ac4e067e1548b43d1332a6f776ad4626652c5304bbeea7c
        B/clauses/window-01/meta.json: 2ebc8ded6c68bd3a6a4acf47c5b8f199f4819570b544a9fd44e5375630b8abbe
        B/clauses/window-06/raw.json: 61406e21888b5153a1ada0896fe522d06b902643442c31285fa78d0397474dc3
        B/clauses/window-06/prompt.txt: a11e789d9dd29cddfc8c19a3774aaad5fbc96fcd6ad11e399cab1591fe856a87
        B/clauses/window-06/meta.json: c448bc1d8b86b19387f1a8620d44d1a39cb11ce63c1d87c65f4b4d681f7d9270
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
      pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2015
      source_status_sha256: 970a392d5c3991707f0aa89edfe3df28f338c972bfc4b1093b0fd15b279b1f72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: proportional damage to BAC and WAC (>25%)
    outcome:
      text: Broca's aphasia
    analysis_label: LOOCV classification (Damage >25%)
    relation: performance
    evidence_ids:
    - P4-S1-C3
    - P4-S1-C4
    qualifier_ids:
    - P4-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2015
      source_status_sha256: 970a392d5c3991707f0aa89edfe3df28f338c972bfc4b1093b0fd15b279b1f72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P4-S2-C2
      - Accounting without a linked unit P4-S2-C3
      - Accounting without a linked unit P4-S2-C5
      - Accounting without a linked unit P4-S2-C7
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C2
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P4-S2-C5
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S2-C2
      - Unaccounted source passage P4-S2-C3
      - Unaccounted source passage P5-S1-C2
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S2-C6
      - Accounting without a linked unit P5-S3-C7
      - Accounting without a linked unit P5-S4-C2
      - Accounting without a linked unit P6-S1-C3
      - Unaccounted source passage P5-S3-C7
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P5-S4-C2
      - Result passage disposed without unit P6-S3-C3
      - Result passage disposed without unit P6-S4-C5
      - Result passage disposed without unit P6-S4-C7
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C6
      unattached_null_or_qualifier_ids:
      - P4-S2-C5
      - P6-S1-C3
      - P6-S4-C5
      - P7-S1-C5
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 145
      unselected_timing_passages:
      - P2-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P4-S1-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S3
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2015
      source_status_sha256: 970a392d5c3991707f0aa89edfe3df28f338c972bfc4b1093b0fd15b279b1f72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement of whole-brain NPM result.
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies that BAC damage is not sufficient.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of follow-up VLSM result.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: General summary of classification accuracy.
    - source_id: P2-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of time post-stroke.
    - source_id: P2-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information (gender).
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of age.
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General lesion overlap map for all participants.
    - source_id: P2-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion overlap locations.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Primary result of whole-brain NPM.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies the pars opercularis as the key area.
    - source_id: P3-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Provides statistical threshold for NPM.
    - source_id: P3-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: 'Null finding: no area more likely damaged in other aphasias.'
    - source_id: P3-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies that BAC damage is not a perfect predictor.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Primary result of follow-up VLSM.
    - source_id: P3-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Provides statistical thresholds for follow-up VLSM.
    - source_id: P3-S3-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Synthesis of VLSM results.
    - source_id: P3-S3-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of BAC result in Figure 2 caption.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Accuracy for >25% analysis.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Specific accuracy for Broca's and other aphasias (>25%).
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Accuracy for >50% analysis.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Specific accuracy for Broca's and other aphasias (>50%).
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Accuracy for >75% analysis.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Specific accuracy for Broca's and other aphasias (>75%).
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Accuracy for lesion size classifier.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Logistic regression significance and accuracy.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Provides coefficients for the logistic model.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Significance of interaction term.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Accuracy and coefficients for combined model.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Completes the coefficients for the combined model.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Significance of WAC and volume as single predictors.
    - source_id: P5-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of BAC result.
    - source_id: P5-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of WAC result.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about the number of analyses.
    - source_id: P5-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of first VLSM.
    - source_id: P5-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of second VLSM.
    - source_id: P5-S1-C11
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of logistic regression accuracy.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Synthesis that damage involves two structures.
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 1
      reason: 'Null finding: no patients with spared BAC but damaged WAC.'
    - source_id: P5-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P5-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to a specific patient's anatomy.
    - source_id: P5-S4-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Note on incorrect classification of a specific case.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Conclusion that Broca's aphasia is most commonly associated with cortical
        injury.
    - source_id: P6-S2-C6
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of classification accuracy.
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about WAB not testing agrammatism.
    - source_id: P6-S4-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion of univariate analysis limitations.
    - source_id: P6-S4-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion of univariate analysis limitations.
    - source_id: P6-S4-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion of second analysis (WAC).
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Final conclusion of the study.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Final conclusion restatement.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Conclusion regarding Wernicke's area involvement.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Conclusion regarding Broca's area involvement.
    unresolved_coverage:
    - source_id: P5-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C5
    - P1-S1-C6
    - P1-S1-C7
    - P2-S1-C14
    - P2-S2-C1
    - P2-S2-C3
    - P2-S2-C5
    - P2-S2-C6
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C9
    - P3-S3-C4
    - P3-S3-C5
    - P3-S3-C12
    - P4-S2-C3
    - P5-S1-C1
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C9
    - P5-S1-C11
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C6
    - P5-S3-C7
    - P5-S3-C10
    - P5-S4-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S2-C6
    - P6-S3-C3
    - P6-S4-C5
    - P6-S4-C6
    - P6-S4-C7
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
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
      - P2-S1-C11
      recruited_sample:
      - P2-S1-C7
      eligibility:
      - P2-S1-C8
      - P2-S1-C9
      imaging_provenance:
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      imaging_timing:
      - P2-S1-C8
      outcome_timing:
      - P2-S1-C8
      outcome_definition:
      - P2-S1-C10
      - P6-S2-C12
      validation:
      - P3-S1-C9
      analysis_restrictions:
      - P3-S1-C6
      dependent_variable_statement:
      - P3-S1-C11
      - P3-S2-C3
      - P4-S1-C14
      - P4-S2-C6
      limitations:
      - P6-S3-C2
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C12
      - P6-S3-C13
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C6
      - P5-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C13
      - P2-S2-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P4-S1-C11
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
      pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
      review_sha256: c8a4c98e2d5942b62e90b07481888678b6ae85256453f17a446e6416dd13919a
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
      - P4-S1-C3
      - P4-S1-C4
      source_result: In a leave-one-out cross-validation (LOOCV) analysis using proportional
        damage to the Broca's area cluster (BAC) and Wernicke's area cluster (WAC)
        with a threshold of >25% damage to both regions, the model achieved 91.4%
        overall classification accuracy. Specifically, Broca's aphasia was classified
        with 90% accuracy (18/20 correctly classified), while other aphasia types
        were classified with 92% accuracy (46/50 correctly classified).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R003 corresponds to the LOOCV classification
            using the >25% damage threshold to BAC and WAC. The source P4-S1-C3 and
            P4-S1-C4 explicitly report the accuracy for this specific 'damage >25%'
            analysis, distinguishing it from the >50% and >75% analyses. The method
            is correctly identified as LOOCV classification based on proportional
            damage to these clusters.
          source_ids:
          - P4-S1-C3
          - P4-S1-C4
          - P3-S3-C6
          - P3-S3-C9
        direction:
          answer: fits
          reason: The claim states the model classified Broca's aphasia with 90% accuracy.
            This aligns with P4-S1-C4 which states 'Broca’s aphasia was classified
            with 90% accuracy'. The direction of the association (damage to BAC/WAC
            predicts Broca's aphasia) is consistent with the VLSM findings described
            in P3-S3-C5 and the classification results.
          source_ids:
          - P4-S1-C4
          - P3-S3-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as proportional damage to BAC
            and WAC (>25%). The outcome is Broca's aphasia. The patient measurement
            is template_lesion_overlap, as the BAC and WAC are defined by VLSM results
            (voxel-wise lesion-symptom mapping) overlaid on standard templates (ICBM),
            and the classification uses the proportion of lesion overlap with these
            clusters. This is distinct from patient_diffusion or functional_imaging.
            The method is correctly described as LOOCV classification.
          source_ids:
          - P4-S1-C2
          - P3-S1-C5
          - P3-S1-C9
          - P3-S2-C6
          - P3-S3-C3
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the model classified Broca's
            aphasia against other types of aphasia, which is accurate per P3-S3-C6
            and P4-S1-C2. It also includes the limitation regarding the WAB classification
            of aphasia types, which is supported by P6-S2-C12 and P6-S3-C12. The grouping
            logic (>25% to both vs <25% to either) is correctly stated from P4-S1-C2.
          source_ids:
          - P4-S1-C2
          - P3-S3-C6
          - P6-S3-C12
        missing_material_caveat:
          answer: fits
          reason: 'The draft captures the key material caveats: the specific threshold
            (>25%), the comparison group (other aphasia types), and the diagnostic
            limitation of the WAB. The note about numerical differences not necessarily
            implying significance (P4-S1-C9) is a general methodological caveat but
            the specific accuracy for this model is reported. The unresolved image
            reading disagreements in P2-S1-C12, P3-S2-C12, and P5-S3-C10 do not directly
            alter the core result of the >25% LOOCV accuracy reported in P4-S1-C3/C4,
            as those passages relate to sample composition details or specific case
            descriptions that do not contradict the aggregate classification accuracy.
            The core relationship is faithful.'
          source_ids:
          - P4-S1-C9
          - P6-S3-C12
      optional_pending:
      - Sample size for the specific >25% subgroup (18 Broca's, 12 other) is mentioned
        in P3-S2-C12 but not explicitly transcribed in the draft's sample_n field,
        though the total N=70 is known from P2-S1-C4. The draft leaves sample_n null,
        which is acceptable for a qualitative draft but could be enriched.
      - The specific odds ratios or coefficients from the logistic regression (P4-S2-C2/C3)
        are not included in this LOOCV-specific draft, which is appropriate as they
        belong to a different analysis model.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for the specific >25% subgroup (18 Broca's, 12 other) is mentioned
      in P3-S2-C12 but not explicitly transcribed in the draft's sample_n field, though
      the total N=70 is known from P2-S1-C4. The draft leaves sample_n null, which
      is acceptable for a qualitative draft but could be enriched.
    - The specific odds ratios or coefficients from the logistic regression (P4-S2-C2/C3)
      are not included in this LOOCV-specific draft, which is appropriate as they
      belong to a different analysis model.
    normalizations:
    - field: sample.n
      original: 70
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R003
      exposure:
        text: proportional damage to BAC and WAC (>25%)
      outcome:
        text: Broca's aphasia
      analysis_label: LOOCV classification (Damage >25%)
      relation: performance
      evidence_ids:
      - P4-S1-C3
      - P4-S1-C4
      qualifier_ids:
      - P4-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2015
        source_status_sha256: 970a392d5c3991707f0aa89edfe3df28f338c972bfc4b1093b0fd15b279b1f72
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7f412e457f6e904343d716513333fad51c779b8113ed41ac3250c5544d3a67ee
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C7
          page: 2
          text_layer_sha256: 7f412e457f6e904343d716513333fad51c779b8113ed41ac3250c5544d3a67ee
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Participants

          The study sample was selected from a database that includes 76 pa-

          tients with chronic left hemispheric stroke.'
        anchor_text: 'Methods

          Participants

          The study sample was selected from a database that includes 76 pa-

          tients with chronic left hemispheric stroke.'
        excluded_fragments: []
        image_sha256: fd7e3b0bd2dbefcb369660b69dc8bda6fe56377fc513cf8a5fb607b9eb1442e4
        transcription: 'Methods


          Participants

          The study sample was selected from a database that includes 76 patients
          with chronic left hemispheric stroke'
      P2-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0f8993e091665ad4231a4d9b02ced1b7c2de723c1c463048cf0e18ae7feedc4c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 579987e528067bdc90c155c9f7002b379b135a1cc4b2c55101011a27e69ff174
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C8
          page: 2
          text_layer_sha256: 579987e528067bdc90c155c9f7002b379b135a1cc4b2c55101011a27e69ff174
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients were at least

          6 months post-stroke and the mean time since stroke onset was 36.7

          months (SD = 45.51; range = 6–276).'
        anchor_text: 'All patients were at least

          6 months post-stroke and the mean time since stroke onset was 36.7

          months (SD = 45.51; range = 6–276).'
        excluded_fragments: []
        image_sha256: 686c029a32d6ac85837efd540133d1dc2b721fa569abd0da80d7f27811d682ba
        transcription: '. All patients were at least

          6 months post-stroke and the mean time since stroke onset was 36.7

          months (SD=45.51; range=6–276)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'For the “damage >25%” analysis, the overall classiﬁcation ac-

    curacy was 91.4% (Fig. 4).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
