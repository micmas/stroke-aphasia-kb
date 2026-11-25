---
id: left_atr_lesion_percentage
name: left anterior thalamic radiation lesion percentage
kind: tract
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: ambiguous_or_composite
    original_target: semantic_composite_score
    reason: A score, generic outcome or composite label does not uniquely identify a behaviour. Check the
      task, subtests and analysis before retargeting.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: semantic_composite_score
  target_kind: impairment
  claim: When lesion percentage was used as the predictor, the left anterior thalamic
    radiation showed a significant unique effect in predicting semantic composite
    scores after controlling for the contribution of the left inferior fronto-occipital
    fasciculus and left uncinate fasciculus.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 76
    population: Right-handed patients with brain damage (majority stroke)
    phase: not_reported
    time_post_onset: At least 1 month post-onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Analyses were constrained by the lesion distribution in the patient group, with
    a tendency toward middle cerebral artery territory lesions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the 25%-threshold sub-template
    of the JHU white-matter tractography atlas for the left anterior thalamic radiation,
    measured as the percentage of lesion voxels within the tract. The semantic composite
    score is an average of z-transformed t-scores from three semantic tasks; The result
    was obtained via hierarchical regression where other tracts of interest were entered
    first. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S3-C6, two-model agreement, human
    verification pending): . The majority of the remaining 76 patients (61

    males) patients suffered from stroke (n = 66) Original text-layer quotation is
    preserved below. PDF image reading (P12-S3-C10, two-model agreement, human verification
    pending): . Consistent with the

    literature (Schwartz et al., 2009), our patients tended to have

    lesions in the territory of the middle cerebral artery and thus rele-

    vant tracts would have larger variances in the data set, leading to

    greater statistical power Original text-layer quotation is preserved below.'
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
    - proposed_concept:semantic_composite_score
  citation: '@Han2013'
  source_passages:
  - section: Original source P9-S1-C3
    page: 9
    quote: 'When lesion

      percentage was considered, the left ATR showed a signiﬁcant

      unique effect as indicated by the fact that it had signiﬁcant pre-

      dictive power for semantic composite scores (r2 change = 0.06,

      P 5 0.02) after controlling for the contribution of left IFOF and

      left uncinate fasciculus.'
    supports: claim
  - section: Original source P5-S1-C9
    page: 5
    quote: 'Tract–semantic mapping

      To identify major white matter tracts, we adopted a widely used

      human brain white-matter template, the ‘JHU white-matter tractogra-

      phy atlas’ from FSL (http://www.fmrib.ox.ac.uk/fsl/data/atlas-descrip

      tions.html#wm), which contains 20 main white matter bundles and

      has three individual sets of sub-templates with different probability

      levels in the probability tractography map: 0%, 25% and 50%, re-

      '
    supports: method
  - section: Original source P5-S2-C3
    page: 5
    quote: 'We chose to use the 25%-threshold sub-

      template, which contains 20 major tracts (Table 1).'
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: 'For each of

      the remaining 17 tracts, the lesion percentage (number of voxels

      with lesion divided by total number of voxels in the tract) was corre-

      lated with patients’ scores in each of the three semantic tasks, as well

      as the semantic composite score.'
    supports: method
  - section: Original source P2-S3-C4
    page: 2
    quote: 'Patients

      Eighty-three patients with brain damage (68 males) from the China

      Rehabilitation Research Centre who were willing to participate in the

      study were recruited with the following inclusion criteria: no previous

      brain injury; no other neurological or psychiatric disease such as alco-

      hol abuse or severe depression; at least 1 month post-onset; able to

      follow task instructions; and right-handed (Edinburgh Handedness

      Inventory, Oldﬁeld, 1971).'
    supports: sample
  - section: Original source P2-S3-C6
    page: 2
    quote: 'The majority of the remaining 76 patients (61

      males) patients suffered from stroke (n = 66).'
    supports: sample
  - section: Original source P3-S4-C3
    page: 3
    quote: 'Besides the t-score for each task, for each patient

      we also calculated a semantic composite score by averaging the

      z-transformed t-scores on the three critical semantic tasks, as an over-

      all index of semantic processing ability.'
    supports: claim
  - section: Original source P12-S3-C10
    page: 12
    quote: 'Consistent with the

      literature (Schwartz et al., 2009), our patients tended to have

      lesions in the territory of the middle cerebral artery and thus rele-

      vant tracts would have larger variances in the data set, leading to

      greater statistical power.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Han2013
  proposal_id: R008
  review_status_sha256: faf6e945a89911e88c1268c4f9fa3c28b5d4b1cd33c308396cc540eebfee407b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
        A/passages.json: 5bfc49bd8a5a2f855855b6960e2415bf975b15a22a51ce8cf2b2226c3799555a
        A/raw.json: 1c47b06467110dbba8e0039d01d663cdb7b2a369acc7d41737ab509cd30d43ef
        A/source-units.json: d98f0ac5ede6476dbb927204de45a46edbacade5d220c97629c05124590a1e7b
        A/full-source-units.json: bbb077e358f2c3a8d35dad040d6c2c72c98cda82da9f22235c41ef0b3e7fb9df
        A/meta.json: e47e3d5d2e95b7620755da28ef042859a5b45e60d4486294064969af6750c2c8
        A/table-images/TABLE-1-page-6-1.png: 84a263c77f49d8e583ed60d6d37ea9f5101f482a83c488c1789708b604f5c793
        A/table-images/page-6.png: 68ddec187e52bf0d37235e402c1a39bf1b69fc24c5981bd4d24b4c66c73e6685
        A/table-images/page-7.png: e0ac28ef4c6ec9ac2880c0c136a407fe49091c42f238649444e6d30134a99f95
        A/table-images/manifest.json: ea6a4a3a6c3ba95fd10198d75991331021ba863144d3b4619f13db744545481a
        A/table-images/TABLE-2-page-7-1.png: 8282fadf77ee264f0356fcb3cdca542c447f86e1ed6890a9c136363fbc61ec2d
        A/clauses/window-10/raw.json: 21a18cbf147e872c6ce072a7351084367c86b48b53c50bfb4669022140dfa2de
        A/clauses/window-10/prompt.txt: 30778cc42d7add4feca86255051dc3c200c88284db8c9104d27e6a56b2307364
        A/clauses/window-10/meta.json: 053434bd2d8b82e5e4bf96e4cdce18231329cea2d905ae8bd67e36b76ba7f22d
        A/clauses/window-03/raw.json: 31f163c32354876062a44fa5e2f7074a19d67632f458706616461d68ced1ca44
        A/clauses/window-03/prompt.txt: 75e27b8b3184391c8daa49860ade7a49af83335df6a9a437eba5f4ca7c0b1b7c
        A/clauses/window-03/meta.json: 27c8d7e516e09cd848fefa4a91608fcce5e059d529dbc00ce15656e1d9160477
        A/clauses/window-04/raw.json: ec52f7783892c505a96df804dcba7e26f47bc9ca72881295a6f87bb4c1071e4e
        A/clauses/window-04/prompt.txt: 952e33f1a2000929cf5861acc7ef999d2c4a0544fa66beb21c139e0bc6db8660
        A/clauses/window-04/meta.json: 4c255e32b2811ace69e7faa9cae334039a194b0c5e3680786d4d6f64205b0d39
        A/clauses/window-05/raw.json: 6cd0a386eed728f287d2e3d98f5704ae13bb990a14250ca62db5dfca9c782501
        A/clauses/window-05/prompt.txt: f10a46a865bda79e8bf81805fe0e7f521c08ba65da719c7f1454c54afbca642d
        A/clauses/window-05/meta.json: d72779869bed49806240d2eb6cb45333faab042be086c29c33f64e2e2a6b4200
        A/clauses/window-02/raw.json: ea23004b0895dea5d33be0b884914e6de0a0eb8ae1653282f9f611be934c2586
        A/clauses/window-02/prompt.txt: e86d364ab71b5f9daeb01d2fcecdf69725c2ddda842f0d8895de906680d719d5
        A/clauses/window-02/meta.json: de0d039bedd2e8059bb8942607a2c32a64051ba599015bd0f898949cdc1a512f
        A/clauses/window-09/raw.json: 2de44b963ca38ef4807671cc2424d21b98dcc5bd64250120f8efc753421753fd
        A/clauses/window-09/prompt.txt: 7e719a1a451f6e05e64cde1744f5d7a658f4a88ddeb1a90e8d421f9f450db1de
        A/clauses/window-09/meta.json: 3dd9f2cdeab1ea11d0309a158ac749a671dd7a38db1af24d6ce771b25f9655cd
        A/clauses/window-07/raw.json: 468a8268b6e4a7c7512534fff333d14bd675f5caa56a4baddce7050fd2c189a6
        A/clauses/window-07/prompt.txt: 3f87874b2b32d6bf912741f9350aa3e14802c8336c7b134821be17c715a84a73
        A/clauses/window-07/meta.json: 5f85dbb1cf2b93aca22b8383296b1d2fe7db15f1a4facf589d97bda4e218b372
        A/clauses/window-01/raw.json: baf9c961decf1d20a770fa03679de71d558717b865f9cba40c3f101342b4735e
        A/clauses/window-01/prompt.txt: bd13c5be2dec2368e6a0ea51e89e6d3bfc2bbf96cb9286e3cf6098440d6ddc9e
        A/clauses/window-01/meta.json: 227f2d7fe64ef74690bccf6f4fb8b4cda8706d361d1ce0ba09cdd3a7696865f5
        A/clauses/window-06/raw.json: 870d6a7cf7231a21374cd4f359626d4e95df2bd5eb53ddfc99bb0fae98037571
        A/clauses/window-06/prompt.txt: cf0373f96bbf283ccca3892afd2754ed43240f2cddb1d9a57d124e5a226659a3
        A/clauses/window-06/meta.json: 8a754d9fb8c0228e1cfeb0c1dc08460a7fc1b41843e1bd3f27578bb6cabbbfbd
        A/clauses/window-08/raw.json: 00cfc31962679335bbbd886ba4d24f67990d98ee1ad494d15ad2675c20d7b835
        A/clauses/window-08/prompt.txt: 251f29423a5a4270cad29d7b06d17a58daa1f0a7f3911e29d05f4917a3628b74
        A/clauses/window-08/meta.json: b69a6141e810c9df3be9438c6303ae5c28a8a8575fb8b9ea4cbc3a62802f4799
        A/tables/TABLE-1-page-6-1/raw.json: c5916583f23ea23989b80fa370bb165e11f7a994d903c79abbaeb0d9f34c01e9
        A/tables/TABLE-1-page-6-1/prompt.txt: eee65ef5bf5a385399b9bac364bcec637490eb8104b8ba33a241be0eccb1b966
        A/tables/TABLE-1-page-6-1/meta.json: ae720ea19814db397235fdde86e646ef84b966dda48f478488c01fdd964370d0
        A/tables/TABLE-2-page-7-2/raw.json: 3967d02bd62d47f370faf69e30948f65abbabd18cfa654bea87daf03f99556af
        A/tables/TABLE-2-page-7-2/prompt.txt: 34bac98f2fb4f32ce9c2c3a181e7a61952ce5380a0c61c6697147f7c24252083
        A/tables/TABLE-2-page-7-2/meta.json: e585c96022d99ce98b322c549400580c4a0bc17d50a57271deacfd4412fb9ac8
        B/passages.json: 5bfc49bd8a5a2f855855b6960e2415bf975b15a22a51ce8cf2b2226c3799555a
        B/raw.json: 2f38e10557c0d993df557033ab304c97e51dad9448339bc7ac1bbf7fba80f960
        B/source-units.json: d98f0ac5ede6476dbb927204de45a46edbacade5d220c97629c05124590a1e7b
        B/full-source-units.json: bbb077e358f2c3a8d35dad040d6c2c72c98cda82da9f22235c41ef0b3e7fb9df
        B/meta.json: 6b22cb6a9eb2e5ed3417afb50dc0fd493e4819db4743f429f7540817d283e0a9
        B/table-images/TABLE-1-page-6-1.png: 84a263c77f49d8e583ed60d6d37ea9f5101f482a83c488c1789708b604f5c793
        B/table-images/page-6.png: 68ddec187e52bf0d37235e402c1a39bf1b69fc24c5981bd4d24b4c66c73e6685
        B/table-images/page-7.png: e0ac28ef4c6ec9ac2880c0c136a407fe49091c42f238649444e6d30134a99f95
        B/table-images/manifest.json: 479300734ed1edc4004919fec87db06213100337d28bacdb19715e96c792783f
        B/table-images/TABLE-2-page-7-1.png: 8282fadf77ee264f0356fcb3cdca542c447f86e1ed6890a9c136363fbc61ec2d
        B/clauses/window-10/raw.json: 03fd1ad1a69942833fdaad6430462250f7c4b5f164e9c16f2ab6258dca4124db
        B/clauses/window-10/prompt.txt: 30778cc42d7add4feca86255051dc3c200c88284db8c9104d27e6a56b2307364
        B/clauses/window-10/meta.json: 678016137061918e98141ed9837ec5266305cfcad732f2c14439c4a61f16e3e8
        B/clauses/window-03/raw.json: 167f09b5248d0b6176e8306c2c8848d99d04f6f2f679b92fd67dea6aa020ed12
        B/clauses/window-03/prompt.txt: 75e27b8b3184391c8daa49860ade7a49af83335df6a9a437eba5f4ca7c0b1b7c
        B/clauses/window-03/meta.json: 7d470787600488edea086696a0916149dfd79a0ce7cbb537710e5a7769178aef
        B/clauses/window-04/raw.json: 6d957aadc8f62ba2159a525b8d49a98595e0b8d19edc5eb5948c598a318cc296
        B/clauses/window-04/prompt.txt: 952e33f1a2000929cf5861acc7ef999d2c4a0544fa66beb21c139e0bc6db8660
        B/clauses/window-04/meta.json: 017a08ebe7d96d1aa3131b558350ac5a888fdcd82cb6c92301b6f24436b4c689
        B/clauses/window-05/raw.json: 3140f537bd6737953aa3f48a2709420d50ca8f0bee68c823dba6091053e6fa4a
        B/clauses/window-05/prompt.txt: f10a46a865bda79e8bf81805fe0e7f521c08ba65da719c7f1454c54afbca642d
        B/clauses/window-05/meta.json: f3afcf87aea9ef9cfee2a0b06c528f28c759c00e0b1240a7b0eec6baaad3237e
        B/clauses/window-02/raw.json: 2351f225ceddbbd93fac2ac7f6bf759644ba8af5136e494ede89b81912b15410
        B/clauses/window-02/prompt.txt: e86d364ab71b5f9daeb01d2fcecdf69725c2ddda842f0d8895de906680d719d5
        B/clauses/window-02/meta.json: 5441cf7da062056329dbd0e33e090baa415648e7b1a5c08a33535dbfe1cc1e86
        B/clauses/window-09/raw.json: 3db25ade3d83b3796aa8e69ea8774beb470a749e658bbdfa29cc283e9d67d456
        B/clauses/window-09/prompt.txt: 7e719a1a451f6e05e64cde1744f5d7a658f4a88ddeb1a90e8d421f9f450db1de
        B/clauses/window-09/meta.json: e34fef74529c1135eaa906affc9395eb3d8db79bc261c198efe8cfbec237018b
        B/clauses/window-07/raw.json: 0e26653d04a609e8ad5b68fb0126c04d97566872c6ea2059c4301a1be4e24b42
        B/clauses/window-07/prompt.txt: 3f87874b2b32d6bf912741f9350aa3e14802c8336c7b134821be17c715a84a73
        B/clauses/window-07/meta.json: c976825ef38e93bd9406197d009b8f9a7357d9f93b64891178891955b8f3e8ff
        B/clauses/window-01/raw.json: e70fdfd737e093f30b006d6f6725e659f365a7613889a1a407a5649a35fda7e9
        B/clauses/window-01/prompt.txt: bd13c5be2dec2368e6a0ea51e89e6d3bfc2bbf96cb9286e3cf6098440d6ddc9e
        B/clauses/window-01/meta.json: f5af2755733ffb990b3cd0e68e6b865ed14c6a2383db60313bdf8db338bd2b32
        B/clauses/window-06/raw.json: db124d67add296477eb6f8424182f3bc40b3614b64b199ace6cf26df2ce79896
        B/clauses/window-06/prompt.txt: cf0373f96bbf283ccca3892afd2754ed43240f2cddb1d9a57d124e5a226659a3
        B/clauses/window-06/meta.json: 79b63232d2afda792d60c565087399e0036dfc391b0f0d39868e013839a5ca65
        B/clauses/window-08/raw.json: ebe02ebf693181f1cd6127a4e05874d6064be3292ef86b6b638a25774ad0f998
        B/clauses/window-08/prompt.txt: 251f29423a5a4270cad29d7b06d17a58daa1f0a7f3911e29d05f4917a3628b74
        B/clauses/window-08/meta.json: 11de56a1172fb10cf1b33c2da208e3009c324a11757ca40852a4b942f8a301db
        B/tables/TABLE-1-page-6-1/raw.json: cc69a6ff01631635878418e19fc458e3bc64650de55d2415bfee39dcdbf8a950
        B/tables/TABLE-1-page-6-1/prompt.txt: eee65ef5bf5a385399b9bac364bcec637490eb8104b8ba33a241be0eccb1b966
        B/tables/TABLE-1-page-6-1/meta.json: 681bafc27f7f605c1afa369b7d3046ed6887bbc495b89438a110d72598d6f7e2
        B/tables/TABLE-2-page-7-2/raw.json: 5f0e65ac44fe7a585d26b43a7ea8169e56e59706357d883b85fd178b110b7440
        B/tables/TABLE-2-page-7-2/prompt.txt: 34bac98f2fb4f32ce9c2c3a181e7a61952ce5380a0c61c6697147f7c24252083
        B/tables/TABLE-2-page-7-2/meta.json: 1241c086c030924c757e6f254777c79dee8e6a6c0a759bea675c54d69784425b
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
      pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
      source_review: _compare/relationships-2026-11-16/review-current/Han2013
      source_status_sha256: d35502344411217ed13b23bef0f06b1dc16021ce7f72a31a58254e7989f397d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: left anterior thalamic radiation (ATR) lesion percentage
    outcome:
      text: semantic composite scores
    analysis_label: Hierarchical regression (lesion percentage)
    relation: association
    evidence_ids:
    - P9-S1-C3
    qualifier_ids:
    - P9-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
      source_review: _compare/relationships-2026-11-16/review-current/Han2013
      source_status_sha256: d35502344411217ed13b23bef0f06b1dc16021ce7f72a31a58254e7989f397d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C6'
      - Result passage disposed without unit P1-S1-C6
      - Accounting without a linked unit P1-S2-C3
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S2-C2
      - Result passage disposed without unit P8-S2-C7
      - Accounting without a linked unit P8-S2-C8
      - Accounting without a linked unit P8-S2-C9
      - Result passage disposed without unit P8-S3-C1
      - Accounting without a linked unit P8-S3-C2
      - Accounting without a linked unit P8-S3-C3
      - Result passage disposed without unit P8-S3-C4
      - Unaccounted source passage P8-S3-C2
      - Unaccounted source passage P8-S2-C9
      - Unaccounted source passage P8-S2-C8
      - Unaccounted source passage P8-S3-C3
      - Result passage disposed without unit P8-S3-C5
      - Accounting without a linked unit P8-S3-C7
      - Accounting without a linked unit P8-S3-C8
      - Accounting without a linked unit P8-S4-C1
      - Accounting without a linked unit P8-S4-C2
      - Accounting without a linked unit P9-S1-C1
      - Accounting without a linked unit P9-S1-C3
      - Accounting without a linked unit P9-S1-C4
      - Unaccounted source passage P8-S3-C8
      - Unaccounted source passage P8-S4-C1
      - Unaccounted source passage P9-S1-C4
      - Unaccounted source passage P9-S1-C3
      - Unaccounted source passage P9-S1-C1
      - Unaccounted source passage P8-S4-C2
      - Unaccounted source passage P8-S3-C7
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P9-S1-C7
      - Result passage disposed without unit P10-S3-C3
      - Result passage disposed without unit P10-S3-C4
      - Result passage disposed without unit P10-S3-C5
      - Result passage disposed without unit P10-S3-C6
      - Result passage disposed without unit P10-S4-C1
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C3
      - Accounting without a linked unit P11-S2-C2
      - Accounting without a linked unit P11-S3-C2
      - Accounting without a linked unit P11-S3-C7
      - Unaccounted source passage P11-S2-C2
      - Unaccounted source passage P11-S3-C2
      - Unaccounted source passage P11-S3-C7
      - Accounting without a linked unit P12-S1-C10
      - Accounting without a linked unit P12-S1-C11
      - Result passage disposed without unit P12-S1-C6
      - Unaccounted source passage P12-S1-C11
      - Unaccounted source passage P12-S1-C10
      - Accounting without a linked unit P12-S3-C4
      - Accounting without a linked unit P12-S3-C8
      - Unaccounted source passage P12-S3-C4
      - Unaccounted source passage P12-S3-C8
      - Result passage disposed without unit P12-S4-C3
      - Result passage disposed without unit P13-S1-C1
      unattached_null_or_qualifier_ids:
      - P8-S1-C10
      - P8-S2-C7
      - P8-S3-C3
      - P8-S3-C5
      - P8-S3-C8
      - P9-S1-C3
      - P9-S1-C4
      - P10-S3-C3
      - P10-S3-C4
      - P10-S3-C6
      - P11-S1-C2
      - P11-S2-C2
      - P12-S3-C4
      suppressed_nonrepresented_units: 25
      default_disposition_count_requires_completeness_check: 190
      unselected_timing_passages:
      - P2-S3-C4
      - P2-S3-C9
      - P2-S3-C12
      - P5-S2-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
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
        source_id: P8-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S4-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S3-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S3-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S3-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: imaging_provenance
        source_ids:
        - P3-S2-C2
        - P3-S2-C3
        - P3-S2-C4
        - P3-S2-C5
        - P3-S2-C6
        - P3-S2-C7
        - P3-S2-C8
        - P3-S2-C9
        - P4-S1-C2
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C11
        - P5-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P5-S2-C7
        - P5-S2-C9
        - P5-S3-C3
        - P5-S3-C9
        - P5-S4-C3
        - P7-S1-C3
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C4
        - P7-S2-C5
        - P8-S1-C2
        - P8-S1-C3
        - P10-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P12-S3-C3
        - P12-S3-C4
        - P12-S3-C5
        - P12-S3-C6
        - P12-S3-C7
        - P12-S3-C8
        - P12-S3-C9
        - P12-S3-C10
        - P12-S3-C11
        - P12-S3-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C6
        - P2-S2-C7
        - P3-S3-C2
        - P3-S3-C5
        - P5-S1-C8
        - P5-S2-C9
        - P5-S3-C3
        - P5-S3-C7
        - P5-S4-C5
        - P7-S1-C3
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C2
        - P7-S2-C3
        - P7-S2-C4
        - P7-S2-C5
        - P8-S1-C2
        - P8-S1-C3
        - P10-S1-C11
        - P10-S2-C2
        - P10-S2-C3
        - P10-S3-C1
        - P10-S3-C2
        - P10-S3-C3
        - P10-S3-C4
        - P10-S3-C5
        - P10-S3-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - analysis_restrictions
      - limitations
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-7-2
      unlinked_tables:
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P7-S1
        - P8-S1
        - P8-S2
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
      source_review: _compare/relationships-2026-11-16/review-current/Han2013
      source_status_sha256: d35502344411217ed13b23bef0f06b1dc16021ce7f72a31a58254e7989f397d9
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports significant correlations of lesion volume and FA of left IFOF,
        ATR, and UF with semantic tasks.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: States associations remained significant after controlling for confounders.
    - source_id: P1-S2-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Qualifies the outcome as impairment in all three semantic tasks.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of specificity to object semantic processing.
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/clinical description of MMSE scores.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/clinical description of control MMSE scores.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of convergence between 25% and 50% maps.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of excluded tracts.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Raw accuracy scores of patients.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Raw accuracy scores of controls.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Regression model coefficients for predicted accuracy.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Predicted performance estimates.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Normalized t-scores of patients.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to lesion overlap map.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion frequency per tract.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion frequency per tract.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant negative correlation of left IFOF, ATR, and UF lesion
        percentages with all three semantic tasks.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation for left SLF (not part of the primary three-tract
        set).
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation for right corticospinal tract.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation with semantic composite score for multiple tracts.
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of replication with raw accuracy/stroke patients.
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant positive correlation of FA of left IFOF, ATR, and
        UF with all three semantic tasks.
    - source_id: P8-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports FA correlations for other tracts (CST, ILF, SLF).
    - source_id: P8-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports FA correlations for other tracts (CST, SLF).
    - source_id: P8-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports FA correlations for right hemisphere tracts.
    - source_id: P8-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports FA correlation with composite score for multiple tracts.
    - source_id: P8-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of replication with raw accuracy.
    - source_id: P8-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of replication in stroke patients.
    - source_id: P8-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of FA vs lesion measures.
    - source_id: P8-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between lesion and FA measures.
    - source_id: P8-S3-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Reports significant partial correlations of FA with composite scores
        after controlling for lesion percentage.
    - source_id: P8-S4-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Provides specific partial r values for FA and composite scores.
    - source_id: P8-S4-C2
      disposition: represented
      result_indexes:
      - 13
      reason: Reports significant correlation between intact voxel FA and composite
        scores.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Provides specific r values for intact voxel FA and composite scores.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports unique predictive power of left ATR lesion percentage.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Reports lack of unique contribution for left IFOF and UF lesion percentages.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Reports marginally significant unique effect of left IFOF FA.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reports lack of unique contribution for left ATR and UF FA.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of FA effects.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of regression results.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of UF unique contribution.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of predictive ability.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of replication with raw accuracy.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifies the confound control analysis with MMSE and total lesion volume
        correlations.
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant partial correlations after factoring out MMSE and
        total lesion volume.
    - source_id: P10-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of correlation between lesion type index and composite
        scores.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant correlations after including lesion type index as
        covariate.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports results for stroke patients and left hemisphere stroke patients.
    - source_id: P10-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlations of grey matter regions with composite scores.
    - source_id: P10-S3-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant correlations of lesion percentages after covarying
        grey matter regions.
    - source_id: P10-S3-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant correlations of FA after covarying grey matter regions.
    - source_id: P10-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of significance for grey matter regions when covarying
        tracts.
    - source_id: P10-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of significance for grey matter regions when covarying
        FA.
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Reports lack of significant correlation between tracts and non-semantic
        control tasks.
    - source_id: P10-S3-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports significant correlations of composite scores with tracts when
        control tasks are covariates.
    - source_id: P10-S4-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Provides specific partial r values for the non-semantic control task
        sensitivity analysis.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of primary correlation results in discussion.
    - source_id: P11-S1-C2
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of confound control results in discussion.
    - source_id: P11-S1-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      reason: Restatement of grey matter and control task specificity results.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of anatomical connection between IFG and thalamus.
    - source_id: P12-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of UF correlations in discussion.
    - source_id: P12-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (de Zubicaray et al., 2011).
    - source_id: P12-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about lack of meaningful right hemisphere effects.
    - source_id: P12-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical discussion of network-level patterns.
    - source_id: P12-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion identifying three necessary tracts.
    - source_id: P12-S4-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restating predictive value of lesion volume and FA.
    unresolved_coverage:
    - source_id: P8-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S4-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C1
    - P1-S2-C3
    - P2-S3-C10
    - P2-S3-C14
    - P5-S2-C5
    - P5-S2-C7
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C8
    - P8-S1-C9
    - P8-S1-C10
    - P8-S2-C2
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C9
    - P8-S3-C1
    - P8-S3-C2
    - P8-S3-C3
    - P8-S3-C4
    - P8-S3-C5
    - P8-S3-C7
    - P8-S3-C8
    - P8-S4-C2
    - P9-S1-C7
    - P10-S1-C1
    - P10-S1-C2
    - P10-S1-C3
    - P10-S1-C6
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C12
    - P10-S2-C3
    - P10-S2-C5
    - P10-S3-C3
    - P10-S3-C4
    - P10-S3-C6
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C3
    - P11-S1-C6
    - P11-S2-C2
    - P11-S3-C2
    - P11-S3-C7
    - P11-S3-C10
    - P12-S1-C6
    - P12-S1-C10
    - P12-S2-C6
    - P12-S3-C4
    - P12-S3-C8
    - P12-S4-C3
    - P12-S4-C4
    - P13-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C6
      recruited_sample:
      - P2-S3-C4
      eligibility:
      - P2-S3-C4
      imaging_provenance: []
      imaging_timing:
      - P3-S2-C2
      outcome_timing:
      - P3-S3-C2
      outcome_definition:
      - P1-S1-C4
      - P2-S2-C6
      - P3-S4-C3
      - P5-S1-C7
      - P5-S1-C8
      - P5-S3-C9
      - P10-S1-C7
      validation:
      - P2-S2-C7
      analysis_restrictions: []
      dependent_variable_statement:
      - P5-S1-C7
      - P5-S3-C9
      - P5-S3-C10
      - P5-S3-C11
      limitations: []
      personal_factors:
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C12
      - P2-S3-C14
      - P3-S3-C5
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P5-S4-C3
      descriptive_personal_factors:
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C12
      - P2-S3-C14
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
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
      source_id: P8-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S4-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S3-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S3-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S3-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: imaging_provenance
      source_ids:
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C9
      - P4-S1-C2
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C11
      - P5-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: analysis_restrictions
      source_ids:
      - P5-S2-C7
      - P5-S2-C9
      - P5-S3-C3
      - P5-S3-C9
      - P5-S4-C3
      - P7-S1-C3
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C4
      - P7-S2-C5
      - P8-S1-C2
      - P8-S1-C3
      - P10-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P12-S3-C3
      - P12-S3-C4
      - P12-S3-C5
      - P12-S3-C6
      - P12-S3-C7
      - P12-S3-C8
      - P12-S3-C9
      - P12-S3-C10
      - P12-S3-C11
      - P12-S3-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C6
      - P2-S2-C7
      - P3-S3-C2
      - P3-S3-C5
      - P5-S1-C8
      - P5-S2-C9
      - P5-S3-C3
      - P5-S3-C7
      - P5-S4-C5
      - P7-S1-C3
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C2
      - P7-S2-C3
      - P7-S2-C4
      - P7-S2-C5
      - P8-S1-C2
      - P8-S1-C3
      - P10-S1-C11
      - P10-S2-C2
      - P10-S2-C3
      - P10-S3-C1
      - P10-S3-C2
      - P10-S3-C3
      - P10-S3-C4
      - P10-S3-C5
      - P10-S3-C6
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
      pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
      review_sha256: faf6e945a89911e88c1268c4f9fa3c28b5d4b1cd33c308396cc540eebfee407b
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
      - P9-S1-C3
      source_result: In a hierarchical regression analysis using lesion percentage
        as the predictor, the left anterior thalamic radiation (ATR) showed a significant
        unique effect on semantic composite scores (R2 change = 0.06, P < 0.02) after
        controlling for the contributions of the left inferior fronto-occipital fasciculus
        (IFOF) and left uncinate fasciculus. This finding was part of a broader pattern
        where these three tracts were identified as relevant to semantic processing,
        with the ATR being the only one showing a significant unique contribution
        in the lesion percentage model.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source P9-S1-C3 explicitly describes a hierarchical regression
            where left ATR lesion percentage is entered in a second step after left
            IFOF and left uncinate fasciculus, testing for unique contribution to
            semantic composite scores. The proposed core accurately identifies this
            specific analysis and its outcome.
          source_ids:
          - P9-S1-C3
          - P5-S3-C11
        direction:
          answer: fits
          reason: The source states the left ATR had 'significant predictive power'
            (P < 0.02). The proposed core uses 'likely' direction, which is a conservative
            representation of a significant association without specifying the sign
            (which is not explicitly stated in the snippet, though typically lesion
            load is negatively correlated with performance). It does not claim a null
            or opposite effect.
          source_ids:
          - P9-S1-C3
        construct:
          answer: fits
          reason: The exposure is correctly identified as 'left anterior thalamic
            radiation lesion percentage' and the outcome as 'semantic composite scores'.
            The method is correctly identified as hierarchical regression. The patient
            measurement is correctly classified as template_lesion_overlap, as the
            lesion percentage is derived from overlaying patient lesions on the JHU
            white-matter tractography atlas (P5-S1-C9, P5-S2-C3).
          source_ids:
          - P9-S1-C3
          - P5-S1-C9
          - P5-S2-C3
          - P3-S4-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the result is
            from a hierarchical regression where other tracts were entered first,
            which is the core condition of the finding in P9-S1-C3. It also notes
            the composite score definition. The limitation regarding lesion distribution
            (P12-S3-C10) is included. No material qualifiers are missing that would
            change the interpretation of this specific result.
          source_ids:
          - P9-S1-C3
          - P12-S3-C10
        missing_material_caveat:
          answer: fits
          reason: The core includes the relevant limitation about lesion distribution
            bias. The fact that this is a unique contribution analysis (controlling
            for other tracts) is captured in the claim and qualifications. No other
            material caveats from the source passages that would invalidate or fundamentally
            alter this specific result are omitted.
          source_ids:
          - P12-S3-C10
          - P9-S1-C3
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R008
      exposure:
        text: left anterior thalamic radiation (ATR) lesion percentage
      outcome:
        text: semantic composite scores
      analysis_label: Hierarchical regression (lesion percentage)
      relation: association
      evidence_ids:
      - P9-S1-C3
      qualifier_ids:
      - P9-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
        source_review: _compare/relationships-2026-11-16/review-current/Han2013
        source_status_sha256: d35502344411217ed13b23bef0f06b1dc16021ce7f72a31a58254e7989f397d9
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P9-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 25681ca98e568839cd537a3752e92b04b4809983e1192662cf134ed4ff031d56
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S1-C3
          page: 9
          text_layer_sha256: 25681ca98e568839cd537a3752e92b04b4809983e1192662cf134ed4ff031d56
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'When lesion

          percentage was considered, the left ATR showed a signiﬁcant

          unique effect as indicated by the fact that it had signiﬁcant pre-

          dictive power for semantic composite scores (r2 change = 0.06,

          P 5 0.02) after controlling for the contribution of left IFOF and

          left uncinate fasciculus.'
        anchor_text: 'When lesion

          percentage was considered, the left ATR showed a signiﬁcant

          unique effect as indicated by the fact that it had signiﬁcant pre-

          dictive power for semantic composite scores (r2 change = 0.06,

          P 5 0.02) after controlling for the contribution of left IFOF and

          left uncinate fasciculus.'
        excluded_fragments: []
        image_sha256: 39c9b8c04a5f3ea9462adbfae9b9af6d43668683ddfb3b529e5e554a37424517
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e800eec42ba1ed66aac4d90ca4fc2f0e9a09414fa3708eb7fbc89c06a1055231
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: e800eec42ba1ed66aac4d90ca4fc2f0e9a09414fa3708eb7fbc89c06a1055231
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Patients

          Eighty-three patients with brain damage (68 males) from the China

          Rehabilitation Research Centre who were willing to participate in the

          study were recruited with the following inclusion criteria: no previous

          brain injury; no other neurological or psychiatric disease such as alco-

          hol abuse or severe depression; at least 1 month post-onset; able to

          follow task instructions; and right-handed (Edinburgh Handedness

          Inventory, Oldﬁeld, 1971).'
        anchor_text: 'Patients

          Eighty-three patients with brain damage (68 males) from the China

          Rehabilitation Research Centre who were willing to participate in the

          study were recruited with the following inclusion criteria: no previous

          brain injury; no other neurological or psychiatric disease such as alco-

          hol abuse or severe depression; at least 1 month post-onset; able to

          follow task instructions; and right-handed (Edinburgh Handedness

          Inventory, Oldﬁeld, 1971).'
        excluded_fragments: []
        image_sha256: 44114766ce6a424fc22cb6da43006b3c68135e6d79f96049ad90bf59ba6bd3c9
      P2-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 450db0bf3184607acc4495bed6acab6fd367040a365ed277ac7629935de469a6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C6
          page: 2
          text_layer_sha256: 450db0bf3184607acc4495bed6acab6fd367040a365ed277ac7629935de469a6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The majority of the remaining 76 patients (61

          males) patients suffered from stroke (n = 66).'
        anchor_text: 'The majority of the remaining 76 patients (61

          males) patients suffered from stroke (n = 66).'
        excluded_fragments: []
        image_sha256: a8871c6295348f25c0cb1aadc29014070bae80b2834c48c0ed90386d1f30dd33
        transcription: '. The majority of the remaining 76 patients (61

          males) patients suffered from stroke (n = 66)'
      P12-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8fa975e81b889fcb56e07487734d069cb2a22514b941872ed3547d485bb01482
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cb9903e1a2b3da3d1b51da5ae8acabcfcf2c35afd6758fddf1cba3e536d27781
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P12-S3-C10
          page: 12
          text_layer_sha256: cb9903e1a2b3da3d1b51da5ae8acabcfcf2c35afd6758fddf1cba3e536d27781
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Consistent with the

          literature (Schwartz et al., 2009), our patients tended to have

          lesions in the territory of the middle cerebral artery and thus rele-

          vant tracts would have larger variances in the data set, leading to

          greater statistical power.'
        anchor_text: 'Consistent with the

          literature (Schwartz et al., 2009), our patients tended to have

          lesions in the territory of the middle cerebral artery and thus rele-

          vant tracts would have larger variances in the data set, leading to

          greater statistical power.'
        excluded_fragments: []
        image_sha256: 2650801d268349ffd5db0c88d0da823a74369ff6dde422986aed64133bede738
        transcription: '. Consistent with the

          literature (Schwartz et al., 2009), our patients tended to have

          lesions in the territory of the middle cerebral artery and thus rele-

          vant tracts would have larger variances in the data set, leading to

          greater statistical power'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'When lesion

    percentage was considered, the left ATR showed a signiﬁcant

    unique effect as indicated by the fact that it had signiﬁcant pre-

    dictive power for semantic composite scores (r2 change = 0.06,

    P 5 0.02) after controlling for the contribution of left IFOF and

    left uncinate fasciculus.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
