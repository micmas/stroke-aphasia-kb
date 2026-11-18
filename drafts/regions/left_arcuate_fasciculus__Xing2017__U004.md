---
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
findings:
- id: f1
  target: auditory_sentence_comprehension
  target_kind: impairment
  claim: No statistically significant association was detected between left arcuate
    fasciculus DTI metrics (FA, MD, AD or RD) and sentence-level auditory comprehension
    after controlling for age, total lesion volume and lesion load within the tract
    (all uncorrected p>0.10).
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 40
    population: Native English-speaking chronic left-hemisphere stroke survivors with
      aphasia documented at stroke; able to follow instructions
    phase: chronic
    time_post_onset: At least 6 months
    cohort: 'Xing2017: same 40 participants across analyses; tract templates from
      a separate 27-person healthy sample'
  statistics:
    threshold: All uncorrected p>0.10 for AF DTI metrics; absence of a detected association
      is not proof of no contribution
    effect_size: 'Table 2 partial r: FA=0.074, MD=-0.079, AD=-0.088, RD=-0.072'
  confounders_controlled:
  - Age
  - Total lesion volume
  - Number of lesioned voxels in the tract
  - Word comprehension regressed out of the sentence outcome before analysis
  confounders_not_controlled:
  - Cortical involvement was not examined
  region_definition:
    kind: tract
    description: Left AF template built by probabilistic tractography in 27 healthy
      controls; group threshold >=50% (14/27), used to sample patient DTI metrics.
      Individual patient tracts were not reconstructed.
  author_limitations:
  - Patient-specific tract reconstruction was generally not possible because of varied
    lesions.
  - Clinical comprehension tasks may be less sensitive to complex syntax; AF segments
    were not assessed separately.
  - Cortical contributions were not examined.
  evidence_quality: cohort
  strength: moderate
  notes: This is a null result for diffusion metrics, not for every measure of AF
    damage. In a separate lesion-burden analysis adjusted for total lesion volume,
    AF lesion load was associated with sentence comprehension. Do not merge these
    analyses or interpret this null as proving that AF lesions are irrelevant. Sentence
    comprehension was residualised for word comprehension; it is not the raw composite.
  outcome_timing:
    type: status_at_assessment
    interval: Cross-sectional assessment at least 6 months after stroke; not longitudinal
      recovery
  imaging_details:
    reference_space: other
    reference_space_detail: MNI standard space; exact variant not stated
    atlases_used: []
  provenance:
    extracted_by: model:gemma4:31b; agent:codex source follow-up
    extracted_on: '2026-11-18'
    paper_section: Main paper Methods, Results and Table 2
    confidence: medium
    flags:
    - human_approval_pending
    - agent_source_followup_after_model_review
    - paper_completeness_pending
  citation: '@Xing2017'
  source_passages:
  - section: Main paper; agent follow-up
    page: 2
    quote: "Forty (14 females) chronic left hemisphere stroke survivors were \nrecruited\
      \ in the study with inclusion criteria as follows: native \nEnglish speaker;\
      \ at least 6 months post-stroke; able to follow test-\ning instructions; and\
      \ no history of other significant neurological \nillnesses. Demographics and\
      \ language scores for the group are \nlisted in Table 1. All patients had aphasia\
      \ at the time of stroke \nbased on medical records and received speech–language\
      \ therapy.\nProbabilistic tract reconstruction was performed in 27 healthy \n\
      older participants (16 female) without neurological and psychiat-\nric disorder.\
      \ The mean age was 59.8 (±14.3) years; mean educa-\ntion was 16.3 (±2.6) years.\
      \ Among them, 24 were right-handed, \n2 left-handed, and 1 ambidextrous.\n"
    supports: sample
  - section: Main paper; agent follow-up
    page: 3
    quote: "Tract-Specific Analysis\nTo examine relationships of more comprehensive\
      \ measures \nof entire tracts to behavioral performance, we conducted a \ntract-specific\
      \ analysis. To precisely localize relevant tracts, we \nreconstructed the left\
      \ inferior fronto-occipital fasciculus (IFOF), \ninferior longitudinal fasciculus\
      \ (ILF), and uncinate fasciculus \n(UF) tracts implicated by the TBSS analysis\
      \ (see Results) in 27 \nage-matched healthy subjects. For completeness, we also\
      \ recon-\nstructed the major dorsal language stream tract (AF) as well. \nPaired\
      \ regions in the left hemisphere was defined as “seed” and \n“target” to reconstruct\
      \ connections between these areas as previ-\nously described (24, 25). The regions\
      \ were reversely transferred \nto the subject’s native DWI space using non-linear\
      \ registrations \nfor FA images. Fiber tracking was performed using a probabilistic\
      \ \ntractography algorithm based on Bayesian estimation of diffu-\nsion parameters\
      \ (26). Fiber tracking was initiated from all voxels \nwithin the seed masks\
      \ in the diffusion space to generate 5,000 \nstreamline samples, with a step\
      \ length of 0.5 mm and a curvature \nthreshold of 0.2. The resultant tract density\
      \ maps were normal-\nized by dividing by the total number of streamline samples\
      \ and \nthresholded at 0.005 to exclude spurious connections. Tracts were \n\
      then non-linearly registered to MNI space using the registration \nparameters\
      \ for FA images as above. The final groupwise prob-\nability map for each tract\
      \ was generated with a threshold at least \n50% (14/27 = 0.52) of healthy subjects\
      \ (27, 28), and the respective \nbinary map was generated as template to extract\
      \ the mean values \nof DTI metrics for individual patient.\n"
    supports: region_definition
  - section: Main paper; agent follow-up
    page: 3
    quote: "To assess brain–behavior associations in the tracts identified \nabove,\
      \ we performed partial correlations between the mean \nvalues of FA, MD, AD,\
      \ and RD (as indexes of white matter integ-\nrity) and WLC and SLC scores (as\
      \ indexes of different level in \n"
    supports: method
  - section: Main paper; agent follow-up
    page: 4
    quote: "comprehension processing) controlling for age and total lesion \nvolume.\
      \ Direct lesion volume within a tract may dramatically \nalter the mean values\
      \ of the white matter integrity measures \nand could also covary with direct\
      \ damage in neighboring tracts \nor gray matter yielding spurious tract–behavior\
      \ relationships. \nTherefore, we further excluded the primary lesion load on\
      \ each \ntract from analyses by including the number of lesioned voxels \nin\
      \ the tracts as nuisance covariates in the analyses. Statistical \nanalyses\
      \ were performed using SPSS (version 22). As previously \ndescribed (29), we\
      \ considered tracts that showed significant cor-\nrelations with behavior for\
      \ the each DTI index at a threshold of \nP < (0.05/4) = 0.0125 (Bonferroni correction).\n"
    supports: confounders
  - section: Main paper; agent follow-up
    page: 4
    quote: "DTI metrics of the left AF did not relate \nto either WLC or SLC scores\
      \ (all uncorrected P > 0.10). "
    supports: claim
  - section: Main paper; agent follow-up
    page: 4
    quote: "DTI metrics of the left AF did not relate \nto either WLC or SLC scores\
      \ (all uncorrected P > 0.10). "
    supports: statistics
  - section: Main paper; agent follow-up
    page: 8
    quote: "Several limitations should be noted. First, lack of objective \nmeasures\
      \ of the individual tracts in patients is a main caveat of \nthis study. Due\
      \ to varied left hemisphere lesions, most of the left \nhemisphere white matter\
      \ connections could not be reconstructed \nwith probabilistic tractography in\
      \ individual patients. Under this \ncircumstance, white matter damage does not\
      \ necessarily indicate \nthat the adjacent cortical regions are crucial for\
      \ comprehension \nbehavior, but may rather indicate that connections between\
      \ the \nposterior and the anterior cortical regions are associated with \ncomprehension\
      \ performance. Second, we did not determine the \ninvolvement of left hemisphere\
      \ cortical areas in word or sentence \ncomprehension. Previous studies have\
      \ shown that regional gray \nmatter damage in the left temporal lobe might support\
      \ auditory \ncomprehension processing in patients with post-stroke aphasia \n\
      or primary progressive aphasia (4, 31, 32). Therefore, inter-\nrelationships\
      \ between both cortical structures and white matter \npathways involved in different\
      \ levels of auditory comprehension \nneed further investigation.\n"
    supports: limitation
  - section: Main paper; agent follow-up
    page: 3
    quote: "Raw scores were normalized by dividing by the maximum score \nof each\
      \ task, and these normalized scores for each component \nof comprehension were\
      \ averaged. Because sentence-level com-\nprehension encompasses word-level comprehension,\
      \ deficits in \neither could cause decreased SLC scores. Thus, the WLC scores\
      \ \nwere regressed out of the SLC scores to obtain a final residual \nSLC score\
      \ that controls for word comprehension deficits. Non-\nverbal semantic performance\
      \ was additionally assessed with the \nPyramids and Palm Trees (PPT) test (15).\n"
    supports: method
  - section: Main paper; agent follow-up
    page: 6
    quote: 'AF

      3,447

      −0.081

      −0.127

      0.129

      0.110

      0.138

      −0.439*

      0.074

      −0.079

      −0.088

      −0.072

      '
    supports: statistics
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-18'
relationship_review:
  paper: Xing2017
  proposal_id: U004
  review_status_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
      A/passages.json: 4b4086dc9237eedb41f63db3ac4ae53d010b9dc227bc51e0919cbb1f2d5cdfbe
      A/raw.json: c8e3c4d1e56b0da68df39ece5594d3d0ef86f881ee46ac521746449744fac852
      A/source-units.json: d254860e6657213b5b83a293926a6e23c3e0bf42ae16481f403d2aff52591281
      A/full-source-units.json: b96bdc8a08798beec2967f6d7b26be513dfa3d1f73e46a4d703c51b6d8cbc684
      A/meta.json: f4312d9a17d9bd7a1d6f0a4d2b1e1f7ed18c029d81004d5ad3ddf8207aca0224
      A/table-images/TABLE-1-page-2-1.png: 16edbd1c6189f1c685006d2ab2ace8f67ca2aff48d6fc3b2ce7b5a8394b5db0d
      A/table-images/page-2.png: 7e8a4efdf7603edaa806dd7516a19a433e07a5e6eaa8ea94ae91d92d1e8b33c6
      A/table-images/page-6.png: 452e3b3021e057afd3bd711d0aaa0938a7b53ffe640632ce242cf2a2862042bc
      A/table-images/TABLE-2-page-6-1.png: d2575a63e6cb4114dcfa178abc0438e8bc442ce2ffd207debef1f387c6afd433
      A/table-images/manifest.json: 4970b7611a7af8a58166004beb2a05be5dd94090c149bb5eed51fcdbd5220a35
      A/clauses/window-03/raw.json: 24c58cd01853d324fab6c1b70be8138ec81a7757275738d3768a4dc94971ac5a
      A/clauses/window-03/prompt.txt: 0100e93b60e10ca63d34d710b97308921ed42ab7bfc4915477020d719c8fd81f
      A/clauses/window-03/meta.json: f7829a57e3e01cd4d481344d4364b3c7586b41674568000b6867c8bb44310627
      A/clauses/window-04/raw.json: 68089b331501192c4fa223c8285554ea042c6681a6a94f1937843022db0ece40
      A/clauses/window-04/prompt.txt: ccab4e5b9fa08e1acae40364483fcc283c13b42be70824e841a850b81e0fb945
      A/clauses/window-04/meta.json: ed4d57644711a8d61fb7d7913ba20ecf13a49ddf9f0917ae8d8cc16fd930e45f
      A/clauses/window-05/raw.json: ee62c80bdacc44c8fd51529fb59aba84b81e72b9bdff7bdfc2a52a1031d017cb
      A/clauses/window-05/prompt.txt: c88c639547fc8f7b3a770a445bfbd9293d1f14c62296584894da7f75a163276c
      A/clauses/window-05/meta.json: af009ee9303f5bec9439014e02a91b20106630cdd92b684e747cd90c1bb53967
      A/clauses/window-02/raw.json: 513f6757d7b85eabaa07790e613cf7ada89e13ca959e4a127fd9a7cb339075fc
      A/clauses/window-02/prompt.txt: 252e282ec942d33f1e4aaa1b78e54efe213cd5ff86115eae89f8395195e3f54d
      A/clauses/window-02/meta.json: 80d8177745a0d1963c7979f9e6da07f8cf7a6015453aad33a310d404d3283b59
      A/clauses/window-01/raw.json: c364a3f5cf804af02c6d56abcd7ac77f0c88f30aac39b74c3f0793d3021918bd
      A/clauses/window-01/prompt.txt: f48cbfbeae32d3c32119e07098003da5f31271114cfa2ee8ff5f238b3278988c
      A/clauses/window-01/meta.json: 82c61b3782b720f9371912e1ac5f53c2548e3170ac55654ccf7f22bb29008582
      A/clauses/window-06/raw.json: 1ab0315ecd1a622f441c9f33746f8a2f79bfad06962f14e9c19f5643223b782f
      A/clauses/window-06/prompt.txt: 27e6fb7864c0d62ce4c420adda6c6694cc1e46b89d889d1a8f23092f06e3698b
      A/clauses/window-06/meta.json: 5b8eea60f2e61ba3f2e0a9cda27db57c64f804fde3a0e56f67ed99ba3da8939c
      A/tables/TABLE-1-page-2-1/raw.json: d6190287e62e6d9bbfca77d33cdd79e421053bb1a24114c8f191d9e94be15ba1
      A/tables/TABLE-1-page-2-1/prompt.txt: 3cc60833a295632344ab4aaeeccb1529728b8aaf1522666de9828eacb78c878d
      A/tables/TABLE-1-page-2-1/meta.json: 3b08b2ae7116fd14ed5afe00b313e10f95aef2bc3358349b1f14cd4d3d5216d9
      A/tables/TABLE-2-page-6-2/raw.json: 2204f1281dc5e03094b363d5c8c5b79dd89b3f7b9e97cda38f1deb7d56c97a23
      A/tables/TABLE-2-page-6-2/prompt.txt: f9460ab6c70914b7826a68abd2822aff0ec4a4f3b49f2fb88339b4f34f0bb601
      A/tables/TABLE-2-page-6-2/meta.json: dfaac7dcc6dcfc82037b6890f6f320ab51485e5f31bc730f8f83e3bb4c824569
      B/passages.json: 4b4086dc9237eedb41f63db3ac4ae53d010b9dc227bc51e0919cbb1f2d5cdfbe
      B/raw.json: ec908fd5fde55a01272be5d1cea7589a641a0ea40a66809ffb709703cf223577
      B/source-units.json: d254860e6657213b5b83a293926a6e23c3e0bf42ae16481f403d2aff52591281
      B/full-source-units.json: b96bdc8a08798beec2967f6d7b26be513dfa3d1f73e46a4d703c51b6d8cbc684
      B/meta.json: 75330a94943f58589f00ecec4cc1681850c730e524e3796e47d8fd6cdfd4e67e
      B/table-images/TABLE-1-page-2-1.png: 16edbd1c6189f1c685006d2ab2ace8f67ca2aff48d6fc3b2ce7b5a8394b5db0d
      B/table-images/page-2.png: 7e8a4efdf7603edaa806dd7516a19a433e07a5e6eaa8ea94ae91d92d1e8b33c6
      B/table-images/page-6.png: 452e3b3021e057afd3bd711d0aaa0938a7b53ffe640632ce242cf2a2862042bc
      B/table-images/TABLE-2-page-6-1.png: d2575a63e6cb4114dcfa178abc0438e8bc442ce2ffd207debef1f387c6afd433
      B/table-images/manifest.json: dabd9c6b6e19f18fe9e8cb43f6ab34ebeb61f25362b6eb3d61b8b7d342bee37b
      B/clauses/window-03/raw.json: 97e4277a80bc599bd82e71f6a6e351c2e7789260d2895a8e6173d4b3cc2e4d1f
      B/clauses/window-03/prompt.txt: 0100e93b60e10ca63d34d710b97308921ed42ab7bfc4915477020d719c8fd81f
      B/clauses/window-03/meta.json: 2a4ec88eecb6f4225d9f855f7a403e080501ee46cdad4616f62d7894b0f4ea36
      B/clauses/window-04/raw.json: b6f78f206b767271cac3a57988c3a82fb9ddd3accf8276e50c2227faf54c614e
      B/clauses/window-04/prompt.txt: ccab4e5b9fa08e1acae40364483fcc283c13b42be70824e841a850b81e0fb945
      B/clauses/window-04/meta.json: 24af9aa24379418fca6c2f5e4d7585d710ea2d18627ada789cb81c49f0eed1a1
      B/clauses/window-05/raw.json: 3f15257a6717fd1e5b1d52a4e2d9f7b1ba5bd838e5b3d0084a5cb2507a075127
      B/clauses/window-05/prompt.txt: c88c639547fc8f7b3a770a445bfbd9293d1f14c62296584894da7f75a163276c
      B/clauses/window-05/meta.json: 620f51489391077e5171131562b4f4e5ac2b6ab00445179d56af6bc837528cd2
      B/clauses/window-02/raw.json: 5da95b63ff1d421c16c569505ba0f9fe7ad56c30b791bc5eaef4f6be080914c9
      B/clauses/window-02/prompt.txt: 252e282ec942d33f1e4aaa1b78e54efe213cd5ff86115eae89f8395195e3f54d
      B/clauses/window-02/meta.json: 8ef1084a00f987679c413b0d5a6b2a416333e2579af35f8e5535a65e20aa3bb0
      B/clauses/window-01/raw.json: 04ffa7a87fff0b3bcfc8884c9eb8cdb02ab2605dcde94f9c0f879f3c22b06467
      B/clauses/window-01/prompt.txt: f48cbfbeae32d3c32119e07098003da5f31271114cfa2ee8ff5f238b3278988c
      B/clauses/window-01/meta.json: bac9460f6f9943317bfae3bf179d200f2f71462af7a0aab6315538809b06c8b8
      B/clauses/window-06/raw.json: 099e5f88d5db098f6327eab04439e298de04a3c47f6c27398d0727b8016e8875
      B/clauses/window-06/prompt.txt: 27e6fb7864c0d62ce4c420adda6c6694cc1e46b89d889d1a8f23092f06e3698b
      B/clauses/window-06/meta.json: 1c92f7e32127e5dacf7fc23776d6743a6de04d22d9ea9858d2d17da15de77500
      B/tables/TABLE-1-page-2-1/raw.json: d30f88002a83cbec627f02b78a61f66436dbf6d1e3bcfc579b1c74449e6d1dd2
      B/tables/TABLE-1-page-2-1/prompt.txt: 3cc60833a295632344ab4aaeeccb1529728b8aaf1522666de9828eacb78c878d
      B/tables/TABLE-1-page-2-1/meta.json: f293d39a6ef2b610e1c17ed1e0d2c32a8bcb887bf98e6f92292ef49099e7b19f
      B/tables/TABLE-2-page-6-2/raw.json: 0ea1406c678228b5106fb28e791ee054da04802e8d424823b38f0dd03cb89051
      B/tables/TABLE-2-page-6-2/prompt.txt: f9460ab6c70914b7826a68abd2822aff0ec4a4f3b49f2fb88339b4f34f0bb601
      B/tables/TABLE-2-page-6-2/meta.json: 061d3996c153491548417bc338fbd5ccc560ccc305beae5c4c79e5ae0c216d01
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
    - P4-S2-C12
    qualifier_ids: []
    context_ids:
    - P2-S3-C14
    - P2-S3-C13
    table_ids: []
    exposure:
      text: DTI metrics of the left AF
      source_id: P4-S2-C12
    outcome:
      text: SLC scores
      source_id: P2-S3-C14
    relation: association
    effect_unit: individual
    result_status: reported_not_detected
    outcome_type: not_applicable
    direction: not_stated
    direction_source_id: ''
    origin: current_study
    label_match_candidates:
      outcome:
      - P3-S1-C3
      - P4-S2-C12
      - P4-S2-C8
      - P4-S2-C9
    id: U004
    flags:
    - nonverbatim_or_missing_label
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P2-S2-C8
    - P2-S2-C9
    - P2-S3-C10
    - P2-S3-C11
    - P2-S3-C2
    - P2-S3-C8
    - P2-S3-C9
    - P3-S1-C1
    - P3-S1-C10
    - P3-S1-C11
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C6
    - P3-S1-C7
    - P3-S1-C8
    - P3-S2-C13
    - P3-S2-C9
    - P3-S3-C12
    - P3-S3-C4
    - P4-S1-C4
    - P4-S1-C8
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S3-C7
    - P4-S3-C8
    - P8-S1-C11
    - P8-S1-C12
    - P8-S1-C13
    - P8-S1-C14
    - P8-S2-C4
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: 99d9c933021e4983cbec71c11e016a0b5602678dfbe48c20e6a50b2ba95190f6
  audit:
    coverage_issues:
    - Result passage disposed without unit P1-S2-C3
    - Result passage disposed without unit P1-S2-C4
    - Result passage disposed without unit P1-S2-C5
    - Result passage disposed without unit P1-S2-C6
    - Accounting without a linked unit P4-S1-C10
    - Accounting without a linked unit P4-S1-C11
    - Accounting without a linked unit P4-S2-C6
    - Accounting without a linked unit P4-S2-C8
    - Accounting without a linked unit P4-S2-C9
    - Unaccounted source passage P4-S1-C10
    - Unaccounted source passage P4-S1-C11
    - Unaccounted source passage P4-S2-C6
    - Unaccounted source passage P4-S2-C8
    - Unaccounted source passage P4-S2-C9
    - Result passage disposed without unit P4-S3-C3
    - Result passage disposed without unit P4-S3-C4
    - Result passage disposed without unit P4-S3-C5
    - Result passage disposed without unit P4-S3-C6
    - Result passage disposed without unit P4-S3-C7
    - Result passage disposed without unit P4-S3-C8
    - Result passage disposed without unit P5-S2-C2
    - Result passage disposed without unit P5-S2-C6
    - Result passage disposed without unit P5-S2-C8
    - Unresolved source passage P6-S2-C7
    - Result passage disposed without unit P7-S1-C6
    - Result passage disposed without unit P7-S2-C6
    - Result passage disposed without unit P7-S2-C7
    - Result passage disposed without unit P8-S2-C5
    - Result passage disposed without unit P8-S2-C6
    - Result passage disposed without unit P8-S2-C7
    unattached_null_or_qualifier_ids:
    - P4-S2-C6
    - P4-S2-C8
    - P7-S2-C7
    suppressed_nonrepresented_units: 20
    default_disposition_count_requires_completeness_check: 142
    unselected_timing_passages:
    - P1-S1-C9
    - P2-S3-C4
    - P2-S3-C6
    personal_effect_slots_without_result_classification: []
    held_frame_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    empty_frame_slots_require_confirmation:
    - validation
    - personal_factors
    - tested_personal_effects
    - explicitly_not_adjusted
    unclassified_extraction_ids: []
    table_review_required:
    - TABLE-1-page-2-1
    - TABLE-2-page-6-2
    unlinked_tables:
    - TABLE-1-page-2-1
    - TABLE-2-page-6-2
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P3-S2
      - P4-S1
      - P4-S2
      - P5-S1
      - P6-S1
      - P7-S1
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C2
      - P2-S3-C5
      recruited_sample:
      - P2-S3-C2
      - P2-S3-C5
      eligibility:
      - P2-S3-C2
      imaging_provenance:
      - P2-S2-C9
      - P3-S3-C4
      - P3-S3-C12
      imaging_timing:
      - P2-S3-C2
      outcome_timing:
      - P2-S3-C2
      outcome_definition:
      - P2-S3-C14
      - P3-S1-C1
      - P3-S1-C3
      validation: []
      analysis_restrictions:
      - P3-S2-C9
      - P3-S2-C13
      - P4-S1-C4
      - P4-S1-C8
      - P4-S2-C8
      - P4-S2-C11
      - P6-S1-C3
      - P7-S1-C2
      dependent_variable_statement:
      - P3-S2-C13
      limitations:
      - P8-S1-C11
      - P8-S1-C12
      - P8-S1-C13
      - P8-S1-C14
      - P8-S2-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C13
      - P4-S1-C8
      - P4-S2-C8
      - P4-S2-C11
      - P4-S3-C2
      - P6-S1-C3
      - P7-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C2
      - P2-S3-C2
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-18'
    approved: false
    pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
    model_material_before_agent_corrections:
      model_check:
        semantic_audit:
          verdict: accept
          checks:
            population: supported
            timing: supported
            anatomy: supported
            outcome: supported
            direction: supported
            statistics: supported
            adjustment: supported
            limitations: supported
            current_study: supported
            target_label: supported
            cohort_identity: supported
          issues: []
        semantic_audit_sha256: 641d6db5879c0a9b42f7c126bb6f1207fdc5b60696f4c060749fd2bf0644cca9
        binding:
          version: source-check-v8
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          pdf_sha256: 820ed5ec7c771ad0988c848ea6743d010885b6864be048780c48d1078c7717b5
          review_sha256: 09a4579a1a08e50ddf86bae14deeae8da17c4dca3772f601a416870aa964c92e
          code_sha256: dc05ea1b563a8f5d2afaa36ab53e178026c94e2a8595eef1353018f153744027
          converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
          schema_sha256: 09335e2c6adf91057d31449f9743b179f23448be337fedadaa33e9f99fb35500
          max_output_tokens: 6000
          host: http://localhost:11434
        prompt_sha256: 8e6060b8ecacc70bf092a1cc1555378746ddf6e2de8cf083b13e1f42a2e91569
        result_sha256: 2d174703a70e583e4200b557349fbf952170b47ced662ac255c5636da6ab2ab4
        result:
          decision: supported
          reason: The study reports that DTI metrics of the left arcuate fasciculus
            (AF) did not relate to sentence-level comprehension (SLC) scores when
            controlling for age, total lesion volume, and direct lesion load in the
            tract. The null result is supported by the lack of significance at the
            Bonferroni-corrected threshold (P < 0.0125), and the specific effect sizes
            (partial correlations) are provided in Table 2.
          checks:
            population: supported
            timing: supported
            anatomy: supported
            outcome: supported
            direction: supported
            statistics: supported
            adjustment: supported
            limitations: supported
            current_study: supported
          needs_visual_check: false
          bucket: regions
          entry:
            id: left_arcuate_fasciculus
            name: Left arcuate fasciculus
            kind: tract
            findings:
            - id: f1
              target: form_to_meaning
              target_kind: impairment
              claim: White matter integrity metrics (FA, MD, AD, RD) of the left arcuate
                fasciculus were not associated with sentence-level comprehension scores.
              direction: no_effect
              relationship: correlational
              method: DTI
              sample:
                n: 40
                population: chronic left hemisphere stroke survivors with aphasia
                phase: chronic
                time_post_onset: at least 6 months
                cohort: not_reported
              statistics:
                threshold: P < 0.0125
                effect_size: r = 0.074 (FA), -0.079 (MD), -0.088 (AD), -0.072 (RD)
              confounders_controlled:
              - age
              - total lesion volume
              - direct lesion load in the tract
              confounders_not_controlled: []
              region_definition:
                kind: tract
                description: Left arcuate fasciculus reconstructed using probabilistic
                  tractography in healthy older participants
              author_limitations:
              - lack of objective measures of individual tracts in patients due to
                varied lesions
              evidence_quality: cohort
              strength: moderate
              notes: The authors note that while direct lesion burden in the AF related
                to SLC, the specific DTI integrity metrics did not.
              outcome_timing:
                type: single_point
                interval: chronic
              imaging_details:
                reference_space: other
                reference_space_detail: Montreal Neurological Institute (MNI) space
                atlases_used: []
              lesion_mapping:
                analysis: univariate
                n_analysed: 40
                lesion_volume_correction: covariate
                multiple_comparisons: bonferroni
          passages:
          - page: 2
            quote: "MATERIALS AND METHODS\nParticipants\nForty (14 females) chronic\
              \ left hemisphere stroke survivors were \nrecruited in the study with\
              \ inclusion criteria as follows: native \nEnglish speaker; at least\
              \ 6 months post-stroke; able to follow test-\ning instructions; and\
              \ no history of other significant neurological \nillnesses."
            supports: sample
          - page: 2
            quote: "Using \nthese scores, we calculated word-level comprehension (WLC)\
              \ and \nsentence-level comprehension (SLC) composite scores to provide\
              \ \nrobust measurements of these two aspects of comprehension. \n"
            supports: method
          - page: 3
            quote: "To precisely localize relevant tracts, we \nreconstructed the\
              \ left inferior fronto-occipital fasciculus (IFOF), \ninferior longitudinal\
              \ fasciculus (ILF), and uncinate fasciculus \n(UF) tracts implicated\
              \ by the TBSS analysis (see Results) in 27 \nage-matched healthy subjects."
            supports: region_definition
          - page: 4
            quote: "Therefore, we further excluded the primary lesion load on each\
              \ \ntract from analyses by including the number of lesioned voxels \n\
              in the tracts as nuisance covariates in the analyses."
            supports: confounders
          - page: 4
            quote: "DTI metrics of the left AF did not relate \nto either WLC or SLC\
              \ scores (all uncorrected P > 0.10)."
            supports: claim
          - page: 4
            quote: "As previously \ndescribed (29), we considered tracts that showed\
              \ significant cor-\nrelations with behavior for the each DTI index at\
              \ a threshold of \nP < (0.05/4) = 0.0125 (Bonferroni correction)."
            supports: statistics
          - page: 6
            quote: "Tract\nTract size (mm3)\nComposite WLC\nComposite SLC\nLesion\n\
              FA\nMD\nAD\nRD\nLesion\nFA\nMD\nAD\nRD\nIFOF\n8,506\n−0.214\n0.410*\n\
              −0.447*\n−0.489*\n−0.432*\n0.118\n0.409*\n−0.413*\n−0.408*\n−0.413*\n\
              ILF\n5,451\n−0.022\n0.248\n−0.378\n−0.380\n−0.369\n−0.406*\n0.382\n\
              −0.461*\n−0.457*\n−0.453*\nUF\n3,097\n−0.400*\n0.408*\n−0.429*\n−0.424*\n\
              −0.439*\n−0.046\n−0.010\n−0.216\n−0.232\n−0.221\nAF\n3,447\n−0.081\n\
              −0.127\n0.129\n0.110\n0.138\n−0.439*\n0.074\n−0.079\n−0.088\n−0.072\n\
              IFOF, inferior fronto-occipital fasciculus; ILF, inferior longitudinal\
              \ fasciculus; UF, uncinate fasciculus; AF, arcuate fasciculus; FA, fractional\
              \ anisotropy; MD, mean diffusivity; AD, axial \ndiffusivity; RD, radial\
              \ diffusivity; WLC, word-level comprehension; SLC, sentence-level comprehension."
            supports: statistics
          - page: 3
            quote: "Structural T1 images \nwere registered to a Montreal Neurological\
              \ Institute (MNI) brain \ntemplate in standard space using the unified\
              \ segmentation tools \nimplemented in Statistical Parametric Mapping\
              \ software (SPM8)1 \nrunning under Matlab R2014a (20)."
            supports: imaging_details
          - page: 8
            quote: "First, lack of objective \nmeasures of the individual tracts in\
              \ patients is a main caveat of \nthis study."
            supports: limitation
      scope: Original model mapping before agent corrections
    checked_pdf_pages:
    - 2
    - 3
    - 4
    - 6
    - 7
    - 8
    visual_pages:
    - 4
    - 6
    scope: Follow-up of AF diffusion-metric null result against the main paper and
      visual Table 2. Original model evidence is retained; corrections were not automatically
      accepted by a model.
    corrections:
    - Keep the measured word/sentence outcome explicit and separate.
    - Separate AF diffusion-metric null from AF lesion-burden association.
    - Use template sampling rather than patient-specific tractography; preserve study
      limitations and outcome timing.
    remaining:
    - Named-person approval.
    - Paper-level completeness; additional relationships remain unmapped.
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: "Forty (14 females) chronic left hemisphere stroke survivors were \nrecruited\
    \ in the study with inclusion criteria as follows: native \nEnglish speaker; at\
    \ least 6 months post-stroke; able to follow test-\ning instructions; and no history\
    \ of other significant neurological \nillnesses. Demographics and language scores\
    \ for the group are \nlisted in Table 1. All patients had aphasia at the time\
    \ of stroke \nbased on medical records and received speech–language therapy.\n\
    Probabilistic tract reconstruction was performed in 27 healthy \nolder participants\
    \ (16 female) without neurological and psychiat-\nric disorder. The mean age was\
    \ 59.8 (±14.3) years; mean educa-\ntion was 16.3 (±2.6) years. Among them, 24\
    \ were right-handed, \n2 left-handed, and 1 ambidextrous.\n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-18'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
