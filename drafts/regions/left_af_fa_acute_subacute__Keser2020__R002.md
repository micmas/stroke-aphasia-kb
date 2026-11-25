---
id: left_af_fa_acute_subacute
name: left AF FA cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: personal_pronoun_cohesiveness
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: personal_pronoun_cohesiveness
  target_kind: impairment
  claim: Acute/subacute personal pronoun cohesiveness was significantly correlated
    with acute/subacute left AF FA.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 28
    population: native English-speaking patients with mild to severe aphasia after
      left hemispheric lobar and/or subcortical ischemic stroke
    phase: not_reported
    time_post_onset: concurrently measured within the first three months after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - only one experienced rater of imaging data
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population reference
    tract template for the left arcuate fasciculus, measured via fractional anisotropy
    (FA) using atlas-based segmentation in DSI Studio. adjusted for age, education,
    and lesion load; did not remain significant after false discovery rate (FDR) correction.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P2-S2-C5, two-model agreement, human verification
    pending): . Twenty-eight native English-speaking patients

    (see Table 1 for demographics) with clinically diagnosed

    mild to severe aphasia after left hemispheric lobar and

    subcortical ischemic stroke were enrolled in the study Original text-layer quotation
    is preserved below. PDF image reading (P8-S1-C1, two-model agreement, human verification
    pending): multiple comparisons, our study is also limited by a small

    sample size, missing time points (see Fig. 2 for all the data

    points), and only one experienced rater of the imaging data Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:personal_pronoun_cohesiveness
  citation: '@Keser2020'
  source_passages:
  - section: Original source P5-S1-C5
    page: 5
    quote: 'Acute/subacute personal pronoun cohesiveness was

      signiﬁcantly correlated with acute/subacute left AF FA

      (r = 0.66, p = 0.028) and left ILF FA (r = 0.85, p = 0.00087)

      (Fig. 3).'
    supports: claim
  - section: Original source P5-S1-C6
    page: 5
    quote: 'Only the relation between acute/subacute ILF FA

      and

      acute/subacute

      personal

      pronoun

      cohesiveness

      remained signiﬁcant after FDR correction.'
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Twenty-eight native English-speaking patients

      (see Table 1 for demographics) with clinically diagnosed

      mild to severe aphasia after left hemispheric lobar and

      subcortical ischemic stroke were enrolled in the study.'
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: "Concurrent imaging and behavioral data were collected\nat acute/subacute\
      \ (<3months after stroke), early chronic\n(4-7 months after stroke), and late\
      \ chronic (11\x0113 months\nafter stroke) time points."
    supports: method
  - section: Original source P4-S1-C6
    page: 4
    quote: 'FA and RD scalar maps were used as

      they reﬂect the white matter integrity accurately in various

      conditions.8,9 The atlas-based segmentation function in DSI

      studio was then conducted to obtain atlas-based segmenta-

      tion of the right and left AF, SLF, frontal aslant tract, infe-

      rior fronto-occipital fasciculus (IFOF), inferior longitudinal

      fasciculus (ILF), uncinate fasciculus (UF) (Fig. 1) by

      warping Human Connectome Project white matter atlas

      (www.humanconnectomeproject.org/)

      into

      individual

      subject space.'
    supports: method
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Next,

      a

      multivariable

      logistical

      regression model was calculated for the lexical and per-

      sonal cohesion performance category, including tract

      measures, age, education, lesion load.'
    supports: method
  - section: Original source P8-S1-C1
    page: 8
    quote: '

      multiple comparisons, our study is also limited by a small

      sample size, missing time points (see Fig. 2 for all the data

      points), and only one experienced rater of the imaging data.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Keser2020
  proposal_id: R002
  review_status_sha256: 70a34c52e669aaf3320cb70a25577cb289f295fe2a864b5b562845d85477d70d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
        A/passages.json: e9afb3675eee4ccab0f9763e26b2c4d28f2a59d36e59f89817f4369ef3032a6d
        A/raw.json: b5cb02f17980a7a21216807926d09f954c36d6b44c45c7a034494cec67e2257a
        A/source-units.json: 0f7558d1c99794bbe699464fefa0ac632a30b66bdfe2a1c917fc2e1bb405ff2c
        A/full-source-units.json: 8935ec3edcde343aa53e4782664b1265a14a4cb23686f71ff3c90c3001591010
        A/meta.json: 055e48ff7fc38832142f90614f5a4330480c40d5c0634e4a61bb1c2187502175
        A/table-images/TABLE-1-page-3-1.png: 5fac3f5f8da4566009ed3106307faabe22e268c90b8f1694977bfb5cd34e5841
        A/table-images/page-3.png: 54c24e7aa80f9b8547ad41d7983a90f49dbcf706938a15cc67083ffc0b14c761
        A/table-images/page-6.png: 4ed4a9e30b6e579d0e32bad769c0f0adb9dc987d59e79706d4bab954c4b6759f
        A/table-images/TABLE-2-page-6-1.png: 874121b69e2bbd181ab2781f611f4bbb2616db0e684bbf8f2f43d45fa6d17fa4
        A/table-images/manifest.json: de260ef5baeb78010914e8035ce2e5114fb9f361ad6915fa9b8ba755272ba844
        A/clauses/window-03/raw.json: 7139abfde1c0f455a144f63cc9d3cbee6cdef59423a863fc43684b3bb3043178
        A/clauses/window-03/prompt.txt: 73747d46acc1111eeea55c577feac65bd7e1aa9b3de3727194a51ee7132b342b
        A/clauses/window-03/meta.json: 55b9375105e247ba4aab42ae0f88cb273cd11def508b7b12bc858ae1ea905e18
        A/clauses/window-04/raw.json: e896624759dec08f459523dee93eb6679ac1cd46a0fc0a2dc092cab57a67ea2f
        A/clauses/window-04/prompt.txt: 2c62a5c5dd06ffebdc779f777cb13f9bffb529fe3a6ef36c0becb15739da59f3
        A/clauses/window-04/meta.json: 4e71d9704df135b51c8c0f3d45223cf1b490ab354fd61688ee5861dc4427152d
        A/clauses/window-05/raw.json: df607edb247eb8189ee27935058b00c3ff67a214704c66426e611cfc8b12bacb
        A/clauses/window-05/prompt.txt: 9f9d7585fb2ac7b8cd07bd03116a78587dffa80e7f9a22b85809ca44ce7038d2
        A/clauses/window-05/meta.json: ecaec3311c52a32b344bc46e2e113bb6fffafc6e8cc3cdecd7bea98933fa7c25
        A/clauses/window-02/raw.json: a19c6a4f560674a35b936f659384148954b880e8db441c261a799aa3e123d787
        A/clauses/window-02/prompt.txt: a1e6fc95ed69f7489a6cb3404c0d0381d923db9bad7cf2f309294ba1b7fb1cc0
        A/clauses/window-02/meta.json: e6f4ca6331da5d71e648c7b58f3103307f539b9b28e021cad6952b211353b9d1
        A/clauses/window-01/raw.json: 6d43ad82f3200ee2bd4f56cf36cf572a4df54cdde00355508879deccb4b3a553
        A/clauses/window-01/prompt.txt: f726729b1ddc78be44d65df139246fb88530da6b6b7309b07823e439e73d1f06
        A/clauses/window-01/meta.json: ec908f1b97d6b4f4dd2f18f3fed9ab0e8920127f19ba1a8867e2869054c9ccfd
        A/tables/TABLE-2-page-6-2/raw.json: 1a7a409abbcda385881ede75300d261944d2052e18f80ca79e7dc4e11c7a595b
        A/tables/TABLE-2-page-6-2/prompt.txt: 2fddb18d0dfc43239ae4f482cefda4ccd4c72df67652b3f6699de757efb4d538
        A/tables/TABLE-2-page-6-2/meta.json: 496d2fa05d0762d68abac1df6a26af1592092e7236ed8a6545b7d59c45aaa85c
        A/tables/TABLE-1-page-3-1/raw.json: d6cc88f4025fbf48704e44cb1b98185132122c3b1d810dd1cee4111e86112823
        A/tables/TABLE-1-page-3-1/prompt.txt: fd254f8c5a3e5fb45d018a365b32d482d8cca8cd4143b9f4eee047cce8a9e8a3
        A/tables/TABLE-1-page-3-1/meta.json: fad06781075e90aaee243d45885eb8ff940114b24454972941a6ebb0882e5b6e
        B/passages.json: e9afb3675eee4ccab0f9763e26b2c4d28f2a59d36e59f89817f4369ef3032a6d
        B/raw.json: 66dc083a0f540f1a8cf708c91a6f9da15fc8bf853556d46878853ac7c4a6e7f9
        B/source-units.json: 0f7558d1c99794bbe699464fefa0ac632a30b66bdfe2a1c917fc2e1bb405ff2c
        B/full-source-units.json: 8935ec3edcde343aa53e4782664b1265a14a4cb23686f71ff3c90c3001591010
        B/meta.json: 1953f7041445e3373f359e6e122c6f7717d8867da2e9e69d0604015a77d84434
        B/table-images/TABLE-1-page-3-1.png: 5fac3f5f8da4566009ed3106307faabe22e268c90b8f1694977bfb5cd34e5841
        B/table-images/page-3.png: 54c24e7aa80f9b8547ad41d7983a90f49dbcf706938a15cc67083ffc0b14c761
        B/table-images/page-6.png: 4ed4a9e30b6e579d0e32bad769c0f0adb9dc987d59e79706d4bab954c4b6759f
        B/table-images/TABLE-2-page-6-1.png: 874121b69e2bbd181ab2781f611f4bbb2616db0e684bbf8f2f43d45fa6d17fa4
        B/table-images/manifest.json: ec987c3e5fffb0924f98ef9d38e78fa12d93d78c48104febadd9798be0321049
        B/clauses/window-03/raw.json: 4a80bb2a6343d12669a5f36ac9a46a760e931a22f8a783c231e8d8c5f2fc8d94
        B/clauses/window-03/prompt.txt: 73747d46acc1111eeea55c577feac65bd7e1aa9b3de3727194a51ee7132b342b
        B/clauses/window-03/meta.json: cc9b6bbe90eb9968ac1a0f0c33a8dd33b99aad5a6691a6cb1897d86316d51643
        B/clauses/window-04/raw.json: 040a3b3b3f1640f5e9402eba2048930598bf6ecd4addf2aea3c31b43e64bbaa1
        B/clauses/window-04/prompt.txt: 2c62a5c5dd06ffebdc779f777cb13f9bffb529fe3a6ef36c0becb15739da59f3
        B/clauses/window-04/meta.json: 11051e73ceed1be4a3a1903314d8bad0fd24a30ff1e74c537c19b077af48f73e
        B/clauses/window-05/raw.json: df607edb247eb8189ee27935058b00c3ff67a214704c66426e611cfc8b12bacb
        B/clauses/window-05/prompt.txt: 9f9d7585fb2ac7b8cd07bd03116a78587dffa80e7f9a22b85809ca44ce7038d2
        B/clauses/window-05/meta.json: 361f2f759aa1b84f9cca92b8533c796c792c8a3d64d68b830469e3bbc7823389
        B/clauses/window-02/raw.json: 6c906ad94d5267ca7f990ad8eaf8d92054bd87c1d68414cf31c928ea68c53b4c
        B/clauses/window-02/prompt.txt: a1e6fc95ed69f7489a6cb3404c0d0381d923db9bad7cf2f309294ba1b7fb1cc0
        B/clauses/window-02/meta.json: 03675d70e34310122e573e40f2a34a77c35df56e20affb6a823c5a15a1a0600b
        B/clauses/window-01/raw.json: 02431292fcc8e362d5afe44779b9f1016aed684ef832bb710205bae5c83a7b2a
        B/clauses/window-01/prompt.txt: f726729b1ddc78be44d65df139246fb88530da6b6b7309b07823e439e73d1f06
        B/clauses/window-01/meta.json: 6404fb3effb32a6891aa6422feb228f9233693425c2cdeba51073ac1387d8f00
        B/tables/TABLE-2-page-6-2/raw.json: ae21e34c480e444c3b3f239bc3e43df9aeed9c4233015684fe879bd9cb54aade
        B/tables/TABLE-2-page-6-2/prompt.txt: 2fddb18d0dfc43239ae4f482cefda4ccd4c72df67652b3f6699de757efb4d538
        B/tables/TABLE-2-page-6-2/meta.json: c2ae01ae21b704b16bce3179e278a823eb528b8b9ae68ea2f58ebc72eceb4635
        B/tables/TABLE-1-page-3-1/raw.json: d97fe2dc3576a23d76b1be003e0e7650f71368f1f3a288190173e474dc9b82c9
        B/tables/TABLE-1-page-3-1/prompt.txt: fd254f8c5a3e5fb45d018a365b32d482d8cca8cd4143b9f4eee047cce8a9e8a3
        B/tables/TABLE-1-page-3-1/meta.json: 51784a87529c4690cafd795c673d018ba37d421d5614cf43477f2759d67779dd
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
      pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
      source_review: _compare/relationships-2026-11-16/review-current/Keser2020
      source_status_sha256: 77846ae9287a4734c06cb9d5772da008656f9759892c8474187391afcae34a9d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: left AF FA
    outcome:
      text: acute/subacute personal pronoun cohesiveness
    analysis_label: Concurrent analysis (Acute/Subacute)
    relation: association
    evidence_ids:
    - P5-S1-C5
    - P6-S1-C6
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
      pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
      source_review: _compare/relationships-2026-11-16/review-current/Keser2020
      source_status_sha256: 77846ae9287a4734c06cb9d5772da008656f9759892c8474187391afcae34a9d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C4
      - Accounting without a linked unit P4-S2-C9
      - Result passage disposed without unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P4-S2-C9
      - Unaccounted source passage P5-S1-C3
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P7-S2-C2
      - Unresolved source passage P7-S2-C2
      - Result passage disposed without unit P8-S1-C5
      unattached_null_or_qualifier_ids:
      - P7-S2-C2
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 100
      unselected_timing_passages:
      - P1-S1-C7
      - P2-S2-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S1
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
      source_review: _compare/relationships-2026-11-16/review-current/Keser2020
      source_status_sha256: 77846ae9287a4734c06cb9d5772da008656f9759892c8474187391afcae34a9d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes: []
      reason: General summary of results restated in detailed analysis sections.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 3
      - 14
      reason: Restatement of specific correlations for ILF FA and AF RD.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the distribution of cohesion scores.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies best predictors from recursive feature selection.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports cohort lesion load mean.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Null finding for acute/subacute tract values and CU.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Longitudinal prediction of CU by AF RD.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Acute/subacute correlations for AF FA and ILF FA with cohesion.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: FDR qualification for ILF FA and cohesion.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Early chronic correlations for AF FA and ILF RD with CU.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: FDR qualification for early chronic associations.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Late chronic associations for AF FA and RD with CU.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Late chronic associations for IFOF FA and RD with CU.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of consistent trend across time points.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend describing scatter plots.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      - 13
      reason: Late chronic associations for IFOF and ILF with CU.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Late chronic associations for AF FA and RD with cohesion.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 15
      reason: FDR qualification for AF RD and cohesion.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 8
      - 15
      reason: Discussion restatement of AF as best correlate.
    - source_id: P7-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of ILF as best correlate for cohesion.
    - source_id: P7-S1-C7
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of AF predicting recovery.
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of late chronic significance.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of ILF role in syntactic processing.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 16
      reason: Null finding for right hemispheric pathways.
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 2
      - 8
      reason: General conclusion restating importance of AF and ILF.
    unresolved_coverage:
    - source_id: P1-S1-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S2-C8
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P2-S3-C4
    - P5-S1-C2
    - P5-S1-C6
    - P5-S1-C8
    - P5-S2-C4
    - P6-S2-C2
    - P7-S1-C3
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C7
    - P7-S2-C2
    - P7-S2-C5
    - P8-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C7
      recruited_sample:
      - P2-S2-C5
      eligibility:
      - P2-S2-C5
      imaging_provenance:
      - P4-S1-C6
      imaging_timing:
      - P2-S2-C6
      - P4-S2-C11
      outcome_timing:
      - P2-S2-C6
      - P4-S2-C11
      outcome_definition:
      - P2-S3-C2
      - P2-S3-C3
      validation:
      - P4-S1-C8
      analysis_restrictions:
      - P4-S1-C4
      - P7-S3-C3
      dependent_variable_statement:
      - P4-S2-C2
      - P4-S2-C3
      limitations:
      - P7-S3-C5
      - P8-S1-C1
      - P8-S1-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S1-C9
      - P4-S2-C2
      - P4-S2-C3
      - P6-S2-C3
      - P7-S3-C2
      explicitly_not_adjusted:
      - P4-S1-C4
      - P7-S3-C3
      descriptive_personal_factors:
      - P3-S2-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
      review_sha256: 70a34c52e669aaf3320cb70a25577cb289f295fe2a864b5b562845d85477d70d
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
      - P5-S1-C5
      source_result: Acute/subacute personal pronoun cohesiveness was significantly
        correlated with acute/subacute left AF FA (r = 0.66, p = 0.028). This association
        did not remain significant after false discovery rate (FDR) correction, whereas
        the association with left ILF FA did.
      result_status: detected_only_at_relaxed_threshold
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the concurrent (acute/subacute)
            correlation between left AF FA and personal pronoun cohesiveness. The
            source explicitly identifies this relationship in P5-S1-C5 and notes its
            status after FDR correction in P5-S1-C6. The proposed core correctly identifies
            this specific analysis.
          source_ids:
          - P5-S1-C5
          - P5-S1-C6
        direction:
          answer: fits
          reason: The source reports a positive correlation (r = 0.66). The proposed
            core states the association was 'significantly correlated' and includes
            the qualification that it did not survive FDR correction. This accurately
            reflects the 'detected at uncorrected threshold but not at FDR' status
            without misrepresenting the direction or the null result after correction.
          source_ids:
          - P5-S1-C5
          - P5-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as left AF FA. The outcome
            is personal pronoun cohesiveness. The patient measurement is correctly
            classified as template_lesion_overlap, as the study used atlas-based segmentation
            (warping HCP atlas to individual space) to obtain FA metrics, rather than
            patient-specific tractography or direct lesion mapping. The method (LSM/Logistic
            Regression) is consistent with the source description of using logistic
            regression for categorical cohesion outcomes.
          source_ids:
          - P4-S1-C6
          - P4-S2-C3
          - P5-S1-C5
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that the association
            'did not remain significant after false discovery rate (FDR) correction'.
            This is essential because P5-S1-C6 explicitly states that only the ILF
            FA relation survived FDR, implying the AF FA relation did not. Omitting
            this would misrepresent the finding as a robust primary result. The core
            also correctly notes the adjustment for age, education, and lesion load.
          source_ids:
          - P5-S1-C6
          - P1-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The core includes the FDR qualification and the small sample size
            limitation. No other material caveats that change the interpretation of
            this specific association are omitted. The distinction between the AF
            FA result (not surviving FDR) and the ILF FA result (surviving FDR) is
            preserved by the qualification.
          source_ids:
          - P5-S1-C6
          - P8-S1-C1
      optional_pending:
      - Exact p-value and r-value transcription
      - Specific FDR threshold value used
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact p-value and r-value transcription
    - Specific FDR threshold value used
    normalizations: []
    analysis_identity:
      id: R002
      exposure:
        text: left AF FA
      outcome:
        text: acute/subacute personal pronoun cohesiveness
      analysis_label: Concurrent analysis (Acute/Subacute)
      relation: association
      evidence_ids:
      - P5-S1-C5
      - P6-S1-C6
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
        pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
        source_review: _compare/relationships-2026-11-16/review-current/Keser2020
        source_status_sha256: 77846ae9287a4734c06cb9d5772da008656f9759892c8474187391afcae34a9d
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 10167c847cd9c3065f9b68719170d2976e25daa783ae638e6c50a559d14b9a21
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 10167c847cd9c3065f9b68719170d2976e25daa783ae638e6c50a559d14b9a21
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Twenty-eight native English-speaking patients

          (see Table 1 for demographics) with clinically diagnosed

          mild to severe aphasia after left hemispheric lobar and

          subcortical ischemic stroke were enrolled in the study.'
        anchor_text: 'Twenty-eight native English-speaking patients

          (see Table 1 for demographics) with clinically diagnosed

          mild to severe aphasia after left hemispheric lobar and

          subcortical ischemic stroke were enrolled in the study.'
        excluded_fragments: []
        image_sha256: 1414acbc5c11a7ea9fa312bcdb749b40c21eb40e1fa7877be6850d5fbdad7b95
        transcription: '. Twenty-eight native English-speaking patients

          (see Table 1 for demographics) with clinically diagnosed

          mild to severe aphasia after left hemispheric lobar and

          subcortical ischemic stroke were enrolled in the study'
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e604dd43f77a0a6341f85b8149e2687b58540627e30e8cbf47aef8b5c1c1b1d7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: e604dd43f77a0a6341f85b8149e2687b58540627e30e8cbf47aef8b5c1c1b1d7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Concurrent imaging and behavioral data were collected\nat\
          \ acute/subacute (<3months after stroke), early chronic\n(4-7 months after\
          \ stroke), and late chronic (11\x0113 months\nafter stroke) time points."
        anchor_text: "Concurrent imaging and behavioral data were collected\nat acute/subacute\
          \ (<3months after stroke), early chronic\n(4-7 months after stroke), and\
          \ late chronic (11\x0113 months\nafter stroke) time points."
        excluded_fragments: []
      P8-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 82e2122bb88f2ae835bd1b37f3eab0c4b3940fd96db6ee5b27882e59fcd82c0c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d476cec95ee5a5c3e0f34debcf33152c2e194f0189b6cf4cb8b143b848063516
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C1
          page: 8
          text_layer_sha256: dd14c40a21f6b68d33d6673241c9cae9d60bd4269553003f6636f8b01747dcc4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '

          multiple comparisons, our study is also limited by a small

          sample size, missing time points (see Fig. 2 for all the data

          points), and only one experienced rater of the imaging data.'
        anchor_text: 'multiple comparisons, our study is also limited by a small

          sample size, missing time points (see Fig. 2 for all the data

          points), and only one experienced rater of the imaging data.'
        excluded_fragments: []
        image_sha256: 06b407b86a6eee657640e09dcaa2a8c8fa19b47c81744b48416cfac9245014e0
        transcription: 'multiple comparisons, our study is also limited by a small

          sample size, missing time points (see Fig. 2 for all the data

          points), and only one experienced rater of the imaging data'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Acute/subacute personal pronoun cohesiveness was

    signiﬁcantly correlated with acute/subacute left AF FA

    (r = 0.66, p = 0.028) and left ILF FA (r = 0.85, p = 0.00087)

    (Fig. 3).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
