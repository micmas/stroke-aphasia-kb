---
id: stroke_incident_dementia
name: stroke
kind: predictor
findings:
- id: f1
  target: incident_dementia
  target_kind: prognosis
  claim: Patients with stroke have an increased risk of incident dementia compared
    to controls, with a risk increase of up to 9-fold in the first year after stroke,
    and a continued excess incidence in following years.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: not_reported
    population: patients with symptomatic stroke and controls
    phase: not_reported
    time_post_onset: first year and following years post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - pooled estimates of risk factors may not include all studies due to inconsistent
    reporting of variables across cohorts
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: occurrence of symptomatic stroke. hazard ratios in
    following years were around four in hospital-based studies and around two in population-based
    studies. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S1-C5, two-model agreement, human
    verification pending): Studies were included if they: were on patients with symptomatic
    stroke; were published in English; reported on a series of consecutive eligible
    patients (with an inclusion rate of at least 50%, allowing for exclusions owing
    to aphasia, visual or hearing impairment, language barriers, and early mortality)
    or volunteers in prospective cohort studies; included all stroke or all ischaemic
    stroke (studies restricted to other particular stroke subtypes were excluded);
    and gave dementia measured by standard criteria, such as diagnostic and statistical
    manual of mental disorders IV (DSM IV), international classification of disease-10
    (ICD-10), or a mini-mental state examination (MMSE) score of less than 24 as an
    outcome Original text-layer quotation is preserved below.'
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
    - proposed_concept:incident_dementia
  citation: '@Pendlebury2009'
  source_passages:
  - section: Original source P6-S2-C8
    page: 6
    quote: "Results of studies that compare the incidence of new \ndementia in patients\
      \ with stroke versus controls reported \nup to a 9-fold increased risk in patients\
      \ with stroke in the \nﬁ rst year after stroke,36,42,82 and the excess incidence,\
      \ \nalthough lower, continued in the following years, with \nhazard ratios of\
      \ around four32,36,42 in hospital-based studies \nand around two in population-based\
      \ studies82,83–86 after the \n"
    supports: claim
  - section: Original source P6-S3-C1
    page: 6
    quote: "although lower, continued in the following years, with \nhazard ratios\
      \ of around four32,36,42 in hospital-based studies \nand around two in population-based\
      \ studies82,83–86 after the \nﬁ rst year post-stroke."
    supports: claim
  - section: Original source P1-S1-C8
    page: 1
    quote: "Findings We identiﬁ ed 22 hospital-based and eight population-based eligible\
      \ cohorts (7511 patients) described in \n73 papers."
    supports: sample
  - section: Original source P2-S1-C5
    page: 2
    quote: "Studies were included if they: were on patients with \nsymptomatic stroke;\
      \ were published in English; reported \non a series of consecutive eligible\
      \ patients (with an \ninclusion rate of at least 50%, allowing for exclusions\
      \ \nowing to aphasia, visual or hearing impairment, language \nbarriers, and\
      \ early mortality) or volunteers in prospective \ncohort studies; included all\
      \ stroke or all ischaemic stroke \n(studies restricted to other particular stroke\
      \ subtypes were \nexcluded); and gave dementia measured by standard \ncriteria,\
      \ such as diagnostic and statistical manual of \nmental disorders IV (DSM IV),\
      \ international classiﬁ cation \nof disease-10 (ICD-10), or a mini-mental state\
      \ examination \n(MMSE) score of less than 24 as an outcome."
    supports: method
predictor_type: clinical
short_definition: occurrence of symptomatic stroke
assessment:
- DSM-IV
- ICD-10
- MMSE
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pendlebury2009
  proposal_id: R010
  review_status_sha256: 1526f5d1df555b0bf1916477ccaa35a8fb115a2697cab63cb15296ae329295e8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
        A/passages.json: 8e3f0b5b486265d6497f4bf83de4c8ffc69bb081a3ebe5cf67f772a432a0b295
        A/raw.json: 12eec75942ab9010d46f526a7f18564f5af8d223ebc7dff67c44d01b698fadd7
        A/source-units.json: 8156c3590e31fd7ad6631b6498f4cb0cc00c59151793b83ebb0543ed8e682a3c
        A/full-source-units.json: b160454be088cf1d0a8f103e579d9459d2844209cba90e3c4393018f2bc9f1fc
        A/meta.json: f235b46a03ac88e99120120e9bcfad5509e669b9258a3e155545e74b887c0ff2
        A/table-images/TABLE-5-page-9-1.png: 5d34051a1caf71d61517a045c92252fe7945cb38f0b51dbeee0d22d856026195
        A/table-images/TABLE-4-page-8-1.png: 49435b2a3e8927271804fbb3252db584054627971861fae6d53c7569be9782aa
        A/table-images/page-5.png: 92244e84909a87a95e34d8ed6732b2562be90cb46f71b767f579be40da340b6e
        A/table-images/page-4.png: 609fa03d8aad74236c303df299f2caf64405e5f6c1ade5529916bf8fba721f71
        A/table-images/TABLE-1-page-4-1.png: a0584b1679b7de2949d7757b4b79297933b5d69048a4d57b5a54598d046493e1
        A/table-images/page-9.png: 3fa758c9b956ed92fc8dd2f6997b21060fecc507996e9e566f990ecb8f6dc7eb
        A/table-images/page-8.png: 144f114ebc515314c51a2b7e243c976efb40ebffd6d800900a029bd846f58519
        A/table-images/manifest.json: b9a1a211ec2a3013a6e94da9c019fc94ba81759b693659472372779f0544d4d2
        A/table-images/TABLE-3-page-5-2.png: fae319f62b1fff32fa78f8c3f7c371dace69b56d2cc15e0431a7b692fbdf5938
        A/table-images/TABLE-2-page-5-1.png: 6b1280c54b29c48e09e188d1b0356acdbfe64d16cea7d9589a95ec262035cf25
        A/clauses/window-03/raw.json: 7e5777a98f3c4097a642e18a31029d8ad27ad20ca7e507ec862ed993d469ef13
        A/clauses/window-03/prompt.txt: f32d06440c84d94f795298174390b5a36e38d32e2c25cccf4ad8ab049fef0802
        A/clauses/window-03/meta.json: 25a6072904b03e3166810dc1c2ad1d2a586af7f0903899a9275810eb7d3b585d
        A/clauses/window-04/raw.json: b798685a579de674bd2f3dc008354be875c6cd8b831a61b8692505042610f4af
        A/clauses/window-04/prompt.txt: 45d3399f2c6c03ab04a368f9e6399a98555edcd1201878ce330a0c29b957134a
        A/clauses/window-04/meta.json: e874da2748533c958e537982b6b0e7899b25e5b009349ebbba9d19fcba1b7e19
        A/clauses/window-05/raw.json: 5383b86b82dcceed5b73a2a49c3f0be25618cb21783dcaa7374ca02fca54e803
        A/clauses/window-05/prompt.txt: 01046958b03c9bdf8b72c194aad0d35b63e56c1dd346c7b497dc4451cf97cd33
        A/clauses/window-05/meta.json: 3ff7c1daef49cd9c1a83673f50c6ec5d8f452efbf11eff318cb17f1e072c7758
        A/clauses/window-02/raw.json: 8462d75bf02890b48a549c85fdb6ce8bddc7bd76de04110b2f7ebd88448b9faf
        A/clauses/window-02/prompt.txt: 87a61660cd942501068533923272b07b7d6f4a7f7bb7c563cacbf16b5547ef07
        A/clauses/window-02/meta.json: 83e625eb6c0b3005454ad0c5c07f407e290fa1707560680c89a832372d29b3c1
        A/clauses/window-07/raw.json: 1964b879eb0f2e47faeb6b344fc3257b783451a889f5e5b79860bccf135b54ab
        A/clauses/window-07/prompt.txt: ec1c3d9cd4e84765e29fbe034380424b8a31d9177f9c5449d2ee8713fbf43420
        A/clauses/window-07/meta.json: ab13ad4471bb247da7f0ffea71040bdaad9e77ed37fc33230e8d08f783d80bf5
        A/clauses/window-01/raw.json: c4e2d77e50fd1c6bbcbf01abffc29f0276fedd836b454f11da5cf7a6f9cbf406
        A/clauses/window-01/prompt.txt: 27900eeab33d263252a37f67d489c4f09c2fa2f79861d8609c98868d508b30fb
        A/clauses/window-01/meta.json: e5f0e8f5b6f8fdfe977689d8f2e02c8f454619768b896082262ad567c2084e46
        A/clauses/window-06/raw.json: 9db79f172b7ab371b1e5c54dd58466b17ca8ba4acf092768c2001a7364de95c7
        A/clauses/window-06/prompt.txt: a163f3d79db7779de4e70bb054b3a15791a79844b7f5610894fff4f998dad84d
        A/clauses/window-06/meta.json: c2c0d8d6bc45e6f2e768d2b1b2ee514c8ee94d7ab6c4ec837d6a9348907aeccc
        A/tables/TABLE-4-page-8-4/raw.json: 3551340e8b72c1e2c1730b5e0b4ffa98bf80e8f1610a38297878ed4eea1ca3d7
        A/tables/TABLE-4-page-8-4/prompt.txt: 944d2f8303ba533f96ed938fc0c105729f5cce87f2e44d7e3829e062c2c4a101
        A/tables/TABLE-4-page-8-4/meta.json: 77c30a58e0285bea517e8b4f6e85209a34c09c64aef3809281f925186c57b78a
        A/tables/TABLE-3-page-5-3/raw.json: c69ae154369e8e9f30b601d7249123c7c9ff354e6ff71ebc0fa13067ad7361bc
        A/tables/TABLE-3-page-5-3/prompt.txt: b277a48fca777cc21a97abd4205d70d1a99d385a79db70b61ba21208ab79c231
        A/tables/TABLE-3-page-5-3/meta.json: 5f20cd604fda1418594fb55a136a3853e60ae3d05f551f39b2b13e9466b67e83
        A/tables/TABLE-2-page-5-2/raw.json: a2dc56d7c7ac078e6a5d5dba77fe18f4a1e7904046dea8ff2102bcf82e068525
        A/tables/TABLE-2-page-5-2/prompt.txt: 4fdb160721dc187ac834057dba49f43b00e41a1f38dd177c4300d9a11bb9255e
        A/tables/TABLE-2-page-5-2/meta.json: 69b3b69dbff20de80283d1e0bfbc6bd4200b5ed74f0adaed39aa891c3a67c139
        A/tables/TABLE-5-page-9-5/raw.json: 9d4c8e7fe79f16a495835006b08b2a258ef60d219ae477bd2408880185bb11f8
        A/tables/TABLE-5-page-9-5/prompt.txt: 1f26aa976eda3f595ff49f190308c353967a57f1e2a3bd40f098aa792f2397bc
        A/tables/TABLE-5-page-9-5/meta.json: fe7f17ea3d790e1b8f416acbec903cb9147a3e73c7d0141a0aa248cf8d68cc62
        A/tables/TABLE-1-page-4-1/raw.json: 13a7156f4db81f6a9708995b3c82b2a35464429249fb2a469554678cee98e445
        A/tables/TABLE-1-page-4-1/prompt.txt: f972999742a4a9b41a7fdb7a0a8967855dd600034766affda7b346f02bd67276
        A/tables/TABLE-1-page-4-1/meta.json: fbc58412d27cbf0bbd2e4e7610f51c8f1ee808b04e9c842ea609b9bb5a629081
        B/passages.json: 8e3f0b5b486265d6497f4bf83de4c8ffc69bb081a3ebe5cf67f772a432a0b295
        B/raw.json: 9d592c356cc3fa03789b5d68748b7b99b0492dbe018c7b5b0a18fea297a21402
        B/source-units.json: 8156c3590e31fd7ad6631b6498f4cb0cc00c59151793b83ebb0543ed8e682a3c
        B/full-source-units.json: b160454be088cf1d0a8f103e579d9459d2844209cba90e3c4393018f2bc9f1fc
        B/meta.json: 5384c29baa639ef478b69dd5096d8685138566012dfcf7fa36737ae835376423
        B/table-images/TABLE-5-page-9-1.png: 5d34051a1caf71d61517a045c92252fe7945cb38f0b51dbeee0d22d856026195
        B/table-images/TABLE-4-page-8-1.png: 49435b2a3e8927271804fbb3252db584054627971861fae6d53c7569be9782aa
        B/table-images/page-5.png: 92244e84909a87a95e34d8ed6732b2562be90cb46f71b767f579be40da340b6e
        B/table-images/page-4.png: 609fa03d8aad74236c303df299f2caf64405e5f6c1ade5529916bf8fba721f71
        B/table-images/TABLE-1-page-4-1.png: a0584b1679b7de2949d7757b4b79297933b5d69048a4d57b5a54598d046493e1
        B/table-images/page-9.png: 3fa758c9b956ed92fc8dd2f6997b21060fecc507996e9e566f990ecb8f6dc7eb
        B/table-images/page-8.png: 144f114ebc515314c51a2b7e243c976efb40ebffd6d800900a029bd846f58519
        B/table-images/manifest.json: 9de7c5e6fa5f60c157bd0d775ae913725c4dcfe583ec1d4f3355f417a4cba3af
        B/table-images/TABLE-3-page-5-2.png: fae319f62b1fff32fa78f8c3f7c371dace69b56d2cc15e0431a7b692fbdf5938
        B/table-images/TABLE-2-page-5-1.png: 6b1280c54b29c48e09e188d1b0356acdbfe64d16cea7d9589a95ec262035cf25
        B/clauses/window-03/raw.json: c96e9d474866394d8496bd2a39e0517c2dfcbd156547cd42eb2a4730aa2c41a0
        B/clauses/window-03/prompt.txt: f32d06440c84d94f795298174390b5a36e38d32e2c25cccf4ad8ab049fef0802
        B/clauses/window-03/meta.json: bc7b0cc51ad5c1a1be49ba10348d434f2d7918d0814160720d36c3e98f2d3bd1
        B/clauses/window-04/raw.json: 508be6c55617e00c0eef3c6f56ae1475925ae11d7e719d6dd45c214627aab99c
        B/clauses/window-04/prompt.txt: 45d3399f2c6c03ab04a368f9e6399a98555edcd1201878ce330a0c29b957134a
        B/clauses/window-04/meta.json: 64ae3b8bb5e6fc07d4ab4cd904c02414e74c31e9efa4c5ccd43cf0a9c19e8631
        B/clauses/window-05/raw.json: a9da0919b9ae70734e74f7ba42f8fd4ff63a3586e3f99d51872ea1f1bf3d1cfa
        B/clauses/window-05/prompt.txt: 01046958b03c9bdf8b72c194aad0d35b63e56c1dd346c7b497dc4451cf97cd33
        B/clauses/window-05/meta.json: 8afcf7280e6dad3218fa801c31a59802ad96c3e00e0bbbc59fd7cf43fc95aa12
        B/clauses/window-02/raw.json: 07be80b408e57be53ba3becb77632b9521423428aaa2e90efa72c0a034df1d4c
        B/clauses/window-02/prompt.txt: 87a61660cd942501068533923272b07b7d6f4a7f7bb7c563cacbf16b5547ef07
        B/clauses/window-02/meta.json: f8495e48855bf46a720ed400064abb87676dd736a9cfda5c9687de79fa66bb96
        B/clauses/window-07/raw.json: 7d30bd9d49c59e6b78a5ace45247b96804d6639cd083dab641cf6bd0f9f40315
        B/clauses/window-07/prompt.txt: ec1c3d9cd4e84765e29fbe034380424b8a31d9177f9c5449d2ee8713fbf43420
        B/clauses/window-07/meta.json: 77c447218989af838d6538940bdf913fd71921983f9f65e4cd681c2cc22c2148
        B/clauses/window-01/raw.json: 135b19adfbeba42e10955d707a6a30daabc0b3142982dedf69ecc229193d46a9
        B/clauses/window-01/prompt.txt: 27900eeab33d263252a37f67d489c4f09c2fa2f79861d8609c98868d508b30fb
        B/clauses/window-01/meta.json: 482542f55dc6634f8803b09a9ef7d8331d5f63049d8f37852dc2fae0eade2577
        B/clauses/window-06/raw.json: 0c7425df41f1cbf94c8c7321967eddf9b714065829df83f449455baeeb257530
        B/clauses/window-06/prompt.txt: a163f3d79db7779de4e70bb054b3a15791a79844b7f5610894fff4f998dad84d
        B/clauses/window-06/meta.json: 9ed5b11d7c69bcf13f24f3783e1e7bdf576c5a8ceb28fd2edd707d80d7785b9e
        B/tables/TABLE-4-page-8-4/raw.json: 98e270dcc1ee95e35bfddae8e113e51ec0a8787a80c4094e45603efe5b457611
        B/tables/TABLE-4-page-8-4/prompt.txt: 944d2f8303ba533f96ed938fc0c105729f5cce87f2e44d7e3829e062c2c4a101
        B/tables/TABLE-4-page-8-4/meta.json: f7e467358b4e1faff8548dac2c59032d7d42b6e2ff204bc125e4bacef325aa91
        B/tables/TABLE-3-page-5-3/raw.json: 0a11fc35cc64363af0cde7d8f9d8e515d213521cd6afafcf797f5a9f2818c39d
        B/tables/TABLE-3-page-5-3/prompt.txt: b277a48fca777cc21a97abd4205d70d1a99d385a79db70b61ba21208ab79c231
        B/tables/TABLE-3-page-5-3/meta.json: 26016bdfc9aae75aa3068e90a8904f8b73dc7cd7658544e94070a7a8769efb3f
        B/tables/TABLE-2-page-5-2/raw.json: 4cc236783f5644445bb34177f39234b0c46043439b190585cc4964f5475afbb1
        B/tables/TABLE-2-page-5-2/prompt.txt: 4fdb160721dc187ac834057dba49f43b00e41a1f38dd177c4300d9a11bb9255e
        B/tables/TABLE-2-page-5-2/meta.json: d37450ee9c86cbc8c730bf6b358f9fd4de164070b2e9df01e0bfb92f9e036e05
        B/tables/TABLE-5-page-9-5/raw.json: 9d4c8e7fe79f16a495835006b08b2a258ef60d219ae477bd2408880185bb11f8
        B/tables/TABLE-5-page-9-5/prompt.txt: 1f26aa976eda3f595ff49f190308c353967a57f1e2a3bd40f098aa792f2397bc
        B/tables/TABLE-5-page-9-5/meta.json: af2cecf43c564b7e184688e6052a0f7093659502f3f5ea9cd53aed9c712859e3
        B/tables/TABLE-1-page-4-1/raw.json: d809b77e2d2e545149fea75e68a81d10a74f3f68dda2c9ede6b91edb2d03957a
        B/tables/TABLE-1-page-4-1/prompt.txt: f972999742a4a9b41a7fdb7a0a8967855dd600034766affda7b346f02bd67276
        B/tables/TABLE-1-page-4-1/meta.json: 38b3fd6268b329b368f128dd2fee3fd40c47c09f119f8e9cb23ca60c91bfc5f2
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
      pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
      source_review: _compare/relationships-2026-11-16/review-current/Pendlebury2009
      source_status_sha256: b485cbe1fbc03e4f219a50ace22bfaa5c8a57c406deb1b9aed8ea309e5a60e72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: stroke
    outcome:
      text: incident dementia
    analysis_label: Incidence of dementia in stroke vs controls
    relation: association
    evidence_ids:
    - P6-S2-C8
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
      pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
      source_review: _compare/relationships-2026-11-16/review-current/Pendlebury2009
      source_status_sha256: b485cbe1fbc03e4f219a50ace22bfaa5c8a57c406deb1b9aed8ea309e5a60e72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S1-C9
      - Accounting without a linked unit P5-S2-C2
      - Unaccounted source passage P5-S2-C2
      - Accounting without a linked unit P6-S3-C5
      - Accounting without a linked unit P6-S3-C6
      - Accounting without a linked unit P6-S3-C7
      - Accounting without a linked unit P7-S1-C1
      - Accounting without a linked unit P7-S2-C7
      - Unaccounted source passage P6-S3-C5
      - Unaccounted source passage P7-S1-C1
      - Unaccounted source passage P6-S3-C6
      - Unaccounted source passage P7-S2-C7
      - Unaccounted source passage P6-S3-C7
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P9-S1-C1
      - Window 8 reached the unit cap; completeness requires inspection
      - Accounting without a linked unit P9-S1-C5
      - Accounting without a linked unit P9-S2-C4
      - Accounting without a linked unit P9-S2-C6
      - Accounting without a linked unit P9-S2-C7
      - Accounting without a linked unit P9-S2-C8
      - Unaccounted source passage P9-S2-C6
      - Unaccounted source passage P9-S2-C8
      - Unaccounted source passage P9-S1-C5
      - Unaccounted source passage P9-S2-C4
      - Unaccounted source passage P9-S2-C7
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C5
      - Accounting without a linked unit P10-S1-C7
      - Accounting without a linked unit P10-S1-C8
      - Accounting without a linked unit P10-S1-C9
      - Accounting without a linked unit P9-S2-C9
      - Unaccounted source passage P10-S1-C9
      - Unaccounted source passage P9-S2-C9
      - Unaccounted source passage P10-S1-C7
      - Unaccounted source passage P10-S1-C8
      - Result passage disposed without unit P10-S2-C2
      - Accounting without a linked unit P10-S2-C3
      - Result passage disposed without unit P10-S2-C7
      - Result passage disposed without unit P10-S3-C1
      - Accounting without a linked unit P10-S3-C2
      - Unaccounted source passage P10-S3-C2
      - Unaccounted source passage P10-S2-C3
      - Result passage disposed without unit P10-S3-C10
      - Result passage disposed without unit P10-S3-C7
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      unattached_null_or_qualifier_ids:
      - P3-S2-C4
      - P3-S3-C2
      - P5-S1-C4
      - P5-S1-C5
      - P5-S2-C1
      - P9-S2-C4
      - P10-S1-C1
      - P10-S1-C5
      - P10-S2-C3
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 112
      unselected_timing_passages:
      - P1-S1-C5
      - P2-S1-C6
      - P2-S2-C2
      - P3-S1-C10
      - P3-S2-C1
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C6
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
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P3-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S3-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S2-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S3-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: recruited_sample
        source_ids:
        - P1-S1-C4
        - P2-S1-C3
        - P2-S1-C4
        - P2-S1-C5
        - P2-S2-C2
        - P2-S2-C5
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P3-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P1-S1-C5
        - P2-S1-C5
        - P2-S1-C6
        - P2-S2-C2
        - P2-S2-C3
        - P2-S2-C5
        - P2-S2-C6
        - P2-S2-C7
        - P3-S1-C10
        - P3-S2-C1
        - P3-S2-C2
        - P3-S2-C3
        - P3-S2-C4
        - P4-S2-C1
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P5-S2-C1
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C5
        - P5-S2-C6
        - P6-S1-C5
        - P6-S1-C6
        - P7-S1-C4
        - P7-S2-C1
        - P7-S2-C7
        - P8-S2-C1
        - P8-S2-C2
        - P9-S1-C6
        - P10-S1-C6
        - P10-S2-C2
        - P10-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P1-S1-C5
        - P2-S1-C6
        - P2-S3-C5
        - P5-S2-C1
        - P5-S2-C2
        - P6-S1-C4
        - P6-S1-C5
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C6
        - P9-S1-C3
        - P9-S1-C5
        - P10-S1-C2
        - P10-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C5
        - P2-S1-C5
        - P2-S3-C3
        - P5-S1-C3
        - P5-S1-C6
        - P6-S1-C4
        - P6-S2-C2
        - P6-S2-C3
        - P9-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P10-S3-C4
        - P10-S3-C5
        - P10-S3-C6
        - P10-S3-C8
        - P10-S3-C9
        - P10-S3-C10
        - P10-S3-C11
        - P11-S1-C1
        - P11-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P1-S2-C3
        - P3-S1-C5
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P7-S1-C2
        - P8-S1-C1
        - P8-S1-C2
        - P8-S3-C6
        - P9-S2-C9
        - P9-S3-C6
        - P10-S1-C7
        - P10-S1-C9
        - P10-S2-C1
        - P10-S2-C3
        - P10-S3-C2
        - P10-S3-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P1-S2-C3
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P7-S1-C2
        - P8-S1-C1
        - P8-S1-C2
        - P10-S1-C7
        - P10-S1-C9
        - P10-S2-C3
        - P10-S3-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - recruited_sample
      - eligibility
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P9-S2-C9
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-5-3
      - TABLE-4-page-8-4
      - TABLE-5-page-9-5
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P6-S2
        - P6-S3
        - P7-S2
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
      source_review: _compare/relationships-2026-11-16/review-current/Pendlebury2009
      source_status_sha256: b485cbe1fbc03e4f219a50ace22bfaa5c8a57c406deb1b9aed8ea309e5a60e72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohort sizes and number of papers.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Provides pooled prevalence of pre-stroke dementia by setting.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      - 8
      reason: Reports variance explanation and prevalence range for post-stroke dementia.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports cumulative incidence of dementia after first year.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Identifies associations for pre- and post-stroke dementia.
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of prevalence findings in interpretation.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of eligible articles.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes hand-searching process.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes total eligible articles.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohort types and patient counts.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes MMSE data reporting.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes depression screening rates.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes depression questionnaires used.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ethnic origin of patients in specific studies.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes estimated ethnic distribution.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data availability and methods for pre-stroke dementia.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes assessment timing for population-based studies.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes heterogeneity of pre-stroke dementia estimates.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variance accounted for by timing and setting.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Provides pooled prevalence of pre-stroke dementia by setting.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-stroke dementia rates in patients reaching follow-up.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variation in post-stroke dementia rates.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: States heterogeneity reduction via stratification.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Quantifies variance explained by study factors.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Qualifies variance explained by diagnostic method.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports highest and lowest post-stroke dementia rates.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of post-stroke dementia rates by recurrence and setting.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports MMSE scores in one hospital study.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports MMSE prevalence rates in population studies.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Reports linear increase in dementia incidence per year.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports lower incidence in population-based studies.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Reports increased risk of dementia in stroke vs controls.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Lists significant predictors of pre-stroke dementia.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Provides prevalence data in Figure 3.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Lists demographic and vascular predictors of post-stroke dementia.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Lists stroke-related predictors of post-stroke dementia.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports loss of significance for haemorrhagic stroke and silent infarcts
        after excluding pre-stroke dementia.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Table 4 provides ORs for pre-stroke dementia factors.
    - source_id: P9-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of post-stroke dementia prevalence range.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports pooled rate of pre-stroke dementia by setting.
    - source_id: P9-S3-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Table 5 provides ORs for post-stroke dementia factors.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies independent predictors in multivariate analysis.
    - source_id: P10-S2-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Compares strength of predictors between pre- and post-stroke dementia.
    unresolved_coverage:
    - source_id: P7-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P3-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C2
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
    pending_source_ids:
    - P1-S1-C8
    - P1-S2-C4
    - P3-S1-C7
    - P3-S1-C8
    - P3-S1-C9
    - P3-S2-C3
    - P3-S2-C4
    - P3-S3-C2
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S2-C1
    - P5-S2-C2
    - P6-S1-C1
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C7
    - P6-S1-C9
    - P6-S2-C2
    - P6-S2-C3
    - P6-S3-C1
    - P6-S3-C2
    - P7-S1-C1
    - P7-S2-C7
    - P8-S2-C1
    - P8-S2-C4
    - P8-S2-C5
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S2-C2
    - P9-S2-C3
    - P9-S2-C7
    - P9-S2-C8
    - P10-S1-C1
    - P10-S1-C2
    - P10-S1-C5
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S2-C1
    - P10-S2-C2
    - P10-S2-C7
    - P10-S3-C1
    - P10-S3-C2
    - P10-S3-C7
    - P10-S3-C10
    - P11-S1-C2
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-5-3
    - TABLE-4-page-8-4
    - TABLE-5-page-9-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C8
      - P3-S2-C3
      recruited_sample: []
      eligibility: []
      imaging_provenance:
      - P3-S1-C5
      - P8-S3-C10
      - P10-S1-C7
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P2-S2-C6
      - P2-S2-C7
      - P3-S2-C2
      - P3-S2-C4
      - P8-S2-C1
      - P8-S2-C2
      - P10-S2-C6
      dependent_variable_statement:
      - P1-S1-C7
      - P2-S2-C9
      - P2-S3-C7
      - P2-S3-C9
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C1
      - P3-S1-C5
      - P10-S2-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C4
      - P5-S1-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C6
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
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P3-S1-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S3-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S2-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S3-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: recruited_sample
      source_ids:
      - P1-S1-C4
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C5
      - P2-S2-C2
      - P2-S2-C5
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S1-C5
      - P2-S1-C5
      - P2-S1-C6
      - P2-S2-C2
      - P2-S2-C3
      - P2-S2-C5
      - P2-S2-C6
      - P2-S2-C7
      - P3-S1-C10
      - P3-S2-C1
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P4-S2-C1
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S2-C1
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
      - P6-S1-C5
      - P6-S1-C6
      - P7-S1-C4
      - P7-S2-C1
      - P7-S2-C7
      - P8-S2-C1
      - P8-S2-C2
      - P9-S1-C6
      - P10-S1-C6
      - P10-S2-C2
      - P10-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P1-S1-C5
      - P2-S1-C6
      - P2-S3-C5
      - P5-S2-C1
      - P5-S2-C2
      - P6-S1-C4
      - P6-S1-C5
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P9-S1-C3
      - P9-S1-C5
      - P10-S1-C2
      - P10-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C5
      - P2-S1-C5
      - P2-S3-C3
      - P5-S1-C3
      - P5-S1-C6
      - P6-S1-C4
      - P6-S2-C2
      - P6-S2-C3
      - P9-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P10-S3-C4
      - P10-S3-C5
      - P10-S3-C6
      - P10-S3-C8
      - P10-S3-C9
      - P10-S3-C10
      - P10-S3-C11
      - P11-S1-C1
      - P11-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P1-S2-C3
      - P3-S1-C5
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P7-S1-C2
      - P8-S1-C1
      - P8-S1-C2
      - P8-S3-C6
      - P9-S2-C9
      - P9-S3-C6
      - P10-S1-C7
      - P10-S1-C9
      - P10-S2-C1
      - P10-S2-C3
      - P10-S3-C2
      - P10-S3-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P1-S2-C3
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P7-S1-C2
      - P8-S1-C1
      - P8-S1-C2
      - P10-S1-C7
      - P10-S1-C9
      - P10-S2-C3
      - P10-S3-C2
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
      pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
      review_sha256: 1526f5d1df555b0bf1916477ccaa35a8fb115a2697cab63cb15296ae329295e8
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
      - P6-S2-C8
      source_result: Studies comparing the incidence of new dementia in patients with
        stroke versus controls reported up to a 9-fold increased risk in the first
        year after stroke, with continued excess incidence in subsequent years (hazard
        ratios ~4 in hospital-based, ~2 in population-based studies).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P6-S2-C8) explicitly describes the comparison of incidence
            of new dementia in stroke patients versus controls, which matches the
            selected analysis label and the proposed core's focus on the association
            between stroke and incident dementia.
          source_ids:
          - P6-S2-C8
        direction:
          answer: fits
          reason: The source states a '9-fold increased risk' and 'excess incidence',
            which aligns with the proposed core's claim of 'increased risk' and direction
            'likely'.
          source_ids:
          - P6-S2-C8
        construct:
          answer: fits
          reason: The exposure is 'stroke' (symptomatic stroke per P1-S1-C5) and the
            outcome is 'incident dementia' (new dementia, excluding pre-stroke dementia
            per P2-S3-C9). The measurement is non-imaging (clinical criteria like
            DSM/ICD/MMSE per P2-S1-C5), not diffusion or template overlap.
          source_ids:
          - P1-S1-C5
          - P6-S2-C8
        qualifications:
          answer: fits
          reason: The proposed core includes the specific hazard ratios for hospital-based
            (~4) and population-based (~2) studies in subsequent years, which are
            explicitly stated in P6-S2-C8 and P6-S3-C1. The timing (first year and
            following years) is also correctly captured.
          source_ids:
          - P6-S2-C8
          - P6-S3-C1
        missing_material_caveat:
          answer: fits
          reason: The core captures the main findings and relevant stratifications.
            While P10-S3-C8 notes that not all studies could be pooled for every factor,
            this is a general limitation of the meta-analysis rather than a specific
            caveat that changes the interpretation of the stroke-dementia incidence
            association itself. The core correctly identifies the association as a
            meta-analytic finding.
          source_ids:
          - P10-S3-C8
      optional_pending:
      - Specific sample sizes for the individual studies contributing to the 9-fold
        risk estimate are not transcribed in the provided source window.
      - Exact confidence intervals for the 9-fold risk estimate are not transcribed
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
    - Specific sample sizes for the individual studies contributing to the 9-fold
      risk estimate are not transcribed in the provided source window.
    - Exact confidence intervals for the 9-fold risk estimate are not transcribed
      in the provided source window.
    normalizations:
    - field: sample.n
      original: 7511
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R010
      exposure:
        text: stroke
      outcome:
        text: incident dementia
      analysis_label: Incidence of dementia in stroke vs controls
      relation: association
      evidence_ids:
      - P6-S2-C8
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
        pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
        source_review: _compare/relationships-2026-11-16/review-current/Pendlebury2009
        source_status_sha256: b485cbe1fbc03e4f219a50ace22bfaa5c8a57c406deb1b9aed8ea309e5a60e72
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c571df8046bf3ac8ab7881eb79f7783b7497723270a701ee076d5df6f12a986f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C8
          page: 1
          text_layer_sha256: c571df8046bf3ac8ab7881eb79f7783b7497723270a701ee076d5df6f12a986f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Findings We identiﬁ ed 22 hospital-based and eight population-based\
          \ eligible cohorts (7511 patients) described in \n73 papers."
        anchor_text: "Findings We identiﬁ ed 22 hospital-based and eight population-based\
          \ eligible cohorts (7511 patients) described in \n73 papers."
        excluded_fragments: []
        image_sha256: 4c20c3d37153c6f4943f5a574392fc71e131d1c64b3a964833ce6790918d28d0
      P2-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bebdd6b9671abd532e33c53a26ac50cc98921c48d6ec85cacaf6cb8735d72e8d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a6a19ae157808e6a6d3b2f5250177eb2bc98785cbb13e822aecaeebb09eba91d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C5
          page: 2
          text_layer_sha256: a6a19ae157808e6a6d3b2f5250177eb2bc98785cbb13e822aecaeebb09eba91d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Studies were included if they: were on patients with \nsymptomatic\
          \ stroke; were published in English; reported \non a series of consecutive\
          \ eligible patients (with an \ninclusion rate of at least 50%, allowing\
          \ for exclusions \nowing to aphasia, visual or hearing impairment, language\
          \ \nbarriers, and early mortality) or volunteers in prospective \ncohort\
          \ studies; included all stroke or all ischaemic stroke \n(studies restricted\
          \ to other particular stroke subtypes were \nexcluded); and gave dementia\
          \ measured by standard \ncriteria, such as diagnostic and statistical manual\
          \ of \nmental disorders IV (DSM IV), international classiﬁ cation \nof disease-10\
          \ (ICD-10), or a mini-mental state examination \n(MMSE) score of less than\
          \ 24 as an outcome."
        anchor_text: "Studies were included if they: were on patients with \nsymptomatic\
          \ stroke; were published in English; reported \non a series of consecutive\
          \ eligible patients (with an \ninclusion rate of at least 50%, allowing\
          \ for exclusions \nowing to aphasia, visual or hearing impairment, language\
          \ \nbarriers, and early mortality) or volunteers in prospective \ncohort\
          \ studies; included all stroke or all ischaemic stroke \n(studies restricted\
          \ to other particular stroke subtypes were \nexcluded); and gave dementia\
          \ measured by standard \ncriteria, such as diagnostic and statistical manual\
          \ of \nmental disorders IV (DSM IV), international classiﬁ cation \nof disease-10\
          \ (ICD-10), or a mini-mental state examination \n(MMSE) score of less than\
          \ 24 as an outcome."
        excluded_fragments: []
        image_sha256: f57716ff9c0f7efcb7733d62ac9b0e16bc2a69db4f2da006b49e327b4dcf6def
        transcription: 'Studies were included if they: were on patients with symptomatic
          stroke; were published in English; reported on a series of consecutive eligible
          patients (with an inclusion rate of at least 50%, allowing for exclusions
          owing to aphasia, visual or hearing impairment, language barriers, and early
          mortality) or volunteers in prospective cohort studies; included all stroke
          or all ischaemic stroke (studies restricted to other particular stroke subtypes
          were excluded); and gave dementia measured by standard criteria, such as
          diagnostic and statistical manual of mental disorders IV (DSM IV), international
          classification of disease-10 (ICD-10), or a mini-mental state examination
          (MMSE) score of less than 24 as an outcome'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "Results of studies that compare the incidence of new \ndementia in patients\
    \ with stroke versus controls reported \nup to a 9-fold increased risk in patients\
    \ with stroke in the \nﬁ rst year after stroke,36,42,82 and the excess incidence,\
    \ \nalthough lower, continued in the following years, with \nhazard ratios of\
    \ around four32,36,42 in hospital-based studies \nand around two in population-based\
    \ studies82,83–86 after the \n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
