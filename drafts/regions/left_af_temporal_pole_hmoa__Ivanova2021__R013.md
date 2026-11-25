---
id: left_af_temporal_pole_hmoa
name: left AF temporal pole cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: naming
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: naming
  target_kind: impairment
  claim: Residual integrity of the left AF temporal pole branch, as measured by HMOA,
    significantly contributes to naming performance on the BNT beyond the effect of
    lesion load to frontal, temporal, and parietal cortical language areas.
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 33
    population: individuals with chronic aphasia following left hemisphere stroke
    phase: not_reported
    time_post_onset: chronic stage of stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Tract reconstructions were performed manually
  - Sample size is small (n=33)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Hindrance Modulated Orientation Anisotropy (HMOA)
    of the left arcuate fasciculus branch extending from the frontal lobe to the temporal
    pole, reconstructed via HARDI deterministic tractography using a modified Glasser
    and Rilling model. Analysis was performed using hierarchical regression; Adjusted
    for gender, time post-onset, and lesion load to frontal, temporal, and parietal
    cortical language areas. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S3-C11, two-model
    agreement, human verification pending): . In the last several years,

    a HARDI-diffusion-weighted imaging sequence has been added

    to our scanning protocol, yielding a group of thirty-three

    successively scanned participants with aphasia (PWA; 24 males, 9

    females) following a left hemisphere stroke (Mage = 63.7 1.4 years,

    from 40 to 83 years of age) Original text-layer quotation is preserved below.'
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
    - proposed_concept:naming
  citation: '@Ivanova2021'
  source_passages:
  - section: Original source P9-S2-C2
    page: 9
    quote: 'Here, only signiﬁcant contributions

      of the AF temporal pole normalized volume to naming scores

      on the WAB (Adj. R2 = 0.530, Sig. F Change = 0.028) and

      BNT (Adj. R2 = 0.493, Sig. F Change = 0.01), as well as the

      AF temporal pole HMOA to naming scores on the BNT (Adj.

      R2 = 0.497, Sig. F Change = 0.009) could be established.'
    supports: claim
  - section: Original source P6-S1-C8
    page: 6
    quote: 'Again, the size of the MTG

      ROI depended on the individual’s brain anatomy.

      • AF temporal pole – ﬁbers extending from the frontal lobe

      all the way to the anterior part of the temporal lobe, including

      the temporal pole, deﬁned by an Temporal Pole ROI and the

      Frontal ROI.'
    supports: method
  - section: Original source P6-S2-C1
    page: 6
    quote: 'Hindrance

      Modulated

      Orientation

      Anisotropy

      (HMOA, Dell’Acqua et al., 2013).'
    supports: method
  - section: Original source P8-S2-C2
    page: 8
    quote: 'In

      the ﬁrst step of this hierarchical regression analysis, lesion

      load to frontal, temporal, and parietal language areas along

      with gender and time post-onset were entered as covariates.'
    supports: method
  - section: Original source P3-S3-C11
    page: 3
    quote: 'In the last several years,

      a HARDI-diﬀusion-weighted imaging sequence has been added

      to our scanning protocol, yielding a group of thirty-three

      successively scanned participants with aphasia (PWA; 24 males, 9

      females) following a left hemisphere stroke (Mage = 63.7 1.4 years,

      from 40 to 83 years of age).'
    supports: sample
  - section: Original source P12-S1-C7
    page: 12
    quote: 'However, our study did not measure recovery over time, but

      rather correlated AF volume/HMOA directly to individuals’

      current language performance in the chronic stage of stroke

      across highly heterogenous post-onset times.'
    supports: method
  - section: Original source P4-S1-C8
    page: 4
    quote: 'To evaluate naming deﬁcits, the short form of the

      Boston Naming Test (BNT; Kaplan et al., 2001) was used.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Ivanova2021
  proposal_id: R013
  review_status_sha256: b5fa59bf9bfa4a0795395c3635c1891fa286b7bccfdb8a57417e11742439e753
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
        A/passages.json: de116c393d9f689fc36bf05c73c13dca9de9a036881d5c8942d19fa1ca92273f
        A/raw.json: c953365e8efa2e96a2cd367ab0defc0a44c5f1f449695a27a1073cce6043aa2f
        A/source-units.json: 9d4fd8411bdceb0293f8a21bc719c48e803e62d8423b3cf3a2ea0e2e988befdc
        A/full-source-units.json: 1874d5ea4291b27838594ceea34b4f5eb951baea3737c052cc5f16c2aa75c1bd
        A/meta.json: 88fdae70d39f6cfa26119b3d0dcc54c4f3ab9abc715f7a3a1456964f29c6a7d1
        A/table-images/TABLE-4-page-9-1.png: a5ebea3707953a6a8396628251372e273a87fc7005d70d28bd92c265712e5a8a
        A/table-images/page-10.png: 8c871ad6c4ba1f955b9204108e0aecca8baf2159849bd0927653fb3e4fe22501
        A/table-images/page-7.png: 43f36185426a305b3a737c4f9fbe0c45cbfefcfd5264a5c84ce5989142847a60
        A/table-images/page-4.png: a07a7e5b10df44755616b043ff0e118ae86c182efdf05a24fbe7a9b4a1f19a8e
        A/table-images/TABLE-1-page-4-1.png: cd6e3f02caf7ccc0fd757298f79fcd4628e758fdc4be1aa946295f6327263d37
        A/table-images/page-9.png: 6f37fb545429d5872765143e2c5068f5a6494500495e527a9e325915729caf4c
        A/table-images/manifest.json: dd583830f99748d931f1328d24740874f7246b7a52c86b7c396aeed842705889
        A/table-images/TABLE-3-page-7-2.png: d61420948e0450a7afe628d296542c37ccf232cc3205b0d8143f2c30cf2e3d8b
        A/table-images/TABLE-5-page-10-1.png: bb9744c5c7b3d3d6004e9340b517e83e89e7e04d21a81a71e368eadc328bd630
        A/table-images/TABLE-2-page-7-1.png: cbd6102405e43b3528421472f04e7a98e00479845b9154d0b0f8f29b26ebd2b8
        A/clauses/window-11/raw.json: 22783a295115bd2ff1eb6c33f3dfbc38377a037fad274b158e9d32210c00423d
        A/clauses/window-11/prompt.txt: 330618b958afb082e1894d2bc9b69ab3af64ff4e6b21b6e24a15090441b2f1bf
        A/clauses/window-11/meta.json: e80591af7d5d866426641bcc07878d96ca3286d5d2cee40ae81c6a9633728d3c
        A/clauses/window-10/raw.json: 2a8497ef32432cae7d2eb354d287d7723b9db47824bb8d3177bf179ab4169a7c
        A/clauses/window-10/prompt.txt: 769bacf07d1ff8d204d191b746acfd93c369e9a5e352e935919cf3ce938e4643
        A/clauses/window-10/meta.json: f2aefbac57d567a637fa6dcb8a19cff4f48f5b870f351d152bf1ff1d565bba61
        A/clauses/window-03/raw.json: c498ebecbed88d0deee27f3121afd91e116b75cc4e9846e0c56a9776987360fb
        A/clauses/window-03/prompt.txt: ba750bedb8c10b883db8bb0011d7ddddfe41dd619085b940149c6d049f8d22fe
        A/clauses/window-03/meta.json: 5c52741965d2ba5fe77353cd6cbca1cfaed004c3ec757b5772fe06e896b9cfc0
        A/clauses/window-04/raw.json: 5567aed0ecb18f1642b835163d4fbf502969184e405a62b1a6589b768ac5863c
        A/clauses/window-04/prompt.txt: 36ca2c68fe79f7f7adc3f457f85c7aeaff8379418ec7288a5d59d19857e7ae53
        A/clauses/window-04/meta.json: faaaee05b0f590aee449c978472b2713953f3f439162b90bd22304cd844a29d9
        A/clauses/window-05/raw.json: 5260a35f6196aeed3517d250842a402582b21738a0babc007c17cdc21e2d5f60
        A/clauses/window-05/prompt.txt: ea4782d413d1066b9e975cf30252cc4dfc8f50d417dd2481a22efb5bb5653541
        A/clauses/window-05/meta.json: 5a3289bf4965ccf099fc5229a1852a6b8dfb210c8adf956b0265e625b3e12288
        A/clauses/window-02/raw.json: 73d504c1babb20c5b6bba09f4ef43fa3873986289b8ce5b289e08c9d8064432d
        A/clauses/window-02/prompt.txt: de1dd423406ca12753e3fd29ab706322dd86be12140faab47b3f5cc70cd60ed3
        A/clauses/window-02/meta.json: 779ba2d8478812958ce469e574dcf0c833d36edfc73d7b645f7d573233d4b9e5
        A/clauses/window-09/raw.json: 217e2bb4b4a5ccf84c5123f71725dfaff8fd5542983bae90e96c461a80aa4410
        A/clauses/window-09/prompt.txt: 3f9a7f75429608995086fee54ba9861b3ca346b9a81e13421131d6ebdb2d80bd
        A/clauses/window-09/meta.json: 3e4dc862a72fda61dcb248ebc5f619e2c3e05e2722e722ef3c63c92b2ed45845
        A/clauses/window-07/raw.json: b266323f25e8a677e28d48eb115d3a5ab5ffb3b436c919c9cf386aba867e3073
        A/clauses/window-07/prompt.txt: 98533c5f918553cbc186ebf8f721bb8b087afa43004e6b501deb9f97dc92ae39
        A/clauses/window-07/meta.json: e638c11a7c4682fde0d2ea4a2a293552c624a04aa7e98bba1a513f67baaed43f
        A/clauses/window-01/raw.json: 3063a5266d711dcf0572e8bcf213c73d84f28463739e9a070819e712426348b0
        A/clauses/window-01/prompt.txt: 7bed00429771648abd7fae0a601a8addaabcc03bcebcc863f8f6c42db2679c1f
        A/clauses/window-01/meta.json: 0932a6b4f3caef9883df5189e0549984bf45b2f0c52c2b39735e68322b888756
        A/clauses/window-06/raw.json: c7999eb3f448fd0899ea71c7897d2d6d85012679639063a40a3ee2aaf9c6c565
        A/clauses/window-06/prompt.txt: 58ad3e871b4237780ef5d5c00f51c3bce54b935473a13e25ada287641b0aec93
        A/clauses/window-06/meta.json: 5589f3fcfb4a156491b181d65ba856b1ecdfb1e827fba882a142ca26e7117c79
        A/clauses/window-08/raw.json: 9bade308afa67c9e401f48013a246e2cafcb490b21e0962dcfb2159450662b29
        A/clauses/window-08/prompt.txt: d11feba04f7fda2cbced36dd49ef380e75a6b0b71366c7f505b88fc25e13ec47
        A/clauses/window-08/meta.json: 1fdf95790bf3553d31cba32b9ac19bd2c8c20b6363bcc76808a06c4521ac6e25
        A/tables/TABLE-5-page-10-5/raw.json: 43a47f4a60c5ec19deef059b80de0ca837bcf428c383eabcac51d056be6add69
        A/tables/TABLE-5-page-10-5/prompt.txt: cb9eb09d110333a3fa80f83a921772b538f614c70f2eca76188171907ffe80b6
        A/tables/TABLE-5-page-10-5/meta.json: 540a92c2e2cc00e05fe0f0af9e7c09bb901d8c53a281202c286b025155f38fd7
        A/tables/TABLE-3-page-7-3/raw.json: 7130b2ff0924566419cf17fe9d369e3868a9f01b61d28ac0ebca0ffb8d5e6bfe
        A/tables/TABLE-3-page-7-3/prompt.txt: 4ca08ceafa0746db7f122857161c6a891441d73a8cf6bfdcf148fa966bb47373
        A/tables/TABLE-3-page-7-3/meta.json: b908ebbd8de2a0ee0bbbfde782d4ee500760020dbf93c66f119621dbe4b2385d
        A/tables/TABLE-2-page-7-2/raw.json: 570d83975b716ab22fa93e7c0db865bd5d65fbabeb25eee0a00ce09e9807c326
        A/tables/TABLE-2-page-7-2/prompt.txt: 8806147b96cd754e0c1bde95b8b62ddf5ef22aa27548a37f8c677a4f28aeabfd
        A/tables/TABLE-2-page-7-2/meta.json: 90699474b1d5ce4a9055341318954c3ba188152eef1faef3a87f1c4d84b937c6
        A/tables/TABLE-1-page-4-1/raw.json: 204cb70e5a685388c32a89e21607c4e03551bb2af3797e5c423feda4b7282e68
        A/tables/TABLE-1-page-4-1/prompt.txt: cfbd0d6d3009566f8699496e4614766ce1f0c147d3bde5d6c742b46fec3bd43b
        A/tables/TABLE-1-page-4-1/meta.json: ef497418c00aa619e0dd03b1371860caf23f3801bca5467c095127eb154f06bb
        A/tables/TABLE-4-page-9-4/raw.json: ff56e72c071b92a275cfd94d7b3c4e3292ba99f8afafac7680c802aa522027a5
        A/tables/TABLE-4-page-9-4/prompt.txt: 00757513639b97411ac92fcbe59eaf77c8c6757c3e7dc6aebf4e38b291a62e2f
        A/tables/TABLE-4-page-9-4/meta.json: 36fb95b07d091cb64a6d68abb79fd527a752bfb306f2599a39d585c7d8615079
        B/passages.json: de116c393d9f689fc36bf05c73c13dca9de9a036881d5c8942d19fa1ca92273f
        B/raw.json: 5b9e48cb925905ebf6276f270d21f69b38e882e30a2e6f23950d7d4e7e23667c
        B/source-units.json: 9d4fd8411bdceb0293f8a21bc719c48e803e62d8423b3cf3a2ea0e2e988befdc
        B/full-source-units.json: 1874d5ea4291b27838594ceea34b4f5eb951baea3737c052cc5f16c2aa75c1bd
        B/meta.json: a25549763f2b3078e867814cb84c1061dd33277775bc123915176a981187a4d9
        B/table-images/TABLE-4-page-9-1.png: a5ebea3707953a6a8396628251372e273a87fc7005d70d28bd92c265712e5a8a
        B/table-images/page-10.png: 8c871ad6c4ba1f955b9204108e0aecca8baf2159849bd0927653fb3e4fe22501
        B/table-images/page-7.png: 43f36185426a305b3a737c4f9fbe0c45cbfefcfd5264a5c84ce5989142847a60
        B/table-images/page-4.png: a07a7e5b10df44755616b043ff0e118ae86c182efdf05a24fbe7a9b4a1f19a8e
        B/table-images/TABLE-1-page-4-1.png: cd6e3f02caf7ccc0fd757298f79fcd4628e758fdc4be1aa946295f6327263d37
        B/table-images/page-9.png: 6f37fb545429d5872765143e2c5068f5a6494500495e527a9e325915729caf4c
        B/table-images/manifest.json: 44c28dacbe9744b0078f8c7b5a08f65d42666d99a2faeea28891914dffff9985
        B/table-images/TABLE-3-page-7-2.png: d61420948e0450a7afe628d296542c37ccf232cc3205b0d8143f2c30cf2e3d8b
        B/table-images/TABLE-5-page-10-1.png: bb9744c5c7b3d3d6004e9340b517e83e89e7e04d21a81a71e368eadc328bd630
        B/table-images/TABLE-2-page-7-1.png: cbd6102405e43b3528421472f04e7a98e00479845b9154d0b0f8f29b26ebd2b8
        B/clauses/window-11/raw.json: 266148b0d5afa9527961b3e1044d6ce5ee03bb2c5bd7e5e72d6ce1ada37e0230
        B/clauses/window-11/prompt.txt: 330618b958afb082e1894d2bc9b69ab3af64ff4e6b21b6e24a15090441b2f1bf
        B/clauses/window-11/meta.json: 957560a67d24857b858f379052247533b6163834bc9d40c3bf5c858dc7031558
        B/clauses/window-10/raw.json: f4c0cd26672f51a4b7e6ee3c3237ac5741ac530450508cffc95cf267cd7c1bf2
        B/clauses/window-10/prompt.txt: 769bacf07d1ff8d204d191b746acfd93c369e9a5e352e935919cf3ce938e4643
        B/clauses/window-10/meta.json: e75c0d99066f2d8483f3180b672c064609c0d4e67caf967bb01719212c22aa2c
        B/clauses/window-03/raw.json: 27c261a87230ad067ef4a0a58a4ecccd752170d4546059fca77c0750abe90f41
        B/clauses/window-03/prompt.txt: ba750bedb8c10b883db8bb0011d7ddddfe41dd619085b940149c6d049f8d22fe
        B/clauses/window-03/meta.json: 7b9694367c3daa46a73e0de8b36fde50b5f6d32fd5dbf11a9c26a5e42ff543a4
        B/clauses/window-04/raw.json: 4b423d207eccd9ceb66b0ceb6e076aed9e21bf5ed4b31485a897a332ecfc212d
        B/clauses/window-04/prompt.txt: 36ca2c68fe79f7f7adc3f457f85c7aeaff8379418ec7288a5d59d19857e7ae53
        B/clauses/window-04/meta.json: 73ab2f58e778dd525792216831c7e1533933bea2e34691703fb35b25b318e63b
        B/clauses/window-05/raw.json: c480cc6123679db2893097115a343b8c29ef1c9d1afbefb3c8c2e6b54bb9f68b
        B/clauses/window-05/prompt.txt: ea4782d413d1066b9e975cf30252cc4dfc8f50d417dd2481a22efb5bb5653541
        B/clauses/window-05/meta.json: 0e81cba22dd17aa877818563287c3b209bd9a1ba47ba3c72c5d0f16a5f08793f
        B/clauses/window-02/raw.json: fd53123654ca0f2d2ab2923150c2f7aca5b673fa2a8b7b8de912097bc04f5bd5
        B/clauses/window-02/prompt.txt: de1dd423406ca12753e3fd29ab706322dd86be12140faab47b3f5cc70cd60ed3
        B/clauses/window-02/meta.json: 9983a3fbbb45fa3f378f856ca9e34d943b9bfd5b8451df692ef27aec3594a971
        B/clauses/window-09/raw.json: 70ae5f1c53e4388745767000de60e9468353dca3429b9f5438f098491b4e9d56
        B/clauses/window-09/prompt.txt: 3f9a7f75429608995086fee54ba9861b3ca346b9a81e13421131d6ebdb2d80bd
        B/clauses/window-09/meta.json: d8285f14c5c176262d88a5824ffb5c2b2151513c98c28f5102eb5f12ab1218fa
        B/clauses/window-07/raw.json: 0e6ba2e458fb2675ff06396b8e4ca8e4db9cee97fa1a63f72a69cf2c6d52acb4
        B/clauses/window-07/prompt.txt: 98533c5f918553cbc186ebf8f721bb8b087afa43004e6b501deb9f97dc92ae39
        B/clauses/window-07/meta.json: 5a36fb2ff529aeb9a271dce035adbae863dc8ca6e1198c505e163fbec0b5bfe3
        B/clauses/window-01/raw.json: a4beaa2dc4e853241a7be440b2a10844e0a2abd02ca882154cbf96646b82f51b
        B/clauses/window-01/prompt.txt: 7bed00429771648abd7fae0a601a8addaabcc03bcebcc863f8f6c42db2679c1f
        B/clauses/window-01/meta.json: 7cd48b09422574b60653d261fc1e1b63a3c2cf0197f866ac2fe1daf847364bb9
        B/clauses/window-06/raw.json: 5ca95cfa514740ee624233ed7de2b14033a59dada6d8b626d225b178cccbf9b1
        B/clauses/window-06/prompt.txt: 58ad3e871b4237780ef5d5c00f51c3bce54b935473a13e25ada287641b0aec93
        B/clauses/window-06/meta.json: f91222856b96b71d3b74005b0e442f005ed437d9aee5bfd66c3b957a084a2291
        B/clauses/window-08/raw.json: 2eab592b2cced428a45138745a22ce48cfc64b18b4a8dac704f02736d4662b6c
        B/clauses/window-08/prompt.txt: d11feba04f7fda2cbced36dd49ef380e75a6b0b71366c7f505b88fc25e13ec47
        B/clauses/window-08/meta.json: a6d7034f564fc0718a3b39b62952ed8f080e1c77cc7196cf9536878db37b8003
        B/tables/TABLE-5-page-10-5/raw.json: 050940c7e461ece87ab0051653b6429fd1a5a93ae9bae87b8105051243c33279
        B/tables/TABLE-5-page-10-5/prompt.txt: cb9eb09d110333a3fa80f83a921772b538f614c70f2eca76188171907ffe80b6
        B/tables/TABLE-5-page-10-5/meta.json: c1f6786a237a1677927683ab61505c7a114576dfc34ba7071f90d2732c79d929
        B/tables/TABLE-3-page-7-3/raw.json: 2cc6ee639baaf4fb2e19ed680e2e093a7ee474038a9916fa1ec8aa4863dcc0dd
        B/tables/TABLE-3-page-7-3/prompt.txt: 4ca08ceafa0746db7f122857161c6a891441d73a8cf6bfdcf148fa966bb47373
        B/tables/TABLE-3-page-7-3/meta.json: ef5e82b6116b25d89c2074c28e9d24b6b3c6e469f5e320c513536671705d4f5c
        B/tables/TABLE-2-page-7-2/raw.json: 5d1a7e57aa1bb31cfb95a84923c9af9d1e59758740e8688a1684b46c49d58d07
        B/tables/TABLE-2-page-7-2/prompt.txt: 8806147b96cd754e0c1bde95b8b62ddf5ef22aa27548a37f8c677a4f28aeabfd
        B/tables/TABLE-2-page-7-2/meta.json: 4812ac53837b2fa7d9bd6df4501dcd57c39e00418f13803105c56ca2c47e9e99
        B/tables/TABLE-1-page-4-1/raw.json: 50eef587d7ef65ba21018b647451c7f3f7cb9ac1cefaa4dd4b6ef1cd4d121416
        B/tables/TABLE-1-page-4-1/prompt.txt: cfbd0d6d3009566f8699496e4614766ce1f0c147d3bde5d6c742b46fec3bd43b
        B/tables/TABLE-1-page-4-1/meta.json: 352d0c5d659638cf502ba0d48fa92233308122422b3572809bc4daf17eb2933a
        B/tables/TABLE-4-page-9-4/raw.json: b377bb900fa696425a78dce758a0e50c2e3a20f7207f3f54374a7708f680febe
        B/tables/TABLE-4-page-9-4/prompt.txt: 00757513639b97411ac92fcbe59eaf77c8c6757c3e7dc6aebf4e38b291a62e2f
        B/tables/TABLE-4-page-9-4/meta.json: 29ae401eed7fc501b6cc981020523faa4d68ad60bc583ec076b91cbf5e46d3c2
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
      pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2021
      source_status_sha256: ca785c0c88f6e8ff27acc34f64a96af478c5770a18641d4761ccf5d8a2992245
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: Left AF temporal pole HMOA
    outcome:
      text: naming (BNT)
    analysis_label: Hierarchical Regression (Glasser and Rilling Model)
    relation: sensitivity
    evidence_ids:
    - P9-S2-C2
    qualifier_ids:
    - P9-S1-C5
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2021
      source_status_sha256: ca785c0c88f6e8ff27acc34f64a96af478c5770a18641d4761ccf5d8a2992245
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S3-C12
      - Result passage disposed without unit P5-S4-C1
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P7-S2-C3
      - 'window 6: invalid/duplicate disposition P7-S2-C14'
      - Result passage disposed without unit P7-S2-C14
      - Unresolved source passage P7-S2-C15
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C7
      - Accounting without a linked unit P11-S1-C8
      - Result passage disposed without unit P9-S2-C6
      - Result passage disposed without unit P9-S2-C8
      - Unaccounted source passage P11-S1-C8
      - Result passage disposed without unit P11-S3-C1
      - Result passage disposed without unit P11-S4-C2
      - Result passage disposed without unit P11-S4-C3
      - Accounting without a linked unit P12-S2-C2
      - Unaccounted source passage P12-S2-C2
      unattached_null_or_qualifier_ids:
      - P4-S1-C2
      - P7-S1-C8
      - P8-S1-C4
      - P12-S2-C2
      suppressed_nonrepresented_units: 20
      default_disposition_count_requires_completeness_check: 225
      unselected_timing_passages:
      - P1-S1-C10
      - P3-S3-C11
      - P4-S1-C1
      - P9-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P4-S2-C10
        - P5-S1-C3
        - P5-S1-C4
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C5
        - P5-S2-C9
        - P6-S1-C4
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S2-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S2-C8
        - P3-S2-C9
        - P3-S3-C2
        - P5-S2-C8
        - P12-S2-C4
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        - P12-S2-C11
        - P12-S2-C12
        - P12-S2-C13
        - P12-S3-C2
        - P12-S3-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C3
        - P6-S2-C7
        - P6-S2-C10
        - P7-S2-C5
        - P7-S2-C9
        - P7-S2-C10
        - P8-S2-C2
        - P8-S2-C3
        - P10-S1-C2
        - P11-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P9-S3-C2
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      - TABLE-4-page-9-4
      - TABLE-5-page-10-5
      unlinked_tables:
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S2
        - P7-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2021
      source_status_sha256: ca785c0c88f6e8ff27acc34f64a96af478c5770a18641d4761ccf5d8a2992245
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 8
      - 10
      - 11
      reason: Abstract summary of regression findings
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Abstract summary of null right hemisphere result
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of prior studies
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient description
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodology description
    - source_id: P5-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodology description
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Outlier description
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Outlier description
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of language deficits
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between tract metrics
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of hemisphere volumes/HMOA
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of tract variability
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Covariate analysis (age/time)
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Covariate analysis (gender)
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Covariate analysis (lesion volume)
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes: []
      reason: Overall AF volume association (not detailed in results list as it is
        a general measure)
    - source_id: P7-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Initial correlation of AF long
    - source_id: P7-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: FDR correction effect on AF long
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 3 reference
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: FDR corrected correlation for AF posterior
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Null result for AF anterior volume
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Correlations for Glasser and Rilling branches
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Null result for other language measures
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: General HMOA findings
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Specific HMOA associations
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Null result for right hemisphere
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      reason: Summary of regression results
    - source_id: P9-S2-C2
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Regression results for Glasser and Rilling model
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of association
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion volume effect
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of segment roles
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: HMOA associations
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: AF posterior role
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Lack of distinction between STG/MTG
    - source_id: P11-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on HMOA sensitivity
    - source_id: P11-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of volume and HMOA
    - source_id: P11-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Consistency with prior studies
    - source_id: P11-S2-C8
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Null distinction between STG and MTG
    - source_id: P11-S2-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Naming ability contribution
    - source_id: P11-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary table
    - source_id: P11-S3-C5
      disposition: represented
      result_indexes:
      - 8
      - 11
      reason: Predictor for lexical-semantic retrieval
    - source_id: P11-S3-C6
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: HMOA importance for language
    - source_id: P11-S3-C7
      disposition: represented
      result_indexes:
      - 0
      - 10
      reason: Specific segment roles
    - source_id: P11-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on cortical damage
    - source_id: P11-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on long segment
    - source_id: P12-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Null right hemisphere result
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Null right hemisphere result
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Consistency with prior studies
    - source_id: P12-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of tumor patients
    - source_id: P12-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of tumor patients
    - source_id: P12-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient description
    - source_id: P12-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of recovery stages
    unresolved_coverage:
    - source_id: P1-S2-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S2-C12
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P11-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C5
    - P1-S2-C7
    - P2-S2-C7
    - P4-S1-C2
    - P5-S3-C12
    - P5-S4-C1
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C8
    - P7-S1-C10
    - P7-S1-C12
    - P7-S2-C3
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C12
    - P7-S2-C13
    - P7-S2-C14
    - P7-S3-C3
    - P8-S1-C8
    - P9-S2-C6
    - P9-S2-C8
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S1-C11
    - P11-S1-C12
    - P11-S2-C2
    - P11-S2-C5
    - P11-S2-C8
    - P11-S2-C9
    - P11-S2-C11
    - P11-S3-C1
    - P11-S3-C5
    - P11-S3-C6
    - P11-S3-C7
    - P11-S4-C2
    - P11-S4-C3
    - P12-S1-C5
    - P12-S2-C2
    - P12-S2-C11
    - P12-S3-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    - TABLE-3-page-7-3
    - TABLE-4-page-9-4
    - TABLE-5-page-10-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P7-S1-C7
      recruited_sample:
      - P3-S3-C11
      eligibility:
      - P3-S3-C11
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      imaging_provenance: []
      imaging_timing:
      - P4-S1-C11
      outcome_timing:
      - P12-S1-C7
      outcome_definition:
      - P4-S1-C6
      - P4-S1-C11
      - P4-S1-C13
      - P4-S2-C2
      - P7-S1-C2
      - P9-S1-C2
      validation: []
      analysis_restrictions:
      - P6-S2-C9
      dependent_variable_statement:
      - P1-S2-C4
      - P6-S2-C7
      - P6-S2-C10
      - P8-S1-C11
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C11
      - P3-S4-C2
      - P3-S4-C3
      - P4-S1-C1
      - P4-S1-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P4-S2-C10
      - P5-S1-C3
      - P5-S1-C4
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C5
      - P5-S2-C9
      - P6-S1-C4
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P6-S2-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S2-C8
      - P3-S2-C9
      - P3-S3-C2
      - P5-S2-C8
      - P12-S2-C4
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C12
      - P12-S2-C13
      - P12-S3-C2
      - P12-S3-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C3
      - P6-S2-C7
      - P6-S2-C10
      - P7-S2-C5
      - P7-S2-C9
      - P7-S2-C10
      - P8-S2-C2
      - P8-S2-C3
      - P10-S1-C2
      - P11-S1-C4
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
      pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
      review_sha256: b5fa59bf9bfa4a0795395c3635c1891fa286b7bccfdb8a57417e11742439e753
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
      - P9-S2-C2
      source_result: In the hierarchical regression analysis using the modified Glasser
        and Rilling model, the HMOA of the left AF temporal pole branch significantly
        contributed to naming scores on the BNT (Adj. R2 = 0.497, Sig. F Change =
        0.009), beyond the effects of cortical lesion load, gender, and time post-onset.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The source P9-S2-C2 explicitly describes the hierarchical regression
            analysis using the Glasser and Rilling model, identifying the AF temporal
            pole HMOA as a significant predictor for BNT naming scores. This matches
            the selected analysis label and evidence ID.
          source_ids:
          - P9-S2-C2
          - P8-S2-C2
        direction:
          answer: fits
          reason: The source states that significant contributions of AF temporal
            pole HMOA to naming scores could be established, indicating a detected
            positive association (residual integrity contributes to performance).
            The draft's direction 'likely' is a reasonable qualitative summary of
            a significant statistical finding, though 'detected' is the precise status.
          source_ids:
          - P9-S2-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as the left AF temporal pole
            HMOA. The outcome is naming (BNT). The method is hierarchical regression.
            The source confirms HMOA is a tract-based diffusion metric (P6-S2-C1,
            P6-S2-C2) and the analysis controls for cortical lesion load (P8-S2-C2).
          source_ids:
          - P9-S2-C2
          - P6-S2-C1
          - P8-S2-C2
        qualifications:
          answer: fits
          reason: The draft includes the key qualification that the analysis was hierarchical
            regression adjusted for cortical lesion load, gender, and time post-onset.
            This aligns with P8-S2-C2 and P9-S2-C2.
          source_ids:
          - P8-S2-C2
          - P9-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft captures the essential methodological context (hierarchical
            regression, specific model, specific metric). While the post-hoc nature
            of the temporal pole branch addition is a limitation (P6-S1-C5, P11-S1-C1),
            it is not a material caveat that invalidates the specific statistical
            result reported in P9-S2-C2, but rather a context for interpretation.
            The core relationship is faithfully represented.
          source_ids:
          - P9-S2-C2
          - P11-S1-C1
      optional_pending:
      - Specific statistical values (Adj. R2, F Change) are not transcribed in the
        draft but are present in source P9-S2-C2.
      - The post-hoc addition of the temporal pole branch to the Glasser and Rilling
        model (P6-S1-C5, P11-S1-C1) is not explicitly flagged as a limitation in the
        draft's limitations list, though it is part of the method description.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values (Adj. R2, F Change) are not transcribed in the draft
      but are present in source P9-S2-C2.
    - The post-hoc addition of the temporal pole branch to the Glasser and Rilling
      model (P6-S1-C5, P11-S1-C1) is not explicitly flagged as a limitation in the
      draft's limitations list, though it is part of the method description.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R013
      exposure:
        text: Left AF temporal pole HMOA
      outcome:
        text: naming (BNT)
      analysis_label: Hierarchical Regression (Glasser and Rilling Model)
      relation: sensitivity
      evidence_ids:
      - P9-S2-C2
      qualifier_ids:
      - P9-S1-C5
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
        source_review: _compare/relationships-2026-11-16/review-current/Ivanova2021
        source_status_sha256: ca785c0c88f6e8ff27acc34f64a96af478c5770a18641d4761ccf5d8a2992245
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a87d2e585bcfcc3c43bb5ef5f324c22f8bcaae238663eed05cd1288046120954
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6304ca9789a9bd627300f869d9275242832f64a7d269baffee2b9cca69842e26
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C11
          page: 3
          text_layer_sha256: 6304ca9789a9bd627300f869d9275242832f64a7d269baffee2b9cca69842e26
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In the last several years,

          a HARDI-diﬀusion-weighted imaging sequence has been added

          to our scanning protocol, yielding a group of thirty-three

          successively scanned participants with aphasia (PWA; 24 males, 9

          females) following a left hemisphere stroke (Mage = 63.7 1.4 years,

          from 40 to 83 years of age).'
        anchor_text: 'In the last several years,

          a HARDI-diﬀusion-weighted imaging sequence has been added

          to our scanning protocol, yielding a group of thirty-three

          successively scanned participants with aphasia (PWA; 24 males, 9

          females) following a left hemisphere stroke (Mage = 63.7 1.4 years,

          from 40 to 83 years of age).'
        excluded_fragments: []
        image_sha256: 50749b1d77098fece1566405db2f3463ee1bdb375aa33b1b15acce07759f1e0b
        transcription: '. In the last several years,

          a HARDI-diffusion-weighted imaging sequence has been added

          to our scanning protocol, yielding a group of thirty-three

          successively scanned participants with aphasia (PWA; 24 males, 9

          females) following a left hemisphere stroke (Mage = 63.7 1.4 years,

          from 40 to 83 years of age)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'Here, only signiﬁcant contributions

    of the AF temporal pole normalized volume to naming scores

    on the WAB (Adj. R2 = 0.530, Sig. F Change = 0.028) and

    BNT (Adj. R2 = 0.493, Sig. F Change = 0.01), as well as the

    AF temporal pole HMOA to naming scores on the BNT (Adj.

    R2 = 0.497, Sig. F Change = 0.009) could be established.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
