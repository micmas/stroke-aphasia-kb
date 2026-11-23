---
id: medial_lemniscus_wmh_model
name: medial lemniscus and WMH combined predictor
kind: predictor
findings:
- id: f1
  target: executive_function
  target_kind: impairment
  claim: Poststroke executive function was associated with both stroke damage to the
    medial lemniscus and the presence of white matter hyperintensities, although no
    significant interaction between these two factors was detected.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: stroke survivors (ischemic or haemorrhagic) recruited from an acute
      stroke unit
    phase: not_reported
    time_post_onset: CT imaging acquired within 0-14 days post stroke; executive function
      assessed 6 months post stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Potential for overfitting due to relatively small sample size
  - Potential selection bias due to requirements for informed consent and 6-month
    follow-up
  - Assessment of WM damage and WMHs may have been complicated by cerebral edema
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multivariable linear regression model combining
    patient lesion overlap with the medial lemniscus reference tract template (defined
    as ≥10% disconnection via the HCP-842 atlas) and the presence of white matter
    hyperintensities (dichotomized as present or absent based on the Age-Related White
    Matter Changes Scale). Adjusted for age, sex, years of education, stroke type,
    stroke lateralization, stroke territory, and stroke volume; The association with
    the medial lemniscus did not reach the Bonferroni correction threshold when stroke
    territory was not included as a covariate. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P4-S2-C9, two-model
    agreement, human verification pending): RESULTS


    Participants

    We collected data from 122 stroke survivors from the acute stroke unit at Oxford
    University Hospital who had both completed a follow-up assessment using the OCS–Plus
    6 months post stroke and had a usable CT scan from the acute stage post stroke
    showing a visible stroke lesion Original text-layer quotation is preserved below.
    PDF image reading (P2-S2-C2, two-model agreement, human verification pending):
    . Our investigation

    included those individuals who had both completed a

    follow-up assessment using the OCS–Plus 6 months post

    stroke (between November 2016 through March 2020)

    and had a usable CT scan from the acute stage post stroke

    (i.e., within 0–14 days post stroke) showing a visible stroke

    lesion Original text-layer quotation is preserved below.'
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
    - proposed_concept:executive_function
  citation: '@Hobden2024'
  source_passages:
  - section: Original source P6-S1-C6
    page: 6
    quote: 'This model

      was signiﬁcant (F18, 68 = 3.86, R2 = 0.51, R2

      adjusted = 0.37,

      P < 0.001): Poststroke EF was associated with both

      stroke damage to the medial lemniscus (B = –8.86, P <

      0.018, 95% CI [–13.29 –4.43]) and the presence of

      WMHs (B = –5.42, P = 0.023, 95% CI [–9.12 –1.72]),

      although there was no signiﬁcant interaction between

      these factors.'
    supports: claim
  - section: Original source P4-S2-C9
    page: 4
    quote: 'RESULTS

      Participants

      We collected data from 122 stroke survivors from

      the acute stroke unit at Oxford University Hospital who

      had both completed a follow-up assessment using the

      OCS–Plus 6 months post stroke and had a usable CT scan

      from the acute stage post stroke showing a visible stroke

      lesion.'
    supports: sample
  - section: Original source P4-S2-C4
    page: 4
    quote: 'All of the analyses included age, sex, years of edu-

      cation, stroke type (ischemic, haemorrhagic), stroke lat-

      eralization (left, right, bilateral), stroke territory (anterior

      cerebral artery, middle cerebral artery, posterior cerebral

      artery, vertebrobasilar, intraventricular, multiple terri-

      tories), and stroke volume as covariates.'
    supports: confounders
  - section: Original source P3-S2-C2
    page: 3
    quote: 'The Le-

      sion Quantiﬁcation Toolkit (Grifﬁs et al., 2021) quantiﬁed

      WM tract disconnection severities based on the stroke le-

      sion delineation for 70 canonical WM tracts, as deﬁned by

      the HCP-842 streamline tractography atlas (Yeh et al.,

      2018) with the corpus callosum divided into ﬁve segments.'
    supports: method
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      WMH Ratings

      We used the Age-Related White Matter Changes

      visual rating scale to evaluate WMHs on CT imaging.'
    supports: method
  - section: Original source P2-S2-C2
    page: 2
    quote: 'Our investigation

      included those individuals who had both completed a

      follow-up assessment using the OCS–Plus 6 months post

      stroke (between November 2016 through March 2020)

      and had a usable CT scan from the acute stage post stroke

      (i.e., within 0–14 days post stroke) showing a visible stroke

      lesion.'
    supports: method
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Assessments

      The individuals completed the EF assessment in

      their homes 6 months post stroke using the OCS–Plus,

      which is a tablet-based cognitive screen that is designed

      to provide ﬁne-grained measures of memory and EF

      (Demeyere et al., 2021; Webb et al., 2022).'
    supports: method
  - section: Original source P8-S2-C4
    page: 8
    quote: "Using CT imaging in the present study led to the\nexclusion of a large\
      \ number of stroke survivors whose\nischemic lesions were not visible on acute\
      \ imaging, but\nwe justify our approach by noting the widespread use of\nCT\
      \ in clinical practice and therefore larger numbers\noverall than would be available\
      \ with routine clinical\nMR imaging.\n\x01 The relatively small sample size\
      \ may have caused\noverﬁtting in the multivariable linear regression models.\n\
      \x01 Although we aimed to include a clinically representative\nsample by recruiting\
      \ consecutively from a regional\nstroke unit, the need for informed consent\
      \ and 6-month\nfollow-up likely resulted in some selection bias."
    supports: limitation
predictor_type: imaging_metric
short_definition: A multivariable linear regression model combining patient lesion
  overlap with the medial lemniscus reference tract template (defined as ≥10% disconnection
  via the HCP-842 atlas) and the presence of white matter hyperintensities (dichotomized
  as present or absent based on the Age-Related White Matter Changes Scale).
assessment:
- Oxford Cognitive Screen–Plus rule-finding task
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hobden2024
  proposal_id: R005
  review_status_sha256: 056653dcd8559c420c65a733f9b054fa38f65d6facd8df014596f7af95581a8f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
        A/passages.json: 50a148ecfd1268b0a67bea3a0e64bce898df83732c69175b2e2f691d403f6543
        A/raw.json: 3b934db2f357a9ef63b5d2745dce72bf305a61523af081f5afa1e312609cdb58
        A/source-units.json: 8b15cada89c4720ab29bc157c85310eec5e4436e6cad8b305c4ec45994f264b1
        A/full-source-units.json: bb1841851a595e50cf1f8d3fa2038260945f3da0ec479fcfa7cd3af2b8ca05e7
        A/meta.json: c6785f6e5d87f0cbc23403337924d81fef88662c9e5c21be017b6bf5d5119121
        A/table-images/page-6.png: 1ab04c6d4adc9990c42fe55e1a524515a37fcca3e07dded7d948c4a8916c3ed9
        A/table-images/TABLE-1-page-4-2.png: bb5ca2d60d3d517b04ecbe4e9421d920eb3733c7ff4a888be9a576f7d05f4d24
        A/table-images/page-5.png: 47725843e90a349d4e729df6a47adf9fb3f447e9c3058e922acb91eaa0c0c114
        A/table-images/page-4.png: cd4eea3240889bdb624fd35793f182e98cc450caa36d03937636d317e9cfd474
        A/table-images/TABLE-1-page-4-1.png: ad2739049078cc4af0153b1a56f23a93b799b1d60deb7747e79a6b80e77d5e0d
        A/table-images/TABLE-3-page-6-1.png: fd8f01db96097836707236205250fabd0b6410e99cfe5121f7346f82030223c9
        A/table-images/manifest.json: 3f9ceffbf2017f759b0f189d21f6b263d7b5a8bf03b1c95c4738ea569431de88
        A/table-images/TABLE-2-page-5-1.png: dac134f90c17eb9ab05ad7d2a8db1c8ab64689450a06ee1d42e87d8351b49601
        A/clauses/window-03/raw.json: a97a093fd955b634a5f2a2e0e39c2923885c040d66ff1c626aa10f67f63ab957
        A/clauses/window-03/prompt.txt: ecd5e78db0e2dc41cbc1dce00cd301186d31c639ec86c62b7eeb21137314df92
        A/clauses/window-03/meta.json: 51c48d242bbdaa9d23768be53f926e0127bf2c8e7e51a4d512bbd61f38273d42
        A/clauses/window-04/raw.json: 46c34f143914fac06bf445afa0eddfbdb8597cf5953aa3123808fd315a34a213
        A/clauses/window-04/prompt.txt: 1b70aef52178c02ed11cf1c3bca1be8f2671224e338f1d765a8a65d324e64219
        A/clauses/window-04/meta.json: f666a7eec84398d79fb101e70bb127e51aa842c464591ebf9bd68bf4bc187f30
        A/clauses/window-05/raw.json: 548a90908648123bc0f176763ba21b7c2ae343fa66283411c1152040d0a667f5
        A/clauses/window-05/prompt.txt: 653e70cd4a360ce5b0f13a7c593a0f703ba0bbd8734c7db39ccf5492a17dbe33
        A/clauses/window-05/meta.json: 4e237d06a9c6c308337dc6b8c6ea4e92f74221bcf59f2466d853ea6a06b0bc16
        A/clauses/window-02/raw.json: ca7ddd987161c85b906d7e33ec1845f961bde3be828839e771497bd9187b73a1
        A/clauses/window-02/prompt.txt: 5dae2bd6bd36eba90cd25c78bf315f540d7b30039194e79c131c604849aac982
        A/clauses/window-02/meta.json: 5a4043327983c77837f3e25b06bcf97fb7e5ff9582159181ac04298d0e74c666
        A/clauses/window-07/raw.json: 7e8573a30853a01a1229e1bcceecfef31fe3dddc1f551860de40ad770b4513bb
        A/clauses/window-07/prompt.txt: 381b18280419e331e8b7e875e1e4f5f9cf4878f95ca816fdb8ed1408ff45c75d
        A/clauses/window-07/meta.json: c8db4d07c7d38c8537a519a7eaa63f55923fe4468c7716feab95edca678da50a
        A/clauses/window-01/raw.json: 30348fb81e03844d0127b91110a85cdb007c451e4ebf801eaf7ef65794dba8d6
        A/clauses/window-01/prompt.txt: 3f38c42703104a6e9ae749e5925470da4bf91b27a265703defbb2a7692284833
        A/clauses/window-01/meta.json: 233eedffce5c960759c71b31291c2408d994805e6fed3c7281cad1e7cfeed6ed
        A/clauses/window-06/raw.json: 91eb259cf614d78c9d9c216a30f217c092e88c98c682eb3eaf3f54d2665af80b
        A/clauses/window-06/prompt.txt: 1c4bdd453a55e57d6637e05df8676cecdf2c7d266a6a40e8dd64dceacc01a711
        A/clauses/window-06/meta.json: c3b7678574b24bbcc98ec972cd2c84b7e26a3de11b3baf220dc7472b0ce61c96
        A/tables/TABLE-2-page-5-2/raw.json: 151615120f9bc6285addd849c628cce932987e9e0cba85533cadcc63f689ef21
        A/tables/TABLE-2-page-5-2/prompt.txt: 1e7b1987a21511084531b548fa19021c14a2b9e8b9df78027f1973db6e2e4ba6
        A/tables/TABLE-2-page-5-2/meta.json: 8e636d84400e346240a9e2fef68f85c9abc3d1f0c247368d20acf638fbeba438
        A/tables/TABLE-3-page-6-3/raw.json: 51da1483a783f49e6d089bbfaa9794eedfab5d57767c3e85e155c259a7aa47ad
        A/tables/TABLE-3-page-6-3/prompt.txt: 4834498498cda5a5e7f50733e3c042814df7062f0528c3c12581c8cf4af75c98
        A/tables/TABLE-3-page-6-3/meta.json: 82825bafbd26a9e7ff84bed71550e83ba941e13265fd879bedcdf749b518a6ad
        A/tables/TABLE-1-page-4-1/raw.json: bca033aad372289a2fea5731832802f7914982677d1e3b1ebe46778c60712337
        A/tables/TABLE-1-page-4-1/prompt.txt: a75f981d9f44647f5ed2c012a4e9c0bc0d30da3ab1b6091b3b4961b677a57509
        A/tables/TABLE-1-page-4-1/meta.json: a2c9f0bd0dc2c939e9d4e4ad743e67ac2faeddaf98d710c2e1b308643c98bb88
        B/passages.json: 50a148ecfd1268b0a67bea3a0e64bce898df83732c69175b2e2f691d403f6543
        B/raw.json: aa794c5a462a40cfed7b677203a529418628b7ff385082357edb0e0139f20e87
        B/source-units.json: 8b15cada89c4720ab29bc157c85310eec5e4436e6cad8b305c4ec45994f264b1
        B/full-source-units.json: bb1841851a595e50cf1f8d3fa2038260945f3da0ec479fcfa7cd3af2b8ca05e7
        B/meta.json: 4e028ab5aa0799739ca925236fb0e0767cf79cfe1c66619180bfd58d22938aa7
        B/table-images/page-6.png: 1ab04c6d4adc9990c42fe55e1a524515a37fcca3e07dded7d948c4a8916c3ed9
        B/table-images/TABLE-1-page-4-2.png: bb5ca2d60d3d517b04ecbe4e9421d920eb3733c7ff4a888be9a576f7d05f4d24
        B/table-images/page-5.png: 47725843e90a349d4e729df6a47adf9fb3f447e9c3058e922acb91eaa0c0c114
        B/table-images/page-4.png: cd4eea3240889bdb624fd35793f182e98cc450caa36d03937636d317e9cfd474
        B/table-images/TABLE-1-page-4-1.png: ad2739049078cc4af0153b1a56f23a93b799b1d60deb7747e79a6b80e77d5e0d
        B/table-images/TABLE-3-page-6-1.png: fd8f01db96097836707236205250fabd0b6410e99cfe5121f7346f82030223c9
        B/table-images/manifest.json: e6bc985dd8f222b597ecc0a4b0a369362c4c379a2698eaf72786f4270fbe5bba
        B/table-images/TABLE-2-page-5-1.png: dac134f90c17eb9ab05ad7d2a8db1c8ab64689450a06ee1d42e87d8351b49601
        B/clauses/window-03/raw.json: 30a48a73b042d72339600c5255233297f93f1cb1708e97d7f8123bd6ab0dd020
        B/clauses/window-03/prompt.txt: ecd5e78db0e2dc41cbc1dce00cd301186d31c639ec86c62b7eeb21137314df92
        B/clauses/window-03/meta.json: f151abc2c85263e317fb13b66a8d49e614070f724be48e68ad837cfc952cf3a3
        B/clauses/window-04/raw.json: 6528bbf33e5c9cc178fc130d01978e3d118b9d50b5f6f5b5821c4cd634108d5e
        B/clauses/window-04/prompt.txt: 1b70aef52178c02ed11cf1c3bca1be8f2671224e338f1d765a8a65d324e64219
        B/clauses/window-04/meta.json: 9107048f5d2035589ac959dfc0ff8391e0d3f6dfa5470384b26e8e7a366a50ee
        B/clauses/window-05/raw.json: c21171f3d784a27a52ef731d508b4b1560d39cdd56ecfa80f243c63aa261c566
        B/clauses/window-05/prompt.txt: 653e70cd4a360ce5b0f13a7c593a0f703ba0bbd8734c7db39ccf5492a17dbe33
        B/clauses/window-05/meta.json: b148b51f1129c90657b369968b60a0830167882e446ca0cde2a5825262a0d0a0
        B/clauses/window-02/raw.json: 6b39ff6a5579d783eabaa846032f6bc469a61c6e07e9c2aac05f03ea22f8ce06
        B/clauses/window-02/prompt.txt: 5dae2bd6bd36eba90cd25c78bf315f540d7b30039194e79c131c604849aac982
        B/clauses/window-02/meta.json: 2db3a241b15530ddab68d08d08636002f4ba289896d5f1731ca936ce8d097263
        B/clauses/window-07/raw.json: a6567e28bde408e5319dfa9ece9d95f326376b992155577e31ddc2e048296383
        B/clauses/window-07/prompt.txt: 381b18280419e331e8b7e875e1e4f5f9cf4878f95ca816fdb8ed1408ff45c75d
        B/clauses/window-07/meta.json: 4a39d74947eed7a2d71b65d179d4ce68f80b876e865a7108064a17565c2a56a6
        B/clauses/window-01/raw.json: bdccdf512a720a55d8c3c9220f3192acf2ce6ddd8a91b27b66e60d5f93bb9d13
        B/clauses/window-01/prompt.txt: 3f38c42703104a6e9ae749e5925470da4bf91b27a265703defbb2a7692284833
        B/clauses/window-01/meta.json: e65f85b5ea8509dab5f771601f21f45fd67b0853a9bef4ceab0e598d37fd31e3
        B/clauses/window-06/raw.json: 53de99291ec14eed7b23765d12586196675618e9a593c9c86cdf87b7750f6424
        B/clauses/window-06/prompt.txt: 1c4bdd453a55e57d6637e05df8676cecdf2c7d266a6a40e8dd64dceacc01a711
        B/clauses/window-06/meta.json: f539ab00da1911d1cb8263839d8d9608a50805b8e7a7f3ec05cfe8718d664cbb
        B/tables/TABLE-2-page-5-2/raw.json: cd843812eeaf3a33f164e0547f3719e561b9dd3e1d25d6fadac950148de824a9
        B/tables/TABLE-2-page-5-2/prompt.txt: 1e7b1987a21511084531b548fa19021c14a2b9e8b9df78027f1973db6e2e4ba6
        B/tables/TABLE-2-page-5-2/meta.json: 78b37dd5d42467841fcc653161558df5d63107d8426f494b208105886de57198
        B/tables/TABLE-3-page-6-3/raw.json: a5f219aed467da0b27d6a312828780372e27e71a6e4010374bb26e163f3da4fd
        B/tables/TABLE-3-page-6-3/prompt.txt: 4834498498cda5a5e7f50733e3c042814df7062f0528c3c12581c8cf4af75c98
        B/tables/TABLE-3-page-6-3/meta.json: 051fec548da35f84007dbf51298acccfdee0a713b3d3a60e78750c6646ee29a3
        B/tables/TABLE-1-page-4-1/raw.json: 136670fc4e48e0d1dcfb9617523d23309639a6d686717aa3c23aa12615d253e6
        B/tables/TABLE-1-page-4-1/prompt.txt: a75f981d9f44647f5ed2c012a4e9c0bc0d30da3ab1b6091b3b4961b677a57509
        B/tables/TABLE-1-page-4-1/meta.json: 4119734ea636d77ba34b022cf7465a15ad3a6bb546c8f617dcde7bd1db1c351a
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
      pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
      source_review: _compare/relationships-2026-11-16/review-current/Hobden2024
      source_status_sha256: a3a9b07251bba876df8826f6b7b240f3c17b36f90c1046cec01b681a3600e318
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: stroke damage to the medial lemniscus and presence of WMHs
    outcome:
      text: poststroke executive function (OCS–Plus rule-finding task accuracy score)
    analysis_label: Multivariable linear regression (combined WM damage and WMHs)
    relation: association
    evidence_ids:
    - P6-S1-C6
    qualifier_ids:
    - P4-S2-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
      source_review: _compare/relationships-2026-11-16/review-current/Hobden2024
      source_status_sha256: a3a9b07251bba876df8826f6b7b240f3c17b36f90c1046cec01b681a3600e318
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C5
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P5-S1-C5
      - Unaccounted source passage P5-S1-C3
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C9
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C10
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P8-S1-C9
      - Result passage disposed without unit P8-S2-C1
      - Accounting without a linked unit P8-S2-C4
      - Unaccounted source passage P8-S1-C9
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P8-S2-C4
      unattached_null_or_qualifier_ids:
      - P6-S1-C6
      - P7-S1-C8
      - P7-S1-C9
      - P8-S1-C3
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 156
      unselected_timing_passages:
      - P1-S1-C5
      - P1-S1-C6
      - P1-S1-C7
      - P2-S1-C10
      - P2-S1-C11
      - P3-S1-C6
      - P4-S2-C9
      - P4-S2-C13
      - P4-S2-C14
      - P8-S1-C9
      - P8-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: outcome_timing
        source_ids:
        - P1-S1-C6
        - P2-S2-C2
        - P2-S2-C6
        - P3-S1-C6
        - P4-S2-C9
        - P5-S1-C1
        - P6-S1-C1
        - P7-S1-C1
        - P7-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C10
        - P4-S2-C4
        - P5-S1-C9
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C14
        - P6-S1-C1
        - P6-S1-C2
        - P6-S1-C6
        - P7-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C10
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C13
        - P4-S2-C14
        - P4-S2-C15
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C5
        - P5-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P5-S1
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
      source_review: _compare/relationships-2026-11-16/review-current/Hobden2024
      source_status_sha256: a3a9b07251bba876df8826f6b7b240f3c17b36f90c1046cec01b681a3600e318
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of combined model results in abstract.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 1
      - 3
      - 4
      reason: General conclusion restating associations.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the dichotomization process for WMHs.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic for OCS-Plus score.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic for stroke volume.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to a table of descriptive statistics.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about lesion coverage.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic for disconnected ROIs.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive distribution of WMH categories.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of overall WM disconnection analysis.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of individual ROI analysis.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports significance of covariates (age, stroke volume) rather than
        the primary exposure.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result of sensitivity analysis without stroke territory.
    - source_id: P5-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports model variance (R2) rather than a specific relationship.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Direct result of WMH analysis.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports significance of covariates.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about non-significant covariates.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Direct results for combined model and interaction.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Direct result for the control task analysis.
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 3
      reason: Discussion restatement of primary findings.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of medial lemniscus finding.
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion of the nature of the association.
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of sensitivity analysis.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Direct report of null findings for other WM pathways.
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of WMH finding.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of combined model result.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Direct result of sensitivity analysis excluding edema.
    unresolved_coverage:
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P4-S1-C11
    - P5-S1-C1
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C12
    - P5-S1-C15
    - P6-S1-C2
    - P6-S1-C3
    - P7-S1-C1
    - P7-S1-C4
    - P7-S1-C8
    - P7-S1-C9
    - P7-S2-C4
    - P8-S1-C1
    - P8-S1-C3
    - P8-S1-C10
    - P8-S2-C3
    - P8-S2-C5
    - P8-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C11
      - P4-S2-C12
      - P5-S1-C10
      recruited_sample:
      - P1-S1-C5
      - P2-S1-C10
      - P2-S1-C11
      eligibility:
      - P1-S1-C5
      - P1-S1-C7
      - P2-S1-C11
      - P2-S2-C2
      - P2-S2-C3
      imaging_provenance:
      - P2-S1-C5
      - P3-S1-C7
      - P3-S1-C8
      - P4-S1-C1
      imaging_timing:
      - P2-S2-C2
      - P3-S1-C7
      - P4-S3-C5
      outcome_timing: []
      outcome_definition:
      - P2-S2-C10
      - P2-S2-C13
      - P2-S3-C7
      - P4-S2-C3
      - P4-S2-C6
      - P5-S1-C1
      validation:
      - P2-S2-C7
      analysis_restrictions:
      - P4-S2-C8
      dependent_variable_statement:
      - P4-S1-C14
      - P4-S2-C3
      - P4-S2-C6
      - P6-S1-C5
      limitations:
      - P8-S1-C8
      - P8-S1-C9
      - P8-S1-C10
      - P8-S2-C2
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P5-S1-C14
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: outcome_timing
      source_ids:
      - P1-S1-C6
      - P2-S2-C2
      - P2-S2-C6
      - P3-S1-C6
      - P4-S2-C9
      - P5-S1-C1
      - P6-S1-C1
      - P7-S1-C1
      - P7-S1-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C10
      - P4-S2-C4
      - P5-S1-C9
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C14
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C6
      - P7-S1-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C10
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C13
      - P4-S2-C14
      - P4-S2-C15
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C5
      - P5-S2-C3
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
      pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
      review_sha256: 056653dcd8559c420c65a733f9b054fa38f65d6facd8df014596f7af95581a8f
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
      - P6-S1-C6
      source_result: In a multivariable linear regression model including both stroke
        lesion-related WM damage (specifically medial lemniscus disconnection) and
        WMHs as predictors, poststroke executive function (OCS-Plus rule-finding task
        accuracy) was significantly associated with both medial lemniscus damage (B
        = -8.86, P < 0.018) and the presence of WMHs (B = -5.42, P = 0.023). The model
        was significant (F18, 68 = 3.86, R2 = 0.51), but no significant interaction
        was found between the two factors. The analysis adjusted for age, sex, education,
        stroke type, lateralization, territory, and volume.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R005 corresponds to the combined model described
            in P6-S1-C6, which evaluates the relative contributions of stroke lesion-related
            WM damage (medial lemniscus) and WMHs to poststroke EF. The proposed core
            correctly identifies this as a multivariable linear regression combining
            these two predictors.
          source_ids:
          - P6-S1-C6
          - P4-S2-C2
        direction:
          answer: fits
          reason: The source states that EF was associated with both factors, with
            negative B coefficients indicating poorer EF with damage/presence. The
            proposed claim states 'associated with both... although no significant
            interaction', which preserves the detected association direction and the
            null interaction finding.
          source_ids:
          - P6-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as stroke damage to the medial
            lemniscus (measured via template overlap with HCP-842 atlas, P3-S2-C2)
            and presence of WMHs (P4-S1-C1). The outcome is the OCS-Plus rule-finding
            task accuracy (P4-S2-C3). The patient measurement is template_lesion_overlap,
            as the lesion is overlaid on the reference tract map to calculate disconnection
            severity, not patient-derived diffusion tractography.
          source_ids:
          - P3-S2-C2
          - P4-S1-C1
          - P4-S2-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the necessary covariates (age, sex, education,
            stroke type, lateralization, territory, volume) as per P4-S2-C4. It also
            correctly notes the lack of significant interaction. The qualification
            regarding the Bonferroni threshold for the medial lemniscus when stroke
            territory is excluded (P5-S1-C14) is included as a qualification, which
            is appropriate as it contextualizes the robustness of the medial lemniscus
            finding in the combined model context.
          source_ids:
          - P4-S2-C4
          - P5-S1-C14
        missing_material_caveat:
          answer: fits
          reason: The core includes limitations regarding overfitting and selection
            bias (P8-S2-C4). The lack of interaction is explicitly stated in the claim.
            No material caveats that change the interpretation of the combined model's
            significance are omitted.
          source_ids:
          - P8-S2-C4
          - P6-S1-C6
      optional_pending:
      - Sample size (n=87) is available in P4-S2-C11 but not transcribed in the core
        fields; this is an optional omission for a qualitative draft.
      - Specific statistical values (B, P, CI) are not transcribed in the core fields,
        which is consistent with the qualitative draft requirement.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=87) is available in P4-S2-C11 but not transcribed in the core
      fields; this is an optional omission for a qualitative draft.
    - Specific statistical values (B, P, CI) are not transcribed in the core fields,
      which is consistent with the qualitative draft requirement.
    normalizations:
    - field: sample.n
      original: 87
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R005
      exposure:
        text: stroke damage to the medial lemniscus and presence of WMHs
      outcome:
        text: poststroke executive function (OCS–Plus rule-finding task accuracy score)
      analysis_label: Multivariable linear regression (combined WM damage and WMHs)
      relation: association
      evidence_ids:
      - P6-S1-C6
      qualifier_ids:
      - P4-S2-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
        source_review: _compare/relationships-2026-11-16/review-current/Hobden2024
        source_status_sha256: a3a9b07251bba876df8826f6b7b240f3c17b36f90c1046cec01b681a3600e318
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f8d7f4d74878f475efc647a9c186dca638de4d93a2cd16ab5bda0fa26002dc3f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C9
          page: 4
          text_layer_sha256: f8d7f4d74878f475efc647a9c186dca638de4d93a2cd16ab5bda0fa26002dc3f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'RESULTS

          Participants

          We collected data from 122 stroke survivors from

          the acute stroke unit at Oxford University Hospital who

          had both completed a follow-up assessment using the

          OCS–Plus 6 months post stroke and had a usable CT scan

          from the acute stage post stroke showing a visible stroke

          lesion.'
        anchor_text: 'RESULTS

          Participants

          We collected data from 122 stroke survivors from

          the acute stroke unit at Oxford University Hospital who

          had both completed a follow-up assessment using the

          OCS–Plus 6 months post stroke and had a usable CT scan

          from the acute stage post stroke showing a visible stroke

          lesion.'
        excluded_fragments: []
        image_sha256: 63e3a235524f3d36f6056d4f583125d5126d56ea20d0bd7224ce8f2084f7bd97
        transcription: 'RESULTS


          Participants

          We collected data from 122 stroke survivors from the acute stroke unit at
          Oxford University Hospital who had both completed a follow-up assessment
          using the OCS–Plus 6 months post stroke and had a usable CT scan from the
          acute stage post stroke showing a visible stroke lesion'
      P2-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b6b6cbbc53ef62d00092540499d1ad4cf4d454b069c1731d0779524bcb7d2a6f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C2
          page: 2
          text_layer_sha256: b6b6cbbc53ef62d00092540499d1ad4cf4d454b069c1731d0779524bcb7d2a6f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Our investigation

          included those individuals who had both completed a

          follow-up assessment using the OCS–Plus 6 months post

          stroke (between November 2016 through March 2020)

          and had a usable CT scan from the acute stage post stroke

          (i.e., within 0–14 days post stroke) showing a visible stroke

          lesion.'
        anchor_text: 'Our investigation

          included those individuals who had both completed a

          follow-up assessment using the OCS–Plus 6 months post

          stroke (between November 2016 through March 2020)

          and had a usable CT scan from the acute stage post stroke

          (i.e., within 0–14 days post stroke) showing a visible stroke

          lesion.'
        excluded_fragments: []
        image_sha256: 79d4ab175d5fc773ec34cc3f8c7f3d7e4865a40e2f9e08610477049da443a073
        transcription: '. Our investigation

          included those individuals who had both completed a

          follow-up assessment using the OCS–Plus 6 months post

          stroke (between November 2016 through March 2020)

          and had a usable CT scan from the acute stage post stroke

          (i.e., within 0–14 days post stroke) showing a visible stroke

          lesion'
      P8-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 19305676cf466d176c1bbb40b44d7249e2557d24d1d75cd0b2c7f3de83b1d3ed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 14b82c82adaae13007bf4c9e4280653f69bb8595f0ea569f39f88067553f05fe
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S2-C4
          page: 8
          text_layer_sha256: 14b82c82adaae13007bf4c9e4280653f69bb8595f0ea569f39f88067553f05fe
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Using CT imaging in the present study led to the\nexclusion\
          \ of a large number of stroke survivors whose\nischemic lesions were not\
          \ visible on acute imaging, but\nwe justify our approach by noting the widespread\
          \ use of\nCT in clinical practice and therefore larger numbers\noverall\
          \ than would be available with routine clinical\nMR imaging.\n\x01 The relatively\
          \ small sample size may have caused\noverﬁtting in the multivariable linear\
          \ regression models.\n\x01 Although we aimed to include a clinically representative\n\
          sample by recruiting consecutively from a regional\nstroke unit, the need\
          \ for informed consent and 6-month\nfollow-up likely resulted in some selection\
          \ bias."
        anchor_text: "Using CT imaging in the present study led to the\nexclusion\
          \ of a large number of stroke survivors whose\nischemic lesions were not\
          \ visible on acute imaging, but\nwe justify our approach by noting the widespread\
          \ use of\nCT in clinical practice and therefore larger numbers\noverall\
          \ than would be available with routine clinical\nMR imaging.\n\x01 The relatively\
          \ small sample size may have caused\noverﬁtting in the multivariable linear\
          \ regression models.\n\x01 Although we aimed to include a clinically representative\n\
          sample by recruiting consecutively from a regional\nstroke unit, the need\
          \ for informed consent and 6-month\nfollow-up likely resulted in some selection\
          \ bias."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'This model

    was signiﬁcant (F18, 68 = 3.86, R2 = 0.51, R2

    adjusted = 0.37,

    P < 0.001): Poststroke EF was associated with both

    stroke damage to the medial lemniscus (B = –8.86, P <

    0.018, 95% CI [–13.29 –4.43]) and the presence of

    WMHs (B = –5.42, P = 0.023, 95% CI [–9.12 –1.72]),

    although there was no signiﬁcant interaction between

    these factors.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
