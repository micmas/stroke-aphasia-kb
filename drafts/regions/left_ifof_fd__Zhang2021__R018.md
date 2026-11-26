---
id: left_ifof_fd
name: left IFOF fiber density
kind: tract
findings:
- id: f1
  target: word_level_comprehension
  target_kind: impairment
  claim: The mean fiber density of the left IFOF is significantly positively correlated
    with word-level comprehension scores.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: concurrent; mean time from stroke onset to enrollment was 13.2
      days
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - heterogeneity of aphasia symptom profiles
  - template-based tractography may not fully capture inter-individual variability
    in tract morphology
  - relatively small number of diffusion directions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: mean fiber density (FD) extracted from the left inferior
    fronto-occipital fasciculus (IFOF) using XTRACT automated tractography and fixel-based
    analysis. Spearman''s partial correlation was used; significance threshold was
    adjusted by Bonferroni correction; adjusted for nuisance covariates including
    age, sex, education level, whole-brain averaged values, lesion volume, and cortical
    involvement of lesion. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P5-S1-C9, two-model agreement,
    human verification pending): . The mean time from stroke onset to enrollment was
    13.2 (7.3)

    days Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - not_transcribed:sample.population
    - proposed_concept:word_level_comprehension
  citation: '@Zhang2021'
  source_passages:
  - section: Original source P5-S3-C12
    page: 5
    quote: "Word-level comprehen­\nsion subdomain significantly correlated with the\
      \ IFOF (r = 0.723, p <\n0.001), while sentence-level comprehension subdomain\
      \ showed a trend- \nlevel positive correlation with the SLF III (r = 0.451,\
      \ p = 0.021)."
    supports: claim
  - section: Original source P2-S4-C3
    page: 2
    quote: "Eligibility criteria included a history \nof initial left-hemisphere ischemic\
      \ stroke during the early subacute stage \n(7 days to 1 month), aphasia confirmed\
      \ by the language scale, age \n18–80 years, right-handedness, Chinese as a first\
      \ language, and educa­\ntion experience ≥6 years."
    supports: sample
  - section: Original source P5-S1-C9
    page: 5
    quote: "The mean time from stroke onset to enrollment was 13.2 (7.3) \ndays."
    supports: sample
  - section: Original source P4-S1-C13
    page: 4
    quote: "We chose seven dual- \nstream tracts (the SLF III, AF, IFOF, UF, ILF,\
      \ MdLF, and frontal aslant \ntract) as TOIs defined by XTRACT, a novel automated\
      \ tractography \nprotocol (see detailed techniques in Supplemental Method 2)\
      \ (War­\nrington et al., 2020)."
    supports: method
  - section: Original source P5-S1-C2
    page: 5
    quote: "Considering the language scores were \nnot normal distribution, Spearman’s\
      \ partial correlation analysis was \nused to investigate the relationship between\
      \ language scores and within- \nTOI mean values in the stroke group."
    supports: method
  - section: Original source P5-S1-C4
    page: 5
    quote: "Age, sex, education level, whole-brain averaged values, lesion vol­\n\
      ume, and cortical involvement of lesion were considered as nuisance \ncovariates\
      \ for the results."
    supports: confounders
  - section: Original source P9-S2-C3
    page: 9
    quote: "The relatively small sample size reduced \nstatistical power and precluded\
      \ the investigation of subgroup differ­\nences."
    supports: limitation
  - section: Original source P9-S2-C4
    page: 9
    quote: "Template-based tractography may lead to insufficient capture of \ninter-individual\
      \ variability in tract morphology for the patients with \nstroke."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2021
  proposal_id: R018
  review_status_sha256: 8efc3be14543c82d88880d3628246940c8e3eac12b049709f9762e1be5b31371
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
        A/passages.json: 7f739af7ba5780497af6ac81d613ada59a1393d16f7a70af0c5fd9fa5e38c925
        A/raw.json: f3f49c6ce898c63b80238f91c489b3bef7472cf6c06f511f577b0951c80f2768
        A/source-units.json: c858db8c099628f650f74c5ccd389dfacf45456be07c2646f2362e75296849eb
        A/full-source-units.json: e8f44819edcf4a4ceb6a1d90f91c8dba9ad718f9d7d7fd210795ff51abd72722
        A/meta.json: fae07cb3fcba9505b0e3b397a32c3f4da3d45f2af0a4b363269e80b2cbf61894
        A/table-images/TABLE-1-page-5-1.png: eba1d299675ca88511b5f7a10fe7c810eb9ea41f86f79419ed57d0c2832e7aee
        A/table-images/page-5.png: 473d41074af46d584d8c85d463746c7ba8ce81235ffd091e4e92575cc4ac2253
        A/table-images/manifest.json: e5f360aefcecbfeb79f7c48cf0cb1e5a527303a04d3b7ba0b22a0b15262bc3f9
        A/clauses/window-03/raw.json: b7ec449b7dcf432517894024a1328cf7bee09413b9952467d33258be4cec9c64
        A/clauses/window-03/prompt.txt: 2dcdfa3e2337d26295f3ee02f3f154a7f3bdd95aa464accd88b0a45dcbd69d05
        A/clauses/window-03/meta.json: f42f8ae8646028d2681ee922e07e5e120a24162b0629ecb842d135885a0b21b8
        A/clauses/window-04/raw.json: b060ec8462a46bbedc474d032de69270f29b73a3e6015d50b78f45cd892aa2cd
        A/clauses/window-04/prompt.txt: 344bd17e0c405b1d0ea57c87c7e10eec073184c38c3e3250075872e7b5084279
        A/clauses/window-04/meta.json: c0eee9abca05d58cd7ca568a12dab7cc1d5f531a110d27981d19d4e52e983804
        A/clauses/window-05/raw.json: 3b882bacaf157bd7767704a6e8d49c3e60937ca690cfc19e9875abaaf5afb233
        A/clauses/window-05/prompt.txt: b3dca1d23ad9f73d085944733b468b095dd9741b3f73969888927eb81ad214a7
        A/clauses/window-05/meta.json: d21c097f75cdc45c30e5e60e696cc0353dbd229afa4c6305144f0f6b67d659df
        A/clauses/window-02/raw.json: 7cc1b785b035e5707ab86e98160ae0898afd11ec9a28a6e6eca79b4a88699d06
        A/clauses/window-02/prompt.txt: 4cd470c1a7dcb9c94ff7180242828d50843ad77e6ec40b1ba5d1e50546e3d8b6
        A/clauses/window-02/meta.json: b0d6093499298bacfd41891fa3fe9d6c5facfc088f563e743405659c46aa6962
        A/clauses/window-09/raw.json: d25a36c2253ff09020b81603a751c49a610ebc928fa31539d49f2493af8d915e
        A/clauses/window-09/prompt.txt: 35b653b9e7e8e03df0af421bc6af5b2123dbb5be33d0e65ca5e37b9e3fcd4842
        A/clauses/window-09/meta.json: a6a77d08eaaf46388071988ba3fcb18f037c9705d7a3b0cc357b2270477da993
        A/clauses/window-07/raw.json: 9b4115e79301c13cb59d9182ec3358fd1d0bd0b14f1bff730b82d9e7999f4c99
        A/clauses/window-07/prompt.txt: b176fee496c5def0d759cbabfef40aed3080f8b6a8b5bf75d4e86a2f834434b8
        A/clauses/window-07/meta.json: a62228ee69724316fec8afbb6082e8a9acc09b1f11be88bd7b2e5c6fc9a08935
        A/clauses/window-01/raw.json: 277c2a893ff2cd25bef4478bf760d5ff5e8c38b822a78fa98bce3d1bb13c8d32
        A/clauses/window-01/prompt.txt: 326bf1186bbd19f309742420df51f315f9f1324f2b81f2217b2e4e85ae1cc89b
        A/clauses/window-01/meta.json: 9d7924ed49d5900aa764adea3fca91d5901a1353dd36c6d3a8db060d909c7437
        A/clauses/window-06/raw.json: 8b42d2b20015b4b4594b6b4c23ae7c8bd66d49438e7d100a8c3b51d0e7614cae
        A/clauses/window-06/prompt.txt: c1929a55a92a093093946988911b85b7a1c66fe94b3815d73df22006eef0ea94
        A/clauses/window-06/meta.json: d5bd65d825c9e1ccb3a0702f99201f66ee5e626e0d069ef8ee6cce02c63b0fa7
        A/clauses/window-08/raw.json: 80fdaaf923520d419f54f26c5d1d25ea8a9d03f1f219c13c68a08bde95d18c4f
        A/clauses/window-08/prompt.txt: 312371d651a0c855dfb6301a8311a7c74a2c32bef71a803e8f6bc35587834efc
        A/clauses/window-08/meta.json: 1b20ae656a6a471b47e9203c4b8c4a6762fb9565a935f3c553c9e6fa8baab1af
        A/tables/TABLE-1-page-5-1/raw.json: cabf2402f45f8852958426f2865e1534a802d4ac52e570e4a926ed0aba6df417
        A/tables/TABLE-1-page-5-1/prompt.txt: 65543503d9f718727eb635097286e8dd3d5e5ebda263bec78c60ebf1b5f45c2f
        A/tables/TABLE-1-page-5-1/meta.json: 4bbbdb1490aa45796db925852b3cd99b2d09d32d4cdc500c037e6c68723378f8
        B/passages.json: 7f739af7ba5780497af6ac81d613ada59a1393d16f7a70af0c5fd9fa5e38c925
        B/raw.json: 694dc51f88751a957befb9272367863520aa20360433c5434e50dc291effb5c4
        B/source-units.json: c858db8c099628f650f74c5ccd389dfacf45456be07c2646f2362e75296849eb
        B/full-source-units.json: e8f44819edcf4a4ceb6a1d90f91c8dba9ad718f9d7d7fd210795ff51abd72722
        B/meta.json: 5ef10497b7352e5fed943f9ccbd67bab1f1908258e83c03029ff26e01ed6e757
        B/table-images/TABLE-1-page-5-1.png: eba1d299675ca88511b5f7a10fe7c810eb9ea41f86f79419ed57d0c2832e7aee
        B/table-images/page-5.png: 473d41074af46d584d8c85d463746c7ba8ce81235ffd091e4e92575cc4ac2253
        B/table-images/manifest.json: 0640e3abce873d7e0bf140700968a76cb303c229797e82b458ea9aa9317fade0
        B/clauses/window-03/raw.json: 016487559c96b06afda985ddedb936ef1ce8277374c7258954c5b4c8059b3506
        B/clauses/window-03/prompt.txt: 2dcdfa3e2337d26295f3ee02f3f154a7f3bdd95aa464accd88b0a45dcbd69d05
        B/clauses/window-03/meta.json: ed1cff99d0203d419d5a6bb54ba88452b074506d5358cd73933ca88b6c85f1b7
        B/clauses/window-04/raw.json: 993965f33b4944c187a932a9343b336dbf266363c3194d967c116b1f69addf9b
        B/clauses/window-04/prompt.txt: 344bd17e0c405b1d0ea57c87c7e10eec073184c38c3e3250075872e7b5084279
        B/clauses/window-04/meta.json: 47c9e177746c6fd5d668805fe2141d9f861d154fe444219bc732445bad6f9222
        B/clauses/window-05/raw.json: 9c79a5348cba8661790503bd7b999fb7c37c628771fd56b6d16be18d909fa1bd
        B/clauses/window-05/prompt.txt: b3dca1d23ad9f73d085944733b468b095dd9741b3f73969888927eb81ad214a7
        B/clauses/window-05/meta.json: 3a89254ea61162a28ef2a00a424e3d5fc22fd0f509edd729f51162d5311e1195
        B/clauses/window-02/raw.json: e1363f4b61da43742028769e485cf3d32e8cbfe60380b2fcb91ad46c6ce1fdfd
        B/clauses/window-02/prompt.txt: 4cd470c1a7dcb9c94ff7180242828d50843ad77e6ec40b1ba5d1e50546e3d8b6
        B/clauses/window-02/meta.json: 40ca06011b71bdb1677ade71a453c29b31e2e9fd56d4f41c66c3dfcd68bd8cca
        B/clauses/window-09/raw.json: 8b398165f9d1efd4201a5128ef4cb9dbedb16f995728c306a56dd6c88d499cf3
        B/clauses/window-09/prompt.txt: 35b653b9e7e8e03df0af421bc6af5b2123dbb5be33d0e65ca5e37b9e3fcd4842
        B/clauses/window-09/meta.json: 6d37e9604ac199e203ffe2e382a9f0134a4d59e580b062bb33a7addff233cfe2
        B/clauses/window-07/raw.json: 514030407b16a096243d4e5c228c5dcf817822cdc8cab2528a2441aff7e97fff
        B/clauses/window-07/prompt.txt: b176fee496c5def0d759cbabfef40aed3080f8b6a8b5bf75d4e86a2f834434b8
        B/clauses/window-07/meta.json: 102ec575afc988867f0571f1f4f8fd7d369b1ea7b6872abfa30d8c5c0f6f35a8
        B/clauses/window-01/raw.json: 52d95f38c402db00841ee3c9edb22ea8a683299556d055d706321c0d8939d6cd
        B/clauses/window-01/prompt.txt: 326bf1186bbd19f309742420df51f315f9f1324f2b81f2217b2e4e85ae1cc89b
        B/clauses/window-01/meta.json: 3650e50e01205e18431eec1eaac55672671fd28d888ed10a341df5c70cffbf5a
        B/clauses/window-06/raw.json: 3bfb3a1bc49473c397dc576705650d865e4f1930979b9388cafbe9ba3cb7d02b
        B/clauses/window-06/prompt.txt: c1929a55a92a093093946988911b85b7a1c66fe94b3815d73df22006eef0ea94
        B/clauses/window-06/meta.json: 5ed765e35f606fd1bdfc69230120392bf468666b48ab2b2f5832fffb793476ee
        B/clauses/window-08/raw.json: 19d0e00c5c249d4828c013b7ed486879b51ead8a33156d5e2595d83656c36486
        B/clauses/window-08/prompt.txt: 312371d651a0c855dfb6301a8311a7c74a2c32bef71a803e8f6bc35587834efc
        B/clauses/window-08/meta.json: 203c0fbc8faaeee2e20657767317540e037943035ff5b394aae8d2921bbef62e
        B/tables/TABLE-1-page-5-1/raw.json: d068e8706b9914e6e660c5e88e130ee1ab3f6d257c8f4fdffe357d75e68c4b8c
        B/tables/TABLE-1-page-5-1/prompt.txt: 65543503d9f718727eb635097286e8dd3d5e5ebda263bec78c60ebf1b5f45c2f
        B/tables/TABLE-1-page-5-1/meta.json: e2fe81bf334b3c38b74e6201a11d93643f75d4b81dfca622a9ed6e1b0b617a59
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
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2021
      source_status_sha256: 965ee0a7e8cac2d75b5f626b72ffd3d06d6afd05ee1ffbd9cb1d7ec8a477cd36
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R018
    exposure:
      text: mean FD of left IFOF
    outcome:
      text: word-level comprehension
    analysis_label: Tract-wise language correlation (word-level comprehension)
    relation: association
    evidence_ids:
    - P5-S3-C12
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
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2021
      source_status_sha256: 965ee0a7e8cac2d75b5f626b72ffd3d06d6afd05ee1ffbd9cb1d7ec8a477cd36
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C5
      - Accounting without a linked unit P1-S2-C6
      - Accounting without a linked unit P1-S2-C7
      - Accounting without a linked unit P1-S2-C8
      - Unaccounted source passage P1-S2-C7
      - Unaccounted source passage P1-S2-C8
      - Unaccounted source passage P1-S2-C6
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C11
      - Accounting without a linked unit P5-S1-C13
      - Accounting without a linked unit P5-S1-C14
      - Accounting without a linked unit P5-S1-C15
      - Accounting without a linked unit P5-S1-C16
      - Accounting without a linked unit P5-S1-C17
      - Unaccounted source passage P5-S1-C15
      - Unaccounted source passage P5-S1-C14
      - Unaccounted source passage P5-S1-C13
      - Unaccounted source passage P5-S1-C17
      - Unaccounted source passage P5-S1-C16
      - Result passage disposed without unit P5-S2-C11
      - Accounting without a linked unit P5-S2-C13
      - Accounting without a linked unit P5-S2-C14
      - Result passage disposed without unit P5-S2-C15
      - Accounting without a linked unit P5-S2-C16
      - Accounting without a linked unit P5-S3-C2
      - Result passage disposed without unit P5-S3-C3
      - Unaccounted source passage P5-S3-C2
      - Unaccounted source passage P5-S2-C16
      - Unaccounted source passage P5-S2-C13
      - Unaccounted source passage P5-S2-C14
      - Result passage disposed without unit P5-S3-C10
      - Accounting without a linked unit P5-S3-C14
      - Accounting without a linked unit P5-S4-C2
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P5-S4-C2
      - Unaccounted source passage P5-S3-C14
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P6-S1-C2
      - Unaccounted source passage P6-S1-C5
      - Result passage disposed without unit P6-S2-C6
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P8-S1-C13
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C11
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P9-S1-C5
      - Result passage disposed without unit P9-S1-C6
      - Result passage disposed without unit P9-S1-C12
      - Result passage disposed without unit P9-S2-C10
      - Result passage disposed without unit P9-S2-C12
      - Result passage disposed without unit P9-S2-C13
      - Result passage disposed without unit P9-S2-C14
      unattached_null_or_qualifier_ids:
      - P6-S1-C1
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 180
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S3-C10
      - P5-S1-C8
      - P6-S1-C8
      - P9-S2-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C5
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
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
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
        source_id: P5-S3-C14
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
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P5-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      unlinked_tables:
      - TABLE-1-page-5-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P3-S3
        - P4-S2
        - P5-S1
        - P5-S2
        - P5-S3
        - P5-S4
        - P6-S2
        - P7-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      source_review: _compare/relationships-2026-11-16/review-current/Zhang2021
      source_status_sha256: 965ee0a7e8cac2d75b5f626b72ffd3d06d6afd05ee1ffbd9cb1d7ec8a477cd36
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant fixel-wise FD reductions in dual-stream tracts.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the existence of mismatched distributions without specifying
        the measured relationship.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      - 10
      reason: Abstract restatement of fixel-wise correlations between FD and comprehension/naming.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Abstract restatement of tract-wise correlations for comprehension.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 21
      - 22
      - 23
      reason: Abstract restatement of tract-wise correlations for naming.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison (no significant difference).
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about behavioral profiles collection.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Reports reduced FD in aphasia patients.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies locations of FD reductions in dual-stream tracts.
    - source_id: P5-S1-C15
      disposition: represented
      result_indexes:
      - 4
      reason: Sensitivity analysis showing FD reduction confined to dual-stream tracts.
    - source_id: P5-S1-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies greatest FD reductions in IFOF.
    - source_id: P5-S1-C17
      disposition: represented
      result_indexes:
      - 1
      reason: Reports FDC reduction in ventral tracts.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Details FDC reduction distribution.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 2
      - 5
      reason: Reports FC reductions in corticospinal tract and lack of change after
        sensitivity analysis.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Positive correlation between total comprehension and FD in IFOF/tapetum.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Specifies IFOF segment around limen insulae as greatest correlation.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Positive correlation between word-level comprehension and FD in IFOF/corpus
        callosum.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Positive correlation between total naming and FD in IFOF.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Correlations of picture and color naming with FD in IFOF/tapetum.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Positive association between responsive naming and FD in IFOF/tapetum.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Null result for FC or FDC correlations.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overlap of VBA and FBA results.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes metrics observed in centrum semiovale.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about mismatched regions.
    - source_id: P5-S2-C16
      disposition: represented
      result_indexes:
      - 27
      reason: Reports FA reductions in left TPJ.
    - source_id: P5-S2-C17
      disposition: represented
      result_indexes:
      - 27
      reason: Reports axial diffusivity decrease in left TPJ.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 27
      reason: Reports complexity and FD3 increase in left TPJ.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Reduced mean FD in AF, IFOF, and UF.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Specifies IFOF as having highest reduction percentage.
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 14
      reason: Significant FDC decrease in IFOF.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 15
      reason: Null result for tract-wise FC group difference.
    - source_id: P5-S3-C9
      disposition: represented
      result_indexes:
      - 16
      reason: Reductions in mean FA of AF, SLF III, IFOF, and MdLF.
    - source_id: P5-S3-C11
      disposition: represented
      result_indexes:
      - 17
      reason: Positive correlations of IFOF and SLF III FD with total comprehension.
    - source_id: P5-S3-C12
      disposition: represented
      result_indexes:
      - 18
      - 19
      reason: Correlations of IFOF and SLF III FD with word-level and sentence-level
        comprehension.
    - source_id: P5-S3-C13
      disposition: represented
      result_indexes:
      - 20
      reason: Null correlation between UF FD and comprehension.
    - source_id: P5-S3-C14
      disposition: represented
      result_indexes:
      - 21
      - 22
      reason: Positive associations of IFOF and UF FD with total naming and picture
        naming.
    - source_id: P5-S3-C15
      disposition: represented
      result_indexes:
      - 23
      - 24
      reason: Correlations of IFOF FD with responsive and color naming.
    - source_id: P5-S4-C1
      disposition: repeated
      result_indexes:
      - 22
      reason: Repeats UF picture naming correlation.
    - source_id: P5-S4-C2
      disposition: repeated
      result_indexes:
      - 24
      reason: Repeats IFOF color naming correlation.
    - source_id: P5-S4-C3
      disposition: represented
      result_indexes:
      - 25
      reason: Tract-wise FA of IFOF correlated with naming domain.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 26
      reason: Trend-level correlation of IFOF FA with word-level comprehension.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 27
      reason: Null correlation for mean FA of SLF III, AF, and MdLF.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend for comprehension correlations.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend for naming correlations.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure legend describing FD and FA results.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about noting mismatched regions.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 27
      reason: Reports VBA metric alterations with negative FBA changes in TPJ.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 27
      reason: Reports higher density of tertiary fiber population in left TPJ.
    - source_id: P8-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about correlation results.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about FBA providing more focused evidence.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about FA involvement in comprehension.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Restatement that FD correlations with comprehension focused on IFOF.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about precise language-tract mapping.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about disentangling crossing fibers.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of results to surgical evidence.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about FBA accuracy compared to FA.
    - source_id: P9-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about dissociable subdomain correlations.
    - source_id: P9-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement about identifying fiber-specific damage.
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement about intra-axonal volume reduction.
    - source_id: P9-S2-C12
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Conclusion restating mapping of comprehension to IFOF.
    - source_id: P9-S2-C13
      disposition: represented
      result_indexes:
      - 21
      - 22
      reason: Conclusion restating UF-naming association.
    - source_id: P9-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement about dissociative associations.
    unresolved_coverage:
    - source_id: P5-S2-C17
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C5
    - P1-S2-C6
    - P1-S2-C7
    - P1-S2-C8
    - P5-S1-C10
    - P5-S1-C11
    - P5-S1-C16
    - P5-S2-C6
    - P5-S2-C13
    - P5-S2-C14
    - P5-S2-C15
    - P5-S3-C3
    - P5-S3-C6
    - P5-S3-C10
    - P5-S4-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S2-C6
    - P6-S2-C9
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C11
    - P8-S1-C3
    - P8-S1-C10
    - P8-S1-C13
    - P8-S2-C3
    - P8-S2-C4
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C11
    - P9-S1-C12
    - P9-S2-C10
    - P9-S2-C12
    - P9-S2-C13
    - P9-S2-C14
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C9
      recruited_sample:
      - P2-S4-C7
      - P2-S4-C9
      eligibility:
      - P2-S4-C3
      - P2-S4-C4
      imaging_provenance:
      - P3-S1-C2
      imaging_timing:
      - P2-S4-C3
      - P5-S1-C9
      outcome_timing:
      - P2-S4-C12
      outcome_definition:
      - P2-S5-C2
      - P2-S5-C3
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P5-S1-C2
      limitations:
      - P9-S2-C3
      - P9-S2-C4
      - P9-S2-C5
      - P9-S2-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C7
      - P5-S1-C4
      - P5-S1-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C8
      - P5-S1-C10
      - P1-S1-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C5
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
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
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
      source_id: P5-S3-C14
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
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P5-S1-C5
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
      pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
      review_sha256: 8efc3be14543c82d88880d3628246940c8e3eac12b049709f9762e1be5b31371
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
      - P5-S3-C12
      source_result: The source reports a significant positive correlation between
        the mean fiber density (FD) of the left inferior fronto-occipital fasciculus
        (IFOF) and word-level comprehension scores in patients with post-stroke aphasia
        (r = 0.723, p < 0.001). This was determined using Spearman's partial correlation
        analysis, adjusted for nuisance covariates including age, sex, education,
        whole-brain averaged values, lesion volume, and cortical involvement, with
        Bonferroni correction for multiple comparisons.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R018 correctly identifies the correlation
            between left IFOF mean FD and word-level comprehension. The source P5-S3-C12
            explicitly states 'Word-level comprehension subdomain significantly correlated
            with the IFOF (r = 0.723, p < 0.001)'. The method is identified as tract-wise
            correlation using fixel-based analysis (FBA) metrics, which matches the
            source description in P4-S2-C3 and P5-S3-C10.
          source_ids:
          - P5-S3-C12
          - P4-S2-C3
          - P5-S3-C10
        direction:
          answer: fits
          reason: The source explicitly states a 'positive correlation' (P5-S3-C12,
            P5-S3-C10). The proposed core claim 'significantly positively correlated'
            preserves this direction. The result is a detected association, not a
            null or lost effect.
          source_ids:
          - P5-S3-C12
          - P5-S3-C10
        construct:
          answer: fits
          reason: The exposure is 'mean FD of left IFOF' and the outcome is 'word-level
            comprehension'. The source confirms these constructs. The measurement
            is derived from fixel-based analysis (FBA) using CSD, where FD represents
            intra-axonal volume. The patient measurement is classified as template_lesion_overlap
            because the tract-wise metrics are extracted from atlas-based tract masks
            (XTRACT) overlaid on the patient's diffusion data, rather than being a
            direct patient-specific tractography or a simple voxel label. The source
            notes that template-based tractography may have limitations (P9-S2-C4),
            but the construct itself is correctly identified as the mean FD within
            the IFOF mask.
          source_ids:
          - P5-S3-C12
          - P4-S1-C13
          - P3-S2-C10
          - P9-S2-C4
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications for Spearman's partial
            correlation, Bonferroni correction, and adjustment for nuisance covariates
            (age, sex, education, etc.). These are supported by P5-S1-C2, P5-S1-C3,
            and P5-S1-C4. The source confirms these methods were used for the tract-wise
            language correlations.
          source_ids:
          - P5-S1-C2
          - P5-S1-C3
          - P5-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes limitations regarding small sample size,
            heterogeneity of aphasia profiles, and template-based tractography limitations.
            These are supported by P9-S2-C3, P9-S1-C13, and P9-S2-C4. No material
            caveats that would change the interpretation of the specific correlation
            are omitted. The unresolved image-reading disagreements in P2-S3-C10,
            P2-S4-C3, and P5-S1-C8 relate to demographic details or timing definitions,
            not the core statistical result of the IFOF-word comprehension correlation.
          source_ids:
          - P9-S2-C3
          - P9-S1-C13
          - P9-S2-C4
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 29
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.population
      original: patients with post-stroke aphasia in the subacute stage (7 days to
        1 month post-stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1, 7'
    analysis_identity:
      id: R018
      exposure:
        text: mean FD of left IFOF
      outcome:
        text: word-level comprehension
      analysis_label: Tract-wise language correlation (word-level comprehension)
      relation: association
      evidence_ids:
      - P5-S3-C12
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
        pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
        source_review: _compare/relationships-2026-11-16/review-current/Zhang2021
        source_status_sha256: 965ee0a7e8cac2d75b5f626b72ffd3d06d6afd05ee1ffbd9cb1d7ec8a477cd36
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6ebd4dcc7cddecb05fbc80b7506ead60b1ce23d81c09d9b1337ac3234878d841
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C3
          page: 2
          text_layer_sha256: 6ebd4dcc7cddecb05fbc80b7506ead60b1ce23d81c09d9b1337ac3234878d841
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Eligibility criteria included a history \nof initial left-hemisphere\
          \ ischemic stroke during the early subacute stage \n(7 days to 1 month),\
          \ aphasia confirmed by the language scale, age \n18–80 years, right-handedness,\
          \ Chinese as a first language, and educa­\ntion experience ≥6 years."
        anchor_text: "Eligibility criteria included a history \nof initial left-hemisphere\
          \ ischemic stroke during the early subacute stage \n(7 days to 1 month),\
          \ aphasia confirmed by the language scale, age \n18–80 years, right-handedness,\
          \ Chinese as a first language, and educa­\ntion experience ≥6 years."
        excluded_fragments: []
        image_sha256: 4046dd3136ade8f395914ad95f90f67214d0e5d067c6c117a7f3f675b626fff5
      P5-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 96e619987834dcf3b519d8142823d11a54cb5095aea35cecde0b685b7a4f0963
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d9b25822fd7b3791064773ba6eee356ed2bce9881d3c8dc8195e38ae498d8e7c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C9
          page: 5
          text_layer_sha256: d9b25822fd7b3791064773ba6eee356ed2bce9881d3c8dc8195e38ae498d8e7c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The mean time from stroke onset to enrollment was 13.2 (7.3)\
          \ \ndays."
        anchor_text: "The mean time from stroke onset to enrollment was 13.2 (7.3)\
          \ \ndays."
        excluded_fragments: []
        image_sha256: e037b12c2066645e7d62162c897f6241da55784e6792b550c5b1719ce9875654
        transcription: '. The mean time from stroke onset to enrollment was 13.2 (7.3)

          days'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Word-level comprehen­\nsion subdomain significantly correlated with the\
    \ IFOF (r = 0.723, p <\n0.001), while sentence-level comprehension subdomain showed\
    \ a trend- \nlevel positive correlation with the SLF III (r = 0.451, p = 0.021)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
