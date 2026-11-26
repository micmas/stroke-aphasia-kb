---
id: right_arcuate_fasciculus_size_change
name: right arcuate fasciculus size change
kind: predictor
findings:
- id: f1
  target: correct_information_units
  target_kind: impairment
  claim: Schlaug2010 reports, citing the six-patient MIT case series of Schlaug et al. (2009; reference 25), a trend between change in correct information units and change in right arcuate fasciculus size (p=.08). This does not establish statistical significance at .05.
  direction: mixed
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Secondary account of the six-patient MIT case series in Schlaug et al. 2009, not a new cohort.
    phase: not_reported
    time_post_onset: See the cited primary case series.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - not_transcribed
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconciled the source identity to reference 25 (Schlaug et al. 2009). Retained one attributed secondary account and the non-significant p=.08 trend; the parallel Plowman2012 R019 account remains excluded to avoid duplication. Human source review remains pending. Source repair (unapproved): Reconciled the source identity to reference 25 (Schlaug et al. 2009). Retained one attributed secondary account and the non-significant p=.08 trend; the parallel Plowman2012 R019 account remains excluded to avoid duplication. Human source review remains pending.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - not_transcribed:sample.n
    - proposed_concept:correct_information_units
    - agent_source_repair_pending_human_review
  therapy:
    id: mit
    name: Melodic Intonation Therapy
  citation: '@Schlaug2010'
  source_passages:
  - section: Original source P3-S1-C4
    page: 3
    quote: "The change in CIUs \nshowed a strong trend for a correlation (p = 0.08) \nwith the change in the size of the right arcu­\nate fasciculus (AF), a fiber bundle connecting \ntemporal and frontal brain regions [25]."
    supports: claim
  - section: Original source P1-S3-C3
    page: 1
    quote: "Keywords\nn aphasia n arcuate fasciculus \nn auditory–motor mapping \nn connectivity n intervention \nn melodic intonation therapy \nn neuroimaging n nonfluent \naphasia n speech therapy\nSpecial Report\nFor reprint orders, please contact: reprints@futuremedicine.com\n\n"
    supports: method
  - section: Original source P3-S1-C2
    page: 3
    quote: "Another case \nseries of six patients treated with MIT showed a \nmore than 200% improvement in a measure of \nspontaneous speech, correct information units \n(CIUs)."
    supports: sample
  design: narrative-review
predictor_type: imaging_metric
short_definition: change in the size of the right arcuate fasciculus measured via imaging
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schlaug2010
  proposal_id: R005
  approved: false
  original_core_review:
    paper: Schlaug2010
    proposal_id: R005
    review_status_sha256: 741d05e3f74dbf84e5c01981ace6df8a56c133df03ce7b972a1edc80529c0bd5
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
      original_review_binding:
        version: relationship-review-v4
        input_hashes:
          pdf: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          A/passages.json: a9d21adebea7fb7507a1af2c645012e6867d0d803ad3e1b60a4f8e988a89d59f
          A/raw.json: 1faaf23be366c6d48844bd49cec2917a48fbd88d7d54b9744f9a81f78e50efce
          A/source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
          A/full-source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
          A/meta.json: e3373fc5ad045b3522c07d04658dc8e5fac0a59136b791d8a1faffdb727ba081
          A/table-images/manifest.json: c9bdf1a333e7fced570b837a9ea1c27eb42a62b1200f7309f5bc2c5aff08365e
          A/clauses/window-11/raw.json: 5f53e57ea0d5d21a872647c34b56a828235bba0fab4eb92725282686da7ac623
          A/clauses/window-11/prompt.txt: 699ec31689367b6ae0afb7211ce818db5b614d2eb297ca072298acf5ca43130a
          A/clauses/window-11/meta.json: bdec43de77649f4515c36fdef7645b3bb4f91550d41133c8fc4ff4f6156b5530
          A/clauses/window-10/raw.json: 56450d03cb1afe7532952b1dd7f3f029d845ec82fa5e351e8f72c7068ff038f7
          A/clauses/window-10/prompt.txt: 2cf0113d478f8916b176861fc44d522bcac069ab531b0060485877434a5d3502
          A/clauses/window-10/meta.json: 93f92956b27b3314c47906cb593a689ea4acd95060e110cd53005f80df2c2ad0
          A/clauses/window-03/raw.json: 315177fa305cd4b899028159b66c61566832abc361a49bf9257853ca0d845f32
          A/clauses/window-03/prompt.txt: 9648e2b1bbcbf601bff8b5a0230dea6055d6a382fd8a173d8b811468bacff05d
          A/clauses/window-03/meta.json: fbc6fd44990e79308cec305d30593749bc2b7458e6d7d6051a8c3f28aed9eaf8
          A/clauses/window-04/raw.json: fc2e94022814613dfcf056f6477fd36e4b944b0f9096fe2dda13e7fd05225f50
          A/clauses/window-04/prompt.txt: 4f7cb35c1ab24a27efc068f8643be352a0a2f9b76749cb3f8f70a4bd99e96267
          A/clauses/window-04/meta.json: 55efcd49b8cd00506590b88a43916342057aa8b53a57a76da5b772e7c9c27c8a
          A/clauses/window-05/raw.json: 54de8be79b25578238de5b0552fd08532413b6893f4edd5c209a874a5d9893e8
          A/clauses/window-05/prompt.txt: f3e4d87443262f4bfdc92f43cc009c5d40ef9ca241084aea1720c6dd25595667
          A/clauses/window-05/meta.json: 17a65fcd6d5e4e184a1543a05e8cec5763a810435f9f5c2141ab540d1f049acd
          A/clauses/window-02/raw.json: af333009af024f64a5fc7d6dff076ec99f497ee5369719b8603ccb22ff371696
          A/clauses/window-02/prompt.txt: 2609357b2542649ae5f3e66c8145404811f662945e48038f5f15ea7d194d5a76
          A/clauses/window-02/meta.json: 12c9238c3ae99072002c171c960911c6f8075a4bb61fc115f99b19ddfa20c29e
          A/clauses/window-09/raw.json: 79b840d84a523e18b1ca65c8c13671a2cc5fd98971823ae2572b3b525a12afda
          A/clauses/window-09/prompt.txt: 24d5cfdf618184f6f6164767e5b24bbeeb9534a9c02535df6e8b209ccd057a4a
          A/clauses/window-09/meta.json: 5ecf80531c5c8226beac2c22c621ed28f3d3c980920933738b056af8bc7c2ff9
          A/clauses/window-07/raw.json: 46789232ff105d5ec5bb0f4d389144108212459c9b2d26b1ca5413653677a2d7
          A/clauses/window-07/prompt.txt: f138d89007e4c5f7e554a720d89f0ba498903e9b1de088810fb7c581a9150a2a
          A/clauses/window-07/meta.json: b82a681f197661c5fab547e547d873595cbe00ed68d2438594701873b1864f62
          A/clauses/window-01/raw.json: ffe993536c43080b2b8a3bb08d6e0b637ae2fe5c6f7e76a99cd694091092d82a
          A/clauses/window-01/prompt.txt: 171a32b8575658ec87a6b4f21236dc5b0c39352e5301eab4b91fc5a4ae70778f
          A/clauses/window-01/meta.json: 8f4d9d654a81ea1703d86fd5bd37809c21ca9c1da557ce0383ebb1cc995afb46
          A/clauses/window-06/raw.json: 18b5a74a1a673e04afc66a059b62cde48a5f3d58199de7e1d1522b8df0bd86b1
          A/clauses/window-06/prompt.txt: 41237e9caa5c5a5fafe984ff33b143c8e6f181ce666648a15d8bee7ab5e7e57b
          A/clauses/window-06/meta.json: fe4bda91f365d026b69de098072f0aca044fed8dedffc8b7e3b03ca36bf6b28b
          A/clauses/window-08/raw.json: 7a3929a7356c714d1bc8a3bdf2274fc91b85e3b3626771c6e40c887b17a676de
          A/clauses/window-08/prompt.txt: 848d3da9eaf1d7b4e68da073b5986a06224a9551e6d87237e88e705057874541
          A/clauses/window-08/meta.json: 09687ac46b058527e63fcdf9dac232d0b4e5aee155acadd016d659f8f5a0e3e6
          B/passages.json: a9d21adebea7fb7507a1af2c645012e6867d0d803ad3e1b60a4f8e988a89d59f
          B/raw.json: e027f6f309754fded5da9f28514e8978931c0265f7ec520cc3d55dbc77715733
          B/source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
          B/full-source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
          B/meta.json: 8cf56ecdf687e18d5016ee7892bd177fc9de48fd58a1bb3c3bb54d29b90421bb
          B/table-images/manifest.json: c9bdf1a333e7fced570b837a9ea1c27eb42a62b1200f7309f5bc2c5aff08365e
          B/clauses/window-11/raw.json: 162548d25dcb1f35e231af6b996bfa7beeadb76bb91c6a6c491f9a6b47da7b91
          B/clauses/window-11/prompt.txt: 699ec31689367b6ae0afb7211ce818db5b614d2eb297ca072298acf5ca43130a
          B/clauses/window-11/meta.json: 1180108000d1d0198eb84d3c6269e026c70d6a42e94d7a1595a2f24134e5926f
          B/clauses/window-10/raw.json: ad091f332eadeba0fac9a6a059ae32d0957e344d87128ab458dcc9a1a94412bf
          B/clauses/window-10/prompt.txt: 2cf0113d478f8916b176861fc44d522bcac069ab531b0060485877434a5d3502
          B/clauses/window-10/meta.json: 4ba1ef5172115b0d52d885d40f9bc3335e154f3940714f36f4d409c3b2aa0c1b
          B/clauses/window-03/raw.json: b4c11ed1fef8d925942056ac15d8a0c86d8653d39fbb2a7c3f6e343e723c7a16
          B/clauses/window-03/prompt.txt: 9648e2b1bbcbf601bff8b5a0230dea6055d6a382fd8a173d8b811468bacff05d
          B/clauses/window-03/meta.json: 290d0a280360078345862da1550bfdc0a8e9ba9088d3458d62da7e1f9cd0d5c3
          B/clauses/window-04/raw.json: c3344313b1f9a8a38ab97efc7ed7f18b99190187a291c0dcc12dcaa759338541
          B/clauses/window-04/prompt.txt: 4f7cb35c1ab24a27efc068f8643be352a0a2f9b76749cb3f8f70a4bd99e96267
          B/clauses/window-04/meta.json: 95aedbc25ee37fd6b1f9eabf4597a3d78dfb52d3a9c0e7cc54f4a333557772be
          B/clauses/window-05/raw.json: f2bea05d849e66d1c57b7c1218951c1bb672ebb64470cae983e3f8cb37cc2a50
          B/clauses/window-05/prompt.txt: f3e4d87443262f4bfdc92f43cc009c5d40ef9ca241084aea1720c6dd25595667
          B/clauses/window-05/meta.json: 8e4528fe9bc418985804f66299883b31d798a2185c862684057672640c11aba9
          B/clauses/window-02/raw.json: a639defb085fc4ce6a3e9e5f2785baafd62a1063ecd234f546ca5e53aba40bfd
          B/clauses/window-02/prompt.txt: 2609357b2542649ae5f3e66c8145404811f662945e48038f5f15ea7d194d5a76
          B/clauses/window-02/meta.json: bb0232fbedb18e7b606647d0738f7cb7c3c31ccaee3edc2079c8ca12c512f457
          B/clauses/window-09/raw.json: 2e1cd054a8be405e2a7188b03fde31742c031cb659dcbb32ff7aeb8529b327b1
          B/clauses/window-09/prompt.txt: 24d5cfdf618184f6f6164767e5b24bbeeb9534a9c02535df6e8b209ccd057a4a
          B/clauses/window-09/meta.json: 797228f3b9ad7e9b6284b38179c5ac3d8b6a83df1e31e2844ff0bb2c5b820a3c
          B/clauses/window-07/raw.json: 46789232ff105d5ec5bb0f4d389144108212459c9b2d26b1ca5413653677a2d7
          B/clauses/window-07/prompt.txt: f138d89007e4c5f7e554a720d89f0ba498903e9b1de088810fb7c581a9150a2a
          B/clauses/window-07/meta.json: a061ea9b4d9e1fb04308d2ba13764269b72e987bf4580911e4b954ac237b3447
          B/clauses/window-01/raw.json: 7e56eca791ea80aa41639cc7a55b64c508157a38f49a2184f2261cf51ed3dca3
          B/clauses/window-01/prompt.txt: 171a32b8575658ec87a6b4f21236dc5b0c39352e5301eab4b91fc5a4ae70778f
          B/clauses/window-01/meta.json: 21edc778280916f565794b1c94a88e3a6f721d3bca2968a2f57f7890565250ef
          B/clauses/window-06/raw.json: 97b94dbb44bd57732d19099276bd04c482a65105dd5553d161ed81864511b936
          B/clauses/window-06/prompt.txt: 41237e9caa5c5a5fafe984ff33b143c8e6f181ce666648a15d8bee7ab5e7e57b
          B/clauses/window-06/meta.json: c4f3f79d8312d35ee3fca43e90599a995f80be9e43d18fec8b3da9844076be96
          B/clauses/window-08/raw.json: 3ad22b85c0e77efef173d42fbc4a4b31fab49b70e3f371557810689cdbf7b867
          B/clauses/window-08/prompt.txt: 848d3da9eaf1d7b4e68da073b5986a06224a9551e6d87237e88e705057874541
          B/clauses/window-08/meta.json: 98ee7762b3d04645def7bfa149ec4beaa63383dd6c4ec527bb360281b1dc7ed8
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
        pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
        source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
        source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R005
      exposure:
        text: change in the size of the right Arcuate fasciculus (AF)
      outcome:
        text: change in correct information units (CIUs)
      analysis_label: Correlation analysis
      relation: association
      evidence_ids:
      - P3-S1-C4
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
        pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
        source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
        source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Accounting without a linked unit P3-S3-C3
        - Accounting without a linked unit P3-S3-C7
        - Accounting without a linked unit P4-S1-C5
        - Accounting without a linked unit P4-S2-C13
        - Unaccounted source passage P3-S3-C7
        - Unaccounted source passage P4-S2-C13
        - Unaccounted source passage P3-S3-C3
        - Unaccounted source passage P4-S1-C5
        - Result passage disposed without unit P5-S2-C8
        - Result passage disposed without unit P6-S2-C5
        - Result passage disposed without unit P6-S2-C9
        - Result passage disposed without unit P6-S3-C1
        - Result passage disposed without unit P7-S1-C1
        unattached_null_or_qualifier_ids: []
        suppressed_nonrepresented_units: 6
        default_disposition_count_requires_completeness_check: 214
        unselected_timing_passages:
        - P1-S1-C3
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P3-S2-C9
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P3-S3-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P3-S3-C7
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S2-C12
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P2-S3-C3
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P2-S3-C5
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S1-C7
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: analysed_sample
          source_ids:
          - P2-S3-C2
          - P2-S3-C5
          - P3-S1-C2
          - P3-S2-C8
          - P3-S2-C9
          - P3-S3-C5
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          - P5-S1-C2
          - P5-S1-C5
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P3-S1-C2
          - P3-S1-C4
          - P3-S2-C9
          - P3-S3-C3
          - P3-S3-C7
          - P4-S1-C10
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - analysed_sample
        - outcome_definition
        - validation
        - analysis_restrictions
        - limitations
        - personal_factors
        - tested_personal_effects
        - adjustment_roles
        - explicitly_not_adjusted
        unclassified_extraction_ids: []
        table_review_required: []
        unlinked_tables: []
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P3-S2
          - P3-S3
          - P4-S2
          - P5-S1
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
        source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
        source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P1-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes general aphasia prevalence and categories in a cohort, not a specific relationship tested in the current study.
      - source_id: P2-S3-C6
        disposition: represented
        result_indexes:
        - 0
        reason: Qualifies the outcome of the MIT vs speech repetition therapy comparison.
      - source_id: P3-S1-C1
        disposition: represented
        result_indexes:
        - 0
        reason: Establishes the treatment effect of MIT over control for propositional speech.
      - source_id: P3-S3-C3
        disposition: represented
        result_indexes:
        - 2
        reason: Establishes increased activation in right hemisphere regions post-therapy.
      - source_id: P3-S3-C7
        disposition: represented
        result_indexes:
        - 3
        reason: Establishes treatment-induced increase in right AF.
      - source_id: P4-S1-C5
        disposition: represented
        result_indexes:
        - 3
        reason: Confirms right AF modification to support speech output.
      - source_id: P4-S2-C13
        disposition: represented
        result_indexes:
        - 3
        reason: Provides visual evidence of increased right AF size and length post-therapy.
      - source_id: P5-S2-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes the utility of slow vocalization rate as a starting point.
      - source_id: P5-S2-C8
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes baseline impairment levels of patients.
      - source_id: P6-S2-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: General summary of recovery pathways.
      - source_id: P6-S2-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: Header for behavioral and neural correlates section.
      - source_id: P6-S3-C1
        disposition: represented
        result_indexes:
        - 5
        - 6
        reason: Establishes both behavioral improvement and right fronto-temporal network engagement.
      - source_id: P6-S3-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses theoretical mechanisms of therapeutic effects.
      - source_id: P7-S1-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion about the facilitating effect of MIT.
      unresolved_coverage: []
      pending_source_ids:
      - P1-S1-C4
      - P2-S3-C6
      - P4-S1-C5
      - P5-S2-C7
      - P5-S2-C8
      - P6-S2-C5
      - P6-S2-C9
      - P6-S3-C2
      - P7-S1-C1
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review: []
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample: []
        recruited_sample:
        - P7-S1-C7
        eligibility:
        - P2-S3-C2
        - P7-S1-C8
        imaging_provenance:
        - P3-S2-C8
        - P3-S3-C5
        - P4-S2-C5
        - P4-S2-C12
        imaging_timing:
        - P3-S2-C9
        - P3-S3-C5
        - P4-S2-C6
        - P4-S2-C12
        - P5-S1-C1
        outcome_timing:
        - P3-S1-C3
        - P3-S2-C9
        - P3-S3-C3
        - P3-S3-C7
        - P4-S2-C6
        - P4-S2-C12
        - P5-S1-C1
        outcome_definition: []
        validation: []
        analysis_restrictions: []
        dependent_variable_statement:
        - P3-S1-C2
        - P3-S1-C4
        - P5-S1-C1
        limitations: []
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles: []
        explicitly_not_adjusted: []
        descriptive_personal_factors:
        - P1-S1-C3
        - P1-S1-C4
        - P2-S3-C2
        - P2-S3-C5
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: internal_cross_validation
      held_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P2-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P2-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P7-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: analysed_sample
        source_ids:
        - P2-S3-C2
        - P2-S3-C5
        - P3-S1-C2
        - P3-S2-C8
        - P3-S2-C9
        - P3-S3-C5
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C12
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P3-S1-C2
        - P3-S1-C4
        - P3-S2-C9
        - P3-S3-C3
        - P3-S3-C7
        - P4-S1-C10
        - P4-S2-C6
        - P4-S2-C12
        - P5-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
        review_sha256: 741d05e3f74dbf84e5c01981ace6df8a56c133df03ce7b972a1edc80529c0bd5
        code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
        source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
        converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
        table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
        mapper_budget: 2500
        reviewer_budget: 1600
        approved: false
        visual:
          models:
          - gemma4:31b
          - qwen3.8:27b
          digests:
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
      approved: false
      core_review:
        own_result_source_ids:
        - P3-S1-C4
        source_result: The change in correct information units (CIUs) showed a strong trend for a correlation (p = 0.08) with the change in the size of the right arcuate fasciculus (AF).
        result_status: detected_only_at_relaxed_threshold
        patient_measurement: template_lesion_overlap
        checks:
          analysis_identity:
            answer: fits
            reason: The source P3-S1-C4 explicitly describes a correlation analysis between the change in CIUs and the change in the size of the right AF. The proposed core correctly identifies this as a correlational relationship between these two specific variables.
            source_ids:
            - P3-S1-C4
          direction:
            answer: fits
            reason: The source states there was a 'strong trend for a correlation' with p=0.08. The proposed core uses the direction 'likely' and includes the qualification 'strong trend for a correlation' with the specific p-value. This accurately reflects the non-significant but suggestive nature of the finding without overstating it as a definitive significant association.
            source_ids:
            - P3-S1-C4
          construct:
            answer: fits
            reason: The exposure is correctly identified as the change in the size of the right AF. The outcome is correctly identified as the change in CIUs. The patient measurement is classified as template_lesion_overlap because the 'size' of the AF in this context (Schlaug et al.) refers to the overlap of patient lesions with the reference tract map, not a direct volumetric measurement of the tract itself in every patient, nor is it a diffusion metric measured in the patient (patient_diffusion). The source P3-S3-C6 describes the AF as a fiber tract, and the context of 'change in size' in aphasia recovery literature typically refers to lesion overlap or tract integrity proxies derived from lesion mapping.
            source_ids:
            - P3-S1-C4
            - P3-S3-C6
          qualifications:
            answer: fits
            reason: The proposed core includes the qualification 'described as a strong trend for a correlation with p = 0.08'. This is a material qualifier that prevents the misinterpretation of the result as a statistically significant finding at the conventional 0.05 threshold. The source explicitly uses the phrase 'strong trend' and provides the p-value.
            source_ids:
            - P3-S1-C4
          missing_material_caveat:
            answer: fits
            reason: The core captures the essential caveat that the result is a trend (p=0.08) rather than a significant correlation. No other material caveats regarding the specific analysis (e.g., sample size, specific statistical test details) are omitted that would change the interpretation of this specific relationship. The 'not_transcribed' limitation in the proposed core is acceptable as an optional pending item for detailed statistics, not a missing material caveat for the qualitative relationship.
            source_ids:
            - P3-S1-C4
        optional_pending:
        - Exact statistical test used (e.g., Pearson vs Spearman)
        - Sample size for this specific correlation
        - Specific definition of 'size' of AF (e.g., lesion overlap percentage vs tract volume)
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      - Exact statistical test used (e.g., Pearson vs Spearman)
      - Sample size for this specific correlation
      - Specific definition of 'size' of AF (e.g., lesion overlap percentage vs tract volume)
      normalizations: []
      analysis_identity:
        id: R005
        exposure:
          text: change in the size of the right Arcuate fasciculus (AF)
        outcome:
          text: change in correct information units (CIUs)
        analysis_label: Correlation analysis
        relation: association
        evidence_ids:
        - P3-S1-C4
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
          pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
          source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: right_arcuate_fasciculus_size_change
    name: right arcuate fasciculus size change
    kind: predictor
    findings:
    - id: f1
      target: correct_information_units
      target_kind: impairment
      claim: The change in correct information units (CIUs) showed a strong trend for a correlation with the change in the size of the right arcuate fasciculus (AF).
      direction: likely
      relationship: correlational
      method: LSM
      sample:
        n: not_reported
        population: patients with nonfluent aphasia
        phase: not_reported
        time_post_onset: post- versus pre-therapy
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - not_transcribed
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: change in the size of the right arcuate fasciculus measured via imaging. described as a ''strong trend for a correlation'' with p = 0.08. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - not_transcribed:sample.n
        - proposed_concept:correct_information_units
      therapy:
        id: mit
        name: Melodic Intonation Therapy
      citation: '@Schlaug2010'
      source_passages:
      - section: Original source P3-S1-C4
        page: 3
        quote: "The change in CIUs \nshowed a strong trend for a correlation (p = 0.08) \nwith the change in the size of the right arcu­\nate fasciculus (AF), a fiber bundle connecting \ntemporal and frontal brain regions [25]."
        supports: claim
      - section: Original source P2-S3-C2
        page: 2
        quote: "Since the initial account of its successful use \nin three chronic, nonfluent ���������������\n(Broca’s) apha­\nsic patients [34], reports have outlined a ����\ncom­\nprehensive program of MIT [35–38] including \nstrict patient selection criteria [37,38] and data \nthat demon­strated significant improvement on \nthe Boston Diagnostic Aphasia Examination \n(BDAE) [39] after treatment [40,41]."
        supports: sample
      - section: Original source P3-S1-C3
        page: 3
        quote: "In post- versus pre-therapy comparisons, \nthe behavioral improvement was highly signifi­\ncant when compared with baseline variations in \nrepeated test assessments."
        supports: method
    predictor_type: imaging_metric
    short_definition: change in the size of the right arcuate fasciculus measured via imaging
    assessment: []
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-25'
    relationship_review:
      paper: Schlaug2010
      proposal_id: R005
      review_status_sha256: 741d05e3f74dbf84e5c01981ace6df8a56c133df03ce7b972a1edc80529c0bd5
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
        original_review_binding:
          version: relationship-review-v4
          input_hashes:
            pdf: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
            A/passages.json: a9d21adebea7fb7507a1af2c645012e6867d0d803ad3e1b60a4f8e988a89d59f
            A/raw.json: 1faaf23be366c6d48844bd49cec2917a48fbd88d7d54b9744f9a81f78e50efce
            A/source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
            A/full-source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
            A/meta.json: e3373fc5ad045b3522c07d04658dc8e5fac0a59136b791d8a1faffdb727ba081
            A/table-images/manifest.json: c9bdf1a333e7fced570b837a9ea1c27eb42a62b1200f7309f5bc2c5aff08365e
            A/clauses/window-11/raw.json: 5f53e57ea0d5d21a872647c34b56a828235bba0fab4eb92725282686da7ac623
            A/clauses/window-11/prompt.txt: 699ec31689367b6ae0afb7211ce818db5b614d2eb297ca072298acf5ca43130a
            A/clauses/window-11/meta.json: bdec43de77649f4515c36fdef7645b3bb4f91550d41133c8fc4ff4f6156b5530
            A/clauses/window-10/raw.json: 56450d03cb1afe7532952b1dd7f3f029d845ec82fa5e351e8f72c7068ff038f7
            A/clauses/window-10/prompt.txt: 2cf0113d478f8916b176861fc44d522bcac069ab531b0060485877434a5d3502
            A/clauses/window-10/meta.json: 93f92956b27b3314c47906cb593a689ea4acd95060e110cd53005f80df2c2ad0
            A/clauses/window-03/raw.json: 315177fa305cd4b899028159b66c61566832abc361a49bf9257853ca0d845f32
            A/clauses/window-03/prompt.txt: 9648e2b1bbcbf601bff8b5a0230dea6055d6a382fd8a173d8b811468bacff05d
            A/clauses/window-03/meta.json: fbc6fd44990e79308cec305d30593749bc2b7458e6d7d6051a8c3f28aed9eaf8
            A/clauses/window-04/raw.json: fc2e94022814613dfcf056f6477fd36e4b944b0f9096fe2dda13e7fd05225f50
            A/clauses/window-04/prompt.txt: 4f7cb35c1ab24a27efc068f8643be352a0a2f9b76749cb3f8f70a4bd99e96267
            A/clauses/window-04/meta.json: 55efcd49b8cd00506590b88a43916342057aa8b53a57a76da5b772e7c9c27c8a
            A/clauses/window-05/raw.json: 54de8be79b25578238de5b0552fd08532413b6893f4edd5c209a874a5d9893e8
            A/clauses/window-05/prompt.txt: f3e4d87443262f4bfdc92f43cc009c5d40ef9ca241084aea1720c6dd25595667
            A/clauses/window-05/meta.json: 17a65fcd6d5e4e184a1543a05e8cec5763a810435f9f5c2141ab540d1f049acd
            A/clauses/window-02/raw.json: af333009af024f64a5fc7d6dff076ec99f497ee5369719b8603ccb22ff371696
            A/clauses/window-02/prompt.txt: 2609357b2542649ae5f3e66c8145404811f662945e48038f5f15ea7d194d5a76
            A/clauses/window-02/meta.json: 12c9238c3ae99072002c171c960911c6f8075a4bb61fc115f99b19ddfa20c29e
            A/clauses/window-09/raw.json: 79b840d84a523e18b1ca65c8c13671a2cc5fd98971823ae2572b3b525a12afda
            A/clauses/window-09/prompt.txt: 24d5cfdf618184f6f6164767e5b24bbeeb9534a9c02535df6e8b209ccd057a4a
            A/clauses/window-09/meta.json: 5ecf80531c5c8226beac2c22c621ed28f3d3c980920933738b056af8bc7c2ff9
            A/clauses/window-07/raw.json: 46789232ff105d5ec5bb0f4d389144108212459c9b2d26b1ca5413653677a2d7
            A/clauses/window-07/prompt.txt: f138d89007e4c5f7e554a720d89f0ba498903e9b1de088810fb7c581a9150a2a
            A/clauses/window-07/meta.json: b82a681f197661c5fab547e547d873595cbe00ed68d2438594701873b1864f62
            A/clauses/window-01/raw.json: ffe993536c43080b2b8a3bb08d6e0b637ae2fe5c6f7e76a99cd694091092d82a
            A/clauses/window-01/prompt.txt: 171a32b8575658ec87a6b4f21236dc5b0c39352e5301eab4b91fc5a4ae70778f
            A/clauses/window-01/meta.json: 8f4d9d654a81ea1703d86fd5bd37809c21ca9c1da557ce0383ebb1cc995afb46
            A/clauses/window-06/raw.json: 18b5a74a1a673e04afc66a059b62cde48a5f3d58199de7e1d1522b8df0bd86b1
            A/clauses/window-06/prompt.txt: 41237e9caa5c5a5fafe984ff33b143c8e6f181ce666648a15d8bee7ab5e7e57b
            A/clauses/window-06/meta.json: fe4bda91f365d026b69de098072f0aca044fed8dedffc8b7e3b03ca36bf6b28b
            A/clauses/window-08/raw.json: 7a3929a7356c714d1bc8a3bdf2274fc91b85e3b3626771c6e40c887b17a676de
            A/clauses/window-08/prompt.txt: 848d3da9eaf1d7b4e68da073b5986a06224a9551e6d87237e88e705057874541
            A/clauses/window-08/meta.json: 09687ac46b058527e63fcdf9dac232d0b4e5aee155acadd016d659f8f5a0e3e6
            B/passages.json: a9d21adebea7fb7507a1af2c645012e6867d0d803ad3e1b60a4f8e988a89d59f
            B/raw.json: e027f6f309754fded5da9f28514e8978931c0265f7ec520cc3d55dbc77715733
            B/source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
            B/full-source-units.json: 8437af011c1522bc4379e3cbe5d07d353644b3acd77fc1cc3a580ebfeba3a06d
            B/meta.json: 8cf56ecdf687e18d5016ee7892bd177fc9de48fd58a1bb3c3bb54d29b90421bb
            B/table-images/manifest.json: c9bdf1a333e7fced570b837a9ea1c27eb42a62b1200f7309f5bc2c5aff08365e
            B/clauses/window-11/raw.json: 162548d25dcb1f35e231af6b996bfa7beeadb76bb91c6a6c491f9a6b47da7b91
            B/clauses/window-11/prompt.txt: 699ec31689367b6ae0afb7211ce818db5b614d2eb297ca072298acf5ca43130a
            B/clauses/window-11/meta.json: 1180108000d1d0198eb84d3c6269e026c70d6a42e94d7a1595a2f24134e5926f
            B/clauses/window-10/raw.json: ad091f332eadeba0fac9a6a059ae32d0957e344d87128ab458dcc9a1a94412bf
            B/clauses/window-10/prompt.txt: 2cf0113d478f8916b176861fc44d522bcac069ab531b0060485877434a5d3502
            B/clauses/window-10/meta.json: 4ba1ef5172115b0d52d885d40f9bc3335e154f3940714f36f4d409c3b2aa0c1b
            B/clauses/window-03/raw.json: b4c11ed1fef8d925942056ac15d8a0c86d8653d39fbb2a7c3f6e343e723c7a16
            B/clauses/window-03/prompt.txt: 9648e2b1bbcbf601bff8b5a0230dea6055d6a382fd8a173d8b811468bacff05d
            B/clauses/window-03/meta.json: 290d0a280360078345862da1550bfdc0a8e9ba9088d3458d62da7e1f9cd0d5c3
            B/clauses/window-04/raw.json: c3344313b1f9a8a38ab97efc7ed7f18b99190187a291c0dcc12dcaa759338541
            B/clauses/window-04/prompt.txt: 4f7cb35c1ab24a27efc068f8643be352a0a2f9b76749cb3f8f70a4bd99e96267
            B/clauses/window-04/meta.json: 95aedbc25ee37fd6b1f9eabf4597a3d78dfb52d3a9c0e7cc54f4a333557772be
            B/clauses/window-05/raw.json: f2bea05d849e66d1c57b7c1218951c1bb672ebb64470cae983e3f8cb37cc2a50
            B/clauses/window-05/prompt.txt: f3e4d87443262f4bfdc92f43cc009c5d40ef9ca241084aea1720c6dd25595667
            B/clauses/window-05/meta.json: 8e4528fe9bc418985804f66299883b31d798a2185c862684057672640c11aba9
            B/clauses/window-02/raw.json: a639defb085fc4ce6a3e9e5f2785baafd62a1063ecd234f546ca5e53aba40bfd
            B/clauses/window-02/prompt.txt: 2609357b2542649ae5f3e66c8145404811f662945e48038f5f15ea7d194d5a76
            B/clauses/window-02/meta.json: bb0232fbedb18e7b606647d0738f7cb7c3c31ccaee3edc2079c8ca12c512f457
            B/clauses/window-09/raw.json: 2e1cd054a8be405e2a7188b03fde31742c031cb659dcbb32ff7aeb8529b327b1
            B/clauses/window-09/prompt.txt: 24d5cfdf618184f6f6164767e5b24bbeeb9534a9c02535df6e8b209ccd057a4a
            B/clauses/window-09/meta.json: 797228f3b9ad7e9b6284b38179c5ac3d8b6a83df1e31e2844ff0bb2c5b820a3c
            B/clauses/window-07/raw.json: 46789232ff105d5ec5bb0f4d389144108212459c9b2d26b1ca5413653677a2d7
            B/clauses/window-07/prompt.txt: f138d89007e4c5f7e554a720d89f0ba498903e9b1de088810fb7c581a9150a2a
            B/clauses/window-07/meta.json: a061ea9b4d9e1fb04308d2ba13764269b72e987bf4580911e4b954ac237b3447
            B/clauses/window-01/raw.json: 7e56eca791ea80aa41639cc7a55b64c508157a38f49a2184f2261cf51ed3dca3
            B/clauses/window-01/prompt.txt: 171a32b8575658ec87a6b4f21236dc5b0c39352e5301eab4b91fc5a4ae70778f
            B/clauses/window-01/meta.json: 21edc778280916f565794b1c94a88e3a6f721d3bca2968a2f57f7890565250ef
            B/clauses/window-06/raw.json: 97b94dbb44bd57732d19099276bd04c482a65105dd5553d161ed81864511b936
            B/clauses/window-06/prompt.txt: 41237e9caa5c5a5fafe984ff33b143c8e6f181ce666648a15d8bee7ab5e7e57b
            B/clauses/window-06/meta.json: c4f3f79d8312d35ee3fca43e90599a995f80be9e43d18fec8b3da9844076be96
            B/clauses/window-08/raw.json: 3ad22b85c0e77efef173d42fbc4a4b31fab49b70e3f371557810689cdbf7b867
            B/clauses/window-08/prompt.txt: 848d3da9eaf1d7b4e68da073b5986a06224a9551e6d87237e88e705057874541
            B/clauses/window-08/meta.json: 98ee7762b3d04645def7bfa149ec4beaa63383dd6c4ec527bb360281b1dc7ed8
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
          pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
          source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R005
        exposure:
          text: change in the size of the right Arcuate fasciculus (AF)
        outcome:
          text: change in correct information units (CIUs)
        analysis_label: Correlation analysis
        relation: association
        evidence_ids:
        - P3-S1-C4
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
          pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
          source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Accounting without a linked unit P3-S3-C3
          - Accounting without a linked unit P3-S3-C7
          - Accounting without a linked unit P4-S1-C5
          - Accounting without a linked unit P4-S2-C13
          - Unaccounted source passage P3-S3-C7
          - Unaccounted source passage P4-S2-C13
          - Unaccounted source passage P3-S3-C3
          - Unaccounted source passage P4-S1-C5
          - Result passage disposed without unit P5-S2-C8
          - Result passage disposed without unit P6-S2-C5
          - Result passage disposed without unit P6-S2-C9
          - Result passage disposed without unit P6-S3-C1
          - Result passage disposed without unit P7-S1-C1
          unattached_null_or_qualifier_ids: []
          suppressed_nonrepresented_units: 6
          default_disposition_count_requires_completeness_check: 214
          unselected_timing_passages:
          - P1-S1-C3
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P3-S2-C9
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P3-S3-C3
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P3-S3-C7
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P4-S2-C6
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P4-S2-C12
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: validation
            source_id: P2-S3-C3
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P2-S3-C5
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P7-S1-C7
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: analysed_sample
            source_ids:
            - P2-S3-C2
            - P2-S3-C5
            - P3-S1-C2
            - P3-S2-C8
            - P3-S2-C9
            - P3-S3-C5
            - P4-S2-C5
            - P4-S2-C6
            - P4-S2-C12
            - P5-S1-C1
            - P5-S1-C2
            - P5-S1-C5
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: outcome_definition
            source_ids:
            - P3-S1-C2
            - P3-S1-C4
            - P3-S2-C9
            - P3-S3-C3
            - P3-S3-C7
            - P4-S1-C10
            - P4-S2-C6
            - P4-S2-C12
            - P5-S1-C1
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - analysed_sample
          - outcome_definition
          - validation
          - analysis_restrictions
          - limitations
          - personal_factors
          - tested_personal_effects
          - adjustment_roles
          - explicitly_not_adjusted
          unclassified_extraction_ids: []
          table_review_required: []
          unlinked_tables: []
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P3-S2
            - P3-S3
            - P4-S2
            - P5-S1
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
          source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P1-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes general aphasia prevalence and categories in a cohort, not a specific relationship tested in the current study.
        - source_id: P2-S3-C6
          disposition: represented
          result_indexes:
          - 0
          reason: Qualifies the outcome of the MIT vs speech repetition therapy comparison.
        - source_id: P3-S1-C1
          disposition: represented
          result_indexes:
          - 0
          reason: Establishes the treatment effect of MIT over control for propositional speech.
        - source_id: P3-S3-C3
          disposition: represented
          result_indexes:
          - 2
          reason: Establishes increased activation in right hemisphere regions post-therapy.
        - source_id: P3-S3-C7
          disposition: represented
          result_indexes:
          - 3
          reason: Establishes treatment-induced increase in right AF.
        - source_id: P4-S1-C5
          disposition: represented
          result_indexes:
          - 3
          reason: Confirms right AF modification to support speech output.
        - source_id: P4-S2-C13
          disposition: represented
          result_indexes:
          - 3
          reason: Provides visual evidence of increased right AF size and length post-therapy.
        - source_id: P5-S2-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes the utility of slow vocalization rate as a starting point.
        - source_id: P5-S2-C8
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes baseline impairment levels of patients.
        - source_id: P6-S2-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: General summary of recovery pathways.
        - source_id: P6-S2-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: Header for behavioral and neural correlates section.
        - source_id: P6-S3-C1
          disposition: represented
          result_indexes:
          - 5
          - 6
          reason: Establishes both behavioral improvement and right fronto-temporal network engagement.
        - source_id: P6-S3-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses theoretical mechanisms of therapeutic effects.
        - source_id: P7-S1-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion about the facilitating effect of MIT.
        unresolved_coverage: []
        pending_source_ids:
        - P1-S1-C4
        - P2-S3-C6
        - P4-S1-C5
        - P5-S2-C7
        - P5-S2-C8
        - P6-S2-C5
        - P6-S2-C9
        - P6-S3-C2
        - P7-S1-C1
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review: []
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample: []
          recruited_sample:
          - P7-S1-C7
          eligibility:
          - P2-S3-C2
          - P7-S1-C8
          imaging_provenance:
          - P3-S2-C8
          - P3-S3-C5
          - P4-S2-C5
          - P4-S2-C12
          imaging_timing:
          - P3-S2-C9
          - P3-S3-C5
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          outcome_timing:
          - P3-S1-C3
          - P3-S2-C9
          - P3-S3-C3
          - P3-S3-C7
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          outcome_definition: []
          validation: []
          analysis_restrictions: []
          dependent_variable_statement:
          - P3-S1-C2
          - P3-S1-C4
          - P5-S1-C1
          limitations: []
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles: []
          explicitly_not_adjusted: []
          descriptive_personal_factors:
          - P1-S1-C3
          - P1-S1-C4
          - P2-S3-C2
          - P2-S3-C5
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: internal_cross_validation
        held_selections:
        - slot: dependent_variable_statement
          source_id: P3-S2-C9
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P3-S3-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P3-S3-C7
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P4-S2-C12
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P2-S3-C3
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P2-S3-C5
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S1-C7
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: analysed_sample
          source_ids:
          - P2-S3-C2
          - P2-S3-C5
          - P3-S1-C2
          - P3-S2-C8
          - P3-S2-C9
          - P3-S3-C5
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          - P5-S1-C2
          - P5-S1-C5
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P3-S1-C2
          - P3-S1-C4
          - P3-S2-C9
          - P3-S3-C3
          - P3-S3-C7
          - P4-S1-C10
          - P4-S2-C6
          - P4-S2-C12
          - P5-S1-C1
          reason: Runaway selection (>8 passages); entire slot requires source review
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
          review_sha256: 741d05e3f74dbf84e5c01981ace6df8a56c133df03ce7b972a1edc80529c0bd5
          code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
          source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
          converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
          table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
          mapper_budget: 2500
          reviewer_budget: 1600
          approved: false
          visual:
            models:
            - gemma4:31b
            - qwen3.8:27b
            digests:
            - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
            code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
            layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
        approved: false
        core_review:
          own_result_source_ids:
          - P3-S1-C4
          source_result: The change in correct information units (CIUs) showed a strong trend for a correlation (p = 0.08) with the change in the size of the right arcuate fasciculus (AF).
          result_status: detected_only_at_relaxed_threshold
          patient_measurement: template_lesion_overlap
          checks:
            analysis_identity:
              answer: fits
              reason: The source P3-S1-C4 explicitly describes a correlation analysis between the change in CIUs and the change in the size of the right AF. The proposed core correctly identifies this as a correlational relationship between these two specific variables.
              source_ids:
              - P3-S1-C4
            direction:
              answer: fits
              reason: The source states there was a 'strong trend for a correlation' with p=0.08. The proposed core uses the direction 'likely' and includes the qualification 'strong trend for a correlation' with the specific p-value. This accurately reflects the non-significant but suggestive nature of the finding without overstating it as a definitive significant association.
              source_ids:
              - P3-S1-C4
            construct:
              answer: fits
              reason: The exposure is correctly identified as the change in the size of the right AF. The outcome is correctly identified as the change in CIUs. The patient measurement is classified as template_lesion_overlap because the 'size' of the AF in this context (Schlaug et al.) refers to the overlap of patient lesions with the reference tract map, not a direct volumetric measurement of the tract itself in every patient, nor is it a diffusion metric measured in the patient (patient_diffusion). The source P3-S3-C6 describes the AF as a fiber tract, and the context of 'change in size' in aphasia recovery literature typically refers to lesion overlap or tract integrity proxies derived from lesion mapping.
              source_ids:
              - P3-S1-C4
              - P3-S3-C6
            qualifications:
              answer: fits
              reason: The proposed core includes the qualification 'described as a strong trend for a correlation with p = 0.08'. This is a material qualifier that prevents the misinterpretation of the result as a statistically significant finding at the conventional 0.05 threshold. The source explicitly uses the phrase 'strong trend' and provides the p-value.
              source_ids:
              - P3-S1-C4
            missing_material_caveat:
              answer: fits
              reason: The core captures the essential caveat that the result is a trend (p=0.08) rather than a significant correlation. No other material caveats regarding the specific analysis (e.g., sample size, specific statistical test details) are omitted that would change the interpretation of this specific relationship. The 'not_transcribed' limitation in the proposed core is acceptable as an optional pending item for detailed statistics, not a missing material caveat for the qualitative relationship.
              source_ids:
              - P3-S1-C4
          optional_pending:
          - Exact statistical test used (e.g., Pearson vs Spearman)
          - Sample size for this specific correlation
          - Specific definition of 'size' of AF (e.g., lesion overlap percentage vs tract volume)
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        - Exact statistical test used (e.g., Pearson vs Spearman)
        - Sample size for this specific correlation
        - Specific definition of 'size' of AF (e.g., lesion overlap percentage vs tract volume)
        normalizations: []
        analysis_identity:
          id: R005
          exposure:
            text: change in the size of the right Arcuate fasciculus (AF)
          outcome:
            text: change in correct information units (CIUs)
          analysis_label: Correlation analysis
          relation: association
          evidence_ids:
          - P3-S1-C4
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
            pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
            source_review: _compare/relationships-2026-11-16/review-current/Schlaug2010
            source_status_sha256: 8eeb8a71b9cab0cfe335540e684fdb9d6834c2c1410959ef20e210926830025b
            code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
            version: candidate-inventory-v1
        paper_complete: false
        visual_prose_readings: {}
        remaining:
        - Human PDF review and approval
        - Pending metadata enrichment
        - Main Results, figures and tables completeness check
    reviewer_marks:
    - id: relationship-source-check
      page: 3
      quote: "The change in CIUs \nshowed a strong trend for a correlation (p = 0.08) \nwith the change in the size of the right arcu­\nate fasciculus (AF), a fiber bundle connecting \ntemporal and frontal brain regions [25]."
      status: pending
      by: agent:relationship-converter
      date: '2026-11-25'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The source describes a correlation between the change in the size of the right arcuate fasciculus and the change in correct information units (CIUs) following Melodic Intonation Therapy (MIT).
    bucket: predictors
    entity_id: right_arcuate_fasciculus_size_change
    name: right arcuate fasciculus size change
    kind: predictor
    predictor_type: imaging_metric
    definition: change in the size of the right arcuate fasciculus measured via imaging
    assessment: []
    target: correct_information_units
    target_kind: impairment
    claim: The change in correct information units (CIUs) showed a strong trend for a correlation with the change in the size of the right arcuate fasciculus (AF).
    direction: likely
    method: LSM
    relationship: correlational
    therapy:
      id: mit
      name: Melodic Intonation Therapy
    sample_n: null
    population: patients with nonfluent aphasia
    timing: post- versus pre-therapy
    qualifications:
    - described as a 'strong trend for a correlation' with p = 0.08
    limitations:
    - not_transcribed
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P3-S1-C4
      supports: claim
    - source_id: P2-S3-C2
      supports: sample
    - source_id: P3-S1-C3
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
      review_sha256: 741d05e3f74dbf84e5c01981ace6df8a56c133df03ce7b972a1edc80529c0bd5
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    proposal: R005
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/predictors/right_arcuate_fasciculus_size_change__Schlaug2010__R005.md
    seconds_this_run: 66.50102624998544
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c2875f9550c0069f21ac179c72aba6a02033f9f16c6a9ae3f08a6abeeadc9d56
      original_mapping_sha256: e2892f6e39e0365a4e0b7cdea0e4cf30fefbdd01843455727c2d66e7a825f308
      original_status_sha256: c87d89edfaef1f7c54d7e95f012a63a8db9287aac9225d099192700919e7f8ae
      evidence_sha256: 49ba7694f96fd419902fce527a93504aefa8b02a05eee416d7d5a889e26cb83d
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 3
      - 8
      note: Reconciled the source identity to reference 25 (Schlaug et al. 2009). Retained one attributed secondary account and the non-significant p=.08 trend; the parallel Plowman2012 R019 account remains excluded to avoid duplication. Human source review remains pending.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "The change in CIUs \nshowed a strong trend for a correlation (p = 0.08) \nwith the change in the size of the right arcu­\nate fasciculus (AF), a fiber bundle connecting \ntemporal and frontal brain regions [25]."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reconciled the source identity to reference 25 (Schlaug et al. 2009). Retained one attributed secondary account and the non-significant p=.08 trend; the parallel Plowman2012 R019 account remains excluded to avoid duplication. Human source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
