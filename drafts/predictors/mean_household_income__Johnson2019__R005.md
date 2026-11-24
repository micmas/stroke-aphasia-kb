---
id: mean_household_income
name: mean household income
kind: predictor
findings:
- id: f1
  target: wab_aq_change
  target_kind: prognosis
  claim: mean household income was not correlated with change between the first and
    last WAB assessments, nor was it a significant predictor when entered into a linear
    mixed-effects model
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 39
    population: individuals in the chronic stage of a single-event, left-hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: first assessment at least 6 months postinjury, with subsequent
      assessments at least 6 months apart
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - convenience sample recruited through advertising and referrals
  - retrospective nature of the study
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: mean household income estimated based on a U.S. Census
    Bureau method. analysis was post hoc. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S3-C11,
    two-model agreement, human verification pending): . Thirty-nine indi-

    viduals (13 women, 26 men) with a mean age of 54.7 years

    (SD = 9.8) at the time of stroke met the inclusion criteria Original text-layer
    quotation is preserved below. PDF image reading (P2-S3-C10, two-model agreement,
    human verification pending): This study included individuals in the chronic stage

    of stroke at the time of both the initial assessment and

    subsequent assessments who (a) had two or more WAB

    assessments acquired at least 6 months apart; (b) had no

    accompanying neuropsychological disorders (self-report);

    (c) had a single-event, left-hemisphere ischemic stroke;

    and (d) were less than 85 years of age Original text-layer quotation is preserved
    below. PDF image reading (P1-S1-C7, two-model agreement, human verification pending):
    Participants were included if they had undergone 2 or

    more standardized language assessments acquired at time

    points at least 6 months apart, with the 1st assessment

    at least 6 months postinjury Original text-layer quotation is preserved below.'
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
    - proposed_concept:wab_aq_change
  citation: '@Johnson2019'
  source_passages:
  - section: Original source P5-S2-C5
    page: 5
    quote: 'In this

      post hoc analysis, mean household income was not correlated

      with change between the first and last WAB assessments

      (r = .20, p = .22), nor was it a significant predictor when

      entered into an LME model (F = −0.00003, p = .83); there-

      fore, this factor was not included in our final model.'
    supports: claim
  - section: Original source P2-S3-C11
    page: 2
    quote: 'Thirty-nine indi-

      viduals (13 women, 26 men) with a mean age of 54.7 years

      (SD = 9.8) at the time of stroke met the inclusion criteria.'
    supports: sample
  - section: Original source P2-S3-C10
    page: 2
    quote: 'This study included individuals in the chronic stage

      of stroke at the time of both the initial assessment and

      subsequent assessments who (a) had two or more WAB

      assessments acquired at least 6 months apart; (b) had no

      accompanying neuropsychological disorders (self-report);

      (c) had a single-event, left-hemisphere ischemic stroke;

      and (d) were less than 85 years of age.'
    supports: sample
  - section: Original source P1-S1-C7
    page: 1
    quote: 'Participants were included if they had undergone 2 or

      more standardized language assessments acquired at time

      points at least 6 months apart, with the 1st assessment

      at least 6 months postinjury.'
    supports: sample
  - section: Original source P5-S2-C3
    page: 5
    quote: 'Although direct information on SES was not avail-

      able in our database, an estimate of SES was calculated

      based on a U.S.'
    supports: method
  - section: Original source P2-S3-C5
    page: 2
    quote: 'These data represent a

      convenience sample and are based on recruitment through

      advertising, referrals from neurologists and speech patholo-

      gists, and active recruitment within support/aphasia groups.'
    supports: limitation
  - section: Original source P8-S2-C11
    page: 8
    quote: 'Additionally, because this

      study was retrospective in nature, changes to participant

      case history may have occurred and have been underre-

      ported.'
    supports: limitation
predictor_type: demographic
short_definition: mean household income estimated based on a U.S. Census Bureau method
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Johnson2019
  proposal_id: R005
  review_status_sha256: 0230bf7a2d856f3598f65ee8be74de9a0a6f90afc7b07f680b72261c61bdb74b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
        A/passages.json: c44110eb29b4d025bc3fcb9a5d3173bd2480efe6ef49d5ee4bcb1d244f692d0b
        A/raw.json: aade9f15ee3ad698300779f94693aca4f08a3566bd3a6f235a5b48847d50e888
        A/source-units.json: fb9031369bc7f4192ed649d85f916bfe7690c3b8f29ee47cf00f85294977ddfb
        A/full-source-units.json: 4e8057e3bddce019a9f1ece24258227d0059e40fba8dd49b4f43f5e35363fb9c
        A/meta.json: 329beb944bbf397a25f63a7b9603e6595f6d3b89f36a647dfe3de7361a1a35a9
        A/table-images/TABLE-1-page-3-1.png: c205347404a0101de385d6396476cac946930d39bf4cb0e4318f7821e860cc3a
        A/table-images/page-3.png: ae4c6e79c4dc25450097ca4d5afeb4a69f2501e0a09c1635ab2847c6be1b25ee
        A/table-images/page-6.png: 0e7d65d0e7761a3e7a82486870b47906e112ebd59179987ed4e99212c286c8f1
        A/table-images/page-4.png: bc27b5b08a30b4920c6a49c44dac312aedd2d09c904477b5cfa7486b0ff00290
        A/table-images/TABLE-3-page-6-1.png: e7da5978328da077c7477e6a25257d404f7636232b47a1285174411b53daaa42
        A/table-images/TABLE-2-page-4-2.png: f4265442a322c0470090c826fdfbe36c085ae824195e1d08c92ca9fa3bb8b38d
        A/table-images/manifest.json: 65e33a2eb806e0c4bb83bd2d78d5f79e62c826054e1eaaa33474052a8c83f457
        A/table-images/TABLE-2-page-4-1.png: 5e7f8d59b0275b078a285762624d8bb15fbce322eb1d25ecd4a3c754fc50c2fc
        A/clauses/window-03/raw.json: 49701c695c6b950b23f03e34678a13de91257f79fa1c3f7461f89183e482312a
        A/clauses/window-03/prompt.txt: b80d9145cfe8200272c6d3fa2c4c4b1f04d81333584fae9d95cacb66f41e1a82
        A/clauses/window-03/meta.json: 6d08861ccb61aec00d3299e096e97ccb1f28f2cbd0b76bf69e3020267f872076
        A/clauses/window-04/raw.json: 7c04fcc6e6724d2f6855d3d8ece03b84c5cf1b5a44c09e9884c6c35119a4737a
        A/clauses/window-04/prompt.txt: 7d0ea0f68e49e17791c9e0b73ad1a4a790b630a3974122d19a8bc2257eebc2ca
        A/clauses/window-04/meta.json: 8dd2037b8b996f3a5dc641d70f1f7370cc50c28a17c1dba09de62392e5163cac
        A/clauses/window-05/raw.json: 139002a5859239f259ce8f636e1b9d6bd37c1fd0361e6276451416cb9eb4d5be
        A/clauses/window-05/prompt.txt: dc1167dea1a5279287114e2464a8e280efe907489962ea98c5e52f6d1d91111b
        A/clauses/window-05/meta.json: 1f9719bfcf19357e4bfc9e4b3b3eae2c6334874269a9c5e8024f1d3fb257a31a
        A/clauses/window-02/raw.json: 9f16ca1d599d90d597e7087c36642a3c9460225527a3365f1a85855c843591f2
        A/clauses/window-02/prompt.txt: 2d1d7069d59eb0f67c3a8b72272b56d4dc1a587ca654e3f6408e1b90caf0bb9f
        A/clauses/window-02/meta.json: 384d8bbf4296c34d941a3dc477dfa0bf2c0f2981e455a8c6a29468ee3431751a
        A/clauses/window-07/raw.json: e04ecb9f3a4c3f1d667fa5d1b676050ecb060cf6ca1bb4919be1633902f79e27
        A/clauses/window-07/prompt.txt: 5482d262ba24cea8ebf1eaea7f0623a74f9f5df2af04d7db7cca3eab82b6bd29
        A/clauses/window-07/meta.json: ca742b98eed2711541e38b9716336146e6bcb75226aec3aec7ac3cde6a9e69c4
        A/clauses/window-01/raw.json: 6c5d064d4249c532e34419c37d5ddc2336a85c1c86d3bdf64f2ae0fbe9234560
        A/clauses/window-01/prompt.txt: 74e17052169429c439532d40acb7a964836f8d01462c013b3d29995762c51113
        A/clauses/window-01/meta.json: e4a7d099937f46db1184305e8878528077c33788efc63f65b3b9e083e85440fa
        A/clauses/window-06/raw.json: 36c8b02e76dc17ae0e2c618a03db292b72b02135c3da9e31e1b5130ce9340878
        A/clauses/window-06/prompt.txt: 49863452212efb55a66b1860e87ea7af592b8dac185478ddfd0075420b217e1b
        A/clauses/window-06/meta.json: fa3d6edce2ea09ebe3f13ee312c6e7e4c8a8fdfccd78aa55af9ca2fa4ecf2002
        A/tables/TABLE-3-page-6-3/raw.json: f69d1736a1fe96c4202eef3def8ae35e451501726e4cc1ba969aa19f52d50e70
        A/tables/TABLE-3-page-6-3/prompt.txt: 8dfda0da39dc466258372816de1f299ed6eb43e82896f43c1637bd0b87cb6251
        A/tables/TABLE-3-page-6-3/meta.json: 4fe70ad9b2495cd98a00cc8cb8bea58bbb23373adfd4682ff20a8a881cc9c442
        A/tables/TABLE-1-page-3-1/raw.json: d4c61ce45f3cffe9c1ebb2ae102867476ce668b225c92952d4f22f32dfe0cd07
        A/tables/TABLE-1-page-3-1/prompt.txt: c7bfa081db9b399320d3b62488694d06fead75f5ca4c8c8f335414de4a1e3184
        A/tables/TABLE-1-page-3-1/meta.json: 7acbfb25c4cc4c9b1d98b11604fc289f5281a96e588ac2b53e73a6703edd7d63
        A/tables/TABLE-2-page-4-2/raw.json: cd9c4fa8974372a7a0d3e63ac3e9ba29bf4d301e28be4e75a966435dcd0d45f3
        A/tables/TABLE-2-page-4-2/prompt.txt: daeaadc03c3db27f6d9986c2e36fed6fb4f2138b9c6ba42f0133928cbd33e912
        A/tables/TABLE-2-page-4-2/meta.json: e72f9551082beef47980971d919717c2f02333e6d913b38416882947b63fc0dd
        B/passages.json: c44110eb29b4d025bc3fcb9a5d3173bd2480efe6ef49d5ee4bcb1d244f692d0b
        B/raw.json: bd2a7628135e26a169a125a6039c5fcf8e0de03e8f302c7249d6da45313066a2
        B/source-units.json: fb9031369bc7f4192ed649d85f916bfe7690c3b8f29ee47cf00f85294977ddfb
        B/full-source-units.json: 4e8057e3bddce019a9f1ece24258227d0059e40fba8dd49b4f43f5e35363fb9c
        B/meta.json: fe67b5f7385b687c6a36fc3027e74970ad65e8665f010d1aa38671ef3e5bb1f8
        B/table-images/TABLE-1-page-3-1.png: c205347404a0101de385d6396476cac946930d39bf4cb0e4318f7821e860cc3a
        B/table-images/page-3.png: ae4c6e79c4dc25450097ca4d5afeb4a69f2501e0a09c1635ab2847c6be1b25ee
        B/table-images/page-6.png: 0e7d65d0e7761a3e7a82486870b47906e112ebd59179987ed4e99212c286c8f1
        B/table-images/page-4.png: bc27b5b08a30b4920c6a49c44dac312aedd2d09c904477b5cfa7486b0ff00290
        B/table-images/TABLE-3-page-6-1.png: e7da5978328da077c7477e6a25257d404f7636232b47a1285174411b53daaa42
        B/table-images/TABLE-2-page-4-2.png: f4265442a322c0470090c826fdfbe36c085ae824195e1d08c92ca9fa3bb8b38d
        B/table-images/manifest.json: 4da6687c7f9405208e71be71bf3f392594848d8f87450eb3d79415d78617f4d9
        B/table-images/TABLE-2-page-4-1.png: 5e7f8d59b0275b078a285762624d8bb15fbce322eb1d25ecd4a3c754fc50c2fc
        B/clauses/window-03/raw.json: b389da252886a99e26e1c86e59ff418906586f2ef9aa3f75e48a4d534f64c69c
        B/clauses/window-03/prompt.txt: b80d9145cfe8200272c6d3fa2c4c4b1f04d81333584fae9d95cacb66f41e1a82
        B/clauses/window-03/meta.json: 574fffde31ebd269d05ede48379d04e65a4b057ab91267c94afa6e9a5c5cd79a
        B/clauses/window-04/raw.json: 146b94d1dcac1925ddf930187b2996c68d0736f373e76d46c628bcdcc3ca4a06
        B/clauses/window-04/prompt.txt: 7d0ea0f68e49e17791c9e0b73ad1a4a790b630a3974122d19a8bc2257eebc2ca
        B/clauses/window-04/meta.json: ae2daa451410fb6298bbac88bb12b0e4668cee5877d0037ad6ccaaf4ddd010a7
        B/clauses/window-05/raw.json: bc61dea5e02d07208e82759f5db70be4753b817aa3a018ef2f7c63cbdfe89523
        B/clauses/window-05/prompt.txt: dc1167dea1a5279287114e2464a8e280efe907489962ea98c5e52f6d1d91111b
        B/clauses/window-05/meta.json: 2e574e9b7c81a4e81851e235d180c3a568a0428ee9c55357701a7a331cbe04c9
        B/clauses/window-02/raw.json: 9ddafb14ba577b54fd5b8eaf6b0580ce439ae4c6acc6530a1b08e950953ef748
        B/clauses/window-02/prompt.txt: 2d1d7069d59eb0f67c3a8b72272b56d4dc1a587ca654e3f6408e1b90caf0bb9f
        B/clauses/window-02/meta.json: 0e14c74733e2a9aed18c6a1a1b494bda99e9fa7194d344d8aa22aedc27c1d6e5
        B/clauses/window-07/raw.json: e04ecb9f3a4c3f1d667fa5d1b676050ecb060cf6ca1bb4919be1633902f79e27
        B/clauses/window-07/prompt.txt: 5482d262ba24cea8ebf1eaea7f0623a74f9f5df2af04d7db7cca3eab82b6bd29
        B/clauses/window-07/meta.json: b52351a09a0f2f45733c4f6fe1a3d0a8200a53be0edfdb56645d7ea6cae54ee4
        B/clauses/window-01/raw.json: 2d1e613142104c2789b50ed9c293117789cfb48ddf217a815fbe8088c51641f7
        B/clauses/window-01/prompt.txt: 74e17052169429c439532d40acb7a964836f8d01462c013b3d29995762c51113
        B/clauses/window-01/meta.json: 1817c34e835e0be82eb2c97e16c16c2006a19810364f2ad1e3aba8e4d1ff11bd
        B/clauses/window-06/raw.json: dc6066f537f9e6df7fb421304674301ab5caf88bb30e590e566c86ee35078f00
        B/clauses/window-06/prompt.txt: 49863452212efb55a66b1860e87ea7af592b8dac185478ddfd0075420b217e1b
        B/clauses/window-06/meta.json: 8be3565d58938468444eebc182e2d908798ac6e92752536ded1c3e6ef47a37a1
        B/tables/TABLE-3-page-6-3/raw.json: e1d1ffbaff75a97bb70b45a213bf9eeb4d42f155811151c62b5009e255d1bdc1
        B/tables/TABLE-3-page-6-3/prompt.txt: 8dfda0da39dc466258372816de1f299ed6eb43e82896f43c1637bd0b87cb6251
        B/tables/TABLE-3-page-6-3/meta.json: 5acb4fbcb21e2045970de0d68b916805aa720923ca51dac0f371bfc8833860d6
        B/tables/TABLE-1-page-3-1/raw.json: 96e1b646e035cb7ddc28befa17afe6edccfd2f71ae8a1fc64ebeea96b9e5fc77
        B/tables/TABLE-1-page-3-1/prompt.txt: c7bfa081db9b399320d3b62488694d06fead75f5ca4c8c8f335414de4a1e3184
        B/tables/TABLE-1-page-3-1/meta.json: 0342335891b4bbc6f04771989422b536d57702549594317f99f71e987a94e322
        B/tables/TABLE-2-page-4-2/raw.json: 68fd36df3eaf5f30539fa7556001b67bc0a36f327cc76a7fc6cfaced7817f575
        B/tables/TABLE-2-page-4-2/prompt.txt: daeaadc03c3db27f6d9986c2e36fed6fb4f2138b9c6ba42f0133928cbd33e912
        B/tables/TABLE-2-page-4-2/meta.json: deda5adbed218a577d471657d341db792dd60558fac8b3b8f376c91df5949afb
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
      pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2019
      source_status_sha256: 4dfb6c872c1d86486aa73a5339d9b4c9a395dd60491bb1377c10d51ede4fcae4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: mean household income
    outcome:
      text: change between first and last WAB assessments
    analysis_label: Post hoc analysis
    relation: association
    evidence_ids:
    - P5-S2-C5
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
      pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2019
      source_status_sha256: 4dfb6c872c1d86486aa73a5339d9b4c9a395dd60491bb1377c10d51ede4fcae4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C12
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P3-S1-C9
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P6-S1-C1
      - Accounting without a linked unit P8-S1-C12
      - Accounting without a linked unit P8-S1-C5
      - Result passage disposed without unit P8-S2-C6
      - Unaccounted source passage P8-S1-C5
      - Unaccounted source passage P8-S1-C12
      - Result passage disposed without unit P8-S3-C13
      - Result passage disposed without unit P8-S4-C1
      unattached_null_or_qualifier_ids:
      - P1-S1-C9
      - P8-S1-C5
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 149
      unselected_timing_passages:
      - P1-S1-C6
      - P1-S1-C7
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C13
      - P5-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P5-S2
        - P7-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2019
      source_status_sha256: 4dfb6c872c1d86486aa73a5339d9b4c9a395dd60491bb1377c10d51ede4fcae4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of improvement/decline/stability across participants,
        not a relationship between exposure and outcome.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: States treatment hours predict improvement and older stroke age is associated
        with decline.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Identifies significant interactions for exercise and age in individuals
        with diabetes.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of stroke age and treatment as influencing recovery.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of exercise improving outcomes for those with diabetes.
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline group mean WAB-AQ and time poststroke.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Average months between assessments.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of WAB assessments relative to treatment.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mean time postonset at initial administration.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mean time postonset at initial administration.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes: []
      reason: 'Null finding: no significant differences for AQ at baseline between
        subgroups.'
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes: []
      reason: 'Null finding: no statistical differences for age of stroke between
        subgroups.'
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Timing of first WAB relative to treatment.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Identifies significant main effects for age at stroke and treatment
        hours.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Quantifies the effect of age and treatment hours on WAB-AQ.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Identifies significant interactions involving diabetes.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Quantifies exercise effect for individuals with diabetes.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Quantifies age effect for individuals with diabetes.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Null finding for household income as a predictor of WAB change.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of number of participants showing improvement.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of study goals.
    - source_id: P6-S2-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of negative effect of age at stroke onset.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Restates interaction between exercise and diabetes.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies significant interaction between age at stroke and diabetes.
    - source_id: P8-S1-C12
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: General conclusion about age and diabetes effects.
    - source_id: P8-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: General support for aphasia treatment in chronic patients.
    - source_id: P8-S3-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion that treatment is a reliable predictor of recovery.
    - source_id: P8-S3-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion that receiving treatment increases likelihood of recovery.
    - source_id: P8-S4-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion that receiving treatment increases likelihood of recovery.
    unresolved_coverage:
    - source_id: P5-S1-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P5-S1-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C12
    - P1-S1-C13
    - P2-S3-C12
    - P2-S3-C13
    - P3-S1-C9
    - P4-S1-C12
    - P4-S2-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C7
    - P5-S2-C6
    - P6-S1-C1
    - P6-S2-C7
    - P8-S1-C12
    - P8-S2-C6
    - P8-S3-C9
    - P8-S3-C13
    - P8-S4-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C3
      recruited_sample:
      - P2-S3-C3
      eligibility:
      - P1-S1-C7
      - P2-S3-C10
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P4-S2-C2
      outcome_definition:
      - P3-S1-C10
      - P4-S1-C5
      validation: []
      analysis_restrictions:
      - P4-S1-C4
      dependent_variable_statement:
      - P1-S1-C8
      - P4-S1-C5
      limitations:
      - P7-S1-C7
      - P8-S1-C13
      - P8-S2-C9
      - P8-S2-C10
      - P8-S2-C11
      - P8-S3-C2
      - P8-S3-C4
      personal_factors:
      - P3-S2-C1
      - P4-S1-C5
      tested_personal_effects:
      - P1-S1-C10
      - P1-S1-C11
      - P5-S1-C9
      - P5-S1-C11
      - P5-S1-C12
      - P5-S2-C5
      - P7-S1-C5
      adjustment_roles:
      - P4-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C5
      - P4-S1-C6
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
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
      pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
      review_sha256: 0230bf7a2d856f3598f65ee8be74de9a0a6f90afc7b07f680b72261c61bdb74b
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
      - P5-S2-C5
      source_result: In a post hoc analysis, mean household income was not correlated
        with change between the first and last WAB assessments (r = .20, p = .22),
        nor was it a significant predictor when entered into a linear mixed-effects
        model (F = -0.00003, p = .83); consequently, it was not included in the final
        model.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the post hoc examination of mean household
            income as a predictor of WAB-AQ change, distinct from the primary LME
            model which included other demographic factors. The source explicitly
            labels this as a 'post hoc analysis' in P5-S2-C5.
          source_ids:
          - P5-S2-C5
          - P5-S2-C3
        direction:
          answer: fits
          reason: The source states that mean household income was 'not correlated'
            and 'not a significant predictor', which aligns with the 'no_effect' direction
            in the proposed core. The p-values (.22 and .83) confirm the lack of statistical
            significance.
          source_ids:
          - P5-S2-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as 'mean household income'
            (estimated via U.S. Census Bureau method per P5-S2-C3/C4). The outcome
            is 'change between first and last WAB assessments' (WAB-AQ change). The
            method is behavioral (WAB), not imaging.
          source_ids:
          - P5-S2-C5
          - P5-S2-C3
          - P5-S2-C4
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis was
            'post hoc', which is explicitly stated in the source (P5-S2-C5). It also
            notes the convenience sample and retrospective nature, which are valid
            limitations mentioned in P2-S3-C5 and P8-S2-C11.
          source_ids:
          - P5-S2-C5
          - P2-S3-C5
          - P8-S2-C11
        missing_material_caveat:
          answer: fits
          reason: 'The core captures the essential context: it is a post hoc analysis,
            the sample is a convenience sample, and the study is retrospective. No
            material caveats that would change the interpretation of the null result
            for income are omitted.'
          source_ids:
          - P5-S2-C5
          - P2-S3-C5
          - P8-S2-C11
      optional_pending:
      - Specific correlation coefficient (r=.20) and p-value (p=.22) for the correlation
      - Specific F-statistic (F=-0.00003) and p-value (p=.83) for the LME model
      - Details of the U.S. Census Bureau method used to estimate SES
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific correlation coefficient (r=.20) and p-value (p=.22) for the correlation
    - Specific F-statistic (F=-0.00003) and p-value (p=.83) for the LME model
    - Details of the U.S. Census Bureau method used to estimate SES
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: mean household income
      outcome:
        text: change between first and last WAB assessments
      analysis_label: Post hoc analysis
      relation: association
      evidence_ids:
      - P5-S2-C5
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
        pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
        source_review: _compare/relationships-2026-11-16/review-current/Johnson2019
        source_status_sha256: 4dfb6c872c1d86486aa73a5339d9b4c9a395dd60491bb1377c10d51ede4fcae4
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fe3797f2af7b97cec1314d3fd9be9650ac3b31843af8cca874053fcd3639adbe
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C11
          page: 2
          text_layer_sha256: fe3797f2af7b97cec1314d3fd9be9650ac3b31843af8cca874053fcd3639adbe
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Thirty-nine indi-

          viduals (13 women, 26 men) with a mean age of 54.7 years

          (SD = 9.8) at the time of stroke met the inclusion criteria.'
        anchor_text: 'Thirty-nine indi-

          viduals (13 women, 26 men) with a mean age of 54.7 years

          (SD = 9.8) at the time of stroke met the inclusion criteria.'
        excluded_fragments: []
        image_sha256: 96b023ceecd6380439a8b7b083df82bccfd6ae71936feaf61ec9af103f09ced8
        transcription: '. Thirty-nine indi-

          viduals (13 women, 26 men) with a mean age of 54.7 years

          (SD = 9.8) at the time of stroke met the inclusion criteria'
      P2-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a9b06fccb5259016873470d2bf0612a998952edc0cbac68e4c6d82e0c92ebb3e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C10
          page: 2
          text_layer_sha256: a9b06fccb5259016873470d2bf0612a998952edc0cbac68e4c6d82e0c92ebb3e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'This study included individuals in the chronic stage

          of stroke at the time of both the initial assessment and

          subsequent assessments who (a) had two or more WAB

          assessments acquired at least 6 months apart; (b) had no

          accompanying neuropsychological disorders (self-report);

          (c) had a single-event, left-hemisphere ischemic stroke;

          and (d) were less than 85 years of age.'
        anchor_text: 'This study included individuals in the chronic stage

          of stroke at the time of both the initial assessment and

          subsequent assessments who (a) had two or more WAB

          assessments acquired at least 6 months apart; (b) had no

          accompanying neuropsychological disorders (self-report);

          (c) had a single-event, left-hemisphere ischemic stroke;

          and (d) were less than 85 years of age.'
        excluded_fragments: []
        image_sha256: 9b487566ca047b6fd53f6d499484eb0e91e537b01ee9958a3effa61bf3289dd6
        transcription: 'This study included individuals in the chronic stage

          of stroke at the time of both the initial assessment and

          subsequent assessments who (a) had two or more WAB

          assessments acquired at least 6 months apart; (b) had no

          accompanying neuropsychological disorders (self-report);

          (c) had a single-event, left-hemisphere ischemic stroke;

          and (d) were less than 85 years of age'
      P1-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 72ea0a788c523b6b28714c92979acb0a34fd5ab374de58b2310cda5409b8cb27
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7127cfb83bc4e7766ce149eb36c2941b8d5ff0985597b779e2ed1bc88f1ce48f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C7
          page: 1
          text_layer_sha256: 7127cfb83bc4e7766ce149eb36c2941b8d5ff0985597b779e2ed1bc88f1ce48f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants were included if they had undergone 2 or

          more standardized language assessments acquired at time

          points at least 6 months apart, with the 1st assessment

          at least 6 months postinjury.'
        anchor_text: 'Participants were included if they had undergone 2 or

          more standardized language assessments acquired at time

          points at least 6 months apart, with the 1st assessment

          at least 6 months postinjury.'
        excluded_fragments: []
        image_sha256: ddfa9970577f4f5a150625903ea4e104df110c0c2b000829d917867dbe887a6a
        transcription: 'Participants were included if they had undergone 2 or

          more standardized language assessments acquired at time

          points at least 6 months apart, with the 1st assessment

          at least 6 months postinjury'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'In this

    post hoc analysis, mean household income was not correlated

    with change between the first and last WAB assessments

    (r = .20, p = .22), nor was it a significant predictor when

    entered into an LME model (F = −0.00003, p = .83); there-

    fore, this factor was not included in our final model.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
