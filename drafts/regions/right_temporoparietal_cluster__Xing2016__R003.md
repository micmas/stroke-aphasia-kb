---
id: right_temporoparietal_cluster
name: right temporoparietal cluster
kind: network
findings:
- id: f1
  target: wab_r_aq
  target_kind: impairment
  claim: grey matter volume in the right temporoparietal cortex (including the supramarginal
    gyrus and posterior superior temporal gyrus) is positively related to the WAB-R
    Aphasia Quotient and is a significant independent predictor of this outcome when
    controlling for lesion burden, lesion size, and demographic factors
  direction: likely
  relationship: correlational
  method: VBM
  sample:
    n: 32
    population: chronic left hemisphere stroke survivors with aphasia
    phase: not_reported
    time_post_onset: at least 6 months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - type and total dose of speech-language therapy received by patients were not quantifiable
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: modulated grey matter volume in the right temporoparietal
    cortex, including the supramarginal gyrus and posterior superior temporal gyrus,
    measured via voxel-based morphometry. analysis controlled for proportion of critical
    area damaged (PCAD), lesion size, total grey and white matter volumes, age, gender,
    education, and handedness; the relationship was tested using both multiple regression
    and hierarchical linear regression. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S1-C11,
    two-model agreement, human verification pending): Patients

    Thirty-two chronic left hemisphere stroke survivors with history of aphasia were
    recruited with inclusion criteria as follows: native English speaker; at least
    6 months post-stroke; able to follow testing instructions; no history of other
    signifi- Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:wab_r_aq
  citation: '@Xing2016'
  source_passages:
  - section: Original source P5-S2-C4
    page: 5
    quote: 'The VBM analysis on overall aphasia

      severity (WAB-R AQ) demonstrated a positive relationship

      between grey matter volume and AQ in the right tempor-

      oparietal cortex including the supramarginal gyrus and pos-

      terior superior temporal gyrus, as well as in the left

      cerebellum lobules IV–VI (Fig. 3A and Table 2).'
    supports: claim
  - section: Original source P5-S3-C6
    page: 5
    quote: 'For WAB-R AQ and Spontaneous Speech, the

      grey matter volumes for both right hemisphere and cerebel-

      lar clusters were added into the model, and in both cases,

      only the right hemisphere grey matter volume was a signiﬁ-

      cant independent predictor of aphasia outcome [WAB-R

      AQ right hemisphere cluster t(22) = 4.70, P = 0.0001, cere-

      bellum cluster t(22) = 0.917, P = 0.37; Spontaneous Speech

      right hemisphere cluster t(22) = 4.44, P = 0.0002, cerebel-

      lum cluster t(22) = 1.47, P = 0.16].'
    supports: claim
  - section: Original source P3-S1-C11
    page: 3
    quote: 'Patients

      Thirty-two chronic left hemisphere stroke survivors with his-

      tory of aphasia were recruited with inclusion criteria as fol-

      lows: native English speaker; at least 6 months post-stroke;

      able to follow testing instructions; no history of other signiﬁ-

      '
    supports: sample
  - section: Original source P4-S2-C3
    page: 4
    quote: 'We included factors as nuisance variables

      that could relate to behavioural performance or grey matter

      volume: age, gender, level of education, handedness, lesion

      size, PCAD, and total volume of grey and white matter.'
    supports: confounders
  - section: Original source P4-S1-C5
    page: 4
    quote: 'Voxel-based morphometry protocol

      VBM is a whole-brain technique designed to discover subtle,

      local changes in grey matter density or volume by applying

      voxel-wise statistics within the context of Gaussian random

      ﬁelds (Ashburner and Friston, 2000).'
    supports: method
  - section: Original source P3-S2-C8
    page: 3
    quote: 'Aphasia and cognitive testing

      Patients were given the Western Aphasia Battery-Revised

      (WAB-R) (Kertesz et al., 1982), which includes subtests that

      provide composite scores of Spontaneous Speech, Repetition,

      Naming/Word-Finding and Auditory-Verbal Comprehension.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Xing2016
  proposal_id: R003
  review_status_sha256: c1729e2565b05e86c4ddffc6f1a155827904a10733719d3a1060d846251ea0a5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
        A/passages.json: 1432221af99887d27749b8038bd4f412e4af8fcb65a1fd3a6f33dbbd75734554
        A/raw.json: 4538eacbb7b5aa6229e2ccef34d383beab16c7883b056987f851176bf56e1107
        A/source-units.json: f98cf8d7adefe756b345945325f4f79dbf98e9e4fc0c3b2488a5e3c9c669266c
        A/full-source-units.json: da4cadd7e8202a821a212bbc89039c0bc9b8873b2286087dc4bc561d873ad42a
        A/meta.json: a956bbc6ed6ba2c79854b4aacf1297634aff0e40435a800b70d0d5b356c8ce30
        A/table-images/TABLE-1-page-5-1.png: d50335ce8098e0c99210db6b60fa0130f75b3a04dfa4d3b0ab222e6f61bac7a3
        A/table-images/page-7.png: fe162fb89eb33307d97b60ee1b944adfe908b29dbb0181ef2d3351f1462165de
        A/table-images/page-5.png: 91dba55944460e492d72731500a275fe99876225abf7e5ff3a7c7fba73531ed1
        A/table-images/page-4.png: 153a705d4a07cc49c908e4ead5a850089e2d1c4ebbd174d7055cd48096a730c7
        A/table-images/TABLE-1-page-4-1.png: 9062fcc7d8ae7e163c3317de9ce5c9d92fc95511b1d51bd0d573c7c4bf388971
        A/table-images/manifest.json: 348df9cb26167986b22c784ba586fc35fc8f21c3ac1634b841785b1ccbc16d74
        A/table-images/TABLE-2-page-7-1.png: 3d85ba2c469d83e03cbc005dc4c95729fc45bce5e9330dc9d78099fbcbcd9563
        A/clauses/window-03/raw.json: 44d1e03e4c18a8414b49cc9fe290bd23bfa8d52238c660d8cf316597c1a5c687
        A/clauses/window-03/prompt.txt: afe76deaee2014d3a5663f265ffb5ac0bb0c8cd9166ef1710b85aef83a5aedd3
        A/clauses/window-03/meta.json: 4dab091faa5e30dc61964714c6979ab8a50936b6723020b60d309be1fd755323
        A/clauses/window-04/raw.json: b4c238ea5479e7d73674ef697fd2c25c35bccd52ea85cda7a4422727b9226e4e
        A/clauses/window-04/prompt.txt: 95bb44902b4d4b0926c598a18626c4b4cc715ffa667525697c1831d5e8cdb3af
        A/clauses/window-04/meta.json: d42057c6afb4fc3557f063eb17c0d0195efa4c786d0191889e700ff69d2ca7c5
        A/clauses/window-05/raw.json: 8199e3e54744222fa963758d27e54f6d11f7132d4c1636ca58681e81ab7f6cb4
        A/clauses/window-05/prompt.txt: 238d69d681aae8bd137d3f5bb35ca61769da3b2bbc61772bbc15cd08e9023644
        A/clauses/window-05/meta.json: c5f37b96477d1a77394aa1e0b745984050c07b035f278e16fa801a81f3a81e38
        A/clauses/window-02/raw.json: f4d8365735a9f69e039073ea3f031624fed235372171c4a2ecbb1e5a06020e10
        A/clauses/window-02/prompt.txt: f6bb8619bb5352bf0052f4c1d258bcd5a5c3afaf4c135743fa66ab313eb8b5fa
        A/clauses/window-02/meta.json: e1257a9fa015cb06c7755db762e6900a7ebfea6c4cd6ef1c61b05853e3c8d706
        A/clauses/window-09/raw.json: d490857e1a7595717dd19ec286ce81113bc6e295cd8bdd4d3fada98ee5f859f6
        A/clauses/window-09/prompt.txt: b6d46f6c166cbbaee467b9eb457b554d965f50aa7ad28a7348f50e425b635dc3
        A/clauses/window-09/meta.json: b7b7701792a8b047b4f63fbb26995e159a6b5f0aede32701fcf5954981037734
        A/clauses/window-07/raw.json: 2b46fb6c5082d28d863f004c042916dbe6ccea7e3709e9fe4a65a45b48775b4d
        A/clauses/window-07/prompt.txt: 8d3f9f2e2cf769d95f5057bb6dacc994af9f433de6d722eeb397ad12f4912555
        A/clauses/window-07/meta.json: f01471d3fb76f0246e7e3655d6f2967498ff791b5b2dbc29ba885efeeb852a16
        A/clauses/window-01/raw.json: 0ced390123196fc492a04114072c06338986e3b8efd7d2ee8eb444b6704a432b
        A/clauses/window-01/prompt.txt: c4ce860724b684037e2886eb41f4dbab09e10339ee383bd375e2965cb4f065e5
        A/clauses/window-01/meta.json: e7ca2ae8cb7b203702cfb555aef5415e244d32fd15ef2142220d8a44d2af1334
        A/clauses/window-06/raw.json: 3bd82d77851a03fd133880642bf3ea250a27c3347f6575701da510e5b0f3ccdd
        A/clauses/window-06/prompt.txt: 9a74df7fb272109c568821f9c72803cae49c0aedc367e0f555336c3332048d9f
        A/clauses/window-06/meta.json: c5cb912ef6dc66a506720c0f5606b5ba69615af79f8e52b886cbb5f209c7633a
        A/clauses/window-08/raw.json: bff4c32693a38e2a4b9d9e59f0b23167b3f8bbb4ea922f8c08e7a933e3a11d5b
        A/clauses/window-08/prompt.txt: faeaba775aa9531cbe20ea092a2e07eb417600aea5e5246de27465b7e83fc7f5
        A/clauses/window-08/meta.json: 8a438d9b3ed297015d1abc79c13f99555beb985b6beca75d14556158d9835c3d
        A/tables/TABLE-1-page-5-2/raw.json: f74654db8e0a37063fd5b9813cba0afb94f7943b08776540c39c3014e244739a
        A/tables/TABLE-1-page-5-2/prompt.txt: a582bc2d9d70ef4f7c92f970d5059d61c339ed331e7c52c6f12100a4721dda78
        A/tables/TABLE-1-page-5-2/meta.json: 8b4c5aaae5a7dd5f86487bdbcc389a859972ca33eb505bb8e88c502609307790
        A/tables/TABLE-2-page-7-3/raw.json: 7bfc3995944de68fadd295d2030a6db8d22894d8eb331271aa154b632a4369c3
        A/tables/TABLE-2-page-7-3/prompt.txt: 0f2a641e44f4b27cd7cdf0457dc9f5410baecd2305f7f8d70389eabfa024debb
        A/tables/TABLE-2-page-7-3/meta.json: 1d33fb57b2a3116ee47817a89021c3fb300cccfd3264276cc6ac2cee52cf6ea7
        A/tables/TABLE-1-page-4-1/raw.json: fe4852bf237bddc7388087e1e46cb7db65eac2e04f4e73bcb05f82015d734d08
        A/tables/TABLE-1-page-4-1/prompt.txt: c7425041ee813696443a367202a0f15e17a2fddf6c2073c785dd2c3ba59d1dbf
        A/tables/TABLE-1-page-4-1/meta.json: b9debaa737f648a72303c4d957e511457dbed49b4c557897f09823ce6062c7e5
        B/passages.json: 1432221af99887d27749b8038bd4f412e4af8fcb65a1fd3a6f33dbbd75734554
        B/raw.json: 72d065e4bf80fd28766e6550ca087fe934cbd8fb53553008d8c064dddba9f67d
        B/source-units.json: f98cf8d7adefe756b345945325f4f79dbf98e9e4fc0c3b2488a5e3c9c669266c
        B/full-source-units.json: da4cadd7e8202a821a212bbc89039c0bc9b8873b2286087dc4bc561d873ad42a
        B/meta.json: 026fecbae75cf8f22f8216aa46cfc0c19061f06725b6a530f2e466a188b6a442
        B/table-images/TABLE-1-page-5-1.png: d50335ce8098e0c99210db6b60fa0130f75b3a04dfa4d3b0ab222e6f61bac7a3
        B/table-images/page-7.png: fe162fb89eb33307d97b60ee1b944adfe908b29dbb0181ef2d3351f1462165de
        B/table-images/page-5.png: 91dba55944460e492d72731500a275fe99876225abf7e5ff3a7c7fba73531ed1
        B/table-images/page-4.png: 153a705d4a07cc49c908e4ead5a850089e2d1c4ebbd174d7055cd48096a730c7
        B/table-images/TABLE-1-page-4-1.png: 9062fcc7d8ae7e163c3317de9ce5c9d92fc95511b1d51bd0d573c7c4bf388971
        B/table-images/manifest.json: 1d6abc52a56171b2a8dd65c4186e54683cbd780dc84a0fe22b8bb8091bd4867b
        B/table-images/TABLE-2-page-7-1.png: 3d85ba2c469d83e03cbc005dc4c95729fc45bce5e9330dc9d78099fbcbcd9563
        B/clauses/window-03/raw.json: 1197304f825c28929a24275b79ec8a9fc96d6710cc283c32b180bcddc7ce805a
        B/clauses/window-03/prompt.txt: afe76deaee2014d3a5663f265ffb5ac0bb0c8cd9166ef1710b85aef83a5aedd3
        B/clauses/window-03/meta.json: 06225ca53564cf53ba8fadadd8d1bd7a0b5a662e19a17adc171931b6718a0a29
        B/clauses/window-04/raw.json: 686fe606c4c82cc339808613eb2304cf6781d9f87de4622a5e8e0c983533758d
        B/clauses/window-04/prompt.txt: 95bb44902b4d4b0926c598a18626c4b4cc715ffa667525697c1831d5e8cdb3af
        B/clauses/window-04/meta.json: c5f08b624f94e5ca43a89221651d308eef176cad5228e2f941b49c494b698099
        B/clauses/window-05/raw.json: 7359abd36b5d8e8e36fa21c513377c93b1a15a74ca4255ad9db0aded06c490b7
        B/clauses/window-05/prompt.txt: 238d69d681aae8bd137d3f5bb35ca61769da3b2bbc61772bbc15cd08e9023644
        B/clauses/window-05/meta.json: 83fc9830fb7c87b407bbd1021a89c8744e5270ad44373083c3e6f9cc6909a79a
        B/clauses/window-02/raw.json: 05b21cf85170e23c08e614dc227ce5e3c53acd7edaa66f3668c73b0116a60665
        B/clauses/window-02/prompt.txt: f6bb8619bb5352bf0052f4c1d258bcd5a5c3afaf4c135743fa66ab313eb8b5fa
        B/clauses/window-02/meta.json: 293b8b51315e659390d05c68b751124c7b33323690456fe91bd8eaf99148b581
        B/clauses/window-09/raw.json: 7b2fa140525bcac6b1a41e70628bbf8b8c9ef9f67453ba67f0260c0f4c8a0b7c
        B/clauses/window-09/prompt.txt: b6d46f6c166cbbaee467b9eb457b554d965f50aa7ad28a7348f50e425b635dc3
        B/clauses/window-09/meta.json: 8c87e77b71743d62424dac81839a15e85e25d6247baf675bcfcb0f040287316c
        B/clauses/window-07/raw.json: 35503b0daf165b5be62cc600ae95b7e525e8a55feb19b049ea87ff1039045afd
        B/clauses/window-07/prompt.txt: 8d3f9f2e2cf769d95f5057bb6dacc994af9f433de6d722eeb397ad12f4912555
        B/clauses/window-07/meta.json: ce6d53d7a5047d47149675a1ee0c9169108e25f87be3f222bd319446e9bc592c
        B/clauses/window-01/raw.json: 3f6d20dbf3c27ff34c2767659af0ede53ed0ce86e552d10ee0508404fa3d1fe0
        B/clauses/window-01/prompt.txt: c4ce860724b684037e2886eb41f4dbab09e10339ee383bd375e2965cb4f065e5
        B/clauses/window-01/meta.json: 942100d8fbd62d1d76e4cf33320ba3bac840809a9b8bfd46ad13f2930a831efe
        B/clauses/window-06/raw.json: 2ca4b0d3c74e0f344b2a9f7372904ac27252e72afacc5b8e8c4df772423b9ade
        B/clauses/window-06/prompt.txt: 9a74df7fb272109c568821f9c72803cae49c0aedc367e0f555336c3332048d9f
        B/clauses/window-06/meta.json: 74ba56f69f4393b9fecc13e9ae0f980532cfd6622b63a675dd1944f6cc47637d
        B/clauses/window-08/raw.json: a01e9b11d7499f0cea41cd44a587220cbd6099914eb691aea8d28163e34a0424
        B/clauses/window-08/prompt.txt: faeaba775aa9531cbe20ea092a2e07eb417600aea5e5246de27465b7e83fc7f5
        B/clauses/window-08/meta.json: 2b257d25b3fb763390bfcfde5cdf3697e2f69fade516f16f37694cfb2c840203
        B/tables/TABLE-1-page-5-2/raw.json: 968cfea9f503300f833381b035c876235cf7aede2244e0d66d373e2317fd9c82
        B/tables/TABLE-1-page-5-2/prompt.txt: a582bc2d9d70ef4f7c92f970d5059d61c339ed331e7c52c6f12100a4721dda78
        B/tables/TABLE-1-page-5-2/meta.json: 1c5eeccdcc4a4c06cd52b10c1984ec11a369fad89c8c7ae8229e715f0e3c539b
        B/tables/TABLE-2-page-7-3/raw.json: 4bb54e600e1eb9a0570a3b51449f67cccdff1db649ffce6e68458a2892f4b609
        B/tables/TABLE-2-page-7-3/prompt.txt: 0f2a641e44f4b27cd7cdf0457dc9f5410baecd2305f7f8d70389eabfa024debb
        B/tables/TABLE-2-page-7-3/meta.json: 79721d9ade88710298d93f15df347c72ce70fb858ed71ca87eae180e90daa492
        B/tables/TABLE-1-page-4-1/raw.json: 8c2377e52be9ad194497d2a9febbafecbe154a072911b3cba64fbb977330160c
        B/tables/TABLE-1-page-4-1/prompt.txt: c7425041ee813696443a367202a0f15e17a2fddf6c2073c785dd2c3ba59d1dbf
        B/tables/TABLE-1-page-4-1/meta.json: dc32abfc3af9d30078793f93b0badddd374d6d71f08c10e15fcdce04f29c9da2
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
      pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
      source_review: _compare/relationships-2026-11-16/review-current/Xing2016
      source_status_sha256: 350201e5d0673d2379630a0a98369846f216618ee176f1e3630c4e8b5a95788d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: grey matter volume in right temporoparietal cortex (supramarginal gyrus
        and posterior superior temporal gyrus)
    outcome:
      text: WAB-R AQ
    analysis_label: VBM
    relation: association
    evidence_ids:
    - P5-S2-C4
    - P7-S1-C2
    qualifier_ids:
    - P5-S2-C3
    - P7-S2-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
      source_review: _compare/relationships-2026-11-16/review-current/Xing2016
      source_status_sha256: 350201e5d0673d2379630a0a98369846f216618ee176f1e3630c4e8b5a95788d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C13
      - Result passage disposed without unit P5-S1-C6
      - 'window 6: invalid/duplicate disposition P8-S1-C5'
      - 'window 7: invalid/duplicate disposition P8-S1-C11'
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C4
      - Result passage disposed without unit P9-S1-C5
      - Result passage disposed without unit P9-S1-C9
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S2-C2
      - Result passage disposed without unit P10-S2-C3
      - 'window 10: invalid/duplicate disposition P11-S1-C12'
      - Result passage disposed without unit P11-S1-C12
      - Accounting without a linked unit P11-S3-C2
      - Accounting without a linked unit P11-S3-C3
      - Accounting without a linked unit P11-S3-C5
      - Accounting without a linked unit P12-S1-C9
      - Accounting without a linked unit P12-S2-C5
      - Unaccounted source passage P12-S1-C9
      - Unaccounted source passage P11-S3-C3
      - Unaccounted source passage P11-S3-C5
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P11-S3-C2
      unattached_null_or_qualifier_ids:
      - P8-S2-C5
      - P9-S1-C4
      - P12-S1-C9
      - P12-S2-C5
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 174
      unselected_timing_passages:
      - P1-S2-C4
      - P3-S2-C1
      - P3-S2-C3
      - P8-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P1-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P8-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P6-S1-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_definition
        source_ids:
        - P1-S1-C8
        - P3-S2-C8
        - P3-S2-C9
        - P4-S1-C1
        - P5-S2-C2
        - P5-S2-C4
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C7
        - P5-S2-C8
        - P6-S1-C5
        - P10-S2-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C11
        - P1-S1-C14
        - P3-S1-C7
        - P3-S1-C8
        - P4-S2-C3
        - P4-S2-C5
        - P5-S2-C3
        - P5-S2-C10
        - P5-S3-C3
        - P5-S3-C6
        - P6-S1-C6
        - P7-S1-C2
        - P7-S1-C5
        - P7-S1-C6
        - P7-S2-C4
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C9
        - P8-S1-C10
        - P9-S1-C9
        - P10-S2-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - analysis_restrictions
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      source_anomalies:
      - evidence_id: P5-S1-C12
        as_printed: P = 2.5
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P5-S1-C12
        as_printed: P = 5.2
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P5-S1-C12
        as_printed: P = 8.8
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P5-S1-C12
        as_printed: P = 8.6
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P7-S1-C5
        as_printed: P = 8.58
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P8-S2-C5
        as_printed: P = 1.20
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P9-S2-C6
        as_printed: P = 1.24
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P10-S2-C7
        as_printed: P = 1.04
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S1
        - P8-S1
        - P8-S2
        - P9-S2
        - P10-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
      source_review: _compare/relationships-2026-11-16/review-current/Xing2016
      source_status_sha256: 350201e5d0673d2379630a0a98369846f216618ee176f1e3630c4e8b5a95788d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes relationship between left hemisphere regions and language
        abilities.
    - source_id: P1-S1-C14
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      reason: Restatement of VBM results in the abstract.
    - source_id: P1-S2-C2
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: Restatement of partial correlation results in the abstract.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 15
      - 16
      - 17
      reason: Restatement of group difference results in the abstract.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 20
      - 21
      - 22
      reason: Restatement of aphasic vs non-aphasic patient results in the abstract.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Points to Table 1 for demographics.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no significant differences in demographics.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Points to Supplementary Table 1.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between lesion locations and WAB-R scores.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Quantifies variance in WAB-R scores explained by PCAD.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Identifies grey matter volume associations with WAB-R AQ.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies grey matter volume associations with WAB-R Repetition.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies grey matter volume associations with WAB-R Naming/Word-Finding.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Identifies grey matter volume associations with WAB-R Spontaneous Speech.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Reports null findings for Auditory-Verbal Comprehension.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the transition to hierarchical regression.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 9
      - 10
      - 11
      reason: Defines the covariates for the regression models.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies PCAD as the only significant predictor without grey matter
        volume.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Identifies significant predictors when grey matter volume is added.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Identifies gender as a predictor for Repetition.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains the relationship between age and grey matter volume.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Identifies right hemisphere grey matter as the independent predictor
        for AQ and Spontaneous Speech.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figures for regression results.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null correlation between grey matter and time from stroke.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null relationship between time from stroke and aphasia scores.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summarizes VBM results.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Defines the covariates for partial correlation analyses.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports association between right hemisphere clusters and digit span
        forward.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Details VBM results for AQ in right temporoparietal cortex and left
        cerebellum.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Scatter plot results for AQ.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figure for marginal mean differences.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports marginal significance for Naming cluster.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Reports association between Spontaneous Speech cluster and pseudoword
        repetition.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 15
      - 16
      - 17
      reason: Defines covariates for group comparison.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 15
      - 16
      - 17
      reason: Reports higher grey matter volume in patients for AQ, Repetition, and
        Naming clusters.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 16
      reason: Reports lower grey matter volume in patients for AQ cerebellar cluster.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 17
      reason: Reports lower volume in cerebellar cluster and no difference in right
        hemisphere cluster for Spontaneous Speech.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 18
      reason: Defines additional confounding variable for sensitivity analysis.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 18
      reason: Confirms significance of right hemisphere clusters after adding total
        volume covariate.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 20
      - 21
      - 22
      reason: Defines covariates for aphasic vs non-aphasic patient comparison.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 20
      - 21
      - 22
      reason: Reports higher grey matter volume in aphasic patients for AQ, Repetition,
        and Naming clusters.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 21
      reason: Reports marginal significance for Spontaneous Speech right hemisphere
        cluster.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 22
      reason: Reports lower grey matter volume in aphasic patients for cerebellar
        clusters.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Details VBM results for Spontaneous Speech.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: References prior studies on right hemisphere activation.
    - source_id: P11-S3-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 8
      reason: Restatement of VBM results in discussion.
    - source_id: P11-S3-C3
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: Restatement of partial correlation results in discussion.
    - source_id: P11-S3-C5
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: Restatement of null cognitive results in discussion.
    - source_id: P12-S2-C6
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of cerebellar results in discussion.
    - source_id: P12-S2-C10
      disposition: represented
      result_indexes: []
      reason: Reports null relationships in the left hemisphere.
    unresolved_coverage:
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P8-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C14
    - P1-S2-C2
    - P1-S2-C3
    - P1-S2-C5
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S3-C5
    - P6-S1-C1
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P7-S1-C5
    - P7-S1-C6
    - P8-S1-C1
    - P8-S2-C5
    - P8-S2-C6
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C9
    - P9-S1-C10
    - P9-S2-C6
    - P9-S2-C7
    - P10-S1-C2
    - P10-S1-C6
    - P10-S2-C2
    - P10-S2-C3
    - P11-S1-C10
    - P11-S1-C12
    - P11-S2-C2
    - P11-S2-C7
    - P11-S2-C9
    - P11-S3-C2
    - P11-S3-C3
    - P11-S3-C5
    - P12-S1-C9
    - P12-S2-C5
    - P12-S2-C6
    - P12-S2-C10
    - P12-S3-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-1-page-5-2
    - TABLE-2-page-7-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C8
      - P1-S1-C9
      - P3-S2-C7
      - P3-S2-C8
      - P4-S2-C5
      - P5-S1-C6
      - P8-S1-C6
      recruited_sample:
      - P1-S1-C8
      - P1-S2-C4
      - P3-S1-C11
      - P3-S2-C1
      - P3-S2-C7
      eligibility:
      - P3-S1-C11
      - P3-S2-C1
      imaging_provenance:
      - P1-S1-C9
      - P3-S2-C11
      imaging_timing:
      - P1-S1-C8
      - P3-S1-C11
      outcome_timing:
      - P1-S1-C8
      - P3-S1-C11
      outcome_definition: []
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C11
      - P4-S2-C2
      - P5-S2-C2
      limitations:
      - P12-S1-C8
      - P12-S1-C11
      - P12-S1-C12
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C12
      personal_factors: []
      tested_personal_effects:
      - P1-S2-C2
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C7
      - P4-S2-C5
      - P5-S1-C6
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P1-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P8-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P6-S1-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_definition
      source_ids:
      - P1-S1-C8
      - P3-S2-C8
      - P3-S2-C9
      - P4-S1-C1
      - P5-S2-C2
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P5-S2-C8
      - P6-S1-C5
      - P10-S2-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C11
      - P1-S1-C14
      - P3-S1-C7
      - P3-S1-C8
      - P4-S2-C3
      - P4-S2-C5
      - P5-S2-C3
      - P5-S2-C10
      - P5-S3-C3
      - P5-S3-C6
      - P6-S1-C6
      - P7-S1-C2
      - P7-S1-C5
      - P7-S1-C6
      - P7-S2-C4
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C9
      - P8-S1-C10
      - P9-S1-C9
      - P10-S2-C4
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
      pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
      review_sha256: c1729e2565b05e86c4ddffc6f1a155827904a10733719d3a1060d846251ea0a5
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
      - P5-S2-C4
      source_result: VBM analysis demonstrated a positive relationship between grey
        matter volume in the right temporoparietal cortex (supramarginal gyrus and
        posterior superior temporal gyrus) and WAB-R AQ. Hierarchical regression confirmed
        this cluster as a significant independent predictor of WAB-R AQ when controlling
        for PCAD, lesion size, total grey/white matter volumes, and demographics.
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VBM analysis of WAB-R AQ
            described in P5-S2-C4 and the subsequent hierarchical regression in P5-S3-C6.
            The exposure (right temporoparietal GMV) and outcome (WAB-R AQ) match
            the source.
          source_ids:
          - P5-S2-C4
          - P5-S3-C6
        direction:
          answer: fits
          reason: The source explicitly states a 'positive relationship' between grey
            matter volume and AQ (P5-S2-C4). The draft claims a positive relation,
            which is consistent.
          source_ids:
          - P5-S2-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as grey matter volume in the
            right temporoparietal cortex (supramarginal gyrus and posterior superior
            temporal gyrus) measured via VBM. The outcome is WAB-R AQ. The method
            is VBM. The population is chronic left hemisphere stroke survivors with
            aphasia.
          source_ids:
          - P5-S2-C4
          - P3-S1-C11
          - P4-S1-C5
        qualifications:
          answer: fits
          reason: The draft includes the necessary qualifications regarding the control
            of covariates (PCAD, lesion size, demographics) which are explicitly stated
            in P5-S2-C3 and P5-S3-C6. The limitation regarding therapy dose is also
            correctly included from P3-S2-C6.
          source_ids:
          - P5-S2-C3
          - P5-S3-C6
          - P3-S2-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly notes the control
            for lesion burden (PCAD) which is central to the study's design (P1-S1-C11,
            P3-S1-C5). The distinction between the VBM finding and the subsequent
            group comparison with controls (P8-S1-C6) is not conflated; the draft
            focuses on the association within the patient group as per the selected
            analysis.
          source_ids:
          - P1-S1-C11
          - P3-S1-C5
      optional_pending:
      - Specific MNI coordinates for the right temporoparietal cluster
      - Exact P-values and t-statistics for the VBM cluster
      - Details of the 10 non-aphasic stroke survivors used for validation
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific MNI coordinates for the right temporoparietal cluster
    - Exact P-values and t-statistics for the VBM cluster
    - Details of the 10 non-aphasic stroke survivors used for validation
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: grey matter volume in right temporoparietal cortex (supramarginal gyrus
          and posterior superior temporal gyrus)
      outcome:
        text: WAB-R AQ
      analysis_label: VBM
      relation: association
      evidence_ids:
      - P5-S2-C4
      - P7-S1-C2
      qualifier_ids:
      - P5-S2-C3
      - P7-S2-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
        source_review: _compare/relationships-2026-11-16/review-current/Xing2016
        source_status_sha256: 350201e5d0673d2379630a0a98369846f216618ee176f1e3630c4e8b5a95788d
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7db0863e5d5bef817a8f0d54d8947cf574866ebc338f60c812bc5710a2ba6e57
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6310897289b7722950e988c1b611c0ee5d9e48e49bc4a3dd24c9f02262baeb93
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C11
          page: 3
          text_layer_sha256: 3ebfbf58b6c7250f213c75af73ed94554c07596233e7c987c024887c2d8cf837
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients

          Thirty-two chronic left hemisphere stroke survivors with his-

          tory of aphasia were recruited with inclusion criteria as fol-

          lows: native English speaker; at least 6 months post-stroke;

          able to follow testing instructions; no history of other signiﬁ-

          '
        anchor_text: 'Patients

          Thirty-two chronic left hemisphere stroke survivors with his-

          tory of aphasia were recruited with inclusion criteria as fol-

          lows: native English speaker; at least 6 months post-stroke;

          able to follow testing instructions; no history of other signiﬁ-'
        excluded_fragments: []
        image_sha256: a99411d134161e5c1a01eb4404f521c4eb4cd0dd59db56ed4bf1ccd64159a66f
        transcription: 'Patients

          Thirty-two chronic left hemisphere stroke survivors with history of aphasia
          were recruited with inclusion criteria as follows: native English speaker;
          at least 6 months post-stroke; able to follow testing instructions; no history
          of other signifi-'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'The VBM analysis on overall aphasia

    severity (WAB-R AQ) demonstrated a positive relationship

    between grey matter volume and AQ in the right tempor-

    oparietal cortex including the supramarginal gyrus and pos-

    terior superior temporal gyrus, as well as in the left

    cerebellum lobules IV–VI (Fig. 3A and Table 2).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
