---
id: rsfmri_fc_predictor
name: rsFMRI-FC predictor
kind: predictor
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: wab_r_aq
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Western Aphasia Battery–Revised
    metric: Aphasia Quotient
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: overall_aphasia_severity
  target_kind: impairment
  claim: In the SVR model, rsFMRI-FC emerges as a crucial feature that significantly
    contributes to model performance, possessing the highest SHAP value and positively
    influencing the model's predictions by enhancing accuracy.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 76
    population: individuals with post-stroke aphasia due to a single left-hemisphere
      stroke
    phase: not_reported
    time_post_onset: chronic
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - models struggle to predict outcomes for severe aphasia patients with WAB-R AQ
    scores lower than 20
  - small sample size of multimodal imaging data
  - gender imbalance with more male than female participants
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Resting-state functional connectivity (rsFMRI-FC)
    measured as Fisher-transformed bivariate correlation coefficients of BOLD signal
    time series between 50 pre-selected ROIs of the AAL3 atlas, reduced to 625 values
    by excluding non-homologous interhemispheric connections. measured using SHAP
    values to determine contribution to prediction accuracy (RMSE); highest contribution
    observed in SVR model; performance is further optimized when combined with structural
    integrity information (PSW or PSG). Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S3-C9, two-model
    agreement, human verification pending): . A total of 76 individuals from two cohorts
    with left hemisphere stroke were included in the study (See Table 1 for overview
    of demographic information of two cohorts) Original text-layer quotation is preserved
    below. PDF image reading (P4-S2-C11, two-model agreement, human verification pending):
    . All participants met the following inclusion

    criteria: chronic aphasia due to a single left-hemisphere stroke, mono-

    lingual English-speaking, medically and neurologically stable, normal

    or corrected-to-normal hearing and vision, at least a high school

    education, between the ages of 35 and 80, and at least one year post-

    stroke Original text-layer quotation is preserved below.'
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
    - proposed_concept:wab_r_aq
  citation: '@Hu2025'
  source_passages:
  - section: Original source P9-S1-C15
    page: 9
    quote: "Resting-state functional connectivity\nNotably, in both the RF and SVR\
      \ models, the predictor rsFMRI-\nFC emerges as a crucial feature, significantly\
      \ contributing to model \nperformance."
    supports: claim
  - section: Original source P9-S1-C18
    page: 9
    quote: "In the SVR model, rsFMRI-FC has the highest SHAP value \nof 3.65, indicating\
      \ that it positively influences the model’s predictions, \nenhancing accuracy."
    supports: claim
  - section: Original source P11-S1-C3
    page: 11
    quote: "Furthermore, rsFMRI-FC has high positive SHAP values in both \nmodel types\
      \ (Supplementary Table S3 and Figure S2), indicating that \nit makes a significant\
      \ positive contribution to the model’s predic-\ntions when combined with other\
      \ predictors."
    supports: claim
  - section: Original source P5-S2-C2
    page: 5
    quote: "Then, ROI-to-ROI connectivity strength was represented by Fisher-\ntransformed\
      \ bivariate correlation coefficients of ROIs’ BOLD signal time \nseries."
    supports: method
  - section: Original source P5-S2-C3
    page: 5
    quote: "These matrices were reduced to 625 values (rsFMRI-FC) by \nexcluding non-homologous\
      \ interhemispheric connections (Billot et al., \n2022)."
    supports: method
  - section: Original source P2-S3-C9
    page: 2
    quote: "A to-\ntal of 76 individuals from two cohorts with left hemisphere stroke\
      \ \nwere included in the study (See Table 1 for overview of demographic \ninformation\
      \ of two cohorts)."
    supports: sample
  - section: Original source P4-S2-C11
    page: 4
    quote: "All participants met the following inclusion \ncriteria: chronic aphasia\
      \ due to a single left-hemisphere stroke, mono-\nlingual English-speaking, medically\
      \ and neurologically stable, normal \nor corrected-to-normal hearing and vision,\
      \ at least a high school \neducation, between the ages of 35 and 80, and at\
      \ least one year post-\nstroke."
    supports: sample
  - section: Original source P9-S1-C21
    page: 9
    quote: "Severe case limitations\nFinally, neither SVR nor RF models are able to\
      \ predict a small subset \nof patients with WAB-R AQ scores lower than 20 (\U0001D441\
      = 3) (Fig. 10 \nand Supplementary Figure S6)."
    supports: limitation
  - section: Original source P11-S1-C9
    page: 11
    quote: "Limitations and future research\nOur research faces limitations due to\
      \ the small sample size of mul-\ntimodal imaging data, despite adequately representing\
      \ aphasia patient \nheterogeneity, and the greater number of male compared to\
      \ female \nparticipants, which could bias the results."
    supports: limitation
predictor_type: imaging_metric
short_definition: Resting-state functional connectivity (rsFMRI-FC) measured as Fisher-transformed
  bivariate correlation coefficients of BOLD signal time series between 50 pre-selected
  ROIs of the AAL3 atlas, reduced to 625 values by excluding non-homologous interhemispheric
  connections.
assessment:
- Western Aphasia Battery-Revised Aphasia Quotient (WAB-R AQ)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hu2025
  proposal_id: R013
  review_status_sha256: c815e756ccac04822ff2bea80320927636c66e31a6bbf00aaf48f820f4415024
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
        A/passages.json: 976bd21ae75c2d7eb3f5b324e6e0bb74b417ec94be3fbc20815db5d0a88b3966
        A/raw.json: f3d5c7cb6d964472b2cd44f6725185f0162378d89d39d141f0987fa0efc2f2d9
        A/source-units.json: a971455d526781a3d2d933233c97a30cc33974d25d7ff475c3f7fdd28a6891ad
        A/full-source-units.json: 97c982479aadf5de9b2fb62f2d4c7116404fabcf5ed0e54d141b77cb2d77209d
        A/meta.json: 609ad611fef6a64a70d3246ab0604ad7a67b4c89b0af4c5aeb021fa21a3ccfa4
        A/table-images/TABLE-3-page-9-1.png: 205bc7f0d5eda0402c7643210acd7b0120e18b68d73a46b34d82260d909b090f
        A/table-images/TABLE-2-page-8-1.png: b7363939ad64658da6c1864bf788f59879b8fe1c7e1c0b015285221c155d8900
        A/table-images/TABLE-1-page-2-1.png: 740cb6f2d2b6759d72cce7361bbc3b5ee0398b4a398a93688e53a820bd866103
        A/table-images/page-2.png: 97d50987560f70cd26eb7391eb5c29954da03717025f3823793c4e4be62accae
        A/table-images/page-9.png: 171507d60a2f4b740be484a6e4a9bbadd5ae88d0923c38f93b46deba1b2204fb
        A/table-images/page-8.png: 7b449209795e08c7d2167a0de8d5e4431916c54cc15f390d2f14558f692ba639
        A/table-images/manifest.json: aceb6b3b310f56e412fafdffe7e6cb480d3a57138bfe4c7dd8589e0de223fc7d
        A/clauses/window-11/raw.json: 144fa7e0ff5ff5ceec9b1b9ac617c788bafe974a02a437f1fe31903e0c44a7b9
        A/clauses/window-11/prompt.txt: 7cb00a9ddced202f9d03db0afaa7c5b61f7f5cee447f84aeff2ac0fbee797ba0
        A/clauses/window-11/meta.json: 73aed4095efe5c5eb6717ec71d2306d9694acea06f1578229be53e7996b492f0
        A/clauses/window-10/raw.json: 4cd953384eed742bcdcf7078a35d12722038e9d180324777def2d5227d06a84b
        A/clauses/window-10/prompt.txt: 6eb06e2bf254e7fc963c4b6da37f2f762ce0ce3a1bba705698e2e977101ea588
        A/clauses/window-10/meta.json: f634e60c178be6e491c7c697fe8d3c046814453186455f9801d4c73fb3185f69
        A/clauses/window-03/raw.json: 4f65a83ba15151c0ae55b5aea39f147c4d5289f0437e51c4941b47247a7741ed
        A/clauses/window-03/prompt.txt: 33ae03a3d1f8df4eae6d7873e8eeed39a1bb9d0b51d4ef90ff8c544ade6ec284
        A/clauses/window-03/meta.json: 69f3aef4d5e259852fd932080bb62857712e4f0d2d0ba08c14e60f18e17c6750
        A/clauses/window-04/raw.json: edf94b68448b9477c2ff60e8099cb4329d495096a590fda1eab51946f73b43bc
        A/clauses/window-04/prompt.txt: 6e753be4b3c845a007b032e0be157d64d362623f03864bca90611036486fa1e7
        A/clauses/window-04/meta.json: 742fa5da02dbfbdb259cf4a0756d085700573b0a2220e8127f1e4cacf4aae4f4
        A/clauses/window-05/raw.json: 150256992afa00e5024e96fce3325fe060987535de603b27ddea520b5c2f23db
        A/clauses/window-05/prompt.txt: ca86e0c7d516a0368ca7f25abbef27b1ef99683ffd47b16d46be280d8b8e80f9
        A/clauses/window-05/meta.json: 74f3e333c5b8575643f6a713d45a65a77a460e3a6c5b24f6147100c38640f44a
        A/clauses/window-02/raw.json: 8e78d2274358e0e4429e861fe70679da26dd85e9c4531bbe6afa66c2d5a89ffe
        A/clauses/window-02/prompt.txt: 3f0f0b42f879c494e4991c08f748101736a3da3316c8f7f8bde36616be1cbd44
        A/clauses/window-02/meta.json: a595d13283eb57c1f070afb4ec2e6daab70ca4b571a0da76f053a7bee99c4de4
        A/clauses/window-12/raw.json: 422a610690528775ceadfa9cd80591384ac9dd697af29a0e6653895f15792317
        A/clauses/window-12/prompt.txt: eebc05989a29228a556f18c30afec9547c9df82ec841a925a20aa2fce423d204
        A/clauses/window-12/meta.json: c5d3be455363e800571666a887a02a022d8277adebf24a5a2b35bbcf4cf3930f
        A/clauses/window-13/raw.json: 7ef1117ff2f233f1fc14aed16bd488da1901cb4fa17a62418e784d7b23ac4837
        A/clauses/window-13/prompt.txt: 887ce5e3ab5dc2ae566bffa52d80145c92f746d6d707eeda05471f72bb987195
        A/clauses/window-13/meta.json: a56e3d8d8e8e4a3d97d1048183d6ddbfb4b101e51ce61e36195142a2feed90d9
        A/clauses/window-09/raw.json: 236e7deed2df1c0b987deab3ef05a7425953b463adbf8e5d627b04fad9f28b9b
        A/clauses/window-09/prompt.txt: ab8ea766f1aceb8339ecab5dd0c87bd0a09f49a59e0af4d76720d00b1d502235
        A/clauses/window-09/meta.json: f4dbd75a4114a60a61b84f87faa25251d5d9902381d701b6c5bff3aa7718f2d8
        A/clauses/window-07/raw.json: 438c3cbc59c703bb561f1433ab84f22fbb429ceda0db4bad23e1c9c1ff1c3102
        A/clauses/window-07/prompt.txt: e672e8ce866dd14648f469c03a3da05eb0ed706797d86c8c4f62987001a628c5
        A/clauses/window-07/meta.json: e0c8e33f5d791f0784d947d9b14b962297186beec465ae5417065eb86938bbb6
        A/clauses/window-01/raw.json: f4a01e84cb6e6971d1c35c116505df46d7794f410728536c5b61a93686becd90
        A/clauses/window-01/prompt.txt: f2f748d27b0bfd5eb11b44064510a13ea58d045fa4a53bccf8894a41d2236aef
        A/clauses/window-01/meta.json: a5db6403eb502822ccd8eebec6bfa48d2d785a78dfcaeddbb22a8d2c8122e554
        A/clauses/window-06/raw.json: fc9e7b9d424ad8737575ef53cb95e84fb0e1e78c089c4a7e71bd12566f406047
        A/clauses/window-06/prompt.txt: a66e22f9fae025199e46e00ea78b4b56dbedf88f6a2dfc8f0f9f03a74b6ff636
        A/clauses/window-06/meta.json: e5b3fff6d57208ab68156648b7727db8d528fd0151102d02efcd8b21d5a84676
        A/clauses/window-08/raw.json: d18dd54a5c932e98fe961c17b747311dfbef83582a0a13c03efa58ad66745c59
        A/clauses/window-08/prompt.txt: f3f67daeeb9f1964957d3048f4335e3ad678972e24bb262e3c89c785deeb77b0
        A/clauses/window-08/meta.json: d7ce407e171a9afde5b7eca1a67fef524187358c9f530a483bf67950be4be923
        A/tables/TABLE-1-page-2-1/raw.json: 67814ccf95d8a52d7c50ec1df9275f96ce6206f011f653508afa3b838989374b
        A/tables/TABLE-1-page-2-1/prompt.txt: 0201a55efb7268793262d66b39504d826cc38791416f5f160c2869126d43eec9
        A/tables/TABLE-1-page-2-1/meta.json: 39a23d970450826b828c25131198bc6998e582a591895bfa81e6b44e37969679
        A/tables/TABLE-2-page-8-2/raw.json: 3d2dffa0e8fad6c9e7534019fac6ae486b6dc4e93f01452e94280e0c9f22694b
        A/tables/TABLE-2-page-8-2/prompt.txt: 2e286597f6c4a415a74475f7135210434b37ca8e71a1ef6bf5d023be88c3c28f
        A/tables/TABLE-2-page-8-2/meta.json: 878b4d4ed25e11e15d3cf2a360753df7a9da0fcfbf964e64c568c7fa9ca30ec5
        A/tables/TABLE-3-page-9-3/raw.json: 0cd012808d553d3ea551bf855399f47034fa7f7073816b75bd48725a60f16ebf
        A/tables/TABLE-3-page-9-3/prompt.txt: db1c8645b8fa3b6ea630fffeb1a174034472a7e5a14372819970f997c4e34336
        A/tables/TABLE-3-page-9-3/meta.json: ffd43c1939c5ac780c638799cded8436291655d5029cb711c71ddb99bb43826c
        B/passages.json: 976bd21ae75c2d7eb3f5b324e6e0bb74b417ec94be3fbc20815db5d0a88b3966
        B/raw.json: a6bc36d76e9f4210460d1dc7181bc8fd20673a62226c89c9f4a5ee9cce6cce5b
        B/source-units.json: a971455d526781a3d2d933233c97a30cc33974d25d7ff475c3f7fdd28a6891ad
        B/full-source-units.json: 97c982479aadf5de9b2fb62f2d4c7116404fabcf5ed0e54d141b77cb2d77209d
        B/meta.json: 01447fb053210efdfe0c9c5ec3af13d4fea7b4c7e5df2c404596c20e15f2ecba
        B/table-images/TABLE-3-page-9-1.png: 205bc7f0d5eda0402c7643210acd7b0120e18b68d73a46b34d82260d909b090f
        B/table-images/TABLE-2-page-8-1.png: b7363939ad64658da6c1864bf788f59879b8fe1c7e1c0b015285221c155d8900
        B/table-images/TABLE-1-page-2-1.png: 740cb6f2d2b6759d72cce7361bbc3b5ee0398b4a398a93688e53a820bd866103
        B/table-images/page-2.png: 97d50987560f70cd26eb7391eb5c29954da03717025f3823793c4e4be62accae
        B/table-images/page-9.png: 171507d60a2f4b740be484a6e4a9bbadd5ae88d0923c38f93b46deba1b2204fb
        B/table-images/page-8.png: 7b449209795e08c7d2167a0de8d5e4431916c54cc15f390d2f14558f692ba639
        B/table-images/manifest.json: 80b98d803e5d27f98ff013349ee859a3763ff30f209e4e49bfcfbc7ff288c94b
        B/clauses/window-11/raw.json: 48d93fbc8a04e92d33546d9802748fd601a84cbbde9e288fe4e8b1f13fe7afbc
        B/clauses/window-11/prompt.txt: 7cb00a9ddced202f9d03db0afaa7c5b61f7f5cee447f84aeff2ac0fbee797ba0
        B/clauses/window-11/meta.json: 579b38478748371841e3742e5f6247e1e34619aa45925c5b5aa785bc677491dc
        B/clauses/window-10/raw.json: 29c83a2818566fe87dc90bdbb94164be3aa503ac0e3e09268f2e437833a0077b
        B/clauses/window-10/prompt.txt: 6eb06e2bf254e7fc963c4b6da37f2f762ce0ce3a1bba705698e2e977101ea588
        B/clauses/window-10/meta.json: 7416dcd9b7a844bb62d8114fd8ace21d46fd865937586928121c392d27cf2367
        B/clauses/window-03/raw.json: 8fa289bdb598edc18308561efde4b07bd5563710e97b2b44dafc15772789ba76
        B/clauses/window-03/prompt.txt: 33ae03a3d1f8df4eae6d7873e8eeed39a1bb9d0b51d4ef90ff8c544ade6ec284
        B/clauses/window-03/meta.json: 4aa07bf2d177711089d9532a3f92b19b3aae723380d69617dfafd5fe0f157991
        B/clauses/window-04/raw.json: 50cdc5b0c365ec37d7c21e3c0103274692c80f5eb4bd433b401ad4fa24be76d6
        B/clauses/window-04/prompt.txt: 6e753be4b3c845a007b032e0be157d64d362623f03864bca90611036486fa1e7
        B/clauses/window-04/meta.json: 8c5e529ba3a58982263bac5062d1f54abfc599ef2add926989d7443dbc0768c6
        B/clauses/window-05/raw.json: 76d37ac664848fd6f2734796ec7651976fab574e88af93d65f14907dd412f857
        B/clauses/window-05/prompt.txt: ca86e0c7d516a0368ca7f25abbef27b1ef99683ffd47b16d46be280d8b8e80f9
        B/clauses/window-05/meta.json: 50b9ca5999a3df4c37356b932cf672a1e40f9151aa798a21f6c9101f2bd39314
        B/clauses/window-02/raw.json: 8fefabad59cabf513414ddeae5d45f1843af67a36b800a5d35e4dac9ce4423d2
        B/clauses/window-02/prompt.txt: 3f0f0b42f879c494e4991c08f748101736a3da3316c8f7f8bde36616be1cbd44
        B/clauses/window-02/meta.json: 58bcf2aa94169183909f9e41f32d3b92835e2654a4eda91e0b7850fe8aff7865
        B/clauses/window-12/raw.json: 59af86e99b89b3d4861329faf7cae7596f7ae8ba6133665da21ae5c902e89b83
        B/clauses/window-12/prompt.txt: eebc05989a29228a556f18c30afec9547c9df82ec841a925a20aa2fce423d204
        B/clauses/window-12/meta.json: d0ffed3ad8ec6916d321f93691ec6c604d2a44b9db27392f847bbdb11c1a8a95
        B/clauses/window-13/raw.json: 7ef1117ff2f233f1fc14aed16bd488da1901cb4fa17a62418e784d7b23ac4837
        B/clauses/window-13/prompt.txt: 887ce5e3ab5dc2ae566bffa52d80145c92f746d6d707eeda05471f72bb987195
        B/clauses/window-13/meta.json: 051bd91bdc91b35470bd386ea941e7b475d9c10861de16bc489cf78fd42a4934
        B/clauses/window-09/raw.json: 90f34cc23e5a874bfd2e9b4f2173f592dae8b2dd1806da0dd91ce2f1d8de98fd
        B/clauses/window-09/prompt.txt: ab8ea766f1aceb8339ecab5dd0c87bd0a09f49a59e0af4d76720d00b1d502235
        B/clauses/window-09/meta.json: 959604d39ad37ecf5d44d8ebde16d1e33300814da62a366a8d7935a0f4249965
        B/clauses/window-07/raw.json: d6b70e202b698894727bc23430fad9b91377669357d36c7fa59e17b8c17bf711
        B/clauses/window-07/prompt.txt: e672e8ce866dd14648f469c03a3da05eb0ed706797d86c8c4f62987001a628c5
        B/clauses/window-07/meta.json: 82e155c90f865b34193eee0be57b75a657e9482af31e9af6d7002fffb3f025f8
        B/clauses/window-01/raw.json: 77cb144d6e53d7991893ed30cd0533c2f5e362552a3ba03b7618e1de687ebae0
        B/clauses/window-01/prompt.txt: f2f748d27b0bfd5eb11b44064510a13ea58d045fa4a53bccf8894a41d2236aef
        B/clauses/window-01/meta.json: 7be31f5eabf2f3a4e7b6097ddfb753a48e258db98c502de73ad6d2503df59744
        B/clauses/window-06/raw.json: 8501b89bf1d1ff01ddcefd0a9b3cab5f49c2519d94f78ff3e4959dac6ab4c7c6
        B/clauses/window-06/prompt.txt: a66e22f9fae025199e46e00ea78b4b56dbedf88f6a2dfc8f0f9f03a74b6ff636
        B/clauses/window-06/meta.json: 472d39322dcc070e3cbaec713c5527e832e222e402cbc492ccd22ae5b6e9898c
        B/clauses/window-08/raw.json: cc275b92c602ab0fb23d53823e0b9cdce356dec550cec0571eb99aab1abb4a2e
        B/clauses/window-08/prompt.txt: f3f67daeeb9f1964957d3048f4335e3ad678972e24bb262e3c89c785deeb77b0
        B/clauses/window-08/meta.json: 13c456618cabe1295da4d3425373678136bfc4938df3a38f1ed5906d8cfddff9
        B/tables/TABLE-1-page-2-1/raw.json: 84f457a101602b647db8b33e5a3aa90610a0f7fb88470f767688cd6474fb35db
        B/tables/TABLE-1-page-2-1/prompt.txt: 0201a55efb7268793262d66b39504d826cc38791416f5f160c2869126d43eec9
        B/tables/TABLE-1-page-2-1/meta.json: cac672e0e422c39958714ca7c0ff12a4e0399a8c9f09e0d39ccce413698c0127
        B/tables/TABLE-2-page-8-2/raw.json: d050ebab3020c6e215a2cb5270ef7c973f05608b99194e47371beafad047dcb8
        B/tables/TABLE-2-page-8-2/prompt.txt: 2e286597f6c4a415a74475f7135210434b37ca8e71a1ef6bf5d023be88c3c28f
        B/tables/TABLE-2-page-8-2/meta.json: 2e6028396e797b346beecb8157b0ca7daf8e42fa6a3a87bf767d8db593fef649
        B/tables/TABLE-3-page-9-3/raw.json: 91e26c7938ae445a4f115246fef579a317e5a5127fbefba00206e81e3f3cf44a
        B/tables/TABLE-3-page-9-3/prompt.txt: db1c8645b8fa3b6ea630fffeb1a174034472a7e5a14372819970f997c4e34336
        B/tables/TABLE-3-page-9-3/meta.json: aa95ed4ffe440e96290f21bf13a37c49d5d7bece5a2b83450588389d414e1c6b
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
      pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
      source_review: _compare/relationships-2026-11-16/review-current/Hu2025
      source_status_sha256: d75917610cfce1e5b058c3b55b91cda05dbe20c85b56871c20b76b1803f9cfb9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: rsFMRI-FC
    outcome:
      text: WAB-R AQ
    analysis_label: SVR predictor contribution (SHAP)
    relation: association
    evidence_ids:
    - P9-S1-C18
    - P11-S1-C3
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
      pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
      source_review: _compare/relationships-2026-11-16/review-current/Hu2025
      source_status_sha256: d75917610cfce1e5b058c3b55b91cda05dbe20c85b56871c20b76b1803f9cfb9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C1
      - Accounting without a linked unit P2-S1-C7
      - Accounting without a linked unit P2-S2-C2
      - Unaccounted source passage P2-S1-C7
      - Unaccounted source passage P2-S2-C2
      - Result passage disposed without unit P2-S3-C11
      - Result passage disposed without unit P2-S4-C1
      - Unresolved source passage P5-S3-C7
      - Unresolved source passage P6-S1-C12
      - Result passage disposed without unit P8-S1-C10
      - 'window 10: invalid/duplicate disposition P10-S1-C11'
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S3-C4
      - Accounting without a linked unit P11-S1-C11
      - Result passage disposed without unit P11-S1-C2
      - Accounting without a linked unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C4
      - Unaccounted source passage P11-S1-C11
      - Unaccounted source passage P11-S1-C3
      - Result passage disposed without unit P11-S2-C10
      - Result passage disposed without unit P11-S2-C13
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P11-S3-C4
      - Result passage disposed without unit P11-S3-C5
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 302
      unselected_timing_passages:
      - P1-S1-C1
      - P2-S4-C12
      - P2-S4-C13
      - P4-S2-C9
      - P4-S2-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P1-S1-C1
        - P2-S1-C4
        - P2-S1-C5
        - P2-S1-C9
        - P2-S1-C11
        - P2-S1-C12
        - P2-S2-C2
        - P2-S3-C5
        - P3-S1-C13
        - P6-S1-C8
        - P10-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P9-S2-C2
        - P9-S2-C3
        - P11-S1-C9
        - P11-S1-C11
        - P11-S1-C12
        - P11-S2-C3
        - P11-S2-C4
        - P11-S2-C5
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S2-C10
        - P11-S2-C11
        - P11-S2-C12
        - P11-S2-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - limitations
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P3-S1-C20
      - P3-S1-C21
      - P3-S1-C22
      - P3-S1-C23
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-8-2
      - TABLE-3-page-9-3
      unlinked_tables:
      - TABLE-1-page-2-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P8-S2
        - P9-S1
        - P9-S2
        - P9-S3
        - P10-S1
        - P10-S2
        - P10-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
      source_review: _compare/relationships-2026-11-16/review-current/Hu2025
      source_status_sha256: d75917610cfce1e5b058c3b55b91cda05dbe20c85b56871c20b76b1803f9cfb9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: States SVR outperformed RF.
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about predictor combinations without specific performance
        metrics.
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about functional connectivity being critical.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about factors beyond lesion location.
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay figure.
    - source_id: P2-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Listing of frequently lesioned ROIs.
    - source_id: P2-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion distribution.
    - source_id: P4-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of FA values between cohorts (supplementary reference).
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of squared error distribution figure.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: SVR significantly lower RMSE than RF.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary RF results.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 5
      reason: No significant difference between linear and RBF for individual predictors.
    - source_id: P6-S3-C6
      disposition: represented
      result_indexes:
      - 5
      reason: RBF kernel lower RMSE for combined rsFMRI-FC and PSW/PSG.
    - source_id: P6-S3-C8
      disposition: represented
      result_indexes:
      - 1
      reason: rsFMRI-FC alone has lowest RMSE among single predictor SVR.
    - source_id: P6-S3-C9
      disposition: represented
      result_indexes:
      - 2
      reason: PSG and PSW show next lowest RMSE.
    - source_id: P6-S3-C10
      disposition: represented
      result_indexes:
      - 3
      reason: rsFMRI-FC and PSG models not statistically different.
    - source_id: P6-S3-C11
      disposition: represented
      result_indexes:
      - 4
      reason: DM and rsFMRI-trans are not informative single predictors.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of figure 4(A).
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: RBF kernel achieved lower RMSE for combined rsFMRI-FC with PSW/PSG.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement that full-predictor model was not the best.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Lowest RMSE model incorporated DM, PSW, and rsFMRI-FC.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 7
      reason: Top 10 models included rsFMRI-FC and structural integrity (PSW or PSG).
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Importance of rsFMRI-FC and structural integrity predictors.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Optimal multimodal SVR significantly outperformed single-modality model.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Within-hemisphere and between-homologous-language-region connections
        frequently selected.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Selected PSG features located in left hemisphere language area.
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Top 2 PSW features are Fronto Insular tracts and Arcuate Posterior Segment
        Left.
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 11
      reason: 'Selected FA features: Left arcuate fasciculus, Left uncinate fasciculus,
        Left inferior Fronto-Occipital fasciculus, and Left inferior longitudinal
        fasciculus.'
    - source_id: P8-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of figure 8.
    - source_id: P9-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about rsFMRI-FC as a crucial feature.
    - source_id: P9-S1-C18
      disposition: represented
      result_indexes:
      - 12
      reason: rsFMRI-FC has highest SHAP value of 3.65.
    - source_id: P9-S1-C20
      disposition: represented
      result_indexes:
      - 7
      reason: rsFMRI-FC combined with structural information attains lowest RMSE.
    - source_id: P9-S1-C21
      disposition: represented
      result_indexes:
      - 13
      reason: Models unable to predict patients with WAB-R AQ < 20.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: SVR consistently outperforms RF.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: RBF kernel achieved lower RMSE than linear for combined rsFMRI-FC with
        PSW/PSG.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about RFE identifying important features.
    - source_id: P10-S1-C13
      disposition: represented
      result_indexes:
      - 8
      reason: Functional activation in language network (both hemispheres and homologous
        regions) provided important information.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: PSG features in left hemisphere language area are informative.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Spared white matter tracts in left hemisphere (arcuate fasciculus and
        fronto-insular) frequently selected.
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement that findings are replicated with RF models.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 12
      reason: rsFMRI-FC has high positive SHAP values in both model types.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Integrated features combining structural and functional integrity yield
        lowest RMSE.
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 13
      reason: Models struggle to predict outcomes for severe aphasia patients.
    - source_id: P11-S3-C4
      disposition: represented
      result_indexes:
      - 0
      reason: SVR models better than RF models.
    - source_id: P11-S3-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Functional connectivity in both hemispheres and between homologous language
        areas is critical.
    unresolved_coverage:
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C5
    - P1-S2-C2
    - P2-S3-C10
    - P2-S3-C11
    - P2-S4-C1
    - P4-S4-C7
    - P6-S2-C6
    - P6-S3-C4
    - P7-S1-C5
    - P8-S1-C10
    - P8-S2-C1
    - P8-S2-C14
    - P9-S1-C15
    - P9-S1-C20
    - P9-S2-C5
    - P9-S2-C7
    - P9-S3-C4
    - P10-S1-C11
    - P10-S3-C3
    - P10-S3-C4
    - P11-S1-C2
    - P11-S2-C3
    - P11-S2-C10
    - P11-S2-C13
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-8-2
    - TABLE-3-page-9-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C9
      recruited_sample:
      - P2-S4-C9
      - P2-S4-C12
      - P2-S4-C13
      eligibility:
      - P3-S1-C19
      - P4-S2-C11
      - P4-S2-C12
      imaging_provenance:
      - P5-S1-C6
      imaging_timing:
      - P2-S2-C3
      - P2-S2-C4
      outcome_timing:
      - P2-S2-C3
      - P2-S2-C4
      outcome_definition: []
      validation:
      - P5-S2-C12
      - P6-S1-C5
      - P6-S1-C7
      - P6-S1-C8
      analysis_restrictions:
      - P5-S3-C14
      - P5-S3-C15
      - P5-S4-C9
      dependent_variable_statement:
      - P1-S1-C1
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C9
      limitations: []
      personal_factors:
      - P2-S3-C5
      - P5-S2-C9
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C5
      - P5-S2-C9
    outcome_type: status_at_assessment
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P1-S1-C1
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C9
      - P2-S1-C11
      - P2-S1-C12
      - P2-S2-C2
      - P2-S3-C5
      - P3-S1-C13
      - P6-S1-C8
      - P10-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P9-S2-C2
      - P9-S2-C3
      - P11-S1-C9
      - P11-S1-C11
      - P11-S1-C12
      - P11-S2-C3
      - P11-S2-C4
      - P11-S2-C5
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S2-C10
      - P11-S2-C11
      - P11-S2-C12
      - P11-S2-C13
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
      pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
      review_sha256: c815e756ccac04822ff2bea80320927636c66e31a6bbf00aaf48f820f4415024
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
      - P9-S1-C18
      - P11-S1-C3
      source_result: In the SVR model, rsFMRI-FC has the highest SHAP value (3.65),
        indicating a positive contribution to prediction accuracy (lower RMSE). This
        finding is replicated in RF models, where rsFMRI-FC also shows high positive
        SHAP values, confirming its significant positive contribution to predicting
        WAB-R AQ when combined with other predictors.
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the evaluation of rsFMRI-FC's
            contribution via SHAP values in the SVR model, matching the source description
            in P9-S1-C18 and P11-S1-C3.
          source_ids:
          - P9-S1-C18
          - P11-S1-C3
        direction:
          answer: fits
          reason: The source explicitly states that rsFMRI-FC has a 'highest SHAP
            value' and 'positively influences' predictions (P9-S1-C18), which aligns
            with the draft's claim of a significant positive contribution.
          source_ids:
          - P9-S1-C18
          - P11-S1-C3
        construct:
          answer: fits
          reason: The exposure (rsFMRI-FC) and outcome (WAB-R AQ) are correctly identified.
            The patient measurement is functional_imaging (rsFMRI), distinct from
            the diffusion-based structural predictors (PSW/FA) mentioned in the source.
          source_ids:
          - P5-S2-C2
          - P5-S2-C3
          - P9-S1-C18
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the performance
            is optimized when combined with structural information (PSW/PSG), as noted
            in P9-S1-C20 and P11-S1-C4. It also correctly notes the limitation regarding
            severe aphasia cases.
          source_ids:
          - P9-S1-C20
          - P11-S1-C4
          - P9-S1-C21
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitations regarding severe aphasia
            prediction failure and sample size/gender imbalance. No material caveats
            that change the interpretation of the rsFMRI-FC contribution are omitted.
          source_ids:
          - P9-S1-C21
          - P11-S1-C9
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
      id: R013
      exposure:
        text: rsFMRI-FC
      outcome:
        text: WAB-R AQ
      analysis_label: SVR predictor contribution (SHAP)
      relation: association
      evidence_ids:
      - P9-S1-C18
      - P11-S1-C3
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
        pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
        source_review: _compare/relationships-2026-11-16/review-current/Hu2025
        source_status_sha256: d75917610cfce1e5b058c3b55b91cda05dbe20c85b56871c20b76b1803f9cfb9
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9ba7a336d18296dfa839dd251eb89bd84fb42eac76dd201224fca96bdd465cf5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C9
          page: 2
          text_layer_sha256: 9ba7a336d18296dfa839dd251eb89bd84fb42eac76dd201224fca96bdd465cf5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A to-\ntal of 76 individuals from two cohorts with left hemisphere\
          \ stroke \nwere included in the study (See Table 1 for overview of demographic\
          \ \ninformation of two cohorts)."
        anchor_text: "A to-\ntal of 76 individuals from two cohorts with left hemisphere\
          \ stroke \nwere included in the study (See Table 1 for overview of demographic\
          \ \ninformation of two cohorts)."
        excluded_fragments: []
        image_sha256: ddc012a16564adb66c8c23a102b49dde19457a28ea5c710a19a46e9bcec79bb0
        transcription: . A total of 76 individuals from two cohorts with left hemisphere
          stroke were included in the study (See Table 1 for overview of demographic
          information of two cohorts)
      P4-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 237d8fd9b380acae7f678a660bb782e37e67d7599674c1b5e675b5a061f473f9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 31858778fa5da8808fce6766c7a62d388e97ad959342689ae1c8a84565bcacea
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C11
          page: 4
          text_layer_sha256: 31858778fa5da8808fce6766c7a62d388e97ad959342689ae1c8a84565bcacea
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All participants met the following inclusion \ncriteria: chronic\
          \ aphasia due to a single left-hemisphere stroke, mono-\nlingual English-speaking,\
          \ medically and neurologically stable, normal \nor corrected-to-normal hearing\
          \ and vision, at least a high school \neducation, between the ages of 35\
          \ and 80, and at least one year post-\nstroke."
        anchor_text: "All participants met the following inclusion \ncriteria: chronic\
          \ aphasia due to a single left-hemisphere stroke, mono-\nlingual English-speaking,\
          \ medically and neurologically stable, normal \nor corrected-to-normal hearing\
          \ and vision, at least a high school \neducation, between the ages of 35\
          \ and 80, and at least one year post-\nstroke."
        excluded_fragments: []
        image_sha256: 1a533fa44c26d0929775e3a00cf319771054ccd5b904e8abbe0cc2217b81a1ec
        transcription: '. All participants met the following inclusion

          criteria: chronic aphasia due to a single left-hemisphere stroke, mono-

          lingual English-speaking, medically and neurologically stable, normal

          or corrected-to-normal hearing and vision, at least a high school

          education, between the ages of 35 and 80, and at least one year post-

          stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: "Resting-state functional connectivity\nNotably, in both the RF and SVR models,\
    \ the predictor rsFMRI-\nFC emerges as a crucial feature, significantly contributing\
    \ to model \nperformance."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
