---
id: fdc_non_canonical_comprehension
name: FDC non-canonical sentence comprehension predictor
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: non_canonical_sentence_comprehension
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: non_canonical_sentence_comprehension
  target_kind: impairment
  claim: FDC exhibited a significant positive association with non-canonical sentence
    comprehension accuracy in fixels predominantly situated in the left perisylvian
    region and the posterior corpus callosum, including the left superior longitudinal
    fasciculus (SLF II and SLF III), arcuate fasciculus (AF), middle longitudinal
    fasciculus, inferior fronto-occipital fasciculus, and the isthmus and splenium
    of the corpus callosum.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 23
    population: right-handed native Mandarin speakers with subacute single left-hemisphere
      strokes and aphasia
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
  - Small sample size may reduce statistical power
  - Cross-sectional design in subacute patients complicates comparison with chronic
    populations
  - Potential overlap of neighboring white matter fixel masks means associations between
    fixel location and specific tracts are not definite
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Whole-brain fixel-based analysis (FBA) of fiber density
    and cross-section (FDC) calculated from diffusion MRI. Analysis controlled for
    age, education, log-transformed time post-stroke, and verb comprehension accuracy;
    Results were robust after excluding outliers identified by Cook''s distance ≥1.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P4-S2-C4, two-model agreement, human verification
    pending): . Ultimately, 23 participants (19 men and 4 women) were included in
    the

    current analysis, with a mean stroke duration of 9.4 weeks at assessment Original
    text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:non_canonical_sentence_comprehension
  citation: '@Fang2025'
  source_passages:
  - section: Original source P10-S1-C2
    page: 10
    quote: 'Fixel‑Based Analyses

      Figure 4 illustrates the spatial distribution of 1601 fixels where FDC exhibited
      a signif‑

      icant positive association with non‑canonical sentence comprehension accuracy
      (family‑

      wise error corrected p < 0.05), controlling for age, education, log‑transformed
      time post

      stroke, and verb comprehension accuracy.'
    supports: claim
  - section: Original source P11-S1-C2
    page: 11
    quote: 'A positive lin‑

      ear relationship was observed between non‑canonical sentence comprehension accuracy

      and FDC in fixels located in the left superior longitudinal fasciculus II (SLF
      II), superior

      longitudinal fasciculus III (SLF III), arcuate fasciculus (AF), middle longitudinal
      fasciculus

      (MdLF), inferior fronto‑occipital fasciculus (IFOF), inferior longitudinal fasciculus
      (ILF),

      and the isthmus (ICC) and splenium (SCC) of the corpus callosum.'
    supports: claim
  - section: Original source P1-S2-C3
    page: 1
    quote: 'Methods: Twenty‑three

      right‑handed native Mandarin speakers with subacute (1–6 months post‑onset)
      single left‑

      hemisphere strokes underwent diffusion MRI.'
    supports: sample
  - section: Original source P4-S2-C4
    page: 4
    quote: 'Ultimately, 23 participants (19 men and 4 women) were included in the

      current analysis, with a mean stroke duration of 9.4 weeks at assessment.'
    supports: sample
  - section: Original source P8-S1-C12
    page: 8
    quote: 'Covariates include age, years of education, log‑transformed time post‑

      stroke, and the overall accuracy of the Verb Comprehension Test from the CALB‑AVS.
      Fol‑

      lowing established guidance for controlling false positives in FBA [74], our
      primary analy‑

      ses focus exclusively on FDC.'
    supports: method
  - section: Original source P10-S1-C5
    page: 10
    quote: 'The results of the same analysis after excluding outliers are shown in
      Figure A7, which re‑

      vealed a similar pattern.'
    supports: confounders
  - section: Original source P16-S2-C10
    page: 16
    quote: 'First, the relatively small sample size of

      this study may reduce its statistical power.'
    supports: limitation
  - section: Original source P17-S1-C11
    page: 17
    quote: 'Finally, this study was cross‑sectional and focused on subacute stroke

      patients, which complicates direct comparison with previous studies primarily
      conducted

      on chronic stroke populations.'
    supports: limitation
  - section: Original source P17-S1-C7
    page: 17
    quote: 'Thus, the associations

      between fixel location and tracts are not definite.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Whole-brain fixel-based analysis (FBA) of fiber density and cross-section
  (FDC) calculated from diffusion MRI.
assessment:
- CALB-AVS Sentence Comprehension Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fang2025
  proposal_id: R006
  review_status_sha256: 18c0246467e40e0b3b2d666903725da86107c530f39e01d3640a40094e9e9a7e
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
        A/passages.json: d103a822c2b049dff914f321cea5aa5042320ac969b1991f6436d12ae41673e6
        A/raw.json: 7141cdbd7426f05b2ae7ad8266ea451eb734aa16beb96c4f3bf1c1eea072e045
        A/source-units.json: 63cd6c72fb7f3048966ea0515e12f406599285931ed5272bff1e344060565c06
        A/full-source-units.json: a914fc1a91c47ed3d4fb524579c56fff66435debf5c146cee56003e4ee85fe1d
        A/meta.json: acb5b8941184b096c224f31d2847b6ce85102360dc0f33f95cc73681bd4c35fa
        A/table-images/TABLE-A1-page-21-1.png: a8b9af96da4fe8c3d262fade9461040177c1828cc6073424bcd9badb6ca967c5
        A/table-images/page-13.png: 7dd1b94b36300c67d48f5df87a71af50db993cf8c4ab5f137caaab77b5cde5b4
        A/table-images/TABLE-1-page-5-1.png: e2656b2b57d85e8d8ecb7533c153ada47ef085b98612ab6abe32b64177a1d3ce
        A/table-images/page-12.png: 288131ef1e3aa141114fad799dae239ed370dbdb63ee7cc1961ae2f58454838c
        A/table-images/page-5.png: a304ca3583e919cfdf8b16d2685bc8e78bb9e965a778a108c87c49bed52b56da
        A/table-images/manifest.json: 18a5a9839bf17ef7d5773af9fff72a263126f206d388df2dbf13eff7e7019254
        A/table-images/TABLE-2-page-13-1.png: 0d47ce1cc10c445b352c7d96a11f28764612962173434e1a643356374e4ddb0c
        A/table-images/page-21.png: 6e3a43084cf053a6c32bccd6c50ceb3028eecd7b0d48880b359db54c55be3d93
        A/table-images/TABLE-2-page-12-1.png: 3552600da9132befafb9e2094156cf3b3e3f427b7030db1d0f611f10ef877bf9
        A/clauses/window-11/raw.json: a99accb9ff0f28160531407cbae6a04ae620f2f8259a4b4ebafc91dd2a76c589
        A/clauses/window-11/prompt.txt: 05f9bccd0784db4e561841abf3e8f9db5120f58a858dea2a11e02d97dd498e66
        A/clauses/window-11/meta.json: a85d33ce8a3fe4c81d5462cef684fc47b999ada6f1061787882f8192a0441291
        A/clauses/window-10/raw.json: e1826c377f786ee6b91d96d27c4d8191bc3f9c960df456c55962d4f9f0b6f9b0
        A/clauses/window-10/prompt.txt: cc3e2197903050d023ba2197ef81766aac2cbbc53149d5c778e4e5476d77c4e8
        A/clauses/window-10/meta.json: bc7b57f64c2a64aafbdfd6a16db79d1ae99c8810dbea598c4334d3f93d33e4d9
        A/clauses/window-03/raw.json: 301a405e5630fa1ca32b5df1722ab05d455823e2ea20e533f74f69f8f5291b95
        A/clauses/window-03/prompt.txt: 5838271a263d8679ecea50aca672168f82925c3a943e441c8c734ecfa0403252
        A/clauses/window-03/meta.json: f9b1207a7efa29269e37cd764e71d15003f6252d32bf8b6be91d6cbff6f7739f
        A/clauses/window-04/raw.json: 30516de9ba2324d99144f448af99c68fb71631e123c8951ea30af779a651c58e
        A/clauses/window-04/prompt.txt: adf1eb98a42436344a87e9e496cee3f75177182c347f2483224560b06dbedd6b
        A/clauses/window-04/meta.json: 7e1e77059755c374156137bfc97ffb1e311221ed5f8940ed135d4f5e51e19d72
        A/clauses/window-05/raw.json: 946636a17d823c44156d521d39309b8bd7b46b606a64cdcd2f624b1d516801cb
        A/clauses/window-05/prompt.txt: e6d1e01e1970a1f780f56836cbee8f2ae7dc75588ec570307b9cc3431fb49778
        A/clauses/window-05/meta.json: 7062c00e4a493e57765b64c4c9db22adbb0f9204d33daacef80fb80c83031c0d
        A/clauses/window-02/raw.json: f3e005d3ff61bc8ec3ae092689056b37a2bcdcd60ab6c07fdcbffdce820e66f9
        A/clauses/window-02/prompt.txt: 91731e56f45719b00332fe62440fd6b8d1762ce038b457d94deff7e3177c334e
        A/clauses/window-02/meta.json: 0213e1489cfaaea300d29a4b93c80cc2431acd96237f980578be9e4f9d2cf82b
        A/clauses/window-09/raw.json: 1485e97464a3140b50b3c14ba9146f8d29b0869f194a1cf0715612ce50ae2d26
        A/clauses/window-09/prompt.txt: 468c038cfffadaf4e217deca8e0f040d517883a8b53be4694c5a4f1ad9d39bfd
        A/clauses/window-09/meta.json: fe3e8d8b8a641bb683e9c3f3aa702c6f06516eebfa4afd0c950e37570e93653a
        A/clauses/window-07/raw.json: ec9fa67106188c7f41d75ccdb099567cc56d99e7b3068fc38bf60d3b93d4e326
        A/clauses/window-07/prompt.txt: 621b32aef5fbbd54eb82ea4f1ed878d53b81f89208583cfa14aab01b44cd985f
        A/clauses/window-07/meta.json: ea90e1b7e43d1707fadfdb613f26fad1fb505972cb200d6931c368601eb85e2f
        A/clauses/window-01/raw.json: 7807df0bb9a8cef7068185d5582b5200ebdb95a969c6f9c5a1bacbe5a7d1631d
        A/clauses/window-01/prompt.txt: 08e20111434058d3fbbd0c666750823cfbbb341a3d98d5eafd4c5ad3270c1013
        A/clauses/window-01/meta.json: 48b97af757805526eeffb291d1f425197011826a7567021bf44c86df896830ec
        A/clauses/window-06/raw.json: be70a22b531b3a8c99de420fa16f497ee9a635bb4fc0c2282af59d1faab02970
        A/clauses/window-06/prompt.txt: f90b2c9813bf1cffa439d0ebea268356a9347ecff6d80a630ffbd70ab0b0a9b7
        A/clauses/window-06/meta.json: 84200563ae8335c04c7cdcbe7b53b91ed02ee96e2ccd7b9d2c3c558e4e152cdf
        A/clauses/window-08/raw.json: b66c141e032378b28e1d897a19d5f1c683bdfbc991ef95ae1b7597a70536c7bb
        A/clauses/window-08/prompt.txt: 5c3dd9bdd02bd640753449127f727f68440e84891e8341b47e228267828d8b5d
        A/clauses/window-08/meta.json: b3f10fd67d138ba3d61c27133644faed41a415f96996b4848a5e529e50a3f33e
        A/tables/TABLE-1-page-5-1/raw.json: 243aa95910f205970da012c289b6a053156111e85f2bec4ae24a53746df107ae
        A/tables/TABLE-1-page-5-1/prompt.txt: 27b087ddd6ccc49e31da10c260575daad37241d772444f4fe87963fa3c283d2d
        A/tables/TABLE-1-page-5-1/meta.json: 78a90bc4f1ed270ad5b88d6b67f35ed9f2f319b5f356921b422c033dab579ec9
        A/tables/TABLE-2-page-12-2/raw.json: 22ef5e91d2f34eaf5826602bdf092eeb006a9bcdf3707c75afb79e6022f8de3c
        A/tables/TABLE-2-page-12-2/prompt.txt: 4272657fa98d336e4c3eb35b04f1cac69593ba09d71e9c124262e44cc109e719
        A/tables/TABLE-2-page-12-2/meta.json: d39a5ae0b59232ea097d67a77443ff60a44bf0a0203ff59452a04b1ba7103495
        A/tables/TABLE-2-page-13-3/raw.json: d41a298472013d6cf3c942d582c1a4f7fb5949f33805f5b347019c8201c4fe75
        A/tables/TABLE-2-page-13-3/prompt.txt: e2c9799ad4492500b44d05f0106b804668507a87b6f02701f52a0ee46f47c529
        A/tables/TABLE-2-page-13-3/meta.json: bf00b07c77fc1fb971a84c280a08cb3f9c57ea23383cff6261b99e47071347eb
        A/tables/TABLE-A1-page-21-4/raw.json: 74dd8a6f52cff88b7d647b6ac63ccb7b991cbb2fd7eb94946ce80b9487f98504
        A/tables/TABLE-A1-page-21-4/prompt.txt: fd5a5a4448a7e0e74181a23e946b0c177b7dfd1866e893bea6a9cd877740ab97
        A/tables/TABLE-A1-page-21-4/meta.json: 7fac71fc9c8bdbd1ef6cd5c6e21ac1aece13212669b73c2173f351a64db82792
        B/passages.json: d103a822c2b049dff914f321cea5aa5042320ac969b1991f6436d12ae41673e6
        B/raw.json: 8b2b3b277083c31df20d119a4b4dcda289e55e127b1a393546338b83d529e336
        B/source-units.json: 63cd6c72fb7f3048966ea0515e12f406599285931ed5272bff1e344060565c06
        B/full-source-units.json: a914fc1a91c47ed3d4fb524579c56fff66435debf5c146cee56003e4ee85fe1d
        B/meta.json: 75c14acb9ec83c3944f6fd8fcd48c33ae1dc7aecaae0b89d394299d0310ac38b
        B/table-images/TABLE-A1-page-21-1.png: a8b9af96da4fe8c3d262fade9461040177c1828cc6073424bcd9badb6ca967c5
        B/table-images/page-13.png: 7dd1b94b36300c67d48f5df87a71af50db993cf8c4ab5f137caaab77b5cde5b4
        B/table-images/TABLE-1-page-5-1.png: e2656b2b57d85e8d8ecb7533c153ada47ef085b98612ab6abe32b64177a1d3ce
        B/table-images/page-12.png: 288131ef1e3aa141114fad799dae239ed370dbdb63ee7cc1961ae2f58454838c
        B/table-images/page-5.png: a304ca3583e919cfdf8b16d2685bc8e78bb9e965a778a108c87c49bed52b56da
        B/table-images/manifest.json: a668b9837d4675dca60ac9ce6271f140aa20632b30c59ee3eda99d69c09903eb
        B/table-images/TABLE-2-page-13-1.png: 0d47ce1cc10c445b352c7d96a11f28764612962173434e1a643356374e4ddb0c
        B/table-images/page-21.png: 6e3a43084cf053a6c32bccd6c50ceb3028eecd7b0d48880b359db54c55be3d93
        B/table-images/TABLE-2-page-12-1.png: 3552600da9132befafb9e2094156cf3b3e3f427b7030db1d0f611f10ef877bf9
        B/clauses/window-11/raw.json: a99accb9ff0f28160531407cbae6a04ae620f2f8259a4b4ebafc91dd2a76c589
        B/clauses/window-11/prompt.txt: 05f9bccd0784db4e561841abf3e8f9db5120f58a858dea2a11e02d97dd498e66
        B/clauses/window-11/meta.json: 4837dd7aeddb0387361f883a43a1bea4520ba90f5fd05df03372669cdf608e85
        B/clauses/window-10/raw.json: dae77a004a47e3957afd49dee785b56beaa89f01cda0852aa2b735fd06bc8584
        B/clauses/window-10/prompt.txt: cc3e2197903050d023ba2197ef81766aac2cbbc53149d5c778e4e5476d77c4e8
        B/clauses/window-10/meta.json: 37e4242b2f4c58bcd98b7e8e821ae502e65543e2798e18d9dbc109a5d423e422
        B/clauses/window-03/raw.json: d385dcac941f2f1df420bca8db2d6ed207747833299794c6ca19bad356e798ce
        B/clauses/window-03/prompt.txt: 5838271a263d8679ecea50aca672168f82925c3a943e441c8c734ecfa0403252
        B/clauses/window-03/meta.json: a02e493b471a27d8d5142d7fdd38c605f70cfb8e72d739f3da5c0af40dd8172a
        B/clauses/window-04/raw.json: 4e8d2d211266fd9ef2a7a0b8479b941733de8a22fb67fc5d28a02969c9b61a66
        B/clauses/window-04/prompt.txt: adf1eb98a42436344a87e9e496cee3f75177182c347f2483224560b06dbedd6b
        B/clauses/window-04/meta.json: 70cb31bb1554d8193eaa1ae3ac116e3ad4f9be5261ddbb594a63db4d061f1f98
        B/clauses/window-05/raw.json: d8d4113c57df8fa7550918c66e677b9bb87d9e1eeff6c9b5be959e174c143067
        B/clauses/window-05/prompt.txt: e6d1e01e1970a1f780f56836cbee8f2ae7dc75588ec570307b9cc3431fb49778
        B/clauses/window-05/meta.json: 280435004a19bc0ff442d369409951cc2e1d73fcdbe80720d47af00ae49de19a
        B/clauses/window-02/raw.json: b1b271d8e2b875aa90e0594b1c7b416dfd9371cfe1d9b72e1f7708376b6155e5
        B/clauses/window-02/prompt.txt: 91731e56f45719b00332fe62440fd6b8d1762ce038b457d94deff7e3177c334e
        B/clauses/window-02/meta.json: 8485941cc0699007ba6ae65e2b38d1fd18a794a86fb33e802d4564a5fc44a3d7
        B/clauses/window-09/raw.json: ad172805ce3c477075253ddf41dac71a89d891a0b5930a8a14bc57a6c0197c1d
        B/clauses/window-09/prompt.txt: 468c038cfffadaf4e217deca8e0f040d517883a8b53be4694c5a4f1ad9d39bfd
        B/clauses/window-09/meta.json: cab5deb36c63482b40fd119dc4989c590665b27913a3b9d18c81bcafcb46875f
        B/clauses/window-07/raw.json: 2485e3d0a973147ded2931edd99972635feeb9317b63b3f2ac511c600386a3d8
        B/clauses/window-07/prompt.txt: 621b32aef5fbbd54eb82ea4f1ed878d53b81f89208583cfa14aab01b44cd985f
        B/clauses/window-07/meta.json: 26aa5e0f98d51a7d32cf6b44c0815480de75276f52f387a069a293ccf7f966a6
        B/clauses/window-01/raw.json: 62c91954c26f62c696aa59282926b8c203c2058341fbad4223c90d10e0e99d51
        B/clauses/window-01/prompt.txt: 08e20111434058d3fbbd0c666750823cfbbb341a3d98d5eafd4c5ad3270c1013
        B/clauses/window-01/meta.json: e69b395a14d9449ed72c50040029d387981bfb41fcc881e0993c6ee0ab7584b3
        B/clauses/window-06/raw.json: c317cb533fa8d492a7f39d387debe5dd50701c78e21dcc2a371770d08d7cd5c0
        B/clauses/window-06/prompt.txt: f90b2c9813bf1cffa439d0ebea268356a9347ecff6d80a630ffbd70ab0b0a9b7
        B/clauses/window-06/meta.json: d04a812e4b811064ae57e923bb1e860539550b2588aa46f67368c290d19f757f
        B/clauses/window-08/raw.json: cd95afcd873a57a07ac30307b11c362435a7877b35c7cd7580099b6d17f5c464
        B/clauses/window-08/prompt.txt: 5c3dd9bdd02bd640753449127f727f68440e84891e8341b47e228267828d8b5d
        B/clauses/window-08/meta.json: 8912501f563c7a095bde95f43706c62d2449726d103f2062e779c7a79f5369c1
        B/tables/TABLE-1-page-5-1/raw.json: 87c80c1a4be1e8858f8cc60687ee8a6a0e1453d5fe0be03da96e01c68d5f4f9c
        B/tables/TABLE-1-page-5-1/prompt.txt: 27b087ddd6ccc49e31da10c260575daad37241d772444f4fe87963fa3c283d2d
        B/tables/TABLE-1-page-5-1/meta.json: 36e06a1d794eac527243bb27751cbbebdd188ec7848f6dc761ad452d42713f94
        B/tables/TABLE-2-page-12-2/raw.json: 8df28d425b005d9cc5710dc9cdfc0602aeb03ef658d65c9404de2ed2965bcf00
        B/tables/TABLE-2-page-12-2/prompt.txt: 4272657fa98d336e4c3eb35b04f1cac69593ba09d71e9c124262e44cc109e719
        B/tables/TABLE-2-page-12-2/meta.json: ff8bde19606fc73503b4d7552799da728562c033ffb216042a6cac5ff1f03e11
        B/tables/TABLE-2-page-13-3/raw.json: d3746c34eac5dc8484a63496b57b15517bce4b2bcff8657c63333539669d7f3b
        B/tables/TABLE-2-page-13-3/prompt.txt: e2c9799ad4492500b44d05f0106b804668507a87b6f02701f52a0ee46f47c529
        B/tables/TABLE-2-page-13-3/meta.json: f3e9f9b948f461e6f6a3f873236d47a48ffdd55409e590ce40d6b1e782c77ec5
        B/tables/TABLE-A1-page-21-4/raw.json: b14843500bc2dd2462b87f85dfdabf767e2800fbd2e638d518a0cfeb252ff35d
        B/tables/TABLE-A1-page-21-4/prompt.txt: fd5a5a4448a7e0e74181a23e946b0c177b7dfd1866e893bea6a9cd877740ab97
        B/tables/TABLE-A1-page-21-4/meta.json: 2563ae49659b3325d34f8c4d5ade592740a1c1ff21b2bba2132f43b11b5e3866
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
      source_review: _compare/relationships-2026-11-16/review-current/Fang2025
      source_status_sha256: 3b9fd6ca64329aadb6978e249c5845110f1cb7e9c9ce84b42efa192018329fb1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: fiber density and cross-section (FDC)
    outcome:
      text: non-canonical sentence comprehension accuracy
    analysis_label: Whole-brain FBA (Primary)
    relation: association
    evidence_ids:
    - P1-S2-C9
    - P10-S1-C2
    - P11-S1-C2
    - P12-S1-C2
    qualifier_ids:
    - P10-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
      source_review: _compare/relationships-2026-11-16/review-current/Fang2025
      source_status_sha256: 3b9fd6ca64329aadb6978e249c5845110f1cb7e9c9ce84b42efa192018329fb1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P9-S1-C8
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C5
      - Accounting without a linked unit P10-S1-C6
      - Accounting without a linked unit P11-S1-C1
      - Unaccounted source passage P11-S1-C1
      - Unaccounted source passage P10-S1-C6
      - Accounting without a linked unit P14-S1-C12
      - Result passage disposed without unit P14-S1-C8
      - Unaccounted source passage P14-S1-C12
      - Result passage disposed without unit P14-S2-C4
      - Result passage disposed without unit P14-S2-C5
      - Result passage disposed without unit P16-S1-C4
      - Result passage disposed without unit P17-S1-C9
      unattached_null_or_qualifier_ids:
      - P9-S1-C8
      - P14-S2-C5
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 254
      unselected_timing_passages:
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C4
      - P4-S1-C6
      - P4-S2-C3
      - P4-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P19-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P20-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P22-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P22-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P23-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P24-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P8-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P1-S2-C2
        - P2-S1-C5
        - P6-S1-C2
        - P6-S2-C6
        - P7-S1-C2
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P8-S1-C3
        - P8-S2-C4
        - P8-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S2-C6
        - P3-S1-C1
        - P3-S1-C2
        - P8-S2-C6
        - P16-S1-C5
        - P16-S2-C10
        - P16-S2-C15
        - P17-S1-C1
        - P17-S1-C2
        - P17-S1-C3
        - P17-S1-C4
        - P17-S1-C6
        - P17-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C5
        - P1-S2-C7
        - P8-S1-C12
        - P8-S2-C10
        - P10-S1-C2
        - P13-S1-C10
        - P21-S1-C5
        - P22-S1-C2
        - P22-S1-C5
        - P23-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S2-C3
        - P4-S2-C4
        - P4-S2-C5
        - P5-S1-C1
        - P5-S1-C6
        - P8-S2-C10
        - P9-S1-C11
        - P13-S1-C10
        - P17-S1-C3
        - P23-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - validation
      - limitations
      - adjustment_roles
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-12-2
      - TABLE-2-page-13-3
      - TABLE-A1-page-21-4
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-12-2
      - TABLE-2-page-13-3
      - TABLE-A1-page-21-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S2
        - P7-S1
        - P9-S1
        - P10-S1
        - P11-S1
        - P12-S1
        - P13-S1
        - P24-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
      source_review: _compare/relationships-2026-11-16/review-current/Fang2025
      source_status_sha256: 3b9fd6ca64329aadb6978e249c5845110f1cb7e9c9ce84b42efa192018329fb1
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: States canonical sentences were comprehended better than non-canonical.
    - source_id: P1-S2-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies positive correlations between FDC and non-canonical sentence
        comprehension in specific tracts.
    - source_id: P1-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the nature of FDC reductions (FD vs FC) rather than a specific
        clinical relationship.
    - source_id: P8-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes behavioral data presentation in Figure 2.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significantly lower accuracy for non-canonical sentences.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports worse performance on subject relative clauses vs active sentences.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Null finding for other sentence type differences.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of subject relative clause impairment.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Positive association between canonical and non-canonical accuracy.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Positive correlations between canonical accuracy and VCT, word recognition,
        and AQ.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Positive correlations between non-canonical accuracy and VCT, word recognition,
        and AQ.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Reports 1601 fixels with positive association between FDC and non-canonical
        accuracy.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Locates fixels in left perisylvian region and posterior corpus callosum.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Null finding for negative relationships.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Confirms similar pattern after excluding outliers.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Reports associations for FD (1003 fixels) and FC (20 fixels) with non-canonical
        comprehension.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Lists specific tracts (SLF II, SLF III, AF, MdLF, IFOF, ILF, ICC, SCC)
        with positive FDC relationship.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Specifies spatial locations of significant fixels within tracts.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Restates 1601 significant fixels in left perisylvian and posterior corpus
        callosum.
    - source_id: P13-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Exploratory analysis showing FD reductions associated with impaired
        non-canonical comprehension.
    - source_id: P13-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Exploratory analysis showing FC reductions in left SLF III and AF associated
        with impaired non-canonical comprehension.
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Positive association between active sentence accuracy and mean FDC of
        left MdLF and SLF II.
    - source_id: P13-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Positive correlation between mean FDC of left SLF III and object extracted,
        subject relative, and all non-canonical sentences.
    - source_id: P13-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Positive association between subject relative clause accuracy and mean
        FDC of left SLF II.
    - source_id: P14-S1-C2
      disposition: represented
      result_indexes:
      - 12
      - 13
      reason: Positive correlations for mean FD of ICC (ba-sentences) and AF/SLF II/SLF
        III (subject relative clauses).
    - source_id: P14-S1-C3
      disposition: represented
      result_indexes:
      - 14
      reason: Positive correlation between non-canonical accuracy and mean FD of left
        AF, SLF III, and MdLF.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 15
      reason: Null finding for mean FC correlations.
    - source_id: P14-S1-C12
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of FDC association in left peri-Sylvian white matter.
    - source_id: P14-S2-C3
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of tracts involved in FDC association.
    - source_id: P14-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of FDC reduction as being driven by FD reduction.
    - source_id: P14-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of FC reduction in SLF III and AF.
    - source_id: P16-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about tract-wise analysis results.
    - source_id: P16-S1-C6
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of left MdLF FDC association with active sentences.
    - source_id: P16-S1-C7
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of left SLF II FDC association with subject relative clauses.
    - source_id: P16-S1-C8
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of left SLF III FDC association with object extracted and
        subject relative clauses.
    - source_id: P16-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post hoc power analysis result.
    - source_id: P17-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overlapping fixels between tracts.
    - source_id: P17-S2-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Conclusion restating FDC associations in specific tracts.
    - source_id: P17-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about dissociative associations.
    - source_id: P19-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports 1003 significant fixels for FD association.
    - source_id: P20-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Reports 20 significant fixels for FC association.
    - source_id: P24-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Reports 2052 significant fixels for FDC association after outlier removal.
    - source_id: P24-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Describes spatial extension of significant fixels in outlier-removed
        model.
    unresolved_coverage:
    - source_id: P14-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C10
    - P8-S2-C14
    - P9-S1-C1
    - P9-S1-C4
    - P10-S1-C3
    - P10-S1-C4
    - P11-S1-C1
    - P11-S1-C4
    - P14-S1-C6
    - P14-S1-C8
    - P14-S1-C12
    - P14-S2-C3
    - P14-S2-C4
    - P14-S2-C5
    - P16-S1-C4
    - P16-S2-C14
    - P17-S1-C9
    - P17-S2-C5
    - P17-S2-C6
    - P24-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-12-2
    - TABLE-2-page-13-3
    - TABLE-A1-page-21-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S2-C3
      - P4-S1-C1
      - P4-S2-C4
      - P8-S2-C6
      - P16-S1-C4
      - P16-S2-C14
      recruited_sample:
      - P1-S2-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S2-C4
      - P8-S2-C6
      - P16-S2-C14
      eligibility:
      - P1-S2-C3
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S2-C3
      - P4-S2-C5
      - P17-S1-C3
      imaging_provenance: []
      imaging_timing:
      - P1-S2-C3
      - P17-S1-C11
      outcome_timing:
      - P1-S2-C3
      - P17-S1-C11
      outcome_definition:
      - P1-S2-C5
      - P1-S2-C7
      - P5-S2-C2
      - P5-S2-C4
      - P6-S2-C16
      - P8-S2-C10
      - P8-S2-C11
      validation: []
      analysis_restrictions:
      - P8-S1-C12
      - P8-S2-C7
      - P16-S2-C15
      - P17-S1-C1
      - P17-S1-C10
      dependent_variable_statement:
      - P1-S2-C5
      - P1-S2-C7
      - P6-S2-C16
      - P8-S1-C11
      limitations: []
      personal_factors:
      - P1-S2-C3
      - P1-S2-C5
      - P8-S2-C10
      tested_personal_effects:
      - P9-S1-C10
      adjustment_roles: []
      explicitly_not_adjusted:
      - P17-S1-C3
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P19-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P20-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P22-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P22-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P23-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P24-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P8-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P1-S2-C2
      - P2-S1-C5
      - P6-S1-C2
      - P6-S2-C6
      - P7-S1-C2
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P8-S1-C3
      - P8-S2-C4
      - P8-S2-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S2-C6
      - P3-S1-C1
      - P3-S1-C2
      - P8-S2-C6
      - P16-S1-C5
      - P16-S2-C10
      - P16-S2-C15
      - P17-S1-C1
      - P17-S1-C2
      - P17-S1-C3
      - P17-S1-C4
      - P17-S1-C6
      - P17-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C5
      - P1-S2-C7
      - P8-S1-C12
      - P8-S2-C10
      - P10-S1-C2
      - P13-S1-C10
      - P21-S1-C5
      - P22-S1-C2
      - P22-S1-C5
      - P23-S1-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S2-C3
      - P4-S2-C4
      - P4-S2-C5
      - P5-S1-C1
      - P5-S1-C6
      - P8-S2-C10
      - P9-S1-C11
      - P13-S1-C10
      - P17-S1-C3
      - P23-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
      review_sha256: 18c0246467e40e0b3b2d666903725da86107c530f39e01d3640a40094e9e9a7e
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
      - P1-S2-C9
      - P10-S1-C2
      - P11-S1-C2
      - P12-S1-C2
      source_result: FBA identified significant positive correlations between FDC
        and non-canonical sentence comprehension in the left superior longitudinal
        fasciculus (SLF II and SLF III), arcuate fasciculus (AF), middle longitudinal
        fasciculus, inferior fronto-occipital fasciculus, and the isthmus and splenium
        of the corpus callosum. These fixels were predominantly situated in the left
        perisylvian region and the posterior corpus callosum.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the primary whole-brain FBA (P8-S1-C11,
            P10-S1-C2) assessing the association between FDC and non-canonical sentence
            comprehension. The source confirms this is the primary analysis, distinct
            from tract-wise or exploratory FD/FC analyses.
          source_ids:
          - P8-S1-C11
          - P10-S1-C2
          - P1-S2-C5
        direction:
          answer: fits
          reason: The source explicitly states 'significant positive correlations'
            (P1-S2-C9, P11-S1-C2) and 'positive association' (P10-S1-C2). The draft
            claim preserves this direction.
          source_ids:
          - P1-S2-C9
          - P10-S1-C2
          - P11-S1-C2
        construct:
          answer: fits
          reason: Exposure is FDC (fiber density and cross-section) from diffusion
            MRI. Outcome is non-canonical sentence comprehension accuracy. The measurement
            is patient-specific diffusion data (FBA on individual dMRI), not template
            overlap or atlas metadata. The draft correctly identifies the imaging
            metric and behavioral target.
          source_ids:
          - P8-S1-C11
          - P8-S1-C12
          - P10-S1-C2
        qualifications:
          answer: fits
          reason: The draft includes the key covariates (age, education, time post-stroke,
            verb comprehension) and the robustness check (outlier exclusion). These
            are material qualifiers present in the source (P8-S1-C12, P10-S1-C5).
          source_ids:
          - P8-S1-C12
          - P10-S1-C5
          - P10-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding sample size, cross-sectional
            design, and tract mask overlap. No material caveats that change the interpretation
            of the primary result are omitted.
          source_ids:
          - P16-S2-C10
          - P17-S1-C11
          - P17-S1-C7
      optional_pending:
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.time_post_onset
      original: subacute (1–6 months post-onset); mean stroke duration of 9.4 weeks
        at assessment
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1, 6'
    analysis_identity:
      id: R006
      exposure:
        text: fiber density and cross-section (FDC)
      outcome:
        text: non-canonical sentence comprehension accuracy
      analysis_label: Whole-brain FBA (Primary)
      relation: association
      evidence_ids:
      - P1-S2-C9
      - P10-S1-C2
      - P11-S1-C2
      - P12-S1-C2
      qualifier_ids:
      - P10-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
        source_review: _compare/relationships-2026-11-16/review-current/Fang2025
        source_status_sha256: 3b9fd6ca64329aadb6978e249c5845110f1cb7e9c9ce84b42efa192018329fb1
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e05eefc08ecb7b3230e40266c74ed749e13517ad8a99efc567f4d4267083849a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C3
          page: 1
          text_layer_sha256: e05eefc08ecb7b3230e40266c74ed749e13517ad8a99efc567f4d4267083849a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Methods: Twenty‑three

          right‑handed native Mandarin speakers with subacute (1–6 months post‑onset)
          single left‑

          hemisphere strokes underwent diffusion MRI.'
        anchor_text: 'Methods: Twenty‑three

          right‑handed native Mandarin speakers with subacute (1–6 months post‑onset)
          single left‑

          hemisphere strokes underwent diffusion MRI.'
        excluded_fragments: []
        image_sha256: 989cc47568c7a4db799e48e62478f5e95228e93d7a9b40227ac4c958658852c6
      P4-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b03d4e3907f66a45b11f94009eb4c6d8f3a05e006abd7f49d160ad223a8f2b30
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8d491f90337214bc8124d7e4a3c6000d0f075ee2cc4b430fbc132b15fd1995b5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C4
          page: 4
          text_layer_sha256: 8d491f90337214bc8124d7e4a3c6000d0f075ee2cc4b430fbc132b15fd1995b5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Ultimately, 23 participants (19 men and 4 women) were included
          in the

          current analysis, with a mean stroke duration of 9.4 weeks at assessment.'
        anchor_text: 'Ultimately, 23 participants (19 men and 4 women) were included
          in the

          current analysis, with a mean stroke duration of 9.4 weeks at assessment.'
        excluded_fragments: []
        image_sha256: b0e404d4b4f4a980ce1e3d62567940596049574e05d5ac0bd3b8a9a16713764c
        transcription: '. Ultimately, 23 participants (19 men and 4 women) were included
          in the

          current analysis, with a mean stroke duration of 9.4 weeks at assessment'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'Fixel‑Based Analyses

    Figure 4 illustrates the spatial distribution of 1601 fixels where FDC exhibited
    a signif‑

    icant positive association with non‑canonical sentence comprehension accuracy
    (family‑

    wise error corrected p < 0.05), controlling for age, education, log‑transformed
    time post

    stroke, and verb comprehension accuracy.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
