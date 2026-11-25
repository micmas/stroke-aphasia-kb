---
id: lesion_volume
name: lesion volume
kind: classical
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: ambiguous_or_composite
    original_target: language_measures
    reason: A score, generic outcome or composite label does not uniquely identify a behaviour. Check the
      task, subtests and analysis before retargeting.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_measures
  target_kind: impairment
  claim: Lesion volume was significantly associated with all measured language functions,
    including overall aphasia severity (WAB-AQ), fluency, spontaneous speech, naming,
    speech repetition, and auditory comprehension.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 116
    population: individuals with chronic left-hemisphere ischemic or hemorrhagic stroke
    phase: not_reported
    time_post_onset: mean time poststroke was 39.4 months
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - prediction models were not validated in an independent sample
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The number of lesioned voxels within the lesion map,
    demarcated on T2-weighted images by a licensed neurologist. analysis used univariate
    linear regression. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P3-S3-C12, two-model agreement, human
    verification pending): After removing subjects

    with missing data points (primarily neuroimaging data, for example,

    some participants did not have CBF data), a total of 116 participants

    were included for data analysis Original text-layer quotation is preserved below.
    PDF image reading (P3-S4-C2, two-model agreement, human verification pending):
    . The mean lesion volume across participants was 122.61 cm³

    (range: 2.09–472.38 cm³; Figure 1 presents the lesion distribution

    across participants) and mean time poststroke was 39.4 months

    (range: 5.6–237.1 months) Original text-layer quotation is preserved below.'
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
    - proposed_concept:language_measures
  citation: '@Kristinsson2021'
  source_passages:
  - section: Original source P10-S1-C4
    page: 10
    quote: 'The only signifi-

      cant association was found between lesion volume and all language

      measures (all p-values <.001).'
    supports: claim
  - section: Original source P3-S3-C12
    page: 3
    quote: 'After removing subjects

      with missing data points (primarily neuroimaging data, for example,

      some participants did not have CBF data), a total of 116 participants

      were

      included

      for

      data

      analysis.'
    supports: sample
  - section: Original source P3-S3-C9
    page: 3
    quote: 'We

      included subjects with aphasia resulting from a single ischemic or

      hemorrhagic stroke to the left hemisphere.'
    supports: sample
  - section: Original source P3-S4-C2
    page: 3
    quote: 'The mean lesion volume across participants was 122.61 cm3

      (range: 2.09–472.38 cm3; Figure 1 presents the lesion distribution

      across participants) and mean time poststroke was 39.4 months

      (range: 5.6–237.1 months).'
    supports: sample
  - section: Original source P7-S3-C7
    page: 7
    quote: 'Based

      on

      prior

      findings

      suggesting

      that

      age

      (Ellis

      &

      Urban, 2016; Kertesz & McCabe, 1977; Pedersen, Jorgensen,

      Nakayama,

      Raaschou,

      &

      Olsen,

      1995;

      Plowman,

      Hentz,

      &

      Ellis, 2012), time poststroke (Hope et al., 2017; Hope, Seghier,

      Leff, & Price, 2013; Ramsey et al., 2017), and overall lesion volume

      (Hope et al., 2013; Plowman et al., 2012) may affect language mea-

      sures, we examined the relationship between these variables and

      language scores (WAB-AQ, Fluency, Spontaneous Speech, Naming,

      Speech Repetition, and Auditory Comprehension; Table 4) using a

      univariate linear regression analysis.'
    supports: method
  - section: Original source P6-S1-C8
    page: 6
    quote: 'The resulting four matrices (one for each modality) of

      the dimensions 116 (subjects) × 150 (brain regions) were used as

      input for our analysis.

      2.3.7

      |

      Generation of lesion-load maps

      Lesions were demarcated on individual T2-weighted images by a

      licensed neurologist using the MRIcron software (Rorden, Bonilha,

      Fridriksson, Bender, & Karnath, 2012).'
    supports: method
  - section: Original source P14-S2-C6
    page: 14
    quote: 'Last, we did not validate the prediction

      accuracy of our models in an independent sample of persons with

      aphasia.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kristinsson2021
  proposal_id: R001
  review_status_sha256: f65aff8b4e4c217c82b1ce6e75ce7f613b73d933411789045df84ca9ddd3969a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
        A/passages.json: 3c7b1af1e353447caf5f857d562ddcabfd5bdf9fcb4d24522329ff2af1c0f07e
        A/raw.json: fc1210b38cbddf4ff17dd841f7ad11e6a8bb5fef683ad889020e3bb0bfe29536
        A/source-units.json: 20f2a8ac90d090fc190c7d354f2d5b086e1111f2e67b3c6840cb0357ff2d69ca
        A/full-source-units.json: 3d07f68d0dfaef748d0350a5a7d23e9b54ce3545dd0f2f423cb4c49c3f59a1e9
        A/meta.json: 790041c1fe83f31bee6d5c1f69a836880bc73d546bd3c4361fbd66a856a787f2
        A/table-images/TABLE-7-page-12-1.png: 73adebd58c766f88e17eba9a850fa2f8a13bb511f354601ec505acae69abc8e6
        A/table-images/TABLE-1-page-5-1.png: da00781e264f4b01e13a394e62e295059ecf7c6c969658d3b858f78759984e46
        A/table-images/page-12.png: 5acbc56175882dbc516c47efcdad91fe2d71edab79cd5bee78bad4c19d26e250
        A/table-images/TABLE-4-page-9-1.png: 6a073ef3a109e08ff95669edd9840fb85af17e6b169b5d7a22e2bb98d34b8713
        A/table-images/page-10.png: 3f9a1ed4d8efc9723bbb660edc2a1e4b90115849c89422fbee5f1b8a546cc603
        A/table-images/page-11.png: 0bbe243fd6e0ffbb5e74ba74fb6a690e7b92cc3103acfc835327ab0387e72f46
        A/table-images/page-6.png: d093e76733b8a3f1f7729d6fa4a17c20a9c144d5b3b491e1b0eef84b63558f36
        A/table-images/TABLE-3-page-8-1.png: d2ca2a2523b4f346a7599f4eef54ce687614eb9e5c63c3128a8792e79b9a8b9f
        A/table-images/page-5.png: 3c4cb6a52ee5dc109f70c7321f0598ef59882bb3963b63fd1124d9a8795c9daf
        A/table-images/page-9.png: c9dc390dbc36b7bc3dc2f9db16c12f4489ac8d03975a836259f9b924306e0c2b
        A/table-images/page-8.png: e177b5332f009320a82891bdd15011741c669950e3d64bb8117adf93e6e77801
        A/table-images/TABLE-6-page-11-1.png: 5e674612c5822b9bd6efd88f1226cf96557818dcc44ed2d463b29c23f42d2e8b
        A/table-images/TABLE-2-page-6-1.png: e63dc62b873d9067c7431b37771e6e2801b7311999768668bf6869486020ccd8
        A/table-images/manifest.json: 273d6c76f2d0c99508aa79684e371611d510ecaa25871f91e7edbd000d0e833b
        A/table-images/TABLE-5-page-10-1.png: 91e49975148ab197ee9020c611ef1050bf46ab27867290ccf72e9be6fed31c38
        A/clauses/window-10/raw.json: 9a6536f56d795b16a8a4be07991c6686bf5768a4a6ef26a9de7afc03a4a58189
        A/clauses/window-10/prompt.txt: d844063b573ad4e541cd60b936a25a8efb51cb944cc0719ce6e787b2e978be42
        A/clauses/window-10/meta.json: e111701da8db151a12fc3bbb6db42f92d022197699c95eff46185c9edd4eeb58
        A/clauses/window-03/raw.json: ebed86a018c16a3124b5777fd9f5ba0ab4b4274490eb5d9f1395b27fbba5d10e
        A/clauses/window-03/prompt.txt: 35ff5d693f4c4f7c920e051febc1ade243a295045a23f3a18804a0956044ce5b
        A/clauses/window-03/meta.json: 6f2e659b03834ab7589c0a5c861e9a979631f2de876bd9917ec587f4959684dd
        A/clauses/window-04/raw.json: 1cb87800a3b56bca0d3fc54317a547a0607bd9728b01fe088bfacba8e94492dc
        A/clauses/window-04/prompt.txt: 8751489e14e0f0f0e22fcf170ce529f2e88592cae715cda8c86065f8e707a08a
        A/clauses/window-04/meta.json: e8d6cf1ebdbbf637c94a95d9ce7dc7cb9507f6c7674e149bfd747edd70fbd802
        A/clauses/window-05/raw.json: f53e6544eee2207bf061e1f45c168a435a324c64c6ff8d60ed163de64e5c4b8a
        A/clauses/window-05/prompt.txt: 0ed40347cffe2b0ab4dda3df036cae9ca1ca34bec3d9ea90a56e9c63ac71b83c
        A/clauses/window-05/meta.json: c9a469606f7f7b85c12127c31880662c4178f7cd6d946277e37498424355a8d3
        A/clauses/window-02/raw.json: b1d3ccc257a2969c8d7b3ef18321d9e594126c42508f9054171afd036a5202aa
        A/clauses/window-02/prompt.txt: f1f276faa9f4e904771333aa6692a9873919323b5183dc473801b96ffecedbd8
        A/clauses/window-02/meta.json: b3c1566640778ea2e1b7f1d5586a0a16f5d0751b7c3c07af69d843af235316c1
        A/clauses/window-09/raw.json: 9a3e39dcacd3f494572c256f46165bf97c0a377d13abaf564cc084e6b581b8c6
        A/clauses/window-09/prompt.txt: 6eaad37c62d1a5cb3d20b7be4392dea4da56e7c9f328a11956cc457073c0aac6
        A/clauses/window-09/meta.json: decd49c062d7fd32ee0c8f6c292bdd9d9b6c5f270bdab894d657c466d623cd71
        A/clauses/window-07/raw.json: eb0a0c11e019a7db17b0841e1011f9bd8a2a415a7ca3ddd1ee589ac0f7614efe
        A/clauses/window-07/prompt.txt: 279ed780a1bb550c5b29fdf99f113080d5e5803fcaff49f89f393de48e6fd3a2
        A/clauses/window-07/meta.json: 3268944f46c7692a66f405b4bb1e76a59f37e723dcf30c23788483f835c5ecb7
        A/clauses/window-01/raw.json: 18e71dd3a43107130de80b11d17bcdadab9d03eb585c35d7f94b6609f8912295
        A/clauses/window-01/prompt.txt: 2fc0dfe6906e8a0c38916704e7fc6ca16ef5e04f6473ab3d87918b01ec0f4027
        A/clauses/window-01/meta.json: c5d38de2f16fb102360ebd61fc6d3e27940ac71024c8f2944060076e8ade62a5
        A/clauses/window-06/raw.json: 1415ed4019844b578247f0c529c7efd71e680acc6ca25e658fe185d5f98b8608
        A/clauses/window-06/prompt.txt: d435104fc0559b57d0d280806932a690105018c3527c4c5d612da07ae8320c8a
        A/clauses/window-06/meta.json: c42af922cc8d7e129323e8a8b34610d3dbb32412dabd148b5902649ad98081af
        A/clauses/window-08/raw.json: 17c0830f10b9d5a6f3711a9421e55207efd4fa3fab4796fe38cf75ee05bba761
        A/clauses/window-08/prompt.txt: 2c08df4ce195a089e208e0a0c5986bead63c1a6ff9386dccc5aca5fbf744d88c
        A/clauses/window-08/meta.json: bd7dadae15713e3f937250a4f8a1be08a0df86f0b63706a22e224dad21e36045
        A/tables/TABLE-1-page-5-1/raw.json: eb3eb42e970c05d510b80952584c0bd8975dc082022a9fdb3d0d710f60be3b3d
        A/tables/TABLE-1-page-5-1/prompt.txt: 247713f30b63b6a0a651f93ce0398937a94c9ffac8fef37994a4d369a4750503
        A/tables/TABLE-1-page-5-1/meta.json: 6f9e79807cb3c8f8b87212d8382d0fdddc77daab7afa766a309fda2055151521
        A/tables/TABLE-6-page-11-6/raw.json: 0344a369ef03aca99902ddac585db9d23972c72640ed718f355f1ea8723a4652
        A/tables/TABLE-6-page-11-6/prompt.txt: 3a9968d13fbaabfa0a11bcb91bcb8387d10ef1feebb0b9266c66f1be747fbd30
        A/tables/TABLE-6-page-11-6/meta.json: bb8f1c79bc84de1d53d9f12a366e85b86bebae3e7628f8c8537acf361f3bda13
        A/tables/TABLE-7-page-12-7/raw.json: 92a8b3f075b829acd4cb5eba90d9a473b57dcb8510db760129a273bc33b3d690
        A/tables/TABLE-7-page-12-7/prompt.txt: da03dcbcc2c4493bbefc58e875853e56a8d30ca8d659a1a12f2e68804bd6488b
        A/tables/TABLE-7-page-12-7/meta.json: 9a32c5c16ebc09702bca5ea52f6508ebfbba7cd70b3730cbc20d861821e5c445
        A/tables/TABLE-3-page-8-3/raw.json: 5f708f06439bf8e494ae4e9b08cd3065fc52022f6d989698fad7a0bc1f1558cf
        A/tables/TABLE-3-page-8-3/prompt.txt: 16743bebf434bf61b72a4cc675cb09a682148251adf76929395aa97e9217433c
        A/tables/TABLE-3-page-8-3/meta.json: cda011c40624dd6eed7003dad237c830bac250e7ef47bd10729694a7219488a8
        A/tables/TABLE-2-page-6-2/raw.json: 9f346f1244b7b0d4b74164a9aaca1802fb34044eebea6b92d8c36d25d03e7544
        A/tables/TABLE-2-page-6-2/prompt.txt: 8c2b697f857d0c2bec4561e8e19a194f60d12649b11fa4d28a6da4828a99cb8b
        A/tables/TABLE-2-page-6-2/meta.json: 4a2ca362d24cb6ef4c85aa7ec99b57409bf96a3c96a8274ea9f64d699e1038fa
        A/tables/TABLE-5-page-10-5/raw.json: 97688a4002f7d6d5c03c0ac8638c2fc80f2fe6980dd1f3170a64d8c286b05301
        A/tables/TABLE-5-page-10-5/prompt.txt: 50b7c7375764b55bfc49e154c959038898e9bcd8487322f5dfd316d2e4134f54
        A/tables/TABLE-5-page-10-5/meta.json: 0f495c42b0880146c5811a6accaee515eedbf658e470439b08fa48ce74b53e2c
        A/tables/TABLE-4-page-9-4/raw.json: f70a16118b5f584d0685c6391cf471008d4ba8e327233c04530b71edad643840
        A/tables/TABLE-4-page-9-4/prompt.txt: 7383ec0284b39ff68f5287acaa3fa3217fc56c76ef9b2a06390168d30384c5c5
        A/tables/TABLE-4-page-9-4/meta.json: 940e35af35574cd10da01ee5a89486084383f4d8228f9e112c6d3d497c3ce15e
        B/passages.json: 3c7b1af1e353447caf5f857d562ddcabfd5bdf9fcb4d24522329ff2af1c0f07e
        B/raw.json: 4612772d4e7408d29902bd5aba9035d53173810efd74141f5e10ac8f464c2ad6
        B/source-units.json: 20f2a8ac90d090fc190c7d354f2d5b086e1111f2e67b3c6840cb0357ff2d69ca
        B/full-source-units.json: 3d07f68d0dfaef748d0350a5a7d23e9b54ce3545dd0f2f423cb4c49c3f59a1e9
        B/meta.json: cf2607cafcece6674275b7f4f234f6f5511ed3fe770e336cd0c1fae32550ff2c
        B/table-images/TABLE-7-page-12-1.png: 73adebd58c766f88e17eba9a850fa2f8a13bb511f354601ec505acae69abc8e6
        B/table-images/TABLE-1-page-5-1.png: da00781e264f4b01e13a394e62e295059ecf7c6c969658d3b858f78759984e46
        B/table-images/page-12.png: 5acbc56175882dbc516c47efcdad91fe2d71edab79cd5bee78bad4c19d26e250
        B/table-images/TABLE-4-page-9-1.png: 6a073ef3a109e08ff95669edd9840fb85af17e6b169b5d7a22e2bb98d34b8713
        B/table-images/page-10.png: 3f9a1ed4d8efc9723bbb660edc2a1e4b90115849c89422fbee5f1b8a546cc603
        B/table-images/page-11.png: 0bbe243fd6e0ffbb5e74ba74fb6a690e7b92cc3103acfc835327ab0387e72f46
        B/table-images/page-6.png: d093e76733b8a3f1f7729d6fa4a17c20a9c144d5b3b491e1b0eef84b63558f36
        B/table-images/TABLE-3-page-8-1.png: d2ca2a2523b4f346a7599f4eef54ce687614eb9e5c63c3128a8792e79b9a8b9f
        B/table-images/page-5.png: 3c4cb6a52ee5dc109f70c7321f0598ef59882bb3963b63fd1124d9a8795c9daf
        B/table-images/page-9.png: c9dc390dbc36b7bc3dc2f9db16c12f4489ac8d03975a836259f9b924306e0c2b
        B/table-images/page-8.png: e177b5332f009320a82891bdd15011741c669950e3d64bb8117adf93e6e77801
        B/table-images/TABLE-6-page-11-1.png: 5e674612c5822b9bd6efd88f1226cf96557818dcc44ed2d463b29c23f42d2e8b
        B/table-images/TABLE-2-page-6-1.png: e63dc62b873d9067c7431b37771e6e2801b7311999768668bf6869486020ccd8
        B/table-images/manifest.json: 84abc167a47b9cfadc8042d92e79932ef42dd1c4e056c431896aeac7350a1027
        B/table-images/TABLE-5-page-10-1.png: 91e49975148ab197ee9020c611ef1050bf46ab27867290ccf72e9be6fed31c38
        B/clauses/window-10/raw.json: dc638524796fec67fe1fe91d90d3f8b0368067e7476bdea993c6b0d2efbbdfde
        B/clauses/window-10/prompt.txt: d844063b573ad4e541cd60b936a25a8efb51cb944cc0719ce6e787b2e978be42
        B/clauses/window-10/meta.json: 443321be690e5d1f9eb79a3ca7bba2c392cd528de19a94e7f58cbe26e3e6f0b1
        B/clauses/window-03/raw.json: 96200a4a560d16936281abf70c3365eb00595df0cb5fce9d4ddc1e53dfbb8bd1
        B/clauses/window-03/prompt.txt: 35ff5d693f4c4f7c920e051febc1ade243a295045a23f3a18804a0956044ce5b
        B/clauses/window-03/meta.json: c6a3e0a64eead29898d91676980fc2e602145cde94a46a63b5cc645cd4b6aadf
        B/clauses/window-04/raw.json: 941f3e5c11add6edc6c6a4bc5b81232cd2f8578e8a4eed5725460e1e779e17de
        B/clauses/window-04/prompt.txt: 8751489e14e0f0f0e22fcf170ce529f2e88592cae715cda8c86065f8e707a08a
        B/clauses/window-04/meta.json: e5318d05b56c25a36df95f0c2d54d0e90e424738a5a0a9ac249e5228d0ffb594
        B/clauses/window-05/raw.json: 1c3504cf6be80299ad9adcc84423b226755c8f151ed5cc5931d300ec6d1fb2af
        B/clauses/window-05/prompt.txt: 0ed40347cffe2b0ab4dda3df036cae9ca1ca34bec3d9ea90a56e9c63ac71b83c
        B/clauses/window-05/meta.json: 1ab466e471ef30f15cfef5427560d95628d1bc4aab5774aa1cff4314a5fed649
        B/clauses/window-02/raw.json: 45df5a6464a9a6997d139e48c4b7653c23c8e6f7a82e6a89803ff9969a2d1244
        B/clauses/window-02/prompt.txt: f1f276faa9f4e904771333aa6692a9873919323b5183dc473801b96ffecedbd8
        B/clauses/window-02/meta.json: ad16cf8785a59a9018b24075f1adce983059bf1ced7f7544da4aff95a6e757b1
        B/clauses/window-09/raw.json: 93e37678a57eee23087a85c65f9ece2fcab93e99238dfacd61a8d623f2320f55
        B/clauses/window-09/prompt.txt: 6eaad37c62d1a5cb3d20b7be4392dea4da56e7c9f328a11956cc457073c0aac6
        B/clauses/window-09/meta.json: a6588124de0f98f650fde7bbd3605eb234e23667ae86853fa9674cce57a80804
        B/clauses/window-07/raw.json: 022006cd7e51f87c259408859d61a8152bdbbd164e8ece6a4244fe9b2edaff72
        B/clauses/window-07/prompt.txt: 279ed780a1bb550c5b29fdf99f113080d5e5803fcaff49f89f393de48e6fd3a2
        B/clauses/window-07/meta.json: a6699ebe7c6fd899d24aa18d9be26c6bd64fdb767df8e4b18f1b4d89f4d98016
        B/clauses/window-01/raw.json: 5a800e6e8172cdcf9827f4f6154e1a6549330168074945a18cac9a890481746f
        B/clauses/window-01/prompt.txt: 2fc0dfe6906e8a0c38916704e7fc6ca16ef5e04f6473ab3d87918b01ec0f4027
        B/clauses/window-01/meta.json: f4fbaccf067fcd602e5f6b2c2455ec27ac2b05cb729a64868b8f1fc5b52b2726
        B/clauses/window-06/raw.json: e4476a89b0cff5cdefd6dbae247f1d2112dcd863d180af20afc4efa575cf092f
        B/clauses/window-06/prompt.txt: d435104fc0559b57d0d280806932a690105018c3527c4c5d612da07ae8320c8a
        B/clauses/window-06/meta.json: ab34db76da5f99737c6d2b6b4c93d305167f2233902a4498d1d03aef31bf8910
        B/clauses/window-08/raw.json: 041d7ad6ff85332c49d284628cf187172be10e8c404fbdbc70b53c55bdeaeb0c
        B/clauses/window-08/prompt.txt: 2c08df4ce195a089e208e0a0c5986bead63c1a6ff9386dccc5aca5fbf744d88c
        B/clauses/window-08/meta.json: d0658d06cd3bc51d07729db085fd2e8ea016192fce82769b7db610e6d158558c
        B/tables/TABLE-1-page-5-1/raw.json: 8ddb2019b6c66e2ea22375b841e50c95259c409a9f9a3359ddbdaf87250b533b
        B/tables/TABLE-1-page-5-1/prompt.txt: 247713f30b63b6a0a651f93ce0398937a94c9ffac8fef37994a4d369a4750503
        B/tables/TABLE-1-page-5-1/meta.json: 975c232248bab8bebf62b6ea338a6c3d52db3fdc37b5be7e807fc6e41859e8fb
        B/tables/TABLE-6-page-11-6/raw.json: b36db5e689a449cad3e38023b62949c40f2a09015447592f1196513948be10bc
        B/tables/TABLE-6-page-11-6/prompt.txt: 3a9968d13fbaabfa0a11bcb91bcb8387d10ef1feebb0b9266c66f1be747fbd30
        B/tables/TABLE-6-page-11-6/meta.json: 1b368a57f39212639fcc65c8594e1f31c18fabe19d26772de8c9419a48a81506
        B/tables/TABLE-7-page-12-7/raw.json: 56ae76c67f082f54861d88a7bad51e07804d57df9aac0d091f3e163a9f4cf058
        B/tables/TABLE-7-page-12-7/prompt.txt: da03dcbcc2c4493bbefc58e875853e56a8d30ca8d659a1a12f2e68804bd6488b
        B/tables/TABLE-7-page-12-7/meta.json: caca89a868e34d19b37eb736d508b0cb1194449075e0d87bc69a6cc24411fe1b
        B/tables/TABLE-3-page-8-3/raw.json: ae80a924dc59520ea40a8f954e14a4b489f5ce7d9c4e025a42dcd9ffcb103644
        B/tables/TABLE-3-page-8-3/prompt.txt: 16743bebf434bf61b72a4cc675cb09a682148251adf76929395aa97e9217433c
        B/tables/TABLE-3-page-8-3/meta.json: 552986fbbd07b1b8eaac3e9e50846eadc27920559a5e3a8a7dbeb21bea530b94
        B/tables/TABLE-2-page-6-2/raw.json: 2a82bf2786484ae1acc40278b704cd3e9995f5a09fe930d9e252b505714c9b10
        B/tables/TABLE-2-page-6-2/prompt.txt: 8c2b697f857d0c2bec4561e8e19a194f60d12649b11fa4d28a6da4828a99cb8b
        B/tables/TABLE-2-page-6-2/meta.json: d7235f98030f65e89d8b80b5fe6a043e548501f1e8b609914edab4ed9fb0de28
        B/tables/TABLE-5-page-10-5/raw.json: ea37ddf49e8028db48507119f7225a81eb5ac96b41e9b707dcbc2b80437fcab8
        B/tables/TABLE-5-page-10-5/prompt.txt: 50b7c7375764b55bfc49e154c959038898e9bcd8487322f5dfd316d2e4134f54
        B/tables/TABLE-5-page-10-5/meta.json: a2e369fc7ad65ade6b3fa851c3b33ca2f3740cfe228c3f9ac2c1a804918843df
        B/tables/TABLE-4-page-9-4/raw.json: 5771efe1296772e2741448c240e570eabdc89e27d19068bb2ea2859478655de4
        B/tables/TABLE-4-page-9-4/prompt.txt: 7383ec0284b39ff68f5287acaa3fa3217fc56c76ef9b2a06390168d30384c5c5
        B/tables/TABLE-4-page-9-4/meta.json: d19f958deaec0b643ddcfab5f86824f3a68157e61e0aa55381c545ad6ec5aed6
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
      pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2021
      source_status_sha256: a2469ab2c7c40094caa92518886d24185caf7e7ce428e41c542f8b5d6acb367a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: lesion volume
    outcome:
      text: all language measures (WAB-AQ, Fluency, Spontaneous Speech, Naming, Speech
        Repetition, and Auditory Comprehension)
    analysis_label: Univariate linear regression
    relation: association
    evidence_ids:
    - P10-S1-C4
    qualifier_ids:
    - P10-S1-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2021
      source_status_sha256: a2469ab2c7c40094caa92518886d24185caf7e7ce428e41c542f8b5d6acb367a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S2-C3
      - Unaccounted source passage P8-S2-C3
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P9-S2-C2
      - 'window 6: invalid/duplicate disposition P10-S3-C2'
      - Result passage disposed without unit P13-S1-C2
      - Result passage disposed without unit P13-S3-C4
      - Result passage disposed without unit P14-S2-C9
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 225
      unselected_timing_passages:
      - P1-S1-C5
      - P3-S3-C13
      - P3-S4-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P8-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P7-S3-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-8-3
      - TABLE-4-page-9-4
      - TABLE-5-page-10-5
      - TABLE-6-page-11-6
      - TABLE-7-page-12-7
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-8-3
      - TABLE-4-page-9-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S4
        - P10-S1
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
      source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2021
      source_status_sha256: a2469ab2c7c40094caa92518886d24185caf7e7ce428e41c542f8b5d6acb367a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of prediction accuracy range in abstract.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of multimodal model accuracy in abstract.
    - source_id: P1-S2-C7
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Restatement of statistical superiority in abstract.
    - source_id: P3-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean lesion volume.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive ceiling scores.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of preprocessing quality check.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of covariate inclusion for preselection.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of kernels during model development.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of modality correlations.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of modality correlations.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of modality correlations.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of modality correlations.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between lesion volume and language measures.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes sex difference in lesion volume.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes features associated with WAB-AQ.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes features associated with other language measures.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of feature distribution across modalities.
    - source_id: P10-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to accuracy table.
    - source_id: P10-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of predictor counts.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports multimodal model accuracy across all measures.
    - source_id: P11-S1-C2
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of accuracy improvement.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 4
      - 6
      reason: Reports WAB-AQ variance and statistical superiority.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Reports superiority over specific single-modality models.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Reports lack of statistical superiority for Fluency and Naming.
    - source_id: P12-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of trend for non-significant results.
    - source_id: P12-S1-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of general model superiority in discussion.
    - source_id: P13-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary analysis.
    - source_id: P13-S1-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Reports fMRI model accuracy for WAB-AQ.
    - source_id: P13-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Reports FA and lesion-load accuracy for Fluency/Spontaneous Speech.
    - source_id: P13-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Naming score variability.
    - source_id: P13-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: Reports FA model accuracy for Naming.
    - source_id: P13-S2-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Reports lesion-load and FA accuracy for Repetition/Comprehension.
    - source_id: P13-S2-C6
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of 28/30 model comparisons.
    - source_id: P13-S2-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of multimodal accuracy range.
    - source_id: P13-S3-C4
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of statistical superiority.
    - source_id: P13-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with prior studies (Hope et al, Halai et al).
    - source_id: P13-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of modality correlations.
    - source_id: P14-S2-C9
      disposition: repeated
      result_indexes:
      - 4
      - 7
      reason: Concluding summary of multimodal improvement.
    unresolved_coverage:
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C5
    - P1-S2-C6
    - P1-S2-C7
    - P3-S4-C2
    - P4-S1-C5
    - P6-S1-C4
    - P8-S1-C4
    - P8-S2-C3
    - P9-S2-C2
    - P9-S2-C3
    - P10-S1-C1
    - P10-S1-C2
    - P10-S1-C11
    - P10-S1-C12
    - P10-S1-C15
    - P11-S1-C2
    - P12-S1-C2
    - P12-S1-C3
    - P12-S1-C4
    - P12-S1-C7
    - P13-S1-C2
    - P13-S1-C10
    - P13-S2-C6
    - P13-S2-C7
    - P13-S2-C8
    - P13-S2-C9
    - P13-S3-C4
    - P13-S3-C5
    - P13-S3-C10
    - P14-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-8-3
    - TABLE-4-page-9-4
    - TABLE-5-page-10-5
    - TABLE-6-page-11-6
    - TABLE-7-page-12-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C12
      recruited_sample:
      - P3-S3-C5
      eligibility:
      - P3-S3-C9
      - P3-S3-C10
      imaging_provenance:
      - P6-S1-C6
      - P6-S1-C7
      - P13-S4-C6
      imaging_timing:
      - P3-S3-C11
      outcome_timing:
      - P3-S3-C11
      outcome_definition:
      - P4-S1-C3
      validation:
      - P7-S2-C11
      - P14-S2-C6
      analysis_restrictions:
      - P8-S1-C2
      - P8-S1-C6
      - P14-S1-C9
      - P14-S1-C10
      - P14-S1-C11
      - P14-S1-C12
      dependent_variable_statement:
      - P1-S2-C3
      - P3-S3-C4
      - P3-S3-C5
      - P7-S3-C3
      limitations:
      - P14-S1-C8
      - P14-S1-C10
      - P14-S1-C11
      - P14-S1-C12
      - P14-S2-C4
      - P14-S2-C5
      - P14-S2-C6
      personal_factors:
      - P7-S3-C7
      - P8-S1-C4
      - P8-S1-C5
      - P10-S1-C3
      tested_personal_effects:
      - P10-S1-C4
      adjustment_roles:
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C7
      - P8-S3-C4
      - P9-S1-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C13
      - P10-S1-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P8-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P7-S3-C7
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
      pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
      review_sha256: f65aff8b4e4c217c82b1ce6e75ce7f613b73d933411789045df84ca9ddd3969a
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
      - P10-S1-C4
      source_result: Univariate linear regression analysis revealed that lesion volume
        was the only variable significantly associated with all language measures
        (WAB-AQ, Fluency, Spontaneous Speech, Naming, Speech Repetition, and Auditory
        Comprehension), with all p-values < .001. No significant associations were
        found for age, time poststroke, or sex with these language measures.
      result_status: detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P7-S3-C7, P10-S1-C3) explicitly describes a univariate
            linear regression analysis testing the association between lesion volume
            and language measures. The proposed core correctly identifies this analysis
            and its outcome.
          source_ids:
          - P7-S3-C7
          - P10-S1-C3
          - P10-S1-C4
        direction:
          answer: fits
          reason: The source states a significant association was found (P10-S1-C4).
            The table readings (Table 4) show negative estimates for lesion volume
            across all language measures, indicating that higher lesion volume is
            associated with lower language scores (greater impairment). The proposed
            core states 'significantly associated' which is directionally neutral
            but factually correct; it does not contradict the source. The direction
            'likely' in the proposed core is vague but not incorrect given the context
            of impairment.
          source_ids:
          - P10-S1-C4
          - P10-S1-C3
        construct:
          answer: fits
          reason: The exposure is 'lesion volume' (defined in P9-S1-C7 as number of
            lesioned voxels). The outcome is 'language measures' (defined in P4-S1-C3
            as WAB subscores). The method is univariate linear regression. The patient
            measurement is regional_lesion_load (lesion volume is a scalar measure
            of total lesion extent, not a voxel-wise map or template overlap in this
            specific regression context, though derived from lesion maps). The proposed
            core correctly identifies these constructs.
          source_ids:
          - P9-S1-C7
          - P4-S1-C3
          - P7-S3-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis used
            univariate linear regression. It also includes the limitation that models
            were not validated in an independent sample (P14-S2-C6). These are faithful
            to the source. The core does not incorrectly claim that the association
            is robust to adjustment (it is univariate) or that it is the primary prediction
            model (it is a preliminary analysis).
          source_ids:
          - P7-S3-C7
          - P14-S2-C6
        missing_material_caveat:
          answer: fits
          reason: The core captures the main finding and key limitations. The fact
            that this is a 'preliminary' analysis (P9-S1-C10) is a minor contextual
            detail, but the core's focus on the association itself is valid. The lack
            of external validation is included. No material caveat that changes the
            interpretation of the association is missing.
          source_ids:
          - P14-S2-C6
          - P9-S1-C10
      optional_pending:
      - Specific p-values and effect sizes from Table 4 are not transcribed in the
        core, but this is acceptable for a qualitative draft.
      - The specific direction of the association (negative correlation) is not explicitly
        stated in the claim, only 'associated', which is acceptable but less precise.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values and effect sizes from Table 4 are not transcribed in the core,
      but this is acceptable for a qualitative draft.
    - The specific direction of the association (negative correlation) is not explicitly
      stated in the claim, only 'associated', which is acceptable but less precise.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R001
      exposure:
        text: lesion volume
      outcome:
        text: all language measures (WAB-AQ, Fluency, Spontaneous Speech, Naming,
          Speech Repetition, and Auditory Comprehension)
      analysis_label: Univariate linear regression
      relation: association
      evidence_ids:
      - P10-S1-C4
      qualifier_ids:
      - P10-S1-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
        source_review: _compare/relationships-2026-11-16/review-current/Kristinsson2021
        source_status_sha256: a2469ab2c7c40094caa92518886d24185caf7e7ce428e41c542f8b5d6acb367a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e0e71d51165ee90a7296b9c2bd4ee28932a47d37d06b96724fce85ee5997ade0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C12
          page: 3
          text_layer_sha256: e0e71d51165ee90a7296b9c2bd4ee28932a47d37d06b96724fce85ee5997ade0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'After removing subjects

          with missing data points (primarily neuroimaging data, for example,

          some participants did not have CBF data), a total of 116 participants

          were

          included

          for

          data

          analysis.'
        anchor_text: 'After removing subjects

          with missing data points (primarily neuroimaging data, for example,

          some participants did not have CBF data), a total of 116 participants

          were

          included

          for

          data

          analysis.'
        excluded_fragments: []
        image_sha256: 44fb7f82330f5fcfb9bac6997f81831b60b3bd87dca7a41d7de267944f9e5922
        transcription: 'After removing subjects

          with missing data points (primarily neuroimaging data, for example,

          some participants did not have CBF data), a total of 116 participants

          were included for data analysis'
      P3-S4-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 43b1b3e961413be8baaa5e3f49fd953bdd4c81f8b3ba523f960065a760a8f786
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d9f4c86327826cac825096ab12d0cf5e0f682862279f33a26d84e79b8fd67747
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S4-C2
          page: 3
          text_layer_sha256: d9f4c86327826cac825096ab12d0cf5e0f682862279f33a26d84e79b8fd67747
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The mean lesion volume across participants was 122.61 cm3

          (range: 2.09–472.38 cm3; Figure 1 presents the lesion distribution

          across participants) and mean time poststroke was 39.4 months

          (range: 5.6–237.1 months).'
        anchor_text: 'The mean lesion volume across participants was 122.61 cm3

          (range: 2.09–472.38 cm3; Figure 1 presents the lesion distribution

          across participants) and mean time poststroke was 39.4 months

          (range: 5.6–237.1 months).'
        excluded_fragments: []
        image_sha256: 1a100eac49c44e7cd10b5f9721e8aef00635aad27e6ef26067e815315455d359
        transcription: '. The mean lesion volume across participants was 122.61 cm³

          (range: 2.09–472.38 cm³; Figure 1 presents the lesion distribution

          across participants) and mean time poststroke was 39.4 months

          (range: 5.6–237.1 months)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'The only signifi-

    cant association was found between lesion volume and all language

    measures (all p-values <.001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
