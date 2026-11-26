---
id: time_since_stroke
name: time since stroke
kind: classical
findings:
- id: f1
  target: depression_severity
  target_kind: impairment
  claim: In the full model, depression severity did not significantly change over time; however, sensitivity analyses excluding outliers revealed a small overall reduction in severity relative to baseline, with a small increase in severity specifically at 12-months post-stroke.
  direction: mixed
  relationship: correlational
  method: meta-analysis
  sample:
    n: not_reported
    population: Stroke survivors aged 18 years or older not undergoing treatment interventions; the review excluded samples with aphasia or other communication impairments.
    phase: not_reported
    time_post_onset: baseline within 10 weeks of stroke; follow-up up to 60 months
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - excluded patients with aphasia or other communication impairments
  - limited to participants functionally capable of completing self-report measures
  - potential for differential dropout rates
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Time elapsed since stroke onset, with baseline measures recorded within the first 10 weeks (acute/subacute stage) and follow-up assessments ranging from 2 weeks to 60 months. full model showed no significant change and time was not a significant moderator; overall reduction and 12-month increase were found only after excluding outliers in sensitivity analyses. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P2-S3-C7, two-model agreement, human verification pending): . Inclusion criteria required that studies involved a sample

    of stroke survivors aged 18 years or older, with depression severity

    measured using a self-report scale at two or more time points Original text-layer quotation is preserved below. PDF image reading (P2-S3-C8, two-model agreement, human verification pending): . Other inclusion criteria involved baseline depression recorded within 10 weeks of stroke (acute/subacute stage) to compare future timepoints with acute/subacute stages of stroke, and medical documentation confirming stroke diagnosis Original text-layer quotation is preserved below. PDF image reading (P2-S4-C14, two-model agreement, human verification pending): Results


    Of 2,244 studies, 41 studies including 6,979 stroke patients met inclusion criteria (see Fig. 1 and Table 1) Original text-layer quotation is preserved below. PDF image reading (P3-S1-C1, two-model agreement, human verification pending): severity from a multitude of depression self-report measures (see

    Table 1) across 14 different times post-stroke onset, ranging from 2

    weeks to 60 months post-stroke Original text-layer quotation is preserved below. Publication correction (human verification pending): Restored the material exclusion of aphasia and communication impairments; this result is not directly generalizable to aphasia.'
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
    - proposed_concept:depression_severity
    - publication_correction_pending_human_verification
  citation: '@Thurston2026'
  source_passages:
  - section: Original source P1-S1-C11
    page: 1
    quote: "Results: In the full model including all eligible studies, depression severity did not significantly change over time, \nand time since stroke was not a significant moderator."
    supports: claim
  - section: Original source P1-S1-C12
    page: 1
    quote: "However, sensitivity analyses excluding studies identified \nas outliers revealed a small but significant overall reduction in depression severity (95 % CI [−0.123, –0.030]; p \n= 0.002), and a small increase in depression severity at 12-months post-stroke (95 % CI [0.006, 0.374]; p =\n0.043)."
    supports: claim
  - section: Original source P2-S3-C7
    page: 2
    quote: "Inclusion criteria required that studies involved a sample \nof stroke survivors aged 18 years or older, with depression severity \nmeasured using a self-report scale at two or more time points."
    supports: sample
  - section: Original source P2-S3-C8
    page: 2
    quote: "Other \ninclusion criteria involved baseline depression recorded within 10 \nweeks of stroke (acute/subacute stage) to compare future timepoints \nwith acute/subacute stages of stroke, and medical documentation con­\nfirming stroke diagnosis."
    supports: method
  - section: Original source P2-S4-C14
    page: 2
    quote: 'Results

      Of 2,244 studies, 41 studies including 6,979 stroke patients met in­

      clusion criteria (see Fig. 1 and Table 1).'
    supports: sample
  - section: Original source P3-S1-C1
    page: 3
    quote: "\nseverity from a multitude of depression self-report measures (see \nTable 1) across 14 different times post-stroke onset, ranging from 2 \nweeks to 60 months post-stroke."
    supports: method
  - section: Original source P3-S1-C8
    page: 3
    quote: "The meta-analysis of longitudinal depression \nseverity in stroke survivors across all timepoints showed no overall \nsignificant improvement in depression severity relative to baseline (p =\n0.075, SMC = −0.078, 95 % CI [−0.165, 0.008]; see Supplemental Fig. \n1), however a within-study effect was found (p = 0.026, SMC = −0.074, \n95 % CI [−0.138, –0.009]), and no between-study effect (p = 0.075, \nSMC = −0.078, 95 % CI [−0.165, 0.008])."
    supports: claim
  - section: Original source P3-S1-C13
    page: 3
    quote: "While a \ntime moderator analysis revealed no overall effect (p = 0.22), an in­\ncrease in depression severity at 12-months post-stroke was indicated (p \n= 0.043, SMC = 0.190, 95 % CI [0.0064, 0.374])."
    supports: claim
  - section: Original source P3-S2-C11
    page: 3
    quote: "In the full model that included all eligible studies, \ndepression severity did not significantly differ over time, and time since \nstroke was not a significant moderator."
    supports: claim
  - section: Original source P3-S2-C12
    page: 3
    quote: "However, sensitivity analyses \nrevealed a small but statistically significant overall reduction in \ndepression overtime with a brief increase in depression severity at 12- \nmonths post-stroke when outliers were excluded, suggesting a possible \ndeterioration effect that may be obscured in the presence of extreme \nvalues."
    supports: claim
  - section: Original source P6-S1-C4
    page: 6
    quote: "Importantly, our analysis is \nlimited to participants who were functionally capable of completing self- \nreport measures, and future research should explore how factors such as \nstroke severity and functional recovery interact with PSD symptom \nprogression."
    supports: limitation
  - section: Original source P6-S2-C12
    page: 6
    quote: "Finally, exclusion of patients suffering from aphasia-related \nsymptoms means that the observed pattern of PSD may not generalize \nto this important subgroup."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Thurston2026
  proposal_id: R001
  review_status_sha256: 2d268e12dfadf1d01ab171169150e790fcea55b896adce77a5ae6abc5e040381
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
        A/passages.json: 7d7d41baeb21a9dfa15571c9b48c77851360aebc498360d9bebb67427c06d82f
        A/raw.json: 68414eba4dbf3f5d116afc2893a43ead388ed0856dc43674e32fe6d0f9f7191a
        A/source-units.json: 0829b9a231d363d9ba5aa00d6f6910f4a214a6d9076e02637c9023cde7d160a1
        A/full-source-units.json: 3951416ba9d594a9da93dc63fe253c6117a164ec81c8e27626f7752b5c4a852c
        A/meta.json: 70ffd94cccd492980e5327bbf8a8eb16dc4123059c083d9a8c44aea3d8b5ccf0
        A/table-images/TABLE-1-page-4-2.png: 11be43cd6df567bdbf3272a3f64eebfe31afd61c48489da38874cf5417c39c73
        A/table-images/page-4.png: 89f859514cfa67b3942382ed699957aab68253135398facb3bfbab1f206bfdde
        A/table-images/TABLE-1-page-4-1.png: fb0493eef1da161bd98f6fddbe6a04aa717c008179a63ed82b9873ef6c85db68
        A/table-images/manifest.json: 990ea1b9a10922846d66f26487fec3a3ed244a7fb38392ce11675ccbe4e07307
        A/clauses/window-03/raw.json: 981cfc666e4cdc2d910fa28cf7c8518fa37c8d12ee32a34e4ebb3e50f19dcfa8
        A/clauses/window-03/prompt.txt: 8ab0662f1bfefdcebf03b90c9740e74f7b74630edaa981153f32c41a9d0986f9
        A/clauses/window-03/meta.json: 0896016b1ed279ce908c745775debc0b8d42722f6562bb976f490ac35246b15d
        A/clauses/window-04/raw.json: 3c3a5b0a8efbf3c38f6a10f4f9ea30085cd42c7782e902f4c78c7ed0d0c7a427
        A/clauses/window-04/prompt.txt: db413b6381280ceb0ce1062ae168fe88dcd511273c63e01a350d0e3c9d1cec3a
        A/clauses/window-04/meta.json: 555eb3b08851bb06d0c54f55ce748590e380abe7a7c777c4c77ef5c089417be3
        A/clauses/window-05/raw.json: 5878714a7cd756389deba65700093a58310c509949e6e0e845190d5a314ea072
        A/clauses/window-05/prompt.txt: ba2d3f089a780ba7bf22a899754e8c023660435da40087f4aad3d9fb5ca91c0c
        A/clauses/window-05/meta.json: 4f5cd7cc7fb7f252c95c12b79f16feac9cba743c11277ed16ce814d69e887b5d
        A/clauses/window-02/raw.json: b6acbdf7d91c86eb20c0ee0888c0ea4d3b0d79002fffb490ae0816d123745e03
        A/clauses/window-02/prompt.txt: 70a28d7dc3d8ba46444a5d6b765aa7e2108b7f8d15fec0c643453b7d372092a0
        A/clauses/window-02/meta.json: 084e021ae6024a0653f969c77a8e0f61762d54f112ad6469e4e7abf080747d25
        A/clauses/window-01/raw.json: fb4af1b0dbaeb935d81a3f23d0b068d54955baf160c1ae5bb80da820a0402977
        A/clauses/window-01/prompt.txt: 0cdc2ec5ddaa01fe5766d1406e3400cadb0f6d55180d4cc8584fe10196e241b0
        A/clauses/window-01/meta.json: 4ecb2ec330d877442d1b2ce408659f44cbd401565bddb1bce723fe1052277b41
        A/clauses/window-06/raw.json: 124b8da49bc93158ce918a176076765992729c9968d3c90ffe651c270c134f41
        A/clauses/window-06/prompt.txt: 7e202c214e4416043fded6b6f4569107686e25f545dcd402f4705de55781d2cd
        A/clauses/window-06/meta.json: bffd1a6dc26c8547f5384144b9a3dd1b408493fb6c95db193710b758c8888dc1
        A/tables/TABLE-1-page-4-1/raw.json: 04ce48fd42b18fa252695c224b5c17872f703c2134f9a6c536ea4f6fd75e3769
        A/tables/TABLE-1-page-4-1/prompt.txt: 4df770f59eb01aed938455b6630a2db9b59f59b4c194333ef170b134393d9d04
        A/tables/TABLE-1-page-4-1/meta.json: 8eaa42485aad20fa4e8c3ad0a2ea6a72bb2e77e5157c090603378484065c2da3
        B/passages.json: 7d7d41baeb21a9dfa15571c9b48c77851360aebc498360d9bebb67427c06d82f
        B/raw.json: 5ab987300706433130f53a51f7abb9dc5a1047c9ef90cefc43d428b4e9b6c3a7
        B/source-units.json: 0829b9a231d363d9ba5aa00d6f6910f4a214a6d9076e02637c9023cde7d160a1
        B/full-source-units.json: 3951416ba9d594a9da93dc63fe253c6117a164ec81c8e27626f7752b5c4a852c
        B/meta.json: fb98da269b892fc8884a6f8993650401cc286772a36b3cac8e6828ac6bc2a9cc
        B/table-images/TABLE-1-page-4-2.png: 11be43cd6df567bdbf3272a3f64eebfe31afd61c48489da38874cf5417c39c73
        B/table-images/page-4.png: 89f859514cfa67b3942382ed699957aab68253135398facb3bfbab1f206bfdde
        B/table-images/TABLE-1-page-4-1.png: fb0493eef1da161bd98f6fddbe6a04aa717c008179a63ed82b9873ef6c85db68
        B/table-images/manifest.json: 1ad075f365bdf1071c82e8f448acd1b05b68e0ba5e12220a66997a1c60630f92
        B/clauses/window-03/raw.json: 801f762045450f71eb354d2c7917d3919630d1bf85491563809be426b5d395aa
        B/clauses/window-03/prompt.txt: 8ab0662f1bfefdcebf03b90c9740e74f7b74630edaa981153f32c41a9d0986f9
        B/clauses/window-03/meta.json: 2cf8c03078df9799758f739b94045dda22e847ee5609e84f6c84468b1aafb7bb
        B/clauses/window-04/raw.json: 114fde2dd24ca9201152e5177f271413728f31b155b3e0a330acf994e2cf40f4
        B/clauses/window-04/prompt.txt: db413b6381280ceb0ce1062ae168fe88dcd511273c63e01a350d0e3c9d1cec3a
        B/clauses/window-04/meta.json: e78a53fe8dac83aa6d1dbd86c95e226d6cc18636936137318af273c50adf626a
        B/clauses/window-05/raw.json: daacffdde2e275e8b3e8c5986de777d969fcae672fc1ac273fa9e2cb43d8eec1
        B/clauses/window-05/prompt.txt: ba2d3f089a780ba7bf22a899754e8c023660435da40087f4aad3d9fb5ca91c0c
        B/clauses/window-05/meta.json: c91772540a24beaeb1215e907d6c0c7fd760ffb6c4666cfbf75c5ed86776e149
        B/clauses/window-02/raw.json: fd9f322806040ebddfe2f1f2fb368398560d6396ccdfae3f38c7e3a9f3621d83
        B/clauses/window-02/prompt.txt: 70a28d7dc3d8ba46444a5d6b765aa7e2108b7f8d15fec0c643453b7d372092a0
        B/clauses/window-02/meta.json: bf3b27116737e07c6fbe34c70764892af7159c0d6db23dde22eb18ac1eaac7c8
        B/clauses/window-01/raw.json: 5779be3141f9afaddca9952da02cd90801e9a443d35011a67c2a3ca2a139989d
        B/clauses/window-01/prompt.txt: 0cdc2ec5ddaa01fe5766d1406e3400cadb0f6d55180d4cc8584fe10196e241b0
        B/clauses/window-01/meta.json: 7665805463b5e92e55e030bf44c815c76d539205e662e7c67d056206123749f2
        B/clauses/window-06/raw.json: 7ba148c4b9841dc0b4b5561684cb0b16799985212c17e8996b64f89857d3c98c
        B/clauses/window-06/prompt.txt: 7e202c214e4416043fded6b6f4569107686e25f545dcd402f4705de55781d2cd
        B/clauses/window-06/meta.json: 19e8607ff480e3f885098f05576ee3cee278e96ade15021250843a6138fc3b32
        B/tables/TABLE-1-page-4-1/raw.json: 4df0b92213f706bb75f4b676e04091b60655d00162e315d55e839e1ac4b1a931
        B/tables/TABLE-1-page-4-1/prompt.txt: 4df770f59eb01aed938455b6630a2db9b59f59b4c194333ef170b134393d9d04
        B/tables/TABLE-1-page-4-1/meta.json: 345992a8509222a8f7b95c1cf18ece8f4d8cfdb16cb5a4a36cf3113cd362ebd6
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
      pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      source_review: _compare/relationships-2026-11-16/review-current/Thurston2026
      source_status_sha256: 22e0aa3ba70a1972597b0d16a935d3b36990043665dd301728919ea3a46de18f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: time since stroke
    outcome:
      text: depression severity
    analysis_label: Full model meta-analysis of longitudinal depression severity
    relation: association
    evidence_ids:
    - P1-S1-C11
    - P3-S1-C8
    - P3-S2-C11
    qualifier_ids:
    - P3-S1-C9
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      source_review: _compare/relationships-2026-11-16/review-current/Thurston2026
      source_status_sha256: 22e0aa3ba70a1972597b0d16a935d3b36990043665dd301728919ea3a46de18f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S2-C11
      - Accounting without a linked unit P3-S2-C12
      - Result passage disposed without unit P3-S2-C7
      - Result passage disposed without unit P3-S2-C8
      - Accounting without a linked unit P3-S3-C2
      - Accounting without a linked unit P3-S3-C4
      - Unaccounted source passage P3-S3-C4
      - Unaccounted source passage P3-S2-C12
      - Unaccounted source passage P3-S3-C2
      - Result passage disposed without unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C8
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C5
      - Unresolved source passage P6-S1-C11
      unattached_null_or_qualifier_ids:
      - P1-S2-C2
      - P3-S1-C5
      - P3-S2-C11
      - P3-S3-C2
      - P3-S3-C4
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 122
      unselected_timing_passages:
      - P2-S3-C7
      - P2-S3-C8
      - P3-S1-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: tested_personal_effects
        source_id: P4-S2-C5
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P4-S2-C6
        reason: No current-result classification; a covariate description is not an individual test
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S4
        - P3-S1
        - P3-S2
        - P3-S3
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      source_review: _compare/relationships-2026-11-16/review-current/Thurston2026
      source_status_sha256: 22e0aa3ba70a1972597b0d16a935d3b36990043665dd301728919ea3a46de18f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no significant change in depression severity over time in the full model.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports overall reduction and 12-month increase in depression severity in sensitivity analyses.
    - source_id: P1-S2-C2
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of sensitivity analysis findings in conclusions.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of timepoints removed for sensitivity analyses.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes effects of correlation coefficients on analysis.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no overall significant improvement in the full meta-analysis.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no moderation of time in the full model.
    - source_id: P3-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports heterogeneity statistics.
    - source_id: P3-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant improvement in depression severity in publication bias sensitivity analysis.
    - source_id: P3-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Provides within-study and between-study effects for publication bias sensitivity analysis.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports increase in depression severity at 12-months in time moderator analysis.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports heterogeneity for the sensitivity analysis.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no further variations in significance for other sensitivity analyses.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports Egger's test of asymmetry.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports general risk of bias assessment.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Details the number of studies by risk of bias level.
    - source_id: P3-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Restates that depression severity did not significantly differ over time in the full model.
    - source_id: P3-S2-C12
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Restates overall reduction and 12-month increase in sensitivity analyses.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses contradiction with previous literature.
    - source_id: P3-S3-C2
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of sensitivity results in discussion.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contrasts current findings with previous literature.
    - source_id: P4-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of sensitivity results in discussion.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretive statement about stability in first 3-6 months.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of gradual improvement in PSD severity.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on the inability to identify sub-classes of patients.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses how results inform hypotheses about timing.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports that correlation corrections did not change results.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports substantial heterogeneity.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of results in conclusion.
    unresolved_coverage:
    - source_id: P3-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C2
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C9
    - P3-S1-C10
    - P3-S2-C2
    - P3-S2-C3
    - P3-S2-C6
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C14
    - P3-S3-C2
    - P3-S3-C4
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C8
    - P6-S1-C6
    - P6-S1-C9
    - P6-S2-C2
    - P6-S2-C6
    - P6-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C14
      recruited_sample:
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      eligibility:
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C7
      - P2-S2-C9
      - P3-S1-C1
      - P3-S1-C3
      outcome_definition:
      - P2-S3-C13
      - P2-S3-C14
      - P3-S1-C8
      - P3-S1-C11
      - P3-S1-C13
      - P6-S3-C2
      validation: []
      analysis_restrictions:
      - P2-S3-C9
      - P2-S3-C10
      dependent_variable_statement: []
      limitations:
      - P6-S1-C4
      - P6-S1-C9
      - P6-S1-C11
      - P6-S2-C4
      - P6-S2-C10
      - P6-S2-C11
      - P6-S2-C12
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S4-C4
      - P2-S4-C6
      - P6-S2-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C7
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: tested_personal_effects
      source_id: P4-S2-C5
      reason: No current-result classification; a covariate description is not an individual test
    - slot: tested_personal_effects
      source_id: P4-S2-C6
      reason: No current-result classification; a covariate description is not an individual test
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Restored the material exclusion of aphasia and communication impairments; this result is not directly generalizable to aphasia.
    binding:
      source_pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      original_source_sha256: 8eef481ed4c9b3ab585e426982f1d34aa563399d07ddf598713822746e20a6a6
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=6979) is mentioned in source P2-S4-C14 but not transcribed into the core fields; this is optional metadata.
    - Specific statistical values (p-values, CIs) are not transcribed into the core fields, which is consistent with the qualitative draft requirement.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 6979
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R001
      exposure:
        text: time since stroke
      outcome:
        text: depression severity
      analysis_label: Full model meta-analysis of longitudinal depression severity
      relation: association
      evidence_ids:
      - P1-S1-C11
      - P3-S1-C8
      - P3-S2-C11
      qualifier_ids:
      - P3-S1-C9
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
        source_review: _compare/relationships-2026-11-16/review-current/Thurston2026
        source_status_sha256: 22e0aa3ba70a1972597b0d16a935d3b36990043665dd301728919ea3a46de18f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 37807c1085bdfc5313194948a96da3eff4d4a8d26af62176e2539cbfc3e93788
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C7
          page: 2
          text_layer_sha256: 37807c1085bdfc5313194948a96da3eff4d4a8d26af62176e2539cbfc3e93788
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Inclusion criteria required that studies involved a sample \nof stroke survivors aged 18 years or older, with depression severity \nmeasured using a self-report scale at two or more time points."
        anchor_text: "Inclusion criteria required that studies involved a sample \nof stroke survivors aged 18 years or older, with depression severity \nmeasured using a self-report scale at two or more time points."
        excluded_fragments: []
        image_sha256: eb7c5df95385f8264de5aef427c1b0003391d93bc88a1dc4ed81e0458b480473
        transcription: '. Inclusion criteria required that studies involved a sample

          of stroke survivors aged 18 years or older, with depression severity

          measured using a self-report scale at two or more time points'
      P2-S3-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d0a2fb5317c96c11578b9fd67088f6976331c22d52750dd85efdb71ee8b330e5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C8
          page: 2
          text_layer_sha256: d0a2fb5317c96c11578b9fd67088f6976331c22d52750dd85efdb71ee8b330e5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Other \ninclusion criteria involved baseline depression recorded within 10 \nweeks of stroke (acute/subacute stage) to compare future timepoints \nwith acute/subacute stages of stroke, and medical documentation con­\nfirming stroke diagnosis."
        anchor_text: "Other \ninclusion criteria involved baseline depression recorded within 10 \nweeks of stroke (acute/subacute stage) to compare future timepoints \nwith acute/subacute stages of stroke, and medical documentation con­\nfirming stroke diagnosis."
        excluded_fragments: []
        image_sha256: fe681f6f3961595998af32a8a75495f978d5e3be857428f81c0131e0a6821afd
        transcription: . Other inclusion criteria involved baseline depression recorded within 10 weeks of stroke (acute/subacute stage) to compare future timepoints with acute/subacute stages of stroke, and medical documentation confirming stroke diagnosis
      P2-S4-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f3997b2303fc9260a22d07143dc4f7e4cd112464efea1d75064b539c0e0803bd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C14
          page: 2
          text_layer_sha256: f3997b2303fc9260a22d07143dc4f7e4cd112464efea1d75064b539c0e0803bd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results

          Of 2,244 studies, 41 studies including 6,979 stroke patients met in­

          clusion criteria (see Fig. 1 and Table 1).'
        anchor_text: 'Results

          Of 2,244 studies, 41 studies including 6,979 stroke patients met in­

          clusion criteria (see Fig. 1 and Table 1).'
        excluded_fragments: []
        image_sha256: 0ed8e1f4c84d7d19da734623584a6e928946e45a20ca3d27fbb1a6444bbe7153
        transcription: 'Results


          Of 2,244 studies, 41 studies including 6,979 stroke patients met inclusion criteria (see Fig. 1 and Table 1)'
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f81059f3e7536e8712559c3f7982ffe24a83e09cfa3a5c739c42ce2f1e51c883
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: 57a71b002f76dd1247033732a21eedd3e6a10bab2d732ebc297ee4aac1f29b4a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "\nseverity from a multitude of depression self-report measures (see \nTable 1) across 14 different times post-stroke onset, ranging from 2 \nweeks to 60 months post-stroke."
        anchor_text: "severity from a multitude of depression self-report measures (see \nTable 1) across 14 different times post-stroke onset, ranging from 2 \nweeks to 60 months post-stroke."
        excluded_fragments: []
        image_sha256: 55b249c506a87e7453ab0a4ee12341784a4df0bc5bff4b2e250bbf1e92750188
        transcription: 'severity from a multitude of depression self-report measures (see

          Table 1) across 14 different times post-stroke onset, ranging from 2

          weeks to 60 months post-stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: 8eef481ed4c9b3ab585e426982f1d34aa563399d07ddf598713822746e20a6a6
      source_pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      pdf_pages:
      - 2
      - 6
      note: Restored the material exclusion of aphasia and communication impairments; this result is not directly generalizable to aphasia.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Restored the material exclusion of aphasia and communication impairments; this result is not directly generalizable to aphasia.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P1-S1-C11
      - P3-S1-C8
      - P3-S2-C11
      source_result: In the full model including all eligible studies, depression severity did not significantly change over time, and time since stroke was not a significant moderator. Sensitivity analyses excluding outliers revealed a small but significant overall reduction in depression severity and a small increase at 12-months post-stroke.
      result_status: mixed
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the full model meta-analysis of longitudinal depression severity. The source explicitly states that in this full model, depression severity did not significantly change and time was not a moderator. The proposed core correctly identifies this as the primary result while noting the sensitivity analysis findings as part of the mixed picture.
          source_ids:
          - P1-S1-C11
          - P3-S1-C8
          - P3-S2-C11
        direction:
          answer: fits
          reason: 'The claim accurately reflects the ''mixed'' nature of the findings: no significant change in the full model (null), but significant reduction and a specific increase at 12 months in sensitivity analyses. The directionality of the sensitivity findings (reduction overall, increase at 12 months) is preserved.'
          source_ids:
          - P1-S1-C11
          - P1-S1-C12
          - P3-S1-C13
        construct:
          answer: fits
          reason: The exposure is 'time since stroke' and the outcome is 'depression severity'. The measurement is correctly identified as non-imaging (self-report scales), as the study is a meta-analysis of clinical data, not neuroimaging. The population is stroke survivors not undergoing treatment. The method is meta-analysis.
          source_ids:
          - P2-S3-C7
          - P2-S3-C8
          - P2-S4-C14
        qualifications:
          answer: fits
          reason: The qualifications correctly state that the null result applies to the full model and that the significant findings (reduction/12-month increase) were found only after excluding outliers in sensitivity analyses. This distinction is crucial and accurately represented.
          source_ids:
          - P3-S1-C8
          - P3-S1-C11
          - P3-S2-C12
        missing_material_caveat:
          answer: fits
          reason: The draft includes key limitations such as the exclusion of patients with aphasia and the restriction to those capable of self-report. It also notes the preliminary nature of the findings. No material caveats that would change the interpretation of the core relationship are missing.
          source_ids:
          - P6-S1-C4
          - P6-S2-C12
          - P4-S1-C11
      optional_pending:
      - Sample size (n=6979) is mentioned in source P2-S4-C14 but not transcribed into the core fields; this is optional metadata.
      - Specific statistical values (p-values, CIs) are not transcribed into the core fields, which is consistent with the qualitative draft requirement.
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
      pdf_sha256: 86eb7eedc3f32fc039330154e0a35491360523286fbf799a14293f92964fe93a
      review_sha256: 2d268e12dfadf1d01ab171169150e790fcea55b896adce77a5ae6abc5e040381
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
  page: 1
  quote: "Results: In the full model including all eligible studies, depression severity did not significantly change over time, \nand time since stroke was not a significant moderator."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Restored the material exclusion of aphasia and communication impairments; this result is not directly generalizable to aphasia. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
