---
id: time_post_onset
name: Time since stroke
kind: predictor
predictor_type: clinical
short_definition: Time since stroke
findings:
- id: f1
  target: functional_communication
  target_kind: impairment
  claim: Main Results report +1.0 AAT spontaneous-speech communication points for
    enrolment within one month (95% CI 0.7–1.4; n=232, 6 RCTs), and +0.33 beyond six
    months (n=170, 7 RCTs). The abstract instead gives +1.1 for the early group; this
    discrepancy remains flagged.
  direction: likely
  relationship: correlational
  method: meta-analysis
  design: meta-analysis
  sample:
    n: 232
    population: Poststroke aphasia; participants with SLT access during the study
      period, from RCT datasets
    phase: mixed
    cohort: RELEASE IPD meta-analysis; shared underlying datasets across outcomes
    time_post_onset: Baseline median 43.6 weeks (IQR 4–165.1) across available outcomes;
      subgroup-specific enrolment below
    subgroup: Enrolment<1 month
    denominator_note: n is the quoted subgroup, not all RELEASE participants or the
      full outcome pool
  statistics:
    threshold: 95% confidence intervals for estimated subgroup mean changes; between-subgroup
      test not reported here
    effect_size: Main Results mean +1.0 [0.7,1.4]; abstract +1.1
  confounders_controlled:
  - Study random effect; jointly modelled demographic covariates passing univariable
    P<0.1 selection. Main text does not enumerate each domain’s final adjustment set.
  confounders_not_controlled:
  - Spontaneous recovery
  - Education, handedness and socioeconomic status excluded
  - Initial stroke severity, mood, cognitive impairments and other concurrent interventions
    inadequately available
  region_definition:
    kind: not_reported
  author_limitations:
  - Unable to account for spontaneous recovery
  - Incomplete availability of important covariates and repeated outcome assessments
  evidence_quality: meta-analysis
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping after dual extraction/local review)
    extracted_on: '2026-11-17'
    paper_section: Main PDF Results pp4–5; Methods p3; limitations p7
    confidence: medium
    flags:
    - human_approval_pending
    - subgroup_means_not_treatment_effects
    - final_covariate_sets_unresolved
  outcome_timing:
    measure: functional_communication
    type: change_from_baseline
    interval: Baseline to first follow-up; overall median interval 10 weeks (IQR 3–26),
      not a fixed follow-up for every participant
  notes: No deterministic patient-level prognosis or eligibility rule. Supplementary
    files not used. Main-text subgroup results retained with their original denominators.
  citation: '@Ali2021'
  source_passages:
  - section: Source passage P1-S2-C6
    page: 1
    quote: "Younger age (<55 \nyears, +15.4 Western Aphasia Battery Aphasia-Quotient\
      \ points [CI, 10.0–20.9], +6.1 correct on AAT Token Test [CI, \n3.2–8.9]; +9.3\
      \ Boston Naming Test points [CI, 4.7–13.9]; +0.8 AAT Spontaneous-Speech Communication\
      \ subscale \npoints [CI, 0.5–1.0]) and enrollment <1 month post-onset (+19.1\
      \ Western Aphasia Battery Aphasia-Quotient points \n[CI, 13.9–24.4]; +5.3 correct\
      \ on AAT Token Test [CI, 1.7–8.8]; +11.1 Boston Naming Test points [CI, 5.7–16.5];\
      \ \nand +1.1 AAT Spontaneous-Speech Communication subscale point [CI, 0.7–1.4])\
      \ conferred the greatest absolute \nchange-from-baseline across each language\
      \ domain."
    supports: claim
  - section: Source passage P3-S1-C8
    page: 3
    quote: "The absolute change \nin language domain scores from baseline to first\
      \ follow-up was \nregressed onto stroke, aphasia, and demographic covariates\
      \ \nspecified a priori (baseline language impairment score, age, \nsex, lesioned\
      \ hemisphere, stroke type, handedness, language \nof data collection, and time\
      \ since stroke)."
    supports: method
  - section: Source passage P3-S1-C9
    page: 3
    quote: "Only variables that \nwere significant at univariable level (P<0.1) were\
      \ included in \nthe multivariable analysis."
    supports: method
  - section: Source passage P3-S1-C10
    page: 3
    quote: "Each multivariable analysis included \nthe study as a random covariate\
      \ to account for possible vari-\nability in the outcome measure between studies,\
      \ with the demo-\ngraphic variables modeled jointly."
    supports: confounders
  - section: Source passage P4-S1-C6
    page: 4
    quote: "Data at baseline \n(median=43.6 weeks since stroke; IQR [4–165.1]) \n\
      and first follow-up (median=10 weeks since baseline; \nIQR [3–26]) were available\
      \ for overall-language-ability \n(n=943; 24 datasets, represented by the Western\
      \ Apha-\nsia Battery-AQ), auditory comprehension (n=1056; 29 \ndatasets, represented\
      \ by the Aachen Aphasia Test [AAT] \nToken Test), naming (n=791, 27 datasets,\
      \ by Boston \nNaming Test), and functional-communication (n=974, \n23 datasets,\
      \ represented by the AAT Spontaneous-\nSpeech Communication subscale, Figure 1)."
    supports: sample
  - section: Source passage P4-S2-C3
    page: 4
    quote: "Education, \nhandedness, and socioeconomic status were therefore \nexcluded\
      \ as covariates from our analyses."
    supports: confounders
  - section: Source passage P7-S1-C8
    page: 7
    quote: "We were unable to account for spontaneous recovery \nin our study."
    supports: limitation
  - section: Source passage P7-S2-C2
    page: 7
    quote: "Many potentially important covariates such \nas language stimulation in\
      \ the living environment, other \nconcomitant rehabilitation interventions,\
      \ education \nlevel, initial stroke severity, mood disorders, co-existing \n\
      cognitive impairments, and socioeconomic status were \ninconsistently available\
      \ across the datasets, and there-\nfore could not inform our planned analyses."
    supports: limitation
  - section: Source passage P5-S1-C4
    page: 5
    quote: "When examining chronicity, the greatest absolute \ngain was observed for\
      \ enrollment within 1 month of \nstroke (+1-point, 95% CI [0.7–1.4]; IPD=232,\
      \ 6 \nRCTs)."
    supports: claim
  - section: Source passage P5-S1-C5
    page: 5
    quote: "Gains were also evident at later time points \n(1–3 months=+0.87 points\
      \ [IPD=68, 5 RCTs]; \n3–6 months=+0.4 points [IPD=62, 4 RCTs]; >6 \nmonths=+0.33\
      \ points [IPD=170, 7 RCTs])."
    supports: claim
assessment:
- Time since index stroke at study enrolment
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-17'
relationship_review:
  paper: Ali2021
  proposal_id: U002
  review_status_sha256: 8fc6ca658a72b20239e8003166457c0b00c12576da6db184efcc2ac7e420f295
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
      A/passages.json: e2aedd1f6f8d7760bcb4e75fb745467ba944988043c714be35ff281faab62aa3
      A/raw.json: eac7a90a194d03bcfd0ef882babbbcb153bea62226a44cd54c667655e0598abe
      A/source-units.json: 7fd786971429746e5c7463d07eaa9a33006112dcb2add198c54cb51a4eceab0b
      A/full-source-units.json: 647a2f1605e85b055578d85b3c47824fbbea7eaad39c10029228f50834060f4a
      A/meta.json: e3737ea5abe15967404a263a4f3f28f7f069b045d3411bc849aa1f978d2075b8
      A/table-images/manifest.json: 958387f4ced803ad14156b407a280f70a0a71f9ab30f3cbceb860001b5f4d1c1
      A/clauses/window-03/raw.json: cd9abe972d3ce84a8d19e4fa86ab3235174a0613889db6bc1285f07087e44192
      A/clauses/window-03/prompt.txt: c2eceb91a2154f66406280757f80e14c63c77c76e86d665241fcd64ae4cc88e4
      A/clauses/window-03/meta.json: 7a77fec04e3a07dcb6a20da21bf4973c523fb2252b957aed3767c1d33cd4ae59
      A/clauses/window-04/raw.json: 0ae40fe2776ceba2fa8978f680033aeceea6e92b8202e511893ffc1c18841a0f
      A/clauses/window-04/prompt.txt: dad01644df4abfddb809140e96a7132e29907ff9ee184d1b1b5d994101af84cc
      A/clauses/window-04/meta.json: 048f53bc0111785a8857d1c0587f0be8035ee0a3ab13e618e4fdfd113e4ab925
      A/clauses/window-05/raw.json: 8fec8eba8902338ae2dc02bc0155f920e5b676b8ce2f6d094e4480518d07ef58
      A/clauses/window-05/prompt.txt: ae7e74cb71ba28d8ebf689e56df5b1765402e3df73482325fb18598ae000044b
      A/clauses/window-05/meta.json: e90818b2fc2bc3b5670d0b64069c4c34867e537577275cfafa111734c1fdaaf0
      A/clauses/window-02/raw.json: 589217bcf35c9ef19df6de6baefd71c2326e4444f5aa478bdd91c88af931995e
      A/clauses/window-02/prompt.txt: 8c61c60a22dc2acb49228d8502157cdb1d5f72ff0bb47ee033aa0f7d1750f851
      A/clauses/window-02/meta.json: 85109ca4ade77a0d2ba9e2e0fba4f75672d2135e967b539ed56e26b59bf93163
      A/clauses/window-07/raw.json: f7ec666f0f6533313569cd969777d43a2098bef97fcf17a8ae463d982a4057c1
      A/clauses/window-07/prompt.txt: ad81ec1f70c7481a0c615efebe80b65b399918c70f704e08d49929ee4c230754
      A/clauses/window-07/meta.json: 1cf4044a77949391120dd569d184b978624a32f59b09e4322742dea73a1e0407
      A/clauses/window-01/raw.json: 916ac02a8f051980bdf848ca71917de2a690e4264b7c84eaa2b35d6509133453
      A/clauses/window-01/prompt.txt: abcb6c9675a08b5b3af45a4963a5383788b9f40e6bcc7f2a71db3bd6f2948c7a
      A/clauses/window-01/meta.json: 55d1c5f118818f287609f7570332cd2f3d595664361cbfd6536dca0214ba0b2a
      A/clauses/window-06/raw.json: b436046953be570df4a5cdf414561af1bfb2ac1d8a4eeef5aa1f4a7041eb4828
      A/clauses/window-06/prompt.txt: 590a31e9cc026aa97acf51cf736e1d789fe1a98d088c84c14038c04798422a8e
      A/clauses/window-06/meta.json: 467e04f15a045be85b6bd014e9d3adf700cdc02e12a407a698cb99f4c3b09fc6
      B/passages.json: e2aedd1f6f8d7760bcb4e75fb745467ba944988043c714be35ff281faab62aa3
      B/raw.json: 471b8cfa714bdcfc8ba53070b21ea72868538f92e2f3ff69b64bc04f175c14e6
      B/source-units.json: 7fd786971429746e5c7463d07eaa9a33006112dcb2add198c54cb51a4eceab0b
      B/full-source-units.json: 647a2f1605e85b055578d85b3c47824fbbea7eaad39c10029228f50834060f4a
      B/meta.json: 7500e1307d5f44aca5ac4c5e17b6ac578113a822b55a398bfeae8d2a44dbf30f
      B/table-images/manifest.json: 958387f4ced803ad14156b407a280f70a0a71f9ab30f3cbceb860001b5f4d1c1
      B/clauses/window-03/raw.json: 4f9bdb5eef120cda6ab9e3545772710505ec54fe3884dae9c1babefff71910eb
      B/clauses/window-03/prompt.txt: c2eceb91a2154f66406280757f80e14c63c77c76e86d665241fcd64ae4cc88e4
      B/clauses/window-03/meta.json: 66525ae42d13d4400ecd2e01ec4037b5f3d46a01fd788294e7a50f686cc23dda
      B/clauses/window-04/raw.json: 5fc5ef9ee65ce54e20b44f3abfd42b919be1d0ca9d12b7d51067f437f1d65bba
      B/clauses/window-04/prompt.txt: dad01644df4abfddb809140e96a7132e29907ff9ee184d1b1b5d994101af84cc
      B/clauses/window-04/meta.json: 72c1c3c13f3aa3121b8b85a21d6619ae6363be44cbc02d8072d2a1bfcf505c02
      B/clauses/window-05/raw.json: cb05bbc61cc9e4012ee476e26ae06759993bcf3414bdbd583a7e4e69c30f2cd4
      B/clauses/window-05/prompt.txt: ae7e74cb71ba28d8ebf689e56df5b1765402e3df73482325fb18598ae000044b
      B/clauses/window-05/meta.json: c96a2f7399111d743cabca3adeb572bf75d53fcb63518f4b83be4a01b211eae8
      B/clauses/window-02/raw.json: d9b6cc77f787e9503c24dabd2202bedf0c4397d3ad7d666c4a694883d0515c4f
      B/clauses/window-02/prompt.txt: 8c61c60a22dc2acb49228d8502157cdb1d5f72ff0bb47ee033aa0f7d1750f851
      B/clauses/window-02/meta.json: ecd3fd2ba7e24d198a120116ebf06c07b73cf6f37a9bcb81588176e1e27e69a4
      B/clauses/window-07/raw.json: 44be998e9ba0d2bcaa691e5c0acfa879314c58ae42746680fc91c64ff215c4dd
      B/clauses/window-07/prompt.txt: ad81ec1f70c7481a0c615efebe80b65b399918c70f704e08d49929ee4c230754
      B/clauses/window-07/meta.json: 52be48fc1259e2cec6f31812322ce4c2cf3e62f0cb0c0b6a9c47ea3adeff79c1
      B/clauses/window-01/raw.json: c06dfb7da06d00e478d18d04aacda63b46a9d1e792837235e221517fe2d01183
      B/clauses/window-01/prompt.txt: abcb6c9675a08b5b3af45a4963a5383788b9f40e6bcc7f2a71db3bd6f2948c7a
      B/clauses/window-01/meta.json: d70ea733692bfb7b5d69f6266685244a28c9fb42aad5419997fe2bc17ebce723
      B/clauses/window-06/raw.json: f9dfa2dc8b2a6bb106764b3b28f70a83c8dbeb3fdb33b81716962ac9333933ef
      B/clauses/window-06/prompt.txt: 590a31e9cc026aa97acf51cf736e1d789fe1a98d088c84c14038c04798422a8e
      B/clauses/window-06/meta.json: f56c81c096ac08bae7ffb4641297537512cd702f34c3073a31d69c0f91616a83
    code:
      relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
      relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
      ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
      strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
    model: gemma4:26b
    model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
    host: http://localhost:11434
    max_output_tokens: 20000
  proposal:
    evidence_ids:
    - P1-S2-C6
    qualifier_ids: []
    context_ids:
    - P1-S1-C12
    - P2-S3-C8
    table_ids: []
    exposure:
      text: enrollment <1 month post-onset (+19.1 Western Aphasia Battery Aphasia-Quotient
        points [CI, 13.9–24.4]; +5.3 correct on AAT Token Test [CI, 1.7–8.8]; +11.1
        Boston Naming Test points [CI, 5.7–16.5]; and +1.1 AAT Spontaneous-Speech
        Communication subcall
      source_id: P1-S2-C6
    outcome:
      text: absolute change-from-baseline across each language domain
      source_id: P1-S2-C6
    relation: association
    effect_unit: individual
    result_status: reported_detected
    outcome_type: change_from_baseline
    direction: positive
    direction_source_id: P1-S2-C6
    origin: current_study
    label_match_candidates:
      exposure: []
    id: U002
    flags:
    - direction_unsupported
    - nonverbatim_or_missing_label
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C14
    - P1-S1-C15
    - P1-S2-C5
    - P2-S1-C5
    - P2-S1-C6
    - P2-S1-C7
    - P2-S2-C4
    - P2-S2-C5
    - P2-S2-C6
    - P2-S2-C7
    - P2-S2-C8
    - P2-S2-C9
    - P2-S3-C1
    - P2-S3-C2
    - P2-S3-C3
    - P2-S3-C5
    - P2-S3-C7
    - P2-S3-C9
    - P3-S1-C10
    - P3-S1-C8
    - P3-S2-C5
    - P4-S2-C3
    - P5-S1-C8
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: 65ae35fffb7cf3b088b690754f27d806ce0e9c348f1d69b9dfbc3b084be2c8e9
  audit:
    coverage_issues:
    - Result passage disposed without unit P3-S2-C9
    - Result passage disposed without unit P4-S1-C4
    - Result passage disposed without unit P4-S1-C8
    - Result passage disposed without unit P4-S1-C9
    - Result passage disposed without unit P4-S2-C4
    - Result passage disposed without unit P4-S2-C7
    - Result passage disposed without unit P4-S2-C8
    - 'window 5: invalid/duplicate disposition P4-S3-C1'
    - Result passage disposed without unit P4-S3-C1
    - Result passage disposed without unit P4-S3-C2
    - Result passage disposed without unit P4-S3-C5
    - Result passage disposed without unit P4-S3-C10
    - Accounting without a linked unit P4-S3-C6
    - Accounting without a linked unit P4-S3-C7
    - Accounting without a linked unit P4-S3-C8
    - Accounting without a linked unit P4-S3-C9
    - Accounting without a linked unit P5-S1-C2
    - Accounting without a linked unit P5-S1-C3
    - Accounting without a linked unit P5-S1-C4
    - Unaccounted source passage P5-S1-C3
    - Unaccounted source passage P4-S3-C8
    - Unaccounted source passage P4-S3-C6
    - Unaccounted source passage P5-S1-C2
    - Unaccounted source passage P4-S3-C9
    - Unaccounted source passage P5-S1-C4
    - Unaccounted source passage P4-S3-C7
    - Result passage disposed without unit P5-S1-C10
    - Result passage disposed without unit P5-S1-C7
    - Result passage disposed without unit P5-S2-C4
    - Accounting without a linked unit P6-S1-C3
    - Accounting without a linked unit P7-S1-C2
    - Accounting without a linked unit P7-S1-C4
    - Accounting without a linked unit P7-S1-C7
    - Accounting without a linked unit P7-S1-C8
    - Accounting without a linked unit P7-S2-C2
    - Accounting without a linked unit P7-S2-C3
    - Unaccounted source passage P7-S1-C4
    - Unaccounted source passage P7-S1-C2
    - Unaccounted source passage P6-S1-C3
    - Unaccounted source passage P7-S2-C2
    - Unaccounted source passage P7-S2-C3
    - Unaccounted source passage P7-S1-C7
    - Unaccounted source passage P7-S1-C8
    unattached_null_or_qualifier_ids:
    - P4-S1-C8
    - P4-S2-C5
    - P7-S1-C2
    - P7-S1-C7
    suppressed_nonrepresented_units: 19
    default_disposition_count_requires_completeness_check: 123
    unselected_timing_passages:
    - P2-S2-C8
    - P3-S1-C4
    - P3-S1-C6
    - P4-S1-C2
    - P4-S1-C10
    - P4-S2-C5
    personal_effect_slots_without_result_classification: []
    held_frame_selections: []
    empty_frame_slots_require_confirmation:
    - imaging_provenance
    - imaging_timing
    unclassified_extraction_ids: []
    table_review_required: []
    unlinked_tables: []
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P2-S3
      - P3-S2
      - P3-S3
      - P4-S1
      - P5-S1
      - P5-S2
      - P6-S1
      - P7-S2
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C10
      - P4-S1-C6
      - P5-S2-C2
      recruited_sample:
      - P2-S2-C8
      eligibility:
      - P2-S2-C8
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S2-C5
      - P4-S1-C6
      - P7-S2-C4
      outcome_definition:
      - P2-S3-C8
      - P2-S3-C9
      - P3-S2-C5
      - P5-S1-C8
      - P7-S1-C7
      validation:
      - P7-S1-C4
      analysis_restrictions:
      - P4-S1-C8
      - P4-S2-C4
      - P4-S2-C5
      - P7-S2-C3
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S3-C8
      - P3-S1-C8
      limitations:
      - P7-S2-C2
      - P7-S2-C3
      - P7-S2-C4
      personal_factors:
      - P2-S2-C9
      - P3-S1-C8
      - P4-S1-C10
      - P4-S2-C3
      - P7-S2-C2
      tested_personal_effects:
      - P1-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C11
      - P5-S1-C2
      - P5-S1-C4
      - P5-S1-C6
      adjustment_roles:
      - P3-S1-C8
      - P3-S1-C10
      explicitly_not_adjusted:
      - P4-S2-C3
      descriptive_personal_factors:
      - P2-S2-C9
      - P4-S1-C2
      - P4-S1-C10
    outcome_type: change_from_baseline
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections: []
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-17'
    approved: false
    pdf_sha256: e892d43e338ecd29cd3f64363943450b6e1a22e1bb59f948bd635d56d9f8b6cb
    licence:
      category: cc
      label: CC BY
      url: https://doi.org/10.1161/strokeaha.120.031162
      version: published
      source: unpaywall
      doi: 10.1161/strokeaha.120.031162
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
    visual_pages:
    - 4
    - 5
    scope: Selected main-text mean-change estimates and clinical qualifiers; not complete
      source review of figures or supplementary material
    corrections:
    - Observed change is baseline to first follow-up, not from stroke onset; median
      follow-up 10 weeks after baseline.
    - Numbers below are subgroup mean changes, not between-group effect sizes or individual
      prognoses.
    - Primary figures use RCT-derived participants but age and enrolment timing were
      not randomised exposures.
    - 'Do not infer a causal benefit of earlier therapy: spontaneous recovery could
      not be accounted for.'
    - 'No education, handedness or socioeconomic null effect inferred: these were
      excluded as covariates.'
    - For functional communication, main Results report +0.75 (age<55) and +1.0 (<1
      month), while abstract rounds/reports +0.8 and +1.1; use main Results and flag
      disagreement.
    - Post-six-month auditory-comprehension estimate CI includes zero despite narrative
      saying gains evident.
    remaining:
    - Named-person approval and reconciliation with existing RELEASE findings; avoid
      double counting overlapping RELEASE datasets.
    - Figures 1–3 and supplementary-only estimates not completely adjudicated. Exact
      final covariate set for each domain cannot be established from main text alone.
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Younger age (<55 \nyears, +15.4 Western Aphasia Battery Aphasia-Quotient\
    \ points [CI, 10.0–20.9], +6.1 correct on AAT Token Test [CI, \n3.2–8.9]; +9.3\
    \ Boston Naming Test points [CI, 4.7–13.9]; +0.8 AAT Spontaneous-Speech Communication\
    \ subscale \npoints [CI, 0.5–1.0]) and enrollment <1 month post-onset (+19.1 Western\
    \ Aphasia Battery Aphasia-Quotient points \n[CI, 13.9–24.4]; +5.3 correct on AAT\
    \ Token Test [CI, 1.7–8.8]; +11.1 Boston Naming Test points [CI, 5.7–16.5]; \n\
    and +1.1 AAT Spontaneous-Speech Communication subscale point [CI, 0.7–1.4]) conferred\
    \ the greatest absolute \nchange-from-baseline across each language domain."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-17'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
