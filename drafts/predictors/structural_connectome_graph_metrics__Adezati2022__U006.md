---
id: structural_connectome_graph_metrics
name: Structural connectome graph measures
kind: predictor
findings:
- id: f1
  target: auditory_sentence_comprehension
  target_kind: impairment
  claim: None of four graph measures (average clustering, transitivity, characteristic
    path length, global efficiency) was significantly associated with Token Test performance
    after simultaneous adjustment for lesion volume and the other graph measures,
    in either whole-brain or left-language networks (all p>0.2). This does not establish
    absence of a connectivity contribution.
  direction: no_effect
  relationship: correlational
  method: tractography
  design: cross-sectional
  sample:
    n: 50
    population: Adults with aphasia after a single left-hemisphere stroke
    phase: mixed
    time_post_onset: 2.24–167.93 months
    cohort: University of Alabama at Birmingham; substantial overlap with Thye2021
  statistics:
    threshold: all graph-metric p>0.2; robust standard errors
    effect_size: See main-paper Table 3; each of eight network-specific metric confidence
      intervals includes zero
  confounders_controlled:
  - Lesion volume
  - Other graph measures in each simultaneous regression
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    description: AAL3, 166 nodes; whole brain and prespecified left-language subnetwork
  author_limitations:
  - Interpretation of connectome disruption requires caution
  evidence_quality: cohort
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping of dual extraction and independent local
      review)
    extracted_on: '2026-11-17'
    paper_section: Main PDF Methods and Results
    confidence: medium
    flags:
    - human_approval_pending
    - paper_coverage_not_certified
  imaging: DWI
  imaging_details:
    reference_space: native
    atlases_used:
    - AAL3
    preprocessing_pipeline: Patient diffusion MRI probabilistic tractography; atlas
      transformed via MNI to native diffusion space; lesion excluded from tracking
  notes: Table 3 lists four graph measures; Methods calls these five. This source
    inconsistency is unresolved. No normative disconnectome or individual tract effect
    was measured.
  citation: '@Adezati2022'
  source_passages:
  - section: Source passage P4-S3-C3
    page: 4
    quote: "None of the graph theory metrics of connectivity disruption were \nstatistically\
      \ significant predictors of Token Test performance, regardless \nof whether\
      \ they were defined at the whole brain level or for the language \nsub-network\
      \ (all p > 0.2)."
    supports: claim
  - section: Source passage P3-S1-C6
    page: 3
    quote: "Whole-brain structural connectomes were generated from each \nparticipant’s\
      \ diffusion images using probabilistic tractography."
    supports: method
  - section: Source passage P3-S1-C7
    page: 3
    quote: "To \nenable fibre tracking between anatomic atlas regions, participant\
      \ T1- \nweighted images were normalized to MNI space using the Clinical \nToolbox\
      \ (Rorden et al., 2012), which accounts for deformations caused \nby brain lesions,\
      \ and the inverse transformation matrix was used to \ntransform the AAL3 atlas\
      \ (Rolls et al., 2020) into native space."
    supports: imaging_details
  - section: Source passage P3-S2-C4
    page: 3
    quote: "For each participant, this \nresulted in a 166x166 symmetric matrix describing\
      \ the number of \npairwise streamlines corrected for the distance between and\
      \ size of the \nconnected regions."
    supports: method
  - section: Source passage P4-S3-C2
    page: 4
    quote: 'The connectivity disruption regressions revealed only one statisti­

      cally significant effect: overall lesion volume (p < 0.001 for both ana­

      lyses).'
    supports: confounders
  - section: Table 3 (visually checked)
    page: 5
    quote: "Table 3 \nResults of connectivity disruption regression analyses. Values\
      \ are the coefficient \nestimates with standard errors in parentheses and 95%\
      \ confidence intervals in \nbrackets. Only lesion volume was statistically significantly\
      \ associated with \nToken Test performance.  \nMetric \nWhole Brain Network\
      \ \nLanguage Network \nLesion volume (cc) \n−0.111 (0.024), [-0.158, \n-0.064]\
      \ \n−0.116 (0.03), [-0.174, \n-0.057] \nAverage Clustering \nCoefficient \n\
      6811 (6773), [-6463, \n20085] \n−20.7 (156), [-327, 286] \nTransitivity \n−4616\
      \ (6433), [-17224, \n7992] \n133 (136), [-134, 400] \nCharacteristic path length\
      \ \n0.011 (0.021), [-0.031, \n0.053] \n0.001 (0.003), [-0.004, \n0.007] \nGlobal\
      \ efficiency \n−202.4 (187.2), [-569.3, \n164.5] \n−14.9 (34.8), [-83.1, \n\
      53.2]  \n"
    supports: statistics
predictor_type: imaging_metric
short_definition: Patient diffusion-derived network segregation and integration measures.
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-17'
relationship_review:
  paper: Adezati2022
  proposal_id: U006
  review_status_sha256: 1c4071d2a004c4126d6c5926369e50d5c24aff88f81e7f416a4fa65d3fc71a81
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
      A/passages.json: 11886d409d20fec61ee25b3d2a3b217d6161dab2fb909d04b4725a8ce719fa2c
      A/raw.json: 875e02cdc21fa9faa82b14be2b740f0a5900c620baf707de4a551a1a9ce97ae4
      A/source-units.json: dc132f8035b4a438c6094f09d3d9faa7d2a541791629dc0841734785c424c34c
      A/full-source-units.json: 62f4829a973a56a478e615824577219549191ee62485f6993247fb91b4e5a134
      A/meta.json: 516a720ef4c4c49835892d23edb5467b6af34a06fdcbf4398054866367771742
      A/table-images/page-3.png: f440b5f57da726bd095636ab776dd0481910933423bf83c2dd313c6a108f4164
      A/table-images/TABLE-1-page-2-1.png: 6da7f6ef0293c8b503ac46cce4f0eeceb314eb3ae7767df2edc53ce733b849d6
      A/table-images/page-2.png: 879c362f5bcfd72563c228a3a1e9da352e6aa7183dc49e7b8da4ac0e5d6c4294
      A/table-images/page-5.png: 95d94cacf3c18db4995c8b978dd760e2fe0d2b62b7558aaed61d84db93df29c9
      A/table-images/manifest.json: 9b54abb50076bb307a14e0727c3fe4e3e15893b9bc176a9eff433ddff6d8277a
      A/table-images/TABLE-2-page-3-1.png: ab9e23386d490f88e8908b6ad68023dcff503ca7e9701de1b1bf43631b1f7f79
      A/table-images/TABLE-3-page-5-1.png: 10169c8e6feca22388ee6ef5104f002a9e6c1d31a39a0d204a9d2fc0274fdb8b
      A/clauses/window-03/raw.json: 86bb54f8c9d1594907a406440ef958041b7eec0347a32703c9f139ab85792780
      A/clauses/window-03/prompt.txt: 25c24d5474ea15f0fec4f28128f4ae3f5b49e9f13d106ec505cf3a19bc131f62
      A/clauses/window-03/meta.json: aba1b67ab3b80a23a4a53e4c825259fd06caecd49fb5d19af44e99935eae12d0
      A/clauses/window-04/raw.json: 645a88aa6567f07d83c57a124a160dbd11f3ed16d08cc68c73dd208f5535824d
      A/clauses/window-04/prompt.txt: 3b6af5e44f7926fe60fe8d8b0a0891a0975672650dec7661cf0db168c3a8e9c1
      A/clauses/window-04/meta.json: 281696fc3fc55e12d4ffda4feeabdb2b39180c78b80a3c699de493a346d22fb5
      A/clauses/window-05/raw.json: b3e1dc57f1c38dc4e820057033287759a796eaeb7dd938ce4cf5896f59ffc67a
      A/clauses/window-05/prompt.txt: 6606cf9a3602a7f7fa85e3a307d0851bf2cbc5ab8ed65eeabcf2ceb3c1951a5d
      A/clauses/window-05/meta.json: 48a7701617839b9208ce2ea712d6ac8d19d85cd66182de1340d25ed827514d9d
      A/clauses/window-02/raw.json: c3e2b2926b3c9a4ce9673b2d23962fc3b767bfce00607f89665606a1f4c616ae
      A/clauses/window-02/prompt.txt: af05a03f57469d17d3e0caa1ba734ea1e24634266b9b602378518193df8c586e
      A/clauses/window-02/meta.json: 8452721adf7449f7df60359a18026ff61d213c604705ddcc6a1aae24cf261e3b
      A/clauses/window-01/raw.json: ff34618267db999b6059a0f3baa09834c3f5d29114c98e62277a65a87a757650
      A/clauses/window-01/prompt.txt: 208cd2889926074f26b673d244d95d0ff90952b781ac34aff326fbc78ccd8495
      A/clauses/window-01/meta.json: 4ed94910bb7381534ba7f55d7a457ac19c7f744760a27df95d3472b6c093e36a
      A/tables/TABLE-3-page-5-3/raw.json: 8c68152a0b7759458a61bc174b1dd20190ed2b528753f5f2fecf1852e6b8e736
      A/tables/TABLE-3-page-5-3/prompt.txt: 6333dea07d7faee3d9fcb0c2aba20ba619545215d76a308d4b835d26d8f7e1c5
      A/tables/TABLE-3-page-5-3/meta.json: 552a747f9b044df1942861c2648354cfeb6e70b9efb2d21fb93c3037428c8636
      A/tables/TABLE-1-page-2-1/raw.json: e5bffed55cf67e23914cc9c4e01a2969de01311866a25e8d731875f603e8a5b5
      A/tables/TABLE-1-page-2-1/prompt.txt: b3f4828a5ba8053f0ad9c017491daaaf8074171e140c4adf01e5473a1d7f5c4a
      A/tables/TABLE-1-page-2-1/meta.json: a128cce801a25262fd28629fd8bd88c9ecce3f787dd0856c67d95cdb96b2e465
      A/tables/TABLE-2-page-3-2/raw.json: 1a423f72e175a065da8b9d4434a2336318874ac83558561af4273b58e93e1782
      A/tables/TABLE-2-page-3-2/prompt.txt: e30b0c9a30ecde0a3d7ad2a79690785571fc91f2639d85509700cd4f12a833d2
      A/tables/TABLE-2-page-3-2/meta.json: 2181e063543da1b09f82d0edcf9582425441ee821bf4dee2a5350c7badfe0ba9
      B/passages.json: 11886d409d20fec61ee25b3d2a3b217d6161dab2fb909d04b4725a8ce719fa2c
      B/raw.json: 1d79be72a44812962b7eaf6a621ca0b58489315b862a0ad7155f4310feeaab9a
      B/source-units.json: dc132f8035b4a438c6094f09d3d9faa7d2a541791629dc0841734785c424c34c
      B/full-source-units.json: 62f4829a973a56a478e615824577219549191ee62485f6993247fb91b4e5a134
      B/meta.json: 050839df919f2d0b9bc275adf0442ee1d15f6133f4634ccd38de0243065d494e
      B/table-images/page-3.png: f440b5f57da726bd095636ab776dd0481910933423bf83c2dd313c6a108f4164
      B/table-images/TABLE-1-page-2-1.png: 6da7f6ef0293c8b503ac46cce4f0eeceb314eb3ae7767df2edc53ce733b849d6
      B/table-images/page-2.png: 879c362f5bcfd72563c228a3a1e9da352e6aa7183dc49e7b8da4ac0e5d6c4294
      B/table-images/page-5.png: 95d94cacf3c18db4995c8b978dd760e2fe0d2b62b7558aaed61d84db93df29c9
      B/table-images/manifest.json: dd4fdf0899bcfe45df5699a97e39cd459d7c07049b05df77b065ccd9778b2c8e
      B/table-images/TABLE-2-page-3-1.png: ab9e23386d490f88e8908b6ad68023dcff503ca7e9701de1b1bf43631b1f7f79
      B/table-images/TABLE-3-page-5-1.png: 10169c8e6feca22388ee6ef5104f002a9e6c1d31a39a0d204a9d2fc0274fdb8b
      B/clauses/window-03/raw.json: e6aab6ab6990f763ca11e70d90977c8910efbaa16df0769d1770368781feebaa
      B/clauses/window-03/prompt.txt: 25c24d5474ea15f0fec4f28128f4ae3f5b49e9f13d106ec505cf3a19bc131f62
      B/clauses/window-03/meta.json: 3ccf684a2411d00eb8df052ac8d42f396c8b0a1026759ce7e53f040a2f1dae93
      B/clauses/window-04/raw.json: 3578bbd0ab7a43530cc60a505d666624cae34626104933cb84a85e338b69ff1a
      B/clauses/window-04/prompt.txt: 3b6af5e44f7926fe60fe8d8b0a0891a0975672650dec7661cf0db168c3a8e9c1
      B/clauses/window-04/meta.json: ed6d76ca3e8886c02f82e4e2fb50cacd3acbd11b36a936ff2e21cb4d7414074f
      B/clauses/window-05/raw.json: 46fc38a3ecae10df4314817de0a59728dd3819e25b77ca3f122504f6bed1a9d3
      B/clauses/window-05/prompt.txt: 6606cf9a3602a7f7fa85e3a307d0851bf2cbc5ab8ed65eeabcf2ceb3c1951a5d
      B/clauses/window-05/meta.json: 2417c1047dcefede7ca9ef583ec18b0589488d431a389fd23802d7aafa5b430d
      B/clauses/window-02/raw.json: 99e3ba3dc7c906143d60b00bb18424e6925ad4cb97557de423e9c140f4ce6c6c
      B/clauses/window-02/prompt.txt: af05a03f57469d17d3e0caa1ba734ea1e24634266b9b602378518193df8c586e
      B/clauses/window-02/meta.json: 5082635e5b8e7abd70f23248340a2b89390205c1ef0290fc6aa08fb409cf4fe1
      B/clauses/window-01/raw.json: e83852410738a262c4b2d19f8f49ed10cfe11bd5aee9d5071da59c74891d34e2
      B/clauses/window-01/prompt.txt: 208cd2889926074f26b673d244d95d0ff90952b781ac34aff326fbc78ccd8495
      B/clauses/window-01/meta.json: 42565868ee9cde8cc56f07ec77487f21f3619ceb7191521935216b41038937ff
      B/tables/TABLE-3-page-5-3/raw.json: 8c68152a0b7759458a61bc174b1dd20190ed2b528753f5f2fecf1852e6b8e736
      B/tables/TABLE-3-page-5-3/prompt.txt: 6333dea07d7faee3d9fcb0c2aba20ba619545215d76a308d4b835d26d8f7e1c5
      B/tables/TABLE-3-page-5-3/meta.json: f7eaff1435bfeeceba58be43c9162038a01e44404f13e4dc322772146bf1393e
      B/tables/TABLE-1-page-2-1/raw.json: 18048d806bc59d502ab708d79ca2d35e16dffd20e60b166fa10cbeede7c1ffad
      B/tables/TABLE-1-page-2-1/prompt.txt: b3f4828a5ba8053f0ad9c017491daaaf8074171e140c4adf01e5473a1d7f5c4a
      B/tables/TABLE-1-page-2-1/meta.json: 8eebc3495cd60f0ec4d237928633ff3bf216f7187ba92a66e7217065180eda0d
      B/tables/TABLE-2-page-3-2/raw.json: 98c83c68830388b1b5124a7da4a9cfe62c6ace5eef60d98fe24d4265b2bfd31c
      B/tables/TABLE-2-page-3-2/prompt.txt: e30b0c9a30ecde0a3d7ad2a79690785571fc91f2639d85509700cd4f12a833d2
      B/tables/TABLE-2-page-3-2/meta.json: 2f0f4b1d24581380c909c73379a4ff4abf8ca5b6e9a2874cca508ed7222220d8
    code:
      relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
      relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
      ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
      strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
    model: gemma4:26b
    model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
    host: http://localhost:11434
    max_output_tokens: 20000
  proposal:
    evidence_ids:
    - P4-S3-C3
    qualifier_ids: []
    context_ids:
    - P4-S2-C13
    table_ids: []
    exposure:
      text: graph theory metrics of connectivity disruption
      source_id: P4-S2-C13
    outcome:
      text: Token Test performance
      source_id: P4-S3-C3
    relation: association
    effect_unit: individual
    result_status: reported_not_detected
    outcome_type: not_applicable
    direction: not_stated
    direction_source_id: ''
    origin: current_study
    label_match_candidates:
      exposure:
      - P4-S3-C3
    id: U006
    flags:
    - nonverbatim_or_missing_label
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P2-S3-C1
    - P2-S3-C2
    - P2-S3-C3
    - P2-S3-C5
    - P2-S3-C6
    - P2-S3-C8
    - P2-S3-C9
    - P3-S1-C10
    - P3-S1-C11
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C6
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S3-C15
    - P3-S3-C2
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C8
    - P3-S3-C9
    - P4-S1-C13
    - P4-S1-C14
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C6
    - P4-S2-C11
    - P4-S2-C12
    - P4-S2-C7
    - P4-S2-C9
    - P4-S4-C4
    - P4-S4-C5
    - P4-S4-C6
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: 609109637abd42c2e51f8d378ca6e9e331bed4ca8de1566c474add42eb135e60
  audit:
    coverage_issues:
    - Accounting without a linked unit P4-S2-C11
    - Accounting without a linked unit P4-S2-C12
    - Unaccounted source passage P4-S2-C12
    - Unaccounted source passage P4-S2-C11
    - Result passage disposed without unit P4-S4-C11
    - Accounting without a linked unit P4-S4-C7
    - 'window 5: invalid/duplicate disposition P4-S4-C8'
    - Unaccounted source passage P4-S4-C7
    unattached_null_or_qualifier_ids:
    - P4-S3-C11
    suppressed_nonrepresented_units: 10
    default_disposition_count_requires_completeness_check: 108
    unselected_timing_passages: []
    personal_effect_slots_without_result_classification: []
    held_frame_selections: []
    empty_frame_slots_require_confirmation:
    - personal_factors
    - tested_personal_effects
    unclassified_extraction_ids: []
    table_review_required:
    - TABLE-1-page-2-1
    - TABLE-2-page-3-2
    - TABLE-3-page-5-3
    unlinked_tables:
    - TABLE-2-page-3-2
    - TABLE-3-page-5-3
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P3-S1
      - P3-S3
      - P3-S4
      - P4-S2
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C5
      recruited_sample:
      - P2-S3-C5
      eligibility:
      - P2-S3-C5
      imaging_provenance:
      - P3-S1-C6
      imaging_timing:
      - P2-S3-C5
      outcome_timing:
      - P2-S3-C5
      outcome_definition:
      - P2-S3-C8
      validation:
      - P4-S2-C3
      analysis_restrictions:
      - P3-S3-C15
      - P4-S1-C13
      dependent_variable_statement:
      - P4-S2-C7
      - P4-S2-C9
      limitations:
      - P4-S4-C4
      - P4-S4-C6
      - P4-S4-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C14
      - P4-S2-C9
      explicitly_not_adjusted:
      - P2-S4-C2
      descriptive_personal_factors:
      - P2-S4-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections: []
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_pdf_pages:
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    visual_pages:
    - 2
    - 3
    - 5
    tables_checked:
    - 1
    - 2
    - 3
    figures_checked:
    - 1
    - 2
    corrections:
    - Recovered primary LSM Results passages omitted from model units, including frontal
      corona radiata.
    - Time since stroke is a tested null association, not a prognostic recovery effect.
    - Keep AAL/JHU lesion labels separate from AAL3 tractography nodes; Colin27 lesion
      space differs from native diffusion space.
    - Regression Table 3 has four graph metrics although Methods says five; retain
      the inconsistency.
    - No region-level effect size or confidence interval is reported for the LSM clusters.
    remaining:
    - Named-person approval and reconciliation with existing findings.
    - No supplementary files examined; no individual-patient predictions established.
    - Existing Adezati findings in regions/left_ifg_pars_triangularis.md and regions/left_posterior_stg.md
      require replacement/deduplication review; do not append as independent evidence.
    checked_by: agent:codex
    date: '2026-11-17'
    pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
    licence:
      category: cc
      label: CC BY 4.0
      url: http://creativecommons.org/licenses/by/4.0/
      version: published
      source: crossref
      doi: 10.1016/j.ynirp.2021.100076
      checked: '2026-10-30'
      consulted:
      - crossref
      - unpaywall
      - pdf
    approved: false
    scope: Agent source check for specified mapped claims; not human approval or certification
      of whole-paper completeness
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "None of the graph theory metrics of connectivity disruption were \nstatistically\
    \ significant predictors of Token Test performance, regardless \nof whether they\
    \ were defined at the whole brain level or for the language \nsub-network (all\
    \ p > 0.2)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-17'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---


# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
