---
id: left_inferior_frontal_lesion
name: left inferior frontal lesion
kind: classical
findings:
- id: f1
  target: right_ifg_activation
  target_kind: impairment
  claim: Left inferior frontal lesions resulted in a greater likelihood of right inferior
    frontal gyrus (IFG) activation compared to patients whose lesions spared the inferior
    frontal cortex.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: not_reported
    population: patients with chronic aphasia after stroke
    phase: not_reported
    time_post_onset: chronic phase
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Findings cannot be extrapolated to acute or subacute aphasia
  - Unable to determine if activation patterns vary by aphasia type or specific language
    task due to limited available studies
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Patient lesion involvement of the inferior frontal
    cortex, extrapolated from published text, figures, and tables in the included
    studies. The finding is based on activation likelihood estimation (ALE) of peak
    activity coordinates from multiple studies; The ''left inferior frontal lesion''
    group included 65 patients (approximately 62 nonfluent); The ''sparing'' group
    included 40 patients (approximately 32 fluent). Additional metadata has not been
    transcribed; review the pending-field flags before approval.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:right_ifg_activation
  citation: '@Turkeltaub2011'
  source_passages:
  - section: Original source P3-S1-C8
    page: 3
    quote: "Subanalyses of the IF\x02 and IF\x03\ngroups demonstrated that left inferior\
      \ frontal lesions\nresulted in greater likelihood of right IFG activation\n\
      (figure 2)."
    supports: claim
  - section: Original source P2-S2-C2
    page: 2
    quote: "To examine the\nimpact of lesion location on activity, we split the aphasia\
      \ dataset\ninto a group of patients with lesions involving inferior frontal\n\
      cortex (IF\x02; n \x01 65; approximately 62 nonfluent), and a group\nwith lesions\
      \ sparing it (IF\x03; n \x01 40; approximately 32 fluent)."
    supports: sample
  - section: Original source P1-S1-C6
    page: 1
    quote: "Methods: Functional neuroimaging articles using language tasks in patients\
      \ with chronic aphasia\nafter stroke (n \x01 105) and control subjects (n \x01\
      \ 129) were collected."
    supports: sample
  - section: Original source P2-S1-C3
    page: 2
    quote: 'We used activation likelihood estimation

      (ALE), a validated, quantitative neuroimaging

      meta-analysis method,19-21 to assess mecha-

      nisms of adaptation in aphasia by comparing

      brain activity of patients with chronic aphasia

      to that of normal control subjects across a va-

      riety of experimental contexts.'
    supports: method
  - section: Original source P7-S2-C5
    page: 7
    quote: 'Since neural adaptation in

      aphasia changes over time,5 these findings also can-

      not be extrapolated to acute or subacute aphasia.'
    supports: limitation
  - section: Original source P7-S2-C6
    page: 7
    quote: 'We

      elected to include any aphasia type or language task,

      but due to the few studies available we were unable to

      determine whether activation patterns and adaptive

      mechanisms vary based on these factors, which they

      almost certainly do.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Turkeltaub2011
  proposal_id: R003
  review_status_sha256: b8f27f868485b345ebdeb6cd1b5074f79a0725e04390242bcc92e15579e19c2b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
        A/passages.json: 0d07d8ffad2bfe7708ed5bc572fab2ce7f59146cf5394ffee6bb00df6629cbae
        A/raw.json: 48ca8b7e80cfdcdbeced6af1ab5333f166f6758f9e03718e6014ea45fab6b208
        A/source-units.json: b1420a13cd750c9bb2218b91b5ab144de74cae5eded85f007865c0f128805be8
        A/full-source-units.json: e448d96501dbff80c7de4c720ee85f6a6e9761f8b093be83648353f15fae467d
        A/meta.json: dc493bf7b1ab80f56ec8972ea967726a1f6518c62669625c7c0c8e830db51e01
        A/table-images/manifest.json: 1b96961476e5ded6fe789a8ae30352702d6dce1e271f3253beb1d20bed532dc0
        A/clauses/window-03/raw.json: 021383fb1946b442954c084798075b2f529ba9deeb1de030ecbcc6462cd60ba1
        A/clauses/window-03/prompt.txt: f42a0b3bf5cc69b7b2a85a6b57ced0b944430af033e8b4c0f64a64730ae84fd9
        A/clauses/window-03/meta.json: f4b7152da9c42c01eb3ee30b254bf7e8fe5a7675da8e8d0311bdebe4c20ec545
        A/clauses/window-04/raw.json: f055b0707eb741fcfcab1f8989620ec69b24da6be5cf740ed3b4ac39136541d6
        A/clauses/window-04/prompt.txt: 0c18c9cf2a24989185598ae5eb83c1e82cc8d75d2dfcca5a9dbf536e27b3caab
        A/clauses/window-04/meta.json: b189793d0b0dc62c38d48eb3292624a2b8a2ee5ba96c4cae3dd6af041bf46e9a
        A/clauses/window-05/raw.json: dce6d9347d9b6cbc6b8b05fc627ff7c3551a9bf6a5d5712f0372b84b9d3af1cf
        A/clauses/window-05/prompt.txt: c35cab1ea09395453a3b5eb6f7689dbd5d9f25606ef1d6608ac488deaed81a17
        A/clauses/window-05/meta.json: 5809be367aa171000c61412ca235e65c0800d4c01891a06f9a8e9f0bf50e81a3
        A/clauses/window-02/raw.json: c344fe7272b5a65d0feda930d51be81a04329b721c637f9452f32bf6982a2d1c
        A/clauses/window-02/prompt.txt: 712b8c9633de8fa479cf486dd6bbd748238e0bd77a7f1c514c819719a7339cdf
        A/clauses/window-02/meta.json: 4ef4e4f2997cfd380205eb0de58d6f63cbeab3a78485b93a1dbc91f8a8b46e93
        A/clauses/window-01/raw.json: 4f707b3a18f00662070521de5f4d8f2ec37456091ffd439484fa3783b82705bf
        A/clauses/window-01/prompt.txt: ac31d553948f584452af4f6aa978f7d1a36da4138deac28e82629787b612fbc0
        A/clauses/window-01/meta.json: b34bc862f89428e09dfcb31be0dc785ed4d91f5c0942c6093b2abe9832449394
        A/clauses/window-06/raw.json: 1c5b435e59a5be170fbe07f0af117d059b9b4e7efb4cc90da408c8bb291389f6
        A/clauses/window-06/prompt.txt: 95c23305bf8128a9a0a38536a62079de232a4bd3e56c8f33f8388931055269a8
        A/clauses/window-06/meta.json: 38329af179804708f5efb210666817b9f86eca650985592f8fcbd0e46015388c
        B/passages.json: 0d07d8ffad2bfe7708ed5bc572fab2ce7f59146cf5394ffee6bb00df6629cbae
        B/raw.json: b24f092f0016c6089bae72396803efd3dd4d7b45b9eea0466d992a17f9f403a2
        B/source-units.json: b1420a13cd750c9bb2218b91b5ab144de74cae5eded85f007865c0f128805be8
        B/full-source-units.json: e448d96501dbff80c7de4c720ee85f6a6e9761f8b093be83648353f15fae467d
        B/meta.json: 58e5964249eaa4ef2dbdc193fb3dfd72039b5514d6fb0298926dae302a78d127
        B/table-images/manifest.json: 1b96961476e5ded6fe789a8ae30352702d6dce1e271f3253beb1d20bed532dc0
        B/clauses/window-03/raw.json: 7c8dfe3b3346dda68a2939757c69c28b481dfcc090660f4d6d52916bc600026a
        B/clauses/window-03/prompt.txt: f42a0b3bf5cc69b7b2a85a6b57ced0b944430af033e8b4c0f64a64730ae84fd9
        B/clauses/window-03/meta.json: 28b4ec43ff5072e9d4b696c5aec9a9efd2365d1fab2291dcb9963940e2a8aa5d
        B/clauses/window-04/raw.json: f94cd584a22f5fba31bb1108e2c7befe534389f782ceb0e06db8fe154062d27b
        B/clauses/window-04/prompt.txt: 0c18c9cf2a24989185598ae5eb83c1e82cc8d75d2dfcca5a9dbf536e27b3caab
        B/clauses/window-04/meta.json: c9c35d70f122701e69c0609484ffece909f3de914b813ba29deceb7d3e455d61
        B/clauses/window-05/raw.json: 1ecc53340d04f70f72afb1c168fcb4ecd2a65603681256d8dfa0c9039df75513
        B/clauses/window-05/prompt.txt: c35cab1ea09395453a3b5eb6f7689dbd5d9f25606ef1d6608ac488deaed81a17
        B/clauses/window-05/meta.json: bb6ce0048cee01156bd5c3fde38032f21aeb39216834da2abb4168c5dbfa4569
        B/clauses/window-02/raw.json: e19f6fd33eb2118bedb3c3f421ec7facd4193abfec6ab610d118755e1e1cf7bb
        B/clauses/window-02/prompt.txt: 712b8c9633de8fa479cf486dd6bbd748238e0bd77a7f1c514c819719a7339cdf
        B/clauses/window-02/meta.json: 8d8965c9d84312ec711ab9e6556e18705f74dbd43fdeab299c8e9cc2a88463d5
        B/clauses/window-01/raw.json: 65835f8f902daf1251f49c2866fe41635a80ab07db948d4ad5b8dba4e41fe674
        B/clauses/window-01/prompt.txt: ac31d553948f584452af4f6aa978f7d1a36da4138deac28e82629787b612fbc0
        B/clauses/window-01/meta.json: af8d9bc84af173e60fd1d2e440959c4d4d3d907029b0c35b50f2b047c047527c
        B/clauses/window-06/raw.json: 1c5b435e59a5be170fbe07f0af117d059b9b4e7efb4cc90da408c8bb291389f6
        B/clauses/window-06/prompt.txt: 95c23305bf8128a9a0a38536a62079de232a4bd3e56c8f33f8388931055269a8
        B/clauses/window-06/meta.json: 0861ffb14b30649e668d57ae2b00621abcae391cea29a41367ff76a71835d161
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
      pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
      source_review: _compare/relationships-2026-11-16/review-current/Turkeltaub2011
      source_status_sha256: ef219534d55aaa1a6c10a1d20483a7b62bb92c39639c687ad443a18c709008be
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: Left inferior frontal lesions
    outcome:
      text: Right IFG activation
    analysis_label: IF lesion subanalysis
    relation: association
    evidence_ids:
    - P3-S1-C8
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
      pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
      source_review: _compare/relationships-2026-11-16/review-current/Turkeltaub2011
      source_status_sha256: ef219534d55aaa1a6c10a1d20483a7b62bb92c39639c687ad443a18c709008be
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S2-C6
      - Result passage disposed without unit P2-S4-C3
      - Result passage disposed without unit P3-S1-C10
      - Accounting without a linked unit P3-S1-C6
      - Accounting without a linked unit P3-S1-C8
      - Accounting without a linked unit P3-S1-C9
      - Result passage disposed without unit P4-S1-C1
      - Unaccounted source passage P3-S1-C8
      - Unaccounted source passage P3-S1-C9
      - Unaccounted source passage P3-S1-C6
      - Result passage disposed without unit P4-S1-C3
      - Accounting without a linked unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Result passage disposed without unit P6-S1-C1
      - Unaccounted source passage P4-S1-C7
      - Unaccounted source passage P4-S1-C5
      - Unaccounted source passage P4-S1-C6
      - Unaccounted source passage P4-S1-C4
      - Accounting without a linked unit P6-S2-C2
      - Accounting without a linked unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C5
      - Accounting without a linked unit P6-S2-C6
      - Accounting without a linked unit P6-S2-C7
      - Accounting without a linked unit P6-S2-C9
      - Accounting without a linked unit P6-S3-C2
      - Unaccounted source passage P6-S2-C2
      - Unaccounted source passage P6-S2-C6
      - Unaccounted source passage P6-S2-C3
      - Unaccounted source passage P6-S3-C2
      - Unaccounted source passage P6-S2-C7
      - Unaccounted source passage P6-S2-C9
      - Unaccounted source passage P6-S2-C5
      - Accounting without a linked unit P7-S2-C1
      - Unaccounted source passage P7-S2-C1
      unattached_null_or_qualifier_ids:
      - P3-S1-C10
      - P4-S1-C7
      - P6-S2-C6
      - P6-S2-C9
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 100
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P2-S4-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P2-S2-C12
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
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
        - P3-S1
        - P4-S1
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
      source_review: _compare/relationships-2026-11-16/review-current/Turkeltaub2011
      source_status_sha256: ef219534d55aaa1a6c10a1d20483a7b62bb92c39639c687ad443a18c709008be
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Describes control network activation.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Describes aphasic patient network activation.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Describes right IFG recruitment in left IF lesions.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 8
      - 13
      reason: Mentions homology of right POp and null homology of right PTr.
    - source_id: P1-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement about consistency.
    - source_id: P2-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological detail on assignment accuracy.
    - source_id: P2-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Example of control LH activation.
    - source_id: P2-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Example of aphasic activation.
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological simulation result.
    - source_id: P2-S4-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Control ALE results.
    - source_id: P2-S4-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Control IFG activation details.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Control IFG activation details.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Control pMTG activation.
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Aphasic ALE results.
    - source_id: P3-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Aphasic network composition.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Aphasic IFG activation.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: IF lesion effect on right IFG.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Homology of spared LH nodes.
    - source_id: P3-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of non-overlapping clusters.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Homology of POrb/insula and null homology of MFG.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: RH cluster homotopy.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on RH IFG patterns.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Right ventral POp homology.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: IF lesion specific RH nodes.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Right PTr null homology.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of small right PTr cluster in IF sparing group.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on compensatory mechanisms.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figure 3.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of aphasic network consistency.
    - source_id: P6-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of aphasic network composition.
    - source_id: P6-S1-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of lesion location effect.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on compensatory mechanisms.
    - source_id: P6-S1-C13
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of spared LH node activity.
    - source_id: P6-S1-C14
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of spared node role.
    - source_id: P6-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on LH areas outside normal network.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Anterior insula homology to POrb.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right POrb as alternate node.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 11
      reason: Left POrb homology in IF sparing group.
    - source_id: P6-S2-C7
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of POrb shift.
    - source_id: P6-S2-C9
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of MFG null homology.
    - source_id: P6-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on lack of consistent RH activity in controls.
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inference about RH activity.
    - source_id: P6-S3-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of right IFG recruitment in IF lesions.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on right PTr function.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Right dorsal POp homology.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on RH mechanisms.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Right PTr null homology.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis on right PTr dysfunction.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Confirmation of right PTr functional difference.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of adaptation patterns.
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion on stimulation targeting.
    unresolved_coverage:
    - source_id: P7-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P2-S2-C6
    - P2-S2-C9
    - P2-S2-C10
    - P2-S4-C3
    - P3-S1-C10
    - P4-S1-C3
    - P4-S1-C7
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C13
    - P6-S1-C14
    - P6-S1-C15
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C9
    - P6-S3-C2
    - P6-S3-C3
    - P6-S3-C4
    - P6-S3-C5
    - P7-S1-C3
    - P7-S1-C8
    - P7-S2-C6
    - P7-S3-C2
    - P7-S3-C3
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
      - P2-S1-C10
      recruited_sample:
      - P2-S1-C10
      eligibility:
      - P2-S1-C6
      - P2-S1-C7
      - P7-S2-C7
      - P7-S2-C8
      imaging_provenance:
      - P2-S2-C14
      imaging_timing:
      - P2-S1-C5
      outcome_timing:
      - P2-S1-C5
      outcome_definition:
      - P2-S1-C12
      validation: []
      analysis_restrictions:
      - P2-S1-C7
      dependent_variable_statement:
      - P2-S2-C12
      limitations:
      - P7-S2-C4
      - P7-S2-C5
      - P7-S2-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C13
      - P2-S1-C14
      - P2-S2-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: validation
      source_id: P2-S4-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P2-S2-C12
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
      pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
      review_sha256: b8f27f868485b345ebdeb6cd1b5074f79a0725e04390242bcc92e15579e19c2b
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
      - P3-S1-C8
      source_result: Subanalyses of the IF+ and IF- groups demonstrated that left
        inferior frontal lesions resulted in greater likelihood of right IFG activation
        (figure 2).
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the IF lesion subanalysis described in
            P3-S1-C8, which compares the IF+ and IF- groups. The proposed core correctly
            identifies this as a subanalysis of the ALE meta-analysis.
          source_ids:
          - P3-S1-C8
          - P2-S2-C2
        direction:
          answer: fits
          reason: The source states that left inferior frontal lesions resulted in
            'greater likelihood' of right IFG activation. The proposed core claims
            'greater likelihood' and direction 'likely', which preserves the detected
            association direction.
          source_ids:
          - P3-S1-C8
        construct:
          answer: fits
          reason: The exposure is 'Left inferior frontal lesions' (IF+ group) and
            the outcome is 'Right IFG activation'. The source P3-S1-C8 explicitly
            links these. The patient measurement is functional imaging (ALE of fMRI/PET
            coordinates), not diffusion or template overlap. The proposed core correctly
            identifies the exposure and outcome.
          source_ids:
          - P3-S1-C8
          - P2-S2-C2
          - P2-S1-C3
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications regarding the ALE method,
            sample sizes (65 vs 40), and limitations regarding chronic phase and aphasia
            type heterogeneity. These align with the source passages P2-S2-C2, P7-S2-C5,
            and P7-S2-C6.
          source_ids:
          - P2-S2-C2
          - P7-S2-C5
          - P7-S2-C6
        missing_material_caveat:
          answer: fits
          reason: The core includes the key limitations mentioned in the discussion
            (chronic phase restriction, heterogeneity of aphasia types/tasks). No
            material caveat that changes the interpretation of the specific IF subanalysis
            result appears to be omitted.
          source_ids:
          - P7-S2-C5
          - P7-S2-C6
      optional_pending:
      - Specific statistical values (p-values, FDR q) for the IF subanalysis are not
        transcribed in the provided source window, only the qualitative result and
        reference to Figure 2.
      - Exact coordinates of the right IFG peaks in the IF+ group are not transcribed
        in the provided source window.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values (p-values, FDR q) for the IF subanalysis are not
      transcribed in the provided source window, only the qualitative result and reference
      to Figure 2.
    - Exact coordinates of the right IFG peaks in the IF+ group are not transcribed
      in the provided source window.
    normalizations:
    - field: sample.n
      original: 105
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R003
      exposure:
        text: Left inferior frontal lesions
      outcome:
        text: Right IFG activation
      analysis_label: IF lesion subanalysis
      relation: association
      evidence_ids:
      - P3-S1-C8
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
        pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
        source_review: _compare/relationships-2026-11-16/review-current/Turkeltaub2011
        source_status_sha256: ef219534d55aaa1a6c10a1d20483a7b62bb92c39639c687ad443a18c709008be
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d34d4685f3e8d7bb23066bb46a2017bc548a98cf6b156d7c4e3788105897aca1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C8
          page: 3
          text_layer_sha256: d34d4685f3e8d7bb23066bb46a2017bc548a98cf6b156d7c4e3788105897aca1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Subanalyses of the IF\x02 and IF\x03\ngroups demonstrated\
          \ that left inferior frontal lesions\nresulted in greater likelihood of\
          \ right IFG activation\n(figure 2)."
        anchor_text: "Subanalyses of the IF\x02 and IF\x03\ngroups demonstrated that\
          \ left inferior frontal lesions\nresulted in greater likelihood of right\
          \ IFG activation\n(figure 2)."
        excluded_fragments: []
      P2-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1465f0ed4dff13a29f9c9417acf534cd85553c22613ba9fec2d781d057680e75
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C2
          page: 2
          text_layer_sha256: 1465f0ed4dff13a29f9c9417acf534cd85553c22613ba9fec2d781d057680e75
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "To examine the\nimpact of lesion location on activity, we\
          \ split the aphasia dataset\ninto a group of patients with lesions involving\
          \ inferior frontal\ncortex (IF\x02; n \x01 65; approximately 62 nonfluent),\
          \ and a group\nwith lesions sparing it (IF\x03; n \x01 40; approximately\
          \ 32 fluent)."
        anchor_text: "To examine the\nimpact of lesion location on activity, we split\
          \ the aphasia dataset\ninto a group of patients with lesions involving inferior\
          \ frontal\ncortex (IF\x02; n \x01 65; approximately 62 nonfluent), and a\
          \ group\nwith lesions sparing it (IF\x03; n \x01 40; approximately 32 fluent)."
        excluded_fragments: []
      P1-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0a7ff23965c385032a7073cbb350bcf119ae89a7d2c9a1a1a0d93dab6ee0fb7e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f3430d15e3710920b72506a83be859a08e0f33ab3c73a7839e90630b62d394b5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C6
          page: 1
          text_layer_sha256: f3430d15e3710920b72506a83be859a08e0f33ab3c73a7839e90630b62d394b5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Methods: Functional neuroimaging articles using language tasks\
          \ in patients with chronic aphasia\nafter stroke (n \x01 105) and control\
          \ subjects (n \x01 129) were collected."
        anchor_text: "Methods: Functional neuroimaging articles using language tasks\
          \ in patients with chronic aphasia\nafter stroke (n \x01 105) and control\
          \ subjects (n \x01 129) were collected."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "Subanalyses of the IF\x02 and IF\x03\ngroups demonstrated that left inferior\
    \ frontal lesions\nresulted in greater likelihood of right IFG activation\n(figure\
    \ 2)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
