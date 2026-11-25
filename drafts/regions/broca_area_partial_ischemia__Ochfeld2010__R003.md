---
id: broca_area_partial_ischemia
name: Broca area partial ischemia cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: broca_global_aphasia
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: broca_global_aphasia
  target_kind: impairment
  claim: In a longitudinal subset of patients, ischemia involving any part of Broca
    area was significantly associated with Broca or global aphasia in the acute phase,
    but this association was not significant in the chronic phase.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 20
    population: Right-hand-dominant native English speakers with left hemisphere ischemic
      stroke
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and
      timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Limitations of WAB-R classification
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Presence of infarct or hypoperfusion involving any
    part of Broca area (defined as Brodmann areas 44 and/or 45 using a probabilistic
    cytoarchitectural map), measured via DWI, T2, or PWI (time-to-peak delay >= 4
    seconds). The finding refers specifically to the longitudinal subset of patients
    studied at both time points. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S3-C7, two-model
    agreement, human verification pending): . A subset of 20

    patients was studied at both time periods Original text-layer quotation is preserved
    below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:broca_global_aphasia
  citation: '@Ochfeld2010'
  source_passages:
  - section: Original source P3-S1-C5
    page: 3
    quote: "In the 20 patients studied longitudinally, the association\nbetween ischemia\
      \ involving part of Broca area and Broca or\nglobal aphasia was significant\
      \ only acutely (\x012\x0320; df1;\nP\x010.0001), not chronically (\x012\x03\
      0; df1; p\x031; not signifi-\ncant)."
    supports: claim
  - section: Original source P2-S2-C10
    page: 2
    quote: "Images were analyzed by\ntechnicians blinded to the language data and\
      \ aphasia classification\nfor the presence of dense ischemia (bright on DWI,\
      \ dark on\napparent diffusion coefficient \x04ADC\x05) in the acute stage or\
      \ infarct\n(on T2 in the chronic stage) or hypoperfusion (on time-to-peak\n\
      maps derived from PWI) involving Broca area, with Broca area\ndefined as Brodmann\
      \ area 44 and/or 45 using a probabilistic\ncytoarchitectural map.6 Time-to-peak\
      \ maps were registered to T2\nimages, which have better spatial resolution,\
      \ to provide anatomic\nlandmarks."
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: "Each patient’s scans were classified according to the\npresence or absence\
      \ of ischemia (on DWI) or infarct (on T2) or\nhypoperfusion, defined as \x02\
      4-second delay in time to peak\nrelative to the homologous region in the right\
      \ hemisphere in any\npart of Broca area or covering the entire region of Broca\
      \ area."
    supports: method
  - section: Original source P2-S3-C7
    page: 2
    quote: 'A subset of 20

      patients was studied at both time periods.'
    supports: sample
  - section: Original source P2-S1-C5
    page: 2
    quote: "Subjects and Methods\nParticipants\nWe included consecutive patients who\
      \ were right-hand-dominant\nwith left hemisphere ischemic stroke (\x0148 hours\
      \ from onset of\nsymptoms or \x026 months after stroke) and native speakers\
      \ of\nEnglish."
    supports: sample
  - section: Original source P5-S2-C2
    page: 5
    quote: 'Conclusion

      Recognizing the limitations of WAB-R classification and the

      relatively small sample size of our study, our results chal-

      lenge the commonly held belief that acute aphasia does not

      reflect classic lesion–deficit associations, at least when “le-

      sion” is defined as ischemic tissue that can be visualized with

      PWI.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Ochfeld2010
  proposal_id: R003
  review_status_sha256: ed686033df44a21d2542e9d61743b822dac16028dd5f5baa30922f1401819846
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
        A/passages.json: fcff0b5233013379fcf419eba431d32cffba8b6f59196d100afef49dd0975d51
        A/raw.json: 9fcc8d52f715e9b7053fe2868ac888fec1df2e3d35f57354d63e1bdef4cda32a
        A/source-units.json: 140b7da7ae2dc5016800300a3dc6d8705df9a2acb820f86a4bbac903ff2df39c
        A/full-source-units.json: 7b92d0bdb6c0b7ad3795633e07fae4f2f95afc1e5d9082db5fbc846c55d25556
        A/meta.json: f37bacb275373a8ed24172c5f3d155ea91d1e04f5ec917d9c1f72a16bca719ae
        A/table-images/manifest.json: bb05902b4eb450d3d8ad7aa1d618f9be383f6698036a2d6058db1cf1939dd8e1
        A/clauses/window-03/raw.json: 6e176860f7f6ad58659ce4c53c7f3e9043695532febac9f6f835be77571584bc
        A/clauses/window-03/prompt.txt: 3b7412cfd66aa142c919010e8145e817cd734e5d1d3b857e87dabbb896784fa1
        A/clauses/window-03/meta.json: ea751bd0deed4b94aa53f4e017ebeee501f00663edfad0d91fdf7c2587239081
        A/clauses/window-04/raw.json: 261ee197ce754340752b269a7bc0685d603c2275e5aac517a348000c6cb58107
        A/clauses/window-04/prompt.txt: 7cbbbb2988fd58b91c7d6e0524da172a284c623be317f54ca37c12316026e360
        A/clauses/window-04/meta.json: 0015c1339f8a98bc6c24d2399dba3fd68e4943a224a2698e5de5efece0954d4b
        A/clauses/window-02/raw.json: 4f2fdef263e7503d65224c3c4eab28003e027dc86e96057fa0006a0b56c02f2b
        A/clauses/window-02/prompt.txt: 8022a2cab874d34d9c504fdbc1154a71b2c49d2d716636ce2ca37589c9ea7ab3
        A/clauses/window-02/meta.json: 4c5a10ccaf5a2c2edc4687192a76a532e4f3a2d180d20e98bcfcfd3be5dcf034
        A/clauses/window-01/raw.json: 60bdd895a4eedffb50d63f6f281922c71465dd515d0eaf93677453fe9f9556de
        A/clauses/window-01/prompt.txt: eb8890845567c1ed882057eda73ea4b7d55a42af46ffe1c73be6e4386253ff1d
        A/clauses/window-01/meta.json: 692f29323b9cd037581e2211689658d701956281bb7f6123ddeaff891f074433
        B/passages.json: fcff0b5233013379fcf419eba431d32cffba8b6f59196d100afef49dd0975d51
        B/raw.json: 8f968cb7b3ba90979b7756987729c846a571d94771586c6157f0e195a1310b2f
        B/source-units.json: 140b7da7ae2dc5016800300a3dc6d8705df9a2acb820f86a4bbac903ff2df39c
        B/full-source-units.json: 7b92d0bdb6c0b7ad3795633e07fae4f2f95afc1e5d9082db5fbc846c55d25556
        B/meta.json: 65e298c513180ac65c56dba0c6381e90366321a626bebcaf2d3d36bf60cdd611
        B/table-images/manifest.json: bb05902b4eb450d3d8ad7aa1d618f9be383f6698036a2d6058db1cf1939dd8e1
        B/clauses/window-03/raw.json: c8092c1d930190b0822366de3e0d0af822b3dcfa7d27822ca1e8acd146167089
        B/clauses/window-03/prompt.txt: 3b7412cfd66aa142c919010e8145e817cd734e5d1d3b857e87dabbb896784fa1
        B/clauses/window-03/meta.json: 9aa0d2e81ff65fea1e7e31e05b445cf42886c0e5f59202dd6ce38c90190c3c2b
        B/clauses/window-04/raw.json: b030519e0564bd5deb94c6f49acdbdcf57543ec2fef972bf710945a505243681
        B/clauses/window-04/prompt.txt: 7cbbbb2988fd58b91c7d6e0524da172a284c623be317f54ca37c12316026e360
        B/clauses/window-04/meta.json: a9e17d77135a0338496aee330068a15706a57311818421de31dacccd39f1fee3
        B/clauses/window-02/raw.json: c644032e41aeecd67625644b724e2be7a7001afa85ff4f5fb0802b9194bd3de7
        B/clauses/window-02/prompt.txt: 8022a2cab874d34d9c504fdbc1154a71b2c49d2d716636ce2ca37589c9ea7ab3
        B/clauses/window-02/meta.json: 055c1fcb04da7bfb401a02ed274499fff0e4039eb751f045585fdd905e5a5e4b
        B/clauses/window-01/raw.json: ab2722330b25b6abf075029109f56fb1a67d2d7cfdb4e4f07a68ebf7d0be9859
        B/clauses/window-01/prompt.txt: eb8890845567c1ed882057eda73ea4b7d55a42af46ffe1c73be6e4386253ff1d
        B/clauses/window-01/meta.json: 37a0435ef9db45c677bb4a4bed4357272f9cfd6599a024e0d7629d78a11f026e
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
      pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
      source_review: _compare/relationships-2026-11-16/review-current/Ochfeld2010
      source_status_sha256: 6de4ab559ccb583c775b6655c18d31ff56495486243bcdb5e55bd46d25b2f121
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: ischemia involving part of Broca area
    outcome:
      text: Broca or global aphasia
    analysis_label: Longitudinal association of Broca area ischemia (any part) with
      Broca/global aphasia
    relation: association
    evidence_ids:
    - P1-S1-C8
    - P3-S1-C5
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
      pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
      source_review: _compare/relationships-2026-11-16/review-current/Ochfeld2010
      source_status_sha256: 6de4ab559ccb583c775b6655c18d31ff56495486243bcdb5e55bd46d25b2f121
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P2-S3-C13
      - Result passage disposed without unit P2-S3-C14
      - Result passage disposed without unit P2-S3-C16
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P2-S4-C3
      - Result passage disposed without unit P2-S4-C4
      - Result passage disposed without unit P2-S4-C5
      - Result passage disposed without unit P3-S1-C1
      - Result passage disposed without unit P3-S1-C2
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S1-C4
      - Accounting without a linked unit P3-S1-C5
      - Unaccounted source passage P3-S1-C5
      - Result passage disposed without unit P3-S2-C5
      - Result passage disposed without unit P3-S2-C8
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Result passage disposed without unit P4-S1-C9
      - Unaccounted source passage P4-S1-C7
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C12
      unattached_null_or_qualifier_ids:
      - P2-S4-C4
      - P3-S1-C2
      - P3-S1-C5
      - P4-S1-C5
      - P4-S2-C2
      - P5-S1-C11
      - P5-S2-C2
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 68
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S1-C5
      - P2-S2-C4
      - P2-S3-C6
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C15
      - P4-S1-C12
      - P5-S1-C2
      - P5-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
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
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
      source_review: _compare/relationships-2026-11-16/review-current/Ochfeld2010
      source_status_sha256: 6de4ab559ccb583c775b6655c18d31ff56495486243bcdb5e55bd46d25b2f121
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports association of any part of Broca area infarct with aphasia in
        acute vs chronic stroke.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports association of all of Broca area infarct with aphasia in acute
        vs chronic stroke.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Reports longitudinal associations for both part and all of Broca area.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement summarizing results.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of chronic patients.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of resolution over time.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of aphasia severity.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia quotient means.
    - source_id: P2-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia quotient for longitudinal subset.
    - source_id: P2-S4-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports association of any part of Broca area infarct with aphasia in
        acute vs chronic stroke.
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of acute patients.
    - source_id: P2-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of one chronic patient.
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive percentage of patients.
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive percentage of patients.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of acute patients.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive classification of specific patients.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of other acute patients.
    - source_id: P3-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Reports longitudinal association for part of Broca area.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of longitudinal subset.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports association of all of Broca area infarct with aphasia in acute
        vs chronic stroke.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of acute patients.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of chronic patients.
    - source_id: P3-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Reports longitudinal association for all of Broca area.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive counts of infarcts.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of perfusion defects.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports association of Broca and Wernicke infarct with global aphasia.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Reports association of Broca and Wernicke infarct with Broca aphasia.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of recovery.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of speech.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of exceptions.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of chronic patients.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of results.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of chronic patients.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of reorganization.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P4-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of motor speech disorder.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure caption reference.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports association of Broca and Wernicke infarct with global aphasia.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of WAB-R classification.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of repetition scores.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement.
    unresolved_coverage:
    - source_id: P4-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P3-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P3-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P3-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P3-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P3-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P3-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C11
    - P2-S3-C8
    - P2-S3-C13
    - P2-S3-C14
    - P2-S3-C16
    - P2-S4-C3
    - P2-S4-C4
    - P2-S4-C5
    - P3-S1-C1
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C6
    - P3-S1-C8
    - P3-S1-C9
    - P3-S1-C11
    - P3-S1-C12
    - P3-S2-C2
    - P3-S2-C4
    - P3-S2-C5
    - P3-S2-C6
    - P3-S2-C8
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C9
    - P4-S1-C11
    - P4-S1-C14
    - P4-S2-C2
    - P4-S2-C8
    - P5-S1-C1
    - P5-S1-C11
    - P5-S1-C12
    - P5-S2-C2
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
      - P2-S3-C6
      - P2-S3-C7
      recruited_sample:
      - P2-S1-C5
      - P2-S2-C4
      - P2-S2-C5
      eligibility:
      - P2-S1-C5
      - P2-S2-C2
      imaging_provenance:
      - P2-S2-C10
      imaging_timing:
      - P2-S2-C11
      outcome_timing:
      - P2-S2-C3
      outcome_definition:
      - P2-S3-C3
      - P2-S3-C4
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S3-C3
      limitations:
      - P5-S2-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C15
      - P5-S1-C2
      - P5-S1-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: repeated_patients
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
      pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
      review_sha256: ed686033df44a21d2542e9d61743b822dac16028dd5f5baa30922f1401819846
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
      - P1-S1-C8
      - P3-S1-C5
      source_result: In a subset of 20 patients studied longitudinally, the association
        between ischemia involving part of Broca area and the presence of Broca or
        global aphasia was significant only acutely (χ²=20; df1; P<0.0001), not chronically
        (χ²=0; df1; p=1; not significant).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R003 correctly identifies the longitudinal
            subset (n=20) and the specific comparison of acute vs chronic phases for
            'ischemia involving part of Broca area'. The source P3-S1-C5 and P1-S1-C8
            confirm this specific statistical test (χ² test) and result.
          source_ids:
          - P3-S1-C5
          - P1-S1-C8
          - P2-S3-C7
        direction:
          answer: fits
          reason: The claim states the association was significant in the acute phase
            but not in the chronic phase. This matches the source data where acute
            P<0.0001 and chronic p=1 (not significant). The direction of the relationship
            (presence of ischemia associated with presence of aphasia) is preserved.
          source_ids:
          - P3-S1-C5
          - P1-S1-C8
        construct:
          answer: fits
          reason: Exposure is 'ischemia involving part of Broca area' (Brodmann 44/45),
            measured via DWI/T2/PWI overlap with a probabilistic map (template_lesion_overlap).
            Outcome is 'Broca or global aphasia' classified by WAB-R. The proposed
            core correctly identifies these constructs. The use of 'template_lesion_overlap'
            is appropriate as lesions are defined by their location relative to a
            cytoarchitectural map, not by patient-specific tractography.
          source_ids:
          - P2-S2-C10
          - P2-S2-C11
          - P2-S3-C3
          - P2-S3-C12
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the finding refers
            to the longitudinal subset. It also lists limitations regarding sample
            size and WAB-R classification, which are supported by P5-S2-C2. The distinction
            between acute and chronic is maintained.
          source_ids:
          - P3-S1-C5
          - P5-S2-C2
          - P2-S3-C7
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly notes the longitudinal
            nature and the specific subset. The 'not significant' chronic result is
            correctly framed as a lack of association in that phase, not a proof of
            zero effect, and the core does not misrepresent it as a standalone null
            finding for the whole study but rather as part of the longitudinal comparison.
          source_ids:
          - P3-S1-C5
          - P4-S1-C10
      optional_pending:
      - 'sample.time_post_onset: Acute <48h, Chronic >6 months (from P1-S1-C3, P2-S1-C5)'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.time_post_onset: Acute <48h, Chronic >6 months (from P1-S1-C3, P2-S1-C5)'
    normalizations:
    - field: sample.time_post_onset
      original: Acute phase (<= 48 hours from onset) and chronic phase (>= 6 months
        after stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 48, 6'
    analysis_identity:
      id: R003
      exposure:
        text: ischemia involving part of Broca area
      outcome:
        text: Broca or global aphasia
      analysis_label: Longitudinal association of Broca area ischemia (any part) with
        Broca/global aphasia
      relation: association
      evidence_ids:
      - P1-S1-C8
      - P3-S1-C5
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
        pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
        source_review: _compare/relationships-2026-11-16/review-current/Ochfeld2010
        source_status_sha256: 6de4ab559ccb583c775b6655c18d31ff56495486243bcdb5e55bd46d25b2f121
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7c7c3242028a22285d732084b386362de6f15505224beef5f71d86f321eba36f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 7c7c3242028a22285d732084b386362de6f15505224beef5f71d86f321eba36f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "In the 20 patients studied longitudinally, the association\n\
          between ischemia involving part of Broca area and Broca or\nglobal aphasia\
          \ was significant only acutely (\x012\x0320; df1;\nP\x010.0001), not chronically\
          \ (\x012\x030; df1; p\x031; not signifi-\ncant)."
        anchor_text: "In the 20 patients studied longitudinally, the association\n\
          between ischemia involving part of Broca area and Broca or\nglobal aphasia\
          \ was significant only acutely (\x012\x0320; df1;\nP\x010.0001), not chronically\
          \ (\x012\x030; df1; p\x031; not signifi-\ncant)."
        excluded_fragments: []
      P2-S2-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2c4cda858d5b1dc9263f3c279d5ac5ffc4ca25e8d97279527f87a19837cae059
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C10
          page: 2
          text_layer_sha256: 2c4cda858d5b1dc9263f3c279d5ac5ffc4ca25e8d97279527f87a19837cae059
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Images were analyzed by\ntechnicians blinded to the language\
          \ data and aphasia classification\nfor the presence of dense ischemia (bright\
          \ on DWI, dark on\napparent diffusion coefficient \x04ADC\x05) in the acute\
          \ stage or infarct\n(on T2 in the chronic stage) or hypoperfusion (on time-to-peak\n\
          maps derived from PWI) involving Broca area, with Broca area\ndefined as\
          \ Brodmann area 44 and/or 45 using a probabilistic\ncytoarchitectural map.6\
          \ Time-to-peak maps were registered to T2\nimages, which have better spatial\
          \ resolution, to provide anatomic\nlandmarks."
        anchor_text: "Images were analyzed by\ntechnicians blinded to the language\
          \ data and aphasia classification\nfor the presence of dense ischemia (bright\
          \ on DWI, dark on\napparent diffusion coefficient \x04ADC\x05) in the acute\
          \ stage or infarct\n(on T2 in the chronic stage) or hypoperfusion (on time-to-peak\n\
          maps derived from PWI) involving Broca area, with Broca area\ndefined as\
          \ Brodmann area 44 and/or 45 using a probabilistic\ncytoarchitectural map.6\
          \ Time-to-peak maps were registered to T2\nimages, which have better spatial\
          \ resolution, to provide anatomic\nlandmarks."
        excluded_fragments: []
      P2-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 281f70f4940bdf3f4c8d83f67be90e460a034d628416282da77b1bab634e5bc4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C11
          page: 2
          text_layer_sha256: 281f70f4940bdf3f4c8d83f67be90e460a034d628416282da77b1bab634e5bc4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Each patient’s scans were classified according to the\npresence\
          \ or absence of ischemia (on DWI) or infarct (on T2) or\nhypoperfusion,\
          \ defined as \x024-second delay in time to peak\nrelative to the homologous\
          \ region in the right hemisphere in any\npart of Broca area or covering\
          \ the entire region of Broca area."
        anchor_text: "Each patient’s scans were classified according to the\npresence\
          \ or absence of ischemia (on DWI) or infarct (on T2) or\nhypoperfusion,\
          \ defined as \x024-second delay in time to peak\nrelative to the homologous\
          \ region in the right hemisphere in any\npart of Broca area or covering\
          \ the entire region of Broca area."
        excluded_fragments: []
      P2-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: de7252aae153d99b372c0f93aca049954ee9d2d6cf6d539008cc923f71123494
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C7
          page: 2
          text_layer_sha256: de7252aae153d99b372c0f93aca049954ee9d2d6cf6d539008cc923f71123494
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'A subset of 20

          patients was studied at both time periods.'
        anchor_text: 'A subset of 20

          patients was studied at both time periods.'
        excluded_fragments: []
        image_sha256: 642b2a3e48d2374e042e049bd5557945056f7a5793453478a97a93b33a12cf43
        transcription: '. A subset of 20

          patients was studied at both time periods'
      P2-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 174bb7554386eb9d133b88fc6bf20ac57df77a035468d3a27f45948f2ca08ae8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: faccc5bcfd533f52986faa5756026b08d27d8e48e933b62dd2b806e4772f232e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C5
          page: 2
          text_layer_sha256: faccc5bcfd533f52986faa5756026b08d27d8e48e933b62dd2b806e4772f232e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Subjects and Methods\nParticipants\nWe included consecutive\
          \ patients who were right-hand-dominant\nwith left hemisphere ischemic stroke\
          \ (\x0148 hours from onset of\nsymptoms or \x026 months after stroke) and\
          \ native speakers of\nEnglish."
        anchor_text: "Subjects and Methods\nParticipants\nWe included consecutive\
          \ patients who were right-hand-dominant\nwith left hemisphere ischemic stroke\
          \ (\x0148 hours from onset of\nsymptoms or \x026 months after stroke) and\
          \ native speakers of\nEnglish."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "In the 20 patients studied longitudinally, the association\nbetween ischemia\
    \ involving part of Broca area and Broca or\nglobal aphasia was significant only\
    \ acutely (\x012\x0320; df1;\nP\x010.0001), not chronically (\x012\x030; df1;\
    \ p\x031; not signifi-\ncant)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
