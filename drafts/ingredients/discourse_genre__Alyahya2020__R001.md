---
id: discourse_genre
name: discourse genre
kind: ingredient
findings:
- id: f1
  target: connected_speech_performance
  target_kind: impairment
  claim: Performance on connected speech measures differed across discourse genres;
    specifically, storytelling narratives provided higher quantities of content words
    and lexical diversity compared to composite picture description and procedural
    discourse.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: patients with chronic post-stroke aphasia
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
  - personal discourse (e.g., 'tell me about your stroke') was excluded to avoid heterogeneity
    and reliance on long-term memory
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The type of connected speech task performed by the
    patient, specifically comparing a composite picture description (Cookie Theft),
    a storytelling narrative (Dinner Party), and unsupported procedural discourse
    (preparing a cup of tea). storytelling narrative was significantly higher than
    both composite picture description and procedural discourse for quantity of production;
    for lexical diversity, storytelling was highest, followed by composite picture
    description and then procedural discourse; for speech rate, the fastest speech
    was produced during procedural discourse, followed by picture description, and
    then storytelling. Additional metadata has not been transcribed; review the pending-field
    flags before approval. Reconcile this new analysis with earlier drafts and source-review
    decisions for the paper; new candidate IDs do not carry earlier decisions forward.'
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
    - not_transcribed:sample.n
    - not_transcribed:sample.time_post_onset
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:connected_speech_performance
  citation: '@Alyahya2020'
  source_passages:
  - section: Original source P1-S1-C11
    page: 1
    quote: 'Content analyses conducted on all connected speech samples indicated

      that performance differed across discourse genres and between groups.'
    supports: claim
  - section: Original source P1-S1-C12
    page: 1
    quote: 'Speciﬁcally, storytelling narratives provided higher quanti-

      ties of content words and lexical diversity compared to composite picture description
      and procedural discourse.'
    supports: claim
  - section: Original source P3-S1-C8
    page: 3
    quote: 'Materials and methods

      Participants

      Forty-six patients who had developed aphasia following a single

      left haemorrhagic or ischaemic stroke were tested in the chronic

      stage (412 months post-stroke).'
    supports: sample
  - section: Original source P3-S2-C4
    page: 3
    quote: 'Discourse samples

      Three discourse samples were collected from each participant

      with no time limit: (i) descriptive discourse, elicited using the

      ‘Cookie Theft’ composite picture from the BDAE (Goodglass

      and Kaplan, 1983); (ii) narrative discourse, elicited using a

      ‘Dinner Party’ storytelling script (Fletcher and Birt, 1983), which

      involved a series of eight black-and-white sequences of pictures;

      and (iii) unsupported procedural discourse, which was elicited

      by asking participants to describe ‘how they prepare a cup of

      tea’.'
    supports: method
  - section: Original source P5-S1-C3
    page: 5
    quote: 'For quantity of produc-

      tion, storytelling narrative was significantly higher than both

      composite

      picture

      description

      and

      procedural

      discourse

      (P5 0.001).'
    supports: claim
  - section: Original source P5-S1-C4
    page: 5
    quote: 'For lexical diversity, storytelling was again the

      highest, followed by composite picture description and then

      procedural discourse.'
    supports: claim
  - section: Original source P5-S1-C6
    page: 5
    quote: 'Finally, for speech rate,

      the fastest speech was produced during procedural discourse,

      followed by picture description, and then storytelling.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Alyahya2020
  proposal_id: R001
  review_status_sha256: 2568f8e8fd3fcb3e46c5c0ec673c4dd1ad443886b7107e9ca56082c087a0b526
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
        A/passages.json: 9911233de4e837bf81ba7b6fd2d506e7b02d9f201d3f3f9c76fa87f396473b41
        A/raw.json: 927365420fa3a9f31ce43024189a8b27ad1a3fee901562b8af14597e652dc28b
        A/source-units.json: 5385076b47c3f953efaf01fff04edda1796fe4f5ff57fdd6cd93054b4cc2fedf
        A/full-source-units.json: 506f27cd9c6b5a72cb96e6d2be95432885ad69a55146ac9fac0ba598476ccffc
        A/meta.json: f21184492fb92a7caa58322b05181047963d62ceab371b099ec53b61b8155644
        A/table-images/page-10.png: 102d76252b3cec1f61a5d8290d340e4f288bff2e5bc34fce7772d035f3fecf7e
        A/table-images/page-4.png: df53d5d8f28a82be71abaf653d8e05041aa03031a89c67f4ecf3fa39134d4db9
        A/table-images/TABLE-1-page-4-1.png: 1be9e838e72f02cefcf039c55841dc92e6f4cd231dc4463f9886a5afc430195b
        A/table-images/manifest.json: d398904ed6ab009c72dfe6d623a76d3bfe8a65d3cfcf961ed76feb6c69f76d4d
        A/table-images/TABLE-2-page-10-1.png: c3983f15dfd989f4835e08a85878655b5b89c43d22b66c9fae1c95a9bb6aa990
        A/clauses/window-03/raw.json: 5555e99a6a1cd116865ccdcab248eef6a7810974a2b0ff54a287853d1ddf39f0
        A/clauses/window-03/prompt.txt: f151627d62b35adc5d53cbcb20d4bb27ba80ae0ce87309617d899bdfc83a3752
        A/clauses/window-03/meta.json: b669a5c272186fb25e283f75ca099a4e3636714ad9e0c84f2d5f2526983cd520
        A/clauses/window-04/raw.json: a7a2d8454902eaedbc930e4e6b39aac2bb43daa76148f2a1a140344cf63ce6dd
        A/clauses/window-04/prompt.txt: 7f29b54c25c066e54eaa8ad7f4b9f4ad4bf97c5fc54bf6e5bfe14317d03f5f87
        A/clauses/window-04/meta.json: f6e4417b7bfa72168091cc1439ad01133703eed53653c10a22842876450515d4
        A/clauses/window-05/raw.json: ba624f2cd4c53b7b0836021e5ff82f7694ecd75e890616944604a1606362af49
        A/clauses/window-05/prompt.txt: b06dbebbb6acc8bad9a4c6f9ea270ed15f3e4364f2fe4c0e0fe40eed16f36d81
        A/clauses/window-05/meta.json: 4cddde3ddd6a386c141633e606f92e847c743b6bfd0e76c6a76a6313bbd51726
        A/clauses/window-02/raw.json: 8033908f6d4e01db9f0d81973b8e7b4a6a84c1cf1923f77e5aa8729cdf3bd842
        A/clauses/window-02/prompt.txt: 9c4f2a62f1bf72075c7a49e5ad51f06a189ec00bd8a1d43916462849ef7cc97b
        A/clauses/window-02/meta.json: 876ca664afef1e6562cb716ec49394a3814ddc6c063b4f3dab3679b51de94eb7
        A/clauses/window-09/raw.json: 9fe2e2868974b2fdfa1d5f3b62f674769c3ff86ac405856f9618d864d9024ec8
        A/clauses/window-09/prompt.txt: 4ad0c44c3b39fc0cdbc01794962f4a8a8f3a6dd576e92a63788ad8853b849ba7
        A/clauses/window-09/meta.json: 00745bea8c9b4a19e7fa9fc8b74dce1520cad1e2b594d30cf3fa66fbd1cf60ab
        A/clauses/window-07/raw.json: 44785dd8ee2fffc18eced0926abc86ba273361252d887b8a575d8f8f946d7fd8
        A/clauses/window-07/prompt.txt: f30b52bf5e5b13b570b25b8fd719bbcd39e81de9be782d284a7502393e3ba78a
        A/clauses/window-07/meta.json: 4793dea5219c9a05e29dba9d8a5b47c5fff4a0ceb72431d0abd3e918a93b8d27
        A/clauses/window-01/raw.json: 4cff88c707551defb00ac0dc559250574ece1c83ba6eb98ddf9b36a660404645
        A/clauses/window-01/prompt.txt: 157c4a540fbb6b882573137499c359766ab38bd809b1094acb612925376bcbbe
        A/clauses/window-01/meta.json: 5205d6cecab74463a65f73d663c74addfb6fbe8c70fa423f1f74c18f010e13e2
        A/clauses/window-06/raw.json: f3affada4c52340df4572bb3c9dd56f80e67ac073e89a1e4005cf524ddfeb803
        A/clauses/window-06/prompt.txt: af6679030afca46f3ac1d75eb5725d183c3d96965fee240ca988718c1df13a56
        A/clauses/window-06/meta.json: 60e5eefa1afe46f34ec82d0bb84166c582d68dd1bbdf7158c52252b8b73d6724
        A/clauses/window-08/raw.json: b5fafbcdc1023f1c6b27fdf2c228f51c8e6b6e0be2e99e429581bd0652e1c474
        A/clauses/window-08/prompt.txt: 5c59c84a4df04ca78d649d1ba87ca2b791585773759d042509691c70dca2906d
        A/clauses/window-08/meta.json: 3f7e17e379f2f25a5fa7626687dc87b7fd602b114d99a689a5d1914bbb57c9ff
        A/tables/TABLE-2-page-10-2/raw.json: 102f6c9952a596937f2854950d8bf4a3eb7587c0d2a67b6ade1f1b19d44fbfac
        A/tables/TABLE-2-page-10-2/prompt.txt: 70c16ba02c2712a70054020672f0deecbca63d0c189d603b9a72e3d3e6e47174
        A/tables/TABLE-2-page-10-2/meta.json: 9c7b491c3636955255ca6375ff714c2c322999c994d63ae213dd51272ec03937
        A/tables/TABLE-1-page-4-1/raw.json: e2e5d87b08eba98bd9096063ce9ff912535691b1daaa0958ec8eff4ddd967622
        A/tables/TABLE-1-page-4-1/prompt.txt: 49295ec3c3eafbf59adff23c08d4d6d3b5902eb976ef5900c7daebd2cdfe5887
        A/tables/TABLE-1-page-4-1/meta.json: 799de74499a24566cacf060b82df2622c139578411441d2aa9f1b32f099359b0
        B/passages.json: 9911233de4e837bf81ba7b6fd2d506e7b02d9f201d3f3f9c76fa87f396473b41
        B/raw.json: 706e8fc7502a93720a885a0d504da13bb67bc8df6496e4b1544e63504eba8ab8
        B/source-units.json: 5385076b47c3f953efaf01fff04edda1796fe4f5ff57fdd6cd93054b4cc2fedf
        B/full-source-units.json: 506f27cd9c6b5a72cb96e6d2be95432885ad69a55146ac9fac0ba598476ccffc
        B/meta.json: 6bd35b7e5641e757404604c5b965f526998da922159976b0c4b2247524eeb8ac
        B/table-images/page-10.png: 102d76252b3cec1f61a5d8290d340e4f288bff2e5bc34fce7772d035f3fecf7e
        B/table-images/page-4.png: df53d5d8f28a82be71abaf653d8e05041aa03031a89c67f4ecf3fa39134d4db9
        B/table-images/TABLE-1-page-4-1.png: 1be9e838e72f02cefcf039c55841dc92e6f4cd231dc4463f9886a5afc430195b
        B/table-images/manifest.json: 02b0e79cbfc2f12eb02df548ac49c3020d3c8e8852bcb450010a03c4645edec6
        B/table-images/TABLE-2-page-10-1.png: c3983f15dfd989f4835e08a85878655b5b89c43d22b66c9fae1c95a9bb6aa990
        B/clauses/window-03/raw.json: e56e8d984fcd5b38481701a0eec7e0524271ed53b70a097631a43a3866f54a20
        B/clauses/window-03/prompt.txt: f151627d62b35adc5d53cbcb20d4bb27ba80ae0ce87309617d899bdfc83a3752
        B/clauses/window-03/meta.json: a36b53c9c233a1997ccdee5572175c71ff5d6d62cc64b79a054df262e4c90f0a
        B/clauses/window-04/raw.json: 879b61c2a093904b10225805e466eeeb5f26ac29c3701ac3eb060f2ba45c7706
        B/clauses/window-04/prompt.txt: 7f29b54c25c066e54eaa8ad7f4b9f4ad4bf97c5fc54bf6e5bfe14317d03f5f87
        B/clauses/window-04/meta.json: 3665012c822024e4b77b446b818aa5b114d147369be5d526196b6f2987fddbce
        B/clauses/window-05/raw.json: 2d1ebf125d923000f13874be040198e3d1b1b2426bcd01a6fddfc69a6f9687a8
        B/clauses/window-05/prompt.txt: b06dbebbb6acc8bad9a4c6f9ea270ed15f3e4364f2fe4c0e0fe40eed16f36d81
        B/clauses/window-05/meta.json: 049c36e0469817f0a8c99354cf44b5dbe18b1db73a54d13767c062031489e930
        B/clauses/window-02/raw.json: d3405b8222098d2d8487cb3284519f7c72eee0887cc4448d4c92ac4607412cb3
        B/clauses/window-02/prompt.txt: 9c4f2a62f1bf72075c7a49e5ad51f06a189ec00bd8a1d43916462849ef7cc97b
        B/clauses/window-02/meta.json: 1b9acb206feefdb257957db790a314685178def6e5dea3db50c6fcd064d571db
        B/clauses/window-09/raw.json: 490f9e18f4e8f589f8398f8dc399016fd04d7d6f03012464f7ec0697a29c6d95
        B/clauses/window-09/prompt.txt: 4ad0c44c3b39fc0cdbc01794962f4a8a8f3a6dd576e92a63788ad8853b849ba7
        B/clauses/window-09/meta.json: 7cffe10dd88dc62db9280b4c56f582d9b04b10a7fdd2fb12ea5627648d502309
        B/clauses/window-07/raw.json: c143729dd1aeba61e4e6b54a58f2480203b7747f951494cc1b2374eccf1748d2
        B/clauses/window-07/prompt.txt: f30b52bf5e5b13b570b25b8fd719bbcd39e81de9be782d284a7502393e3ba78a
        B/clauses/window-07/meta.json: 9fe4a2e9185afd2ea930bf96d35273d428f8d1c03a429157cd1dd1417c645005
        B/clauses/window-01/raw.json: 94a7a0266eaf2a44190d60952365a610a2af0511ef1fe01509c9cacc3970b933
        B/clauses/window-01/prompt.txt: 157c4a540fbb6b882573137499c359766ab38bd809b1094acb612925376bcbbe
        B/clauses/window-01/meta.json: 34497c87a478bae3404ca688ef9f71d0b23b6a5e401062c7f5a834924b901aa9
        B/clauses/window-06/raw.json: c8f0e091faf6ba40fcd66961833de58fb93241506e1e6b0d394b72ac932a8f50
        B/clauses/window-06/prompt.txt: af6679030afca46f3ac1d75eb5725d183c3d96965fee240ca988718c1df13a56
        B/clauses/window-06/meta.json: b1a20528cc77b61f82e2b692451ebe9b315f38b7fa6ed374c451ec1e9cbeb644
        B/clauses/window-08/raw.json: 7d1829723e9623eeef6281429c1e8a33a624ded85fc4dcfcf0c06200fc7ea08e
        B/clauses/window-08/prompt.txt: 5c59c84a4df04ca78d649d1ba87ca2b791585773759d042509691c70dca2906d
        B/clauses/window-08/meta.json: 59a63adba23ba32ec4242c2cb2a00c88108c54afa94bdc9e48fab3b70d6e0c9b
        B/tables/TABLE-2-page-10-2/raw.json: be24d4ae4a65774a9c8f3c997a84cb75a3cc506f06ea67f453a028e8cede6678
        B/tables/TABLE-2-page-10-2/prompt.txt: 70c16ba02c2712a70054020672f0deecbca63d0c189d603b9a72e3d3e6e47174
        B/tables/TABLE-2-page-10-2/meta.json: 62d81e5da057a493aae6b056c9ede05736589063ed4b6b121acf47d327eefb54
        B/tables/TABLE-1-page-4-1/raw.json: 8fdf13a51d5b4eaec28602c72f6b1d96f8956238981d6926768822b222c319f2
        B/tables/TABLE-1-page-4-1/prompt.txt: 49295ec3c3eafbf59adff23c08d4d6d3b5902eb976ef5900c7daebd2cdfe5887
        B/tables/TABLE-1-page-4-1/meta.json: d136cce6a1d9d0f9e8cc093ead32652ac072df580de2d24e8c887174b121a5ff
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
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      source_review: _compare/relationships-2026-11-16/review-current/Alyahya2020
      source_status_sha256: 2098be11ece6e6965b0178d3e7e122b0a8799637b7236495c9d3f6311d0ed502
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: discourse genre
    outcome:
      text: quantity of production, lexical diversity, and speech rate
    analysis_label: Content analysis of connected speech across genres
    relation: association
    evidence_ids:
    - P1-S1-C11
    - P5-S1-C2
    qualifier_ids:
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      source_review: _compare/relationships-2026-11-16/review-current/Alyahya2020
      source_status_sha256: 2098be11ece6e6965b0178d3e7e122b0a8799637b7236495c9d3f6311d0ed502
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C3
      - Result passage disposed without unit P1-S2-C4
      - Result passage disposed without unit P1-S2-C6
      - Accounting without a linked unit P2-S2-C11
      - Unaccounted source passage P2-S2-C11
      - Accounting without a linked unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S2-C2
      - Unaccounted source passage P4-S1-C11
      - Result passage disposed without unit P4-S2-C11
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C7
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P5-S1-C5
      - Unaccounted source passage P5-S1-C2
      - Accounting without a linked unit P5-S2-C10
      - Accounting without a linked unit P5-S2-C11
      - Accounting without a linked unit P5-S2-C12
      - Accounting without a linked unit P5-S2-C8
      - Accounting without a linked unit P5-S2-C9
      - Accounting without a linked unit P5-S3-C4
      - Unaccounted source passage P5-S2-C9
      - Unaccounted source passage P5-S3-C4
      - Unaccounted source passage P5-S2-C10
      - Unaccounted source passage P5-S2-C11
      - Unaccounted source passage P5-S2-C8
      - Unaccounted source passage P5-S2-C12
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C8
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P8-S3-C5
      - Result passage disposed without unit P8-S3-C7
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S2-C1
      - Accounting without a linked unit P11-S3-C7
      - Accounting without a linked unit P11-S3-C8
      - Accounting without a linked unit P11-S3-C9
      - Accounting without a linked unit P12-S1-C2
      - Accounting without a linked unit P12-S1-C4
      - Accounting without a linked unit P12-S1-C8
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P11-S3-C9
      - Unaccounted source passage P12-S1-C4
      - Unaccounted source passage P11-S3-C8
      - Unaccounted source passage P11-S3-C7
      - Unaccounted source passage P12-S1-C8
      - Accounting without a linked unit P12-S2-C3
      - Accounting without a linked unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C7
      - Accounting without a linked unit P12-S2-C9
      - Accounting without a linked unit P12-S3-C3
      - Unaccounted source passage P12-S3-C3
      - Unaccounted source passage P12-S2-C9
      - Unaccounted source passage P12-S2-C7
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P12-S2-C3
      - Result passage disposed without unit P12-S3-C8
      - Accounting without a linked unit P12-S4-C2
      - Accounting without a linked unit P12-S4-C3
      - Accounting without a linked unit P13-S1-C2
      - Result passage disposed without unit P13-S1-C3
      - Unaccounted source passage P13-S1-C2
      - Unaccounted source passage P12-S4-C2
      - Unaccounted source passage P12-S4-C3
      - Result passage disposed without unit P13-S1-C8
      unattached_null_or_qualifier_ids:
      - P5-S1-C7
      - P5-S2-C9
      - P5-S2-C10
      - P5-S2-C11
      - P5-S3-C4
      - P8-S1-C10
      - P8-S3-C5
      - P11-S3-C9
      suppressed_nonrepresented_units: 17
      default_disposition_count_requires_completeness_check: 145
      unselected_timing_passages:
      - P3-S1-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-10-2
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-10-2
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
        - P5-S3
        - P6-S1
        - P7-S1
        - P8-S1
        - P8-S3
        - P9-S1
        - P11-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      source_review: _compare/relationships-2026-11-16/review-current/Alyahya2020
      source_status_sha256: 2098be11ece6e6965b0178d3e7e122b0a8799637b7236495c9d3f6311d0ed502
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes differences across discourse genres and groups.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies storytelling narratives as higher in quantity and diversity.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports reduction in quantity, diversity, and informativeness in aphasia
        patients.
    - source_id: P1-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement about the unified model.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Identifies the components extracted in the unified model.
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about lesion-symptom mapping.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of neural correlates.
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on neural correlates alignment.
    - source_id: P2-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of study aim.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: KMO index and Bartlett's test for PCA adequacy.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of collinearity.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of collinearity.
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: ANOVA results for group effects on all measures.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: ANOVA results for main effects of discourse genre.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Post hoc results for quantity of production.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Post hoc results for lexical diversity.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Post hoc results for lexical diversity.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Post hoc results for speech rate.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Post hoc results for speech rate.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Significant Group x Discourse interaction for quantity and diversity.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Interaction driven by storytelling narrative.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Diversity difference between picture and procedural discourse in patients.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Group differences across all three discourses.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Group effects for fluent vs non-fluent on all measures.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Main effects of discourse genre for fluent/non-fluent groups.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Post hoc for quantity in fluent/non-fluent.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Post hoc for diversity in fluent/non-fluent.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Post hoc for diversity in fluent/non-fluent.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Post hoc for speech rate in fluent/non-fluent.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Interaction effects for fluent vs non-fluent.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Interaction driven by storytelling.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Diversity difference in fluent group only.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Group differences across all discourses for fluent/non-fluent.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Sensitivity results with lesion size covariate.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about PCA solution.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Variance explained by PCA solution.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Phonological production component loadings.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Verbal quantity component loadings.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Semantic processing component loadings.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Verbal quality component loadings.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Phonological recognition component loadings.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 12
      reason: Motor speech component loadings.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Executive function component loadings.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 13
      reason: Neural correlates for verbal quantity.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Neural correlates for verbal quantity.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Neural correlates for verbal quality.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Neural correlates for motor speech.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Neural correlates for phonological recognition and semantic processing.
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 17
      reason: Neural correlates for semantic processing.
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 18
      - 19
      reason: Neural correlates for phonological recognition and production.
    - source_id: P8-S3-C3
      disposition: represented
      result_indexes:
      - 23
      reason: Correlation between semantic processing and lesion volume.
    - source_id: P8-S3-C4
      disposition: represented
      result_indexes:
      - 20
      - 21
      reason: VBCM results with lesion volume correction.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 20
      reason: Neural correlates for executive function.
    unresolved_coverage:
    - source_id: P5-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C15
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P2-S2-C11
    - P4-S1-C11
    - P4-S1-C12
    - P4-S2-C2
    - P4-S2-C11
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S3-C5
    - P5-S3-C8
    - P8-S1-C10
    - P8-S1-C11
    - P8-S2-C4
    - P8-S2-C5
    - P8-S3-C1
    - P8-S3-C2
    - P8-S3-C5
    - P8-S3-C7
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C10
    - P11-S1-C11
    - P11-S1-C12
    - P11-S2-C1
    - P11-S2-C2
    - P11-S2-C3
    - P11-S2-C6
    - P11-S2-C7
    - P11-S2-C8
    - P11-S2-C11
    - P11-S3-C2
    - P11-S3-C4
    - P11-S3-C6
    - P11-S3-C7
    - P11-S3-C8
    - P11-S3-C9
    - P12-S1-C2
    - P12-S1-C4
    - P12-S1-C8
    - P12-S2-C2
    - P12-S2-C3
    - P12-S2-C5
    - P12-S2-C7
    - P12-S2-C9
    - P12-S3-C3
    - P12-S3-C8
    - P12-S3-C9
    - P12-S3-C10
    - P12-S4-C2
    - P12-S4-C3
    - P13-S1-C2
    - P13-S1-C3
    - P13-S1-C7
    - P13-S1-C8
    - P13-S1-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-10-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C10
      - P3-S1-C13
      recruited_sample:
      - P1-S1-C10
      - P3-S1-C8
      eligibility:
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C14
      imaging_provenance:
      - P3-S3-C7
      imaging_timing:
      - P3-S3-C7
      outcome_timing:
      - P1-S1-C10
      outcome_definition:
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C13
      - P3-S2-C15
      - P3-S3-C4
      validation:
      - P4-S1-C10
      analysis_restrictions:
      - P4-S2-C6
      dependent_variable_statement:
      - P4-S1-C5
      - P4-S2-C5
      limitations:
      - P12-S3-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C5
      - P4-S2-C6
      - P5-S2-C14
      - P8-S3-C4
      - P9-S1-C4
      - P10-S2-C2
      - P12-S3-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections: []
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
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      review_sha256: 2568f8e8fd3fcb3e46c5c0ec673c4dd1ad443886b7107e9ca56082c087a0b526
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
      - P1-S1-C11
      - P5-S1-C2
      source_result: Content analyses of connected speech samples from patients with
        chronic post-stroke aphasia and neurotypical adults revealed significant main
        effects of discourse genre on quantity of production, lexical diversity, and
        speech rate. Specifically, storytelling narratives elicited significantly
        higher quantities of content words and lexical diversity compared to composite
        picture description and procedural discourse. Conversely, speech rate was
        fastest during procedural discourse, followed by picture description, and
        then storytelling. These differences were observed across the sample, with
        specific post-hoc comparisons confirming the ranking of genres for each measure.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the content analysis of connected
            speech across genres (P1-S1-C11, P5-S1-C2). The proposed core correctly
            identifies the exposure (discourse genre) and the outcome (quantity, lexical
            diversity, speech rate) as measured by content analysis, distinct from
            the subsequent PCA or lesion-symptom mapping analyses.
          source_ids:
          - P1-S1-C11
          - P5-S1-C2
          - P4-S1-C4
        direction:
          answer: fits
          reason: The proposed core accurately reflects the direction of the effects
            reported in the source. P5-S1-C3 and P5-S1-C4 confirm that storytelling
            narrative was significantly higher for quantity and lexical diversity.
            P5-S1-C6 and P5-S1-C7 confirm that procedural discourse had the fastest
            speech rate, followed by picture description, then storytelling. The core's
            claim that storytelling provided higher quantity/diversity is faithful
            to the source.
          source_ids:
          - P5-S1-C3
          - P5-S1-C4
          - P5-S1-C6
          - P5-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as discourse genre (descriptive,
            narrative, procedural). The outcome is correctly identified as connected
            speech performance metrics (quantity, lexical diversity, speech rate).
            The measurement method is correctly identified as content analysis of
            connected speech samples, which is a non-imaging behavioral measure. The
            source explicitly distinguishes this from the neural correlates analysis
            (VLSM) which uses imaging data.
          source_ids:
          - P3-S2-C4
          - P3-S2-C9
          - P3-S3-C4
          - P5-S1-C2
        qualifications:
          answer: fits
          reason: The qualifications in the proposed core accurately reflect the specific
            post-hoc findings detailed in P5-S1-C3 through P5-S1-C7. The core correctly
            notes the ranking of genres for each measure (storytelling > others for
            quantity/diversity; procedural > others for rate). The limitation regarding
            the exclusion of personal discourse is also correctly captured from P3-S1-C2.
          source_ids:
          - P5-S1-C3
          - P5-S1-C4
          - P5-S1-C5
          - P5-S1-C6
          - P5-S1-C7
          - P3-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The core does not omit material caveats that would change the interpretation
            of the behavioral association. The source notes that these analyses were
            repeated with lesion size as a covariate and the effects remained (P5-S3-C4),
            which supports the robustness of the finding but does not change the primary
            result. The core correctly focuses on the behavioral association itself.
            No significant caveats regarding the validity of the content analysis
            or the specific genre comparisons are missing.
          source_ids:
          - P5-S3-C4
          - P5-S1-C2
      optional_pending:
      - Sample size (n=46 patients, n=20 controls) is mentioned in source P1-S1-C10
        and P3-S1-C8 but not explicitly transcribed in the proposed core's sample_n
        field; however, the population is correctly identified.
      - Timing (chronic stage, mean 69.43 months post-stroke) is mentioned in source
        P3-S1-C8 and P4-S2-C11 but marked as not transcribed in the proposed core;
        this is a pending detail rather than a material conflict for the qualitative
        relationship.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=46 patients, n=20 controls) is mentioned in source P1-S1-C10
      and P3-S1-C8 but not explicitly transcribed in the proposed core's sample_n
      field; however, the population is correctly identified.
    - Timing (chronic stage, mean 69.43 months post-stroke) is mentioned in source
      P3-S1-C8 and P4-S2-C11 but marked as not transcribed in the proposed core; this
      is a pending detail rather than a material conflict for the qualitative relationship.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    - field: sample.n
      original: 46
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: chronic stage (4-12 months post-stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 12, 4'
    analysis_identity:
      id: R001
      exposure:
        text: discourse genre
      outcome:
        text: quantity of production, lexical diversity, and speech rate
      analysis_label: Content analysis of connected speech across genres
      relation: association
      evidence_ids:
      - P1-S1-C11
      - P5-S1-C2
      qualifier_ids:
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
        source_review: _compare/relationships-2026-11-16/review-current/Alyahya2020
        source_status_sha256: 2098be11ece6e6965b0178d3e7e122b0a8799637b7236495c9d3f6311d0ed502
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 473603444f7b2b0597fba08eb149c99184b7e72b042c285c23737df2fe6f7738
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C8
          page: 3
          text_layer_sha256: 473603444f7b2b0597fba08eb149c99184b7e72b042c285c23737df2fe6f7738
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Materials and methods

          Participants

          Forty-six patients who had developed aphasia following a single

          left haemorrhagic or ischaemic stroke were tested in the chronic

          stage (412 months post-stroke).'
        anchor_text: 'Materials and methods

          Participants

          Forty-six patients who had developed aphasia following a single

          left haemorrhagic or ischaemic stroke were tested in the chronic

          stage (412 months post-stroke).'
        excluded_fragments: []
        image_sha256: ad390ddee6751e102fbe27b3906d4289848db515bc37159cb45f8c06714114d8
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Content analyses conducted on all connected speech samples indicated

    that performance differed across discourse genres and between groups.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
