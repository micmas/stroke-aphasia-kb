---
id: left_atr
name: left ATR cluster
kind: network
findings:
- id: f1
  target: semantic_fluency
  target_kind: impairment
  claim: The lesion percentage of the left ATR was significantly correlated with two
    semantic fluency cues and marginally significantly correlated with one semantic
    fluency cue.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 51
    population: right-handed stroke patients
    phase: not_reported
    time_post_onset: at least 1-month post-onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The number of patients with different lesions was not equivalent across tracts
  - The sample included a high proportion of aphasic patients
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the left anterior thalamic
    radiation (ATR) tract template from the JHU white-matter tractography atlas (25%-threshold
    sub-template), expressed as a lesion percentage (number of voxels with lesion
    divided by total number of voxels on the tract). The association was tested using
    corrected t scores for each cue; Results for each cue were adjusted using the
    Bonferroni correction method. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S3-C4, two-model
    agreement, human verification pending): Patients

    Fifty-one right-handed stroke patients (40 males) were chosen from the China Rehabilitation
    Research Center Original text-layer quotation is preserved below. PDF image reading
    (P2-S3-C5, two-model agreement, human verification pending): . They all suffered
    from their

    first brain injury, which was at least 1-month post-onset (mean=11.9

    months; SD=34.4; range: 1–184 months) Original text-layer quotation is preserved
    below. PDF image reading (P10-S1-C13, two-model agreement, human verification
    pending): . First, although

    we sought to recruit a variety of lesion distributions in our patients, the

    numbers of patients with different lesions were not equivalent across

    tracts (see Table 1) Original text-layer quotation is preserved below.'
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
    - proposed_concept:semantic_fluency
  citation: '@Li2017'
  source_passages:
  - section: Original source P5-S2-C1
    page: 5
    quote: 'Performance on each of the three cues in semantic ﬂuency task was

      signiﬁcantly correlated with the lesion percentages of four tracts: the

      left IFOF (r=−0.55 to −0.46, corrected p-values < 0.05), left SLF

      (r=−0.59 to −0.53, corrected p-values < 0.01), left UF (r=−0.52 to

      −0.41, corrected p-values < 0.05) and left FAT (r=−0.50 to −0.49,

      corrected p-values < 0.01), however, the left ATR was signiﬁcantly

      correlated with two cues of semantic ﬂuency (r=−0.47 and −0.47,

      corrected p-values < 0.01) and marginally signiﬁcantly correlated with

      one semantic cue (r=−0.39 corrected p-values < 0.06).'
    supports: claim
  - section: Original source P2-S3-C4
    page: 2
    quote: 'Patients

      Fifty-one right-handed stroke patients (40 males) were chosen from

      the China Rehabilitation Research Center.'
    supports: sample
  - section: Original source P2-S3-C5
    page: 2
    quote: 'They all suﬀered from their

      ﬁrst brain injury, which was at least 1-month post-onset (mean=11.9

      months; SD=34.4; range: 1–184 months).'
    supports: sample
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Twenty tracts were extracted from the “JHU white-matter

      tractography atlas” (Hua et al., 2008) in the FMRIB Software Library

      (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases).'
    supports: method
  - section: Original source P4-S2-C4
    page: 4
    quote: 'We

      used

      the

      25%-

      threshold sub-template.'
    supports: method
  - section: Original source P4-S2-C9
    page: 4
    quote: 'For each of the

      remaining 19 tracts, the lesion percentage (number of voxels with

      lesion divided by total number of voxels on the tract) was correlated

      with the corrected t scores of each cue of semantic (and phonological)

      ﬂuency tasks across 51 patients.'
    supports: method
  - section: Original source P4-S2-C11
    page: 4
    quote: 'The results for each cue were adjusted for the 19

      tracts with the Bonferroni correction method (p < 0.0026, corrected

      p < 0.05).

      2.4.2.'
    supports: method
  - section: Original source P10-S1-C13
    page: 10
    quote: 'First, although

      we sought to recruit a variety of lesion distributions in our patients, the

      numbers of patients with diﬀerent lesions were not equivalent across

      tracts (see Table 1).'
    supports: limitation
  - section: Original source P10-S2-C4
    page: 10
    quote: 'Therefore,

      our patient sample included a high proportion of aphasic patients.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Li2017
  proposal_id: R002
  review_status_sha256: 1d0b37c8ba7d2851af794d88451ca5eeb3c42b8b5788de019fccca5d6c7ba6f9
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
        A/passages.json: c445588aa3a968c6644b6de5b05ddc5ac9f851a7ad1ae5290cd718b0b6829980
        A/raw.json: 64f822998badf347d0174dfad84b9e54eb84617a05d926e20c77bb285f266938
        A/source-units.json: 0732a8640b1adaa59eb0d4f08154bf7c5cae7f821af02ef4cb82063dacc48a7a
        A/full-source-units.json: 7bdaab92a5eb26efb98e4cdf752ff65ec7130171407754a03cf46a1e93960970
        A/meta.json: 54e828ac118bc6756c10073d69d3a99855c817dc91dbe6bffda4ce70f738c878
        A/table-images/TABLE-1-page-3-1.png: 00691253998ddb8505392d9cab6ad4f7611d2af66ee416a846f2c0eabc6e4cea
        A/table-images/page-3.png: 3df1e3ec966dc4daa1e2b8c3c5858b913e704e382fdbdc4bdfa28b01fdf26d53
        A/table-images/TABLE-3-page-8-1.png: 9dca4d248b9ea028ee4aef09d86ec6656517a1de41bf1c637937fc6d65261531
        A/table-images/page-5.png: d77907076e364e350fa154793f122271946a006317e67889cd7e85587fcecac9
        A/table-images/page-8.png: 0a07aa7e6417866b95fbf79ddcc4a7241bf2e05dec267d974e37e550cd85350f
        A/table-images/manifest.json: f9ee9454eeaab2b0f89c8ddcf81a3a5295e12c3f8438eef3c879beff709177c4
        A/table-images/TABLE-2-page-5-1.png: 9c47babe4c1c9c2ce8742a5b0b412b673206ec2eaca226aef59483d82d2140ca
        A/clauses/window-03/raw.json: 3812a445621ab57eec0466b7dd6275e0274803f1c87331f0450b75619491b9a3
        A/clauses/window-03/prompt.txt: 04ce4a9a7537ee1eded3cf8f176fbae822086bf55f65b0a52f9264f01914161c
        A/clauses/window-03/meta.json: ea74a0bc0dc88020f5f27959fd59d3e32c48ed1ecf0ed762adaf1dc57cf55c97
        A/clauses/window-04/raw.json: 112332ea77b95650c4602c28a3ee7cba7323c7d4c2a8464c946aa58e4f7c75d9
        A/clauses/window-04/prompt.txt: 770294b48d5490a876c1050fbb78b6913a4d0b47e24eb1725431e611c58a4990
        A/clauses/window-04/meta.json: 64f20fc5ed9720fdf5bceeb2d5e36264730858c180302ed9d661dd69b29f4bf6
        A/clauses/window-05/raw.json: 59a47b147fc986b44d22a6252b4646acbcc09a02efee7d3ab21b7bc262a407d2
        A/clauses/window-05/prompt.txt: e172d0c8a3fb26c775b4b657e2568db4ca1d5f86eb7b7928c465b254a8d15b96
        A/clauses/window-05/meta.json: 751b3c3b4d011dde8fb44728f3c74d9b42500d74642ff7fbc6c348f9856ffe9e
        A/clauses/window-02/raw.json: 81bfea177ec23c70af36d6f0af6bf4821e679879f771d89b72423cf954d14936
        A/clauses/window-02/prompt.txt: 69176e57d2c7a512c7252ef6f29c4b67275604cc3911eec8c4280faa139fc03e
        A/clauses/window-02/meta.json: cd468c5140074ee908b4385c254209c13b38298c7f88a251cacde6ca0279352e
        A/clauses/window-09/raw.json: 66c2d7926a3ddbf671ab34f0ed53823fbbf106032b4cce432484ae16ea04b3b6
        A/clauses/window-09/prompt.txt: 36b643668de19ecc1b81ba8964b94e0893b5b999d08ac62b62613b77cebdfe42
        A/clauses/window-09/meta.json: 74348c92bf7d3fbc60e3942a65a868ffc02c25678d4a3f4a4867331dba4990e8
        A/clauses/window-07/raw.json: bceeff3e67eab9ef9502f324160be4b82f4d248d2be206b3877155aebebdb082
        A/clauses/window-07/prompt.txt: 103156160b79265ca9048ccc386063987511b89c5b2a5e01a7bcddf2f825143c
        A/clauses/window-07/meta.json: 0bd41a2e5f1b255d02be9bf5cb765c1fc18333d62e379d1a588bab5cb2ee11a5
        A/clauses/window-01/raw.json: 79596c0b12e80358bd42489498fa4d727f78c2dc905f7e443c321e278cdc0b4e
        A/clauses/window-01/prompt.txt: 942b6486d7420cc5d10e23593394f90db7802ce6d1dcf08b967aba40a311e1c6
        A/clauses/window-01/meta.json: 61cff504360d158c616ff2f1b4a9e53fbdec66404d6e5d5472e8b5e0c3208ca1
        A/clauses/window-06/raw.json: c2b0fe3a28c9b9d6fbccee77743d6013955cdd18c78c243e9f23c71f15bcfe08
        A/clauses/window-06/prompt.txt: 9335b5b0b92c44a1543270c6a7cb19bb385b117c2233e5ff0198216331e76b06
        A/clauses/window-06/meta.json: bfc533d671a49849885d0f5d3d108d788b91ee8303558d370e160ced2846c0a3
        A/clauses/window-08/raw.json: 74f83bad7a5584ef304e1fc8157489544310417033017e7f6eed7bccaec72818
        A/clauses/window-08/prompt.txt: 5ca87aeb79f6db9fe591b0b4f1a1d6ed3a6ad117200bfbf16c1d531e865b0fa4
        A/clauses/window-08/meta.json: 6967ff3a52f8d2172d7d889e83f6f27e817589eef6e6a5f001f41ab919036a49
        A/tables/TABLE-2-page-5-2/raw.json: 8157457e59b877c91f661505d120740fc5d7c0ef0f7770adc6ca65a33f75ee02
        A/tables/TABLE-2-page-5-2/prompt.txt: 5af9e2cdadbc09b6667c93bef69b806174b9f16cc9a76779d74a3637cad75679
        A/tables/TABLE-2-page-5-2/meta.json: fa540525074f3f5d6eed0ac08b4950ae898668b163cfcde163d3df80165d9724
        A/tables/TABLE-3-page-8-3/raw.json: 99cd407419b811063334db0a64572d4400788c464048c8dd844153e47e85cab0
        A/tables/TABLE-3-page-8-3/prompt.txt: c76d2ec0ae550ae7aabf804052f158da0a2759a6aa24d128af9bb204ba61f150
        A/tables/TABLE-3-page-8-3/meta.json: 1f7486e709fd5826e31cdd7e843432983282c713ad44a9c69eb19ecfff906a54
        A/tables/TABLE-1-page-3-1/raw.json: 7f5bb70158f280d1f8b3d115d390c3264e8d2524d27721d5a56c141269b165f5
        A/tables/TABLE-1-page-3-1/prompt.txt: 03bf24efe5a46bb8ee38a0d36cffec11593eced88d4de1ca3bb07a461e38b117
        A/tables/TABLE-1-page-3-1/meta.json: 32a3fe4024a71ebf6245f2ef51653da5d7d6998e14f5728b800bafa77c890fbf
        B/passages.json: c445588aa3a968c6644b6de5b05ddc5ac9f851a7ad1ae5290cd718b0b6829980
        B/raw.json: ac78b76fa94c4cdf01025f4c7e8b2820cc0d4c839ee1e325d46e34a2feb36290
        B/source-units.json: 0732a8640b1adaa59eb0d4f08154bf7c5cae7f821af02ef4cb82063dacc48a7a
        B/full-source-units.json: 7bdaab92a5eb26efb98e4cdf752ff65ec7130171407754a03cf46a1e93960970
        B/meta.json: fb19b2174b4afa7af3d143abb77b3ae698995e9b218e9627f8a74088f00cf3b1
        B/table-images/TABLE-1-page-3-1.png: 00691253998ddb8505392d9cab6ad4f7611d2af66ee416a846f2c0eabc6e4cea
        B/table-images/page-3.png: 3df1e3ec966dc4daa1e2b8c3c5858b913e704e382fdbdc4bdfa28b01fdf26d53
        B/table-images/TABLE-3-page-8-1.png: 9dca4d248b9ea028ee4aef09d86ec6656517a1de41bf1c637937fc6d65261531
        B/table-images/page-5.png: d77907076e364e350fa154793f122271946a006317e67889cd7e85587fcecac9
        B/table-images/page-8.png: 0a07aa7e6417866b95fbf79ddcc4a7241bf2e05dec267d974e37e550cd85350f
        B/table-images/manifest.json: 54509091cba974d49f6339b1fcf889026b1ec86366f54754c5a47a8ef191e710
        B/table-images/TABLE-2-page-5-1.png: 9c47babe4c1c9c2ce8742a5b0b412b673206ec2eaca226aef59483d82d2140ca
        B/clauses/window-03/raw.json: 01bbc815a6528d3e8285263c4573b694323f8ac8bed7cc1938329b33c5f9c397
        B/clauses/window-03/prompt.txt: 04ce4a9a7537ee1eded3cf8f176fbae822086bf55f65b0a52f9264f01914161c
        B/clauses/window-03/meta.json: 94544cc8584de860796fbeed961aabf59b75a06d83e64acdbce3be71e1e2410b
        B/clauses/window-04/raw.json: 647f7f71973dd8388d676eb15a01bd85a50e11f303a8741f7af0139066f395a7
        B/clauses/window-04/prompt.txt: 770294b48d5490a876c1050fbb78b6913a4d0b47e24eb1725431e611c58a4990
        B/clauses/window-04/meta.json: 191da150eb64a7b51acefabc726e8f65fe7bdc1276c5596ea7d26b2a031ae52f
        B/clauses/window-05/raw.json: db49251090f7576e564cd543827ef46c6d49770de23418a87fb6fec5de80dcd0
        B/clauses/window-05/prompt.txt: e172d0c8a3fb26c775b4b657e2568db4ca1d5f86eb7b7928c465b254a8d15b96
        B/clauses/window-05/meta.json: 04d21c21a9af2238c40479f7a9cb94bbc1587f5c575655f17b23beed4aebb70d
        B/clauses/window-02/raw.json: 68781747a7740f3fe79b62d1baba4ed7acb66fcbc1c81a4070dbacb349ac064f
        B/clauses/window-02/prompt.txt: 69176e57d2c7a512c7252ef6f29c4b67275604cc3911eec8c4280faa139fc03e
        B/clauses/window-02/meta.json: 856ff9929183ec38d41dc4fe90d02253292b03a9365091d049119519a212cc21
        B/clauses/window-09/raw.json: 9c08afbc23ce1fc5f115e1c152b0c45624b8654544c0882afde33b49c72ed9a7
        B/clauses/window-09/prompt.txt: 36b643668de19ecc1b81ba8964b94e0893b5b999d08ac62b62613b77cebdfe42
        B/clauses/window-09/meta.json: 4ed9b2d4aa7282dc2e4352a55041d2190211191921460ad9506f99121ac0f020
        B/clauses/window-07/raw.json: 40dfe1c4d035ed4533bdbb866981f930c98e904d62e119669218170287f50a79
        B/clauses/window-07/prompt.txt: 103156160b79265ca9048ccc386063987511b89c5b2a5e01a7bcddf2f825143c
        B/clauses/window-07/meta.json: 388123b524f6610c15367e142aac62e6d691907c8d88ce031ea1e6645606684d
        B/clauses/window-01/raw.json: 63918e78e20721282318c384a1a82d14b3801a7be42d0b2a840028211da86f50
        B/clauses/window-01/prompt.txt: 942b6486d7420cc5d10e23593394f90db7802ce6d1dcf08b967aba40a311e1c6
        B/clauses/window-01/meta.json: adaf84c90774bbecd67884a7c29111a6d0f13a4a8535c420c48c042e2a764c34
        B/clauses/window-06/raw.json: f367a8702c24cb1b926133eb2cc43578fe7b31d767997032a0657a8dc39f8a1a
        B/clauses/window-06/prompt.txt: 9335b5b0b92c44a1543270c6a7cb19bb385b117c2233e5ff0198216331e76b06
        B/clauses/window-06/meta.json: 7bbf8d38c309869f033523df711e8026bb6d83b0829e66f340385f17fee5b60a
        B/clauses/window-08/raw.json: bf88ddd9ec218a6d9081e7d5b82bca8b249992ed9ff2b3636fbb0f4930799c5f
        B/clauses/window-08/prompt.txt: 5ca87aeb79f6db9fe591b0b4f1a1d6ed3a6ad117200bfbf16c1d531e865b0fa4
        B/clauses/window-08/meta.json: 36707f3a9365f9a6eb6a417c4a024ab7921b1bf7a5c019c46473a08b47b7008e
        B/tables/TABLE-2-page-5-2/raw.json: 0a7e42100e2ff4b0e821b13fc554bc1f2c008c0edde85c526b47bf9c38de5bb8
        B/tables/TABLE-2-page-5-2/prompt.txt: 5af9e2cdadbc09b6667c93bef69b806174b9f16cc9a76779d74a3637cad75679
        B/tables/TABLE-2-page-5-2/meta.json: cb491993e3bcb415dc70226f9999a2db1cf3826c1928fff74bb884bcb1cf6270
        B/tables/TABLE-3-page-8-3/raw.json: 00e84e25335320612f5ea8307a58014b983c6f6dbb96eaf853f1469f94e87df9
        B/tables/TABLE-3-page-8-3/prompt.txt: c76d2ec0ae550ae7aabf804052f158da0a2759a6aa24d128af9bb204ba61f150
        B/tables/TABLE-3-page-8-3/meta.json: 112fab3fd81b6f9c8066810e91c0f450c642e7445f0580b8f1394d1e7f43ccb0
        B/tables/TABLE-1-page-3-1/raw.json: 8ea265f6508b199595bd78aafcef94725c1f24fdd7ada6e38086fa8708df6132
        B/tables/TABLE-1-page-3-1/prompt.txt: 03bf24efe5a46bb8ee38a0d36cffec11593eced88d4de1ca3bb07a461e38b117
        B/tables/TABLE-1-page-3-1/meta.json: fca0071c1383a54320a2f44b97e6b524e54da26d8782131486b0314be12c675d
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
      pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
      source_review: _compare/relationships-2026-11-16/review-current/Li2017
      source_status_sha256: fbf65f4a844a9c26994044efa396a36b9a92c44cbf42c8a6dd43b174c58eeb74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: left ATR lesion percentage
    outcome:
      text: semantic fluency (two cues)
    analysis_label: Lesion-behavior correlation
    relation: association
    evidence_ids:
    - P5-S2-C1
    qualifier_ids:
    - P5-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
      source_review: _compare/relationships-2026-11-16/review-current/Li2017
      source_status_sha256: fbf65f4a844a9c26994044efa396a36b9a92c44cbf42c8a6dd43b174c58eeb74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C5'
      - Result passage disposed without unit P1-S1-C5
      - Accounting without a linked unit P2-S3-C10
      - Unaccounted source passage P2-S3-C10
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P7-S1-C2
      - 'window 17: invalid/duplicate disposition P7-S2-C2'
      - Result passage disposed without unit P7-S2-C4
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P9-S3-C4
      - 'window 21: invalid/duplicate disposition P9-S3-C13'
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S2-C2
      - Result passage disposed without unit P10-S2-C6
      - Accounting without a linked unit P10-S2-C7
      - Unaccounted source passage P10-S2-C7
      unattached_null_or_qualifier_ids:
      - P8-S1-C7
      - P10-S2-C2
      suppressed_nonrepresented_units: 18
      default_disposition_count_requires_completeness_check: 183
      unselected_timing_passages:
      - P2-S2-C13
      - P2-S3-C5
      - P2-S3-C7
      - P4-S3-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S4-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C3
        - P2-S2-C11
        - P2-S3-C4
        - P3-S2-C12
        - P4-S2-C9
        - P4-S3-C2
        - P4-S3-C11
        - P5-S3-C1
        - P6-S2-C6
        - P8-S1-C2
        - P10-S1-C13
        - P10-S2-C2
        - P10-S2-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C3
        - P2-S2-C11
        - P2-S3-C4
        - P2-S4-C14
        - P3-S2-C12
        - P4-S2-C9
        - P4-S3-C2
        - P5-S3-C1
        - P6-S2-C6
        - P8-S1-C2
        - P10-S1-C13
        - P10-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C3
        - P3-S1-C6
        - P3-S1-C7
        - P3-S1-C8
        - P4-S2-C3
        - P4-S2-C6
        - P4-S3-C13
        - P4-S4-C3
        - P5-S1-C12
        - P5-S3-C1
        - P6-S2-C7
        - P8-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C3
        - P2-S2-C5
        - P4-S3-C6
        - P4-S3-C12
        - P4-S4-C1
        - P4-S4-C4
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C10
        - P8-S1-C10
        - P8-S2-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S1-C10
        - P2-S2-C2
        - P2-S2-C4
        - P9-S3-C12
        - P10-S1-C12
        - P10-S1-C13
        - P10-S1-C14
        - P10-S1-C15
        - P10-S1-C16
        - P10-S2-C2
        - P10-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P2-S2-C13
        - P2-S3-C7
        - P2-S3-C9
        - P2-S3-C10
        - P2-S4-C14
        - P6-S1-C7
        - P6-S1-C10
        - P6-S2-C4
        - P8-S1-C3
        - P8-S1-C10
        - P8-S2-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C5
        - P3-S1-C2
        - P3-S1-C3
        - P3-S2-C5
        - P3-S2-C9
        - P4-S3-C5
        - P4-S3-C10
        - P5-S1-C4
        - P5-S1-C5
        - P6-S1-C8
        - P6-S1-C11
        - P6-S2-C2
        - P6-S2-C5
        - P7-S1-C4
        - P7-S1-C8
        - P7-S2-C2
        - P7-S2-C3
        - P8-S1-C3
        - P8-S1-C10
        - P8-S2-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P2-S2-C12
        - P2-S2-C13
        - P2-S2-C14
        - P2-S3-C4
        - P2-S3-C5
        - P2-S3-C7
        - P2-S3-C8
        - P2-S3-C9
        - P2-S4-C14
        - P3-S2-C12
        - P4-S3-C7
        - P4-S3-C8
        - P5-S1-C11
        - P5-S1-C12
        - P6-S2-C6
        - P8-S1-C10
        - P8-S2-C1
        - P10-S1-C15
        - P10-S2-C2
        - P10-S2-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - limitations
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-3-page-8-3
      unlinked_tables:
      - TABLE-3-page-8-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P3-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
      source_review: _compare/relationships-2026-11-16/review-current/Li2017
      source_status_sha256: fbf65f4a844a9c26994044efa396a36b9a92c44cbf42c8a6dd43b174c58eeb74
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Abstract summary of the primary findings regarding the five left-lateralized
        tracts.
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 14
      reason: Abstract statement on persistence of effects after ruling out confounding
        factors.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 20
      reason: Abstract statement on unique contributions of ATR, IFOF, and UF to semantic
        fluency.
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes comparability of subject groups.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological note on raw vs standardized scores.
    - source_id: P3-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 1 behavioral performance data (group differences).
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes exclusion of tracts with few lesions.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General behavioral result (patients < healthy).
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General behavioral result (low t scores).
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between different fluency cues.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion distribution.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General FA reduction in patients.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Introduces lesion-behavior correlation results.
    - source_id: P5-S2-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Specific lesion-behavior correlations for semantic fluency.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 3
      - 4
      - 5
      reason: Specific lesion-behavior correlations for phonological fluency.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Lesion correlations for right corticospinal tract and right FAT.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 8
      reason: FA-behavior correlations for semantic fluency.
    - source_id: P5-S3-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      reason: Table 2 contains the primary correlation coefficients for all tracts
        and cues.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 legend/significance levels.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Restatement of FA-behavior correlations for semantic fluency.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: FA-behavior correlations for phonological fluency.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      - 13
      reason: FA correlations for left CT, temporal SLF, right CT, and left ILF/FAT.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation of total lesion volume with composite scores.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 14
      reason: Sensitivity result for lesion percentages controlling for total lesion
        volume.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 14
      reason: Sensitivity result for FA values controlling for total lesion volume.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation of aphasia type with fluency scores.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 15
      reason: Sensitivity result for lesion percentages controlling for aphasia type.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Aphasia type correlation p-value.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 15
      reason: Sensitivity result for lesion percentages controlling for aphasia type
        (including UF null).
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Sensitivity result for FA values controlling for aphasia type.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation of illness duration with composite scores.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 16
      reason: Sensitivity result controlling for duration of illness.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Sensitivity result for subset of patients (3-10 months duration).
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 16
      reason: Continuation of results for 3-10 month onset group.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: VLSM results (grey matter regions).
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 17
      reason: Sensitivity result for FA values controlling for grey-matter lesion
        volumes.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 18
      reason: Sensitivity result for lesion percentages (ATR, SLF) controlling for
        grey-matter.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 18
      reason: Sensitivity result for lesion percentages (phonological) controlling
        for grey-matter.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation of control tasks with fluency scores.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 19
      reason: Sensitivity result controlling for nonverbal control task performance.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 20
      reason: 'Dissociation analysis: unique contribution of ATR, IFOF, UF to semantic
        fluency.'
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 20
      reason: Null results for other tracts in dissociation analysis.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 8
      - 9
      reason: Discussion restatement of primary findings.
    - source_id: P8-S1-C3
      disposition: repeated
      result_indexes:
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      reason: Discussion restatement of sensitivity results.
    - source_id: P8-S1-C4
      disposition: repeated
      result_indexes:
      - 20
      reason: Discussion restatement of dissociation results.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      reason: Table 3 contains partial correlation coefficients for all sensitivity
        analyses.
    - source_id: P9-S1-C1
      disposition: repeated
      result_indexes:
      - 20
      reason: Discussion restatement of dissociation results.
    - source_id: P10-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 8
      - 9
      reason: Conclusion restatement of primary findings.
    - source_id: P10-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 8
      - 9
      reason: Conclusion restatement of primary findings.
    - source_id: P10-S2-C8
      disposition: repeated
      result_indexes:
      - 20
      reason: Conclusion restatement of dissociation results.
    - source_id: P10-S2-C9
      disposition: repeated
      result_indexes:
      - 20
      reason: Conclusion restatement of dissociation results.
    unresolved_coverage:
    - source_id: P5-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C5
    - P1-S2-C3
    - P2-S3-C10
    - P3-S1-C4
    - P3-S3-C1
    - P4-S2-C8
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C11
    - P5-S1-C12
    - P5-S1-C13
    - P6-S1-C7
    - P6-S1-C10
    - P6-S1-C11
    - P6-S2-C1
    - P6-S2-C4
    - P6-S2-C6
    - P7-S1-C2
    - P7-S1-C7
    - P7-S2-C4
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C6
    - P8-S1-C7
    - P9-S1-C1
    - P9-S1-C2
    - P9-S3-C4
    - P10-S1-C11
    - P10-S2-C2
    - P10-S2-C6
    - P10-S2-C7
    - P10-S2-C8
    - P10-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    - TABLE-3-page-8-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P2-S2-C12
      - P2-S2-C14
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation:
      - P3-S2-C9
      - P4-S3-C5
      - P6-S1-C6
      - P8-S1-C8
      analysis_restrictions:
      - P4-S2-C8
      - P4-S3-C11
      - P4-S4-C2
      dependent_variable_statement:
      - P1-S1-C3
      - P2-S2-C5
      - P3-S2-C7
      - P4-S2-C9
      limitations: []
      personal_factors: []
      tested_personal_effects:
      - P6-S1-C10
      - P6-S2-C4
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: not_stated
    imaging_vs_outcome: concurrent
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S4-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C3
      - P2-S2-C11
      - P2-S3-C4
      - P3-S2-C12
      - P4-S2-C9
      - P4-S3-C2
      - P4-S3-C11
      - P5-S3-C1
      - P6-S2-C6
      - P8-S1-C2
      - P10-S1-C13
      - P10-S2-C2
      - P10-S2-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C3
      - P2-S2-C11
      - P2-S3-C4
      - P2-S4-C14
      - P3-S2-C12
      - P4-S2-C9
      - P4-S3-C2
      - P5-S3-C1
      - P6-S2-C6
      - P8-S1-C2
      - P10-S1-C13
      - P10-S2-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C3
      - P3-S1-C6
      - P3-S1-C7
      - P3-S1-C8
      - P4-S2-C3
      - P4-S2-C6
      - P4-S3-C13
      - P4-S4-C3
      - P5-S1-C12
      - P5-S3-C1
      - P6-S2-C7
      - P8-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C3
      - P2-S2-C5
      - P4-S3-C6
      - P4-S3-C12
      - P4-S4-C1
      - P4-S4-C4
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C10
      - P8-S1-C10
      - P8-S2-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S1-C10
      - P2-S2-C2
      - P2-S2-C4
      - P9-S3-C12
      - P10-S1-C12
      - P10-S1-C13
      - P10-S1-C14
      - P10-S1-C15
      - P10-S1-C16
      - P10-S2-C2
      - P10-S2-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P2-S2-C13
      - P2-S3-C7
      - P2-S3-C9
      - P2-S3-C10
      - P2-S4-C14
      - P6-S1-C7
      - P6-S1-C10
      - P6-S2-C4
      - P8-S1-C3
      - P8-S1-C10
      - P8-S2-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S2-C5
      - P3-S2-C9
      - P4-S3-C5
      - P4-S3-C10
      - P5-S1-C4
      - P5-S1-C5
      - P6-S1-C8
      - P6-S1-C11
      - P6-S2-C2
      - P6-S2-C5
      - P7-S1-C4
      - P7-S1-C8
      - P7-S2-C2
      - P7-S2-C3
      - P8-S1-C3
      - P8-S1-C10
      - P8-S2-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P2-S2-C12
      - P2-S2-C13
      - P2-S2-C14
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S4-C14
      - P3-S2-C12
      - P4-S3-C7
      - P4-S3-C8
      - P5-S1-C11
      - P5-S1-C12
      - P6-S2-C6
      - P8-S1-C10
      - P8-S2-C1
      - P10-S1-C15
      - P10-S2-C2
      - P10-S2-C4
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
      pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
      review_sha256: 1d0b37c8ba7d2851af794d88451ca5eeb3c42b8b5788de019fccca5d6c7ba6f9
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
      - P5-S2-C1
      source_result: The lesion percentage of the left ATR was significantly correlated
        with two semantic fluency cues (r=-0.47, corrected p < 0.01) and marginally
        significantly correlated with one semantic fluency cue (r=-0.39, corrected
        p < 0.06).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the lesion-behavior correlation
            for the left ATR tract with semantic fluency cues, as described in P5-S2-C1
            and defined in P4-S2-C9.
          source_ids:
          - P5-S2-C1
          - P4-S2-C9
        direction:
          answer: fits
          reason: The source reports negative correlations (r=-0.47, -0.39), indicating
            that higher lesion percentage is associated with lower performance. The
            draft's direction 'likely' is a qualitative placeholder that does not
            contradict the detected negative association, and the claim text correctly
            specifies the significant and marginal nature of the correlations.
          source_ids:
          - P5-S2-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as left ATR lesion percentage
            (template overlap), and the outcome is semantic fluency. The method is
            correctly identified as lesion-symptom mapping (LSM) using the JHU atlas.
          source_ids:
          - P4-S2-C9
          - P4-S2-C3
          - P5-S2-C1
        qualifications:
          answer: fits
          reason: The draft includes the relevant qualifications regarding the use
            of corrected t scores and Bonferroni correction, which are consistent
            with the methods described in P4-S2-C11 and P3-S1-C3.
          source_ids:
          - P4-S2-C11
          - P3-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitations regarding non-equivalent
            lesion distributions and the high proportion of aphasic patients, which
            are material caveats found in P10-S1-C13 and P10-S2-C4. No other material
            caveats are omitted that would change the interpretation of this specific
            correlation.
          source_ids:
          - P10-S1-C13
          - P10-S2-C4
      optional_pending:
      - Specific correlation coefficients and p-values for the left ATR semantic fluency
        correlations
      - Exact definition of the 'marginally significant' threshold used in the paper
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific correlation coefficients and p-values for the left ATR semantic fluency
      correlations
    - Exact definition of the 'marginally significant' threshold used in the paper
    normalizations: []
    analysis_identity:
      id: R002
      exposure:
        text: left ATR lesion percentage
      outcome:
        text: semantic fluency (two cues)
      analysis_label: Lesion-behavior correlation
      relation: association
      evidence_ids:
      - P5-S2-C1
      qualifier_ids:
      - P5-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
        source_review: _compare/relationships-2026-11-16/review-current/Li2017
        source_status_sha256: fbf65f4a844a9c26994044efa396a36b9a92c44cbf42c8a6dd43b174c58eeb74
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1e23f3d54f3749076377cf4d6b5fe4df368783abc8f406a6c48ee6301d4c3807
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: 1e23f3d54f3749076377cf4d6b5fe4df368783abc8f406a6c48ee6301d4c3807
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients

          Fifty-one right-handed stroke patients (40 males) were chosen from

          the China Rehabilitation Research Center.'
        anchor_text: 'Patients

          Fifty-one right-handed stroke patients (40 males) were chosen from

          the China Rehabilitation Research Center.'
        excluded_fragments: []
        image_sha256: 221016366e355254b1d59654b335d0f7f2b650009cfa986064ba6f6ece5c6be6
        transcription: 'Patients

          Fifty-one right-handed stroke patients (40 males) were chosen from the China
          Rehabilitation Research Center'
      P2-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2bd82cc51ac618abbdfb0b90e9129a271def15df8156a8f20ddfa8924c2fd7e3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C5
          page: 2
          text_layer_sha256: 2bd82cc51ac618abbdfb0b90e9129a271def15df8156a8f20ddfa8924c2fd7e3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'They all suﬀered from their

          ﬁrst brain injury, which was at least 1-month post-onset (mean=11.9

          months; SD=34.4; range: 1–184 months).'
        anchor_text: 'They all suﬀered from their

          ﬁrst brain injury, which was at least 1-month post-onset (mean=11.9

          months; SD=34.4; range: 1–184 months).'
        excluded_fragments: []
        image_sha256: aa87383d5f2030d74d9685f20efa5197923df44e7faabb9b451efa5e44390111
        transcription: '. They all suffered from their

          first brain injury, which was at least 1-month post-onset (mean=11.9

          months; SD=34.4; range: 1–184 months)'
      P10-S1-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8a87174c373b372e451d35663a0927f4bc184ede46d2f5e2b3a4f1f775e67baa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f724020650d51333bf976c206bc535caeaadc0142e159ad3707925e1f814c946
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S1-C13
          page: 10
          text_layer_sha256: f724020650d51333bf976c206bc535caeaadc0142e159ad3707925e1f814c946
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'First, although

          we sought to recruit a variety of lesion distributions in our patients,
          the

          numbers of patients with diﬀerent lesions were not equivalent across

          tracts (see Table 1).'
        anchor_text: 'First, although

          we sought to recruit a variety of lesion distributions in our patients,
          the

          numbers of patients with diﬀerent lesions were not equivalent across

          tracts (see Table 1).'
        excluded_fragments: []
        image_sha256: 791c53d6ce82e33cc759784274235bb18b725f31cccd09dea5951642b84a9948
        transcription: '. First, although

          we sought to recruit a variety of lesion distributions in our patients,
          the

          numbers of patients with different lesions were not equivalent across

          tracts (see Table 1)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Performance on each of the three cues in semantic ﬂuency task was

    signiﬁcantly correlated with the lesion percentages of four tracts: the

    left IFOF (r=−0.55 to −0.46, corrected p-values < 0.05), left SLF

    (r=−0.59 to −0.53, corrected p-values < 0.01), left UF (r=−0.52 to

    −0.41, corrected p-values < 0.05) and left FAT (r=−0.50 to −0.49,

    corrected p-values < 0.01), however, the left ATR was signiﬁcantly

    correlated with two cues of semantic ﬂuency (r=−0.47 and −0.47,

    corrected p-values < 0.01) and marginally signiﬁcantly correlated with

    one semantic cue (r=−0.39 corrected p-values < 0.06).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
