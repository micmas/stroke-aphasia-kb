---
id: left_extreme_capsule_fibre_region
name: Left extreme-capsule fibre region
kind: tract
findings:
- id: f1
  target: aphasia_presence
  target_kind: impairment
  claim: 'The higher ECF overlap category (>=15% in Table3; >15% in prose) was associated
    with greater odds of concurrent aphasia versus no ECF overlap: adjusted OR 16.37
    (95%CI 3.11–86.16). This is the maximum damaged slice area of a tract template,
    not loss of 15% of all tract fibres. The region may include overlapping ECF, IFOF
    and uncinate fibres. The <15% category was not associated (OR 0.72, CI 0.07–7.08,
    p=.78); no ECF×AF interaction was detected (p=.71).'
  direction: likely
  relationship: correlational
  method: LSM
  design: cross-sectional
  sample:
    n: 123
    population: First embolic left-hemisphere ischaemic stroke; German native speakers
      under 90; no lesion in four selected Stanford cortical language ROIs
    phase: acute
    time_post_onset: Testing 0–10 days; mean 3.93 SD 2.28 days
    cohort: Freiburg large-scale prospective stroke project, selected 2011–2018 cohort
    subgroup: 18 with aphasia, 105 without; not an aphasia-only sample
  statistics:
    effect_size: Adjusted OR 16.37 [3.11,86.16], p<.01;9/14 cases versus 8/93 with
      no ECF lesion
    threshold: Two-sided Wald tests; adjusted logistic regression. Multiplicity correction
      not reported.
  confounders_controlled:
  - AF lesion category
  - Age dichotomised at 70
  - Sex/gender as reported
  - Continuous stroke volume in ml
  confounders_not_controlled:
  - Lesions outside the four Stanford language ROIs may affect other language-related
    regions
  region_definition:
    kind: tract
    description: Study-specific tract template and slice-area overlap; not an entire
      atlas parcel
  imaging: DTI
  imaging_details:
    reference_space: not_reported
    atlases_used:
    - Stanford functional language ROIs for selection
    - Global-tractography-derived ECF and AF templates
    measure: Maximum lesion overlap percentage across slices perpendicular to mid-bundle
      orientation; stroke volume from diffusion-weighted MRI
  lesion_mapping:
    analysis: region_based
    n_analysed: 123
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: not_reported
  outcome_timing:
    type: status_at_assessment
    interval: Binary Token-Test-defined aphasia within 10 days; not prospective recovery
  author_limitations:
  - Only 18 aphasia cases and wide confidence intervals
  - External validity requires further studies
  - Stanford atlas does not cover all language-relevant cortex
  - Token Test emphasises comprehension and attention rather than overt speech production
  evidence_quality: cohort
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping after dual extraction and local review)
    extracted_on: '2026-11-17'
    paper_section: Main PDF Methods, Results, Table3
    confidence: medium
    flags:
    - human_approval_pending
    - selected_cortical_sparing_cohort
    - threshold_discrepancy
    - no_external_prediction_validation
  notes: These odds ratios describe concurrent aphasia in a selected acute-stroke
    cohort. They do not establish individual prognosis or a clinical lesion threshold.
    Table3 uses >=15% and Methods uses >=7 Token Test errors; Results prose uses >15%
    and >7. Boundaries remain flagged.
  citation: '@Oeckel2021'
  source_passages:
  - section: Source passage P8-S1-C6
    page: 8
    quote: 'The multivariate logistic regression

      analysis showed that stroke patients with >15% ECF le-

      sion were at greater odds to be affected with aphasia

      than those without ECF lesions (OR ¼ 16.37, 95% confi-

      dence

      interval:

      3.11–86.16,

      P < 0.01).'
    supports: claim
  - section: Source passage P5-S2-C6
    page: 5
    quote: 'We used multivari-

      ate logistic regression to estimate the odds ratio (OR) of

      aphasia, associated with ECF lesions compared with no

      ECF lesions, adjusting for AF lesions, stroke volume as a

      continuous variable, age (dichotomous with cut-off at

      70 years) and gender.'
    supports: claim
  - section: Source passage P3-S2-C2
    page: 3
    quote: 'The inclusion criteria were (i) embolic

      first-time stroke of the left middle cerebral artery-terri-

      tory, (ii) age < 90 years and (iii) German native speaker.'
    supports: sample
  - section: Source passage P3-S2-C6
    page: 3
    quote: 'To further restrict the 282 patients to those with

      infarct areas outside the cortical language-zones, overlaps

      between stroke lesion and the four left-hemispheric func-

      tional

      ROIs

      of

      the

      Stanford

      atlas

      language

      network

      (Fig. 1) were calculated and all patients with lesions

      (>0%) in at least one of the four ROIs were excluded

      (n ¼ 150).'
    supports: sample
  - section: Source passage P3-S2-C7
    page: 3
    quote: The study outcome was aphasia as a binary variable.
    supports: method
  - section: Source passage P3-S2-C8
    page: 3
    quote: 'The Token Test was found to discriminate particularly

      well between patients with aphasia and normal con-

      trols,31 normal hospitalized adults,32 non-aphasic right-

      hemisphere-damaged adults33,34 and non-aphasic diffuse-

      and focal-brain-damaged adults.35 To assess aphasic defi-

      cits in our cohort, all patients completed the Token Test

      of the AAT.26 Aphasia was diagnosed for patients with

      deficits

      of

      at

      least

      seven

      age-corrected

      error

      scores

      according to the allocation of the AAT.'
    supports: method
  - section: Source passage P3-S2-C10
    page: 3
    quote: 'These patients were allo-

      cated to the non-aphasia group as they scored <7 error

      points in the Token Test; however, they scored <78 of

      90 points in the AAT subtests for reading and writing.'
    supports: sample
  - section: Source passage P3-S2-C11
    page: 3
    quote: 'We decided to exclude these nine patients from the study

      to ensure unharmed language function in the non-aphasia

      group.'
    supports: sample
  - section: Source passage P5-S1-C9
    page: 5
    quote: 'For each slice of these ROIs, we calculated the

      percentage of overlap between the fibre bundle area in that

      slice and the lesion of each patient.'
    supports: method
  - section: Source passage P5-S1-C10
    page: 5
    quote: 'Assuming that associ-

      ation fibres are discontinued as soon as the lesion overlaps

      with at least one slice of an ROI, we computed the max-

      imum percentage of overlap across the slices of ECF and

      AF ROIs for each patient.'
    supports: method
  - section: Source passage P5-S2-C6
    page: 5
    quote: 'We used multivari-

      ate logistic regression to estimate the odds ratio (OR) of

      aphasia, associated with ECF lesions compared with no

      ECF lesions, adjusting for AF lesions, stroke volume as a

      continuous variable, age (dichotomous with cut-off at

      70 years) and gender.'
    supports: confounders
  - section: Source passage P5-S2-C8
    page: 5
    quote: 'Results

      The study cohort consisted of 123 patients with acute

      left-hemispheric ischaemic infarcts without lesions in the

      functional ROIs of the language network.'
    supports: sample
  - section: Source passage P7-S1-C1
    page: 7
    quote: '

      time stroke (mean 3.93 6 2.28 days, range 0–10 days).'
    supports: sample
  - section: Source passage P7-S1-C6
    page: 7
    quote: "The mean stroke\nvolume was 6.9 6 8.0 ml, 6.0 6 7.4 ml in those without\n\
      Table 3 Predictors of aphasia in 123 patients with left-hemispheric stroke\n\
      With aphasia,\nn (%)\nWithout aphasia,\nn (%)\nCrude OR\n(0.95-CI)\nAdjusted\
      \ ORa\n(0.95-CI)\nP-Valueb\nTotal\n18 (100.0)\n105 (100.0)\nECF lesionc\nNone\n\
      8 (44.44)\n85 (80.95)\n1\n1\n–\n<15%\n1 (5.56)\n15 (14.29)\n0.71 (0.08–6.08)\n\
      0.72 (0.07–7.08)\n0.78\n\x0415%\n9 (50.00)\n5 (4.76)\n19.12 (5.15–71.00)\n16.37\
      \ (3.11–86.16)\n<0.01\n\x0415% < 30%\n4 (22.22)\n2 (1.90)\n21.25 (3.36–134.56)\n\
      18.31 (1.86–180.77)\n0.01\n>30%\n5 (27.78)\n3 (2.86)\n17.71 (3.56–88.10)\n15.32\
      \ (2.31–101.57)\n<0.01\nAF lesionc\none\n12 (66.67)\n65 (61.90)\n1\n1\n–\n15%\n\
      3 (16.67)\n20 (19.05)\n0.81 (0.21–3.17)\n0.33 (0.05–2.25)\n0.26\n\x0415%\n3\
      \ (16.67)\n20 (19.05)\n0.81 (0.21–3.17)\n0.30 (0.04–2.35)\n0.25\nOther factors\n\
      Female gender\n6 (33.33)\n39 (37.14)\n0.85 (0.29–2.43)\n0.70 (0.19–2.56)\n0.59\n\
      Age \x0470 years\n13 (72.22)\n43 (40.95)\n3.75 (1.25–11.29)\n3.97 (1.02–15.46)\n\
      0.05\nStroke volume (ml)d\n11.68\n6.04\n1.07 (1.01–1.12)\n1.06 (0.98–1.14)\n\
      0.13\nCI: conﬁdence interval; OR: odds ratio.\naAdjusted for ECF lesion, AF\
      \ lesion, gender, age and stroke volume.\nbTwo-sided Wald-test derived from\
      \ logistic regression.\ncLesions dichotomized according to their median split.\n\
      dMean volume in ml presented instead of n (%) and used as continuous variable\
      \ in the logistic regression models."
    supports: statistics
  - section: Source passage P8-S1-C2
    page: 8
    quote: 'Aphasia

      occurred in 14.6% (18 of 123 patients) (Table 1).'
    supports: sample
  - section: Source passage P8-S3-C4
    page: 8
    quote: 'The external valid-

      ity of this strong association has to be proven in further

      studies.'
    supports: limitation
  - section: Source passage P8-S3-C7
    page: 8
    quote: 'The Stanford atlas does not include all brain regions po-

      tentially involved in language processing.'
    supports: limitation
  - section: Source passage P8-S3-C8
    page: 8
    quote: "Consequently, we\ndid not examine and can therefore not exclude that patients\n\
      with \x0415% affection of the extreme capsule cluster have\nlesions of other\
      \ regions that contribute to aphasia."
    supports: limitation
  - section: Source passage P9-S1-C2
    page: 9
    quote: 'The Token Test examines language com-

      prehension in addition to attention and other cognitive

      functions, not however overt language production.64 The

      Token Test may thus be especially suited to test ‘ventral’

      '
    supports: limitation
  - section: Source passage P8-S2-C5
    page: 8
    quote: 'There is an on-

      going

      discussion

      about

      the

      correct

      naming

      of

      the

      language-related ventral tracts running through the ex-

      treme capsule, consisting of uncinate fascicle, inferior

      frontal-occipital fascicle and ECF.14,41 We took great care

      to separate the ECF but are well aware that the three

      tracts anatomically overlap within the extreme capsule,42

      and thus may be not really differentiable conceptually.'
    supports: claim
  - section: Source passage P8-S2-C6
    page: 8
    quote: 'Thus, we studied the bulk of fibres running through the

      extreme capsule and each of the tracts may be associated

      with aphasia, not that lesions of either ECF, inferior

      frontal-occipital fascicle or uncinate fascicle are mainly

      responsible.'
    supports: claim
  - section: Source passage P8-S2-C8
    page: 8
    quote: 'In the absence of an established param-

      eter for defining ECF lesion cut-off, we arbitrarily set it

      at 15% using the median split.'
    supports: claim
  - section: Source passage P8-S1-C9
    page: 8
    quote: 'There was no interaction be-

      tween ECF and AF lesions (P ¼ 0.71).'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-17'
relationship_review:
  paper: Oeckel2021
  proposal_id: U006
  review_status_sha256: e962120d69715a0ab035dbd15b292b7425053d5972a9ad35530a2842640c3c0f
  review_binding:
    version: relationship-review-v5
    input_hashes:
      pdf: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
      A/passages.json: 98a0dd62439e67dd17651b68d9b3b8d4c8019340226a70c501f9e9b95d63df9b
      A/raw.json: bc00e8fd7bc55a6fd1667e12dc098fc67d644116344cf9cd8dfd5bb5d42a651a
      A/source-units.json: da8df2b6522ecc2653e879d21bffc8e79c7382deefdf99c815473313ebbfef88
      A/full-source-units.json: 1c36c2b449a4a34be91732632952d46ffd9a362de2356ed2b83a85298ad05653
      A/meta.json: f682fd601bdb2ed394553e838a0272b57edf50fea69a6cf8e79187a8a8a82fa2
      A/table-images/TABLE-1-page-6-1.png: 0fccdc779d75a0a12d6c5e29b9b25ca8ccad012e531af42a6a53fca15d4468ca
      A/table-images/page-6.png: 2bc4e973c062e464c8ca9722105d7c6a142b09696febabecd3af99e8480b9c3f
      A/table-images/page-7.png: 5f967699aa5cf7b899378be2414da2cf82e8e9f3681b5ac832063df6fe7bdb2d
      A/table-images/manifest.json: 67523da4d010c6fb88b0c40b32af1ab9d009996083b81dd03ef70569872de400
      A/table-images/TABLE-2-page-6-2.png: 7c6006e02512fa45f62fc1b40d6055f904280a9f1fdf2d2c94347109b80b83a7
      A/table-images/TABLE-3-page-7-1.png: 938bb44b6178918eb664b2b5cffcbaf7f23fd55fca04c6ca993985a826ddd452
      A/clauses/window-03/raw.json: c93fee4a477e9019fb71c3234663be9dea9cc05c9c0117b3e8237eba7687a41a
      A/clauses/window-03/prompt.txt: ee36d78bc10edb3726a2a7d77d16447b64e236212522b824c3ec36a52549fae9
      A/clauses/window-03/meta.json: eec2770de8b95e7cc9cc25c1f2aa543dbd3a6d30cdd3fc4a5346f815d91edff2
      A/clauses/window-04/raw.json: 0ace9af37d34fdccc670708f5df4cb3f443543854c10379b7bba63e4539a14cf
      A/clauses/window-04/prompt.txt: 61e141a125386b4228eda533cd8239488c8c22d4c32977d9034b77c1ffdfb947
      A/clauses/window-04/meta.json: 480a37dd972fbfcdd03f3ff8244bc8e850ed0b3f8dce27b0120c0abdbc6245ed
      A/clauses/window-05/raw.json: 94c9cb32b2d0e1e4bad7e5e1a606cb704edf8ce7635740da9d707fc65202b69b
      A/clauses/window-05/prompt.txt: 589d4b88e6bd66e7684e656d3031a7c11d8091090295dfb3579351959db11cb0
      A/clauses/window-05/meta.json: 9b5d1be5e0d536f8ebac520c926deb389ec0ef681e3828b77cb6bfd2c57f1ec5
      A/clauses/window-02/raw.json: 0955627a83a2d8aee00600c4b935acc3ca38718c90123ed0a9d8c54b887151a7
      A/clauses/window-02/prompt.txt: 25be8a247985763b0588469832c407dd62350180405f83366a10ef2d91998dda
      A/clauses/window-02/meta.json: 9f2468b7eef0a656598ddf59c939043d9db957297c38b030489225b379464ba6
      A/clauses/window-01/raw.json: 4a6ccf498c03519fe85cf95c4cc4a22d49b9d73467281627bbd9d7755d0c5afe
      A/clauses/window-01/prompt.txt: aa187670107125f94b43d569708e91fe73c46a0d9b9ba1c0f776eb3a42a71125
      A/clauses/window-01/meta.json: 0b3ccced2d14e7487fba02aaa93b1e0baa893f8871d03bb728a9e073159a7e6f
      A/tables/TABLE-1-page-6-1/raw.json: e8e979f14f3ff4129dc9fb091c26cdf6ac9d43855006981210376aa04e3c1f7e
      A/tables/TABLE-1-page-6-1/prompt.txt: 40674e6e9a0b1aee6b2fdee07cc862e7b495b0fc149d87986d41675261bf1c16
      A/tables/TABLE-1-page-6-1/meta.json: 5440b775cbd8355abe89f798f7b8934239631d80b9fa9bbfe8c814016098af1e
      A/tables/TABLE-2-page-6-2/raw.json: a3a450872d6cd90d356fca6485c9153cc818f04e2fd2460818ccdffcd5f4143e
      A/tables/TABLE-2-page-6-2/prompt.txt: cd39e5d0194fa64b276a57665e72b295337aa2b1da8742a9ecb85fb1f29c6687
      A/tables/TABLE-2-page-6-2/meta.json: c6e6050b99eb5ae288ac4aeaaf9f8bf9565c5c8d2eb7813ee96dc7968e1d3256
      A/tables/TABLE-3-page-7-3/raw.json: b3e894714d445eae4dbbb1840659ddfc00e1d0a8ff9f41381c1eea85fececaaa
      A/tables/TABLE-3-page-7-3/prompt.txt: 77580ba5208221cda6408221bb003f6067853dbee9e5e39f78043de0ccefa507
      A/tables/TABLE-3-page-7-3/meta.json: 404c5c9dbea341eac162b0700a3274536d22e6de716472b523d81ccf528a4cb0
      B/passages.json: 98a0dd62439e67dd17651b68d9b3b8d4c8019340226a70c501f9e9b95d63df9b
      B/raw.json: e190dea628b1feab883bb5866bba088335ecbdd59d6102d82f5031af49c3ae8d
      B/source-units.json: da8df2b6522ecc2653e879d21bffc8e79c7382deefdf99c815473313ebbfef88
      B/full-source-units.json: 1c36c2b449a4a34be91732632952d46ffd9a362de2356ed2b83a85298ad05653
      B/meta.json: 052ac617616b26f357c76c99a43b5d68f540b7672fb7c16033490a7f12221d7b
      B/table-images/TABLE-1-page-6-1.png: 0fccdc779d75a0a12d6c5e29b9b25ca8ccad012e531af42a6a53fca15d4468ca
      B/table-images/page-6.png: 2bc4e973c062e464c8ca9722105d7c6a142b09696febabecd3af99e8480b9c3f
      B/table-images/page-7.png: 5f967699aa5cf7b899378be2414da2cf82e8e9f3681b5ac832063df6fe7bdb2d
      B/table-images/manifest.json: eea8d456f39556209d717179e2bc8deb650afb3a92cc3c09af29b0cb33d49fed
      B/table-images/TABLE-2-page-6-2.png: 7c6006e02512fa45f62fc1b40d6055f904280a9f1fdf2d2c94347109b80b83a7
      B/table-images/TABLE-3-page-7-1.png: 938bb44b6178918eb664b2b5cffcbaf7f23fd55fca04c6ca993985a826ddd452
      B/clauses/window-03/raw.json: 56ef04d32decd754e5e0a750e5900fff16d3624f9030ecf21435414ba841505b
      B/clauses/window-03/prompt.txt: ee36d78bc10edb3726a2a7d77d16447b64e236212522b824c3ec36a52549fae9
      B/clauses/window-03/meta.json: c600a443b650e67d23df9c1d233060e73de1efc9397ececa9dc35fd385372d23
      B/clauses/window-04/raw.json: 0f5422ee33434548c85ff80508b46a2089f20b793eb2bc3175d17654843e86c4
      B/clauses/window-04/prompt.txt: 61e141a125386b4228eda533cd8239488c8c22d4c32977d9034b77c1ffdfb947
      B/clauses/window-04/meta.json: 7bb639867d87771f843e26609e241e5b3e3e8a7ec77b1b672f52bc1beaec77fa
      B/clauses/window-05/raw.json: 16bfe5aca4bfe8ce6ec99e7595f6de758d10a7e81e50a251bb75d6631d055855
      B/clauses/window-05/prompt.txt: 589d4b88e6bd66e7684e656d3031a7c11d8091090295dfb3579351959db11cb0
      B/clauses/window-05/meta.json: 620196de33753bc1c4905ac827d1373021220c267dd1271f474a79e2ecb58ae4
      B/clauses/window-02/raw.json: 7f04a366270b0c1c8574a40d23c5fd400c039e42df0124afd92b18a7ae0437fa
      B/clauses/window-02/prompt.txt: 25be8a247985763b0588469832c407dd62350180405f83366a10ef2d91998dda
      B/clauses/window-02/meta.json: 67715306043d9c43625fe9614b417213e07d595a939d3c76d2a8c06ce28acaa7
      B/clauses/window-01/raw.json: 3677c09cf603d458ba1b8f810831ab3be5c5f2103551d39e2791fac6613497a1
      B/clauses/window-01/prompt.txt: aa187670107125f94b43d569708e91fe73c46a0d9b9ba1c0f776eb3a42a71125
      B/clauses/window-01/meta.json: 32bd95c79ddfad87dc70c5c988515cc947097b1201d9916831f950a3d170556f
      B/tables/TABLE-1-page-6-1/raw.json: 5533df29580c17d18bc92ebf3fcf4d07cc212fbfbe88f04c3ab92644b596ce82
      B/tables/TABLE-1-page-6-1/prompt.txt: 40674e6e9a0b1aee6b2fdee07cc862e7b495b0fc149d87986d41675261bf1c16
      B/tables/TABLE-1-page-6-1/meta.json: 786a1742f7a496124183eb2e7d6da1e1dff729b134950971823ffe54f71dd59b
      B/tables/TABLE-2-page-6-2/raw.json: 168374d5ebb4245d2dd3d46ffaaff3bc7f5108a7890d1e1a99b88c8cc1c85070
      B/tables/TABLE-2-page-6-2/prompt.txt: cd39e5d0194fa64b276a57665e72b295337aa2b1da8742a9ecb85fb1f29c6687
      B/tables/TABLE-2-page-6-2/meta.json: 8b9d180ac06e8153a8a499f75b646d74b1c7b1d8ef9c6731b9b2c1d08d1baa45
      B/tables/TABLE-3-page-7-3/raw.json: 61682513384c8a0a709af8001a280285f3271bcb3cb4264066091ffcda82b4f4
      B/tables/TABLE-3-page-7-3/prompt.txt: 77580ba5208221cda6408221bb003f6067853dbee9e5e39f78043de0ccefa507
      B/tables/TABLE-3-page-7-3/meta.json: 735ba3c736212d1cc5be3fabc598fefa65c0588b6d60d58081e6553ff8530152
    code:
      relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
      relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
      ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
      strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
    model: gemma4:26b
    model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
    host: http://localhost:11434
    max_output_tokens: 20000
  proposal:
    evidence_ids:
    - P8-S1-C6
    qualifier_ids:
    - P5-S2-C6
    context_ids:
    - P5-S2-C6
    - P3-S2-C7
    table_ids: []
    exposure:
      text: '>15% ECF lesion'
      source_id: P8-S1-C6
    outcome:
      text: aphasia
      source_id: P3-S2-C7
    relation: association
    effect_unit: individual
    result_status: reported_detected
    outcome_type: status_at_assessment
    direction: positive
    direction_source_id: P8-S1-C6
    origin: current_study
    label_match_candidates: {}
    id: U006
    flags:
    - overlapping_evidence_roles
    - source_display_check
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P1-S1-C3
    - P1-S1-C4
    - P2-S2-C5
    - P3-S1-C1
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C9
    - P3-S2-C6
    - P3-S2-C8
    - P5-S1-C10
    - P5-S1-C11
    - P5-S1-C13
    - P5-S1-C9
    - P5-S2-C9
    - P7-S1-C1
    - P8-S1-C11
    - P8-S1-C12
    - P8-S1-C17
    - P8-S1-C3
    - P8-S1-C5
    - P8-S2-C10
    - P8-S2-C7
    - P8-S3-C12
    - P8-S3-C2
    - P8-S3-C4
    - P8-S3-C5
    - P8-S3-C7
    - P8-S3-C8
    - P8-S3-C9
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: 69980fc808ff75b20638df2b8e60c42b6da694d91990414d7eb041024399ee08
  audit:
    coverage_issues:
    - Result passage disposed without unit P7-S1-C3
    - Result passage disposed without unit P7-S1-C4
    - Result passage disposed without unit P7-S1-C5
    - Result passage disposed without unit P7-S1-C6
    - Result passage disposed without unit P8-S1-C1
    - Result passage disposed without unit P8-S1-C2
    - Result passage disposed without unit P8-S1-C3
    - Result passage disposed without unit P8-S3-C11
    - Result passage disposed without unit P8-S3-C13
    unattached_null_or_qualifier_ids: []
    suppressed_nonrepresented_units: 7
    default_disposition_count_requires_completeness_check: 111
    unselected_timing_passages:
    - P1-S1-C3
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S2-C2
    - P3-S2-C4
    - P3-S2-C5
    - P5-S2-C8
    personal_effect_slots_without_result_classification: []
    held_frame_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C6
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
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C3
      - P3-S2-C4
      - P3-S2-C6
      - P5-S2-C8
      - P6-S1-C1
      - P7-S1-C4
      - P8-S1-C2
      - P8-S1-C10
      - P8-S3-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S1-C3
      - P2-S2-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C6
      - P5-S1-C13
      - P5-S2-C8
      - P8-S1-C12
      - P8-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C4
      - P3-S1-C1
      - P3-S3-C5
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P8-S1-C17
      - P8-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C4
      - P1-S1-C5
      - P1-S1-C6
      - P3-S2-C7
      - P3-S2-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C13
      - P7-S1-C2
      - P8-S1-C14
      - P8-S3-C9
      - P8-S3-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    empty_frame_slots_require_confirmation:
    - analysed_sample
    - eligibility
    - imaging_provenance
    - outcome_definition
    - validation
    - tested_personal_effects
    - explicitly_not_adjusted
    unclassified_extraction_ids: []
    table_review_required:
    - TABLE-1-page-6-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    unlinked_tables:
    - TABLE-1-page-6-1
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P3-S2
      - P3-S3
      - P4-S1
      - P5-S1
      - P5-S2
      - P7-S1
      - P8-S1
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C3
      - P3-S1-C7
      - P5-S2-C8
      - P6-S1-C1
      - P7-S1-C4
      - P8-S1-C2
      - P8-S1-C10
      - P8-S2-C10
      eligibility: []
      imaging_provenance: []
      imaging_timing:
      - P3-S1-C4
      - P8-S1-C3
      - P8-S2-C10
      outcome_timing:
      - P3-S1-C4
      - P5-S2-C9
      - P7-S1-C1
      - P8-S1-C3
      - P8-S2-C10
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P2-S2-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S2-C6
      - P8-S3-C8
      dependent_variable_statement:
      - P1-S1-C4
      - P3-S2-C7
      - P5-S1-C10
      - P5-S2-C6
      limitations:
      - P8-S3-C2
      - P8-S3-C4
      - P8-S3-C5
      - P8-S3-C7
      - P8-S3-C8
      personal_factors:
      - P5-S1-C11
      - P6-S1-C1
      - P7-S1-C3
      - P8-S1-C15
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C11
      - P5-S2-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C3
      - P3-S2-C2
      - P5-S1-C11
      - P6-S1-C1
      - P7-S1-C3
      - P8-S1-C15
      - P8-S3-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C6
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
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C3
      - P3-S2-C4
      - P3-S2-C6
      - P5-S2-C8
      - P6-S1-C1
      - P7-S1-C4
      - P8-S1-C2
      - P8-S1-C10
      - P8-S3-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S1-C3
      - P2-S2-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C6
      - P5-S1-C13
      - P5-S2-C8
      - P8-S1-C12
      - P8-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C4
      - P3-S1-C1
      - P3-S3-C5
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P8-S1-C17
      - P8-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C4
      - P1-S1-C5
      - P1-S1-C6
      - P3-S2-C7
      - P3-S2-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C13
      - P7-S1-C2
      - P8-S1-C14
      - P8-S3-C9
      - P8-S3-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-17'
    approved: false
    pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
    licence:
      category: cc
      label: CC BY 4.0
      url: http://creativecommons.org/licenses/by/4.0/
      version: published
      source: crossref
      doi: 10.1093/braincomms/fcab040
      checked: '2026-10-30'
      consulted:
      - crossref
      - unpaywall
      - pdf
    checked_pdf_pages:
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
    - 8
    - 9
    visual_pages:
    - 3
    - 5
    - 7
    scope: Main adjusted ECF/AF relationships and Table3 personal/volume factors;
      selected source checks, not all imaging acquisitions or individual-patient records.
    corrections:
    - 123 patients total,18 aphasia cases; acute outcome within 10 days, not later
      recovery.
    - Exclusion covers four Stanford language ROIs, not every cortical language region.
    - Exposure is maximum lesion/template slice-area overlap, not whole-tract percentage
      or a count of severed streamlines.
    - ECF region contains anatomically overlapping fibre systems; do not assign the
      effect uniquely to IFOF or uncinate.
    - Table3 uses >=15% whereas prose often says >15%; preserve threshold discrepancy.
    - Age>=70 adjusted OR 3.97 CI 1.02–15.46 p=.05 conflicts with Discussion stating
      no age association.
    - Token Test criterion is >=7 in Methods but >7 in Results; do not invent a resolved
      threshold.
    - Age, sex and lesion volume tested in Table3, not merely listed as covariates.
    remaining:
    - Named-person approval, including definition/mapping of binary aphasia_presence
      target.
    - Resolve age/threshold discrepancies if needed; AF labels in Table3 appear clipped.
    - Figure2 and individual-patient Table2 not visually adjudicated; no overall completeness
      claim.
    - Exact template registration space not established from main text.
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'The multivariate logistic regression

    analysis showed that stroke patients with >15% ECF le-

    sion were at greater odds to be affected with aphasia

    than those without ECF lesions (OR ¼ 16.37, 95% confi-

    dence

    interval:

    3.11–86.16,

    P < 0.01).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-17'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
