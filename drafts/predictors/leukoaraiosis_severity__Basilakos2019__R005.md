---
id: leukoaraiosis_severity
name: leukoaraiosis severity
kind: predictor
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: aq_change
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Western Aphasia Battery–Revised
    metric: Follow-up minus initial Aphasia Quotient
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: aphasia_severity_change
  target_kind: prognosis
  claim: More severe leukoaraiosis at initial evaluation predicted decline in Aphasia
    Quotient (AQ) at follow-up.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 35
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: Initial assessment at mean 36.4 months poststroke; follow-up
      assessment at least 6 months after initial evaluation (mean interval 34.8 months).
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Retrospective study design
  - Unable to control for factors influencing leukoaraiosis such as diabetes, hypertension,
    or atherosclerotic disease
  - Male-dominated sample (approximately 3:1 ratio)
  - Mean stroke age was relatively young (55.5 years)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Visual rating of periventricular hyperintensities
    and deep white matter hyperintensities on T2-weighted MRI scans using the Fazekas
    scale (total score 0-6), rated for the right hemisphere only. Initial AQ scores
    also predicted decline in AQ; The relationship was evaluated using a regression
    model that included initial AQ, stroke age, and time post-stroke at follow-up
    assessment. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S3-C1, two-model agreement, human
    verification pending): This is a retrospective study including multi–time point
    assessment of N = 35 participants (9 females; age at stroke: M = 55.5 ± 10 years,
    range = 31-71 years) in the chronic stage of recovery after a single-event left
    hemisphere stroke (ie, ≥6 months poststroke; at initial MRI assessment, M = 36.4
    ± 40.8 months poststroke, range = 6-202 months) Original text-layer quotation
    is preserved below. PDF image reading (P3-S1-C5, two-model agreement, human verification
    pending): The mean test-retest interval for all participants was 34.8 ± 26.2 months
    (range = 6-87 months) Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - not_transcribed:sample.population
    - proposed_concept:aq_change
  citation: '@Basilakos2019'
  source_passages:
  - section: Original source P7-S1-C4
    page: 7
    quote: "More severe leukoaraiosis at initial evaluation \npredicted decline in\
      \ AQ at follow-up, as did higher initial \nAQ scores."
    supports: claim
  - section: Original source P7-S1-C5
    page: 7
    quote: "Specifically, for every 1-point increase in \nFazekas score, AQ decreased\
      \ by 2.6 points (t = −2.3, P \n= .028), and for every 1-unit increase in initial\
      \ AQ, fol-\nlow-up AQ decreased by 0.22 (t = −2.6, P = .014)."
    supports: claim
  - section: Original source P3-S1-C13
    page: 3
    quote: "Leukoaraiosis was scored on the \nT2-weighted MRI scans using the Fazekas\
      \ scale,13 a \nvisual rating scale."
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: "Of note, total Fazekas \nscores ≥3 have been considered to reflect severe\
      \ white \nmatter changes, as these scores correspond to the pres-\nence of early-confluent\
      \ or confluent WMH.26 Because of \nvariability in left hemisphere lesion size\
      \ and location, rat-\nings were completed for the right hemisphere only, as\
      \ per \nprior work in post-stroke individuals23 and the assump-\ntion that leukoaraiotic\
      \ changes are generally symmetric \nbetween hemispheres.27 Scans were rated\
      \ by consensus \nby authors AB and LJ, who were blind to all participant \n\
      information."
    supports: method
  - section: Original source P2-S3-C1
    page: 2
    quote: "This is a retrospective study including multi–time point \nassessment\
      \ of N = 35 participants (9 females; age at stroke: \nM = 55.5 ± 10 years, range\
      \ = 31-71 years) in the chronic \nstage of recovery after a single-event left\
      \ hemisphere stroke \n(ie, ≥6 months poststroke; at initial MRI assessment,\
      \ M = \n36.4 ± 40.8 months poststroke, range = 6-202 months)."
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: "Inclusion criteria for these studies were as follows: \nbetween the ages\
      \ of 21 and 85 years, premorbidly right-\nhanded individuals in the chronic\
      \ (≥6 months poststroke) \nstage of recovery following a single-event left hemisphere\
      \ \nstroke, presence of aphasia (as indicated by a Western \nAphasia Battery24,25\
      \ (WAB) Aphasia Quotient (AQ) <93.8), \nand able to undergo neuroimaging on\
      \ a 3T MRI scanner."
    supports: sample
  - section: Original source P2-S3-C4
    page: 2
    quote: "All \nparticipants presented with left hemisphere stroke to the ter-\n\
      ritory of the middle cerebral artery."
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: "The mean test-retest interval for all participants was 34.8 ± \n26.2 months\
      \ (range = 6-87 months)."
    supports: sample
  - section: Original source P6-S1-C1
    page: 6
    quote: "\nBasilakos et al\t\n723\nfollow-up assessment.* Initial AQ was also used\
      \ as a pre-\ndictor in this analysis, alongside stroke age and time \npost-stroke\
      \ at follow-up assessment, as these variables \nwere significantly correlated\
      \ with AQ change (see cor-\nrelation results in the Results section)."
    supports: confounders
  - section: Original source P10-S1-C2
    page: 10
    quote: "First, the \nsample size was relatively small, and we were unable to \n\
      control for, or identify, factors that may have influenced \nthe presence and\
      \ severity of leukoaraiosis (eg, diabetes, \natherosclerotic disease, hypertension,\
      \ age)."
    supports: limitation
  - section: Original source P10-S2-C6
    page: 10
    quote: "Third, it should also be noted that the male dominated \nsample in this\
      \ study (ie, approximately a 3:1 ratio of \nmales:females) is not representative\
      \ of the fact that when \ncontrolling for age, rates of poststroke aphasia are\
      \ similar \nbetween males and females.56 However, sex differences \nin leukoaraiosis\
      \ have been reported, where women have \nbeen shown to demonstrate more severe\
      \ leukoaraiosis,57,58 \nand that WMH tend to progress more rapidly in deep \n\
      white matter regions.59 However, sex differences in leu-\nkoaraiosis are not\
      \ a unanimous finding.60 Given these \nreported sex differences in leukoaraiosis\
      \ and its progres-\nsion, further study with a larger sample size should indeed\
      \ \nexplore the role of sex on leukoaraiosis in poststroke \naphasia, and whether\
      \ this gives rise to a sex difference in \nrates of decline."
    supports: limitation
predictor_type: imaging_metric
short_definition: Visual rating of periventricular hyperintensities and deep white
  matter hyperintensities on T2-weighted MRI scans using the Fazekas scale (total
  score 0-6), rated for the right hemisphere only.
assessment:
- Fazekas scale
- Western Aphasia Battery Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Basilakos2019
  proposal_id: R005
  review_status_sha256: 792ae8a84920eeb61cc2d6ccf27dca72b3766c3f8f0c80825b514787b1794a28
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
        A/passages.json: fb05d255fb5b510c3cb6bcf39d523ddec772f709aa93e6bd8ef11f50c41b2db3
        A/raw.json: 21d43203491aa227a3499a2d41f539d550020ce02e8bb68638d1800457d158c1
        A/source-units.json: 35f9d7d086e0259d79885d8db4b4a6c361257307b80a752aa6b0e3dc1502d9d7
        A/full-source-units.json: cd24483d7d8e514c02cdcfbab33ad24819f2e8e8780341a52776172b36e7298b
        A/meta.json: 23dbf2cc023201807904ae3ae2a777657feb499f2aef9b1be30df42601305d6e
        A/table-images/page-6.png: 7830868b3bfd0f860e5d0afb8be573b41c91b8928aa150af37844c8b7c6bf2fe
        A/table-images/TABLE-3-page-8-1.png: df53998b2df560a11c297588cfc714442790cf7e3dc68c340caa8ce82ea086da
        A/table-images/page-7.png: 52593c0bd54dfb37072f3d2f85e1b7c1596d71212a1f6eba928114b5af610fff
        A/table-images/page-4.png: 3182121ef6a297b01ee17862ac2c26673ab2c5c345bd2599520a9101f371bf5d
        A/table-images/TABLE-1-page-4-1.png: 4b9af9d6b48b258184e8a48cf16660c16b440c6d39c25464fe6924ad1a32fcac
        A/table-images/page-8.png: 483f07f6213b76b1a8b87ff508d0d65a5c52c302682cab8f7ee6ed9f811bea6a
        A/table-images/TABLE-2-page-6-1.png: afad483f1432e62ad17f9509f12e27c11c449cbeff66d34429f1aff7bb821a9f
        A/table-images/manifest.json: 0f96484acf59b474eb785202fb5a720f0e4e2a94fac882d95b0962aed73ca28c
        A/table-images/TABLE-3-page-7-1.png: c5d63af8411691fccdc9d44dac78fe3efa1e4e81638a2db16bb41b283f64b3ce
        A/clauses/window-03/raw.json: 9e6b59ddfce7f9926d3934c1ef944b4f9bf6870b9670ab35beb8fb9695e5e765
        A/clauses/window-03/prompt.txt: 7eb2fcf3461a92fe259bcf80d8cb4da9fd5d5e4a021cb99b787d1a93ead27348
        A/clauses/window-03/meta.json: 570a1727c1f4d263cd8b7529838a0eb9f16bef6c6e4db3a996f0931125fad61d
        A/clauses/window-04/raw.json: 860c845757b51737a2a4bee9ada6eb1c1f740cc8fbd38f0d4907611fa7224911
        A/clauses/window-04/prompt.txt: beaa0fabdb847bb884e5170b73840e1baa50a2d5c792a7aa5ee77235dde6ec41
        A/clauses/window-04/meta.json: 659fd0f5403768be08b98b69e161dd1382fdbacad0701157f0a65fef5c1f23e3
        A/clauses/window-05/raw.json: 49e9c16addc2494e33901263ac4b9c54511dc93760750215aa19fd1890556b9c
        A/clauses/window-05/prompt.txt: b85c8f5046f17132493b03511938c68f0e81bc522e3d54feef1d50198a73f66e
        A/clauses/window-05/meta.json: 4b750a5e89335efd4e697435db5f1194e9a28fc68bb3201264ae7d1ce433050e
        A/clauses/window-02/raw.json: d14ac89973a15acef53f99e3c43d2456d123928683dd3b12f9ae7033e908dd92
        A/clauses/window-02/prompt.txt: 52d362e58c336e43e125e462852c22cb0d562a3c7458633e4028f2b218d026c0
        A/clauses/window-02/meta.json: 04240bbf397f7142713948cc9e8afe063d0ad90db3177a096f8cf7e56f1039e4
        A/clauses/window-01/raw.json: cda12e7cd73e7596ab58426c9072fdf8832f4fff85904e085a5d3898a8c5e7d6
        A/clauses/window-01/prompt.txt: 47749135cd8f6cea08b0aa32a62069e61ff7b38db9d1dfea809bb3ed4e27dffc
        A/clauses/window-01/meta.json: 1fd3121717e181070733839f2a7880b84b1dbea0662a02d7951a50484dbc6cf0
        A/clauses/window-06/raw.json: 90073fd957b12e082a557c34ff339196350c2097de5d0d9d71dc14496d090403
        A/clauses/window-06/prompt.txt: a3abd0e8e9eaad2ce3faad9927542ba1653d5b34096e1778281eff6b49bdabd0
        A/clauses/window-06/meta.json: f2a66d356152460a1421894f79957a374bf34ca236540632713c6cc90da2f79d
        A/tables/TABLE-3-page-8-4/raw.json: 7d2a1b2f01d91552de57ee7c69dc70319b3520185c614e790b0224ba8fa85f8d
        A/tables/TABLE-3-page-8-4/prompt.txt: 575ab256867eeb682f1eb49ac2acd14aeec785ad7dc88bf37c0cd4bd776ce20d
        A/tables/TABLE-3-page-8-4/meta.json: bd4de38a781364643aa1a30753a47cba6fa2eabaa67999c0cdb92de35138ebee
        A/tables/TABLE-2-page-6-2/raw.json: 44c3c37040dce500d19663294f151979d2b6cb6546beb81efb6441235f39e42c
        A/tables/TABLE-2-page-6-2/prompt.txt: ee5c99c11d10521e45f40ec0528b9324788f0157a60676ef13a3f045c88506a5
        A/tables/TABLE-2-page-6-2/meta.json: 81fa4dcb12f2e5050516024212f7f6ab78230018c2df7ebcdf3128ff9de20516
        A/tables/TABLE-3-page-7-3/raw.json: 1c9b4cea569fe000a10b7435a52ffadc0349ef9b4f8fab95ed123f65b88c5a1f
        A/tables/TABLE-3-page-7-3/prompt.txt: d2cc7c5d8ca14b60462e3acf2541d783834b32b0de4deda49acaeb0b3977fee7
        A/tables/TABLE-3-page-7-3/meta.json: e1a1a3aa168c63b21227faac0c00f30914c9ce8a1705110c75cd202257860bf0
        A/tables/TABLE-1-page-4-1/raw.json: f912750d5d8d90f368ff3d8d5ee0010a46b1060dc3200b291399a9f614db3428
        A/tables/TABLE-1-page-4-1/prompt.txt: c264e0df9c71f486ab7c61b7fcfe23b05d9e73345fc58b68d6e06fb452a7e6cf
        A/tables/TABLE-1-page-4-1/meta.json: cc4ff81811251b106474694aa5dd7e5ddcd2ca59f8353db6debe7dbf44652451
        B/passages.json: fb05d255fb5b510c3cb6bcf39d523ddec772f709aa93e6bd8ef11f50c41b2db3
        B/raw.json: 19c8395757703f0482b6f435393b6d0557ddc12c5b0477aacb16a0612f67d67f
        B/source-units.json: 35f9d7d086e0259d79885d8db4b4a6c361257307b80a752aa6b0e3dc1502d9d7
        B/full-source-units.json: cd24483d7d8e514c02cdcfbab33ad24819f2e8e8780341a52776172b36e7298b
        B/meta.json: f243a5d711d26933bbb3b8ca101fc2610dba3a6c71432ac0479abb0fa7c16eff
        B/table-images/page-6.png: 7830868b3bfd0f860e5d0afb8be573b41c91b8928aa150af37844c8b7c6bf2fe
        B/table-images/TABLE-3-page-8-1.png: df53998b2df560a11c297588cfc714442790cf7e3dc68c340caa8ce82ea086da
        B/table-images/page-7.png: 52593c0bd54dfb37072f3d2f85e1b7c1596d71212a1f6eba928114b5af610fff
        B/table-images/page-4.png: 3182121ef6a297b01ee17862ac2c26673ab2c5c345bd2599520a9101f371bf5d
        B/table-images/TABLE-1-page-4-1.png: 4b9af9d6b48b258184e8a48cf16660c16b440c6d39c25464fe6924ad1a32fcac
        B/table-images/page-8.png: 483f07f6213b76b1a8b87ff508d0d65a5c52c302682cab8f7ee6ed9f811bea6a
        B/table-images/TABLE-2-page-6-1.png: afad483f1432e62ad17f9509f12e27c11c449cbeff66d34429f1aff7bb821a9f
        B/table-images/manifest.json: 56ba7c3f17f00226c2cd4b17aeb3250cb198c840402874a527c147f6a21f5b88
        B/table-images/TABLE-3-page-7-1.png: c5d63af8411691fccdc9d44dac78fe3efa1e4e81638a2db16bb41b283f64b3ce
        B/clauses/window-03/raw.json: 538004f70f00ed3c83416c86c67cac9aac54e16e71aa3612b43a595c2693ad50
        B/clauses/window-03/prompt.txt: 7eb2fcf3461a92fe259bcf80d8cb4da9fd5d5e4a021cb99b787d1a93ead27348
        B/clauses/window-03/meta.json: 84b85dc2a5dfae7e1ca6861b955e510263ebcc357244f7168c7c265bbe084a35
        B/clauses/window-04/raw.json: acb95499052e29ba61ef0ea3f1af64f9127a8dd11671e490fff6f13a4655592c
        B/clauses/window-04/prompt.txt: beaa0fabdb847bb884e5170b73840e1baa50a2d5c792a7aa5ee77235dde6ec41
        B/clauses/window-04/meta.json: 0235d2a18f80e77df09dc60fba2f3f9d104df174e903f1ee59bb0c538e9e84d1
        B/clauses/window-05/raw.json: 63a8c66df8cd43a972dea8259bc8b26ce305e2772ab11608774e3c72393f0798
        B/clauses/window-05/prompt.txt: b85c8f5046f17132493b03511938c68f0e81bc522e3d54feef1d50198a73f66e
        B/clauses/window-05/meta.json: 753cb3a6ed9f001afed15c01c3e463125aa8b12fdbb946892f7e39f63e8b98c1
        B/clauses/window-02/raw.json: 545fdb1f96b3bc04eba5207e0f5aa25c4b401d5745c9e456c649399915af908b
        B/clauses/window-02/prompt.txt: 52d362e58c336e43e125e462852c22cb0d562a3c7458633e4028f2b218d026c0
        B/clauses/window-02/meta.json: 322e70febe9a7d55767adf5b40989874163e6f77870eebfe2e320981b5d6c4a3
        B/clauses/window-01/raw.json: 808d217db7d268a2aaa937e9c3e120a1da2296d811b1fccee0058ef35777a9cc
        B/clauses/window-01/prompt.txt: 47749135cd8f6cea08b0aa32a62069e61ff7b38db9d1dfea809bb3ed4e27dffc
        B/clauses/window-01/meta.json: 1c24c55cbe0c1cc1557b1c55ebbd9b504eae6dfb3162675039f1023ee86d5e77
        B/clauses/window-06/raw.json: 2f8273585eb03168e265af925579c072c9476bdaa13577ad52e3bd86a1fe394f
        B/clauses/window-06/prompt.txt: a3abd0e8e9eaad2ce3faad9927542ba1653d5b34096e1778281eff6b49bdabd0
        B/clauses/window-06/meta.json: 3425b3db0c937a9267c4d6f15ebb8e126a1988bacca855d8a0d79ee600d2297e
        B/tables/TABLE-3-page-8-4/raw.json: 5c04820f8a2090300a6d7f977837db63d6a94e5bb504a1b777e1d9b1d0891ba9
        B/tables/TABLE-3-page-8-4/prompt.txt: 575ab256867eeb682f1eb49ac2acd14aeec785ad7dc88bf37c0cd4bd776ce20d
        B/tables/TABLE-3-page-8-4/meta.json: 9a15d65e7b0d80863c1157ae29d879fac8e5f2ddf32da0149fc575d07cdb9704
        B/tables/TABLE-2-page-6-2/raw.json: 51ff5c38daec5f307a57098fff7ab5d9c781af79deebdd92b8177dc0c7494cd5
        B/tables/TABLE-2-page-6-2/prompt.txt: ee5c99c11d10521e45f40ec0528b9324788f0157a60676ef13a3f045c88506a5
        B/tables/TABLE-2-page-6-2/meta.json: 3d6db70e030a421f66307fd767f1a24c733832f15590efbe01f44fb09806cf03
        B/tables/TABLE-3-page-7-3/raw.json: 85cebf0ac3d0ba52af2a32d78a42f76e5ad8762a0c3e62cd115d9b40eadb8e75
        B/tables/TABLE-3-page-7-3/prompt.txt: d2cc7c5d8ca14b60462e3acf2541d783834b32b0de4deda49acaeb0b3977fee7
        B/tables/TABLE-3-page-7-3/meta.json: b03aaa2c2adc0b22c026efeb466e25db5ae2f47186ac29a387ffe3d7e396ce72
        B/tables/TABLE-1-page-4-1/raw.json: 8815755c3511616ca678fa71340917a795c078b538d3ee282dafaf9393aeff80
        B/tables/TABLE-1-page-4-1/prompt.txt: c264e0df9c71f486ab7c61b7fcfe23b05d9e73345fc58b68d6e06fb452a7e6cf
        B/tables/TABLE-1-page-4-1/meta.json: bae33e9d21883a526400a17b10b7a397662222ec37f6d3915fcc3569350967b2
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
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2019
      source_status_sha256: 504f9e1813e76e2933b0280983c1643f67d3a4183483b109d68f16d75dee0787
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: initial AQ
    outcome:
      text: AQ change
    analysis_label: Aphasia Severity Change Prediction
    relation: association
    evidence_ids:
    - P7-S1-C4
    - P7-S1-C5
    qualifier_ids:
    - P8-S1-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2019
      source_status_sha256: 504f9e1813e76e2933b0280983c1643f67d3a4183483b109d68f16d75dee0787
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S2-C4
      - Result passage disposed without unit P6-S1-C2
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C7
      - Accounting without a linked unit P7-S1-C1
      - Accounting without a linked unit P7-S1-C3
      - Unaccounted source passage P7-S1-C3
      - Unaccounted source passage P6-S2-C4
      - Unaccounted source passage P7-S1-C1
      - Unaccounted source passage P6-S2-C7
      - Result passage disposed without unit P9-S1-C3
      - Unresolved source passage P10-S2-C8
      - Unresolved source passage P10-S3-C2
      unattached_null_or_qualifier_ids:
      - P9-S1-C3
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 133
      unselected_timing_passages:
      - P1-S2-C8
      - P2-S2-C8
      - P2-S3-C1
      - P2-S3-C3
      - P2-S3-C7
      - P3-S1-C5
      - P10-S1-C4
      - P10-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P10-S1-C1
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S1-C8
        - P10-S2-C2
        - P10-S2-C3
        - P10-S2-C4
        - P10-S2-C5
        - P10-S2-C6
        - P10-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      - TABLE-3-page-8-4
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P5-S1
        - P7-S1
        - P7-S2
        - P8-S1
        - P9-S1
        - P9-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2019
      source_status_sha256: 504f9e1813e76e2933b0280983c1643f67d3a4183483b109d68f16d75dee0787
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: States lesion volume and time poststroke best predicted initial aphasia
        severity.
    - source_id: P1-S2-C13
      disposition: represented
      result_indexes:
      - 2
      reason: States leukoaraiosis and initial severity predicted decline in language
        abilities.
    - source_id: P1-S2-C14
      disposition: represented
      result_indexes:
      - 5
      reason: States more severe leukoaraiosis associated with 4.3 odds increase of
        decline.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant reporting of exclusionary events.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater reliability for Fazekas scale.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes model inclusion of time poststroke.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes predictor variables for AQ change.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean Fazekas and lesion volume values.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no correlation between Fazekas and lesion volume.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlations between Fazekas and time poststroke, education,
        and age.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlations between Fazekas and age.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reports correlation between Fazekas and follow-up AQ when controlling
        for time.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports negative correlation between Fazekas total and AQ change.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports correlation between Fazekas and AQ change controlling for time
        poststroke.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Reports correlation between lesion volume and initial/follow-up AQ.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no correlation between lesion volume and AQ change.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 2.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports Durbin-Watson statistics.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports outlier and homoscedasticity analysis.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports VIF for collinearity.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies lesion volume and time poststroke as significant predictors
        of initial AQ.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between Fazekas and time poststroke.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Provides specific t-values and effects for lesion volume and time on
        initial AQ.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: States initial AQ and Fazekas scores predicted AQ change.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: States leukoaraiosis and higher initial AQ predicted decline in AQ.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Provides specific t-values and point changes for Fazekas and initial
        AQ on AQ change.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 3.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Reports binary logistic regression results for odds of decline based
        on Fazekas.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Confirms lesion volume/time as best predictors and leukoaraiosis as
        not significant for initial severity.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: States changes in aphasia were driven by initial severity and leukoaraiosis.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Provides specific effect of initial AQ on AQ change.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Provides specific effect of Fazekas score on AQ decline.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about long-term changes being possible.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses variance in AQ change.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual variability in response to leukoaraiosis.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports non-significant correlation between age and Fazekas severity.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: States age at evaluation was correlated with worsening aphasia.
    - source_id: P10-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no sex differences in improvement/decline in another study.
    unresolved_coverage:
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S1-C3
    - P3-S2-C4
    - P5-S1-C2
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C11
    - P6-S2-C1
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C7
    - P7-S1-C1
    - P7-S1-C7
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C8
    - P8-S2-C2
    - P8-S2-C3
    - P9-S1-C3
    - P10-S1-C8
    - P10-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    - TABLE-3-page-8-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C2
      recruited_sample:
      - P2-S3-C2
      eligibility:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P3-S1-C2
      imaging_provenance:
      - P3-S1-C9
      imaging_timing:
      - P2-S3-C6
      - P3-S1-C9
      outcome_timing:
      - P2-S2-C7
      - P2-S3-C6
      - P5-S1-C4
      - P6-S1-C1
      outcome_definition:
      - P7-S1-C10
      validation: []
      analysis_restrictions:
      - P7-S1-C9
      dependent_variable_statement:
      - P4-S2-C4
      - P5-S1-C1
      - P5-S1-C3
      - P5-S1-C4
      limitations: []
      personal_factors: []
      tested_personal_effects:
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P10-S2-C2
      adjustment_roles:
      - P4-S2-C1
      - P4-S2-C2
      - P5-S1-C2
      - P6-S1-C6
      - P6-S1-C8
      - P7-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      explicitly_not_adjusted:
      - P10-S1-C2
      - P10-S2-C7
      descriptive_personal_factors:
      - P2-S3-C1
      - P3-S1-C4
      - P4-S1-C2
      - P4-S2-C1
      - P6-S1-C2
      - P10-S1-C3
      - P10-S1-C7
      - P10-S2-C6
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P10-S1-C1
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S1-C8
      - P10-S2-C2
      - P10-S2-C3
      - P10-S2-C4
      - P10-S2-C5
      - P10-S2-C6
      - P10-S2-C7
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
      pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
      review_sha256: 792ae8a84920eeb61cc2d6ccf27dca72b3766c3f8f0c80825b514787b1794a28
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
      - P7-S1-C4
      - P7-S1-C5
      source_result: In a regression model predicting change in Aphasia Quotient (AQ)
        from initial to follow-up, higher initial leukoaraiosis severity (Fazekas
        score) was significantly associated with greater decline in AQ (negative coefficient),
        while higher initial AQ was associated with less decline (negative coefficient).
        The model included initial AQ, stroke age, and time post-stroke at follow-up
        as covariates.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: 'The selected analysis corresponds to the second line of inquiry
            described in the source: predicting AQ change using leukoaraiosis severity
            and lesion volume, with initial AQ, stroke age, and time post-stroke at
            follow-up as covariates. The source explicitly states that initial AQ
            and total Fazekas scores predicted AQ change (P7-S1-C3, P7-S1-C4, P7-S1-C5).'
          source_ids:
          - P7-S1-C3
          - P7-S1-C4
          - P7-S1-C5
          - P6-S1-C1
        direction:
          answer: fits
          reason: The source states that 'More severe leukoaraiosis at initial evaluation
            predicted decline in AQ at follow-up' (P7-S1-C4) and 'for every 1-point
            increase in Fazekas score, AQ decreased by 2.6 points' (P7-S1-C5). The
            proposed claim 'More severe leukoaraiosis... predicted decline' preserves
            the detected negative association (higher leukoaraiosis -> lower AQ change
            -> decline).
          source_ids:
          - P7-S1-C4
          - P7-S1-C5
        construct:
          answer: fits
          reason: The exposure is leukoaraiosis severity measured by the Fazekas scale
            on T2-weighted MRI (P3-S1-C13, P3-S2-C2). The outcome is AQ change (P5-S1-C3,
            P6-S1-C1). The patient measurement is non_imaging (behavioral/clinical
            rating of white matter hyperintensities), not diffusion or template overlap.
            The proposed definition correctly identifies the Fazekas scale and T2-weighted
            MRI.
          source_ids:
          - P3-S1-C13
          - P3-S2-C2
          - P5-S1-C3
          - P6-S1-C1
        qualifications:
          answer: fits
          reason: The proposed qualifications correctly note that initial AQ also
            predicted decline and that the model included initial AQ, stroke age,
            and time post-stroke at follow-up. This aligns with P6-S1-C1 and P7-S1-C5.
            The source also notes that lesion volume was in the model but not significant
            for this outcome (implied by P7-S1-C3 focusing on initial AQ and Fazekas),
            but the core relationship is correctly qualified.
          source_ids:
          - P6-S1-C1
          - P7-S1-C5
          - P8-S1-C6
        missing_material_caveat:
          answer: fits
          reason: 'The proposed draft includes key limitations: small sample size,
            retrospective design, inability to control for vascular risk factors (diabetes,
            etc.), and male-dominated sample. These are explicitly stated in P10-S1-C1,
            P10-S1-C2, and P10-S2-C6. No material caveat changing the interpretation
            of the association is omitted.'
          source_ids:
          - P10-S1-C1
          - P10-S1-C2
          - P10-S2-C6
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: Individuals in the chronic stage of recovery (>=6 months poststroke)
        after a single-event left-hemisphere middle cerebral artery stroke with aphasia
        (initial WAB AQ < 93.8).
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 93.8'
    analysis_identity:
      id: R005
      exposure:
        text: initial AQ
      outcome:
        text: AQ change
      analysis_label: Aphasia Severity Change Prediction
      relation: association
      evidence_ids:
      - P7-S1-C4
      - P7-S1-C5
      qualifier_ids:
      - P8-S1-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
        source_review: _compare/relationships-2026-11-16/review-current/Basilakos2019
        source_status_sha256: 504f9e1813e76e2933b0280983c1643f67d3a4183483b109d68f16d75dee0787
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ae7dc98a6c20dbf8db0350365ca26054857aac7964c0156bb17c9e6bf66735d2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C1
          page: 2
          text_layer_sha256: ae7dc98a6c20dbf8db0350365ca26054857aac7964c0156bb17c9e6bf66735d2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "This is a retrospective study including multi–time point \n\
          assessment of N = 35 participants (9 females; age at stroke: \nM = 55.5\
          \ ± 10 years, range = 31-71 years) in the chronic \nstage of recovery after\
          \ a single-event left hemisphere stroke \n(ie, ≥6 months poststroke; at\
          \ initial MRI assessment, M = \n36.4 ± 40.8 months poststroke, range = 6-202\
          \ months)."
        anchor_text: "This is a retrospective study including multi–time point \n\
          assessment of N = 35 participants (9 females; age at stroke: \nM = 55.5\
          \ ± 10 years, range = 31-71 years) in the chronic \nstage of recovery after\
          \ a single-event left hemisphere stroke \n(ie, ≥6 months poststroke; at\
          \ initial MRI assessment, M = \n36.4 ± 40.8 months poststroke, range = 6-202\
          \ months)."
        excluded_fragments: []
        image_sha256: 61a9ffb7a7cb7557469c1e5be8b21f799b8dae8f5c8a7cfa02fe4094d75d854c
        transcription: 'This is a retrospective study including multi–time point assessment
          of N = 35 participants (9 females; age at stroke: M = 55.5 ± 10 years, range
          = 31-71 years) in the chronic stage of recovery after a single-event left
          hemisphere stroke (ie, ≥6 months poststroke; at initial MRI assessment,
          M = 36.4 ± 40.8 months poststroke, range = 6-202 months)'
      P2-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 600d870146827cbe4a68828b6cf4c13dd9e60c87c40f2cc4b19806bd52a7e6b1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C3
          page: 2
          text_layer_sha256: 600d870146827cbe4a68828b6cf4c13dd9e60c87c40f2cc4b19806bd52a7e6b1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Inclusion criteria for these studies were as follows: \nbetween\
          \ the ages of 21 and 85 years, premorbidly right-\nhanded individuals in\
          \ the chronic (≥6 months poststroke) \nstage of recovery following a single-event\
          \ left hemisphere \nstroke, presence of aphasia (as indicated by a Western\
          \ \nAphasia Battery24,25 (WAB) Aphasia Quotient (AQ) <93.8), \nand able\
          \ to undergo neuroimaging on a 3T MRI scanner."
        anchor_text: "Inclusion criteria for these studies were as follows: \nbetween\
          \ the ages of 21 and 85 years, premorbidly right-\nhanded individuals in\
          \ the chronic (≥6 months poststroke) \nstage of recovery following a single-event\
          \ left hemisphere \nstroke, presence of aphasia (as indicated by a Western\
          \ \nAphasia Battery24,25 (WAB) Aphasia Quotient (AQ) <93.8), \nand able\
          \ to undergo neuroimaging on a 3T MRI scanner."
        excluded_fragments: []
        image_sha256: dfd7cf5f45a2be12b0a571539185f53c2daed8d92c130b986ceaceb7f4a52112
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 93427f503ad6e0356e6d2b8088af32d7995ce85551a1c960f3ebaf132fba6acc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 93427f503ad6e0356e6d2b8088af32d7995ce85551a1c960f3ebaf132fba6acc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The mean test-retest interval for all participants was 34.8\
          \ ± \n26.2 months (range = 6-87 months)."
        anchor_text: "The mean test-retest interval for all participants was 34.8\
          \ ± \n26.2 months (range = 6-87 months)."
        excluded_fragments: []
        image_sha256: cf1781d126793d3e7dc2ff16975adb6013e9019780e02f40c1cff474a910e686
        transcription: The mean test-retest interval for all participants was 34.8
          ± 26.2 months (range = 6-87 months)
      P10-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7c9edea727724d391deaecf85e7a46cc20e0918fea45d011718cae9b44eb1694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fb88db55774d3b6bb769b4f361aa62cec32eb5a2b0db5126a9b89d7ce7862106
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S2-C6
          page: 10
          text_layer_sha256: fb88db55774d3b6bb769b4f361aa62cec32eb5a2b0db5126a9b89d7ce7862106
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Third, it should also be noted that the male dominated \n\
          sample in this study (ie, approximately a 3:1 ratio of \nmales:females)\
          \ is not representative of the fact that when \ncontrolling for age, rates\
          \ of poststroke aphasia are similar \nbetween males and females.56 However,\
          \ sex differences \nin leukoaraiosis have been reported, where women have\
          \ \nbeen shown to demonstrate more severe leukoaraiosis,57,58 \nand that\
          \ WMH tend to progress more rapidly in deep \nwhite matter regions.59 However,\
          \ sex differences in leu-\nkoaraiosis are not a unanimous finding.60 Given\
          \ these \nreported sex differences in leukoaraiosis and its progres-\nsion,\
          \ further study with a larger sample size should indeed \nexplore the role\
          \ of sex on leukoaraiosis in poststroke \naphasia, and whether this gives\
          \ rise to a sex difference in \nrates of decline."
        anchor_text: "Third, it should also be noted that the male dominated \nsample\
          \ in this study (ie, approximately a 3:1 ratio of \nmales:females) is not\
          \ representative of the fact that when \ncontrolling for age, rates of poststroke\
          \ aphasia are similar \nbetween males and females.56 However, sex differences\
          \ \nin leukoaraiosis have been reported, where women have \nbeen shown to\
          \ demonstrate more severe leukoaraiosis,57,58 \nand that WMH tend to progress\
          \ more rapidly in deep \nwhite matter regions.59 However, sex differences\
          \ in leu-\nkoaraiosis are not a unanimous finding.60 Given these \nreported\
          \ sex differences in leukoaraiosis and its progres-\nsion, further study\
          \ with a larger sample size should indeed \nexplore the role of sex on leukoaraiosis\
          \ in poststroke \naphasia, and whether this gives rise to a sex difference\
          \ in \nrates of decline."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "More severe leukoaraiosis at initial evaluation \npredicted decline in AQ\
    \ at follow-up, as did higher initial \nAQ scores."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
