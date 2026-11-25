---
id: left_motor_cortex_lesion
name: left motor cortex lesion
kind: classical
findings:
- id: f1
  target: right_motor_cortex_activity
  target_kind: impairment
  claim: Lesions in the left motor cortex were related to significantly greater activity
    in the right motor cortex during overt naming; furthermore, this increased right
    motor activity was positively associated with naming performance only in participants
    with left motor lesions.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 39
    population: chronic left hemisphere stroke survivors with aphasia
    phase: not_reported
    time_post_onset: at least six months after stroke (mean chronicity = 52.9 months);
      naming ability tested within one week of MRI scan
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Analysis restricted to correct trials only to minimize effort effects
  - Participants with severe anomia (correctly naming <10% of trials in scanner) were
    excluded
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a 5 mm sphere ROI centered
    on the peak voxel of motor cortex activity identified in a healthy control group
    during overt naming. Analysis of right motor activity and naming performance was
    conducted separately for those with and without left motor lesions; Right motor
    activity was positively associated with naming only in the left motor lesion group
    (N=24); No relationship between right motor activity and naming was found in the
    intact left motor cortex group (N=15); Analysis controlled for total lesion volume.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P3-S1-C8, two-model agreement, human verification
    pending): . Ten partic-

    ipants were then excluded based on fMRI task performance

    (<10% accuracy) resulting in a final sample of 39 participants

    in the aphasia group Original text-layer quotation is preserved below. PDF image
    reading (P3-S1-C9, two-model agreement, human verification pending): All participants
    in the aphasia group were native English speakers and testing occurred at least
    six months after their stroke (mean chronicity = 52.9 months) Original text-layer
    quotation is preserved below. PDF image reading (P13-S1-C5, two-model agreement,
    human verification pending): . Finally, our study

    excluded participants with severe anomia, who could not

    correctly name at least 10% of the trials in the scanner Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:right_motor_cortex_activity
  citation: '@SkipperKallal2017'
  source_passages:
  - section: Original source P9-S2-C11
    page: 9
    quote: 'For overt naming, lesions in the left motor cortex were

      related to significantly greater activity in the right motor cor-

      tex, 𝑡(36) = 2.91, 𝑃< 0.01, while lesions in the left STS were

      associated with lower activity in right motor cortex, 𝑡(36) =

      −2.24, 𝑃< 0.05 (Figure 4).'
    supports: claim
  - section: Original source P9-S3-C2
    page: 9
    quote: 'However, for participants

      with left motor lesions (𝑁= 24), right motor activity was

      positively associated with naming, 𝑡(21) = 3.67, 𝑃= 0.001.

      4.'
    supports: claim
  - section: Original source P9-S2-C14
    page: 9
    quote: 'For participants

      in the aphasia group with intact left motor cortex (𝑁= 15),

      there was no relationship between right motor activity and

      naming, 𝑡(12) = −0.28, 𝑃= 0.75.'
    supports: claim
  - section: Original source P13-S1-C8
    page: 13
    quote: 'We did find evidence for homotopic remapping in motor

      cortex, in that left motor cortex lesions led to significantly

      greater right motor cortex activation during overt naming,

      controlling for total lesion volume.'
    supports: claim
  - section: Original source P3-S1-C7
    page: 3
    quote: 'Forty-nine chronic left hemisphere stroke

      survivors with a history of aphasia were recruited.'
    supports: sample
  - section: Original source P3-S1-C8
    page: 3
    quote: 'Ten partic-

      ipants were then excluded based on fMRI task performance

      (<10% accuracy) resulting in a final sample of 39 participants

      in the aphasia group.'
    supports: sample
  - section: Original source P3-S1-C9
    page: 3
    quote: 'All participants in the aphasia group were native English

      speakers and testing occurred at least six months after

      their stroke (mean chronicity = 52.9 months).'
    supports: sample
  - section: Original source P4-S2-C12
    page: 4
    quote: 'For each of the left hemisphere ROIs, aphasia group

      participants were grouped based on lesion status at the ROI.'
    supports: method
  - section: Original source P4-S2-C13
    page: 4
    quote: 'As these were very small ROIs, not large clusters, the distri-

      butions of percent lesions in the ROIs were highly bimodal,

      so an all or nothing approach was used: If a participant had

      a lesion that overlapped with the ROI in even one voxel, the

      participant was counted in the “lesion” group for that ROI.'
    supports: method
  - section: Original source P9-S1-C6
    page: 9
    quote: 'For overt naming, ROIs

      were selected in both the left and right motor cortex and STS.'
    supports: method
  - section: Original source P12-S1-C11
    page: 12
    quote: 'Like

      other recent studies, we restricted our analysis to correct trials

      only in part to minimize these effort effects.'
    supports: limitation
  - section: Original source P13-S1-C5
    page: 13
    quote: 'Finally, our study

      excluded participants with severe anomia, who could not

      correctly name at least 10% of the trials in the scanner.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: SkipperKallal2017
  proposal_id: R003
  review_status_sha256: 29a1d4527fb97ef9ea2105a33fb9993d68b82a177bf207007e777215ff20e05d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
        A/passages.json: be3c45153928ddafaa04e0fb6403c3b0a97b6644ef134920e0f8aef83b7a7ec6
        A/raw.json: f68f9788c6726247db084e9d6662063d8b28ba77d34364b4a35ad2e0336bca52
        A/source-units.json: 3fb7d038469738493922557e6ca8ecead84ef3583c4f279b7bae83a5f315206b
        A/full-source-units.json: 2abd56457d9a6df2f7f60ec369123f063d5dd5ffabb7318fb49b9ae28efaacea
        A/meta.json: 3476cfea5492a904981aae2d63398faf3fce3f70b4b52ed9ec94dd45c30e83d7
        A/table-images/TABLE-1-page-3-1.png: 7811d41d18460c864936684fd31d26ec2faefc64bb37cd6aaa96357210fffa7b
        A/table-images/page-10.png: d7a54261a2ea49d99d78ddd9bb90a4082fb32977ed6dc2c89123a4e00fc125cf
        A/table-images/page-3.png: 16322039b21296af5488726393a4f6b442dc692ba183b87b69c28522aeff7bf6
        A/table-images/page-6.png: b0c4ac1afae50c94150fa0a7895b88e004e78d4ad1dc4d3a0b3017e15187e878
        A/table-images/TABLE-4-page-8-1.png: 223a1ba2a9174070fc5f0bf0e2d3a41f7af12170251a61ebef851984dbc95dba
        A/table-images/page-7.png: 9db1998483e871108b4a1ea60802fc46d4dd596e76f7a2fbe94a5b511dae145e
        A/table-images/page-5.png: ff0d2fe7a6f4fc709768fb05fce853fdae9c3ef699ab46aa34861faa7d58e428
        A/table-images/TABLE-3-page-6-1.png: 996ee3f9d8bd393e407ee8fcc3682928ac5b81be80c7f2fe78f1f7dbb4f08156
        A/table-images/page-8.png: 00be3b1a60dcd6f13cf382bd600ff8597dfe9a174cfe3c0f8fb04481d131169c
        A/table-images/manifest.json: be6c2b617d969fcf0c3eb5c73469721b6833c6126c895af07e9037bed351f360
        A/table-images/TABLE-5-page-10-1.png: 0b1332d4ff2177161c6d993758ec65a6752c67e2b7e0ede82233c1bd4a8a755b
        A/table-images/TABLE-3-page-7-1.png: aa664038dca876ee6a30c83c5bda5876a111bee73df77928c15b0b12a208fe41
        A/table-images/TABLE-2-page-5-1.png: 5ddd5a43a46706e655c8194ba56d70cc9cc7afad9bda296a85a2926677025cf0
        A/table-images/TABLE-6-page-10-2.png: 0b1332d4ff2177161c6d993758ec65a6752c67e2b7e0ede82233c1bd4a8a755b
        A/clauses/window-11/raw.json: e64642775cd0812205b828f8b90c6106dc13d17ee76536aa664151b562d3d2fe
        A/clauses/window-11/prompt.txt: 42137f1067f55da679a0fb69627373e0c99d7565e33f8c9113c7af512cc42ae3
        A/clauses/window-11/meta.json: ce05a8d6e53f1c32c8681d1e5c0d3350dfd63d6b16356a2efd6105d3bc53a7dc
        A/clauses/window-10/raw.json: fdc72423a2c66f35bb0daac20418971ae982a95dabb8b6d758f627e8ec9c5a35
        A/clauses/window-10/prompt.txt: e997b5259acc142743a62abc449bc9cd6dbfbc0489c4eba01d3581a86a0039fd
        A/clauses/window-10/meta.json: 3929e519d3e488775e6b89c42891ede3cabce22e42ac49adf6ea3f1d7e0b47da
        A/clauses/window-03/raw.json: 3fb106e9c714d296b40302679370841e192e39fa7ceb9b8d282764897c057339
        A/clauses/window-03/prompt.txt: 4b2aaa9baf13ff85796b418c608e6dc3e8c05421ce2c03fa365185c9ca02154c
        A/clauses/window-03/meta.json: 61e4f5e4270422b469a4b9acbed833210bad93b19a26b66d99edfc2b29381094
        A/clauses/window-04/raw.json: 18a06eddbf795cda538dee7fa92187df8de99a9b8f77c7a00c6050f8dd73f4f9
        A/clauses/window-04/prompt.txt: da2653c7dbd8180707e58329db14f76ac99e821da2db2d4e7b17ae5ce463a1bd
        A/clauses/window-04/meta.json: 74827717a9c8af8379c606baec255801ffab93e97018794fe32157752ea8a1dc
        A/clauses/window-05/raw.json: 8a039caa9b5ac4e219810879853395507e60b810f83fe3bf7f1820060de05be0
        A/clauses/window-05/prompt.txt: bb0f1c722eaff64bd56230255754d2843133b49b505f6959dc0dc4b25795f46c
        A/clauses/window-05/meta.json: f2bf0b5c73f1d7bc366e7ca8ed6a0fc494ab47f2fbc924d437bb9892e63d0970
        A/clauses/window-02/raw.json: 85a875bad23b30c542336e316b4121ec77839dd9faf7ab3bef02705c2ef40f27
        A/clauses/window-02/prompt.txt: 92ce2b5ae2d0282a059459d7868530940bb381bae5c801061427a7cd58b91e8d
        A/clauses/window-02/meta.json: 007270081c5673b56f73c02fb777cd55176b90685d3ead62a87f709273a1bef2
        A/clauses/window-09/raw.json: 666a6d77e667d363f8bf854a57d6bc9f60786aff24fba9b8cf11fa80c20a54ef
        A/clauses/window-09/prompt.txt: e700b993f89550a491e185448e76b08a871c12da7d4681f6552a6b9e730495f0
        A/clauses/window-09/meta.json: accbc18dfdbcb2273d4cf641e7ef5dc90749069e2929a4c14d561f462c0c98fb
        A/clauses/window-07/raw.json: 9ddf60cc86d13026f137d87ba527f158b4d5c706930d445e05a104b539e60377
        A/clauses/window-07/prompt.txt: 0645a149f5b23ad50572f9ed94fe9e4ca912ead138570ca142f7197981c4402c
        A/clauses/window-07/meta.json: 7f947c9bf292349487d629c8268613ad7aa78140407afb1584b2ceae4427af62
        A/clauses/window-01/raw.json: 39fdd5a96d1f98617f4ad6e4d9fe1d28ce0d865b760ee1fdea19277169c2fcd6
        A/clauses/window-01/prompt.txt: a3a29418c424d781d37e8e3bb470ca42d638db11f446eaad0184d2c90fc9f2df
        A/clauses/window-01/meta.json: 4a20ea3a2288cfdb5bf7cd845509aaa2417f98803b1088f0ca913cd31cd87713
        A/clauses/window-06/raw.json: b4663fd798c0459d0df540906a94b28f88fba35c2df85211d801e046496e5705
        A/clauses/window-06/prompt.txt: b7f806ce8c361a6251bb00e942aca02c45271420be99f457ca4c37ccd292ca4f
        A/clauses/window-06/meta.json: 677f7618590661c45818f90201a81333ea4d3c0d53044b3b5533f37fe5c07bbc
        A/clauses/window-08/raw.json: 620bd370ebedc70dc4c20ecf9fe54d7822d2c90033c10ac1360e75265faf9873
        A/clauses/window-08/prompt.txt: 118a09e3c24e6ef85cf8ff53a9aa21699dd65d09f837f4f6349c4bd5cfbc16f3
        A/clauses/window-08/meta.json: 05957156d58aef077a79803fc9ab1feb7c4813d999b126d1149ce8cbd424e128
        A/tables/TABLE-4-page-8-5/raw.json: 382ed8b031d79e6711f41e4441258b1eecbaa27717af3fe5cfca1a1abdd3ae6d
        A/tables/TABLE-4-page-8-5/prompt.txt: 5ea58467381a557367e5282d8e6ff27cd09692395593b50cd389330dfe94485f
        A/tables/TABLE-4-page-8-5/meta.json: af06049f577f62439696c76d3f99c098b18cb80d01478e2bbcb384fbab24ed92
        A/tables/TABLE-5-page-10-6/raw.json: c27aa7f0456e8970fbb27ea501eabba8af9ce735c332dbf46059e55a7d359eec
        A/tables/TABLE-5-page-10-6/prompt.txt: 00af5d7f4b0bc41947cef3eb7607697cc3472f9bb7ca684fb9f32fc453b4f9cd
        A/tables/TABLE-5-page-10-6/meta.json: 58f02c2d551d7cbd8533ab8878e869ae5c111620dc6927e4f518f1cf6d502c10
        A/tables/TABLE-2-page-5-2/raw.json: a7f6197dca8879a1f5844f485ca38a201fdf2b86bea3c3deacca045df8fd9165
        A/tables/TABLE-2-page-5-2/prompt.txt: 66c523c23ec4fd5c45704db85479f10f6b944d9dd0156fd5236844ffd274a75f
        A/tables/TABLE-2-page-5-2/meta.json: e7777aa07e980c5844f702e93d653dc69a36820b8d11326f7939137573956bf1
        A/tables/TABLE-3-page-6-3/raw.json: 3bc443376b1d18937ef12818f1ad1bbea04e86bfe02c54fda43b5d2d06e32211
        A/tables/TABLE-3-page-6-3/prompt.txt: c30eb158fd4d9933785ff70d323728c405ca961715cc5398abf47f8707c69801
        A/tables/TABLE-3-page-6-3/meta.json: 572ef814f7bfca33082ca515febf0c5c5ea59aa1bdcc82d1822a92f556d342f7
        A/tables/TABLE-1-page-3-1/raw.json: 60d668b601831b56f08a847ec67f562346c453f9a6a71ce702a9f45e21b8f40b
        A/tables/TABLE-1-page-3-1/prompt.txt: 2021109fdf7dde20d9b2ca3307c2038aadc0cbc34c5e8b4013236d446b370706
        A/tables/TABLE-1-page-3-1/meta.json: e7352874b1d4621434cde9192485eb652418a69177856b3f60fa1e26b0443a87
        A/tables/TABLE-3-page-7-4/raw.json: beabb62be3ba1584365e6dfae9f4ad5ebea4c0f15f13195f56fcb9f1cec2a1f8
        A/tables/TABLE-3-page-7-4/prompt.txt: c93c8f88b777a7a0a8b9d4fec488f06e570ce4a454e22e99992a10b4f165be72
        A/tables/TABLE-3-page-7-4/meta.json: 47bf9a4e84916ab3bded1f1e373b1db6d0acb5ba3f121575dd08ca772098883a
        A/tables/TABLE-6-page-10-7/raw.json: 0d40084b5b804a43262b78097fecb0ce59c13b13d8811df16188c9e278f011eb
        A/tables/TABLE-6-page-10-7/prompt.txt: 20aa3f48fa00dc9094d678fec2f93f01e0809bcc725d08c97899355ed0827c63
        A/tables/TABLE-6-page-10-7/meta.json: 25ea209a262d555a715d2866d432902a1695bf423a1fb6540be36fdb55e1f8e1
        B/passages.json: be3c45153928ddafaa04e0fb6403c3b0a97b6644ef134920e0f8aef83b7a7ec6
        B/raw.json: 83336d615c799626f9674934924a083dd8742a5f658fdf98099abaf20746ac79
        B/source-units.json: 3fb7d038469738493922557e6ca8ecead84ef3583c4f279b7bae83a5f315206b
        B/full-source-units.json: 2abd56457d9a6df2f7f60ec369123f063d5dd5ffabb7318fb49b9ae28efaacea
        B/meta.json: a0f0ab3934afe1bfaf07bad908e6d160cd64540ebef80e249e94ef108a16c49c
        B/table-images/TABLE-1-page-3-1.png: 7811d41d18460c864936684fd31d26ec2faefc64bb37cd6aaa96357210fffa7b
        B/table-images/page-10.png: d7a54261a2ea49d99d78ddd9bb90a4082fb32977ed6dc2c89123a4e00fc125cf
        B/table-images/page-3.png: 16322039b21296af5488726393a4f6b442dc692ba183b87b69c28522aeff7bf6
        B/table-images/page-6.png: b0c4ac1afae50c94150fa0a7895b88e004e78d4ad1dc4d3a0b3017e15187e878
        B/table-images/TABLE-4-page-8-1.png: 223a1ba2a9174070fc5f0bf0e2d3a41f7af12170251a61ebef851984dbc95dba
        B/table-images/page-7.png: 9db1998483e871108b4a1ea60802fc46d4dd596e76f7a2fbe94a5b511dae145e
        B/table-images/page-5.png: ff0d2fe7a6f4fc709768fb05fce853fdae9c3ef699ab46aa34861faa7d58e428
        B/table-images/TABLE-3-page-6-1.png: 996ee3f9d8bd393e407ee8fcc3682928ac5b81be80c7f2fe78f1f7dbb4f08156
        B/table-images/page-8.png: 00be3b1a60dcd6f13cf382bd600ff8597dfe9a174cfe3c0f8fb04481d131169c
        B/table-images/manifest.json: b9d37dd36f4d3ad5a2151c537e84c182ca6cfc7e17bc7aca8fae6e0afc786a71
        B/table-images/TABLE-5-page-10-1.png: 0b1332d4ff2177161c6d993758ec65a6752c67e2b7e0ede82233c1bd4a8a755b
        B/table-images/TABLE-3-page-7-1.png: aa664038dca876ee6a30c83c5bda5876a111bee73df77928c15b0b12a208fe41
        B/table-images/TABLE-2-page-5-1.png: 5ddd5a43a46706e655c8194ba56d70cc9cc7afad9bda296a85a2926677025cf0
        B/table-images/TABLE-6-page-10-2.png: 0b1332d4ff2177161c6d993758ec65a6752c67e2b7e0ede82233c1bd4a8a755b
        B/clauses/window-11/raw.json: 3de101b6aca8fadd660ac876663b323b493a06bbb67c6a713c5816c6bbc3b1f3
        B/clauses/window-11/prompt.txt: 42137f1067f55da679a0fb69627373e0c99d7565e33f8c9113c7af512cc42ae3
        B/clauses/window-11/meta.json: 09c566f97d5af7caa5fc186954b22caaa6025cd9aa62e7a9c6b8d57886069ebb
        B/clauses/window-10/raw.json: ac1a35c61a5daf26b38d121772b293f2f377142a190fa8eb506d96ad1f5aa552
        B/clauses/window-10/prompt.txt: e997b5259acc142743a62abc449bc9cd6dbfbc0489c4eba01d3581a86a0039fd
        B/clauses/window-10/meta.json: a17308256f8a232338c35b5eda347bc4c47723a9c03915910b4b4fcdf5bee937
        B/clauses/window-03/raw.json: e9ab41a9bd641a28bc9106f951475611627c3655cc9b3e46dec0503a211a16a8
        B/clauses/window-03/prompt.txt: 4b2aaa9baf13ff85796b418c608e6dc3e8c05421ce2c03fa365185c9ca02154c
        B/clauses/window-03/meta.json: c57223839fd6b094d0e2c8374f938a6365baad39337bbbcd0eeae522eaceb22b
        B/clauses/window-04/raw.json: 5825d61345d1ff2e73b7203cde4320d008b20a2ca479c208ab78d5483a2b2cec
        B/clauses/window-04/prompt.txt: da2653c7dbd8180707e58329db14f76ac99e821da2db2d4e7b17ae5ce463a1bd
        B/clauses/window-04/meta.json: c8e910a7574171c47af11a4a87bdece22f55642bbc94050023189584243d2cdc
        B/clauses/window-05/raw.json: 7f75f16e1bb815e555d0848cf28fd8b2cb8db62ae7e719fc4733fb533d8076b0
        B/clauses/window-05/prompt.txt: bb0f1c722eaff64bd56230255754d2843133b49b505f6959dc0dc4b25795f46c
        B/clauses/window-05/meta.json: d18a132a50e6f259b527b9064854f6543aa6c75be7bf2da6b3160055bb78d6a8
        B/clauses/window-02/raw.json: 187f5004e4288c086ce28d5499e5b17154071837cdaabae11955de6c826c91c4
        B/clauses/window-02/prompt.txt: 92ce2b5ae2d0282a059459d7868530940bb381bae5c801061427a7cd58b91e8d
        B/clauses/window-02/meta.json: 2d88b62fdd8b8a076c117d772fea5e4f89ba83a6e7e5c615461db85771ef7724
        B/clauses/window-09/raw.json: a7f81086c977a36ce74c11e0d47fba138d7f0533681866fd3db8ed2855f0efd5
        B/clauses/window-09/prompt.txt: e700b993f89550a491e185448e76b08a871c12da7d4681f6552a6b9e730495f0
        B/clauses/window-09/meta.json: 41e9a45e01370ff93ca03016d24f9c464813a0259ee5bd755dfee76af05d5625
        B/clauses/window-07/raw.json: 3bbfb203d7f67a8c82ff38f843f46a8865019cae4a49b51efcc9c6a8f87fb340
        B/clauses/window-07/prompt.txt: 0645a149f5b23ad50572f9ed94fe9e4ca912ead138570ca142f7197981c4402c
        B/clauses/window-07/meta.json: 3c7bdcc628401543823b187853fbfea3fda4920f66170c668514b6b844ab9a9b
        B/clauses/window-01/raw.json: 7ac29cf6a216a67c865cfba26c1eec3388ae08cfcd712bc815f262f07523d3fb
        B/clauses/window-01/prompt.txt: a3a29418c424d781d37e8e3bb470ca42d638db11f446eaad0184d2c90fc9f2df
        B/clauses/window-01/meta.json: 44b9db468a2af8d3b405a1543005a167b79183f4edd94dffd36b2f9c9433f22c
        B/clauses/window-06/raw.json: 9ea8043292f8383b6bd7bb65b2ccd939738e8fe8ee98174a65d057ef89248f43
        B/clauses/window-06/prompt.txt: b7f806ce8c361a6251bb00e942aca02c45271420be99f457ca4c37ccd292ca4f
        B/clauses/window-06/meta.json: e1cf5b462c8d4d1365d662ae1d2698182f0d34a83abde4ba5201b82e28fcfc19
        B/clauses/window-08/raw.json: 2ef7738e1b7bbb2095d09463a00372db03c8f38140f926a142f5533224e999a7
        B/clauses/window-08/prompt.txt: 118a09e3c24e6ef85cf8ff53a9aa21699dd65d09f837f4f6349c4bd5cfbc16f3
        B/clauses/window-08/meta.json: 064bb3b7f0dff89ac75a6ee1f341facbc6f43af06ebbd27e0bab35a0478a1267
        B/tables/TABLE-4-page-8-5/raw.json: 1c75417a30d57c4506e95757864c63bceb9b403f4d32c2bdf954e247bf7f37b4
        B/tables/TABLE-4-page-8-5/prompt.txt: 5ea58467381a557367e5282d8e6ff27cd09692395593b50cd389330dfe94485f
        B/tables/TABLE-4-page-8-5/meta.json: e6fae6ae88d14eca63d327b91c1cc22d4bc0562ed5de3f943d0891667a23eade
        B/tables/TABLE-5-page-10-6/raw.json: 78929af5ec0ff2b6953669d59eb9870eb5eb11abbadb7652183bddef21f9305f
        B/tables/TABLE-5-page-10-6/prompt.txt: 00af5d7f4b0bc41947cef3eb7607697cc3472f9bb7ca684fb9f32fc453b4f9cd
        B/tables/TABLE-5-page-10-6/meta.json: 86a729dc6997b9080e58bf82700ff571a2c95dbb71c245361a262a752f734783
        B/tables/TABLE-2-page-5-2/raw.json: 52e4f47bb099b386b05140017ad8a13afb9308aa00f5df67b7d4cd1ba32d432f
        B/tables/TABLE-2-page-5-2/prompt.txt: 66c523c23ec4fd5c45704db85479f10f6b944d9dd0156fd5236844ffd274a75f
        B/tables/TABLE-2-page-5-2/meta.json: e9cd59d42364a5eba9a47c2a9dc265b87cc2c530dc5dfe6bf896e4984692e228
        B/tables/TABLE-3-page-6-3/raw.json: 74a24e03ea4aadecb99c86a6dcff8115c381ef64874766187cc759151b6a0fbf
        B/tables/TABLE-3-page-6-3/prompt.txt: c30eb158fd4d9933785ff70d323728c405ca961715cc5398abf47f8707c69801
        B/tables/TABLE-3-page-6-3/meta.json: 0c6a7f7ed899a8009ee6407d9157df4c8f6452de278d713eb3744d200dce88f9
        B/tables/TABLE-1-page-3-1/raw.json: 60d668b601831b56f08a847ec67f562346c453f9a6a71ce702a9f45e21b8f40b
        B/tables/TABLE-1-page-3-1/prompt.txt: 2021109fdf7dde20d9b2ca3307c2038aadc0cbc34c5e8b4013236d446b370706
        B/tables/TABLE-1-page-3-1/meta.json: a9af2e9e25f3ed2f24c4f814170b0e28d533e286af92a35b47b4b1065b3f82f5
        B/tables/TABLE-3-page-7-4/raw.json: 9aacd41c011abdd77e4066ab311562f926d4bec6060ae4e410585234b8f93c41
        B/tables/TABLE-3-page-7-4/prompt.txt: c93c8f88b777a7a0a8b9d4fec488f06e570ce4a454e22e99992a10b4f165be72
        B/tables/TABLE-3-page-7-4/meta.json: dafefb2d0cea7b01fb02acfe2dbb83fc2f3540a30e3e8580f311204947bea254
        B/tables/TABLE-6-page-10-7/raw.json: 79a2e37e8fb366dbda82ec3d60edcbf2e61a5c35101061d35fd46a8fe3555baa
        B/tables/TABLE-6-page-10-7/prompt.txt: 20aa3f48fa00dc9094d678fec2f93f01e0809bcc725d08c97899355ed0827c63
        B/tables/TABLE-6-page-10-7/meta.json: 48b0a40c4ea608c20d222d81613d15b2acff6441aeec30e11c0fa68f313216c7
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
      pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017
      source_status_sha256: 71081048af3ff874c32c67b6ed9a6e877f785ed51c989d0903ef3d8f11cf90ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: lesions in motor cortex
    outcome:
      text: increased right motor cortex activity
    analysis_label: Lesion location effect on overt naming activity
    relation: association
    evidence_ids:
    - P1-S1-C13
    - P9-S2-C11
    - P13-S1-C8
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
      pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017
      source_status_sha256: 71081048af3ff874c32c67b6ed9a6e877f785ed51c989d0903ef3d8f11cf90ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P4-S3-C6
      - Result passage disposed without unit P4-S3-C7
      - Accounting without a linked unit P9-S1-C12
      - Accounting without a linked unit P9-S1-C13
      - Accounting without a linked unit P9-S1-C14
      - Accounting without a linked unit P9-S2-C4
      - Accounting without a linked unit P9-S2-C5
      - Unaccounted source passage P9-S1-C13
      - Unaccounted source passage P9-S2-C4
      - Unaccounted source passage P9-S1-C12
      - Unaccounted source passage P9-S2-C5
      - Unaccounted source passage P9-S1-C14
      - 'window 8: invalid/duplicate disposition P9-S3-C11'
      - Result passage disposed without unit P11-S1-C9
      - Result passage disposed without unit P12-S1-C3
      - Unresolved source passage P12-S1-C3
      - Result passage disposed without unit P12-S4-C3
      - Result passage disposed without unit P13-S2-C7
      - Result passage disposed without unit P14-S1-C5
      - Result passage disposed without unit P14-S2-C7
      - Result passage disposed without unit P14-S2-C8
      - Accounting without a linked unit P14-S3-C10
      - Accounting without a linked unit P14-S3-C2
      - Accounting without a linked unit P14-S3-C8
      - Accounting without a linked unit P14-S3-C9
      - Unaccounted source passage P14-S3-C8
      - Unaccounted source passage P14-S3-C2
      - Unaccounted source passage P14-S3-C10
      - Unaccounted source passage P14-S3-C9
      unattached_null_or_qualifier_ids:
      - P13-S2-C7
      - P14-S2-C8
      - P14-S3-C10
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 256
      unselected_timing_passages:
      - P2-S4-C4
      - P3-S1-C7
      - P9-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S3-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P14-S2-C7
        - P14-S2-C8
        - P14-S2-C9
        - P14-S2-C10
        - P14-S2-C11
        - P14-S2-C12
        - P14-S2-C13
        - P14-S2-C14
        - P14-S3-C3
        - P14-S3-C5
        - P14-S3-C6
        - P14-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P4-S1-C13
        - P4-S2-C15
        - P4-S3-C2
        - P9-S1-C8
        - P9-S1-C11
        - P9-S2-C3
        - P9-S2-C5
        - P9-S2-C8
        - P10-S1-C4
        - P11-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-3-page-7-4
      - TABLE-4-page-8-5
      - TABLE-5-page-10-6
      - TABLE-6-page-10-7
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-5-page-10-6
      - TABLE-6-page-10-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S3
        - P4-S4
        - P7-S1
        - P8-S1
        - P9-S1
        - P9-S2
        - P10-S1
        - P11-S1
        - P12-S1
        - P13-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
      source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017
      source_status_sha256: 71081048af3ff874c32c67b6ed9a6e877f785ed51c989d0903ef3d8f11cf90ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: States lesion size is positively associated with greater right hemisphere
        activity.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Describes effects of IFG and motor cortex lesions on contralateral activity.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Links right motor activity to better naming specifically when left motor
        cortex is lesioned.
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to a prior meta-analysis.
    - source_id: P1-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to a prior meta-analysis.
    - source_id: P3-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PNT scoring method.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic group comparison.
    - source_id: P4-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Between-group contrast description.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Between-group contrast description.
    - source_id: P4-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Within-group contrast description.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Within-group contrast description.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Within-group contrast description.
    - source_id: P4-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Between-group contrast description.
    - source_id: P4-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Between-group contrast description.
    - source_id: P4-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Within-group contrast description.
    - source_id: P4-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Within-group contrast description.
    - source_id: P4-S3-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to lesion size analysis.
    - source_id: P5-S2-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Describes right hemisphere activity predicted by larger lesions during
        covert naming.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Describes right hemisphere activity predicted by larger lesions during
        overt naming.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes: []
      reason: 'Null finding: no areas where activity was predicted by smaller lesions.'
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continuation of null finding from P5-S2-C4.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ROI removal.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports left insula lesion effect on naming that disappears with lesion
        size control.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null relationship between several left ROIs and naming performance.
    - source_id: P9-S1-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Reports no difference for left IPS lesions in covert naming.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 7
      reason: Reports left insula lesions led to less activity in right MFG and PTr.
    - source_id: P9-S1-C14
      disposition: represented
      result_indexes:
      - 8
      reason: Reports left POp lesions led to less activation in right dorsal POp.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no significant relationship between right peak activation and
        naming.
    - source_id: P9-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no relationship for left insula group.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for overt naming ROIs in whole-volume analysis.
    - source_id: P9-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to ROI analysis.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Marginally significant relationship between left insula lesions and
        left POp activity.
    - source_id: P9-S2-C11
      disposition: represented
      result_indexes:
      - 10
      - 13
      reason: Reports effects of left motor and STS lesions on right motor cortex
        activity.
    - source_id: P9-S2-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Null relationship between right motor activity and naming in intact
        left motor group.
    - source_id: P9-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Positive association between right motor activity and naming in left
        motor lesion group.
    - source_id: P9-S3-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right motor activity and naming result.
    - source_id: P9-S3-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right motor activity and naming result.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Weak evidence for perilesional recruitment in left dorsal frontal cortex.
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Restatement of left insula lesion and left POp activity relationship.
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on perilesional compensation.
    - source_id: P12-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of lesion size effect on right hemisphere activity.
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: States larger lesions showed greater activity in homotopic right hemisphere
        areas.
    - source_id: P12-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that bilateral visual cortex activity related to lesion
        size.
    - source_id: P12-S3-C10
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Reports left POp and insula lesions led to decreased activity in right
        PTr and MFG.
    - source_id: P12-S3-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Reports right frontal activity was not related to naming ability.
    - source_id: P13-S1-C8
      disposition: represented
      result_indexes:
      - 2
      - 13
      reason: Restates left motor cortex lesions led to greater right motor cortex
        activation.
    - source_id: P13-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Restates right motor overactivation associated with better naming in
        left motor lesions.
    - source_id: P14-S3-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of right motor activity and naming result.
    unresolved_coverage:
    - source_id: P5-S2-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S2-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C9
    - P1-S2-C10
    - P3-S1-C13
    - P3-S2-C10
    - P4-S3-C6
    - P4-S3-C7
    - P4-S3-C8
    - P4-S3-C9
    - P4-S3-C10
    - P4-S3-C11
    - P4-S3-C12
    - P4-S3-C13
    - P4-S3-C14
    - P4-S3-C17
    - P5-S2-C4
    - P9-S1-C1
    - P9-S1-C5
    - P9-S2-C6
    - P9-S2-C9
    - P9-S2-C14
    - P9-S3-C2
    - P9-S3-C9
    - P9-S3-C10
    - P9-S3-C13
    - P11-S1-C6
    - P11-S1-C9
    - P12-S1-C3
    - P12-S1-C5
    - P12-S1-C10
    - P12-S2-C3
    - P12-S4-C3
    - P13-S1-C4
    - P13-S2-C7
    - P14-S1-C5
    - P14-S2-C7
    - P14-S2-C8
    - P14-S3-C2
    - P14-S3-C8
    - P14-S3-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    - TABLE-3-page-7-4
    - TABLE-4-page-8-5
    - TABLE-5-page-10-6
    - TABLE-6-page-10-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C8
      - P3-S1-C12
      recruited_sample:
      - P3-S1-C7
      - P3-S1-C12
      eligibility:
      - P3-S1-C9
      - P3-S1-C10
      imaging_provenance:
      - P3-S1-C2
      imaging_timing:
      - P3-S1-C9
      outcome_timing:
      - P3-S3-C12
      outcome_definition:
      - P3-S3-C11
      - P3-S3-C13
      validation: []
      analysis_restrictions:
      - P3-S3-C10
      - P12-S1-C11
      - P13-S1-C5
      dependent_variable_statement:
      - P4-S2-C6
      - P4-S3-C16
      - P9-S1-C7
      - P9-S2-C3
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C11
      - P3-S1-C13
      - P3-S2-C11
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S3-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P14-S2-C7
      - P14-S2-C8
      - P14-S2-C9
      - P14-S2-C10
      - P14-S2-C11
      - P14-S2-C12
      - P14-S2-C13
      - P14-S2-C14
      - P14-S3-C3
      - P14-S3-C5
      - P14-S3-C6
      - P14-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P4-S1-C13
      - P4-S2-C15
      - P4-S3-C2
      - P9-S1-C8
      - P9-S1-C11
      - P9-S2-C3
      - P9-S2-C5
      - P9-S2-C8
      - P10-S1-C4
      - P11-S1-C3
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
      pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
      review_sha256: 29a1d4527fb97ef9ea2105a33fb9993d68b82a177bf207007e777215ff20e05d
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
      - P1-S1-C13
      - P9-S2-C11
      - P13-S1-C8
      source_result: During overt naming, lesions in the left motor cortex were associated
        with significantly greater activity in the right motor cortex (t(36) = 2.91,
        P < 0.01), controlling for total lesion volume. Furthermore, this increased
        right motor activity was positively associated with naming performance only
        in participants with left motor lesions (t(21) = 3.67, P = 0.001), whereas
        no such relationship was found in participants with intact left motor cortex.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the specific ROI-based
            regression analysis described in P9-S2-C11 and P13-S1-C8, which tests
            the effect of left motor cortex lesion status on right motor cortex activity
            during overt naming, controlling for lesion volume. It is distinct from
            the whole-brain lesion size analysis or the covert naming analyses.
          source_ids:
          - P9-S2-C11
          - P13-S1-C8
          - P4-S3-C2
        direction:
          answer: fits
          reason: 'The draft correctly captures the direction of the association:
            left motor lesions are associated with increased right motor activity,
            and this increased activity is associated with better naming performance
            (positive association) specifically in the lesioned group. The draft does
            not conflate this with the null finding in the intact group or the negative
            findings in other regions.'
          source_ids:
          - P9-S2-C11
          - P9-S3-C2
          - P13-S1-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesion status in the left
            motor cortex (defined by overlap with a control-derived ROI). The outcome
            is right motor cortex activity. The patient measurement is template_lesion_overlap,
            as the analysis groups patients based on whether their lesion overlapped
            with the ROI (P4-S2-C13), rather than using patient-specific diffusion
            tractography or continuous lesion load for this specific ROI comparison.
            The method (LSM/regression) and population (chronic aphasia) are accurate.
          source_ids:
          - P4-S2-C12
          - P4-S2-C13
          - P9-S1-C6
          - P9-S2-C11
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the association
            between right motor activity and naming performance was observed only
            in the group with left motor lesions, not in the intact group. It also
            notes the control for total lesion volume. The distinction between the
            two subgroups (N=24 vs N=15) is preserved.
          source_ids:
          - P9-S2-C14
          - P9-S3-C2
          - P13-S2-C7
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the restriction to correct
            trials and the exclusion of severe anomia patients, which are material
            caveats affecting the generalizability of the finding. No other material
            caveats that would change the interpretation of this specific association
            are omitted.
          source_ids:
          - P12-S1-C11
          - P13-S1-C5
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
      id: R003
      exposure:
        text: lesions in motor cortex
      outcome:
        text: increased right motor cortex activity
      analysis_label: Lesion location effect on overt naming activity
      relation: association
      evidence_ids:
      - P1-S1-C13
      - P9-S2-C11
      - P13-S1-C8
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
        pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
        source_review: _compare/relationships-2026-11-16/review-current/SkipperKallal2017
        source_status_sha256: 71081048af3ff874c32c67b6ed9a6e877f785ed51c989d0903ef3d8f11cf90ce
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 843da09bc2399ec81f29918a5df111d5234014482a1d738f20d68094decac1dc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C8
          page: 3
          text_layer_sha256: 843da09bc2399ec81f29918a5df111d5234014482a1d738f20d68094decac1dc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Ten partic-

          ipants were then excluded based on fMRI task performance

          (<10% accuracy) resulting in a final sample of 39 participants

          in the aphasia group.'
        anchor_text: 'Ten partic-

          ipants were then excluded based on fMRI task performance

          (<10% accuracy) resulting in a final sample of 39 participants

          in the aphasia group.'
        excluded_fragments: []
        image_sha256: e9e76f00c9f2ef4946b59a66b45178b51260c3814381efe61893cc2334b3ed8c
        transcription: '. Ten partic-

          ipants were then excluded based on fMRI task performance

          (<10% accuracy) resulting in a final sample of 39 participants

          in the aphasia group'
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d65d430df4efa027c54f7e1fdb596d7e6536a809044a257b55600cfde05daadf
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: d65d430df4efa027c54f7e1fdb596d7e6536a809044a257b55600cfde05daadf
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants in the aphasia group were native English

          speakers and testing occurred at least six months after

          their stroke (mean chronicity = 52.9 months).'
        anchor_text: 'All participants in the aphasia group were native English

          speakers and testing occurred at least six months after

          their stroke (mean chronicity = 52.9 months).'
        excluded_fragments: []
        image_sha256: b66412a3a053a787f78e1cdcd69755f322afd566085c147e6530c242e09db4d9
        transcription: All participants in the aphasia group were native English speakers
          and testing occurred at least six months after their stroke (mean chronicity
          = 52.9 months)
      P13-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3a184b9634a52bfe71b5444f40fc423e8f052d0850fafc5e5e5863be59c159f2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cd382b3aa2d8e10e4436f6e2003e0302af91bb89b515450bbda4aba2bb1cad81
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P13-S1-C5
          page: 13
          text_layer_sha256: cd382b3aa2d8e10e4436f6e2003e0302af91bb89b515450bbda4aba2bb1cad81
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Finally, our study

          excluded participants with severe anomia, who could not

          correctly name at least 10% of the trials in the scanner.'
        anchor_text: 'Finally, our study

          excluded participants with severe anomia, who could not

          correctly name at least 10% of the trials in the scanner.'
        excluded_fragments: []
        image_sha256: 5feffde7a3df2efaaa09e2d148178bbbd56fb273be5fec4407bcfc34e0eae94d
        transcription: '. Finally, our study

          excluded participants with severe anomia, who could not

          correctly name at least 10% of the trials in the scanner'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'For overt naming, lesions in the left motor cortex were

    related to significantly greater activity in the right motor cor-

    tex, 𝑡(36) = 2.91, 𝑃< 0.01, while lesions in the left STS were

    associated with lower activity in right motor cortex, 𝑡(36) =

    −2.24, 𝑃< 0.05 (Figure 4).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
