---
id: left_hemisphere_tract_fa
name: left hemisphere tract FA
kind: predictor
findings:
- id: f1
  target: left_hemisphere_cortical_thickness
  target_kind: impairment
  claim: mean FA values of the left hemisphere tracts were positively related to cortical
    thickness in the left hemisphere clusters related to the scores of auditory-verbal
    comprehension, spontaneous speech, and naming/word finding
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 32
    population: patients with chronic left subcortical stroke (ischemic or hemorrhagic)
      and history of aphasia
    phase: not_reported
    time_post_onset: over 6 months after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - cross-sectional investigation precludes empirical evidence of remote cortical
    atrophy mediated by neurodegeneration of connecting fiber tracts
  - DTI findings should be interpreted with caution
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: mean fractional anisotropy (FA) values of reconstructed
    white matter tracts connecting subcortical stroke lesions to identified cortical
    regions in the left hemisphere. analysis controlled for demographic variables
    and lesion size. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S2-C11, two-model agreement, human
    verification pending): Materials and methods


    Participants


    Thirty-two patients with chronic left subcortical stroke (ischemic or hemorrhagic)
    and history of aphasia were recruited with the following inclusion criteria: (i)
    Native Chinese speakers; (ii) over 6 months after stroke; (iii) unilateral subcortical
    lesion; (iv) ability to perform tests; and (v) absence of prior diagnosis of neurological
    disease Original text-layer quotation is preserved below.'
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
    - proposed_concept:left_hemisphere_cortical_thickness
  citation: '@Tang2022'
  source_passages:
  - section: Original source P7-S1-C5
    page: 7
    quote: 'The results showed that mean

      FA values of the left hemisphere tracts were positively related

      to cortical thickness in the left hemisphere clusters related

      to the scores of auditory-verbal comprehension [t(24) = 2.59,

      p = 0.016], spontaneous speech [t(24) = 2.58, p = 0.017],

      and naming/word ﬁnding [cluster 1: t(24) = 2.80, p = 0.010;

      cluster 2: t(24) = 2.74, p = 0.011].'
    supports: claim
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Materials and methods

      Participants

      Thirty-two patients with chronic left subcortical stroke

      (ischemic or hemorrhagic) and history of aphasia were recruited

      with the following inclusion criteria: (i) Native Chinese speakers;

      (ii) over 6 months after stroke; (iii) unilateral subcortical

      lesion; (iv) ability to perform tests; and (v) absence of prior

      diagnosis of neurological disease.'
    supports: sample
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Connections between the lesion and cortical ROIs or their

      mirrored homologs were reconstructed using the probabilistic

      tracking of crossing ﬁbers (probtrackx) and Bayesian estimation

      of diﬀusion parameters (bedpostx) algorithms implemented in

      FSL as previously described (Smith et al., 2004; Behrens et al.,

      2007).'
    supports: method
  - section: Original source P4-S1-C9
    page: 4
    quote: 'Thereafter, FA values of reconstructed connections were

      extracted for individual patients.'
    supports: method
  - section: Original source P7-S1-C4
    page: 7
    quote: 'The demographic variables,

      lesion size and FA values of connecting tracts were added to the

      models as independent factors.'
    supports: confounders
  - section: Original source P10-S2-C2
    page: 10
    quote: 'First,

      this is a cross-sectional investigation that might preclude

      the empirical evidence of remote cortical atrophy mediated

      by neurodegeneration of the connecting ﬁber tracts.'
    supports: limitation
  - section: Original source P10-S2-C4
    page: 10
    quote: 'Secondly, the DTI ﬁndings should be

      interpreted with caution.'
    supports: limitation
predictor_type: imaging_metric
short_definition: mean fractional anisotropy (FA) values of reconstructed white matter
  tracts connecting subcortical stroke lesions to identified cortical regions in the
  left hemisphere
assessment:
- DTI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Tang2022
  proposal_id: R011
  review_status_sha256: 31adbe281ea00eb7ba313dc37b9789f34a6b2f52ed43da11ad670c7faba52750
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
        A/passages.json: 03f5234be644eaa45398f0a2271c4a074695693b5c5a3420d0f2d51128291935
        A/raw.json: 1a63c5277617d752e2faf53b684ab3229a90982e701d2bf345c7d4053401ed87
        A/source-units.json: 02d140a7feae5aa4df0314e5694f11c1080f2b78b36615e40ad31bae33ed9176
        A/full-source-units.json: 04a3497d172c917edbe084191a913326aa22928a7b3718421fd532a790da7f45
        A/meta.json: 309ad4e0ada9c7a7a9bd4c0d1907e3a84fda16de7b78d0ec3d2123d9f8cf779b
        A/table-images/page-7.png: e8468f25b71b96e554aab652ba9e6ec29f3c8540df1db9590c0b990e025f723d
        A/table-images/page-4.png: a4cbabb47ba4bc5b26e0c1d346e3bbd3ae6d8c26f956565ad61911060828aa2b
        A/table-images/TABLE-1-page-4-1.png: 71e713c0c6f3449def147e4e11493e8817ba77824e277026bfaa483a58bf0930
        A/table-images/manifest.json: 23f238c793f50bc72860f777125b4bc15b30ef2d9fd1fbc4d780f3a79ea2f332
        A/table-images/TABLE-2-page-7-1.png: f808e6d04d88138cc87177c1ff578cab22e95ebac249f06d19557edb1f68cfaf
        A/clauses/window-03/raw.json: ad997f60f93fbf86a6131baf943cfb17c9fea24a4562ad45dbce69a92ebd16d2
        A/clauses/window-03/prompt.txt: 250396f097f93ea1212ef543f6eadd72d2078fd8c57a2a583e8b45be62816df3
        A/clauses/window-03/meta.json: a46af65f61166278ba713f89d9834af6e966a5b169e642cf6419805f3d984c01
        A/clauses/window-04/raw.json: 94ff2cb31fae3c9d904ad0aaf119a9b4d642db3d9cbc46d93b632990174abb0f
        A/clauses/window-04/prompt.txt: 5952087472bf7019f8b9adab1cb3002bec7233865ee1913e9e1bed247e1437fb
        A/clauses/window-04/meta.json: de756f2d16618967d234c0a04856d7ef9f7704209fb0955c247b77a950183f51
        A/clauses/window-05/raw.json: 55d1453a666c73c2fbb6c200969e83ab06d8661466223c4a09d920429d9521c5
        A/clauses/window-05/prompt.txt: 4800529dd5785ba7c8008cb8a25217d90aaac7b065182d0572195b6f4b3aeb42
        A/clauses/window-05/meta.json: ec06de0e7ea5aace975321934256ace871d0693db504ebcb262c9646e9775265
        A/clauses/window-02/raw.json: 1854735567505d02f2a7fdac2398540fa215e328e2d5ad2a6543e33841579c07
        A/clauses/window-02/prompt.txt: b99dee08fc7e9baf7d4bc8ec757dee0442be6644710203754bed352562fb485c
        A/clauses/window-02/meta.json: f5bed1f5ae76f5af15bba76661e30d91b183e105262923314396b35b5716b77d
        A/clauses/window-07/raw.json: 61d987777eea1e8d34212bcf9208e6e2e4417af8fea534bebc1b88f0a4b91416
        A/clauses/window-07/prompt.txt: 29aaf0cadd73939d4e5cd888541130c0d4d3ba7aeb2a92927c17239978c8e9de
        A/clauses/window-07/meta.json: 01c85c70945f8d7a2e2334d22ff291403578f5584f8b9e00511bc6fb8c3de874
        A/clauses/window-01/raw.json: b3eef6bda45291036346d5a250978c4cecbd94b77f0a109453f120d683aca130
        A/clauses/window-01/prompt.txt: ef16e2efc3f00ac30c21ef0ad2b7e35f6ae726b4f3d41e84de2e877e76763fec
        A/clauses/window-01/meta.json: 0f8e68d0345dcc8c57a89129f075ab09fde46abfde8cbd06fd7303f6027b0c26
        A/clauses/window-06/raw.json: c9d83022f97d8adf1ea99b64f6db508a8cd9f2a29d264438b868f07dcbeb6554
        A/clauses/window-06/prompt.txt: e01ea2d360b945e92bb863fef7fc017e384f872c602cc3a1e2938777edeface0
        A/clauses/window-06/meta.json: 9ddec6294291225b1ad93b067264029a9a1f206e52c628b2bcf0e79a37128d9c
        A/clauses/window-08/raw.json: cdb494911015638c4bb6f21bda224e37307e4fdf48e158b94d2277b7b2a9a96a
        A/clauses/window-08/prompt.txt: 3ccca943f11d8ee89f9a802a661ed7670db718663dc2392f97d37a9a66207785
        A/clauses/window-08/meta.json: 02268c3de9155118a9e6b636b4dfef0ac0b566484dd52a0096ac0a1fecfdbe07
        A/tables/TABLE-2-page-7-2/raw.json: f61b28f3518d717fc503a1d74457b57ad92b462dad3635b212d6b20744dc2993
        A/tables/TABLE-2-page-7-2/prompt.txt: a9fb411f152b5306e698adbe0cf692a67492e1f838dd77b4586d3f3e8a4891ee
        A/tables/TABLE-2-page-7-2/meta.json: 5efd00b2c7f420178aca105ad3c08021f2f23391871094a9bb36d8b169403480
        A/tables/TABLE-1-page-4-1/raw.json: b7a513464c3f8e5c100cf37c23b618d153e1bf7a3d3a2cc5650b50617866f1c3
        A/tables/TABLE-1-page-4-1/prompt.txt: 89bf1e8b029c17eaf49d807b115c94b1544ced0a8aa1fbbe2a67ec19c2b6fedf
        A/tables/TABLE-1-page-4-1/meta.json: f299629ccf600304d7e5b2e50e4f018c707489e5705e47484c1cf5812bb7c07c
        B/passages.json: 03f5234be644eaa45398f0a2271c4a074695693b5c5a3420d0f2d51128291935
        B/raw.json: a08b710c88c4bdc0fb7886d2a3cb9520bb2e90cce261c196994b7f84f7413257
        B/source-units.json: 02d140a7feae5aa4df0314e5694f11c1080f2b78b36615e40ad31bae33ed9176
        B/full-source-units.json: 04a3497d172c917edbe084191a913326aa22928a7b3718421fd532a790da7f45
        B/meta.json: a222f1abcc30612c02a0983ef3d19880acc038a1335542decea9ea1d9c14ffde
        B/table-images/page-7.png: e8468f25b71b96e554aab652ba9e6ec29f3c8540df1db9590c0b990e025f723d
        B/table-images/page-4.png: a4cbabb47ba4bc5b26e0c1d346e3bbd3ae6d8c26f956565ad61911060828aa2b
        B/table-images/TABLE-1-page-4-1.png: 71e713c0c6f3449def147e4e11493e8817ba77824e277026bfaa483a58bf0930
        B/table-images/manifest.json: 6df42184f5f49e2ede109ce7e27dffb28f3ddeff7b1250468b470942684727cc
        B/table-images/TABLE-2-page-7-1.png: f808e6d04d88138cc87177c1ff578cab22e95ebac249f06d19557edb1f68cfaf
        B/clauses/window-03/raw.json: 4708e397695b00985fa62da0a7a6d944ce767f32b60321a964f6309584c243ee
        B/clauses/window-03/prompt.txt: 250396f097f93ea1212ef543f6eadd72d2078fd8c57a2a583e8b45be62816df3
        B/clauses/window-03/meta.json: 8520574b2ae2f7d783a63b1796d1872350f7a31170798529231f2146cca4f973
        B/clauses/window-04/raw.json: 89ebd3acfeeff11af695913837f9927d7a85b19a72a8cdd44ab6949abf7fd386
        B/clauses/window-04/prompt.txt: 5952087472bf7019f8b9adab1cb3002bec7233865ee1913e9e1bed247e1437fb
        B/clauses/window-04/meta.json: cf5e6eb1d3ccd470d7bf3dcb1c998a274617d88bbf702e5df33a34548c9a7114
        B/clauses/window-05/raw.json: e04808206b817c5fc32a2469877a8b4a1a93bfea7f430321816f5db50a5d3c91
        B/clauses/window-05/prompt.txt: 4800529dd5785ba7c8008cb8a25217d90aaac7b065182d0572195b6f4b3aeb42
        B/clauses/window-05/meta.json: bbbc9742bbf3478fa6cbf2f217af0e315bda0faf4f3c2674320c2727b103418d
        B/clauses/window-02/raw.json: 9d00a3597bc9c762970861a62fbd1584c75367bcd0d9c9f80ebd8f1ca1727446
        B/clauses/window-02/prompt.txt: b99dee08fc7e9baf7d4bc8ec757dee0442be6644710203754bed352562fb485c
        B/clauses/window-02/meta.json: cdfb578180a7316507d1455aa3816af61fb9036274ec01c948bd6dfdc94d22d2
        B/clauses/window-07/raw.json: 4cd612d33c36e26d4286ec7a4bc1dba82ef61e4839d9e60dac1ba25daddda673
        B/clauses/window-07/prompt.txt: 29aaf0cadd73939d4e5cd888541130c0d4d3ba7aeb2a92927c17239978c8e9de
        B/clauses/window-07/meta.json: db0d807a38a7a44682985a1a97f214d4ceff94bc94d0baa0c3b3a23252c72e16
        B/clauses/window-01/raw.json: 786a26f7e0f212c0f91341181d11c184f623bb538fae6ed9f9f997e372f46562
        B/clauses/window-01/prompt.txt: ef16e2efc3f00ac30c21ef0ad2b7e35f6ae726b4f3d41e84de2e877e76763fec
        B/clauses/window-01/meta.json: 3024f71d098fd0fcee20cd6dec2701414088f17d2aacbac6c375ff7991fc3aae
        B/clauses/window-06/raw.json: 282470b45b852c09dcc039d44651277c8bca4ba9e24c68a94e231cb0344331c2
        B/clauses/window-06/prompt.txt: e01ea2d360b945e92bb863fef7fc017e384f872c602cc3a1e2938777edeface0
        B/clauses/window-06/meta.json: b15b3d19836542da89a013af755fe66882085de051c4671d506adf03b5277dc7
        B/clauses/window-08/raw.json: 54147bf2b7d49dbfef85b6537686651a448290344233f8ed431216dc7024445b
        B/clauses/window-08/prompt.txt: 3ccca943f11d8ee89f9a802a661ed7670db718663dc2392f97d37a9a66207785
        B/clauses/window-08/meta.json: 88399fa28ef9dee6960c46e381cd91d94d0e75ac9c7b778fa39d3931ac9d6a09
        B/tables/TABLE-2-page-7-2/raw.json: 028d94a126645e0286878e8d3507d10dea436fa8262f5347a18a92c2c570beaf
        B/tables/TABLE-2-page-7-2/prompt.txt: a9fb411f152b5306e698adbe0cf692a67492e1f838dd77b4586d3f3e8a4891ee
        B/tables/TABLE-2-page-7-2/meta.json: 17ea35ad6bac0b239ffab3296d10b96aa0aadcf61a00af00d5cc9a78ba486402
        B/tables/TABLE-1-page-4-1/raw.json: 6b72d787615e4ed31ec551880c67b74795202a5005aeee3bab35f2785c96d717
        B/tables/TABLE-1-page-4-1/prompt.txt: 89bf1e8b029c17eaf49d807b115c94b1544ced0a8aa1fbbe2a67ec19c2b6fedf
        B/tables/TABLE-1-page-4-1/meta.json: d34b9f6561aae7ea3c9bff4453f6c74fd68b1dc3cc971cd4d6d027428e437d1b
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
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      source_review: _compare/relationships-2026-11-16/review-current/Tang2022
      source_status_sha256: c25152622bcadbcb3131773c5a4933ad3695b3fb651198304fc89c5a6b96d4fc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R011
    exposure:
      text: mean FA values of left hemisphere tracts
    outcome:
      text: cortical thickness in left hemisphere clusters (auditory-verbal comprehension,
        spontaneous speech, and naming/word finding)
    analysis_label: Hierarchical regression of tract integrity and cortical thickness
    relation: association
    evidence_ids:
    - P7-S1-C5
    qualifier_ids:
    - P7-S1-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      source_review: _compare/relationships-2026-11-16/review-current/Tang2022
      source_status_sha256: c25152622bcadbcb3131773c5a4933ad3695b3fb651198304fc89c5a6b96d4fc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C6
      - Accounting without a linked unit P1-S2-C7
      - Accounting without a linked unit P1-S2-C8
      - Unaccounted source passage P1-S2-C7
      - Unaccounted source passage P1-S2-C8
      - Unaccounted source passage P1-S2-C6
      - Result passage disposed without unit P4-S2-C9
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C7
      - Accounting without a linked unit P5-S2-C8
      - Accounting without a linked unit P5-S2-C9
      - Accounting without a linked unit P5-S3-C2
      - Accounting without a linked unit P5-S3-C3
      - Accounting without a linked unit P5-S3-C4
      - Unaccounted source passage P5-S2-C9
      - Unaccounted source passage P5-S3-C4
      - Unaccounted source passage P5-S2-C7
      - Unaccounted source passage P5-S2-C8
      - Unaccounted source passage P5-S3-C2
      - Unaccounted source passage P5-S3-C3
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P7-S2-C10
      - Result passage disposed without unit P7-S2-C11
      - Result passage disposed without unit P7-S2-C13
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P9-S2-C13
      - Result passage disposed without unit P10-S3-C2
      - Accounting without a linked unit P10-S3-C3
      - Unaccounted source passage P10-S3-C3
      unattached_null_or_qualifier_ids:
      - P1-S2-C6
      - P5-S2-C7
      - P5-S2-C8
      - P5-S2-C9
      - P10-S1-C9
      suppressed_nonrepresented_units: 21
      default_disposition_count_requires_completeness_check: 161
      unselected_timing_passages:
      - P2-S2-C11
      - P5-S1-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P10-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C6
        - P4-S1-C11
        - P4-S2-C2
        - P4-S2-C3
        - P4-S2-C5
        - P5-S1-C5
        - P5-S1-C10
        - P5-S2-C6
        - P5-S2-C11
        - P6-S1-C3
        - P7-S1-C2
        - P7-S2-C5
        - P7-S2-C7
        - P7-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P7-S3-C1
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S1
        - P5-S1
        - P5-S2
        - P5-S3
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      source_review: _compare/relationships-2026-11-16/review-current/Tang2022
      source_status_sha256: c25152622bcadbcb3131773c5a4933ad3695b3fb651198304fc89c5a6b96d4fc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Abstract summary of cortical thickness and language outcomes.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Abstract summary of cortical thickness and fiber tract integrity.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 15
      reason: Abstract summary of perfusion status and cortical thickness.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes demographic table.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic statement.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Group difference in language scores based on demographics.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 16
      reason: SVR-LSM null result for subcortical regions.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation of education/lesion size with outcomes (supplementary).
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Association of left inferior parietal/superior temporal gyrus with comprehension.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Association of left orbitofrontal gyrus with spontaneous speech.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Association of left inferior precentral gyrus, pars orbitalis, and posterior
        cingulum with naming.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Naming association result.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Association of right lateral orbitofrontal cortex with naming.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about absence of negative relationships.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Lesion size as predictor without cortical thickness.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Cortical thickness as predictor in hierarchical model.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Right hemisphere cluster as predictor for naming.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Lower cortical thickness in patients for comprehension and speech clusters.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Lower cortical thickness in patients for naming clusters.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 9
      reason: No difference in right hemisphere cluster thickness.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: FA values of left tracts related to cortical thickness.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Null relationship for right hemisphere naming cluster and lesion size/tracts.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Lower FA in left vs right hemisphere homologs.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic differences between HP and NHP groups.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null difference in language performance between HP and NHP.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Reduction of cortical thickness in right cuneus for HP group.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 14
      reason: No difference in left hemisphere thickness between HP and NHP.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 15
      reason: No difference in individual language-related clusters between HP and
        NHP.
    - source_id: P7-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion restatement of results.
    - source_id: P7-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section heading/introductory text.
    - source_id: P8-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of auditory-verbal comprehension result.
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of speech outcome result.
    - source_id: P9-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of naming outcome result.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of right hemisphere naming result.
    - source_id: P9-S2-C5
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of right hemisphere null difference.
    - source_id: P9-S2-C8
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Discussion restatement of cortical thickness reduction in patients.
    - source_id: P9-S2-C12
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of cortical thickness and tract integrity relationship.
    - source_id: P9-S2-C13
      disposition: repeated
      result_indexes:
      - 12
      reason: Discussion restatement of FA reduction in lesional hemisphere.
    - source_id: P10-S1-C9
      disposition: repeated
      result_indexes:
      - 15
      reason: Discussion restatement of null language difference between HP and NHP.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 14
      reason: Discussion restatement of null left hemisphere thickness difference
        between HP and NHP.
    - source_id: P10-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on feasibility of method.
    - source_id: P10-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage:
    - source_id: P5-S1-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C6
    - P1-S2-C7
    - P1-S2-C8
    - P4-S2-C9
    - P5-S1-C1
    - P5-S1-C5
    - P5-S1-C9
    - P5-S2-C2
    - P5-S2-C4
    - P5-S3-C5
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C9
    - P7-S2-C10
    - P7-S2-C11
    - P7-S2-C13
    - P7-S3-C1
    - P8-S1-C7
    - P9-S1-C7
    - P9-S1-C9
    - P9-S1-C11
    - P9-S2-C3
    - P9-S2-C5
    - P9-S2-C8
    - P9-S2-C12
    - P9-S3-C4
    - P10-S1-C9
    - P10-S3-C2
    - P10-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C3
      recruited_sample:
      - P2-S3-C2
      - P2-S3-C3
      eligibility:
      - P2-S3-C2
      - P2-S3-C3
      imaging_provenance:
      - P3-S1-C4
      - P3-S1-C11
      - P3-S2-C6
      - P4-S1-C3
      imaging_timing:
      - P2-S3-C9
      outcome_timing:
      - P2-S3-C2
      outcome_definition:
      - P2-S3-C7
      - P2-S3-C8
      validation: []
      analysis_restrictions:
      - P3-S1-C9
      - P4-S1-C12
      - P6-S1-C3
      dependent_variable_statement:
      - P4-S1-C11
      - P4-S2-C2
      - P5-S2-C5
      limitations:
      - P10-S2-C2
      - P10-S2-C4
      - P10-S2-C5
      - P10-S2-C8
      - P10-S2-C10
      - P10-S2-C11
      - P10-S2-C13
      personal_factors:
      - P4-S2-C10
      - P5-S1-C10
      - P7-S1-C2
      tested_personal_effects:
      - P5-S1-C9
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C10
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P10-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C6
      - P4-S1-C11
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C5
      - P5-S1-C5
      - P5-S1-C10
      - P5-S2-C6
      - P5-S2-C11
      - P6-S1-C3
      - P7-S1-C2
      - P7-S2-C5
      - P7-S2-C7
      - P7-S2-C8
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
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      review_sha256: 31adbe281ea00eb7ba313dc37b9789f34a6b2f52ed43da11ad670c7faba52750
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
      - P7-S1-C5
      source_result: In patients with chronic left subcortical stroke, mean FA values
        of left hemisphere tracts connecting subcortical lesions to cortical clusters
        were positively associated with cortical thickness in left hemisphere clusters
        related to auditory-verbal comprehension, spontaneous speech, and naming/word
        finding, after controlling for demographic variables and lesion size.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the hierarchical regression
            of tract integrity (FA) and cortical thickness described in P7-S1-C5 and
            P7-S1-C4, matching the proposed core's analysis label and evidence.
          source_ids:
          - P7-S1-C5
          - P7-S1-C4
        direction:
          answer: fits
          reason: The source explicitly states a positive relationship between mean
            FA values and cortical thickness (P7-S1-C5), which aligns with the 'likely'
            direction and positive association in the proposed core.
          source_ids:
          - P7-S1-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as mean FA of left hemisphere
            tracts (P7-S1-C5, P4-S1-C9) and the outcome as cortical thickness in specific
            left hemisphere clusters (P7-S1-C5). The measurement is patient-specific
            diffusion (FA) and structural (cortical thickness), not template overlap.
          source_ids:
          - P7-S1-C5
          - P4-S1-C9
          - P3-S2-C5
        qualifications:
          answer: fits
          reason: The proposed core correctly includes the qualification that the
            analysis controlled for demographic variables and lesion size, as stated
            in P7-S1-C4 and P6-S1-C3.
          source_ids:
          - P7-S1-C4
          - P6-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes the key limitations regarding the cross-sectional
            design (P10-S2-C2) and the caution required for DTI findings (P10-S2-C4),
            which are material to interpreting the causal or structural implications
            of the association.
          source_ids:
          - P10-S2-C2
          - P10-S2-C4
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R011
      exposure:
        text: mean FA values of left hemisphere tracts
      outcome:
        text: cortical thickness in left hemisphere clusters (auditory-verbal comprehension,
          spontaneous speech, and naming/word finding)
      analysis_label: Hierarchical regression of tract integrity and cortical thickness
      relation: association
      evidence_ids:
      - P7-S1-C5
      qualifier_ids:
      - P7-S1-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
        source_review: _compare/relationships-2026-11-16/review-current/Tang2022
        source_status_sha256: c25152622bcadbcb3131773c5a4933ad3695b3fb651198304fc89c5a6b96d4fc
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: da1454c174521790c8f17177989affe8946c4f61efe9da641a9e0594a849827f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C11
          page: 2
          text_layer_sha256: da1454c174521790c8f17177989affe8946c4f61efe9da641a9e0594a849827f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and methods

          Participants

          Thirty-two patients with chronic left subcortical stroke

          (ischemic or hemorrhagic) and history of aphasia were recruited

          with the following inclusion criteria: (i) Native Chinese speakers;

          (ii) over 6 months after stroke; (iii) unilateral subcortical

          lesion; (iv) ability to perform tests; and (v) absence of prior

          diagnosis of neurological disease.'
        anchor_text: 'Materials and methods

          Participants

          Thirty-two patients with chronic left subcortical stroke

          (ischemic or hemorrhagic) and history of aphasia were recruited

          with the following inclusion criteria: (i) Native Chinese speakers;

          (ii) over 6 months after stroke; (iii) unilateral subcortical

          lesion; (iv) ability to perform tests; and (v) absence of prior

          diagnosis of neurological disease.'
        excluded_fragments: []
        image_sha256: b9764febe95c4673594a69b80e2ffb1cd30b81a036badf735b43e5c83b2fbe34
        transcription: 'Materials and methods


          Participants


          Thirty-two patients with chronic left subcortical stroke (ischemic or hemorrhagic)
          and history of aphasia were recruited with the following inclusion criteria:
          (i) Native Chinese speakers; (ii) over 6 months after stroke; (iii) unilateral
          subcortical lesion; (iv) ability to perform tests; and (v) absence of prior
          diagnosis of neurological disease'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'The results showed that mean

    FA values of the left hemisphere tracts were positively related

    to cortical thickness in the left hemisphere clusters related

    to the scores of auditory-verbal comprehension [t(24) = 2.59,

    p = 0.016], spontaneous speech [t(24) = 2.58, p = 0.017],

    and naming/word ﬁnding [cluster 1: t(24) = 2.80, p = 0.010;

    cluster 2: t(24) = 2.74, p = 0.011].'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
