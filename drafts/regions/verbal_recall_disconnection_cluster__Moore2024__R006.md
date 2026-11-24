---
id: verbal_recall_disconnection_cluster
name: verbal recall disconnection cluster
kind: network
findings:
- id: f1
  target: verbal_recall
  target_kind: impairment
  claim: Verbal recall deficits were associated with damage to 173 network edges,
    with the strongest predictor of impairment being damage to streamlines connecting
    the left frontal eye fields (dorsal attentional network) and the left putamen.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: acute stroke survivors
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
  - retrospective analysis
  - unable to distinguish between pre-morbid and post-stroke impairments
  - lower power to detect contributions of neural regions supplied by the ACA, PCA,
    and ACoA
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population-averaged
    disconnectome atlas (HCP-842) to estimate the proportion of disconnected streamlines
    (network edges) connecting 135 defined grey matter parcels (Schaefer-Yeo and AAL/Harvard-Oxford
    atlases). lesion volume was included as a covariate of no interest in the regression;
    results survived Bonferroni or 5% FDR corrections. Additional metadata has not
    been transcribed; review the pending-field flags before approval.'
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
    - proposed_concept:verbal_recall
  citation: '@Moore2024'
  source_passages:
  - section: Original source P5-S1-C11
    page: 5
    quote: 'Verbal Recall deficits were associated with damage to 173

      edges (R2 values = 0.002–0.005, all p < 3.26 × 10−5).'
    supports: claim
  - section: Original source P5-S1-C12
    page: 5
    quote: 'The strongest

      predictor of impairment on this task was damage to streamlines con-

      necting the left frontal eye fields (dorsal attentional network) and the

      left putamen.'
    supports: claim
  - section: Original source P3-S1-C1
    page: 3
    quote: '

      (Health

      Research

      Authority

      UK

      (REC

      references:14/LO/0648,

      18/SC/0550, 12/WM/00335). Patients were included in the present

      analysis if they completed the Oxford Cognitive Screen (OCS) within 31

      days of stroke and had available acute neuroimaging (within 31 days of

      stroke) which was of sufficient quality to facilitate lesion delineation. Of

      the 1198 patients recruited in the OCS Programme, 398 were excluded

      from this analysis for having no useable neuroimaging data. Ninety-six

      patients were excluded due to evidence of multiple, temporally

      distinct stroke lesions. One hundred and thirteen additional patients

      were excluded due to OCS or neuroimaging data being collected >31

      days post stroke.

      2.2. Behavioural data

      Cognitive status was assessed using the Oxford Cognitive Screen

      (OCS; Demeyere et al., 2015). The OCS is a short, stroke-specific

      cognitive screen designed for use in acute stroke settings. It yields 16

      distinct measures summarising cognitive impairments across commonly

      impacted cognitive domains: executive function, language, memory,

      number processing, praxis, and visuospatial attention (Demeyere et al.,

      2015, 2016). This measure is designed to be inclusive for patients with

      common stroke-related impairments including aphasia, visuospatial

      neglect, primary visual impairments (e.g. hemianopia), and primary

      motor impairments (e.g. hemiplegia) (Demeyere et al., 2015, 2016).

      The OCS executive function domain is assessed using a modified

      (shape-based) trail making task. The OCS language domain consists of a

      picture naming task (images of four objects/animals), a semantics task

      (follow verbally presented instructions), and a sentence reading task.

      The OCS memory domain includes a delayed recall of the previously

      read sentence (verbal recall task), an incidental multiple-choice recall of

      stimuli and tasks completed earlier in the OCS (episodic recognition

      task), and 4 items assessing the participant’s orientation in time and

      location (orientation task). The OCS numerical processing domain in-

      cludes a number tasks in which participants are asked to write three

      verbally presented numbers (in digits) and a calculation task where

      participants are asked to solve four simple addition and subtraction

      '
    supports: sample
  - section: Original source P3-S4-C4
    page: 3
    quote: 'The Schaefer-Yeo cortical parcellation was compared with the HCP-

      842 atlas to quantify disconnection statistics.'
    supports: method
  - section: Original source P3-S4-C8
    page: 3
    quote: 'Network-level disconnectivity sta-

      tistics were generated by calculating the proportion of streamlines that

      terminate (end or begin) in each pair of parcels that were disconnected

      (Griffis et al., 2021).'
    supports: method
  - section: Original source P3-S4-C12
    page: 3
    quote: 'Each regression included only partici-

      pants who completed the relevant subtest, and included lesion volume

      as a covariate of no interest.'
    supports: confounders
  - section: Original source P8-S2-C4
    page: 8
    quote: 'Our analyses cannot effectively distinguish between impairments

      that were pre-morbid and impairments that followed the stroke.'
    supports: limitation
  - section: Original source P13-S3-C8
    page: 13
    quote: 'The lesion distribution

      is representative of the stroke population (e.g. primarily MCA strokes)

      but has comparatively lower power to detect contributions of neural

      regions supplied by the anterior cerebral artery, posterior cerebral ar-

      tery, and anterior cerebral communicating artery.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Moore2024
  proposal_id: R006
  review_status_sha256: e211a9c0f722864c45472379302ae75d52976bd643cd6f13f1153106231aa29d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
        A/passages.json: 8ef2ee713a42a8639efb0e0c64923f0927612d88844bf1b18e9d251273cf2a90
        A/raw.json: 9c767081b694c2515790d14f92e2107eabf6650bf707050de366698197e533f9
        A/source-units.json: 9c24be407363cd3a441b0615a36bfefa3afb0cddddd754d8a8c1dc3fed0cff87
        A/full-source-units.json: ee96cc88aa74b5388add42a52fe8c88e8c483d0a250780178d5d04c15224fd0c
        A/meta.json: db20e04a925ad5e8ba80a80f02658c013650a474e6b6a35146c34c1ff5621c52
        A/table-images/TABLE-3-page-12-1.png: 22051271c4b2bab3ab54b5a67f7346b5a88b1c971265f24e47d987a38b0d1368
        A/table-images/TABLE-3-page-10-1.png: 4213e204e8c8086fb73fe00a4e36212141e23329b4505d2aa47fa761ba2b261a
        A/table-images/page-12.png: ed9a66ccf3bfce36588434bb8e0eef6dc0fd405cd2992f63e88aea6421440be6
        A/table-images/page-10.png: e324189837aae3f22778f4bc74eaceefa4e43a39f65e224056587387ecae12da
        A/table-images/page-11.png: 0e83713f9e589e0d2b71c93d85157aa8c5f1fe87fff4398eb22e2e294d1a2958
        A/table-images/TABLE-3-page-11-1.png: 29b45e31e4629149c99bbead06c139e84f20c7915eb5e18b0ee8bbaa985ef023
        A/table-images/TABLE-1-page-2-1.png: bbda21547ff3cd95408b7cb5c4d1afd2331f43692cc1438a8afbb90616b05efe
        A/table-images/page-2.png: 40b75b60131c3a475ce65cfae754248d6ada8af3165d99efc294ce357e7f14e1
        A/table-images/page-4.png: e6dcd21a323f7e0f5bbd47e28026a9931857746dfc69f9b831d291dbbee46bf7
        A/table-images/manifest.json: 6eeb6bc10737631620f5cfae72cacf56d0a4b9cc9207dfd2d713b0253bb417be
        A/table-images/TABLE-2-page-4-1.png: 9a81e3e9c1432ed618ac95b3d6c34920f92911101ff21e0b50179a69eb0231e9
        A/clauses/window-11/raw.json: bc6691ece0308864e477e7ae24113e866eedb35e6b231728cd940421e223f6a1
        A/clauses/window-11/prompt.txt: a9eae13cd84b28962172f899d6d27770a0015dc07181cd0106ad1198f555f6a7
        A/clauses/window-11/meta.json: 56db5ed398022c6c90090e874a62c30cb2c62f98759aa916ee0268a02308daed
        A/clauses/window-10/raw.json: 7d834e7ca088c6fd9dd516616ef82f777b2480d8ced5106d77868157857032b3
        A/clauses/window-10/prompt.txt: ee4d67b66c8fb8e5cbd265389fbeb215f49aac21b05a759450aea4295631679f
        A/clauses/window-10/meta.json: a3a3007dc17ee6d05452575921f486382bcebd51cf638b0d2b0d90283b831282
        A/clauses/window-03/raw.json: e74eb74e7ce76d5786c6894f2266114c632b9defa44adb5a53ec89bd4d85a8be
        A/clauses/window-03/prompt.txt: cbb6048476815ac0d8ab39e42cf43bba9d4adf5e5f8ae63da1d92d661768b49e
        A/clauses/window-03/meta.json: 6d710822153b540463275775d98f60995680891ec897ef8759eb2a6655e2781d
        A/clauses/window-04/raw.json: d1d98381b2b56202af21f39c30cec66dd89a04aae752ba146b39e32ee058790b
        A/clauses/window-04/prompt.txt: 9cf1394663b40cb802f15ddfc6b0271dba5c65767e6c80d92f6de39ed3ed0e34
        A/clauses/window-04/meta.json: 92a9086b8fe2f2b2c8af5cf8b30ccf3f3944f6d851a02e4a6eaf8f86a1078b0b
        A/clauses/window-05/raw.json: e11f777295793eb56bd3c6a0071f36ea59013c5e275ef12a69fac907e8065a69
        A/clauses/window-05/prompt.txt: f6e6e1c3f45aeb17124c4e0e298b8afe9eccdb8ade55df720eeaa2afb48915f3
        A/clauses/window-05/meta.json: 4a08f1d09f7a8c02a58ea48f3438aee91d34060f602fb1f213a5f59bf31e136b
        A/clauses/window-02/raw.json: 2ae7936019d78618e91a755a968c3f7aaff73d58a4fcec553ec9988b3ee90b3a
        A/clauses/window-02/prompt.txt: 4c2240073e461827dfc8466f4c21d93439cba2837554775ee5eeaf88dcc75336
        A/clauses/window-02/meta.json: 51dc2a8a6acbad69b479e2c31c50f19f9fa693c4fc34689bf6b34c39714031a2
        A/clauses/window-09/raw.json: d5903511f6d83e31e12288457385e5eaedec9d368586a8e349c5b5f867e6bec2
        A/clauses/window-09/prompt.txt: cb4e935cb48827d745477eff314572344175c880658bff3d00928b1873684e7e
        A/clauses/window-09/meta.json: 2376d622bb1608308a1a85607fce918400ce15a02ce11f359c9f93d3db3abe0a
        A/clauses/window-07/raw.json: e068ac5bf8d4b1514f027a0c9d7b9be3e6b92f9b14788c98ded9aabbb1e4d968
        A/clauses/window-07/prompt.txt: 577ac48024dffc255dc15f94ec742ce98cf7fcb4e9dc647598ca4f31384c8b3b
        A/clauses/window-07/meta.json: 84b12b77f42b143596471d369e96aeffbba66128f16496590aad1321a9da5f59
        A/clauses/window-01/raw.json: 019fa0c8fd809cab2e2d6bbd8ac23d3b499a0f6adb6ac15a5d393ca0828b325f
        A/clauses/window-01/prompt.txt: 0f08bbe04b1072689d287f49a84c41105a8510335913f09da48f7b309abea706
        A/clauses/window-01/meta.json: f1f4047a094ab8b35f8bbbb6cb6bb108d471b8ff06b1ac8c423c6ef4008f93b8
        A/clauses/window-06/raw.json: 625c964d0ca5f6f003dce54f70d654002cef2d72c67ed1c93ad77c68541706d4
        A/clauses/window-06/prompt.txt: 7915624fa0cd6f35f482d3069a1e3867a0a28c543ad053e72c3ff770a9bb7fa8
        A/clauses/window-06/meta.json: 82b713bd2b8f618c1b33848645a907b10cc4e9f60069e6111f71a6dbf6a680ff
        A/clauses/window-08/raw.json: 0355377ad3d83661bdeffb66ebea867b7dcb6e20cd8c59e47b43438415c53ba3
        A/clauses/window-08/prompt.txt: 61d650c25a65b4341e6cbc23493c77b9533ea8df2dba483fe00e06416d351861
        A/clauses/window-08/meta.json: 459a3327379a1d22873d8e01b91b286a79e7a74ac4f78f12c3c53be9af09e5dd
        A/tables/TABLE-3-page-12-5/raw.json: e1dc602fe3fef96086160b5cf2562c048f07b232cd709ec707a9bea7e5d9cb03
        A/tables/TABLE-3-page-12-5/prompt.txt: 26eaf9b8cdf1301418b0d7b5429941a847eeb1db56ec7a0177dcb6ad944c3a21
        A/tables/TABLE-3-page-12-5/meta.json: c691c131533c7bef9d132b632538d80ead25f3b3b91a6be793566e07947158c1
        A/tables/TABLE-3-page-11-4/raw.json: f75ca2c96678c7eec6701fcdd815fd3e1aa7835087e713a243bb1fdbf253d566
        A/tables/TABLE-3-page-11-4/prompt.txt: de3941571a8b0ae26ee84efc3e28e1b185229ab894736dfe8cc1923999ba2481
        A/tables/TABLE-3-page-11-4/meta.json: d90afe89f83dff591fac80dc7a3887dc476a8cec4804487989efe39c08b005eb
        A/tables/TABLE-1-page-2-1/raw.json: 4a8a30001222245ae22ef4b782b1373eef3bb894b040843b4dec41de8b44c799
        A/tables/TABLE-1-page-2-1/prompt.txt: ea843398c1ac5fd27ce0e1ed3762d7e6ff76071d81d7ad296c9aa226cceca411
        A/tables/TABLE-1-page-2-1/meta.json: c00df1572ef48dd64bbf7eca354067eaa99a99771d2676eba7e5485a5f7ba0d1
        A/tables/TABLE-3-page-10-3/raw.json: 1fa74e70801084156f42d37ae47ecb3bd705e0a2c6eed7ecfdbba10a5635ae8c
        A/tables/TABLE-3-page-10-3/prompt.txt: a41c3a284588c5302f0a11baee35b886a378c220325a1f8531a52d9cc34c8d34
        A/tables/TABLE-3-page-10-3/meta.json: 898c6dfdbdb125299eaad9b8fed0e19a5c087988f433ad593c69a622fa7186e7
        A/tables/TABLE-2-page-4-2/raw.json: b53192442c60a91be650e8c2add60a0c4f3be3786eadf887ad1e6cc222d58bff
        A/tables/TABLE-2-page-4-2/prompt.txt: d135ad1aa456b4cbbfcca3778d454e19d4f9b60d401011d3ce84ae1feb31b536
        A/tables/TABLE-2-page-4-2/meta.json: 4e78683042b387b20344314cc14fb048a09cdb87462b4ede31e8dce8e48daf18
        B/passages.json: 8ef2ee713a42a8639efb0e0c64923f0927612d88844bf1b18e9d251273cf2a90
        B/raw.json: 298a279e1bb76e0c5a8488cbd40c45a34730248780ee1468725e45e0a2571f74
        B/source-units.json: 9c24be407363cd3a441b0615a36bfefa3afb0cddddd754d8a8c1dc3fed0cff87
        B/full-source-units.json: ee96cc88aa74b5388add42a52fe8c88e8c483d0a250780178d5d04c15224fd0c
        B/meta.json: e2976886549434cc0cbccc81a977cacf154d29f788ed8d5d51322181b8e37d20
        B/table-images/TABLE-3-page-12-1.png: 22051271c4b2bab3ab54b5a67f7346b5a88b1c971265f24e47d987a38b0d1368
        B/table-images/TABLE-3-page-10-1.png: 4213e204e8c8086fb73fe00a4e36212141e23329b4505d2aa47fa761ba2b261a
        B/table-images/page-12.png: ed9a66ccf3bfce36588434bb8e0eef6dc0fd405cd2992f63e88aea6421440be6
        B/table-images/page-10.png: e324189837aae3f22778f4bc74eaceefa4e43a39f65e224056587387ecae12da
        B/table-images/page-11.png: 0e83713f9e589e0d2b71c93d85157aa8c5f1fe87fff4398eb22e2e294d1a2958
        B/table-images/TABLE-3-page-11-1.png: 29b45e31e4629149c99bbead06c139e84f20c7915eb5e18b0ee8bbaa985ef023
        B/table-images/TABLE-1-page-2-1.png: bbda21547ff3cd95408b7cb5c4d1afd2331f43692cc1438a8afbb90616b05efe
        B/table-images/page-2.png: 40b75b60131c3a475ce65cfae754248d6ada8af3165d99efc294ce357e7f14e1
        B/table-images/page-4.png: e6dcd21a323f7e0f5bbd47e28026a9931857746dfc69f9b831d291dbbee46bf7
        B/table-images/manifest.json: 30375dbf30766fe36d2168fdbd9f8102d5b66d044ffb03737e9065742d107774
        B/table-images/TABLE-2-page-4-1.png: 9a81e3e9c1432ed618ac95b3d6c34920f92911101ff21e0b50179a69eb0231e9
        B/clauses/window-11/raw.json: 3f00e170eb80fbf876528ed48b367f159bac056f44a20b730a93da5a12938553
        B/clauses/window-11/prompt.txt: a9eae13cd84b28962172f899d6d27770a0015dc07181cd0106ad1198f555f6a7
        B/clauses/window-11/meta.json: 78000e526eeb1b25b84f15ccaabecd03475ec249589128e341ad7f8a1f11c4d1
        B/clauses/window-10/raw.json: d86b2d209639aee1d3c22e94a707518aaf6ad8b2105a334293b0ea6941c020ca
        B/clauses/window-10/prompt.txt: ee4d67b66c8fb8e5cbd265389fbeb215f49aac21b05a759450aea4295631679f
        B/clauses/window-10/meta.json: 15a34a1401e667dbda9ebf135d716f2a1ccd5c78c7ed486d266ba4439eb074aa
        B/clauses/window-03/raw.json: cfd053fcece529b57139513eb1768332f355dd54067acd02a3af918d5dea97c3
        B/clauses/window-03/prompt.txt: cbb6048476815ac0d8ab39e42cf43bba9d4adf5e5f8ae63da1d92d661768b49e
        B/clauses/window-03/meta.json: 5bd78dd58865d203d2822d7e23385bfeab1b0f4f8633d32e1a582b0c7a98ff32
        B/clauses/window-04/raw.json: 56dc740aac552a36e0c5d6a767a67346c9d4d7850ceaa1de209219a89daa0892
        B/clauses/window-04/prompt.txt: 9cf1394663b40cb802f15ddfc6b0271dba5c65767e6c80d92f6de39ed3ed0e34
        B/clauses/window-04/meta.json: c0ea9a9b7d4e0e94c34c2946fe124410411891d7c257ed218b4bfa150030295d
        B/clauses/window-05/raw.json: 86fd70a4ad112a0bb82a4b5eda5d5c8490270f7366faf32fa6f00771d80e638f
        B/clauses/window-05/prompt.txt: f6e6e1c3f45aeb17124c4e0e298b8afe9eccdb8ade55df720eeaa2afb48915f3
        B/clauses/window-05/meta.json: 0acbe74dac4f8e0652e044ae56bd1f2b25276d18c139881af1904e6abe6ac0be
        B/clauses/window-02/raw.json: 339617a200f8d0552bda8ea0cabdbd31033e44629414859fa009694b8978d524
        B/clauses/window-02/prompt.txt: 4c2240073e461827dfc8466f4c21d93439cba2837554775ee5eeaf88dcc75336
        B/clauses/window-02/meta.json: 1a4548531ed1305c1b959a5e4703c78b0148614715abdc012c54ef839ba1fb00
        B/clauses/window-09/raw.json: a3a361c1122e674a062d6984a97385d7057fe3b8d280a2b923204b5d56fcf6ad
        B/clauses/window-09/prompt.txt: cb4e935cb48827d745477eff314572344175c880658bff3d00928b1873684e7e
        B/clauses/window-09/meta.json: f04e1a2bd17ad9e567090a1981a796e797108d24b6f3ff1e54db4ece67b2236d
        B/clauses/window-07/raw.json: 19b629d02ed5d910fa4ac68f1458edce47bbff5dbe970400275036cc4b589037
        B/clauses/window-07/prompt.txt: 577ac48024dffc255dc15f94ec742ce98cf7fcb4e9dc647598ca4f31384c8b3b
        B/clauses/window-07/meta.json: 6be5964047b73ca176b9ef777a6b6e67fb92b717e01dab3fc28a3cb86c294700
        B/clauses/window-01/raw.json: b445d9e469425d9613e20a7260a2f9576d320b35deb7e58d80cb79778d720bd0
        B/clauses/window-01/prompt.txt: 0f08bbe04b1072689d287f49a84c41105a8510335913f09da48f7b309abea706
        B/clauses/window-01/meta.json: eb2f00527c816253cf9007b1a6799899c6cb63401bf0f07149ffb7c3b58771bd
        B/clauses/window-06/raw.json: c288f5113271c66e5b6446c8c9287c5087a56edbc309666933436d1fd59d342c
        B/clauses/window-06/prompt.txt: 7915624fa0cd6f35f482d3069a1e3867a0a28c543ad053e72c3ff770a9bb7fa8
        B/clauses/window-06/meta.json: baf1c4a21882f9d617b384a2124a8d312cbca11d85a67642ee9f57c34c18e6bd
        B/clauses/window-08/raw.json: b29b61e904d5b3fd6393f409227c8a90719b135d6e687ea9814417c2b51b2df3
        B/clauses/window-08/prompt.txt: 61d650c25a65b4341e6cbc23493c77b9533ea8df2dba483fe00e06416d351861
        B/clauses/window-08/meta.json: d07b73d027720fa68163b44da3cbb915d8c9a3eef1f1d44997972a6b899d4eb9
        B/tables/TABLE-3-page-12-5/raw.json: e1dc602fe3fef96086160b5cf2562c048f07b232cd709ec707a9bea7e5d9cb03
        B/tables/TABLE-3-page-12-5/prompt.txt: 26eaf9b8cdf1301418b0d7b5429941a847eeb1db56ec7a0177dcb6ad944c3a21
        B/tables/TABLE-3-page-12-5/meta.json: 100898aa826ebbea3d4ff6bf14f76ca0dce979c5d012ffc9e1b64ce859854598
        B/tables/TABLE-3-page-11-4/raw.json: ead2abf6cbacae17cd07e608062e2226a13edb1c0e290a0aae0c8f7827646f17
        B/tables/TABLE-3-page-11-4/prompt.txt: de3941571a8b0ae26ee84efc3e28e1b185229ab894736dfe8cc1923999ba2481
        B/tables/TABLE-3-page-11-4/meta.json: edf8dc409703d6b8fb9f2d00d1e5955e39cc8f744dd806fa8c89e272331b33a9
        B/tables/TABLE-1-page-2-1/raw.json: 2e0d5ea085b00d6e144a741123fc5d7a9480b357cacf80efb4e0011a76497da3
        B/tables/TABLE-1-page-2-1/prompt.txt: ea843398c1ac5fd27ce0e1ed3762d7e6ff76071d81d7ad296c9aa226cceca411
        B/tables/TABLE-1-page-2-1/meta.json: 2009556c9cee77e652c1b1e022636143dd6dc33fd2f0a582a2caafc02310a38a
        B/tables/TABLE-3-page-10-3/raw.json: 5497c04f25aa28bf9b47b2da7c8dcd1d0ac71de65ab1b93b8d763ce8d6833dd6
        B/tables/TABLE-3-page-10-3/prompt.txt: a41c3a284588c5302f0a11baee35b886a378c220325a1f8531a52d9cc34c8d34
        B/tables/TABLE-3-page-10-3/meta.json: e68b45224e88a117ef3012e79a46913110ac8a8469e098acead9020fc75adb2e
        B/tables/TABLE-2-page-4-2/raw.json: b53192442c60a91be650e8c2add60a0c4f3be3786eadf887ad1e6cc222d58bff
        B/tables/TABLE-2-page-4-2/prompt.txt: d135ad1aa456b4cbbfcca3778d454e19d4f9b60d401011d3ce84ae1feb31b536
        B/tables/TABLE-2-page-4-2/meta.json: dcc086cd1f3ce6e7d40c9cde159f2df8dbf759ee607c6027f748539ec7f09b30
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
      pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
      source_review: _compare/relationships-2026-11-16/review-current/Moore2024
      source_status_sha256: 8406c408c3fc8874a4c59385f9b4a1eafa93ae728b6cee0c26350f47edd4e34b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: damage to 173 edges
    outcome:
      text: Verbal Recall deficits
    analysis_label: Network-level lesion mapping
    relation: association
    evidence_ids:
    - P5-S1-C11
    qualifier_ids:
    - P5-S1-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
      source_review: _compare/relationships-2026-11-16/review-current/Moore2024
      source_status_sha256: 8406c408c3fc8874a4c59385f9b4a1eafa93ae728b6cee0c26350f47edd4e34b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C6
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S1-C6
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - Unaccounted source passage P1-S1-C9
      - Unaccounted source passage P1-S2-C3
      - Result passage disposed without unit P4-S3-C5
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P8-S1-C5
      - Accounting without a linked unit P9-S1-C2
      - Accounting without a linked unit P9-S1-C3
      - Unaccounted source passage P9-S1-C2
      - Unaccounted source passage P9-S1-C3
      - Result passage disposed without unit P9-S1-C7
      - Result passage disposed without unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C3
      - Result passage disposed without unit P9-S2-C10
      - Accounting without a linked unit P9-S2-C8
      - Unaccounted source passage P9-S2-C8
      - Unaccounted source passage P12-S1-C10
      - Result passage disposed without unit P13-S3-C7
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 210
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S4-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
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
        source_id: P6-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: limitations
        source_ids:
        - P8-S1-C7
        - P8-S1-C8
        - P8-S1-C9
        - P8-S1-C10
        - P8-S1-C11
        - P8-S2-C4
        - P8-S2-C5
        - P13-S2-C3
        - P13-S2-C4
        - P13-S2-C5
        - P13-S2-C6
        - P13-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      - TABLE-3-page-10-3
      - TABLE-3-page-11-4
      - TABLE-3-page-12-5
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-3-page-10-3
      - TABLE-3-page-11-4
      - TABLE-3-page-12-5
      source_anomalies:
      - evidence_id: P4-S3-C6
        as_printed: p = 1.87
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S3
        - P5-S3
        - P5-S4
        - P6-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P9-S2
        - P12-S1
        - P13-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
      source_review: _compare/relationships-2026-11-16/review-current/Moore2024
      source_status_sha256: 8406c408c3fc8874a4c59385f9b4a1eafa93ae728b6cee0c26350f47edd4e34b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes: []
      reason: Summary of results; specific associations are detailed in later sections.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes: []
      reason: General summary of language results.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes: []
      reason: General summary of memory results.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes: []
      reason: General summary of number processing results.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes: []
      reason: General summary of attention results.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes: []
      reason: General summary of praxis results.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Table 2.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of impairment prevalence.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 29
      reason: Association between lesion volume and OCS performance.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Figure 2.
    - source_id: P4-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of network mapping success rate.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Figure 3.
    - source_id: P4-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Figure 4.
    - source_id: P4-S3-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Specific association for Picture Naming.
    - source_id: P4-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 content (demographics/scores).
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Specific association for Picture Naming.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifier for Picture Naming strongest predictor.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Specific association for Semantics.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifier for Semantics strongest predictor.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Specific association for Sentence Reading.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics across language tasks.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Specific association for Episodic Recognition.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Qualifier for Episodic Recognition strongest predictor.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Specific association for Orientation.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Qualifier for Orientation strongest predictor.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Specific association for Verbal Recall.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Qualifier for Verbal Recall strongest predictor.
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics across memory tasks.
    - source_id: P5-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics across memory tasks.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics across memory tasks.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Specific association for Number Writing.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Qualifier for Number Writing strongest predictor.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Specific association for Calculation.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Qualifier for Calculation strongest predictor.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap between Calculation and Number Writing.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Specific association for Cancellation Total.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Qualifier for Cancellation Total strongest predictor.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Specific association for Left Egocentric Neglect.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 10
      reason: Specific association for Left Allocentric Neglect.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Qualifier for both Left Egocentric and Allocentric Neglect.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap between neglect types.
    - source_id: P5-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap between neglect types.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics between neglect types.
    - source_id: P5-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of non-overlapping edges.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of non-overlapping edges.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Specific association for Right Egocentric Neglect.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Specific association for Right Allocentric Neglect.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Qualifier for Right Allocentric Neglect strongest predictor.
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap statistics for right neglect.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 13
      reason: Specific association for Visual Field Task.
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 13
      reason: Qualifier for Visual Field Task strongest predictor.
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 14
      reason: Specific association for Praxis impairment.
    - source_id: P5-S3-C11
      disposition: represented
      result_indexes:
      - 15
      reason: Null result for Trail Making Task.
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of SCCAN model success rate.
    - source_id: P5-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Figure 5.
    - source_id: P5-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Table 3.
    - source_id: P5-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces Table 3.
    - source_id: P5-S4-C3
      disposition: represented
      result_indexes:
      - 16
      reason: Specific association for Picture Naming (SCCAN).
    - source_id: P5-S4-C4
      disposition: represented
      result_indexes:
      - 17
      reason: Specific association for Sentence Reading (SCCAN).
    - source_id: P5-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 1 caption.
    - source_id: P5-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 1 caption.
    - source_id: P5-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 1 caption.
    - source_id: P5-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 1 caption.
    - source_id: P5-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Page footer.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 17
      reason: Specific association for Sentence Reading (SCCAN).
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 18
      reason: Null result for Semantics (SCCAN).
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 19
      reason: Null result for Orientation (SCCAN).
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 20
      - 21
      reason: Specific associations for Episodic Recognition and Verbal Recall (SCCAN).
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 20
      - 21
      reason: Qualifier for Episodic Recognition and Verbal Recall (SCCAN).
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 22
      - 23
      reason: Specific associations for Number Writing and Calculation (SCCAN).
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 22
      - 23
      reason: Qualifier for Number Writing and Calculation (SCCAN).
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 24
      reason: Specific association for Cancellation Total (SCCAN).
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 25
      reason: Specific association for Left Egocentric Neglect (SCCAN).
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 26
      reason: Null results for Right Egocentric, Left Allocentric, and Right Allocentric
        Neglect (SCCAN).
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 27
      reason: Specific association for Visual Field Task (SCCAN).
    - source_id: P6-S1-C12
      disposition: represented
      result_indexes:
      - 28
      reason: Null result for Gesture Imitation Task (SCCAN).
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 29
      reason: Specific association for Trail Making Task (SCCAN).
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 29
      reason: Specific association for Trail Making Task (SCCAN).
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of language results.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of memory results.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of memory results.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Qualifier for Orientation strongest predictor.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of orientation and default network.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of memory task completion.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right hemisphere lesions and memory.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion-mapping results for memory.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of multivariate mapping limitations.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of neglect results.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of neglect results.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of interhemispheric edges in neglect.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right neglect results.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of right allocentric neglect.
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of cancellation task.
    - source_id: P9-S2-C5
      disposition: represented
      result_indexes:
      - 24
      reason: Specific association for Cancellation Total (SCCAN).
    - source_id: P9-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of cancellation total and visual network.
    - source_id: P9-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of visual field impairment lateralization.
    - source_id: P12-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of visual field deficits.
    - source_id: P12-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of network-level analysis for visual field deficits.
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 15
      - 29
      reason: Null results for Trail Making Task.
    - source_id: P13-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample size and power.
    - source_id: P13-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion distribution.
    unresolved_coverage:
    - source_id: P1-S1-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S1-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S1-C7
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S1-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S1-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S2-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C16
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S2-C3
    - P4-S3-C4
    - P4-S3-C5
    - P4-S3-C7
    - P4-S3-C8
    - P4-S3-C9
    - P4-S3-C10
    - P4-S3-C11
    - P5-S1-C2
    - P5-S1-C4
    - P5-S1-C6
    - P5-S1-C8
    - P5-S1-C10
    - P5-S1-C12
    - P5-S1-C13
    - P5-S2-C3
    - P5-S2-C5
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C10
    - P5-S2-C13
    - P5-S2-C14
    - P5-S2-C15
    - P5-S3-C3
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C9
    - P5-S3-C12
    - P6-S1-C5
    - P6-S1-C7
    - P6-S1-C17
    - P7-S1-C6
    - P7-S1-C10
    - P7-S1-C11
    - P7-S2-C2
    - P7-S2-C4
    - P8-S1-C1
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C8
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C7
    - P9-S1-C11
    - P9-S2-C4
    - P9-S2-C5
    - P9-S2-C8
    - P9-S2-C10
    - P12-S1-C1
    - P12-S1-C3
    - P12-S1-C10
    - P13-S3-C7
    - P13-S3-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-4-2
    - TABLE-3-page-10-3
    - TABLE-3-page-11-4
    - TABLE-3-page-12-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C4
      - P3-S1-C1
      recruited_sample:
      - P2-S4-C4
      - P3-S1-C1
      eligibility:
      - P3-S1-C1
      - P3-S3-C10
      imaging_provenance:
      - P3-S3-C4
      - P3-S4-C5
      - P3-S4-C6
      imaging_timing:
      - P3-S1-C1
      - P2-S4-C9
      outcome_timing:
      - P3-S1-C1
      outcome_definition:
      - P3-S2-C11
      - P3-S3-C2
      validation:
      - P4-S2-C2
      analysis_restrictions:
      - P4-S2-C5
      - P4-S2-C11
      - P5-S4-C7
      - P6-S1-C10
      dependent_variable_statement:
      - P3-S4-C11
      - P4-S1-C13
      - P4-S2-C7
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S4-C12
      - P4-S2-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C9
      - P3-S2-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
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
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: limitations
      source_ids:
      - P8-S1-C7
      - P8-S1-C8
      - P8-S1-C9
      - P8-S1-C10
      - P8-S1-C11
      - P8-S2-C4
      - P8-S2-C5
      - P13-S2-C3
      - P13-S2-C4
      - P13-S2-C5
      - P13-S2-C6
      - P13-S2-C7
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
      pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
      review_sha256: e211a9c0f722864c45472379302ae75d52976bd643cd6f13f1153106231aa29d
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
      - P5-S1-C11
      source_result: Verbal Recall deficits were significantly associated with damage
        to 173 network edges (R2 values = 0.002–0.005, all p < 3.26 × 10−5). The strongest
        predictor of impairment was damage to streamlines connecting the left frontal
        eye fields (dorsal attentional network) and the left putamen.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the network-level lesion mapping
            results for the Verbal Recall subtest of the Oxford Cognitive Screen,
            as described in P5-S1-C11 and P5-S1-C12. The proposed core correctly identifies
            this specific outcome and method.
          source_ids:
          - P5-S1-C11
          - P5-S1-C12
          - P3-S3-C11
        direction:
          answer: fits
          reason: The source states that deficits were 'associated with damage' to
            the edges, implying that greater disconnection predicts greater impairment.
            The proposed core preserves this directionality by stating 'Verbal recall
            deficits were associated with damage to 173 network edges'.
          source_ids:
          - P5-S1-C11
          - P5-S1-C12
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to network edges
            (disconnection). The outcome is Verbal Recall deficits. The patient measurement
            is correctly classified as template_lesion_overlap, as the method involves
            overlaying patient lesion masks on a population-averaged disconnectome
            atlas (HCP-842) to estimate disconnectivity, rather than performing patient-specific
            diffusion tractography.
          source_ids:
          - P5-S1-C11
          - P3-S4-C4
          - P3-S4-C5
          - P3-S4-C8
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that lesion volume
            was included as a covariate of no interest (P3-S4-C12) and that results
            survived multiple comparison corrections (P4-S1-C1, P4-S1-C2). These are
            material qualifiers present in the source.
          source_ids:
          - P3-S4-C12
          - P4-S1-C1
          - P4-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes relevant limitations such as the retrospective
            nature of the analysis and the inability to distinguish pre-morbid from
            post-stroke impairments (P8-S2-C4). No material caveats that would change
            the interpretation of the association are omitted.
          source_ids:
          - P8-S2-C4
          - P13-S3-C8
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 593
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: assessment and neuroimaging within 31 days of stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 31'
    analysis_identity:
      id: R006
      exposure:
        text: damage to 173 edges
      outcome:
        text: Verbal Recall deficits
      analysis_label: Network-level lesion mapping
      relation: association
      evidence_ids:
      - P5-S1-C11
      qualifier_ids:
      - P5-S1-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
        source_review: _compare/relationships-2026-11-16/review-current/Moore2024
        source_status_sha256: 8406c408c3fc8874a4c59385f9b4a1eafa93ae728b6cee0c26350f47edd4e34b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 542ac5068971063205e71ce3fe31837632b69db85aab01392152622eaee5e8c6
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fb0bca677f0a068169b9658de7e971780f3a166aab9be448d50641493bc6d172
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: ebee1d53e4d213a7c900faee1aa2805fc821926a9a9f0ba63797571a79e63903
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: '

          (Health

          Research

          Authority

          UK

          (REC

          references:14/LO/0648,

          18/SC/0550, 12/WM/00335). Patients were included in the present

          analysis if they completed the Oxford Cognitive Screen (OCS) within 31

          days of stroke and had available acute neuroimaging (within 31 days of

          stroke) which was of sufficient quality to facilitate lesion delineation.
          Of

          the 1198 patients recruited in the OCS Programme, 398 were excluded

          from this analysis for having no useable neuroimaging data. Ninety-six

          patients were excluded due to evidence of multiple, temporally

          distinct stroke lesions. One hundred and thirteen additional patients

          were excluded due to OCS or neuroimaging data being collected >31

          days post stroke.

          2.2. Behavioural data

          Cognitive status was assessed using the Oxford Cognitive Screen

          (OCS; Demeyere et al., 2015). The OCS is a short, stroke-specific

          cognitive screen designed for use in acute stroke settings. It yields 16

          distinct measures summarising cognitive impairments across commonly

          impacted cognitive domains: executive function, language, memory,

          number processing, praxis, and visuospatial attention (Demeyere et al.,

          2015, 2016). This measure is designed to be inclusive for patients with

          common stroke-related impairments including aphasia, visuospatial

          neglect, primary visual impairments (e.g. hemianopia), and primary

          motor impairments (e.g. hemiplegia) (Demeyere et al., 2015, 2016).

          The OCS executive function domain is assessed using a modified

          (shape-based) trail making task. The OCS language domain consists of a

          picture naming task (images of four objects/animals), a semantics task

          (follow verbally presented instructions), and a sentence reading task.

          The OCS memory domain includes a delayed recall of the previously

          read sentence (verbal recall task), an incidental multiple-choice recall
          of

          stimuli and tasks completed earlier in the OCS (episodic recognition

          task), and 4 items assessing the participant’s orientation in time and

          location (orientation task). The OCS numerical processing domain in-

          cludes a number tasks in which participants are asked to write three

          verbally presented numbers (in digits) and a calculation task where

          participants are asked to solve four simple addition and subtraction

          '
        anchor_text: '(Health

          Research

          Authority

          UK

          (REC

          references:14/LO/0648,

          18/SC/0550, 12/WM/00335). Patients were included in the present

          analysis if they completed the Oxford Cognitive Screen (OCS) within 31

          days of stroke and had available acute neuroimaging (within 31 days of

          stroke) which was of sufficient quality to facilitate lesion delineation.
          Of

          the 1198 patients recruited in the OCS Programme, 398 were excluded

          from this analysis for having no useable neuroimaging data. Ninety-six

          patients were excluded due to evidence of multiple, temporally

          distinct stroke lesions. One hundred and thirteen additional patients

          were excluded due to OCS or neuroimaging data being collected >31

          days post stroke.

          2.2. Behavioural data

          Cognitive status was assessed using the Oxford Cognitive Screen

          (OCS; Demeyere et al., 2015). The OCS is a short, stroke-specific

          cognitive screen designed for use in acute stroke settings. It yields 16

          distinct measures summarising cognitive impairments across commonly

          impacted cognitive domains: executive function, language, memory,

          number processing, praxis, and visuospatial attention (Demeyere et al.,

          2015, 2016). This measure is designed to be inclusive for patients with

          common stroke-related impairments including aphasia, visuospatial

          neglect, primary visual impairments (e.g. hemianopia), and primary

          motor impairments (e.g. hemiplegia) (Demeyere et al., 2015, 2016).

          The OCS executive function domain is assessed using a modified

          (shape-based) trail making task. The OCS language domain consists of a

          picture naming task (images of four objects/animals), a semantics task

          (follow verbally presented instructions), and a sentence reading task.

          The OCS memory domain includes a delayed recall of the previously

          read sentence (verbal recall task), an incidental multiple-choice recall
          of

          stimuli and tasks completed earlier in the OCS (episodic recognition

          task), and 4 items assessing the participant’s orientation in time and

          location (orientation task). The OCS numerical processing domain in-

          cludes a number tasks in which participants are asked to write three

          verbally presented numbers (in digits) and a calculation task where

          participants are asked to solve four simple addition and subtraction'
        excluded_fragments: []
        image_sha256: c3e45d8cca1953b30e067efe2ab3034e2f740f68ca43bd7b7b1558cc7494ace8
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Verbal Recall deficits were associated with damage to 173

    edges (R2 values = 0.002–0.005, all p < 3.26 × 10−5).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
