---
id: chronic_canonical_comprehension_model
name: chronic canonical sentence comprehension prediction model
kind: predictor
findings:
- id: f1
  target: canonical_sentence_comprehension
  target_kind: impairment
  claim: At the chronic time point, the model for canonical sentence comprehension
    contained greater proportion of damage to pSTG and AG, but neither was an independent
    significant predictor.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 15
    population: patients with ischemic left hemisphere stroke
    phase: not_reported
    time_post_onset: chronic stage (at least 6 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - lack of subacute stage testing
  - hypoperfusion not assessed
  - potential for brain changes between MRI and acute testing
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A LASSO regression model predicting impaired canonical
    sentence comprehension at the chronic stage, using predictors including percent
    damage to the posterior superior temporal gyrus (pSTG) and angular gyrus (AG)
    as measured by patient lesion overlap with JHU atlas parcels on acute DWI. model
    included other predictors: age, overall lesion volume, number of unrelated errors
    on the SOAP, and time since stroke onset; impaired performance defined as accuracy
    more than two standard deviations below the mean of the healthy control group.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P3-S1-C10, two-model agreement, human verification
    pending): Participants with left hemisphere stroke

    Fifteen patients (6 women, 9 men) at Johns Hopkins Hospital with ischemic left
    hemisphere stroke were enrolled in this study (Table 1) Original text-layer quotation
    is preserved below. PDF image reading (P3-S3-C11, two-model agreement, human verification
    pending): . First, they were tested at the

    acute stage within six days of stroke onset and next they were tested at

    the chronic stage of recovery (at least 6 months post-stroke) Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:canonical_sentence_comprehension
  citation: '@Sheppard2022'
  source_passages:
  - section: Original source P7-S1-C2
    page: 7
    quote: "At the chronic time point the model \nfor canonical sentence comprehension\
      \ contained greater proportion of \ndamage to pSTG and AG, but neither was an\
      \ independent significant \npredictor."
    supports: claim
  - section: Original source P3-S1-C10
    page: 3
    quote: "Participants with left hemisphere stroke \nFifteen patients (6 women,\
      \ 9 men) at Johns Hopkins Hospital with \nischemic left hemisphere stroke were\
      \ enrolled in this study (Table 1)."
    supports: sample
  - section: Original source P3-S3-C11
    page: 3
    quote: "First, they were tested at the \nacute stage within six days of stroke\
      \ onset and next they were tested at \nthe chronic stage of recovery (at least\
      \ 6 months post-stroke)."
    supports: method
  - section: Original source P3-S4-C9
    page: 3
    quote: "Proportion of infarcted \ntissue was calculated for each participant in\
      \ every anatomical parcel of \nthe Johns Hopkins University (JHU) atlas (Faria\
      \ et al., 2012; Mori et al., \n2008)."
    supports: method
  - section: Original source P5-S2-C7
    page: 5
    quote: "Predictors included age, overall lesion volume, number of \nunrelated\
      \ errors on the SOAP out of the 40 total sentences (to control for \nword-level\
      \ comprehension deficits), time since stroke onset, and percent \ndamage to\
      \ seven ROIs that previous studies have implicated in sentence \ncomprehension\
      \ (Broca’s area (IFGtri + IFGop), STG, MTG, pSTG, \nangular gyrus, supramarginal\
      \ gyrus, and SLF). \n3."
    supports: method
  - section: Original source P5-S1-C4
    page: 5
    quote: "For \nanalyses in the patient group, Least Absolute Shrinkage and Selection\
      \ \nOperator (LASSO) regression (Tibshirani, 1996) was used to evaluate \nwhether\
      \ damage to specific ROIs were related to sentence comprehen­\nsion at acute\
      \ and chronic time points."
    supports: method
  - section: Original source P5-S2-C11
    page: 5
    quote: "Impaired sentence comprehension in \nthe patient group was defined as\
      \ performance more than two standard \ndeviations below the accuracy of the\
      \ control group."
    supports: claim
  - section: Original source P9-S5-C5
    page: 9
    quote: First, we have a relatively small sample size.
    supports: limitation
  - section: Original source P10-S1-C3
    page: 10
    quote: "Fourth, we did \nnot assess hypoperfusion, which can significantly impair\
      \ brain func­\ntioning beyond the borders of the lesion at acute and chronic\
      \ stages of \nrecovery (Abbott et al., 2021; Hillis et al., 2001, 2002b, 2002a;\
      \ Love \net al., 2002; Robson et al., 2017; Thompson et al., 2017)."
    supports: limitation
predictor_type: imaging_metric
short_definition: A LASSO regression model predicting impaired canonical sentence
  comprehension at the chronic stage, using predictors including percent damage to
  the posterior superior temporal gyrus (pSTG) and angular gyrus (AG) as measured
  by patient lesion overlap with JHU atlas parcels on acute DWI.
assessment:
- Subject-relative, Object-relative, Active, and Passive Test of Comprehension (SOAP)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Sheppard2022
  proposal_id: R003
  review_status_sha256: ba0a606bbb21d1f83e4035c523ad59666fbcb4f4088f5fb7bd837681756460b8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
        A/passages.json: c3a9b0f1431f111d6badc4add5767ea6916498827a56fe2e5f19608b415f7691
        A/raw.json: fb5a66cc3265bbdcfb3a700ae975fd051e0bca7d3f4607a8f870323de90ab497
        A/source-units.json: f2c368d4fda659480ad47472a22406b3c37a4c245bfa4ad1d0bb45ae77745fa3
        A/full-source-units.json: a0b49046d3d2dae24c9adfc4a793f522f2c35eab46d162eb18de9c39febc1d84
        A/meta.json: 685251e9d7184e18f049ee3a3802fa9422c887566c4f74ea1c37a943aabe24bf
        A/table-images/page-6.png: cc9d159d5273d0bc71ed50a4743c72c017ad617895f669fa9b2ee471123cfbbe
        A/table-images/page-7.png: d8d1fd0e95f180f79350163ebea56da76265831651e0af0306461499edc71b48
        A/table-images/page-5.png: 4f7cc5fd4cb291488d104c4ce514c50e27d2d95d60ffd026ee1c7a44d1593d79
        A/table-images/page-4.png: a9cc826caf60d728c81946ea141fdc8f224e0181ecedd041423ff117324a1d7e
        A/table-images/TABLE-1-page-4-1.png: 0ce6e9d005499f337cdd16e3273558835d375aab39d2f914557abe8399454109
        A/table-images/TABLE-3-page-6-1.png: 550c7edff9c309c70912d1a25c4ff28101065daccf1f1159b19016b1f24914f2
        A/table-images/manifest.json: 5e3108ebf13c4fa7f75ab4549b1dac40dd7d082a6557bd2efc53e90584efa631
        A/table-images/TABLE-3-page-5-1.png: e5430f9011dbf345e942c4a45be739d83a93ac876bfb9fadcbd64fcfe1be9db7
        A/table-images/TABLE-4-page-7-1.png: 1ed0b4b16fb0a844cf6999a4b3faf0c76a58cc06fe0e037da7438aa2a6d948cf
        A/table-images/TABLE-5-page-7-2.png: 33b17d26ad9649b6d75cf69026ae5b7bdba56641b4ce0414bb2f0ec14626464e
        A/table-images/TABLE-2-page-5-2.png: a66622a4a120e7898513357b678205141c2f3802fd9643fcf0cd80981d270a81
        A/clauses/window-11/raw.json: 364d86f48bd628402fa7b46edeed2b637db08e9fd8dffb58aa1a6bf7bc5d484b
        A/clauses/window-11/prompt.txt: 76c6951dbaf01cbc3f4674b6afdf8659a67464c7a0ca2b9e260e418f05e38aee
        A/clauses/window-11/meta.json: 210061dd1e7b1be7abb112faf6c4faf696ec66c844def437514cc0e5ee643357
        A/clauses/window-10/raw.json: 8a8f78d8a14d35309a95c77e2b16a909fd1211628f166441f4ec2178e564f1ff
        A/clauses/window-10/prompt.txt: b8d612a6fbc4638fe49743533c7c67f475dd902598c1dbf2d19115e6c05e6662
        A/clauses/window-10/meta.json: 2d51e66f95d247385c8e39fe07096f9d9e11e95e8936e614c3871db5b7304b4c
        A/clauses/window-03/raw.json: 3d8b08a9becfe98063316b142f10d8650b72e0b0e5b1077658504eb8bc871eb3
        A/clauses/window-03/prompt.txt: 8c952a931efcbeb1b7dc5953b9e67c7f6960af85353ef34a689507f786beade6
        A/clauses/window-03/meta.json: b56af9039eb5cbdc624165e6fdfdd2e307076784cabdc5573f727727e6b30c19
        A/clauses/window-04/raw.json: a96d89e57b3ea28ce0a1d225fef0fcaaf6f4d3bffbc6d0642fd9e2c3dce9aca4
        A/clauses/window-04/prompt.txt: 36e1ffb3f23933a77f45ff7202592c9472b65783af56f60cd7bb29b66be9693d
        A/clauses/window-04/meta.json: 6c42769e2143396abcd203ae0721f061e0b8339839e1dcfc3e1fed6bd5117502
        A/clauses/window-05/raw.json: 04a5cbf15ec9aabc04dc323de434879bbef57143534a898fc839451e31b72862
        A/clauses/window-05/prompt.txt: fcbc42043ca357a32e4407a92c8c03c814d96bd0b0781ffae9d65b74538576e7
        A/clauses/window-05/meta.json: aee49975456c356ec9391be2749835e405c01773f99fdeac1070fdc377d97879
        A/clauses/window-02/raw.json: 278b9c4762e02d1d29f564fa4958c8c79ed993b59d1c667a3956b7dd270adabd
        A/clauses/window-02/prompt.txt: 9bb69140f159758dd123d68be2ee5713c45c18aff263da22f64c893a568517ef
        A/clauses/window-02/meta.json: f259dc49d874302fa5d77adf804d53cb0be54279b224b7d0a0f93960093b0098
        A/clauses/window-09/raw.json: f4673a0a523da91f1d5281f59354e3adcc27e5748eab72deba56530579eef85e
        A/clauses/window-09/prompt.txt: 87815eabf61ccd2a44e00d6869de3a3249aa11b96521194a2354d0e31baa8b3b
        A/clauses/window-09/meta.json: aaaca0df733426565b08af16a0c7226f9d572f46125f2ab1c2f27be6a63676c2
        A/clauses/window-07/raw.json: 6f38965b4fe4f7480575a6ead76433cd046e8afc23ed399481316b2262d62c75
        A/clauses/window-07/prompt.txt: a9c521e9b9d9950014a9a600d4564e63fd1fe57aedb8a30c4bb45122cfc46ed6
        A/clauses/window-07/meta.json: e5c3554e5ede49a0fc7610056de614500cdf38e8b000e8b36a8cdfe5debbb55d
        A/clauses/window-01/raw.json: b95f13ce941ce7d04192afea1f639469561c890e71461cd2ff1d7c98083fb88f
        A/clauses/window-01/prompt.txt: 03892e578f34efde3ff843823c8fe12df99cb97fd4eb9eb78f470cad78ce587e
        A/clauses/window-01/meta.json: e9271d48248801fb3ab376d69947af9a3a8eb8054c64092bb7ac4075c44f6754
        A/clauses/window-06/raw.json: 1764c32d15add55d442ed89e5ef702dbefe910bce7a9708ef0df77c04fb4a2ce
        A/clauses/window-06/prompt.txt: 77d33e6991079f02f738e3da3e9b15350601bd180872c4233f8dab7090ef9ce7
        A/clauses/window-06/meta.json: f0ba67b0b07b848e9706f15951f532622d636dd87f3f1bcfcb69fd6b10d23f03
        A/clauses/window-08/raw.json: 5a6a84743c082c471ed9da8b4fc313eef0f48bbdb530cf4900aaa3c3636ad5e0
        A/clauses/window-08/prompt.txt: 69d33cb5a9543bd80e7430935754b9577a56aa50176d49e53ae50ccdf5753d22
        A/clauses/window-08/meta.json: 22a52acc84ccf1d12f91c8cff49d89517843734ad2be76b7e8c95a3e81d68630
        A/tables/TABLE-2-page-5-3/raw.json: 19632f4b34628efc4e9c909b32f60aae803697cdf17e513933257a1db58bde43
        A/tables/TABLE-2-page-5-3/prompt.txt: e6d2a555f8e7b3c2bf1e773a055172515f7f602e25d3d80a4421e79171dc1b78
        A/tables/TABLE-2-page-5-3/meta.json: a0852c1195bf0925e1876de0f611f463e6b6ceed64d99310c946dbf590d259df
        A/tables/TABLE-3-page-5-2/raw.json: 19632f4b34628efc4e9c909b32f60aae803697cdf17e513933257a1db58bde43
        A/tables/TABLE-3-page-5-2/prompt.txt: 73e53bc461d35a5eea5e7fdadf151947a0c8feef49a25652b8cf6f8518b28af3
        A/tables/TABLE-3-page-5-2/meta.json: d20ca26c38058a44d428e808fa57e81fa9d3590a52985df52dae98ce631bc506
        A/tables/TABLE-5-page-7-6/raw.json: bc3a0272c20c0844ba92efc0003a6b198381c6cdf26ab1c78d2c2fa3d84192a1
        A/tables/TABLE-5-page-7-6/prompt.txt: f0219e636e73f452021c72199fff1345b615eea240cc7d988bd907a218a11f05
        A/tables/TABLE-5-page-7-6/meta.json: ff0a6edbbbb034c76c9fa436c27c8f9098085d06d0b36c835ce6d47a649d8caf
        A/tables/TABLE-3-page-6-4/raw.json: a296a4e72cdb676bcbd7221d7b34f7371f12a253b9d41ec100daa07cb282a0b0
        A/tables/TABLE-3-page-6-4/prompt.txt: 42050b6669e8bdd9fe4edd4525b1f07bdbe94f4519c798e5175a7bdee2af7f53
        A/tables/TABLE-3-page-6-4/meta.json: 3b8bb3722b07872f7c8cd15f6187da2c890b3a30ad49fabe67d719942f0844d2
        A/tables/TABLE-1-page-4-1/raw.json: 54043c85797433602ea362e9f3d252175804de563408f19715f77c987405e1b4
        A/tables/TABLE-1-page-4-1/prompt.txt: 9d8b68e0ff57a0126b16200e817552d6e6e8fc1d9dfcc1ff4f6cd6bc1e5dd4dd
        A/tables/TABLE-1-page-4-1/meta.json: 661aecb030adc882a1038ad3761a8a1dee9b83dabe039fbaaa279ccfd39dc8d4
        A/tables/TABLE-4-page-7-5/raw.json: 7b67b5682ca7f85e6dbb43e30f3f18e9411cae519333c00acef85ed51e0d83ce
        A/tables/TABLE-4-page-7-5/prompt.txt: 6e9587abff25ffc1e6e5d1ac1b2f09b4df094b118f36bdd287d56a6ea2e202f3
        A/tables/TABLE-4-page-7-5/meta.json: 14d33b39f2c28ca991b4aaadc2ed6f121844a917b2a0fbf708cb9d0d084d846a
        B/passages.json: c3a9b0f1431f111d6badc4add5767ea6916498827a56fe2e5f19608b415f7691
        B/raw.json: a51af8f1cc4931d0dd8d6e4652484c83229a38d80d3c84e5255c0101ac754feb
        B/source-units.json: f2c368d4fda659480ad47472a22406b3c37a4c245bfa4ad1d0bb45ae77745fa3
        B/full-source-units.json: a0b49046d3d2dae24c9adfc4a793f522f2c35eab46d162eb18de9c39febc1d84
        B/meta.json: 70100d1e582460f99eb1520556ae5634d646b796e3481d422d68e3b356f094c7
        B/table-images/page-6.png: cc9d159d5273d0bc71ed50a4743c72c017ad617895f669fa9b2ee471123cfbbe
        B/table-images/page-7.png: d8d1fd0e95f180f79350163ebea56da76265831651e0af0306461499edc71b48
        B/table-images/page-5.png: 4f7cc5fd4cb291488d104c4ce514c50e27d2d95d60ffd026ee1c7a44d1593d79
        B/table-images/page-4.png: a9cc826caf60d728c81946ea141fdc8f224e0181ecedd041423ff117324a1d7e
        B/table-images/TABLE-1-page-4-1.png: 0ce6e9d005499f337cdd16e3273558835d375aab39d2f914557abe8399454109
        B/table-images/TABLE-3-page-6-1.png: 550c7edff9c309c70912d1a25c4ff28101065daccf1f1159b19016b1f24914f2
        B/table-images/manifest.json: e898bdc3147c3665b0d542a7df4f17f66e1e89501b27b5359f016feccb7d417c
        B/table-images/TABLE-3-page-5-1.png: e5430f9011dbf345e942c4a45be739d83a93ac876bfb9fadcbd64fcfe1be9db7
        B/table-images/TABLE-4-page-7-1.png: 1ed0b4b16fb0a844cf6999a4b3faf0c76a58cc06fe0e037da7438aa2a6d948cf
        B/table-images/TABLE-5-page-7-2.png: 33b17d26ad9649b6d75cf69026ae5b7bdba56641b4ce0414bb2f0ec14626464e
        B/table-images/TABLE-2-page-5-2.png: a66622a4a120e7898513357b678205141c2f3802fd9643fcf0cd80981d270a81
        B/clauses/window-11/raw.json: abb69620213e0849b3012c8d614909574bb5b3a513c1a5fb12e4a81e8eca6e31
        B/clauses/window-11/prompt.txt: 76c6951dbaf01cbc3f4674b6afdf8659a67464c7a0ca2b9e260e418f05e38aee
        B/clauses/window-11/meta.json: 886bf1373b2effaf738ab54fcbcbc316a5ff725dc7d8193117d6f136287a85ca
        B/clauses/window-10/raw.json: ff6c2db24b6ab64b2cdc441ad6750417bd03bc8e2b4dc4a7d9695b4cf1065c83
        B/clauses/window-10/prompt.txt: b8d612a6fbc4638fe49743533c7c67f475dd902598c1dbf2d19115e6c05e6662
        B/clauses/window-10/meta.json: b12d552ebe4d9a74c1d9882bc616e11b9cdac98182112f99c772e7b6cd9284d8
        B/clauses/window-03/raw.json: 047f1a1082e947eeb93e4e6761e3487549a9fb98244bc80728b8a2d69d24f547
        B/clauses/window-03/prompt.txt: 8c952a931efcbeb1b7dc5953b9e67c7f6960af85353ef34a689507f786beade6
        B/clauses/window-03/meta.json: ac3d6c901ed4e17bfca4d8219f9acfdbb81ac640f5db5b8883f0e3ac916854e6
        B/clauses/window-04/raw.json: 5f8f30ca3a1483a3d96dee7d02202e5fd0246ae903916fea124dc962dc7a6107
        B/clauses/window-04/prompt.txt: 36e1ffb3f23933a77f45ff7202592c9472b65783af56f60cd7bb29b66be9693d
        B/clauses/window-04/meta.json: ab7b9c7697b6ea150acb5f817eb49d60fcfa936d725dec9b409ac55cacbef643
        B/clauses/window-05/raw.json: fcf073ced8cb5d2b521ee4b8e35e488476179a193c1365532a618115ea19f1f5
        B/clauses/window-05/prompt.txt: fcbc42043ca357a32e4407a92c8c03c814d96bd0b0781ffae9d65b74538576e7
        B/clauses/window-05/meta.json: 8224418b5e9461695088bdcd807d23e63a14e26707dc0c68c6ac66663f40d6e5
        B/clauses/window-02/raw.json: 94549dcbacaac952dead7c9cad744e5f5c6d2c451f91748d41c834ad4c377880
        B/clauses/window-02/prompt.txt: 9bb69140f159758dd123d68be2ee5713c45c18aff263da22f64c893a568517ef
        B/clauses/window-02/meta.json: 64cda7d6613440cbc488191eb6f21833bc2263a5f4768f1e57237b76eaa4d8fd
        B/clauses/window-09/raw.json: 6552c5ae3fb4a44ff0e76074d07cafc9cacf475ef27b1f54e69eb48bd561d0e2
        B/clauses/window-09/prompt.txt: 87815eabf61ccd2a44e00d6869de3a3249aa11b96521194a2354d0e31baa8b3b
        B/clauses/window-09/meta.json: 59fd8748f7d64b5e95e0ecf9ad29ad9acf899bda87564f0f7064405bb19351f0
        B/clauses/window-07/raw.json: 73d91381239064fc8b61ac5f315375c8956445d797792a81860251162dfbcd90
        B/clauses/window-07/prompt.txt: a9c521e9b9d9950014a9a600d4564e63fd1fe57aedb8a30c4bb45122cfc46ed6
        B/clauses/window-07/meta.json: b45ab21b97915ae9e4128a0c9a835ce1b802b6c42d509b77934dbe1bdb80d418
        B/clauses/window-01/raw.json: 7dbcf6fefd90233e88fd8ef683c8919ac6bf8a18b24477069a823326af83ff8c
        B/clauses/window-01/prompt.txt: 03892e578f34efde3ff843823c8fe12df99cb97fd4eb9eb78f470cad78ce587e
        B/clauses/window-01/meta.json: 6d05a58baaf997213194fdb6903fadeb7ea187076aefd07925653818564ae484
        B/clauses/window-06/raw.json: bd446d41f79852143eaae926a4bc07009352f2121bec809ecc9c8f725158fb67
        B/clauses/window-06/prompt.txt: 77d33e6991079f02f738e3da3e9b15350601bd180872c4233f8dab7090ef9ce7
        B/clauses/window-06/meta.json: c485751e59d27ec1ad40479a482ab55461546237bfe38546e3277c41af923ed3
        B/clauses/window-08/raw.json: 18a6160577ff2ba5a779152002f134eb15f8dd821212c212700a68acedc1ea9a
        B/clauses/window-08/prompt.txt: 69d33cb5a9543bd80e7430935754b9577a56aa50176d49e53ae50ccdf5753d22
        B/clauses/window-08/meta.json: def6d2a93a9a93c13d55ef70c133e3eebdbd1629da76e1bf48a88545dd33a775
        B/tables/TABLE-2-page-5-3/raw.json: 57ab9146d38ddb33131bf7452b8c75e5f63b42ae98a9c53763f2009c10778e3a
        B/tables/TABLE-2-page-5-3/prompt.txt: e6d2a555f8e7b3c2bf1e773a055172515f7f602e25d3d80a4421e79171dc1b78
        B/tables/TABLE-2-page-5-3/meta.json: f35bfc9574efafc323953cdf26509198ae83d4d0946abf179ec7b810458bcad5
        B/tables/TABLE-3-page-5-2/raw.json: 57ab9146d38ddb33131bf7452b8c75e5f63b42ae98a9c53763f2009c10778e3a
        B/tables/TABLE-3-page-5-2/prompt.txt: 73e53bc461d35a5eea5e7fdadf151947a0c8feef49a25652b8cf6f8518b28af3
        B/tables/TABLE-3-page-5-2/meta.json: 130f93954333152678e1b61ed04f429cd302c77c6934352472b0dd61b8c50d49
        B/tables/TABLE-5-page-7-6/raw.json: a28f2143ed09db9958b55727bced3243e447447aa1cea45c206ff5c87d2d44a4
        B/tables/TABLE-5-page-7-6/prompt.txt: f0219e636e73f452021c72199fff1345b615eea240cc7d988bd907a218a11f05
        B/tables/TABLE-5-page-7-6/meta.json: 3b64c84d4f0585f833691e4a00ef9b4cf3501733e2fc8803616ddb92d1b40588
        B/tables/TABLE-3-page-6-4/raw.json: 3d0b6113825c11e999617b4e0bc9ff5f2a0d370b2c0e200a8fd4c6486fd051c3
        B/tables/TABLE-3-page-6-4/prompt.txt: 42050b6669e8bdd9fe4edd4525b1f07bdbe94f4519c798e5175a7bdee2af7f53
        B/tables/TABLE-3-page-6-4/meta.json: 876d6292f839b77306799bbdc55a098aee12723b8c2617c080a11442b34ee310
        B/tables/TABLE-1-page-4-1/raw.json: 85a47e764835b994ce1667f5605b92c85feb5e211bfce6b2ac98e207555ecec9
        B/tables/TABLE-1-page-4-1/prompt.txt: 9d8b68e0ff57a0126b16200e817552d6e6e8fc1d9dfcc1ff4f6cd6bc1e5dd4dd
        B/tables/TABLE-1-page-4-1/meta.json: 1dc59d91ae72c4d58f3832ef5f09f578ee51724e9f1c99a3fbf3cd0b061ae939
        B/tables/TABLE-4-page-7-5/raw.json: d6581248091898fcf02739adc6445e63d08be1f56d8dee871c5ce1a6af26af48
        B/tables/TABLE-4-page-7-5/prompt.txt: 6e9587abff25ffc1e6e5d1ac1b2f09b4df094b118f36bdd287d56a6ea2e202f3
        B/tables/TABLE-4-page-7-5/meta.json: 3d637185a3341f10aa1ba8d0bef3dccf0460e93d5a16614fdac02b8bc551774e
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
      pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2022
      source_status_sha256: b4e56e81a2cfbecfcef9d54b9d11641510cc735316337383ea47325d758c57cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: percent damage to posterior superior temporal gyrus (pSTG) and angular
        gyrus (AG)
    outcome:
      text: canonical sentence comprehension
    analysis_label: Chronic canonical sentence comprehension prediction
    relation: association
    evidence_ids:
    - P7-S1-C2
    qualifier_ids:
    - P7-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2022
      source_status_sha256: b4e56e81a2cfbecfcef9d54b9d11641510cc735316337383ea47325d758c57cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C13
      - Result passage disposed without unit P2-S3-C14
      - Result passage disposed without unit P2-S3-C15
      - Result passage disposed without unit P2-S4-C3
      - Accounting without a linked unit P3-S3-C2
      - Unaccounted source passage P3-S3-C2
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C6
      - Accounting without a linked unit P5-S3-C8
      - Accounting without a linked unit P5-S3-C9
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C7
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P5-S3-C8
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P6-S1-C2
      - Unaccounted source passage P5-S3-C9
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P6-S2-C5
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P8-S2-C8
      - Result passage disposed without unit P8-S2-C9
      - Accounting without a linked unit P8-S3-C4
      - Accounting without a linked unit P8-S3-C5
      - Unaccounted source passage P8-S3-C4
      - Unaccounted source passage P8-S3-C5
      - Result passage disposed without unit P8-S3-C11
      - Result passage disposed without unit P8-S3-C6
      - Result passage disposed without unit P8-S3-C7
      - Result passage disposed without unit P8-S4-C3
      - Result passage disposed without unit P8-S4-C5
      - Result passage disposed without unit P8-S5-C5
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C4
      - Result passage disposed without unit P9-S1-C5
      - Result passage disposed without unit P9-S1-C7
      - Result passage disposed without unit P9-S2-C4
      - Result passage disposed without unit P9-S2-C5
      - Result passage disposed without unit P9-S2-C7
      - Result passage disposed without unit P9-S2-C8
      - Accounting without a linked unit P9-S4-C12
      - Unaccounted source passage P9-S4-C12
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S1-C6
      unattached_null_or_qualifier_ids:
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C3
      - P6-S1-C4
      - P6-S2-C6
      - P9-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      suppressed_nonrepresented_units: 35
      default_disposition_count_requires_completeness_check: 216
      unselected_timing_passages:
      - P1-S1-C13
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C16
      - P3-S2-C5
      - P3-S2-C13
      - P3-S4-C4
      - P8-S1-C3
      - P9-S5-C7
      - P10-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: limitations
        source_ids:
        - P9-S5-C4
        - P9-S5-C5
        - P9-S5-C6
        - P9-S5-C7
        - P9-S5-C8
        - P10-S1-C1
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-3
      - TABLE-3-page-5-2
      - TABLE-3-page-6-4
      - TABLE-4-page-7-5
      - TABLE-5-page-7-6
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S4
        - P5-S3
        - P5-S4
        - P6-S1
        - P6-S2
        - P8-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2022
      source_status_sha256: b4e56e81a2cfbecfcef9d54b9d11641510cc735316337383ea47325d758c57cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 0
      - 3
      reason: Abstract summary of acute deficits related to word-level comprehension,
        SMG, and SLF.
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Abstract statement that Broca's area was only implicated in chronic
        deficits.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes previous study by Saur et al. (2006).
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes previous study by Saur et al. (2006).
    - source_id: P2-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes previous study by Saur et al. (2006).
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes previous study by Saur et al. (2006).
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes age matching statistical test.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ROI selection criteria.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes LASSO regression utility.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports healthy control mean accuracy.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports acute mean accuracy for patient group.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of impaired patients acutely.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports chronic mean accuracy for patient group.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of impaired patients chronically.
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for canonical sentences.
    - source_id: P5-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for canonical sentences.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for canonical sentences.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for canonical sentences.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for noncanonical sentences.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for noncanonical sentences.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of unimpaired patients.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error analysis results (thematic vs unrelated).
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error analysis results (thematic vs unrelated).
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error analysis results (thematic vs unrelated).
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 4.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 5.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 3
      reason: Reports acute canonical and noncanonical predictors.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports independent predictor for acute canonical sentences.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports acute canonical predictors and independent predictor.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports chronic canonical predictors.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Reports acute noncanonical predictors.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports independent predictors for acute noncanonical sentences.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports chronic noncanonical predictors and independent predictor.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 7
      - 9
      reason: Reports chronic asyntactic predictors and null result for acute asyntactic.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Reports independent predictor for chronic asyntactic comprehension.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Restatement of independent predictor for chronic asyntactic comprehension.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean accuracy improvement for canonical sentences.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of impaired patients for canonical sentences.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general improvement trend.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient decline.
    - source_id: P8-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on noncanonical difficulty.
    - source_id: P8-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean accuracy for noncanonical sentences.
    - source_id: P8-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual score stability.
    - source_id: P8-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of impaired patients for noncanonical sentences.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal improvement for noncanonical sentences.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes longitudinal changes for noncanonical sentences.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error analysis trend (unrelated errors).
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error analysis trend (thematic reversals).
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes evolution of error types.
    - source_id: P8-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient declines.
    - source_id: P8-S3-C4
      disposition: represented
      result_indexes:
      - 0
      - 3
      reason: Restatement of acute predictors for canonical and noncanonical sentences.
    - source_id: P8-S3-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Restatement of SLF as predictor for acute noncanonical sentences.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 5
      - 9
      reason: Restatement of chronic noncanonical and acute asyntactic predictors.
    - source_id: P8-S3-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Restatement of chronic asyntactic predictors.
    - source_id: P8-S3-C11
      disposition: represented
      result_indexes:
      - 3
      - 5
      reason: Comparison of acute (inferior parietal) vs chronic (Broca's) implications.
    - source_id: P8-S4-C3
      disposition: represented
      result_indexes:
      - 5
      - 7
      reason: Restatement of Broca's area association with chronic noncanonical and
        asyntactic comprehension.
    - source_id: P8-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with Magnusdottir et al. (2013).
    - source_id: P8-S4-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Restatement of pSTG and Broca's area as chronic noncanonical predictors.
    - source_id: P8-S5-C5
      disposition: represented
      result_indexes:
      - 3
      - 5
      reason: Synthesis of acute (SMG) vs chronic (Broca's/pSTG) deficits.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 3
      - 5
      reason: Synthesis of acute (SLF, SMG) vs chronic (Broca's, pSTG) deficits.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Broca's area role.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on noncanonical vs canonical difficulty.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on chronic canonical impairment.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Broca's area compensation.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on patient deficits.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on patient decline.
    - source_id: P9-S4-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Null result for Broca's area in acute asyntactic/canonical/noncanonical
        comprehension.
    - source_id: P9-S5-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Null result for Broca's area in acute asyntactic/canonical/noncanonical
        comprehension.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 3
      - 5
      reason: Synthesis of acute (SLF, SMG) vs chronic (Broca's, pSTG) deficits.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 5
      - 7
      reason: Statement that Broca's area was only implicated in chronic stages.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Conclusion that Broca's area is not as critical as temporoparietal areas
        acutely.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on chronic difficulties.
    unresolved_coverage:
    - source_id: P6-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S5-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S5-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C15
    - P1-S1-C16
    - P2-S3-C13
    - P2-S3-C14
    - P2-S3-C15
    - P2-S4-C3
    - P3-S3-C2
    - P5-S1-C1
    - P5-S1-C6
    - P5-S2-C10
    - P5-S2-C13
    - P5-S3-C3
    - P5-S3-C4
    - P5-S3-C5
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C8
    - P5-S3-C9
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P6-S2-C4
    - P7-S1-C7
    - P8-S1-C7
    - P8-S1-C8
    - P8-S1-C9
    - P8-S1-C10
    - P8-S1-C12
    - P8-S1-C13
    - P8-S1-C14
    - P8-S1-C15
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C8
    - P8-S2-C9
    - P8-S3-C9
    - P8-S3-C10
    - P8-S3-C11
    - P8-S4-C3
    - P8-S4-C4
    - P8-S4-C5
    - P8-S5-C5
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C7
    - P9-S2-C3
    - P9-S2-C4
    - P9-S2-C5
    - P9-S2-C7
    - P9-S2-C8
    - P9-S4-C12
    - P9-S5-C2
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C10
    - P10-S1-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-3
    - TABLE-3-page-5-2
    - TABLE-3-page-6-4
    - TABLE-4-page-7-5
    - TABLE-5-page-7-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C10
      - P3-S2-C12
      recruited_sample:
      - P3-S1-C10
      - P3-S2-C12
      eligibility:
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C15
      - P3-S1-C16
      - P3-S1-C17
      imaging_provenance:
      - P3-S4-C1
      - P3-S4-C8
      - P3-S4-C9
      imaging_timing:
      - P3-S4-C2
      - P3-S4-C3
      outcome_timing:
      - P3-S1-C3
      - P3-S2-C4
      - P3-S3-C11
      - P5-S1-C11
      - P6-S2-C2
      outcome_definition:
      - P5-S1-C11
      - P5-S2-C11
      - P5-S2-C12
      validation:
      - P5-S1-C8
      analysis_restrictions:
      - P5-S1-C10
      dependent_variable_statement:
      - P5-S1-C12
      - P6-S2-C2
      - P6-S2-C3
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S2-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C10
      - P3-S1-C12
      - P3-S1-C13
      - P3-S1-C14
      - P3-S1-C15
      - P3-S1-C16
      - P3-S1-C17
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: limitations
      source_ids:
      - P9-S5-C4
      - P9-S5-C5
      - P9-S5-C6
      - P9-S5-C7
      - P9-S5-C8
      - P10-S1-C1
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
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
      pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
      review_sha256: ba0a606bbb21d1f83e4035c523ad59666fbcb4f4088f5fb7bd837681756460b8
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
      - P7-S1-C2
      source_result: At the chronic time point, the LASSO regression model for canonical
        sentence comprehension included greater proportion of damage to the posterior
        superior temporal gyrus (pSTG) and angular gyrus (AG) as predictors, but neither
        region was an independent significant predictor of performance.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source P7-S1-C2 explicitly describes the chronic time point
            model for canonical sentence comprehension. The proposed core correctly
            identifies this specific analysis (chronic, canonical) and the specific
            predictors (pSTG, AG) mentioned in that passage.
          source_ids:
          - P7-S1-C2
          - P5-S1-C4
        direction:
          answer: fits
          reason: The source states that while pSTG and AG were in the model, 'neither
            was an independent significant predictor.' The proposed core uses 'no_effect'
            to represent this lack of significant association, which is faithful to
            the source's finding of non-significance for these specific variables
            in this specific model.
          source_ids:
          - P7-S1-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as percent damage to pSTG and
            AG. The outcome is canonical sentence comprehension. The measurement method
            is correctly identified as lesion overlap with atlas parcels (JHU atlas)
            on DWI, which corresponds to 'template_lesion_overlap' rather than patient
            diffusion tractography or functional imaging.
          source_ids:
          - P3-S4-C9
          - P3-S4-C11
          - P5-S1-C4
        qualifications:
          answer: fits
          reason: The proposed core includes the necessary context that this is a
            LASSO model and that the variables were included but not significant.
            It correctly notes the population (left hemisphere stroke) and timing
            (chronic).
          source_ids:
          - P7-S1-C2
          - P3-S1-C10
        missing_material_caveat:
          answer: fits
          reason: The core captures the essential finding that the association was
            not significant. While the source mentions other predictors in the model
            (age, lesion volume, etc.), the specific claim regarding pSTG and AG is
            accurately represented as non-significant. No material caveat that changes
            the interpretation of the null result for these specific ROIs is omitted.
          source_ids:
          - P7-S1-C2
          - P5-S2-C7
      optional_pending:
      - Specific p-values or coefficients for pSTG and AG in the chronic canonical
        model
      - Details of the other significant predictors in the chronic canonical model
        (if any, though source implies none for pSTG/AG)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values or coefficients for pSTG and AG in the chronic canonical model
    - Details of the other significant predictors in the chronic canonical model (if
      any, though source implies none for pSTG/AG)
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: percent damage to posterior superior temporal gyrus (pSTG) and angular
          gyrus (AG)
      outcome:
        text: canonical sentence comprehension
      analysis_label: Chronic canonical sentence comprehension prediction
      relation: association
      evidence_ids:
      - P7-S1-C2
      qualifier_ids:
      - P7-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
        source_review: _compare/relationships-2026-11-16/review-current/Sheppard2022
        source_status_sha256: b4e56e81a2cfbecfcef9d54b9d11641510cc735316337383ea47325d758c57cd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3a0c8111c953b4660a828eabe74d85330a579f22d8e0b74ec3ac4dd05b90d2e9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C10
          page: 3
          text_layer_sha256: 3a0c8111c953b4660a828eabe74d85330a579f22d8e0b74ec3ac4dd05b90d2e9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants with left hemisphere stroke \nFifteen patients\
          \ (6 women, 9 men) at Johns Hopkins Hospital with \nischemic left hemisphere\
          \ stroke were enrolled in this study (Table 1)."
        anchor_text: "Participants with left hemisphere stroke \nFifteen patients\
          \ (6 women, 9 men) at Johns Hopkins Hospital with \nischemic left hemisphere\
          \ stroke were enrolled in this study (Table 1)."
        excluded_fragments: []
        image_sha256: 92d32b235b639dabef25df32cc37bf87a656a445e7430c618b037d4585babf64
        transcription: 'Participants with left hemisphere stroke

          Fifteen patients (6 women, 9 men) at Johns Hopkins Hospital with ischemic
          left hemisphere stroke were enrolled in this study (Table 1)'
      P3-S3-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a0bd896c83907cadd201eb6a8d28ecb8ed2932e4ab412b27f2e3088a7e4b8b6d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 730152c34f4509a560380aab0aa80018dfde28ffd1d51a429e3e886a980de38c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C11
          page: 3
          text_layer_sha256: 730152c34f4509a560380aab0aa80018dfde28ffd1d51a429e3e886a980de38c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "First, they were tested at the \nacute stage within six days\
          \ of stroke onset and next they were tested at \nthe chronic stage of recovery\
          \ (at least 6 months post-stroke)."
        anchor_text: "First, they were tested at the \nacute stage within six days\
          \ of stroke onset and next they were tested at \nthe chronic stage of recovery\
          \ (at least 6 months post-stroke)."
        excluded_fragments: []
        image_sha256: 48093d85aeb909870fc87cd14e9d9aec2ba7ae67829df09c9bfabfb9692cae10
        transcription: '. First, they were tested at the

          acute stage within six days of stroke onset and next they were tested at

          the chronic stage of recovery (at least 6 months post-stroke)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "At the chronic time point the model \nfor canonical sentence comprehension\
    \ contained greater proportion of \ndamage to pSTG and AG, but neither was an\
    \ independent significant \npredictor."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
