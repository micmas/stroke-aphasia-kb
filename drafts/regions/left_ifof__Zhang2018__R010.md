---
id: left_ifof
name: left IFOF
kind: tract
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: Aphasic patients showed significantly reduced FA and AD and increased RD
    in the left IFOF compared to healthy controls; furthermore, mean FA of the left
    IFOF positively correlated with comprehension, repetition, naming, and general
    oral language (AQ) scores.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: not_reported
    population: Right-handed, native Chinese-speaking subacute post-stroke patients
      with left hemisphere infarction and clinically suspected language dysfunction
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
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Mean diffusion metrics (FA, AD, RD) extracted from
    the left inferior fronto-occipital fascicle using automated fiber quantification
    (AFQ) by resampling 100 equidistant nodes along the tract. Correlation analyses
    were controlled for age, sex, and lesion size; The strongest correlations with
    comprehension, naming, and reading were located in the narrow stem of the IFOF,
    while the strongest correlation with repetition was in the frontal radiation.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P2-S3-C12, two-model agreement, human verification
    pending): . The participant inclusion criteria were as follows: (1)

    diagnosed with left hemisphere infarction confirmed by clinical

    and magnetic resonance imaging (MRI) evidence; (2) within

    1 month of initial stroke episode; (3) right-handed, assessed by

    the Standard Chinese Handedness Scale; (4) aged >25 years old

    with an educational level $\geq 6$ years; (5) native Chinese-speaking, Original
    text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:post_stroke_aphasia
  citation: '@Zhang2018'
  source_passages:
  - section: Original source P5-S2-C10
    page: 5
    quote: "Multiple diffusion metrics of the left IFOF in aphasic \npatients changed\
      \ significantly, including reduced FA (0.32 ± 0.07 \nvs 0.48 ± 0.03), reduced\
      \ AD (1.19 ± 0.13 vs 1.35 ± 0.04), and \nincreased RD (0.72 ± 0.08 vs 0.60 ± 0.05)\
      \ compared with healthy \ncontrols (all corrected p < 0.05)."
    supports: claim
  - section: Original source P5-S3-C9
    page: 5
    quote: "The mean FA of the left \nIFOF correlated positively with four different\
      \ language scores \n(rcomprehension  =  0.839, p  =  0.001; rrepetition  = \
      \ 0.845, p  =  0.001; \nrnaming = 0.813, p = 0.002; rAQ = 0.847, p = 0.001),\
      \ as seen in \nFigure 5B."
    supports: claim
  - section: Original source P2-S3-C12
    page: 2
    quote: "The participant inclusion criteria were as follows: (1) \ndiagnosed with\
      \ left hemisphere infarction confirmed by clinical \nand magnetic resonance\
      \ imaging (MRI) evidence; (2) within \n1 month of initial stroke episode; (3)\
      \ right-handed, assessed by \nthe Standard Chinese Handedness Scale; (4) aged\
      \ >25 years old \nwith an educational level ≥6 years; (5) native Chinese-speaking,\
      \ \n"
    supports: sample
  - section: Original source P4-S2-C7
    page: 4
    quote: "Language function was \nassessed 10 ± 2 days after onset, and MRI scans\
      \ were completed \nafter 14 ± 2 days."
    supports: sample
  - section: Original source P3-S3-C11
    page: 3
    quote: "Automated Fiber Quantification\nWe performed AFQ (version 1.2; Stanford\
      \ University, California, \nUSA;2) to enable further quantitative analysis along\
      \ the major \ntracts."
    supports: method
  - section: Original source P6-S1-C5
    page: 6
    quote: "All the correlations were controlled by additional covariates including\
      \ \nage, sex, and lesion size."
    supports: confounders
  - section: Original source P7-S2-C6
    page: 7
    quote: "The narrow stem of the left IFOF had the strongest correlation \nwith\
      \ comprehension, naming, and reading, whereas the frontal \nradiation presented\
      \ the maximal repetition-related correlation."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2018
  proposal_id: R010
  review_status_sha256: 905ac8d1292336fa44ac6fa433bde54c7249a3a1ffbf24814f53692ea7de7fd5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
        A/passages.json: ec329391eb7a596add6f07bdc68d757f842c9213f3e6380b40dfbdaa915e7bac
        A/raw.json: 7fb0a1c1d43ab62ed61f9c1b04b896a06a361ae7ef5d4a464db6ccf33e371328
        A/source-units.json: c59a5a71382443a845b1b1b4a64aa227f25f1eb8d3bc3a5989917b90d9c41a94
        A/full-source-units.json: 1bee638047a6b683328a62969811d6225a2eb22b5e93bee3aa1667f6ec834261
        A/meta.json: 61c0b6c5b02c724129d52a5e74a03138a05d26c5d2ef5663fe7c78092a1dd241
        A/table-images/TABLE-1-page-5-1.png: 7978751a224c55e621f15cfb0b8e144a0f1a9a11c087965bfe47350a8b7fd685
        A/table-images/page-7.png: 6ff4f0a19b0f02a731f2d03f1d8f481ceacf3db0343e4c1559caeaea4d990ce1
        A/table-images/page-5.png: 8c114878c8cd3f7d5ce681fb838d06c8415f7441307ccc49de7dc6efc736268c
        A/table-images/manifest.json: c2ef2ab3a3757d7f509946d093993475a251fd61a675a6642cf554c5d4bf31cc
        A/table-images/TABLE-2-page-7-1.png: 196fc3d5b732a4e529edea52d5fff65bf00f624a508ad339b18819cc737d8979
        A/clauses/window-03/raw.json: 629b60bea182d64f884be87141288fa212537ed72240df00363dfcb219bbbf03
        A/clauses/window-03/prompt.txt: c4b3b85899225fab096acd90adba8d1745e061d42cad5dd30cedf56e7df92852
        A/clauses/window-03/meta.json: 125685532d99d2b585ba6f524cd7b14f84f76a7d28731c2e26e07e8776d7c42a
        A/clauses/window-04/raw.json: 458b77f842676526af32e3640286a3cd78301f3bc6090fadbac4d76385124c09
        A/clauses/window-04/prompt.txt: 30bd46fe60e4d2a68f892f4618a061e576acc09f5b8fd7eb0de8083e880ed5cb
        A/clauses/window-04/meta.json: 07cbc6776178d638d749c3916481f48d41e7e095c4c67426b7f55942b33c10c2
        A/clauses/window-05/raw.json: 51494df14cbfbe26939bde32a0e1c0bb1d1403bb0d53f38fbe970f8b78bc947e
        A/clauses/window-05/prompt.txt: c82dd3a0726dfab335ac977a3750c8c88359811c76d81b32b471331e774d47d4
        A/clauses/window-05/meta.json: 4557b42618579b085b33b01f1e553f5cd7eae3e0ec26c8d2746f07c2d5ada069
        A/clauses/window-02/raw.json: e841cd6f82861cb32635995ae92740f8fbe85895d6ea47117e5a832392fbb54e
        A/clauses/window-02/prompt.txt: 65507b2c70d10a4de31a0d2e5591e4b2f62b66b128d2825dc963106f6263e4bb
        A/clauses/window-02/meta.json: 73ce1e913afb35226d35da0030deba993c34e4e691e4f54e2478a97273f42610
        A/clauses/window-07/raw.json: 70cdbe50ad2bcde80824cc825fe4300f17ad062b1aa55eb860d7e488e46d8d82
        A/clauses/window-07/prompt.txt: 2a8dd9aed336ce55805c0a0ca9e0d00a14e3d9a958b22006d810d240097304d0
        A/clauses/window-07/meta.json: 88e20d3e5797b0cdd5f9e524c7a584b96b6933b2beb58500b072d337949f1678
        A/clauses/window-01/raw.json: 5197832b7abdcdc74cb4b921a5864f1c0da0eb18690fd5f91ae907075021dee3
        A/clauses/window-01/prompt.txt: 30e3c3192bb20d8cb07205c6135f246a4a94cc54be80a888160e159519d428d4
        A/clauses/window-01/meta.json: e9b5c2a00f7f15ba4dceee5b413455f16af7530c4f65650f11899b7601e546a4
        A/clauses/window-06/raw.json: dcb4dae28001ad11e244b06f0c20b2c3937a408c066d6a6bf9076751518f6d65
        A/clauses/window-06/prompt.txt: c7959c38d0b4b857679c662e58498ce017f9856a42b6a045a46420d1fc1ccc0f
        A/clauses/window-06/meta.json: a258aed2bbbd5c23aff032cef9821feed54c76eab1665d728d8cda8efee68b95
        A/tables/TABLE-1-page-5-1/raw.json: 024cf8c8fb159a8dd8e02af65ab827254081ed498441e6d493a9280f26fd72d8
        A/tables/TABLE-1-page-5-1/prompt.txt: 268f41c21a22471274b3114664644b508b923abb7b63207981a5bf1e75ca19fe
        A/tables/TABLE-1-page-5-1/meta.json: e670735bc7dd0b661bd78d9c236ffa920bd8721e3a11d920bc0c13d4e4c7dd24
        A/tables/TABLE-2-page-7-2/raw.json: e242e6c3ab95df7afe679f0574ed1e26a949a882b48acd8f72aeb723ce89f885
        A/tables/TABLE-2-page-7-2/prompt.txt: b14a451746d2fe905cf3d9b7f43191fa4667fda8644d7d32649ff58db499476e
        A/tables/TABLE-2-page-7-2/meta.json: ca41ecd6128f78b842e92cb17a56c6cb76f5e5e6e7b63e32d5289285b6ac370b
        B/passages.json: ec329391eb7a596add6f07bdc68d757f842c9213f3e6380b40dfbdaa915e7bac
        B/raw.json: 32563f4748a22cf0ebec2a4366702a7cc06c12e0ee836535ab298cf72ae0538c
        B/source-units.json: c59a5a71382443a845b1b1b4a64aa227f25f1eb8d3bc3a5989917b90d9c41a94
        B/full-source-units.json: 1bee638047a6b683328a62969811d6225a2eb22b5e93bee3aa1667f6ec834261
        B/meta.json: 251b657566cefedaae869cedce1c50c0a97b8a7eb5178a0762ee53492a1f169a
        B/table-images/TABLE-1-page-5-1.png: 7978751a224c55e621f15cfb0b8e144a0f1a9a11c087965bfe47350a8b7fd685
        B/table-images/page-7.png: 6ff4f0a19b0f02a731f2d03f1d8f481ceacf3db0343e4c1559caeaea4d990ce1
        B/table-images/page-5.png: 8c114878c8cd3f7d5ce681fb838d06c8415f7441307ccc49de7dc6efc736268c
        B/table-images/manifest.json: 55a4427fe36eb115dc2051350f4c51ce55629da4ec19a8bb38d6eb8861bed834
        B/table-images/TABLE-2-page-7-1.png: 196fc3d5b732a4e529edea52d5fff65bf00f624a508ad339b18819cc737d8979
        B/clauses/window-03/raw.json: 3b6d24a69724ecc5e143b558cd53ac0c8d6ef37a3fd37e5447f3c199857add68
        B/clauses/window-03/prompt.txt: c4b3b85899225fab096acd90adba8d1745e061d42cad5dd30cedf56e7df92852
        B/clauses/window-03/meta.json: 8c179eaa67f635e26b2d09c9759cd68cf31e98bc081649d2aa6b759a0d876fd2
        B/clauses/window-04/raw.json: 1c3c4432dfd874bcd59ba1403a67f8ec07bc5be6000512677f05ac74ad6846fb
        B/clauses/window-04/prompt.txt: 30bd46fe60e4d2a68f892f4618a061e576acc09f5b8fd7eb0de8083e880ed5cb
        B/clauses/window-04/meta.json: 3c04c3f308d834bcfb65b2b34e4fe0da8787b223ac269f5e7ff1fbd63696c087
        B/clauses/window-05/raw.json: 3d3c231fdcc3341e7b494b62fe5e43145897dd2f6ed871f68f73fab4729a6d70
        B/clauses/window-05/prompt.txt: c82dd3a0726dfab335ac977a3750c8c88359811c76d81b32b471331e774d47d4
        B/clauses/window-05/meta.json: 746025621de6f2ce5f2024743927d2c8b5bc0a1499515983328fa5426977cf9d
        B/clauses/window-02/raw.json: 32788f9eedf45f240baeba107f356cd221672205f18fccdc91de6f652411f661
        B/clauses/window-02/prompt.txt: 65507b2c70d10a4de31a0d2e5591e4b2f62b66b128d2825dc963106f6263e4bb
        B/clauses/window-02/meta.json: 9bf7d26b4bb0e0516aaed61e72a9581cefb36aa73463526e5ba035be432616fe
        B/clauses/window-07/raw.json: 5851e32bac7f0a7a032a476e8c2852e481d8fff734422db296e9791da99cecc8
        B/clauses/window-07/prompt.txt: 2a8dd9aed336ce55805c0a0ca9e0d00a14e3d9a958b22006d810d240097304d0
        B/clauses/window-07/meta.json: 9c7b2c4d83ae4884faa7baa2c63ed2965b5111eb7ae432dee91f107a404cdeb0
        B/clauses/window-01/raw.json: 87aa0d068d0b164a7b8214560ecb329bbc2104e5b693913ef6144a8e0ac36d6d
        B/clauses/window-01/prompt.txt: 30e3c3192bb20d8cb07205c6135f246a4a94cc54be80a888160e159519d428d4
        B/clauses/window-01/meta.json: 98df90c8537b54f867a9c871dac48596cb8b6b29021dd017836426b629e18da5
        B/clauses/window-06/raw.json: 4e84a9afaaa74fe1d62504f11c91c1aa2632f2e31b43ef6667d3acc18ee6085e
        B/clauses/window-06/prompt.txt: c7959c38d0b4b857679c662e58498ce017f9856a42b6a045a46420d1fc1ccc0f
        B/clauses/window-06/meta.json: 98574f9bbf2476782fe32a2f233d742c4bc72a8b04ac825691df5bdad64920d8
        B/tables/TABLE-1-page-5-1/raw.json: 267226ce09c0be63c022d9d7906ad77065a50880a3656091edfa8cc8b1b285a2
        B/tables/TABLE-1-page-5-1/prompt.txt: 268f41c21a22471274b3114664644b508b923abb7b63207981a5bf1e75ca19fe
        B/tables/TABLE-1-page-5-1/meta.json: 0dab4fbb3a9c8d008d791e36fc315f337c230b0e55e71432c3de123ad704b1de
        B/tables/TABLE-2-page-7-2/raw.json: 07e77dd25608b182f140eeb853cb67fa0ee55ed82a2357c16e6d4233f731ca4b
        B/tables/TABLE-2-page-7-2/prompt.txt: b14a451746d2fe905cf3d9b7f43191fa4667fda8644d7d32649ff58db499476e
        B/tables/TABLE-2-page-7-2/meta.json: f502c2300ea04f2c8d65c52771213477c615c316ad97588390e2174f0596b308
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
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2018
      source_status_sha256: ab0bb30b3b8f5fa2e2406aabeb21dc1fb3d3e47769439e59e647cba08f9c159c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: left IFOF (FA, AD, RD)
    outcome:
      text: post-stroke aphasia
    analysis_label: AFQ group comparison (mean diffusion)
    relation: association
    evidence_ids:
    - P5-S2-C10
    - P7-S1-C2
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
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2018
      source_status_sha256: ab0bb30b3b8f5fa2e2406aabeb21dc1fb3d3e47769439e59e647cba08f9c159c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C9
      - Accounting without a linked unit P5-S2-C2
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C6
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C2
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C5
      - Unaccounted source passage P5-S2-C3
      - Result passage disposed without unit P5-S3-C10
      - Accounting without a linked unit P5-S3-C9
      - Accounting without a linked unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C9
      - Accounting without a linked unit P7-S1-C4
      - Unaccounted source passage P7-S1-C4
      - Unaccounted source passage P6-S1-C10
      - Unaccounted source passage P5-S3-C9
      - Result passage disposed without unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C4
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C8
      - Accounting without a linked unit P7-S3-C5
      - Unaccounted source passage P7-S2-C8
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P7-S3-C10
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P9-S2-C3
      unattached_null_or_qualifier_ids:
      - P2-S1-C1
      - P5-S1-C8
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 164
      unselected_timing_passages:
      - P1-S2-C3
      - P2-S3-C9
      - P2-S3-C11
      - P2-S3-C12
      - P2-S4-C1
      - P4-S2-C4
      - P4-S2-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S3-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-7-2
      unlinked_tables:
      - TABLE-1-page-5-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P5-S1
        - P5-S2
        - P5-S3
        - P6-S1
        - P8-S1
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2018
      source_status_sha256: ab0bb30b3b8f5fa2e2406aabeb21dc1fb3d3e47769439e59e647cba08f9c159c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Establishes TBSS linguistic associations and AFQ integrity loss in dorsal/ventral
        streams.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Establishes mean FA correlations for IFOF and UF.
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative statement about the narrow stem without specific measured
        outcome.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes ILF temporal segment correlation with comprehension and
        repetition.
    - source_id: P2-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 18
      reason: Highlights section restating findings from results.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison (null result).
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive language performance summary.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia type distribution.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion distribution.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion distribution.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to TBSS results.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Establishes IFOF FA correlation with multiple subtests.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Establishes repetition correlation with specific IFOF/UF/AIC regions.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive spatial distribution of AQ-related regions.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Establishes comprehension and naming association with FA (excluding
        AIC).
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive spatial distribution of correlations.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Establishes null correlation for AD, RD, and MD.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to AFQ group differences.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Establishes IFOF FA, AD, and RD changes.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Establishes ILF, AF, and UF FA/RD changes.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 12
      reason: Establishes point-wise FA reduction in IFOF.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 13
      reason: Establishes point-wise AD reduction in IFOF.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Establishes point-wise RD increase in IFOF.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Establishes point-wise FA/RD alterations in UF.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Establishes null change in MD.
    - source_id: P5-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about ventral tract correlations.
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes mean FA of IFOF correlation with four language scores.
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes mean FA of UF correlation with naming.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 18
      reason: Restatement of narrow stem as crucial common segment.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 18
      - 19
      reason: Establishes point-wise correlations for narrow stem and frontal radiation.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes ILF temporal segment correlation.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of TBSS mapping.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General interpretation of FA/AD/RD changes.
    - source_id: P7-S2-C3
      disposition: repeated
      result_indexes:
      - 16
      reason: Restatement of null MD changes.
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 18
      reason: Restatement of IFOF point-wise correlations.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 18
      - 19
      reason: Restatement of narrow stem vs frontal radiation correlations.
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 3
      - 4
      reason: Restatement of ILF and UF correlations.
    - source_id: P7-S3-C5
      disposition: repeated
      result_indexes:
      - 19
      reason: Restatement of frontal section IFOF and repetition.
    - source_id: P7-S3-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of IFOF integrity and comprehension.
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about indirect pathway evidence.
    - source_id: P8-S1-C12
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of UF FA and naming.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 18
      - 19
      reason: Establishes point-wise correlation segments for IFOF.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study on ILF plasticity.
    unresolved_coverage:
    - source_id: P5-S2-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C6
    - P2-S1-C1
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C11
    - P5-S2-C4
    - P5-S2-C6
    - P5-S2-C8
    - P5-S3-C8
    - P6-S1-C9
    - P7-S1-C8
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C6
    - P7-S2-C8
    - P7-S3-C5
    - P7-S3-C10
    - P8-S1-C11
    - P8-S1-C12
    - P9-S1-C3
    - P9-S2-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C9
      - P4-S2-C8
      recruited_sample:
      - P2-S3-C9
      eligibility:
      - P2-S3-C12
      - P2-S4-C1
      - P2-S4-C2
      - P3-S1-C11
      imaging_provenance:
      - P3-S3-C10
      imaging_timing:
      - P3-S1-C9
      - P3-S1-C10
      - P3-S1-C11
      - P4-S2-C7
      outcome_timing:
      - P3-S1-C4
      - P4-S2-C7
      outcome_definition:
      - P3-S1-C5
      - P3-S1-C7
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S1-C12
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S3-C5
      - P3-S3-C6
      - P4-S1-C14
      - P6-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C2
      - P5-S1-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S3-C11
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
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      review_sha256: 905ac8d1292336fa44ac6fa433bde54c7249a3a1ffbf24814f53692ea7de7fd5
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
      - P5-S2-C10
      source_result: The source reports that in aphasic patients, the left IFOF showed
        significantly reduced FA and AD and increased RD compared to healthy controls
        (P5-S2-C10). It also reports that mean FA of the left IFOF positively correlated
        with comprehension, repetition, naming, and AQ scores (P5-S3-C9). The group
        comparison is a between-group difference, while the correlation is an association
        within the patient group.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R010 is labeled 'AFQ group comparison (mean
            diffusion)' and cites P5-S2-C10. P5-S2-C10 explicitly describes the group
            difference in mean diffusion metrics (FA, AD, RD) for the left IFOF. The
            proposed core claim includes this group difference. Although the core
            also includes correlation data (P5-S3-C9), the primary identity of the
            selected result is the group difference, which is faithfully represented.
          source_ids:
          - P5-S2-C10
          - P5-S3-C9
        direction:
          answer: fits
          reason: The source states reduced FA and AD, and increased RD in patients
            compared to controls (P5-S2-C10). The proposed claim states 'significantly
            reduced FA and AD and increased RD'. The direction is preserved. The correlation
            direction (positive) is also preserved in the claim.
          source_ids:
          - P5-S2-C10
          - P5-S3-C9
        construct:
          answer: fits
          reason: The exposure is 'left IFOF (FA, AD, RD)' and the outcome is 'post-stroke
            aphasia'. The source confirms the use of AFQ to extract mean diffusion
            metrics from the left IFOF (P3-S3-C11, P4-S1-C9) and compares patients
            with aphasia to controls (P5-S2-C8). The patient measurement is diffusion
            metrics (FA, AD, RD) extracted from patient tractography (AFQ), which
            corresponds to 'patient_diffusion' as per the instructions (diffusion
            used to construct maps does not mean patient_diffusion, but here the metrics
            are extracted from patient tracts).
          source_ids:
          - P3-S3-C11
          - P4-S1-C9
          - P5-S2-C10
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications about covariates (age,
            sex, lesion size) for correlations (P6-S1-C5) and specific anatomical
            locations of correlations (P7-S2-C6). These are present in the source.
            The group comparison itself (P5-S2-C10) does not explicitly mention covariates
            in the snippet, but the general statistical analysis section (P3-S3-C5)
            mentions adjusting for age and sex in TBSS, and P4-S1-C14 mentions nuisance
            covariates for correlations. The core correctly attributes the covariate
            control to the correlation analyses.
          source_ids:
          - P6-S1-C5
          - P7-S2-C6
        missing_material_caveat:
          answer: fits
          reason: The core includes the limitation of small sample size. The source
            mentions 'preliminary investigation' (P2-S3-C6) and 'small sample' is
            implied by the N=14 patients. No material caveat that changes the interpretation
            of the group difference or correlation is omitted. The distinction between
            group difference and correlation is maintained in the claim text.
          source_ids:
          - P2-S3-C6
          - P4-S2-C4
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 14
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: Language function assessed 10 ± 2 days after onset; MRI scans completed
        after 14 ± 2 days
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 14, 1E+1'
    analysis_identity:
      id: R010
      exposure:
        text: left IFOF (FA, AD, RD)
      outcome:
        text: post-stroke aphasia
      analysis_label: AFQ group comparison (mean diffusion)
      relation: association
      evidence_ids:
      - P5-S2-C10
      - P7-S1-C2
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
        pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
        source_review: _compare/relationships-2026-11-16/review-current/Zhang2018
        source_status_sha256: ab0bb30b3b8f5fa2e2406aabeb21dc1fb3d3e47769439e59e647cba08f9c159c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f815d0fce6ae1b6cd8e56f6ab4787462c1ea0836a5a1b83d59513438bfca2337
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C12
          page: 2
          text_layer_sha256: 2cea396b4c8474d9a32c5060a0aeac0f7db21e37657cca5bd2e8b7c2e2f0cc86
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The participant inclusion criteria were as follows: (1) \n\
          diagnosed with left hemisphere infarction confirmed by clinical \nand magnetic\
          \ resonance imaging (MRI) evidence; (2) within \n1 month of initial stroke\
          \ episode; (3) right-handed, assessed by \nthe Standard Chinese Handedness\
          \ Scale; (4) aged >25 years old \nwith an educational level ≥6 years; (5)\
          \ native Chinese-speaking, \n"
        anchor_text: "The participant inclusion criteria were as follows: (1) \ndiagnosed\
          \ with left hemisphere infarction confirmed by clinical \nand magnetic resonance\
          \ imaging (MRI) evidence; (2) within \n1 month of initial stroke episode;\
          \ (3) right-handed, assessed by \nthe Standard Chinese Handedness Scale;\
          \ (4) aged >25 years old \nwith an educational level ≥6 years; (5) native\
          \ Chinese-speaking, "
        excluded_fragments: []
        image_sha256: b561b0c92eba52223660790253915049524a17043de6ea5c81e00d1ec4e9ede4
        transcription: '. The participant inclusion criteria were as follows: (1)

          diagnosed with left hemisphere infarction confirmed by clinical

          and magnetic resonance imaging (MRI) evidence; (2) within

          1 month of initial stroke episode; (3) right-handed, assessed by

          the Standard Chinese Handedness Scale; (4) aged >25 years old

          with an educational level $\geq 6$ years; (5) native Chinese-speaking,'
      P4-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8e40a4c7cb8e564d2b8fb654aa6ceef9c06b4277d5de62298268d46e41d2ceb2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C7
          page: 4
          text_layer_sha256: 8e40a4c7cb8e564d2b8fb654aa6ceef9c06b4277d5de62298268d46e41d2ceb2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Language function was \nassessed 10 ± 2 days after onset,\
          \ and MRI scans were completed \nafter 14 ± 2 days."
        anchor_text: "Language function was \nassessed 10 ± 2 days after onset, and\
          \ MRI scans were completed \nafter 14 ± 2 days."
        excluded_fragments: []
        image_sha256: a56b4168df4064c933df406fd90d912e7e50fc938901301fb3241bfe567011dd
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Multiple diffusion metrics of the left IFOF in aphasic \npatients changed\
    \ significantly, including reduced FA (0.32 ± 0.07 \nvs 0.48 ± 0.03), reduced\
    \ AD (1.19 ± 0.13 vs 1.35 ± 0.04), and \nincreased RD (0.72 ± 0.08 vs 0.60 ± 0.05)\
    \ compared with healthy \ncontrols (all corrected p < 0.05)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
