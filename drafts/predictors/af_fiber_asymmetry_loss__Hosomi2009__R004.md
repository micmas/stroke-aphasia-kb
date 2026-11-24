---
id: af_fiber_asymmetry_loss
name: loss of leftward asymmetry in number of AF fibers
kind: predictor
findings:
- id: f1
  target: aphasia_at_discharge
  target_kind: prognosis
  claim: Loss of leftward asymmetry in the number of arcuate fasciculus fibers predicted
    aphasia at discharge.
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 13
    population: right-handed patients with left middle cerebral artery infarcts
    phase: not_reported
    time_post_onset: imaging performed within 48 hours after stroke onset; outcome
      measured at discharge
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - retrospective review
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Loss of leftward asymmetry in the number of arcuate
    fasciculus fibers, measured by an asymmetry index ((L-R)/(L+R)) using diffusion
    tensor tractography with three ROIs covering the unilateral AF. aphasia at discharge
    was defined as an NIHSS best language score >= 1. Additional metadata has not
    been transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S1-C12, two-model agreement, human verification pending): Subjects


    We carried out a retrospective review of the records of 13 consecutive right-handed
    patients (six women and seven men; median age 72.8 years; age range 41–85) with
    left MCA infarcts identified on MRI within 48 h after stroke onset (mean 17.7
    h; range 3–44) Original text-layer quotation is preserved below. PDF image reading
    (P2-S2-C4, two-model agreement, human verification pending): . Using the

    best language score of the National Institute of Health

    Stroke Scale (NIHSS) at discharge, these patients were

    divided into two groups: an aphasic group (NIHSS best

    language score$\ge$1) and a nonaphasic group (score 0) [13] Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:aphasia_at_discharge
  citation: '@Hosomi2009'
  source_passages:
  - section: Original source P4-S1-C7
    page: 4
    quote: "Loss of leftward asymmetry in number of AF fibers \npredicted aphasia\
      \ at discharge with a sensitivity of 0.83 \nand specificity of 0.86. \nleft\
      \ \nPatient #10 \n84F \nNHISS \n9 \nnon-aphasic \nasymmetry was observed in\
      \ the number of AF fibers (asymmetry \n"
    supports: claim
  - section: Original source P2-S1-C12
    page: 2
    quote: "Subjects \nWe carried out a retrospective review of the records of 13\
      \ \nconsecutive right-handed patients (six women and seven \nmen; median age\
      \ 72.8 years; age range 41-85) with left \nMCA infarcts identified on MRI within\
      \ 48 h after stroke \nonset (mean 17.7 h; range 3-44)."
    supports: sample
  - section: Original source P2-S2-C4
    page: 2
    quote: "Using the \nbest language score of the National Institute of Health \n\
      Stroke Scale (NIHSS) at discharge, these patients were \ndivided into two groups:\
      \ an aphasic group (NIHSS best \nlanguage score>1) and a nonaphasic group (score\
      \ 0) [13]."
    supports: claim
  - section: Original source P3-S1-C9
    page: 3
    quote: "In order to compare AF fiber tracts intraindividually, an \nasymmetry\
      \ index was calculated for both the FA and \nnumber of AF fibers as (L—R)/(L+R),\
      \ where L and R are \nthe numbers or FA values of AF fibers on the left and\
      \ right \nsides, respectively [4]."
    supports: method
  - section: Original source P2-S3-C11
    page: 2
    quote: "When tracking the AF, we placed three ROIs so that they \ncovered the\
      \ unilateral AF (Fig. 1)."
    supports: method
  - section: Original source P6-S2-C11
    page: 6
    quote: "First, the \nnumber of patients was somewhat limited."
    supports: limitation
  - section: Original source P6-S2-C13
    page: 6
    quote: "Second, this study \nwas performed in retrospective fashion."
    supports: limitation
predictor_type: imaging_metric
short_definition: Loss of leftward asymmetry in the number of arcuate fasciculus fibers,
  measured by an asymmetry index ((L-R)/(L+R)) using diffusion tensor tractography
  with three ROIs covering the unilateral AF.
assessment:
- diffusion tensor tractography
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hosomi2009
  proposal_id: R004
  review_status_sha256: b15bcae5a8a3378642c8fcab82197c58623ef96e3974a137fd8906e988c386da
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
        A/passages.json: 90bca0e9a7822ee4d0c3b7f091f871bd93f5a3284c3088c0cb27e2044689820b
        A/raw.json: 87920df2a1ac61f97c47928b1c879644626f90bc7b435ea4229c245dcf86f17d
        A/source-units.json: c0b6c5734cd436d740064b8eb453fdd34417e91cc8de3c22fdb508fac1f4e7c2
        A/full-source-units.json: b258a44e5be73448527fe532d3cff614e1445132eb4514748efabee9e0b2d1af
        A/meta.json: a487707df1e0a78a2094410d86e56617cc46c00f15c63e51bcae866b4458c32a
        A/table-images/page-4.png: 55c01d3679c42c2684fa038a150d7a025e6aad512ebf9b2fbf7ba09a686718e2
        A/table-images/TABLE-1-page-4-1.png: 4d0dc5d87a3dd3286013cfaab8c89be92beb3a001f06adcf8a76ca4bc84dda60
        A/table-images/manifest.json: c09ffc21dc2ec8031dc2392cb04e787db9ad94fc2923c9fe3e7e5d6810e201dc
        A/clauses/window-03/raw.json: 2e319c93aa565cdfc1370c080945d39f4563f77d56b80933be867bade2fb3e49
        A/clauses/window-03/prompt.txt: 133b405ae7d378306b24d4d4ecdd32a34a60fac16f79ee8e3bd848d1e30cdb1f
        A/clauses/window-03/meta.json: 1a2716998249c3708b3900762d63c80490a243d3b2bc0ebfa50348c8f54271d8
        A/clauses/window-04/raw.json: 24c9d244736a310413bd77ccd0fb1249f92664c7e360115eb37d445b0d1253bd
        A/clauses/window-04/prompt.txt: fefb1b5bb02be6a4c8471638f876e1fccc94ad35cdc80072f2ad00286118b68b
        A/clauses/window-04/meta.json: ab4a284dd309228bc18970e78cca3445c82f555cf914cdc8f71c83db553bbe52
        A/clauses/window-05/raw.json: 2c1bec5bc75b54ba37653fb1a450a199e4699fb39393f93ecf5e8e680136dc31
        A/clauses/window-05/prompt.txt: d3fb72944b937a2a443c84a2efe06ae2a28464c495167396d6c092cb3c2ab2fa
        A/clauses/window-05/meta.json: 1da78cfb467654ae8d36ca5589f5608ed27ac02c1b57e96010272f82b6388e93
        A/clauses/window-02/raw.json: 71afd5032eedcc1b7b2edfbc33c772641433ee16ea1a346788ece1f4fdab3518
        A/clauses/window-02/prompt.txt: 91abff7e486364b5dc31acb51df9c9168bbbb2a848f9e0a9ff4736ecf7b125d2
        A/clauses/window-02/meta.json: d2532a723d47a66b3b8db79bbc93224817e3c44ba7a6220deea0c702acee24db
        A/clauses/window-01/raw.json: e9b4940bec5aec43b1aa1f7877a0f9d8b9bf302e62666fafe81a801a98a9cf8c
        A/clauses/window-01/prompt.txt: 757553087ec1554f9a664d0767e41375b018471b847354e336563f701b46aa49
        A/clauses/window-01/meta.json: 505cf66e5642954f1c1175b947389282101768db88ee07ee4df17aff0d00ed41
        A/tables/TABLE-1-page-4-1/raw.json: b5bda902d4d61ad19cac5c21f5558e2de2ffea24d82df2bdb86dc1ff7293f640
        A/tables/TABLE-1-page-4-1/prompt.txt: acc52d7ce88077f8a9cc818327e90d68d0f793bc05b66addface896c4688c664
        A/tables/TABLE-1-page-4-1/meta.json: 8acbe7be92fabc1e067fe1650d1db5bf0476e5150aec420e3f23c61f643502fe
        B/passages.json: 90bca0e9a7822ee4d0c3b7f091f871bd93f5a3284c3088c0cb27e2044689820b
        B/raw.json: 27f95a1c25ed2d46161c0bbdc3ce8679bad7eed10d850c09067d46210c5ccc65
        B/source-units.json: c0b6c5734cd436d740064b8eb453fdd34417e91cc8de3c22fdb508fac1f4e7c2
        B/full-source-units.json: b258a44e5be73448527fe532d3cff614e1445132eb4514748efabee9e0b2d1af
        B/meta.json: 3f259f0836bf5025451d2cbe43eb8ea8aae440ed3c226c542bec5a5969fdea47
        B/table-images/page-4.png: 55c01d3679c42c2684fa038a150d7a025e6aad512ebf9b2fbf7ba09a686718e2
        B/table-images/TABLE-1-page-4-1.png: 4d0dc5d87a3dd3286013cfaab8c89be92beb3a001f06adcf8a76ca4bc84dda60
        B/table-images/manifest.json: ee626913ac6b69f247d5f924c450899dcf5d8fdd0b9fc9259ea1cbca1164d4b1
        B/clauses/window-03/raw.json: 20c4e5592386841cd825b6a1a7d10f20695bf67d1e0ec18b3792e1469dd5b7e2
        B/clauses/window-03/prompt.txt: 133b405ae7d378306b24d4d4ecdd32a34a60fac16f79ee8e3bd848d1e30cdb1f
        B/clauses/window-03/meta.json: 36d7f215983197fba7bb635d8c7eb0347574a0f80b6f6ef58859bc6c52aa9e54
        B/clauses/window-04/raw.json: 6d76e9dcf19bdf090c1a2254f9dce6a067cfba3ed87ae9c61abec10767d1fd72
        B/clauses/window-04/prompt.txt: fefb1b5bb02be6a4c8471638f876e1fccc94ad35cdc80072f2ad00286118b68b
        B/clauses/window-04/meta.json: b5e37a47f0aaf82f09946837da29465ba0ca0fafd848a4576c8686bf15e1b8ac
        B/clauses/window-05/raw.json: 2c1bec5bc75b54ba37653fb1a450a199e4699fb39393f93ecf5e8e680136dc31
        B/clauses/window-05/prompt.txt: d3fb72944b937a2a443c84a2efe06ae2a28464c495167396d6c092cb3c2ab2fa
        B/clauses/window-05/meta.json: d3862d9ce7651dc45bb76f23509fa45bf2af1466a075dd142815f1f6711eacf6
        B/clauses/window-02/raw.json: 0616dec1d4f8a22b5cfe9943477c47165634bb4c8f9bc4fdc2164a35d922c845
        B/clauses/window-02/prompt.txt: 91abff7e486364b5dc31acb51df9c9168bbbb2a848f9e0a9ff4736ecf7b125d2
        B/clauses/window-02/meta.json: 0ab8ceaa6af483b80b4033380db6bb64ba9eb20251bda9eb7c2b5949ccf76a08
        B/clauses/window-01/raw.json: 8fae309352065b8ed11bd7d2cc1d520ba213f2260397510c15ce4820bb753130
        B/clauses/window-01/prompt.txt: 757553087ec1554f9a664d0767e41375b018471b847354e336563f701b46aa49
        B/clauses/window-01/meta.json: c84a15443f83fc0da44a3c39266e055898ac609d3f4fe7b69aeacf8341c76913
        B/tables/TABLE-1-page-4-1/raw.json: c64cf3ac082f4ad8752156b4af380b6086d4868a4ee29a80ffe40d17b1df7a15
        B/tables/TABLE-1-page-4-1/prompt.txt: acc52d7ce88077f8a9cc818327e90d68d0f793bc05b66addface896c4688c664
        B/tables/TABLE-1-page-4-1/meta.json: 8b8409b7db505cf400483bb363e09c4dfb378403b30887751f1ad37f21d7d036
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
      pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
      source_review: _compare/relationships-2026-11-16/review-current/Hosomi2009
      source_status_sha256: 1af6633211d5ac0902a66139fa939fbeb2472161d9ba0e448d5cad1c2be835d4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: loss of leftward asymmetry in number of AF fibers
    outcome:
      text: aphasia at discharge
    analysis_label: Aphasia prediction model
    relation: performance
    evidence_ids:
    - P1-S2-C3
    - P4-S1-C7
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
      pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
      source_review: _compare/relationships-2026-11-16/review-current/Hosomi2009
      source_status_sha256: 1af6633211d5ac0902a66139fa939fbeb2472161d9ba0e448d5cad1c2be835d4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C17
      - Accounting without a linked unit P1-S2-C2
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C17
      - Unaccounted source passage P1-S1-C10
      - Unaccounted source passage P1-S2-C2
      - Accounting without a linked unit P2-S2-C4
      - Unaccounted source passage P2-S2-C4
      - Result passage disposed without unit P3-S2-C6
      - Accounting without a linked unit P3-S2-C7
      - Accounting without a linked unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C6
      - Unaccounted source passage P3-S2-C7
      - Unaccounted source passage P4-S1-C3
      - Result passage disposed without unit P4-S2-C4
      unattached_null_or_qualifier_ids:
      - P3-S2-C6
      - P4-S1-C2
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 92
      unselected_timing_passages:
      - P2-S2-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S2-C15
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S1
        - P3-S2
        - P4-S1
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
      source_review: _compare/relationships-2026-11-16/review-current/Hosomi2009
      source_status_sha256: 1af6633211d5ac0902a66139fa939fbeb2472161d9ba0e448d5cad1c2be835d4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no difference in FA values between hemispheres.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant leftward asymmetry in fiber number for controls
        and nonaphasic group.
    - source_id: P1-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Affiliation/date information.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports lower asymmetry index in aphasic group compared to others.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Provides sensitivity and specificity for predicting aphasia.
    - source_id: P3-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hospital stay duration is a descriptive characteristic.
    - source_id: P3-S1-C14
      disposition: represented
      result_indexes:
      - 6
      reason: Reports higher NIHSS in aphasic group.
    - source_id: P3-S1-C15
      disposition: represented
      result_indexes:
      - 7
      reason: Reports lower ASPECTS DWI in aphasic group (non-significant).
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides raw FA values for controls.
    - source_id: P3-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 4
      reason: Reports no asymmetry in FA and no difference in FA asymmetry index among
        groups.
    - source_id: P3-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports leftward asymmetry in fiber number for controls and nonaphasic
        group.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports lack of leftward asymmetry in aphasic group.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence to asymmetry index results.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant difference in asymmetry index between aphasic and
        other groups.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Restates sensitivity and specificity of the prediction.
    - source_id: P4-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case data.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 4
      reason: Restates FA results and the predictive value of AF asymmetry.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Reports no specific correlation between aphasia severity and infarct
        location.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Restates leftward asymmetry in nonaphasic/controls and lack thereof
        in aphasic group.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Restates rightward deviation of asymmetry index in aphasic group.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample size limitations.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports association between high admission NIHSS and persistent aphasia.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case example.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific case example.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on lesion size as a predictor.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Restates non-significant trend for ASPECTS DWI.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion on infarct location vs size.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Reports that FA did not exhibit a clear correlation with prognosis.
    unresolved_coverage:
    - source_id: P6-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C6
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P1-S1-C17
    - P3-S1-C13
    - P3-S2-C4
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S2-C1
    - P4-S2-C2
    - P4-S2-C3
    - P4-S2-C4
    - P6-S1-C1
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C4
      - P1-S1-C5
      - P2-S1-C12
      - P2-S2-C5
      recruited_sample:
      - P1-S1-C4
      - P1-S1-C5
      - P2-S1-C12
      - P2-S2-C5
      eligibility:
      - P1-S1-C4
      - P2-S1-C12
      imaging_provenance:
      - P2-S2-C8
      imaging_timing:
      - P1-S1-C4
      - P2-S1-C12
      outcome_timing:
      - P1-S1-C6
      - P2-S2-C4
      - P3-S1-C12
      - P4-S1-C7
      outcome_definition:
      - P1-S1-C6
      - P2-S2-C4
      - P3-S1-C12
      - P4-S1-C7
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations:
      - P6-S2-C11
      - P6-S2-C12
      - P6-S2-C13
      - P6-S2-C14
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C12
      - P2-S2-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S2-C15
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
      pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
      review_sha256: b15bcae5a8a3378642c8fcab82197c58623ef96e3974a137fd8906e988c386da
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
      - P1-S2-C3
      - P4-S1-C7
      source_result: Loss of leftward asymmetry in the number of arcuate fasciculus
        (AF) fibers, measured via diffusion tensor tractography, was associated with
        aphasia at discharge. The asymmetry index was significantly lower (rightward)
        in the aphasic group compared to nonaphasic and control groups. This metric
        predicted aphasia at discharge with a sensitivity of 0.83 and specificity
        of 0.86.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the predictive model described
            in the source where AF fiber asymmetry is used to predict aphasia status.
            The source explicitly states 'Loss of leftward asymmetry in number of
            AF fibers predicted aphasia at discharge' (P1-S2-C3, P4-S1-C7).
          source_ids:
          - P1-S2-C3
          - P4-S1-C7
        direction:
          answer: fits
          reason: The source indicates that the asymmetry index was significantly
            lower (rightward) in the aphasic group, meaning a loss of the typical
            leftward asymmetry is associated with aphasia. The draft's direction 'likely'
            (implying association/prediction) and the claim 'predicted aphasia' align
            with the source's finding of a significant association and reported sensitivity/specificity.
          source_ids:
          - P1-S2-C2
          - P1-S2-C3
          - P4-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as 'loss of leftward asymmetry
            in number of AF fibers' and the outcome as 'aphasia at discharge'. The
            measurement method is correctly identified as diffusion tensor tractography.
            The patient measurement is 'patient_diffusion' because the study involves
            performing DT tractography on the patients' own MRI data to count fibers
            and calculate asymmetry indices, rather than overlaying lesions on a pre-existing
            template map.
          source_ids:
          - P1-S1-C7
          - P1-S1-C8
          - P3-S1-C9
          - P2-S2-C4
        qualifications:
          answer: fits
          reason: The draft includes the qualification that aphasia was defined by
            NIHSS best language score >= 1, which matches the source (P2-S2-C4). The
            limitations (small sample, retrospective) are also correctly included.
            The population (right-handed, left MCA infarct) and timing (imaging <48h,
            outcome at discharge) are accurate.
          source_ids:
          - P2-S2-C4
          - P6-S2-C11
          - P6-S2-C13
          - P2-S1-C12
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key methodological details and limitations.
            The source notes that the study is preliminary and has a small sample
            size, which are included. There are no omitted material caveats that would
            change the interpretation of the predictive relationship.
          source_ids:
          - P6-S2-C10
          - P6-S2-C11
          - P6-S2-C13
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
      id: R004
      exposure:
        text: loss of leftward asymmetry in number of AF fibers
      outcome:
        text: aphasia at discharge
      analysis_label: Aphasia prediction model
      relation: performance
      evidence_ids:
      - P1-S2-C3
      - P4-S1-C7
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
        pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
        source_review: _compare/relationships-2026-11-16/review-current/Hosomi2009
        source_status_sha256: 1af6633211d5ac0902a66139fa939fbeb2472161d9ba0e448d5cad1c2be835d4
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e974cecbd24bff9657e5fbd4466c0e92e3104856c702fa12e6470203ae09c992
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C12
          page: 2
          text_layer_sha256: e974cecbd24bff9657e5fbd4466c0e92e3104856c702fa12e6470203ae09c992
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Subjects \nWe carried out a retrospective review of the records\
          \ of 13 \nconsecutive right-handed patients (six women and seven \nmen;\
          \ median age 72.8 years; age range 41-85) with left \nMCA infarcts identified\
          \ on MRI within 48 h after stroke \nonset (mean 17.7 h; range 3-44)."
        anchor_text: "Subjects \nWe carried out a retrospective review of the records\
          \ of 13 \nconsecutive right-handed patients (six women and seven \nmen;\
          \ median age 72.8 years; age range 41-85) with left \nMCA infarcts identified\
          \ on MRI within 48 h after stroke \nonset (mean 17.7 h; range 3-44)."
        excluded_fragments: []
        image_sha256: 4aa6437d5f90d607da9d0d896824b3c02a569a2e7fa77584fd9e76a5d022369a
        transcription: 'Subjects


          We carried out a retrospective review of the records of 13 consecutive right-handed
          patients (six women and seven men; median age 72.8 years; age range 41–85)
          with left MCA infarcts identified on MRI within 48 h after stroke onset
          (mean 17.7 h; range 3–44)'
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bd504e5ebde07d6af6ed28ff5258333ad10838b0bc9d96b495534e7c0e895c7a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: aea2bb26d8f2f67443f07c0bd141632d68fba587eba232711b46c6aef49e30fb
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: aea2bb26d8f2f67443f07c0bd141632d68fba587eba232711b46c6aef49e30fb
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Using the \nbest language score of the National Institute\
          \ of Health \nStroke Scale (NIHSS) at discharge, these patients were \n\
          divided into two groups: an aphasic group (NIHSS best \nlanguage score>1)\
          \ and a nonaphasic group (score 0) [13]."
        anchor_text: "Using the \nbest language score of the National Institute of\
          \ Health \nStroke Scale (NIHSS) at discharge, these patients were \ndivided\
          \ into two groups: an aphasic group (NIHSS best \nlanguage score>1) and\
          \ a nonaphasic group (score 0) [13]."
        excluded_fragments: []
        image_sha256: 5cda4047716f54bf925c72f5b3e6c65043cdfd8d65e9aa129f1f63335616780d
        transcription: '. Using the

          best language score of the National Institute of Health

          Stroke Scale (NIHSS) at discharge, these patients were

          divided into two groups: an aphasic group (NIHSS best

          language score$\ge$1) and a nonaphasic group (score 0) [13]'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "Loss of leftward asymmetry in number of AF fibers \npredicted aphasia at\
    \ discharge with a sensitivity of 0.83 \nand specificity of 0.86. \nleft \nPatient\
    \ #10 \n84F \nNHISS \n9 \nnon-aphasic \nasymmetry was observed in the number of\
    \ AF fibers (asymmetry \n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
