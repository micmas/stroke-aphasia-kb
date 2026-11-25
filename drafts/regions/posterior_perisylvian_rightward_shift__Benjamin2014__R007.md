---
id: posterior_perisylvian_rightward_shift
name: posterior perisylvian rightward shift
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: category_member_generation_gains
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: category_member_generation_gains
  target_kind: prognosis
  claim: In patients receiving Intention Treatment, a rightward shift in posterior
    perisylvian activity was significantly correlated with treatment gains for category-member
    generation.
  direction: likely
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 7
    population: Chronic (>6 months) aphasia patients with left-hemisphere ischemic
      or hemorrhagic strokes, predominantly with conduction aphasia in the IT group.
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
  - IT group was dominated by patients with conduction aphasia and significant posterior
    perisylvian damage
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Rightward shift in activity within the posterior perisylvian
    region of interest (constructed from the Harvard-Oxford atlas), measured as the
    change in laterality index from pretreatment to posttreatment fMRI during category
    member generation. Finding is specific to the Intention Treatment (IT) group;
    For the Control Treatment (CT) group, gains were only marginally associated with
    a leftward shift in the same region. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S2-C5, two-model
    agreement, human verification pending): Method


    Subjects


    Fourteen chronic (>6 months) aphasia patients participated Original text-layer
    quotation is preserved below. PDF image reading (P8-S1-C9, two-model agreement,
    human verification pending): . In the current study, IT patients were

    dominated by patients with conduction aphasia and had sig-

    nificant posterior perisylvian damage (see Supplemental

    Figure 1) Original text-layer quotation is preserved below. Reconcile this new
    analysis with earlier drafts and source-review decisions for the paper; new candidate
    IDs do not carry earlier decisions forward.'
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
    - proposed_concept:category_member_generation_gains
  therapy:
    id: intention_treatment
    name: Intention Treatment
  citation: '@Benjamin2014'
  source_passages:
  - section: Original source P6-S1-C8
    page: 6
    quote: "However, rightward shifts in pos-\nterior persylvian activity showed a\
      \ significant correlation \nwith treatment gains for IT (r = −0.86, n = 7, P\
      \ < .01), but \nfor CT, treatment gains were marginally associated with a \n\
      leftward shift in posterior perisylvian activity (r = 0.77, \nn = 6, P < .10)."
    supports: claim
  - section: Original source P4-S2-C2
    page: 4
    quote: "Three regions of interest (ROIs; medial \nfrontal, lateral frontal, and\
      \ posterior perisylvian) were con-\nstructed for each hemisphere by combining\
      \ regions from \nthe Harvard–Oxford atlas distributed with FSL (the anterior\
      \ \nmost portion of frontal polar cortex was eliminated from \nfrontal ROIs)."
    supports: method
  - section: Original source P4-S2-C3
    page: 4
    quote: "The volume of active cortex from each ROI \nwas extracted, and laterality\
      \ indices used the following for-\nmula (left − right)/(left + right); 1.0 represented\
      \ completely \nleft-lateralized activity, and −1.0 represented completely \n\
      right-lateralized activity."
    supports: method
  - section: Original source P4-S3-C5
    page: 4
    quote: "To \ndetermine the relationship between improvement during \ntreatment\
      \ and changes in laterality, Z scores for both pic-\nture-naming and category\
      \ probes were correlated with later-\nality \nshifts \nfrom \npre- \nto \nposttreatment\
      \ \nusing \na \nproduct–moment correlation for the lateral frontal, medial \n\
      frontal, and posterior perisylvian ROIs."
    supports: method
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Method

      Subjects

      Fourteen chronic (>6 months) aphasia patients participated.'
    supports: sample
  - section: Original source P2-S2-C7
    page: 2
    quote: "Patients were premor-\nbidly right-handed,16 used English as a first language,\
      \ and \nhad single or multiple left-hemisphere ischemic or hemor-\nrhagic strokes."
    supports: sample
  - section: Original source P8-S1-C9
    page: 8
    quote: "In the current study, IT patients were \ndominated by patients with conduction\
      \ aphasia and had sig-\nnificant posterior perisylvian damage (see Supplemental\
      \ \nFigure 1)."
    supports: limitation
  - section: Original source P4-S2-C13
    page: 4
    quote: "It assesses treatment gains \nfor individual-subject time series by evaluating\
      \ changes in \nslope from baseline to treatment relative to variability in \n\
      successive data points."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Benjamin2014
  proposal_id: R007
  review_status_sha256: c8c5e8a0ca775d302af2fa6c4001c53659b5d56fd685411fdaf58c38b23da95d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
        A/passages.json: bdb552d8c59fbc2410c6befd03ea73a3857b86686ff996f44029e9ca4fa01de9
        A/raw.json: c89b70106bde8af4b4ca69c9f90d27cb6078bef4482bf7146dc9fef7270d3a71
        A/source-units.json: 11adb8aa1f731d08488985bb89ddf379fbafc9826ea433ba80839c4cf244f905
        A/full-source-units.json: 3bc7f899cd1b38fee3134210518a4632d62cbfc270b0deb2d56b4df0d4b54a3f
        A/meta.json: 1e49916f9f570cfe709e68a0516c5c0c6213270a13a4282b4a95e3afdfd4392a
        A/table-images/TABLE-1-page-3-1.png: e81b2bef61f8457749ef03e5f4b72387b518782178f670fdac81e7c8c3ec88d9
        A/table-images/page-3.png: 6372652268ff796c770e10de1b0255a3ec0c84dce0d0d7e7325eb8c26aa5fd75
        A/table-images/manifest.json: 978c738f3a3d63a5c471ce2dba62d6c6eb8c7b6d647841181576fe35db12fe90
        A/clauses/window-03/raw.json: 689c67172bfa03a5580106d9ed79e36232ccb833d2e1e84a924393242bfa34d3
        A/clauses/window-03/prompt.txt: 0cb85e100562347d629269fbb54573f4fa40fc4b7a01e249274fc7aa15970982
        A/clauses/window-03/meta.json: b25657c8c53bf255c18d1044831d4f89f8bd28cad4b3ae7d15d0d0964ca716b2
        A/clauses/window-04/raw.json: ccbf4c9cb1fec78405ec503a4ce5f9f605d926c74dcac5ade9bbd7307f8501a8
        A/clauses/window-04/prompt.txt: 9d1b5cbf053aa26fc40b48584fac40ce3e46175a8038b2e34c9d93423fb8ff86
        A/clauses/window-04/meta.json: 32b0ae5b7d3e5cbe83a4dcd48753d1717d11f55a778df5e90fd681b0b1a2386f
        A/clauses/window-05/raw.json: 86a6630646cc166d201c861bcea03035dd94cf8bfeb425d5c4ba65df43481ef9
        A/clauses/window-05/prompt.txt: d00fffc6d682622c465627547b392ad5f74a12461002858deb792a003c0bbd99
        A/clauses/window-05/meta.json: 5dc936c7d427a14a50613ae2fa9fdeb3907d395ee90a484c483794681c425574
        A/clauses/window-02/raw.json: 3553ac56e934dac3871728a10c34abc4863a51a5822987cc94b9f4f285445d7c
        A/clauses/window-02/prompt.txt: bfafd41c095e540e2f7c0e9f0b28d1266af5344a4959fc68a4a6c5b17337b125
        A/clauses/window-02/meta.json: bb02c277a0f0d8807ca50734457a15d66b40e9c45811073ecdaa939d6e9aa86b
        A/clauses/window-07/raw.json: dac8d334c13b61aef7be606cb0409eb156e9e0ba78a10ed40ae4e94f98268d8d
        A/clauses/window-07/prompt.txt: c55d115967d21fc413b1e2d92cf32c2d5b9908fa6042d4d1a11b6caa65365b55
        A/clauses/window-07/meta.json: 100631d38148a8bf29914d3d6b70b2445d675fba787cc155a08c5a8d2f5316d7
        A/clauses/window-01/raw.json: 2710099e8d1f6df3f1b99121b5efd35c9bc4b407c77931a1f2c1ede28cf8b50c
        A/clauses/window-01/prompt.txt: 41ccba26620ca2cde1d2b0dd5570582c16fa6234d60b2cb1779bcefe76f92e1b
        A/clauses/window-01/meta.json: 26b887e4169c130e3c29138e400c7658f7529f01227948bd59853b3ee52ba368
        A/clauses/window-06/raw.json: 4d4240f935988a48a618791294f157ccacb25064d2763244a3ffb88d6aa157f2
        A/clauses/window-06/prompt.txt: 034e70436236e166af5c7112ac180d01b0f677ba4a5ee6b165953939fa656eeb
        A/clauses/window-06/meta.json: 2fa15f09c3d57159edfccdbe842008e6c292f7cdc42f3378cc907559ee8bb5db
        A/tables/TABLE-1-page-3-1/raw.json: 5f9e1c3a5c71097d8581910f8e0b1724d822d105f33562f1206ae34b945c11e8
        A/tables/TABLE-1-page-3-1/prompt.txt: 4f09019c265ded66fd22c9b23fdbe08c860c93be71ba75dc7dabb99cd2ec495a
        A/tables/TABLE-1-page-3-1/meta.json: c94c6d03a244d1a5d07a66891610614a7db89993df437c9fbad6ab6e8c4dcd00
        B/passages.json: bdb552d8c59fbc2410c6befd03ea73a3857b86686ff996f44029e9ca4fa01de9
        B/raw.json: 6d6b9eccff94af712e4d53aca3129b77f7a891f85d2b68fa9794191af81de897
        B/source-units.json: 11adb8aa1f731d08488985bb89ddf379fbafc9826ea433ba80839c4cf244f905
        B/full-source-units.json: 3bc7f899cd1b38fee3134210518a4632d62cbfc270b0deb2d56b4df0d4b54a3f
        B/meta.json: 6d37a50675f323f606f81fcef4b36b1e6128efb9581fd9f69b74c527e19e0e8e
        B/table-images/TABLE-1-page-3-1.png: e81b2bef61f8457749ef03e5f4b72387b518782178f670fdac81e7c8c3ec88d9
        B/table-images/page-3.png: 6372652268ff796c770e10de1b0255a3ec0c84dce0d0d7e7325eb8c26aa5fd75
        B/table-images/manifest.json: 2a5e8c09fe3cba87559acd0a9364d3824dd5bad45b0bb4678c9a6a211d3d375a
        B/clauses/window-03/raw.json: 7c55bec97c863ff90a103f19c789e0dc3ba686cce4d0d5fb7761ff3cba6273d9
        B/clauses/window-03/prompt.txt: 0cb85e100562347d629269fbb54573f4fa40fc4b7a01e249274fc7aa15970982
        B/clauses/window-03/meta.json: 7180ac2b76393f335452c5ad6abd0d9c6cfb071952cf0c51298a9e287405463f
        B/clauses/window-04/raw.json: a113ffedabe8824b8ce574730d0ce68e75eb319ae5859bebed647cfdb0e34bb6
        B/clauses/window-04/prompt.txt: 9d1b5cbf053aa26fc40b48584fac40ce3e46175a8038b2e34c9d93423fb8ff86
        B/clauses/window-04/meta.json: 20b7634d8ca9edfca7ef028faf441e6bfb79896293da896138ec88777b19f317
        B/clauses/window-05/raw.json: 73a2ae61ff7e01582d69f2becef10d86c0c6c3e3c891c27fc16050ca0746e86d
        B/clauses/window-05/prompt.txt: d00fffc6d682622c465627547b392ad5f74a12461002858deb792a003c0bbd99
        B/clauses/window-05/meta.json: b0e2be3b2f55ea2d39ab90f8a222adf28a5e4cf36ef821e63839f6f0ff0a7643
        B/clauses/window-02/raw.json: dd5c6529c64a36bf52574d9b7180e3d52ecd6557c1bf844a830654778a68acf9
        B/clauses/window-02/prompt.txt: bfafd41c095e540e2f7c0e9f0b28d1266af5344a4959fc68a4a6c5b17337b125
        B/clauses/window-02/meta.json: 083618b1c4c1ee348df3ed79b6cebd87edf9acac5759abb36fd97f9d6bf20755
        B/clauses/window-07/raw.json: 13ff11b8fa778a874cb781184847450672d2e132cfde6eb7a25c4d3bdea8c96c
        B/clauses/window-07/prompt.txt: c55d115967d21fc413b1e2d92cf32c2d5b9908fa6042d4d1a11b6caa65365b55
        B/clauses/window-07/meta.json: 459a61aca2c595bf64a34344d27965eae92fbad3a676a83727645ca80ec1a1d1
        B/clauses/window-01/raw.json: dc6b56079f6e06e754b9754e5ce50b83036a9316bc611e71c3fe1e2ae967a484
        B/clauses/window-01/prompt.txt: 41ccba26620ca2cde1d2b0dd5570582c16fa6234d60b2cb1779bcefe76f92e1b
        B/clauses/window-01/meta.json: 8995ab45da7e4412d3a4b6f024b6186ae98289b2abd08e56914f1163ce4df793
        B/clauses/window-06/raw.json: f27924f013cb6312afe011c0873f0ff07e166da20775e0f306d95a6ab06c7965
        B/clauses/window-06/prompt.txt: 034e70436236e166af5c7112ac180d01b0f677ba4a5ee6b165953939fa656eeb
        B/clauses/window-06/meta.json: cfb91ca3c03f1df9b7bbfddfb17d5c56db5ab76c96f81e436c86e38002c69528
        B/tables/TABLE-1-page-3-1/raw.json: b6c383ba2d7e8db42ffce7f765dc042cb7688dba4d292fd7635e559578cf4333
        B/tables/TABLE-1-page-3-1/prompt.txt: 4f09019c265ded66fd22c9b23fdbe08c860c93be71ba75dc7dabb99cd2ec495a
        B/tables/TABLE-1-page-3-1/meta.json: 7afbb2c6ee062ef6aa4b9487b98b627302e4c2985500f5df3f2b56d088644bb2
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
      pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
      source_review: _compare/relationships-2026-11-16/review-current/Benjamin2014
      source_status_sha256: 36667873b7b889a34bc912cc87dafe8cdaaf64a180baaaf93ffb0267f22de53d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: rightward shift in posterior perisylvian activity
    outcome:
      text: category-member generation treatment gains
    analysis_label: treatment gain correlation analysis
    relation: association
    evidence_ids:
    - P6-S1-C8
    qualifier_ids:
    - P8-S1-C3
    - P8-S2-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
      source_review: _compare/relationships-2026-11-16/review-current/Benjamin2014
      source_status_sha256: 36667873b7b889a34bc912cc87dafe8cdaaf64a180baaaf93ffb0267f22de53d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C19
      - Result passage disposed without unit P2-S3-C2
      - Result passage disposed without unit P2-S3-C3
      - Result passage disposed without unit P2-S3-C4
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C10
      - Accounting without a linked unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P5-S1-C9
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C9
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P5-S1-C11
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C7
      - Accounting without a linked unit P8-S1-C1
      - Unaccounted source passage P8-S1-C1
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C7
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S2-C2
      - Result passage disposed without unit P8-S2-C7
      - Accounting without a linked unit P8-S3-C2
      - Unaccounted source passage P8-S3-C2
      - Unaccounted source passage P8-S2-C2
      unattached_null_or_qualifier_ids:
      - P4-S3-C3
      - P5-S1-C10
      - P6-S1-C3
      - P7-S1-C6
      - P7-S2-C2
      - P7-S2-C6
      - P7-S2-C7
      - P8-S1-C11
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 151
      unselected_timing_passages:
      - P2-S2-C5
      - P2-S2-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P1-S2-C16
        - P1-S2-C18
        - P3-S1-C18
        - P4-S2-C5
        - P4-S3-C9
        - P5-S1-C14
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P4-S2-C3
        - P4-S2-C8
        - P4-S2-C10
        - P4-S3-C5
        - P5-S1-C7
        - P5-S1-C11
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P7-S1-C3
        - P7-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
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
        - P2-S2
        - P3-S2
        - P4-S3
        - P5-S1
        - P6-S1
        - P7-S1
        - P7-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
      source_review: _compare/relationships-2026-11-16/review-current/Benjamin2014
      source_status_sha256: 36667873b7b889a34bc912cc87dafe8cdaaf64a180baaaf93ffb0267f22de53d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C18
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports IT rightward shift and CT lack thereof.
    - source_id: P1-S2-C19
      disposition: represented
      result_indexes:
      - 3
      reason: Reports similar changes for all probes between IT and CT.
    - source_id: P1-S2-C20
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports IT gains for untrained probes and CT lack thereof.
    - source_id: P1-S2-C23
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of generalization finding.
    - source_id: P2-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of groups.
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Aphasia classification demographics.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Apraxia of speech prevalence demographics.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of probe categories.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline stability criteria.
    - source_id: P4-S3-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Statistical result for IT rightward shift.
    - source_id: P4-S3-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Statistical result for CT lack of shift.
    - source_id: P4-S3-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Statistical result for IT medial frontal shift.
    - source_id: P4-S3-C14
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: States no other significant shifts occurred.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continuation of text from previous page.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline stability erratum details.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: No significant difference between IT and CT for overall probe accuracy
        change.
    - source_id: P5-S1-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of similar gains for naming probes.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual subject improvement counts.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual subject improvement counts for categories.
    - source_id: P5-S1-C11
      disposition: repeated
      result_indexes:
      - 3
      reason: Reports significant gains for both groups on combined probes.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual subject counts for untrained naming probes.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual subject counts for untrained category probes.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Group analysis of untrained probes showing IT improvement and CT null.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Null correlation for frontal shifts and category gains.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Correlation of posterior perisylvian shifts with gains for IT and CT.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of regression line stability.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Null correlation for naming probes and ROI shifts.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of lateral frontal shift.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of persistence of shift.
    - source_id: P7-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of CT null shift.
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of medial frontal shift.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of timing of medial vs lateral shifts.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of general gains.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Discussion restatement of untrained probe results.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Discussion restatement of generalization.
    - source_id: P8-S1-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of posterior perisylvian correlation.
    - source_id: P8-S2-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of posterior perisylvian correlation.
    - source_id: P8-S3-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of posterior perisylvian correlation.
    unresolved_coverage:
    - source_id: P8-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C23
    - P2-S3-C2
    - P2-S3-C3
    - P2-S3-C4
    - P3-S1-C2
    - P4-S3-C3
    - P4-S3-C14
    - P5-S1-C1
    - P5-S1-C5
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C10
    - P5-S1-C11
    - P6-S1-C2
    - P6-S1-C3
    - P7-S1-C2
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C8
    - P7-S2-C2
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P8-S1-C1
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C11
    - P8-S2-C2
    - P8-S2-C7
    - P8-S3-C2
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
      - P2-S2-C5
      recruited_sample:
      - P2-S2-C5
      eligibility:
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C10
      imaging_provenance:
      - P4-S1-C5
      imaging_timing:
      - P3-S1-C18
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S1-C5
      - P5-S1-C6
      dependent_variable_statement:
      - P4-S2-C8
      - P4-S2-C10
      - P4-S3-C5
      - P6-S1-C6
      limitations:
      - P4-S2-C9
      - P6-S1-C9
      - P7-S1-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S2-C12
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      - P3-S2-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P1-S2-C16
      - P1-S2-C18
      - P3-S1-C18
      - P4-S2-C5
      - P4-S3-C9
      - P5-S1-C14
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P4-S2-C3
      - P4-S2-C8
      - P4-S2-C10
      - P4-S3-C5
      - P5-S1-C7
      - P5-S1-C11
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P7-S1-C3
      - P7-S2-C10
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
      pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
      review_sha256: c8c5e8a0ca775d302af2fa6c4001c53659b5d56fd685411fdaf58c38b23da95d
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
      - P6-S1-C8
      source_result: For the Intention Treatment (IT) group, a rightward shift in
        posterior perisylvian activity was significantly correlated with treatment
        gains for category-member generation (r = -0.86, P < .01). For the Control
        Treatment (CT) group, treatment gains were marginally associated with a leftward
        shift in the same region (r = 0.77, P < .10). No significant correlations
        were found for lateral or medial frontal ROIs.
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the correlation between
            posterior perisylvian laterality shifts and category-member generation
            gains for the IT group, as described in P6-S1-C8. The method (fMRI laterality
            index change) and outcome (probe performance change) match the source.
          source_ids:
          - P6-S1-C8
          - P4-S3-C5
        direction:
          answer: fits
          reason: The source states a 'rightward shift' correlated with 'treatment
            gains' for IT (P6-S1-C8). The proposed claim preserves this direction.
            The negative r-value (-0.86) is consistent with the laterality index formula
            (Left-Right)/(Left+Right) where a rightward shift yields a more negative
            value, correlating with positive gains.
          source_ids:
          - P6-S1-C8
          - P4-S2-C3
        construct:
          answer: fits
          reason: The exposure is the change in laterality index for the posterior
            perisylvian ROI (P4-S2-C2, P6-S1-C6). The outcome is treatment gains for
            category-member generation probes (P6-S1-C6). The population is chronic
            aphasia patients (P2-S2-C5). The measurement is functional imaging (fMRI),
            not diffusion or lesion overlap.
          source_ids:
          - P6-S1-C6
          - P4-S2-C2
          - P2-S2-C5
        qualifications:
          answer: fits
          reason: The draft correctly limits the finding to the IT group and notes
            the marginal/contrasting finding for the CT group. It also includes the
            limitation regarding the IT group's composition (conduction aphasia/posterior
            perisylvian damage) from P8-S1-C9.
          source_ids:
          - P6-S1-C8
          - P8-S1-C9
          - P8-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveat that the IT group was dominated
            by conduction aphasia patients with posterior perisylvian damage (P8-S1-C9),
            which is a material qualifier for interpreting the correlation. It also
            notes the small sample size implicitly via the 'cohort' quality and explicit
            limitations. No other material caveats are omitted that would change the
            interpretation of this specific correlation.
          source_ids:
          - P8-S1-C9
          - P7-S1-C2
      optional_pending:
      - sample.time_post_onset
      - statistical_values_r_p
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
    - statistical_values_r_p
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: Concurrent correlation between pre-to-posttreatment laterality shift
        and baseline-to-phase 3 treatment gains.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 3'
    analysis_identity:
      id: R007
      exposure:
        text: rightward shift in posterior perisylvian activity
      outcome:
        text: category-member generation treatment gains
      analysis_label: treatment gain correlation analysis
      relation: association
      evidence_ids:
      - P6-S1-C8
      qualifier_ids:
      - P8-S1-C3
      - P8-S2-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
        source_review: _compare/relationships-2026-11-16/review-current/Benjamin2014
        source_status_sha256: 36667873b7b889a34bc912cc87dafe8cdaaf64a180baaaf93ffb0267f22de53d
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 160d35dad259d25cf1692059f772f2f984e3c8d825b3141094f27d578a11b8fd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 160d35dad259d25cf1692059f772f2f984e3c8d825b3141094f27d578a11b8fd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Method

          Subjects

          Fourteen chronic (>6 months) aphasia patients participated.'
        anchor_text: 'Method

          Subjects

          Fourteen chronic (>6 months) aphasia patients participated.'
        excluded_fragments: []
        image_sha256: 46c4e0b27e55755696e9973d5e4694fd7651924e010794494a8637e295e6c9b7
        transcription: 'Method


          Subjects


          Fourteen chronic (>6 months) aphasia patients participated'
      P2-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2704d0845329b075b62f0f4a510f6fb68aef8089cdb1900bf4835fbc8804edc7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C7
          page: 2
          text_layer_sha256: 2704d0845329b075b62f0f4a510f6fb68aef8089cdb1900bf4835fbc8804edc7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Patients were premor-\nbidly right-handed,16 used English\
          \ as a first language, and \nhad single or multiple left-hemisphere ischemic\
          \ or hemor-\nrhagic strokes."
        anchor_text: "Patients were premor-\nbidly right-handed,16 used English as\
          \ a first language, and \nhad single or multiple left-hemisphere ischemic\
          \ or hemor-\nrhagic strokes."
        excluded_fragments: []
      P8-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 9ee7b8d02060b6e24b4261dc8b2d36489ff14b1f972bf68cfa6fcf8d5c4714db
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0a21c914ff99ca3f09e2f62583c42964e1e18149f35bd8993a579f6cc979dfae
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C9
          page: 8
          text_layer_sha256: 0a21c914ff99ca3f09e2f62583c42964e1e18149f35bd8993a579f6cc979dfae
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "In the current study, IT patients were \ndominated by patients\
          \ with conduction aphasia and had sig-\nnificant posterior perisylvian damage\
          \ (see Supplemental \nFigure 1)."
        anchor_text: "In the current study, IT patients were \ndominated by patients\
          \ with conduction aphasia and had sig-\nnificant posterior perisylvian damage\
          \ (see Supplemental \nFigure 1)."
        excluded_fragments: []
        image_sha256: 59ee91fc3437f7dedec0fc1f7d637e4c4ff2a232932fd0e32743a8c99360b438
        transcription: '. In the current study, IT patients were

          dominated by patients with conduction aphasia and had sig-

          nificant posterior perisylvian damage (see Supplemental

          Figure 1)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "However, rightward shifts in pos-\nterior persylvian activity showed a significant\
    \ correlation \nwith treatment gains for IT (r = −0.86, n = 7, P < .01), but \n\
    for CT, treatment gains were marginally associated with a \nleftward shift in\
    \ posterior perisylvian activity (r = 0.77, \nn = 6, P < .10)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
