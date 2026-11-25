---
id: baseline_language_functioning
name: baseline language functioning
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: language_functioning_90_days
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_functioning_90_days
  target_kind: prognosis
  claim: Baseline language functioning was predictive of 90-day language functioning.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 22
    population: English- and Spanish-speaking patients with first-time stroke and
      aphasia (at least one abnormal language domain at baseline), at least 18 years
      of age, with positive MRI diffusion-weighted imaging for stroke.
    phase: not_reported
    time_post_onset: Baseline measured 24–72 hours after stroke onset; follow-up measured
      at 90 days.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Wide variability in 90-day scores among patients with similar baselines
  - Unable to assess the impact of speech-language therapy due to lack of information
    on intensity and lack of a non-therapy comparison group
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Combined score of three test domains (comprehension,
    repetition, and naming) measured within 24–72 hours of stroke onset, where each
    domain is converted to a 10-point scale. The prediction accounted for 33% of the
    variance; Addition of age, education, and lesion size to the regression equation
    did not reliably improve the variance explained. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P1-S2-C6, two-model agreement, human verification pending): All were examined
    for baseline function within 24–

    72 hours of stroke onset Original text-layer quotation is preserved below. PDF
    image reading (P1-S2-C7, two-model agreement, human verification pending): . The
    follow-up examina-

    tion reported here took place at 90 days after the

    qualifying stroke because it is felt that most

    spontaneous recovery occurs by this point.⁵ ⁶

    Patients with prior clinical stroke or other known Original text-layer quotation
    is preserved below. PDF image reading (P2-S1-C8, two-model agreement, human verification
    pending): Relative lesion volumes on MRI were calculated by measuring the largest
    X and Y diameters of the lesion on axial diffusion imaging, and multiplying by
    the number of visualised slices times the slice thickness (5 mm) divided by 2,
    similar to methods used to calculate haematoma volume.17


    RESULTS

    There were 91 patients in the complete PARIS database, accrued from 15 April 2001
    to 18 July 2005, of whom 22 were considered to have a focal language disorder
    at the time of stroke admission because each had at least one impaired language
    domain (see below) Original text-layer quotation is preserved below. PDF image
    reading (P1-S2-C5, two-model agreement, human verification pending): SUBJECTS
    AND METHODS

    Patients

    The Columbia PARIS database is comprised of

    English- and Spanish-speaking patients with first-

    time stroke, at least 18 years of age, presenting on

    admission with a new deficit in motor, language

    and/or visual–spatial dysfunction, and a positive

    MRI diffusion-weighted image (DWI) for stroke Original text-layer quotation is
    preserved below.'
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
    - proposed_concept:language_functioning_90_days
  citation: '@Lazar2008'
  source_passages:
  - section: Original source P2-S2-C10
    page: 2
    quote: 'Regression analysis demonstrated that baseline language

      functioning was predictive of 90-day language functioning,

      accounting for 33% of the variance (p,0.01).'
    supports: claim
  - section: Original source P1-S2-C6
    page: 1
    quote: 'All were examined for baseline function within 24–

      72 hours of stroke onset.'
    supports: method
  - section: Original source P1-S2-C7
    page: 1
    quote: 'The follow-up examina-

      tion reported here took place at 90 days after the

      qualifying stroke because it is felt that most

      spontaneous

      recovery

      occurs

      by

      this

      point.5 6

      Patients with prior clinical stroke or other known

      '
    supports: method
  - section: Original source P1-S3-C4
    page: 1
    quote: 'Measures

      The

      aphasia

      battery

      consisted

      of

      three

      test

      domains: Comprehension, repetition and naming.'
    supports: method
  - section: Original source P1-S3-C5
    page: 1
    quote: 'For comprehension, patients were given either the

      dictated

      commands

      subtest

      from

      the

      Boston

      Diagnostic Aphasia Examination15 (BDAE) or the

      Sequential Commands subtest from the Western

      Aphasia Battery16 (WAB).'
    supports: method
  - section: Original source P1-S3-C6
    page: 1
    quote: 'Naming was assessed via

      the

      Object

      Naming

      subtest

      from

      the

      WAB.'
    supports: method
  - section: Original source P1-S3-C7
    page: 1
    quote: 'Repetition was tested with either the low and

      high probability phrases from the BDAE, or with

      the Repetition subtest from the WAB.'
    supports: method
  - section: Original source P2-S1-C6
    page: 2
    quote: 'To provide a

      single, overall measure of language function, the scores of the

      three test domains were combined into a single variable, with a

      range of 0–30.'
    supports: method
  - section: Original source P2-S1-C8
    page: 2
    quote: 'Relative lesion volumes on MRI were calculated by measuring

      the largest X and Y diameters of the lesion on axial diffusion

      imaging, and multiplying by the number of visualised slices

      times the slice thickness (5 mm) divided by 2, similar to

      methods used to calculate haematoma volume.17

      RESULTS

      There were 91 patients in the complete PARIS database, accrued

      from 15 April 2001 to 18 July 2005, of whom 22 were considered

      to have a focal language disorder at the time of stroke admission

      because each had at least one impaired language domain (see

      below).'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'Addition of these variables to the equation did not

      reliably improve r2.'
    supports: claim
  - section: Original source P2-S2-C12
    page: 2
    quote: 'Although the

      group data show improvement, visual inspection of figure 1,

      however, does show that there could be wide variability in 90-

      day scores among patients with similar baselines.'
    supports: limitation
  - section: Original source P4-S2-C7
    page: 4
    quote: 'As a result, we

      could not assess the impact of therapy on the recovery in our

      cohort.'
    supports: limitation
  - section: Original source P1-S2-C5
    page: 1
    quote: 'SUBJECTS AND METHODS

      Patients

      The Columbia PARIS database is comprised of

      English- and Spanish-speaking patients with first-

      time stroke, at least 18 years of age, presenting on

      admission with a new deficit in motor, language

      and/or visual–spatial dysfunction, and a positive

      MRI diffusion-weighted image (DWI) for stroke.'
    supports: sample
predictor_type: behavioural
short_definition: Combined score of three test domains (comprehension, repetition,
  and naming) measured within 24–72 hours of stroke onset, where each domain is converted
  to a 10-point scale.
assessment:
- Boston Diagnostic Aphasia Examination
- Western Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lazar2008
  proposal_id: R007
  review_status_sha256: 06a6590104320c7e4fe4e99ef6a47e957e42ade1de841bd07598b7ac4414cd6d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
        A/passages.json: 6b389973a5188037b8dea99a884ff8b0662ab36147d36114f731f3aabcae5a46
        A/raw.json: 2253fa7f19f6bbc7cd50f9d37afec5f38ef01615412b8323f0b57cdaabc8f4f2
        A/source-units.json: b8b7e8675acf604a6775748411c0a540963682074a21436f4391f0b45c7175a7
        A/full-source-units.json: 4e18adaceef42430677e2748f5bb872090a434d1920be4f4bf3df6d393311fb1
        A/meta.json: f78e2d03590589a0a75a4766dc4895fcde832b47c16055d288f3bb74c88e24dc
        A/table-images/TABLE-1-page-3-1.png: 62e4f90712a3c1188400acb0e560093d08186a358dd2c8f77c244bf8ddffcdb8
        A/table-images/page-3.png: 9391b3749efb4038b3047fe29e8f782a88d0630a78bc0d90d9d29aca7449aab3
        A/table-images/manifest.json: f4e7652e6e9c511195108abc6aae8b8fa62dfc1f8f9a49d021a799c781a49728
        A/table-images/TABLE-2-page-3-2.png: 93547cc4f47afc5f5456de021e6f2eacea5d39dcb46e17e7178442c9525292d8
        A/clauses/window-03/raw.json: be7b32247f0ddf848a4996e9f4eb6e6bd90525e1d194051ae0fe7aa70da0ba0c
        A/clauses/window-03/prompt.txt: 4a1f2372335e65f39c90eeb65fcd1cde7108a625b2f0a9b2aca365acbdf4bbf8
        A/clauses/window-03/meta.json: 59a32929627dc5d2b19a490b8a702ab37fa14f7a0f666929173ac5753b742f8b
        A/clauses/window-04/raw.json: abf13907473efc17c87e432d7f531420398adc199c62fd66cfd3d2cac099d963
        A/clauses/window-04/prompt.txt: dee29e6969ad49aa4e1127f4a9edcb68469ff535ffaecb3687a81049931aa0cd
        A/clauses/window-04/meta.json: af61343117e570db7bc76d2122ab44dba198d392f394e85a5166f1eecc728dcf
        A/clauses/window-02/raw.json: bf3c5088e9076c28ab93cb3ca1b7ea47a35923abaa2b72faa3114e1f16a0c255
        A/clauses/window-02/prompt.txt: 8e53edbec2df03afafe04db48bc3f31eae4a27818216fb545c6c30723250ada3
        A/clauses/window-02/meta.json: 8d958f420a1d002553ea9c6fc737c104ea0530fc4da6803aa6761bc3969ce215
        A/clauses/window-01/raw.json: f716b4f177498a940b72351c9d9fbf9d8eabbcde56a6a21e2e9e9d5cfc61ab88
        A/clauses/window-01/prompt.txt: 6d10deb4717dcdf1e2a4c96407c5daadc8f2532fc7c0e543d78bf09b117813a5
        A/clauses/window-01/meta.json: beee5bb53a6d783facd5dc531ea0c77224bfa4de4b61c43efc2d74772d57f1ee
        A/tables/TABLE-1-page-3-1/raw.json: 2535ad67c524c811b04c8c55ef65d37515d05573134ff34e215f65b2fba9ed66
        A/tables/TABLE-1-page-3-1/prompt.txt: 44eb5d289861be7a2f09b5fe6809c636ec41c363f2d4238365ec3df0e6026fa4
        A/tables/TABLE-1-page-3-1/meta.json: 86bd46f7b3282fa7542ed978e32ee2097a2e98a09c809ca63b57b309cead8099
        A/tables/TABLE-2-page-3-2/raw.json: 48e56ec726c27370bff0e9817193c715a1fd011c13b8a842475c7156ed3444f9
        A/tables/TABLE-2-page-3-2/prompt.txt: 5133840011ffbe9db9a5d020ec1980f9b2b63b7eab13df3226021870f9f7e756
        A/tables/TABLE-2-page-3-2/meta.json: cb86e712cb101a90dc5568015e425f2178e1fbfd8837d8956d628c3b73170810
        B/passages.json: 6b389973a5188037b8dea99a884ff8b0662ab36147d36114f731f3aabcae5a46
        B/raw.json: 0d85fd322b7eeb752fd030447716aa11cc0d11b99d0e7bb3c6c7d5895b24fd6d
        B/source-units.json: b8b7e8675acf604a6775748411c0a540963682074a21436f4391f0b45c7175a7
        B/full-source-units.json: 4e18adaceef42430677e2748f5bb872090a434d1920be4f4bf3df6d393311fb1
        B/meta.json: c722a885be11a9d862a16ed50de260e0334efc70ebf25fbc123e3719c865a20e
        B/table-images/TABLE-1-page-3-1.png: 62e4f90712a3c1188400acb0e560093d08186a358dd2c8f77c244bf8ddffcdb8
        B/table-images/page-3.png: 9391b3749efb4038b3047fe29e8f782a88d0630a78bc0d90d9d29aca7449aab3
        B/table-images/manifest.json: 9b067aa62315558b9356a8a82dd7d30c22887f6c0cabb2437a6352e277bfd468
        B/table-images/TABLE-2-page-3-2.png: 93547cc4f47afc5f5456de021e6f2eacea5d39dcb46e17e7178442c9525292d8
        B/clauses/window-03/raw.json: 70d7b7e78be6d06829b5c842301684554c6dee3bd41757337bf05305d9e93ad8
        B/clauses/window-03/prompt.txt: 4a1f2372335e65f39c90eeb65fcd1cde7108a625b2f0a9b2aca365acbdf4bbf8
        B/clauses/window-03/meta.json: 067d5ddb06d67eed13e7c34970d9083d8a1ec097ff7609ab99267d691ac2deac
        B/clauses/window-04/raw.json: 77a52846c35e8b355a491ffce27362455c9b1c43db6ea4ffad150ee5f96bfc9a
        B/clauses/window-04/prompt.txt: dee29e6969ad49aa4e1127f4a9edcb68469ff535ffaecb3687a81049931aa0cd
        B/clauses/window-04/meta.json: bf63471ffc62cb4171796211b42c644db7c2d994985e6f7c11e5e362294124e7
        B/clauses/window-02/raw.json: 2def9b3808782551c2f43b1b69c959f614b577c413cd309270cdd5401e5605f3
        B/clauses/window-02/prompt.txt: 8e53edbec2df03afafe04db48bc3f31eae4a27818216fb545c6c30723250ada3
        B/clauses/window-02/meta.json: 755bf0bb9b5bc789387c061a9f754f3e82d95d4db4f36350cb9c7303db9bc09b
        B/clauses/window-01/raw.json: 9453daf15082cb7b05d74ec4ff494de8bce9857b1a50840d7aa6bf9e5e3ab34c
        B/clauses/window-01/prompt.txt: 6d10deb4717dcdf1e2a4c96407c5daadc8f2532fc7c0e543d78bf09b117813a5
        B/clauses/window-01/meta.json: 1277b2e6e419c0307f3b73d35da16cbc3651d7da8345a2df5986e7f7ce933013
        B/tables/TABLE-1-page-3-1/raw.json: 988916352b5f977458c9043e24779116d8cb122ffe257d1d41944bf0d0ea2c97
        B/tables/TABLE-1-page-3-1/prompt.txt: 44eb5d289861be7a2f09b5fe6809c636ec41c363f2d4238365ec3df0e6026fa4
        B/tables/TABLE-1-page-3-1/meta.json: b82e74f3d84f024a630be92794e897716807f08898a50345a357447bec3583b0
        B/tables/TABLE-2-page-3-2/raw.json: d41785176251e85a319f647ca6b02313b1eb4a73c872f3ec2d1a118630866fed
        B/tables/TABLE-2-page-3-2/prompt.txt: 5133840011ffbe9db9a5d020ec1980f9b2b63b7eab13df3226021870f9f7e756
        B/tables/TABLE-2-page-3-2/meta.json: 03fd77c69291c11b4e3f723a8eddb75cf23ffc78e4d93bc0b0bc1352bef02c39
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
      pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2008
      source_status_sha256: 13049d3f8572a8c8837c5e074aa3928af729b1aad292fd4f4aba0a5935f5f915
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: baseline language functioning
    outcome:
      text: 90-day language functioning
    analysis_label: Regression of baseline language functioning on 90-day language
      functioning
    relation: association
    evidence_ids:
    - P2-S2-C10
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
      pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2008
      source_status_sha256: 13049d3f8572a8c8837c5e074aa3928af729b1aad292fd4f4aba0a5935f5f915
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P2-S1-C10
      - Result passage disposed without unit P2-S1-C11
      - Result passage disposed without unit P2-S1-C12
      - Result passage disposed without unit P2-S1-C14
      - Result passage disposed without unit P2-S2-C2
      - Result passage disposed without unit P2-S2-C3
      - Result passage disposed without unit P2-S2-C5
      - Result passage disposed without unit P2-S2-C6
      - Result passage disposed without unit P2-S2-C8
      - Result passage disposed without unit P2-S2-C12
      - Result passage disposed without unit P2-S2-C13
      - Accounting without a linked unit P2-S3-C10
      - Accounting without a linked unit P2-S3-C3
      - Result passage disposed without unit P2-S3-C6
      - Result passage disposed without unit P2-S3-C7
      - Result passage disposed without unit P2-S3-C8
      - Accounting without a linked unit P2-S3-C9
      - Unaccounted source passage P2-S3-C3
      - Unaccounted source passage P2-S3-C9
      - Unaccounted source passage P2-S3-C10
      - Result passage disposed without unit P2-S3-C13
      - Result passage disposed without unit P2-S4-C1
      - Result passage disposed without unit P3-S1-C3
      - 'window 6: invalid/duplicate disposition P3-S1-C5'
      - Result passage disposed without unit P3-S2-C2
      - Result passage disposed without unit P4-S2-C3
      unattached_null_or_qualifier_ids:
      - P2-S2-C6
      - P2-S2-C8
      - P2-S3-C3
      - P4-S2-C3
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 54
      unselected_timing_passages:
      - P1-S2-C7
      - P1-S3-C1
      - P2-S1-C8
      - P4-S1-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: outcome_timing
        source_ids:
        - P1-S1-C4
        - P1-S2-C4
        - P1-S2-C7
        - P2-S1-C13
        - P2-S1-C14
        - P2-S2-C3
        - P2-S2-C4
        - P2-S2-C10
        - P2-S2-C11
        - P2-S3-C4
        - P3-S1-C1
        - P3-S1-C10
        - P3-S2-C1
        - P4-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P1-S1-C7
        - P1-S1-C8
        - P1-S1-C9
        - P2-S1-C7
        - P2-S3-C10
        - P2-S3-C11
        - P2-S3-C12
        - P3-S1-C7
        - P4-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - validation
      - dependent_variable_statement
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-3-2
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-3-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S1
        - P2-S3
        - P2-S4
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2008
      source_status_sha256: 13049d3f8572a8c8837c5e074aa3928af729b1aad292fd4f4aba0a5935f5f915
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of patients with language disorders.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports correlations between initial scores and 90-day scores/change.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports null correlations for lesion size, age, and education.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports null association between education and recovery.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Reports multiple regression model performance.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of recovery patterns.
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion volume calculation and cohort size.
    - source_id: P2-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information (handedness).
    - source_id: P2-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information (sex, age).
    - source_id: P2-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy administration.
    - source_id: P2-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean scores.
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean scores for patients without therapy info.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General group improvement statement.
    - source_id: P2-S2-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports Pearson correlations for initial and 90-day scores.
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes common disorders at baseline.
    - source_id: P2-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of language abnormalities.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports baseline correlation between naming and comprehension.
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports counts of resolved deficits.
    - source_id: P2-S2-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports Chi-square analysis of recovery by baseline severity.
    - source_id: P2-S2-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Reports regression of baseline function on 90-day function.
    - source_id: P2-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Reports regression of baseline function on 90-day recovery.
    - source_id: P2-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative observation of variability.
    - source_id: P2-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of individual patient recovery.
    - source_id: P2-S2-C14
      disposition: repeated
      result_indexes:
      - 8
      reason: Introduces the multivariate regression analysis.
    - source_id: P2-S3-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Reports that adding variables did not improve r2.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative observation of variability.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of baseline scores.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of individual recovery outcomes.
    - source_id: P2-S3-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null correlations for lesion size.
    - source_id: P2-S3-C10
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports null correlations for age/education and lesion location differences.
    - source_id: P2-S3-C11
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null correlations for education.
    - source_id: P2-S3-C12
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null correlations for age.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1.
    - source_id: P2-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1.
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on recovery.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about predictability.
    - source_id: P3-S1-C4
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Restates variance explained by baseline functioning.
    - source_id: P3-S1-C7
      disposition: repeated
      result_indexes:
      - 3
      - 10
      reason: Restates that age and education were not predictive.
    - source_id: P3-S1-C8
      disposition: repeated
      result_indexes:
      - 4
      - 8
      reason: Restates multiple regression results.
    - source_id: P3-S1-C9
      disposition: repeated
      result_indexes:
      - 5
      reason: Restates recovery likelihood for severe deficits.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about naming disorders.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about recovery in non-anomic cases.
    unresolved_coverage:
    - source_id: P2-S2-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P3-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C10
    - P2-S1-C8
    - P2-S1-C10
    - P2-S1-C11
    - P2-S1-C12
    - P2-S1-C14
    - P2-S2-C2
    - P2-S2-C3
    - P2-S2-C5
    - P2-S2-C6
    - P2-S2-C7
    - P2-S2-C8
    - P2-S2-C12
    - P2-S2-C13
    - P2-S3-C6
    - P2-S3-C7
    - P2-S3-C8
    - P2-S3-C13
    - P2-S4-C1
    - P3-S1-C1
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S2-C2
    - P4-S2-C3
    - P4-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-3-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C5
      - P2-S1-C9
      recruited_sample:
      - P1-S1-C4
      - P1-S2-C5
      eligibility:
      - P1-S2-C5
      - P1-S3-C1
      - P4-S1-C3
      - P4-S1-C4
      imaging_provenance:
      - P1-S2-C5
      - P2-S1-C8
      imaging_timing:
      - P1-S1-C4
      - P1-S2-C5
      outcome_timing: []
      outcome_definition:
      - P2-S1-C5
      - P2-S1-C6
      - P2-S2-C9
      - P2-S3-C2
      validation: []
      analysis_restrictions:
      - P2-S2-C6
      dependent_variable_statement: []
      limitations:
      - P4-S1-C5
      - P4-S2-C2
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      personal_factors: []
      tested_personal_effects:
      - P1-S1-C7
      - P1-S1-C8
      - P1-S1-C9
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P3-S1-C7
      adjustment_roles:
      - P2-S3-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C10
      - P2-S1-C11
      - P4-S1-C3
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: outcome_timing
      source_ids:
      - P1-S1-C4
      - P1-S2-C4
      - P1-S2-C7
      - P2-S1-C13
      - P2-S1-C14
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C10
      - P2-S2-C11
      - P2-S3-C4
      - P3-S1-C1
      - P3-S1-C10
      - P3-S2-C1
      - P4-S1-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P1-S1-C7
      - P1-S1-C8
      - P1-S1-C9
      - P2-S1-C7
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P3-S1-C7
      - P4-S1-C3
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
      pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
      review_sha256: 06a6590104320c7e4fe4e99ef6a47e957e42ade1de841bd07598b7ac4414cd6d
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
      - P2-S2-C10
      source_result: Regression analysis demonstrated that baseline language functioning
        was predictive of 90-day language functioning, accounting for 33% of the variance
        (p<0.01).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R007 correctly identifies the regression of
            baseline language functioning on 90-day language functioning as described
            in P2-S2-C10. The exposure and outcome match the source text.
          source_ids:
          - P2-S2-C10
        direction:
          answer: fits
          reason: The source states baseline functioning was 'predictive' of 90-day
            functioning. The proposed draft uses 'likely' direction, which is a reasonable
            qualitative representation of a significant positive predictive relationship
            (implied by the context of recovery and correlation in P2-S2-C4, though
            P2-S2-C10 itself just says predictive). The direction is not contradicted.
          source_ids:
          - P2-S2-C10
          - P2-S2-C4
        construct:
          answer: fits
          reason: The exposure is defined as the combined language score (comprehension,
            repetition, naming) measured at baseline (24-72h), and the outcome is
            the 90-day language score. This matches the source definitions in P1-S3-C4,
            P2-S1-C6, and P1-S2-C6/P1-S2-C7. The measurement is behavioral/non-imaging,
            not diffusion-based.
          source_ids:
          - P1-S3-C4
          - P2-S1-C6
          - P1-S2-C6
          - P1-S2-C7
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the model accounted for
            33% of variance and that adding covariates (age, education, lesion size)
            did not improve the model. This correctly reflects P2-S2-C10 and P2-S3-C3.
            The robustness of the baseline predictor after adjustment is correctly
            framed as a qualification/robustness check rather than a standalone finding
            about the covariates.
          source_ids:
          - P2-S2-C10
          - P2-S3-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding variability and therapy.
            The source P3-S1-C5 mentions 'artifacts' confounding interpretation, but
            the draft's inclusion of variability and therapy limitations covers the
            main interpretive caveats provided in the results/discussion sections
            relevant to this specific regression. No material caveat that changes
            the interpretation of the regression result itself is omitted.
          source_ids:
          - P2-S2-C12
          - P4-S2-C7
          - P3-S1-C5
      optional_pending:
      - Specific p-value threshold (p<0.01 vs p<0.001) not explicitly transcribed
        in optional fields but present in source
      - Exact R-squared value (33%) is in qualifications but not in optional numeric
        fields
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-value threshold (p<0.01 vs p<0.001) not explicitly transcribed in
      optional fields but present in source
    - Exact R-squared value (33%) is in qualifications but not in optional numeric
      fields
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: baseline language functioning
      outcome:
        text: 90-day language functioning
      analysis_label: Regression of baseline language functioning on 90-day language
        functioning
      relation: association
      evidence_ids:
      - P2-S2-C10
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
        pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
        source_review: _compare/relationships-2026-11-16/review-current/Lazar2008
        source_status_sha256: 13049d3f8572a8c8837c5e074aa3928af729b1aad292fd4f4aba0a5935f5f915
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: aeb0050bc1c1c44746588dbd06263f0f2bed5f9dbc0a6b8aefb4ee2b66c7ddc2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C6
          page: 1
          text_layer_sha256: aeb0050bc1c1c44746588dbd06263f0f2bed5f9dbc0a6b8aefb4ee2b66c7ddc2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All were examined for baseline function within 24–

          72 hours of stroke onset.'
        anchor_text: 'All were examined for baseline function within 24–

          72 hours of stroke onset.'
        excluded_fragments: []
        image_sha256: ab18432d21591d70742c0b507b9bab22427510332fc9afa5d5053120ce2d3a14
        transcription: 'All were examined for baseline function within 24–

          72 hours of stroke onset'
      P1-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4940889b404ccb7a41fb6686aa54d83853b2b56ec95c91dffdaaf0d0a06c4fb8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C7
          page: 1
          text_layer_sha256: a14d80d48da0d4d04d6bcf24fa072dac3ffc82b4c717a5826eaaccec22ee1bc7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The follow-up examina-

          tion reported here took place at 90 days after the

          qualifying stroke because it is felt that most

          spontaneous

          recovery

          occurs

          by

          this

          point.5 6

          Patients with prior clinical stroke or other known

          '
        anchor_text: 'The follow-up examina-

          tion reported here took place at 90 days after the

          qualifying stroke because it is felt that most

          spontaneous

          recovery

          occurs

          by

          this

          point.5 6

          Patients with prior clinical stroke or other known'
        excluded_fragments: []
        image_sha256: 753bcbd364a0e9134c1ebe6d321e99fd3a12b5d33a9f9566cf6f19ef76c76414
        transcription: '. The follow-up examina-

          tion reported here took place at 90 days after the

          qualifying stroke because it is felt that most

          spontaneous recovery occurs by this point.⁵ ⁶

          Patients with prior clinical stroke or other known'
      P2-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 36fe129dd9553f5e68336842a2534b985df24356968772213eabd2ffe7bb2ce3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C8
          page: 2
          text_layer_sha256: 36fe129dd9553f5e68336842a2534b985df24356968772213eabd2ffe7bb2ce3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Relative lesion volumes on MRI were calculated by measuring

          the largest X and Y diameters of the lesion on axial diffusion

          imaging, and multiplying by the number of visualised slices

          times the slice thickness (5 mm) divided by 2, similar to

          methods used to calculate haematoma volume.17

          RESULTS

          There were 91 patients in the complete PARIS database, accrued

          from 15 April 2001 to 18 July 2005, of whom 22 were considered

          to have a focal language disorder at the time of stroke admission

          because each had at least one impaired language domain (see

          below).'
        anchor_text: 'Relative lesion volumes on MRI were calculated by measuring

          the largest X and Y diameters of the lesion on axial diffusion

          imaging, and multiplying by the number of visualised slices

          times the slice thickness (5 mm) divided by 2, similar to

          methods used to calculate haematoma volume.17

          RESULTS

          There were 91 patients in the complete PARIS database, accrued

          from 15 April 2001 to 18 July 2005, of whom 22 were considered

          to have a focal language disorder at the time of stroke admission

          because each had at least one impaired language domain (see

          below).'
        excluded_fragments: []
        image_sha256: 6f8d881ed59f7a5f8ea7105015b4d6c327600fffc240f09f424a1f3e8291052c
        transcription: 'Relative lesion volumes on MRI were calculated by measuring
          the largest X and Y diameters of the lesion on axial diffusion imaging,
          and multiplying by the number of visualised slices times the slice thickness
          (5 mm) divided by 2, similar to methods used to calculate haematoma volume.17


          RESULTS

          There were 91 patients in the complete PARIS database, accrued from 15 April
          2001 to 18 July 2005, of whom 22 were considered to have a focal language
          disorder at the time of stroke admission because each had at least one impaired
          language domain (see below)'
      P1-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dae0fd855c1a586a365d258d93dd8cc964cf56562c864be0e77dced9f1fdb869
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 277d1047223d5ce34f0f2c6015684ca207bc42421b097c1cdebdc9a9633befda
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C5
          page: 1
          text_layer_sha256: 277d1047223d5ce34f0f2c6015684ca207bc42421b097c1cdebdc9a9633befda
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'SUBJECTS AND METHODS

          Patients

          The Columbia PARIS database is comprised of

          English- and Spanish-speaking patients with first-

          time stroke, at least 18 years of age, presenting on

          admission with a new deficit in motor, language

          and/or visual–spatial dysfunction, and a positive

          MRI diffusion-weighted image (DWI) for stroke.'
        anchor_text: 'SUBJECTS AND METHODS

          Patients

          The Columbia PARIS database is comprised of

          English- and Spanish-speaking patients with first-

          time stroke, at least 18 years of age, presenting on

          admission with a new deficit in motor, language

          and/or visual–spatial dysfunction, and a positive

          MRI diffusion-weighted image (DWI) for stroke.'
        excluded_fragments: []
        image_sha256: da4d5f2a3bdd4db46715a0c90a0ee6fc30337ede9d70f301acae5b19c66ac9ad
        transcription: 'SUBJECTS AND METHODS

          Patients

          The Columbia PARIS database is comprised of

          English- and Spanish-speaking patients with first-

          time stroke, at least 18 years of age, presenting on

          admission with a new deficit in motor, language

          and/or visual–spatial dysfunction, and a positive

          MRI diffusion-weighted image (DWI) for stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: 'Regression analysis demonstrated that baseline language

    functioning was predictive of 90-day language functioning,

    accounting for 33% of the variance (p,0.01).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
