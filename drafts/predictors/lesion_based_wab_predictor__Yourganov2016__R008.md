---
id: lesion_based_wab_predictor
name: lesion-based WAB predictor
kind: predictor
findings:
- id: f1
  target: wab_scores
  target_kind: impairment
  claim: The model accurately predicted WAB scores for speech fluency, auditory comprehension,
    speech repetition, and naming, with the most important regions for fluency being
    the precentral gyrus, opercular part of inferior frontal gyrus, and posterior
    part of the superior temporal gyrus (PSTG).
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 90
    population: individuals with aphasia resulting from a single ischemic or hemorrhagic
      stroke to the left hemisphere
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
  - lesion-based analysis tended to overestimate WAB scores
  - lesion size was approximately as predictive as ROI-specific damage
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multivariate support vector regression (SVR) model
    using the proportion of intact voxels within 42 predefined gray-matter regions
    (damaged in at least 4 of 90 participants) as features. prediction of speech fluency
    scores was the most accurate; prediction was more accurate for lesion-based analysis
    than connectome-based analysis for fluency, repetition, and naming; model evaluated
    using leave-one-participant-out cross-validation; features were pre-selected based
    on correlation with the target score (p < 0.05 with Bonferroni correction). Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S3-C7, two-model agreement, human verification pending):
    Imaging data

    MRI scanning was performed within 2 d of behavioral testing of language

    abilities Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:wab_scores
  citation: '@Yourganov2016'
  source_passages:
  - section: Original source P1-S1-C5
    page: 1
    quote: 'In this study, we applied a predictive multivariate framework to investigate
      the relationship between

      language deficits in human participants with chronic aphasia and the topological
      distribution of structural brain damage, defined as

      post-strokenecrosisorcorticaldisconnection.Weanalyzedlesionmapsaswellasstructuralconnectomemeasuresofwhole-brainneural

      network integrity to predict clinically applicable language scores from the
      Western Aphasia Battery (WAB).'
    supports: claim
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Only individuals with aphasia resulting from a single ischemic

      or hemorrhagic stroke to the left hemisphere were included.'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: "All partici-\npants were at least 6 months after stroke, and the mean\
      \ \x03 SD time since\nstroke onset was 42.8 \x03 50 months (range, 6–276 months)."
    supports: sample
  - section: Original source P2-S3-C7
    page: 2
    quote: 'Imaging data

      MRI scanning was performed within 2 d of behavioral testing of language

      abilities.'
    supports: sample
  - section: Original source P3-S1-C4
    page: 3
    quote: 'Then, lesion-based damage was com-

      puted as the proportion of intact (i.e., not le-

      sioned) voxels per each gray-matter region.'
    supports: method
  - section: Original source P3-S3-C5
    page: 3
    quote: 'In the first case, we only considered gray-matter regions that

      were damaged in at least 4 of 90 participants; there were 42 such regions

      (Table 1).'
    supports: method
  - section: Original source P4-S2-C11
    page: 4
    quote: 'The accuracy of our prediction was evaluated by computing

      Pearson’s correlation coefficient between the actual and predicted WAB

      scores.'
    supports: method
  - section: Original source P4-S4-C4
    page: 4
    quote: 'For both types of analysis (lesion- and connectome-based),

      prediction of speech fluency scores was the most accurate, per-

      haps because of the fact that the fluency scores were whole num-

      bers whereas the other three scores were fractional.'
    supports: claim
  - section: Original source P4-S4-C5
    page: 4
    quote: 'For three

      scores (fluency, repetition, and naming), prediction was more

      accurate for lesion-based analysis; auditory comprehension

      scores were more accurately predicted from the connectome.'
    supports: claim
  - section: Original source P5-S1-C2
    page: 5
    quote: 'Lesion-based analysis tended to overestimate the

      WAB scores, e.g., the predicted scores were better than the actual

      scores.'
    supports: limitation
  - section: Original source P5-S1-C4
    page: 5
    quote: "When Tables 3–5 are compared, we can see\nthat lesion size is approximately\
      \ as predictive as ROI-specific\ndamage and connectome integrity (there was\
      \ no significant dif-\nference in r-to-Z transformed correlations; p \a 0.15);\
      \ this is ex-\npected given the correlation between overall lesion size and\n\
      amount of damage in some regions (Fig. 3)."
    supports: limitation
  - section: Original source P5-S1-C7
    page: 5
    quote: 'For lesion-based analysis, the most important re-

      gions for predicting fluency scores were the precentral gyrus,

      opercular part of inferior frontal gyrus, and the posterior part of

      the superior temporal gyrus (PSTG); for predicting auditory

      comprehension scores, the PSTG, the triangular part of inferior

      frontal gyrus, the pole and the posterior part of the middle tem-

      poral gyrus, the amygdala, and the dorsal part of the middle

      frontal gyrus; for predicting speech repetition scores, the poste-

      rior part of the superior and the middle temporal gyri; and, fi-

      nally, for predicting naming scores, the PSTG, the pole of the

      superior and middle temporal gyri, and the triangular part of the

      inferior frontal gyrus.'
    supports: claim
predictor_type: imaging_metric
short_definition: A multivariate support vector regression (SVR) model using the proportion
  of intact voxels within 42 predefined gray-matter regions (damaged in at least 4
  of 90 participants) as features.
assessment:
- Western Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yourganov2016
  proposal_id: R008
  review_status_sha256: 6df5c5e305c5c91c620d81aad4dc81697fb0341522f9dab5bb3079c21f90be67
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
        A/passages.json: 5bb1c488835ccb3a27f1339ddec7165b39163faef15b3bb1f87de2040774adeb
        A/raw.json: 07e48632cf66082f6c72d0bbe85326fb8f641072b8873834ec8e1b0539fbf7c4
        A/source-units.json: 33d3a28dc031bc41c60ca1b18d39e15b86903c6fbed9dfca1847cca215b161e5
        A/full-source-units.json: b0d7ef51deb8a34e15aa73c5c10e5f21a578f03f3d3d44dbf89ccc5ac0279039
        A/meta.json: da57f0191b62151eaa96b2ecce0122ca537caeb1ff8fd2396cb36efdeede077a
        A/table-images/TABLE-1-page-3-1.png: 713874469c4ecb8c7042c2deaf05b66c7b2ea9eb1bea1e0160f72fda1f79c11a
        A/table-images/page-11.png: 2a478acf3db6fd3c65f4a294fc4810c1ff0b884a6c96dd5e53ed2c0e492d08db
        A/table-images/page-3.png: 4f4a5e5c92950cf5398f87211a37cc7d1b94c3fbc418728ea7c99f40668b4088
        A/table-images/TABLE-7-page-11-2.png: abc4afc85fbf3259dbba02a6035d0d2d70728f648c5ffe2543e69db34e60783c
        A/table-images/page-6.png: 6f5355045dcd3786d5e682da6e10ee3767847a247a8f9478bb84ee16a357d434
        A/table-images/page-5.png: d25bbcaa1ab1c1762804b0c936ab30abfef7f4f40a102ce5d114161ae0cb782c
        A/table-images/TABLE-4-page-6-1.png: 5d3054ea6f9a06396b792288b5883023561a5ab299efe18a6f24faec8d24898a
        A/table-images/TABLE-6-page-11-1.png: cea926bc152ab9f8c1ba78ed60cdd36ee794c2ca296e90d420381c0fe0bb8bc7
        A/table-images/manifest.json: bc3a2a9a28c60e03a7c15c9364bbd983ec2110dd5fe0704fb8a8c70846fde1e9
        A/table-images/TABLE-5-page-6-2.png: c1c321f8a03ec16675b8d608243509abd9a6495a140d827743261737c030590a
        A/table-images/TABLE-8-page-11-3.png: 30015ef6d5cd4e13373508f93812a06c7676f53850c9eee27803fe886fd54346
        A/table-images/TABLE-3-page-5-2.png: ddd561ba5da2dc717e43da1aa0a673d8a2eb23b413b0e62c0bd0a1dd6213fab1
        A/table-images/TABLE-2-page-5-1.png: 5254e1bee1334d23483087fcb2042e471a205995ab7c2b203f22ee7991d6e4cd
        A/clauses/window-03/raw.json: b8cb17ed0befacc5e3970862a8855669506037a01ad49ddf2b3547b79bf1c97c
        A/clauses/window-03/prompt.txt: 0f7bbed5425049588d9a975578ab3afdbde7b1fd3f97b64d2b001988437ffe43
        A/clauses/window-03/meta.json: fd0035688a1f0b6b2ca45e47ec1a263cf8e2d1c3486dfc44a60af38914af6664
        A/clauses/window-04/raw.json: cd2791da5f73faa00398b6e5841b9d737e09983dd5c5ce51e68d1a59c615d79d
        A/clauses/window-04/prompt.txt: c03e542e762c1d60866b9d1a58cf2faba1003a72c9b0c0669b590a82cd457734
        A/clauses/window-04/meta.json: d744993f8f70af8dc0ee6ebce9887f079ff019d258847395b9813e599cf208cf
        A/clauses/window-05/raw.json: cc311f6651538f35c2fdc487a6ec163450688a0d1253b663261a429450b2f262
        A/clauses/window-05/prompt.txt: 84a9ff0205ceefeae1eb8df2d36b3121500a9183d1d14251f9fd6b2a1e63e207
        A/clauses/window-05/meta.json: 287bb43cb2488422390cf11621b7da16fce65ce0e9feaaa65349ee9077212e39
        A/clauses/window-02/raw.json: 9fb76dfc8c7a9473c4ca7ec7e5b009227016a6be575138356538655f22d0a65b
        A/clauses/window-02/prompt.txt: 1612706e4ff19e87290cf8f381826e3890f0e4898640b874e9217d56113d2c17
        A/clauses/window-02/meta.json: 8386d4f92d839b0205f97e23a7659c240c42265c1bf9807a1de06b69ecdfa4c2
        A/clauses/window-09/raw.json: d8dc698b789249fe49e9aa497a4dae70dcef88bbae5e8426a4b3fd9251534f96
        A/clauses/window-09/prompt.txt: 5ab197241a59a15070a8e6f779dbd44ded56931cc70eec5264d258f450929bbc
        A/clauses/window-09/meta.json: 99806e00758f511a8edae83799982a241ea49b0cfbbead3481d172054553106a
        A/clauses/window-07/raw.json: 5058d88c9edc0f954431e382551fa1acbe653173e471b43132920e0570841cef
        A/clauses/window-07/prompt.txt: 305646c31cda7b9853f2876542cbb08bd1e3e5b6d8185fbf33889a56caa10228
        A/clauses/window-07/meta.json: 973705108ad4d39683468248265fea2af82ad3cead7b8fbb05cc47a551c7bcf8
        A/clauses/window-01/raw.json: 5e64e184bdf50507ef2da50291780cf405c04910cead86d49fda5e0f53562135
        A/clauses/window-01/prompt.txt: 0e07f3b16755876958a0bf67aae4754699a03d0698a5cb53be82282d98327f6c
        A/clauses/window-01/meta.json: 2c6fff2ed4ea1fab97b384c673e8a5a600beccbd5994fbfaf9c3790d04921bc3
        A/clauses/window-06/raw.json: 7294826ad145848f8c8234cb28182332450ee0f0bad1ca362717653967b17fab
        A/clauses/window-06/prompt.txt: d8942c7689b6a16f44f2702d19108e1d5a98993426d3fae3363748feb82a167c
        A/clauses/window-06/meta.json: eb05f92f55e11fd7bcd462c92e6eed7dfe6a1cfd3e0b26d1220fca73c701d0d2
        A/clauses/window-08/raw.json: d9e99cbac539ef52a250b8f56ae45f0a98e9ac5b2c2eb3600c5de663af20fb80
        A/clauses/window-08/prompt.txt: 3dc0d751c583b41c0d47618013f9127ec2f801673923ea68b238f8cd6d62f077
        A/clauses/window-08/meta.json: dcb0f49206bd5d4d82fda07522b3ecbf82987a2edca8000a499e6362b8141eb1
        A/tables/TABLE-4-page-6-4/raw.json: 40e826dd9101c8cfc628b5189c698ac5e8e12701b66ee819313210ccfa622efe
        A/tables/TABLE-4-page-6-4/prompt.txt: 2ed3c4c5a27377eaa0c92e5df67a7946d771b26f7e798b6a89e1ecf810a478ba
        A/tables/TABLE-4-page-6-4/meta.json: 79263e026e528cff370518fa0be5f1a81b27ce1d71e0720a0a7dc45bdd6f35b5
        A/tables/TABLE-5-page-6-5/raw.json: 6c8bb4e7033e5c9dac2d350000864a3cd37735145322c3db697071cc1a8a4b69
        A/tables/TABLE-5-page-6-5/prompt.txt: af3febc684505f2a57cdea3fc50f871af20dac48be7983f48d901eaa419fd95b
        A/tables/TABLE-5-page-6-5/meta.json: ba984ccd03dd97971bac8a023ff403eea372f471a3bad38f4d465a28e711ee8d
        A/tables/TABLE-3-page-5-3/raw.json: aca66a23fc6a44027173141c2d98a435a054d1fd0b32739f0c16b1ee2b59f976
        A/tables/TABLE-3-page-5-3/prompt.txt: df31905789807e7727fba5f21ac089b0fd5a4131e69a0e83993809142cd651d1
        A/tables/TABLE-3-page-5-3/meta.json: 8e4ede2806c78294fc5c24764e6e2741d34c441cfb89df147662d355c3a9dbf0
        A/tables/TABLE-6-page-11-6/raw.json: 79dbed88c3634a2bc85059b0d5ef1659d8296ef0da96ae68783a004196c90c75
        A/tables/TABLE-6-page-11-6/prompt.txt: 1652aa4cb23f9fd78f3610eae285caee99cca792cf28b41c4f99d7995dd26201
        A/tables/TABLE-6-page-11-6/meta.json: a82bf1d52ca31a9c2e28b2efef11cad256507af23205c3c6a1f71925d7d9d466
        A/tables/TABLE-2-page-5-2/raw.json: 5c8f0c1a73daa6f2593aa753a26393099da90a87bc4c58516a9b89ce0ebde28f
        A/tables/TABLE-2-page-5-2/prompt.txt: 1c734dfd36fa9af0c037cab4ff63e0586dbbc39af7c0919505052317cf3f14ac
        A/tables/TABLE-2-page-5-2/meta.json: a7e6ddcaf896c46c34cbab442b52afe85fd44e3d8a5f394c6c13ab12ab04354d
        A/tables/TABLE-7-page-11-7/raw.json: 4903b6046c005a24361557a343611099680832ac086587f23237489968654f10
        A/tables/TABLE-7-page-11-7/prompt.txt: ed2b04d9a302caaae3dbfe7f2215522bd2a81605ee0ca7fd24ebddfeb1be0f96
        A/tables/TABLE-7-page-11-7/meta.json: 71a0fa030a08ef51e50b8d61a33b31395413a4382a1b633cc1e100844b291801
        A/tables/TABLE-1-page-3-1/raw.json: 118860259f344cf89e4d8cd064668236532060df1eed68e49ceb1639d85ff08a
        A/tables/TABLE-1-page-3-1/prompt.txt: cde2ad18f153b0856791022261a1343fe5ee8817f3015dd46be3cdaae8acb6ca
        A/tables/TABLE-1-page-3-1/meta.json: a8cea23688c53e2bea2fd4950c765b5fa558405a48ccf9d25e963e972f15db39
        A/tables/TABLE-8-page-11-8/raw.json: 22c5b93f00aa481f8218d64f08e2c21d29db3482cf3a35ecb37ec3892c92cf1d
        A/tables/TABLE-8-page-11-8/prompt.txt: 2bdb46bbaa3a7e87b34ad08d8cd76c6dc89fe16a56c0558cfd621aced658ddbd
        A/tables/TABLE-8-page-11-8/meta.json: f378306167bba34292708bee739c4ff1805f6570e20f5f03a980fbf20d960581
        B/passages.json: 5bb1c488835ccb3a27f1339ddec7165b39163faef15b3bb1f87de2040774adeb
        B/raw.json: 7e10fa2443e41bb569d078c65be19e4f9d22ae9bf8f91d51a7b0bc1c5c6beefb
        B/source-units.json: 33d3a28dc031bc41c60ca1b18d39e15b86903c6fbed9dfca1847cca215b161e5
        B/full-source-units.json: b0d7ef51deb8a34e15aa73c5c10e5f21a578f03f3d3d44dbf89ccc5ac0279039
        B/meta.json: 2237578d6253143408a635b33aa8cd31d92759226019ed25f34c2ab838529a6d
        B/table-images/TABLE-1-page-3-1.png: 713874469c4ecb8c7042c2deaf05b66c7b2ea9eb1bea1e0160f72fda1f79c11a
        B/table-images/page-11.png: 2a478acf3db6fd3c65f4a294fc4810c1ff0b884a6c96dd5e53ed2c0e492d08db
        B/table-images/page-3.png: 4f4a5e5c92950cf5398f87211a37cc7d1b94c3fbc418728ea7c99f40668b4088
        B/table-images/TABLE-7-page-11-2.png: abc4afc85fbf3259dbba02a6035d0d2d70728f648c5ffe2543e69db34e60783c
        B/table-images/page-6.png: 6f5355045dcd3786d5e682da6e10ee3767847a247a8f9478bb84ee16a357d434
        B/table-images/page-5.png: d25bbcaa1ab1c1762804b0c936ab30abfef7f4f40a102ce5d114161ae0cb782c
        B/table-images/TABLE-4-page-6-1.png: 5d3054ea6f9a06396b792288b5883023561a5ab299efe18a6f24faec8d24898a
        B/table-images/TABLE-6-page-11-1.png: cea926bc152ab9f8c1ba78ed60cdd36ee794c2ca296e90d420381c0fe0bb8bc7
        B/table-images/manifest.json: cd622e5efe507c0991b5b98b720295ed03791e329f0508f0e9c5a3f489eb183d
        B/table-images/TABLE-5-page-6-2.png: c1c321f8a03ec16675b8d608243509abd9a6495a140d827743261737c030590a
        B/table-images/TABLE-8-page-11-3.png: 30015ef6d5cd4e13373508f93812a06c7676f53850c9eee27803fe886fd54346
        B/table-images/TABLE-3-page-5-2.png: ddd561ba5da2dc717e43da1aa0a673d8a2eb23b413b0e62c0bd0a1dd6213fab1
        B/table-images/TABLE-2-page-5-1.png: 5254e1bee1334d23483087fcb2042e471a205995ab7c2b203f22ee7991d6e4cd
        B/clauses/window-03/raw.json: dfbdcd5641a32d0ad7f3616934406af218547c3c408780f2fbb452dc3827e8f7
        B/clauses/window-03/prompt.txt: 0f7bbed5425049588d9a975578ab3afdbde7b1fd3f97b64d2b001988437ffe43
        B/clauses/window-03/meta.json: 458fa26ac6a3cebf92b8eda79f86b59a9e3f9c89c1c5ee7f997b5310a2d6834c
        B/clauses/window-04/raw.json: 9de361be5919d539168fb244afe8ef326b02cfdb7a58d7ffc3989c1816f150fb
        B/clauses/window-04/prompt.txt: c03e542e762c1d60866b9d1a58cf2faba1003a72c9b0c0669b590a82cd457734
        B/clauses/window-04/meta.json: 43fcb9dedd63f270e7ae63ac6f3ea4cb902ab1c51672770efbacbdb86a0a146c
        B/clauses/window-05/raw.json: 053cdc1aeb78d7e2f16191a616678250db1719e50eae0a419b228f3cf2fcd959
        B/clauses/window-05/prompt.txt: 84a9ff0205ceefeae1eb8df2d36b3121500a9183d1d14251f9fd6b2a1e63e207
        B/clauses/window-05/meta.json: 9cc229bb2c6fd67f4eb657a8cfc4753c5f289dd872f45410d5a3f5347424bfb2
        B/clauses/window-02/raw.json: 28dc1c505a75916ce4875550d040871c61003e37f4bff42204c67c81b667e8da
        B/clauses/window-02/prompt.txt: 1612706e4ff19e87290cf8f381826e3890f0e4898640b874e9217d56113d2c17
        B/clauses/window-02/meta.json: be00dfb0a41c631e37a71fbaea37f19898dc4925d7a4bc4e48b9c27f97e56c61
        B/clauses/window-09/raw.json: 86bf4557cfb94c12431015ad0a20263bf8e695c450633bff8bdc7433726de31b
        B/clauses/window-09/prompt.txt: 5ab197241a59a15070a8e6f779dbd44ded56931cc70eec5264d258f450929bbc
        B/clauses/window-09/meta.json: 6b51db239a1c75c0fbde11e48d042d95b77e9a843df33e495f4b28ceca3acb92
        B/clauses/window-07/raw.json: 688297809be24f0c9f70ad253d39d96f30992219bf726454413349319db92c94
        B/clauses/window-07/prompt.txt: 305646c31cda7b9853f2876542cbb08bd1e3e5b6d8185fbf33889a56caa10228
        B/clauses/window-07/meta.json: 65afeedc0753514e1cfd3490196f2975e5f85e9b38cdc95b60153864d21a9068
        B/clauses/window-01/raw.json: e257cdcb912c58db66a416e1413709688204095fd8e4069c6f48d849426ac0f6
        B/clauses/window-01/prompt.txt: 0e07f3b16755876958a0bf67aae4754699a03d0698a5cb53be82282d98327f6c
        B/clauses/window-01/meta.json: 5d29462046405315a62412ca858389a9d395ee1d85ebb60e06f885093fe42a89
        B/clauses/window-06/raw.json: 1a65459636833d4583eebd24bb248997917cc4bd623141b694d51144b66e5525
        B/clauses/window-06/prompt.txt: d8942c7689b6a16f44f2702d19108e1d5a98993426d3fae3363748feb82a167c
        B/clauses/window-06/meta.json: f5d79061e0978b07226c3db07e001eacb3b2d4fdf594ed3341a04c1f4060c750
        B/clauses/window-08/raw.json: 2ee5f092cd6987013e75ddd00b0a16dd04eb3373b3b83f57b193eef0a95ed8b4
        B/clauses/window-08/prompt.txt: 3dc0d751c583b41c0d47618013f9127ec2f801673923ea68b238f8cd6d62f077
        B/clauses/window-08/meta.json: 9e353ce7c69c5783f7ea9afdf7037ea749d8bfa5b4d6c39ca7d30cd57c744770
        B/tables/TABLE-4-page-6-4/raw.json: e35652be0710ffec3bd3fd9d681430306ba36920f5dd34df5f94bedb22375e7c
        B/tables/TABLE-4-page-6-4/prompt.txt: 2ed3c4c5a27377eaa0c92e5df67a7946d771b26f7e798b6a89e1ecf810a478ba
        B/tables/TABLE-4-page-6-4/meta.json: 83dc69643bf6768f706550d232624b2122227fc57c7cfc14f3206d086dc0ea7f
        B/tables/TABLE-5-page-6-5/raw.json: 758d35a0db1d9fb3d084543211f8639e6155f9c7436a48decb9cd56f3aea3fe3
        B/tables/TABLE-5-page-6-5/prompt.txt: af3febc684505f2a57cdea3fc50f871af20dac48be7983f48d901eaa419fd95b
        B/tables/TABLE-5-page-6-5/meta.json: afec0749ca47777136220e6952deb3f8da3f601beb5feb172c995dc68a0706ad
        B/tables/TABLE-3-page-5-3/raw.json: b18e7c71f61795382356381b8201fbd63acbe7ffa45e9ee9f8942d1d7edeec50
        B/tables/TABLE-3-page-5-3/prompt.txt: df31905789807e7727fba5f21ac089b0fd5a4131e69a0e83993809142cd651d1
        B/tables/TABLE-3-page-5-3/meta.json: f69e0368d4a776d20f108e0d8b82961b09df8894a2db041b518f4791600d8a0f
        B/tables/TABLE-6-page-11-6/raw.json: 9bb230ccecadf6f90e6f3fea172c5c2f1540994b6888e5fbb60f3ba5be620e76
        B/tables/TABLE-6-page-11-6/prompt.txt: 1652aa4cb23f9fd78f3610eae285caee99cca792cf28b41c4f99d7995dd26201
        B/tables/TABLE-6-page-11-6/meta.json: d4292889f9b7f9f4e4a693d7dcecce23f92c8c6911c2142e115c8de1d96adee5
        B/tables/TABLE-2-page-5-2/raw.json: 252c268dfaef41c0784e82554fb6efcec447840bd3a58f9f75524714b71d1620
        B/tables/TABLE-2-page-5-2/prompt.txt: 1c734dfd36fa9af0c037cab4ff63e0586dbbc39af7c0919505052317cf3f14ac
        B/tables/TABLE-2-page-5-2/meta.json: ef5d3cac2c961eafb6a19fb0fde76a955136cf218bcd0246ac06f1989cdc2329
        B/tables/TABLE-7-page-11-7/raw.json: 53efae0aed8a4c19ce3e66932fbad147b4e63e02f878c952fbcb02913e343ed1
        B/tables/TABLE-7-page-11-7/prompt.txt: ed2b04d9a302caaae3dbfe7f2215522bd2a81605ee0ca7fd24ebddfeb1be0f96
        B/tables/TABLE-7-page-11-7/meta.json: a922dd7f0166d42da9c5d3fba1690a699a676a1cded4dc2f05200fdca631a620
        B/tables/TABLE-1-page-3-1/raw.json: bc107f1352f5db49f47970d2bf28f952f87612724a73b61340a52ca49bf0fa3f
        B/tables/TABLE-1-page-3-1/prompt.txt: cde2ad18f153b0856791022261a1343fe5ee8817f3015dd46be3cdaae8acb6ca
        B/tables/TABLE-1-page-3-1/meta.json: 604ad7ca037580c07842611956af0e736a1747b90af1f0d7cfb844159ab35bdb
        B/tables/TABLE-8-page-11-8/raw.json: df890cd9ab61752cfa85a38fe209e8e9ed4b0d5750f3ca5e0c10278f23c48324
        B/tables/TABLE-8-page-11-8/prompt.txt: 2bdb46bbaa3a7e87b34ad08d8cd76c6dc89fe16a56c0558cfd621aced658ddbd
        B/tables/TABLE-8-page-11-8/meta.json: f4d6db5091929ee79b093c504a7dd56f9c59d94417814d12cb0236e0eb801dc2
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
      pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2016
      source_status_sha256: 35611474e48b6a6bb44cbd545e0dde6a742b430bdf1c491021d97f140e56b4d1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: gray-matter regional damage
    outcome:
      text: WAB scores (fluency, auditory comprehension, repetition, naming)
    analysis_label: lesion-based feature association
    relation: association
    evidence_ids:
    - P5-S1-C7
    - P6-S1-C4
    - P6-S1-C5
    - P7-S1-C1
    - P7-S1-C2
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
      pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2016
      source_status_sha256: 35611474e48b6a6bb44cbd545e0dde6a742b430bdf1c491021d97f140e56b4d1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P1-S3-C6
      - Result passage disposed without unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P7-S1-C1
      - Accounting without a linked unit P9-S1-C10
      - Accounting without a linked unit P9-S1-C2
      - Accounting without a linked unit P9-S1-C4
      - Accounting without a linked unit P9-S1-C6
      - Accounting without a linked unit P9-S1-C8
      - Accounting without a linked unit P9-S1-C9
      - Unaccounted source passage P9-S1-C9
      - Unaccounted source passage P9-S1-C10
      - Unaccounted source passage P9-S1-C4
      - Unaccounted source passage P9-S1-C6
      - Unaccounted source passage P9-S1-C2
      - Unaccounted source passage P9-S1-C8
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P9-S2-C5
      - Result passage disposed without unit P11-S2-C10
      unattached_null_or_qualifier_ids:
      - P3-S3-C5
      suppressed_nonrepresented_units: 3
      default_disposition_count_requires_completeness_check: 191
      unselected_timing_passages:
      - P1-S3-C5
      - P2-S2-C14
      - P2-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P2-S2-C3
        - P2-S3-C8
        - P2-S3-C9
        - P2-S3-C10
        - P2-S3-C11
        - P2-S3-C12
        - P2-S3-C14
        - P2-S3-C15
        - P2-S4-C2
        - P3-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S1-C3
        - P2-S1-C4
        - P2-S1-C5
        - P2-S1-C6
        - P11-S1-C11
        - P11-S1-C2
        - P11-S1-C6
        - P11-S1-C7
        - P11-S2-C2
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-3-page-5-3
      - TABLE-4-page-6-4
      - TABLE-5-page-6-5
      - TABLE-6-page-11-6
      - TABLE-7-page-11-7
      - TABLE-8-page-11-8
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-6-page-11-6
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S4
        - P3-S3
        - P4-S3
        - P4-S4
        - P5-S1
        - P6-S1
        - P7-S2
        - P8-S1
        - P9-S1
        - P9-S2
        - P10-S1
        - P11-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2016
      source_status_sha256: 35611474e48b6a6bb44cbd545e0dde6a742b430bdf1c491021d97f140e56b4d1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: States comparable prediction accuracy for both analyses.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Establishes better-than-chance prediction from spared connections.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about temporoparietal junction role.
    - source_id: P1-S3-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Restates similarity in predictive accuracy.
    - source_id: P2-S4-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1 (lesion overlap).
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes feature selection criteria for lesion analysis.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes feature selection criteria for connectome analysis.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 2
      reason: States lesion size prediction was better than chance.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses correlation between predictors.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cross-validation procedure.
    - source_id: P4-S4-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Confirms all correlations are significant.
    - source_id: P4-S4-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Identifies speech fluency as most accurate prediction.
    - source_id: P4-S4-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Compares accuracy across specific WAB scores for lesion vs connectome.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: States no significant difference in r-to-Z transformed correlations.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overestimation tendency of lesion-based analysis.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes underestimation tendency of connectome-based analysis.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Compares lesion size predictability to ROI/connectome.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies specific regions predictive of WAB scores in lesion analysis.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies specific connections predictive of WAB scores in connectome
        analysis.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 8
      reason: Restates connectome-based feature associations.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on agreement between analyses.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Identifies PSTG as important for both analyses.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Identifies precentral gyrus and pars opercularis as important for both.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Identifies angular gyrus and PSTG as relevant for both.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about feature differences.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reference to Tables 4 and 5 for accuracy.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies temporal lobe polar regions as predictive in lesion analysis.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Identifies differences in predictive features (frontal/parietal/pars
        orbitalis).
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: States predictions are comparable in accuracy but different in spatial
        features.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: States combined modality accuracy is similar to single modalities.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: States reduced connectome prediction was better than chance for most
        scores.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 1
      - 3
      reason: Restates equivalence of lesion, connectome, and lesion size accuracy.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on identifying important regions/tracts.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: States combined modality was not generally more accurate.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses correlation between lesion site and connection strength.
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on spatial sensitivity of connectome analysis.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: States predictions were better than chance without lesioned regions.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Restates better-than-chance prediction for reduced connectome.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses correspondence in feature maps.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies parietal and orbito-frontal connections as predictive.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on connectome identifying specific links.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Identifies PSTG to angular gyrus link as most implicated.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: States angular gyrus connectivity was more predictive than damage.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies angular to middle occipital gyri connection as predictive.
    - source_id: P11-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: States connectome was less accurate for naming and repetition.
    - source_id: P11-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: States connectome was more accurate for auditory comprehension.
    - source_id: P11-S3-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Restates ability to predict WAB subscores from intact regions.
    unresolved_coverage:
    - source_id: P4-S3-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P2-S4-C12
    - P3-S3-C5
    - P3-S3-C8
    - P4-S3-C9
    - P4-S4-C2
    - P4-S4-C4
    - P5-S1-C2
    - P5-S1-C3
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C6
    - P9-S1-C4
    - P9-S1-C8
    - P9-S1-C9
    - P9-S1-C10
    - P9-S2-C3
    - P9-S2-C5
    - P10-S1-C2
    - P10-S1-C3
    - P11-S2-C8
    - P11-S2-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    - TABLE-3-page-5-3
    - TABLE-4-page-6-4
    - TABLE-5-page-6-5
    - TABLE-6-page-11-6
    - TABLE-7-page-11-7
    - TABLE-8-page-11-8
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C13
      recruited_sample:
      - P2-S2-C10
      eligibility:
      - P2-S2-C11
      - P2-S2-C12
      imaging_provenance: []
      imaging_timing:
      - P2-S3-C7
      outcome_timing:
      - P2-S3-C7
      outcome_definition:
      - P2-S3-C6
      validation:
      - P2-S2-C7
      - P3-S3-C10
      analysis_restrictions:
      - P3-S1-C6
      - P11-S1-C9
      dependent_variable_statement:
      - P2-S3-C6
      - P3-S3-C3
      - P4-S1-C2
      - P4-S2-C6
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C14
      - P2-S3-C5
      - P2-S3-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P2-S2-C3
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C14
      - P2-S3-C15
      - P2-S4-C2
      - P3-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C6
      - P11-S1-C11
      - P11-S1-C2
      - P11-S1-C6
      - P11-S1-C7
      - P11-S2-C2
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
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
      pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
      review_sha256: 6df5c5e305c5c91c620d81aad4dc81697fb0341522f9dab5bb3079c21f90be67
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
      - P5-S1-C7
      - P6-S1-C4
      - P6-S1-C5
      - P7-S1-C1
      - P7-S1-C2
      source_result: The study utilized a multivariate support vector regression (SVR)
        framework to predict Western Aphasia Battery (WAB) scores (fluency, auditory
        comprehension, repetition, naming) from regional gray-matter damage. The patient
        measurement was the proportion of intact voxels within predefined gray-matter
        regions (template_lesion_overlap), derived from manually drawn lesions on
        T2 images normalized to standard space. The analysis identified specific cortical
        regions (e.g., precentral gyrus, PSTG) as significant predictors for specific
        language domains, with prediction accuracy significantly better than chance.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the lesion-based SVR prediction
            of WAB scores. The source confirms the use of SVR with linear kernel,
            leave-one-participant-out cross-validation, and the specific outcome variables
            (WAB subscores). The evidence IDs correctly point to the results describing
            the predictive regions and accuracy.
          source_ids:
          - P3-S2-C12
          - P3-S3-C10
          - P4-S1-C3
          - P5-S1-C7
        direction:
          answer: fits
          reason: The source indicates that the model successfully predicted WAB scores
            (correlations significant, p < 0.000005). The direction of the relationship
            is that greater intactness (less damage) in specific regions is associated
            with higher WAB scores (better function), as implied by the feature selection
            and the nature of the predictor (proportion of intact voxels). The draft's
            'likely' direction is consistent with the detected positive association
            between integrity and performance.
          source_ids:
          - P4-S4-C2
          - P4-S2-C3
          - P5-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as gray-matter regional damage.
            The patient measurement is template_lesion_overlap, as the lesions were
            normalized to a standard space and overlaid on an atlas (Faria et al.,
            2012) to compute the proportion of intact voxels per region. The outcome
            is WAB scores. The method is MVPA (SVR). This matches the source description
            in P3-S1-C4 and P3-S3-C5.
          source_ids:
          - P3-S1-C4
          - P3-S3-C5
          - P2-S4-C14
          - P2-S3-C6
        qualifications:
          answer: fits
          reason: 'The draft includes relevant qualifications: fluency was the most
            accurate prediction, lesion-based analysis was more accurate than connectome-based
            for fluency/repetition/naming, and the model used leave-one-out cross-validation.
            These are supported by P4-S4-C4, P4-S4-C5, and P3-S3-C10. The feature
            selection threshold (p < 0.05 Bonferroni) is also correctly noted.'
          source_ids:
          - P4-S4-C4
          - P4-S4-C5
          - P3-S3-C10
          - P4-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding overestimation of scores
            and the predictive power of lesion size. It does not omit material caveats
            that would change the interpretation of the core association. The distinction
            between lesion-based and connectome-based results is maintained. No critical
            caveat regarding the validity of the association itself is missing.
          source_ids:
          - P5-S1-C2
          - P5-S1-C4
          - P7-S1-C3
      optional_pending:
      - sample.time_post_onset
      - exact_correlation_values
      - specific_region_coordinates
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - sample.time_post_onset
    - exact_correlation_values
    - specific_region_coordinates
    normalizations:
    - field: sample.time_post_onset
      original: at least 6 months after stroke; MRI scanning performed within 2 days
        of behavioral testing
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R008
      exposure:
        text: gray-matter regional damage
      outcome:
        text: WAB scores (fluency, auditory comprehension, repetition, naming)
      analysis_label: lesion-based feature association
      relation: association
      evidence_ids:
      - P5-S1-C7
      - P6-S1-C4
      - P6-S1-C5
      - P7-S1-C1
      - P7-S1-C2
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
        pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
        source_review: _compare/relationships-2026-11-16/review-current/Yourganov2016
        source_status_sha256: 35611474e48b6a6bb44cbd545e0dde6a742b430bdf1c491021d97f140e56b4d1
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e94506cac9662e3995b752c2dcf43cc849d3609764272a9a6c3e0bad0ade6161
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C3
          page: 2
          text_layer_sha256: e94506cac9662e3995b752c2dcf43cc849d3609764272a9a6c3e0bad0ade6161
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "All partici-\npants were at least 6 months after stroke, and\
          \ the mean \x03 SD time since\nstroke onset was 42.8 \x03 50 months (range,\
          \ 6–276 months)."
        anchor_text: "All partici-\npants were at least 6 months after stroke, and\
          \ the mean \x03 SD time since\nstroke onset was 42.8 \x03 50 months (range,\
          \ 6–276 months)."
        excluded_fragments: []
      P2-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8e0b93b4280bba28aaa0d8fc1b62253eef3c2046444184c17b83961a72d01c0c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C7
          page: 2
          text_layer_sha256: 8e0b93b4280bba28aaa0d8fc1b62253eef3c2046444184c17b83961a72d01c0c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Imaging data

          MRI scanning was performed within 2 d of behavioral testing of language

          abilities.'
        anchor_text: 'Imaging data

          MRI scanning was performed within 2 d of behavioral testing of language

          abilities.'
        excluded_fragments: []
        image_sha256: 94484d552d8ab4f5d8903da3b8d8aec80a3ce144ca1ee13d82a19b8c8ba6eff5
        transcription: 'Imaging data

          MRI scanning was performed within 2 d of behavioral testing of language

          abilities'
      P5-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e0ff583339e6382052bbf13a2ff1a95dc393932fa0edf27fee24037e53fd4de7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7fd45ce6ab86ddfa1903a37281e062298dd3b58a54b0964e6d36260237044f65
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C4
          page: 5
          text_layer_sha256: 7fd45ce6ab86ddfa1903a37281e062298dd3b58a54b0964e6d36260237044f65
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "When Tables 3–5 are compared, we can see\nthat lesion size\
          \ is approximately as predictive as ROI-specific\ndamage and connectome\
          \ integrity (there was no significant dif-\nference in r-to-Z transformed\
          \ correlations; p \a 0.15); this is ex-\npected given the correlation between\
          \ overall lesion size and\namount of damage in some regions (Fig. 3)."
        anchor_text: "When Tables 3–5 are compared, we can see\nthat lesion size is\
          \ approximately as predictive as ROI-specific\ndamage and connectome integrity\
          \ (there was no significant dif-\nference in r-to-Z transformed correlations;\
          \ p \a 0.15); this is ex-\npected given the correlation between overall\
          \ lesion size and\namount of damage in some regions (Fig. 3)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'In this study, we applied a predictive multivariate framework to investigate
    the relationship between

    language deficits in human participants with chronic aphasia and the topological
    distribution of structural brain damage, defined as

    post-strokenecrosisorcorticaldisconnection.Weanalyzedlesionmapsaswellasstructuralconnectomemeasuresofwhole-brainneural

    network integrity to predict clinically applicable language scores from the Western
    Aphasia Battery (WAB).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
