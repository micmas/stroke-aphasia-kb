---
id: bdnf_val_val_atdcs_interaction
name: BDNF val/val and A-tDCS interaction
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: naming_improvement
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: naming_improvement
  target_kind: prognosis
  claim: Participants with typical BDNF genotype (val/val) who received A-tDCS during
    aphasia treatment showed greater naming improvement than those with typical BDNF
    genotype who received sham tDCS, and greater improvement than participants with
    atypical BDNF genotype regardless of tDCS condition.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: 66
    population: individuals with chronic stroke-induced aphasia
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
  - Baseline differences in aphasia severity between genotype groups may reflect other
    factors besides BDNF genotype
  - Depression levels were not compared between genotype groups
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: Interaction between typical BDNF genotype (val/val
    at rs6265, measured via TaqMan genotyping assay from whole blood) and receipt
    of 1 mA anodal tDCS (A-tDCS) to the left temporoparietal region during language
    therapy. Analysis used a mixed effects linear model adjusted for baseline WAB-AQ
    and lesion size; A baseline difference in language performance was observed, where
    typical BDNF participants had milder symptoms, though this was not statistically
    significant after adjusting for time post-stroke and lesion size. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P4-S2-C12, two-model agreement, human verification pending): In
    the current study, the average time post-stroke at enrollment

    was greater than 3.5 years Original text-layer quotation is preserved below. PDF
    image reading (P2-S4-C2, two-model agreement, human verification pending): . Therefore,
    BDNF

    genotype and post-treatment assessment data were available for

    66 participants Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:naming_improvement
  therapy:
    id: atdcs_aphasia_treatment
    name: anodal tDCS during behavioral aphasia treatment
  citation: '@Fridriksson2018BDNF'
  source_passages:
  - section: Original source P1-S2-C6
    page: 1
    quote: 'Participants with val/val genotype who received A-tDCS

      showed greater response to aphasia treatment than val/val participants who received
      S-tDCS, as well as

      the Met allele carriers, regardless of tDCS condition.'
    supports: claim
  - section: Original source P4-S1-C8
    page: 4
    quote: 'Based on the repeated measures mixed model, an interaction

      between BDNF genotype and tDCS condition was revealed for

      naming improvement (Table 2).'
    supports: claim
  - section: Original source P4-S1-C9
    page: 4
    quote: 'Participants with typical BDNF

      genotype who received A-tDCS during the aphasia treatment

      improved more than those with typical BDNF genotype but

      received S-tDCS (Fig. 2).'
    supports: claim
  - section: Original source P4-S1-C10
    page: 4
    quote: 'The participants with typical BDNF geno-

      type who received A-tDCS also improved more than participants

      with atypical genotype, regardless of tDCS condition.'
    supports: claim
  - section: Original source P5-S1-C6
    page: 5
    quote: 'Among participants who were randomized to receive A-tDCS

      during the aphasia treatment, those with typical BDNF genotype

      beneﬁtted more from the language treatment than those with

      atypical BDNF genotype.'
    supports: claim
  - section: Original source P1-S1-C8
    page: 1
    quote: 'Methods: Seventy-four individuals with chronic stroke-induced aphasia
      completed 15 language therapy

      sessions and were randomized to receive 1 mA A-tDCS or sham tDCS (S-tDCS) to
      the intact left tem-

      poroparietal region for the ﬁrst 20 min of each session.'
    supports: method
  - section: Original source P2-S4-C8
    page: 2
    quote: 'Genotyping for the SNP was

      accomplished using a TaqMan® single tube genotyping assay.'
    supports: method
  - section: Original source P3-S1-C11
    page: 3
    quote: 'A picture naming test consisting of 80

      items selected from the aphasia treatment paradigm; for the sake of

      brevity, we refer to this test as ‘Naming 80; ’ and 2.'
    supports: method
  - section: Original source P3-S1-C12
    page: 3
    quote: 'The Philadelphia

      Naming Test (PNT), which is also a picture naming test and is

      widely used in the literature [34].'
    supports: method
  - section: Original source P3-S3-C7
    page: 3
    quote: 'A mixed effects linear model of the repeated

      measures of proportional change in correct naming (calculated as

      described above) was ﬁt with the following independent variables:

      tDCS condition (A-tDCS or S-tDCS), BDNF genotype status (typical

      or atypical), tDCS x BDNF, time of testing (1 week post-, 4 weeks

      post-, 24 weeks post-treatment), tDCS x time, BDNF Genotype x

      tDCS x time, baseline WAB-AQ, and lesion size (time was consid-

      ered a classiﬁcation variable using SAS v 9.4 PROC MIXED repeated

      time/AR(1)).'
    supports: method
  - section: Original source P4-S2-C12
    page: 4
    quote: 'In the current study, the average time post-stroke at enrollment

      was greater than 3.5 years.'
    supports: sample
  - section: Original source P2-S4-C2
    page: 2
    quote: 'Therefore, BDNF

      genotype and post-treatment assessment data were available for

      66 participants.'
    supports: sample
  - section: Original source P5-S1-C1
    page: 5
    quote: '

      statistically signiﬁcant once group means were adjusted for time

      post-stroke and lesion size, which suggests these ﬁndings may

      reﬂect other potential differences besides BDNF genotype.'
    supports: confounders
predictor_type: clinical
short_definition: Interaction between typical BDNF genotype (val/val at rs6265, measured
  via TaqMan genotyping assay from whole blood) and receipt of 1 mA anodal tDCS (A-tDCS)
  to the left temporoparietal region during language therapy.
assessment:
- Naming 80
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2018BDNF
  proposal_id: R001
  review_status_sha256: 7f883182368e50edaee203227ad13f7a34ea876168c1b5e3040a2548e9631c91
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
        A/passages.json: 789d28ebdee9e2a254945dfbc1d77f60a8d595d9c4c092b4c99a41aac21db3d9
        A/raw.json: c8d472e1c24d46e477fb89807522b8617693b29ca46448d16a736556b7729935
        A/source-units.json: 5521a213665e9be949a87fff4338b54b09f3e4422e0dcd0e68ad1c0525ebf86a
        A/full-source-units.json: 2c501e282ed796ddb66a974ebceccc4f4afe268e574e34924dd051ee00bb27bc
        A/meta.json: 339160b9bec21250483c41575a762162b2e39035f0f2b8216532c5dd7ad75d5b
        A/table-images/page-5.png: 0ae09cbb1606fea8dfd6b65317968c5a0a7a21f778145680c945d7d6c5450c27
        A/table-images/page-4.png: fda957e80d19cb09318803cde80afcfbaf1eb3483ad33cf57882f0bd32a9be76
        A/table-images/TABLE-1-page-4-1.png: 3db8e1aef7d749d9f45036379238a4001da837448463f76fcab49123ae9d646d
        A/table-images/manifest.json: cc612d1a7288c52780ad5e53bbe0715107d29b3b79f278da7c7df6467a55ae15
        A/table-images/TABLE-2-page-5-1.png: 267e4e433c5c5fb85ae6cf98d7504690a61f693d4ee20af4b95a7854b4dbdcf7
        A/clauses/window-03/raw.json: a08843bcd02d600a0ae0891cdea5d37f9a3ea1bc727726968f3c9980d9bdce63
        A/clauses/window-03/prompt.txt: f1d129aff7c058500618c176b0fe13b3af11a0b593f8b60a087a3cb3cbbcb2af
        A/clauses/window-03/meta.json: c38d32398ff1553e9a247d96f5b1c0942e96c3a7d4bd9b418a601ea5004116bf
        A/clauses/window-04/raw.json: f06e3ec05af3f66afaefe8843b0e93bc110ae54f6524d37a8ed4fa2605a12b35
        A/clauses/window-04/prompt.txt: da0eb4bff14b84053afd04dbc196df2914b3d9ec6138e55e438b4eff8e56f0c9
        A/clauses/window-04/meta.json: d86c44639bbab1efb71d2b07c3ee2e9385a6b5d97ebfa3c676562b480cd8f983
        A/clauses/window-05/raw.json: 3e0a8213e3765dfce8f09248d36eae98d6c6eb15718d6a0adea58343ee96b8d6
        A/clauses/window-05/prompt.txt: 99e9f2b4e20cdb8c8b52cc774cad4123abe32623276a37ec73c02ddfc3cd24ba
        A/clauses/window-05/meta.json: bbcaeb6716dba0d04114b529f9fa411061351599a709c9c7d95c093ac97c305a
        A/clauses/window-02/raw.json: 7e34370ea5bfa5011eab6c574f75efcecb901234a70be0cbe9f58d26643d5f36
        A/clauses/window-02/prompt.txt: 4f95e938bd865db2a71558bd0b767ed5718cac3ee5d9c5f17477a8007d6ce93d
        A/clauses/window-02/meta.json: f9286bf7e9980bd324fdd829498d40c60befaec6263b8f9f5f5d09e2a5bb4d04
        A/clauses/window-07/raw.json: 6f4e2de50a3d3a0a6a072f72f0e666206a61e09f183ed65af865443e4fc5879c
        A/clauses/window-07/prompt.txt: 79aa98a70696f2b8b74c6fd31ee19506b64e700e5eb7387ae4bbc8626cb98c65
        A/clauses/window-07/meta.json: 9130d3f2a0d38d91651d78b1a1f09920b50be87707a599bbbb597f91f46c2c51
        A/clauses/window-01/raw.json: 99b59bd4b98add266231f02095cf5c03bdfbc3b628feeec6802bfc8f03457119
        A/clauses/window-01/prompt.txt: 64555b7be040973945eff1f89b917ad1200191572618d33208604bade8ea4295
        A/clauses/window-01/meta.json: d3959e16e74657390d8deb5d43682422531c3dc08381d1a2a9763cf14761b14d
        A/clauses/window-06/raw.json: a01da9fa6d0327d9b3b70450023a9c92310a865059ce15f5bd436a5866899b5f
        A/clauses/window-06/prompt.txt: b8d324741af702e11d0b4274c5237ba9da1563db5b514fa6f1b3829856fff7ec
        A/clauses/window-06/meta.json: 35976c3894c2a3f58234c071644c7f13c06517da7af26468b30aa06dbf072326
        A/tables/TABLE-2-page-5-2/raw.json: 802213915359864ecb8e32a2624c6de26d191ba0bd2c3016478ccf677eaa98cf
        A/tables/TABLE-2-page-5-2/prompt.txt: 609702c50cce8556c257b49fb184a9d1da7c7684674c4954a495056acd5584a4
        A/tables/TABLE-2-page-5-2/meta.json: 0d27ece3afe07d5ee1225b83fa15ff0bb175ffe4e05a162e1d6882710d95df87
        A/tables/TABLE-1-page-4-1/raw.json: 245e24e769661075e862ebd0c38fdee12f90ece7231393fb28b4d820a663158d
        A/tables/TABLE-1-page-4-1/prompt.txt: 3cc263e678c6b39586e4c8179c405bfdda20886c77b624a213e724133a28dc11
        A/tables/TABLE-1-page-4-1/meta.json: b85b8ed8d50ed5796e98fa8626ef50a31a88d2001b7d978af141c7e32681ebee
        B/passages.json: 789d28ebdee9e2a254945dfbc1d77f60a8d595d9c4c092b4c99a41aac21db3d9
        B/raw.json: 5fde07755a2eb73caa9efdbbc33fd213e1176feffb992ec3f5f800d5cc23672c
        B/source-units.json: 5521a213665e9be949a87fff4338b54b09f3e4422e0dcd0e68ad1c0525ebf86a
        B/full-source-units.json: 2c501e282ed796ddb66a974ebceccc4f4afe268e574e34924dd051ee00bb27bc
        B/meta.json: 56e16f8e6f89f6374fd6d2cba869a3ba0b60a2f6af4d5e364486739254d265e1
        B/table-images/page-5.png: 0ae09cbb1606fea8dfd6b65317968c5a0a7a21f778145680c945d7d6c5450c27
        B/table-images/page-4.png: fda957e80d19cb09318803cde80afcfbaf1eb3483ad33cf57882f0bd32a9be76
        B/table-images/TABLE-1-page-4-1.png: 3db8e1aef7d749d9f45036379238a4001da837448463f76fcab49123ae9d646d
        B/table-images/manifest.json: c83d41c5a463924dd052ddca9fd08de7e133b8a94ffb99657e1473a899807848
        B/table-images/TABLE-2-page-5-1.png: 267e4e433c5c5fb85ae6cf98d7504690a61f693d4ee20af4b95a7854b4dbdcf7
        B/clauses/window-03/raw.json: 2dc3cdb860fd205969d3d796eed224b66562021e733f559aa19bbd3afc4fefe5
        B/clauses/window-03/prompt.txt: f1d129aff7c058500618c176b0fe13b3af11a0b593f8b60a087a3cb3cbbcb2af
        B/clauses/window-03/meta.json: 533ab5207f6098451350fc36ab276680f57bf57a0439a549e5e78bc4c37aecce
        B/clauses/window-04/raw.json: 56829f0b6836ae5a21734d5c83c0e784f234cb88c05ce966e1446ef2d3a5b9d5
        B/clauses/window-04/prompt.txt: da0eb4bff14b84053afd04dbc196df2914b3d9ec6138e55e438b4eff8e56f0c9
        B/clauses/window-04/meta.json: f8d08d644ba645bc15705a86a3dc0e06da070a9d2319354dd636074db3d190d7
        B/clauses/window-05/raw.json: c75a3aeeeaf405bb3dc491b21d0fd91990edd83f1ca7ba651e85b9fb1bb69de4
        B/clauses/window-05/prompt.txt: 99e9f2b4e20cdb8c8b52cc774cad4123abe32623276a37ec73c02ddfc3cd24ba
        B/clauses/window-05/meta.json: bb366187a573886a4dea0ed1ac66e6c67d769a73e5bbaae634a6ab997237a822
        B/clauses/window-02/raw.json: 7b83f3f35dca889a6252dd93b5af7b41916c147a52e67a633333a84dc8b7d0a9
        B/clauses/window-02/prompt.txt: 4f95e938bd865db2a71558bd0b767ed5718cac3ee5d9c5f17477a8007d6ce93d
        B/clauses/window-02/meta.json: 76a885ebfc86f94b1abf825b9c7b9a0592b145cbbdb110ad19608704895223b0
        B/clauses/window-07/raw.json: 4593cff1c3597be55d2afb3c8abb31c689d6d9914951336139f7bfa4964e1c1b
        B/clauses/window-07/prompt.txt: 79aa98a70696f2b8b74c6fd31ee19506b64e700e5eb7387ae4bbc8626cb98c65
        B/clauses/window-07/meta.json: bd29463b0690d62066f7f118483a28023c82836fed6c4456a4b1a88e9947e8c6
        B/clauses/window-01/raw.json: fc1e36fd5f29463a0a610a231d0abb70132277eeba85d2ba7e77bd4f90b3dd73
        B/clauses/window-01/prompt.txt: 64555b7be040973945eff1f89b917ad1200191572618d33208604bade8ea4295
        B/clauses/window-01/meta.json: 47be2eff4140ffab419afbf793658641c79252bdf3e44e23a5e19aef9683f842
        B/clauses/window-06/raw.json: 42361558ae5f5e0eeb8bee2eb92162a476da0380e5709a790013382968ed3aff
        B/clauses/window-06/prompt.txt: b8d324741af702e11d0b4274c5237ba9da1563db5b514fa6f1b3829856fff7ec
        B/clauses/window-06/meta.json: 4ac04c657a4ecf37c8457e187e60489d14de1dcf3f1976e543d51dbe68a292f0
        B/tables/TABLE-2-page-5-2/raw.json: 8682cb9ec5a0358e13bf65049d45f8e0516eae9d1fd382aaacabcb6c5ff15060
        B/tables/TABLE-2-page-5-2/prompt.txt: 609702c50cce8556c257b49fb184a9d1da7c7684674c4954a495056acd5584a4
        B/tables/TABLE-2-page-5-2/meta.json: b9a862cce69bd75ca7fbe73060b03151166c3158daa1988c261e2417eaea8e23
        B/tables/TABLE-1-page-4-1/raw.json: 245e24e769661075e862ebd0c38fdee12f90ece7231393fb28b4d820a663158d
        B/tables/TABLE-1-page-4-1/prompt.txt: 3cc263e678c6b39586e4c8179c405bfdda20886c77b624a213e724133a28dc11
        B/tables/TABLE-1-page-4-1/meta.json: f112797a493d6298088f508897b5c62b35317755db164c3992a46539fb7f2eb7
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
      pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018BDNF
      source_status_sha256: 74bd0fbdce65de6839175ec188bdebea6feb6d9f1b5f01311f7b5390a6dc10ac
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: Interaction between A-tDCS and typical BDNF genotype (val/val)
    outcome:
      text: Treatment-related naming improvement
    analysis_label: Interaction analysis of tDCS and BDNF genotype
    relation: association
    evidence_ids:
    - P1-S2-C5
    - P4-S1-C8
    - P4-S1-C9
    - P4-S1-C10
    - P4-S2-C6
    - P5-S1-C6
    qualifier_ids:
    - P3-S3-C7
    - P5-S3-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018BDNF
      source_status_sha256: 74bd0fbdce65de6839175ec188bdebea6feb6d9f1b5f01311f7b5390a6dc10ac
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P2-S1-C12'
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P3-S3-C2
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S1-C6
      - Result passage disposed without unit P4-S1-C7
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S1-C9
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C9
      - Result passage disposed without unit P4-S1-C13
      - Result passage disposed without unit P4-S2-C14
      - Result passage disposed without unit P4-S2-C15
      - Result passage disposed without unit P4-S3-C7
      - Result passage disposed without unit P4-S3-C8
      - Result passage disposed without unit P4-S3-C9
      - Result passage disposed without unit P4-S4-C1
      - Result passage disposed without unit P5-S1-C1
      unattached_null_or_qualifier_ids:
      - P4-S1-C8
      - P4-S4-C1
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 155
      unselected_timing_passages:
      - P1-S1-C8
      - P2-S1-C11
      - P4-S1-C1
      - P4-S2-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P1-S1-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S3-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S3-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S3-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S1-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P3-S4
        - P4-S1
        - P5-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018BDNF
      source_status_sha256: 74bd0fbdce65de6839175ec188bdebea6feb6d9f1b5f01311f7b5390a6dc10ac
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant interaction between tDCS and genotype for naming
        improvement.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Describes the direction of the interaction effect.
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports results from a previous RCT (Ref 13), not the current genotype
        analysis.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the futility hypothesis of a previous RCT.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null relationship between genotype and race.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mean location of stimulation.
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides coordinate locations for stimulation.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Associates atypical genotype with severe language impairment at baseline.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Specifies WAB-AQ difference between genotype groups at baseline.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Associates atypical genotype with lower Naming 80 and PNT scores.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Reports no difference in PPTT, WAIS III, or NIHSS between groups.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports no difference in age, lesion size, education, or time post stroke.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports interaction between BDNF genotype and tDCS for naming improvement.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies that typical BDNF + A-tDCS improved more than typical BDNF
        + S-tDCS.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies that typical BDNF + A-tDCS improved more than atypical genotype.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports no main effect for BDNF genotype or tDCS condition.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Reports main effect of time of follow-up testing.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about stability of improvement over time.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports null interaction for tDCS vs time and three-way interaction.
    - source_id: P4-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Restatement of null interaction effects.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of significant effects.
    - source_id: P4-S2-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of baseline difference.
    - source_id: P4-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of the predicted interaction.
    - source_id: P4-S2-C14
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of null main effect for BDNF genotype.
    - source_id: P4-S2-C15
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of null difference in NIHSS.
    - source_id: P4-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of NIHSS sensitivity.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of non-significant differences in cortical damage and time
        post-stroke.
    - source_id: P4-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of age differences.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to Table 1.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical test used for Table 1.
    - source_id: P4-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains table formatting.
    - source_id: P4-S3-C12
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Table 1 data showing significant differences in AQ, Naming 80, PNT and
        null differences in others.
    - source_id: P4-S4-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Reports that adjusting for time and lesion size removes significance
        of BDNF genotype on AQ and PNT+Naming 80.
    - source_id: P4-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Footer for Table 1.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Restates that adjusted means for BDNF genotype were not significant.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies that typical BDNF genotype benefited more from treatment within
        the A-tDCS group.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Reports no difference in outcome between genotypes in the S-tDCS group.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Reports non-significant trend where atypical BDNF improved more in S-tDCS
        group.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to Table 2.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Table 2 results for interaction, main effects, and three-way interaction.
    unresolved_coverage:
    - source_id: P4-S1-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S3-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S3-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C6
    - P2-S2-C2
    - P2-S2-C3
    - P3-S2-C7
    - P3-S2-C12
    - P3-S3-C2
    - P4-S1-C13
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C15
    - P4-S2-C16
    - P4-S3-C7
    - P4-S3-C8
    - P4-S3-C9
    - P5-S3-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C10
      - P2-S4-C2
      - P3-S3-C10
      recruited_sample:
      - P1-S1-C8
      - P2-S3-C10
      eligibility:
      - P3-S1-C13
      - P4-S3-C2
      imaging_provenance:
      - P3-S2-C11
      imaging_timing: []
      outcome_timing:
      - P1-S1-C11
      - P1-S1-C12
      - P2-S2-C2
      - P3-S1-C14
      - P4-S1-C12
      outcome_definition:
      - P3-S1-C11
      - P3-S1-C16
      - P3-S2-C3
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C7
      - P3-S3-C7
      limitations:
      - P4-S3-C6
      - P4-S3-C7
      - P4-S3-C8
      - P5-S1-C2
      personal_factors: []
      tested_personal_effects:
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P5-S1-C6
      adjustment_roles:
      - P2-S1-C13
      - P3-S3-C7
      - P3-S3-C9
      - P4-S4-C3
      - P5-S3-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C10
      - P3-S3-C11
      - P3-S3-C12
      - P4-S1-C1
      - P4-S1-C2
      - P4-S4-C1
    outcome_type: change_from_baseline
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P1-S1-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S3-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S3-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S3-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S1-C9
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
      pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
      review_sha256: 7f883182368e50edaee203227ad13f7a34ea876168c1b5e3040a2548e9631c91
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
      - P1-S2-C5
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S2-C6
      - P5-S1-C6
      source_result: A significant interaction was detected between BDNF genotype
        and tDCS condition for treatment-related naming improvement (F=4.97, p=0.03).
        Participants with the typical val/val genotype who received anodal tDCS (A-tDCS)
        showed greater improvement than those with val/val who received sham tDCS,
        and greater improvement than participants with atypical genotype (Met carriers)
        regardless of tDCS condition. No main effects were found for BDNF genotype
        or tDCS condition alone.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The proposed core correctly identifies the analysis as an interaction
            between BDNF genotype and tDCS condition on naming improvement, matching
            the mixed-effects model described in P3-S3-C7 and results in P4-S1-C8.
          source_ids:
          - P3-S3-C7
          - P4-S1-C8
        direction:
          answer: fits
          reason: The claim that val/val + A-tDCS showed greater improvement than
            val/val + S-tDCS and atypical + any condition aligns with P1-S2-C6, P4-S1-C9,
            and P4-S1-C10. The direction of the association is preserved.
          source_ids:
          - P1-S2-C6
          - P4-S1-C9
          - P4-S1-C10
        construct:
          answer: fits
          reason: Exposure (BDNF val/val + A-tDCS), outcome (naming improvement),
            and population (chronic aphasia) are correctly identified. The measurement
            is behavioral (naming tests), not imaging-based, so 'non_imaging' is correct.
          source_ids:
          - P1-S1-C8
          - P3-S1-C10
          - P3-S1-C11
        qualifications:
          answer: fits
          reason: The qualifications regarding the mixed model adjustment for WAB-AQ
            and lesion size are present. The note about baseline differences losing
            significance after adjustment for time post-stroke and lesion size is
            also included, which is a material caveat from P4-S4-C1 and P5-S1-C1.
          source_ids:
          - P3-S3-C7
          - P4-S4-C1
          - P5-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveat that baseline severity differences
            may reflect other factors (time post-stroke, lesion size) and that depression
            was not assessed. No other material caveats appear to be missing from
            the provided source window.
          source_ids:
          - P5-S1-C1
          - P5-S1-C3
      optional_pending:
      - sample.time_post_onset
      - exact_p_value_for_interaction
      - effect_size_for_interaction
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - sample.time_post_onset
    - exact_p_value_for_interaction
    - effect_size_for_interaction
    normalizations:
    - field: sample.time_post_onset
      original: naming improvement measured at 1 week after completion of 15 language
        therapy sessions; average time post-stroke at enrollment was greater than
        3.5 years
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 15'
    analysis_identity:
      id: R001
      exposure:
        text: Interaction between A-tDCS and typical BDNF genotype (val/val)
      outcome:
        text: Treatment-related naming improvement
      analysis_label: Interaction analysis of tDCS and BDNF genotype
      relation: association
      evidence_ids:
      - P1-S2-C5
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S2-C6
      - P5-S1-C6
      qualifier_ids:
      - P3-S3-C7
      - P5-S3-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018BDNF
        source_status_sha256: 74bd0fbdce65de6839175ec188bdebea6feb6d9f1b5f01311f7b5390a6dc10ac
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 18c16fafda24c4e6e4947693958c8af0457880910d985a5f75ab97a427edfc2a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C8
          page: 1
          text_layer_sha256: 18c16fafda24c4e6e4947693958c8af0457880910d985a5f75ab97a427edfc2a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Methods: Seventy-four individuals with chronic stroke-induced
          aphasia completed 15 language therapy

          sessions and were randomized to receive 1 mA A-tDCS or sham tDCS (S-tDCS)
          to the intact left tem-

          poroparietal region for the ﬁrst 20 min of each session.'
        anchor_text: 'Methods: Seventy-four individuals with chronic stroke-induced
          aphasia completed 15 language therapy

          sessions and were randomized to receive 1 mA A-tDCS or sham tDCS (S-tDCS)
          to the intact left tem-

          poroparietal region for the ﬁrst 20 min of each session.'
        excluded_fragments: []
        image_sha256: b8980b4a96bb485d7a5dde39eb7c3849e17b3068272260597d75bef15d3a5790
      P4-S2-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 68105096919e2af5617917e75ad947b9c473debcba925c14816a111fdc410ba4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C12
          page: 4
          text_layer_sha256: 68105096919e2af5617917e75ad947b9c473debcba925c14816a111fdc410ba4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In the current study, the average time post-stroke at enrollment

          was greater than 3.5 years.'
        anchor_text: 'In the current study, the average time post-stroke at enrollment

          was greater than 3.5 years.'
        excluded_fragments: []
        image_sha256: 2782747471738ba81d832d5c54448b7fd98dab912587b101910a2fb1b7254f7e
        transcription: 'In the current study, the average time post-stroke at enrollment

          was greater than 3.5 years'
      P2-S4-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e586a6d48b6ef586371eeffd4488f0d8bd5fac00763d9acd6bf8cb4bbbce7757
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a8279ac0d05d6749ccaf9f64cf64e08713c37103a448a75ae5446eb08ad61c1c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C2
          page: 2
          text_layer_sha256: a8279ac0d05d6749ccaf9f64cf64e08713c37103a448a75ae5446eb08ad61c1c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Therefore, BDNF

          genotype and post-treatment assessment data were available for

          66 participants.'
        anchor_text: 'Therefore, BDNF

          genotype and post-treatment assessment data were available for

          66 participants.'
        excluded_fragments: []
        image_sha256: 5c560a7695302753304548b2711847085378d5dfea4f27e101b8e4460ced2723
        transcription: '. Therefore, BDNF

          genotype and post-treatment assessment data were available for

          66 participants'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Participants with val/val genotype who received A-tDCS

    showed greater response to aphasia treatment than val/val participants who received
    S-tDCS, as well as

    the Met allele carriers, regardless of tDCS condition.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
