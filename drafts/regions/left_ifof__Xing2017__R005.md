---
id: left_ifof
name: left inferior fronto-occipital fasciculus cluster
kind: network
findings:
- id: f1
  target: comprehension_scores
  target_kind: impairment
  claim: Reduced FA and increased MD, AD, and RD of the left IFOF were significantly associated with both word-level comprehension (WLC) and sentence-level comprehension (SLC) scores.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: not_reported
    population: chronic left hemisphere stroke survivors with aphasia
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Most left hemisphere white matter connections could not be reconstructed with probabilistic tractography in individual patients due to varied lesions, necessitating the use of a healthy-subject template
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population reference tract template of the left inferior fronto-occipital fasciculus, used to extract mean fractional anisotropy (FA), mean diffusivity (MD), axial diffusivity (AD), and radial diffusivity (RD). Analysis controlled for age, total lesion volume, and the number of lesioned voxels within the tract; Results remained significant when further controlling for handedness (Edinburgh Handedness Index). Additional metadata has not been transcribed; review the pending-field flags before approval. Reconcile this new analysis with earlier drafts and source-review decisions for the paper; new candidate IDs do not carry earlier decisions forward. Publication correction (human verification pending): Corrected to patient diffusion metrics: TBSS and mean diffusion values in reference-defined tract masks, with template construction distinguished from patient measurements.'
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
    - not_transcribed:sample.n
    - not_transcribed:sample.time_post_onset
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:comprehension_scores
    - publication_correction_pending_human_verification
  citation: '@Xing2017'
  source_passages:
  - section: Original source P4-S2-C8
    page: 4
    quote: "Partial \ncorrelations showed that when controlling for age, total lesion \nvolume, and the number of lesioned voxels in each tract, reduced \nFA and increased diffusivity measures including MD, AD, and \nRD of the left IFOF were significantly associated with both WLC \nand SLC scores (corrected P < 0.05, Figure 4A)."
    supports: claim
  - section: Original source P2-S3-C2
    page: 2
    quote: "MATERIALS AND METHODS\nParticipants\nForty (14 females) chronic left hemisphere stroke survivors were \nrecruited in the study with inclusion criteria as follows: native \nEnglish speaker; at least 6 months post-stroke; able to follow test-\ning instructions; and no history of other significant neurological \nillnesses."
    supports: sample
  - section: Original source P3-S3-C12
    page: 3
    quote: "The final groupwise prob-\nability map for each tract was generated with a threshold at least \n50% (14/27 = 0.52) of healthy subjects (27, 28), and the respective \nbinary map was generated as template to extract the mean values \nof DTI metrics for individual patient."
    supports: method
  - section: Original source P4-S3-C2
    page: 4
    quote: "Considering the potential \nconfounding effect of handedness, we further performed the par-\ntial correlation analyses with the Edinburgh Handedness Index as \nan additional covariate and the results remained significant (data \nnot shown)."
    supports: confounders
  - section: Original source P8-S1-C12
    page: 8
    quote: "Due to varied left hemisphere lesions, most of the left \nhemisphere white matter connections could not be reconstructed \nwith probabilistic tractography in individual patients."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Xing2017
  proposal_id: R005
  review_status_sha256: bbbce7523354e006983364051e91b2f353054fccca7e536a8f16543cc9573a3d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
        A/passages.json: 4b4086dc9237eedb41f63db3ac4ae53d010b9dc227bc51e0919cbb1f2d5cdfbe
        A/raw.json: c8e3c4d1e56b0da68df39ece5594d3d0ef86f881ee46ac521746449744fac852
        A/source-units.json: d254860e6657213b5b83a293926a6e23c3e0bf42ae16481f403d2aff52591281
        A/full-source-units.json: b96bdc8a08798beec2967f6d7b26be513dfa3d1f73e46a4d703c51b6d8cbc684
        A/meta.json: f4312d9a17d9bd7a1d6f0a4d2b1e1f7ed18c029d81004d5ad3ddf8207aca0224
        A/table-images/TABLE-1-page-2-1.png: 16edbd1c6189f1c685006d2ab2ace8f67ca2aff48d6fc3b2ce7b5a8394b5db0d
        A/table-images/page-2.png: 7e8a4efdf7603edaa806dd7516a19a433e07a5e6eaa8ea94ae91d92d1e8b33c6
        A/table-images/page-6.png: 452e3b3021e057afd3bd711d0aaa0938a7b53ffe640632ce242cf2a2862042bc
        A/table-images/TABLE-2-page-6-1.png: d2575a63e6cb4114dcfa178abc0438e8bc442ce2ffd207debef1f387c6afd433
        A/table-images/manifest.json: 4970b7611a7af8a58166004beb2a05be5dd94090c149bb5eed51fcdbd5220a35
        A/clauses/window-03/raw.json: 24c58cd01853d324fab6c1b70be8138ec81a7757275738d3768a4dc94971ac5a
        A/clauses/window-03/prompt.txt: 0100e93b60e10ca63d34d710b97308921ed42ab7bfc4915477020d719c8fd81f
        A/clauses/window-03/meta.json: f7829a57e3e01cd4d481344d4364b3c7586b41674568000b6867c8bb44310627
        A/clauses/window-04/raw.json: 68089b331501192c4fa223c8285554ea042c6681a6a94f1937843022db0ece40
        A/clauses/window-04/prompt.txt: ccab4e5b9fa08e1acae40364483fcc283c13b42be70824e841a850b81e0fb945
        A/clauses/window-04/meta.json: ed4d57644711a8d61fb7d7913ba20ecf13a49ddf9f0917ae8d8cc16fd930e45f
        A/clauses/window-05/raw.json: ee62c80bdacc44c8fd51529fb59aba84b81e72b9bdff7bdfc2a52a1031d017cb
        A/clauses/window-05/prompt.txt: c88c639547fc8f7b3a770a445bfbd9293d1f14c62296584894da7f75a163276c
        A/clauses/window-05/meta.json: af009ee9303f5bec9439014e02a91b20106630cdd92b684e747cd90c1bb53967
        A/clauses/window-02/raw.json: 513f6757d7b85eabaa07790e613cf7ada89e13ca959e4a127fd9a7cb339075fc
        A/clauses/window-02/prompt.txt: 252e282ec942d33f1e4aaa1b78e54efe213cd5ff86115eae89f8395195e3f54d
        A/clauses/window-02/meta.json: 80d8177745a0d1963c7979f9e6da07f8cf7a6015453aad33a310d404d3283b59
        A/clauses/window-01/raw.json: c364a3f5cf804af02c6d56abcd7ac77f0c88f30aac39b74c3f0793d3021918bd
        A/clauses/window-01/prompt.txt: f48cbfbeae32d3c32119e07098003da5f31271114cfa2ee8ff5f238b3278988c
        A/clauses/window-01/meta.json: 82c61b3782b720f9371912e1ac5f53c2548e3170ac55654ccf7f22bb29008582
        A/clauses/window-06/raw.json: 1ab0315ecd1a622f441c9f33746f8a2f79bfad06962f14e9c19f5643223b782f
        A/clauses/window-06/prompt.txt: 27e6fb7864c0d62ce4c420adda6c6694cc1e46b89d889d1a8f23092f06e3698b
        A/clauses/window-06/meta.json: 5b8eea60f2e61ba3f2e0a9cda27db57c64f804fde3a0e56f67ed99ba3da8939c
        A/tables/TABLE-1-page-2-1/raw.json: d6190287e62e6d9bbfca77d33cdd79e421053bb1a24114c8f191d9e94be15ba1
        A/tables/TABLE-1-page-2-1/prompt.txt: 3cc60833a295632344ab4aaeeccb1529728b8aaf1522666de9828eacb78c878d
        A/tables/TABLE-1-page-2-1/meta.json: 3b08b2ae7116fd14ed5afe00b313e10f95aef2bc3358349b1f14cd4d3d5216d9
        A/tables/TABLE-2-page-6-2/raw.json: 2204f1281dc5e03094b363d5c8c5b79dd89b3f7b9e97cda38f1deb7d56c97a23
        A/tables/TABLE-2-page-6-2/prompt.txt: f9460ab6c70914b7826a68abd2822aff0ec4a4f3b49f2fb88339b4f34f0bb601
        A/tables/TABLE-2-page-6-2/meta.json: dfaac7dcc6dcfc82037b6890f6f320ab51485e5f31bc730f8f83e3bb4c824569
        B/passages.json: 4b4086dc9237eedb41f63db3ac4ae53d010b9dc227bc51e0919cbb1f2d5cdfbe
        B/raw.json: ec908fd5fde55a01272be5d1cea7589a641a0ea40a66809ffb709703cf223577
        B/source-units.json: d254860e6657213b5b83a293926a6e23c3e0bf42ae16481f403d2aff52591281
        B/full-source-units.json: b96bdc8a08798beec2967f6d7b26be513dfa3d1f73e46a4d703c51b6d8cbc684
        B/meta.json: 75330a94943f58589f00ecec4cc1681850c730e524e3796e47d8fd6cdfd4e67e
        B/table-images/TABLE-1-page-2-1.png: 16edbd1c6189f1c685006d2ab2ace8f67ca2aff48d6fc3b2ce7b5a8394b5db0d
        B/table-images/page-2.png: 7e8a4efdf7603edaa806dd7516a19a433e07a5e6eaa8ea94ae91d92d1e8b33c6
        B/table-images/page-6.png: 452e3b3021e057afd3bd711d0aaa0938a7b53ffe640632ce242cf2a2862042bc
        B/table-images/TABLE-2-page-6-1.png: d2575a63e6cb4114dcfa178abc0438e8bc442ce2ffd207debef1f387c6afd433
        B/table-images/manifest.json: dabd9c6b6e19f18fe9e8cb43f6ab34ebeb61f25362b6eb3d61b8b7d342bee37b
        B/clauses/window-03/raw.json: 97e4277a80bc599bd82e71f6a6e351c2e7789260d2895a8e6173d4b3cc2e4d1f
        B/clauses/window-03/prompt.txt: 0100e93b60e10ca63d34d710b97308921ed42ab7bfc4915477020d719c8fd81f
        B/clauses/window-03/meta.json: 2a4ec88eecb6f4225d9f855f7a403e080501ee46cdad4616f62d7894b0f4ea36
        B/clauses/window-04/raw.json: b6f78f206b767271cac3a57988c3a82fb9ddd3accf8276e50c2227faf54c614e
        B/clauses/window-04/prompt.txt: ccab4e5b9fa08e1acae40364483fcc283c13b42be70824e841a850b81e0fb945
        B/clauses/window-04/meta.json: 24af9aa24379418fca6c2f5e4d7585d710ea2d18627ada789cb81c49f0eed1a1
        B/clauses/window-05/raw.json: 3f15257a6717fd1e5b1d52a4e2d9f7b1ba5bd838e5b3d0084a5cb2507a075127
        B/clauses/window-05/prompt.txt: c88c639547fc8f7b3a770a445bfbd9293d1f14c62296584894da7f75a163276c
        B/clauses/window-05/meta.json: 620f51489391077e5171131562b4f4e5ac2b6ab00445179d56af6bc837528cd2
        B/clauses/window-02/raw.json: 5da95b63ff1d421c16c569505ba0f9fe7ad56c30b791bc5eaef4f6be080914c9
        B/clauses/window-02/prompt.txt: 252e282ec942d33f1e4aaa1b78e54efe213cd5ff86115eae89f8395195e3f54d
        B/clauses/window-02/meta.json: 8ef1084a00f987679c413b0d5a6b2a416333e2579af35f8e5535a65e20aa3bb0
        B/clauses/window-01/raw.json: 04ffa7a87fff0b3bcfc8884c9eb8cdb02ab2605dcde94f9c0f879f3c22b06467
        B/clauses/window-01/prompt.txt: f48cbfbeae32d3c32119e07098003da5f31271114cfa2ee8ff5f238b3278988c
        B/clauses/window-01/meta.json: bac9460f6f9943317bfae3bf179d200f2f71462af7a0aab6315538809b06c8b8
        B/clauses/window-06/raw.json: 099e5f88d5db098f6327eab04439e298de04a3c47f6c27398d0727b8016e8875
        B/clauses/window-06/prompt.txt: 27e6fb7864c0d62ce4c420adda6c6694cc1e46b89d889d1a8f23092f06e3698b
        B/clauses/window-06/meta.json: 1c92f7e32127e5dacf7fc23776d6743a6de04d22d9ea9858d2d17da15de77500
        B/tables/TABLE-1-page-2-1/raw.json: d30f88002a83cbec627f02b78a61f66436dbf6d1e3bcfc579b1c74449e6d1dd2
        B/tables/TABLE-1-page-2-1/prompt.txt: 3cc60833a295632344ab4aaeeccb1529728b8aaf1522666de9828eacb78c878d
        B/tables/TABLE-1-page-2-1/meta.json: f293d39a6ef2b610e1c17ed1e0d2c32a8bcb887bf98e6f92292ef49099e7b19f
        B/tables/TABLE-2-page-6-2/raw.json: 0ea1406c678228b5106fb28e791ee054da04802e8d424823b38f0dd03cb89051
        B/tables/TABLE-2-page-6-2/prompt.txt: f9460ab6c70914b7826a68abd2822aff0ec4a4f3b49f2fb88339b4f34f0bb601
        B/tables/TABLE-2-page-6-2/meta.json: 061d3996c153491548417bc338fbd5ccc560ccc305beae5c4c79e5ae0c216d01
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
      pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      source_review: _compare/relationships-2026-11-16/review-current/Xing2017
      source_status_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: reduced FA and increased MD, AD, and RD of the left inferior fronto-occipital fasciculus (IFOF)
    outcome:
      text: word-level comprehension (WLC) and sentence-level comprehension (SLC) scores
    analysis_label: Partial correlation (tract integrity)
    relation: association
    evidence_ids:
    - P4-S2-C8
    qualifier_ids:
    - P4-S2-C7
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      source_review: _compare/relationships-2026-11-16/review-current/Xing2017
      source_status_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C3
      - Result passage disposed without unit P1-S2-C4
      - Result passage disposed without unit P1-S2-C5
      - Result passage disposed without unit P1-S2-C6
      - Accounting without a linked unit P4-S1-C10
      - Accounting without a linked unit P4-S1-C11
      - Accounting without a linked unit P4-S2-C6
      - Accounting without a linked unit P4-S2-C8
      - Accounting without a linked unit P4-S2-C9
      - Unaccounted source passage P4-S1-C10
      - Unaccounted source passage P4-S1-C11
      - Unaccounted source passage P4-S2-C6
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P4-S2-C9
      - Result passage disposed without unit P4-S3-C3
      - Result passage disposed without unit P4-S3-C4
      - Result passage disposed without unit P4-S3-C5
      - Result passage disposed without unit P4-S3-C6
      - Result passage disposed without unit P4-S3-C7
      - Result passage disposed without unit P4-S3-C8
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P5-S2-C8
      - Unresolved source passage P6-S2-C7
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P8-S2-C7
      unattached_null_or_qualifier_ids:
      - P4-S2-C6
      - P4-S2-C8
      - P7-S2-C7
      suppressed_nonrepresented_units: 20
      default_disposition_count_requires_completeness_check: 142
      unselected_timing_passages:
      - P1-S1-C9
      - P2-S3-C4
      - P2-S3-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P2-S3-C12
        reason: No validation-design cue; inspect the source rather than inferring a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-6-2
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-6-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S1
        - P6-S1
        - P7-S1
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      source_review: _compare/relationships-2026-11-16/review-current/Xing2017
      source_status_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of UF integrity and WLC association.
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of ILF integrity and SLC association.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of IFOF integrity and WLC/SLC association.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 3
      - 9
      reason: Restatement of AF lesion burden vs integrity results.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Directly reports TBSS association for WLC.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Directly reports TBSS association for SLC.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Reports partial correlations for lesion burden in AF, ILF, and UF.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports partial correlations for IFOF integrity.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports partial correlations for ILF integrity.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Reports partial correlations for UF integrity.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Reports sensitivity analysis for UF controlling for PPT.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes:
      - 8
      reason: Reports null result for AF integrity.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Reports sensitivity analysis for handedness.
    - source_id: P4-S3-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      reason: Summary of tract associations.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of ventral stream damage.
    - source_id: P4-S3-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of UF and WLC.
    - source_id: P4-S3-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of ILF and SLC.
    - source_id: P4-S3-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of IFOF and WLC/SLC.
    - source_id: P4-S3-C8
      disposition: repeated
      result_indexes:
      - 3
      - 8
      reason: Discussion restatement of AF lesion burden vs integrity.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of UF integrity.
    - source_id: P5-S2-C6
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of IFOF integrity.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of previous literature on posterior middle temporal gyrus.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to healthy subject studies.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of ILF in sentence comprehension.
    - source_id: P7-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of TBSS posterior temporal results.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of AF lesion load.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of AF integrity null result.
    - source_id: P8-S2-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Conclusion restatement of UF and WLC.
    - source_id: P8-S2-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Conclusion restatement of ILF and SLC.
    - source_id: P8-S2-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restatement of IFOF and WLC/SLC.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P4-S3-C3
    - P4-S3-C4
    - P4-S3-C5
    - P4-S3-C6
    - P4-S3-C7
    - P4-S3-C8
    - P5-S2-C2
    - P5-S2-C6
    - P5-S2-C8
    - P6-S1-C8
    - P7-S1-C5
    - P7-S1-C6
    - P7-S2-C6
    - P7-S2-C7
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C2
      - P2-S3-C5
      recruited_sample:
      - P2-S3-C2
      - P2-S3-C5
      eligibility:
      - P2-S3-C2
      imaging_provenance:
      - P2-S2-C9
      - P3-S3-C4
      - P3-S3-C12
      imaging_timing:
      - P2-S3-C2
      outcome_timing:
      - P2-S3-C2
      outcome_definition:
      - P2-S3-C14
      - P3-S1-C1
      - P3-S1-C3
      validation: []
      analysis_restrictions:
      - P3-S2-C9
      - P3-S2-C13
      - P4-S1-C4
      - P4-S1-C8
      - P4-S2-C8
      - P4-S2-C11
      - P6-S1-C3
      - P7-S1-C2
      dependent_variable_statement:
      - P3-S2-C13
      limitations:
      - P8-S1-C11
      - P8-S1-C12
      - P8-S1-C13
      - P8-S1-C14
      - P8-S2-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C13
      - P4-S1-C8
      - P4-S2-C8
      - P4-S2-C11
      - P4-S3-C2
      - P6-S1-C3
      - P7-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C2
      - P2-S3-C2
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: validation
      source_id: P2-S3-C12
      reason: No validation-design cue; inspect the source rather than inferring a design
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: 'Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Corrected to patient diffusion metrics: TBSS and mean diffusion values in reference-defined tract masks, with template construction distinguished from patient measurements.'
    binding:
      source_pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      original_source_sha256: ff4a3bb7b0e9e26673d05797714e5e8923a6cdd7942c1048c60b72f354d6a8da
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording remains in the audit.'
    normalizations:
    - field: sample.n
      original: 40
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: at least 6 months post-stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R005
      exposure:
        text: reduced FA and increased MD, AD, and RD of the left inferior fronto-occipital fasciculus (IFOF)
      outcome:
        text: word-level comprehension (WLC) and sentence-level comprehension (SLC) scores
      analysis_label: Partial correlation (tract integrity)
      relation: association
      evidence_ids:
      - P4-S2-C8
      qualifier_ids:
      - P4-S2-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
        source_review: _compare/relationships-2026-11-16/review-current/Xing2017
        source_status_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d9db111f1b078e6061cd6c06d74d25c4b4c3038a708cb45c75defca72e4f44c5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C2
          page: 2
          text_layer_sha256: d9db111f1b078e6061cd6c06d74d25c4b4c3038a708cb45c75defca72e4f44c5
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
        status: held
        original_text: "MATERIALS AND METHODS\nParticipants\nForty (14 females) chronic left hemisphere stroke survivors were \nrecruited in the study with inclusion criteria as follows: native \nEnglish speaker; at least 6 months post-stroke; able to follow test-\ning instructions; and no history of other significant neurological \nillnesses."
        anchor_text: "MATERIALS AND METHODS\nParticipants\nForty (14 females) chronic left hemisphere stroke survivors were \nrecruited in the study with inclusion criteria as follows: native \nEnglish speaker; at least 6 months post-stroke; able to follow test-\ning instructions; and no history of other significant neurological \nillnesses."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: ff4a3bb7b0e9e26673d05797714e5e8923a6cdd7942c1048c60b72f354d6a8da
      source_pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      pdf_pages:
      - 3
      - 4
      note: 'Corrected to patient diffusion metrics: TBSS and mean diffusion values in reference-defined tract masks, with template construction distinguished from patient measurements.'
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - 'Corrected to patient diffusion metrics: TBSS and mean diffusion values in reference-defined tract masks, with template construction distinguished from patient measurements.'
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P4-S2-C8
      source_result: Partial correlations showed that when controlling for age, total lesion volume, and the number of lesioned voxels in each tract, reduced FA and increased diffusivity measures including MD, AD, and RD of the left IFOF were significantly associated with both WLC and SLC scores (corrected P < 0.05).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the tract-specific partial correlation analysis described in P4-S2-C8, which examines the relationship between DTI metrics of the left IFOF and comprehension scores, controlling for specific covariates.
          source_ids:
          - P4-S2-C8
          - P3-S3-C13
        direction:
          answer: fits
          reason: The source explicitly states 'reduced FA and increased diffusivity measures... were significantly associated', which matches the proposed claim's direction of reduced FA/increased MD, AD, RD associated with comprehension scores.
          source_ids:
          - P4-S2-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as DTI metrics (FA, MD, AD, RD) of the left IFOF. The outcome is WLC and SLC scores. The patient measurement is correctly classified as template_lesion_overlap because the tract template was constructed from healthy subjects (P3-S3-C12) and used to extract mean values in patients, rather than patient-specific tractography.
          source_ids:
          - P4-S2-C8
          - P3-S3-C12
          - P3-S3-C4
        qualifications:
          answer: fits
          reason: The proposed qualifications include controlling for age, total lesion volume, and lesioned voxels in the tract, which are explicitly stated in P4-S2-C8. The additional qualification regarding handedness (P4-S3-C2) is also correctly included as a robustness check.
          source_ids:
          - P4-S2-C8
          - P4-S3-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that individual tract reconstruction was not possible for most patients due to varied lesions, necessitating the use of a healthy-subject template (P8-S1-C12). This is a material caveat regarding the measurement method. No other material caveats appear to be missing from the core relationship description.
          source_ids:
          - P8-S1-C12
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    original_profile: core
    original_binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      review_sha256: bbbce7523354e006983364051e91b2f353054fccca7e536a8f16543cc9573a3d
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: *id001
        digests: *id002
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "Partial \ncorrelations showed that when controlling for age, total lesion \nvolume, and the number of lesioned voxels in each tract, reduced \nFA and increased diffusivity measures including MD, AD, and \nRD of the left IFOF were significantly associated with both WLC \nand SLC scores (corrected P < 0.05, Figure 4A)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: 'Corrected to patient diffusion metrics: TBSS and mean diffusion values in reference-defined tract masks, with template construction distinguished from patient measurements. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
