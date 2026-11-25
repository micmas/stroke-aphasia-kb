---
id: rsfc_change_naming_improvement
name: rsFC change and naming improvement correlation
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
  claim: No significant correlation was found between the therapy-induced rsFC changes
    and the improvements in naming accuracy for both trained and untrained items.
  direction: no_effect
  relationship: correlational
  method: rs_fMRI
  sample:
    n: 10
    population: Francophones with chronic aphasia following a single left hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: Post-therapy assessment performed within one week of the end
      of therapy
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Absence of a control group
  - Liberal outlier detection settings may have impacted results
  - Lesions were regressed out as CSF, which may not fully remove all lesion-related
    artifacts
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Changes in resting-state functional connectivity (rsFC)
    measured via ROI-to-ROI bivariate correlation between pre-therapy (T0) and post-therapy
    (T1) fMRI sessions. Analysis was performed using Spearman''s correlation between
    individual beta values of significant rsFC changes and behavioral improvements.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P3-S1-C10, two-model agreement, human verification
    pending): Participants

    Ten participants with chronic aphasia (3 women, mean age = 68.9 ± 10.2) following
    a single left hemisphere ischemic stroke recruited through local patient association
    by referral following discharge from rehabilitation centers in the area and following
    self-referral are included in this study Original text-layer quotation is preserved
    below. PDF image reading (P3-S2-C7, two-model agreement, human verification pending):
    . A second lan-

    guage evaluation and fMRI session (T1) were performed within a week of the end
    of therapy Original text-layer quotation is preserved below.'
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
    - proposed_concept:naming_improvement
  therapy:
    id: fr_pca
    name: French Phonological Components Approach (Fr-PCA)
  citation: '@MassonTrottier2021'
  source_passages:
  - section: Original source P7-S1-C16
    page: 7
    quote: 'Within the group of 10 participants with aphasia, no signiﬁcant correlation
      was found

      between the rsFC changes and the main language outcome measures.


      '
    supports: claim
  - section: Original source P6-S2-C3
    page: 6
    quote: 'Furthermore, to investigate the link between rsFC changes and naming improvements

      after therapy, we applied Spearman’s correlation analyses between ROI-to-ROI
      (R2R) rsFC

      changes (found signiﬁcant in the main analyses), and the improvements on trained
      and

      untrained items.

      3.'
    supports: method
  - section: Original source P3-S1-C10
    page: 3
    quote: 'Participants

      Ten participants with chronic aphasia (3 women, mean age = 68.9 ± 10.2) following
      a

      single left hemisphere ischemic stroke recruited through local patient association
      by referral

      following discharge from rehabilitation centers in the area and following self-referral
      are

      included in this study.'
    supports: sample
  - section: Original source P3-S2-C7
    page: 3
    quote: 'A second lan-

      guage evaluation and fMRI session (T1) were performed within a week of the end
      of therapy.'
    supports: method
  - section: Original source P10-S1-C9
    page: 10
    quote: 'Moreover, the absence

      of a control group is acknowledged by the authors.'
    supports: limitation
  - section: Original source P10-S2-C7
    page: 10
    quote: 'First, regarding the outlier detection, although the parameters

      used are commonly applied in the clinical studies [34,58–60], using liberal
      settings leads to

      higher frame-wise displacement values, which can have an impact on the results.'
    supports: limitation
  - section: Original source P10-S2-C8
    page: 10
    quote: 'Second,

      the lesion was segmented and regressed out as CSF.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Changes in resting-state functional connectivity (rsFC) measured
  via ROI-to-ROI bivariate correlation between pre-therapy (T0) and post-therapy (T1)
  fMRI sessions.
assessment:
- Test de dénomination de Québec-60 (TDQ60)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: MassonTrottier2021
  proposal_id: R004
  review_status_sha256: ac1d4b97a3f6664ee7d78c8bd5076a3a8d3c560a90933e957cbd7148b64f91ce
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
        A/passages.json: ef56aa8b5abc173635d046f791d540d2ba52bf481ae906e75636a2001f840c2a
        A/raw.json: 6590e2c6b6f9a49f15024e1cd4f7e6304f735fab9d449c24e8766092fc1cf891
        A/source-units.json: e223a58c0d1399323f63de295a0e2506fbc384483af506ff59bf2c27e4c56805
        A/full-source-units.json: 5c0108c29d5f85434aa872247b4e2ddcb490e0b9bd5d1037f726c577a2985cd8
        A/meta.json: b12fdbec0995488975e7801a3864bbfac2a96aa7f0335535263363b3b32a9ce1
        A/table-images/TABLE-1-page-3-1.png: 971d5a2f0d738d396ad6d605ecae3af37d9af78766cde22df9d56800f26e9993
        A/table-images/page-12.png: be6eb980a92e131653e5a3781156474047511bd7a97efee8554750c94d32b596
        A/table-images/page-3.png: 748cf103331a626e5364b3b087b62b1936f9ebc33bf950ce2f6d494b2834351f
        A/table-images/page-7.png: 876450739fc9f7ba52dd78685c93e035a355938ee622814e4d770ec88578aa62
        A/table-images/manifest.json: b3c2e4dd05bacf4b13ae3681fb715bfab5b0d62548dbf892965fbf7a5426f35e
        A/table-images/TABLE-3-page-7-2.png: 4fedf46bf2fce2bae2aaea856a7e5c2aff806f19fe83fa35c80c02a675acacbe
        A/table-images/TABLE-A1-page-12-1.png: fe07549a366f0f1fa985401029929af308687c22000cc7a5ec2654e900250eb2
        A/table-images/TABLE-2-page-7-1.png: a9f5d9e1c2e531ea86825eac6980255d56422aae6cb42123dc7f342684014f1b
        A/clauses/window-03/raw.json: 8dcc9af0ba2ca4969730262a8e9ca843eb4317d2b73d248537aa8203e85c9f50
        A/clauses/window-03/prompt.txt: 150eeeb7aac216b1f7f9b6c1c8a8d0592996c425393d41936cf9c7b03bbba51a
        A/clauses/window-03/meta.json: 1a72f64b4e069390403a9ce9436d2d97b044ab85410d7ac7adcd8b7a3c739b89
        A/clauses/window-04/raw.json: fc839eea114090e2db4c1bc5e80e87faf8832d603f27ca243662aef7247dd1cb
        A/clauses/window-04/prompt.txt: be9cce9e84c631e3cd236479eb1fcabe4a24ae3feeff997793e1f94975d05e6e
        A/clauses/window-04/meta.json: 89bf78868b1b9255165c568d3062653166be488356b7d0d6948b82ee05ce129f
        A/clauses/window-05/raw.json: 0575dd26becd0b0213a1850efa843579ab28bb7a4486c7414f52a1dcf891c8f6
        A/clauses/window-05/prompt.txt: 78fdb5097dc255de9b14118b047695febda6aeb8c2bfc8424a5dc856bf78effa
        A/clauses/window-05/meta.json: 4812a453b63bf8eb94513152b034e59aa10185844f003479b203e194d4312cdd
        A/clauses/window-02/raw.json: b79a456c392dd829fe3440bfbc7741ece3e1b23ad8bc63b3a85cef7d23c85f34
        A/clauses/window-02/prompt.txt: d28f053b331acbda28ea31e1dc5451d6a3b1977fcdcc04265d4126fe88384a5f
        A/clauses/window-02/meta.json: e58dbb3a09d963d47bf36f66a7fc6684497f062cbd606e24f4994eba0647f129
        A/clauses/window-07/raw.json: 828fe7448bc427e992378e47f414f4ce4e1d7cecae2b55521fb05c0eb77128d5
        A/clauses/window-07/prompt.txt: a2f59a6ab2431e9386807520d066a9d711fc4837f887fa752e5f3f46e258fcf6
        A/clauses/window-07/meta.json: 4ba32bd98e2aef1d6b972e8bd465978cfc411cf144e11090572a7254088aa445
        A/clauses/window-01/raw.json: afecbc9c5cdef9d9f00f013abf15e74c6f117498a59110f1db7f8d7a2eda0420
        A/clauses/window-01/prompt.txt: 28885abf1c89c5a5cfd5bafe176959c426da278a298f0d4b6268109217a61956
        A/clauses/window-01/meta.json: a5d5e3653863feddadace968d89e55ace5ccf0bfcd25bac290293d9375ce8b45
        A/clauses/window-06/raw.json: d42416d02e4825a92ed4020eb92a4a195c36093b9f4127d983d04d05aebad774
        A/clauses/window-06/prompt.txt: 8e07c1fa4064d4c0e5b418180ba130025bb72672370f0ed1e5c8ad726613eadd
        A/clauses/window-06/meta.json: d66b24aca9dbc2f184afc807fba4a1fdf8ab6bbaf6f42eed2cc11f353a3b7b5c
        A/clauses/window-08/raw.json: 96e3f083422b2a110ef799481bbd0a24da2c90bba94526445fefca294241314b
        A/clauses/window-08/prompt.txt: 418b0bfcee60e8d345222d0b6b2a4840028017264a01e9f5be1c0e71d56a2fc8
        A/clauses/window-08/meta.json: c2b067cb0d8c3651eaf0af49765554a51a922f05378d651bdfd4164cc13f934f
        A/tables/TABLE-A1-page-12-4/raw.json: 271031f13ad1b9fb9c2899a5987816341dcf548cb63446a8da38369b6928bd9c
        A/tables/TABLE-A1-page-12-4/prompt.txt: 7a3965d890f0b38cbaea591a0713d4260d8cfc4d6d803aa17dc894722c1c9ef7
        A/tables/TABLE-A1-page-12-4/meta.json: 360dd3fee82143c017982166a2ae99588fa3794a0deef96278545c8f2244caaf
        A/tables/TABLE-1-page-3-1/raw.json: 4e90f4ad9640ce262b9701747d565f365017306ad7f3cbde88360fc17e0e2903
        A/tables/TABLE-1-page-3-1/prompt.txt: df4e6f2022d9725f85ea940abbec95413b48fdfc4a372e193557efc43b2c4c9c
        A/tables/TABLE-1-page-3-1/meta.json: be44c7a8549d3ba6d6d72f3dcea1e82238b5977140e0e5545087ec6ebfb29d7c
        A/tables/TABLE-3-page-7-3/raw.json: de7a62d33787cec6e1029a4a669c296a7de2d3bc4d5721075c157526296b28b8
        A/tables/TABLE-3-page-7-3/prompt.txt: cefd9d44aaa820662050b3043462024cf67747a753b89004761f66f990a2f753
        A/tables/TABLE-3-page-7-3/meta.json: 6bea7d258e91a8ab7e1ec402992ae8ab587065532aadff219a25ec60a9d07263
        A/tables/TABLE-2-page-7-2/raw.json: 110a81428e7fbe250befc257a1bdbc9c668bcd0dc7549bbc0c96e4b5a1ba84c2
        A/tables/TABLE-2-page-7-2/prompt.txt: 56231218ea88b95b9fc4be4b1eb9499d06f4fdef0774128c743d9a033d917282
        A/tables/TABLE-2-page-7-2/meta.json: d282f6f0ce2cf65c9123e1f60dbbf2098546fcf2bddfd69cc25e88a3564d9246
        B/passages.json: ef56aa8b5abc173635d046f791d540d2ba52bf481ae906e75636a2001f840c2a
        B/raw.json: e1f35ea3d4b58dac07d898729f48a9a1ddfff946f38d9922e8ac6cc3f4c13258
        B/source-units.json: e223a58c0d1399323f63de295a0e2506fbc384483af506ff59bf2c27e4c56805
        B/full-source-units.json: 5c0108c29d5f85434aa872247b4e2ddcb490e0b9bd5d1037f726c577a2985cd8
        B/meta.json: cbc1ab0304191a8aee145dc9c37f15f79270dd1fce0223b4ee7c386fa2a7c378
        B/table-images/TABLE-1-page-3-1.png: 971d5a2f0d738d396ad6d605ecae3af37d9af78766cde22df9d56800f26e9993
        B/table-images/page-12.png: be6eb980a92e131653e5a3781156474047511bd7a97efee8554750c94d32b596
        B/table-images/page-3.png: 748cf103331a626e5364b3b087b62b1936f9ebc33bf950ce2f6d494b2834351f
        B/table-images/page-7.png: 876450739fc9f7ba52dd78685c93e035a355938ee622814e4d770ec88578aa62
        B/table-images/manifest.json: 0e44c564ffb48acc367da6ba9435c04e4943272a71bcae1283e3d02c9441920e
        B/table-images/TABLE-3-page-7-2.png: 4fedf46bf2fce2bae2aaea856a7e5c2aff806f19fe83fa35c80c02a675acacbe
        B/table-images/TABLE-A1-page-12-1.png: fe07549a366f0f1fa985401029929af308687c22000cc7a5ec2654e900250eb2
        B/table-images/TABLE-2-page-7-1.png: a9f5d9e1c2e531ea86825eac6980255d56422aae6cb42123dc7f342684014f1b
        B/clauses/window-03/raw.json: 8059f04d6c96709dcec32a516fe4dfb4ef842a60b44661c1e0939c6e1c0c4f17
        B/clauses/window-03/prompt.txt: 150eeeb7aac216b1f7f9b6c1c8a8d0592996c425393d41936cf9c7b03bbba51a
        B/clauses/window-03/meta.json: 1a2148dff76ae5cf54f26938110f9544a9d049050e0de619879c44a3b16038ee
        B/clauses/window-04/raw.json: 40a55236b69a1949a31b233f7956556f7b883fab35cbbf66d647020a07cfa539
        B/clauses/window-04/prompt.txt: be9cce9e84c631e3cd236479eb1fcabe4a24ae3feeff997793e1f94975d05e6e
        B/clauses/window-04/meta.json: 1a668e92ab54574b910de7c8bd146d0d889f2cc3054a9d03394ecda88dc379f0
        B/clauses/window-05/raw.json: da433d838dda4f0311c0868d29a8106c58a1a18c19d91ea675bb19ba9dff53bc
        B/clauses/window-05/prompt.txt: 78fdb5097dc255de9b14118b047695febda6aeb8c2bfc8424a5dc856bf78effa
        B/clauses/window-05/meta.json: 752bebd06efa5061b16a4c6f94f20097fc39b0ac0e89b86ff68a488a5e0c772c
        B/clauses/window-02/raw.json: 0743082c987e80777454103d022b2297950ce80e90e4abfb8f23c601f2e6b137
        B/clauses/window-02/prompt.txt: d28f053b331acbda28ea31e1dc5451d6a3b1977fcdcc04265d4126fe88384a5f
        B/clauses/window-02/meta.json: bab3e2582bf4f4b9f9943e2911c827c72499b50eda73cf2c99a3e782ec84bb09
        B/clauses/window-07/raw.json: 0fce1ae334d6683ee04d13f85eda1910d1f89201df4530efb5f9531f1cd2455e
        B/clauses/window-07/prompt.txt: a2f59a6ab2431e9386807520d066a9d711fc4837f887fa752e5f3f46e258fcf6
        B/clauses/window-07/meta.json: 16fa9ef328592c172de8395aaadd98b9489085cca9d7d710dab67c05a3ad6a94
        B/clauses/window-01/raw.json: 092735d5bb7c0ef6c6724099f102e076498283d3a0c3c7aa0150d0d1256e5d32
        B/clauses/window-01/prompt.txt: 28885abf1c89c5a5cfd5bafe176959c426da278a298f0d4b6268109217a61956
        B/clauses/window-01/meta.json: c762af893bd924dc917ed9642ecb164caba4319c89b5015b1aded161276a5601
        B/clauses/window-06/raw.json: 2abca047e4ff9f07508826ef10debe07e7f355754a83b68f124e90730da3fb12
        B/clauses/window-06/prompt.txt: 8e07c1fa4064d4c0e5b418180ba130025bb72672370f0ed1e5c8ad726613eadd
        B/clauses/window-06/meta.json: 32f78c9710f95ab1c74f6eabba9ac210d3eaee4fbfd808fd9775abe856505cab
        B/clauses/window-08/raw.json: b9bf3d0718cd4858a3966f53374a86d71933cf7ddf8d8fbb828dd018e95516a1
        B/clauses/window-08/prompt.txt: 418b0bfcee60e8d345222d0b6b2a4840028017264a01e9f5be1c0e71d56a2fc8
        B/clauses/window-08/meta.json: b8130ee55e148e8cf0146ab15d21469f49fd87a49f1c3704bdcbfe9cff8f559a
        B/tables/TABLE-A1-page-12-4/raw.json: 5b0c725713b2ae3047fb4699580c3b21de8e55f7e35261c274aa4f555678e0dd
        B/tables/TABLE-A1-page-12-4/prompt.txt: 7a3965d890f0b38cbaea591a0713d4260d8cfc4d6d803aa17dc894722c1c9ef7
        B/tables/TABLE-A1-page-12-4/meta.json: f77f4eb56e3574a633f4953e4f8637cd8b6647b1866d9ba23885b5a3f31efa87
        B/tables/TABLE-1-page-3-1/raw.json: 1e6bbb650391d40cd44d7610edc766645e07fb9f6ba048c49108f3df03ee8391
        B/tables/TABLE-1-page-3-1/prompt.txt: df4e6f2022d9725f85ea940abbec95413b48fdfc4a372e193557efc43b2c4c9c
        B/tables/TABLE-1-page-3-1/meta.json: 7499505d73c00e6899f71d1222c9418e74afda9a573eb6d594507196f08a056f
        B/tables/TABLE-3-page-7-3/raw.json: d11f723861c08e75d4ba4e6476e861567b126c137902589c1d334dbb2b18a7b8
        B/tables/TABLE-3-page-7-3/prompt.txt: cefd9d44aaa820662050b3043462024cf67747a753b89004761f66f990a2f753
        B/tables/TABLE-3-page-7-3/meta.json: 0e9ec3baec1da757fba92f6ab72c93194e0ea4b71abc9a5ebb55dd58e8963388
        B/tables/TABLE-2-page-7-2/raw.json: b58e4823a03b183cce7a873570551034b345c7cef19bec982d14811e2973e694
        B/tables/TABLE-2-page-7-2/prompt.txt: 56231218ea88b95b9fc4be4b1eb9499d06f4fdef0774128c743d9a033d917282
        B/tables/TABLE-2-page-7-2/meta.json: 922c4091061eee24742cf9b702e31bd72598acec70a8922c0609cdabb7e3d378
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
      pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
      source_review: _compare/relationships-2026-11-16/review-current/MassonTrottier2021
      source_status_sha256: c4950ee8fcc5f471bc2437bb23b0cef3fb3a7b7916218de9d12a524aa1434089
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: rsFC changes
    outcome:
      text: naming improvements (trained and untrained items)
    analysis_label: Correlation between rsFC Changes and Naming Improvements
    relation: association
    evidence_ids:
    - P7-S1-C16
    qualifier_ids:
    - P6-S2-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
      source_review: _compare/relationships-2026-11-16/review-current/MassonTrottier2021
      source_status_sha256: c4950ee8fcc5f471bc2437bb23b0cef3fb3a7b7916218de9d12a524aa1434089
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C9'
      - Result passage disposed without unit P6-S2-C8
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P8-S1-C12
      - Result passage disposed without unit P8-S3-C3
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S2-C7
      - Result passage disposed without unit P9-S3-C1
      - Result passage disposed without unit P10-S2-C13
      - Result passage disposed without unit P10-S2-C15
      - Result passage disposed without unit P10-S3-C3
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 20
      default_disposition_count_requires_completeness_check: 180
      unselected_timing_passages:
      - P3-S1-C10
      - P8-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P10-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P6-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      - TABLE-A1-page-12-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-7-2
      - TABLE-3-page-7-3
      - TABLE-A1-page-12-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P4-S1
        - P6-S2
        - P7-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
      source_review: _compare/relationships-2026-11-16/review-current/MassonTrottier2021
      source_status_sha256: c4950ee8fcc5f471bc2437bb23b0cef3fb3a7b7916218de9d12a524aa1434089
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of behavioral results.
    - source_id: P1-S2-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Abstract restatement of rsFC changes.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant improvement on trained and untrained items.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Provides mean improvement percentages for trained and untrained items.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table A1 for individual performance.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Introduces the observation of significant rsFC changes.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Reports increased connectivity between left temporal fusiform cortex
        and supracalcarine cortex.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports increased connectivity between left SCC cortex and left inferior
        temporal gyrus.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports decreased connectivity between lingual gyrus and RH superior
        frontal gyrus.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports effect of severity on connectivity between left temporal fusiform
        cortex, right STG, and right insular cortex.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports effect of severity on connectivity between right frontal operculum
        and right pallidum.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 3.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table header for severity regressor analysis.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifies the analysis as using initial aphasia severity as a regressor.
    - source_id: P7-S1-C16
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no significant correlation between rsFC changes and language
        outcomes.
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of behavioral improvements.
    - source_id: P8-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of neurofunctional changes.
    - source_id: P8-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of null correlation.
    - source_id: P8-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with prior studies (Marcotte et al., Rochon et al.).
    - source_id: P8-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with prior study (van Hees et al.).
    - source_id: P9-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of rsFC changes.
    - source_id: P9-S1-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of specific connectivity increase.
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of specific connectivity increase.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: 'Reports null finding: no changes in connectivity between ROIs in the
        dorsal stream.'
    - source_id: P9-S2-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of decreased RH connectivity.
    - source_id: P9-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of severity effect on rsFC.
    - source_id: P9-S3-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of connectivity increase between right frontal
        operculum and right pallidum.
    - source_id: P10-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of null correlation.
    - source_id: P10-S2-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of naming improvements.
    - source_id: P10-S3-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Conclusion restatement of rsFC changes.
    unresolved_coverage:
    - source_id: P7-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C6
    - P1-S2-C7
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C8
    - P7-S1-C9
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C8
    - P8-S1-C10
    - P8-S1-C12
    - P8-S2-C2
    - P8-S2-C9
    - P8-S2-C11
    - P8-S3-C3
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C8
    - P9-S1-C13
    - P9-S2-C1
    - P9-S2-C4
    - P9-S2-C7
    - P9-S3-C1
    - P10-S1-C3
    - P10-S2-C13
    - P10-S2-C14
    - P10-S2-C15
    - P10-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-7-2
    - TABLE-3-page-7-3
    - TABLE-A1-page-12-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C10
      recruited_sample:
      - P3-S1-C10
      eligibility:
      - P3-S1-C12
      - P3-S1-C13
      imaging_provenance:
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      imaging_timing:
      - P3-S2-C5
      - P3-S2-C7
      outcome_timing:
      - P3-S2-C5
      - P3-S2-C7
      outcome_definition:
      - P5-S1-C2
      - P5-S1-C5
      validation: []
      analysis_restrictions:
      - P6-S1-C13
      dependent_variable_statement:
      - P6-S1-C4
      - P6-S1-C8
      - P6-S2-C2
      - P6-S2-C3
      limitations:
      - P10-S1-C9
      - P10-S2-C6
      - P10-S2-C7
      - P10-S2-C8
      - P10-S2-C9
      personal_factors: []
      tested_personal_effects:
      - P7-S1-C7
      adjustment_roles:
      - P5-S2-C8
      - P5-S2-C9
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C10
      - P3-S2-C10
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P10-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P6-S2-C2
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
      pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
      review_sha256: ac1d4b97a3f6664ee7d78c8bd5076a3a8d3c560a90933e957cbd7148b64f91ce
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
      - P7-S1-C16
      source_result: Within the group of 10 participants with aphasia, no significant
        correlation was found between the rsFC changes and the main language outcome
        measures (improvements on trained and untrained items).
      result_status: not_detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the correlation between therapy-induced
            rsFC changes and naming improvements. The source (P7-S1-C16, P6-S2-C3)
            confirms this specific analysis was performed using Spearman's correlation
            on individual beta values of significant rsFC changes and behavioral improvements.
          source_ids:
          - P7-S1-C16
          - P6-S2-C3
        direction:
          answer: fits
          reason: The source explicitly states 'no significant correlation was found'
            (P7-S1-C16). The draft's 'no_effect' direction correctly represents this
            null finding as a lack of detected association, not a proof of zero effect.
          source_ids:
          - P7-S1-C16
          - P8-S1-C10
        construct:
          answer: fits
          reason: The exposure is rsFC changes (measured via ROI-to-ROI analysis,
            P6-S1-C8, P6-S1-C15) and the outcome is naming improvements (trained and
            untrained items, P6-S2-C3). The patient measurement is functional_imaging
            (rs-fMRI), not template_lesion_overlap or patient_diffusion. The draft
            correctly identifies the imaging metric and behavioral target.
          source_ids:
          - P6-S1-C8
          - P6-S2-C3
          - P5-S1-C2
        qualifications:
          answer: fits
          reason: The draft includes the key qualification that the analysis used
            Spearman's correlation between individual beta values of significant rsFC
            changes and behavioral improvements (P6-S2-C3). It also lists relevant
            limitations such as small sample size and lack of control group (P10-S1-C8,
            P10-S1-C9).
          source_ids:
          - P6-S2-C3
          - P10-S1-C8
          - P10-S1-C9
        missing_material_caveat:
          answer: fits
          reason: 'The draft includes the main limitations mentioned in the source:
            small sample size (P10-S1-C8), absence of control group (P10-S1-C9), liberal
            outlier detection (P10-S2-C7), and lesion regression as CSF (P10-S2-C8).
            No material caveat that changes the interpretation of the null result
            is omitted.'
          source_ids:
          - P10-S1-C8
          - P10-S1-C9
          - P10-S2-C7
          - P10-S2-C8
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R004
      exposure:
        text: rsFC changes
      outcome:
        text: naming improvements (trained and untrained items)
      analysis_label: Correlation between rsFC Changes and Naming Improvements
      relation: association
      evidence_ids:
      - P7-S1-C16
      qualifier_ids:
      - P6-S2-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
        source_review: _compare/relationships-2026-11-16/review-current/MassonTrottier2021
        source_status_sha256: c4950ee8fcc5f471bc2437bb23b0cef3fb3a7b7916218de9d12a524aa1434089
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 339c09e3bef9f6747be3ffdcb8ec9b2bbd7c3d5fc8fa74d791191ebbd9643783
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C10
          page: 3
          text_layer_sha256: 339c09e3bef9f6747be3ffdcb8ec9b2bbd7c3d5fc8fa74d791191ebbd9643783
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants

          Ten participants with chronic aphasia (3 women, mean age = 68.9 ± 10.2)
          following a

          single left hemisphere ischemic stroke recruited through local patient association
          by referral

          following discharge from rehabilitation centers in the area and following
          self-referral are

          included in this study.'
        anchor_text: 'Participants

          Ten participants with chronic aphasia (3 women, mean age = 68.9 ± 10.2)
          following a

          single left hemisphere ischemic stroke recruited through local patient association
          by referral

          following discharge from rehabilitation centers in the area and following
          self-referral are

          included in this study.'
        excluded_fragments: []
        image_sha256: e25e6b4bc87233e036c5f12fa14b854cc9a169c2ac161afac554852c48619a64
        transcription: 'Participants

          Ten participants with chronic aphasia (3 women, mean age = 68.9 ± 10.2)
          following a single left hemisphere ischemic stroke recruited through local
          patient association by referral following discharge from rehabilitation
          centers in the area and following self-referral are included in this study'
      P3-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fd0200f0b1139aff4859d7633c63b2518cc2302494559f4ceb94a39c86c7a148
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 93db150e0f4f96095c08d09b065651468c5372bcbb4b1320965f16e48e54422a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C7
          page: 3
          text_layer_sha256: 93db150e0f4f96095c08d09b065651468c5372bcbb4b1320965f16e48e54422a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'A second lan-

          guage evaluation and fMRI session (T1) were performed within a week of the
          end of therapy.'
        anchor_text: 'A second lan-

          guage evaluation and fMRI session (T1) were performed within a week of the
          end of therapy.'
        excluded_fragments: []
        image_sha256: 1e24bc766e4f74429209425de7fb5eac9bfc41e7df546af8142ccc70a9a9247d
        transcription: '. A second lan-

          guage evaluation and fMRI session (T1) were performed within a week of the
          end of therapy'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'Within the group of 10 participants with aphasia, no signiﬁcant correlation
    was found

    between the rsFC changes and the main language outcome measures.


    '
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
