---
id: left_lesion_size
name: left lesion size
kind: predictor
findings:
- id: f1
  target: spoken_picture_description_ability
  target_kind: impairment
  claim: When used as a feature in a Hybrid ROI ResNet-18 model, left lesion size
    was found to have a negligible or negative impact on the classification of spoken
    picture description ability as aphasic or non-aphasic.
  direction: no_effect
  relationship: correlational
  method: MVPA
  sample:
    n: 758
    population: English speaking stroke survivors
    phase: not_reported
    time_post_onset: measured months or years post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - MRI data restricted to research quality scanners
  - Binary classification used instead of continuous regression of CAT scores
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Estimate of the number of damaged voxels in the patient''s
    left hemisphere binary lesion image. Finding is specific to the Hybrid ROI model
    where other features (ROIs, initial severity, and recovery time) were also present;
    The apparent negative impact may be due to signal redundancy with other features
    and the addition of noise. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S1-C11, two-model
    agreement, human verification pending): Dataset


    The participants were 758 S survivors from the PLORAS database (Seghier et al.,
    2016) Original text-layer quotation is preserved below. PDF image reading (P9-S3-C14,
    two-model agreement, human verification pending): . In addition, the images are
    collected on

    research scanners at a mean of 46.38 (standard deviation 54.21) months

    after the stroke Original text-layer quotation is preserved below.'
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
    - proposed_concept:spoken_picture_description_ability
  citation: '@White2024'
  source_passages:
  - section: Original source P7-S2-C8
    page: 7
    quote: "As shown in Table 4, \n‘initial severity’ was found to have the largest\
      \ impact, whilst ‘left lesion \nsize’ had a negligible or negative impact."
    supports: claim
  - section: Original source P4-S1-C4
    page: 4
    quote: "Left \nlesion size was an estimate of the number of damaged voxels in\
      \ each \npatient’s left hemisphere binary lesion image (see Hope et al., 2013)."
    supports: method
  - section: Original source P3-S1-C11
    page: 3
    quote: "Dataset \nThe participants were 758 S survivors from the PLORAS database\
      \ \n(Seghier et al., 2016)."
    supports: sample
  - section: Original source P2-S2-C4
    page: 2
    quote: "This includes patients’ high resolution \nT1-weighted structural MRI brain\
      \ scans that are acquired months or \nyears post stroke, lesion images derived\
      \ from the MRIs, and tabular data \nincluding language and cognitive scores\
      \ from the Comprehensive \nAphasia Test (CAT) battery (Swinburn et al., 2004)."
    supports: method
  - section: Original source P9-S3-C14
    page: 9
    quote: "In addition, the images are collected on \nresearch scanners at a mean\
      \ of 46.38 (standard deviation 54.21) months \nafter the stroke."
    supports: limitation
  - section: Original source P9-S4-C11
    page: 9
    quote: "In \nthis paper, this scale has been simplified to a binary classification\
      \ task."
    supports: limitation
  - section: Original source P7-S2-C10
    page: 7
    quote: "The apparent nega­\ntive impact of ‘left lesion size’ when included with\
      \ the other two features \nmay be due to its signal already being present in\
      \ the other features \n(ROIs, ‘initial severity’ and ‘recovery time’), and that\
      \ adding ‘left lesion \nsize’ added noise that impaired classification."
    supports: claim
predictor_type: imaging_metric
short_definition: Estimate of the number of damaged voxels in the patient's left hemisphere
  binary lesion image
assessment:
- Comprehensive Aphasia Test (CAT) spoken picture description task
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: White2024
  proposal_id: R010
  review_status_sha256: c606c77e567bc76b063748f5a1ecd84d1d7b709c0b5bad21d103b73852c0ce36
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
        A/passages.json: cece9ef0eff05d5d0aed05263dfc5cdc29905caa2a82a15fa932e14f0b65606f
        A/raw.json: ad0c74f0c843c459ad80cb2a11b7679c47fe5f2c1ea9f3f7a0138810a7a0af6d
        A/source-units.json: 8390a3eca934b1686d2f61e56f4bc3356e9b682321d8d5ab4d446c8c77b1432c
        A/full-source-units.json: 7d11fb7997e1478807122f4412217b11add7269112de4e11b5c76fa062ebbbd1
        A/meta.json: fb4ecee4249d4988cd00996a36b32f0c080830b340da7ca30d680cfb74d76d0e
        A/table-images/page-13.png: 154e06344051e36f9c2d96b208cf27d821de51d0575b3862c7b4ae75a7a79288
        A/table-images/TABLE-1-page-7-2.png: 9ecfab5190d001389b194e7826dbfbbc6594f09447b9a779ef8af715eb76da4b
        A/table-images/TABLE-5-page-8-3.png: 4075e8a48eb1edf46d2ff45bdba0c82c337b1b1b6fbfdfa65cb73f15b600ab6f
        A/table-images/TABLE-3-page-8-1.png: 951ac1f9c32ce019698f08f1b57d8905b1ab5d304bda7b038bf6ba359140d1c0
        A/table-images/page-7.png: f74faa09b06c093496573dbd8e5a26e83126c7d4dd786a3b48b84968d4f21b6a
        A/table-images/TABLE-4-page-8-2.png: 503a57ffb0aa2af9b40ca4bf51e71ed669bc359d4cf453b4186a6c1578c78ed1
        A/table-images/page-8.png: 2ed158bbf749c52bc0c7c3cdda17707dbc9ed139a34ed1167b283576b94d7300
        A/table-images/TABLE-A2.1-page-13-1.png: 8469bfc9e21ff5a176ebd48a89510b66fb1b55293d91e10d2b7e44d6c699d1ee
        A/table-images/manifest.json: b0c2ae867334b9606ac0c770204090e1838362e55427bda26f3f99defb3079ed
        A/table-images/TABLE-2-page-7-3.png: 118a43a43fdf31596d1139e9a6a2d6b17d01bef109493117dc060a865a984a81
        A/table-images/TABLE-2-page-7-1.png: d9a44376fd8b3b53ce303b97e2e07372ee5f2c2db5722250b2ae43a44a583bda
        A/clauses/window-11/raw.json: a0c93aac9548faf55b99d73209687812c2d282e898483800a6815cc91332358b
        A/clauses/window-11/prompt.txt: f4355ebf1e5ce8b42eaa891723cbca7a88bf5444c86f6e0feb1cb0e2aedccd66
        A/clauses/window-11/meta.json: d368f79f31e81c9cbc0efc45fc1a507ff447ca136430a6f82ec5ab3071055adf
        A/clauses/window-16/raw.json: de8ec66993b9be63b63effb9e8325acdc7799d5367a14956bee8e63a56d248e6
        A/clauses/window-16/prompt.txt: 3f794a93b87519d5ce2a45718eb0436023af23911c45b5d5a2ce6d04983ab202
        A/clauses/window-16/meta.json: 57c6092cd8a5f760c2b5065d15db144c247ed1004f803c2d5104f7a8597c4a5f
        A/clauses/window-10/raw.json: ebf33b03fed7e845d646a455bf7e3b2db39c3559dfee9153c9e852d2ce274e7a
        A/clauses/window-10/prompt.txt: 2ff4dc33624d7e414b3a1d2f63fc29eb9b6396250a405e0d67194c5a29b1df0a
        A/clauses/window-10/meta.json: fb18f5e9c1eae4a75aa3b137280c8b3b6824fd5e1e58382181323358f64dcf7c
        A/clauses/window-03/raw.json: 8bebcf4d25afcc69f22a5f91a3613789349ad39ac0acead9eb5858d08205d846
        A/clauses/window-03/prompt.txt: 2176c35f6dc3652ef2908763353ed273b9942df20441f65894c8ba156a24d3d1
        A/clauses/window-03/meta.json: 36426fff128e50a9f4d0c490744ccfc4e1a1ddcd310da6aaa2d63a5bdbf4a4e3
        A/clauses/window-04/raw.json: 52811daf3c182185ee522cd74b1b8c78a7626145a3837eab270d66c2d8e8ebdf
        A/clauses/window-04/prompt.txt: 2f1ff397ca3a80b954ff28ee6e2d30d12c34b04c2e428bad4147af8da7900499
        A/clauses/window-04/meta.json: b4d44b7420f0c341a22528e640f6d168b36a9be9f3ea8448989c3cec739c42f3
        A/clauses/window-05/raw.json: 19757965e33e780dd294f224e543d8848a16164d5cae5b4b4ae826911df23b7a
        A/clauses/window-05/prompt.txt: 92f0080ea80e33ff270943c83b687eca7fdc965ce91b3bef67e46606c494a745
        A/clauses/window-05/meta.json: 32a16c00d60ec21adafde7ca1007c990a3689ae7effb0b12c73a8092e5d01a87
        A/clauses/window-02/raw.json: 5f72cbf5244acdf432797355dfa67afe2313b3576b847925e97373fe0df4c1d9
        A/clauses/window-02/prompt.txt: 60638406bb36c2803444d78d12df4d06d452af9b99323cbe5caf4c24711eab36
        A/clauses/window-02/meta.json: 12122ab72d43b073f67cadaea71a0b602227f7cd5ed8b06830054b40f98f39d4
        A/clauses/window-15/raw.json: 27e414ff65b3cfd1bc1344642634b1bb642a167b9a7e4628185c4171d1267e32
        A/clauses/window-15/prompt.txt: 916d2b699d52ce86469adb28f4a451cf4f955f361f3abcdddb9b7cb17557718b
        A/clauses/window-15/meta.json: 6978a05459fac8dea5211a190db0c9c1419276ac47130a8b0aee20b8adb18108
        A/clauses/window-12/raw.json: 843e96c348967cac9947deaca97881c5dd62fd4f18eccef7af2d6de7b24ebed6
        A/clauses/window-12/prompt.txt: 31a6671073fdf800501ab789bad98e43e421a9444d220d8a3c2dc617fe4038e6
        A/clauses/window-12/meta.json: 8378da9881834bacd183fba946ad693eee2fe7d20db2f3068acf061a49aa711a
        A/clauses/window-13/raw.json: 299c18d6f2cfb318dd850f7815cceb980607b7ede6a6aec0c797cfa45fd4c499
        A/clauses/window-13/prompt.txt: 6dc979221bc842be9f6c946925d1457791c3ef8936ff68e34419055b3946026f
        A/clauses/window-13/meta.json: 37161db978739db5f27f5268da49555440f0780ae6ec7e16d25de66a694ff7f9
        A/clauses/window-14/raw.json: e1c2429c3a87376ae94ea84edebb76c287d23518c2d0992a78d1d29b27cc42c0
        A/clauses/window-14/prompt.txt: a59dfac5799526d4848e4faeeb8df176b68cad1bebd4ba1d5429148244f6579f
        A/clauses/window-14/meta.json: 3d79ba2a5d07b6ef4840dba0406f83275ecf476891595e9147f6e630a994b8a7
        A/clauses/window-09/raw.json: 39c2dd0d8ce1c03a8655c8475d9ce6acc51be1dc2aebb6a5afbcf2d83fe9180a
        A/clauses/window-09/prompt.txt: 0ee96458b1beded3c12a142518ff1b0e6b83f0ee8ae3fafbdc484356e28e2639
        A/clauses/window-09/meta.json: a97c07eed0c94683728b7f7762fa261c83b3aaba7eef68fa04113ef0cc90eb0e
        A/clauses/window-07/raw.json: 9cf6fd34e192cf9c81eb7bdf8a86f6901a79115c7be91e7816cbad976e53a4f9
        A/clauses/window-07/prompt.txt: 90fd64c9a73a098b45f2b59e2c4601861e1a9a586b7b32681eb727ffd9d9363b
        A/clauses/window-07/meta.json: 4e686aa7746af8d7104f626e2f36f9fc61079a79662a08320add2468b96c93f5
        A/clauses/window-01/raw.json: 841fcf6d86e2d7cf55727438c74537cebbce917f843fec80b59d9cd3ac70a93f
        A/clauses/window-01/prompt.txt: 746385a7af7f01edad9d4c470eb12c640fbcf21a9d558baf1214d16e5da3aa0b
        A/clauses/window-01/meta.json: 9240a41f9eea2b5c77f66cc6f373d13efed6501b86cce0b263392470606e1ab6
        A/clauses/window-06/raw.json: 33aa91c42be41489d084e861a2f319c925be0634c6ead7468a9ca41be3fb76b0
        A/clauses/window-06/prompt.txt: 03a1a9b92a71bbeb35bde7e39330a26af69a70b3dbaa964ed31faa045ca7fdf7
        A/clauses/window-06/meta.json: a27ce0775d8b1e33a278a2670a9b4afbbec0a427ba4f6528bc16a6e6a8710248
        A/clauses/window-08/raw.json: 084a0b8f02b33b4e91935b24296d522dbb35de1a015b403f0abd78c6f542bf5f
        A/clauses/window-08/prompt.txt: 9fd19e4a06258a0297afe1fcc656b5d512bd8de077029e4f69c24435b8d5a166
        A/clauses/window-08/meta.json: dbf350b40a135f4f183feab45841279c83bfccb5bc0757bc1de1565ec7ecb705
        A/tables/TABLE-5-page-8-5/raw.json: f6ee1dda33952af19cce813ec0083960616d95dedb01207771e9a95db7001ee4
        A/tables/TABLE-5-page-8-5/prompt.txt: 395e399c5e75742355d47d9769ee393cc56b50dcb858b30b9295e9da707ec523
        A/tables/TABLE-5-page-8-5/meta.json: b9b292c4679a8612e6f3d6b1734630cef8b2997a0aacd74404226caa668a3d95
        A/tables/TABLE-4-page-8-4/raw.json: c82fd794d6d6761e1469073dfb86a311b7bf3df208188bd23da4670040758f16
        A/tables/TABLE-4-page-8-4/prompt.txt: e41d67cfed4f93f57434d0707938d4ff56283f5f3996b687a7ab73d422cbf1a1
        A/tables/TABLE-4-page-8-4/meta.json: 3313d0a6e6d542ad3a18da9b58f613b216beb3a0b521286d70f59c533b032a48
        A/tables/TABLE-A2.1-page-13-6/raw.json: 2cb90322e2d91cc58dd09b5080f01e347b938bbbc8b2e3fa572c78bccf62a625
        A/tables/TABLE-A2.1-page-13-6/prompt.txt: bfedb0a89a0b7c2e1c57e34fa6e0a8ac31564d9d57cbf422c7f8b00b1cb87e7b
        A/tables/TABLE-A2.1-page-13-6/meta.json: b441389372318ceda6c72f9211e4449b3e740f0ad5f13f691e7bfde1220787b6
        A/tables/TABLE-3-page-8-3/raw.json: 13dc7fb81ae59720d010e000e9eab17bbf1da0215a65d380c93801a691d0ebad
        A/tables/TABLE-3-page-8-3/prompt.txt: c1f2529914dfdad36c8f62219ea407c62e80e4f3fa6a8f587bf42dad0264337b
        A/tables/TABLE-3-page-8-3/meta.json: b5f4fb27649a53fab4c93d9f692eef36c640d5c3496c0f202be85bf7db4fd0f6
        A/tables/TABLE-1-page-7-1/raw.json: f7677a1be7de4f4376d54cdd4d2dae580e1f80686f3bd83553e38c6310af52c2
        A/tables/TABLE-1-page-7-1/prompt.txt: dc2d9d12bb8dd2f213c1dc2219279fcdcc49d7cea7b554219e86e280aeb91056
        A/tables/TABLE-1-page-7-1/meta.json: 896c438dd0b1eafb84bf753837ac78333d8d9c12ad1418686737608b9d17b03e
        A/tables/TABLE-2-page-7-2/raw.json: 28ace884139b88ea02d20bcd999eca4563daf8d5b8daee761dcc4338b603c3b2
        A/tables/TABLE-2-page-7-2/prompt.txt: 859c07d6910f77025a6a31de89e2781755ac4e1dda43da85b8bffa2b04226a3d
        A/tables/TABLE-2-page-7-2/meta.json: 76ddd006bb6eafeffe6186c6db6a47ea3a589104937ec03539eea89795725f22
        B/passages.json: cece9ef0eff05d5d0aed05263dfc5cdc29905caa2a82a15fa932e14f0b65606f
        B/raw.json: 3becf2fb0b2540402b1708b154ff74f22a270ea76960fd336c2a24ad966bac4f
        B/source-units.json: 8390a3eca934b1686d2f61e56f4bc3356e9b682321d8d5ab4d446c8c77b1432c
        B/full-source-units.json: 7d11fb7997e1478807122f4412217b11add7269112de4e11b5c76fa062ebbbd1
        B/meta.json: 71c921991e4dcd9e2e1f6244ed207c3076a5b24cb8f8ba2af4f855949c5d8058
        B/table-images/page-13.png: 154e06344051e36f9c2d96b208cf27d821de51d0575b3862c7b4ae75a7a79288
        B/table-images/TABLE-1-page-7-2.png: 9ecfab5190d001389b194e7826dbfbbc6594f09447b9a779ef8af715eb76da4b
        B/table-images/TABLE-5-page-8-3.png: 4075e8a48eb1edf46d2ff45bdba0c82c337b1b1b6fbfdfa65cb73f15b600ab6f
        B/table-images/TABLE-3-page-8-1.png: 951ac1f9c32ce019698f08f1b57d8905b1ab5d304bda7b038bf6ba359140d1c0
        B/table-images/page-7.png: f74faa09b06c093496573dbd8e5a26e83126c7d4dd786a3b48b84968d4f21b6a
        B/table-images/TABLE-4-page-8-2.png: 503a57ffb0aa2af9b40ca4bf51e71ed669bc359d4cf453b4186a6c1578c78ed1
        B/table-images/page-8.png: 2ed158bbf749c52bc0c7c3cdda17707dbc9ed139a34ed1167b283576b94d7300
        B/table-images/TABLE-A2.1-page-13-1.png: 8469bfc9e21ff5a176ebd48a89510b66fb1b55293d91e10d2b7e44d6c699d1ee
        B/table-images/manifest.json: ab931f67a33a30cdd9b6c60db36f277c6d9e89c44549116c3d512f078a1e11e5
        B/table-images/TABLE-2-page-7-3.png: 118a43a43fdf31596d1139e9a6a2d6b17d01bef109493117dc060a865a984a81
        B/table-images/TABLE-2-page-7-1.png: d9a44376fd8b3b53ce303b97e2e07372ee5f2c2db5722250b2ae43a44a583bda
        B/clauses/window-11/raw.json: 58c50c225b0a7aaef075ec2c640addcccd5866a9f1c2954b629c2a2be6c58252
        B/clauses/window-11/prompt.txt: f4355ebf1e5ce8b42eaa891723cbca7a88bf5444c86f6e0feb1cb0e2aedccd66
        B/clauses/window-11/meta.json: bff7bc29cb3eadb87ba5d5172da88749be4d679cdca23a41861580774fcea79e
        B/clauses/window-16/raw.json: b8311e05acaede12202cbb9b8d90935c29e9acaa02f558c1315b3fb20faf9905
        B/clauses/window-16/prompt.txt: 3f794a93b87519d5ce2a45718eb0436023af23911c45b5d5a2ce6d04983ab202
        B/clauses/window-16/meta.json: 54fd720af60dcf9297dc642d8318221283f42fa07a2a3c2095fd417e18de3e77
        B/clauses/window-10/raw.json: c6738fc29132aca2cb07fbf1a4b22cbe5a79eaa3b4bb48dcad368da4de9fe648
        B/clauses/window-10/prompt.txt: 2ff4dc33624d7e414b3a1d2f63fc29eb9b6396250a405e0d67194c5a29b1df0a
        B/clauses/window-10/meta.json: 844030d0484328cc3a4ec89f4501f2157afadabf97adc17cbb805808f5bbb100
        B/clauses/window-03/raw.json: 1090703213e491bb8eece1530e2aa40947675a97f6730d02267f396970aa8525
        B/clauses/window-03/prompt.txt: 2176c35f6dc3652ef2908763353ed273b9942df20441f65894c8ba156a24d3d1
        B/clauses/window-03/meta.json: 54e355f5175e98f1dbb4531b4f98951e72ae9cf80bfd150a80162ba231412856
        B/clauses/window-04/raw.json: 4f8866a8f7da49fefef9648cb6652dd74b98056633d4a9a6d814aa0694592ce9
        B/clauses/window-04/prompt.txt: 2f1ff397ca3a80b954ff28ee6e2d30d12c34b04c2e428bad4147af8da7900499
        B/clauses/window-04/meta.json: fa1773eac34e0bcfa15132bb2eb35db631b728ad225c90d9be1023c2ac0433b6
        B/clauses/window-05/raw.json: a6d9f5d06b5ad1b744664eaf3c9b8ce3e650c0c08397953db8260a51a862bbb4
        B/clauses/window-05/prompt.txt: 92f0080ea80e33ff270943c83b687eca7fdc965ce91b3bef67e46606c494a745
        B/clauses/window-05/meta.json: bd3fa3c4188d83f6ccaffe23e0b87c2252e3dc8814025157642250abc0fd4d77
        B/clauses/window-02/raw.json: a7ff4dd4fe48e512424c9f60f1c9a7704974be1801129b3db02aa7409e6c765b
        B/clauses/window-02/prompt.txt: 60638406bb36c2803444d78d12df4d06d452af9b99323cbe5caf4c24711eab36
        B/clauses/window-02/meta.json: d3639e3195584d9b49651e07a1721faa101447b5f841facceecc497edbf479d4
        B/clauses/window-15/raw.json: 0ffe8d04f48b2d08aa80898d0fab1e997f8c188145f41bfbbec339897eeb5bb6
        B/clauses/window-15/prompt.txt: 916d2b699d52ce86469adb28f4a451cf4f955f361f3abcdddb9b7cb17557718b
        B/clauses/window-15/meta.json: 8877a4dfacb090f95b15b81a4b700520fe8fe82b357d8024a06e5d8806b77c64
        B/clauses/window-12/raw.json: 79d343f0659f97d64a35219144a327f5a34cf646f23298640e51f1b2e8fd5027
        B/clauses/window-12/prompt.txt: 31a6671073fdf800501ab789bad98e43e421a9444d220d8a3c2dc617fe4038e6
        B/clauses/window-12/meta.json: 6f3223fb14609002d521749cd4f39f0a25c5b3791b92249e57274b38d28a46ec
        B/clauses/window-13/raw.json: aea56a799c5a82fdb20e0adc618135448f5cfbe4a85e1ea970fec955ccc1b1c5
        B/clauses/window-13/prompt.txt: 6dc979221bc842be9f6c946925d1457791c3ef8936ff68e34419055b3946026f
        B/clauses/window-13/meta.json: 5102bf1243691261101246bdcdf5ab3857457248053eb9a9bf2d30ccf38f388c
        B/clauses/window-14/raw.json: 1df567a057a2b7cf1572029807d6861c76d0ff133a716ab0f64540f30ccdf73a
        B/clauses/window-14/prompt.txt: a59dfac5799526d4848e4faeeb8df176b68cad1bebd4ba1d5429148244f6579f
        B/clauses/window-14/meta.json: e654c43923cc744fb46e6d45ea81ec0afb41cfb778e862457371674ea6d06bf1
        B/clauses/window-09/raw.json: ad25f71936d5fc302341321d0a5729d681d9afed7121fa7b9415fd17425e88d0
        B/clauses/window-09/prompt.txt: 0ee96458b1beded3c12a142518ff1b0e6b83f0ee8ae3fafbdc484356e28e2639
        B/clauses/window-09/meta.json: 8a0c7cd5ec249b5850f495c6b449ab41a7671a0f843c87358b51419cead6ab4c
        B/clauses/window-07/raw.json: bf31ed9f1d0669d6b63e487ec55bc0daf539fe431385667e5c70f88ea734807c
        B/clauses/window-07/prompt.txt: 90fd64c9a73a098b45f2b59e2c4601861e1a9a586b7b32681eb727ffd9d9363b
        B/clauses/window-07/meta.json: 107083ea52f43ce6751596c25f030cec333ee6097517b85f54072ac58716a42b
        B/clauses/window-01/raw.json: 9a3259a60fcc1a658f94394c52fbd41dc31126c0d136ae11fbabab55e2e6b49e
        B/clauses/window-01/prompt.txt: 746385a7af7f01edad9d4c470eb12c640fbcf21a9d558baf1214d16e5da3aa0b
        B/clauses/window-01/meta.json: c25d563fa61594d20ea08989a359093f5430ced65404a0a8d0693d28258cf5e0
        B/clauses/window-06/raw.json: 153c9a661de12fef9b128a7150a373b80ffa29aab36a209e36c6ad26cdd5d8ed
        B/clauses/window-06/prompt.txt: 03a1a9b92a71bbeb35bde7e39330a26af69a70b3dbaa964ed31faa045ca7fdf7
        B/clauses/window-06/meta.json: 8c0c0d3e8ade6cc500c5faa2f34b0f323710fc43baacd6520174817e6dd40a9f
        B/clauses/window-08/raw.json: 94d2cc7c89f1d519cff7849a37dfb38fff0865f77be9e6b6d3561b0164f8cae7
        B/clauses/window-08/prompt.txt: 9fd19e4a06258a0297afe1fcc656b5d512bd8de077029e4f69c24435b8d5a166
        B/clauses/window-08/meta.json: 28179c626f7702671ccbbad6202397b253bd1d874af7258009a1482ee6e30c06
        B/tables/TABLE-5-page-8-5/raw.json: 419936ffdcee8151bec71d601943bc2b6ff88b8a74002c5e60fe79019fcb226d
        B/tables/TABLE-5-page-8-5/prompt.txt: 395e399c5e75742355d47d9769ee393cc56b50dcb858b30b9295e9da707ec523
        B/tables/TABLE-5-page-8-5/meta.json: 7e68639b4d26a698c009ee67c6c040f8e499ce25482db8a8668791445cdebc5d
        B/tables/TABLE-4-page-8-4/raw.json: 7993d569dd17f0c72e106100b5128bccdab1a06f4929fbc31ef834b04c3cac55
        B/tables/TABLE-4-page-8-4/prompt.txt: e41d67cfed4f93f57434d0707938d4ff56283f5f3996b687a7ab73d422cbf1a1
        B/tables/TABLE-4-page-8-4/meta.json: 0bae95515d2872a686bebf83cb3232dd81efd870ade6bdb8a6a35dc8e9b1d24d
        B/tables/TABLE-A2.1-page-13-6/raw.json: 2cb90322e2d91cc58dd09b5080f01e347b938bbbc8b2e3fa572c78bccf62a625
        B/tables/TABLE-A2.1-page-13-6/prompt.txt: bfedb0a89a0b7c2e1c57e34fa6e0a8ac31564d9d57cbf422c7f8b00b1cb87e7b
        B/tables/TABLE-A2.1-page-13-6/meta.json: 632a0bcaf30124261b61597bd9300bb2be9f8f4ce218e910510baf749b992dea
        B/tables/TABLE-3-page-8-3/raw.json: 6fa27f9dca898ad412679b08382798420b1335e668df420d1f4b3e1d9b3c3b16
        B/tables/TABLE-3-page-8-3/prompt.txt: c1f2529914dfdad36c8f62219ea407c62e80e4f3fa6a8f587bf42dad0264337b
        B/tables/TABLE-3-page-8-3/meta.json: 4193ec45035daf7610d1a233b4a2b6a9bb669b998f58467d6462ade8bc8c4da4
        B/tables/TABLE-1-page-7-1/raw.json: 808605238a1c3f14bf1247fe58ad355eb1ba7908464df13e977609224963e034
        B/tables/TABLE-1-page-7-1/prompt.txt: dc2d9d12bb8dd2f213c1dc2219279fcdcc49d7cea7b554219e86e280aeb91056
        B/tables/TABLE-1-page-7-1/meta.json: b8396e01486fc5f4f387d7f7281d148cd767323a0b62c1eaa7aed9bd446e2061
        B/tables/TABLE-2-page-7-2/raw.json: 293529bc91748525f3a73c1b90a4a431f00dfde4ed2054e26ac509d1ec61b775
        B/tables/TABLE-2-page-7-2/prompt.txt: 859c07d6910f77025a6a31de89e2781755ac4e1dda43da85b8bffa2b04226a3d
        B/tables/TABLE-2-page-7-2/meta.json: d401e2bbe28c1922fd4cd1a26bb1ff8626cebe0d635bbcb1c80d046908fe936f
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
      pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
      source_review: _compare/relationships-2026-11-16/review-current/White2024
      source_status_sha256: 901db0c639a62c7cc51c1719df817c73446144a81fb3fc2b44a527eee58dcd8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: left lesion size
    outcome:
      text: spoken picture description ability (aphasic vs non-aphasic)
    analysis_label: Hybrid ROI Feature Contribution (Left Lesion Size)
    relation: association
    evidence_ids:
    - P7-S2-C8
    qualifier_ids:
    - P7-S2-C7
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
      source_review: _compare/relationships-2026-11-16/review-current/White2024
      source_status_sha256: 901db0c639a62c7cc51c1719df817c73446144a81fb3fc2b44a527eee58dcd8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S2-C6
      - Result passage disposed without unit P3-S3-C5
      - Result passage disposed without unit P3-S3-C6
      - Result passage disposed without unit P4-S3-C10
      - Result passage disposed without unit P4-S5-C3
      - Result passage disposed without unit P5-S2-C11
      - Accounting without a linked unit P5-S2-C12
      - Unaccounted source passage P5-S2-C12
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C9
      - Unresolved source passage P7-S1-C9
      - Result passage disposed without unit P7-S2-C11
      - Result passage disposed without unit P7-S2-C12
      - Result passage disposed without unit P7-S2-C13
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P8-S1-C9
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P8-S1-C9
      - Accounting without a linked unit P8-S2-C9
      - Unaccounted source passage P8-S2-C9
      - Result passage disposed without unit P9-S4-C6
      - 'window 15: invalid/duplicate disposition P10-S1-C5'
      - Result passage disposed without unit P10-S2-C5
      - Result passage disposed without unit P10-S3-C2
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C11
      - Result passage disposed without unit P12-S1-C5
      - Result passage disposed without unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S1-C8
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P13-S1-C11
      unattached_null_or_qualifier_ids:
      - P5-S2-C12
      - P7-S1-C7
      - P8-S1-C9
      suppressed_nonrepresented_units: 53
      default_disposition_count_requires_completeness_check: 354
      unselected_timing_passages:
      - P1-S1-C14
      - P4-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C14
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C7
        - P3-S3-C9
        - P4-S1-C2
        - P4-S1-C3
        - P4-S2-C7
        - P4-S2-C9
        - P4-S2-C13
        - P4-S2-C14
        - P5-S1-C1
        - P5-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C12
        - P2-S1-C10
        - P2-S1-C12
        - P2-S2-C5
        - P3-S2-C7
        - P3-S2-C10
        - P3-S2-C11
        - P3-S2-C13
        - P3-S3-C3
        - P3-S3-C5
        - P4-S1-C11
        - P4-S2-C12
        - P4-S3-C6
        - P4-S3-C7
        - P4-S3-C8
        - P4-S3-C9
        - P4-S3-C12
        - P4-S5-C2
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P5-S1-C15
        - P5-S1-C16
        - P5-S1-C17
        - P5-S1-C18
        - P5-S1-C19
        - P6-S1-C11
        - P6-S1-C15
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S2-C1
        - P7-S2-C3
        - P7-S2-C4
        - P7-S2-C5
        - P7-S2-C6
        - P7-S2-C7
        - P7-S2-C8
        - P7-S2-C9
        - P7-S2-C10
        - P7-S2-C11
        - P7-S2-C12
        - P7-S2-C13
        - P7-S3-C2
        - P7-S3-C3
        - P7-S3-C4
        - P7-S3-C5
        - P7-S3-C6
        - P7-S3-C7
        - P7-S3-C9
        - P7-S3-C10
        - P7-S4-C1
        - P8-S1-C10
        - P8-S1-C11
        - P8-S1-C12
        - P8-S1-C13
        - P8-S1-C14
        - P8-S2-C3
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C6
        - P8-S2-C7
        - P8-S2-C8
        - P8-S2-C9
        - P8-S2-C10
        - P8-S2-C11
        - P8-S2-C12
        - P8-S2-C13
        - P8-S3-C2
        - P8-S3-C3
        - P8-S3-C4
        - P8-S3-C5
        - P8-S4-C1
        - P8-S4-C2
        - P8-S4-C3
        - P8-S4-C5
        - P9-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: validation
        source_ids:
        - P1-S2-C4
        - P1-S2-C5
        - P4-S1-C6
        - P4-S1-C9
        - P4-S1-C11
        - P4-S2-C4
        - P5-S2-C4
        - P5-S2-C5
        - P6-S1-C13
        - P7-S3-C5
        - P11-S1-C6
        - P11-S1-C8
        - P12-S2-C7
        - P12-S2-C8
        - P13-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S1-C8
        - P3-S3-C7
        - P9-S3-C12
        - P9-S3-C13
        - P9-S3-C14
        - P9-S3-C15
        - P9-S3-C16
        - P10-S1-C11
        - P10-S1-C12
        - P10-S1-C13
        - P10-S1-C14
        - P10-S2-C6
        - P10-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C14
        - P2-S3-C2
        - P4-S1-C5
        - P6-S1-C12
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S2-C6
        - P7-S2-C7
        - P7-S2-C8
        - P7-S2-C9
        - P7-S2-C10
        - P7-S2-C11
        - P7-S2-C12
        - P7-S2-C13
        - P7-S3-C2
        - P7-S3-C3
        - P7-S3-C4
        - P7-S3-C5
        - P7-S3-C6
        - P7-S3-C7
        - P7-S3-C9
        - P7-S3-C10
        - P7-S4-C1
        - P8-S1-C10
        - P8-S1-C11
        - P8-S1-C12
        - P8-S1-C13
        - P8-S1-C14
        - P8-S2-C3
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C6
        - P8-S2-C7
        - P8-S2-C8
        - P8-S2-C9
        - P8-S2-C10
        - P8-S2-C11
        - P8-S2-C12
        - P8-S2-C13
        - P8-S3-C2
        - P8-S3-C3
        - P8-S3-C4
        - P8-S3-C5
        - P8-S4-C1
        - P8-S4-C2
        - P8-S4-C3
        - P8-S4-C5
        - P9-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      - TABLE-2-page-7-2
      - TABLE-3-page-8-3
      - TABLE-4-page-8-4
      - TABLE-5-page-8-5
      - TABLE-A2.1-page-13-6
      unlinked_tables:
      - TABLE-5-page-8-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S3
        - P3-S4
        - P4-S2
        - P4-S4
        - P4-S5
        - P5-S1
        - P5-S2
        - P6-S2
        - P6-S3
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
      source_review: _compare/relationships-2026-11-16/review-current/White2024
      source_status_sha256: 901db0c639a62c7cc51c1719df817c73446144a81fb3fc2b44a527eee58dcd8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Reports accuracy for baseline logistic regression with varying feature
        sets.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports highest accuracy, AUC, and F1 for the 2D ResNet with 8 ROIs
        and tabular data.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports performance for the best model in the moderate/severe aphasia
        subgroup.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information (male to female ratio, average age).
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distribution of initial severity scores.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distribution of spoken picture description scores.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic of aphasic range in severe/moderate subgroup.
    - source_id: P4-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of how key ROIs were identified.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: List of identified key ROIs.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Categorization of ROIs by lobe.
    - source_id: P4-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of the top three ROIs.
    - source_id: P4-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Finding that top eight ROIs minimized loss during cross-validation.
    - source_id: P4-S5-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Finding that seven top ROIs should be included in hybrid images.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of the early stopping rule.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that test accuracy varies slightly with number of ROIs.
    - source_id: P6-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of the lightweight CNN architecture.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that all models performed well.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on statistical significance of tabular features in logistic
        regression.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports balanced accuracy for logistic regression with lesion size only.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports balanced accuracy for logistic regression with added initial
        severity and recovery time.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explanation of why logistic regression results lack confidence intervals.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 3
      - 5
      reason: Identifies Hybrid ROI ResNet-18 as the best model.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: States the difference between Hybrid ROI and baseline is statistically
        significant.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Compares Stitched MRI models to ResNet3D.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about balanced vs unbalanced accuracy in the subgroup.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 3
      reason: States Hybrid ROI model had highest AUC and F1 scores.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Reports ResNet3D as having the second highest AUC.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: States Hybrid ROI model dominated ResNet3D at all thresholds.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports impact of initial severity and left lesion size in Hybrid ROI
        model.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about Hybrid ROI images with only two features (not cross-validated).
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 10
      reason: Reports that increasing ResNet depth slightly reduced accuracies.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on balanced accuracy of CNNs.
    - source_id: P7-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of best model performance.
    - source_id: P7-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: States left hemisphere lesion size was least important when ROIs were
        incorporated.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Restates that 2D CNNs on Stitched MRI had similar accuracies to 3D ResNet.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Compares Hybrid ROIs/ROIs datasets to Stitched MRI datasets.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about performance with only four ROIs.
    - source_id: P9-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that logistic regression classified surprisingly well.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Restates that Hybrid ROI model performed better than logistic regression.
    - source_id: P9-S3-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Reports improvement in balanced accuracy of Hybrid ROIs due to pre-training
        weights.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Preliminary results on classification vs regression encoding.
    - source_id: P10-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on CLEAR Image fidelity statistics.
    - source_id: P10-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on the objective of the paper.
    - source_id: P10-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on the effectiveness of ResNets and multimodal data.
    - source_id: P11-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure A1.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of why paired Wilcoxon failed.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of false positive rate inflation in traditional methods.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Simulation result for t-paired-bast1.
    - source_id: P12-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on inflation of false-positive rates.
    - source_id: P12-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement that proposed correction returned t-test to non-inflating
        regime.
    - source_id: P12-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Specific type-I error rate for 0.45 scaling.
    - source_id: P13-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mean accuracy and CI for refitted logistic regression.
    - source_id: P13-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Rejects null hypothesis that Hybrid ROI model has same accuracy as logistic
        regression.
    - source_id: P13-S2-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Table A2.1 providing statistical comparisons of Hybrid ROI model against
        others.
    unresolved_coverage:
    - source_id: P10-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S4-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S4-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S1-C12
    - P3-S2-C6
    - P3-S3-C5
    - P3-S3-C6
    - P4-S2-C15
    - P4-S3-C9
    - P4-S3-C10
    - P4-S3-C12
    - P4-S4-C3
    - P4-S5-C3
    - P5-S2-C11
    - P5-S2-C12
    - P6-S2-C16
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C3
    - P7-S2-C9
    - P7-S2-C12
    - P7-S2-C13
    - P7-S3-C2
    - P8-S1-C9
    - P8-S2-C9
    - P9-S1-C12
    - P9-S1-C13
    - P9-S4-C6
    - P9-S4-C7
    - P9-S4-C8
    - P10-S1-C3
    - P10-S2-C5
    - P10-S2-C14
    - P10-S3-C2
    - P10-S3-C3
    - P11-S3-C9
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S1-C11
    - P13-S1-C3
    - P13-S1-C5
    - P13-S1-C8
    - P13-S1-C9
    - P13-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    - TABLE-2-page-7-2
    - TABLE-3-page-8-3
    - TABLE-4-page-8-4
    - TABLE-5-page-8-5
    - TABLE-A2.1-page-13-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C13
      - P4-S1-C5
      - P4-S1-C6
      - P5-S2-C5
      - P7-S3-C7
      recruited_sample:
      - P1-S1-C13
      eligibility:
      - P2-S2-C6
      - P2-S2-C7
      - P3-S1-C13
      - P3-S3-C8
      imaging_provenance: []
      imaging_timing:
      - P2-S2-C4
      - P3-S3-C7
      - P9-S3-C14
      outcome_timing:
      - P2-S1-C10
      - P3-S1-C10
      - P9-S3-C14
      - P9-S3-C15
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S1-C9
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S1-C12
      - P3-S2-C7
      - P3-S2-C10
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C12
      - P1-S1-C13
      - P1-S1-C14
      - P3-S1-C12
      - P3-S1-C15
      - P3-S2-C6
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: held_out_internal
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C14
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C7
      - P3-S3-C9
      - P4-S1-C2
      - P4-S1-C3
      - P4-S2-C7
      - P4-S2-C9
      - P4-S2-C13
      - P4-S2-C14
      - P5-S1-C1
      - P5-S1-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C12
      - P2-S1-C10
      - P2-S1-C12
      - P2-S2-C5
      - P3-S2-C7
      - P3-S2-C10
      - P3-S2-C11
      - P3-S2-C13
      - P3-S3-C3
      - P3-S3-C5
      - P4-S1-C11
      - P4-S2-C12
      - P4-S3-C6
      - P4-S3-C7
      - P4-S3-C8
      - P4-S3-C9
      - P4-S3-C12
      - P4-S5-C2
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C14
      - P5-S1-C15
      - P5-S1-C16
      - P5-S1-C17
      - P5-S1-C18
      - P5-S1-C19
      - P6-S1-C11
      - P6-S1-C15
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S2-C1
      - P7-S2-C3
      - P7-S2-C4
      - P7-S2-C5
      - P7-S2-C6
      - P7-S2-C7
      - P7-S2-C8
      - P7-S2-C9
      - P7-S2-C10
      - P7-S2-C11
      - P7-S2-C12
      - P7-S2-C13
      - P7-S3-C2
      - P7-S3-C3
      - P7-S3-C4
      - P7-S3-C5
      - P7-S3-C6
      - P7-S3-C7
      - P7-S3-C9
      - P7-S3-C10
      - P7-S4-C1
      - P8-S1-C10
      - P8-S1-C11
      - P8-S1-C12
      - P8-S1-C13
      - P8-S1-C14
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C6
      - P8-S2-C7
      - P8-S2-C8
      - P8-S2-C9
      - P8-S2-C10
      - P8-S2-C11
      - P8-S2-C12
      - P8-S2-C13
      - P8-S3-C2
      - P8-S3-C3
      - P8-S3-C4
      - P8-S3-C5
      - P8-S4-C1
      - P8-S4-C2
      - P8-S4-C3
      - P8-S4-C5
      - P9-S1-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: validation
      source_ids:
      - P1-S2-C4
      - P1-S2-C5
      - P4-S1-C6
      - P4-S1-C9
      - P4-S1-C11
      - P4-S2-C4
      - P5-S2-C4
      - P5-S2-C5
      - P6-S1-C13
      - P7-S3-C5
      - P11-S1-C6
      - P11-S1-C8
      - P12-S2-C7
      - P12-S2-C8
      - P13-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S1-C8
      - P3-S3-C7
      - P9-S3-C12
      - P9-S3-C13
      - P9-S3-C14
      - P9-S3-C15
      - P9-S3-C16
      - P10-S1-C11
      - P10-S1-C12
      - P10-S1-C13
      - P10-S1-C14
      - P10-S2-C6
      - P10-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C14
      - P2-S3-C2
      - P4-S1-C5
      - P6-S1-C12
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S2-C6
      - P7-S2-C7
      - P7-S2-C8
      - P7-S2-C9
      - P7-S2-C10
      - P7-S2-C11
      - P7-S2-C12
      - P7-S2-C13
      - P7-S3-C2
      - P7-S3-C3
      - P7-S3-C4
      - P7-S3-C5
      - P7-S3-C6
      - P7-S3-C7
      - P7-S3-C9
      - P7-S3-C10
      - P7-S4-C1
      - P8-S1-C10
      - P8-S1-C11
      - P8-S1-C12
      - P8-S1-C13
      - P8-S1-C14
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C6
      - P8-S2-C7
      - P8-S2-C8
      - P8-S2-C9
      - P8-S2-C10
      - P8-S2-C11
      - P8-S2-C12
      - P8-S2-C13
      - P8-S3-C2
      - P8-S3-C3
      - P8-S3-C4
      - P8-S3-C5
      - P8-S4-C1
      - P8-S4-C2
      - P8-S4-C3
      - P8-S4-C5
      - P9-S1-C12
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
      pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
      review_sha256: c606c77e567bc76b063748f5a1ecd84d1d7b709c0b5bad21d103b73852c0ce36
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
      - P7-S2-C8
      source_result: In the Hybrid ROI model, 'left lesion size' was found to have
        a negligible or negative impact on classification accuracy, whereas 'initial
        severity' had the largest impact. The authors suggest the negative impact
        may be due to signal redundancy with other features (ROIs, initial severity,
        recovery time) and added noise.
      result_status: not_detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the feature contribution assessment
            of the Hybrid ROI model described in P7-S2-C8 and P7-S2-C7. The proposed
            core correctly identifies the model (Hybrid ROI ResNet-18) and the specific
            feature being tested (left lesion size).
          source_ids:
          - P7-S2-C8
          - P7-S2-C7
        direction:
          answer: fits
          reason: The source states that left lesion size had a 'negligible or negative
            impact' (P7-S2-C8). The proposed core uses 'no_effect' which aligns with
            the lack of positive contribution (negligible/negative) in the context
            of model performance. It does not claim a positive association.
          source_ids:
          - P7-S2-C8
        construct:
          answer: fits
          reason: The exposure is 'left lesion size', defined in P4-S1-C4 as the number
            of damaged voxels in the left hemisphere binary lesion image. The outcome
            is the classification of spoken picture description ability (aphasic vs
            non-aphasic). The method is correctly identified as a feature contribution
            analysis within a multimodal model.
          source_ids:
          - P4-S1-C4
          - P3-S2-C7
          - P7-S2-C8
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that this
            finding is specific to the Hybrid ROI model where other features are present,
            and notes the potential cause (redundancy/noise) as stated in P7-S2-C10.
            This prevents misinterpretation as a general null finding for lesion size
            in all contexts.
          source_ids:
          - P7-S2-C8
          - P7-S2-C10
        missing_material_caveat:
          answer: fits
          reason: The core includes the necessary context that this is a model-specific
            finding and mentions the redundancy explanation. It does not omit material
            caveats that would change the interpretation of the 'negligible/negative'
            result within this specific analysis.
          source_ids:
          - P7-S2-C8
          - P7-S2-C10
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
      id: R010
      exposure:
        text: left lesion size
      outcome:
        text: spoken picture description ability (aphasic vs non-aphasic)
      analysis_label: Hybrid ROI Feature Contribution (Left Lesion Size)
      relation: association
      evidence_ids:
      - P7-S2-C8
      qualifier_ids:
      - P7-S2-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
        source_review: _compare/relationships-2026-11-16/review-current/White2024
        source_status_sha256: 901db0c639a62c7cc51c1719df817c73446144a81fb3fc2b44a527eee58dcd8e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e2d70eb54e674951d6cdde0da79e32c062af5657a015d065b241d9f3cb3bb11d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C11
          page: 3
          text_layer_sha256: e2d70eb54e674951d6cdde0da79e32c062af5657a015d065b241d9f3cb3bb11d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Dataset \nThe participants were 758 S survivors from the PLORAS\
          \ database \n(Seghier et al., 2016)."
        anchor_text: "Dataset \nThe participants were 758 S survivors from the PLORAS\
          \ database \n(Seghier et al., 2016)."
        excluded_fragments: []
        image_sha256: 2ea578d1577a80d81f31f20802176a4eae55a0c320d0bb031a56f19405677217
        transcription: 'Dataset


          The participants were 758 S survivors from the PLORAS database (Seghier
          et al., 2016)'
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 25467f2a42c914a77751eb9cabb4a86ec27162bc8e2a6e73781b5cb564a3c95b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: 25467f2a42c914a77751eb9cabb4a86ec27162bc8e2a6e73781b5cb564a3c95b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "This includes patients’ high resolution \nT1-weighted structural\
          \ MRI brain scans that are acquired months or \nyears post stroke, lesion\
          \ images derived from the MRIs, and tabular data \nincluding language and\
          \ cognitive scores from the Comprehensive \nAphasia Test (CAT) battery (Swinburn\
          \ et al., 2004)."
        anchor_text: "This includes patients’ high resolution \nT1-weighted structural\
          \ MRI brain scans that are acquired months or \nyears post stroke, lesion\
          \ images derived from the MRIs, and tabular data \nincluding language and\
          \ cognitive scores from the Comprehensive \nAphasia Test (CAT) battery (Swinburn\
          \ et al., 2004)."
        excluded_fragments: []
        image_sha256: 9058d39daf8be6c6ba7e352fb8cd58f9eb17077fb933cdb9474ec389c7c49a75
      P9-S3-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82b56601293feaff545666004f3d9c8e1209957096f708ceed1f3a4cb55cb853
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 34bab1cb746fb276fd97ddb3a0d6c6d72ca64e6a9b4c481e3e5ec3ebbe63378a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S3-C14
          page: 9
          text_layer_sha256: 34bab1cb746fb276fd97ddb3a0d6c6d72ca64e6a9b4c481e3e5ec3ebbe63378a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "In addition, the images are collected on \nresearch scanners\
          \ at a mean of 46.38 (standard deviation 54.21) months \nafter the stroke."
        anchor_text: "In addition, the images are collected on \nresearch scanners\
          \ at a mean of 46.38 (standard deviation 54.21) months \nafter the stroke."
        excluded_fragments: []
        image_sha256: d9002ee5332efe2b2a0d2fa0cb5da5906e74fbd543c64ae24a5cefe7b9fe4908
        transcription: '. In addition, the images are collected on

          research scanners at a mean of 46.38 (standard deviation 54.21) months

          after the stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "As shown in Table 4, \n‘initial severity’ was found to have the largest\
    \ impact, whilst ‘left lesion \nsize’ had a negligible or negative impact."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
