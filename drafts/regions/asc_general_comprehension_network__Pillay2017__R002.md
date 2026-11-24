---
id: asc_general_comprehension_network
name: general comprehension cluster
kind: network
findings:
- id: f1
  target: asc_impairment
  target_kind: impairment
  claim: When no covariates were included in the analysis, auditory sentence comprehension
    (ASC) impairment was associated with damage in the left inferior frontal cortex,
    superior temporal gyrus (STG), middle temporal gyrus (MTG), supramarginal gyrus
    (SMG), and angular gyrus.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 51
    population: right-handed native English speakers with chronic left hemisphere
      stroke
    phase: not_reported
    time_post_onset: at least 180 days poststroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - results are limited to the left middle cerebral artery territory
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the left inferior frontal
    cortex, superior temporal gyrus (STG), middle temporal gyrus (MTG), supramarginal
    gyrus (SMG), and angular gyrus, measured via high-resolution T1-weighted MRI.
    analysis performed with no covariates. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S1-C3, two-model
    agreement, human verification pending): . Participants were 51 patients (25 women)
    with focal encephalomalacia from chronic left hemisphere stroke, included regardless
    of language ability, but without comorbid neurologic or major psychiatric disease
    (e.g., bipolar disorder, dementia, epilepsy, major depression, schizophrenia)
    Original text-layer quotation is preserved below. PDF image reading (P2-S1-C5,
    two-model agreement, human verification pending): All participants were at least
    180 days poststroke, native English

    speakers, and premorbidly right-handed according to the

    Edinburgh Handedness Inventory.17 Estimated premorbid general

    intelligence was average according to the Barona intelligence

    quotient.18 Lesion descriptions are provided in table e-1. Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:asc_impairment
  citation: '@Pillay2017'
  source_passages:
  - section: Original source P3-S2-C10
    page: 3
    quote: 'When no covariates were included in the

      analysis, ASC impairment was associated with damage

      in similar regions (figure e-1B; see table e-3 for peak

      coordinates), replicating previous results using similar

      methods.9 Notably, PN impairment was also associ-

      ated with damage in similar frontal, inferior parietal,

      and posterior STG regions (figure e-1C), consistent

      with our hypothesis that all 3 tasks require nonspecific

      executive control and phonologic processes.'
    supports: claim
  - section: Original source P2-S1-C3
    page: 2
    quote: 'Participants were 51 patients (25

      women) with focal encephalomalacia from chronic left hemi-

      sphere stroke, included regardless of language ability, but without

      comorbid neurologic or major psychiatric disease (e.g., bipolar

      disorder, dementia, epilepsy, major depression, schizophrenia).'
    supports: sample
  - section: Original source P2-S1-C5
    page: 2
    quote: 'All participants were at least 180 days poststroke, native English

      speakers,

      and

      premorbidly

      right-handed

      according

      to

      the

      Edinburgh Handedness Inventory.17 Estimated premorbid general

      intelligence was average according to the Barona intelligence

      quotient.18 Lesion descriptions are provided in table e-1.'
    supports: sample
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Voxel-based lesion-

      symptom mapping (VLSM) uses lesion status at each voxel as

      a grouping variable, and then compares the lesioned and nonle-

      sioned groups on any given dependent measure, to produce an

      effect size statistic for each voxel.23 VLSM was implemented as an

      analysis of covariance, using a custom MATLAB script to account

      for within-group variance of no interest.'
    supports: method
  - section: Original source P5-S2-C6
    page: 5
    quote: 'The methods used in the present study

      do not allow conclusions to be drawn concerning re-

      gions outside the left middle cerebral artery territory

      that are not well-represented in this patient sample.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pillay2017
  proposal_id: R002
  review_status_sha256: 6f07b3a1a29e48dde8d2a1a8186210e822ab68207c9e708d64e5beab9bb99ece
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
        A/passages.json: c52d60c8a32076136e408d49364e6806c81b289cf99ce9f96b2ba45dd3c0761a
        A/raw.json: 26404103a3489827c57507f075cb645af594a3ef12a6747e8f22933f8f1b52d0
        A/source-units.json: 1d00885cee4213e1273419bbea8c0b8ff578defcf499f8a0768c150ea20e846c
        A/full-source-units.json: 112b0df8b4bef37c732b897d697729aa03c9eb65a252a90a57246312fdce04c8
        A/meta.json: 3ce8ef36e184dd7b1c1dc2ca6259d6944efeccb27751f77cca16ab13a0b04bdf
        A/table-images/TABLE-1-page-2-1.png: f776abdee040914ebe34c7026b7f6b36bfdcd0a11e65235fd3a0f1f6010a48a4
        A/table-images/page-2.png: e7359e1ceaf0b53aa415a27650663d92088a0191ea6decdaadcd8b7ad7aeda18
        A/table-images/manifest.json: 57a21782117032de8d1237efd6490ad19e6b910ee8640794c5b2777a8ca98a14
        A/clauses/window-03/raw.json: 965ea9b28efafd952b9b81aea889913eefca40fb4517932f3c5f63f775511894
        A/clauses/window-03/prompt.txt: 9786e5b88bce5ddc26f2f77388bb0b5f0dfff68ced70a5fc02cb1265d1197f45
        A/clauses/window-03/meta.json: 133113e87a58c5a604b3156a4286f90bd9ad124d9b90db7c0ceacb5cda314a28
        A/clauses/window-04/raw.json: cd00cfc7574859ac8ec132a9f287be6932951aed939f9de722ea75f0c8897af0
        A/clauses/window-04/prompt.txt: 3cefcb736734d8ddba0350fba10396c4fe3d85152eff7f04a7c78c34b0d8715e
        A/clauses/window-04/meta.json: 3243010246991c94d45a8250a8436dd772baef6f7363e894d45bb79f77f1e70a
        A/clauses/window-05/raw.json: 482e2fea6fd9a3c26bddbfe2d205198317c3783011115f367e09d3095a9015c0
        A/clauses/window-05/prompt.txt: 37cb8b4c9cff79d335e55be67cfe5dab0ecc42fd80eac3733a49fe8eebebc935
        A/clauses/window-05/meta.json: bc7b4c9b5fe7960ad5959fe82f97eb707e3cca52e4a96489752999dba9ff42d2
        A/clauses/window-02/raw.json: d80f6afc4def9c9a9e5987c185b951962deabaaceed2bfe3dc89789d96179b29
        A/clauses/window-02/prompt.txt: 3a8f860c7c5e9bba1a35878582fb01b936b59b2b6c247afe05c4a22d89a9af5e
        A/clauses/window-02/meta.json: 87580a12866eed9b6265478081b2de58e6d35429994f34bfc31db403338abbec
        A/clauses/window-01/raw.json: 913f5c79f7fa6cac1da68723a81646db7b16ecf51c04d86f38a508e04cae3903
        A/clauses/window-01/prompt.txt: 12f59ccfdec6b2fe5283459accfa4df69470f1122aa8be43fd096f1f9e55b04a
        A/clauses/window-01/meta.json: 541e35c313ffdfd6d79684f6f8301d1b5f7db6e70f8f86e53f67451bd39b8cb7
        A/tables/TABLE-1-page-2-1/raw.json: 7820737b5d7a92d66fcae0d81305a34b08212a0babcd49f5584645431129af31
        A/tables/TABLE-1-page-2-1/prompt.txt: 02f0007a2e24590c5cd1970098d986f4937af51024aa3d8719f82fec35718606
        A/tables/TABLE-1-page-2-1/meta.json: 94c49840d8ba4df417eece799fe8eb078824bf47006d61458936d7027cb6353c
        B/passages.json: c52d60c8a32076136e408d49364e6806c81b289cf99ce9f96b2ba45dd3c0761a
        B/raw.json: 9b38490951d4ffac09243dc7212340cb9792a0a0c1cdc8bf10f1136210f0a54c
        B/source-units.json: 1d00885cee4213e1273419bbea8c0b8ff578defcf499f8a0768c150ea20e846c
        B/full-source-units.json: 112b0df8b4bef37c732b897d697729aa03c9eb65a252a90a57246312fdce04c8
        B/meta.json: e7caa42efc4f850817df271dc188aa079cc0911468aec44b62eb0010add7d325
        B/table-images/TABLE-1-page-2-1.png: f776abdee040914ebe34c7026b7f6b36bfdcd0a11e65235fd3a0f1f6010a48a4
        B/table-images/page-2.png: e7359e1ceaf0b53aa415a27650663d92088a0191ea6decdaadcd8b7ad7aeda18
        B/table-images/manifest.json: 57c69e2ecc7b0dec515d09d1cc897e70015801bbdb1e4fc5b13f0c7246f002dc
        B/clauses/window-03/raw.json: 499e655f82ec001c764f59e4ae8c6a5efba00b4d8bc3d74f19cb45167f7944f5
        B/clauses/window-03/prompt.txt: 9786e5b88bce5ddc26f2f77388bb0b5f0dfff68ced70a5fc02cb1265d1197f45
        B/clauses/window-03/meta.json: 4e928b34cacfb77c1f0db5637413dc771b4199225e91f214b49a3d158514e28a
        B/clauses/window-04/raw.json: 36f1ffa0c2089a73c5b5c5ac71748e41b28d720ba745c70a98f17863d0904d19
        B/clauses/window-04/prompt.txt: 3cefcb736734d8ddba0350fba10396c4fe3d85152eff7f04a7c78c34b0d8715e
        B/clauses/window-04/meta.json: 25adc0a593a3b3379221389501baa56b509546d94d5229008799ef0686e7a89c
        B/clauses/window-05/raw.json: f797e8c435a01b42fdda3d6734dd1f6911e4fac352f90d5eb1e399236bb6af68
        B/clauses/window-05/prompt.txt: 37cb8b4c9cff79d335e55be67cfe5dab0ecc42fd80eac3733a49fe8eebebc935
        B/clauses/window-05/meta.json: 74d874cc501f0a2e227320c0a5612f3010ee1a2f2f6084ef7145461e0e59cac9
        B/clauses/window-02/raw.json: 6b3b76ea924f37f0f8f5e309bcc9d82903c4269d242964c849f870e7d43a9d42
        B/clauses/window-02/prompt.txt: 3a8f860c7c5e9bba1a35878582fb01b936b59b2b6c247afe05c4a22d89a9af5e
        B/clauses/window-02/meta.json: 8808512597a7301ccd7c3ba718bd9e154911fa49f442dd55688604202018776d
        B/clauses/window-01/raw.json: c35001d7667693a43058a09449145aff1a4383f9e99dcfe0197300e871a4005f
        B/clauses/window-01/prompt.txt: 12f59ccfdec6b2fe5283459accfa4df69470f1122aa8be43fd096f1f9e55b04a
        B/clauses/window-01/meta.json: 40f4054ffa26ade91e63f9cb8af68befdcac54eccb1b940c2f77d3a1abd8c68c
        B/tables/TABLE-1-page-2-1/raw.json: 6c0f5fb5c273b53c1c0357b69ada08a24b4ade27895718874a27402185cf1c3c
        B/tables/TABLE-1-page-2-1/prompt.txt: 02f0007a2e24590c5cd1970098d986f4937af51024aa3d8719f82fec35718606
        B/tables/TABLE-1-page-2-1/meta.json: 3bcbf7e5fd5ff80c4731ade60dc2a4653b45185de4cdaeb47b6eac5d67208650
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
      pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
      source_review: _compare/relationships-2026-11-16/review-current/Pillay2017
      source_status_sha256: 3f793f51df7fdd97222139bb5bc36f6af172a47406d0d44c501ee90e93f61790
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: lesions in left inferior frontal cortex, superior temporal gyrus (STG),
        middle temporal gyrus (MTG), supramarginal gyrus (SMG), and angular gyrus
    outcome:
      text: auditory sentence comprehension (ASC) impairment
    analysis_label: General comprehension network (no covariates)
    relation: association
    evidence_ids:
    - P3-S2-C10
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
      pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
      source_review: _compare/relationships-2026-11-16/review-current/Pillay2017
      source_status_sha256: 3f793f51df7fdd97222139bb5bc36f6af172a47406d0d44c501ee90e93f61790
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C12
      - Accounting without a linked unit P3-S1-C13
      - Accounting without a linked unit P3-S2-C1
      - Unaccounted source passage P3-S2-C1
      - Unaccounted source passage P3-S1-C13
      - Accounting without a linked unit P3-S2-C10
      - Accounting without a linked unit P3-S2-C12
      - Accounting without a linked unit P3-S2-C13
      - Accounting without a linked unit P3-S2-C3
      - Accounting without a linked unit P3-S2-C4
      - Accounting without a linked unit P3-S2-C5
      - Accounting without a linked unit P3-S2-C9
      - Unaccounted source passage P3-S2-C9
      - Unaccounted source passage P3-S2-C10
      - Unaccounted source passage P3-S2-C13
      - Unaccounted source passage P3-S2-C5
      - Unaccounted source passage P3-S2-C3
      - Unaccounted source passage P3-S2-C12
      - Unaccounted source passage P3-S2-C4
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C4
      - Result passage disposed without unit P3-S3-C6
      - Accounting without a linked unit P3-S3-C7
      - Accounting without a linked unit P3-S3-C8
      - Result passage disposed without unit P3-S3-C9
      - Unaccounted source passage P3-S3-C7
      - Unaccounted source passage P3-S3-C8
      - Accounting without a linked unit P4-S1-C1
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S2-C4
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P4-S1-C1
      - Unaccounted source passage P5-S2-C4
      unattached_null_or_qualifier_ids:
      - P3-S3-C4
      - P3-S3-C6
      - P3-S3-C7
      - P5-S2-C4
      suppressed_nonrepresented_units: 2
      default_disposition_count_requires_completeness_check: 111
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S1-C3
      - P2-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C9
        - P2-S2-C11
        - P2-S3-C7
        - P3-S1-C2
        - P3-S1-C7
        - P3-S2-C11
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
      source_review: _compare/relationships-2026-11-16/review-current/Pillay2017
      source_status_sha256: 3f793f51df7fdd97222139bb5bc36f6af172a47406d0d44c501ee90e93f61790
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Abstract restatement of results
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 3
      - 8
      reason: Abstract restatement of results
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missing data for ASC task
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about task correlations
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports residualized correlations between ASC, ADN, and PN
    - source_id: P3-S2-C1
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Qualifies the residualization process
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation of lesion volume with behavioral measures
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation of education/IQ with ADN
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null correlation of education/IQ with ASC/PN
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null correlations for age, onset, and handedness
    - source_id: P3-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports ADN lesion correlates without covariates
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports ASC and PN lesion correlates without covariates
    - source_id: P3-S2-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Reports ADN lesion correlates with covariates
    - source_id: P3-S2-C13
      disposition: represented
      result_indexes:
      - 3
      reason: Reports white matter involvement in ADN analysis
    - source_id: P3-S3-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports null findings for frontal/SMG/angular gyrus in ADN analysis
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that adding education/IQ as covariates did not change results
    - source_id: P3-S3-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null finding for ASC in posterior superior temporal sulcus
    - source_id: P3-S3-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports ASC lesion correlates with PN covariate
    - source_id: P3-S3-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports overlap between ASC and ADN lesion clusters
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap map
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between lesion overlap and t-values
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion about MTG cluster not being an artifact
    - source_id: P3-S3-C12
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of general network results
    - source_id: P3-S3-C13
      disposition: repeated
      result_indexes:
      - 3
      - 7
      reason: Discussion restatement of specific results
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Reports shared MTG localization for ADN and ASC
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of inferior frontal lobe role
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      - 7
      reason: Discussion restatement of MTG association
    unresolved_coverage:
    - source_id: P3-S3-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P2-S2-C5
    - P3-S1-C12
    - P3-S2-C1
    - P3-S2-C2
    - P3-S2-C3
    - P3-S2-C4
    - P3-S2-C5
    - P3-S3-C4
    - P3-S3-C9
    - P3-S3-C10
    - P3-S3-C11
    - P3-S3-C12
    - P5-S1-C4
    - P5-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C3
      recruited_sample:
      - P2-S1-C3
      eligibility:
      - P2-S1-C3
      - P2-S1-C5
      imaging_provenance:
      - P2-S2-C7
      imaging_timing:
      - P2-S2-C7
      outcome_timing:
      - P2-S2-C7
      outcome_definition:
      - P2-S1-C13
      - P2-S2-C4
      validation:
      - P2-S2-C4
      analysis_restrictions:
      - P2-S2-C12
      dependent_variable_statement:
      - P2-S3-C4
      - P2-S3-C7
      - P3-S1-C5
      - P3-S3-C5
      limitations:
      - P5-S2-C6
      - P5-S2-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C3
      - P2-S1-C5
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C9
      - P2-S2-C11
      - P2-S3-C7
      - P3-S1-C2
      - P3-S1-C7
      - P3-S2-C11
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C7
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
      pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
      review_sha256: 6f07b3a1a29e48dde8d2a1a8186210e822ab68207c9e708d64e5beab9bb99ece
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
      - P3-S2-C10
      source_result: When no covariates were included in the analysis, ASC impairment
        was associated with damage in similar regions (left inferior frontal cortex,
        superior temporal gyrus, middle temporal gyrus, supramarginal gyrus, and angular
        gyrus), replicating previous results.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the 'General comprehension
            network' VLSM for ASC impairment with no covariates, as described in P2-S3-C4
            and P3-S2-C10.
          source_ids:
          - P2-S3-C4
          - P3-S2-C10
        direction:
          answer: fits
          reason: The source explicitly states that ASC impairment was 'associated
            with damage' in the specified regions, which aligns with the proposed
            claim of an association.
          source_ids:
          - P3-S2-C10
        construct:
          answer: fits
          reason: The exposure (lesions in specific cortical regions) and outcome
            (ASC impairment) are correctly identified. The measurement is template
            lesion overlap via VLSM, not patient diffusion or functional imaging.
          source_ids:
          - P3-S2-C10
          - P2-S2-C11
        qualifications:
          answer: fits
          reason: The draft correctly qualifies the finding as being from the analysis
            with 'no covariates', distinguishing it from the adjusted analyses that
            follow in the paper.
          source_ids:
          - P3-S2-C10
          - P3-S2-C11
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the left middle cerebral
            artery territory (P5-S2-C6). No other material caveats that change the
            interpretation of this specific unadjusted result are omitted.
          source_ids:
          - P5-S2-C6
      optional_pending:
      - Peak coordinates for the ASC no-covariate cluster (referenced in table e-3
        but not transcribed)
      - Specific cluster size or volume for the ASC no-covariate cluster
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Peak coordinates for the ASC no-covariate cluster (referenced in table e-3 but
      not transcribed)
    - Specific cluster size or volume for the ASC no-covariate cluster
    normalizations: []
    analysis_identity:
      id: R002
      exposure:
        text: lesions in left inferior frontal cortex, superior temporal gyrus (STG),
          middle temporal gyrus (MTG), supramarginal gyrus (SMG), and angular gyrus
      outcome:
        text: auditory sentence comprehension (ASC) impairment
      analysis_label: General comprehension network (no covariates)
      relation: association
      evidence_ids:
      - P3-S2-C10
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
        pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
        source_review: _compare/relationships-2026-11-16/review-current/Pillay2017
        source_status_sha256: 3f793f51df7fdd97222139bb5bc36f6af172a47406d0d44c501ee90e93f61790
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6856f5ef72eb94712498d8db36cb8690b9139122361d7b9c606844c7afaed3e0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C3
          page: 2
          text_layer_sha256: 6856f5ef72eb94712498d8db36cb8690b9139122361d7b9c606844c7afaed3e0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants were 51 patients (25

          women) with focal encephalomalacia from chronic left hemi-

          sphere stroke, included regardless of language ability, but without

          comorbid neurologic or major psychiatric disease (e.g., bipolar

          disorder, dementia, epilepsy, major depression, schizophrenia).'
        anchor_text: 'Participants were 51 patients (25

          women) with focal encephalomalacia from chronic left hemi-

          sphere stroke, included regardless of language ability, but without

          comorbid neurologic or major psychiatric disease (e.g., bipolar

          disorder, dementia, epilepsy, major depression, schizophrenia).'
        excluded_fragments: []
        image_sha256: ef616d252305065223f255fed5159d863476641aba3cb750b28748bc98b9713f
        transcription: . Participants were 51 patients (25 women) with focal encephalomalacia
          from chronic left hemisphere stroke, included regardless of language ability,
          but without comorbid neurologic or major psychiatric disease (e.g., bipolar
          disorder, dementia, epilepsy, major depression, schizophrenia)
      P2-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ed4ae8ac025a6ca9862258660e6bea5ac16978e31319a28a346526f0ba44f4d2
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 246fbc769c1e70a83219ee65de9123deca4e4e76b00c8d840f7a72896862ae58
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C5
          page: 2
          text_layer_sha256: 246fbc769c1e70a83219ee65de9123deca4e4e76b00c8d840f7a72896862ae58
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants were at least 180 days poststroke, native
          English

          speakers,

          and

          premorbidly

          right-handed

          according

          to

          the

          Edinburgh Handedness Inventory.17 Estimated premorbid general

          intelligence was average according to the Barona intelligence

          quotient.18 Lesion descriptions are provided in table e-1.'
        anchor_text: 'All participants were at least 180 days poststroke, native English

          speakers,

          and

          premorbidly

          right-handed

          according

          to

          the

          Edinburgh Handedness Inventory.17 Estimated premorbid general

          intelligence was average according to the Barona intelligence

          quotient.18 Lesion descriptions are provided in table e-1.'
        excluded_fragments: []
        image_sha256: a445fcadae63ae3cb61ab782007913732f1e661d7c11129734f12e753676e358
        transcription: 'All participants were at least 180 days poststroke, native
          English

          speakers, and premorbidly right-handed according to the

          Edinburgh Handedness Inventory.17 Estimated premorbid general

          intelligence was average according to the Barona intelligence

          quotient.18 Lesion descriptions are provided in table e-1.'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'When no covariates were included in the

    analysis, ASC impairment was associated with damage

    in similar regions (figure e-1B; see table e-3 for peak

    coordinates), replicating previous results using similar

    methods.9 Notably, PN impairment was also associ-

    ated with damage in similar frontal, inferior parietal,

    and posterior STG regions (figure e-1C), consistent

    with our hypothesis that all 3 tasks require nonspecific

    executive control and phonologic processes.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
