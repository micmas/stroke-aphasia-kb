---
id: age_lyric_memory_interaction
name: age and lyric memory interaction
kind: predictor
findings:
- id: f1
  target: articulatory_quality
  target_kind: impairment
  claim: Elderly patients showed an increased articulatory performance when producing
    original, familiar lyrics compared with formulaic lyrics, whereas this difference
    was not confirmed in younger patients.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 17
    population: non-fluent aphasics (Broca's aphasia or global aphasia with prevailing
      expressive deficits)
    phase: not_reported
    time_post_onset: at least 3 months post-infarction (except one case)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (N=17)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient age used as a covariate in a repeated-measures
    ANOVA to assess its interaction with lyric type (original, formulaic, non-formulaic)
    on speech production. The effect of age was found specifically in the comparison
    between original and formulaic lyrics; Younger and elderly patients showed similar
    results in the production of novel lyrics. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S2-C6, two-model
    agreement, human verification pending): . At

    the time of testing, all patients were at least 3 months post-infarction,

    except in one case (Patient HS) Original text-layer quotation is preserved below.
    PDF image reading (P3-S2-C9, two-model agreement, human verification pending):
    All patients were classified as non-fluent aphasics, diagnosed with Broca''s aphasia
    (n = 10) or global aphasia with prevailing expressive deficits (n = 7) Original
    text-layer quotation is preserved below.'
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
    - proposed_concept:articulatory_quality
  citation: '@Stahl2011'
  source_passages:
  - section: Original source P9-S1-C15
    page: 9
    quote: "A contrast analysis revealed an inter-\naction of age with original and\
      \ formulaic lyrics [F(1) = 13.18,\nP = 0.003, partial \x022 = 0.49]."
    supports: claim
  - section: Original source P9-S2-C2
    page: 9
    quote: 'As can be seen in Table 5 and

      Fig. 5, the group of elderly patients showed a higher production

      of original, familiar lyrics as compared with novel lyrics.'
    supports: claim
  - section: Original source P9-S3-C6
    page: 9
    quote: 'The results show a signiﬁcant interaction of age

      and lyric memory (**P 5 0.01).'
    supports: claim
  - section: Original source P9-S2-C3
    page: 9
    quote: 'This dif-

      ference was not conﬁrmed in the younger group.'
    supports: claim
  - section: Original source P9-S3-C7
    page: 9
    quote: 'Only elderly patients showed an

      increased performance of original lyrics compared with formulaic

      lyrics.'
    supports: claim
  - section: Original source P3-S2-C2
    page: 3
    quote: 'Seventeen stroke patients were

      included in the study.'
    supports: sample
  - section: Original source P3-S2-C6
    page: 3
    quote: 'At

      the time of testing, all patients were at least 3 months post-infarction,

      except in one case (Patient HS).'
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: 'All patients were classiﬁed as non-ﬂuent aphasics, diagnosed with

      Broca’s aphasia (n = 10) or global aphasia with prevailing expressive

      deﬁcits (n = 7).'
    supports: sample
  - section: Original source P6-S2-C15
    page: 6
    quote: 'Data analysis

      Two speech–language pathology students and the experimenter (B.S.)

      independently rated the articulatory quality of the produced utter-

      ances, based on the digital sound ﬁles, with two raters for each pa-

      tient.'
    supports: method
  - section: Original source P6-S2-C16
    page: 6
    quote: 'Articulatory quality was denoted as the percentage of correct

      syllables in each condition.'
    supports: method
  - section: Original source P7-S1-C5
    page: 7
    quote: 'A repeated-measures ANOVA was performed

      based on the average scores for articulatory quality in each condition,

      including the factors modality (sung, spoken, spoken arrhythmic con-

      trol) and lyrics (original, formulaic, non-formulaic) with patients’ age

      and composite basal ganglia lesion scale as covariates.'
    supports: method
predictor_type: demographic
short_definition: Patient age used as a covariate in a repeated-measures ANOVA to
  assess its interaction with lyric type (original, formulaic, non-formulaic) on speech
  production.
assessment:
- articulatory quality (percentage of correct syllables)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Stahl2011
  proposal_id: R007
  review_status_sha256: 553002c43d943cc341de539abd58bf654c8468fb7efda1ffdcdb58eca7953c2d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
        A/passages.json: 36530580952acbb2a90a0937070a7300c1805268cf6af224866a9ff5e7c1cf3b
        A/raw.json: c7c802a7274bbc53cb606e9bbbd2382faf39f592f8e20dc8a46817c3d3c86e52
        A/source-units.json: ff5b65f8b79ae17d258443fc77748a1bfe7694110b3ee6e36f704dfdcd99198a
        A/full-source-units.json: fcb38a311e6c5f012692de1eddbb98f15aa6958a8b02cc45621da29dba1b1c55
        A/meta.json: c91772451eab7a3f924141c8163b577e87c53695852077b75ccb0c6c496745f6
        A/table-images/TABLE-1-page-3-1.png: 5b8d61d036783079458fc67dd765918ce6a23c689c9f6f666388a04659762a01
        A/table-images/TABLE-5-page-9-1.png: 6a9f089c54762fbf681e884340f0312ce03504f68bd727e8d6ac2e79e20f9020
        A/table-images/page-3.png: 5dfa2f348c2694ee6eb31f7bdbf3c1b1f84dc2542843773eecacd3bc1481fbf8
        A/table-images/page-6.png: 68a6d6a75a0bc5d2d0d64b4c5d601005ce57bdecfbb6b0b0a16d4d4272690d26
        A/table-images/TABLE-4-page-8-1.png: eb80ec4b35d4152a023f6641fc61eec3d0605be03b8500a36b9f0220c4df168c
        A/table-images/page-4.png: 90f3eb163a93a4b9ee2e38cefd3c224e1626833e77e2349d70809dddff6e8f6d
        A/table-images/page-9.png: 352ebb99b233518e96d363b60209c738d4f92bb6c8fe0974dfe7ec0943fb2345
        A/table-images/TABLE-3-page-6-1.png: 40fd82e34142cb315f2232c27e0a443e90249babf4102ec8efabb478255604de
        A/table-images/page-8.png: ea1b8bed5cb9c88dd375c62aa5e408677f3982bbd961ac865986b41d53a44253
        A/table-images/manifest.json: 32283794edd7eb5546c077f51227e48c0895b922b9bc9a6bd19314bdb1007eb3
        A/table-images/TABLE-2-page-4-1.png: 5bac72147782ef00b0a5479751f3f3f165824547049b882a6628b462f517d95d
        A/clauses/window-11/raw.json: b7969906d425db98c11913d3494e5aa6820fe496e028636fff748294a1c5001c
        A/clauses/window-11/prompt.txt: a082205ff170745cb92f8a5745e12f8a239e86fc368f74d48bf37276db1bd6f2
        A/clauses/window-11/meta.json: 4b617e497c64d228cb38c9c841645837dd306b481d78fabbcda74ca275b54242
        A/clauses/window-10/raw.json: fb756b9e764d14564bb69a3be5496987b42cd8aa166180d937789e86a2c7bc05
        A/clauses/window-10/prompt.txt: b7bc76b1374ad4334242011b6a6d85a8f7c5f9c17939b234ee74dbf9a67f1dad
        A/clauses/window-10/meta.json: e3ed362428572366a81101ec0cf491c342dead4f056efa92dc0e6a08344e26c8
        A/clauses/window-03/raw.json: 8b464d812574675467ee62c6b1d3683a6b8b79ee455a4f4d7e1be29a5526f933
        A/clauses/window-03/prompt.txt: dc6fa4ed0c38716bc6863c856747be5b361ff26bc9529c4777d91d803b6fdb2d
        A/clauses/window-03/meta.json: 6a9cd64266d9cbe42fe357f1c5046bc426f245fbb1c1feedc1182aa65cf4b9f4
        A/clauses/window-04/raw.json: 41ec9fcbdda0f54370ca49a894c487e6d25d70d7e270b09a26b8b6a08372f5f4
        A/clauses/window-04/prompt.txt: c5a93d19e87869b6b79bebcff0c3824beffe2b097cbe2be11094fb8541d59f42
        A/clauses/window-04/meta.json: 32fd46de47159a09aace1e1a11e763a96680620096c0c0a853d659da57949271
        A/clauses/window-05/raw.json: 038ed348870ec52da57423cbdc754baccdce12542862ab466cbdfe05fb3a8838
        A/clauses/window-05/prompt.txt: 59fcc1be44edf276f7e106bea1bdf60fbae725015f224a9494e754b35be0a4c3
        A/clauses/window-05/meta.json: 85e2e46af064544a2b95dc953a074d815c60fb6f2e23954143a219478b80fc19
        A/clauses/window-02/raw.json: 6a2d5804f56a5e1b8f912a3631cba8f838633c81dc0f005611efed572f43a47e
        A/clauses/window-02/prompt.txt: 6a4f7cfae698318ebed58ce51d82c466cb95a3a662fbd81c001f3ac87919eb39
        A/clauses/window-02/meta.json: 9a02b3a253a9a020a204cb25e1c4562655acae340a2506a2771a7410cd2b1336
        A/clauses/window-09/raw.json: 28e6b8d8c2edf973d4f7d8c2de4eba08d8b4e5baaec78ca8e47d369c3da00a0e
        A/clauses/window-09/prompt.txt: a8415c4e023d8a3e1ab40e27906d9cc29982dd73525272a1e57fc80a82edfcda
        A/clauses/window-09/meta.json: 1bc18e5c9b48c84f69fbfb441fabc5853ceafd527bb258b667623be11932dad6
        A/clauses/window-07/raw.json: e7c8faa850a1cc4a82c97f17258daaa264b4fa59c885ee91f53d686cdec01d71
        A/clauses/window-07/prompt.txt: d6d5f9ab21bc55081b0c4034ce067847194d4de353f9a8daae9fab7d78e86d28
        A/clauses/window-07/meta.json: 6f86108ee8ad20e205d04ef8bf0d9c527a405b2091024a98df927e8a3aae27a9
        A/clauses/window-01/raw.json: 4ba62e45a67ca72c0382c76863e817bd9553bd8aeccb88e6684d20a7510afed1
        A/clauses/window-01/prompt.txt: d5f72bc07406dabe1b6f2bdb2e624b4e4eda405307d85841a8d89fa5390cecd8
        A/clauses/window-01/meta.json: bc245cdfb8c0ff5ec9d5f44a27ffd3648c0c682f73264634d397fd4735d3b96f
        A/clauses/window-06/raw.json: 57c206d4a42796123b88d826551216b42dc73c7c46d8685ac299de458a6aea2c
        A/clauses/window-06/prompt.txt: 7efb4eeb0da4e0a2a3581909483da5fd1f7bb916299958bd1047ccb7af6fe263
        A/clauses/window-06/meta.json: e04ffe735b3c95d7387dfef6984c6bb3a2d634b0e266240345723f285e0d6a38
        A/clauses/window-08/raw.json: 15f277f5262004a5e48248307d616fae5c4897658e4301d88e5b88e68d8df85f
        A/clauses/window-08/prompt.txt: 0774e111bd63e48eaa428cfdc3465deeacfa25e79c5a26f38e8dd98f32349ba9
        A/clauses/window-08/meta.json: f6bcc005046968c5a50fd3dbae279ed0c2c8a7fa2bfd3e334d89cfa57f645b85
        A/tables/TABLE-4-page-8-4/raw.json: 0c8653337c0317cfbb5ac96eff628ec844ba68dc313a53d3535b62781cb890f5
        A/tables/TABLE-4-page-8-4/prompt.txt: 762a518a94544407ae7c683d4e1815a4fd1509cabb010d3427c67941af6879b7
        A/tables/TABLE-4-page-8-4/meta.json: 20d79e60c7cf2be0f489118d2e79b8ba811c914c4beac9a18bd16bb0f67637ca
        A/tables/TABLE-3-page-6-3/raw.json: 8a15dc10bfa5cbc984e23638e9ea08dd7274d107ec4cbca1d50ffed517188104
        A/tables/TABLE-3-page-6-3/prompt.txt: 0d1e7a33aed1c54ae8cf33378c89ca54334f7685e50c06fabb4d40d37803733b
        A/tables/TABLE-3-page-6-3/meta.json: 2efaa254b1fac15209636ecc46c4d69fb40946c449a3cf2a1c38be645f26367e
        A/tables/TABLE-1-page-3-1/raw.json: e7fc4e6d13fa341ca63198bcd93cd95693dd4239e4243e4c11d446728b123a9f
        A/tables/TABLE-1-page-3-1/prompt.txt: fe85c967e7bec245eb22cb51e591f3076cea3c942727bfac01aecec2a1df4ceb
        A/tables/TABLE-1-page-3-1/meta.json: 86d0ac11315b5781905cddd917d13108b9ad40c38f3a6792c6f02baf2d4d8e0b
        A/tables/TABLE-5-page-9-5/raw.json: a294b5d1f1ae2b1877fea25932a327afe145f297b500fab2b1d7c743957fd135
        A/tables/TABLE-5-page-9-5/prompt.txt: fa6d5a5e6e3b8ee3aa32254e6982a85147ea5b085291ac59297c23c3757d0783
        A/tables/TABLE-5-page-9-5/meta.json: e72538eecb0c42952db99b5fe72eb9586a78fe44f6476554b519f2e0a006cae9
        A/tables/TABLE-2-page-4-2/raw.json: 8f7439902328a6ef05ee0ad5f1490ef829f50a3ce43daa36d3c7a02ceb1082c9
        A/tables/TABLE-2-page-4-2/prompt.txt: 5caedc0364cf7294f40ce8bd008b756d4952c9975d0b9f19cec805eee59c1d8f
        A/tables/TABLE-2-page-4-2/meta.json: 7e98c4587ce7a57c27ecbbb025a9374c4015b483d3a93554188c36d33d7d71ca
        B/passages.json: 36530580952acbb2a90a0937070a7300c1805268cf6af224866a9ff5e7c1cf3b
        B/raw.json: c43c462fa4db9f5cb4b22287e436d8c9912532991d1da0aa56107d0f4d4fdf1f
        B/source-units.json: ff5b65f8b79ae17d258443fc77748a1bfe7694110b3ee6e36f704dfdcd99198a
        B/full-source-units.json: fcb38a311e6c5f012692de1eddbb98f15aa6958a8b02cc45621da29dba1b1c55
        B/meta.json: 80f86cd25231568e7b40ed69a22e6ee12e7e22c4558d4e6c5775bc9deb30c54f
        B/table-images/TABLE-1-page-3-1.png: 5b8d61d036783079458fc67dd765918ce6a23c689c9f6f666388a04659762a01
        B/table-images/TABLE-5-page-9-1.png: 6a9f089c54762fbf681e884340f0312ce03504f68bd727e8d6ac2e79e20f9020
        B/table-images/page-3.png: 5dfa2f348c2694ee6eb31f7bdbf3c1b1f84dc2542843773eecacd3bc1481fbf8
        B/table-images/page-6.png: 68a6d6a75a0bc5d2d0d64b4c5d601005ce57bdecfbb6b0b0a16d4d4272690d26
        B/table-images/TABLE-4-page-8-1.png: eb80ec4b35d4152a023f6641fc61eec3d0605be03b8500a36b9f0220c4df168c
        B/table-images/page-4.png: 90f3eb163a93a4b9ee2e38cefd3c224e1626833e77e2349d70809dddff6e8f6d
        B/table-images/page-9.png: 352ebb99b233518e96d363b60209c738d4f92bb6c8fe0974dfe7ec0943fb2345
        B/table-images/TABLE-3-page-6-1.png: 40fd82e34142cb315f2232c27e0a443e90249babf4102ec8efabb478255604de
        B/table-images/page-8.png: ea1b8bed5cb9c88dd375c62aa5e408677f3982bbd961ac865986b41d53a44253
        B/table-images/manifest.json: 0a9accd591f42b1798c9c74cf0bd049b49c63ea16a10538c2cdac5278606189b
        B/table-images/TABLE-2-page-4-1.png: 5bac72147782ef00b0a5479751f3f3f165824547049b882a6628b462f517d95d
        B/clauses/window-11/raw.json: e4fc120bbdcd16002bfa80aaad4f0ae97982683edb4a3457a5ec7648a2d299b5
        B/clauses/window-11/prompt.txt: a082205ff170745cb92f8a5745e12f8a239e86fc368f74d48bf37276db1bd6f2
        B/clauses/window-11/meta.json: 38dce28274353853f76ffe7bcdd19ca73259a13ab224e613d988a65ba79165d9
        B/clauses/window-10/raw.json: d215f8c8b4088c4bdcbf1f7d4d5570912438d758b050eceeff59ded7d7c3937c
        B/clauses/window-10/prompt.txt: b7bc76b1374ad4334242011b6a6d85a8f7c5f9c17939b234ee74dbf9a67f1dad
        B/clauses/window-10/meta.json: a5d247f8057d3569434f6697cb5daf65c9a25018f6b8c93d0efef5574add7a89
        B/clauses/window-03/raw.json: 118af0c6d4d1a1ed9ebcc1c9ae55ee95a7c96a88bf456297a5b2d48d85a8929e
        B/clauses/window-03/prompt.txt: dc6fa4ed0c38716bc6863c856747be5b361ff26bc9529c4777d91d803b6fdb2d
        B/clauses/window-03/meta.json: 86ffde4554f87f827b0e45adeb806f1805205ac6a67f463518c014a736655359
        B/clauses/window-04/raw.json: 43fb14af19c314182a34cbc338655e84bdad9eebae248ff17571a69a9a2f21a3
        B/clauses/window-04/prompt.txt: c5a93d19e87869b6b79bebcff0c3824beffe2b097cbe2be11094fb8541d59f42
        B/clauses/window-04/meta.json: ee58c6e8492364a295fedc5b5f9dbd7522c82f568a0b98b0c7c795f0f4cbe0f6
        B/clauses/window-05/raw.json: f2136c01944fe812340867017839840851923da7b5a624980572dff86ee47340
        B/clauses/window-05/prompt.txt: 59fcc1be44edf276f7e106bea1bdf60fbae725015f224a9494e754b35be0a4c3
        B/clauses/window-05/meta.json: a8e7aa2eb299e2f40497c889fc90413bb3370961084c39f1a102348da2a48eab
        B/clauses/window-02/raw.json: 83f31f9c55cec83ae132f2cf7af50c3648c20a6cc8e888cce8c0c0f37441e8ee
        B/clauses/window-02/prompt.txt: 6a4f7cfae698318ebed58ce51d82c466cb95a3a662fbd81c001f3ac87919eb39
        B/clauses/window-02/meta.json: 8a299702d8df533a3beb6242a19a07bebff2e6b34311cc8966cda8f258844546
        B/clauses/window-09/raw.json: 1836108978f48806d5fcdb2194a825d0c02338eaf7c0eaa543a33239d1e91981
        B/clauses/window-09/prompt.txt: a8415c4e023d8a3e1ab40e27906d9cc29982dd73525272a1e57fc80a82edfcda
        B/clauses/window-09/meta.json: f391ed4772e3b0d4811eff9776ce518845ca5f84b9080f89592ddcf7809a082a
        B/clauses/window-07/raw.json: 8f81a0d8287405914f3e35666a9aeb190300e3ce4a2c82159f6e968f8f9ac18f
        B/clauses/window-07/prompt.txt: d6d5f9ab21bc55081b0c4034ce067847194d4de353f9a8daae9fab7d78e86d28
        B/clauses/window-07/meta.json: 708efa3f2ba74679418c7dd4e20ef2e16998fa63e7323f0ba0568a238ecb9ca9
        B/clauses/window-01/raw.json: e67f93816a061ea69fb40ccb90a00edea2dd3223344ced6af8fe6310a695ad43
        B/clauses/window-01/prompt.txt: d5f72bc07406dabe1b6f2bdb2e624b4e4eda405307d85841a8d89fa5390cecd8
        B/clauses/window-01/meta.json: d46ee3df5dcab10f01c57dab57ab686132f7c5c7f9e4db12336058c962685697
        B/clauses/window-06/raw.json: 4894e411cba27ac972cdc472cb2cb580f637de2b25826dd53878685b4a08ea7d
        B/clauses/window-06/prompt.txt: 7efb4eeb0da4e0a2a3581909483da5fd1f7bb916299958bd1047ccb7af6fe263
        B/clauses/window-06/meta.json: cdd19f5d457223e88fc35ea214dfe39ff66fd8b3719cde33fe01c674ae016609
        B/clauses/window-08/raw.json: 3855d62f26652f57a221d1ad83efc9ef4f5a24381f47854dbed937c613c91339
        B/clauses/window-08/prompt.txt: 0774e111bd63e48eaa428cfdc3465deeacfa25e79c5a26f38e8dd98f32349ba9
        B/clauses/window-08/meta.json: e1297841b137dd1e4ea1b3b208810a28b02d8059f2d34e6dc9ca2220c450f066
        B/tables/TABLE-4-page-8-4/raw.json: c827cc8be97856dcd139e2a010e394ec181667aea8a9e1649c93c6b3ffbf1849
        B/tables/TABLE-4-page-8-4/prompt.txt: 762a518a94544407ae7c683d4e1815a4fd1509cabb010d3427c67941af6879b7
        B/tables/TABLE-4-page-8-4/meta.json: a477862d673ba46b1d6db4575278dfcb3542dfb0d4650490cf4b4e5f33dc0194
        B/tables/TABLE-3-page-6-3/raw.json: f6f8a0ae185553709e612676aae8d3078c81610f42b1c5d806f17ed425be5a56
        B/tables/TABLE-3-page-6-3/prompt.txt: 0d1e7a33aed1c54ae8cf33378c89ca54334f7685e50c06fabb4d40d37803733b
        B/tables/TABLE-3-page-6-3/meta.json: 1bb94cbb3d81d6dd359e07ef6b3e91cf14e4d21cde5290069352124af251a38f
        B/tables/TABLE-1-page-3-1/raw.json: 6367cbf726af948175b9b8ee6295150b17a7d930763d7a894af63f87dbb489db
        B/tables/TABLE-1-page-3-1/prompt.txt: fe85c967e7bec245eb22cb51e591f3076cea3c942727bfac01aecec2a1df4ceb
        B/tables/TABLE-1-page-3-1/meta.json: 3e07bb21e771e90d6a188a42f8140e8bf4e6ff556bde49719753650559a5dd93
        B/tables/TABLE-5-page-9-5/raw.json: c38f4a4fb8dfe532359b128d3bc002dd6d2005c91e169d7bec4b942ef62eb3c9
        B/tables/TABLE-5-page-9-5/prompt.txt: fa6d5a5e6e3b8ee3aa32254e6982a85147ea5b085291ac59297c23c3757d0783
        B/tables/TABLE-5-page-9-5/meta.json: ec94be621b1b98a0c9bcb623977a5b7e0f8184f55bd8799fc5f7a4b1006d6bda
        B/tables/TABLE-2-page-4-2/raw.json: bfb3a6eb4a3f23310cab8f2bf04cc76ad4282c0810b9e323b6795c60754436ec
        B/tables/TABLE-2-page-4-2/prompt.txt: 5caedc0364cf7294f40ce8bd008b756d4952c9975d0b9f19cec805eee59c1d8f
        B/tables/TABLE-2-page-4-2/meta.json: f58ea952ab83c6613af2118de780deb6853143d456be0da98834d281349b5d66
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
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2011
      source_status_sha256: 158e60fa9b065575c696b5ac3560fd1c6852f428594b4f16b94deb82c9528a65
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: age
    outcome:
      text: articulatory quality (original vs novel lyrics)
    analysis_label: Age and lyric memory interaction
    relation: association
    evidence_ids:
    - P9-S1-C15
    - P9-S2-C2
    - P9-S3-C6
    qualifier_ids:
    - P9-S2-C3
    - P9-S3-C7
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2011
      source_status_sha256: 158e60fa9b065575c696b5ac3560fd1c6852f428594b4f16b94deb82c9528a65
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C9
      - Result passage disposed without unit P4-S1-C15
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S3-C4
      - Accounting without a linked unit P5-S1-C11
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S1-C11
      - Unaccounted source passage P6-S1-C2
      - Unaccounted source passage P5-S2-C5
      - Accounting without a linked unit P6-S1-C12
      - 'window 6: invalid/duplicate disposition P6-S1-C9'
      - Accounting without a linked unit P6-S2-C5
      - Result passage disposed without unit P6-S2-C6
      - Unresolved source passage P6-S3-C1
      - Unaccounted source passage P6-S1-C12
      - Unaccounted source passage P6-S2-C5
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C10
      - Accounting without a linked unit P7-S1-C12
      - Accounting without a linked unit P7-S1-C13
      - Accounting without a linked unit P7-S1-C2
      - Accounting without a linked unit P7-S1-C3
      - Accounting without a linked unit P7-S1-C9
      - Accounting without a linked unit P7-S2-C8
      - Unaccounted source passage P7-S1-C3
      - Unaccounted source passage P7-S2-C8
      - Unaccounted source passage P7-S1-C9
      - Unaccounted source passage P7-S1-C2
      - Unaccounted source passage P7-S1-C12
      - Unaccounted source passage P7-S1-C13
      - 'window 9: invalid/duplicate disposition P7-S2-C13'
      - Result passage disposed without unit P7-S2-C13
      - Result passage disposed without unit P7-S2-C14
      - Result passage disposed without unit P7-S2-C15
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P7-S3-C7
      - Result passage disposed without unit P7-S3-C8
      - Result passage disposed without unit P8-S1-C1
      - Unresolved source passage P8-S1-C1
      - Unresolved source passage P8-S1-C2
      - Result passage disposed without unit P8-S1-C5
      - Unresolved source passage P8-S1-C5
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P8-S2-C10
      - Result passage disposed without unit P8-S2-C12
      - Accounting without a linked unit P8-S2-C14
      - Accounting without a linked unit P8-S2-C15
      - Accounting without a linked unit P8-S2-C16
      - Unaccounted source passage P8-S2-C16
      - Unaccounted source passage P8-S2-C15
      - Unaccounted source passage P8-S2-C14
      - Result passage disposed without unit P9-S2-C12
      - Result passage disposed without unit P9-S2-C13
      - Result passage disposed without unit P9-S2-C15
      - Accounting without a linked unit P9-S2-C4
      - Unaccounted source passage P9-S2-C4
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C12
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C7
      - Result passage disposed without unit P10-S1-C9
      - Accounting without a linked unit P9-S3-C6
      - Accounting without a linked unit P9-S3-C7
      - Unaccounted source passage P9-S3-C7
      - Unaccounted source passage P9-S3-C6
      unattached_null_or_qualifier_ids:
      - P4-S1-C15
      - P5-S2-C5
      - P6-S1-C2
      - P6-S1-C12
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C12
      - P7-S2-C8
      - P7-S3-C7
      - P7-S3-C8
      - P8-S1-C14
      - P8-S2-C14
      - P9-S3-C6
      - P9-S3-C7
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 228
      unselected_timing_passages:
      - P3-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C17
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      - TABLE-4-page-8-4
      - TABLE-5-page-9-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P5-S2
        - P7-S2
        - P7-S3
        - P8-S2
        - P9-S1
        - P9-S2
        - P9-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2011
      source_status_sha256: 158e60fa9b065575c696b5ac3560fd1c6852f428594b4f16b94deb82c9528a65
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of melodic intoning null effect.
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Abstract restatement of rhythm/basal ganglia relationship.
    - source_id: P1-S1-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: Abstract restatement of variance attributed to basal ganglia.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Abstract restatement of memory and automaticity mediation.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes diagnosed concomitant speech disorders.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Confirms aphasia diagnosis in all patients.
    - source_id: P4-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion locations (MCA vs basal ganglia).
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot subject rating of arrhythmic control.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes tempo selection based on pilot data.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group familiarity results for song selection.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of MRI scans in Figure 1.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group performance on song selection.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation between age and syllable production in control group.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of word transition frequencies between lyric types.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null differences in word/syllable frequency between lyric types.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Learning effects observed in three patients.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement that learning effects did not deviate overall means.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Total number of syllables rated.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distribution of scoring points across rated syllables.
    - source_id: P6-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distribution of scoring points across rated syllables.
    - source_id: P6-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distribution of scoring points across rated syllables.
    - source_id: P6-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null difference in pitch accuracy between lyric types.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pitch accuracy of patients with right hemisphere lesions.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pitch accuracy of patients with right hemisphere lesions.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability correlations.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: ANOVA result for melodic intoning effect.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Sensitivity result excluding right hemisphere lesions.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Null interaction of modality and lyrics.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Conclusion on absence of singing effect across lyric types.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Null correlation between frequency variance and articulatory quality.
    - source_id: P7-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifier for frequency variance result.
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Null correlation between pitch accuracy and articulatory quality.
    - source_id: P7-S2-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifier for pitch accuracy result.
    - source_id: P7-S2-C14
      disposition: repeated
      result_indexes:
      - 0
      reason: Interim discussion restatement of null singing effect.
    - source_id: P7-S3-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Interim discussion restatement of null frequency variability effect.
    - source_id: P7-S3-C6
      disposition: repeated
      result_indexes:
      - 2
      reason: Interim discussion restatement of null pitch accuracy effect.
    - source_id: P7-S3-C7
      disposition: repeated
      result_indexes:
      - 2
      reason: Interim discussion restatement of null pitch accuracy effect.
    - source_id: P7-S3-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Interim discussion summary of null effects.
    - source_id: P7-S3-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Interim discussion restatement of null singing effect.
    - source_id: P7-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that articulatory quality differed by lyric type.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of null advantage for singing with original lyrics.
    - source_id: P8-S1-C17
      disposition: represented
      result_indexes:
      - 3
      reason: Pair-wise comparison of rhythmic speech vs arrhythmic control.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Mean values for rhythmic speech vs arrhythmic control.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Contrast analysis of basal ganglia lesions and rhythmicity.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Null interaction of basal ganglia lesions with melodic intoning.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Observation of performance drop in arrhythmic control for larger BG
        lesions.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Observation of lack of pattern in smaller BG lesions.
    - source_id: P8-S2-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Null difference in spoken conditions with/without percussion.
    - source_id: P8-S2-C14
      disposition: represented
      result_indexes:
      - 4
      reason: Figure 4 caption confirming BG lesion interaction.
    - source_id: P8-S2-C15
      disposition: represented
      result_indexes:
      - 4
      reason: Specific performance of larger BG lesion group.
    - source_id: P8-S2-C16
      disposition: represented
      result_indexes:
      - 4
      reason: Specific performance of smaller BG lesion group.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Variance attributed to basal ganglia lesions.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: ANOVA main effect of lyric type (original vs formulaic).
    - source_id: P9-S1-C15
      disposition: represented
      result_indexes:
      - 6
      reason: Contrast analysis of age and lyric memory interaction.
    - source_id: P9-S2-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Elderly patients' performance on original vs novel lyrics.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Lack of difference in younger group.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Superiority of formulaic over non-formulaic lyrics.
    - source_id: P9-S3-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Control for song familiarity in age-matched group.
    - source_id: P9-S3-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Figure 5 caption confirming age/lyric memory interaction.
    - source_id: P9-S3-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Specific performance of elderly patients.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Superiority of formulaic lyrics in every single patient.
    - source_id: P10-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: General discussion restatement of null singing effect.
    - source_id: P10-S1-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: General discussion restatement of rhythm/BG effect.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 4
      reason: General discussion restatement of variance attributed to BG.
    - source_id: P10-S1-C12
      disposition: repeated
      result_indexes:
      - 5
      - 7
      reason: General discussion restatement of lyric importance.
    - source_id: P10-S1-C13
      disposition: repeated
      result_indexes:
      - 5
      - 7
      reason: General discussion restatement of lyric importance.
    - source_id: P10-S1-C14
      disposition: repeated
      result_indexes:
      - 5
      - 7
      reason: General discussion restatement of memory/automaticity mediation.
    unresolved_coverage:
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C11
    - P4-S1-C5
    - P4-S1-C8
    - P4-S1-C15
    - P4-S3-C4
    - P5-S1-C11
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C11
    - P6-S1-C12
    - P6-S2-C5
    - P6-S2-C6
    - P6-S3-C4
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C8
    - P6-S3-C11
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C10
    - P7-S1-C13
    - P7-S2-C9
    - P7-S2-C13
    - P7-S2-C14
    - P7-S2-C15
    - P7-S2-C17
    - P7-S3-C2
    - P7-S3-C6
    - P7-S3-C7
    - P7-S3-C8
    - P7-S3-C9
    - P7-S3-C11
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C5
    - P8-S1-C14
    - P8-S2-C4
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C11
    - P8-S2-C12
    - P8-S2-C15
    - P8-S2-C16
    - P9-S1-C2
    - P9-S2-C3
    - P9-S2-C6
    - P9-S2-C12
    - P9-S2-C13
    - P9-S2-C15
    - P9-S3-C7
    - P10-S1-C7
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C12
    - P10-S1-C13
    - P10-S1-C14
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    - TABLE-4-page-8-4
    - TABLE-5-page-9-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C2
      recruited_sample:
      - P3-S2-C2
      eligibility:
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C9
      - P4-S1-C6
      imaging_provenance:
      - P4-S1-C13
      - P4-S1-C14
      - P4-S2-C2
      - P5-S2-C5
      imaging_timing:
      - P4-S1-C14
      outcome_timing:
      - P3-S2-C6
      outcome_definition:
      - P6-S2-C16
      - P6-S3-C10
      validation: []
      analysis_restrictions:
      - P3-S3-C1
      - P4-S2-C4
      - P6-S3-C5
      dependent_variable_statement:
      - P7-S1-C5
      - P7-S2-C4
      - P7-S2-C10
      limitations:
      - P4-S1-C9
      - P6-S2-C5
      - P6-S2-C6
      - P8-S2-C8
      - P9-S1-C6
      personal_factors:
      - P4-S1-C11
      tested_personal_effects:
      - P9-S1-C15
      - P9-S2-C12
      adjustment_roles:
      - P7-S1-C5
      - P8-S1-C18
      - P9-S1-C14
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C9
      - P4-S1-C10
      - P4-S1-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C17
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C2
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
      pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
      review_sha256: 553002c43d943cc341de539abd58bf654c8468fb7efda1ffdcdb58eca7953c2d
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
      - P9-S1-C15
      - P9-S2-C2
      - P9-S3-C6
      source_result: A significant interaction was detected between patient age and
        lyric type (original vs. formulaic) on articulatory quality. Specifically,
        elderly patients showed higher performance for original lyrics compared to
        formulaic lyrics, whereas this difference was not confirmed in younger patients.
        The analysis was a repeated-measures ANOVA with age as a covariate.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P9-S1-C15, P9-S3-C6) describes a contrast analysis/repeated-measures
            ANOVA examining the interaction of age with lyric type (original vs formulaic)
            on articulatory quality. The proposed core correctly identifies this as
            the 'age and lyric memory interaction' analysis.
          source_ids:
          - P9-S1-C15
          - P9-S3-C6
          - P7-S1-C5
        direction:
          answer: fits
          reason: 'The source states that elderly patients showed increased performance
            for original lyrics compared to formulaic lyrics, while this difference
            was not confirmed in younger patients (P9-S2-C2, P9-S2-C3, P9-S3-C7).
            The proposed claim accurately reflects this directionality: elderly >
            younger for the original vs formulaic difference.'
          source_ids:
          - P9-S2-C2
          - P9-S2-C3
          - P9-S3-C7
        construct:
          answer: fits
          reason: The exposure is patient age (P9-S1-C14), the outcome is articulatory
            quality (P6-S2-C16), and the comparison is between original and formulaic
            lyrics (P9-S1-C15). The patient measurement is non-imaging (behavioral
            rating of syllables), which is correctly identified. The construct is
            faithful to the source.
          source_ids:
          - P9-S1-C14
          - P6-S2-C16
          - P9-S1-C15
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the effect was
            specific to the original vs formulaic comparison and that younger/elderly
            patients showed similar results for novel lyrics. This aligns with P9-S2-C3
            and P9-S2-C15. The core correctly limits the claim to the specific interaction
            found.
          source_ids:
          - P9-S2-C3
          - P9-S2-C15
          - P9-S3-C7
        missing_material_caveat:
          answer: fits
          reason: The core includes the small sample size limitation. The source notes
            that the finding should be viewed with caution regarding generalizability
            due to the small N (implied by the context of the study and explicit in
            the proposed limitations). No other material caveats that change the interpretation
            of this specific interaction are omitted. The OCR warnings on P9-S1-C15
            and P9-S3-C6 do not obscure the qualitative finding of the interaction
            itself, which is clearly stated in the text.
          source_ids:
          - P9-S1-C15
          - P9-S3-C6
      optional_pending:
      - Exact F-statistic and p-value for the age interaction (P9-S1-C15 has OCR warning,
        but qualitative result is clear)
      - Partial eta-squared value for the age interaction (P9-S1-C15 has OCR warning)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact F-statistic and p-value for the age interaction (P9-S1-C15 has OCR warning,
      but qualitative result is clear)
    - Partial eta-squared value for the age interaction (P9-S1-C15 has OCR warning)
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: age
      outcome:
        text: articulatory quality (original vs novel lyrics)
      analysis_label: Age and lyric memory interaction
      relation: association
      evidence_ids:
      - P9-S1-C15
      - P9-S2-C2
      - P9-S3-C6
      qualifier_ids:
      - P9-S2-C3
      - P9-S3-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
        source_review: _compare/relationships-2026-11-16/review-current/Stahl2011
        source_status_sha256: 158e60fa9b065575c696b5ac3560fd1c6852f428594b4f16b94deb82c9528a65
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P9-S1-C15:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3c0bc8113408cacde37218c457c8b93c9c0f16e0d0e1a542bcab4373532fc5a5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S1-C15
          page: 9
          text_layer_sha256: 3c0bc8113408cacde37218c457c8b93c9c0f16e0d0e1a542bcab4373532fc5a5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "A contrast analysis revealed an inter-\naction of age with\
          \ original and formulaic lyrics [F(1) = 13.18,\nP = 0.003, partial \x02\
          2 = 0.49]."
        anchor_text: "A contrast analysis revealed an inter-\naction of age with original\
          \ and formulaic lyrics [F(1) = 13.18,\nP = 0.003, partial \x022 = 0.49]."
        excluded_fragments: []
      P9-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: eb9b4ca43e1575486b1fdc10a07ebcd4d1de4f751e2e6ef2d3dae615c03763fd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S3-C6
          page: 9
          text_layer_sha256: eb9b4ca43e1575486b1fdc10a07ebcd4d1de4f751e2e6ef2d3dae615c03763fd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The results show a signiﬁcant interaction of age

          and lyric memory (**P 5 0.01).'
        anchor_text: 'The results show a signiﬁcant interaction of age

          and lyric memory (**P 5 0.01).'
        excluded_fragments: []
        image_sha256: fc3fe9d1dcefffdcedf0957c855d9ed9b0b887bdc32d0133cf3816d222f670da
      P3-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: adf9221b5082b980da0396a2fa614637ccb2e10d889116b4e8a4e6ab193373f4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C6
          page: 3
          text_layer_sha256: adf9221b5082b980da0396a2fa614637ccb2e10d889116b4e8a4e6ab193373f4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'At

          the time of testing, all patients were at least 3 months post-infarction,

          except in one case (Patient HS).'
        anchor_text: 'At

          the time of testing, all patients were at least 3 months post-infarction,

          except in one case (Patient HS).'
        excluded_fragments: []
        image_sha256: c76cf74de20ce373b82df6d1209f0424c62e19c245662997a673991bd6ffba60
        transcription: '. At

          the time of testing, all patients were at least 3 months post-infarction,

          except in one case (Patient HS)'
      P3-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 020a22d9e9fa4d0d283e0db1e2f5ae3aebe88032dfd66415bd2f8c057d157267
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4585cf6d447caf3c0219c3456f040bba724a656652dfbee564051494a5679c9f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C9
          page: 3
          text_layer_sha256: 4585cf6d447caf3c0219c3456f040bba724a656652dfbee564051494a5679c9f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients were classiﬁed as non-ﬂuent aphasics, diagnosed
          with

          Broca’s aphasia (n = 10) or global aphasia with prevailing expressive

          deﬁcits (n = 7).'
        anchor_text: 'All patients were classiﬁed as non-ﬂuent aphasics, diagnosed
          with

          Broca’s aphasia (n = 10) or global aphasia with prevailing expressive

          deﬁcits (n = 7).'
        excluded_fragments: []
        image_sha256: 255a8d6692dccbe496af280f922e0f9f7b0c2fa8dbd43b488380276b337cf89b
        transcription: All patients were classified as non-fluent aphasics, diagnosed
          with Broca's aphasia (n = 10) or global aphasia with prevailing expressive
          deficits (n = 7)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: "A contrast analysis revealed an inter-\naction of age with original and\
    \ formulaic lyrics [F(1) = 13.18,\nP = 0.003, partial \x022 = 0.49]."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
