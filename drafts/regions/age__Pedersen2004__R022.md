---
id: age
name: age
kind: classical
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: recovery_of_aphasia
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: recovery_of_aphasia
  target_kind: prognosis
  claim: age did not influence the recovery of aphasia
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 270
    population: acute stroke patients with aphasia
    phase: not_reported
    time_post_onset: recovery measured from admission to 1 year after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - some patients were admitted to internal medicine wards rather than stroke units
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: patient age at time of stroke. recovery was assessed
    using the Aphasia Quotient (AQ) of the Western Aphasia Battery. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P1-S1-C4, two-model agreement, human verification pending): . Methods:
    270 acute stroke patients with aphasia (203 with first-ever strokes) were included
    consecutively and prospectively from three hospitals in Copenhagen, Denmark, and
    assessed with the Western Aphasia Battery Original text-layer quotation is preserved
    below. PDF image reading (P1-S1-C5, two-model agreement, human verification pending):
    The assessment was repeated 1 year after stroke Original text-layer quotation
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
    - proposed_concept:recovery_of_aphasia
  citation: '@Pedersen2004'
  source_passages:
  - section: Original source P8-S3-C13
    page: 8
    quote: 'The present

      study did not find any influence of age on recovery and is

      thus in accord with most previous studies.'
    supports: claim
  - section: Original source P1-S1-C4
    page: 1
    quote: 'Methods: 270 acute stroke patients with aphasia

      (203 with first-ever strokes) were included consecutively

      and prospectively from three hospitals in Copenhagen,

      Denmark, and assessed with the Western Aphasia Batte-

      ry.'
    supports: sample
  - section: Original source P1-S1-C5
    page: 1
    quote: The assessment was repeated 1 year after stroke.
    supports: method
  - section: Original source P2-S2-C6
    page: 2
    quote: 'It is sufficient to determine the type

      of aphasia according to the Boston classification, and it yields a mea-

      sure of severity of aphasia, the Aphasia Quotient (AQ), ranging from

      0 to 100, with scores above 93.8 being considered normal (nonaphas-

      ic).'
    supports: method
  - section: Original source P6-S1-C4
    page: 6
    quote: 'However, during the study period, all pa-

      tients were not admitted to stroke or neurological depart-

      ments and, thus, some patients had to be traced on wards

      of general medicine.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pedersen2004
  proposal_id: R022
  review_status_sha256: 42d26153ceac6f6636443bf84a48054a6c8995c2806edf976473f0125a18040b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
        A/passages.json: 114b579b8258ef96365cd5da7a07634781168e96970031b7bc94737daa501756
        A/raw.json: e3640a8312f96c32b1b0befaab81851efe9610d047a69de3e9c3868502314687
        A/source-units.json: 924f85f5e7957a8ddba0f4e269353431628428753dfa5d38dd1f747d17ac6f04
        A/full-source-units.json: 5dff7e5221661c53e5afc5f02cabf9b5f75b72f1a1a40d480a981af57327fd03
        A/meta.json: 900fc25977823b11aabfc38abc45aa47b506ca2e38290740cbe4d9991ae61500
        A/table-images/TABLE-1-page-3-1.png: c61492605bb369ea5e34fd5bfadc556d7320a25a39774ec1976d82c5a5beb37f
        A/table-images/TABLE-6-page-7-1.png: 7cd40b4c36871670319e8bf6d22847f81b4e540b42b50ea4317f0aa52e1d39b6
        A/table-images/page-3.png: 363c3a07817e277a67e72d8b328b6b56f8b7d7195962c6ec048b5db2d6d8a02e
        A/table-images/page-6.png: ca4e41f1aa994753a3d6c8ae71addc83b15875ba4992fcf76a4f3776b4ff090a
        A/table-images/page-7.png: a44d61e6d88102aa53a8f11e827e7e560e7b0eda7bf2b536fba30f213806fb7d
        A/table-images/page-5.png: 681a37673f0c8f42e2617036528fdf85c1c79fec5e38c7726444b43081cb1d12
        A/table-images/page-4.png: 5881a701f8941594fa8c6c727875f0039c52297df43f51fd56c9b5bb7bf03c0c
        A/table-images/TABLE-3-page-4-2.png: 14923c73ad8435be9cb6223774f7a84116c3f2b430da3df712b98cebaa99fe3e
        A/table-images/TABLE-5-page-6-1.png: 60a9870ec48efe07b217e8ae6f15bffd3102712d8b717c4944161be6dd8452de
        A/table-images/manifest.json: 55683088b0a15f6ec436010bcf4fcac3e2263496a4aae72c135398cad657bbad
        A/table-images/TABLE-2-page-4-1.png: 1d6f8af1163e9365a9e7a11397c0ab90128cfa20d5b8d1913ba357fc70a46b70
        A/table-images/TABLE-4-page-5-1.png: 173ad4599ffa061f7ce41f0e1fec80445bf7410db6064a23a16b7687cd805e44
        A/clauses/window-03/raw.json: 14aecb81f3f45bf333233c7eb73260c55ddd72c839006a568a24ed26474ba74f
        A/clauses/window-03/prompt.txt: b83dab71340977bbf68d440404546056f2792db19480a36bb2edafc78dabc77d
        A/clauses/window-03/meta.json: a1420ff10f422f9827c498358763e01b7eed2c5917e47d9b41636cdd8b232a12
        A/clauses/window-04/raw.json: 76f6a040c550116d10108b6afd14a250157c1f2613d6bd1471fc4d8e80b3af78
        A/clauses/window-04/prompt.txt: aba96252cd151c5d82f9074e44aa379cfaf913cb54742e1d5088704adf4f2f96
        A/clauses/window-04/meta.json: 9c0ab45449524ea52b5ba25f70459a4faf99f940ed26e14faa3715a13dc2a2f1
        A/clauses/window-05/raw.json: c8373df6e3d7be37877fbb9ec4009a09e9be2d78752583cb370d809469eb16c2
        A/clauses/window-05/prompt.txt: 06b31fcd20116d0ba796b155f49f009bb534d33b6e135d8962bc629d3d2b8e49
        A/clauses/window-05/meta.json: 8bdee1abd2a80b129131f02a3e187d3f25cb8d16e798490ca67ede68d67b3b80
        A/clauses/window-02/raw.json: a6e0c3ad0e5a736446afc8da70cd6d89f4bef803b72c1dc093196edec2a0687d
        A/clauses/window-02/prompt.txt: edd118c1d947b83aec33def0039e8d8e4f4ea83e053001bd0306f70d4cc8fc7b
        A/clauses/window-02/meta.json: 7076058d1523365730cd580301eec5dd4724d34e1159d93aa9ee83d9af756232
        A/clauses/window-07/raw.json: b3fd7e910126d9c2b119bbde5ba3c9020a164b715409c36033aa77ed59d8268e
        A/clauses/window-07/prompt.txt: 3bdbe8909ea740abe8495477a3ba9715cbfa5dbe1b7d91cbeb48302c6a19012b
        A/clauses/window-07/meta.json: b60fab86ea62e89c804652811dae37843a4f77ee787cf87a1e05741d9d18c672
        A/clauses/window-01/raw.json: 4aa139a3f24b93e614bb964de72a4bfe46856c83938599c9ab7e112d8ca63948
        A/clauses/window-01/prompt.txt: 7c2215beef537683b72df511e1e883710ee923644820e85fde93c28d99d16601
        A/clauses/window-01/meta.json: 27885483aafc33383f85c93fe4c2c624ace6c75e81365793302e7c78e99fa4db
        A/clauses/window-06/raw.json: 1a1b9412fcb10dc978e12bda75987d43d310502881e5a013becb348209d756c2
        A/clauses/window-06/prompt.txt: b1abaec407eeb6d6452f524b4779a5400d6e4a0e1abb733d8b73958f1c01ec1e
        A/clauses/window-06/meta.json: 80f634668526a71d2f7d431050270d7df869691f095cd7206616988f4bc21f02
        A/tables/TABLE-5-page-6-5/raw.json: 45d827fb4aaf75f43c35400afc4aede6dbbfa2dc6aea413f3e565df885c8a52b
        A/tables/TABLE-5-page-6-5/prompt.txt: f5f677878ac582b6e77fcb98a35495f43945b4b957db634d54f7ac472a3b3411
        A/tables/TABLE-5-page-6-5/meta.json: 9b95b66bd296c6a95d05975130341942d4457f6baaf2b4a03d4809914d134660
        A/tables/TABLE-4-page-5-4/raw.json: cd04488c39db5dddc545200e1ab4c4854a86536453bd7278a5560d026b363882
        A/tables/TABLE-4-page-5-4/prompt.txt: 6e097c11f0b2890e8cf1bcf3f133937e268cdf5dc4c02ced62bd5ad7b0a440f1
        A/tables/TABLE-4-page-5-4/meta.json: 92bd36f9e4d270f4894dcb3ed2d381af57b2d5ff80f44aef723c497eb006df25
        A/tables/TABLE-1-page-3-1/raw.json: f3a98681478f7376de41836e954b6259efdbccf701ad03785cacefe6c2009d27
        A/tables/TABLE-1-page-3-1/prompt.txt: 2c95f2760b07f18a37d3c02a27413c437a8bc42b2fa5bc1ec95ced79b0b96cae
        A/tables/TABLE-1-page-3-1/meta.json: be2e02bec0138a1430d66eaa4fcb603aa1fa6ef87454612bfac82a1316b8bf40
        A/tables/TABLE-3-page-4-3/raw.json: 7aac018721c17dfae45bba2ee2954feade3d7e0fdacfe0a64eac40b6f0c0804c
        A/tables/TABLE-3-page-4-3/prompt.txt: 5b1023c423429686dc9e963169d0d5fcaab301464c5a6424544bb1f2212a8b3c
        A/tables/TABLE-3-page-4-3/meta.json: 8d583ebdafe9a92f5dcc2a38bbdc5184424d9dbad30c88e61788ad7a99219d14
        A/tables/TABLE-6-page-7-6/raw.json: 0db58f1b7a7414da1007eddfce6123622c8fecbbaaadd937b6f368c4281fae40
        A/tables/TABLE-6-page-7-6/prompt.txt: ec5d6e0e905407ef02ac8a4c2d07b0e1096c03f043e48f56a1817ea486e1a858
        A/tables/TABLE-6-page-7-6/meta.json: a500725cf5e7b73e13b9b53db6eeefa591ca16db96a2130f8cdce48360449089
        A/tables/TABLE-2-page-4-2/raw.json: 40d023f5ce48996939e4edc13053befd2207bca906fcb851a7d661b15641bf79
        A/tables/TABLE-2-page-4-2/prompt.txt: 16407a351a080d0fbebe55877da604f5b7f8aa3102303730ad955aa70e5cda36
        A/tables/TABLE-2-page-4-2/meta.json: 4f6cbe438ef7aac2b0786259d5c2e29333893bd2772d5d78f0d2fe70a7707532
        B/passages.json: 114b579b8258ef96365cd5da7a07634781168e96970031b7bc94737daa501756
        B/raw.json: bc2fd8d2df6b85313e5a531bbb2519d47d29724628e6601a74bfd05b57d0b79e
        B/source-units.json: 924f85f5e7957a8ddba0f4e269353431628428753dfa5d38dd1f747d17ac6f04
        B/full-source-units.json: 5dff7e5221661c53e5afc5f02cabf9b5f75b72f1a1a40d480a981af57327fd03
        B/meta.json: 3c307880ffac0368421c8f8624d06a8ead6d2b5105141667d17456a56c561a62
        B/table-images/TABLE-1-page-3-1.png: c61492605bb369ea5e34fd5bfadc556d7320a25a39774ec1976d82c5a5beb37f
        B/table-images/TABLE-6-page-7-1.png: 7cd40b4c36871670319e8bf6d22847f81b4e540b42b50ea4317f0aa52e1d39b6
        B/table-images/page-3.png: 363c3a07817e277a67e72d8b328b6b56f8b7d7195962c6ec048b5db2d6d8a02e
        B/table-images/page-6.png: ca4e41f1aa994753a3d6c8ae71addc83b15875ba4992fcf76a4f3776b4ff090a
        B/table-images/page-7.png: a44d61e6d88102aa53a8f11e827e7e560e7b0eda7bf2b536fba30f213806fb7d
        B/table-images/page-5.png: 681a37673f0c8f42e2617036528fdf85c1c79fec5e38c7726444b43081cb1d12
        B/table-images/page-4.png: 5881a701f8941594fa8c6c727875f0039c52297df43f51fd56c9b5bb7bf03c0c
        B/table-images/TABLE-3-page-4-2.png: 14923c73ad8435be9cb6223774f7a84116c3f2b430da3df712b98cebaa99fe3e
        B/table-images/TABLE-5-page-6-1.png: 60a9870ec48efe07b217e8ae6f15bffd3102712d8b717c4944161be6dd8452de
        B/table-images/manifest.json: 94fd6494448e4c43859bce66c8dec3903dd7138104055c692e5ad50ae9ae1325
        B/table-images/TABLE-2-page-4-1.png: 1d6f8af1163e9365a9e7a11397c0ab90128cfa20d5b8d1913ba357fc70a46b70
        B/table-images/TABLE-4-page-5-1.png: 173ad4599ffa061f7ce41f0e1fec80445bf7410db6064a23a16b7687cd805e44
        B/clauses/window-03/raw.json: af7e2faeef9739f42f8638c30bf3f0e49d1c030a54809576409f017cffed4291
        B/clauses/window-03/prompt.txt: b83dab71340977bbf68d440404546056f2792db19480a36bb2edafc78dabc77d
        B/clauses/window-03/meta.json: edaf9028dd7303362b48c01b03d95b9675997a5d3e94c326a548a9e106c69699
        B/clauses/window-04/raw.json: 3715005e4c9d14a084e8432c15ee97d2c48de999f5af8e29c984f64c78cb88e4
        B/clauses/window-04/prompt.txt: aba96252cd151c5d82f9074e44aa379cfaf913cb54742e1d5088704adf4f2f96
        B/clauses/window-04/meta.json: b25c0fde9903f7aa051bd066e74a3e9cda04973169aad52faf25fbd69aacbcb7
        B/clauses/window-05/raw.json: 34947426d95a8271414c8fe92c940cd6888f2d9d6bc5162be8f569a1ecfa409b
        B/clauses/window-05/prompt.txt: 06b31fcd20116d0ba796b155f49f009bb534d33b6e135d8962bc629d3d2b8e49
        B/clauses/window-05/meta.json: a3466c2c01f35cc822b749027a29a65863aa292dddd9e0297ef6246063d50177
        B/clauses/window-02/raw.json: 87a3030b0b057eaa8a7f0e1bf75bd4a1ee62027ec7bf67b091344bee8a133ce0
        B/clauses/window-02/prompt.txt: edd118c1d947b83aec33def0039e8d8e4f4ea83e053001bd0306f70d4cc8fc7b
        B/clauses/window-02/meta.json: 41db4c3a4bcc2a855ca247c9d32b093f02cd62be0b76f3e7ffcd95c3fdcd14d8
        B/clauses/window-07/raw.json: 83873911faa9a9a6a60def8f6eeb5aabd2ff14f294ab2de26a04e06d51aeef9b
        B/clauses/window-07/prompt.txt: 3bdbe8909ea740abe8495477a3ba9715cbfa5dbe1b7d91cbeb48302c6a19012b
        B/clauses/window-07/meta.json: 8f9deb5a07cd283f25c5dc17f41a14ae9dba2a6238242e7edd17102066de6aa2
        B/clauses/window-01/raw.json: 8ec02496a907c9bbcdd4af324c9cfcef65073a92ef0acd33c1fd0b799516de27
        B/clauses/window-01/prompt.txt: 7c2215beef537683b72df511e1e883710ee923644820e85fde93c28d99d16601
        B/clauses/window-01/meta.json: 154bae6b9e7efeb0a88ededf310f222bb54488749dccea53b2cab589c6f709e1
        B/clauses/window-06/raw.json: cdd117a00f4f39bf716b16e7102b1a192a1a94e3c87a7e838af465d21bd4abe6
        B/clauses/window-06/prompt.txt: b1abaec407eeb6d6452f524b4779a5400d6e4a0e1abb733d8b73958f1c01ec1e
        B/clauses/window-06/meta.json: 5faa1c575acc6ae30f7aaffa09c6f72af3c496eb05d09d5621adfbdab9e1c5e5
        B/tables/TABLE-5-page-6-5/raw.json: 45d827fb4aaf75f43c35400afc4aede6dbbfa2dc6aea413f3e565df885c8a52b
        B/tables/TABLE-5-page-6-5/prompt.txt: f5f677878ac582b6e77fcb98a35495f43945b4b957db634d54f7ac472a3b3411
        B/tables/TABLE-5-page-6-5/meta.json: 95fdf58d719012b4b94c2be0994bb06994887139a09096d01f797f973ebfbfce
        B/tables/TABLE-4-page-5-4/raw.json: 2d3ce7e30c2cfc10b0f101a2a494b11bd9a1f595e41caa8e8698d823c24dfc39
        B/tables/TABLE-4-page-5-4/prompt.txt: 6e097c11f0b2890e8cf1bcf3f133937e268cdf5dc4c02ced62bd5ad7b0a440f1
        B/tables/TABLE-4-page-5-4/meta.json: 920f17720b0ae4d3455f67c12abec71e8f307c6d6615a17f8c88a090e7e2a61a
        B/tables/TABLE-1-page-3-1/raw.json: 1c76ac3803f5a2677a48329569525052e82af36f2c70c076c12e1ab8441dea45
        B/tables/TABLE-1-page-3-1/prompt.txt: 2c95f2760b07f18a37d3c02a27413c437a8bc42b2fa5bc1ec95ced79b0b96cae
        B/tables/TABLE-1-page-3-1/meta.json: a67c8878fc2af29ac0c29e4360b043019142fcdc0211d0935a7e98fd4fa19ba2
        B/tables/TABLE-3-page-4-3/raw.json: efd1c2e5cd9f33087fd638eaf9219fa3a78edadebd8bc08aa80b1aeebc53a4ea
        B/tables/TABLE-3-page-4-3/prompt.txt: 5b1023c423429686dc9e963169d0d5fcaab301464c5a6424544bb1f2212a8b3c
        B/tables/TABLE-3-page-4-3/meta.json: ae67cfebc357d1636636456c570f6c810e4a3c9dc7e5874e27df72fb2d7e22df
        B/tables/TABLE-6-page-7-6/raw.json: 521848d649371db8c6757c396d6ed29f5eac76f0beb4490f0724e55673cfc049
        B/tables/TABLE-6-page-7-6/prompt.txt: ec5d6e0e905407ef02ac8a4c2d07b0e1096c03f043e48f56a1817ea486e1a858
        B/tables/TABLE-6-page-7-6/meta.json: cb8e6c9735ff1e5194e76a2aced04a2ba0c4bebc5556ef783c68f07cf49f3492
        B/tables/TABLE-2-page-4-2/raw.json: a8934ef35307fbc3c77c05c684a0f09766c42ee2cf5abd271e9d305e43111f15
        B/tables/TABLE-2-page-4-2/prompt.txt: 16407a351a080d0fbebe55877da604f5b7f8aa3102303730ad955aa70e5cda36
        B/tables/TABLE-2-page-4-2/meta.json: 6d7d20fdaaf1956232552e9fb2cc22f36dda3d6b2efb69272ba7c4bd04a479ff
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
      pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen2004
      source_status_sha256: 1321b9bc62f745cd1b554568ed7e9099ebff15aea2e95aeea4f6856915bd5e46
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R022
    exposure:
      text: age
    outcome:
      text: recovery of aphasia
    analysis_label: Analysis of age and recovery
    relation: association
    evidence_ids:
    - P8-S3-C13
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
      pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen2004
      source_status_sha256: 1321b9bc62f745cd1b554568ed7e9099ebff15aea2e95aeea4f6856915bd5e46
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P1-S2-C2
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P2-S3-C9
      - Accounting without a linked unit P3-S1-C3
      - Accounting without a linked unit P3-S1-C4
      - Accounting without a linked unit P3-S1-C5
      - Accounting without a linked unit P3-S1-C7
      - Accounting without a linked unit P3-S1-C8
      - Accounting without a linked unit P3-S1-C9
      - Unaccounted source passage P3-S1-C7
      - Unaccounted source passage P3-S1-C9
      - Unaccounted source passage P3-S1-C8
      - Unaccounted source passage P3-S1-C5
      - Unaccounted source passage P3-S1-C4
      - Unaccounted source passage P3-S1-C3
      - Result passage disposed without unit P3-S1-C11
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P3-S2-C16
      - Result passage disposed without unit P3-S2-C9
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S2-C10
      - Result passage disposed without unit P4-S2-C12
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Accounting without a linked unit P7-S1-C6
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C8
      - Unaccounted source passage P7-S1-C6
      - Result passage disposed without unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C8
      - Accounting without a linked unit P7-S2-C9
      - Result passage disposed without unit P8-S1-C15
      - Accounting without a linked unit P8-S1-C3
      - Unaccounted source passage P7-S2-C8
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P7-S2-C9
      - Result passage disposed without unit P8-S2-C9
      - Result passage disposed without unit P9-S1-C1
      - Accounting without a linked unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C4
      - Unaccounted source passage P9-S1-C3
      unattached_null_or_qualifier_ids:
      - P4-S1-C5
      - P7-S1-C6
      - P7-S2-C6
      - P9-S1-C4
      suppressed_nonrepresented_units: 24
      default_disposition_count_requires_completeness_check: 115
      unselected_timing_passages:
      - P1-S1-C4
      - P2-S1-C14
      - P2-S2-C8
      - P6-S1-C3
      - P6-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P1-S2-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S2-C13
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P4-S2-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S1-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C12
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S1-C14
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S1-C16
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C13
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C14
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C15
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C16
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C3
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C12
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: recruited_sample
        source_ids:
        - P1-S1-C4
        - P2-S1-C7
        - P2-S1-C8
        - P2-S1-C9
        - P2-S1-C10
        - P2-S1-C11
        - P2-S1-C12
        - P2-S1-C13
        - P2-S1-C14
        - P2-S1-C15
        - P2-S3-C7
        - P2-S3-C8
        - P2-S3-C9
        - P2-S3-C10
        - P3-S1-C1
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C4
        - P3-S1-C5
        - P3-S1-C6
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P3-S1-C10
        - P3-S1-C11
        - P3-S1-C12
        - P3-S1-C13
        - P3-S2-C10
        - P3-S2-C15
        - P3-S2-C16
        - P4-S1-C1
        - P4-S1-C2
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C7
        - P4-S1-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P2-S1-C7
        - P2-S1-C8
        - P2-S1-C9
        - P2-S1-C10
        - P2-S1-C11
        - P2-S1-C12
        - P2-S1-C13
        - P2-S1-C14
        - P2-S1-C15
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P1-S2-C3
        - P1-S2-C5
        - P3-S1-C13
        - P3-S2-C4
        - P3-S2-C5
        - P3-S2-C14
        - P4-S2-C7
        - P5-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P7-S2-C5
        - P7-S2-C6
        - P7-S2-C8
        - P7-S2-C9
        - P8-S1-C3
        - P8-S1-C15
        - P8-S2-C3
        - P8-S2-C4
        - P8-S2-C8
        - P8-S3-C5
        - P8-S3-C7
        - P8-S3-C13
        - P9-S1-C2
        - P9-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S1-C2
        - P3-S1-C11
        - P3-S1-C12
        - P3-S1-C13
        - P3-S2-C3
        - P3-S2-C4
        - P3-S2-C5
        - P3-S2-C10
        - P3-S2-C12
        - P4-S1-C2
        - P4-S1-C10
        - P5-S1-C6
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C14
        - P6-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - recruited_sample
      - eligibility
      - imaging_provenance
      - imaging_timing
      - validation
      - personal_factors
      - tested_personal_effects
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-3
      - TABLE-4-page-5-4
      - TABLE-5-page-6-5
      - TABLE-6-page-7-6
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-3
      - TABLE-4-page-5-4
      - TABLE-6-page-7-6
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen2004
      source_status_sha256: 1321b9bc62f745cd1b554568ed7e9099ebff15aea2e95aeea4f6856915bd5e46
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive frequency of aphasia types on admission.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of aphasia type change.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of aphasia type evolution.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive frequency of aphasia types at 1 year.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on distribution differences.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 10
      - 11
      - 12
      reason: Abstract restatement of predictors for language outcome.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 15
      reason: Abstract restatement of age difference in fluency at 1 year.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count for aphasia.
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count for remission.
    - source_id: P2-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of AQ across hospitals.
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive data on patient subset.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive CT diagnosis data.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive handedness data.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive crossed aphasia data.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive severity frequency.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive severity frequency.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive severity frequency.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive severity frequency for first-ever strokes.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Univariate analysis of AQ by age and sex.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Age difference in fluency.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Sex difference in fluency.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Fluency and AQ association.
    - source_id: P3-S2-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Sex difference in Broca's vs Wernicke's.
    - source_id: P3-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Age difference in Broca's vs Wernicke's.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive SSS mean.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive modified SSS mean.
    - source_id: P3-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Association between neurological severity and AQ.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive stroke severity by sex.
    - source_id: P3-S2-C14
      disposition: represented
      result_indexes:
      - 8
      reason: Multiple linear regression of initial AQ.
    - source_id: P3-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive data on non-participants.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive reassessment count.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive reassessment count for first-ever strokes.
    - source_id: P4-S2-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Mortality and initial AQ association.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of individual deterioration.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Regression formula.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: R2 value.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Multiple linear regression of 1-year AQ.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of aphasia type change.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on global aphasia recovery.
    - source_id: P4-S2-C12
      disposition: repeated
      result_indexes:
      - 20
      reason: ANOVA on AQ-gain between types.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Age and sex association with AQ at 1 year.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Sex difference in AQ at 1 year.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on sex differences in WAB subtests.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 13
      reason: Fluency and AQ association at 1 year.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 14
      reason: Sex difference in fluency at 1 year.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 15
      reason: Age difference in fluency at 1 year.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 16
      reason: Logistic regression performance for fluency.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 17
      reason: Sex difference in Broca's vs Wernicke's at 1 year.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 17
      reason: Sex difference in Broca's vs Wernicke's at 1 year.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 18
      reason: Age difference in Broca's vs Wernicke's at 1 year.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 18
      reason: Age difference in Broca's vs Wernicke's at 1 year.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on WAB part improvement.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on repetition improvement inconsistency.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on global aphasia and nonverbal function.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive Raven scores.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of AQ across hospitals.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive frequency of classic aphasia types.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to previous findings.
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General assumption on aphasia frequencies.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of AQ to other study.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of subtest distribution.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia prevalence at 1 year.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of aphasia type progression.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of nonfluent to fluent change.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to previous findings.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on Broca's aphasia at 1 year.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on repetition ability improvement.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of univariate sex difference in AQ.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of multiple regression result for sex.
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of sex difference in nonfluent aphasia.
    - source_id: P7-S2-C9
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of no sex difference in Broca's vs Wernicke's.
    - source_id: P8-S1-C3
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement of age difference in fluency at 1 year.
    - source_id: P8-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of tendency in univariate analysis.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 22
      reason: No effect of sex on fluency in multivariate analysis.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 22
      reason: Age significance for fluency in multivariate analysis.
    - source_id: P8-S2-C8
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of neurological severity improving prognosis.
    - source_id: P8-S3-C5
      disposition: represented
      result_indexes:
      - 20
      reason: No effect of aphasia type on AQ improvement.
    - source_id: P8-S3-C7
      disposition: represented
      result_indexes:
      - 21
      reason: No sex difference in recovery.
    - source_id: P8-S3-C13
      disposition: represented
      result_indexes:
      - 22
      reason: No age influence on recovery.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on recovery.
    - source_id: P9-S1-C2
      disposition: repeated
      result_indexes:
      - 20
      reason: Conclusion on aphasia type and recovery.
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 21
      - 22
      reason: Conclusion on age and sex as predictors of remission.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 10
      reason: Conclusion on general stroke severity as a predictor.
    unresolved_coverage:
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P1-S2-C2
    - P1-S2-C3
    - P1-S2-C5
    - P2-S3-C8
    - P2-S3-C9
    - P2-S3-C11
    - P2-S3-C12
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S1-C11
    - P3-S2-C9
    - P3-S2-C10
    - P3-S2-C12
    - P3-S2-C16
    - P4-S1-C5
    - P4-S1-C6
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C9
    - P4-S2-C10
    - P4-S2-C12
    - P5-S1-C7
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C9
    - P6-S1-C7
    - P6-S2-C5
    - P6-S2-C6
    - P6-S2-C12
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C9
    - P7-S1-C10
    - P7-S2-C3
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C8
    - P7-S2-C9
    - P8-S1-C3
    - P8-S1-C15
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C11
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-4-3
    - TABLE-4-page-5-4
    - TABLE-5-page-6-5
    - TABLE-6-page-7-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C8
      - P4-S1-C6
      - P4-S1-C8
      - P4-S1-C9
      recruited_sample: []
      eligibility: []
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C5
      - P2-S2-C9
      - P2-S2-C10
      - P4-S2-C6
      outcome_definition:
      - P2-S2-C6
      - P2-S2-C11
      - P4-S2-C6
      validation: []
      analysis_restrictions:
      - P4-S1-C9
      dependent_variable_statement:
      - P3-S2-C13
      - P4-S2-C6
      - P5-S1-C11
      limitations:
      - P2-S1-C11
      - P6-S1-C4
      - P6-S2-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C13
      - P3-S2-C14
      - P4-S2-C6
      - P4-S2-C7
      - P5-S1-C11
      - P7-S2-C6
      explicitly_not_adjusted:
      - P3-S2-C14
      - P4-S2-C7
      - P5-S1-C11
      - P7-S2-C6
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P1-S2-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S2-C13
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P4-S2-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S1-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P7-S2-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P7-S2-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P7-S2-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P7-S2-C12
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S1-C14
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S1-C16
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C13
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C14
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C15
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C16
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C3
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C8
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C12
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: recruited_sample
      source_ids:
      - P1-S1-C4
      - P2-S1-C7
      - P2-S1-C8
      - P2-S1-C9
      - P2-S1-C10
      - P2-S1-C11
      - P2-S1-C12
      - P2-S1-C13
      - P2-S1-C14
      - P2-S1-C15
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P3-S2-C10
      - P3-S2-C15
      - P3-S2-C16
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C7
      - P4-S1-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P2-S1-C7
      - P2-S1-C8
      - P2-S1-C9
      - P2-S1-C10
      - P2-S1-C11
      - P2-S1-C12
      - P2-S1-C13
      - P2-S1-C14
      - P2-S1-C15
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P1-S2-C3
      - P1-S2-C5
      - P3-S1-C13
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C14
      - P4-S2-C7
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C14
      - P7-S2-C5
      - P7-S2-C6
      - P7-S2-C8
      - P7-S2-C9
      - P8-S1-C3
      - P8-S1-C15
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C8
      - P8-S3-C5
      - P8-S3-C7
      - P8-S3-C13
      - P9-S1-C2
      - P9-S1-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S1-C2
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C10
      - P3-S2-C12
      - P4-S1-C2
      - P4-S1-C10
      - P5-S1-C6
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C14
      - P6-S1-C2
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
      pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
      review_sha256: 42d26153ceac6f6636443bf84a48054a6c8995c2806edf976473f0125a18040b
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
      - P8-S3-C13
      source_result: The study found no statistically significant influence of age
        on the recovery of aphasia, as measured by the change in Aphasia Quotient
        (AQ) from admission to 1 year post-stroke. This null finding is consistent
        with the majority of previous studies cited in the discussion.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R022) correctly identifies the relationship
            between age and aphasia recovery. The source (P8-S3-C13) explicitly states
            that the present study did not find an influence of age on recovery, matching
            the proposed core's claim.
          source_ids:
          - P8-S3-C13
          - P4-S2-C6
        direction:
          answer: fits
          reason: The source explicitly states 'did not find any influence of age
            on recovery' (P8-S3-C13) and the conclusion states 'Neither age nor sex
            predicts the degree of remission' (P9-S1-C3). The proposed core's 'no_effect'
            direction accurately reflects this null finding.
          source_ids:
          - P8-S3-C13
          - P9-S1-C3
        construct:
          answer: fits
          reason: The exposure is 'age' and the outcome is 'recovery of aphasia'.
            The source confirms age was an independent variable in regression models
            predicting AQ at 1 year (P4-S2-C6) and that no effect was found (P8-S3-C13).
            The measurement is behavioral (WAB/AQ), correctly classified as non_imaging.
          source_ids:
          - P4-S2-C6
          - P8-S3-C13
          - P2-S2-C6
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that recovery was assessed
            using the Aphasia Quotient (AQ) of the Western Aphasia Battery. This is
            supported by P2-S2-C6 and P4-S2-C6, which define the dependent variable
            as AQ. The limitation regarding admission to internal medicine wards is
            also correctly noted from P6-S1-C4.
          source_ids:
          - P2-S2-C6
          - P4-S2-C6
          - P6-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core captures the main null finding and the measurement method.
            While the source mentions that age differences were found in aphasia *type*
            at 1 year (P8-S1-C3), the specific analysis in question is about *recovery*
            (AQ change), for which no effect was found. The distinction is maintained.
            No material caveat regarding the null result itself is omitted.
          source_ids:
          - P8-S3-C13
          - P8-S1-C3
      optional_pending:
      - Specific regression coefficients or p-values for the age variable in the recovery
        model are not transcribed in the provided source window, but the qualitative
        null result is clear.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific regression coefficients or p-values for the age variable in the recovery
      model are not transcribed in the provided source window, but the qualitative
      null result is clear.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R022
      exposure:
        text: age
      outcome:
        text: recovery of aphasia
      analysis_label: Analysis of age and recovery
      relation: association
      evidence_ids:
      - P8-S3-C13
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
        pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
        source_review: _compare/relationships-2026-11-16/review-current/Pedersen2004
        source_status_sha256: 1321b9bc62f745cd1b554568ed7e9099ebff15aea2e95aeea4f6856915bd5e46
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a7ed34cfefff32a39c4d30162d8aee026cc39e705fb0ec0b098ea1fbaa3fda5e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C4
          page: 1
          text_layer_sha256: a7ed34cfefff32a39c4d30162d8aee026cc39e705fb0ec0b098ea1fbaa3fda5e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods: 270 acute stroke patients with aphasia

          (203 with first-ever strokes) were included consecutively

          and prospectively from three hospitals in Copenhagen,

          Denmark, and assessed with the Western Aphasia Batte-

          ry.'
        anchor_text: 'Methods: 270 acute stroke patients with aphasia

          (203 with first-ever strokes) were included consecutively

          and prospectively from three hospitals in Copenhagen,

          Denmark, and assessed with the Western Aphasia Batte-

          ry.'
        excluded_fragments: []
        image_sha256: 43bd368cf644d4d611354c8aba935ba74de452181643e3576dde1370ec99580b
        transcription: '. Methods: 270 acute stroke patients with aphasia (203 with
          first-ever strokes) were included consecutively and prospectively from three
          hospitals in Copenhagen, Denmark, and assessed with the Western Aphasia
          Battery'
      P1-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 311b40a71103ce1439583f5bffe66383352c822bdbd0483bb85302e6bc7c24a0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 88ed6ef2cdfcedc1391a3268e4446b60af5491d1b7d1bfc22063606e9c170c90
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C5
          page: 1
          text_layer_sha256: 88ed6ef2cdfcedc1391a3268e4446b60af5491d1b7d1bfc22063606e9c170c90
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: The assessment was repeated 1 year after stroke.
        anchor_text: The assessment was repeated 1 year after stroke.
        excluded_fragments: []
        image_sha256: 4d39766b2a7de627257c857de97baa87fbbdbe2191e4fff9fd67094064096108
        transcription: The assessment was repeated 1 year after stroke
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'The present

    study did not find any influence of age on recovery and is

    thus in accord with most previous studies.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
