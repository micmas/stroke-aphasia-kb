---
id: left_uncinate_ilf_overlap
name: Left uncinate/ILF overlap
kind: tract
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Higher mean T1 intensity in the left uncinate/ilf overlap was associated
    with better WAB-R fluency score (0–10) (r=0.296, p=.005; n=76). It was not retained
    as an additional predictor in the final stepwise model.
  direction: likely
  relationship: correlational
  method: LSM
  design: cross-sectional
  sample:
    n: 76
    population: Chronic aphasia/persistent deficits after one left-hemisphere ischaemic
      stroke
    phase: chronic
    time_post_onset: 6–276 months; cohort mean 35.57 months
    cohort: University of South Carolina Aphasia Lab; 76 participants total, 57 with
      semantic scores
    denominator_note: Outcome-specific n; two of 76 above WAB-R aphasia cutoff but
      residual deficits
  statistics:
    effect_size: Pearson r=0.296; p=.005
    threshold: Bonferroni alpha .008 for correlations; .025 for regression; Hotelling
      comparisons exploratory and uncorrected
  confounders_controlled: []
  confounders_not_controlled:
  - Pearson correlations unadjusted
  - Other WAB-R subtests explicitly not controlled
  - Age, sex, education, handedness and time poststroke not reported as covariate
    effects
  region_definition:
    kind: tract
    description: Catani atlas-derived ROI; unique tract tissue or explicitly named
      overlap, not whole-tract equivalence
  imaging: T1
  imaging_details:
    reference_space: other
    reference_space_detail: 1mm isotropic ICBM standard template; exact variant not
      specified
    atlases_used:
    - Catani et al. 2012 white-matter atlas; aslant ROI supplied by Catani and colleagues
    measure: Mean left-ROI T1 intensity Z-score normalised using intact right-hemisphere
      intensity; not FA or streamline count
  lesion_mapping:
    analysis: univariate
    n_analysed: 76
    min_lesion_overlap: not_reported
    lesion_volume_correction: none
    multiple_comparisons: bonferroni
    scope: Unadjusted scalar ROI-intensity correlation; stepwise model qualifiers
      described separately
  outcome_timing:
    type: status_at_assessment
    interval: At least 6 months after stroke; scan and testing usually same day, no
      more than 1 month apart
  author_limitations:
  - T1 intensity is indirect tissue integrity measure and cannot be compared with
    DTI here
  - WAB-R forced-choice fluency scale does not isolate initiation, grammar or lexical
    retrieval
  evidence_quality: cohort
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping after dual extraction and local review)
    extracted_on: '2026-11-17'
    paper_section: Main PDF Methods pp2–3, Results pp3–5, Table1, Figures1–3
    confidence: medium
    flags:
    - human_approval_pending
    - cross_sectional_not_prognostic
    - unique_and_overlap_ROIs_distinct
  notes: No deterministic patient prognosis. Lesion size and all six ROIs entered
    stepwise selection; Table1 lists retained ROI predictors without enumerating a
    retained lesion-volume coefficient. Preserve this distinction from forced covariate
    adjustment. Check cohort overlap with Fridriksson2013 before pooling.
  citation: '@Basilakos2014'
  source_passages:
  - section: Source passage P3-S4-C4
    page: 3
    quote: 'RESULTS

      The ASAF/aslant ROI overlap (r = 0.64, p < 0.001), aslant

      (r = 0.634, p < 0.001), ASAF (r = 0.428, p < 0.001), uncinate

      fasciculus (r = 0.574, p < 0.001), and the uncinate/ILF overlap

      (r = 0.296, p = 0.005) were correlated with speech ﬂuency scores,

      whereas the ILF was not (r = 0.015, p = 0.448).'
    supports: claim
  - section: Source passage P3-S3-C11
    page: 3
    quote: 'To control for multiple comparisons in the corre-

      lation analyses, the alpha-level was Bonferroni corrected within

      each behavioral measure by dividing the alpha-level of p = 0.05

      by the number of regions examined (six).'
    supports: claim
  - section: Source passage P3-S3-C12
    page: 3
    quote: 'Thus, the threshold for

      signiﬁcance was set to p = 0.008.'
    supports: claim
  - section: Source passage P3-S3-C13
    page: 3
    quote: 'To control for multiple compar-

      isons in the regression analyses, the alpha-level was Bonferroni

      corrected by dividing the alpha-level of p = 0.05 by the num-

      ber of behavioral measures examined (two).'
    supports: claim
  - section: Source passage P3-S3-C14
    page: 3
    quote: 'Thus, the threshold

      for signiﬁcance was set to p = 0.025.'
    supports: claim
  - section: Source passage P2-S2-C2
    page: 2
    quote: 'MATERIALS AND METHODS

      PARTICIPANTS

      This study included 76 patients (32 female, 73 right-handed) with

      chronic aphasia who have undergone language testing and MRI

      studies at the University of South Carolina’s Aphasia Lab over a

      follow-up period of 10 years.'
    supports: sample
  - section: Source passage P2-S2-C9
    page: 2
    quote: 'The mean age of the patients was 61.35 years (SD = 12.67,

      range = 36–83), and the mean time post-stroke was 35.57 months

      (SD = 47.56, range = 6–276).'
    supports: sample
  - section: Source passage P2-S3-C7
    page: 2
    quote: 'PyramidsandPalmTrees

      Test scores were available for 57 of the 76 individuals; the mean

      score was 46 of 52 possible (SD = 5.25, range = 26–52).'
    supports: sample
  - section: Source passage P2-S3-C10
    page: 2
    quote: 'MRI DATA COLLECTION

      All subjects underwent a structural brain anatomy assessment

      using a high-resolution T1-MRI performed at least 6 months after

      the stroke, in close chronological proximity with the language

      testing session (usually within the same day, but no longer than

      1 month apart).'
    supports: method
  - section: Source passage P3-S1-C3
    page: 3
    quote: 'T1, T2, and lesion images

      were co-registered, and T1 images were bias corrected, segmented,

      and normalized to the 1 mm isotropic ICBM standard brain tem-

      plate using the cost-function approach (Andersen et al., 2010).'
    supports: method
  - section: Source passage P3-S3-C2
    page: 3
    quote: 'Due to notable overlap between the aslant and ASAF and

      the uncinate and ILF, we created two additional ROIs composed of

      the areas of overlap between the aslant and ASAF regions (herein

      referred to as theASAF/aslant region overlap) and the uncinate fas-

      ciculus and ILF (herein referred to as the uncinate fasciculus/ILF

      overlap).'
    supports: method
  - section: Source passage P3-S3-C3
    page: 3
    quote: 'This allowed for analyses based on unique white matter

      ROIs, as well as ROI overlap.'
    supports: method
  - section: Source passage P3-S3-C6
    page: 3
    quote: 'First, we used separate Pearson corre-

      lations for each ROI, to predict ﬂuency (WAB-R ﬂuency subtest

      score) and semantic processing (Pyramids and Palm Trees Test).'
    supports: method
  - section: Source passage P3-S3-C8
    page: 3
    quote: 'Finally, these intensity values were entered into

      a stepwise regression analysis including all six ROIs, along with

      lesion size as a control variable (including both cortical and

      subcortical damage), to determine which regions remained sig-

      niﬁcant predictors for each behavioral measure, given extent of

      damage and damage to all other areas as cofactors.'
    supports: confounders
  - section: Source passage P3-S3-C9
    page: 3
    quote: 'Scores on addi-

      tional WAB-R subtests were not controlled for, as these are highly

      associated with our dependent variables, ﬂuency, and semantic

      processing.'
    supports: confounders
  - section: Source passage P3-S3-C12
    page: 3
    quote: 'Thus, the threshold for

      signiﬁcance was set to p = 0.008.'
    supports: statistics
  - section: Source passage P3-S3-C14
    page: 3
    quote: 'Thus, the threshold

      for signiﬁcance was set to p = 0.025.'
    supports: statistics
  - section: Source passage P6-S1-C6
    page: 6
    quote: 'We are not able to compare

      DTI data to those data presented here, nor are we aware of avail-

      able studies that compare these two approaches.'
    supports: limitation
  - section: Source passage P4-S1-C14
    page: 4
    quote: 'The relationship between ﬂuency and the remaining

      tracts investigated was not found to be signiﬁcant in this model.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-17'
relationship_review:
  paper: Basilakos2014
  proposal_id: U005
  review_status_sha256: 94fe2915721833240400c299aaebdb918d5182d204e74443476227fcabcc5ce4
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
      A/passages.json: 252fa20deef64fcaaa7bfb384be74d25163e7c8b05d3c59d4897072c0f5db518
      A/raw.json: 387d2a3d5d5d3ef774251e73bc434f770f041ff6d98492e3e884d5b2f6e6ade4
      A/source-units.json: 82c8714e90260ce76c6996c23079d876386e7b596c2b123af8a26f44e0207bf4
      A/full-source-units.json: e8eda30b82910da3c5eaab23e87726053ae325bac92dc3a1a78d365524d34076
      A/meta.json: ed8ea8b7751d09bfbf463facbbb50bf746ee6088764b0d90bc670a9bac6fb568
      A/table-images/TABLE-1-page-5-1.png: bca47854bb53f1e2ce90350c385018e34efe66e429f9087926476d75d0ce4105
      A/table-images/page-5.png: 43ad14d17b3ed01eb9a3a75981eda92605cea7e687365575f107a3338786a874
      A/table-images/manifest.json: 6e5a5a61f758c11750b2890d8b3428beda56ce4ad811a8c5b80f27720f6824a6
      A/clauses/window-03/raw.json: ca11d30d399af45c99dc8d881b9ed77b0e1ec7df167857b37595875564772893
      A/clauses/window-03/prompt.txt: 181dfcee0d359239f187947df7df97f6d55573eab86e15a6d3e5ea2b37107732
      A/clauses/window-03/meta.json: 216f744f7d427e6b764b107f8d0870979df442c022634bfc0a6b632d2cf04e0e
      A/clauses/window-04/raw.json: 7422d3550de3b67828bf30f7ae0e0fbfb06862e2ba63bf46768356788188f352
      A/clauses/window-04/prompt.txt: e3fa43602af596835929de79d9d1f8b6905830deb2960f292b6b3b2f26dd9558
      A/clauses/window-04/meta.json: 8bf017ec38b90faf11a5307fb1777d89c401d2bd713969a7149f997c13ebde58
      A/clauses/window-05/raw.json: 6acbd39096886c65726e747fdef9dac95381d8e8cd9ba8e3f31873b5fe024cac
      A/clauses/window-05/prompt.txt: 5a6b5b27c5ba5b6128d52a7c53b5b3ba1de9cea2e3c801184787944d341faddc
      A/clauses/window-05/meta.json: 9cb644007faa1e3e06d9ac729afd4fae91d4721cf0b8a2cd7be1f69e2212415e
      A/clauses/window-02/raw.json: d2270fe483faea4f1967586d9854b131231740168c20c9d7c30c38f5e7039dc3
      A/clauses/window-02/prompt.txt: 703a6b0dfdb4a2ea2debcee1f6a7cecee87f8f7c059988623e45ff7ea31abf62
      A/clauses/window-02/meta.json: 10db06c0c9f2f79857f93346375adeaf64164f7763d0bb14452729f54dd3e8b4
      A/clauses/window-01/raw.json: 97d959b578bb3265d366292cd954b13a5fec232581bab90e5c27c5849ee24af2
      A/clauses/window-01/prompt.txt: 076fbcef95c0f095298ef08747fbc74717598afca20be71051f556d858182183
      A/clauses/window-01/meta.json: 69d3b545fc50ad5591b99509e5fbc432dd35ac8545d22eed2922657a54e9e65d
      A/clauses/window-06/raw.json: 994b811ee046f32fbf2074900fc24a77067cf9ab24a15ea2dbc3b59bbb430b9d
      A/clauses/window-06/prompt.txt: 1e2f3b1636b37a8a8d16452e44703bbf64adff848071fa58c64317e81434af3a
      A/clauses/window-06/meta.json: 15ef8ca5afeffa27874c3a6437c8bbfec2f6f634f27b8e6ff475525d9094b4fe
      A/tables/TABLE-1-page-5-1/raw.json: d3681ab0ba84c974706238d6d0dce697c6b00a568b83bd41384a430099c0b788
      A/tables/TABLE-1-page-5-1/prompt.txt: f232de63e5dea046bd46f8eabdfbb1653d4430e9bf769b3eb3df2d382f2f709e
      A/tables/TABLE-1-page-5-1/meta.json: 064c9e7fbc6bc51db408a047d5f415f4cd3db24b9de6aeeb72246ec05f0793fb
      B/passages.json: 252fa20deef64fcaaa7bfb384be74d25163e7c8b05d3c59d4897072c0f5db518
      B/raw.json: 87529eec5eaff004b93dffa403c17e21c56727d65ba92d7c425c9a70e3f084b5
      B/source-units.json: 82c8714e90260ce76c6996c23079d876386e7b596c2b123af8a26f44e0207bf4
      B/full-source-units.json: e8eda30b82910da3c5eaab23e87726053ae325bac92dc3a1a78d365524d34076
      B/meta.json: 13fe066f33adfda82aa5d0c95138065a2015c4bb4f000c818e38101275a73658
      B/table-images/TABLE-1-page-5-1.png: bca47854bb53f1e2ce90350c385018e34efe66e429f9087926476d75d0ce4105
      B/table-images/page-5.png: 43ad14d17b3ed01eb9a3a75981eda92605cea7e687365575f107a3338786a874
      B/table-images/manifest.json: 936561cc2dad47e24590a38489e6518423ed328c9340ef3ad3beb76aa6e351aa
      B/clauses/window-03/raw.json: 109f53309bdc615d7670a313235eb16d586b62dba479d1091ac4da9f675ac2da
      B/clauses/window-03/prompt.txt: 181dfcee0d359239f187947df7df97f6d55573eab86e15a6d3e5ea2b37107732
      B/clauses/window-03/meta.json: 5b6a0386edfd3bd3473cdd6bf5ff96ae2609e7c7806007a085770ed4377e8f4a
      B/clauses/window-04/raw.json: d38af3752a80e46b6ca4758f2a8b525bf009c2ff10082a78d5bbd3425bbce833
      B/clauses/window-04/prompt.txt: e3fa43602af596835929de79d9d1f8b6905830deb2960f292b6b3b2f26dd9558
      B/clauses/window-04/meta.json: 9ad162c93330faeacde4cc56894369071584f281fadd8057398612df89087aca
      B/clauses/window-05/raw.json: 63e66e3b30105d737435063fe57637aeb9ac9836faee611a46aadf53bffd2b75
      B/clauses/window-05/prompt.txt: 5a6b5b27c5ba5b6128d52a7c53b5b3ba1de9cea2e3c801184787944d341faddc
      B/clauses/window-05/meta.json: 29f880b914b562897d0a10dd2f13ab127636a4f43918394d880e05212127b60a
      B/clauses/window-02/raw.json: 1828a8edc12287e4d719d0e65e42363fa26a05fb60df774a369991ee68dec98f
      B/clauses/window-02/prompt.txt: 703a6b0dfdb4a2ea2debcee1f6a7cecee87f8f7c059988623e45ff7ea31abf62
      B/clauses/window-02/meta.json: 59d99fce79bf516d86f18386aac1a563e98d951e7eceb6e853d40d9a90703137
      B/clauses/window-01/raw.json: 68ade726ce2951117b5f9e86996a26754913a4d36d887c78581e84a5526d8203
      B/clauses/window-01/prompt.txt: 076fbcef95c0f095298ef08747fbc74717598afca20be71051f556d858182183
      B/clauses/window-01/meta.json: d881a3e31a5a670d30eadd726336b15e91669af9370c824b242be906a5f929e9
      B/clauses/window-06/raw.json: 58f4b3b169873f77b8bb97f7219f1c63a1e41e360318a583a6fe0e2d499519b2
      B/clauses/window-06/prompt.txt: 1e2f3b1636b37a8a8d16452e44703bbf64adff848071fa58c64317e81434af3a
      B/clauses/window-06/meta.json: fe7c19dad36f27a0b6ce05755594b7f28aede1f5d9bdc19488700c1dd88e63a2
      B/tables/TABLE-1-page-5-1/raw.json: 4eb00387a7b0b29b5790a4e2ea6eaad199fc84ec8acb3729724b6cd397c1e93e
      B/tables/TABLE-1-page-5-1/prompt.txt: f232de63e5dea046bd46f8eabdfbb1653d4430e9bf769b3eb3df2d382f2f709e
      B/tables/TABLE-1-page-5-1/meta.json: 057337b13ef89d0b294e6573103b0dd7999fc56f70a2b46e0952b669c92b99b4
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
    - P3-S4-C4
    qualifier_ids:
    - P3-S3-C11
    - P3-S3-C12
    - P3-S3-C13
    - P3-S3-C14
    context_ids:
    - P3-S2-C5
    - P3-S2-C6
    - P3-S3-C2
    table_ids: []
    exposure:
      text: uncinate/ILF overlap
      source_id: P3-S2-C5
    outcome:
      text: speech ﬂuency scores
      source_id: P2-S2-C13
    relation: association
    effect_unit: individual
    result_status: reported_detected
    outcome_type: status_at_assessment
    direction: positive
    direction_source_id: ''
    origin: current_study
    label_match_candidates:
      exposure:
      - P3-S4-C4
      outcome:
      - P3-S4-C4
    id: U005
    flags:
    - direction_unsupported
    - label_source_not_attached
    - nonverbatim_or_missing_label
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P2-S2-C10
    - P2-S2-C11
    - P2-S2-C12
    - P2-S2-C13
    - P2-S2-C14
    - P2-S2-C3
    - P2-S2-C4
    - P2-S2-C5
    - P2-S2-C6
    - P2-S3-C10
    - P2-S3-C11
    - P2-S3-C12
    - P2-S3-C13
    - P2-S3-C3
    - P2-S3-C6
    - P3-S2-C10
    - P3-S2-C11
    - P3-S2-C2
    - P3-S2-C3
    - P3-S2-C4
    - P3-S3-C10
    - P3-S3-C6
    - P3-S3-C8
    - P3-S3-C9
    - P3-S4-C3
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C13
    - P5-S3-C10
    - P5-S3-C2
    - P5-S3-C8
    - P6-S1-C4
    - P6-S1-C7
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: bb33be810efb33e813474b57e59c1527335955cdd4226267bbe0af82818ee0dd
  audit:
    coverage_issues:
    - Result passage disposed without unit P1-S1-C8
    - Result passage disposed without unit P2-S3-C5
    - Result passage disposed without unit P2-S3-C7
    - Result passage disposed without unit P2-S3-C8
    - Result passage disposed without unit P2-S3-C9
    - 'window 4: invalid/duplicate disposition P3-S3-C11'
    - 'window 4: invalid/duplicate disposition P3-S3-C12'
    - 'window 4: invalid/duplicate disposition P3-S3-C13'
    - 'window 4: invalid/duplicate disposition P3-S3-C14'
    - Result passage disposed without unit P4-S1-C11
    - Result passage disposed without unit P4-S1-C15
    - Result passage disposed without unit P5-S1-C3
    unattached_null_or_qualifier_ids:
    - P1-S1-C8
    - P2-S3-C9
    - P4-S1-C15
    suppressed_nonrepresented_units: 6
    default_disposition_count_requires_completeness_check: 127
    unselected_timing_passages:
    - P2-S2-C2
    - P2-S2-C4
    - P2-S2-C7
    - P2-S2-C9
    personal_effect_slots_without_result_classification: []
    held_frame_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    empty_frame_slots_require_confirmation:
    - validation
    - personal_factors
    - tested_personal_effects
    unclassified_extraction_ids: []
    table_review_required:
    - TABLE-1-page-5-1
    unlinked_tables: []
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P3-S3
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C2
      recruited_sample:
      - P2-S2-C2
      eligibility:
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C6
      imaging_provenance:
      - P3-S2-C10
      - P3-S2-C11
      imaging_timing:
      - P2-S3-C10
      outcome_timing:
      - P2-S3-C10
      outcome_definition:
      - P2-S2-C13
      - P2-S2-C14
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
      - P5-S3-C10
      validation: []
      analysis_restrictions:
      - P3-S3-C11
      - P3-S3-C13
      - P3-S4-C3
      dependent_variable_statement:
      - P3-S3-C6
      - P3-S3-C8
      limitations:
      - P5-S3-C1
      - P5-S3-C2
      - P5-S3-C8
      - P6-S1-C4
      - P6-S1-C6
      - P6-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S3-C8
      explicitly_not_adjusted:
      - P3-S3-C9
      descriptive_personal_factors:
      - P2-S2-C9
      - P2-S3-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-17'
    approved: false
    pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
    licence:
      category: cc
      label: CC BY
      url: https://doi.org/10.3389/fnhum.2014.00845
      version: published
      source: unpaywall
      doi: 10.3389/fnhum.2014.00845
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
    - 9
    visual_pages:
    - 4
    - 5
    - 6
    - 7
    scope: Main ROI fluency and semantic relationships, Table 1 and Figures 1–3; selected
      regression and null qualifiers. No supplements.
    corrections:
    - Study measured atlas-based structural T1 intensity, not patient diffusion tractography
      or disconnection.
    - Six ROIs distinguish unique tract portions from ASAF/aslant and uncinate/ILF
      overlaps.
    - 76 participants for fluency; 57 for semantic processing. Ten years describes
      data collection, not individual follow-up.
    - Cross-sectional chronic status, not prospective recovery prediction. Scan and
      language testing usually same day, at most one month apart.
    - Unadjusted correlations distinguished from stepwise models; lesion size entered
      as candidate/control but retained final model not enumerated as volume-adjusted
      in Table 1.
    - P5 semantic paragraph ends with an apparent fluency typo; Table 1 confirms semantic
      outcome. Figure 2 caption mentions aslant and ASAF, whereas legend displays
      overlap and uncinate-unique.
    - Source F, p and R2 values retained as reported; no p values recomputed or confidence
      intervals invented.
    remaining:
    - Named-person approval and reconciliation with existing findings, including possible
      cohort overlap with Fridriksson2013.
    - Exact atlas mask files/thresholds and final retained volume term not supplied
      here.
    - Exploratory Hotelling comparisons and AphasiaBank measurement-validation analysis
      not separately converted.
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'RESULTS

    The ASAF/aslant ROI overlap (r = 0.64, p < 0.001), aslant

    (r = 0.634, p < 0.001), ASAF (r = 0.428, p < 0.001), uncinate

    fasciculus (r = 0.574, p < 0.001), and the uncinate/ILF overlap

    (r = 0.296, p = 0.005) were correlated with speech ﬂuency scores,

    whereas the ILF was not (r = 0.015, p = 0.448).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-17'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
