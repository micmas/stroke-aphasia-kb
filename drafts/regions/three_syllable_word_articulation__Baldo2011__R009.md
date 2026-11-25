---
id: three_syllable_word_articulation
name: 3-syllable word articulation
kind: classical
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: articulation_error_rate
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Experimental word-repetition articulation task
      subtest: 48 low-frequency words, repeated five times each
    metric: 0/1 apraxic-error score per word; syllable, consonant-cluster and articulatory-travel conditions
      retained in claim
    definition_source:
      citation: '@Baldo2011'
      page: 3
      quote: 'In a separate testing session, patients were administered an experimental test of articulation
        by two different licensed speech pathologists who were blind to the lesion analysis data. This test
        required patients to repeat an auditorily-pre- sented word five times in succession. For example,
        the examiner would say spaghetti, and the patient was asked to repeat the word five times. There
        were 48 words in total (see Table 1 for stimuli), and they varied on three dimensions: number of
        syllables, initial consonant cluster, and degree of travel. We chose to look at these three aspects
        of articulation, because they were suggested to be critical factors in a previous study on AOS (Ogar
        et al., 2006). The stimuli were all low frequency nouns (KuceraeFrancis count < 34), with word frequency
        matched across the three condition comparisons (i.e., low- vs high-travel, initial cluster vs no
        initial cluster, and 1-syllable vs 3-syllable words; all ps < .05). Data regarding other variables
        such as familiarity and age of acquisition were not available for all stimuli due to the use of
        low frequency words. Half of the stimuli were 1-syllable words, and the other half were 3-syllable
        words. Half of the words began with a consonant cluster (e.g., drill ), and the other half did not
        (e.g., zeal ). Half of the words had a low degree of travel (i.e., the consonants were in a similar
        place of articulation, e.g., nicety), and the other half, a high degree of travel (e.g., tobacco).
        The low-travel condition consisted of words ranging between zero travel (e.g., sanity) and one place
        transition (e.g., flattery), while the high-travel condition included words with one, two (e.g.,
        tobacco), and three place transitions (e.g., spaghetti). The degree of travel was based on the number
        of movements only; we did not factor in the “distance” (i.e., /pa/ to /ta/ was considered the same
        as /pa/ to /ka/). The test was videotaped, and the speech pathologist scored any apraxic errors
        in the patient’s performance. Patients received a score of 0 or 1 for each stimulus word (i.e.,
        trial of 5 repetitions). If there were no errors on the 5 repetitions, it was scored as 0, and if
        there were 1 or more errors on the 5 repe- titions, it was scored as 1 (i.e., whether the patient
        made 1 or 5 errors on the 5 repetitions, it was scored as a single error). Other errors such as
        those due to dysarthria or perseveration were not scored as errors.'
      basis: Main paper methods checked directly
      source_pdf: C0111_Baldo2011.pdf
      source_pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
    note: Measurement metadata identified from source evidence; finding remains unapproved. Not the screening
      Motor Speech Evaluation score.
  target: articulation_error_rate
  target_kind: impairment
  claim: Articulation of 3-syllable words produced significantly more errors than
    articulation of 1-syllable words
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 33
    population: right-handed native English speakers with a history of a single left
      hemisphere stroke
    phase: not_reported
    time_post_onset: post-acute phase
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Repetition of auditorily-presented 3-syllable low-frequency
    nouns five times in succession. compared to 1-syllable words. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S3-C7, two-model agreement, human verification pending): Participants


    The study included 33 patients (27 males) who had a history of a single, left
    hemisphere stroke Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - not_transcribed:author_limitations
    - proposed_concept:articulation_error_rate
  citation: '@Baldo2011'
  source_passages:
  - section: Original source P4-S2-C5
    page: 4
    quote: "Articulation\nof\n3-syllable\nwords\nproduced\nsigniﬁcantly\nmore\nerrors\n\
      than\narticulation\nof\n1-syllable words, t(32) ¼ \x044.03, p < .001 (M ¼ 28%\
      \ vs 17%,\nrespectively)."
    supports: claim
  - section: Original source P2-S3-C7
    page: 2
    quote: 'Participants

      The study included 33 patients (27 males) who had a history of

      a single, left hemisphere stroke.'
    supports: sample
  - section: Original source P2-S3-C8
    page: 2
    quote: 'Other study criteria included

      that patients be right-handed and native English speakers, with

      no prior history of psychiatric or neurologic disorders.'
    supports: sample
  - section: Original source P3-S1-C8
    page: 3
    quote: 'This test required patients to repeat an auditorily-pre-

      sented word ﬁve times in succession.'
    supports: method
  - section: Original source P3-S1-C14
    page: 3
    quote: 'Half of the stimuli were 1-syllable words, and the other

      half were 3-syllable words.'
    supports: method
  - section: Original source P7-S3-C9
    page: 7
    quote: 'It is important to note, however, that participants were

      tested in the post-acute phase of stroke, when both lesion site

      and behavioral proﬁle were relatively stable.'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Baldo2011
  proposal_id: R009
  review_status_sha256: 141a4fb5689892f8d2f1931c41ec85a7eae92e7127a089d4ee0c6ed4e545d87f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
        A/passages.json: 8083e272d817cba14f869241ece2dbd0b8b07aaf8a4e5cc8fa87a61995a562c1
        A/raw.json: 1232296423dea12a05e4355a2cbc6517d3af217579ed5cbaa5dfd34e58978c16
        A/source-units.json: 7d95fdfade9deaec907cb66afd0e0e3dab4ccf29d418db4dc948869414d7baba
        A/full-source-units.json: 7d95fdfade9deaec907cb66afd0e0e3dab4ccf29d418db4dc948869414d7baba
        A/meta.json: 690a08ff33d0116e36e2148a7e2912aaaa20c19e7359d5bd1f84dc901eafaa8a
        A/table-images/manifest.json: a389daf7b896da4318d055b2f94fa21da0e537a7bf41244237633fe588e5f839
        A/clauses/window-10/raw.json: 3133591e0d2d8423129772eadb4f35636d7be11c1578a71583de724ea39680a3
        A/clauses/window-10/prompt.txt: a88b50f600c9613e6312c3f7c75116b07f8732c508ca86cf52b1a451ffa22bc3
        A/clauses/window-10/meta.json: f24d7abb5dc9823a1d3ea9132a5777364bc3c3267342bcf9385f0fe075f1e7d0
        A/clauses/window-03/raw.json: 8bef49434c62af782f3eb29ba950346a6bbb9c44ef242b21dedee82fe24686ee
        A/clauses/window-03/prompt.txt: 0d1a258a0acdde105827e644f59a906da0d937c407515ca98a3e2b9c90db090a
        A/clauses/window-03/meta.json: 073b4508a8f94ae1829cf976ade5e0e479fae8f2fd91b2914f2530f587288198
        A/clauses/window-04/raw.json: ea1d5d4ba3347f14d7872df9c1066388db37e813a251801b23a0bcb91f248010
        A/clauses/window-04/prompt.txt: 59b8c247504ffdc6dbaa8492ce94285ddfce7fa2ee2de1c029111adbb821c921
        A/clauses/window-04/meta.json: ff87e25c75a4f0567da76f09a50173fe260b50a957d19e3a80d54f8393b0ad13
        A/clauses/window-05/raw.json: 998ef8121513d52c7d248a27e0a281e9ef956009559ea712391ed76b2f7a7498
        A/clauses/window-05/prompt.txt: 91dba86e4b883dc7121d10d9db338a2cc06a3a630f06294982dac177f6315da7
        A/clauses/window-05/meta.json: aad9e0442938ec22efb251ef5c10844620a847ebc9c1c04dc14f117291ce5b87
        A/clauses/window-02/raw.json: 7fe7c8096dc09a4562ac8253e3c3b856b69affc0a6c8d8c8f99e2fb09068451e
        A/clauses/window-02/prompt.txt: 892e59c93f85091176bb36720b6cf5faced2f717fed5a638db587293297e024c
        A/clauses/window-02/meta.json: ca234661804f959454414bfa57e1b24d977d7b15baf902dc2e8fba6212c67cc3
        A/clauses/window-09/raw.json: f88f66dadc9b68d14b49282f00a4f2474ee585168c6ef2b6b90985f11f8ec5d2
        A/clauses/window-09/prompt.txt: cbc05fd8d5637388d975e7e95f69cbe598df8e6e076528f32a0fffebe1190dc0
        A/clauses/window-09/meta.json: 319ed9a5030955c187d063ab612fcfb9027cdf47ade0b365a6d9e314d4073c28
        A/clauses/window-07/raw.json: 4b3d43378091a3a750ee40f9e742b4cff62ed9f271ab081d41cc1446af4bfa61
        A/clauses/window-07/prompt.txt: a8bd33bf367c1ea7d6da630030a80471816d1ac62feb6ad31bc39ce01df93d61
        A/clauses/window-07/meta.json: 85a4d2db5d6305973e3a5a32fe03f3d63d59ed5ef5e60ff4a3063f06c1ff1b23
        A/clauses/window-01/raw.json: 66c70294b6bd7da0f5113ddddaaf2f97c13670044cb8fb9be6b8fc9238fdac7b
        A/clauses/window-01/prompt.txt: 3953459ff03850369d65bf6aa75427d327616de9903adb04d7b415e2b729e797
        A/clauses/window-01/meta.json: d102cd632b4aaf3c8d245cc166d5dae55cc2be48f7146d939653e579bfc3784c
        A/clauses/window-06/raw.json: ebf477fc3a197b8657a2a12a004cc9791c0ed3248d8532c244d1b27b4fadd261
        A/clauses/window-06/prompt.txt: f7c1cda8dc7ea8b4145e305a5f7e32f609c52131c65559445f0a4980e6e8b49a
        A/clauses/window-06/meta.json: 5e68f9fab32e703789b4e508525b5b5715ea0ddcc55242fab61fa64ee63a5c3b
        A/clauses/window-08/raw.json: 25ae30646d30742118b941e3174b33721f3033b9c29d9bba295159d76c1cd8f7
        A/clauses/window-08/prompt.txt: 8d66616d559d7a0ec1e99e7cb96dde6a47176306f5355a385d801d51865c7954
        A/clauses/window-08/meta.json: dce25d1bd4e1b069d6490dd6e3c5ec8ba6b99a42fba7d0714f3beec0c0ddaa66
        B/passages.json: 8083e272d817cba14f869241ece2dbd0b8b07aaf8a4e5cc8fa87a61995a562c1
        B/raw.json: 2572c8d2c61e50557ff14e6522dacd30e6f65cba41d0f24c75133672c481470a
        B/source-units.json: 7d95fdfade9deaec907cb66afd0e0e3dab4ccf29d418db4dc948869414d7baba
        B/full-source-units.json: 7d95fdfade9deaec907cb66afd0e0e3dab4ccf29d418db4dc948869414d7baba
        B/meta.json: 179f1028b9f4b174ac13addea2463890f9e68363b09383c834760fce7a97b331
        B/table-images/manifest.json: a389daf7b896da4318d055b2f94fa21da0e537a7bf41244237633fe588e5f839
        B/clauses/window-10/raw.json: f30ba2dceb5820321fa03d4e52d768c2762e8dc908f5fb72e5a15071e15e2ab3
        B/clauses/window-10/prompt.txt: a88b50f600c9613e6312c3f7c75116b07f8732c508ca86cf52b1a451ffa22bc3
        B/clauses/window-10/meta.json: e073307d5dd182cdb9af822d58946911d40ecdf00066d665c529b8bfbc7eb28f
        B/clauses/window-03/raw.json: 11ca553be93cab99b24b47cfce2fc8d3a80a5a020886a7143a86b01dd9e5093b
        B/clauses/window-03/prompt.txt: 0d1a258a0acdde105827e644f59a906da0d937c407515ca98a3e2b9c90db090a
        B/clauses/window-03/meta.json: 1d2d5d5f5eb96ff621812d4f52066124e5afcd7742e31113b33ca889d78f46b4
        B/clauses/window-04/raw.json: 76a5916d2dfe45416aa2f6053eff2bc3b7f295e410c05f02a150a7584cff14c9
        B/clauses/window-04/prompt.txt: 59b8c247504ffdc6dbaa8492ce94285ddfce7fa2ee2de1c029111adbb821c921
        B/clauses/window-04/meta.json: 87f2be03b3388f58c236edd94290f4373e2c47620b26c1e32ca5d591902866f0
        B/clauses/window-05/raw.json: dde1b29c7c62aa5edfcb72a69f8b53d0869745dd3dd457ca150dee7944149c26
        B/clauses/window-05/prompt.txt: 91dba86e4b883dc7121d10d9db338a2cc06a3a630f06294982dac177f6315da7
        B/clauses/window-05/meta.json: 223b19b450931a03cea1e931738ff31fd458b88bbdef484dc7cebeefca3962b5
        B/clauses/window-02/raw.json: 5727ff2efabc543b9150b4d9485d99ef17789e405977f07218e7ea79b5ae1f2c
        B/clauses/window-02/prompt.txt: 892e59c93f85091176bb36720b6cf5faced2f717fed5a638db587293297e024c
        B/clauses/window-02/meta.json: 9dc8fa7b9d358b0e8af74533d3e25358a7353038c8e8a024ba379b26e2bce894
        B/clauses/window-09/raw.json: eb592eacb84970a3d9295ec015b2520358ce2e131f8b2b307b3127bc917dc189
        B/clauses/window-09/prompt.txt: cbc05fd8d5637388d975e7e95f69cbe598df8e6e076528f32a0fffebe1190dc0
        B/clauses/window-09/meta.json: f840f7a178138cba358735bc6b1fa3f2d75390dc7d711547828419ccb31c9287
        B/clauses/window-07/raw.json: 7bf1e0633a915f596bea4097508eaf4c780e10982bb5a0a2a46dab1920e58588
        B/clauses/window-07/prompt.txt: a8bd33bf367c1ea7d6da630030a80471816d1ac62feb6ad31bc39ce01df93d61
        B/clauses/window-07/meta.json: d8738cffcca56206528321c44704ad0913c68b35f9e7f4063d175a2232328313
        B/clauses/window-01/raw.json: 7237237d2a47468ab5fc80b083391d3b021b07a88903171178ebeee5247894f0
        B/clauses/window-01/prompt.txt: 3953459ff03850369d65bf6aa75427d327616de9903adb04d7b415e2b729e797
        B/clauses/window-01/meta.json: 765c1e347748d92e62d0b54aee15ff4f2b1ec46b390793fe8e3255a5163abae5
        B/clauses/window-06/raw.json: d77f3e920dfba4206baed26788518fabb1d5f69697d37824d37dcb3d28842d40
        B/clauses/window-06/prompt.txt: f7c1cda8dc7ea8b4145e305a5f7e32f609c52131c65559445f0a4980e6e8b49a
        B/clauses/window-06/meta.json: 3f026b2438d8ce130b658781052531d536e74abc2c7ad57137b6dbf1890e6619
        B/clauses/window-08/raw.json: 1f2fc7cb52d04368d50391aac725c85f0b5d76fa53eddb57e26b6ad76c3b678c
        B/clauses/window-08/prompt.txt: 8d66616d559d7a0ec1e99e7cb96dde6a47176306f5355a385d801d51865c7954
        B/clauses/window-08/meta.json: ef1530ffdba5c2dc4427848afc840e15c3507f491546556bc81194e8a539f827
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
      pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2011
      source_status_sha256: 5d9715b5396e3dd9148083a38c3dd30df4f4351f014fbc31bf13a491d4112275
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: 3-syllable words
    outcome:
      text: articulation error rate
    analysis_label: Behavioral analysis
    relation: association
    evidence_ids:
    - P4-S2-C5
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
      pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2011
      source_status_sha256: 5d9715b5396e3dd9148083a38c3dd30df4f4351f014fbc31bf13a491d4112275
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S2-C4
      - Result passage disposed without unit P2-S4-C3
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C6
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 149
      unselected_timing_passages:
      - P2-S3-C12
      - P7-S3-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P7-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S3-C15
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2011
      source_status_sha256: 5d9715b5396e3dd9148083a38c3dd30df4f4351f014fbc31bf13a491d4112275
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes power analysis for predictions.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 4
      reason: Abstract restatement of VLSM results.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Abstract restatement of minimal complexity result.
    - source_id: P2-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient example of AOS.
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of AOS patterns.
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case study report (Nagao et al.).
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/score summary (WAB).
    - source_id: P2-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification summary (WAB).
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification summary (WAB).
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/score summary (MSE).
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification summary (MSE).
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/classification summary (MSE).
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Stimuli frequency matching description.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Imaging acquisition details.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1 (overlay map).
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion distribution.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2 (power map).
    - source_id: P4-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting critical t-values for VLSM.
    - source_id: P4-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting critical t-values for VLSM.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Direct behavioral result for syllable count.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Direct behavioral result for travel.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 12
      - 13
      reason: Direct behavioral result for clusters.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Direct VLSM result for 3-syllable words.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Direct VLSM result for 3- vs 1-syllable words.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting small number of voxels in other regions.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about travel VLSM pattern.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Direct VLSM result for high- vs low-travel words.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting small number of voxels in other regions.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Direct VLSM result for cluster vs no cluster.
    - source_id: P5-S2-C1
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Restatement of cluster VLSM result.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting small number of voxels in other regions.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Direct VLSM result for combined complexity vs minimal.
    - source_id: P6-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 4
      reason: Discussion restatement of VLSM results.
    - source_id: P6-S1-C8
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of minimal complexity result.
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of specificity and other lab studies.
    - source_id: P7-S3-C6
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 4
      reason: Discussion restatement of critical conditions.
    - source_id: P7-S4-C2
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 4
      reason: Discussion restatement of critical conditions.
    - source_id: P7-S4-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of minimal complexity result.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S2-C3
    - P2-S1-C7
    - P2-S1-C8
    - P2-S2-C4
    - P2-S4-C3
    - P2-S4-C4
    - P3-S1-C1
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C12
    - P3-S2-C13
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C6
    - P4-S1-C15
    - P4-S2-C1
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C10
    - P5-S2-C1
    - P5-S2-C2
    - P6-S1-C7
    - P6-S1-C8
    - P7-S3-C3
    - P7-S3-C6
    - P7-S4-C2
    - P7-S4-C3
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
      - P2-S3-C7
      - P3-S1-C4
      recruited_sample:
      - P2-S3-C7
      - P2-S3-C10
      eligibility:
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      imaging_provenance:
      - P3-S2-C13
      - P3-S2-C14
      - P3-S2-C15
      - P3-S2-C16
      - P3-S3-C4
      - P3-S3-C6
      imaging_timing:
      - P3-S2-C11
      outcome_timing:
      - P3-S2-C12
      outcome_definition:
      - P4-S1-C11
      - P5-S1-C2
      validation: []
      analysis_restrictions:
      - P4-S1-C9
      - P4-S1-C10
      dependent_variable_statement:
      - P4-S1-C11
      - P5-S1-C2
      limitations:
      - P7-S2-C10
      - P7-S2-C11
      - P7-S3-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C12
      - P3-S1-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: validation
      source_id: P7-S3-C3
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
      pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
      review_sha256: 141a4fb5689892f8d2f1931c41ec85a7eae92e7127a089d4ee0c6ed4e545d87f
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
      source_result: Behavioral analysis showed that articulation of 3-syllable words
        produced significantly more errors than articulation of 1-syllable words (t(32)
        = 4.03, p < .001; M = 28% vs 17%).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the behavioral comparison of error rates
            between 3-syllable and 1-syllable words, as described in P4-S2-C5. The
            proposed core correctly identifies this as a behavioral analysis (paired
            t-test) rather than the subsequent VLSM lesion analysis.
          source_ids:
          - P4-S2-C5
          - P4-S2-C4
        direction:
          answer: fits
          reason: The source states 3-syllable words produced significantly more errors
            than 1-syllable words. The proposed core claims 'significantly more errors'
            for 3-syllable words, preserving the direction of the effect.
          source_ids:
          - P4-S2-C5
        construct:
          answer: fits
          reason: Exposure is 3-syllable words vs 1-syllable words. Outcome is articulation
            error rate. The method is behavioral (repetition task). The patient measurement
            is non-imaging (behavioral scores), distinct from the VLSM lesion mapping
            which uses imaging data. The core correctly separates the behavioral finding
            from the lesion analysis.
          source_ids:
          - P4-S2-C5
          - P3-S1-C8
          - P3-S1-C14
        qualifications:
          answer: fits
          reason: The core includes the qualification 'compared to 1-syllable words',
            which is essential to the specific contrast. The population (left hemisphere
            stroke) and timing (post-acute) are correctly identified from P2-S3-C7
            and P7-S3-C9.
          source_ids:
          - P4-S2-C5
          - P2-S3-C7
          - P7-S3-C9
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core is a qualitative draft
            of the behavioral result. The limitations regarding VLSM coverage (P7-S2-C10)
            apply to the lesion analysis, not the behavioral t-test. The OCR warnings
            on P4-S2-C5 do not obscure the core finding of significance and direction.
          source_ids:
          - P4-S2-C5
          - P7-S2-C10
      optional_pending:
      - Exact t-statistic and p-value transcription
      - Mean error rates (28% vs 17%)
      - Specific MNI coordinates for associated voxels
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact t-statistic and p-value transcription
    - Mean error rates (28% vs 17%)
    - Specific MNI coordinates for associated voxels
    normalizations:
    - field: bucket
      original: impairments
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R009
      exposure:
        text: 3-syllable words
      outcome:
        text: articulation error rate
      analysis_label: Behavioral analysis
      relation: association
      evidence_ids:
      - P4-S2-C5
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
        pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
        source_review: _compare/relationships-2026-11-16/review-current/Baldo2011
        source_status_sha256: 5d9715b5396e3dd9148083a38c3dd30df4f4351f014fbc31bf13a491d4112275
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5b798afb365455785424b290a4b96828fce7a37b31a33a214b93d6d299a3134d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C5
          page: 4
          text_layer_sha256: 5b798afb365455785424b290a4b96828fce7a37b31a33a214b93d6d299a3134d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Articulation\nof\n3-syllable\nwords\nproduced\nsigniﬁcantly\n\
          more\nerrors\nthan\narticulation\nof\n1-syllable words, t(32) ¼ \x044.03,\
          \ p < .001 (M ¼ 28% vs 17%,\nrespectively)."
        anchor_text: "Articulation\nof\n3-syllable\nwords\nproduced\nsigniﬁcantly\n\
          more\nerrors\nthan\narticulation\nof\n1-syllable words, t(32) ¼ \x044.03,\
          \ p < .001 (M ¼ 28% vs 17%,\nrespectively)."
        excluded_fragments: []
      P2-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 30de9cfab53deb282fe5a6eb5ca2ac07738f7163fa8a9bcacb15f5ce2b3e8cc4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 77cecb93f1cee7155daace5c08cfbfd713bf8899d71ecc47bada24f59e4deef6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C7
          page: 2
          text_layer_sha256: 77cecb93f1cee7155daace5c08cfbfd713bf8899d71ecc47bada24f59e4deef6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants

          The study included 33 patients (27 males) who had a history of

          a single, left hemisphere stroke.'
        anchor_text: 'Participants

          The study included 33 patients (27 males) who had a history of

          a single, left hemisphere stroke.'
        excluded_fragments: []
        image_sha256: 1e2866207698ea3f8410591133746aa468a266588d81af0b2383a7f0974ca8d3
        transcription: 'Participants


          The study included 33 patients (27 males) who had a history of a single,
          left hemisphere stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "Articulation\nof\n3-syllable\nwords\nproduced\nsigniﬁcantly\nmore\nerrors\n\
    than\narticulation\nof\n1-syllable words, t(32) ¼ \x044.03, p < .001 (M ¼ 28%\
    \ vs 17%,\nrespectively)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
