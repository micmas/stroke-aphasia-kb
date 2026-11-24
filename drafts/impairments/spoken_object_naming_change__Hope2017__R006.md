---
id: spoken_object_naming_change
name: change in spoken object naming
kind: impairment
findings:
- id: f1
  target: written_and_action_naming_change
  target_kind: impairment
  claim: Changes in spoken object naming scores were significantly correlated with
    changes in written object naming scores and spoken action naming scores.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 28
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
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
  - The analysis focuses on the rate of change over time rather than absolute scores.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Longitudinal change in spoken object naming skills,
    calculated by subtracting the Comprehensive Aphasia Test (CAT) score at the first
    assessment (T1) from the score at the second assessment (T2) and dividing by the
    number of months between assessments. The correlation was not significant for
    auditory repetition scores. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S1-C1, two-model
    agreement, human verification pending): hemisphere (34 patients); and (v) were
    right-handed pre-stroke

    (28 patients) Original text-layer quotation is preserved below. PDF image reading
    (P1-S1-C8, two-model agreement, human verification pending): . Here, we analysed
    longitudinal change in 28 left-hemisphere stroke patients, each more than a year
    post-stroke when first assessed—testing each patient’s spoken object naming skills
    and acquiring structural brain scans twice Original text-layer quotation is preserved
    below.'
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
    - not_transcribed:sample.population
    - not_transcribed:sample.time_post_onset
    - proposed_concept:written_and_action_naming_change
  citation: '@Hope2017'
  source_passages:
  - section: Original source P8-S1-C1
    page: 8
    quote: '

      previous analyses, we found changes in the spoken object

      naming scores were signiﬁcantly correlated with changes in:

      (i) written object naming scores (r = 0.71, P 5 0.001); and

      (ii) spoken action naming scores (r = 0.67, P 5 0.001)

      (Table 1).'
    supports: claim
  - section: Original source P3-S1-C1
    page: 3
    quote: '

      hemisphere (34 patients); and (v) were right-handed pre-stroke

      (28 patients).'
    supports: sample
  - section: Original source P4-S1-C4
    page: 4
    quote: 'Behavioural changes over time were

      calculated by subtracting the scores at T1 from the scores at

      T2 for each task, and dividing the result by the months

      between T1 and T2.'
    supports: method
  - section: Original source P1-S1-C8
    page: 1
    quote: 'Here, we analysed longitudinal change in 28 left-hemisphere stroke patients,
      each more than a year post-stroke when ﬁrst

      assessed—testing each patient’s spoken object naming skills and acquiring structural
      brain scans twice.'
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: 'Behavioural data

      Each patient was assessed (twice) using the CAT (Swinburn,

      2004).'
    supports: method
  - section: Original source P8-S1-C2
    page: 8
    quote: 'In contrast, the correlation between spoken

      object naming and auditory repetition scores was not sig-

      niﬁcant (r = 0.04, P = 0.83).'
    supports: confounders
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hope2017
  proposal_id: R006
  review_status_sha256: ec3cca1865f88327d33162494a87a9ea9ac14af9aeb65e94ca83be49d154a5fc
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
        A/passages.json: 0ea1c984da5c13cc97beedc76859bf64fe536ebfff83771ec3be3cb7dbbfe297
        A/raw.json: a397c6a2814df81ec32f171468f4555887e31ea967a991ed9c09a2ba0e416c44
        A/source-units.json: e12a2566552cdf0aaa3086280d1d3f6f1aa946f9dea170df01c2864ba7401949
        A/full-source-units.json: 7e2ea6bcc3f01b5218de886a00103362db8fe1a064e0af838ea158d9c9ae17f0
        A/meta.json: 7c10996ce8f13b0d181dda6f9400ac5e852790a6b3ce07f8a9d6d9724c09b4ff
        A/table-images/TABLE-1-page-3-1.png: 407d51d599f943017e4c78e007be1d7b0b8a4a1e5941630de368fd275033436b
        A/table-images/page-3.png: 07f396f717aeb559a3a46b625f02375a2d9378373b03e238d6bc813406d8f420
        A/table-images/manifest.json: 899c1792edca2ec84ccb07dbee1e39fb399a32cfdae0ac1ae94acd654c41b03b
        A/clauses/window-03/raw.json: 119caf164d3c242bcba579a8d82d6d1825cef03d6f372f56c12a69269bc357ee
        A/clauses/window-03/prompt.txt: 2a060f43b86992c1995dd86981ad4e95d6242819d6a011dd4d3bd33237540234
        A/clauses/window-03/meta.json: ee352eaa1c9ad75aeaea79fb6051a883c038b22dec53155fc70f399035cb994a
        A/clauses/window-04/raw.json: 9d92330482fc6ac82a0ddcbc0df19cbbd7736c4b0f170c40398733e81baa14eb
        A/clauses/window-04/prompt.txt: a2a22bd8b442acbfd0f5121434a5b8fba78f60ab4e14d264d2e7718f0a276ce1
        A/clauses/window-04/meta.json: 3e41b8c1be0f93d9ad3822359891a5cf1c44cc9043da89c261053327f507a77b
        A/clauses/window-05/raw.json: eb1782c44c0130f53e6c7658116ce2198d3f00a518090cb31b1d973b78374467
        A/clauses/window-05/prompt.txt: 7cab69c7893bdd522673f91d5730ab86c57384ee757a0f65ca853c537ae34223
        A/clauses/window-05/meta.json: e8303af93e3fe9540a2de0b0310bc433ac41bda1d75891906b610d76f3b4e423
        A/clauses/window-02/raw.json: 2db8b2da31bc8c01d4e3ba4060c14b93827b8d41e19699dbeb5e746182407b15
        A/clauses/window-02/prompt.txt: 566819b58a222c9b1e4c08364aef4679ede8bffa167501bbdcb771bd19049797
        A/clauses/window-02/meta.json: 971536fcfaa0d3afa18e00d395b82cad3fdcbd5b57c88a1ee9ce9b00f572eeac
        A/clauses/window-07/raw.json: c8592fc9d6f410c8ea980c68c7bb79130c4440eb28aed4eeeda8354deaac7925
        A/clauses/window-07/prompt.txt: 36d66b4dc69a9e96936a00b2d0d001b034113ba7ca5854731e40a0b280e876dd
        A/clauses/window-07/meta.json: fd06974ccee26e0c9b5edebbf4559c379ac9d08858adc5da0e10c3d0687c7580
        A/clauses/window-01/raw.json: e3ba2ef49670c9aed14eb699ef5b77ff8d296258ae077a2ad75d39be9b564eaf
        A/clauses/window-01/prompt.txt: 62b4ad79d1f4aeac46c4e030662ae06720368dbc245448047091e7a42c038b59
        A/clauses/window-01/meta.json: 98499e8375b9e3413e6281fb3285f0a01283a18a1d8e9caa798b4f44ac7a5011
        A/clauses/window-06/raw.json: c9ae5677a13e050d26e2c75c030ca1b2032b6cfaa50a23c75c412316d1b4decf
        A/clauses/window-06/prompt.txt: 646df8c720a98d36c75b0f5e3ddb01c04ed8fd8b79bb297adcd17d1b4fea3902
        A/clauses/window-06/meta.json: 23807c8300467c1657f58ea8c151c8db34dbea0f6ceab0499baaf9e0fca9a67d
        A/clauses/window-08/raw.json: 95756ae403a497dc5a2ae67dc0d7416ea6a9723e10de7fd352e2fa45d03836b9
        A/clauses/window-08/prompt.txt: f5a0fa3bf793281104c37e3b3415be6d6dd78325f7232535da2c999d0535d462
        A/clauses/window-08/meta.json: de207ea378d3dbf88483fd4c95d54e60bfd678cc512279071df505526e2f6a7f
        A/tables/TABLE-1-page-3-1/raw.json: 14859778c9e16f2522543541af2758f6c98b58a4b73985fff4eadab44285e807
        A/tables/TABLE-1-page-3-1/prompt.txt: 1dba7829ff85182dfdb043ef952562b60f956dd3513599f9eba855f26d4a19ca
        A/tables/TABLE-1-page-3-1/meta.json: 7e6ae4973373b033f0aa6a8e4605d6b70ad941af422c1996840e700ff4e101c3
        B/passages.json: 0ea1c984da5c13cc97beedc76859bf64fe536ebfff83771ec3be3cb7dbbfe297
        B/raw.json: 44ba03c5e48e830bab065ee41a6a6dd98e9d92b092f42e6d55aa4b9d3640b291
        B/source-units.json: e12a2566552cdf0aaa3086280d1d3f6f1aa946f9dea170df01c2864ba7401949
        B/full-source-units.json: 7e2ea6bcc3f01b5218de886a00103362db8fe1a064e0af838ea158d9c9ae17f0
        B/meta.json: 46dd0ade6926aef58553853f832c847d7132d90f47490ff0e59fd47a2012350d
        B/table-images/TABLE-1-page-3-1.png: 407d51d599f943017e4c78e007be1d7b0b8a4a1e5941630de368fd275033436b
        B/table-images/page-3.png: 07f396f717aeb559a3a46b625f02375a2d9378373b03e238d6bc813406d8f420
        B/table-images/manifest.json: 4363bd0c6b1ddcf17c776d0071f3e2ebd23cc7accb933bd1521e532600cc1709
        B/clauses/window-03/raw.json: c04a0d1f69c36edb4697227439dafa3d7e5c83403f2054a987e02b1ca56e6d60
        B/clauses/window-03/prompt.txt: 2a060f43b86992c1995dd86981ad4e95d6242819d6a011dd4d3bd33237540234
        B/clauses/window-03/meta.json: a3c09f91e34f11c87aadb1f75c95dc1279c85e31a507638fa8a94ced4a21ea4e
        B/clauses/window-04/raw.json: b0616239cf74035045fcaf563b01f44c3691122c567fb956674697865b5c5fb9
        B/clauses/window-04/prompt.txt: a2a22bd8b442acbfd0f5121434a5b8fba78f60ab4e14d264d2e7718f0a276ce1
        B/clauses/window-04/meta.json: 0f1b229f04d5f543dd91b6fe6bce0c0d953d32545e400c489de4a03d2ee3c462
        B/clauses/window-05/raw.json: 124450b6413010d7b60d9315cc0d8516ba755ebd94e7ab49adddabc892ee8af2
        B/clauses/window-05/prompt.txt: 7cab69c7893bdd522673f91d5730ab86c57384ee757a0f65ca853c537ae34223
        B/clauses/window-05/meta.json: c5ce7128feb17e6d6d0ddf05c42b1158225661d3dca9135b6b5eec746e753ce2
        B/clauses/window-02/raw.json: 58cfdec7b7b688714b80b64e2c5fe93cee283b4cd7fb9161eafa7729c48524dd
        B/clauses/window-02/prompt.txt: 566819b58a222c9b1e4c08364aef4679ede8bffa167501bbdcb771bd19049797
        B/clauses/window-02/meta.json: 600f4a34803df742e7761ec0c17d75b8a4b3c4399d4dc797afdb88115150c6d6
        B/clauses/window-07/raw.json: 2f2b49e1b3d6330cb88aacc01cbb9bc415f737c0a427b8f3be4f8459fe40b56e
        B/clauses/window-07/prompt.txt: 36d66b4dc69a9e96936a00b2d0d001b034113ba7ca5854731e40a0b280e876dd
        B/clauses/window-07/meta.json: eee40220fe4fb89256c391de345501253b7b0aa3472ad951c86381f6da874999
        B/clauses/window-01/raw.json: 492fe0c80b85db851b14beec70202fe5cb73f96fd8abac2baeebf785dc23c603
        B/clauses/window-01/prompt.txt: 62b4ad79d1f4aeac46c4e030662ae06720368dbc245448047091e7a42c038b59
        B/clauses/window-01/meta.json: af4e87fb05f4b6c7e04c56d68490c730a319c1f759a22715b8bbb3857a3c866b
        B/clauses/window-06/raw.json: 1dc433d77853ad93187820cf150eedd163192b43fddfa091a4817e7f2fd6142a
        B/clauses/window-06/prompt.txt: 646df8c720a98d36c75b0f5e3ddb01c04ed8fd8b79bb297adcd17d1b4fea3902
        B/clauses/window-06/meta.json: bc51eec885ed9dc8b06f2b428048e7ab3a6d1709980c167f2871430c36648f03
        B/clauses/window-08/raw.json: f37187763af1722627061e967e24a9c13dce944a37c21a82d8de264acc6564c9
        B/clauses/window-08/prompt.txt: f5a0fa3bf793281104c37e3b3415be6d6dd78325f7232535da2c999d0535d462
        B/clauses/window-08/meta.json: b42f3cc462e8cc6730f99ed87fba47d79ff2c29a78be44de445b506fc9caade5
        B/tables/TABLE-1-page-3-1/raw.json: acdd53b9920faf5b59d9232e8587ffb6688e76f51fcc58bbf0a57a58b5451bf0
        B/tables/TABLE-1-page-3-1/prompt.txt: 1dba7829ff85182dfdb043ef952562b60f956dd3513599f9eba855f26d4a19ca
        B/tables/TABLE-1-page-3-1/meta.json: 8c433a82a7a5f69415dafa660486cb015bf89b31b50be718266feb1919b22289
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
      pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
      source_review: _compare/relationships-2026-11-16/review-current/Hope2017
      source_status_sha256: b136dab0155c9046dacecdf7e36e1fc7fbff14930d4737dd90c6f85abef67c9b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: change in spoken object naming scores
    outcome:
      text: change in written object naming and spoken action naming scores
    analysis_label: Task correlation analysis
    relation: association
    evidence_ids:
    - P8-S1-C1
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
      pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
      source_review: _compare/relationships-2026-11-16/review-current/Hope2017
      source_status_sha256: b136dab0155c9046dacecdf7e36e1fc7fbff14930d4737dd90c6f85abef67c9b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C7
      - Accounting without a linked unit P5-S2-C5
      - Unaccounted source passage P5-S2-C5
      - Result passage disposed without unit P5-S2-C7
      - Result passage disposed without unit P5-S2-C8
      - Accounting without a linked unit P5-S3-C2
      - Accounting without a linked unit P5-S3-C3
      - Accounting without a linked unit P5-S3-C4
      - Unaccounted source passage P5-S3-C4
      - Unaccounted source passage P5-S3-C3
      - Unaccounted source passage P5-S3-C2
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P8-S2-C7
      - Accounting without a linked unit P8-S2-C8
      - Result passage disposed without unit P8-S2-C9
      - Accounting without a linked unit P9-S1-C4
      - Result passage disposed without unit P9-S1-C5
      - Result passage disposed without unit P9-S1-C7
      - Unaccounted source passage P9-S1-C4
      - Unaccounted source passage P8-S2-C8
      - Result passage disposed without unit P9-S2-C10
      - Result passage disposed without unit P10-S1-C2
      unattached_null_or_qualifier_ids:
      - P5-S1-C7
      - P7-S1-C8
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 145
      unselected_timing_passages:
      - P1-S1-C8
      - P2-S3-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P4-S3-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S3-C1
      - P2-S3-C2
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P8-S1-C11
      table_review_required:
      - TABLE-1-page-3-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S2
        - P5-S3
        - P6-S1
        - P6-S2
        - P7-S2
        - P8-S1
        - P8-S3
        - P9-S1
        - P10-S1
        - P10-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
      source_review: _compare/relationships-2026-11-16/review-current/Hope2017
      source_status_sha256: b136dab0155c9046dacecdf7e36e1fc7fbff14930d4737dd90c6f85abef67c9b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Abstract statement of brain-behaviour association.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies peak clusters in anterior temporal lobe and precentral gyrus.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: fMRI results in controls for naming vs semantic decisions.
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 7
      reason: Correlation between spoken object naming and other tasks.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Comparison of written object naming vs auditory repetition.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Direction of effect for anterior temporal vs precentral gyrus.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient exclusion/inclusion regarding scan timing.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Defines the Bayes factor criterion for decisive evidence.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains Frequentist equivalent of the Bayesian analysis.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Group-level main effect of change (null).
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive results of therapy experience.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal report of a single patient.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports five clusters surviving correction in VBM.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies positive clusters in right middle temporal gyrus.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies peak negative cluster in right precentral gyrus.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Positive-only cross-validation performance (r=0.88).
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Negative-only cross-validation performance (r=0.46).
    - source_id: P6-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Sensitivity results after excluding specific patients.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Summary of VBM clusters (positive and negative).
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of predictability given structural adaptation.
    - source_id: P7-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: General summary of systematic changes.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Bayes factors for predictability of improvements vs declines.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: fMRI activation of peak clusters during naming.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Null activation in semantic decision task.
    - source_id: P7-S2-C11
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of cross-validation significance.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Correlation between spoken object naming and written/action naming.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Null correlation with auditory repetition.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Comparison of written naming vs auditory repetition correlations.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: VBM association with naming tasks and null for repetition.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Comparison of VBM effects for written naming vs repetition.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Null differences in demographics between improvers and decliners.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Null differences in age, time post-stroke, volume, and sex.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Null effect of damage to left homologue of peak negative cluster.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Null VBM association with T1 grey matter (whole brain).
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 14
      reason: Null association with T1 grey matter in peak clusters.
    - source_id: P8-S2-C6
      disposition: repeated
      result_indexes:
      - 12
      - 13
      - 14
      reason: Summary of lack of T1 predictors.
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of group-level stability.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation between task scores and time post-stroke.
    - source_id: P8-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion of dichotomy of improving/declining skills.
    - source_id: P8-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Restatement of predictability and systematicity.
    - source_id: P8-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that changes are not measurement noise.
    - source_id: P8-S3-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of structural adaptation in right hemisphere.
    - source_id: P8-S3-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that changes are not measurement noise.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 6
      - 9
      reason: Restatement of correlated change and VBM overlap.
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of fMRI results in controls.
    - source_id: P9-S1-C11
      disposition: repeated
      result_indexes:
      - 8
      - 11
      reason: Restatement of written naming vs repetition effects.
    - source_id: P9-S2-C1
      disposition: repeated
      result_indexes:
      - 8
      - 11
      reason: Restatement of written naming vs repetition effects.
    - source_id: P9-S2-C2
      disposition: repeated
      result_indexes:
      - 8
      reason: Conclusion that change is driven by word-finding skills.
    - source_id: P9-S3-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of adaptation in chronic phase.
    - source_id: P9-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of hypertrophy as functional enhancement.
    - source_id: P9-S3-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of positive vs negative cluster effects.
    - source_id: P9-S3-C10
      disposition: repeated
      result_indexes:
      - 12
      - 13
      - 14
      reason: Restatement of lack of T1 predictors.
    - source_id: P9-S4-C1
      disposition: repeated
      result_indexes:
      - 12
      - 13
      - 14
      reason: Restatement of lack of T1 predictors.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of missing therapy data.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on inability to explain why changes occur.
    unresolved_coverage:
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S2-C6
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C10
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C15
    - P1-S2-C2
    - P1-S2-C4
    - P3-S1-C3
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C5
    - P5-S2-C7
    - P5-S2-C8
    - P5-S3-C3
    - P5-S3-C4
    - P6-S1-C4
    - P7-S1-C1
    - P7-S1-C2
    - P7-S2-C4
    - P7-S2-C11
    - P8-S1-C11
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C10
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C7
    - P9-S1-C11
    - P9-S2-C10
    - P9-S3-C4
    - P9-S3-C5
    - P9-S3-C6
    - P9-S3-C7
    - P9-S3-C10
    - P10-S1-C2
    - P10-S1-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C4
      recruited_sample:
      - P2-S3-C1
      eligibility:
      - P2-S3-C2
      - P2-S3-C6
      - P4-S2-C2
      imaging_provenance:
      - P4-S1-C12
      - P5-S1-C8
      imaging_timing:
      - P3-S1-C4
      - P4-S1-C9
      outcome_timing:
      - P4-S1-C4
      - P4-S1-C9
      - P4-S1-C10
      outcome_definition:
      - P4-S1-C4
      - P4-S1-C10
      - P5-S3-C1
      validation:
      - P4-S3-C4
      - P5-S3-C7
      analysis_restrictions:
      - P4-S2-C9
      - P5-S2-C3
      - P7-S2-C3
      dependent_variable_statement:
      - P4-S2-C7
      - P5-S3-C1
      - P6-S1-C1
      - P7-S1-C6
      limitations:
      - P10-S1-C1
      - P10-S1-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C7
      - P5-S3-C1
      - P8-S2-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C4
      - P8-S2-C2
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: validation
      source_id: P4-S3-C8
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
      pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
      review_sha256: ec3cca1865f88327d33162494a87a9ea9ac14af9aeb65e94ca83be49d154a5fc
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
      - P8-S1-C1
      source_result: Changes in spoken object naming scores were significantly correlated
        with changes in written object naming scores (r = 0.71, P < 0.001) and spoken
        action naming scores (r = 0.67, P < 0.001). In contrast, the correlation with
        auditory repetition scores was not significant (r = 0.04, P = 0.83).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R006) corresponds to the behavioral correlation
            analysis described in P8-S1-C1, which tests the association between change
            in spoken object naming and other language tasks (written object naming,
            spoken action naming). This is distinct from the VBM analysis (brain-behavior
            correlation) or cross-validation analysis.
          source_ids:
          - P8-S1-C1
          - P7-S2-C8
        direction:
          answer: fits
          reason: The source explicitly states that changes in spoken object naming
            were 'significantly correlated' with changes in written object naming
            and spoken action naming. The proposed claim preserves this detected association.
            The direction is positive (implied by the context of shared word-finding
            deficits and the positive r-values in the source, though the specific
            sign is not in the OCR text, the 'significant correlation' is the key
            detected status).
          source_ids:
          - P8-S1-C1
        construct:
          answer: fits
          reason: The exposure is 'change in spoken object naming scores' and the
            outcome is 'change in written object naming and spoken action naming scores'.
            The source P8-S1-C1 confirms these exact variables. The measurement is
            behavioral (CAT scores), not imaging-based, so 'non_imaging' is the correct
            patient measurement type for this specific analysis.
          source_ids:
          - P8-S1-C1
          - P3-S1-C10
          - P3-S1-C11
        qualifications:
          answer: fits
          reason: The proposed draft includes the qualification that the correlation
            was not significant for auditory repetition scores. This matches P8-S1-C2,
            which states 'the correlation between spoken object naming and auditory
            repetition scores was not significant'. This is a material qualifier that
            distinguishes the word-finding interpretation from an articulation interpretation.
          source_ids:
          - P8-S1-C2
          - P8-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The draft correctly identifies the significant correlations and
            the null result for auditory repetition. No other material caveats regarding
            this specific behavioral correlation analysis are omitted. The population
            and timing are marked as pending, which is appropriate given the instruction
            not to infer completeness, but the core relationship is faithful.
          source_ids:
          - P8-S1-C1
          - P8-S1-C2
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: Right-handed left-hemisphere stroke patients with English as their
        first language and lesions at least 1 cm3 in the left hemisphere and no more
        than 1 cm3 in the right hemisphere.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1'
    - field: sample.time_post_onset
      original: Chronic phase; all patients were more than 1 year post-stroke at first
        assessment.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1'
    analysis_identity:
      id: R006
      exposure:
        text: change in spoken object naming scores
      outcome:
        text: change in written object naming and spoken action naming scores
      analysis_label: Task correlation analysis
      relation: association
      evidence_ids:
      - P8-S1-C1
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
        pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
        source_review: _compare/relationships-2026-11-16/review-current/Hope2017
        source_status_sha256: b136dab0155c9046dacecdf7e36e1fc7fbff14930d4737dd90c6f85abef67c9b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P8-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f83c279dbc2721ec95cffe706471e45c3d2c778dad1358b323d3358b18f4fcbd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C1
          page: 8
          text_layer_sha256: a4594d088cd37ca97db78cb33840921ea6a13a4f1b6bd3585fe45f289d2a874f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: '

          previous analyses, we found changes in the spoken object

          naming scores were signiﬁcantly correlated with changes in:

          (i) written object naming scores (r = 0.71, P 5 0.001); and

          (ii) spoken action naming scores (r = 0.67, P 5 0.001)

          (Table 1).'
        anchor_text: 'previous analyses, we found changes in the spoken object

          naming scores were signiﬁcantly correlated with changes in:

          (i) written object naming scores (r = 0.71, P 5 0.001); and

          (ii) spoken action naming scores (r = 0.67, P 5 0.001)

          (Table 1).'
        excluded_fragments: []
        image_sha256: 0d42165fad9abc75228150e2a43b56f06d039f453e4c9a0e42d9f2cb66b99116
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a220b185f6d340a93a16bbce2f6c13becf4c75a5d05c3f79d2cd329bf9e926df
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: e35ce647b40442348c386e275d50113a0bca1a64701459de0adc27fcbe882fca
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '

          hemisphere (34 patients); and (v) were right-handed pre-stroke

          (28 patients).'
        anchor_text: 'hemisphere (34 patients); and (v) were right-handed pre-stroke

          (28 patients).'
        excluded_fragments: []
        image_sha256: 8188ba57887eebd9675f27b7cc8e1f86e3747a6f525436c4e1fde680257e1a03
        transcription: 'hemisphere (34 patients); and (v) were right-handed pre-stroke

          (28 patients)'
      P1-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fe88864b0eb968fc792eff3681e9034043eda09fc36ea0b06056e1b3e3712c3d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5917eb9fc326cd0b655b8898699498baed879b69086091a9955df2d38aac5d0f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C8
          page: 1
          text_layer_sha256: 5917eb9fc326cd0b655b8898699498baed879b69086091a9955df2d38aac5d0f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Here, we analysed longitudinal change in 28 left-hemisphere
          stroke patients, each more than a year post-stroke when ﬁrst

          assessed—testing each patient’s spoken object naming skills and acquiring
          structural brain scans twice.'
        anchor_text: 'Here, we analysed longitudinal change in 28 left-hemisphere
          stroke patients, each more than a year post-stroke when ﬁrst

          assessed—testing each patient’s spoken object naming skills and acquiring
          structural brain scans twice.'
        excluded_fragments: []
        image_sha256: 3e032680931cc7ebbead52167bee2f278d62e33b967c0edf9bd6fb01d9d748fd
        transcription: . Here, we analysed longitudinal change in 28 left-hemisphere
          stroke patients, each more than a year post-stroke when first assessed—testing
          each patient’s spoken object naming skills and acquiring structural brain
          scans twice
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: '

    previous analyses, we found changes in the spoken object

    naming scores were signiﬁcantly correlated with changes in:

    (i) written object naming scores (r = 0.71, P 5 0.001); and

    (ii) spoken action naming scores (r = 0.67, P 5 0.001)

    (Table 1).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
