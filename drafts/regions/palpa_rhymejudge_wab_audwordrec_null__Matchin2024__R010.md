---
id: palpa_rhymejudge_wab_audwordrec_null
name: PALPA RhymeJudge and WAB-R AudWordRec cluster
kind: network
findings:
- id: f1
  target: behavioural_deficits
  target_kind: impairment
  claim: No regions were found for which damage was significantly associated with
    deficits on the PALPA RhymeJudge and WAB-R AudWordRec tasks when including total
    lesion volume as a covariate.
  direction: no_effect
  relationship: correlational
  method: VLSM
  sample:
    n: not_reported
    population: individuals with chronic post-stroke aphasia
    phase: not_reported
    time_post_onset: at least 1 year post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - linear sequencing demands were low in the rhyme judgement tasks
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: proportion damage to regions of the JHU atlas. total
    lesion volume was included as a covariate; corrected for multiple comparisons
    using permutation testing. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S3-C6, two-model
    agreement, human verification pending): All participants

    were at least 1 year post-stroke Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:behavioural_deficits
  citation: '@Matchin2024'
  source_passages:
  - section: Original source P10-S1-C6
    page: 10
    quote: "We did not find any regions for which damage was signifi­\ncantly associated\
      \ with deficits on the PALPA RhymeJudge \nand WAB-R AudWordRec task when including\
      \ total lesion \nvolume as a covariate and correcting for multiple compari­\n\
      sons with permutation testing, which contrasts with previous \nstudies that\
      \ have found significant effects for the same or \n"
    supports: claim
  - section: Original source P3-S3-C6
    page: 3
    quote: "All participants \nwere at least 1 year post-stroke."
    supports: sample
  - section: Original source P5-S3-C6
    page: 5
    quote: "Lesion-symptom and connectome-symptom mapping analyses \nwere performed\
      \ on voxels/regions that were damaged in at \nleast 10% of sample in order for\
      \ maximum spatial reliabil­\nity.88,89 Connectome-symptom mapping analyses were\
      \ per­\nformed on connections within the LH only in order to keep \nthe number\
      \ of independent comparisons within a manageable \nlevel.90 Lesion-symptom mapping\
      \ analyses were performed at \nthe voxel level, incorporating overall lesion\
      \ volume as a covari­\nate to provide strongest spatial inference.91 By contrast,\
      \ all \nconnectome-based analyses did not incorporate lesion volume \nas a covariate\
      \ lesion volume, as this was already factored into \nour analyses by removing\
      \ damaged tissue from estimated trac­\ntographies.90 All analyses were corrected\
      \ for multiple compar­\nisons using permutation testing (4000 permutations)."
    supports: method
  - section: Original source P12-S1-C6
    page: 12
    quote: "It is also important to note that linear sequencing \ndemands were low\
      \ in our rhyme judgement tasks."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Matchin2024
  proposal_id: R010
  review_status_sha256: 0c5df108760f5139cb1a0da1563dc9e0e95542e070a892cce02187133159521b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
        A/passages.json: 670589637617e963cc0cd28f1d0b4ad6b1640c7a051a672c5012c9453f02d1bf
        A/raw.json: a95f510f10af7dba8580ec65ca7a47d6ad73d47bd37dab4881c297c3d940ddc1
        A/source-units.json: 8180cca81d41ccd49ac0b1e5dd7053c8f518bdd51d13a480de2e184cbcca4114
        A/full-source-units.json: dd2438563b9f0d622c2c45d98887eb26bac0d454fc4574376eeb5439e2faf549
        A/meta.json: 447cf5c70047d704ec0470767e3a7d61762c9b6753045b3506d4f3e080bf2f69
        A/table-images/TABLE-3-page-9-1.png: a4390cb290275f5653212d893d8ab6db633f6472cf0981788f65ad4ab5ff8eb4
        A/table-images/page-11.png: eaa1cf18b85a7cf8d79ae92c9cf8476193ff61a7eff2a0ed3f727650df126715
        A/table-images/page-6.png: 93c602ce7bddce27a3bca2d55e9c04e63a2a45703c74ae4fcbab110c8c91d959
        A/table-images/page-7.png: f0d103da2121208f58ee57f3f01ab6665d3d09ec378494ff37bb8007053d57a9
        A/table-images/TABLE-4-page-11-1.png: 14469c610a12555dd7f9c5df5fa006fcb535836fb28dcfce9f9c5e91d4e86df0
        A/table-images/page-4.png: 999e64f700a92738418a7bf69bff7c996cb056edb8dbff306038ca79519c5915
        A/table-images/TABLE-1-page-4-1.png: a5a7a8b1e9d4f356d438e092c03ae57d12c98106b94315241cf15d3ef1291f88
        A/table-images/page-9.png: 4f5d5f80d0b28491be9b4204873e3a0c14194a1abca3d1582c199c36fe20ec16
        A/table-images/TABLE-3-page-6-1.png: ae60e3e594eb116a2634bc42ee15d742562601a4cb91637c82bed5475b48371d
        A/table-images/manifest.json: d7af164285cd0eec83e54fecf8ddecc9729a053b40732763e1300fddc444935c
        A/table-images/TABLE-2-page-7-1.png: 610ada8e94c8571d2e58336ddf9d986636e972e1102df27e9e45a3762edf651f
        A/clauses/window-03/raw.json: 530d9e4dd05529084d87f88aed75cc1e27e2355b854d2efee2644b67f0b5ecfe
        A/clauses/window-03/prompt.txt: b8e4f3774f7b05c0fe0661c02728658eff15474316fd218d962f8ad00f7c7177
        A/clauses/window-03/meta.json: 1fbb78320b7ce339852b1535e927bb43bd00b56173f46b42831ea0b0fc85883c
        A/clauses/window-04/raw.json: 99d1340803de1bed629f85826357f82e9e368242f786bf7da4cd7b2a1b9416d6
        A/clauses/window-04/prompt.txt: 1a5cd7aa5d63a41482e8bcdf7974d9dcba9c1f9d4c111cc425b158d33b6d88a8
        A/clauses/window-04/meta.json: 90b2fd7667edaca12a04fac513990168708ff0b93a3787bfc59478a512bc92cc
        A/clauses/window-05/raw.json: 093e4ea46200f8067f9c068b0d190ed620981b9978e1906d94ffb13a579948ec
        A/clauses/window-05/prompt.txt: 2c367a4565a8175199f783bce1b8415c5d45277d02eb3910df69c045b0fdf1c0
        A/clauses/window-05/meta.json: 7b7b979f84fbf29a804065ef51713f7b9f84eff540a98a791a715612432f1a69
        A/clauses/window-02/raw.json: 6af88dda8d270006b97eb794bb54c779071f253b820120c99fdb8384743a093c
        A/clauses/window-02/prompt.txt: e79208981eb4d96b10759a1919151ac6c79c9eae2c7846a61004ff394da70979
        A/clauses/window-02/meta.json: f540647bebee75dd199111a2c02b6edc4264f4772495d238ac99303d541cad9b
        A/clauses/window-07/raw.json: 14c7dc3a7ebcd94970c260b094be9b9446ccf3cb89f0db249843d45ae9ecbd83
        A/clauses/window-07/prompt.txt: 5f7d335d9e54a7c798f54ca23b70c9e00afe5d8c148edb2eee3080031367428f
        A/clauses/window-07/meta.json: 81e4e9a1ee6ead05dbe5d010f7e1bac78c030296704755a27e5e67bc09858958
        A/clauses/window-01/raw.json: c2b9498bd5e23b933c16a9893d61cbeac5ee5caba772e59d08dde41a0186e12d
        A/clauses/window-01/prompt.txt: eae08fffb4a6d91b929f3ea4bfc5827ebf8bf638124025b65c2d2ac5aa5af988
        A/clauses/window-01/meta.json: d7d4ce0cd3e4fa2dc923e939faaab9c4f362761532f98ff5275175cbcc50f733
        A/clauses/window-06/raw.json: 76b65e827390dab6d780b04948803c65feea97ec497b812902c7e419143d1ac0
        A/clauses/window-06/prompt.txt: ae5b10a6d32e030e2fdd146097a5b641813fe86090c67db2d5f0b2834b1e956d
        A/clauses/window-06/meta.json: b89ebcfc4f2839b1f7776f861b929cc9c14cf7baecc20a6f4c1b33195384248e
        A/tables/TABLE-4-page-11-5/raw.json: c72e84da3838ba2e793fd296e2eb4cefe5f1193997db51ee16580e02c7d76379
        A/tables/TABLE-4-page-11-5/prompt.txt: 94c845b02713e7b7d412d57ed6c893feeff84c0d6505f71ce17d3f88c02330ca
        A/tables/TABLE-4-page-11-5/meta.json: 13620b5012b28eed15dbfc1db64ef82bc1f76944fb72f9767162d06978cc5aaf
        A/tables/TABLE-3-page-6-2/raw.json: 89d51a002ef8fb6fde6855900685314c22d8931630cf0a4b518e3371a3bb9a8e
        A/tables/TABLE-3-page-6-2/prompt.txt: 332a84f678c1103387fc9afa576e93b31456117da51270c3b627cc0bb1927a5d
        A/tables/TABLE-3-page-6-2/meta.json: b30f8936de811b31ba951538601e8d1ec100582564b1e8e047dda5e5aa872252
        A/tables/TABLE-2-page-7-3/raw.json: 8dcbc4d0b92f8808f335a1ff2fb0e5b8d41ca7c5b0ab81d61647e7993fb9d4fe
        A/tables/TABLE-2-page-7-3/prompt.txt: 17765e753d6c9dbf79274f5eb658c44ab13f1694d1f3a5449bbaad711960c545
        A/tables/TABLE-2-page-7-3/meta.json: 0c09bf4ce5376a88d9618a9c1406779ca5a57c23cca27b510328f0701ecbdccf
        A/tables/TABLE-3-page-9-4/raw.json: cd48135e318d51fb37dd04602bf193d91253383f91e433f3a612da2fadf3258e
        A/tables/TABLE-3-page-9-4/prompt.txt: c28d8ed9678c25eec7f5101b1c51d807fe4676b5ad23c1c015bcdbfff4859ed7
        A/tables/TABLE-3-page-9-4/meta.json: 1651b911b2da4ebe45961fb7702397d5132112a56da399b106eb55496265651f
        A/tables/TABLE-1-page-4-1/raw.json: 9eb9e5fe3ac351adcda5c88f2e17c6af53afe5816e5386738c530a78599d535f
        A/tables/TABLE-1-page-4-1/prompt.txt: 4bac6d617d96dc09129d77127bd39444660db528bfe508f60d245eec842f958b
        A/tables/TABLE-1-page-4-1/meta.json: 405c2b4eab74d4e6a1bbec5d44998481f822b7fa3315cadfba74a1b286d00699
        B/passages.json: 670589637617e963cc0cd28f1d0b4ad6b1640c7a051a672c5012c9453f02d1bf
        B/raw.json: a78e2858d7270f7252e100bd1e8494c86fc2413ee05dadb9b5a85d08c369590d
        B/source-units.json: 8180cca81d41ccd49ac0b1e5dd7053c8f518bdd51d13a480de2e184cbcca4114
        B/full-source-units.json: dd2438563b9f0d622c2c45d98887eb26bac0d454fc4574376eeb5439e2faf549
        B/meta.json: f77afdd29cae2a59a8de655e2b179e78583fe3b55c9e75e4dd385a0b7624389d
        B/table-images/TABLE-3-page-9-1.png: a4390cb290275f5653212d893d8ab6db633f6472cf0981788f65ad4ab5ff8eb4
        B/table-images/page-11.png: eaa1cf18b85a7cf8d79ae92c9cf8476193ff61a7eff2a0ed3f727650df126715
        B/table-images/page-6.png: 93c602ce7bddce27a3bca2d55e9c04e63a2a45703c74ae4fcbab110c8c91d959
        B/table-images/page-7.png: f0d103da2121208f58ee57f3f01ab6665d3d09ec378494ff37bb8007053d57a9
        B/table-images/TABLE-4-page-11-1.png: 14469c610a12555dd7f9c5df5fa006fcb535836fb28dcfce9f9c5e91d4e86df0
        B/table-images/page-4.png: 999e64f700a92738418a7bf69bff7c996cb056edb8dbff306038ca79519c5915
        B/table-images/TABLE-1-page-4-1.png: a5a7a8b1e9d4f356d438e092c03ae57d12c98106b94315241cf15d3ef1291f88
        B/table-images/page-9.png: 4f5d5f80d0b28491be9b4204873e3a0c14194a1abca3d1582c199c36fe20ec16
        B/table-images/TABLE-3-page-6-1.png: ae60e3e594eb116a2634bc42ee15d742562601a4cb91637c82bed5475b48371d
        B/table-images/manifest.json: 27cf864084ef5ea3551049a2d4fd4bf3e5d633522f0691b08216eb48db43ab6c
        B/table-images/TABLE-2-page-7-1.png: 610ada8e94c8571d2e58336ddf9d986636e972e1102df27e9e45a3762edf651f
        B/clauses/window-03/raw.json: 576274417330b374edd8940f7d2119ae50becbf9d37be8a5edf1bc97b7112432
        B/clauses/window-03/prompt.txt: b8e4f3774f7b05c0fe0661c02728658eff15474316fd218d962f8ad00f7c7177
        B/clauses/window-03/meta.json: 0e5f1b99eba9dc03792d07c64e4519b6a87782213795d044efe356796a183874
        B/clauses/window-04/raw.json: d033230a0ebf53f387345a1f8ac043317537212707bebeef0a1ad41c39330c5c
        B/clauses/window-04/prompt.txt: 1a5cd7aa5d63a41482e8bcdf7974d9dcba9c1f9d4c111cc425b158d33b6d88a8
        B/clauses/window-04/meta.json: dfcb964ec1c9e35f93c47d6e0263f1c4beb5eab614f4bf088dcc979521415f3b
        B/clauses/window-05/raw.json: 302ceb8735f26fdc9eb55a7c9722ce3f53755a12af81a9205bea01aa43ced7e3
        B/clauses/window-05/prompt.txt: 2c367a4565a8175199f783bce1b8415c5d45277d02eb3910df69c045b0fdf1c0
        B/clauses/window-05/meta.json: 31949fa0759f0fea174a4c9d0c79144810b2fe5bddbbf23e7615413e727430db
        B/clauses/window-02/raw.json: c43f2ae2bb1643a16b1ef99a89abfbe0ca90cb25cc1fc5b3a6cfc433afdffc64
        B/clauses/window-02/prompt.txt: e79208981eb4d96b10759a1919151ac6c79c9eae2c7846a61004ff394da70979
        B/clauses/window-02/meta.json: 29a4557e1171d9dcd439ad1918b7761608b62ae8b4b2f0e6579a7bb6ef791f52
        B/clauses/window-07/raw.json: 886bd7c6feb1580405c92c23d13f82c32689b645b66ca259ef552ec6e3f987cb
        B/clauses/window-07/prompt.txt: 5f7d335d9e54a7c798f54ca23b70c9e00afe5d8c148edb2eee3080031367428f
        B/clauses/window-07/meta.json: c0f57415bacbf6a0a69003b6e6684c91e3ce1941aab54a011b08c99e3e374f0d
        B/clauses/window-01/raw.json: e7368f150d6bc15b8fd39b494a696e3214c05b7bada2ae24df9e90a6ab210c34
        B/clauses/window-01/prompt.txt: eae08fffb4a6d91b929f3ea4bfc5827ebf8bf638124025b65c2d2ac5aa5af988
        B/clauses/window-01/meta.json: 62117a95cdd1ca072c3f89588cb09dd181313f4d3ac370c6b43bff5e7af0cd77
        B/clauses/window-06/raw.json: 470517e3e07fd064f6ac8a2eb1e862047ab07bd0ae781accee2e8f258b21486e
        B/clauses/window-06/prompt.txt: ae5b10a6d32e030e2fdd146097a5b641813fe86090c67db2d5f0b2834b1e956d
        B/clauses/window-06/meta.json: 91b86dd7b39e361976fe26ad0eb5f7064c9be04a974b38f6416b3b61fb9641af
        B/tables/TABLE-4-page-11-5/raw.json: 4afc72dbd1face08889e93aa4f69e405de9d0ab15e7f5298213e6dd8215b4ee6
        B/tables/TABLE-4-page-11-5/prompt.txt: 94c845b02713e7b7d412d57ed6c893feeff84c0d6505f71ce17d3f88c02330ca
        B/tables/TABLE-4-page-11-5/meta.json: ced1b8ab4c810689ed9d5c4d8f14b3b6335fd49fc4770be6f58c21632cdec29f
        B/tables/TABLE-3-page-6-2/raw.json: d3c02909e1ff63cb03f16e3b20b7e1273fd367ca9ff0cb75e84beb033f6157b7
        B/tables/TABLE-3-page-6-2/prompt.txt: 332a84f678c1103387fc9afa576e93b31456117da51270c3b627cc0bb1927a5d
        B/tables/TABLE-3-page-6-2/meta.json: 2bc97f4ee8a3789ee03825db76d3ddddcf325df67081fd1ac0e626b49927cab8
        B/tables/TABLE-2-page-7-3/raw.json: 6c7b44d12b26df4c72098bef3288c95abf6070b73bc4c565a1c29120e9cb2359
        B/tables/TABLE-2-page-7-3/prompt.txt: 17765e753d6c9dbf79274f5eb658c44ab13f1694d1f3a5449bbaad711960c545
        B/tables/TABLE-2-page-7-3/meta.json: b9457e372abc0de4730865cfcb4451d1f842285bb7199f0dc1aceb170be5eace
        B/tables/TABLE-3-page-9-4/raw.json: dc201cbd68afb8aeaf9433d3d20335df85f732be2fa49a3553245e9213f20802
        B/tables/TABLE-3-page-9-4/prompt.txt: c28d8ed9678c25eec7f5101b1c51d807fe4676b5ad23c1c015bcdbfff4859ed7
        B/tables/TABLE-3-page-9-4/meta.json: 2b401f76b71be73b1b925bf8f62428493854ac7fe21b37ddf71494b21251f567
        B/tables/TABLE-1-page-4-1/raw.json: 6e31c1f0ae7887ae43ef95d5c5d5cf9f070a8c7b9ba08e41d70b64a24b85bbae
        B/tables/TABLE-1-page-4-1/prompt.txt: 4bac6d617d96dc09129d77127bd39444660db528bfe508f60d245eec842f958b
        B/tables/TABLE-1-page-4-1/meta.json: 83b4608741f04a87d690f1a4ed8462316cd378184a819bd8bdf24ae2e2632f36
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
      pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2024
      source_status_sha256: dd4d3fd671ae86ce4ac0e304da9b89e2034f7255c0aba65dba07fc084a6e383e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: damage to PALPA RhymeJudge and WAB-R AudWordRec tasks
    outcome:
      text: behavioural deficits
    analysis_label: Voxel-based lesion-symptom mapping (Null)
    relation: association
    evidence_ids:
    - P10-S1-C6
    qualifier_ids:
    - P10-S1-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2024
      source_status_sha256: dd4d3fd671ae86ce4ac0e304da9b89e2034f7255c0aba65dba07fc084a6e383e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C14
      - Result passage disposed without unit P5-S2-C7
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C7
      - Accounting without a linked unit P6-S1-C8
      - Accounting without a linked unit P6-S1-C9
      - Accounting without a linked unit P7-S1-C1
      - Accounting without a linked unit P7-S1-C2
      - Accounting without a linked unit P7-S1-C3
      - Unaccounted source passage P7-S1-C3
      - Unaccounted source passage P7-S1-C2
      - Unaccounted source passage P6-S1-C8
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P7-S1-C1
      - Unaccounted source passage P6-S1-C6
      - 'window 5: invalid/duplicate disposition P7-S2-C3'
      - 'window 5: invalid/duplicate disposition P7-S3-C2'
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S2-C1
      - Result passage disposed without unit P12-S2-C2
      unattached_null_or_qualifier_ids:
      - P6-S1-C7
      - P6-S1-C8
      - P10-S1-C3
      - P10-S1-C4
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 132
      unselected_timing_passages:
      - P4-S2-C7
      - P12-S1-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C5
        - P1-S1-C6
        - P1-S1-C7
        - P1-S1-C9
        - P3-S2-C5
        - P3-S2-C6
        - P3-S2-C7
        - P4-S2-C4
        - P4-S2-C6
        - P5-S2-C9
        - P5-S2-C10
        - P5-S3-C4
        - P5-S3-C6
        - P5-S4-C2
        - P6-S1-C9
        - P7-S1-C2
        - P7-S1-C4
        - P7-S1-C5
        - P8-S1-C2
        - P8-S2-C7
        - P9-S1-C3
        - P9-S1-C4
        - P10-S1-C2
        - P11-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-3
      - TABLE-3-page-6-2
      - TABLE-3-page-9-4
      - TABLE-4-page-11-5
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-3-page-9-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S1
        - P7-S2
        - P8-S2
        - P10-S2
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
      source_review: _compare/relationships-2026-11-16/review-current/Matchin2024
      source_status_sha256: dd4d3fd671ae86ce4ac0e304da9b89e2034f7255c0aba65dba07fc084a6e383e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement of WM load localization to dorsal stream.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of syntactic comprehension localization to ventral stream.
    - source_id: P5-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes imaging coverage/statistical power.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on hemisphere connectivity strength.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pointer to Table 2.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pointer to Figure 2 and Table 3.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pointer to Figure 3.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on multiple regression significance.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on WAB-R AQ prediction.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports relationship between triplets and non-canonical sentences.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports voxel-based LSM results for triplets task.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend for lesion overlap.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies anatomical regions for WM load association.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports voxel-based LSM results for non-canonical sentence comprehension.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Compares univariate and multivariate ROI-based LSM.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Reports CLSM results for WM load.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports CLSM results for non-canonical sentence comprehension.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Compares univariate and multivariate CLSM.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pointer to Figure 3B and D.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports fibre tracking results for WM and syntax.
    - source_id: P7-S3-C1
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Table 2 data for behavioural regressions.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation analysis parameters.
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Page footer.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of differentiation.
    - source_id: P8-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Summary of lesion and disconnection results.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports behavioural associations between triplets, non-canonical, and
        RhymeJudge.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Reports relationship between WAB-R AQ and Repetition.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of absence of relationship between repetition and non-canonical
        sentences.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports LSM results for WM load.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses importance of covariates.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of CLSM results for WM load.
    - source_id: P9-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 3 data (transcribed in results).
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 1
      - 3
      reason: Reports LSM and CLSM results for non-canonical sentence comprehension.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null result for RhymeJudge and AudWordRec.
    - source_id: P10-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pointer to Figure 3.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend for CLSM.
    - source_id: P11-S2-C1
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Table 4 data for CLSM results.
    - source_id: P12-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Conclusion summarizing dissociation.
    - source_id: P12-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on the utility of the triplets task.
    unresolved_coverage:
    - source_id: P6-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P1-S1-C9
    - P5-S1-C14
    - P5-S2-C7
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P7-S2-C3
    - P8-S1-C2
    - P8-S1-C3
    - P8-S2-C6
    - P9-S1-C4
    - P9-S2-C3
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S2-C1
    - P12-S1-C10
    - P12-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-3
    - TABLE-3-page-6-2
    - TABLE-3-page-9-4
    - TABLE-4-page-11-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C5
      - P1-S1-C6
      - P3-S3-C8
      - P5-S3-C5
      recruited_sample:
      - P3-S3-C4
      eligibility:
      - P3-S3-C6
      imaging_provenance:
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C15
      - P5-S2-C1
      imaging_timing:
      - P3-S3-C6
      outcome_timing:
      - P3-S3-C6
      outcome_definition:
      - P4-S1-C6
      - P4-S1-C8
      - P4-S1-C11
      - P4-S1-C12
      - P4-S2-C5
      validation:
      - P4-S1-C10
      analysis_restrictions:
      - P5-S3-C6
      - P6-S1-C1
      dependent_variable_statement:
      - P5-S3-C2
      - P5-S3-C4
      limitations:
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P5-S3-C6
      descriptive_personal_factors:
      - P4-S3-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C5
      - P1-S1-C6
      - P1-S1-C7
      - P1-S1-C9
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C7
      - P4-S2-C4
      - P4-S2-C6
      - P5-S2-C9
      - P5-S2-C10
      - P5-S3-C4
      - P5-S3-C6
      - P5-S4-C2
      - P6-S1-C9
      - P7-S1-C2
      - P7-S1-C4
      - P7-S1-C5
      - P8-S1-C2
      - P8-S2-C7
      - P9-S1-C3
      - P9-S1-C4
      - P10-S1-C2
      - P11-S1-C2
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
      pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
      review_sha256: 0c5df108760f5139cb1a0da1563dc9e0e95542e070a892cce02187133159521b
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
      - P10-S1-C6
      source_result: The source reports that no regions were found for which damage
        was significantly associated with deficits on the PALPA RhymeJudge and WAB-R
        AudWordRec tasks when including total lesion volume as a covariate and correcting
        for multiple comparisons with permutation testing. This is a null finding
        (no detected association) for these specific covariates/tasks in the lesion-symptom
        mapping analysis.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the Voxel-based lesion-symptom
            mapping (VLSM) for the PALPA RhymeJudge and WAB-R AudWordRec tasks, as
            described in P10-S1-C6. The draft correctly identifies this as a null
            result for these specific tasks.
          source_ids:
          - P10-S1-C6
          - P5-S3-C6
        direction:
          answer: fits
          reason: The source explicitly states 'We did not find any regions...', which
            aligns with the 'no_effect' direction in the draft. The draft correctly
            interprets this as a lack of statistically detected association, not a
            proof of zero effect.
          source_ids:
          - P10-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to regions (JHU atlas)
            associated with the specific tasks. The outcome is behavioural deficits
            on those tasks. The method is VLSM. The patient measurement is template_lesion_overlap
            (lesion maps overlaid on standard space/atlas), not patient_diffusion,
            as the primary analysis is voxel-based lesion mapping, not connectome-based
            (though connectome was also done, the null finding cited is for the lesion
            mapping or the general finding for these tasks). P10-S1-C6 refers to the
            general finding for these tasks. P5-S3-C6 confirms VLSM was performed.
            The draft's 'definition' as 'proportion damage to regions of the JHU atlas'
            is consistent with the VLSM method described in P5-S3-C6 and P6-S1-C1
            (though P6-S1-C1 mentions SVR without lesion volume, P10-S1-C6 explicitly
            mentions 'including total lesion volume as a covariate', which aligns
            with the primary VLSM in P5-S3-C6).
          source_ids:
          - P10-S1-C6
          - P5-S3-C6
          - P3-S3-C9
          - P3-S3-C10
        qualifications:
          answer: fits
          reason: 'The draft includes the critical qualifications: ''total lesion
            volume was included as a covariate'' and ''corrected for multiple comparisons
            using permutation testing''. These are explicitly stated in P10-S1-C6.
            The limitation regarding ''linear sequencing demands'' is also included
            from P12-S1-C6.'
          source_ids:
          - P10-S1-C6
          - P12-S1-C6
        missing_material_caveat:
          answer: fits
          reason: 'The draft captures the main caveats: the null result is specific
            to the inclusion of lesion volume and multiple comparison correction.
            It does not omit any material caveat that would change the interpretation
            of the null finding. The contrast with previous studies is mentioned in
            the source but is not a caveat to the current finding''s validity, rather
            a comparison. The limitation about linear sequencing is included.'
          source_ids:
          - P10-S1-C6
          - P12-S1-C6
      optional_pending:
      - Sample size for this specific null analysis is not explicitly transcribed
        in the selected source window, though P5-S3-C5 suggests 103 participants for
        most analyses except non-canonical sentence comprehension. Confirmation of
        N for RhymeJudge/AudWordRec VLSM is pending.
      - Specific cluster sizes or coordinates for the null finding are not applicable
        as no significant clusters were found, but detailed statistics (e.g., exact
        p-values of non-significant results) are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific null analysis is not explicitly transcribed in
      the selected source window, though P5-S3-C5 suggests 103 participants for most
      analyses except non-canonical sentence comprehension. Confirmation of N for
      RhymeJudge/AudWordRec VLSM is pending.
    - Specific cluster sizes or coordinates for the null finding are not applicable
      as no significant clusters were found, but detailed statistics (e.g., exact
      p-values of non-significant results) are not transcribed.
    normalizations:
    - field: sample.n
      original: 103
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R010
      exposure:
        text: damage to PALPA RhymeJudge and WAB-R AudWordRec tasks
      outcome:
        text: behavioural deficits
      analysis_label: Voxel-based lesion-symptom mapping (Null)
      relation: association
      evidence_ids:
      - P10-S1-C6
      qualifier_ids:
      - P10-S1-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
        source_review: _compare/relationships-2026-11-16/review-current/Matchin2024
        source_status_sha256: dd4d3fd671ae86ce4ac0e304da9b89e2034f7255c0aba65dba07fc084a6e383e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 149c56aa49a55d479240eee0d965bf2e2534b7d19cf4844fe95db7e75ab67e5a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 27bd2bcebfa26f0faeb8b880bbdc11617510486a7159cd3899f6918325f6fe90
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C6
          page: 3
          text_layer_sha256: 27bd2bcebfa26f0faeb8b880bbdc11617510486a7159cd3899f6918325f6fe90
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All participants \nwere at least 1 year post-stroke."
        anchor_text: "All participants \nwere at least 1 year post-stroke."
        excluded_fragments: []
        image_sha256: cd0285b239d029ab08c1948f8a06ba7a8c453f94d3656af3aa3ca43b6bd741f0
        transcription: 'All participants

          were at least 1 year post-stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "We did not find any regions for which damage was signifi­\ncantly associated\
    \ with deficits on the PALPA RhymeJudge \nand WAB-R AudWordRec task when including\
    \ total lesion \nvolume as a covariate and correcting for multiple compari­\n\
    sons with permutation testing, which contrasts with previous \nstudies that have\
    \ found significant effects for the same or \n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
