---
id: left_frontal_executive_cluster
name: Left frontal executive-function cluster
kind: network
findings:
- id: f1
  target: executive_functions
  target_kind: impairment
  claim: The executive-functions PCA factor (especially D-KEFS concept formation and
    problem solving) was associated with left IFG pars triangularis/orbitalis and
    dorsolateral prefrontal tissue integrity. After adding lesion volume, this association
    met significance only at a relaxed voxel threshold (p<0.05), not the original
    p<=0.001; cluster FWE p<0.05 remained the criterion. These are cross-sectional
    associations in a selected chronic-anomia cohort, not treatment-response or recovery
    predictions.
  direction: likely
  relationship: correlational
  method: VBCM
  design: cross-sectional
  sample:
    n: 36
    population: Adults with aphasia after a single left-hemisphere stroke
    phase: chronic
    time_post_onset: At least 12 months; Table 1 range 1–34 years
    cohort: English-speaking chronic anomia cohort; good single-word comprehension,
      relatively spared monosyllabic repetition, no speech apraxia
  statistics:
    threshold: Main maps voxel p<=0.001, cluster FWE p<0.05; executive factor after
      lesion-volume adjustment requires voxel p<0.05
    effect_size: Z statistics/coordinates in Table 3; not individual-patient effect
      estimates
  confounders_controlled:
  - Other three PCA factor scores; additional models assess lesion volume, age and
    time post-stroke
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: Reported Harvard–Oxford labels; no whole-parcel equivalence or sphere
      radius inferred
  author_limitations:
  - Small sample (36); PCA uses 55 variables
  - Structural MRI/VBCM not optimised for white-matter fibre bundles
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
  imaging: T1
  imaging_details:
    reference_space: other
    reference_space_detail: MNI; exact template variant not specified
    atlases_used:
    - Harvard–Oxford (as reported by authors)
    coordinates_reported:
    - region: Left IFG pars triangularis
      mni:
      - -44
      - 36
      - 2
    - region: Left IFG pars orbitalis
      mni:
      - -40
      - 42
      - -8
    - region: Left dorsolateral prefrontal cortex
      mni:
      - -30
      - 44
      - 4
  lesion_mapping:
    analysis: univariate
    n_analysed: 36
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: cluster_fwe
  notes: 'Age and time post-stroke did not change map patterns; not individual null
    effect tests. Figure numbering inconsistent in prose: cluster map Fig.1 p3, overlap
    Fig.2 p5. Table 3 peaks kept with their reported labels, including white matter
    despite stated Harvard–Oxford naming; atlas reconciliation remains pending.'
  citation: '@Akkad2023'
  source_passages:
  - section: Source passage P5-S3-C2
    page: 5
    quote: "Performance on the executive functions factor was uniquely related \n\
      to a cluster of voxels in the left frontal lobe, with peak voxels in the left\
      \ \ndorsolateral prefrontal cortex and the left inferior frontal gyrus (LIFG,\
      \ \npars orbitalis and pars triangularis)."
    supports: claim
  - section: Source passage P2-S5-C1
    page: 2
    quote: "Thirty-six English speakers with chronic aphasia following a single \n\
      left-hemisphere stroke participated in the study (see Fig. 1 for a lesion \n\
      overlap map, Table 1 for demographic and clinical data)."
    supports: sample
  - section: Source passage P5-S1-C3
    page: 5
    quote: "The analysis used the four continuous multidimen­\nsional predictors of\
      \ the PCA factor scores, which are necessarily un­\ncorrelated (orthogonal)\
      \ with one another; these were entered \nsimultaneously as continuous behavioural\
      \ covariates."
    supports: method
  - section: Source passage P5-S1-C4
    page: 5
    quote: "The outcome of \nthe analysis therefore denotes which voxels’ variation\
      \ in tissue con­\ncentration corresponds to the unique variance in a given principal\
      \ \ncomponent, while controlling for variation in the other components in \n\
      the analysis."
    supports: method
  - section: Source passage P5-S1-C6
    page: 5
    quote: "All analyses were performed with and without a correction for lesion \n\
      volume."
    supports: confounders
  - section: Source passage P5-S1-C7
    page: 5
    quote: "All anatomical labels were based on the Harvard–Oxford atlas \nin MNI\
      \ space. \n3."
    supports: imaging_details
  - section: Source passage P5-S2-C7
    page: 5
    quote: "Results are \nthresholded at p ≤0.001 voxel-level and p < 0.05 FWE corrected\
      \ at \ncluster-level."
    supports: statistics
  - section: Source passage P6-S1-C2
    page: 6
    quote: "Including age and time post-stroke in the VBCM model with the PCA \nfactor\
      \ scores did not alter the pattern of results obtained."
    supports: confounders
  - section: Source passage P6-S1-C4
    page: 6
    quote: "However, \nincluding lesion volume in the model reduced the significance\
      \ of the \nexecutive functions measure, which only reached suprathreshold at\
      \ \nvoxel-level p < 0.05 and FWEc cluster-level p < 0.05, but did not alter\
      \ \nthe pattern of results in the remaining 3 PCA factors."
    supports: limitation
  - section: Source passage P6-S4-C3
    page: 6
    quote: "Principal Component \nLocation \nExtent (voxels) \nZ \nMNI co-ordinates\
      \ \nx \ny \nz \nF1 (Phonology) \nLeft Superior Parietal Lobe \n175  \n4.16 \n\
      −34 \n−54 \n58 \nF2 (Executive Functions)  \n1563      \nLeft Inferior Frontal\
      \ Gyrus (Pars Triangularis)   \n3.93 \n−44 \n36 \n2  \nLeft Inferior Frontal\
      \ Gyrus (Pars Orbitalis)   \n3.59 \n−40 \n42 \n−8  \nLeft Middle Frontal Gyrus\
      \ (Dorsolateral Prefrontal Cortex)   \n3.56 \n−30 \n44 \n4 \nF3 (Verbal Working\
      \ Memory)  \n5262      \nLeft Posterior Superior Temporal Gyrus   \n4.49 \n\
      −58 \n−28 \n6  \nLeft Superior Longitudinal Fasciculus   \n4.94 \n−38 \n−44\
      \ \n18  \nLeft Posterior Thalamic Radiation   \n5.35 \n−36 \n−46 \n2 \nF4 (Semantics)\
      \  \n209      \nLeft Superior Temporal Pole   \n4.82 \n–22 \n10 \n−24  \nLeft\
      \ Middle Temporal Pole   \n4.47 \n−20 \n12 \n−34   \n2343      \nLeft Superior\
      \ Temporal Gyrus   \n4.14 \n−64 \n−10 \n−4  \nLeft Middle Temporal Gyrus   \n\
      4.14 \n−62 \n−14 \n−12 \nOnly clusters with cluster-level FWEc p < 0.05 are\
      \ shown in the table."
    supports: statistics
  - section: Source passage P5-S2-C13
    page: 5
    quote: "Note that VBM and \nstructural MRI scans are not optimised for the detection\
      \ of white matter \nfibre bundles."
    supports: limitation
  - section: Source passage P5-S2-C14
    page: 5
    quote: "As such, any interpretation of white matter tracts should \nbe made with\
      \ caution."
    supports: limitation
hemisphere: left
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-17'
relationship_review:
  paper: Akkad2023
  proposal_id: U005
  review_status_sha256: 15ad6658b87971a6e568f6ae98cd0be730493d4704512aa6376c56a31606b3df
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
      A/passages.json: 8c6cf2b3daafd546e3ce17ada8141a3d1e940ecc90f70c4625d1d88cbe44ebdb
      A/raw.json: 119f238116774559d4d8fe39b1850918f4253ab4df7c6504c2d76b06d5ea861a
      A/source-units.json: 0b6e7b4ecac4cc15b854d9d6244ad327fd2853c3e7e1f6283464dfac06b2fa50
      A/full-source-units.json: eb83db8d362899e54f24fb7a0b52bb14e3e491568ba7b1f5df858d76b95f2e2b
      A/meta.json: 0ad5e15295dfb6ac7a5f11e29cea643cc7567cc2c21e26bf2b31602d6814265f
      A/table-images/page-6.png: 08aacae3c967dee76d396065585a0a4cb4270bdc3fccdb697c1887f3bf33e7e6
      A/table-images/page-4.png: 178e254ac56b367b9ba1984ce7f44b02ec724749abe7e333a3e0a21cfd63e7b4
      A/table-images/TABLE-1-page-4-1.png: 0369966b0095e1349e7a393b27d1b9ce07be71431ff50833e3cd5efed11b7c85
      A/table-images/TABLE-3-page-6-1.png: 7b48e852629aa7042af308d192015c5c84814d7bd5e845132cdedbd095b3621f
      A/table-images/TABLE-2-page-4-2.png: 6c2623fe0939da6deb0706d37c6fa1ed2500e2d7cff3ba1566e3327ccd39fea2
      A/table-images/manifest.json: 57a893bf52bf6dc7c8e5703c711bedd1ec64f88bb4827f8be478a3cf11b4f4fc
      A/clauses/window-03/raw.json: fb2ebcdb9ca66fe581b1ce8b5cd6b9b587a499c5340beaf5f48b69b224fd9f91
      A/clauses/window-03/prompt.txt: 1bf39734a2bd21111625aed07717ce8671b3fbf7579b3f041af37459b3f1e668
      A/clauses/window-03/meta.json: 071fc8cb33ba16ddca064281c59bf3dc450c669fb6d6146c33eac4f9b1ac5d7a
      A/clauses/window-04/raw.json: 9f01ed7e33d92a08cba31baed75619958f7cd020eb295cfb39fba079c589e348
      A/clauses/window-04/prompt.txt: 718622945ab855d2ccfad5383921de5518fccbf55b564c21014bb94f792dd09d
      A/clauses/window-04/meta.json: ed01824402c0397d6f2233d3f72be0b04c9b0f2f64b938cd7652c8cb3c530375
      A/clauses/window-05/raw.json: a56a435ebaef11f3bb7dab955e16f5dbd74696b1f61f1edd1892cb3cf9e36e8a
      A/clauses/window-05/prompt.txt: e81462383fe5e8003f3ba4a03a01d3eb9f340ccf814c2b92058e46bf69acf55d
      A/clauses/window-05/meta.json: 6b5e8dcfad4039ae2b5d38f5e5f612192874987dc4988874aaf1ea5ecf1570b0
      A/clauses/window-02/raw.json: 002891ab1fb5aa84a74f5ff323cea390e4b2dbc01d1be72f39ff0847e6dd1178
      A/clauses/window-02/prompt.txt: 81ff665755e53068034c71c31ffe028ecd7f800ad0785135e41cf1679e439c37
      A/clauses/window-02/meta.json: 8ed446778c7adb6c94c3e878684639a4aae070a6746134cd136c5d80d80690fd
      A/clauses/window-07/raw.json: 9cc67a5dbf62d98722ebafad17748f93e9844d15a83aada85269d78a46830bd3
      A/clauses/window-07/prompt.txt: 73badb46c3f3b9d98cf2e3d544f9fdc64dbd355e72e4373fd237a2d0831c2c9c
      A/clauses/window-07/meta.json: d8b2f0fd542a218e8941c8ec06edd83b91cb36f68566c29fbb437274454480cd
      A/clauses/window-01/raw.json: 9bf3af3e315a3067ddeb9ee1369c0b478fe3e6b0fd2d6e0e5fbfcd8b2ef0ba6b
      A/clauses/window-01/prompt.txt: e92dab33369c07205dfd02e8f8a80970a43fad527ed50148bcc5c16a03696715
      A/clauses/window-01/meta.json: dd9ee73230908ad42b63e90b12047297bcccd3b4cc6faadfacbd49e9a3667afa
      A/clauses/window-06/raw.json: 3c880c2036c7e094a731362363db1e18f5f06268ec6b27f5e81413a42ef38cf2
      A/clauses/window-06/prompt.txt: 832b157d3b49798257b027ecef0b76c78c8257eac14ecba8ffeba13a7d39d5d8
      A/clauses/window-06/meta.json: 65da4b01ef78edad4c5b2ba0917063c1faabf77709fc859839efe4b50aa35ca2
      A/clauses/window-08/raw.json: e707c704e012eacdd64db5a61f5dc8abcc1da7a9e4ee6fb9a47ee1573ab1e735
      A/clauses/window-08/prompt.txt: 46d2406d97ab52ef747854bb3bc341bd2f5bb209ad725fefa002e62fc4b3be0c
      A/clauses/window-08/meta.json: e5b421ffc9c3ded168129ba4d1a84a2ef5a61b68a694d4b59ca9f305cca28477
      A/tables/TABLE-3-page-6-3/raw.json: 8dfa59c6b4b4122a8749b4f5dceef005cb9bdf6e4c862072f9839de2fde3d3c1
      A/tables/TABLE-3-page-6-3/prompt.txt: 2cd8a4a4819c10fb017a613bdd9705e923ac2fdcafbe70af588729a6e48f202c
      A/tables/TABLE-3-page-6-3/meta.json: 9c6a9a57400ca7624fbada59e995bc8e923e15fc0e84afdb3685636037d61516
      A/tables/TABLE-1-page-4-1/raw.json: 34523ca975d3b354491b914d971c6246667378ce236c3c20d95025e48af6f0c0
      A/tables/TABLE-1-page-4-1/prompt.txt: b6b2fca8175855253046f4aeb2617d0bb039d65f141cf8f8177d7bf2953370a9
      A/tables/TABLE-1-page-4-1/meta.json: e5a3ab7d07e5c5b966e0ca4e2d150acb4125b29b8c7a7bf4c0d67d41aaab00db
      A/tables/TABLE-2-page-4-2/raw.json: a39f884564040d659c853e278fe792dfea8b91f51dcec4fa82e20765405f0682
      A/tables/TABLE-2-page-4-2/prompt.txt: 6bbb6563b1313f08f526ba7c5e9fbb067b222dd871f1e66241ccf9cf1f558bdf
      A/tables/TABLE-2-page-4-2/meta.json: fba781e3c19dcab686d4739e5b32f5153a1db2f1fa4d0d5710f8e72a84f6fc3a
      B/passages.json: 8c6cf2b3daafd546e3ce17ada8141a3d1e940ecc90f70c4625d1d88cbe44ebdb
      B/raw.json: 0ee1339a4c929cdc048bc8dec86c79892270497168d5ad5ff3c37df2440ce034
      B/source-units.json: 0b6e7b4ecac4cc15b854d9d6244ad327fd2853c3e7e1f6283464dfac06b2fa50
      B/full-source-units.json: eb83db8d362899e54f24fb7a0b52bb14e3e491568ba7b1f5df858d76b95f2e2b
      B/meta.json: 975aa54b2bc582d8a6a938cad3fa2d0408a0e367889423fad37d219d2e6ef0a2
      B/table-images/page-6.png: 08aacae3c967dee76d396065585a0a4cb4270bdc3fccdb697c1887f3bf33e7e6
      B/table-images/page-4.png: 178e254ac56b367b9ba1984ce7f44b02ec724749abe7e333a3e0a21cfd63e7b4
      B/table-images/TABLE-1-page-4-1.png: 0369966b0095e1349e7a393b27d1b9ce07be71431ff50833e3cd5efed11b7c85
      B/table-images/TABLE-3-page-6-1.png: 7b48e852629aa7042af308d192015c5c84814d7bd5e845132cdedbd095b3621f
      B/table-images/TABLE-2-page-4-2.png: 6c2623fe0939da6deb0706d37c6fa1ed2500e2d7cff3ba1566e3327ccd39fea2
      B/table-images/manifest.json: 1a81202cffd0ee9272d22dacb5cd9a05ffa480b56dc5e4b77edad175b7e4393e
      B/clauses/window-03/raw.json: 34722af7028b0efafba52b9a2195addb0315da5620c26d2f528f845edd00cf54
      B/clauses/window-03/prompt.txt: 1bf39734a2bd21111625aed07717ce8671b3fbf7579b3f041af37459b3f1e668
      B/clauses/window-03/meta.json: bc7557d755d9a94f25457f70d8174b79163c4291c2ef127e9a43d007eca3d925
      B/clauses/window-04/raw.json: df8b0d3d15090a3e7179a0a85b2f46673fec9f442e667a1ff535964ec737386d
      B/clauses/window-04/prompt.txt: 718622945ab855d2ccfad5383921de5518fccbf55b564c21014bb94f792dd09d
      B/clauses/window-04/meta.json: fb2273e4622aa5c8dbff55f649b582be8abbcc5ee8cda6a4282ee014f0324039
      B/clauses/window-05/raw.json: 5030cd3227048f8f2896aa1ef56ced1ea6387f8f9341159aa3860ce2145f7617
      B/clauses/window-05/prompt.txt: e81462383fe5e8003f3ba4a03a01d3eb9f340ccf814c2b92058e46bf69acf55d
      B/clauses/window-05/meta.json: 82b962fa6580546ccb2b75c54baaaa9d9fbec97a47c3b0d1140771ce396f6b45
      B/clauses/window-02/raw.json: b44ab149ba470c2f29ab6e427a33c1c20300ee1005e81e9ac6c886debb3c2891
      B/clauses/window-02/prompt.txt: 81ff665755e53068034c71c31ffe028ecd7f800ad0785135e41cf1679e439c37
      B/clauses/window-02/meta.json: 3e72b72defbe6bdfde2077632d4c93599c11a584db99919ac9c99b605f4fad6f
      B/clauses/window-07/raw.json: 1644384374c5d61c4422bcf07753bba967dcb320f28c3eba842619f96d3447d3
      B/clauses/window-07/prompt.txt: 73badb46c3f3b9d98cf2e3d544f9fdc64dbd355e72e4373fd237a2d0831c2c9c
      B/clauses/window-07/meta.json: af267c402b4f8a22838734bb0c5381dbb70a5fe4c7aa06cd8ce81dfc25f697b2
      B/clauses/window-01/raw.json: 89b3af628f868c9d4a028c496c794a93f6670fb59306e7e374833bec74895f2e
      B/clauses/window-01/prompt.txt: e92dab33369c07205dfd02e8f8a80970a43fad527ed50148bcc5c16a03696715
      B/clauses/window-01/meta.json: cf37f029687fc6d6ff7aabb74480f109a7e5d2ebd079dfc0a6c231aaef7e52f5
      B/clauses/window-06/raw.json: c915bbf3e536ac7b03407509affe23ef95051decb68a34de150c38c870767413
      B/clauses/window-06/prompt.txt: 832b157d3b49798257b027ecef0b76c78c8257eac14ecba8ffeba13a7d39d5d8
      B/clauses/window-06/meta.json: 14e8b3ba1965cb3b81e8a5ace0d791780a3e3452ddc026db46198f0077689775
      B/clauses/window-08/raw.json: efde6d505f1030374f070a22f70d4d6be883f05ae5e5e4593a2a96e1af494721
      B/clauses/window-08/prompt.txt: 46d2406d97ab52ef747854bb3bc341bd2f5bb209ad725fefa002e62fc4b3be0c
      B/clauses/window-08/meta.json: 330f9e24d4966b25f0b77c2aa570d2b646cebde19976d41e73fba6483de17a35
      B/tables/TABLE-3-page-6-3/raw.json: 37ad8984785f499f2ad735d29d6639d51787638c4f8010117efea3f2c73d63e4
      B/tables/TABLE-3-page-6-3/prompt.txt: 2cd8a4a4819c10fb017a613bdd9705e923ac2fdcafbe70af588729a6e48f202c
      B/tables/TABLE-3-page-6-3/meta.json: 9f1d524fdc3a9383ff48e474ff0ca11fad2be10053cd5b7f2b8fee51e7393070
      B/tables/TABLE-1-page-4-1/raw.json: 85b9734dfc99b0ff782da20fc6c5085f460ef829f0d669e62999c63a15c21af8
      B/tables/TABLE-1-page-4-1/prompt.txt: b6b2fca8175855253046f4aeb2617d0bb039d65f141cf8f8177d7bf2953370a9
      B/tables/TABLE-1-page-4-1/meta.json: 0e6ef5198c68c5ce5e255389d446b79ff8d83a724fa5d09a1b2ca4f26860199d
      B/tables/TABLE-2-page-4-2/raw.json: a71377cfe0c1143133f7dd7086f6c9c6b11e37829456f43db1f7f5a88116064c
      B/tables/TABLE-2-page-4-2/prompt.txt: 6bbb6563b1313f08f526ba7c5e9fbb067b222dd871f1e66241ccf9cf1f558bdf
      B/tables/TABLE-2-page-4-2/meta.json: b6aad5097601df6ae03cc717fb180455a7a8636aa71a0e7bd990a5f330983703
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
    - P5-S3-C2
    qualifier_ids: []
    context_ids:
    - P5-S1-C3
    table_ids: []
    exposure:
      text: executive functions factor
      source_id: P5-S3-C2
    outcome:
      text: left frontal lobe
      source_id: P5-S3-C2
    relation: association
    effect_unit: individual
    result_status: reported_detected
    outcome_type: status_at_assessment
    direction: positive
    direction_source_id: P5-S3-C2
    origin: current_study
    label_match_candidates: {}
    id: U005
    flags:
    - direction_unsupported
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P2-S5-C2
    - P2-S5-C3
    - P3-S1-C1
    - P3-S1-C2
    - P3-S2-C10
    - P3-S2-C11
    - P3-S2-C12
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C16
    - P3-S2-C2
    - P3-S2-C5
    - P3-S2-C6
    - P3-S2-C7
    - P4-S1-C1
    - P4-S1-C11
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C8
    - P4-S1-C9
    - P5-S1-C2
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C13
    - P5-S2-C14
    - P5-S2-C15
    - P5-S3-C7
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S3-C10
    - P7-S4-C2
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: cd0c4f4f69ca8dc7c692cb92fea4a4f7b7d5d282a4d895acff4efb54d563ddbc
  audit:
    coverage_issues:
    - Accounting without a linked unit P1-S2-C2
    - Accounting without a linked unit P1-S2-C3
    - Unaccounted source passage P1-S2-C3
    - Unaccounted source passage P1-S2-C2
    - Result passage disposed without unit P5-S1-C11
    - Result passage disposed without unit P5-S1-C12
    - Result passage disposed without unit P5-S2-C2
    - Result passage disposed without unit P5-S2-C3
    - Result passage disposed without unit P5-S2-C15
    - 'window 7: invalid/duplicate disposition P6-S3-C10'
    - Result passage disposed without unit P6-S4-C2
    - Accounting without a linked unit P7-S1-C11
    - Accounting without a linked unit P7-S1-C3
    - Accounting without a linked unit P7-S1-C7
    - Result passage disposed without unit P7-S2-C7
    - Unaccounted source passage P7-S1-C7
    - Unaccounted source passage P7-S1-C11
    - Unaccounted source passage P7-S1-C3
    - Result passage disposed without unit P7-S2-C8
    - Result passage disposed without unit P7-S2-C9
    unattached_null_or_qualifier_ids: []
    suppressed_nonrepresented_units: 17
    default_disposition_count_requires_completeness_check: 173
    unselected_timing_passages:
    - P1-S1-C11
    - P2-S3-C9
    - P2-S4-C13
    - P4-S2-C3
    - P6-S1-C3
    personal_effect_slots_without_result_classification: []
    held_frame_selections:
    - slot: validation
      source_id: P4-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    empty_frame_slots_require_confirmation:
    - validation
    - personal_factors
    - tested_personal_effects
    - explicitly_not_adjusted
    unclassified_extraction_ids:
    - P2-S2-C11
    table_review_required:
    - TABLE-1-page-4-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    unlinked_tables:
    - TABLE-1-page-4-1
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P2-S4
      - P2-S5
      - P3-S1
      - P3-S3
      - P4-S1
      - P5-S1
      - P5-S2
      - P5-S3
      - P5-S4
      - P6-S1
      - P6-S2
      - P6-S3
      - P7-S1
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C2
      recruited_sample:
      - P4-S2-C2
      eligibility:
      - P2-S5-C2
      - P2-S5-C3
      - P3-S1-C1
      - P3-S1-C2
      imaging_provenance:
      - P4-S1-C6
      imaging_timing:
      - P2-S5-C2
      outcome_timing:
      - P2-S5-C2
      outcome_definition:
      - P4-S1-C11
      validation: []
      analysis_restrictions:
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      dependent_variable_statement:
      - P4-S1-C11
      - P5-S1-C4
      limitations:
      - P6-S3-C10
      - P7-S4-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C12
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      - P5-S3-C7
      - P6-S1-C2
      - P6-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C2
      - P4-S2-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: validation
      source_id: P4-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
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
    - 7
    visual_pages:
    - 3
    - 4
    - 5
    - 6
    tables_checked:
    - 1
    - 2
    - 3
    figures_checked:
    - 1
    - 2
    corrections:
    - Converted variable-to-voxel model labels into explicitly correlational brain-behaviour
      claims; not causal predictions.
    - 'Retained lesion-volume sensitivity: executive-function cluster requires a relaxed
      voxel threshold after adjustment.'
    - Age/time-post-stroke are adjustment variables; stable maps do not establish
      independent null personal effects.
    - White-matter labels arise from structural MRI VBCM, not diffusion tractography
      or measured disconnection.
    - Results text points to Fig. 2, but the cluster map is Fig. 1 on PDF page 3;
      Fig. 2 on page 5 is lesion overlap.
    - Executive-factor lesion-volume r=-0.426, p=0.10 is retained as a source inconsistency;
      no correction or significance inferred.
    remaining:
    - Named-person approval; unresolved source inconsistency in lesion-volume executive-factor
      correlation.
    - Supplementary-only assessments and individual scores not extracted. Not evidence
      of treatment response.
    checked_by: agent:codex
    date: '2026-11-17'
    pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
    licence:
      category: cc
      label: CC BY 4.0
      url: http://creativecommons.org/licenses/by/4.0/
      version: published
      source: crossref
      doi: 10.1016/j.nicl.2023.103452
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
  page: 5
  quote: "Performance on the executive functions factor was uniquely related \nto\
    \ a cluster of voxels in the left frontal lobe, with peak voxels in the left \n\
    dorsolateral prefrontal cortex and the left inferior frontal gyrus (LIFG, \npars\
    \ orbitalis and pars triangularis)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-17'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
