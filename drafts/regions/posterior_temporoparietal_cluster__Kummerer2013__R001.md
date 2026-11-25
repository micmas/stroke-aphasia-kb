---
id: posterior_temporoparietal_cluster
name: posterior temporoparietal cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: repetition_impairment
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: repetition_impairment
  target_kind: impairment
  claim: repetition impairments were mainly associated with lesions located in the
    posterior temporoparietal region with a statistical lesion maximum in the periventricular
    white matter in projection of the dorsal superior longitudinal and arcuate fasciculus
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 100
    population: native German-speaking patients with acute aphasia caused by ischaemic
      stroke
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
  - haemodynamic infarcts were not explicitly excluded
  - structural MRI limitations for white-matter labels (projection of tracts)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: voxelwise lesion overlap in the posterior temporoparietal
    region, with a statistical maximum in the periventricular white matter in projection
    of the dorsal superior longitudinal and arcuate fasciculus. repetition impairment
    was measured as a principal component of 6 subtest scores; analysis used the Brunner-Munzel
    rank test; only voxels affected in at least 10 patients were considered. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S2-C3, two-model agreement, human verification pending):
    To test this hypothesis, we conducted a voxelwise lesion-behaviour mapping (VLBM;
    Rorden et al., 2007) study in a large cohort of 100 acute stroke patients Original
    text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:repetition_impairment
  citation: '@Kummerer2013'
  source_passages:
  - section: Original source P1-S2-C3
    page: 1
    quote: 'We found that

      repetition impairments were mainly associated with lesions located in the posterior
      temporoparietal region with a statistical lesion

      maximum in the periventricular white matter in projection of the dorsal superior
      longitudinal and arcuate fasciculus.'
    supports: claim
  - section: Original source P2-S2-C3
    page: 2
    quote: 'To

      test

      this

      hypothesis,

      we

      conducted

      a

      voxelwise

      lesion-behaviour mapping (VLBM; Rorden et al., 2007) study in

      a large cohort of 100 acute stroke patients.'
    supports: method
  - section: Original source P2-S3-C4
    page: 2
    quote: "Finally, we included 100 native German-speaking patients\n(mean age 62\
      \ years, 67 male, 6 left-handed) with acute aphasia\ncaused by ischaemic stroke\
      \ (Table 1), who were examined on average\n3 \x02 2.6 (\x02 SD) days after onset."
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Speciﬁcally, we performed the Brunner–Munzel test, a rank

      test for continuous behavioural variables and binary images to identify

      lesioned voxels associated with repetition or comprehension deﬁcits.'
    supports: method
  - section: Original source P4-S2-C8
    page: 4
    quote: 'To increase statistical power, only voxels affected

      in at least 10 patients were considered for analysis.'
    supports: method
  - section: Original source P5-S2-C5
    page: 5
    quote: 'The principle component analysis across the 12 repetition and

      comprehension scores revealed two distinct components that

      could be assigned either to the repetition or comprehension tests

      based on the correlations of the factor loadings with the respective

      test scores (Table 1).'
    supports: method
  - section: Original source P5-S3-C2
    page: 5
    quote: 'Impairments of repetition (Fig. 2B) were associated with lesions

      of the superior and middle temporal gyrus, the parietal operculum,

      primary sensory-motor and premotor cortex, posterior insular

      cortex as well as large subcortical tissue.'
    supports: claim
  - section: Original source P5-S3-C3
    page: 5
    quote: "The statistically most\nsigniﬁcant voxels were found in the deep white\
      \ matter of the\nfrontal semioval centre (\x0636, \x0620, 28; z = 9.5) and the\
      \ posterior\ntemporal cortex (\x0630, \x0624, 8; z = 8.7) in projection of the\
      \ arcu-\nate and superior longitudinal fascicle ﬁbres, respectively, and in\
      \ the\nposterior most part of the insular cortex (\x0638, \x0612, \x061; z =\
      \ 7.1)."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kummerer2013
  proposal_id: R001
  review_status_sha256: a5cfafc45c00763efb5f32245f05823e544ce6ac131697c94d08dbbb3a57eda4
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
        A/passages.json: f9750d9c7f4e2594a5b683a3f7c7f211627387b079cf695294376c582537ded9
        A/raw.json: 118bbc3bc7660f16cf9ee9ed936f65ee5c7a4e6910175a1854f95166203bcfcc
        A/source-units.json: c420e5bbe2d143936c5ff36dc888e8eaeabdc39e5ef7c56c4bfaa3b320823c74
        A/full-source-units.json: bc33377deac7175608ecbf4ad96d3959f9a8352cc812a778bd5772ff71d5d318
        A/meta.json: bc0d3c4166fb6299cffdf2e7d64df730ba72ef4c6b7ffd724f6245ff5f98469a
        A/table-images/TABLE-1-page-3-1.png: 9d54ddfb777fa4a00c043ea6f84d1fa7a7c66c66b249d40cb0a75cae2aa59947
        A/table-images/page-3.png: 6be1fadec5505bfa15a25edc7dc3ed1cb1bfb660db293cc2c2ea7f04c9b7213d
        A/table-images/manifest.json: 59f5d78c0780ee8fcf57abb3ac5d5f908fc0aa283db81242c53af393535c1edd
        A/clauses/window-03/raw.json: f5ed3af5d2e1fb2c8851100169b1d92f9f1cb686d749bb5bd064ec9923cb4093
        A/clauses/window-03/prompt.txt: 7dee1a4898b0d33b8a46f240ccafbb64b293f645346a8cbca45515112d6ea59b
        A/clauses/window-03/meta.json: 3f979a803989b6fecc88c5e2ec25dffadc716a611d96395f7f3c29286a493f01
        A/clauses/window-04/raw.json: 8abf2a184f6d242fdb6dbe7784107af7827321b6f3866884e2e2bf1ef8a46ee8
        A/clauses/window-04/prompt.txt: 00102f8d4179c0ae6935e8a9ed423acdee0bfa26afbd73a43958d576e6844bde
        A/clauses/window-04/meta.json: 16455015e33e2e0a0d0bda0f92bde763164d83be539ed2449455503921bf4d00
        A/clauses/window-05/raw.json: 7744f5a7e8a2e70dac8a404c96c27374e501bfb3aac44abeb0953d73871ebe09
        A/clauses/window-05/prompt.txt: 9a157ecb4f2d3baa8052eea775cbbe6f2f1fc827c2ccba7aa454610ad1990999
        A/clauses/window-05/meta.json: 30c0070e42397cc80faa763a82e1ba03e7d56c875b8f7c0c6e8d0888f5924747
        A/clauses/window-02/raw.json: 689dfd26635e5ace4165bc1ca910a8c29d9c06c7ca0dc50776c823d4222e42c8
        A/clauses/window-02/prompt.txt: 1ec4bcad095e4d0149a9d8c571940eb858a93717e703511f0b54f79b390bc652
        A/clauses/window-02/meta.json: 11a650158bec555cfffd28b04fe9f034acba08125b360747df72ab24491cb930
        A/clauses/window-07/raw.json: 313a778d9a41fe9507ed3a32b2293a104f556819e01ec194c3149c30819da0fc
        A/clauses/window-07/prompt.txt: 2b6b728e027572ee38eb492c34be6c3fbd54490561b8fa86059fba65d843db85
        A/clauses/window-07/meta.json: d8e53ff066099c4c73c7619b99ac0a00b4df68408162ab628ad5cd8d39a8e49e
        A/clauses/window-01/raw.json: 78419e34248bcb0f40cabfd869fb9bc0a8c4684afa6cea195637fdab084285fc
        A/clauses/window-01/prompt.txt: bf7da9e25c0b03b7df88dcbaa9427634ccde0947654c7cc3c897b009141dc7a2
        A/clauses/window-01/meta.json: f8bcdbfc99c07e2a663ab0137469461bba7a10746aeac033e5baedb841f9790c
        A/clauses/window-06/raw.json: b5d03bcf25b03a0d82debf2fe8f544e864fe2bb5f18066b4259d28a738050d24
        A/clauses/window-06/prompt.txt: 8f6681e055748d74592e52b5cdeee003df28ce35e68a4cd52d61b2dcae3995a5
        A/clauses/window-06/meta.json: 76c88edbb061c7916ed7f591b36eed89b0163737255cdfea011b5fdff001f609
        A/clauses/window-08/raw.json: c215d15308758d84559accefeacdb1799cd1fd31ec929954f89f7f3287ead32c
        A/clauses/window-08/prompt.txt: 67debde6234dd867d80dcd646430579bff1e775524c41a8889d112ec36724c83
        A/clauses/window-08/meta.json: e607c33e29d18515a376e4f593c3d1fd72ec51cf5d9818329ad24091b93ba32f
        A/tables/TABLE-1-page-3-1/raw.json: 1b88108d4649e9872cafcff1db06d59afa18e06d961e2c0f70822de0867c7c16
        A/tables/TABLE-1-page-3-1/prompt.txt: 948ce244dccd60748334ee5275cc4ac35972300a3c985124845fe3e9ef9dc327
        A/tables/TABLE-1-page-3-1/meta.json: 36184f401b1c2c1ee17a646812cf39602920347cfd0aacebf4bb016e11f7ca4e
        B/passages.json: f9750d9c7f4e2594a5b683a3f7c7f211627387b079cf695294376c582537ded9
        B/raw.json: 921e5c2498a6225773a4092b11b26f425168273895c7b82bafcc43b5ffe5f4b8
        B/source-units.json: c420e5bbe2d143936c5ff36dc888e8eaeabdc39e5ef7c56c4bfaa3b320823c74
        B/full-source-units.json: bc33377deac7175608ecbf4ad96d3959f9a8352cc812a778bd5772ff71d5d318
        B/meta.json: d5348f56675ef25c45f5e43dd05f58f71f054c769e8c96e4fb5233826177fb44
        B/table-images/TABLE-1-page-3-1.png: 9d54ddfb777fa4a00c043ea6f84d1fa7a7c66c66b249d40cb0a75cae2aa59947
        B/table-images/page-3.png: 6be1fadec5505bfa15a25edc7dc3ed1cb1bfb660db293cc2c2ea7f04c9b7213d
        B/table-images/manifest.json: bb250f8e8aaedcaec0a1233188e6940ca31573ecf8fb0647e360b577f3ab8d07
        B/clauses/window-03/raw.json: 61af21366a952aac55840ccfb0c48c609eabf5f308ea0e5c57e9b98821fa366a
        B/clauses/window-03/prompt.txt: 7dee1a4898b0d33b8a46f240ccafbb64b293f645346a8cbca45515112d6ea59b
        B/clauses/window-03/meta.json: 253a4a1d68b9ececd65968df25511dbb5277f57de5ea324656bac258b243534e
        B/clauses/window-04/raw.json: 112270d2c3ac25df98457af67c9c095f3860f8b14d5a4dda0772c40d670a817a
        B/clauses/window-04/prompt.txt: 00102f8d4179c0ae6935e8a9ed423acdee0bfa26afbd73a43958d576e6844bde
        B/clauses/window-04/meta.json: 9cb6eb5aa9c3ab9bb01d18a658615b85500c63b69915a9f6eb0f55b15ad95619
        B/clauses/window-05/raw.json: e32c9acc34ee2901f79df6ac2cb63ae83dfb3004d6be08355b4f400b18a86182
        B/clauses/window-05/prompt.txt: 9a157ecb4f2d3baa8052eea775cbbe6f2f1fc827c2ccba7aa454610ad1990999
        B/clauses/window-05/meta.json: 546c118d3d62d75c961f999c1801fe698d12e2716070548632ea731f13f62d9f
        B/clauses/window-02/raw.json: 85215c22e5620e74b2e86bc86b6c911a85547fc6ef663c09c66131030daf17c6
        B/clauses/window-02/prompt.txt: 1ec4bcad095e4d0149a9d8c571940eb858a93717e703511f0b54f79b390bc652
        B/clauses/window-02/meta.json: 81de129a1a39479ac313d0f3a9dfccbe7577cab908f084c2cc0071368793d887
        B/clauses/window-07/raw.json: 4d369165b4288089e00e2da3166befbe7ac0c1bd7b89c1106c7be822778b4b50
        B/clauses/window-07/prompt.txt: 2b6b728e027572ee38eb492c34be6c3fbd54490561b8fa86059fba65d843db85
        B/clauses/window-07/meta.json: be73190257a6336264ec2a0711851bcb6b078c92c2819495907c2e7e43332053
        B/clauses/window-01/raw.json: e4b4a705030deb56391fac754e7b3757301e0810642985ec3c4fd2d42c6b037a
        B/clauses/window-01/prompt.txt: bf7da9e25c0b03b7df88dcbaa9427634ccde0947654c7cc3c897b009141dc7a2
        B/clauses/window-01/meta.json: 456884dc1b75d78210b1035f69269e107d5f39767e1364ef7deac4b10467b8ba
        B/clauses/window-06/raw.json: c6b8ead190d13edadf1b402595856e00316b1a1ac297dfc392ddba75bbf0ee30
        B/clauses/window-06/prompt.txt: 8f6681e055748d74592e52b5cdeee003df28ce35e68a4cd52d61b2dcae3995a5
        B/clauses/window-06/meta.json: 3019347468b413bc715b57f9e31e6de4861e21680496a90ce2fa0d3436cd0434
        B/clauses/window-08/raw.json: 2ac2995d043df97a37bf109b6f209ca8b320cb61067ec42c3b96dcfdad4879b9
        B/clauses/window-08/prompt.txt: 67debde6234dd867d80dcd646430579bff1e775524c41a8889d112ec36724c83
        B/clauses/window-08/meta.json: c31c206d4b6be555ea0f30288f8ced191fa231bf3d5362d3ba71e9166750cac8
        B/tables/TABLE-1-page-3-1/raw.json: ebb8f23c54faa6f37cc16259601e8fed64edcab15069d42ece0f835ec71f17b7
        B/tables/TABLE-1-page-3-1/prompt.txt: 948ce244dccd60748334ee5275cc4ac35972300a3c985124845fe3e9ef9dc327
        B/tables/TABLE-1-page-3-1/meta.json: d77719578c384aa51218d44718c4311f3191a03a9b25012a1b9fd9df9b76132a
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
      pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
      source_review: _compare/relationships-2026-11-16/review-current/Kummerer2013
      source_status_sha256: bef49501278e756f44f0532f28cdee34f0a60e2c9753c35fb2dea52abb849e62
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: brain lesions
    outcome:
      text: repetition impairments
    analysis_label: voxelwise lesion-behaviour mapping (Brunner–Munzel test)
    relation: association
    evidence_ids:
    - P1-S2-C3
    - P5-S2-C12
    - P5-S3-C2
    - P5-S3-C3
    qualifier_ids:
    - P5-S3-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
      source_review: _compare/relationships-2026-11-16/review-current/Kummerer2013
      source_status_sha256: bef49501278e756f44f0532f28cdee34f0a60e2c9753c35fb2dea52abb849e62
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C6
      - Result passage disposed without unit P2-S3-C7
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P4-S2-C9
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C10
      - Accounting without a linked unit P5-S2-C12
      - Accounting without a linked unit P5-S2-C7
      - Accounting without a linked unit P5-S2-C8
      - Result passage disposed without unit P5-S3-C1
      - Accounting without a linked unit P5-S3-C2
      - Accounting without a linked unit P5-S3-C3
      - Unaccounted source passage P5-S2-C12
      - Unaccounted source passage P5-S2-C7
      - Unaccounted source passage P5-S2-C8
      - Unaccounted source passage P5-S2-C10
      - Unaccounted source passage P5-S3-C2
      - Unaccounted source passage P5-S3-C3
      - Accounting without a linked unit P5-S3-C10
      - Accounting without a linked unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C7
      - Result passage disposed without unit P5-S3-C8
      - Unaccounted source passage P5-S3-C10
      - Unaccounted source passage P5-S3-C5
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S3-C4
      - Result passage disposed without unit P8-S3-C5
      - Accounting without a linked unit P8-S4-C2
      - Accounting without a linked unit P8-S4-C3
      - Result passage disposed without unit P9-S1-C6
      - Unaccounted source passage P8-S4-C2
      - Unaccounted source passage P8-S4-C3
      - Result passage disposed without unit P9-S1-C13
      - Result passage disposed without unit P9-S3-C8
      - Accounting without a linked unit P9-S3-C9
      - Unaccounted source passage P9-S3-C9
      unattached_null_or_qualifier_ids:
      - P5-S3-C9
      - P8-S3-C5
      - P9-S1-C6
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 160
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S2-C3
      - P2-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P2-S2-C5
        - P2-S2-C6
        - P2-S2-C9
        - P4-S1-C2
        - P4-S2-C6
        - P4-S2-C7
        - P5-S1-C11
        - P5-S2-C5
        - P5-S2-C9
        - P7-S1-C6
        - P9-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S3-C14
      table_review_required:
      - TABLE-1-page-3-1
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S2
        - P5-S3
        - P6-S1
        - P7-S1
        - P8-S2
        - P8-S3
        - P8-S4
        - P9-S1
        - P9-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
      source_review: _compare/relationships-2026-11-16/review-current/Kummerer2013
      source_status_sha256: bef49501278e756f44f0532f28cdee34f0a60e2c9753c35fb2dea52abb849e62
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between repetition impairments and posterior
        temporoparietal lesions.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes association between comprehension deficits and ventral-anterior
        temporoprefrontal lesions.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Establishes negative correlations between tract overlap and performance
        for both streams.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ultrasound results of carotid artery stenosis.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes infarct patterns as embolic.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes intracranial collateralization.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Defines the principal components as repetition and comprehension.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes manual inspection of lesion maps.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Justifies use of non-parametric testing.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that lesion maps were generated.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of subtests.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of severity, fluency, and aphasia type.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variance of subtests.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA results.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports Bartlett's test of sphericity.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports PCA variance explained.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Reports correlation between lesion volume and language scores.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes maximum lesion overlap location.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Describes spatial dissociation of lesions for repetition and comprehension.
    - source_id: P5-S3-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Repeats spatial dissociation findings.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Lists specific brain regions associated with repetition impairments.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies statistically most significant voxels for repetition.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Lists specific brain regions associated with comprehension deficits.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies statistically most significant voxels for comprehension.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces logistic regression results.
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Notes lack of correlation between factor loadings.
    - source_id: P5-S3-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Notes lesion maxima were identical to Brunner-Munzel tests.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains rationale for logistic regression.
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null finding when using lesion volume as covariate.
    - source_id: P5-S3-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Confirms robustness of spatial dissociation via logistic regression.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports grey/white matter overlap percentages for repetition.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports grey/white matter overlap percentages for comprehension.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Notes subcortical location of lesion maxima.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports overlap of repetition map with dorsal/ventral tracts.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports overlap of comprehension map with dorsal/ventral tracts.
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: States dissociation was present in logistic regression.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Reports overlap of repetition map (logistic) with tracts.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Reports overlap of comprehension map (logistic) with tracts.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports significant negative relationships between tract damage and
        performance.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restates spatial dissociation in discussion.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Restates correlation of deficits with specific pathways.
    - source_id: P8-S2-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates involvement of ventrolateral prefrontal cortex and temporal
        lobe.
    - source_id: P8-S2-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Links statistical peak to extreme capsule.
    - source_id: P8-S3-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restates repetition map findings.
    - source_id: P8-S3-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restates location of statistical maximum for repetition.
    - source_id: P8-S4-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restates anterior-posterior insular dissociation.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Confirms spatial dissociation preserved in logistic regression.
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 7
      reason: Restates overlap of logistic maps with tracts.
    - source_id: P9-S1-C8
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Restates regression analysis of individual overlap.
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses disconnection as a pathophysiological mechanism.
    - source_id: P9-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Notes number of patients with global aphasia.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses contribution of white matter damage.
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses statistical power in subcortical regions.
    - source_id: P9-S3-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Summary of brain regions involved in impairments.
    - source_id: P9-S3-C9
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Summary of importance of specific fibre tracts.
    - source_id: P9-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Ueno et al. model.
    - source_id: P9-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes transcortical sensory aphasia.
    - source_id: P9-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses disconnection in clinical syndromes.
    unresolved_coverage:
    - source_id: P5-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S3-C6
    - P2-S3-C7
    - P2-S3-C8
    - P4-S1-C2
    - P4-S2-C3
    - P4-S2-C5
    - P4-S2-C9
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C10
    - P5-S3-C1
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C8
    - P5-S3-C9
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C4
    - P7-S1-C3
    - P8-S1-C1
    - P8-S1-C2
    - P8-S2-C2
    - P8-S2-C4
    - P8-S3-C4
    - P8-S3-C5
    - P8-S4-C2
    - P8-S4-C3
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C10
    - P9-S1-C13
    - P9-S2-C3
    - P9-S3-C8
    - P9-S3-C9
    - P9-S4-C4
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
      - P2-S2-C3
      - P2-S3-C4
      recruited_sample:
      - P2-S2-C11
      - P2-S3-C4
      eligibility:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      imaging_provenance:
      - P2-S2-C7
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C5
      - P5-S1-C12
      imaging_timing:
      - P2-S3-C4
      outcome_timing:
      - P2-S3-C4
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S2-C12
      dependent_variable_statement:
      - P2-S2-C5
      - P2-S2-C6
      - P4-S2-C6
      - P4-S2-C7
      limitations:
      - P4-S3-C5
      - P4-S3-C6
      - P4-S3-C7
      - P5-S3-C10
      - P5-S3-C11
      - P9-S2-C9
      - P9-S2-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C11
      - P4-S2-C12
      - P5-S3-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C4
      - P3-S2-C2
      - P4-S1-C4
      - P4-S3-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P2-S2-C5
      - P2-S2-C6
      - P2-S2-C9
      - P4-S1-C2
      - P4-S2-C6
      - P4-S2-C7
      - P5-S1-C11
      - P5-S2-C5
      - P5-S2-C9
      - P7-S1-C6
      - P9-S1-C8
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
      pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
      review_sha256: a5cfafc45c00763efb5f32245f05823e544ce6ac131697c94d08dbbb3a57eda4
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
      - P1-S2-C3
      - P5-S2-C12
      - P5-S3-C2
      - P5-S3-C3
      source_result: Voxelwise lesion-behaviour mapping (Brunner-Munzel test) in 100
        acute stroke patients revealed a statistically significant association between
        repetition impairments and lesions in the posterior temporoparietal region,
        with maxima in the periventricular white matter in projection of the dorsal
        superior longitudinal and arcuate fasciculus.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the primary voxelwise lesion-behaviour
            mapping (VLBM) using the Brunner-Munzel test, correlating repetition impairment
            scores with lesion maps. This matches the source description in P1-S2-C3,
            P4-S2-C6, and P5-S3-C2/C3.
          source_ids:
          - P1-S2-C3
          - P4-S2-C6
          - P5-S3-C2
          - P5-S3-C3
        direction:
          answer: fits
          reason: The source explicitly states that repetition impairments were 'associated
            with' lesions in the specified region (P1-S2-C3, P5-S2-C12). The proposed
            draft correctly identifies this as an association. The direction of the
            relationship (impairment linked to lesion presence) is preserved.
          source_ids:
          - P1-S2-C3
          - P5-S2-C12
        construct:
          answer: fits
          reason: The exposure is 'brain lesions' (specifically overlap with template
            tracts/voxels) and the outcome is 'repetition impairments' (measured via
            principal components of Aachen tests). The method is correctly identified
            as VLBM. The patient measurement is template_lesion_overlap, as the analysis
            overlays patient lesions on reference tract maps derived from healthy
            subjects (P5-S1-C12), not patient diffusion data.
          source_ids:
          - P1-S2-C3
          - P4-S2-C6
          - P5-S1-C12
          - P5-S3-C3
        qualifications:
          answer: fits
          reason: 'The draft includes key qualifications: the use of the Brunner-Munzel
            test, the restriction to voxels affected in at least 10 patients (P4-S2-C8),
            and the nature of the repetition measure (principal component). It correctly
            notes the acute timing and population. The ''likely'' direction in the
            draft is a reasonable qualitative summary of a significant association,
            though ''associated'' is the precise source term.'
          source_ids:
          - P4-S2-C8
          - P5-S2-C5
          - P2-S3-C4
        missing_material_caveat:
          answer: fits
          reason: The draft includes the caveat regarding haemodynamic infarcts not
            being excluded (P2-S3-C5) and the limitation regarding white matter labels
            being projections. It does not omit material caveats that would change
            the interpretation of the primary association. The fact that the association
            is robust to covariates (lesion size, opposite deficit) is a qualification
            of the result's robustness, not a contradiction of the primary finding.
          source_ids:
          - P2-S3-C5
          - P5-S3-C10
          - P5-S3-C12
      optional_pending:
      - 'sample.time_post_onset: Source P2-S3-C4 indicates ''3 ± 2.6 days'' but has
        an OCR warning; exact value to be confirmed in PDF review.'
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
    - 'sample.time_post_onset: Source P2-S3-C4 indicates ''3 ± 2.6 days'' but has
      an OCR warning; exact value to be confirmed in PDF review.'
    normalizations:
    - field: sample.time_post_onset
      original: examined on average 3 +/- 2.6 days after onset
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 2.6, 3'
    analysis_identity:
      id: R001
      exposure:
        text: brain lesions
      outcome:
        text: repetition impairments
      analysis_label: voxelwise lesion-behaviour mapping (Brunner–Munzel test)
      relation: association
      evidence_ids:
      - P1-S2-C3
      - P5-S2-C12
      - P5-S3-C2
      - P5-S3-C3
      qualifier_ids:
      - P5-S3-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
        source_review: _compare/relationships-2026-11-16/review-current/Kummerer2013
        source_status_sha256: bef49501278e756f44f0532f28cdee34f0a60e2c9753c35fb2dea52abb849e62
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 043d57084d27dfcb3cd1431110b9692fda2e0558a98d9e56bbf2e9dc56ab26af
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C3
          page: 2
          text_layer_sha256: 043d57084d27dfcb3cd1431110b9692fda2e0558a98d9e56bbf2e9dc56ab26af
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'To

          test

          this

          hypothesis,

          we

          conducted

          a

          voxelwise

          lesion-behaviour mapping (VLBM; Rorden et al., 2007) study in

          a large cohort of 100 acute stroke patients.'
        anchor_text: 'To

          test

          this

          hypothesis,

          we

          conducted

          a

          voxelwise

          lesion-behaviour mapping (VLBM; Rorden et al., 2007) study in

          a large cohort of 100 acute stroke patients.'
        excluded_fragments: []
        image_sha256: cec89e1afce8a705f44c32767a1fa35c4bd27e3cf86f1923bb38983a4fb9e2ac
        transcription: To test this hypothesis, we conducted a voxelwise lesion-behaviour
          mapping (VLBM; Rorden et al., 2007) study in a large cohort of 100 acute
          stroke patients
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ac845968c859874fd29c7837608de9ac7a2689cee3c3f4e1c6ab27c0224ece28
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: ac845968c859874fd29c7837608de9ac7a2689cee3c3f4e1c6ab27c0224ece28
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Finally, we included 100 native German-speaking patients\n\
          (mean age 62 years, 67 male, 6 left-handed) with acute aphasia\ncaused by\
          \ ischaemic stroke (Table 1), who were examined on average\n3 \x02 2.6 (\x02\
          \ SD) days after onset."
        anchor_text: "Finally, we included 100 native German-speaking patients\n(mean\
          \ age 62 years, 67 male, 6 left-handed) with acute aphasia\ncaused by ischaemic\
          \ stroke (Table 1), who were examined on average\n3 \x02 2.6 (\x02 SD) days\
          \ after onset."
        excluded_fragments: []
      P5-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c303abdc6d8fdb367028de07affca19dd04c615c9d17b53292ff2f1dd2ba253a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 479798dc49a8a7a9dd9c047da2cf479006386faf4aeeb7bd06ec57ac7d2cae3d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S3-C3
          page: 5
          text_layer_sha256: 479798dc49a8a7a9dd9c047da2cf479006386faf4aeeb7bd06ec57ac7d2cae3d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The statistically most\nsigniﬁcant voxels were found in the\
          \ deep white matter of the\nfrontal semioval centre (\x0636, \x0620, 28;\
          \ z = 9.5) and the posterior\ntemporal cortex (\x0630, \x0624, 8; z = 8.7)\
          \ in projection of the arcu-\nate and superior longitudinal fascicle ﬁbres,\
          \ respectively, and in the\nposterior most part of the insular cortex (\x06\
          38, \x0612, \x061; z = 7.1)."
        anchor_text: "The statistically most\nsigniﬁcant voxels were found in the\
          \ deep white matter of the\nfrontal semioval centre (\x0636, \x0620, 28;\
          \ z = 9.5) and the posterior\ntemporal cortex (\x0630, \x0624, 8; z = 8.7)\
          \ in projection of the arcu-\nate and superior longitudinal fascicle ﬁbres,\
          \ respectively, and in the\nposterior most part of the insular cortex (\x06\
          38, \x0612, \x061; z = 7.1)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'We found that

    repetition impairments were mainly associated with lesions located in the posterior
    temporoparietal region with a statistical lesion

    maximum in the periventricular white matter in projection of the dorsal superior
    longitudinal and arcuate fasciculus.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
