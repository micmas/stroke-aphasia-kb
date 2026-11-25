---
id: ldlpfc_to_lptl_modulation
name: lDLPFC to lPTL auditory speech modulation
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: language_improvement
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_improvement
  target_kind: prognosis
  claim: Greater auditory speech processing-induced facilitation of the connection
    from the left DLPFC to the left PTL in the acute phase was associated with more
    language improvement from the subacute to the chronic phase.
  direction: likely
  relationship: correlational
  method: computational_model
  sample:
    n: not_reported
    population: patients with either left-hemispheric frontal or temporo-parietal
      first-time ischaemic stroke
    phase: not_reported
    time_post_onset: Predictor measured in acute phase (≤1 week); outcome measured
      as improvement from subacute (1-2 weeks) to chronic (>6 months) phase.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (17 patients per lesion group).
  - DCM focuses on a restricted set of regions rather than large-scale networks.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The modulatory influence of auditory speech processing
    on the effective connectivity from the left dorsolateral prefrontal cortex (lDLPFC)
    to the left posterior temporal lobe (lPTL), measured via Dynamic Causal Modelling
    (DCM) during an auditory sentence comprehension paradigm in the acute phase (≤1
    week post-stroke). The association was found to be independent of lesion location.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P3-S1-C11, two-model agreement, human verification
    pending): Materials and methods

    Participants

    Two groups of patients with either frontal (n = 17, mean age 52.3 ± 18.9 years,
    7 female) or temporo-parietal (n = 17, mean age 54.4 ± 12.7 years, 2 female) first
    time ischaemic stroke lesions were examined longitudinally during the acute (≤1
    week), subacute (1–2 weeks) and chronic (>6 months) phases after stroke Original
    text-layer quotation is preserved below. PDF image reading (P1-S1-C10, two-model
    agreement, human verification pending): . All patients repeatedly underwent an
    auditory sentence comprehension paradigm during functional neuroimaging in the
    acute (≤1 week), subacute (1–2 weeks) and chronic (>6 months) phases after stroke
    Original text-layer quotation is preserved below. PDF image reading (P10-S3-C8,
    two-model agreement, human verification pending): . Other factors

    may also have contributed to the lack of behavioural relevance: as

    we assigned patients to two groups based on their lesion sites, there

    were ultimately only 17 patients in each group Original text-layer quotation is
    preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:language_improvement
  citation: '@Jiang2025'
  source_passages:
  - section: Original source P5-S3-C11
    page: 5
    quote: "For the connection from lDLPFC to lPTL, greater auditory speech \nprocessing-induced\
      \ facilitation in the acute phase was associated \nwith more language improvement\
      \ from the subacute to the chronic \nphase (β = 0.35, P = 0.029) (Fig. 3B)."
    supports: claim
  - section: Original source P3-S1-C11
    page: 3
    quote: "Materials and methods\nParticipants\nTwo groups of patients with either\
      \ frontal (n = 17, mean age 52.3 ±  \n18.9 years, 7 female) or temporo-parietal\
      \ (n = 17, mean age 54.4 ±  \n12.7 years, 2 female) first time ischaemic stroke\
      \ lesions were exam­\nined longitudinally during the acute (≤1 week), subacute\
      \ (1–2 \nweeks) and chronic (>6 months) phases after stroke."
    supports: sample
  - section: Original source P1-S1-C10
    page: 1
    quote: "All patients repeatedly underwent \nan auditory sentence comprehension\
      \ paradigm during functional neuroimaging in the acute (≤1 week), subacute \n\
      (1–2 weeks) and chronic (>6 months) phases after stroke."
    supports: method
  - section: Original source P3-S2-C5
    page: 3
    quote: "Language performance was assessed with the Aachen Aphasia \nTest (AAT),42\
      \ the standard diagnostic battery for subacute and chronic \naphasia in Germany\
      \ (Supplementary material for details)."
    supports: method
  - section: Original source P3-S3-C1
    page: 3
    quote: "Effective connectivity analyses\nEffective connectivity within the LN\
      \ and between the LN and the \nMDN was explored using DCM with the Parametric\
      \ Empirical \nBayes (PEB) framework in SPM12 implemented in MATLAB (version\
      \ \n9.12)."
    supports: method
  - section: Original source P5-S3-C8
    page: 5
    quote: "We first report correlations independent of lesion locations, \nwhich\
      \ means that a significant interaction effect with lesion loca­\ntion was absent\
      \ in the linear mixed models (Fig. 3)."
    supports: confounders
  - section: Original source P10-S3-C8
    page: 10
    quote: "Other factors \nmay also have contributed to the lack of behavioural relevance:\
      \ as \nwe assigned patients to two groups based on their lesion sites, there\
      \ \nwere ultimately only 17 patients in each group."
    supports: limitation
  - section: Original source P11-S1-C1
    page: 11
    quote: "\nA general limitation of DCM is its focus on functional interactions\
      \ \nwithin a restricted set of regions rather than large-scale networks."
    supports: limitation
predictor_type: imaging_metric
short_definition: The modulatory influence of auditory speech processing on the effective
  connectivity from the left dorsolateral prefrontal cortex (lDLPFC) to the left posterior
  temporal lobe (lPTL), measured via Dynamic Causal Modelling (DCM) during an auditory
  sentence comprehension paradigm in the acute phase (≤1 week post-stroke).
assessment:
- Dynamic Causal Modelling (DCM)
- Aachen Aphasia Test (AAT)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Jiang2025
  proposal_id: R009
  review_status_sha256: 67cf768b6d25de85286c6c4101332fdf10fbc411c4c6d80b9f300eb04cd4e496
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
        A/passages.json: b3978e04ea5350f70adb5c97458700690e46e5883da7f379e7d7e7616d3de429
        A/raw.json: e34567b485c828f14759c5ca39fe534533a16d488bef231209d4a0874abc3dc7
        A/source-units.json: 257d218fca1fe209ed63e6a4e75a24921308670ef09451b64e1823efac635f2a
        A/full-source-units.json: 77f8e2779e378854d1223d8a1529ea6558e6088468f46da8a679b03bd5690c19
        A/meta.json: 0c5c19a670f24a634f44d02aaf1ca76812bc88f4315ff90469c2f8b05ea0e1be
        A/table-images/TABLE-1-page-7-1.png: f94ebd944d3888871f38ea35682cb7103f6f833cdd1639db9d6175e8b658bb88
        A/table-images/page-7.png: 294bb421cef309e3e8e764f8abcba59f1f6321a6467b3c81bf084c37c122ea17
        A/table-images/manifest.json: d417ffd47ac6667f45fc77b5733a20835c4a29fb973c3caa37d30a372f31a976
        A/clauses/window-10/raw.json: 9000aafddba26e0c0e2400392fc0083573585d81dc62126fa1c598afee72eba6
        A/clauses/window-10/prompt.txt: f5f46e10c54584bfd7884045a6a81d2e4dd0d5a0e61c4b9b46a1cad5b21c8478
        A/clauses/window-10/meta.json: 823e747e4332ec1496688b70e003b7e7ab8884077c498091903b3a2a3b78250f
        A/clauses/window-03/raw.json: 4ba32959c603a97976f28541ba2799c95bf83c0aa4f9f05c3a17c06ee628d996
        A/clauses/window-03/prompt.txt: 491b1821f8e99b39512acd56c498a72d126e565070aa5197e3681ce3ed81b294
        A/clauses/window-03/meta.json: 1df434c021a2bc1f68c49a545eeb7f4cec54f7478f97d46ec0f2da081c648b79
        A/clauses/window-04/raw.json: 91dfa194d55a7d450f4dab5472a2d6a4eabca126a2ad50e5cbd4a75052f4d2fd
        A/clauses/window-04/prompt.txt: 0d70c534cc6df773ec41bd170b7804d1f43d0ea6d52a63f245cd15c93eb22480
        A/clauses/window-04/meta.json: bd5c48dea38c8be416a6527453eab2ac280014e4164b5ee454de87b294665fc6
        A/clauses/window-05/raw.json: 640976c9d19481f71d68a1a17491e77513b7e2f8363523594276c3f24dd0b3c4
        A/clauses/window-05/prompt.txt: 7480d738d1d3dcf6edb28340025680737e476cbe871782b9ecdd510c94318dad
        A/clauses/window-05/meta.json: bba5ed2b62f453994b88af3caf0434ecb68fd4424f865ced6d49c3722b18f161
        A/clauses/window-02/raw.json: 3db4a190d81113d8ab86cc79747f3cd139b93d5cf099258d4a775f486ee8fb29
        A/clauses/window-02/prompt.txt: b066cda0c63f0f8b42ff92175cb7936be59ba43258f640b51f9a49bc0fe1aec6
        A/clauses/window-02/meta.json: 2f773f3c4b6548a80b28562a8b6c3876e4e0aba8a41a484c0118d534afd3dd67
        A/clauses/window-09/raw.json: f9a172cf20e2dd7f35e5f98dd403c512d654bbe02977eb893027a46e19ffe453
        A/clauses/window-09/prompt.txt: 10c424983c392dc446fc6852b90b1f7804397bffb204883afb3ecbb80e617f7c
        A/clauses/window-09/meta.json: aad0c09b162bc8f963ebd4846628d314419cd1a7b213bd42765ffd0915845d25
        A/clauses/window-07/raw.json: 858a11c4cb25517450964187da82f9f89ea31350a7196e9f5795c4e2b0747610
        A/clauses/window-07/prompt.txt: f8a651a2659b5a6f72a40b34ea8cf0e2e9ca447cda8ff151e7f1ed5def80826b
        A/clauses/window-07/meta.json: 3c47d1074864778692bcbf14e3d963adcc7c4da6e79384beca4ccd6fe54c1cbd
        A/clauses/window-01/raw.json: dc05159c6de81d90e6a5c284a7e6fb8f29ce14e99589b6d91fede754d0812381
        A/clauses/window-01/prompt.txt: 724d9ffa53ecfa32fb9140ddee44a5cfd3c46ab1f3582dcb29bcd1df9bc492a6
        A/clauses/window-01/meta.json: fa0f8bf0dd75b5062fc0177285f01befc52cdd2ad09737c5513754785d49da77
        A/clauses/window-06/raw.json: b1ffd3a286d8abe43ca173022c2a169c8c48968bc3701ee05224a032ce576a32
        A/clauses/window-06/prompt.txt: 9ac098a7d8278b7ef0cb4cede2f80757e9f0fb49b2dd6dbe9380b64bd6aa2261
        A/clauses/window-06/meta.json: 85e5c404858c823672ea9fb41b20fb8b4157f3ea42b66c4d71f1c7ba805524ca
        A/clauses/window-08/raw.json: f2cad0e3732a97aefd5fc245aa133f721e8cc86d376355eb485c350a40cc1591
        A/clauses/window-08/prompt.txt: 41cda892cc6b915603b5e67bb1af229fd016f56b5b11cccee18e63ceafef99e8
        A/clauses/window-08/meta.json: 00d2680a4c51db1907e41f75f83bd44f3b41d668eaed5636dc498d13c9780b9d
        A/tables/TABLE-1-page-7-1/raw.json: 417b2fa29a712c0d1f865400f48df055cd2b6dc32fff3337e4cd6e1549f6630b
        A/tables/TABLE-1-page-7-1/prompt.txt: b9efb061101e114f74753b095172cee1c6b81604af788ec753604c5ea43fbc1b
        A/tables/TABLE-1-page-7-1/meta.json: 8d9a6adb6360424a8127786ddc6a8abec6104042b3e68188459f3719c71eddf1
        B/passages.json: b3978e04ea5350f70adb5c97458700690e46e5883da7f379e7d7e7616d3de429
        B/raw.json: 1bd7b225eb27efdcfee8f855a84a2fb134c53fc7cde814ffef37a3af8186dac6
        B/source-units.json: 257d218fca1fe209ed63e6a4e75a24921308670ef09451b64e1823efac635f2a
        B/full-source-units.json: 77f8e2779e378854d1223d8a1529ea6558e6088468f46da8a679b03bd5690c19
        B/meta.json: 4742f032a74bccc864634992948f28d7fb7b99330f86b5f11734a598ecf34756
        B/table-images/TABLE-1-page-7-1.png: f94ebd944d3888871f38ea35682cb7103f6f833cdd1639db9d6175e8b658bb88
        B/table-images/page-7.png: 294bb421cef309e3e8e764f8abcba59f1f6321a6467b3c81bf084c37c122ea17
        B/table-images/manifest.json: 1bcf5d2726745838c0c62c33e3d35465a9c02656195df2e68968ef80cbf6e23f
        B/clauses/window-10/raw.json: 9000aafddba26e0c0e2400392fc0083573585d81dc62126fa1c598afee72eba6
        B/clauses/window-10/prompt.txt: f5f46e10c54584bfd7884045a6a81d2e4dd0d5a0e61c4b9b46a1cad5b21c8478
        B/clauses/window-10/meta.json: 0c5f8a1dc0276a14f306626d2dd6aa74657c36db690b36979f99e4dadf2fb51d
        B/clauses/window-03/raw.json: a3d1aef63183d57f0b45758819672fe037e455d4ac1b9374d7ae70c64e20fdee
        B/clauses/window-03/prompt.txt: 491b1821f8e99b39512acd56c498a72d126e565070aa5197e3681ce3ed81b294
        B/clauses/window-03/meta.json: c0f03e47f4978c792b532f982f9fb93bc093977119ec7a58c8e314fed6174dd4
        B/clauses/window-04/raw.json: 4985243e78e6577efb6d356efb96c86fec98ff95a3198459ea396434fc03a0c0
        B/clauses/window-04/prompt.txt: 0d70c534cc6df773ec41bd170b7804d1f43d0ea6d52a63f245cd15c93eb22480
        B/clauses/window-04/meta.json: 1b495e85be793a64b00b843e6463a5bdabbd08762ca5cb400b720f5f430e22c7
        B/clauses/window-05/raw.json: 887556166f4e333c64b41cda0bd01a3ba1a053b758d9b0b973fb04460b012370
        B/clauses/window-05/prompt.txt: 7480d738d1d3dcf6edb28340025680737e476cbe871782b9ecdd510c94318dad
        B/clauses/window-05/meta.json: a4ecf4faca867a28b6294fe2710b6f21113153f8b2fb5271817a9ebe694f6d15
        B/clauses/window-02/raw.json: 6b9bbf19339f27c1a88ba28180f87736e9bee9c827a1d564362e846a8f294c59
        B/clauses/window-02/prompt.txt: b066cda0c63f0f8b42ff92175cb7936be59ba43258f640b51f9a49bc0fe1aec6
        B/clauses/window-02/meta.json: 59550424d4cc9811d26c22b4c1e7d98b2cabf71ca6a0874c7d1dc7d4db4931ea
        B/clauses/window-09/raw.json: 7620c749fbb05100b7190b28e5374cdfc88d26054c6831c99954f5448bd11be0
        B/clauses/window-09/prompt.txt: 10c424983c392dc446fc6852b90b1f7804397bffb204883afb3ecbb80e617f7c
        B/clauses/window-09/meta.json: 647482bc3ac8c454d842f00259d3aeea701b6400d2f272f8e6abfd07e80edd5a
        B/clauses/window-07/raw.json: 646d2137f7999426b258ca8876c50662d4dea607f05c8f3774f9b1a05de5159b
        B/clauses/window-07/prompt.txt: f8a651a2659b5a6f72a40b34ea8cf0e2e9ca447cda8ff151e7f1ed5def80826b
        B/clauses/window-07/meta.json: 3b7c022ee4d3fead96b70db47f61101e5d7b8d4fea023f648dac791b536c40a3
        B/clauses/window-01/raw.json: 650245aca1b4cffa495a28bbd5d1d0c440f4b7603e1abba745124178dd3c1c13
        B/clauses/window-01/prompt.txt: 724d9ffa53ecfa32fb9140ddee44a5cfd3c46ab1f3582dcb29bcd1df9bc492a6
        B/clauses/window-01/meta.json: 406650d3872bbd4f3d605f6310ecd334245df8a8fd45991651da676f58ca191e
        B/clauses/window-06/raw.json: a92ff217ce2223076cd01c844780274b2a7fb12842410b3a28ecbf7a631db519
        B/clauses/window-06/prompt.txt: 9ac098a7d8278b7ef0cb4cede2f80757e9f0fb49b2dd6dbe9380b64bd6aa2261
        B/clauses/window-06/meta.json: 81ffd25b80eaf74ae007f1ad232d481717a861116e0e6ad21585d1d3e27564f1
        B/clauses/window-08/raw.json: 99e6dde7e19bc9231d76b0f1fe2ecb0362119985c95ee4fd3b225c4cd8da9116
        B/clauses/window-08/prompt.txt: 41cda892cc6b915603b5e67bb1af229fd016f56b5b11cccee18e63ceafef99e8
        B/clauses/window-08/meta.json: 7a42177d295162bea76453df2d71d6ebf93756ce40273147747eaee1f1fd156d
        B/tables/TABLE-1-page-7-1/raw.json: a0c65d90a649e14aa4ee69a6eabe0b3fe1df05cb99a804497c26e37eca6f1484
        B/tables/TABLE-1-page-7-1/prompt.txt: b9efb061101e114f74753b095172cee1c6b81604af788ec753604c5ea43fbc1b
        B/tables/TABLE-1-page-7-1/meta.json: f4929b9ab746a47ee93d095f11d62e597f07759d8832b662f53fbdf4a1c247a0
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
      pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
      source_review: _compare/relationships-2026-11-16/review-current/Jiang2025
      source_status_sha256: aa2dd24c85755f29900644b54281eae4fbc58d3377f8693f19f2c552c34df9b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: auditory speech facilitation (acute phase)
    outcome:
      text: language improvement (subacute to chronic)
    analysis_label: Lesion-independent behavioral correlation (lDLPFC to lPTL)
    relation: association
    evidence_ids:
    - P5-S3-C11
    qualifier_ids:
    - P5-S3-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
      source_review: _compare/relationships-2026-11-16/review-current/Jiang2025
      source_status_sha256: aa2dd24c85755f29900644b54281eae4fbc58d3377f8693f19f2c552c34df9b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Unresolved source passage P1-S1-C13
      - Accounting without a linked unit P5-S2-C2
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C6
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C2
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C5
      - Unaccounted source passage P5-S2-C3
      - Unresolved source passage P5-S4-C3
      - 'window 8: invalid/duplicate disposition P6-S1-C8'
      - Result passage disposed without unit P6-S2-C5
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C12
      - Result passage disposed without unit P7-S1-C13
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C4
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S2-C7
      - Accounting without a linked unit P7-S2-C8
      - Accounting without a linked unit P7-S2-C9
      - Unaccounted source passage P7-S2-C8
      - Unaccounted source passage P7-S2-C9
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C7
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S3-C4
      - Result passage disposed without unit P10-S3-C5
      - Result passage disposed without unit P10-S4-C3
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C11
      - Result passage disposed without unit P11-S1-C9
      unattached_null_or_qualifier_ids:
      - P6-S2-C6
      - P7-S1-C12
      - P7-S2-C7
      - P7-S2-C8
      - P8-S1-C3
      - P8-S2-C8
      - P10-S1-C1
      - P10-S3-C2
      - P11-S1-C9
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 169
      unselected_timing_passages:
      - P8-S3-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S3-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      unlinked_tables:
      - TABLE-1-page-7-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P4-S3
        - P5-S1
        - P5-S2
        - P5-S3
        - P5-S4
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S2
        - P9-S2
        - P10-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
      source_review: _compare/relationships-2026-11-16/review-current/Jiang2025
      source_status_sha256: aa2dd24c85755f29900644b54281eae4fbc58d3377f8693f19f2c552c34df9b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes: []
      reason: General summary of MDN to LN connectivity
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      - 11
      reason: Summary of early facilitation correlating with improvement
    - source_id: P1-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis/general statement
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis/general statement
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Chronic phase reorganization by lesion site
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 2
      - 6
      reason: Subacute phase LN connectivity
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Acute phase rIFG to lIFG facilitation
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Introduction to control results
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Control lDLPFC facilitation
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Control SMA/dACC inhibition
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary table
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Frontal acute rIFG to lIFG
    - source_id: P5-S2-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Comparison to controls
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Frontal acute lDLPFC inhibition
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Frontal subacute lPTL to lIFG
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Frontal chronic lIFG to lPTL
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Frontal chronic rDLPFC facilitation
    - source_id: P5-S2-C11
      disposition: repeated
      result_indexes:
      - 3
      reason: Comparison to other groups
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 4
      reason: TP acute lDLPFC facilitation
    - source_id: P5-S2-C13
      disposition: repeated
      result_indexes:
      - 4
      reason: Comparison to frontal group
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 4
      reason: TP acute rDLPFC facilitation
    - source_id: P5-S2-C15
      disposition: represented
      result_indexes:
      - 5
      reason: TP subacute lPTL to lIFG
    - source_id: P5-S2-C16
      disposition: represented
      result_indexes:
      - 5
      reason: TP subacute rIFG inhibition
    - source_id: P5-S3-C3
      disposition: repeated
      result_indexes:
      - 5
      reason: Comparison to frontal group
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 5
      reason: TP subacute SMA/dACC inhibition
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 6
      reason: TP chronic SMA/dACC facilitation
    - source_id: P5-S3-C6
      disposition: repeated
      result_indexes:
      - 6
      reason: Comparison to other groups
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of analysis method
    - source_id: P5-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of analysis method
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Interaction effect for lIFG to lPTL
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Acute lIFG to lPTL correlation
    - source_id: P5-S3-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Acute lDLPFC to lPTL correlation
    - source_id: P5-S3-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Acute rDLPFC to lPTL correlation
    - source_id: P5-S4-C1
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of rDLPFC to lPTL effect
    - source_id: P5-S4-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Subacute lDLPFC to lIFG correlation
    - source_id: P5-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of analysis method
    - source_id: P5-S4-C4
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Interaction effect of lesion location
    - source_id: P5-S4-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Three-way interaction for SMA/dACC to lPTL
    - source_id: P5-S4-C6
      disposition: represented
      result_indexes:
      - 11
      reason: TP acute SMA/dACC to lPTL correlation
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Interaction effect for rDLPFC to lPTL
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: TP acute rDLPFC to lPTL correlation
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Interaction effect for rIFG to lIFG
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 13
      reason: TP acute rIFG to lIFG correlation
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 14
      reason: Interaction effect for lDLPFC to lIFG
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 14
      reason: TP subacute lDLPFC to lIFG correlation
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for frontal lesions
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 15
      reason: Introduction to change correlations
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 15
      reason: rDLPFC to lPTL change correlation
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 16
      reason: Interaction effect for lDLPFC to lIFG change
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 16
      reason: TP lDLPFC to lIFG change correlation
    - source_id: P6-S2-C1
      disposition: repeated
      result_indexes:
      - 16
      reason: Restatement of lDLPFC to lIFG change
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 16
      reason: TP lDLPFC to lIFG change correlation
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of connectivity patterns
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 17
      reason: Inverse relationship SMA/dACC vs rDLPFC
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of TP chronic SMA/dACC
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of lIFG to lPTL correlation
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of subacute and chronic LN connectivity
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 13
      reason: Restatement of rIFG to lIFG
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S2-C3
      disposition: repeated
      result_indexes:
      - 3
      - 6
      reason: Restatement of chronic phase reorganization
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of LN connectivity
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 1
      - 13
      reason: Restatement of rIFG to lIFG
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of frontal chronic MDN connectivity
    - source_id: P8-S1-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of TP acute MDN connectivity
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S2-C7
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of rDLPFC to lPTL correlation
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P8-S2-C9
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of lIFG to lPTL correlation
    - source_id: P8-S2-C10
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Restatement of DLPFC to lPTL correlations
    - source_id: P8-S2-C11
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of lDLPFC to lIFG correlation
    - source_id: P8-S3-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of lDLPFC to lIFG correlation
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 10
      - 16
      reason: Restatement of decreasing influence of DLPFC
    - source_id: P9-S1-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of frontal chronic rDLPFC
    - source_id: P9-S1-C8
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of TP chronic SMA/dACC
    - source_id: P9-S1-C9
      disposition: repeated
      result_indexes:
      - 17
      reason: Restatement of inverse relationship SMA/dACC vs rDLPFC
    - source_id: P9-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for chronic phase correlations
    - source_id: P9-S2-C8
      disposition: repeated
      result_indexes:
      - 11
      - 12
      reason: Restatement of TP acute MDN correlations
    - source_id: P9-S2-C9
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of TP acute rIFG correlation
    - source_id: P9-S2-C10
      disposition: repeated
      result_indexes:
      - 14
      reason: Restatement of TP subacute lDLPFC correlation
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for acute LN interaction
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of acute lIFG to lPTL correlation
    - source_id: P10-S2-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of acute rIFG to lIFG
    - source_id: P10-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for behavioral association in frontal group
    - source_id: P10-S2-C8
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of TP rIFG to lIFG correlation
    - source_id: P10-S3-C1
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of TP rIFG to lIFG correlation
    - source_id: P10-S3-C2
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of TP rIFG to lIFG correlation
    - source_id: P10-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P10-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for chronic phase correlations
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P11-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    - source_id: P11-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary
    unresolved_coverage:
    - source_id: P1-S1-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P5-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P5-S1-C11
    - P5-S2-C4
    - P5-S2-C6
    - P5-S2-C11
    - P5-S2-C13
    - P5-S3-C3
    - P5-S3-C6
    - P5-S3-C8
    - P5-S3-C9
    - P5-S4-C4
    - P5-S4-C5
    - P6-S1-C1
    - P6-S1-C3
    - P6-S1-C5
    - P6-S1-C7
    - P6-S1-C10
    - P6-S2-C3
    - P6-S2-C5
    - P6-S2-C6
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S1-C13
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C9
    - P8-S1-C1
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C7
    - P8-S1-C8
    - P8-S2-C1
    - P8-S2-C2
    - P8-S2-C7
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C10
    - P8-S2-C11
    - P8-S3-C3
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C5
    - P9-S1-C8
    - P9-S1-C9
    - P9-S2-C5
    - P9-S2-C8
    - P9-S2-C9
    - P9-S2-C10
    - P9-S2-C11
    - P9-S3-C3
    - P10-S1-C1
    - P10-S1-C3
    - P10-S1-C6
    - P10-S1-C7
    - P10-S2-C4
    - P10-S2-C6
    - P10-S2-C8
    - P10-S3-C2
    - P10-S3-C4
    - P10-S3-C5
    - P10-S4-C3
    - P11-S1-C9
    - P11-S1-C10
    - P11-S1-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C11
      - P3-S1-C13
      recruited_sample:
      - P3-S1-C11
      - P3-S1-C13
      eligibility:
      - P3-S1-C11
      imaging_provenance:
      - P3-S3-C9
      - P3-S4-C1
      - P3-S4-C2
      - P3-S4-C3
      - P4-S1-C1
      - P4-S1-C4
      imaging_timing:
      - P1-S1-C10
      - P3-S1-C11
      outcome_timing:
      - P1-S1-C10
      - P3-S1-C11
      outcome_definition:
      - P3-S2-C6
      - P3-S2-C7
      validation: []
      analysis_restrictions:
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C5
      dependent_variable_statement:
      - P4-S2-C12
      - P4-S2-C13
      - P5-S1-C3
      - P5-S3-C7
      limitations:
      - P10-S3-C5
      - P10-S3-C6
      - P10-S3-C7
      - P10-S3-C8
      - P10-S3-C9
      - P10-S3-C10
      - P11-S1-C1
      - P11-S1-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C10
      - P4-S2-C7
      - P4-S2-C9
      - P5-S1-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C11
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S3-C8
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
      pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
      review_sha256: 67cf768b6d25de85286c6c4101332fdf10fbc411c4c6d80b9f300eb04cd4e496
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
      - P5-S3-C11
      source_result: For the connection from lDLPFC to lPTL, greater auditory speech
        processing-induced facilitation in the acute phase was associated with more
        language improvement from the subacute to the chronic phase (β = 0.35, P =
        0.029). This association was reported as independent of lesion location.
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P5-S3-C11 explicitly describes the correlation for the
            lDLPFC to lPTL connection, linking acute phase modulation to subacute-to-chronic
            improvement. The proposed core correctly identifies this specific connection
            and outcome window.
          source_ids:
          - P5-S3-C11
          - P5-S3-C8
        direction:
          answer: fits
          reason: The source states 'greater auditory speech processing-induced facilitation...
            was associated with more language improvement'. The proposed core claims
            'Greater... facilitation... was associated with more language improvement',
            preserving the positive directionality.
          source_ids:
          - P5-S3-C11
        construct:
          answer: fits
          reason: The exposure is correctly identified as the modulatory effect of
            auditory speech on lDLPFC->lPTL connectivity (a DCM parameter). The outcome
            is language improvement (AAT-based). The measurement is functional imaging
            (fMRI/DCM), not diffusion or lesion overlap. The timing (acute predictor,
            subacute-to-chronic outcome) matches the source.
          source_ids:
          - P5-S3-C11
          - P3-S3-C3
          - P3-S2-C5
          - P4-S3-C2
        qualifications:
          answer: fits
          reason: The source P5-S3-C8 states that these correlations are 'independent
            of lesion locations' (no significant interaction with lesion location).
            The proposed core includes the qualification 'The association was found
            to be independent of lesion location.' This is faithful.
          source_ids:
          - P5-S3-C8
          - P5-S3-C11
        missing_material_caveat:
          answer: fits
          reason: The core includes limitations regarding sample size and DCM scope.
            No material caveats that would change the interpretation of this specific
            association are omitted. The 'lesion-independent' status is correctly
            captured as a qualification rather than a standalone finding about lesion
            location effects.
          source_ids:
          - P10-S3-C8
          - P11-S1-C1
      optional_pending:
      - Exact beta coefficient and p-value not transcribed in core fields
      - Specific AAT subtests used for the improvement score not detailed in core
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact beta coefficient and p-value not transcribed in core fields
    - Specific AAT subtests used for the improvement score not detailed in core
    normalizations:
    - field: sample.n
      original: 34
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R009
      exposure:
        text: auditory speech facilitation (acute phase)
      outcome:
        text: language improvement (subacute to chronic)
      analysis_label: Lesion-independent behavioral correlation (lDLPFC to lPTL)
      relation: association
      evidence_ids:
      - P5-S3-C11
      qualifier_ids:
      - P5-S3-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
        source_review: _compare/relationships-2026-11-16/review-current/Jiang2025
        source_status_sha256: aa2dd24c85755f29900644b54281eae4fbc58d3377f8693f19f2c552c34df9b8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e47c2c7a7a307f6310e4f8ca54b3b8784e2df36df9543309430bdc6c4a3d8ea5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C11
          page: 3
          text_layer_sha256: e47c2c7a7a307f6310e4f8ca54b3b8784e2df36df9543309430bdc6c4a3d8ea5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Materials and methods\nParticipants\nTwo groups of patients\
          \ with either frontal (n = 17, mean age 52.3 ±  \n18.9 years, 7 female)\
          \ or temporo-parietal (n = 17, mean age 54.4 ±  \n12.7 years, 2 female)\
          \ first time ischaemic stroke lesions were exam­\nined longitudinally during\
          \ the acute (≤1 week), subacute (1–2 \nweeks) and chronic (>6 months) phases\
          \ after stroke."
        anchor_text: "Materials and methods\nParticipants\nTwo groups of patients\
          \ with either frontal (n = 17, mean age 52.3 ±  \n18.9 years, 7 female)\
          \ or temporo-parietal (n = 17, mean age 54.4 ±  \n12.7 years, 2 female)\
          \ first time ischaemic stroke lesions were exam­\nined longitudinally during\
          \ the acute (≤1 week), subacute (1–2 \nweeks) and chronic (>6 months) phases\
          \ after stroke."
        excluded_fragments: []
        image_sha256: a77e543662fd98594712c4e556fb941d80a28c3a033b74517317557656890646
        transcription: 'Materials and methods

          Participants

          Two groups of patients with either frontal (n = 17, mean age 52.3 ± 18.9
          years, 7 female) or temporo-parietal (n = 17, mean age 54.4 ± 12.7 years,
          2 female) first time ischaemic stroke lesions were examined longitudinally
          during the acute (≤1 week), subacute (1–2 weeks) and chronic (>6 months)
          phases after stroke'
      P1-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6be4337287c15ff51009bf65df5a43b5d5fcbc92912d62e7b746812ecf45c884
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C10
          page: 1
          text_layer_sha256: 6be4337287c15ff51009bf65df5a43b5d5fcbc92912d62e7b746812ecf45c884
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All patients repeatedly underwent \nan auditory sentence comprehension\
          \ paradigm during functional neuroimaging in the acute (≤1 week), subacute\
          \ \n(1–2 weeks) and chronic (>6 months) phases after stroke."
        anchor_text: "All patients repeatedly underwent \nan auditory sentence comprehension\
          \ paradigm during functional neuroimaging in the acute (≤1 week), subacute\
          \ \n(1–2 weeks) and chronic (>6 months) phases after stroke."
        excluded_fragments: []
        image_sha256: 6c759a7e8ac34f087e6b9520877621026501a0ea9137bd6c4e9c9d9b72a7b0e1
        transcription: . All patients repeatedly underwent an auditory sentence comprehension
          paradigm during functional neuroimaging in the acute (≤1 week), subacute
          (1–2 weeks) and chronic (>6 months) phases after stroke
      P10-S3-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dd95168b6e7e3ef4d10eb251727e8ae7df9deeef23cd5666b660df771893589e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8497ede5e8e7d02542d5fdc9d828fae6b536c9d1530569a89b1650c9461855a2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S3-C8
          page: 10
          text_layer_sha256: 8497ede5e8e7d02542d5fdc9d828fae6b536c9d1530569a89b1650c9461855a2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Other factors \nmay also have contributed to the lack of behavioural\
          \ relevance: as \nwe assigned patients to two groups based on their lesion\
          \ sites, there \nwere ultimately only 17 patients in each group."
        anchor_text: "Other factors \nmay also have contributed to the lack of behavioural\
          \ relevance: as \nwe assigned patients to two groups based on their lesion\
          \ sites, there \nwere ultimately only 17 patients in each group."
        excluded_fragments: []
        image_sha256: c6cbfd224b98c646c2101112445b7b208cad9c6910f0356bc4e539d3ea984166
        transcription: '. Other factors

          may also have contributed to the lack of behavioural relevance: as

          we assigned patients to two groups based on their lesion sites, there

          were ultimately only 17 patients in each group'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "For the connection from lDLPFC to lPTL, greater auditory speech \nprocessing-induced\
    \ facilitation in the acute phase was associated \nwith more language improvement\
    \ from the subacute to the chronic \nphase (β = 0.35, P = 0.029) (Fig. 3B)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
