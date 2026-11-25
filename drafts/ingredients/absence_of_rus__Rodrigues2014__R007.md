---
id: absence_of_rus
name: absence of RUs
kind: ingredient
findings:
- id: f1
  target: language_recovery
  target_kind: prognosis
  claim: patients without recurrent utterances showed significant improvement between
    baseline and follow-up assessments in aphasia quotient (AQ), naming performance,
    repetition, BAAL comprehension task, and Token test scores
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: patients with aphasia resulting from a single left stroke
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
  - retrospective study of clinical records
  - sample primarily composed of inpatients, potentially limiting the number of mild
    aphasia cases
  - no follow-up performed after discharge from the rehabilitation unit
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: absence of recurrent utterances, defined as the production
    of the same utterance against the patient''s presumed intention in all communicative
    contexts. control group was matched for age, gender, time since onset, handedness,
    hours of therapy, and aphasia classification. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P4-S2-C7, two-model agreement, human verification pending): . The aphasic syndrome,
    based on this assessment, was estab-

    lished not earlier than 1-month post-stroke onset Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-25'
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
    - proposed_concept:language_recovery
  citation: '@Rodrigues2014'
  source_passages:
  - section: Original source P8-S1-C14
    page: 8
    quote: 'Considering the control group, we observed a significant difference in
      all

      language tasks between baseline and follow-up assessments, i.e., in AQ (U =
      98.0;

      p = .000), naming performance (U = 102.0; p = .002), repetition (U = 51.0; p
      = .001),

      BAAL comprehension task (U = 94.0; p = .000) and Token test scores (U = 106.0;

      p = .001).'
    supports: claim
  - section: Original source P4-S1-C12
    page: 4
    quote: 'The criteria for verbal stereotypy classification were the production
      of

      the same utterance against the patient’s presumed intention in all communicative

      contexts.'
    supports: method
  - section: Original source P4-S2-C7
    page: 4
    quote: 'The aphasic syndrome, based on this assessment, was estab-

      lished not earlier than 1-month post-stroke onset.'
    supports: method
  - section: Original source P5-S1-C12
    page: 5
    quote: 'Time post-stroke onset was similar in all patients (M = 3.15 months; range
      2–

      5 months), and all language revaluations were made 3 months after the initial

      evaluation.'
    supports: method
  - section: Original source P4-S1-C5
    page: 4
    quote: 'Inclusion criteria were as follows: aphasia resulting from a single left
      stroke,

      absence of psychiatric or other neurological diseases previous to stroke, living
      at

      home before stroke and right-handedness.'
    supports: sample
  - section: Original source P5-S1-C2
    page: 5
    quote: 'Each control was matched with a corresponding experimental

      subject for the variables of age, gender, time since onset, handedness, hours
      of

      therapy and aphasia classification.'
    supports: confounders
  - section: Original source P11-S1-C6
    page: 11
    quote: 'Some limitations of the current study included a relatively small number
      of milder

      forms of aphasia because the most severe cases are more in need of hospitalisation.'
    supports: limitation
  - section: Original source P11-S1-C8
    page: 11
    quote: 'The results

      were obtained from inpatients with sub-acute aphasia during the treatment phase,
      and

      no follow-up was performed after discharge.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Rodrigues2014
  proposal_id: R007
  review_status_sha256: a2b6fad3168d5f59efa7ff4fcadc80fe7097d6818389962118fb994835f0f5fa
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
        A/passages.json: e166452b07863dd6788e89a96f2f2c19df2eb126acec72ef434fa1c0759ff89b
        A/raw.json: 53174ff27a26cc1fc8fad97f6907b4b76f208ea417aed94e487a6a713348cb18
        A/source-units.json: a181a41e8bbeff920c911dff22f26ce522231f229b196c6d651530341f2b6145
        A/full-source-units.json: e02dbc2d6f951c49debda54454ab350b38f982e104feba2a6fc6b7b552ba4577
        A/meta.json: 0a991f15c2ab13290c2d575ccd54987d705b8a76576fcb1ae012a2d01fdeecee
        A/table-images/page-6.png: 64df5f5ce7f0ba923462eea15e6aec68de210960fed39a286b31497e91884236
        A/table-images/page-7.png: d22a5454078710a4120f12da343bce97e1ae90a13ee4efd56c04f45b52ac9623
        A/table-images/TABLE-1-page-6-2.png: 6616288309818d006706ea36da5b1483561c0d63eafac97729f106552dd4010f
        A/table-images/TABLE-2-page-6-1.png: 6616288309818d006706ea36da5b1483561c0d63eafac97729f106552dd4010f
        A/table-images/manifest.json: 4cd891b353af52b478a77af8e653dee4c67c3b7c344c4bea276e3d67e8fb554b
        A/table-images/TABLE-4-page-7-2.png: ddaaea9bff74f2f05b8d45cce5942830554b8256d77083dff63eb787b9fabe4c
        A/table-images/TABLE-3-page-7-1.png: ddaaea9bff74f2f05b8d45cce5942830554b8256d77083dff63eb787b9fabe4c
        A/clauses/window-03/raw.json: a8b18679baae747d0b1741be079a4ac965bef9baeb382bdeaa242c2d74467a30
        A/clauses/window-03/prompt.txt: 17d5fd69e97de0a57085d763c71ecea72cb2e76c6d5787b7bc3f80192c3a3ad2
        A/clauses/window-03/meta.json: f7e63937e2df6efa379c3b9866a65dd29dddc1cab4cda7d300e8e3f392daa971
        A/clauses/window-04/raw.json: 1d43fc5ea8eac74e659312a0cc27ccd693772457082822935c21d237aeb06b59
        A/clauses/window-04/prompt.txt: f20b3db07162ebed142bec8699e2cbb0eb8c0f1d633717ec0701d22f72dccab3
        A/clauses/window-04/meta.json: 1622b1af132a21c9fa214ba9970deb0a96854b6e7939f1b88707254bcdec844e
        A/clauses/window-05/raw.json: 7e0c568692dd058cc78c88d674859a55cc3b18d34e05c40d3d404824bbcb3dd3
        A/clauses/window-05/prompt.txt: d4816e74103a89bda60deb985de20c69c7be69d2336db7a2b902b985439dd93f
        A/clauses/window-05/meta.json: c4acb4cc0ec5d45089e1dba4524f071d6047f75f5b28cc789d898f89aa474a5c
        A/clauses/window-02/raw.json: bf9bbcfdefa69344737120791d17bda94b4bf7f5b8dbebc18ebc8b4fc9d5e1d4
        A/clauses/window-02/prompt.txt: c1ae14fbc86c7ddf8049b4a9c7b2334984b4f2a3e9e8692da23eabdbd84156b1
        A/clauses/window-02/meta.json: f18cfd4d6a58d902cf442c16bda0614b276bbcde5ad4b3c90b478ad0603e1bc4
        A/clauses/window-07/raw.json: ff6a2d07960a7f93dadcbd93303b6c2ec428354ae5dec1fccb89cf97d08a3afe
        A/clauses/window-07/prompt.txt: bc83cb69e28261cff42d8823375c9bd4d692a599730e1fb50fc9ff0db205e6c5
        A/clauses/window-07/meta.json: 7fc6566e1e8139e0c5c82296083fbb4331c90e4b3cb53c6cca0ccb723677f531
        A/clauses/window-01/raw.json: 1685f0d4f709db878b19f30711bd2c73095c48101daf9a7ed45dd186c8209542
        A/clauses/window-01/prompt.txt: 92a6126f67ba17ed5f494979f4aa4d59f9ca35709902a965608426d41f3a9851
        A/clauses/window-01/meta.json: 39ed8a587fbd58fafd66e1604a8ae91e21cc43e56a4b8308c03463396527e0e3
        A/clauses/window-06/raw.json: 414da91fae9908b3e128c348ecdbd21feebe4c60eb1f1b6534c10dea44ccc4b3
        A/clauses/window-06/prompt.txt: c8a0f00e0e63d085e6760f370a113635d1fa370ec8506f031682f17966f53c0f
        A/clauses/window-06/meta.json: e8f5b7e30adf5698132373663243f49d4518f2359855d42277fbc045c011b7ae
        A/tables/TABLE-3-page-7-3/raw.json: 1f66491252e289d2df0fd8f4063d8de06d845df59ea36158b01127f6689d8313
        A/tables/TABLE-3-page-7-3/prompt.txt: be52ec1283453a1512dd59da48a9c8d453dd1777f73bb1ba2ff475cd6c9d9f71
        A/tables/TABLE-3-page-7-3/meta.json: 52332af627c57ac42a5a3e5b52649d907cfddb6dbdb200bd8382c82ad71fa9b7
        A/tables/TABLE-4-page-7-4/raw.json: 578fb4601a76bfe3a0304a569f99d17ee73e2e5e823c30ace7422da2f94eb6ff
        A/tables/TABLE-4-page-7-4/prompt.txt: 8f70cd106e0fe389c4c766cbf87aea61fd75c1b6f47d1baf5351261fa186a5dd
        A/tables/TABLE-4-page-7-4/meta.json: 742e14a28b25e7ec18e5d1256c3a811f49dc79a29747248fef8f34bdc80cc88d
        A/tables/TABLE-1-page-6-2/raw.json: a1080dd745401c9e4903ce906158d033f0a770eff378bec71b2fb4865bf2468d
        A/tables/TABLE-1-page-6-2/prompt.txt: 7198ddbbfbce9cf0ebf897dee1e81a559381deaaad49db7557b42c0375c399ad
        A/tables/TABLE-1-page-6-2/meta.json: 150e2a5b600f0dd0c79ec851ef46b40c9c5dfa4ab2b433041c381891f2f0adfc
        A/tables/TABLE-2-page-6-1/raw.json: 51bc86bf1534bc4e1daafb21e4ecf580ec47714b98a57f70bcf9dff63c726a17
        A/tables/TABLE-2-page-6-1/prompt.txt: eed84a048f47102b3f5f4c5efb0fba024f134e5b51ca3d68455bf69da44648a4
        A/tables/TABLE-2-page-6-1/meta.json: c75575e230f46e48a12d51ac7bf05e0f7b3e614581ad5244929ffb06edcda153
        B/passages.json: e166452b07863dd6788e89a96f2f2c19df2eb126acec72ef434fa1c0759ff89b
        B/raw.json: ce74720cb55a2a674aeda5eff5320e46f3ff1dd1ec9746782580f02889645d98
        B/source-units.json: a181a41e8bbeff920c911dff22f26ce522231f229b196c6d651530341f2b6145
        B/full-source-units.json: e02dbc2d6f951c49debda54454ab350b38f982e104feba2a6fc6b7b552ba4577
        B/meta.json: cdc217b8b4482e8d1b91fade9deea61ac0f53123ff8b2930d9f20cb2a0bdca4b
        B/table-images/page-6.png: 64df5f5ce7f0ba923462eea15e6aec68de210960fed39a286b31497e91884236
        B/table-images/page-7.png: d22a5454078710a4120f12da343bce97e1ae90a13ee4efd56c04f45b52ac9623
        B/table-images/TABLE-1-page-6-2.png: 6616288309818d006706ea36da5b1483561c0d63eafac97729f106552dd4010f
        B/table-images/TABLE-2-page-6-1.png: 6616288309818d006706ea36da5b1483561c0d63eafac97729f106552dd4010f
        B/table-images/manifest.json: 2fbeb0f005fe128c875ead5f284ae96676e654bec3e487d109f99730d37be7de
        B/table-images/TABLE-4-page-7-2.png: ddaaea9bff74f2f05b8d45cce5942830554b8256d77083dff63eb787b9fabe4c
        B/table-images/TABLE-3-page-7-1.png: ddaaea9bff74f2f05b8d45cce5942830554b8256d77083dff63eb787b9fabe4c
        B/clauses/window-03/raw.json: 269b4dcf7c770a1fe49da3f42970759a318605e757523fa5a0960760389b444d
        B/clauses/window-03/prompt.txt: 17d5fd69e97de0a57085d763c71ecea72cb2e76c6d5787b7bc3f80192c3a3ad2
        B/clauses/window-03/meta.json: 56a747754f2687d351f2f448ce497e1891fc511ab52b7f44496dfe08cb0e5bfd
        B/clauses/window-04/raw.json: b2838b42174b98a539108c9a26b813a49b9f6d4ec904e0a83b2cc5e2a15df1ca
        B/clauses/window-04/prompt.txt: f20b3db07162ebed142bec8699e2cbb0eb8c0f1d633717ec0701d22f72dccab3
        B/clauses/window-04/meta.json: 1e2e1b565ba74ac8e9a6dea9f11ad6ceb5e54267f049fd24e388d918c6deabf2
        B/clauses/window-05/raw.json: 7ca210cb3f295f09c2b2d7dd57d30338e7af8999bcc719ae2da40a8087dd0ea0
        B/clauses/window-05/prompt.txt: d4816e74103a89bda60deb985de20c69c7be69d2336db7a2b902b985439dd93f
        B/clauses/window-05/meta.json: f15d0ceffbd01ab8977059a2e40a1f89cc45032835e6ad1173a7c794571aac81
        B/clauses/window-02/raw.json: cc01ce14d4554416014b864737fe94bd6c904746617c3485fef39665bbcaceac
        B/clauses/window-02/prompt.txt: c1ae14fbc86c7ddf8049b4a9c7b2334984b4f2a3e9e8692da23eabdbd84156b1
        B/clauses/window-02/meta.json: 51b35d6dbfa6d5432b7974c33e339130cfdfdc562723339f94d3a44d325619ab
        B/clauses/window-07/raw.json: 30bed4766ce06fdbde83cd39b8b61a889aa0793112b861984ea97f0841699010
        B/clauses/window-07/prompt.txt: bc83cb69e28261cff42d8823375c9bd4d692a599730e1fb50fc9ff0db205e6c5
        B/clauses/window-07/meta.json: e848261e687911435956115464c18cee7098b29ab793224ff6cb538b24f592b8
        B/clauses/window-01/raw.json: bda122bced96a884593d73f80ff3ad3bf42829cb1e66bf359c6d951bfc9cb28c
        B/clauses/window-01/prompt.txt: 92a6126f67ba17ed5f494979f4aa4d59f9ca35709902a965608426d41f3a9851
        B/clauses/window-01/meta.json: 0695c673c6802aefe54df74fae38846127e0fe523fd428402d868dbb7341e949
        B/clauses/window-06/raw.json: cd1901675187baf17fd6a32f39aaf4c3d2fc75e6e29bbfd6f045556e53591343
        B/clauses/window-06/prompt.txt: c8a0f00e0e63d085e6760f370a113635d1fa370ec8506f031682f17966f53c0f
        B/clauses/window-06/meta.json: 9feeba66ff4dd54c7cca693325009269dcf558b385f734401494dfe7e4eca60c
        B/tables/TABLE-3-page-7-3/raw.json: 50b3a925ab4b35e3baad257d14882b9072115f43ea30841ccda80355c5b1f0cf
        B/tables/TABLE-3-page-7-3/prompt.txt: be52ec1283453a1512dd59da48a9c8d453dd1777f73bb1ba2ff475cd6c9d9f71
        B/tables/TABLE-3-page-7-3/meta.json: 7a70a7c3a1a0df1915f68368c644996024305ff7d2e0927109c331c7d012af9e
        B/tables/TABLE-4-page-7-4/raw.json: a05b43f79af93b6f00e6df6fda35c905bd61f7eb5c4fadbdcc4aff018226041c
        B/tables/TABLE-4-page-7-4/prompt.txt: 8f70cd106e0fe389c4c766cbf87aea61fd75c1b6f47d1baf5351261fa186a5dd
        B/tables/TABLE-4-page-7-4/meta.json: afb895788dae06f31d70a41a4387ad62878f4c2f6095cd1cd46ebd6e1c1e5df8
        B/tables/TABLE-1-page-6-2/raw.json: 0dc814e0c3a54d8c8864d55a512a241afc35ae36872fbdc8cdc718591c56d464
        B/tables/TABLE-1-page-6-2/prompt.txt: 7198ddbbfbce9cf0ebf897dee1e81a559381deaaad49db7557b42c0375c399ad
        B/tables/TABLE-1-page-6-2/meta.json: f2a1f6077b31c2fafea0acf0a38d2d36bfcf9e5437b93cf5371eafca6fee79ea
        B/tables/TABLE-2-page-6-1/raw.json: 51bc86bf1534bc4e1daafb21e4ecf580ec47714b98a57f70bcf9dff63c726a17
        B/tables/TABLE-2-page-6-1/prompt.txt: eed84a048f47102b3f5f4c5efb0fba024f134e5b51ca3d68455bf69da44648a4
        B/tables/TABLE-2-page-6-1/meta.json: fb2bd7239da280f4a3cacf2728bdbbc0055bc2fb642eb8792378de306ee5d0fa
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
      pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
      source_review: _compare/relationships-2026-11-16/review-current/Rodrigues2014
      source_status_sha256: b42203447ab89fa6eca0bef8731e60b07c50f4ad5cc22583913bcbb74a064b2c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: absence of RUs
    outcome:
      text: AQ, naming performance, repetition, BAAL comprehension task, and Token
        test scores
    analysis_label: Within-group recovery (Control group)
    relation: association
    evidence_ids:
    - P8-S1-C14
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
      pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
      source_review: _compare/relationships-2026-11-16/review-current/Rodrigues2014
      source_status_sha256: b42203447ab89fa6eca0bef8731e60b07c50f4ad5cc22583913bcbb74a064b2c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - 'window 1: invalid/duplicate disposition P1-S1-C4'
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P5-S1-C17
      - Result passage disposed without unit P5-S1-C19
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S1-C9
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P9-S2-C11
      - Result passage disposed without unit P9-S2-C12
      - Result passage disposed without unit P9-S2-C8
      - Result passage disposed without unit P9-S2-C9
      - Result passage disposed without unit P11-S1-C14
      - Result passage disposed without unit P11-S2-C3
      - Accounting without a linked unit P11-S2-C5
      - Unaccounted source passage P11-S2-C5
      unattached_null_or_qualifier_ids:
      - P1-S1-C10
      - P9-S2-C8
      - P11-S2-C5
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 129
      unselected_timing_passages:
      - P4-S2-C7
      - P5-S1-C13
      - P11-S1-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-2
      - TABLE-2-page-6-1
      - TABLE-3-page-7-3
      - TABLE-4-page-7-4
      unlinked_tables:
      - TABLE-1-page-6-2
      - TABLE-2-page-6-1
      - TABLE-3-page-7-3
      - TABLE-4-page-7-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
      source_review: _compare/relationships-2026-11-16/review-current/Rodrigues2014
      source_status_sha256: b42203447ab89fa6eca0bef8731e60b07c50f4ad5cc22583913bcbb74a064b2c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports prevalence of RUs in the total sample.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports prevalence of RUs in global aphasia.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about modulation of RUs.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about language impairment.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant differences in AQ, naming, and repetition.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Reports null differences in comprehension and Token test.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Repeats prevalence of RUs in total sample.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Repeats prevalence of RUs in global aphasia.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (age).
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (aphasia type distribution).
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (aetiology).
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (aetiology).
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical characteristic (apraxia).
    - source_id: P5-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical observation of agraphia.
    - source_id: P5-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical observation of writing.
    - source_id: P5-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical observation of reading.
    - source_id: P5-S1-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about modulation of RUs.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Examples of communicative intent.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of real word RUs.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of real word RUs.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on patients with multiple RUs.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on lack of demographic differences.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant differences in AQ, naming, and repetition.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Reports null differences in comprehension and Token test.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on score improvement.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on syndromatic classification change.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on fluency improvement.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on specific patient improvement.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence statement (restatement).
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on relapse into RU.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on replacement of stereotypy.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of new stereotypy.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of new stereotypy.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of new stereotypy.
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on language improvement.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Reports non-significant improvement in AQ, naming, and repetition.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Reports significant improvement in comprehension and Token test.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 6
      reason: Reports significant improvement across all tasks for control group.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 7
      reason: Reports follow-up differences in AQ, naming, and repetition.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Reports null differences in follow-up comprehension and Token test.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with prior literature prevalence.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (aphasia type distribution).
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample characteristics.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of language processing levels.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of preserved abilities.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of oral language formulation.
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of modulation of RUs.
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of RU use in discourse.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of communicative competence.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of RUs.
    - source_id: P9-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of RUs.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of RU context.
    - source_id: P9-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of RU context.
    - source_id: P9-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Distinction from echolalia.
    - source_id: P9-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on context of real word RUs.
    - source_id: P9-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on range of utterances.
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of shared RU.
    - source_id: P9-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of intonation patterns.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of social impact.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on social impact.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on verbal production improvement.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on therapy effect.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on replacement of stereotypy.
    - source_id: P10-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on comprehension score increase.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on lack of neuropsychology assessments.
    - source_id: P10-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on patients who improved from RU.
    - source_id: P11-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restatement on language abilities.
    - source_id: P11-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restatement on language faculties.
    - source_id: P11-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on recovery patterns.
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on unclear output prognosis.
    unresolved_coverage:
    - source_id: P9-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C10
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C10
    - P5-S1-C11
    - P5-S1-C15
    - P5-S1-C16
    - P5-S1-C17
    - P5-S1-C19
    - P5-S2-C2
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C6
    - P6-S1-C2
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C8
    - P8-S1-C9
    - P8-S1-C10
    - P8-S1-C11
    - P8-S2-C6
    - P9-S1-C1
    - P9-S1-C3
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C7
    - P9-S1-C9
    - P9-S1-C10
    - P9-S1-C11
    - P9-S1-C13
    - P9-S2-C3
    - P9-S2-C5
    - P9-S2-C6
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    - P9-S2-C10
    - P9-S2-C11
    - P9-S2-C12
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C11
    - P10-S1-C12
    - P10-S2-C4
    - P10-S2-C8
    - P11-S1-C14
    - P11-S2-C3
    - P11-S2-C5
    - P11-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-2
    - TABLE-2-page-6-1
    - TABLE-3-page-7-3
    - TABLE-4-page-7-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S1-C5
      - P6-S1-C4
      - P7-S1-C7
      - P8-S1-C15
      - P8-S2-C2
      recruited_sample:
      - P4-S1-C10
      eligibility:
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P5-S1-C12
      - P7-S1-C3
      - P8-S1-C13
      outcome_definition:
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C8
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations:
      - P11-S1-C6
      - P11-S1-C7
      - P11-S1-C8
      - P11-S1-C9
      - P11-S1-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C11
      - P5-S1-C13
      - P6-S1-C3
      - P7-S1-C6
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C2
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
      pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
      review_sha256: a2b6fad3168d5f59efa7ff4fcadc80fe7097d6818389962118fb994835f0f5fa
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
      - P8-S1-C14
      source_result: 'In the control group (patients without recurrent utterances),
        significant improvements were observed between baseline and follow-up assessments
        for all measured language tasks: Aphasia Quotient (AQ), naming performance,
        repetition, BAAL comprehension task, and Token test scores.'
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R007) correctly identifies the within-group
            recovery analysis for the control group (absence of RUs) as described
            in P8-S1-C14. The source explicitly states that for the control group,
            significant differences were found in all language tasks between baseline
            and follow-up.
          source_ids:
          - P8-S1-C14
          - P8-S1-C11
        direction:
          answer: fits
          reason: The claim that patients without RUs showed significant improvement
            aligns with the source finding of significant positive changes (improvement)
            in scores between assessments. The direction of 'improvement' is consistent
            with the context of recovery studies where higher scores indicate better
            performance.
          source_ids:
          - P8-S1-C14
          - P8-S1-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as the absence of RUs (control
            group). The outcomes (AQ, naming, repetition, BAAL comprehension, Token
            test) match the specific tasks listed in P8-S1-C14. The measurement is
            behavioral (non-imaging), consistent with the use of BAAL and Token tests.
          source_ids:
          - P8-S1-C14
          - P4-S2-C4
          - P4-S2-C8
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the control group was
            matched for demographics and clinical characteristics, which is supported
            by P5-S1-C2 and P6-S1-C1. This is a material qualifier for the validity
            of the comparison, though the specific result in P8-S1-C14 is a within-group
            change, the group definition relies on this matching.
          source_ids:
          - P5-S1-C2
          - P6-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding the retrospective nature,
            inpatient status, and lack of post-discharge follow-up. These are material
            caveats present in the source (P11-S1-C6, P11-S1-C8). No material caveat
            changing the interpretation of the control group's improvement is omitted.
          source_ids:
          - P11-S1-C6
          - P11-S1-C8
      optional_pending:
      - 'sample.time_post_onset: Source P5-S1-C12 indicates M=3.15 months, but image
        transcription disagreement noted; confirm exact timing window from PDF.'
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
    - 'sample.time_post_onset: Source P5-S1-C12 indicates M=3.15 months, but image
      transcription disagreement noted; confirm exact timing window from PDF.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    - field: sample.time_post_onset
      original: initial assessment not earlier than 1-month post-stroke onset, with
        follow-up 3 months later
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 3'
    analysis_identity:
      id: R007
      exposure:
        text: absence of RUs
      outcome:
        text: AQ, naming performance, repetition, BAAL comprehension task, and Token
          test scores
      analysis_label: Within-group recovery (Control group)
      relation: association
      evidence_ids:
      - P8-S1-C14
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
        pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
        source_review: _compare/relationships-2026-11-16/review-current/Rodrigues2014
        source_status_sha256: b42203447ab89fa6eca0bef8731e60b07c50f4ad5cc22583913bcbb74a064b2c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b3db8d3f306a56db42a3246283f64601c836b9531d7c87442f26104156e490db
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C7
          page: 4
          text_layer_sha256: b3db8d3f306a56db42a3246283f64601c836b9531d7c87442f26104156e490db
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The aphasic syndrome, based on this assessment, was estab-

          lished not earlier than 1-month post-stroke onset.'
        anchor_text: 'The aphasic syndrome, based on this assessment, was estab-

          lished not earlier than 1-month post-stroke onset.'
        excluded_fragments: []
        image_sha256: b883d9b36395c2f4e639e8fa2816baf54af32daa5446a16048e23f0bdd259220
        transcription: '. The aphasic syndrome, based on this assessment, was estab-

          lished not earlier than 1-month post-stroke onset'
      P5-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c6063f2e58ba7fa8ed57efa2ff1cf248f871898882bf8900e682d9226c297c6b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5f30539467b63c4fe21cb92d85cf1f60c548202719d2a3789fd01ea0423d8485
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C12
          page: 5
          text_layer_sha256: 5f30539467b63c4fe21cb92d85cf1f60c548202719d2a3789fd01ea0423d8485
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Time post-stroke onset was similar in all patients (M = 3.15
          months; range 2–

          5 months), and all language revaluations were made 3 months after the initial

          evaluation.'
        anchor_text: 'Time post-stroke onset was similar in all patients (M = 3.15
          months; range 2–

          5 months), and all language revaluations were made 3 months after the initial

          evaluation.'
        excluded_fragments: []
        image_sha256: 0456ae6f83187fdaa6fe8a17e3fb3e4a217cfe4a20bfd31a4692fe93bf64447f
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'Considering the control group, we observed a significant difference in all

    language tasks between baseline and follow-up assessments, i.e., in AQ (U = 98.0;

    p = .000), naming performance (U = 102.0; p = .002), repetition (U = 51.0; p =
    .001),

    BAAL comprehension task (U = 94.0; p = .000) and Token test scores (U = 106.0;

    p = .001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
