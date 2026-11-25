---
id: disconnection_model_fluency_naming
name: disconnection model
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: ambiguous_or_composite
    original_target: fluency_and_naming_scores
    reason: A score, generic outcome or composite label does not uniquely identify a behaviour. Check the
      task, subtests and analysis before retargeting.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Comprehensive Aphasia Test
      subtest: Category/letter fluency and object/action naming
    metric: Separate CAT fluency and naming T scores
    definition_source:
      citation: '@Hope2016'
      page: 2
      quote: 'Following the emphasis, in Marchina et al. (2011), on fluency and naming skills, our analysis
        focuses on T-scores assigned in the fluency and naming portions of the CAT. The fluency tests summarise
        scores on two sub-tests. In the first test, patients are asked to name as many animals as they can
        in one minute (i.e. a test of category fluency), and in the second test, patients are asked to say
        as many words as they can beginning with the letter ‘S’ in one minute (i.e. a test of letter fluency):
        scores are based on the number of correct utterances given. There are also two sub-tests in the
        naming assessment: in the first, patients must name each of 24 line drawings (pictures) of common
        ob- jects, and in the second, they name 5 pictures depicting common actions (e.g. ‘eating’).'
      basis: Main paper methods checked directly
      source_pdf: C5206_Hope2016.pdf
      source_pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
    note: Measurement metadata identified from source evidence; finding remains unapproved.
  target: fluency_and_naming_scores
  target_kind: impairment
  claim: The disconnection model explains a significantly greater proportion of the
    variance in fluency and naming scores than the lesion load model, and provides
    strong evidence of being the better model of the data.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: Patients with chronic left hemisphere stroke
    phase: not_reported
    time_post_onset: At least 12 months post-stroke at assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Reference tract templates were derived from a younger population (18-22 years)
    than the patient sample
  - The study does not claim this specific measure of disconnection is the only or
    best possible measure
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A prediction model consisting of binary indicators
    of whether the arcuate fasciculus and uncinate fasciculus were disconnected (severed)
    by the patient''s lesion, combined with total lesion volume; disconnection was
    determined by subtracting the patient''s binary lesion from reference tract templates
    and identifying if the tract remained a single connected object. The disconnection
    model includes binary predictors for disconnection of the arcuate and uncinate
    fascicles and total lesion volume; The lesion load model includes continuous predictors
    for lesion load in the same two fascicles and total lesion volume; Adding disconnection
    data to the lesion load model significantly improved variance explained, whereas
    adding lesion load data to the disconnection model did not. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S2-C3, two-model agreement, human verification pending): . Patients
    were excluded

    if they: (a) were left handed or ambidextrous prior to their stroke;

    (b) were <12 months post-stroke at assessment; (c) had evidence of

    other significant neurological conditions (e.g. dementia, multiple sclero-

    sis); (e) did not speak English as a first language; (f) had suffered

    right or bilateral lesions, as assessed by a neurologist (APL), using the

    patients'' raw T1-weighted scans; or (g) had suffered dispersed rather

    than focal damage Original text-layer quotation is preserved below. PDF image
    reading (P5-S1-C4, two-model agreement, human verification pending): Another reason
    for caution stems from the age difference between

    our patient population, and the participants used to derive the tract im-

    ages (18–22 years: (Thiebaut de Schotten et al., 2011)) Original text-layer quotation
    is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:fluency_and_naming_scores
  citation: '@Hope2016'
  source_passages:
  - section: Original source P4-S2-C5
    page: 4
    quote: 'Both models explain a signiﬁcant proportion of the variance in both

      of the two language scores, though the lesion load model (ﬂuency:

      R2 = 0.25, p b 0.001; naming: R2 = 0.31, p b 0.001) explains slightly

      less than the disconnection model (ﬂuency: R2 = 0.29, p b 0.001; nam-

      ing: R2 = 0.35, p b 0.001).'
    supports: claim
  - section: Original source P4-S2-C2
    page: 4
    quote: 'The lesion load model

      includes two continuous predictors for lesion load in the arcuate and

      uncinate fascicles, whereas the disconnection model includes two bina-

      ry predictors for disconnection of the same two fascicles.'
    supports: method
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Both models

      also include lesion volume.'
    supports: method
  - section: Original source P4-S3-C2
    page: 4
    quote: 'Following the convention proposed by Jeffreys (1961), this is

      ‘strong’ evidence (i.e. ratio N 10) in favour of the tract disconnection

      model over the lesion load model for both language skills.'
    supports: claim
  - section: Original source P2-S2-C7
    page: 2
    quote: 'A total of 142 patients met

      these criteria, 58 women and 84 men (age at onset: mean = 52.1

      years, standard deviation = 13.2 years; time post-stroke: mean =

      74.1 months; standard deviation = 80.0 months).'
    supports: sample
  - section: Original source P2-S2-C3
    page: 2
    quote: 'Patients were excluded

      if they: (a) were left handed or ambidextrous prior to their stroke;

      (b) were b12 months post-stroke at assessment; (c) had evidence of

      other signiﬁcant neurological conditions (e.g. dementia, multiple scle-

      rosis); (e) did not speak English as a ﬁrst language; (f) had suffered

      right or bilateral lesions, as assessed by a neurologist (APL), using the

      patients'' raw T1-weighted scans; or (g) had suffered dispersed rather

      than focal damage.'
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Moreover, the variance explained improves

      signiﬁcantly when disconnection data is added to the lesion load

      model (ﬂuency: R2 change = 0.05, p = 0.007; naming: R2 = 0.04,

      p = 0.019), but not when lesion load data is added to the disconnection

      model (ﬂuency: R2 change = 0.006, p = 0.56; naming: R2 change =

      0.007, p = 0.47).'
    supports: claim
  - section: Original source P5-S1-C4
    page: 5
    quote: 'Another reason for caution stems from the age difference between

      our patient population, and the participants used to derive the tract im-

      ages (18–22 years: (Thiebaut de Schotten et al., 2011)).'
    supports: limitation
predictor_type: imaging_metric
short_definition: A prediction model consisting of binary indicators of whether the
  arcuate fasciculus and uncinate fasciculus were disconnected (severed) by the patient's
  lesion, combined with total lesion volume; disconnection was determined by subtracting
  the patient's binary lesion from reference tract templates and identifying if the
  tract remained a single connected object.
assessment:
- Comprehensive Aphasia Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hope2016
  proposal_id: R006
  review_status_sha256: 047898022b284c12bbece1baa93839d961bbb32dd56e622dcdce1b4bb3b0a101
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
        A/passages.json: b7bab1f6de679eef7a4bbb54fc7db6871193551ad580ceb3f2e2bfe205131f41
        A/raw.json: f99f47d141eb3c5b515e97f984df91b0221ae810596640fb7ac1b51054adda78
        A/source-units.json: 1945fe4b0e74e721cf66fdb146ef49859f51ec90692116581ff4ff081df05519
        A/full-source-units.json: 93d500f36ca677ecf6575f1c1d090fc8bdae13d937aba6347c575795545c8b1d
        A/meta.json: aea96945f27875a388d2bc47f8f4a70e68ef7b5583c27936d9dac5e74fcd1c12
        A/table-images/manifest.json: 4ff7cb6561949a51d3fb4132daed366442e34e957806dc91d35653f5391a829c
        A/clauses/window-03/raw.json: 5b511cee0e0890f22266005096cdda79d901af48931528d1931dbb4659bc483a
        A/clauses/window-03/prompt.txt: 681da849a26a974011b4056f12fafaf973e27e21513b27bd3d682e7c5438e63c
        A/clauses/window-03/meta.json: d708f5c56a26af842077863ba300f2b1d8552d79bdbbee114beb4fcd49689fcf
        A/clauses/window-04/raw.json: 2bcbd517265b0a0717aa2fa8ff405d19b286b3d512d12260812493e9589acaa8
        A/clauses/window-04/prompt.txt: e0961b76a994dc4aaa29350bb787988c33eb9e34f099877e71a05a5eed51be52
        A/clauses/window-04/meta.json: 578dc1a443f70145bd17be5bdceacfcfcd835e3097ee18c3991ed0591adfdc87
        A/clauses/window-05/raw.json: 4882668894e6054adcafe9e3e88b162fc93157748a888058a86c1fa722c5c9c1
        A/clauses/window-05/prompt.txt: 371b3cc81c74ff102072b3251a3d9e71ece292a37b9be4be70922fc34b656200
        A/clauses/window-05/meta.json: b90ebe8287d8c2ec1b2fcd3a3d668a2009228fcd80635cfb10fe4e1309cbe6b9
        A/clauses/window-02/raw.json: e5fae3e25046c677b1409adfea9b36247fde89ad3a16f858d687af31dae8b719
        A/clauses/window-02/prompt.txt: 2f09e5d09e7fa8ea8bfebe79b638614cf95e7dc763c117e6c475e5b570773995
        A/clauses/window-02/meta.json: 90cc75d5001e971853ee8319dc89490c1b9de302d08b3e383c25d61c52b94bb0
        A/clauses/window-01/raw.json: db3f829227977f703ad266c099a2b003ac27a25973087f4d9d58adcc2357a429
        A/clauses/window-01/prompt.txt: dc126a1e039a18276d078f784010e8f3a78705e0f880f3d352f8570108c3b737
        A/clauses/window-01/meta.json: b1166280829d0a3a85af0ca06b60f78871d4a5a703d4a18441065e9a571b5228
        B/passages.json: b7bab1f6de679eef7a4bbb54fc7db6871193551ad580ceb3f2e2bfe205131f41
        B/raw.json: 1de0a4b352b4d92cfa750e9ce1411468c840825e67a477823e5ab40d0a886333
        B/source-units.json: 1945fe4b0e74e721cf66fdb146ef49859f51ec90692116581ff4ff081df05519
        B/full-source-units.json: 93d500f36ca677ecf6575f1c1d090fc8bdae13d937aba6347c575795545c8b1d
        B/meta.json: e234d06eac771ad341bc0f7200dfb6aca5d3b1878e6838738305b7913c4a7d76
        B/table-images/manifest.json: 4ff7cb6561949a51d3fb4132daed366442e34e957806dc91d35653f5391a829c
        B/clauses/window-03/raw.json: 047d6d4dabd763ba5f2f3a9b7c691149c11a94b7e406db82936c0c99b4600579
        B/clauses/window-03/prompt.txt: 681da849a26a974011b4056f12fafaf973e27e21513b27bd3d682e7c5438e63c
        B/clauses/window-03/meta.json: 3b17de200426e064953a0b925ea809269823201a8e03ed234d3cb7d9b2e757be
        B/clauses/window-04/raw.json: 4663482ee94796333f04de437bc39947d4016332eaadf26ae761ea457413f1ec
        B/clauses/window-04/prompt.txt: e0961b76a994dc4aaa29350bb787988c33eb9e34f099877e71a05a5eed51be52
        B/clauses/window-04/meta.json: 0fc4475d3fee8c7288e374fe74d7148a44b93cc3c1caf78a04ee018c3738f50c
        B/clauses/window-05/raw.json: 4710468247f3f9ae0f858bbaa85276ed6c805dcf9db75a2c46ce6b9846e3b608
        B/clauses/window-05/prompt.txt: 371b3cc81c74ff102072b3251a3d9e71ece292a37b9be4be70922fc34b656200
        B/clauses/window-05/meta.json: e5fac2e063ee38ea28f953ff06617bf70d4b009395280010be738fa448d87444
        B/clauses/window-02/raw.json: 14493f02ee30309ab390f5a9779c218a5d0fdd05c33a6563aedcd0842a98301e
        B/clauses/window-02/prompt.txt: 2f09e5d09e7fa8ea8bfebe79b638614cf95e7dc763c117e6c475e5b570773995
        B/clauses/window-02/meta.json: 768968215f55dfdbd7d3b1d39088ea89907c627eb332d1b770b839dcf19358af
        B/clauses/window-01/raw.json: 54f0577a70df6e2c6777a24847073b65fb8124feaa6b44c6ad5a510b39f55a74
        B/clauses/window-01/prompt.txt: dc126a1e039a18276d078f784010e8f3a78705e0f880f3d352f8570108c3b737
        B/clauses/window-01/meta.json: dd7a00b6b9300c714dfa02e5c49d1372069e1341f2bc6bf151b05cfd7a23a43b
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
      pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
      source_review: _compare/relationships-2026-11-16/review-current/Hope2016
      source_status_sha256: 5cd97f9a8a93eccb9f40cc5a2bbe6d4614fd5e0cc0c99f58d2e6143eac1102cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: disconnection model (arcuate/uncinate disconnection and lesion volume)
    outcome:
      text: fluency and naming scores
    analysis_label: Analysis 3
    relation: performance
    evidence_ids:
    - P4-S2-C5
    qualifier_ids:
    - P4-S2-C2
    - P4-S2-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
      source_review: _compare/relationships-2026-11-16/review-current/Hope2016
      source_status_sha256: 5cd97f9a8a93eccb9f40cc5a2bbe6d4614fd5e0cc0c99f58d2e6143eac1102cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C10'
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C9
      - Accounting without a linked unit P1-S2-C9
      - Unaccounted source passage P1-S1-C9
      - Unaccounted source passage P1-S2-C9
      - Accounting without a linked unit P2-S3-C11
      - Accounting without a linked unit P3-S1-C7
      - Accounting without a linked unit P3-S1-C8
      - Accounting without a linked unit P3-S2-C1
      - Accounting without a linked unit P3-S2-C2
      - Unaccounted source passage P3-S1-C7
      - Unaccounted source passage P3-S1-C8
      - Unaccounted source passage P3-S2-C1
      - Unaccounted source passage P2-S3-C11
      - Unaccounted source passage P3-S2-C2
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S2-C10
      - Accounting without a linked unit P4-S2-C5
      - Accounting without a linked unit P4-S2-C6
      - Accounting without a linked unit P4-S2-C7
      - Accounting without a linked unit P4-S2-C9
      - Accounting without a linked unit P4-S3-C2
      - Unaccounted source passage P4-S2-C5
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S3-C2
      - Unaccounted source passage P4-S2-C9
      - Unaccounted source passage P4-S2-C10
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S2-C6
      - Result passage disposed without unit P5-S1-C6
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P5-S2-C4
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C3
      unattached_null_or_qualifier_ids:
      - P3-S1-C8
      - P4-S1-C8
      - P5-S1-C8
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 98
      unselected_timing_passages:
      - P2-S2-C3
      - P2-S2-C7
      - P4-S3-C3
      - P5-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P1-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S3
        - P2-S4
        - P3-S1
        - P3-S2
        - P4-S4
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
      source_review: _compare/relationships-2026-11-16/review-current/Hope2016
      source_status_sha256: 5cd97f9a8a93eccb9f40cc5a2bbe6d4614fd5e0cc0c99f58d2e6143eac1102cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of general conclusions.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of Analysis 1.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of Analysis 2.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of Analysis 3.
    - source_id: P1-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction statement of intent.
    - source_id: P1-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction description of analysis goals.
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction description of analysis goals.
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of lesion volumes.
    - source_id: P2-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological correlation between measurement types.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive relationship between disconnection and lesion load.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive counts of divergence between measures.
    - source_id: P3-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive counts of divergence between measures.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive counts of divergence between measures.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports null association for lesion volume in Analysis 1.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null association for uncinate lesion load in Analysis 1.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant association for arcuate lesion load in Analysis
        1.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant associations for both tracts in Analysis 2.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports association for lesion volume in Analysis 2.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports R2 performance for both models in Analysis 3.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Reports R2 change when adding disconnection or lesion load data.
    - source_id: P4-S2-C7
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Restatement of unique variance findings.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports AIC values for model comparison.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Reports Bayes Factors for model comparison.
    - source_id: P4-S3-C2
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of strong evidence for disconnection model.
    - source_id: P4-S3-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of Analysis 1.
    - source_id: P4-S3-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of Analysis 2.
    - source_id: P4-S3-C7
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Discussion restatement of unique variance.
    - source_id: P4-S3-C8
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of model preference.
    - source_id: P4-S3-C9
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of model preference.
    - source_id: P5-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of replication of Marchina et al.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of study aim.
    - source_id: P5-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of arcuate convergence.
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of uncinate divergence.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P1-S2-C7
    - P1-S2-C8
    - P1-S2-C9
    - P2-S2-C8
    - P2-S3-C11
    - P3-S1-C7
    - P3-S1-C8
    - P3-S2-C1
    - P3-S2-C2
    - P4-S2-C7
    - P4-S3-C4
    - P4-S3-C5
    - P4-S3-C7
    - P4-S3-C8
    - P4-S3-C9
    - P5-S1-C6
    - P5-S1-C8
    - P5-S2-C3
    - P5-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C7
      recruited_sample:
      - P1-S3-C1
      eligibility:
      - P2-S1-C2
      - P2-S2-C3
      - P2-S2-C5
      - P2-S2-C6
      imaging_provenance:
      - P2-S3-C5
      - P2-S3-C6
      imaging_timing:
      - P1-S3-C1
      outcome_timing:
      - P1-S3-C1
      outcome_definition:
      - P2-S1-C6
      - P2-S1-C10
      validation: []
      analysis_restrictions:
      - P2-S3-C7
      dependent_variable_statement:
      - P3-S1-C1
      - P4-S1-C1
      limitations:
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C7
      - P5-S1-C9
      - P5-S2-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C1
      - P4-S1-C3
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S2-C3
      - P4-S4-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P1-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S3-C4
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
      pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
      review_sha256: 047898022b284c12bbece1baa93839d961bbb32dd56e622dcdce1b4bb3b0a101
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
      - P4-S2-C5
      source_result: 'Analysis 3 compared a ''lesion load model'' (continuous lesion
        load in arcuate/uncinate + lesion volume) with a ''disconnection model'' (binary
        disconnection of arcuate/uncinate + lesion volume) for fluency and naming
        scores. Both models explained a significant proportion of variance, but the
        disconnection model explained slightly more (fluency: R2=0.29 vs 0.25; naming:
        R2=0.35 vs 0.31). Adding disconnection data to the lesion load model significantly
        improved variance explained, whereas adding lesion load to the disconnection
        model did not. AIC analysis provided strong evidence (Bayes Factor > 10) in
        favor of the disconnection model for both scores.'
      result_status: model_comparison
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The draft correctly identifies Analysis 3 as a comparison between
            the lesion load model and the disconnection model, using the same outcome
            variables (fluency and naming) and covariates (lesion volume).
          source_ids:
          - P4-S1-C10
          - P4-S2-C2
          - P4-S2-C3
        direction:
          answer: fits
          reason: The draft correctly states that the disconnection model explains
            significantly greater variance and is preferred by AIC, matching the source
            findings that disconnection adds unique variance while lesion load does
            not add to the disconnection model.
          source_ids:
          - P4-S2-C5
          - P4-S2-C6
          - P4-S2-C10
        construct:
          answer: fits
          reason: The exposure is correctly defined as the disconnection model (binary
            disconnection of arcuate/uncinate + lesion volume) and the outcome as
            fluency/naming scores. The patient measurement is correctly identified
            as template_lesion_overlap, as the analysis relies on overlaying patient
            binary lesions on reference tract maps to determine disconnection or load,
            rather than patient-specific diffusion tractography.
          source_ids:
          - P2-S3-C5
          - P2-S3-C6
          - P2-S4-C3
          - P4-S2-C2
        qualifications:
          answer: fits
          reason: The draft includes the necessary qualifications regarding the model
            composition (binary vs continuous predictors) and the specific finding
            that disconnection adds unique variance. It also includes the limitation
            regarding the age difference between the patient sample and the reference
            tract atlas population.
          source_ids:
          - P4-S2-C2
          - P4-S2-C3
          - P4-S2-C6
          - P5-S1-C4
        missing_material_caveat:
          answer: fits
          reason: 'The draft captures the main caveats: the model comparison nature,
            the specific tracts involved, and the limitation of the reference atlas
            age. No material caveats that change the interpretation of the model comparison
            are omitted.'
          source_ids:
          - P4-S3-C10
          - P5-S1-C4
      optional_pending:
      - Sample size (142) is mentioned in source P2-S2-C7 but not explicitly in the
        draft's sample_n field; however, the draft notes it requires confirmation.
      - Specific R2 values and AIC/Bayes Factor numbers are not transcribed in the
        draft, which is acceptable for a qualitative draft.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (142) is mentioned in source P2-S2-C7 but not explicitly in the
      draft's sample_n field; however, the draft notes it requires confirmation.
    - Specific R2 values and AIC/Bayes Factor numbers are not transcribed in the draft,
      which is acceptable for a qualitative draft.
    normalizations:
    - field: sample.n
      original: 142
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R006
      exposure:
        text: disconnection model (arcuate/uncinate disconnection and lesion volume)
      outcome:
        text: fluency and naming scores
      analysis_label: Analysis 3
      relation: performance
      evidence_ids:
      - P4-S2-C5
      qualifier_ids:
      - P4-S2-C2
      - P4-S2-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
        source_review: _compare/relationships-2026-11-16/review-current/Hope2016
        source_status_sha256: 5cd97f9a8a93eccb9f40cc5a2bbe6d4614fd5e0cc0c99f58d2e6143eac1102cd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 139de52470a9d7b9b21ae796db301950e72b6f0ab2b408f1c4f33a07ca0be994
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C5
          page: 4
          text_layer_sha256: 139de52470a9d7b9b21ae796db301950e72b6f0ab2b408f1c4f33a07ca0be994
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Both models explain a signiﬁcant proportion of the variance
          in both

          of the two language scores, though the lesion load model (ﬂuency:

          R2 = 0.25, p b 0.001; naming: R2 = 0.31, p b 0.001) explains slightly

          less than the disconnection model (ﬂuency: R2 = 0.29, p b 0.001; nam-

          ing: R2 = 0.35, p b 0.001).'
        anchor_text: 'Both models explain a signiﬁcant proportion of the variance
          in both

          of the two language scores, though the lesion load model (ﬂuency:

          R2 = 0.25, p b 0.001; naming: R2 = 0.31, p b 0.001) explains slightly

          less than the disconnection model (ﬂuency: R2 = 0.29, p b 0.001; nam-

          ing: R2 = 0.35, p b 0.001).'
        excluded_fragments: []
        image_sha256: 270bc5bbd94b96a7095240c4c6e2d2a489711133b16dfe5895a40fc82547c4af
      P2-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a9f7f01eea8cef6ea410381823bbaa94ba2084c86714fb0aa094f22ec766c434
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C7
          page: 2
          text_layer_sha256: a9f7f01eea8cef6ea410381823bbaa94ba2084c86714fb0aa094f22ec766c434
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'A total of 142 patients met

          these criteria, 58 women and 84 men (age at onset: mean = 52.1

          years, standard deviation = 13.2 years; time post-stroke: mean =

          74.1 months; standard deviation = 80.0 months).'
        anchor_text: 'A total of 142 patients met

          these criteria, 58 women and 84 men (age at onset: mean = 52.1

          years, standard deviation = 13.2 years; time post-stroke: mean =

          74.1 months; standard deviation = 80.0 months).'
        excluded_fragments: []
      P2-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5cdb4f5eb1f530b890e24e07391238a1a40ad57e9e8b19c0d5a597660a31314e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C3
          page: 2
          text_layer_sha256: 5cdb4f5eb1f530b890e24e07391238a1a40ad57e9e8b19c0d5a597660a31314e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients were excluded

          if they: (a) were left handed or ambidextrous prior to their stroke;

          (b) were b12 months post-stroke at assessment; (c) had evidence of

          other signiﬁcant neurological conditions (e.g. dementia, multiple scle-

          rosis); (e) did not speak English as a ﬁrst language; (f) had suffered

          right or bilateral lesions, as assessed by a neurologist (APL), using the

          patients'' raw T1-weighted scans; or (g) had suffered dispersed rather

          than focal damage.'
        anchor_text: 'Patients were excluded

          if they: (a) were left handed or ambidextrous prior to their stroke;

          (b) were b12 months post-stroke at assessment; (c) had evidence of

          other signiﬁcant neurological conditions (e.g. dementia, multiple scle-

          rosis); (e) did not speak English as a ﬁrst language; (f) had suffered

          right or bilateral lesions, as assessed by a neurologist (APL), using the

          patients'' raw T1-weighted scans; or (g) had suffered dispersed rather

          than focal damage.'
        excluded_fragments: []
        image_sha256: 161a0a9a37ab93a198be54ccc794268fd36f15347a435c59d93717e7dff18afa
        transcription: '. Patients were excluded

          if they: (a) were left handed or ambidextrous prior to their stroke;

          (b) were <12 months post-stroke at assessment; (c) had evidence of

          other significant neurological conditions (e.g. dementia, multiple sclero-

          sis); (e) did not speak English as a first language; (f) had suffered

          right or bilateral lesions, as assessed by a neurologist (APL), using the

          patients'' raw T1-weighted scans; or (g) had suffered dispersed rather

          than focal damage'
      P5-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 958d8a86be14388bc200ab86e3f946d0fca7e82b3d3240be9a3e00369cbd5848
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d580219ecfbb811cc53afddf4002002106a357b1ed22b29390f24e2bdb20a6a3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C4
          page: 5
          text_layer_sha256: d580219ecfbb811cc53afddf4002002106a357b1ed22b29390f24e2bdb20a6a3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Another reason for caution stems from the age difference between

          our patient population, and the participants used to derive the tract im-

          ages (18–22 years: (Thiebaut de Schotten et al., 2011)).'
        anchor_text: 'Another reason for caution stems from the age difference between

          our patient population, and the participants used to derive the tract im-

          ages (18–22 years: (Thiebaut de Schotten et al., 2011)).'
        excluded_fragments: []
        image_sha256: 0c1e04eed3914e9d463d90b7c4ca366bbf77f74b93f640f34dd8925db1ded031
        transcription: 'Another reason for caution stems from the age difference between

          our patient population, and the participants used to derive the tract im-

          ages (18–22 years: (Thiebaut de Schotten et al., 2011))'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Both models explain a signiﬁcant proportion of the variance in both

    of the two language scores, though the lesion load model (ﬂuency:

    R2 = 0.25, p b 0.001; naming: R2 = 0.31, p b 0.001) explains slightly

    less than the disconnection model (ﬂuency: R2 = 0.29, p b 0.001; nam-

    ing: R2 = 0.35, p b 0.001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
