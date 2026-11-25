---
id: chronic_stage_activation_comparison
name: chronic stage activation comparison
kind: predictor
findings:
- id: f1
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: language_activation
    reason: Imaging or methodological endpoint; retain its scope and do not relabel it as a behaviour.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  target: language_activation
  target_kind: impairment
  claim: The comparison of controls and patients in the chronic stage did not show
    any significant differences in language-specific activation.
  direction: no_effect
  relationship: correlational
  method: fMRI_activation
  sample:
    n: not_reported
    population: Aphasic patients with embolic first-ever left MCA territory stroke
      and age-matched controls
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
  - Highly selected patient group (able to perform early fMRI and cooperate during
    sessions)
  - Results limited to somewhat less severely impaired patients who were able to understand
    the task
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Language-specific activation (intelligible speech
    > reversed speech) measured by fMRI in the chronic stage (mean 321 days post-stroke).
    Comparison performed using two-sample t-tests; Statistical threshold for this
    comparison was P < 0.001 uncorrected. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P4-S2-C5, two-model
    agreement, human verification pending): . From a total of 198 consecutively screened
    aphasic

    stroke patients, 14 met our inclusion criteria and were

    recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

    11 male and three female] Original text-layer quotation is preserved below. PDF
    image reading (P4-S2-C4, two-model agreement, human verification pending): Results

    Clinical data

    The control group comprised 11 male and three female subjects, aged between 18
    and 66 years [mean (SD): 48.6 (13.9) years] Original text-layer quotation is preserved
    below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:language_activation
  citation: '@Saur2006'
  source_passages:
  - section: Original source P6-S1-C10
    page: 6
    quote: 'The comparison of controls and patients in the chronic

      stage did not show any signiﬁcant differences (no ﬁgure,

      Table 6).'
    supports: claim
  - section: Original source P4-S2-C5
    page: 4
    quote: 'From a total of 198 consecutively screened aphasic

      stroke patients, 14 met our inclusion criteria and were

      recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

      11 male and three female].'
    supports: sample
  - section: Original source P4-S2-C4
    page: 4
    quote: 'Results

      Clinical data

      The control group comprised 11 male and three female sub-

      jects, aged between 18 and 66 years [mean (SD): 48.6 (13.9)

      years].'
    supports: sample
  - section: Original source P2-S4-C2
    page: 2
    quote: "A follow-up examina-\ntion in the chronic stage was carried out \x024–12\
      \ months post-stroke\n(Ex3, mean: 321 dps)."
    supports: method
  - section: Original source P4-S1-C14
    page: 4
    quote: 'Statistical inference

      For the language activation in controls and aphasic patients at

      different phases, we report regions that showed signiﬁcant effects

      at P < 0.05 corrected for multiple comparisons across the whole

      brain; for comparisons of patients at different phases, for compar-

      isons of patients with controls and for the correlation analyses,

      the statistical threshold was lowered to P < 0.001 uncorrected for

      multiple comparisons across the whole brain.'
    supports: method
  - section: Original source P12-S3-C7
    page: 12
    quote: 'Thus, the

      results are limited to somewhat less severely impaired patients

      who were clearly aphasic at the ﬁrst exam but were able to

      understand the task.'
    supports: limitation
  - section: Original source P11-S1-C4
    page: 11
    quote: 'However, our

      observations reﬂect the optimal course of language recovery

      after stroke derived from a highly selected patient group, all

      able to perform early fMRI and all presenting with an embolic

      ﬁrst-ever stroke hitting an otherwise ‘healthy’ brain with high

      plastic potential.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Language-specific activation (intelligible speech > reversed speech)
  measured by fMRI in the chronic stage (mean 321 days post-stroke).
assessment:
- fMRI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Saur2006
  proposal_id: R010
  review_status_sha256: 62f2029b8c3c7c439c1d6c00c11eb6280d30f7de8dde5ca4a7dcdcc0940f79bb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
        A/passages.json: 024247056c296c4b91a4495a69a6f6f8101bffed48993ef901c25010e5b10cab
        A/raw.json: d7bcb3f5f2ac45fc316058122d22166e8e32a2923af20a75c30bac19aa5298be
        A/source-units.json: 9169078814ecb6194e142e3e513894a6d08aea855ff7b35dcb9f84609a0ce970
        A/full-source-units.json: 96e7b7371c5212d0ff5c064d3425e9ca55add9a7bd43b594cd10f796bfc673a0
        A/meta.json: c233caba4a460064666716dc3ff71802e91e7aa5a59b666916b62213d8df9434
        A/table-images/TABLE-5-page-9-2.png: 1ef6a2901109353005ecfd00fd7cc9e57daf30cf05c771f96711a62b2b74a270
        A/table-images/TABLE-1-page-5-1.png: 4ac269b112ff01190acdc1c749082b50c8ba9450b2c4b890671eb48df847fda8
        A/table-images/TABLE-4-page-9-1.png: c991c7e57cd7bd84b0d73c265b5940e7f6d17902a4eabc8a2c0c10a71c50b1b6
        A/table-images/page-6.png: 27fff8f675d665dd788e68ed3085078ddd9d4be789c00921ea1fa406de91e37f
        A/table-images/page-7.png: 4a831d77cd0371ca0358f4c8ef0ddbffcfa72fe2912a8f633611a0f4c774b79b
        A/table-images/page-5.png: 1e87c62877536a656fc62c3ede6090ed2dfd3b3bd3fb50b495df2b2b1c96de4c
        A/table-images/page-9.png: 8800c56b6b57a83618d7a1b356391557b703ca47c6e5d5a33577ee7fb1439d7a
        A/table-images/TABLE-2-page-6-1.png: ffc8795102501c586db8871e5e97311982b4da5bbb0ba3d3fd54e67b41836819
        A/table-images/manifest.json: 73f7a50bf2c66b47e23a1346135c0e331ae049eafe30def28b2ce69a558ffe4e
        A/table-images/TABLE-6-page-9-3.png: b9301134f2bdc75ae26d2f8682ad6c5114bf136cc5f52423eed0e53af40467ff
        A/table-images/TABLE-3-page-7-1.png: 2fb0fc2bfa406307e4739d1dc95b80a1b80bf2f38d098a16c812c6fea243e2f7
        A/clauses/window-10/raw.json: 45082ec9026f39846add24ee4d7bab691f932bff1dceb014f01b7854f2cb0831
        A/clauses/window-10/prompt.txt: 0b03147b1313d0b9dd6ff0a899b909e2f4be8c8629e32090d1825bd24df7e0ee
        A/clauses/window-10/meta.json: ba087295052a861c5b35834a7d2749febfae6c63705e035c2822d27fb0bdd31d
        A/clauses/window-03/raw.json: bb2374a18c64f5ea03afbf2b0345aa47fd2e499d5439993e356b0e787d9907d7
        A/clauses/window-03/prompt.txt: 265f89fd5dd451251928def9ac9a945fd86657be263bbf2f2fb8417eee725157
        A/clauses/window-03/meta.json: 8ca093b6394aa07cde48e565f6cc1f86c79b1bcee5a14d187e4eadab64aa19e5
        A/clauses/window-04/raw.json: f015707f75af6b04a6322ca91769677254f91970b947b4e43647236d3578d163
        A/clauses/window-04/prompt.txt: cc77f308139621993722c9b8953c90854148be9e0db10f474513c0661c18a91c
        A/clauses/window-04/meta.json: 44eb1ba30947fb548c084a7994283835e7e179d265aefb8f4fb59b3ff98cfd85
        A/clauses/window-05/raw.json: ccdacb20fbaeb7207f2f68cd5c64f83d6af35e5a6c5112084990365c7207bf53
        A/clauses/window-05/prompt.txt: 91fe6c96dec0598466f5019d7bd54a9d5e0445b6caf62052c5b4d8117716ac9b
        A/clauses/window-05/meta.json: 3506c5971b3dd1b58b6eb62709419acad3786bf2503fac765d2307a9d680d66b
        A/clauses/window-02/raw.json: 9c9a61c6d715b190ba7cf6918d79b12a2ffa9791628627a80c95f8ed256883b1
        A/clauses/window-02/prompt.txt: b2e8837de85001dc4b6718e7f3370a307807673c325582ca85269331b989e0d9
        A/clauses/window-02/meta.json: 88ad9c5957a6a56395162a390b40619026ec2c834b59e75af527296467cd5a1d
        A/clauses/window-09/raw.json: 5ba280a70c0203fd6c9e8b3b5553756ee2a64dc4828f5b309a0bc73b66d45795
        A/clauses/window-09/prompt.txt: 21755e84e35e65ac9e27d2dd174c92cb63ad86ff74084138861e55ff5c40fab8
        A/clauses/window-09/meta.json: ca6dca0e8c515b9ace9851c81b80869bb36273e879e6d4486e7df68efbda6868
        A/clauses/window-07/raw.json: 26ec339b8499b322a1224cbbf974af9bac5a107fa49b3623483ba7f0707abefa
        A/clauses/window-07/prompt.txt: b5535f5904f38f9f51e61e13f9943ebcdd8cb6d77297df97493697564d877e6e
        A/clauses/window-07/meta.json: 95341533b065bacfa55e61bf189275c41ec5593ebbcefa9c49a6a190398bc312
        A/clauses/window-01/raw.json: a56c19f4628e00db20a20d8fb0ffa33ed3192c690962b19cf997eca8579311cc
        A/clauses/window-01/prompt.txt: 3f75e26ee7f802c5713a4a0aa97e5645d84d52277e798b9b7838443134a60f60
        A/clauses/window-01/meta.json: 5243e59532a391d683488f6b21d78fb68f25c0f0a30e4b5319dce5cf6a121212
        A/clauses/window-06/raw.json: c5e351261e7a5eb40cbf1775cad7b4a847500e87ed95c342971683d39df2ea3c
        A/clauses/window-06/prompt.txt: c18bee16fc25c97588d57ff048befc1321b0c084481adc75b34c3ff3f12a8070
        A/clauses/window-06/meta.json: 6a3190a2c6cad477073c794cd85817510c595eca418ce3f0f0de26c7bb74920d
        A/clauses/window-08/raw.json: 34e6096972d9fd5833de238bcae38a540d12ba5b97dc0de7de081570fb6c3ceb
        A/clauses/window-08/prompt.txt: 9bd23d7e661a1a84d075f765eb2c1a1ad2de9a68a0b9fc61fe1250a1fddc85f4
        A/clauses/window-08/meta.json: f8a681b6752194e09bdbc8403c200b1b36eb1492c5ec2032da9902b750d174a8
        A/tables/TABLE-1-page-5-1/raw.json: 153915bc21dcbc9d2a45226819055652d8ec8f8e98a1fb8717a5025ca8d1f335
        A/tables/TABLE-1-page-5-1/prompt.txt: 78a18d2d28251f2823d6411489783b96a9abd0a2093bd85abf54553bff67ba8a
        A/tables/TABLE-1-page-5-1/meta.json: 824afc3639d42ae6793bd3538e3c8c333c4552cb85bb085410acfb355dad6c35
        A/tables/TABLE-2-page-6-2/raw.json: 963322edc09b95522aba86a62d69d1110f3594503ea8e7fd3ae955339c544daa
        A/tables/TABLE-2-page-6-2/prompt.txt: c95e76bb9628de452e055cd77c34cf38e5ad92009f5456a0ccf56088ad496404
        A/tables/TABLE-2-page-6-2/meta.json: 8d1186a4beff400c626252615fc6728d5c03ea7cd8160cd428f7c72497ce56df
        A/tables/TABLE-3-page-7-3/raw.json: a64ae6d268ec85716d9e6a521d92a8c7724fe9e4629e521cc63d755a756d7db0
        A/tables/TABLE-3-page-7-3/prompt.txt: aa482171ff21b6ff18f6b41fbc8994e68108a3e388210183bde1aaac7bef501b
        A/tables/TABLE-3-page-7-3/meta.json: bfb2988fa9307855b1125a26fd0e5b145bc4641318e256e01eceba539d27dfb7
        A/tables/TABLE-5-page-9-5/raw.json: 628d3ad73c7dee63b4807c93845fe1f42af0b6e685cf0666270230aad466fcdc
        A/tables/TABLE-5-page-9-5/prompt.txt: 7312fd2da1bb75e9d6eb40a9391e6435bbbffc7bb8c77ee50b1a1ba25779f14a
        A/tables/TABLE-5-page-9-5/meta.json: 22ccd79bb39a0f89fa0a741ec1e474d1443d7021b684de1919bb3fd7a4627259
        A/tables/TABLE-4-page-9-4/raw.json: 3f0830ac8de694d8111909b2e837cd8a2fc0818802a13b2e834fcc0fa8e0cd73
        A/tables/TABLE-4-page-9-4/prompt.txt: f935d1e91ca282bd51724e0b896791964f36f588299c9a030120cd570dec1bf3
        A/tables/TABLE-4-page-9-4/meta.json: 70348076d72a1e2d8b0a87da819248e9169d1238456ae231bef8eb7e899ef9fb
        A/tables/TABLE-6-page-9-6/raw.json: 5ee1ac4ae7cefb4342509dbe68fd1c7d26238939f5063a3d3ee740538e3c0de7
        A/tables/TABLE-6-page-9-6/prompt.txt: 84d24c7a9bfeee2f02a83c6fadc610478a16ef1da20c9ac1a81c17c015fce438
        A/tables/TABLE-6-page-9-6/meta.json: cafb194c43ea89930043cd9f6208595fdeaa5962293fc4e03354ef7ee41debb7
        B/passages.json: 024247056c296c4b91a4495a69a6f6f8101bffed48993ef901c25010e5b10cab
        B/raw.json: c20bee7af91b020eb2ecdb3a7ae4df6abb6f43d923511ba00505451ee23e2759
        B/source-units.json: 9169078814ecb6194e142e3e513894a6d08aea855ff7b35dcb9f84609a0ce970
        B/full-source-units.json: 96e7b7371c5212d0ff5c064d3425e9ca55add9a7bd43b594cd10f796bfc673a0
        B/meta.json: 400a3446a4c5407ba56a1d32ef9c9638193d76cd4cb06b5b46afadefb7f7015d
        B/table-images/TABLE-5-page-9-2.png: 1ef6a2901109353005ecfd00fd7cc9e57daf30cf05c771f96711a62b2b74a270
        B/table-images/TABLE-1-page-5-1.png: 4ac269b112ff01190acdc1c749082b50c8ba9450b2c4b890671eb48df847fda8
        B/table-images/TABLE-4-page-9-1.png: c991c7e57cd7bd84b0d73c265b5940e7f6d17902a4eabc8a2c0c10a71c50b1b6
        B/table-images/page-6.png: 27fff8f675d665dd788e68ed3085078ddd9d4be789c00921ea1fa406de91e37f
        B/table-images/page-7.png: 4a831d77cd0371ca0358f4c8ef0ddbffcfa72fe2912a8f633611a0f4c774b79b
        B/table-images/page-5.png: 1e87c62877536a656fc62c3ede6090ed2dfd3b3bd3fb50b495df2b2b1c96de4c
        B/table-images/page-9.png: 8800c56b6b57a83618d7a1b356391557b703ca47c6e5d5a33577ee7fb1439d7a
        B/table-images/TABLE-2-page-6-1.png: ffc8795102501c586db8871e5e97311982b4da5bbb0ba3d3fd54e67b41836819
        B/table-images/manifest.json: 66a3ed5403578d0e7b0956f34e0b5f814107e5d77ca233b4ed4abd571376261d
        B/table-images/TABLE-6-page-9-3.png: b9301134f2bdc75ae26d2f8682ad6c5114bf136cc5f52423eed0e53af40467ff
        B/table-images/TABLE-3-page-7-1.png: 2fb0fc2bfa406307e4739d1dc95b80a1b80bf2f38d098a16c812c6fea243e2f7
        B/clauses/window-10/raw.json: 7eeea88bbf0c1ac7b3dd4c4cc9525e1b54af44b5714ecd993aee22ae7f3d8168
        B/clauses/window-10/prompt.txt: 0b03147b1313d0b9dd6ff0a899b909e2f4be8c8629e32090d1825bd24df7e0ee
        B/clauses/window-10/meta.json: a3590fccfcd215bee25f48563b5232dab9d8ace6c9e8d44464898cd407c79fee
        B/clauses/window-03/raw.json: 4f771630a59918adb6b3ca40371b8f656843cf44cfd6d4dc6fe7834e89072aad
        B/clauses/window-03/prompt.txt: 265f89fd5dd451251928def9ac9a945fd86657be263bbf2f2fb8417eee725157
        B/clauses/window-03/meta.json: 231a08b1ebe29beb99dc9cf0130b69071d599186af94b4a141ed4bbb2e2e336f
        B/clauses/window-04/raw.json: 3537c35d103a13afa78405ac16f2f886da1f2ff74c6f69ae9cbdfc7c0bdb379a
        B/clauses/window-04/prompt.txt: cc77f308139621993722c9b8953c90854148be9e0db10f474513c0661c18a91c
        B/clauses/window-04/meta.json: 0134463f21243760a2a03407850d0087fd38d2ab7c5723a624efef7423dfdc0c
        B/clauses/window-05/raw.json: b217620a91b02179ed6280980c628de1b41e4bcbee0a51c1ae2d39a59c2f23d8
        B/clauses/window-05/prompt.txt: 91fe6c96dec0598466f5019d7bd54a9d5e0445b6caf62052c5b4d8117716ac9b
        B/clauses/window-05/meta.json: c337ee83dfbd919dcb83cb7ec773755110c8c9c3ed477d485cc5c4f78ec73dae
        B/clauses/window-02/raw.json: fd5417f91a902f996021a0534b309b0c5708410472ad9eb0d61f5020e16be863
        B/clauses/window-02/prompt.txt: b2e8837de85001dc4b6718e7f3370a307807673c325582ca85269331b989e0d9
        B/clauses/window-02/meta.json: 99353bb5176b372318a390e55fd2ae3e9eab78233277acedd1bca41cff9db824
        B/clauses/window-09/raw.json: 4f2d2c5c8d2c84eedb97c2ab2dfaf3c848cd816bb8b75905d226801d3449aa9e
        B/clauses/window-09/prompt.txt: 21755e84e35e65ac9e27d2dd174c92cb63ad86ff74084138861e55ff5c40fab8
        B/clauses/window-09/meta.json: 60427a74d057715e21a422fab22332b5b5b9934faa4b343f1abd4db93f1287db
        B/clauses/window-07/raw.json: de3ded26ef0e8a0f54b92d82620441c1549069924717180d10ad83bde97300ad
        B/clauses/window-07/prompt.txt: b5535f5904f38f9f51e61e13f9943ebcdd8cb6d77297df97493697564d877e6e
        B/clauses/window-07/meta.json: fb8ac1cc2f1f3ad629df8bf3480e13d7ef6dd955012c240b20defe2894b1039b
        B/clauses/window-01/raw.json: 66b0babb5b133d082bca565a13442df21d77ca2de9702a397c92439189bf6e17
        B/clauses/window-01/prompt.txt: 3f75e26ee7f802c5713a4a0aa97e5645d84d52277e798b9b7838443134a60f60
        B/clauses/window-01/meta.json: 0da03b9ecaa1eb7139436843ad6b60c94ec6e781e5a3e8e7f83a1480b0294611
        B/clauses/window-06/raw.json: 0aef3edac11adbadd58d3ee8159b177f008457050c5ff8c52cb2b8d4e111df26
        B/clauses/window-06/prompt.txt: c18bee16fc25c97588d57ff048befc1321b0c084481adc75b34c3ff3f12a8070
        B/clauses/window-06/meta.json: 3abbebc6a5a37848bfe13e972308ff399ca3678cdc6013f50f70a35efae1c878
        B/clauses/window-08/raw.json: fdd610c04fc28a9e9d8f53731eae9b4d35764ecb56bf6183cdda4171c2e79621
        B/clauses/window-08/prompt.txt: 9bd23d7e661a1a84d075f765eb2c1a1ad2de9a68a0b9fc61fe1250a1fddc85f4
        B/clauses/window-08/meta.json: 69363afcb75da9b57a62ecd627954bf4e012c441967ce2e38fa9717b7bd1329d
        B/tables/TABLE-1-page-5-1/raw.json: 30c5e8b0dd4cf66d9154cdca68ee545063ed3389aad7d3d5bb527477e43056e7
        B/tables/TABLE-1-page-5-1/prompt.txt: 78a18d2d28251f2823d6411489783b96a9abd0a2093bd85abf54553bff67ba8a
        B/tables/TABLE-1-page-5-1/meta.json: 38d87db60dadfeae930043ed0a18486d412f11c6279022279bb13680e53632c0
        B/tables/TABLE-2-page-6-2/raw.json: 302cb2066fe182296025444ba7221c7dffaa90f7015b0aa021ac760e185b42a0
        B/tables/TABLE-2-page-6-2/prompt.txt: c95e76bb9628de452e055cd77c34cf38e5ad92009f5456a0ccf56088ad496404
        B/tables/TABLE-2-page-6-2/meta.json: 20a5a04980c07171f8fc6e6c59ffb990580b1a846c83ab996e7abdc12077bee7
        B/tables/TABLE-3-page-7-3/raw.json: a64ae6d268ec85716d9e6a521d92a8c7724fe9e4629e521cc63d755a756d7db0
        B/tables/TABLE-3-page-7-3/prompt.txt: aa482171ff21b6ff18f6b41fbc8994e68108a3e388210183bde1aaac7bef501b
        B/tables/TABLE-3-page-7-3/meta.json: 82bdbef07ef213893ffb900c49358ad1c30ca761612203bf50ef3c185ae53471
        B/tables/TABLE-5-page-9-5/raw.json: 7f01fc7a04329814e38054f3bb65bfae94ee3a9ca7c1c7287691210d21e937cb
        B/tables/TABLE-5-page-9-5/prompt.txt: 7312fd2da1bb75e9d6eb40a9391e6435bbbffc7bb8c77ee50b1a1ba25779f14a
        B/tables/TABLE-5-page-9-5/meta.json: ec1673c9ea5e06189826ad973608b33ffce9e9b9d33ec29bf2502ba30e69c636
        B/tables/TABLE-4-page-9-4/raw.json: 29eedde7c7bd3670d791d01b080b0c3a34f9889ae6af144b6acd5f99b552384b
        B/tables/TABLE-4-page-9-4/prompt.txt: f935d1e91ca282bd51724e0b896791964f36f588299c9a030120cd570dec1bf3
        B/tables/TABLE-4-page-9-4/meta.json: d419eedd4bde5cc13abb95d900e46c67a0cd1f5cf8404c5c405f45f1ac2dbf4d
        B/tables/TABLE-6-page-9-6/raw.json: 0871d5137ab02e54588e92df3aeaab9b3878b5d38a4d2cc223d68f32cea24bae
        B/tables/TABLE-6-page-9-6/prompt.txt: 84d24c7a9bfeee2f02a83c6fadc610478a16ef1da20c9ac1a81c17c015fce438
        B/tables/TABLE-6-page-9-6/meta.json: 30095d02b26ac2b0a58d7df0a9a427a597712ced31f3ea253052b601e91b5742
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
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      source_review: _compare/relationships-2026-11-16/review-current/Saur2006
      source_status_sha256: 97312e29896d114da14b6d2890a4fe4454d73470c136b430174ce489f8a922c3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: chronic stage (Ex3)
    outcome:
      text: language activation
    analysis_label: Chronic phase patient-control comparison
    relation: association
    evidence_ids:
    - P6-S1-C10
    - P7-S2-C2
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
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      source_review: _compare/relationships-2026-11-16/review-current/Saur2006
      source_status_sha256: 97312e29896d114da14b6d2890a4fe4454d73470c136b430174ce489f8a922c3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P3-S1-C12
      - Result passage disposed without unit P3-S1-C9
      - Result passage disposed without unit P4-S2-C11
      - Result passage disposed without unit P4-S2-C12
      - Result passage disposed without unit P4-S3-C3
      - Result passage disposed without unit P4-S3-C4
      - Result passage disposed without unit P4-S3-C5
      - Result passage disposed without unit P4-S3-C6
      - Result passage disposed without unit P4-S3-C7
      - Result passage disposed without unit P4-S3-C12
      - Result passage disposed without unit P4-S3-C13
      - Result passage disposed without unit P4-S3-C14
      - Result passage disposed without unit P4-S3-C15
      - Result passage disposed without unit P4-S3-C8
      - Accounting without a linked unit P5-S1-C1
      - Unaccounted source passage P5-S1-C1
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P5-S1-C5
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P10-S1-C13
      - Result passage disposed without unit P10-S1-C14
      - Result passage disposed without unit P10-S1-C15
      - Result passage disposed without unit P10-S2-C2
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C11
      - Accounting without a linked unit P11-S1-C12
      - Result passage disposed without unit P11-S2-C3
      - Unaccounted source passage P11-S1-C12
      - Result passage disposed without unit P12-S2-C11
      - Accounting without a linked unit P12-S2-C12
      - Result passage disposed without unit P12-S3-C3
      - Result passage disposed without unit P12-S3-C4
      - Unaccounted source passage P12-S2-C12
      - Accounting without a linked unit P13-S1-C4
      - Accounting without a linked unit P13-S1-C5
      - Unaccounted source passage P13-S1-C4
      - Unaccounted source passage P13-S1-C5
      unattached_null_or_qualifier_ids:
      - P4-S3-C14
      - P6-S1-C1
      - P11-S1-C10
      - P11-S1-C11
      - P11-S2-C3
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 214
      unselected_timing_passages:
      - P2-S2-C5
      - P2-S2-C7
      - P2-S2-C8
      - P4-S2-C4
      - P4-S2-C5
      - P12-S3-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P8-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P4-S1-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P4-S1-C12
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P10-S2-C3
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P10-S2-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S3-C2
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P11-S2-C8
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      - TABLE-4-page-9-4
      - TABLE-5-page-9-5
      - TABLE-6-page-9-6
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      - TABLE-4-page-9-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S3
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S1
        - P8-S1
        - P9-S1
        - P10-S2
        - P11-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      source_review: _compare/relationships-2026-11-16/review-current/Saur2006
      source_status_sha256: 97312e29896d114da14b6d2890a4fe4454d73470c136b430174ce489f8a922c3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general clinical recovery of patients.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Describes activation in acute and subacute phases.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Describes increase of activation between acute and subacute phases.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 16
      reason: Correlates improved language function with increased activation.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Describes activation in chronic phase.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes feasibility of the task paradigm.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes task modification for patients.
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes DWI sequence utility for masking.
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes infarct location.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes infarct location.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes infarct location.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes vessel occlusion.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes thrombolysis treatment.
    - source_id: P4-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes recanalization.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes vessel flow.
    - source_id: P4-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes vessel occlusion.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes handedness.
    - source_id: P4-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes handedness.
    - source_id: P4-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group task performance.
    - source_id: P4-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia types at admission.
    - source_id: P4-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia recovery status.
    - source_id: P4-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes LRS in acute phase.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes LRS improvement over time.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes LRS differences across examinations.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy and control group activation.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group activation areas.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group activation areas.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Describes acute phase activation.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Describes subacute phase activation.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Describes chronic phase activation.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Describes increase of activation from acute to subacute.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Describes decrease of activation from subacute to chronic.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Describes increase of activation from acute to chronic.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null findings for specific comparisons.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Compares controls and patients in acute phase.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Compares controls and patients in subacute phase.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Compares controls and patients in chronic stage.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Identifies peak voxels for analysis.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Describes monophasic and biphasic activation curves.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports ANOVA interaction for regional activation.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reports regional activation differences across phases.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Reports significant early increase in regions.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Reports significant late increase in regions.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 13
      reason: Reports significant decrease in regions.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Reports results after Bonferroni-Holm correction.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 7
      - 8
      - 9
      reason: Reports t-test comparisons between controls and patients.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Reports correlation between LRSEx1 and activation.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Reports null correlations in subacute and chronic stages.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Reports significant correlation for early relative improvement.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 16
      reason: Specifies regions for early improvement correlation.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 17
      reason: Reports correlation for early absolute improvement.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of three phases of recovery.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement of acute phase activation.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes LRS in acute phase.
    - source_id: P10-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of subacute phase upregulation.
    - source_id: P10-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes language improvement.
    - source_id: P10-S1-C14
      disposition: represented
      result_indexes:
      - 2
      reason: Restatement of chronic phase normalization.
    - source_id: P10-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes language improvement in chronic stage.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Restatement of monophasic and biphasic courses.
    - source_id: P11-S1-C12
      disposition: represented
      result_indexes:
      - 14
      reason: Restatement of LRSEx1 correlation.
    - source_id: P12-S1-C3
      disposition: represented
      result_indexes:
      - 16
      reason: Restatement of early improvement correlation.
    unresolved_coverage:
    - source_id: P8-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C3
    - P3-S1-C9
    - P3-S1-C12
    - P3-S3-C2
    - P4-S2-C11
    - P4-S2-C12
    - P4-S3-C3
    - P4-S3-C4
    - P4-S3-C5
    - P4-S3-C6
    - P4-S3-C7
    - P4-S3-C8
    - P4-S3-C10
    - P4-S3-C11
    - P4-S3-C12
    - P4-S3-C13
    - P4-S3-C14
    - P4-S3-C15
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P7-S1-C2
    - P7-S1-C6
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C8
    - P9-S1-C1
    - P9-S1-C6
    - P10-S1-C2
    - P10-S1-C9
    - P10-S1-C11
    - P10-S1-C13
    - P10-S1-C15
    - P10-S1-C16
    - P10-S2-C2
    - P11-S1-C1
    - P11-S1-C10
    - P11-S1-C11
    - P11-S2-C3
    - P11-S2-C4
    - P12-S2-C11
    - P12-S2-C12
    - P12-S3-C3
    - P12-S3-C4
    - P13-S1-C2
    - P13-S1-C4
    - P13-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    - TABLE-4-page-9-4
    - TABLE-5-page-9-5
    - TABLE-6-page-9-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C5
      - P4-S2-C4
      recruited_sample:
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C9
      eligibility:
      - P2-S2-C6
      - P2-S2-C7
      - P2-S2-C8
      - P3-S1-C15
      imaging_provenance:
      - P3-S2-C5
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C14
      - P5-S2-C3
      imaging_timing:
      - P2-S4-C1
      - P2-S4-C2
      - P4-S2-C10
      outcome_timing:
      - P2-S4-C1
      - P2-S4-C2
      outcome_definition:
      - P2-S3-C10
      - P2-S3-C11
      - P4-S1-C11
      validation: []
      analysis_restrictions:
      - P3-S3-C13
      - P4-S1-C14
      - P4-S2-C3
      dependent_variable_statement:
      - P4-S1-C9
      - P4-S1-C12
      - P7-S2-C3
      limitations:
      - P12-S3-C6
      - P12-S3-C7
      - P12-S3-C8
      - P12-S3-C9
      personal_factors: []
      tested_personal_effects:
      - P7-S2-C4
      - P8-S1-C6
      - P8-S1-C7
      adjustment_roles:
      - P3-S3-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C10
      - P4-S2-C4
      - P4-S2-C5
      - P4-S3-C10
      - P4-S3-C13
      - P5-S2-C1
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P8-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P4-S1-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P4-S1-C12
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P10-S2-C3
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P10-S2-C6
      reason: No current-result classification; a covariate description is not an
        individual test
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
      pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
      review_sha256: 62f2029b8c3c7c439c1d6c00c11eb6280d30f7de8dde5ca4a7dcdcc0940f79bb
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
      - P6-S1-C10
      - P7-S2-C2
      source_result: The comparison of controls and patients in the chronic stage
        (Ex3) did not show any significant differences in language-specific activation
        (P6-S1-C10). Specifically, post hoc two-sample t-tests of controls and patients
        at the chronic stage revealed no significant differences in the depicted voxels
        (P7-S2-C2).
      result_status: not_detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the patient-control comparison at the chronic
            stage (Ex3). The source explicitly describes this comparison in P6-S1-C10
            and P7-S2-C2, confirming the identity of the analysis as a two-sample
            t-test comparing controls and patients at Ex3.
          source_ids:
          - P6-S1-C10
          - P7-S2-C2
          - P4-S1-C5
        direction:
          answer: fits
          reason: The source states that the comparison 'did not show any significant
            differences' (P6-S1-C10) and 'revealed no significant differences' (P7-S2-C2).
            The proposed draft correctly characterizes this as a 'no_effect' (null
            result) in the direction field, meaning no statistically detected association/difference,
            which aligns with the source's null finding.
          source_ids:
          - P6-S1-C10
          - P7-S2-C2
        construct:
          answer: fits
          reason: The exposure is the chronic stage (Ex3), and the outcome is language
            activation. The measurement is fMRI activation (functional_imaging), specifically
            the contrast of intelligible speech vs reversed speech. The source confirms
            this method and timing (P2-S4-C2, P3-S3-C14). The patient measurement
            is correctly identified as functional imaging, not diffusion or lesion
            overlap.
          source_ids:
          - P2-S4-C2
          - P3-S3-C14
          - P6-S1-C10
        qualifications:
          answer: fits
          reason: The draft includes the statistical threshold (P < 0.001 uncorrected)
            as a qualification, which is supported by P4-S1-C14. It also includes
            limitations regarding the highly selected patient group (P11-S1-C4, P12-S3-C7).
            These qualifiers are appropriate for this specific analysis.
          source_ids:
          - P4-S1-C14
          - P11-S1-C4
          - P12-S3-C7
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key limitations regarding the selectivity
            of the patient group and the statistical threshold used. No material caveats
            that would change the interpretation of the null result are omitted. The
            null result is a standalone finding for this specific comparison.
          source_ids:
          - P11-S1-C4
          - P12-S3-C7
          - P4-S1-C14
      optional_pending:
      - Sample size for the chronic stage comparison specifically (though total N=14
        patients and N=14 controls is mentioned, the exact N for Ex3 might vary due
        to dropouts, but P4-S2-C5 mentions 14 recruited, and P4-S2-C6 mentions dropouts,
        so N might be less than 14 for Ex3. This is a minor detail not critical for
        the qualitative draft but noted as pending.)
      - Exact coordinates of the non-significant regions are not transcribed, which
        is acceptable for a qualitative draft.
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
    - Sample size for the chronic stage comparison specifically (though total N=14
      patients and N=14 controls is mentioned, the exact N for Ex3 might vary due
      to dropouts, but P4-S2-C5 mentions 14 recruited, and P4-S2-C6 mentions dropouts,
      so N might be less than 14 for Ex3. This is a minor detail not critical for
      the qualitative draft but noted as pending.)
    - Exact coordinates of the non-significant regions are not transcribed, which
      is acceptable for a qualitative draft.
    normalizations:
    - field: sample.n
      original: 28
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: Chronic stage (mean 321 days post-stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 321'
    analysis_identity:
      id: R010
      exposure:
        text: chronic stage (Ex3)
      outcome:
        text: language activation
      analysis_label: Chronic phase patient-control comparison
      relation: association
      evidence_ids:
      - P6-S1-C10
      - P7-S2-C2
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
        pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
        source_review: _compare/relationships-2026-11-16/review-current/Saur2006
        source_status_sha256: 97312e29896d114da14b6d2890a4fe4454d73470c136b430174ce489f8a922c3
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 603c02bb295e412bbc3b49b570298b9b7450a207d6ebdd8e52df1550c3723060
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C5
          page: 4
          text_layer_sha256: 603c02bb295e412bbc3b49b570298b9b7450a207d6ebdd8e52df1550c3723060
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'From a total of 198 consecutively screened aphasic

          stroke patients, 14 met our inclusion criteria and were

          recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

          11 male and three female].'
        anchor_text: 'From a total of 198 consecutively screened aphasic

          stroke patients, 14 met our inclusion criteria and were

          recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

          11 male and three female].'
        excluded_fragments: []
        image_sha256: 48157297be6811c78d484044e996fb7738c347b041502855a818aea89186ec2c
        transcription: '. From a total of 198 consecutively screened aphasic

          stroke patients, 14 met our inclusion criteria and were

          recruited [range: 16–68 years, mean (SD): 51.9 (14.2),

          11 male and three female]'
      P4-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3a3552c29e69e568c77b37ebe2a7272ad83f96b24c0ae29af092e5a624f0f6b1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C4
          page: 4
          text_layer_sha256: 3a3552c29e69e568c77b37ebe2a7272ad83f96b24c0ae29af092e5a624f0f6b1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results

          Clinical data

          The control group comprised 11 male and three female sub-

          jects, aged between 18 and 66 years [mean (SD): 48.6 (13.9)

          years].'
        anchor_text: 'Results

          Clinical data

          The control group comprised 11 male and three female sub-

          jects, aged between 18 and 66 years [mean (SD): 48.6 (13.9)

          years].'
        excluded_fragments: []
        image_sha256: ba2e0ca3d55b610aa852c96546e05f604f32dc399cd9b4917481d20c4be020c4
        transcription: 'Results

          Clinical data

          The control group comprised 11 male and three female subjects, aged between
          18 and 66 years [mean (SD): 48.6 (13.9) years]'
      P2-S4-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bb2b3d3c1b886a5115949b3008e5666374c01d73caa87f5d8585376839ec59ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 383e52624e981d613c875b6c0b9f59634078b66d88912341f2f72e69e1d51a92
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C2
          page: 2
          text_layer_sha256: 383e52624e981d613c875b6c0b9f59634078b66d88912341f2f72e69e1d51a92
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "A follow-up examina-\ntion in the chronic stage was carried\
          \ out \x024–12 months post-stroke\n(Ex3, mean: 321 dps)."
        anchor_text: "A follow-up examina-\ntion in the chronic stage was carried\
          \ out \x024–12 months post-stroke\n(Ex3, mean: 321 dps)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'The comparison of controls and patients in the chronic

    stage did not show any signiﬁcant differences (no ﬁgure,

    Table 6).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
