---
id: lesion_volume
name: lesion volume
kind: classical
findings:
- id: f1
  target: naming_improvement
  target_kind: prognosis
  claim: Lesion volume was not associated with treatment-induced improvements in naming.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic
      stroke occurring at least 6 months prior to enrollment
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
  - heterogeneous population pooling different aphasic syndromes
  - focused only on anomia
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The volume of the necrotic stroke lesion, calculated
    as the number of voxels multiplied by voxel volume from manually drawn 3-dimensional
    representations of the lesion on T2 images. naming improvement was defined as
    the increase in naming of untrained items (items not targeted in treatment); the
    analysis controlled for age, time since stroke, overall aphasia severity (WAB-AQ),
    and neural architecture measures in the broader regression models, though the
    specific lesion volume finding is reported as a correlation. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S3-C4, two-model agreement, human verification pending): Methods


    Subjects


    We studied 24 individuals recruited from the local community with chronic aphasia
    as a result of a left hemisphere ischemic stroke that occurred at least 6 months
    prior to enrolling in this study Original text-layer quotation is preserved below.
    PDF image reading (P3-S2-C10, two-model agreement, human verification pending):
    . The evaluation occurred no longer than 1 week

    after treatment completion Original text-layer quotation is preserved below. Reconcile
    this new analysis with earlier drafts and source-review decisions for the paper;
    new candidate IDs do not carry earlier decisions forward.'
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
    - not_transcribed:sample.time_post_onset
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:naming_improvement
  therapy:
    id: anomia_treatment
    name: anomia treatment using semantic and phonological cueing hierarchies
  citation: '@Bonilha2016'
  source_passages:
  - section: Original source P6-S3-C2
    page: 6
    quote: "Lesion volume was not associated \nwith treatment-induced improvements\
      \ in naming (r = −.28, \nP = .18)."
    supports: claim
  - section: Original source P3-S3-C5
    page: 3
    quote: "The 3-dimensional representation of this \nlesion was then used to calculate\
      \ the lesion volume (num-\nber of voxels × voxel volume) for the purposes of\
      \ our sta-\ntistical analyses (see below)."
    supports: method
  - section: Original source P2-S3-C4
    page: 2
    quote: "Methods\nSubjects\nWe studied 24 individuals recruited from the local\
      \ com-\nmunity with chronic aphasia as a result of a left hemi-\nsphere ischemic\
      \ stroke that occurred at least 6 months \nprior to enrolling in this study."
    supports: sample
  - section: Original source P3-S2-C10
    page: 3
    quote: "The evaluation occurred no longer than 1 week \nafter treatment completion."
    supports: limitation
  - section: Original source P3-S2-C6
    page: 3
    quote: 'Thus, naming improvement was qual-

      ified as an increase in naming of untrained items.'
    supports: confounders
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Bonilha2016
  proposal_id: R005
  review_status_sha256: 30e5e988583897e38833369847bb311ba30b35e2168057e5f40d9744755cc14a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
        A/passages.json: 965c711cb2c3e7dd71fee993b6be3227cca3fc54aa9c66c15ec31236e759b5d8
        A/raw.json: c1d680c6b36f7c6f3232fd7645cacbf57dccb7d0a0d782ea27f0c3564cf91fc7
        A/source-units.json: fa96c6f907c41ed73207e100e1fd64f45caf51074e2a665c0d9fb7c68eaf668b
        A/full-source-units.json: d13aa33786f4058f67834dbac4397d6cc5fae082bd29c86bfd9eb3d31affe377
        A/meta.json: 00d670c3c6e841c7bbd7ea738a86e9f1de596a39e48ee515812fd8f0a7124133
        A/table-images/manifest.json: 58bb03529327917e47f979974f89f540dcafadefd216e499a8fc6ed2fba7b93f
        A/clauses/window-03/raw.json: f4383fa40e338a18224376f734221a9d447ee18769163a60a1aa8940545055e0
        A/clauses/window-03/prompt.txt: 4faa3e8ec18e06982ae88401d8ed12d9e232760352df68806e34481ae82decdd
        A/clauses/window-03/meta.json: e4a2218a82ef00e40094d64eff6d0000eab0d1bbd83308123b6d5df454ed0e61
        A/clauses/window-04/raw.json: 5df15bf434afe42d443e0e4258aeb64102d22d1ee346d667b315eaad818f4bca
        A/clauses/window-04/prompt.txt: 450436c7d26ada28025da42c7a1008795ef0149fdbd97e6c702f36d00e9e25d3
        A/clauses/window-04/meta.json: 52a7a5cfe28789bed075e7bc6f58d6480ee802a58d87ca37502a67e27b9222e6
        A/clauses/window-05/raw.json: e59d426ccf62b3807c1198a824e6664b2e8befc2774aa752d26fbe0da0bab381
        A/clauses/window-05/prompt.txt: e2e4d0dc3c911a00e5858477ba32d1b472d2ea59469f2c155841f3c3b55cf423
        A/clauses/window-05/meta.json: b78f13331c6b4f60c2476265900ba41514b5335ae422d6dd320067426d1e7ab1
        A/clauses/window-02/raw.json: 158bcaa6c6b2ee1d13747b25afc34acd3ba06f7c9bf5f1c4fb91006c3ca6f3ad
        A/clauses/window-02/prompt.txt: 1a4b44f8e6d568dc6d0fb2409b0b8224c4d68f431d2d6ce922483d126c400aa8
        A/clauses/window-02/meta.json: 95cbafa1602e5b1a9f5d73dcdc00a8da2e769c483c097110dc7b25186e47f228
        A/clauses/window-09/raw.json: 5d9a182a02dacde2a66a4b59a28847049922b6950197e8d7a20a72987689e828
        A/clauses/window-09/prompt.txt: fc417fe386b9df75303ae5e5ced1394a759225d32ae8012b12de5d82d3914d60
        A/clauses/window-09/meta.json: f694421a03ccdb29df8049b661fad16d11ef3d9b3d8e175568cdc48da64ff952
        A/clauses/window-07/raw.json: 5c54c513cb86da92ab90d6f3c7db2806eff99692bb8a3e9f4b3774a78e3f3a43
        A/clauses/window-07/prompt.txt: 001cf642b6936a7543a8cb0cd4317aefdb71ca277a4cd9604a85c5769728a6cf
        A/clauses/window-07/meta.json: b5d0b4a8e78ce70f93a2d5f62bcf26040a8cc6310ffb47b46962fd2f5795b326
        A/clauses/window-01/raw.json: bd40494e4b026b6eb1603557bf810304bf124aad6fa09ed9b1b0f03aeff4dcc7
        A/clauses/window-01/prompt.txt: 12bd4e8a6d59d29eab77a1349a2380c89a8a283f26c150c4dc7efdc34155380e
        A/clauses/window-01/meta.json: ba3c1f3baec0990200a90265f5ea410716ea142e03bb337d8b9638b49f4f318e
        A/clauses/window-06/raw.json: fc5bc8174eb5166d46d25ec66aded691075fc7030b472b200d9a5889226a33a1
        A/clauses/window-06/prompt.txt: 9e0741204c3852db2a127f4d29e7b83eb183c0cd0b16df5edf8d0a0db785328f
        A/clauses/window-06/meta.json: ad212d47ba1d40fb49ed0966a8a3d2a0a3560da88c1938078e2cab2f1ba1dc45
        A/clauses/window-08/raw.json: 2353a8793d8d66c0a1bc68d19660cbdd78a040544fea384c959d6e5a69e0ec38
        A/clauses/window-08/prompt.txt: 9e7d7df71e75673a2f1d11d0d07dc740d3e7fc1771cd4811e11e718bd1b9a06c
        A/clauses/window-08/meta.json: f53b7b998b9ad7bf3652e18568e1295dcc57c2079c195231b6a4bc0c3c4f384d
        B/passages.json: 965c711cb2c3e7dd71fee993b6be3227cca3fc54aa9c66c15ec31236e759b5d8
        B/raw.json: d9f6b61e5d861533ab5939a1fb20262d91135b65b2225d40458e73dfe483e77d
        B/source-units.json: fa96c6f907c41ed73207e100e1fd64f45caf51074e2a665c0d9fb7c68eaf668b
        B/full-source-units.json: d13aa33786f4058f67834dbac4397d6cc5fae082bd29c86bfd9eb3d31affe377
        B/meta.json: 1a8fcad61b2848848669a1938ef1a0593d29c855a57959e5db7a15d8681d3881
        B/table-images/manifest.json: 58bb03529327917e47f979974f89f540dcafadefd216e499a8fc6ed2fba7b93f
        B/clauses/window-03/raw.json: a061de181c098706362ed4098dc8b50a131570ecc1474fbde88be22512096234
        B/clauses/window-03/prompt.txt: 4faa3e8ec18e06982ae88401d8ed12d9e232760352df68806e34481ae82decdd
        B/clauses/window-03/meta.json: 6ea027aa9258e373f5f2e364b2111329adf2f7d349a78c58dc4449d01832fef4
        B/clauses/window-04/raw.json: a5b0e1d9db2995cf7e37328def871968612228896ea000cd159fe105810140de
        B/clauses/window-04/prompt.txt: 450436c7d26ada28025da42c7a1008795ef0149fdbd97e6c702f36d00e9e25d3
        B/clauses/window-04/meta.json: fb3f563639f68beb65ddc0a9e9bca013ec8f61b6fd0526ea517544e5167d62a1
        B/clauses/window-05/raw.json: 57d226fa76cb1facbab4f33398eca6fc9ddc3634245477c04be05e869299f174
        B/clauses/window-05/prompt.txt: e2e4d0dc3c911a00e5858477ba32d1b472d2ea59469f2c155841f3c3b55cf423
        B/clauses/window-05/meta.json: 04d4da6397452a2b208714c7b09db372d81ce2851e08a9b06f1377c5c275375a
        B/clauses/window-02/raw.json: 49d740ee329ae96fb21cf4a4d136157b6166cf8e6117e3e353072848b7c79ada
        B/clauses/window-02/prompt.txt: 1a4b44f8e6d568dc6d0fb2409b0b8224c4d68f431d2d6ce922483d126c400aa8
        B/clauses/window-02/meta.json: 806b444ffeb2e2e5fdbd90ceb22df01097854a5776698c1a90ce9fbfa5226037
        B/clauses/window-09/raw.json: 994ad998c31d384318ca4290af5ef65f8231e928d162c6fc2c84e11ed05b94cb
        B/clauses/window-09/prompt.txt: fc417fe386b9df75303ae5e5ced1394a759225d32ae8012b12de5d82d3914d60
        B/clauses/window-09/meta.json: b7fbe7e987edf5602292e7edf94fc164e92544315182b5a46808267c04a257fa
        B/clauses/window-07/raw.json: 5d8552564553d5e0326cdec7857d6b963fad8966c8c5a5201f440e95779a5012
        B/clauses/window-07/prompt.txt: 001cf642b6936a7543a8cb0cd4317aefdb71ca277a4cd9604a85c5769728a6cf
        B/clauses/window-07/meta.json: 815b9dbb7a5fe90767f89255f5513326fb88f1515506c6f57f91f5c1e8345b6f
        B/clauses/window-01/raw.json: 1db2a8c714d9dae5edf49834d03cadcbcf8989045f946ed24728f3b4e7a780d6
        B/clauses/window-01/prompt.txt: 12bd4e8a6d59d29eab77a1349a2380c89a8a283f26c150c4dc7efdc34155380e
        B/clauses/window-01/meta.json: 5ae8a31efaaed70cdb03067890637c39d2e04d6592a0555342a017c0570bfef1
        B/clauses/window-06/raw.json: 12b5ec4a960b2b9a3567e24411e121a15daecfc4472faf3c7624bbde301ce1f6
        B/clauses/window-06/prompt.txt: 9e0741204c3852db2a127f4d29e7b83eb183c0cd0b16df5edf8d0a0db785328f
        B/clauses/window-06/meta.json: 88ebd9869649a907daf15c44d0ba8fda200a7448cb614e8c66456b853da04506
        B/clauses/window-08/raw.json: 8771f517a1260efa051f9e1a5670b3ac8bc53cb65ed4360137b457924727ff46
        B/clauses/window-08/prompt.txt: 9e7d7df71e75673a2f1d11d0d07dc740d3e7fc1771cd4811e11e718bd1b9a06c
        B/clauses/window-08/meta.json: d24f96411f2b9558cf0bd566e568de08c7e42a4cadbcaf45ea99746578af9f48
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
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2016
      source_status_sha256: 474eb33585a00db0e927959487f196b73f304545dbda272b12d5f1d6184d3070
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: lesion volume
    outcome:
      text: treatment-induced improvements in naming
    analysis_label: Correlation analysis
    relation: association
    evidence_ids:
    - P6-S3-C2
    qualifier_ids:
    - P6-S3-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2016
      source_status_sha256: 474eb33585a00db0e927959487f196b73f304545dbda272b12d5f1d6184d3070
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C6
      - Result passage disposed without unit P5-S3-C7
      - Result passage disposed without unit P5-S3-C8
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P9-S3-C5
      - Accounting without a linked unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C5
      - Unaccounted source passage P11-S1-C2
      - Accounting without a linked unit P11-S2-C14
      - Unaccounted source passage P11-S2-C14
      unattached_null_or_qualifier_ids:
      - P6-S1-C4
      - P8-S2-C5
      suppressed_nonrepresented_units: 18
      default_disposition_count_requires_completeness_check: 176
      unselected_timing_passages:
      - P1-S2-C5
      - P2-S2-C5
      - P2-S3-C4
      - P5-S2-C8
      - P5-S2-C9
      - P6-S1-C7
      - P11-S2-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P11-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S2-C10
        - P11-S2-C13
        - P11-S2-C14
        - P11-S2-C15
        - P11-S3-C2
        - P11-S3-C3
        - P11-S3-C4
        - P11-S3-C5
        - P11-S3-C6
        - P11-S3-C7
        - P11-S3-C8
        - P11-S3-C9
        - P11-S3-C10
        - P12-S1-C3
        - P12-S1-C4
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P5-S2-C8
        - P5-S2-C9
        - P5-S2-C10
        - P5-S3-C3
        - P5-S3-C4
        - P5-S3-C5
        - P5-S3-C6
        - P5-S3-C7
        - P6-S1-C7
        - P6-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P10-S1
        - P10-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2016
      source_status_sha256: 474eb33585a00db0e927959487f196b73f304545dbda272b12d5f1d6184d3070
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C9
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Abstract summary of associations between naming improvement and NSW/BC.
    - source_id: P1-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Abstract statement on variance explained by the combined model.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean AQ for the group.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive distribution of aphasia types.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive baseline PNT scores.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive baseline response attempts and no responses.
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive baseline paraphasia counts.
    - source_id: P5-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive average improvement in items named.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of average item improvement.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean percentage improvement in naming.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive increase in response attempts.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive changes in paraphasia types.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Null correlation between time poststroke and naming changes.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement on lesion visibility.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive common locations of damage.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive comparison of left vs right hemisphere connectivity.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of connectivity in necrotic areas.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Trend association between WAB-AQ and left temporal BC.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Qualification that the WAB-AQ/BC model was not statistically significant.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Null relationship between baseline aphasia severity and NSW.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation between NSW and lesion volume.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Association between naming improvement and left temporal BC.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Association between WAB-AQ and naming improvement.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Null relationship between naming improvement and frontal/parietal BC.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Null association between lesion volume and naming improvement.
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation between temporal lobe lesion burden and BC.
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Association between PNT improvement and global NSW.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Association between higher global NSW and naming improvement.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of WAB-AQ association with PNT improvement.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Performance of combined model (NSW and left temporal BC).
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explanation of multicollinearity between NSW and BC.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Null association of right hemisphere regions with improvement.
    - source_id: P8-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of NSW association.
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of left temporal BC association.
    - source_id: P8-S1-C11
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of WAB-AQ association.
    - source_id: P8-S2-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of combined model performance.
    - source_id: P8-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of null frontal/parietal BC relationship.
    - source_id: P9-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion summary of NSW and left temporal BC as determinants.
    - source_id: P9-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right hemisphere role in recovery.
    - source_id: P9-S3-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of left temporal BC association.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Review of prior literature on naming regions.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Hickok and Poeppel model.
    - source_id: P10-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive note on subject 8's BC in Figure 6.
    - source_id: P11-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion of temporal lobe regions and naming recovery.
    - source_id: P11-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion of influence of temporal regions on network.
    - source_id: P11-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion of global network preservation.
    - source_id: P11-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive note on performance variability.
    - source_id: P11-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on connectivity utility.
    - source_id: P11-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive note on performance variability.
    - source_id: P12-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restatement of NSW and BC importance.
    - source_id: P12-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Conclusion restatement of variance explained.
    unresolved_coverage:
    - source_id: P8-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C9
    - P5-S3-C3
    - P5-S3-C4
    - P5-S3-C5
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C8
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C12
    - P6-S2-C3
    - P6-S2-C5
    - P6-S2-C8
    - P6-S3-C3
    - P6-S3-C4
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C10
    - P8-S2-C5
    - P8-S2-C9
    - P9-S2-C9
    - P9-S3-C5
    - P10-S1-C8
    - P10-S2-C2
    - P10-S2-C9
    - P11-S1-C2
    - P11-S1-C3
    - P11-S1-C5
    - P11-S2-C10
    - P11-S2-C14
    - P11-S2-C15
    - P12-S1-C8
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
      - P2-S3-C8
      recruited_sample:
      - P2-S3-C4
      eligibility:
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
      imaging_provenance:
      - P3-S1-C9
      imaging_timing:
      - P3-S1-C10
      outcome_timing:
      - P3-S2-C10
      outcome_definition:
      - P5-S2-C2
      validation: []
      analysis_restrictions:
      - P5-S2-C6
      dependent_variable_statement:
      - P5-S2-C4
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C11
      - P5-S2-C6
      - P6-S2-C9
      - P6-S2-C10
      - P7-S1-C9
      - P8-S1-C1
      - P8-S1-C3
      - P8-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P11-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S2-C10
      - P11-S2-C13
      - P11-S2-C14
      - P11-S2-C15
      - P11-S3-C2
      - P11-S3-C3
      - P11-S3-C4
      - P11-S3-C5
      - P11-S3-C6
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C9
      - P11-S3-C10
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P5-S2-C8
      - P5-S2-C9
      - P5-S2-C10
      - P5-S3-C3
      - P5-S3-C4
      - P5-S3-C5
      - P5-S3-C6
      - P5-S3-C7
      - P6-S1-C7
      - P6-S1-C9
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
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      review_sha256: 30e5e988583897e38833369847bb311ba30b35e2168057e5f40d9744755cc14a
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
      - P6-S3-C2
      source_result: The source reports that lesion volume was not associated with
        treatment-induced improvements in naming (r = −.28, P = .18). This is a standalone
        null finding from a correlation analysis, distinct from the regression models
        that controlled for lesion volume to test neural architecture measures.
      result_status: not_detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is a correlation between lesion volume and
            naming improvement. The source explicitly states 'Lesion volume was not
            associated with treatment-induced improvements in naming (r = −.28, P
            = .18)' in P6-S3-C2. This is distinct from the regression models (P6-S2-C9,
            P8-S1-C1) where lesion volume was a covariate. The draft correctly identifies
            this as a correlation analysis.
          source_ids:
          - P6-S3-C2
          - P5-S2-C6
        direction:
          answer: fits
          reason: The source reports a non-significant correlation (P = .18). The
            draft claims 'no_effect' (no statistically detected association), which
            accurately reflects the null result. It does not claim zero effect, just
            lack of statistical detection.
          source_ids:
          - P6-S3-C2
        construct:
          answer: fits
          reason: Exposure is lesion volume (defined in P3-S3-C5 as voxels * voxel
            volume from T2). Outcome is treatment-induced naming improvement (defined
            in P5-S2-C2 as PNT change adjusted for baseline). The draft correctly
            identifies these constructs. The method is labeled 'LSM' in the draft,
            which is slightly imprecise as it is a correlation, but the relationship
            type 'correlational' is correct. The patient measurement is regional_lesion_load,
            which is accurate for lesion volume.
          source_ids:
          - P3-S3-C5
          - P5-S2-C2
          - P6-S3-C2
        qualifications:
          answer: fits
          reason: The draft includes the qualification that naming improvement was
            defined as untrained items (P3-S2-C6). It also notes that while broader
            models controlled for lesion volume, this specific finding is a correlation.
            This is accurate; P6-S3-C2 reports a simple correlation, not a regression
            coefficient.
          source_ids:
          - P3-S2-C6
          - P6-S3-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding the heterogeneous population
            and focus on anomia. It does not omit any material caveats that would
            change the interpretation of the null result. The fact that lesion volume
            was a covariate in other models is noted in the qualifications, preventing
            misinterpretation as a robustness check for those models.
          source_ids:
          - P11-S2-C7
          - P11-S2-C8
      optional_pending:
      - sample.time_post_onset
      - statistical_values.r
      - statistical_values.p
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
    - sample.time_post_onset
    - statistical_values.r
    - statistical_values.p
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: measured at baseline before a 2-week intense intervention, with outcome
        assessed no longer than 1 week after treatment completion
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 2'
    analysis_identity:
      id: R005
      exposure:
        text: lesion volume
      outcome:
        text: treatment-induced improvements in naming
      analysis_label: Correlation analysis
      relation: association
      evidence_ids:
      - P6-S3-C2
      qualifier_ids:
      - P6-S3-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
        source_review: _compare/relationships-2026-11-16/review-current/Bonilha2016
        source_status_sha256: 474eb33585a00db0e927959487f196b73f304545dbda272b12d5f1d6184d3070
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 71e387913dfb9d7711840c59d6eb04be93e036a8288b6e19363423e4da6f82c1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: 71e387913dfb9d7711840c59d6eb04be93e036a8288b6e19363423e4da6f82c1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods\nSubjects\nWe studied 24 individuals recruited from\
          \ the local com-\nmunity with chronic aphasia as a result of a left hemi-\n\
          sphere ischemic stroke that occurred at least 6 months \nprior to enrolling\
          \ in this study."
        anchor_text: "Methods\nSubjects\nWe studied 24 individuals recruited from\
          \ the local com-\nmunity with chronic aphasia as a result of a left hemi-\n\
          sphere ischemic stroke that occurred at least 6 months \nprior to enrolling\
          \ in this study."
        excluded_fragments: []
        image_sha256: 2cac9421cf0b1b05f0c1d601151d8ae836da57be05409fdc535ccce2684c9dbc
        transcription: 'Methods


          Subjects


          We studied 24 individuals recruited from the local community with chronic
          aphasia as a result of a left hemisphere ischemic stroke that occurred at
          least 6 months prior to enrolling in this study'
      P3-S2-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c5828c2e0da3f67d2d829c41163cad95ba0dc3c2ef56690701a18e81f7146082
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C10
          page: 3
          text_layer_sha256: c5828c2e0da3f67d2d829c41163cad95ba0dc3c2ef56690701a18e81f7146082
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The evaluation occurred no longer than 1 week \nafter treatment\
          \ completion."
        anchor_text: "The evaluation occurred no longer than 1 week \nafter treatment\
          \ completion."
        excluded_fragments: []
        image_sha256: 635e247183798c604eb01d0ed0d0f3ae9e80bc9cb55ce9a596bdf085f5cb5e60
        transcription: '. The evaluation occurred no longer than 1 week

          after treatment completion'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "Lesion volume was not associated \nwith treatment-induced improvements in\
    \ naming (r = −.28, \nP = .18)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
