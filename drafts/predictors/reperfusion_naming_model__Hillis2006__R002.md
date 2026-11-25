---
id: reperfusion_naming_model
name: multivariate reperfusion model for oral naming improvement
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: oral_naming_improvement
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: oral_naming_improvement
  target_kind: prognosis
  claim: The degree of improvement in oral naming of pictures was best predicted by
    a model including reperfusion of left BA 37, BA 44/45, and BA 22, with BA 37 being
    the strongest predictor; each area contributed independently to the prediction
    after adjustment for the others.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: right-handed English-speaking patients with acute left-hemisphere
      ischemic stroke and impaired picture naming
    phase: not_reported
    time_post_onset: initial imaging and assessment at day 1, follow-up imaging and
      assessment at days 3-5
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The model was derived from a subset of patients who completed both initial and
    follow-up imaging and testing
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multivariate model based on the reperfusion of left
    Brodmann areas 37, 44/45, and 22, where reperfusion is defined as hypoperfusion
    (>= 4s TTP delay) at day 1 followed by normal perfusion (<= 4s TTP delay and >=
    2s improvement in TTP) and absence of DWI abnormality at days 3-5. BA 37 was the
    strongest predictor; BA 44/45 and BA 22 contributed independently after adjustment
    for each other and BA 37. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P1-S3-C5, two-model
    agreement, human verification pending): . The population consisted of a consecutive
    series of patients with acute left-hemisphere ischemic stroke who were admitted
    to Johns Hopkins Hospital and met the following inclusion criteria: (1) right
    handed; (2) premorbidly proficient in English; (3) able to provide informed consent
    for the study or indicate a family member who provided informed consent; (4) no
    contraindication to MRI (e.g., implanted ferrous metal); and (5) no previous diagnosis
    of dementia or other neurological disease, significant hearing loss, or blindness
    Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:oral_naming_improvement
  citation: '@Hillis2006'
  source_passages:
  - section: Original source P2-S4-C7
    page: 2
    quote: "The degree of improvement in oral naming of pictures was\nbest predicted\
      \ by the following model derived from the stepwise\nlinear regression, where\
      \ IN stands for improvement in naming\naccuracy and RP stands for “reperfusion\
      \ of” as defined above:\nIN \x02 RP BA 37 \x05 0.71 \x06 RP BA 44/45 \x05 0.25\
      \ \x06 RP BA 22 \x05 0.20\n\x06 0.13 (r \x02 0.81; p \x03 0.0001)."
    supports: claim
  - section: Original source P2-S4-C10
    page: 2
    quote: "This\nmodel indicates that reperfusion of left BA 37 (posterior middle\n\
      and inferior temporal/fusiform gyrus) was the strongest predic-\ntor of acute\
      \ improvement in picture naming after stroke ( p \x03\n0.0001)."
    supports: claim
  - section: Original source P2-S4-C11
    page: 2
    quote: "Reperfusion of left BA 44/45 (Broca’s area; p \x02 0.027)\nand reperfusion\
      \ of left BA 22 (Wernicke’s area; p \x02 0.047) also\nindependently contributed\
      \ to the prediction of early improve-\nment in naming after adjustment for each\
      \ other and for left BA 37\nreperfusion."
    supports: claim
  - section: Original source P2-S4-C12
    page: 2
    quote: 'Although improvement in some patients may have

      occurred with reperfusion of two or more of these areas, stepwise

      regression demonstrated that there was at least some indepen-

      dent contribution from each of these three areas in a multivariate

      model.'
    supports: claim
  - section: Original source P2-S3-C5
    page: 2
    quote: "Reperfusion of a given Brodmann’s area (BA) (an area of the brain\nwith\
      \ distinct cytoarchitecture) was defined as hypoperfusion of that re-\ngion\
      \ at day 1 and normal perfusion (\x034 s delay in TTP and at least 2 s\nimprovement\
      \ in TTP compared with day 1) and the absence of DWI\nabnormality in that area\
      \ at follow-up (days 3–5)."
    supports: method
  - section: Original source P2-S1-C3
    page: 2
    quote: "The current study was restricted to a subset of 87 patients who\nhad impaired\
      \ naming (as defined by accuracy in naming a set of pictures\n\x012 SDs that\
      \ of non-brain-damaged age-matched control subjects) and\nwho completed language\
      \ tests and imaging with both DWI and PWI at\nday 1 and days 3–5."
    supports: sample
  - section: Original source P1-S3-C5
    page: 1
    quote: 'The population consisted of a consecutive series of patients with

      acute left-hemisphere ischemic stroke who were admitted to Johns Hop-

      kins Hospital and met the following inclusion criteria: (1) right handed;

      (2) premorbidly proficient in English; (3) able to provide informed con-

      sent for the study or indicate a family member who provided informed

      consent; (4) no contraindication to MRI (e.g., implanted ferrous metal);

      and (5) no previous diagnosis of dementia or other neurological disease,

      significant hearing loss, or blindness.'
    supports: sample
  - section: Original source P2-S1-C6
    page: 2
    quote: 'Within 24 h of onset of stroke symptoms (day 1) and at

      days 3–5, patients were administered tests of oral naming of 17 pictured

      objects and 17 objects presented for tactile exploration; written naming

      of 17 pictured objects; repetition and spelling of 34 words; oral reading of

      34 words; visual and auditory lexical decision; and spoken and written

      word comprehension.'
    supports: method
predictor_type: imaging_metric
short_definition: A multivariate model based on the reperfusion of left Brodmann areas
  37, 44/45, and 22, where reperfusion is defined as hypoperfusion (>= 4s TTP delay)
  at day 1 followed by normal perfusion (<= 4s TTP delay and >= 2s improvement in
  TTP) and absence of DWI abnormality at days 3-5.
assessment:
- oral naming of pictures
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hillis2006
  proposal_id: R002
  review_status_sha256: b69bac43daef68f623b6d61c5985713822c0e1122721ba7189729f8212f3df6f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
        A/passages.json: c8aa6b810f4aef3bbcbba5c7b6e2ab477b0736d30d7fa80e302cf5e965734ef9
        A/raw.json: 9c36383c6b9257b7a9cb38b598a62d61d473cab44795e6615c39dbe7d8a9bdf9
        A/source-units.json: 80ed429b1db8b07b0d2f95686bb20d892a6f106f3c6b2ca3a15129b067e2787b
        A/full-source-units.json: c184b9653948d950dd7fc633403229a43d534f5071a7db938ca81d23b9fc711f
        A/meta.json: f36aaf82f06d696176b2c87bf064e30ba7d6f9a9c7172d08e1a93069b9e7ff63
        A/table-images/manifest.json: ad9c7e6fa90c00667ac35e3125389b616e5d6ca8e04a47f7f3e2d2c02e70f56c
        A/clauses/window-03/raw.json: 39eaaff000cda46d12ba642dd803194b87566872a23950847aebab3f26906df3
        A/clauses/window-03/prompt.txt: 346e7a2b109d8f71c8088fb39259bf2fdbb172889c8aa5aaef4134c63c504bde
        A/clauses/window-03/meta.json: ea7e2b8883c4a5af76ad9252db4771771fe92b42997f1f03f0baf45aae2c6b73
        A/clauses/window-04/raw.json: ae67d0127317a37a2c9c3a857a9407eec38edcc60b73a20b0480b7a06e321257
        A/clauses/window-04/prompt.txt: d53a2c99b80e155f8ded391cfd91a5a55b4a46a6ed3d3fcc5ae4281969e7b438
        A/clauses/window-04/meta.json: 86c71278e5e8181a96146238842d48a39990da6e70bf00ccd7ccf665f32311f3
        A/clauses/window-05/raw.json: 432af5520c941043df231dd5665ed13f5417da8b7b1ead85fdcde080bb4d0378
        A/clauses/window-05/prompt.txt: 4e963a5d6820e2ee92d3430b3fa7d60f0fa5a37e67a5fb44f742e7fe221f4930
        A/clauses/window-05/meta.json: 2e9eddd47728533001d14f78c416eb8591085a812f11b99baf8cb7897f7f4657
        A/clauses/window-02/raw.json: 6ac0c4b439fde892bdf0e31612eaae8a95187313a692dac97e5a3ffb52037365
        A/clauses/window-02/prompt.txt: a085d07e96c55055bc73fc73dad76bc9a0b879d8db39d702fc415827320abe49
        A/clauses/window-02/meta.json: 580066f67be4b4cc8238c4e26c58f28707e3d7368baa4004e3532f3a98020fad
        A/clauses/window-01/raw.json: d23c0bb1cb82caaf646ddc95588088db01df9d91e184d9348558f15c69a5ead0
        A/clauses/window-01/prompt.txt: 2ab775f6b9f50dbc90bd3329ad3134bb10f514e6611cd4f7dd01b109f301a5e3
        A/clauses/window-01/meta.json: 4226bf067df181870eaab06f5b83e2ff2e7060bdf092876239af4d518640f8d4
        B/passages.json: c8aa6b810f4aef3bbcbba5c7b6e2ab477b0736d30d7fa80e302cf5e965734ef9
        B/raw.json: cb910f42c585610464a34bf163665c222240446f13f061de239c02012a7c6513
        B/source-units.json: 80ed429b1db8b07b0d2f95686bb20d892a6f106f3c6b2ca3a15129b067e2787b
        B/full-source-units.json: c184b9653948d950dd7fc633403229a43d534f5071a7db938ca81d23b9fc711f
        B/meta.json: f2ffd31543a22bba41569e11e42b7abdd541d0a3cdb52b98a23db3d6e27505f3
        B/table-images/manifest.json: ad9c7e6fa90c00667ac35e3125389b616e5d6ca8e04a47f7f3e2d2c02e70f56c
        B/clauses/window-03/raw.json: 46abd323b7c4f4d74af292432569f32b813107a4e15f5b9580d3dc8ad82f70fe
        B/clauses/window-03/prompt.txt: 346e7a2b109d8f71c8088fb39259bf2fdbb172889c8aa5aaef4134c63c504bde
        B/clauses/window-03/meta.json: 9c0a62d6e3059e3869459cb78be8d677b4e7352bd7aa13cb1b3d0534b0f4a3f3
        B/clauses/window-04/raw.json: 43c32dde99d31a4aa77a001560c10c5a2a6fdb4f09b88978ee331f9477f4fa80
        B/clauses/window-04/prompt.txt: d53a2c99b80e155f8ded391cfd91a5a55b4a46a6ed3d3fcc5ae4281969e7b438
        B/clauses/window-04/meta.json: ff0476966677107a689abd0009d9ff039a50209b360c4b7b65e6476e44d82da1
        B/clauses/window-05/raw.json: 9eccbcb23264e92891a4f710452ccd053021c6eaab01445d39839890ac5484e9
        B/clauses/window-05/prompt.txt: 4e963a5d6820e2ee92d3430b3fa7d60f0fa5a37e67a5fb44f742e7fe221f4930
        B/clauses/window-05/meta.json: 0909724cd432b42e876026b47899fdab27864e34b043d39deecd39b2e4b794cd
        B/clauses/window-02/raw.json: 344977f17a3f71fdbbce6ec54ccf8fe6b1af4adc2e9eecc1695b8a1795739e5b
        B/clauses/window-02/prompt.txt: a085d07e96c55055bc73fc73dad76bc9a0b879d8db39d702fc415827320abe49
        B/clauses/window-02/meta.json: 49741161a7378033263091ea204a14644e3342d2df616dfcd1eac5bed070805b
        B/clauses/window-01/raw.json: d1f424364a807cb7623a9b3b0e66f3a8fcb4c70c9551c8254104c3b9968fc1ce
        B/clauses/window-01/prompt.txt: 2ab775f6b9f50dbc90bd3329ad3134bb10f514e6611cd4f7dd01b109f301a5e3
        B/clauses/window-01/meta.json: 02af461fc18e39efd36225a89e46d1384eb58cc2eb1801297cee8cd1abddc007
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
      pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2006
      source_status_sha256: e0502377586628ca92dd1c3ad68aa8bc58c1fab20aa41487700245e486fa2a7f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: Reperfusion of left BA 37, BA 44/45, and BA 22
    outcome:
      text: Improvement in oral naming of pictures
    analysis_label: Multivariate model for oral naming improvement
    relation: association
    evidence_ids:
    - P2-S4-C11
    - P2-S4-C12
    qualifier_ids:
    - P2-S5-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2006
      source_status_sha256: e0502377586628ca92dd1c3ad68aa8bc58c1fab20aa41487700245e486fa2a7f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C5'
      - 'window 1: invalid/duplicate disposition P1-S1-C6'
      - Result passage disposed without unit P2-S2-C3
      - Result passage disposed without unit P2-S4-C4
      - Result passage disposed without unit P3-S1-C6
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C9
      unattached_null_or_qualifier_ids:
      - P2-S4-C4
      - P3-S1-C6
      - P4-S2-C4
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 93
      unselected_timing_passages:
      - P1-S3-C5
      - P2-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S4-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
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
        - P2-S5
        - P3-S1
        - P3-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2006
      source_status_sha256: e0502377586628ca92dd1c3ad68aa8bc58c1fab20aa41487700245e486fa2a7f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes initial imaging of patients with impaired naming.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of study objective.
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Abstract summary of the regression and multivariate findings.
    - source_id: P1-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of study purpose.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of spontaneous reperfusion in untreated patients.
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming accuracy.
    - source_id: P2-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive range of day 1 scores.
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive range of follow-up scores.
    - source_id: P2-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Percentage of patients showing improvement.
    - source_id: P2-S4-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Provides the stepwise linear regression model for naming improvement.
    - source_id: P2-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains exclusion of non-significant areas from the model.
    - source_id: P2-S4-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies BA 37 as the strongest predictor in the model.
    - source_id: P2-S4-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes independent contribution of BA 44/45 and BA 22 after adjustment.
    - source_id: P2-S4-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Confirms independent contribution of the three areas in a multivariate
        model.
    - source_id: P2-S5-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports 100% of BA 37 reperfusion patients showed improvement.
    - source_id: P2-S5-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports improvement rate in patients who failed to reperfuse BA 37.
    - source_id: P2-S5-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes which areas reperfused in the 17% of BA 37 non-reperfused
        improvers.
    - source_id: P2-S5-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of the likelihood of practice effects.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Null finding for BA 37 reperfusion and general language task improvement.
    - source_id: P3-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Provides the regression model for spoken word comprehension improvement.
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Qualifies BA 22 as the only significant area for comprehension improvement.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive summary of voxel overlap in Figure 2.
    - source_id: P3-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of the independent association of the three areas.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological justification for the study design.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Argument against reorganization as the cause of improvement.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of the study's utility.
    unresolved_coverage:
    - source_id: P3-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C7
    - P1-S1-C8
    - P1-S3-C3
    - P2-S2-C3
    - P2-S4-C3
    - P2-S4-C4
    - P2-S4-C5
    - P2-S4-C6
    - P2-S4-C9
    - P2-S4-C10
    - P2-S5-C4
    - P2-S5-C5
    - P3-S1-C4
    - P3-S1-C6
    - P3-S1-C8
    - P3-S3-C3
    - P4-S2-C2
    - P4-S2-C4
    - P4-S2-C9
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
      - P2-S1-C3
      recruited_sample:
      - P2-S1-C2
      eligibility:
      - P1-S3-C5
      - P2-S1-C3
      imaging_provenance:
      - P2-S2-C10
      - P2-S3-C2
      - P2-S3-C5
      - P2-S3-C6
      imaging_timing:
      - P1-S1-C5
      - P1-S1-C6
      - P2-S1-C3
      - P2-S2-C5
      outcome_timing:
      - P2-S1-C3
      - P2-S1-C6
      - P2-S4-C3
      - P3-S1-C3
      outcome_definition:
      - P2-S3-C5
      - P2-S3-C7
      - P2-S4-C7
      - P3-S1-C3
      validation: []
      analysis_restrictions:
      - P2-S3-C9
      dependent_variable_statement:
      - P2-S3-C7
      limitations:
      - P3-S3-C5
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C6
      - P4-S1-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S4-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C3
      - P2-S4-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S4-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C8
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
      pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
      review_sha256: b69bac43daef68f623b6d61c5985713822c0e1122721ba7189729f8212f3df6f
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
      - P2-S4-C11
      - P2-S4-C12
      source_result: Reperfusion of left BA 44/45 and left BA 22 independently contributed
        to the prediction of early improvement in oral naming after adjustment for
        each other and for left BA 37 reperfusion, as part of a multivariate model
        where BA 37 was the strongest predictor.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the multivariate stepwise linear
            regression model described in P2-S4-C7, C10, C11, and C12, which predicts
            improvement in oral naming from reperfusion of specific Brodmann areas.
          source_ids:
          - P2-S4-C7
          - P2-S4-C11
          - P2-S4-C12
        direction:
          answer: fits
          reason: The source explicitly states that reperfusion of these areas 'contributed
            to the prediction' and 'independently contributed', indicating a detected
            positive association with improvement, which aligns with the draft's claim
            of a predictive model.
          source_ids:
          - P2-S4-C11
          - P2-S4-C12
        construct:
          answer: fits
          reason: The exposure is correctly identified as reperfusion of left BA 37,
            44/45, and 22. The outcome is improvement in oral naming. The measurement
            method is correctly identified as template_lesion_overlap, as the source
            describes transferring hypoperfusion/lesion regions to Brodmann's and
            MNI atlases (P2-S2-C10, P2-S3-C2) and defining reperfusion based on these
            mapped regions (P2-S3-C5).
          source_ids:
          - P2-S3-C5
          - P2-S2-C10
          - P2-S4-C11
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that BA 37 was the
            strongest predictor and that BA 44/45 and BA 22 contributed independently
            after adjustment. This matches the source text in P2-S4-C10 and P2-S4-C11.
          source_ids:
          - P2-S4-C10
          - P2-S4-C11
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the subset of patients.
            No other material caveats that change the interpretation of the core relationship
            are omitted. The source notes that the model was derived from a specific
            subset, which is captured.
          source_ids:
          - P2-S1-C3
          - P2-S4-C12
      optional_pending:
      - Specific p-values and coefficients for the model are not transcribed in the
        draft but are present in the source (P2-S4-C7, P2-S4-C11).
      - Sample size (n=87) is mentioned in source P2-S1-C3 but not explicitly in the
        draft's sample_n field.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values and coefficients for the model are not transcribed in the
      draft but are present in the source (P2-S4-C7, P2-S4-C11).
    - Sample size (n=87) is mentioned in source P2-S1-C3 but not explicitly in the
      draft's sample_n field.
    normalizations:
    - field: sample.n
      original: 87
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R002
      exposure:
        text: Reperfusion of left BA 37, BA 44/45, and BA 22
      outcome:
        text: Improvement in oral naming of pictures
      analysis_label: Multivariate model for oral naming improvement
      relation: association
      evidence_ids:
      - P2-S4-C11
      - P2-S4-C12
      qualifier_ids:
      - P2-S5-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2006
        source_status_sha256: e0502377586628ca92dd1c3ad68aa8bc58c1fab20aa41487700245e486fa2a7f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cb3142360d8d853b194423836de28f77f0ffb05191e92b31091fd98749510610
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C7
          page: 2
          text_layer_sha256: cb3142360d8d853b194423836de28f77f0ffb05191e92b31091fd98749510610
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The degree of improvement in oral naming of pictures was\n\
          best predicted by the following model derived from the stepwise\nlinear\
          \ regression, where IN stands for improvement in naming\naccuracy and RP\
          \ stands for “reperfusion of” as defined above:\nIN \x02 RP BA 37 \x05 0.71\
          \ \x06 RP BA 44/45 \x05 0.25 \x06 RP BA 22 \x05 0.20\n\x06 0.13 (r \x02\
          \ 0.81; p \x03 0.0001)."
        anchor_text: "The degree of improvement in oral naming of pictures was\nbest\
          \ predicted by the following model derived from the stepwise\nlinear regression,\
          \ where IN stands for improvement in naming\naccuracy and RP stands for\
          \ “reperfusion of” as defined above:\nIN \x02 RP BA 37 \x05 0.71 \x06 RP\
          \ BA 44/45 \x05 0.25 \x06 RP BA 22 \x05 0.20\n\x06 0.13 (r \x02 0.81; p\
          \ \x03 0.0001)."
        excluded_fragments: []
      P2-S4-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fb6f704dea223853176d0a3b943c5ebf46bd7d6ccd241158c9a3ff44240d5a03
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C10
          page: 2
          text_layer_sha256: fb6f704dea223853176d0a3b943c5ebf46bd7d6ccd241158c9a3ff44240d5a03
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "This\nmodel indicates that reperfusion of left BA 37 (posterior\
          \ middle\nand inferior temporal/fusiform gyrus) was the strongest predic-\n\
          tor of acute improvement in picture naming after stroke ( p \x03\n0.0001)."
        anchor_text: "This\nmodel indicates that reperfusion of left BA 37 (posterior\
          \ middle\nand inferior temporal/fusiform gyrus) was the strongest predic-\n\
          tor of acute improvement in picture naming after stroke ( p \x03\n0.0001)."
        excluded_fragments: []
      P2-S4-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 278d48a2194b4916b91c7431f806e0ad1887f0d3d78bc9f6ac9dbb5771c7f140
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C11
          page: 2
          text_layer_sha256: 278d48a2194b4916b91c7431f806e0ad1887f0d3d78bc9f6ac9dbb5771c7f140
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Reperfusion of left BA 44/45 (Broca’s area; p \x02 0.027)\n\
          and reperfusion of left BA 22 (Wernicke’s area; p \x02 0.047) also\nindependently\
          \ contributed to the prediction of early improve-\nment in naming after\
          \ adjustment for each other and for left BA 37\nreperfusion."
        anchor_text: "Reperfusion of left BA 44/45 (Broca’s area; p \x02 0.027)\n\
          and reperfusion of left BA 22 (Wernicke’s area; p \x02 0.047) also\nindependently\
          \ contributed to the prediction of early improve-\nment in naming after\
          \ adjustment for each other and for left BA 37\nreperfusion."
        excluded_fragments: []
      P2-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1d6f6494eb27a7f589163455fb4d3f20896d214baa98c23089e56b012a4e8f0b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C5
          page: 2
          text_layer_sha256: 1d6f6494eb27a7f589163455fb4d3f20896d214baa98c23089e56b012a4e8f0b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Reperfusion of a given Brodmann’s area (BA) (an area of the\
          \ brain\nwith distinct cytoarchitecture) was defined as hypoperfusion of\
          \ that re-\ngion at day 1 and normal perfusion (\x034 s delay in TTP and\
          \ at least 2 s\nimprovement in TTP compared with day 1) and the absence\
          \ of DWI\nabnormality in that area at follow-up (days 3–5)."
        anchor_text: "Reperfusion of a given Brodmann’s area (BA) (an area of the\
          \ brain\nwith distinct cytoarchitecture) was defined as hypoperfusion of\
          \ that re-\ngion at day 1 and normal perfusion (\x034 s delay in TTP and\
          \ at least 2 s\nimprovement in TTP compared with day 1) and the absence\
          \ of DWI\nabnormality in that area at follow-up (days 3–5)."
        excluded_fragments: []
      P2-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1a2148381e60d14d4db40c4015cf06b4ca3a2accffaa705d1f56452031a5f66f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C3
          page: 2
          text_layer_sha256: 1a2148381e60d14d4db40c4015cf06b4ca3a2accffaa705d1f56452031a5f66f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The current study was restricted to a subset of 87 patients\
          \ who\nhad impaired naming (as defined by accuracy in naming a set of pictures\n\
          \x012 SDs that of non-brain-damaged age-matched control subjects) and\n\
          who completed language tests and imaging with both DWI and PWI at\nday 1\
          \ and days 3–5."
        anchor_text: "The current study was restricted to a subset of 87 patients\
          \ who\nhad impaired naming (as defined by accuracy in naming a set of pictures\n\
          \x012 SDs that of non-brain-damaged age-matched control subjects) and\n\
          who completed language tests and imaging with both DWI and PWI at\nday 1\
          \ and days 3–5."
        excluded_fragments: []
      P1-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f74a5e5cf8d9b2dbad23e9e39bfa8043325d4770ff947be6f33d08e2ca8996df
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4593dc4d05cd70e56ae03ad9c7fbb94819d2e33828a4ea86d340340301fb019b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C5
          page: 1
          text_layer_sha256: 4593dc4d05cd70e56ae03ad9c7fbb94819d2e33828a4ea86d340340301fb019b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The population consisted of a consecutive series of patients
          with

          acute left-hemisphere ischemic stroke who were admitted to Johns Hop-

          kins Hospital and met the following inclusion criteria: (1) right handed;

          (2) premorbidly proficient in English; (3) able to provide informed con-

          sent for the study or indicate a family member who provided informed

          consent; (4) no contraindication to MRI (e.g., implanted ferrous metal);

          and (5) no previous diagnosis of dementia or other neurological disease,

          significant hearing loss, or blindness.'
        anchor_text: 'The population consisted of a consecutive series of patients
          with

          acute left-hemisphere ischemic stroke who were admitted to Johns Hop-

          kins Hospital and met the following inclusion criteria: (1) right handed;

          (2) premorbidly proficient in English; (3) able to provide informed con-

          sent for the study or indicate a family member who provided informed

          consent; (4) no contraindication to MRI (e.g., implanted ferrous metal);

          and (5) no previous diagnosis of dementia or other neurological disease,

          significant hearing loss, or blindness.'
        excluded_fragments: []
        image_sha256: 27ff467a12702db2f27942e1ddda6e052f7c02c0d17aca284598d8a31b5d6040
        transcription: '. The population consisted of a consecutive series of patients
          with acute left-hemisphere ischemic stroke who were admitted to Johns Hopkins
          Hospital and met the following inclusion criteria: (1) right handed; (2)
          premorbidly proficient in English; (3) able to provide informed consent
          for the study or indicate a family member who provided informed consent;
          (4) no contraindication to MRI (e.g., implanted ferrous metal); and (5)
          no previous diagnosis of dementia or other neurological disease, significant
          hearing loss, or blindness'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: "The degree of improvement in oral naming of pictures was\nbest predicted\
    \ by the following model derived from the stepwise\nlinear regression, where IN\
    \ stands for improvement in naming\naccuracy and RP stands for “reperfusion of”\
    \ as defined above:\nIN \x02 RP BA 37 \x05 0.71 \x06 RP BA 44/45 \x05 0.25 \x06\
    \ RP BA 22 \x05 0.20\n\x06 0.13 (r \x02 0.81; p \x03 0.0001)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
