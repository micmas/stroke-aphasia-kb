---
id: gm_only_lesion_classification
name: GM-only lesion classification cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: overall_aphasia_severity
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: overall_aphasia_severity
  target_kind: impairment
  claim: GM-only lesion classification significantly predicted overall aphasia severity,
    and the amount of explained variance indicated it best predicted this outcome
    compared to combined GM + WM clustering.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 34
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - possible lack of power in cluster analyses
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient classification into one of four clusters based
    on k-medoids analysis of the number of spared voxels within five cortical masks
    (DLPFC, iFrontal, aTemporal, pTemporal, and Parietal). patients in clusters 2,
    3, and 4 had significantly lower WAB-R AQ scores than patients in cluster 1. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S3-C6, two-model agreement, human verification pending):
    Materials and methods


    Participants


    Thirty-four individuals (24 males; mean age = 61.91 ± 10.84 years) with chronic
    stroke-induced aphasia (i.e., ≥ six months post-onset; mean time post-onset =
    61.18 ± 86.49 months) due to left hemisphere ischemic infarct participated in
    the study Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.population
    - proposed_concept:overall_aphasia_severity
  citation: '@Meier2019'
  source_passages:
  - section: Original source P7-S1-C5
    page: 7
    quote: 'Specifically, both clus-

      tering types significantly predicted overall aphasia severity

      per WAB-R AQ, yet the predictive power of the GM-only

      lesion classification (F(3, 29) = 12.260, p < 0.001, R2 =

      0.559) was higher than the combined GM + WM clustering

      (F(3, 29) = 9.562, p < 0.001, R2 = 0.497).'
    supports: claim
  - section: Original source P8-S1-C1
    page: 8
    quote: '

      within the GM-only predictive model, patients within cluster 2

      (β = −48.432, t = −5.363, p < 0.001), cluster 3 (β = −29.075,

      t = −3.428, p = 0.002) and cluster 4 (β = −31.932, t = −4.396,

      p < 0.001) had significantly lower WAB-R AQ scores than

      patients in cluster 1.'
    supports: claim
  - section: Original source P8-S2-C1
    page: 8
    quote: 'statistically compared (as would be the case in nested models),

      the amount of explained variance indicates that the GM-only

      model best predicts overall aphasia severity, while baseline

      naming skills and naming treatment outcomes are best predict-

      ed by combined GM + WM metrics.'
    supports: claim
  - section: Original source P2-S3-C6
    page: 2
    quote: 'Materials and methods

      Participants

      Thirty-four individuals (24 males; mean age = 61.91 ±

      10.84 years) with chronic stroke-induced aphasia (i.e., ≥six

      months post-onset; mean time post-onset = 61.18 ±

      86.49 months) due to left hemisphere ischemic infarct partic-

      ipated in the study.'
    supports: sample
  - section: Original source P2-S3-C7
    page: 2
    quote: 'The primary eligibility requirement was

      presence of anomia.'
    supports: sample
  - section: Original source P5-S1-C1
    page: 5
    quote: '

      Around Medoids (PAM) algorithm to determine how patients

      clustered according to (1) GM-only metrics (i.e., number of

      spared voxels in the DLPFC, iFrontal, aTemporal, pTemporal

      and Parietal masks) versus (2) combined GM + WM metrics

      (i.e., number of spared voxels in GM masks plus spared

      voxels in and FAmean extracted from the left AF, IFOF, ILF

      Fig. 1 Anatomical masks. a Gray matter (GM) regions of interest (ROIs),

      including DLPFC (purple), iFrontal (green), aTemporal (red), pTemporal

      (navy blue), Parietal (cyan) and Occipital (yellow). Numbers denote ROIs

      in the AAL atlas, listed in Table 1. b Bilateral white matter (WM) tract

      masks, including—from left to right—the arcuate (in red), inferior fronto-

      occipital (in green), inferior longitudinal (in blue) and uncinate (in violet)

      fasciculi. c From left to right, the normalized T1 image, lesion map, and

      subject-specific GM and WM masks shown for a sample patient.

      Matrices below the masks represent 4x4mm swathes of tissue as a toy

      example of the procedure used to calculate spared tissue and fractional

      anisotropy (FA) per each subject-specific mask. In the far left and middle

      matrices, 1 = spared and 0 = lesioned voxels in the GM and WM masks,

      respectively; the font color corresponds to the mask from which spared

      voxels were extracted. The numbers in the third matrix (at right) reflect

      FA values per voxel in the same 4x4mm of WM tissue shown in the

      middle matrix

      Brain Imaging and Behavior (2019) 13:1510–1525

      1514


      '
    supports: method
  - section: Original source P13-S1-C13
    page: 13
    quote: 'Although the present sample represents one of the

      largest samples of patients in the aphasia treatment neuroim-

      aging literature, it is possible the cluster analyses suffered

      from lack of power.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Meier2019
  proposal_id: R001
  review_status_sha256: fbf8c63d37fb67316e5dc3c7ed2e363b0cac295988d8df6530b4c7a821146eb1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
        A/passages.json: 705c5619f6006a4ada7a641e0fd58bcaa6b3573ae67ad5b1faeae7c7bca0c675
        A/raw.json: 863bca2f5ae162fa20879fe8bffc79b558281abe9e08f33090f1547cf2a960b9
        A/source-units.json: 16aadb80d0fbf7dcf7759edfae144f5e23c83828e86e7bcef9098b58d2b5cef3
        A/full-source-units.json: 3a4615ca8a0c9c8eba608843a75fe6007d8d17e426368c0bd64309de3a3aabfe
        A/meta.json: 2f8c17c47e8046ee81abad74e8dd3bfd96583a233395287468ff7e5d1046a0f1
        A/table-images/page-12.png: c4e784d9e93c67ad506f340e73a5aa5549447e9f7d7aa12de3a6615888a69528
        A/table-images/TABLE-4-page-12-1.png: d3bf748ef54e6cbf415ce8a47d97c11d5e3ec00e76e2761da6727fd41acf5f7d
        A/table-images/TABLE-3-page-8-1.png: ca4a0ce774f61ab21755e3b1b9ede519619e1726dbbaa178f642bd8db38765af
        A/table-images/page-7.png: 8e8c303cf847d5a1ad2f8b9a2c7427d8f2ac14af8c3630e4af77602ae63b1156
        A/table-images/page-4.png: 491a17b9bede12d3041b98046fc5018065fb74db737e702109a470adb53dbd12
        A/table-images/TABLE-1-page-4-1.png: a4b27e1974b022cb4bedb207dd70ab1e277922b2d7e35239720b0f98091efc0a
        A/table-images/page-8.png: c943870bc111ee0d8cd77944f5b79f0e201b330e2987331ef813af39f64c1b47
        A/table-images/manifest.json: 0a0e58c6bd6607af721683954db55a967282ba724edd47589652f4c5e42cefa7
        A/table-images/TABLE-2-page-7-1.png: 8d932e637e57890c94a2a5b7cdf3e82bdd7aebb0cacbd98e86c1c79fce9a7a0b
        A/clauses/window-03/raw.json: 87c80e0acd3bf5aa08c421b4f197b1014ab0eb42026558737dd203003e1dc440
        A/clauses/window-03/prompt.txt: 7a830fbd0b802726a7425ff22c52152ae5155f7873dfb63fd948cfe05cc7bee9
        A/clauses/window-03/meta.json: dd52fce3035efedd09f97a155c31ccefa8dff78501262f1cae162e4d8a73f44a
        A/clauses/window-04/raw.json: b0fc315d8f9f27342a28bdc32a49dfffe6d77659792b8aa3c87e71ce14a56293
        A/clauses/window-04/prompt.txt: 53074d487cb6826e011f52a73ece61b33a0bdfe3b5dd9d41e65bf5e361a3738c
        A/clauses/window-04/meta.json: 8608b220262fd03d84f8bff9754679f47e2964cd3c3261932c5b76733597cc5d
        A/clauses/window-05/raw.json: 06ab44d9938cf75b095da7c2e61a01b99c53a21a3d61d00eed5e6a3943e7f53b
        A/clauses/window-05/prompt.txt: bb5a5c616f5e49ca2443e7f2e4c375d4b142b2a1beda73c1058ca717703592e7
        A/clauses/window-05/meta.json: 993b1ea321c0280a02d04bad41fdfdf2836932c0758cbc7f688d782b29759bf3
        A/clauses/window-02/raw.json: 9b48629a56afaabf3810715268f8248bdb68876f94fbe113f7689ee31bc31f71
        A/clauses/window-02/prompt.txt: fe57195cd9814f3f8795420de21be586dd763f750930e16c871183d31c8f19c1
        A/clauses/window-02/meta.json: 3ed6c1a378f6ba38b0a9c4115457bcc0a2952fbfb5c10cd4e4c6a2d7501df936
        A/clauses/window-07/raw.json: f6641408f4b2b1963ebd894b835278b509910f827d94c0aa5f7c04a6ad2a584e
        A/clauses/window-07/prompt.txt: a96303e8a0db6da18a4823310eae970e42efc9de5df3c718a18cd778dabe0064
        A/clauses/window-07/meta.json: cf240f6b22e3c8613999387994606c3b14a38c38ebea61c4cf61e6f5622a4047
        A/clauses/window-01/raw.json: 52a98c342f0dd1e7df44970f0120d655eae587a4a25cf85317e78415c532ecba
        A/clauses/window-01/prompt.txt: c0b40c5b00260f86fe580bb866d3fecf4199bb26cc9a134429da814531768f9f
        A/clauses/window-01/meta.json: 84c9efd9eea375c391e40bf9a0ff0203e3e30d5bfc9083f4c979fdb91087ae79
        A/clauses/window-06/raw.json: 82bc1d41be275d9fba3406d47a43d970dea2d3dbc4a547622c922338de339179
        A/clauses/window-06/prompt.txt: 6b2bf0e9a083a0974aad056d66c4420ce823180829deda2acb54d19f3f743de6
        A/clauses/window-06/meta.json: 101c82bdff241cab170cb600edd6b9ddfbedd1c500445bed7678ae67ee41dde0
        A/clauses/window-08/raw.json: f8751129f38e7397357fc32dcb82a55386fcbd214a1d3963ef8eef3c05355286
        A/clauses/window-08/prompt.txt: 345f89a8475d6808c050f2574a8dc7ec9bdaeeb398bc607726178ccd6b298a77
        A/clauses/window-08/meta.json: 1f06c1979755db91c0572184d5f25cab71b3df3d578833ee5a94f5a967a05a22
        A/tables/TABLE-4-page-12-4/raw.json: 35e55050f14b9f625f8fbbba745ec260b9024ffaf3484f4cd947776e879fed58
        A/tables/TABLE-4-page-12-4/prompt.txt: db7b6a615e847b085019298cdf71be9729e65b0b149e4023dc92f6a25f607752
        A/tables/TABLE-4-page-12-4/meta.json: c7f47fd15dbddbf4c139f0ccae7cb3707d4188dea1fa5a47c27109e6bed5eccc
        A/tables/TABLE-3-page-8-3/raw.json: c9716060a440ebd7013b9d21cb7a6a102bb79ee9b72a3b5e128c2a97eccfe721
        A/tables/TABLE-3-page-8-3/prompt.txt: 17a7571485e124b53afd929dcf1ede78885aaebf60a43b58538d68e4244efef9
        A/tables/TABLE-3-page-8-3/meta.json: 9686d33fa60930cd8516ecbc2cd4b8dcadc359e7ab468377f43ebedde14e06b0
        A/tables/TABLE-2-page-7-2/raw.json: 508037d5741cde6bd90d636af1472343586128d30e14baee8dc51d84bc7cff04
        A/tables/TABLE-2-page-7-2/prompt.txt: 8e39d55d1fd25a593d9dfabe33867f54f7cf4e2ae6e5e22edad45241bee59b32
        A/tables/TABLE-2-page-7-2/meta.json: 5b8880a592c4f0ab6aa916b45b234676ed5f1874df549b563ed933876207c3e8
        A/tables/TABLE-1-page-4-1/raw.json: a98c4c3411dc8e56a273181874969eaa5836fb255ff3650bbf94ec67bd9873b7
        A/tables/TABLE-1-page-4-1/prompt.txt: 61e24dd1d36fd3da7e28ded11c761a62113af5b9f3494d2ae3ad57b7f90d7253
        A/tables/TABLE-1-page-4-1/meta.json: 6c538830f14d3e9fd45efe5e4a78baa6ed63b3b5872b019b4d33ddc37d6d69f6
        B/passages.json: 705c5619f6006a4ada7a641e0fd58bcaa6b3573ae67ad5b1faeae7c7bca0c675
        B/raw.json: bef9392ad59de72e10d23b86755926129701552b63006fdeb78a165da68d6aca
        B/source-units.json: 16aadb80d0fbf7dcf7759edfae144f5e23c83828e86e7bcef9098b58d2b5cef3
        B/full-source-units.json: 3a4615ca8a0c9c8eba608843a75fe6007d8d17e426368c0bd64309de3a3aabfe
        B/meta.json: 2a9df1c1f815dcd46700170e89326d6ceca0a0262fa1c8187bc9dca4cb968fca
        B/table-images/page-12.png: c4e784d9e93c67ad506f340e73a5aa5549447e9f7d7aa12de3a6615888a69528
        B/table-images/TABLE-4-page-12-1.png: d3bf748ef54e6cbf415ce8a47d97c11d5e3ec00e76e2761da6727fd41acf5f7d
        B/table-images/TABLE-3-page-8-1.png: ca4a0ce774f61ab21755e3b1b9ede519619e1726dbbaa178f642bd8db38765af
        B/table-images/page-7.png: 8e8c303cf847d5a1ad2f8b9a2c7427d8f2ac14af8c3630e4af77602ae63b1156
        B/table-images/page-4.png: 491a17b9bede12d3041b98046fc5018065fb74db737e702109a470adb53dbd12
        B/table-images/TABLE-1-page-4-1.png: a4b27e1974b022cb4bedb207dd70ab1e277922b2d7e35239720b0f98091efc0a
        B/table-images/page-8.png: c943870bc111ee0d8cd77944f5b79f0e201b330e2987331ef813af39f64c1b47
        B/table-images/manifest.json: 3fc1c636a590adbdcec102639f1cca8f0a7861a8ba807903d07fbb8aecee80b1
        B/table-images/TABLE-2-page-7-1.png: 8d932e637e57890c94a2a5b7cdf3e82bdd7aebb0cacbd98e86c1c79fce9a7a0b
        B/clauses/window-03/raw.json: b931ee59208fbc220c5b9d84ae5f339da11942538c236ad10aacff0edc4109c5
        B/clauses/window-03/prompt.txt: 7a830fbd0b802726a7425ff22c52152ae5155f7873dfb63fd948cfe05cc7bee9
        B/clauses/window-03/meta.json: 889f27795bbf793b8946172fec55e95ce894c599d3b0b09cf4f9418139db3bbe
        B/clauses/window-04/raw.json: 37a9a58c47b9c7547eec5683e327efb9ab80bf533afd649b93864e9ad61abf6a
        B/clauses/window-04/prompt.txt: 53074d487cb6826e011f52a73ece61b33a0bdfe3b5dd9d41e65bf5e361a3738c
        B/clauses/window-04/meta.json: 6616e2697d2acb8ac45613b05341a12a51dc7a768718c7d41e5f9654456ea608
        B/clauses/window-05/raw.json: a18fbc85e6f3644c34a00945c0af0c1b5285641ba67c8420adf0b068d11583da
        B/clauses/window-05/prompt.txt: bb5a5c616f5e49ca2443e7f2e4c375d4b142b2a1beda73c1058ca717703592e7
        B/clauses/window-05/meta.json: 9332ee43cf76d801c313eb11bd6bd2c4e5b04f2f3231b4b4ea655c3d38861025
        B/clauses/window-02/raw.json: d86d82b74c5a60d9b5b34448e46f48e290c276fba88abbf39a97d26583b0af63
        B/clauses/window-02/prompt.txt: fe57195cd9814f3f8795420de21be586dd763f750930e16c871183d31c8f19c1
        B/clauses/window-02/meta.json: e71117a480258a0f861b935e85069ae269e765398568ea17d1a2a517f187417e
        B/clauses/window-07/raw.json: 98d37e09320b87b4a6eca3959f6edf985190c489559c6106730e247227c96439
        B/clauses/window-07/prompt.txt: a96303e8a0db6da18a4823310eae970e42efc9de5df3c718a18cd778dabe0064
        B/clauses/window-07/meta.json: c417701bc2352153b95afc1b60655b421d5b54eed3bd36dfe7e805fd6b56b53f
        B/clauses/window-01/raw.json: 4060a64f90b9daeed1eef4dc4f4cac92826a1d7788ff88b3d1ac778af2278986
        B/clauses/window-01/prompt.txt: c0b40c5b00260f86fe580bb866d3fecf4199bb26cc9a134429da814531768f9f
        B/clauses/window-01/meta.json: fd6eeea22118fea7a0bdbfa480aad764b692890f558e4556d8e8ac677f6cfc9f
        B/clauses/window-06/raw.json: c81073fdef0d3012d5d60520d0b58fc16121997d2bd56cea10efbf2108e60537
        B/clauses/window-06/prompt.txt: 6b2bf0e9a083a0974aad056d66c4420ce823180829deda2acb54d19f3f743de6
        B/clauses/window-06/meta.json: a4fac55ad145df3df12a5175a477c138bc34193dc3a972a21e8ace7b511854bf
        B/clauses/window-08/raw.json: f8751129f38e7397357fc32dcb82a55386fcbd214a1d3963ef8eef3c05355286
        B/clauses/window-08/prompt.txt: 345f89a8475d6808c050f2574a8dc7ec9bdaeeb398bc607726178ccd6b298a77
        B/clauses/window-08/meta.json: 1c0b1f543db95b48e71af7ac578ca1ede2bef94847308608efcdde4891348511
        B/tables/TABLE-4-page-12-4/raw.json: ff8d6aa78795db08d506a105a91927f91eae2335e28c549b9148a96d28445884
        B/tables/TABLE-4-page-12-4/prompt.txt: db7b6a615e847b085019298cdf71be9729e65b0b149e4023dc92f6a25f607752
        B/tables/TABLE-4-page-12-4/meta.json: 177a267f1d6c79893bb584d45cc44d5c03d8b7400ceb48ceb70726f5eabeb5cb
        B/tables/TABLE-3-page-8-3/raw.json: 6c8f90cffe7c075cde35e79cbfb99b063123122f397581bc39a75b82b5c5f86a
        B/tables/TABLE-3-page-8-3/prompt.txt: 17a7571485e124b53afd929dcf1ede78885aaebf60a43b58538d68e4244efef9
        B/tables/TABLE-3-page-8-3/meta.json: 3da1409e2b5b3387c5850a4206c2f61d0e95c6b430e42f006113990c635812d7
        B/tables/TABLE-2-page-7-2/raw.json: 53b93a0c62f9e637b9c8280b456f0634ae0c275a150170371e7bf78cc1ef9818
        B/tables/TABLE-2-page-7-2/prompt.txt: 8e39d55d1fd25a593d9dfabe33867f54f7cf4e2ae6e5e22edad45241bee59b32
        B/tables/TABLE-2-page-7-2/meta.json: ac9b2042b6a38a90dbe5408b9ddc2a3ac6ff6a7e5e3c2d6083eca85494317204
        B/tables/TABLE-1-page-4-1/raw.json: 87174fe70c9977c72bb14d352a9669f0706a0e16174e3f8415c7225dbfbc2b2d
        B/tables/TABLE-1-page-4-1/prompt.txt: 61e24dd1d36fd3da7e28ded11c761a62113af5b9f3494d2ae3ad57b7f90d7253
        B/tables/TABLE-1-page-4-1/meta.json: d508d6909043c8aa0f17b308449bbf2d7ec2bd4596e5454c2a5e0c95a03bc138
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
      pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
      source_review: _compare/relationships-2026-11-16/review-current/Meier2019
      source_status_sha256: b3d71fb953ef86b0766fe402235d7a6d78f881a90c2f021c082a5a03827ba5f6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: GM-only lesion classification (clusters)
    outcome:
      text: overall aphasia severity (WAB-R AQ)
    analysis_label: GM-only clustering prediction of aphasia severity
    relation: association
    evidence_ids:
    - P7-S1-C5
    - P8-S1-C1
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
      pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
      source_review: _compare/relationships-2026-11-16/review-current/Meier2019
      source_status_sha256: b3d71fb953ef86b0766fe402235d7a6d78f881a90c2f021c082a5a03827ba5f6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C12
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C9
      - Unaccounted source passage P1-S1-C12
      - Accounting without a linked unit P6-S2-C11
      - Accounting without a linked unit P6-S2-C8
      - Accounting without a linked unit P6-S2-C9
      - Unaccounted source passage P6-S2-C8
      - Unaccounted source passage P6-S2-C11
      - Unaccounted source passage P6-S2-C9
      - Result passage disposed without unit P6-S2-C12
      - Result passage disposed without unit P6-S2-C14
      - Accounting without a linked unit P6-S3-C2
      - Result passage disposed without unit P6-S3-C3
      - Result passage disposed without unit P6-S3-C4
      - Accounting without a linked unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C6
      - Accounting without a linked unit P6-S3-C7
      - Unaccounted source passage P6-S3-C5
      - Unaccounted source passage P6-S3-C2
      - Unaccounted source passage P6-S3-C7
      - Result passage disposed without unit P6-S3-C10
      - Result passage disposed without unit P6-S3-C11
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S2-C1
      - Accounting without a linked unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C11
      - Result passage disposed without unit P9-S2-C1
      - Result passage disposed without unit P9-S2-C2
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S1-C8
      - Result passage disposed without unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C4
      - Result passage disposed without unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P12-S2-C1
      - Result passage disposed without unit P12-S2-C4
      - Unresolved source passage P13-S1-C1
      - Result passage disposed without unit P13-S1-C10
      - Result passage disposed without unit P13-S1-C5
      - Result passage disposed without unit P13-S1-C12
      - Accounting without a linked unit P14-S1-C6
      - Accounting without a linked unit P14-S1-C7
      - Unaccounted source passage P14-S1-C6
      - Unaccounted source passage P14-S1-C7
      unattached_null_or_qualifier_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P1-S1-C11
      - P6-S3-C3
      - P6-S3-C7
      - P7-S1-C3
      - P7-S1-C4
      - P8-S1-C8
      - P8-S2-C1
      - P9-S2-C2
      - P9-S2-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S2-C4
      - P13-S1-C1
      - P14-S1-C6
      suppressed_nonrepresented_units: 20
      default_disposition_count_requires_completeness_check: 159
      unselected_timing_passages:
      - P2-S3-C6
      - P3-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
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
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C1
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
        source_id: P9-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C11
        - P2-S2-C2
        - P6-S1-C12
        - P6-S2-C2
        - P9-S1-C5
        - P9-S1-C6
        - P9-S1-C7
        - P9-S1-C8
        - P10-S1-C6
        - P12-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      - TABLE-3-page-8-3
      - TABLE-4-page-12-4
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P5-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P8-S2
        - P9-S1
        - P9-S2
        - P10-S1
        - P10-S2
        - P13-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
      source_review: _compare/relationships-2026-11-16/review-current/Meier2019
      source_status_sha256: b3d71fb953ef86b0766fe402235d7a6d78f881a90c2f021c082a5a03827ba5f6
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the clustering process and characteristics captured, not a
        specific outcome relationship.
    - source_id: P1-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Abstract summary of findings reported in detail in Results.
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 6
      reason: Abstract summary of unadjusted correlations.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 7
      reason: Abstract summary of adjusted aphasia severity results.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Abstract summary of adjusted naming and treatment results.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ROI mask generation.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions supplementary materials.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of aphasia severity.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming skills.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of therapy benefit (average PMG).
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about lesion volume variability.
    - source_id: P6-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of spared tissue.
    - source_id: P6-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of FA between hemispheres.
    - source_id: P6-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes elbow plot results for cluster number.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports PCA variance for GM clustering.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Regression of lesion volume from cluster membership (internal validation).
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of lesion volume differences.
    - source_id: P6-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Regression of lesion volume from cluster membership (internal validation).
    - source_id: P6-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of lesion location via subtraction plots.
    - source_id: P6-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of clusters retained for combined data.
    - source_id: P6-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports PCA variance for combined clustering.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Regression of lesion volume from combined cluster membership.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of lesion location via subtraction plots.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion about dimensions captured by clustering.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to predictive utility results.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 12
      reason: Reports predictive power of both clustering types for AQ and compares
        them.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Details specific cluster associations with AQ in GM-only model.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Details specific cluster associations with AQ in combined model.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 13
      reason: Compares explanatory power of combined vs GM-only clustering for BNTtotal.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Details specific cluster associations with BNTtotal in GM-only model.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Details specific cluster associations with BNTtotal in combined model.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 13
      reason: Reports that combined clustering predicts PMG while GM-only does not.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Details specific cluster associations with PMG in combined model.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 12
      - 13
      reason: Synthesizes which models best predict which outcomes.
    - source_id: P8-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Commentary on statistical comparison of models.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to Aim 2 correlations.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports unadjusted correlations between AQ and all LH metrics.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports unadjusted correlations between BNTtotal/PMG and most LH metrics.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null unadjusted correlations for specific masks.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null unadjusted correlations for RH tracts.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null adjusted correlations for AQ.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Reports significant adjusted correlations for BNTtotal and specific
        tracts.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Reports significant adjusted correlations for PMG and specific tracts.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null adjusted correlations for RH tracts.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of combined GM+WM classification results.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion size and location information in clusters.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of null adjusted AQ results.
    - source_id: P10-S1-C8
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of adjusted naming and treatment results.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of adjusted naming and treatment results.
    - source_id: P12-S1-C4
      disposition: repeated
      result_indexes:
      - 13
      reason: Discussion restatement of model comparison results.
    - source_id: P12-S1-C5
      disposition: repeated
      result_indexes:
      - 13
      reason: Discussion restatement of model comparison results.
    - source_id: P12-S1-C6
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of adjusted naming and treatment results.
    - source_id: P12-S1-C9
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of null unadjusted results for temporal ROIs.
    - source_id: P12-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Part of a figure caption.
    - source_id: P12-S2-C4
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of null adjusted AF results.
    - source_id: P12-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table header.
    - source_id: P12-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table header.
    - source_id: P12-S2-C10
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      - 10
      reason: Table 4 contains the raw correlation and partial correlation data.
    - source_id: P13-S1-C1
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of null adjusted AF results.
    - source_id: P13-S1-C5
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of null RH results.
    - source_id: P13-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Forkel et al. 2014).
    - source_id: P13-S1-C10
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of null RH results.
    - source_id: P13-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of study limitations (low variance explained).
    - source_id: P14-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 4
      - 5
      reason: Conclusion restatement of clustering results.
    - source_id: P14-S1-C7
      disposition: repeated
      result_indexes:
      - 7
      - 8
      - 9
      reason: Conclusion restatement of adjusted structural results.
    unresolved_coverage:
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P3-S3-C9
    - P6-S2-C6
    - P6-S2-C8
    - P6-S2-C9
    - P6-S2-C11
    - P6-S2-C12
    - P6-S2-C14
    - P6-S3-C2
    - P6-S3-C3
    - P6-S3-C4
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C10
    - P6-S3-C11
    - P6-S3-C12
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P8-S2-C1
    - P8-S2-C2
    - P9-S1-C11
    - P9-S2-C1
    - P9-S2-C2
    - P9-S2-C3
    - P10-S1-C1
    - P10-S1-C3
    - P10-S1-C6
    - P10-S1-C8
    - P12-S1-C1
    - P12-S1-C4
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C9
    - P12-S2-C1
    - P12-S2-C4
    - P13-S1-C1
    - P13-S1-C5
    - P13-S1-C8
    - P13-S1-C10
    - P13-S1-C12
    - P14-S1-C6
    - P14-S1-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    - TABLE-3-page-8-3
    - TABLE-4-page-12-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C6
      recruited_sample:
      - P2-S3-C6
      eligibility:
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      imaging_provenance:
      - P3-S2-C6
      - P3-S3-C8
      - P4-S1-C2
      imaging_timing:
      - P1-S1-C5
      outcome_timing:
      - P3-S1-C2
      outcome_definition:
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C9
      validation: []
      analysis_restrictions:
      - P6-S1-C12
      - P6-S2-C4
      dependent_variable_statement:
      - P6-S1-C8
      - P6-S1-C11
      limitations:
      - P13-S1-C12
      - P13-S1-C13
      - P13-S1-C14
      - P14-S1-C2
      - P14-S1-C3
      - P14-S1-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C6
      - P7-S2-C1
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
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
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C1
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
      source_id: P9-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C11
      - P2-S2-C2
      - P6-S1-C12
      - P6-S2-C2
      - P9-S1-C5
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C8
      - P10-S1-C6
      - P12-S1-C8
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
      pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
      review_sha256: fbf8c63d37fb67316e5dc3c7ed2e363b0cac295988d8df6530b4c7a821146eb1
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
      - P7-S1-C5
      - P8-S1-C1
      source_result: The GM-only k-medoids clustering (4 clusters) significantly predicted
        overall aphasia severity (WAB-R AQ) with higher explained variance (R2 = 0.559)
        than the combined GM+WM model (R2 = 0.497). Specifically, patients in clusters
        2, 3, and 4 had significantly lower AQ scores than the reference cluster 1.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the GM-only clustering
            model predicting WAB-R AQ. The source confirms this specific model was
            tested and found significant (P7-S1-C5, P8-S1-C1).
          source_ids:
          - P7-S1-C5
          - P8-S1-C1
        direction:
          answer: fits
          reason: The claim that GM-only classification predicted severity is supported
            by the significant F-statistic and the specific finding that clusters
            2, 3, and 4 had lower AQ scores than cluster 1 (P8-S1-C1). The direction
            of association (lower AQ in certain clusters) is preserved.
          source_ids:
          - P8-S1-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as GM-only lesion classification
            based on spared voxels in cortical masks (P5-S1-C1). The outcome is WAB-R
            AQ (P3-S1-C1). The patient measurement is template_lesion_overlap, as
            the analysis relies on the intersection of patient lesion maps with template-based
            ROI masks to calculate spared tissue, not patient-specific tractography
            or raw diffusion metrics for this specific model.
          source_ids:
          - P5-S1-C1
          - P3-S1-C1
          - P4-S1-C5
        qualifications:
          answer: fits
          reason: The draft includes the specific cluster differences (clusters 2,
            3, 4 vs 1) which are material to the interpretation of the significant
            model. It also notes the comparison to the GM+WM model regarding explained
            variance, which is a key finding in the source (P7-S1-C5, P8-S2-C1).
          source_ids:
          - P8-S1-C1
          - P7-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding potential lack of power
            (P13-S1-C13). No other material caveats that would change the interpretation
            of the GM-only AQ result are omitted. The distinction between GM-only
            and GM+WM is preserved.
          source_ids:
          - P13-S1-C13
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.population
      original: patients with chronic stroke-induced aphasia (>=6 months post-onset)
        due to left hemisphere ischemic infarct with presence of anomia
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R001
      exposure:
        text: GM-only lesion classification (clusters)
      outcome:
        text: overall aphasia severity (WAB-R AQ)
      analysis_label: GM-only clustering prediction of aphasia severity
      relation: association
      evidence_ids:
      - P7-S1-C5
      - P8-S1-C1
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
        pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
        source_review: _compare/relationships-2026-11-16/review-current/Meier2019
        source_status_sha256: b3d71fb953ef86b0766fe402235d7a6d78f881a90c2f021c082a5a03827ba5f6
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0c61613ead3c1a89a71507d63cffc12d6f42dcfc5e8fba6d3dc30cb88d176f8c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 393b8a5559f73984053b509e07281a6c220c14cfb8d275499dc940c31040a731
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C6
          page: 2
          text_layer_sha256: 393b8a5559f73984053b509e07281a6c220c14cfb8d275499dc940c31040a731
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and methods

          Participants

          Thirty-four individuals (24 males; mean age = 61.91 ±

          10.84 years) with chronic stroke-induced aphasia (i.e., ≥six

          months post-onset; mean time post-onset = 61.18 ±

          86.49 months) due to left hemisphere ischemic infarct partic-

          ipated in the study.'
        anchor_text: 'Materials and methods

          Participants

          Thirty-four individuals (24 males; mean age = 61.91 ±

          10.84 years) with chronic stroke-induced aphasia (i.e., ≥six

          months post-onset; mean time post-onset = 61.18 ±

          86.49 months) due to left hemisphere ischemic infarct partic-

          ipated in the study.'
        excluded_fragments: []
        image_sha256: 028e4a7d957b18be0bbbc075a7bf674bd2df1f623a97db6604a892671bf1657a
        transcription: 'Materials and methods


          Participants


          Thirty-four individuals (24 males; mean age = 61.91 ± 10.84 years) with
          chronic stroke-induced aphasia (i.e., ≥ six months post-onset; mean time
          post-onset = 61.18 ± 86.49 months) due to left hemisphere ischemic infarct
          participated in the study'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'Specifically, both clus-

    tering types significantly predicted overall aphasia severity

    per WAB-R AQ, yet the predictive power of the GM-only

    lesion classification (F(3, 29) = 12.260, p < 0.001, R2 =

    0.559) was higher than the combined GM + WM clustering

    (F(3, 29) = 9.562, p < 0.001, R2 = 0.497).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
