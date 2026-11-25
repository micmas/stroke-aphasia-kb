---
id: left_insular_precentral_gyrus_cluster
name: left precentral gyrus of the insula cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: apraxia_of_speech
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: apraxia_of_speech
  target_kind: impairment
  claim: A discrete region of the left precentral gyrus of the insula was infarcted
    in all patients with apraxia of speech and completely spared in all patients without
    the disorder.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 44
    population: Right-handed, native English-speaking stroke patients with single
      left-hemisphere cerebrovascular accidents
    phase: not_reported
    time_post_onset: Injuries occurred at least one year before inclusion; imaging
      performed at least 3 weeks after onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Association of a lesion site with a behavioural deficit is not conclusive proof
    of function
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a discrete region of the
    left precentral gyrus of the insula, reconstructed from CT and MRI scans onto
    templates. Double dissociation found between 25 patients with apraxia of speech
    and 19 patients without the deficit. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S2-C11,
    two-model agreement, human verification pending): . All patients had undergone
    CT or MRI at least 3

    weeks (typically 4–5 years) after onset of their injury to guarantee distinct

    boundaries of the completed stroke Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:apraxia_of_speech
  citation: '@Dronkers1996'
  source_passages:
  - section: Original source P1-S1-C6
    page: 1
    quote: "All patients with articulatory \nplanning deficits had lesions that included\
      \ a discrete region ofthe \nleft precentral gyrus of the insula, a cortical\
      \ area beneath the \nfrontal and temporal lobes."
    supports: claim
  - section: Original source P1-S1-C7
    page: 1
    quote: "This area was completely spared in \nall patients without these articulation\
      \ deficits."
    supports: claim
  - section: Original source P2-S1-C6
    page: 2
    quote: "These lesions span essentially the same arterial \ndistribution as the\
      \ group of apraxic patients but spare one \nsignificant area; the very area\
      \ which is consistently infarcted in \npatients with apraxia of speech (Fig.\
      \ 1a, top) is entirely spared in \nthose patients without the disorder (Fig.\
      \ lb, top)."
    supports: claim
  - section: Original source P2-S1-C8
    page: 2
    quote: "Every one of the 25 patients with apraxia \nof speech had a lesion encompassing\
      \ this discrete region of the \ninsula, whereas none of the lesions in the 19\
      \ patients without \napraxia of speech involved this critical area."
    supports: claim
  - section: Original source P2-S2-C4
    page: 2
    quote: "Sectioning the brain to compare to the same horizontal slice as the \n\
      computerized lesion reconstructions revealed that the area of \n160 \ninterest\
      \ lay on the precentral gyrus of the insula, directly anterior \nto the central\
      \ sulcus as marked."
    supports: claim
  - section: Original source P3-S1-C2
    page: 3
    quote: "Assessments \nwere based on four criteria measuring a pattern of articulatory\
      \ \nbehaviour as described by Wertz et a/."
    supports: method
  - section: Original source P3-S2-C8
    page: 3
    quote: Forty-four patients met the following criteria.
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: "All had suffered a \nsingle left-hemisphere cerebrovascular accident (stroke)\
      \ with no other history \nof neurological or psychiatric problems."
    supports: sample
  - section: Original source P3-S2-C10
    page: 3
    quote: "The injuries had occurred at least one \nyear before inclusion in the\
      \ study to ensure that the observed speech and \nlanguage deficits had stabilized."
    supports: sample
  - section: Original source P3-S2-C11
    page: 3
    quote: "All patients had undergone CT or MRI at least 3 \nweeks (typically 4-5\
      \ years) after onset of their injury to guarantee distinct \nboundaries of the\
      \ completed stroke."
    supports: sample
  - section: Original source P3-S3-C3
    page: 3
    quote: "This was done either by direct administration of the Motor \nSpeech Evaluation28\
      \ or by viewing a videotape of its administration and scoring \nblind to the\
      \ other clinicians' diagnosis of the patient."
    supports: method
  - section: Original source P1-S2-C2
    page: 1
    quote: "In this study, lesions derived from CT and MRI scans of 25 \npatients\
      \ with apraxia of speech were reconstructed onto templates \nand entered into\
      \ a minicomputer using software and techniques \ndeveloped at the VA Medical\
      \ Center in Martinez, California4."
    supports: method
  - section: Original source P1-S2-C3
    page: 1
    quote: "Lesion overlays were produced by computer-superimposing \nlesions represented\
      \ on each horizontal slice for all patients \ndemonstrating the same articulatory\
      \ deficit."
    supports: method
  - section: Original source P2-S1-C10
    page: 2
    quote: "To determine the exact location of this articulatory planning \narea,\
      \ a normal human brain was dissected and comparisons were \nmade with the slices\
      \ of the reconstruction programme (Fig. 2)."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Dronkers1996
  proposal_id: R002
  review_status_sha256: 4df083ea1eec5e1d9d59df9f1d9af62b02e8366686f773d4211404733a05ab22
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
        A/passages.json: 4b3de3878982c8d854ebadb4ead6bf9da388bf6f59713e6fb7878aefc0f943cd
        A/raw.json: a6cc6bba2cf03d1b1b37db727b8276e72a849f863c7eecd0600e81d8c095250f
        A/source-units.json: 149c27acb09634c50e7c55de575baf9edc61c1ccb427077c1dfad15c41a038c5
        A/full-source-units.json: 149c27acb09634c50e7c55de575baf9edc61c1ccb427077c1dfad15c41a038c5
        A/meta.json: 47e74ece8257f574a7db09d186957d9f9eaf6786335eca151c06c2322502febe
        A/table-images/TABLE-1-page-3-1.png: 49f0fdc31da3e46ebb08fc0abc17d2e5d989a9a390d45a71d641458ae58893a1
        A/table-images/page-3.png: 1f4d1cd0e349b4b1828b3143697d85a3205eecea393e3c880d1ebe2e43d2ea6d
        A/table-images/manifest.json: 1f5bf1c7f793b3261f1e2ce223dddfca43ea79871b9166636cfb615c195a3889
        A/clauses/window-03/raw.json: 7b4759a261076778fb96e9ab5ff472c648f8fe13b4ff3c44a6a8724b805152f9
        A/clauses/window-03/prompt.txt: db6870d5e9f935691f84e9d6c7f18e470e8eea8d322c3f8ede53505db5898cf9
        A/clauses/window-03/meta.json: c7d4803836b29d83765bdbd98c4d54f8edbeed72776ad0e9e7a192c45bebd9a1
        A/clauses/window-04/raw.json: 02ae64de0b6b726039aeeb3c07f9df313b78322170e2bb70df7e647edaa0eb88
        A/clauses/window-04/prompt.txt: 3488ee6b4d6bdbb1353847085ff946f34cde8cf8a9ab802d5a68457dc83eacd1
        A/clauses/window-04/meta.json: dbcba10b15d633b3b543fcaff7950567d3f58cd805432b4f1fbf3885e449abb8
        A/clauses/window-05/raw.json: 7ffd004e8c5eb6cd5fb4a91c76a41a4dd211e78e2c7107e675b644692775fc4c
        A/clauses/window-05/prompt.txt: d2b1f234b2c36d2cd199ec66e313a642727c4c6018a27de2602d6c85a2e52a78
        A/clauses/window-05/meta.json: 1e2e67037026c4881ee95921edd05e21f0ed90da94313254cc11a40acd300b7e
        A/clauses/window-02/raw.json: f27f38ae1c090c5623241c68c66c0c460d7fb036aa9446346b0f956784832131
        A/clauses/window-02/prompt.txt: c544571989264503b6972be72c4cb586372cb005e124f08d7b1f9e0b5fb1f529
        A/clauses/window-02/meta.json: d7a1637ec4c87e41c8e69090942be2b16c11ba52d304aab8ee0af7441c06d7cb
        A/clauses/window-01/raw.json: e27ce46b0a6641b1690f793aef2ad64ab2c0d5f541fa471169aed33b9a863910
        A/clauses/window-01/prompt.txt: 033127e8919af3b8cea0b4f1c7e93991bd143661ac6568ac7c2aa884c6a91350
        A/clauses/window-01/meta.json: d6cc466e690b8dc6d6d7605c891c142aa7d534ff74a8d162b23369e0ae175a45
        A/tables/TABLE-1-page-3-1/raw.json: 3212027ebd4aeb501fcfa5b096afcb648a1c38246eb0ebb1b0bfd01f1dd1999d
        A/tables/TABLE-1-page-3-1/prompt.txt: a71340da5f09917c2499d909a71ea1763b558a0f30110ebd8bb162b98ddc8743
        A/tables/TABLE-1-page-3-1/meta.json: e9261406431531e21a07907c7ef5ac48dd29be2881347bc56e0de16290421e96
        B/passages.json: 4b3de3878982c8d854ebadb4ead6bf9da388bf6f59713e6fb7878aefc0f943cd
        B/raw.json: 59df52d7e0c8fc13a7ab301bb313895461b4fa99906073e9c99029a6cd917adb
        B/source-units.json: 149c27acb09634c50e7c55de575baf9edc61c1ccb427077c1dfad15c41a038c5
        B/full-source-units.json: 149c27acb09634c50e7c55de575baf9edc61c1ccb427077c1dfad15c41a038c5
        B/meta.json: c4ced46fb8fcbcde41f06c5d8d98b901bbc6bf08ad7fe0097008a5de43f209b6
        B/table-images/TABLE-1-page-3-1.png: 49f0fdc31da3e46ebb08fc0abc17d2e5d989a9a390d45a71d641458ae58893a1
        B/table-images/page-3.png: 1f4d1cd0e349b4b1828b3143697d85a3205eecea393e3c880d1ebe2e43d2ea6d
        B/table-images/manifest.json: aace214ad455d17a4879079bb5d24540a87350cb951320926feab2b56b86584b
        B/clauses/window-03/raw.json: f7239f2c1be53e1809e5a8447fe7ae34c5852a81baae63a20b27a738da8c0b1e
        B/clauses/window-03/prompt.txt: db6870d5e9f935691f84e9d6c7f18e470e8eea8d322c3f8ede53505db5898cf9
        B/clauses/window-03/meta.json: 188e05beecd009cd98ef101b247a00e2e9eac0cb89cfbb0e4cabb774daee56a2
        B/clauses/window-04/raw.json: b909a4df1d0b4cb987b8e1663d08018f12e16b182508f84ecf9862b3b9defb72
        B/clauses/window-04/prompt.txt: 3488ee6b4d6bdbb1353847085ff946f34cde8cf8a9ab802d5a68457dc83eacd1
        B/clauses/window-04/meta.json: a5e80d86d6e9f03128eb916038507e52d47e1154d813d5e672182a6c6e3f3080
        B/clauses/window-05/raw.json: 838999484f125878fa4e6b074e7cccd67d015ecfaae3aec73576a42ace4f172c
        B/clauses/window-05/prompt.txt: d2b1f234b2c36d2cd199ec66e313a642727c4c6018a27de2602d6c85a2e52a78
        B/clauses/window-05/meta.json: b36923a6f17246a79c704610e8ce4a831875295947769660311e52e14bc0a397
        B/clauses/window-02/raw.json: 45e3e7ba456a9a6b7d53a26bc86d4714b4b8f8943e0fbd82b68675173762c7cd
        B/clauses/window-02/prompt.txt: c544571989264503b6972be72c4cb586372cb005e124f08d7b1f9e0b5fb1f529
        B/clauses/window-02/meta.json: e325c350fe071ebe0e67e0743f8e6361eba9d6bc28d42a1a518c54c4e38483de
        B/clauses/window-01/raw.json: ace9262c8cf459f86bfc512266378c7b645e5d2062541476124228658d88c658
        B/clauses/window-01/prompt.txt: 033127e8919af3b8cea0b4f1c7e93991bd143661ac6568ac7c2aa884c6a91350
        B/clauses/window-01/meta.json: ac2b4697960efa034b85c0378b318fb98b4004f8eeff438e3e976188c51bc265
        B/tables/TABLE-1-page-3-1/raw.json: 564ce06d361cd4ff30580bd7664e651a4c26de7fe3501de60395b8f920a40726
        B/tables/TABLE-1-page-3-1/prompt.txt: a71340da5f09917c2499d909a71ea1763b558a0f30110ebd8bb162b98ddc8743
        B/tables/TABLE-1-page-3-1/meta.json: 949a4fe0bf55d8fa76c241108bce69410e6eda591b112ae073eb9911513842ff
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
      pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers1996
      source_status_sha256: 1580c9f2b847bf5bdfacaaa0a89d8371695b55d81ec30180da079bf20a09c7cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: sparing of a discrete region of the left precentral gyrus of the insula
    outcome:
      text: absence of apraxia of speech
    analysis_label: Lesion overlay analysis (control group)
    relation: association
    evidence_ids:
    - P1-S1-C7
    - P2-S1-C6
    qualifier_ids:
    - P1-S1-C7
    - P2-S1-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers1996
      source_status_sha256: 1580c9f2b847bf5bdfacaaa0a89d8371695b55d81ec30180da079bf20a09c7cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P1-S2-C8
      - Accounting without a linked unit P1-S3-C5
      - Accounting without a linked unit P2-S1-C6
      - Accounting without a linked unit P2-S1-C8
      - Accounting without a linked unit P2-S1-C9
      - Result passage disposed without unit P2-S2-C4
      - Unaccounted source passage P1-S3-C5
      - Unaccounted source passage P2-S1-C9
      - Unaccounted source passage P2-S1-C6
      - Unaccounted source passage P2-S1-C8
      - Result passage disposed without unit P3-S3-C8
      unattached_null_or_qualifier_ids:
      - P3-S3-C8
      suppressed_nonrepresented_units: 1
      default_disposition_count_requires_completeness_check: 70
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
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
        - P2-S1
        - P2-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers1996
      source_status_sha256: 1580c9f2b847bf5bdfacaaa0a89d8371695b55d81ec30180da079bf20a09c7cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes the double dissociation between the two groups.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States all patients with deficits had lesions in the left precentral
        gyrus of the insula.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: States this area was completely spared in patients without deficits.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports a common area of infarction in all 25 cases of apraxia of speech.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Locates the common area of injury within the insula.
    - source_id: P1-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overlap in neighboring sections but not the primary finding.
    - source_id: P2-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the anatomical dissection process.
    - source_id: P2-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Confirms the critical area is entirely spared in patients without the
        disorder.
    - source_id: P2-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Explicitly states every patient with apraxia had the lesion and none
        without it did.
    - source_id: P2-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides Talairach coordinates for the area.
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the anatomical location on the precentral gyrus via dissection.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides an example of a patient's articulatory error.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides an example of a patient's articulatory error.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the nature of errors (islands of fluent speech).
    - source_id: P2-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes changes in rate and prosody as potential compensation.
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distinguishes errors from word retrieval deficits.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes typical phoneme substitution patterns.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports the mean severity rating of the group.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the severity rating for the control group.
    - source_id: P3-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the percentage of CT scans used.
    - source_id: P3-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the percentage of MRI scans used.
    - source_id: P2-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: States the role of the insula is supported by a double dissociation.
    unresolved_coverage:
    - source_id: P2-S1-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C8
    - P1-S2-C11
    - P2-S1-C3
    - P2-S1-C9
    - P2-S2-C4
    - P2-S3-C5
    - P2-S3-C6
    - P2-S3-C7
    - P2-S4-C2
    - P2-S4-C3
    - P3-S3-C5
    - P3-S3-C7
    - P3-S3-C8
    - P3-S3-C15
    - P3-S3-C16
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
      - P1-S1-C4
      - P1-S3-C3
      recruited_sample:
      - P1-S1-C4
      - P1-S3-C3
      eligibility:
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
      - P3-S2-C11
      - P3-S2-C12
      imaging_provenance:
      - P1-S2-C2
      - P3-S3-C11
      - P3-S3-C14
      imaging_timing:
      - P3-S2-C11
      outcome_timing:
      - P3-S2-C10
      outcome_definition:
      - P3-S3-C6
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C4
      - P3-S2-C13
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S1-C10
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
      pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
      review_sha256: 4df083ea1eec5e1d9d59df9f1d9af62b02e8366686f773d4211404733a05ab22
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
      - P1-S1-C7
      - P2-S1-C6
      source_result: In the control group of 19 patients without apraxia of speech,
        lesions were overlaid on reference templates. The analysis revealed that the
        specific discrete region of the left precentral gyrus of the insula, which
        was consistently infarcted in the apraxic group, was completely spared in
        all 19 control patients. This finding constitutes the second half of a double
        dissociation, supporting the association between this specific lesion site
        and the presence of apraxia of speech.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R002 is identified as a 'Lesion overlay analysis
            (control group)'. The source passages P1-S1-C7 and P2-S1-C6 explicitly
            describe the findings for the group of 19 patients without apraxia of
            speech, confirming that the analysis identity matches the control group
            overlay described in the draft.
          source_ids:
          - P1-S1-C7
          - P2-S1-C6
          - P1-S3-C4
        direction:
          answer: fits
          reason: The draft claims the region was 'completely spared' in patients
            without the disorder. Source P1-S1-C7 states 'This area was completely
            spared in all patients without these articulation deficits' and P2-S1-C6
            states the area 'is entirely spared in those patients without the disorder'.
            The direction of the association (sparing in the absence of the deficit)
            is faithfully represented.
          source_ids:
          - P1-S1-C7
          - P2-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as the sparing of the left
            precentral gyrus of the insula. The outcome is the absence of apraxia
            of speech. The patient measurement is correctly classified as template_lesion_overlap,
            as the source describes reconstructing lesions onto templates and superimposing
            them (P1-S2-C2, P1-S2-C3), not using patient diffusion data or functional
            imaging.
          source_ids:
          - P1-S1-C6
          - P1-S2-C2
          - P1-S2-C3
          - P2-S1-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that this is part of a 'double
            dissociation' involving 25 patients with and 19 without the deficit. It
            also includes the limitation that 'Association of a lesion site with a
            behavioural deficit is not conclusive proof of function', which is explicitly
            stated in P1-S2-C10. These material qualifiers are present and accurate.
          source_ids:
          - P1-S1-C5
          - P1-S2-C10
          - P2-S1-C7
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key methodological caveat regarding the non-conclusive
            nature of lesion-behavior association (P1-S2-C10). It also correctly notes
            the population restrictions (right-handed, native English speakers, single
            left-hemisphere stroke) in the population field. No material caveats that
            would change the interpretation of the control group result are omitted.
          source_ids:
          - P1-S2-C10
          - P3-S2-C9
          - P3-S2-C12
      optional_pending:
      - Specific Talairach coordinates (-41, -2, 10) mentioned in P2-S1-C9 are not
        transcribed in the draft, but this is optional metadata for a qualitative
        draft.
      - Details of the 'Motor Speech Evaluation' criteria (P3-S1-C2, P3-S1-C3) are
        not fully detailed in the draft, but the assessment method is correctly identified.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific Talairach coordinates (-41, -2, 10) mentioned in P2-S1-C9 are not transcribed
      in the draft, but this is optional metadata for a qualitative draft.
    - Details of the 'Motor Speech Evaluation' criteria (P3-S1-C2, P3-S1-C3) are not
      fully detailed in the draft, but the assessment method is correctly identified.
    normalizations: []
    analysis_identity:
      id: R002
      exposure:
        text: sparing of a discrete region of the left precentral gyrus of the insula
      outcome:
        text: absence of apraxia of speech
      analysis_label: Lesion overlay analysis (control group)
      relation: association
      evidence_ids:
      - P1-S1-C7
      - P2-S1-C6
      qualifier_ids:
      - P1-S1-C7
      - P2-S1-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
        source_review: _compare/relationships-2026-11-16/review-current/Dronkers1996
        source_status_sha256: 1580c9f2b847bf5bdfacaaa0a89d8371695b55d81ec30180da079bf20a09c7cc
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 9beca57a0acb454ee7de40193677ec8a8f2cf14ae1465959f49e4f3df5e9427a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8acb9890f0a91dba2ba36e77c9b471279035baf76f3034139a08feffeeb0711f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C11
          page: 3
          text_layer_sha256: 8acb9890f0a91dba2ba36e77c9b471279035baf76f3034139a08feffeeb0711f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All patients had undergone CT or MRI at least 3 \nweeks (typically\
          \ 4-5 years) after onset of their injury to guarantee distinct \nboundaries\
          \ of the completed stroke."
        anchor_text: "All patients had undergone CT or MRI at least 3 \nweeks (typically\
          \ 4-5 years) after onset of their injury to guarantee distinct \nboundaries\
          \ of the completed stroke."
        excluded_fragments: []
        image_sha256: e32d5a29b4e8f2915148c6ac4adf8769df66d1f3d022113fa08e86c32f1c058e
        transcription: '. All patients had undergone CT or MRI at least 3

          weeks (typically 4–5 years) after onset of their injury to guarantee distinct

          boundaries of the completed stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "All patients with articulatory \nplanning deficits had lesions that included\
    \ a discrete region ofthe \nleft precentral gyrus of the insula, a cortical area\
    \ beneath the \nfrontal and temporal lobes."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
