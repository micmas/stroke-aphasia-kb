---
id: baseline_clinical_demographic_predictors
name: baseline clinical and demographic predictors
kind: predictor
findings:
- id: f1
  target: good_functional_outcome_1yr
  target_kind: prognosis
  claim: Age, Barthel Index score, educational level, and stroke subtype were identified
    as significant predictors of good functional outcome at 1 year (defined as an
    ASRS score of 4 or 5) in univariable logistic regression analyses.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 130
    population: Adult Dutch native/near-native speakers with aphasia due to a first-ever
      stroke
    phase: not_reported
    time_post_onset: Predictors measured at baseline (mean 4 days post-stroke); outcome
      measured at 1 year post-stroke.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Outcome variable was dichotomized due to lack of adequate numbers in more severe
    ASRS categories
  - Structural brain damage was not incorporated into the model due to inadequate
    routine CT data
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Age, Barthel Index score, educational level (categorized
    as high or low), and stroke subtype (haemorrhage or infarction) measured at baseline
    (mean of 4 days after stroke). Analysis performed using univariable logistic regression;
    Good functional outcome defined as ASRS score of 4 or 5. Additional metadata has
    not been transcribed; review the pending-field flags before approval. PDF image
    reading (P3-S1-C16, two-model agreement, human verification pending): A total
    of 130 patients were entered into the prognostic ana-

    lyses Original text-layer quotation is preserved below. PDF image reading (P1-S3-C4,
    two-model agreement, human verification pending): . Adult Dutch native/near-native
    speakers

    who could complete language tests between 2 and

    14 days after stroke were eligible for inclusion Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:good_functional_outcome_1yr
  citation: '@ElHachioui2013'
  source_passages:
  - section: Original source P1-S1-C9
    page: 1
    quote: 'Age, Barthel

      Index score, educational level and haemorrhagic stroke

      were identiﬁed as other signiﬁcant predictors of

      outcome.'
    supports: claim
  - section: Original source P3-S2-C7
    page: 3
    quote: 'Age, Barthel Index score, educational level and stroke subtype

      were the other signiﬁcant independent predictors with a p value

      ≤0.20 in univariable logistic regression analyses (table 2).'
    supports: claim
  - section: Original source P3-S1-C16
    page: 3
    quote: 'A total of 130 patients were entered into the prognostic ana-

      lyses.'
    supports: sample
  - section: Original source P1-S3-C4
    page: 1
    quote: 'Adult Dutch native/near-native speakers

      who could complete language tests between 2 and

      14 days after stroke were eligible for inclusion.'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'Next, we investigated the

      inﬂuence of other potential prognostic factors with univariable

      logistic regression analyses, selected on the basis of the

      Table 1

      Baseline characteristics of the 147 included patients

      Demographics

      Age (years), mean (SD)

      67 (15)

      Females, n (%)

      78 (53)

      Handedness, n (%)

      Right-handed

      127 (86)

      Not right-handed (ie, left or ambidextrous)

      17 (12)

      Unknown

      3 (2)

      Level of education, n (%)

      High*

      73 (50)

      Low†

      69 (47)

      Unknown

      5 (3)

      Neurological

      Clinical localisation of stroke, n (%)

      Left hemisphere

      145 (99)

      Right hemisphere

      2 (1)

      Stroke subtype, n (%)

      Infarction

      126 (86)

      Non-cardioembolic

      84 (57)

      Cardioembolic

      42 (29)

      Intracerebral haemorrhage

      21 (14)

      Lesion location, n (%)

      Cortical only

      64 (51)

      Subcortical or combined cortical and subcortical

      15 (12)

      No visible lesions

      47 (37)

      Barthel Index at T1‡ (0–20), median (IQR)

      15 (7.75–20)

      Risk factors

      Vascular history, n (%)

      Ischaemic heart disease

      32 (22)

      Other heart disease

      14 (10)

      Other vascular disease

      12 (8)

      Transient ischaemic attack

      16 (11)

      Vascular risk factors, n (%)

      Current smoking

      54 (37)

      Excessive alcohol use

      4 (3)

      Hypercholesterolaemia

      37 (25)

      Hypertension

      64 (44)

      Diabetes mellitus

      15 (10)

      Atrial fibrillation

      34 (23)

      Linguistic performance (ScreeLing test14)

      Semantics at T1‡ (0–24), mean (SD)

      17 (6)

      Phonology at T1‡ (0–24), mean (SD)

      14 (6)

      Syntax at T1‡ (0–24), mean (SD)

      15 (6)

      *Junior high school or middle vocational education up to university.

      †Unfinished elementary school up to sophomore high school or lower vocational

      education.

      ‡T1 (baseline) was a mean of 4 days after stroke.'
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Outcome measure

      We chose verbal communicative ability at 1 year after stroke as

      the outcome measure, which was deﬁned by the ASRS11 as a

      dichotomous variable with scores of 0–3 indicating poor

      functional aphasia outcome and scores of 4–5 indicating good

      functional aphasia outcome.'
    supports: method
  - section: Original source P4-S1-C8
    page: 4
    quote: 'First, we had to dichotomise

      our outcome variable because in the more severe categories of

      the ASRS we lacked adequate numbers of patients, which pre-

      cluded the use of ordinal regression models (shift analysis).'
    supports: limitation
  - section: Original source P5-S1-C3
    page: 5
    quote: 'Finally, we were unable to incorporate the

      role of structural brain damage in our prognostic model because

      as a consequence of the observational design of our study, data

      from routine CT scanning were inadequate.'
    supports: limitation
predictor_type: clinical
short_definition: Age, Barthel Index score, educational level (categorized as high
  or low), and stroke subtype (haemorrhage or infarction) measured at baseline (mean
  of 4 days after stroke).
assessment:
- Barthel Index
- Aphasia Severity Rating Scale
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: ElHachioui2013
  proposal_id: R004
  review_status_sha256: e3a46ab7c4d86829d8187292e3e0a22e79943796f7e1f153f6d23f2a126e1ff0
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
        A/passages.json: a6e618cac5b9ed655c7fd7c02d0398c6d3df5843eab522c2ad7b2b2557c15e2a
        A/raw.json: 91b925547d061c52f5afefd43b9b6d1d1faf5a2be70c62e83f663fe38f1634c2
        A/source-units.json: f720ce5d67887c0cf08e2c7b4d3e910f3abcea75f16345456ddf36f18701dfc3
        A/full-source-units.json: 0dccb5256ad1eb22d7e5be32d6c47743a4a3e41ecededdc74bcedfc5605c14c7
        A/meta.json: 2b343a4fb8a27606b054bb3fb96bbc6f380046ed2b011aae559283dc844f61a6
        A/table-images/TABLE-1-page-2-1.png: 45d64ae49d30a2c4cd48115fce3db974e8f2af4644fa66e4b6e2ac2bd16f0cb9
        A/table-images/page-2.png: ba1b8989c0321904e11d8224f083ab6baff60721fc2449652b0306989ebafcf4
        A/table-images/page-4.png: 2fdc56dd8b183065c5d80bfc2e29e8aa500f04658e5180ce54f16cba6218b05d
        A/table-images/TABLE-3-page-4-3.png: 463e149187eff0b807090eb4b57cc091e2c45a9efee9930a829d6e42759e0199
        A/table-images/TABLE-4-page-4-2.png: 4c4a4d9f68838edc2f06fd0bfaeafab83ab1b93e39f373b0ea8e6750b29190ba
        A/table-images/manifest.json: 9950c155f6bd865ad0a42c4643e2e6bd77d0ed103548e5fec930cf42eed28475
        A/table-images/TABLE-2-page-4-1.png: 7331c4e819f437fb767b58e00855c22c598336671a6f4ba88e51267a245eae3d
        A/clauses/window-03/raw.json: e5a298d57086f07ed47850e3df1e684af64d435360f77e55903842762f34f52f
        A/clauses/window-03/prompt.txt: a995591622138730431a714a5b707542a6811c2f5687cec11015006239199ac4
        A/clauses/window-03/meta.json: 3694b5d17d22b4aa380092a55039a1e1186449e92405ffab923ef22fead204dd
        A/clauses/window-04/raw.json: 15891675af3a9f321062f79614953ed5c44541a03f36e7261861a3aa0457503c
        A/clauses/window-04/prompt.txt: 2a9c47b5178719dc3d5ae8a1fe9daeffd2edee955bdbb85d70464adabbf258bc
        A/clauses/window-04/meta.json: c1d25b70885bd7dd668762ca58e2bf33d29d5230b843a94103d7b25963a5aeb3
        A/clauses/window-05/raw.json: 49984d2e0170c1808edcb06771a9971186149b4cff0266f21e4e923d54064b59
        A/clauses/window-05/prompt.txt: 59e600099e87b6a58312bda0b52fcb7dfae115c75781ed5d22ec894ec40afd4a
        A/clauses/window-05/meta.json: b20a73369daf2772e591ccb420bed7253abe9c522ad2ee06ca2d75355f4a13bd
        A/clauses/window-02/raw.json: 1e4cb60058aa48fe52d12bb3c8d535a988224040bdaa0a211b5dd8ec6f2466d6
        A/clauses/window-02/prompt.txt: cdce593152ae0aecefc3b32f4ef46d7b7658954f330fb3c0bd64579c068d092d
        A/clauses/window-02/meta.json: 3fd5068000e83f087bb52db98afbe4ec5c83cd8f7055398caa18bae60b0ec3d3
        A/clauses/window-01/raw.json: ee5b06f55f6261fb61f0f7c9f52a953db82aa0be7e214241f3e0c6a92a46fdee
        A/clauses/window-01/prompt.txt: 8fda234ad61d500466b5acc64dc3b8f4208a6add0488aae70a960b9642412d43
        A/clauses/window-01/meta.json: 90bbee175b3ce1fc6ffe9ab609ac2d4741f62a756bbd6d05f1ad5cd18f396535
        A/clauses/window-06/raw.json: e638ef51e5e61b3352d0532874e1fbecd45194e21069474516352515006b439b
        A/clauses/window-06/prompt.txt: 02a7d2277b4781313b5e7933a931f587c53b48406b4c377d098b731c4b85999f
        A/clauses/window-06/meta.json: 0828f7613f3335603c611bdc33660d0656ffb08983ebef9c05e53903c28de463
        A/tables/TABLE-1-page-2-1/raw.json: f5299382e06379a926bc3488eca41193b29e157df20946945b27a443c89027b2
        A/tables/TABLE-1-page-2-1/prompt.txt: 13c30350f7fa2a736c4476703cd6519d8009d1b15698165740c6857a68b9a351
        A/tables/TABLE-1-page-2-1/meta.json: 526601836827d304c43a935a79c7c9101c58a921472eec0f3dc56e0040eeaebd
        A/tables/TABLE-4-page-4-3/raw.json: b866e65df483457d79f4c075ec4d0a98770f50cbc38c130940c03d5e346e339e
        A/tables/TABLE-4-page-4-3/prompt.txt: 73070f50b2512fcc7017ee8fe57851cbcfab716c618b7c01b2dc8ba33f4b61c7
        A/tables/TABLE-4-page-4-3/meta.json: b42c367532c107b53395741507e3f29f5ddbb4dac9ccaeb9d8a7598e20aa850d
        A/tables/TABLE-3-page-4-4/raw.json: 502f0e1ce0e07e6d9d3ee481d4a05516d324bc291ca60cb3e66de06820388a8d
        A/tables/TABLE-3-page-4-4/prompt.txt: a4edea5a8406374290576d0a6a6a6801d38626b03bb57981833800b2bf1c75a8
        A/tables/TABLE-3-page-4-4/meta.json: f208994667570244bd471de06cc6fddf2767ddceffdd38bf28c3fe39f5b1ddae
        A/tables/TABLE-2-page-4-2/raw.json: 267fed2fa902e37ddf95678aa4f4f49c66f6f3489c82315fc2f9e18587b9f5f8
        A/tables/TABLE-2-page-4-2/prompt.txt: 613d5e385d9db4fa70ff0060d40a2bc93b2984afda94ebca40fd2b2fa11169db
        A/tables/TABLE-2-page-4-2/meta.json: ed943356e68a859b2fdf5c95f1dd85ed21db8a603e2ced1316d946338884a332
        B/passages.json: a6e618cac5b9ed655c7fd7c02d0398c6d3df5843eab522c2ad7b2b2557c15e2a
        B/raw.json: 2d7036fc4333320f7fae6225359a1771943c31503763e2b39326849a30c77bc7
        B/source-units.json: f720ce5d67887c0cf08e2c7b4d3e910f3abcea75f16345456ddf36f18701dfc3
        B/full-source-units.json: 0dccb5256ad1eb22d7e5be32d6c47743a4a3e41ecededdc74bcedfc5605c14c7
        B/meta.json: 2701dc8562bff193b0ac7a0379600098cfc7cd9ccb443cae7215dc183ce0fa78
        B/table-images/TABLE-1-page-2-1.png: 45d64ae49d30a2c4cd48115fce3db974e8f2af4644fa66e4b6e2ac2bd16f0cb9
        B/table-images/page-2.png: ba1b8989c0321904e11d8224f083ab6baff60721fc2449652b0306989ebafcf4
        B/table-images/page-4.png: 2fdc56dd8b183065c5d80bfc2e29e8aa500f04658e5180ce54f16cba6218b05d
        B/table-images/TABLE-3-page-4-3.png: 463e149187eff0b807090eb4b57cc091e2c45a9efee9930a829d6e42759e0199
        B/table-images/TABLE-4-page-4-2.png: 4c4a4d9f68838edc2f06fd0bfaeafab83ab1b93e39f373b0ea8e6750b29190ba
        B/table-images/manifest.json: 4e515f23456bd1d1965719b50620d36cba36c425b823616f9f62083167d25075
        B/table-images/TABLE-2-page-4-1.png: 7331c4e819f437fb767b58e00855c22c598336671a6f4ba88e51267a245eae3d
        B/clauses/window-03/raw.json: ee7eb71eaf7bb33819a2a05012268009f0dc39aa8e94236446e8b0e2a24978c6
        B/clauses/window-03/prompt.txt: a995591622138730431a714a5b707542a6811c2f5687cec11015006239199ac4
        B/clauses/window-03/meta.json: 7c67073d447dc2172a84002022f638adc4b9c858c7361fe9b5a2789f7547ba09
        B/clauses/window-04/raw.json: 40e037439925a12cf8aaa04333834dd041381b0e0d7c7e5c406ad3080b675458
        B/clauses/window-04/prompt.txt: 2a9c47b5178719dc3d5ae8a1fe9daeffd2edee955bdbb85d70464adabbf258bc
        B/clauses/window-04/meta.json: 4023252aaf007bb0f8a50d2239cb11b93256f95f213b59e24cc662a46a4043b2
        B/clauses/window-05/raw.json: 32f5f08ccd1d5a8afd2b3d57ce54a2ea169957c1ea563de066cce42a2a34fdb4
        B/clauses/window-05/prompt.txt: 59e600099e87b6a58312bda0b52fcb7dfae115c75781ed5d22ec894ec40afd4a
        B/clauses/window-05/meta.json: 07411377243a05a712d2853edee21eac4e2b8e97aec947afe16483a9668a9b31
        B/clauses/window-02/raw.json: ca612518619ff2e0f9ab653be235bf5c8710a89234e22584b8e5cdc421d4e7b7
        B/clauses/window-02/prompt.txt: cdce593152ae0aecefc3b32f4ef46d7b7658954f330fb3c0bd64579c068d092d
        B/clauses/window-02/meta.json: b4dd9099b5b6c5a809ff50677a7a89cd1f0864f71595f797b9695a2d3475a7c5
        B/clauses/window-01/raw.json: 0e201eebe9631e7c443873ecc1915bb6ca42ac6d495fadf9123f3b557e0dc771
        B/clauses/window-01/prompt.txt: 8fda234ad61d500466b5acc64dc3b8f4208a6add0488aae70a960b9642412d43
        B/clauses/window-01/meta.json: c8b1748ffcbf84339a7db786cd4b517097eaf7e4c3b2948b8afb1d435e6304cc
        B/clauses/window-06/raw.json: 23c9814e5de7c58e9c2118801821a0fb5863efee4b71b7cf718e880f29bc75ff
        B/clauses/window-06/prompt.txt: 02a7d2277b4781313b5e7933a931f587c53b48406b4c377d098b731c4b85999f
        B/clauses/window-06/meta.json: 3f6f0dcdc9d2196095b4c411dc9dc2d0ab61d0d1bbe5358071e25b94d52399f4
        B/tables/TABLE-1-page-2-1/raw.json: 3658224862faada7da6134d719a595f28ea4a8fe7af7f1e9bb58082e360ebf5f
        B/tables/TABLE-1-page-2-1/prompt.txt: 13c30350f7fa2a736c4476703cd6519d8009d1b15698165740c6857a68b9a351
        B/tables/TABLE-1-page-2-1/meta.json: cdb6e5279a896b202f995adc1d3e2dda4902a1312abe3b661933d77187e90518
        B/tables/TABLE-4-page-4-3/raw.json: 0db65e9a16ed6757eedcfdf9d9d238222f7d9354d1527c78c43996708a81954f
        B/tables/TABLE-4-page-4-3/prompt.txt: 73070f50b2512fcc7017ee8fe57851cbcfab716c618b7c01b2dc8ba33f4b61c7
        B/tables/TABLE-4-page-4-3/meta.json: 19ce1acf7ca4a00aea183a16706e8e00b5535f53214ea07379858c029a3f3058
        B/tables/TABLE-3-page-4-4/raw.json: fd6221fff6eb216767d4756a1e7f3db8d152cad400cf597f3792d5b1aaf6a59f
        B/tables/TABLE-3-page-4-4/prompt.txt: a4edea5a8406374290576d0a6a6a6801d38626b03bb57981833800b2bf1c75a8
        B/tables/TABLE-3-page-4-4/meta.json: 451a101e470aecca3af26ee9ff080289d1d4d4c4f25925bdf4ca9442a7468f1b
        B/tables/TABLE-2-page-4-2/raw.json: fc1820dc4a7cab803b2fb2f3fb446ecd91c64217bc86de816361faeab78f03bf
        B/tables/TABLE-2-page-4-2/prompt.txt: 613d5e385d9db4fa70ff0060d40a2bc93b2984afda94ebca40fd2b2fa11169db
        B/tables/TABLE-2-page-4-2/meta.json: 25011612d8088a089eeed391332a225d18adf22846004987d9245723c03d2dc5
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
      pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
      source_review: _compare/relationships-2026-11-16/review-current/ElHachioui2013
      source_status_sha256: da8293962379f6156eb33a94b26d075c78bdb632e16b20e3502849fc2f828b7c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: age, Barthel Index score, educational level, and stroke subtype
    outcome:
      text: good functional outcome at 1 year (ASRS 4 or 5)
    analysis_label: univariable logistic regression
    relation: association
    evidence_ids:
    - P1-S1-C9
    - P3-S2-C7
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
      pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
      source_review: _compare/relationships-2026-11-16/review-current/ElHachioui2013
      source_status_sha256: da8293962379f6156eb33a94b26d075c78bdb632e16b20e3502849fc2f828b7c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C17
      - Result passage disposed without unit P3-S2-C1
      - Result passage disposed without unit P3-S2-C3
      - Accounting without a linked unit P3-S3-C4
      - Unaccounted source passage P3-S3-C4
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C11
      - Result passage disposed without unit P3-S3-C12
      - Result passage disposed without unit P3-S3-C13
      - Result passage disposed without unit P3-S3-C14
      - Result passage disposed without unit P3-S3-C15
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P5-S2-C1
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C8
      - Unaccounted source passage P5-S2-C1
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C8
      - Result passage disposed without unit P5-S2-C9
      - Accounting without a linked unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C8
      - Accounting without a linked unit P5-S3-C9
      - Unaccounted source passage P5-S3-C3
      - Unaccounted source passage P5-S3-C9
      unattached_null_or_qualifier_ids:
      - P5-S1-C8
      - P5-S2-C1
      - P5-S2-C8
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 100
      unselected_timing_passages:
      - P1-S1-C5
      - P1-S3-C4
      - P1-S3-C6
      - P2-S1-C5
      - P3-S1-C13
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P4-S2-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - analysis_restrictions
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-4
      - TABLE-4-page-4-3
      unlinked_tables:
      - TABLE-1-page-2-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
      source_review: _compare/relationships-2026-11-16/review-current/ElHachioui2013
      source_status_sha256: da8293962379f6156eb33a94b26d075c78bdb632e16b20e3502849fc2f828b7c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports baseline linguistic components as significant predictors in
        univariable analysis.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports variance explained by linguistic variables and phonology as
        the only significant predictor in multivariable analysis.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies age, Barthel Index, education, and stroke subtype as significant
        predictors.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: States the final model explained 55.7% of the variance.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Provides the AUC of 0.89 for the final model.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Reports increase in variance and AUC when adding phonological recovery.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion summarizing findings.
    - source_id: P2-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive data on treatment hours.
    - source_id: P3-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about sensitivity analysis regarding extrapolated data.
    - source_id: P3-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count for analysis.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of ASRS scores.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Confirms association between baseline linguistic scores and 1-year outcome.
    - source_id: P3-S2-C6
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports multivariable variance and phonology as the only significant
        predictor.
    - source_id: P3-S2-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Lists other significant independent predictors in univariable analysis.
    - source_id: P3-S2-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Reports variance and AUC for the final model.
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Reports improvement in variance and AUC with phonological recovery.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of how to calculate probability.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S2-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study result.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study description.
    - source_id: P3-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study result.
    - source_id: P3-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion statement.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of predictors.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion interpretation of phonology.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion statement on model ability.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion statement on recovery value.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of good outcome.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with other studies.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with other studies.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of recovery rate variance.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of Barthel Index and age findings with other studies.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of education findings with other studies.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Reports no effect of sex, handedness, lesion location, vascular history
        or other risk factors.
    unresolved_coverage:
    - source_id: P5-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C5
    - P2-S2-C10
    - P3-S1-C17
    - P3-S2-C1
    - P3-S2-C3
    - P3-S2-C11
    - P3-S2-C12
    - P3-S2-C13
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C16
    - P3-S2-C17
    - P3-S2-C18
    - P3-S2-C19
    - P3-S3-C4
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C7
    - P3-S3-C8
    - P3-S3-C9
    - P3-S3-C10
    - P3-S3-C11
    - P3-S3-C12
    - P3-S3-C13
    - P3-S3-C14
    - P3-S3-C15
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C9
    - P5-S1-C8
    - P5-S2-C1
    - P5-S2-C4
    - P5-S2-C8
    - P5-S2-C9
    - P5-S3-C8
    - P5-S3-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-4-2
    - TABLE-3-page-4-4
    - TABLE-4-page-4-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C16
      recruited_sample:
      - P1-S3-C2
      eligibility:
      - P1-S3-C4
      - P1-S3-C5
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P2-S1-C3
      - P2-S2-C11
      outcome_definition:
      - P2-S2-C11
      validation:
      - P1-S2-C3
      - P3-S1-C7
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C6
      - P2-S2-C12
      - P2-S2-C13
      - P2-S2-C14
      limitations:
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C10
      - P4-S1-C13
      - P5-S1-C3
      - P5-S1-C4
      - P5-S2-C5
      - P5-S3-C7
      personal_factors: []
      tested_personal_effects:
      - P3-S2-C6
      - P3-S2-C7
      - P5-S3-C3
      adjustment_roles:
      - P4-S3-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C8
      - P2-S1-C9
      - P2-S2-C6
      - P2-S2-C7
      - P3-S1-C12
      - P3-S3-C12
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P4-S2-C4
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
      pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
      review_sha256: e3a46ab7c4d86829d8187292e3e0a22e79943796f7e1f153f6d23f2a126e1ff0
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
      - P1-S1-C9
      - P3-S2-C7
      source_result: Age, Barthel Index score, educational level, and stroke subtype
        were identified as significant predictors of good functional outcome at 1
        year (ASRS 4 or 5) in univariable logistic regression analyses.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly states that these variables were identified
            as significant predictors in univariable logistic regression analyses
            (P1-S1-C9, P3-S2-C7). The proposed core correctly identifies this as the
            univariable analysis, distinct from the multivariable model where only
            phonology remained significant.
          source_ids:
          - P1-S1-C9
          - P3-S2-C7
        direction:
          answer: fits
          reason: The source indicates these variables are 'significant predictors'
            (P1-S1-C9). The proposed core uses 'likely' direction, which is a reasonable
            qualitative summary of a significant association without specifying the
            exact odds ratio direction for each variable, which is appropriate for
            a qualitative draft.
          source_ids:
          - P1-S1-C9
          - P3-S2-C7
        construct:
          answer: fits
          reason: The exposure (age, Barthel, education, stroke subtype) and outcome
            (good functional outcome at 1 year, ASRS 4-5) match the source descriptions
            in P1-S1-C9 and P3-S2-C7. The measurement is non-imaging (clinical/demographic
            variables and ASRS scale).
          source_ids:
          - P1-S1-C9
          - P3-S2-C7
          - P2-S2-C11
        qualifications:
          answer: fits
          reason: The core correctly qualifies the finding as being from 'univariable
            logistic regression analyses'. This is a material qualifier because the
            multivariable analysis yielded different results (only phonology significant).
            The definition of the outcome (ASRS 4 or 5) is also correctly included.
          source_ids:
          - P1-S1-C9
          - P3-S2-C7
        missing_material_caveat:
          answer: fits
          reason: The core includes the key limitation regarding the dichotomization
            of the outcome variable (P4-S1-C8) and the exclusion of structural brain
            damage (P5-S1-C3). No other material caveats that change the interpretation
            of the univariable result are missing.
          source_ids:
          - P4-S1-C8
          - P5-S1-C3
      optional_pending:
      - Specific odds ratios and confidence intervals for each predictor in the univariable
        analysis
      - Exact p-values for each predictor in the univariable analysis
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific odds ratios and confidence intervals for each predictor in the univariable
      analysis
    - Exact p-values for each predictor in the univariable analysis
    normalizations: []
    analysis_identity:
      id: R004
      exposure:
        text: age, Barthel Index score, educational level, and stroke subtype
      outcome:
        text: good functional outcome at 1 year (ASRS 4 or 5)
      analysis_label: univariable logistic regression
      relation: association
      evidence_ids:
      - P1-S1-C9
      - P3-S2-C7
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
        pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
        source_review: _compare/relationships-2026-11-16/review-current/ElHachioui2013
        source_status_sha256: da8293962379f6156eb33a94b26d075c78bdb632e16b20e3502849fc2f828b7c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C16:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fabb1f58bd5cdacccc1a826814821091864576f79cc0d9acd694d7b06ba162f0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C16
          page: 3
          text_layer_sha256: fabb1f58bd5cdacccc1a826814821091864576f79cc0d9acd694d7b06ba162f0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'A total of 130 patients were entered into the prognostic ana-

          lyses.'
        anchor_text: 'A total of 130 patients were entered into the prognostic ana-

          lyses.'
        excluded_fragments: []
        image_sha256: 6be1c71cda1250b50295c0d434780d6abd3d43b28a4b343c0f3cbb427ea30ab2
        transcription: 'A total of 130 patients were entered into the prognostic ana-

          lyses'
      P1-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a792aa147995b6552e70a0b14b204f62309aa2927b4e93ae55adc9840e970284
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6f8b7672fa948cb3c0fe51884d963b51bf5b9f19a1ea033b3b6becbb0f75d771
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C4
          page: 1
          text_layer_sha256: 6f8b7672fa948cb3c0fe51884d963b51bf5b9f19a1ea033b3b6becbb0f75d771
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Adult Dutch native/near-native speakers

          who could complete language tests between 2 and

          14 days after stroke were eligible for inclusion.'
        anchor_text: 'Adult Dutch native/near-native speakers

          who could complete language tests between 2 and

          14 days after stroke were eligible for inclusion.'
        excluded_fragments: []
        image_sha256: 6df8b91e9b727c81849f5daaa3dbb142bb616f2ee2be816162cbc45977add181
        transcription: '. Adult Dutch native/near-native speakers

          who could complete language tests between 2 and

          14 days after stroke were eligible for inclusion'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Age, Barthel

    Index score, educational level and haemorrhagic stroke

    were identiﬁed as other signiﬁcant predictors of

    outcome.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
