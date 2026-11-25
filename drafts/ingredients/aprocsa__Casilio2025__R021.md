---
id: aprocsa
name: APROCSA
kind: ingredient
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: aprocsa_dimension_scores
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: aprocsa_dimension_scores
  target_kind: impairment
  claim: The APROCSA measurement system demonstrated high internal consistency in
    acute post-stroke aphasia, with strong alignment between the observed feature
    ratings and the four intended dimension constructs.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 118
    population: adults with acute post-stroke aphasia
    phase: not_reported
    time_post_onset: acute post-stroke period (1–5 days post-onset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Sample was skewed towards participants with less severe speech-language impairments
    due to the requirement for a scorable naturalistic language sample (at least 3
    min of speech or 10 words per minute)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Auditory-perceptual rating of connected speech where
    more than twenty salient features are rated on a five-point scale, then rescaled
    and averaged to create four explanatory dimension scores (Paraphasia, Logopenia,
    Agrammatism, and Motor speech). Internal consistency was evaluated using polyserial
    correlations (26 of 29 associations were r > 0.7) and McDonald''s omega coefficients
    (ranging from 0.87 to 0.92 across the four dimensions). Additional metadata has
    not been transcribed; review the pending-field flags before approval. PDF image
    reading (P2-S3-C2, two-model agreement, human verification pending): Materials
    and methods

    Participants

    The present study included 118 participants with aphasia who were evaluated in
    the acute post-stroke period (1–5 days post-onset) and deemed to have a scorable
    naturalistic language sample, as defined later Original text-layer quotation is
    preserved below.'
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
    - proposed_concept:aprocsa_dimension_scores
  citation: '@Casilio2025'
  source_passages:
  - section: Original source P4-S1-C1
    page: 4
    quote: "\nEvaluation of naturalistic language production\nAuditory-perceptual\
      \ rating of connected speech in aphasia\nNaturalistic language production was\
      \ quantified using auditory- \nperceptual rating of connected speech in aphasia\
      \ (APROCSA),25,58 a \npsychometrically robust and comprehensive measurement\
      \ system \nvalidated on a diverse sample of individuals with chronic aphasia.25\n\
      Based on the gold-standard auditory-perceptual approach for evalu­\nating neuromotor\
      \ speech disorders,61-63 APROCSA involves rating \nmore than twenty salient\
      \ features on a five-point scale, where higher \nscores denote greater impairment."
    supports: method
  - section: Original source P5-S1-C6
    page: 5
    quote: "We then used an established rating scale scoring system82\nto derive four\
      \ dimension scores, where feature ratings for a given di­\nmension are transformed\
      \ to a 0–100 scale (0 = 0, 1 = 25, 2 = 50, 3 = 75, \n4 = 100) and then averaged."
    supports: method
  - section: Original source P6-S3-C5
    page: 6
    quote: 'Characterizing the APROCSA dimensions

      To validate our novel scoring system, we evaluated each dimen­

      sion’s internal consistency, or the degree to which a measure cap­

      tures the construct(s) of interest.'
    supports: claim
  - section: Original source P7-S2-C12
    page: 7
    quote: "Results\nCharacterizing the APROCSA dimensions\nA wide spread of individual\
      \ differences was appreciable for both \nthe dimension scores (Fig. 1E) and\
      \ the feature–dimension associa­\ntions (Fig. 2), again demonstrating that APROCSA\
      \ comprehensively \ncaptures salient features of naturalistic language production\
      \ in \naphasia.25 There also was converging evidence of high internal con­\n\
      sistency (i.e. alignment between observed scores and their in­\n"
    supports: claim
  - section: Original source P7-S3-C1
    page: 7
    quote: "captures salient features of naturalistic language production in \naphasia.25\
      \ There also was converging evidence of high internal con­\nsistency (i.e. alignment\
      \ between observed scores and their in­\ntended constructs) among the features\
      \ that comprised each of \nthe dimension scores."
    supports: claim
  - section: Original source P7-S3-C2
    page: 7
    quote: "The polyserial correlations were strong; 26 \nof 29 possible bivariate\
      \ associations were ˆr > 0.7 with generally \ntight bootstrapped 95% CIs (Fig.\
      \ 2)."
    supports: claim
  - section: Original source P7-S3-C3
    page: 7
    quote: "McDonald’s ωt coefficients \nwere similarly high (Paraphasia: ωt = 0.87;\
      \ Logopenia: ωt = 0.92; \nAgrammatism: ωt = 0.89; Motor speech: ωt = 0.87)."
    supports: claim
  - section: Original source P2-S3-C2
    page: 2
    quote: "Materials and methods\nParticipants\nThe present study included 118 participants\
      \ with aphasia who were \nevaluated in the acute post-stroke period (1–5 days\
      \ post-onset) and \ndeemed to have a scorable naturalistic language sample,\
      \ as defined \nlater."
    supports: sample
  - section: Original source P16-S3-C7
    page: 16
    quote: "First, indi­\nviduals with unscorable naturalistic language samples were\
      \ \nexcluded."
    supports: limitation
  - section: Original source P16-S3-C8
    page: 16
    quote: "This was a necessary constraint; however, it consequent­\nly means that\
      \ our sample was skewed towards participants with \nless severe speech-language\
      \ impairments and with lesions in par­\nticular regions, thus likely influencing\
      \ the brain associations we \nidentified."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Casilio2025
  proposal_id: R021
  review_status_sha256: dcb397e9e63d8825a897f2390fd94a084db2132d66f0e10f1c9fce408f083dfa
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
        A/passages.json: a794f8b46455642792c6a397885409f385dcb719c9d7fedf94ce3a4e3561d755
        A/raw.json: f0776ce1ff5ae612b6d717737fdfe9f0403f55f551da0324df85625ee4aab9d1
        A/source-units.json: 96ccd815635e5bd541ba2425d219aeaceb081dd4802971f472c943701a2ed12e
        A/full-source-units.json: 0d201932b444b721321d9a9487535d7a63f8e6c371820df6ac0b8c91a8b000c3
        A/meta.json: 45b33656839a1ed0c8bbb5d01683b01415d8c160f8bcbaf5a9821b7ee5124ae3
        A/table-images/page-10.png: 35e75e886768582bf676a5eddb9c870419466e2bbf4698f7dee4ce1f32dd675a
        A/table-images/TABLE-1-page-2-1.png: 9e07a3b20c43b5a83705aa4f4ae0864bc59411ff7e2fb6a8c09d947893676845
        A/table-images/page-2.png: 19f896b6d792fd7098229e11b06d379889c30fc736b6b52934fc6aab83721420
        A/table-images/page-4.png: 9d4c0967a845da8cd903fb49db99204837c5e99dfa381c9f8b3a40f31167b7fb
        A/table-images/TABLE-1-page-4-1.png: 5a0f4adad6f183af0b91615864ea050d542aa83c3549c33416626dfbbdafeaa2
        A/table-images/manifest.json: 1f84cd92620635cdb4b44cb53cbcac315a0ca80b10bc5aed0d884f2458f1db9f
        A/table-images/TABLE-2-page-10-1.png: 5c799edd851f7c93c70f5968cbb157a722d17193e1a46ecdabce029cbd1e5499
        A/clauses/window-11/raw.json: 8634ad7feb03a3cd274d0fb3570c1ac12fa0ae36457b006ce4ea1be4ba51de9e
        A/clauses/window-11/prompt.txt: 4f5e7b087fa51977e2e7ebd2679c140977483b262ca5c69a9136970f300c181e
        A/clauses/window-11/meta.json: 5b0cff3ab503c39a21bbbbc6ff685ffe17c0e105d2ecfa12da7a87cd851e334f
        A/clauses/window-10/raw.json: a9a9288c611ee28ee0cd240a131851731c81065d1a8ebb41d577ed62e5d69fe0
        A/clauses/window-10/prompt.txt: b9f28cccf16cb1ec97c8aa92435210aa6e0e39b4cc275188ce214c925ebaee06
        A/clauses/window-10/meta.json: d2c424d256ac7aeecaec51dc47efde07c1391ff73e7d479f76c373f299784f8a
        A/clauses/window-03/raw.json: 80e41c2016dbbcd97ff14f6a2e4887eaad9f2b1172a1dbc08f9b05486ec08fd8
        A/clauses/window-03/prompt.txt: 54af5209d3f49bbc57177ca3981c60b5f5ef948ff0d6c6a5e7ce6eaa6d6fd80a
        A/clauses/window-03/meta.json: 50e0eb64daad1c086b470e17e53e17aa0e3da531b38d4d61561f23cbd319ec7b
        A/clauses/window-04/raw.json: 9125c733ed33ecfa4e7cc175141f70bf4315350c517e2d159e69d6b0793e73c1
        A/clauses/window-04/prompt.txt: f4674bf780b765c3e77106b8d3677d1e912aa031c5ac22f596b574b6948e85fc
        A/clauses/window-04/meta.json: f7d512635593d31cd446329406ee62df797614380daa15f3c0bad007ee21bb7b
        A/clauses/window-05/raw.json: 5428a0ff396938bc85fca36cc4a966719acd9e16570fcf87315c96942765cb5f
        A/clauses/window-05/prompt.txt: 4cc8466707ab6bec238f9f92552e2df1dc660109edfa712dde23fd32b329efeb
        A/clauses/window-05/meta.json: da042921488c5b7fd91f94e4be9406471dd5acd9e3473c8498c56d24d454b546
        A/clauses/window-02/raw.json: b6f093d547cfafced2256b12110a0786682a22b34f8db2d53c4668c4f54106df
        A/clauses/window-02/prompt.txt: 34feb97da3c5ddb77935514171f250d68af28b49e2cb98489a3c7abb6a72629c
        A/clauses/window-02/meta.json: b337e65631c0b21f6260c19be2cbe01cb46f331f26c4c478757932d7d39de581
        A/clauses/window-09/raw.json: 6c5dbdde61b1cde1ab968d6033ea5a0c72095ffc4e681497c6dbea69bfed3617
        A/clauses/window-09/prompt.txt: 798f4828f60331442640f8c733333c1a2a3feef3a42f755333d9a5fa10916aed
        A/clauses/window-09/meta.json: 546dab94752e9a871e386fc584b8a3f88972475fccb1733f7aace05b6b3ab551
        A/clauses/window-07/raw.json: c2cb956f0fca14d45593785793338214b373d6a5bdf4d8dc2643b92d3886303d
        A/clauses/window-07/prompt.txt: 9a9fd997d966a03fe0682539f6c774bde4b89c9d499ed976a064facfd297b322
        A/clauses/window-07/meta.json: 32256372297413e7c01e54cd98e77b002bc8bccbcbaf91b68a03fd5b7565901b
        A/clauses/window-01/raw.json: e1649a2d1e816df63a3bcd333df32fb94a23d0a9df8088297c1b4e63d40e56a5
        A/clauses/window-01/prompt.txt: 762cba294e7367113aaec312f9a11b82312c0fe63b6f881ed7c7c67910dd67b9
        A/clauses/window-01/meta.json: 27ff5ed6c2c34de06bc1cb63ac33e38906a43e0a5c4ac01361dae487920891d2
        A/clauses/window-06/raw.json: dfde5f72588a85d96de76ece162c65c2097d515abd218f302044d1fa514b038e
        A/clauses/window-06/prompt.txt: b9da8f25ee503304bcb7bad54369eac30b2616068fc72682bffe1e6ef2182e8c
        A/clauses/window-06/meta.json: 4fdcd34f333b12227a30493bdd7abce52399499eb761a3d73f5c83cafdf7792c
        A/clauses/window-08/raw.json: f73400f802182d912703871f86fa43ec212bb7a42dc5a373800b38f15939935b
        A/clauses/window-08/prompt.txt: b6645428dfa1ac6dac559c1260d3c84b68d83976c52c6318930edc20b7e28329
        A/clauses/window-08/meta.json: c8a68c7d82c7fce3a08d17a04a753b46606adfd4d51835b1cafc49130959f3d7
        A/tables/TABLE-1-page-4-2/raw.json: 92044aa6cdd42c9f1994e31ff257e4f63ff3ad6570d7e82cb9e14f256ae0ffaf
        A/tables/TABLE-1-page-4-2/prompt.txt: 09321afcac5031354e8e3c56fed8d95909878e6764a1b6e3f2cb58ed7edda1d3
        A/tables/TABLE-1-page-4-2/meta.json: d9a503c0a84bd2593d19ee74736199e76b7da34c1d1793ed8aeb96dd6837af53
        A/tables/TABLE-1-page-2-1/raw.json: da06e0eb6780353b1df1ff6c8434dbf9c6ad22bf30d0f9582fa0641aae42cf34
        A/tables/TABLE-1-page-2-1/prompt.txt: d0339e119d5557ad9de09acfcc9f86c16e0797c8d424871b2ec9bce5cd558b9d
        A/tables/TABLE-1-page-2-1/meta.json: 34de96ef496f906c5fd0de14b586bd7ee45674de2a1384159a6e4e13792ae0ca
        A/tables/TABLE-2-page-10-3/raw.json: 66df4c1427b49c78344d3730fb8163b23c9a4dd31056a358f0e1d41d72afd1aa
        A/tables/TABLE-2-page-10-3/prompt.txt: 89f94fc791046d06acae08303ce6cc10684dcf65f4d6d06fadb397da6ca52392
        A/tables/TABLE-2-page-10-3/meta.json: 68cfc0db0450fff9ac0689f78ee11650870d45ea5b5c965a9e956b6eff02ea0f
        B/passages.json: a794f8b46455642792c6a397885409f385dcb719c9d7fedf94ce3a4e3561d755
        B/raw.json: f6bd0a0e149cb71917f8dd08028fe4222bc709c47880f0b065ca0bab79328f7c
        B/source-units.json: 96ccd815635e5bd541ba2425d219aeaceb081dd4802971f472c943701a2ed12e
        B/full-source-units.json: 0d201932b444b721321d9a9487535d7a63f8e6c371820df6ac0b8c91a8b000c3
        B/meta.json: dcd4e590fbd0d8b8555f3d3162ab3ca11454c82929b1f08e5f460ecd062e9c51
        B/table-images/page-10.png: 35e75e886768582bf676a5eddb9c870419466e2bbf4698f7dee4ce1f32dd675a
        B/table-images/TABLE-1-page-2-1.png: 9e07a3b20c43b5a83705aa4f4ae0864bc59411ff7e2fb6a8c09d947893676845
        B/table-images/page-2.png: 19f896b6d792fd7098229e11b06d379889c30fc736b6b52934fc6aab83721420
        B/table-images/page-4.png: 9d4c0967a845da8cd903fb49db99204837c5e99dfa381c9f8b3a40f31167b7fb
        B/table-images/TABLE-1-page-4-1.png: 5a0f4adad6f183af0b91615864ea050d542aa83c3549c33416626dfbbdafeaa2
        B/table-images/manifest.json: 7b80c8721c0030a1a13ba7b779f47e1545be0b52d6c5c3210c8659a334d6ea5e
        B/table-images/TABLE-2-page-10-1.png: 5c799edd851f7c93c70f5968cbb157a722d17193e1a46ecdabce029cbd1e5499
        B/clauses/window-11/raw.json: 23558fc8622b2c7f7e203bd146e50d4d04376d07e164cfbc3a448a748ad98229
        B/clauses/window-11/prompt.txt: 4f5e7b087fa51977e2e7ebd2679c140977483b262ca5c69a9136970f300c181e
        B/clauses/window-11/meta.json: 85a370defb174654e68712c675e37ee6e1e43bd18776afd6ee5172a60be00866
        B/clauses/window-10/raw.json: 3ce604b7943b14f91318a27e2f062ce180e79baa1ec1207e6c38eea5de31a28c
        B/clauses/window-10/prompt.txt: b9f28cccf16cb1ec97c8aa92435210aa6e0e39b4cc275188ce214c925ebaee06
        B/clauses/window-10/meta.json: 8406dc6eed0fc0e77f49f1f47c6fa961d5ca61d830ae51d227f35754886f5a1e
        B/clauses/window-03/raw.json: 9c788afbe35a44c2c91cdb9dd29a5be7cfd92c8c4dd9816bdcb25a41c8b78de8
        B/clauses/window-03/prompt.txt: 54af5209d3f49bbc57177ca3981c60b5f5ef948ff0d6c6a5e7ce6eaa6d6fd80a
        B/clauses/window-03/meta.json: bcd7e7a393d3f5bfe26259f18f1d96e03455a3056369239bf7af578aaa3bd595
        B/clauses/window-04/raw.json: 5a3bf26beed6d8ae87396662f70cc47d6729340e437cc6c4c4ce546054229e5f
        B/clauses/window-04/prompt.txt: f4674bf780b765c3e77106b8d3677d1e912aa031c5ac22f596b574b6948e85fc
        B/clauses/window-04/meta.json: 6c28c9ff407c66ebae763dd96766296977075503a904d54eadfe4226ed6f0c31
        B/clauses/window-05/raw.json: b8aa32f1e8ab9ef36638148881dcc242fc73da3e4369d863e71058979884b65d
        B/clauses/window-05/prompt.txt: 4cc8466707ab6bec238f9f92552e2df1dc660109edfa712dde23fd32b329efeb
        B/clauses/window-05/meta.json: 4e512d270d9bf4abc6142e11566039fb2915ac63b981b4ab6d7813f73f655565
        B/clauses/window-02/raw.json: ed0d33e85274e15b3515fbbef936d6ac2f215fc729cff099f7bcf6c85d3b9d60
        B/clauses/window-02/prompt.txt: 34feb97da3c5ddb77935514171f250d68af28b49e2cb98489a3c7abb6a72629c
        B/clauses/window-02/meta.json: 839bb5e2a277def7a5eb8889f08eda968ddd7b42b00fa3def0f562889e9995bb
        B/clauses/window-09/raw.json: 1830aaff28b8c0254faf265e6a5e09104a5de1eaf92123361d154881dc875c13
        B/clauses/window-09/prompt.txt: 798f4828f60331442640f8c733333c1a2a3feef3a42f755333d9a5fa10916aed
        B/clauses/window-09/meta.json: eed4a665037cebe27419cc70eeb35259e7a2ba96ede411fd2968bdd9d87f2371
        B/clauses/window-07/raw.json: 2c10eb451d789f1e16ecbe1306c8e2dbc4ba14b0f89dc4ef8fc08cb882cb08f0
        B/clauses/window-07/prompt.txt: 9a9fd997d966a03fe0682539f6c774bde4b89c9d499ed976a064facfd297b322
        B/clauses/window-07/meta.json: 32a007f4e44d9bbd5d48687180ad6ec65d9afbac3065add7aff1876d6f176bbe
        B/clauses/window-01/raw.json: 2a676df3162996ef92fb5773567b466362ece25a3882b4f3e7b692d71086a815
        B/clauses/window-01/prompt.txt: 762cba294e7367113aaec312f9a11b82312c0fe63b6f881ed7c7c67910dd67b9
        B/clauses/window-01/meta.json: b509531258cbbe4ad41c794c420d1de96e12a1273929f0bb14fc1a5c773ab9bd
        B/clauses/window-06/raw.json: 0f97bfde15c3b2539cbf959de565239d3340df4c653e5e3c965ce6aad391d373
        B/clauses/window-06/prompt.txt: b9da8f25ee503304bcb7bad54369eac30b2616068fc72682bffe1e6ef2182e8c
        B/clauses/window-06/meta.json: e2aebb96b0ef869c4f3b47852a8d6b0166d2feffffdf626d020c6caa5a005e6e
        B/clauses/window-08/raw.json: 1f57d371ede15eb9b47d53b8954a5f1723d89a1f0a1104b26f57ba3b22c44ae9
        B/clauses/window-08/prompt.txt: b6645428dfa1ac6dac559c1260d3c84b68d83976c52c6318930edc20b7e28329
        B/clauses/window-08/meta.json: f66ef582bdd4017be0db2fef58b01853631b10844ddfc22ab2735257acfd9246
        B/tables/TABLE-1-page-4-2/raw.json: 1df0fbd5a638d509c53c0b814b288b5bb5de2f8248da7305f1fde57a084c29b6
        B/tables/TABLE-1-page-4-2/prompt.txt: 09321afcac5031354e8e3c56fed8d95909878e6764a1b6e3f2cb58ed7edda1d3
        B/tables/TABLE-1-page-4-2/meta.json: 160950c9bd5e80a8a4d3711706f5dc2b4ce16694813616dc1844e238cd2eaf06
        B/tables/TABLE-1-page-2-1/raw.json: d9869660d7aec73cd07c6478347165c30979c7270782e4fd6f9a00891ecb8717
        B/tables/TABLE-1-page-2-1/prompt.txt: d0339e119d5557ad9de09acfcc9f86c16e0797c8d424871b2ec9bce5cd558b9d
        B/tables/TABLE-1-page-2-1/meta.json: 7b3efb324b9d684745392ed3e77480b074318a8918efbe4c6ac3621efe68ce6a
        B/tables/TABLE-2-page-10-3/raw.json: 467ea04258c8271fb788e9f0c5459ed07ffb059a48226d68d0b7392f7bf662b8
        B/tables/TABLE-2-page-10-3/prompt.txt: 89f94fc791046d06acae08303ce6cc10684dcf65f4d6d06fadb397da6ca52392
        B/tables/TABLE-2-page-10-3/meta.json: fc5a92d7615f166700a4b4437941ab246b97d861b2ecab492be3a40c2ae7c96c
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
      pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
      source_review: _compare/relationships-2026-11-16/review-current/Casilio2025
      source_status_sha256: fae623c1d1149a0af1aaf3f6172088060c67200579700e57255d6a54ba4fc1cb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R021
    exposure:
      text: APROCSA features
    outcome:
      text: APROCSA dimension scores
    analysis_label: Internal consistency analysis
    relation: association
    evidence_ids:
    - P7-S3-C2
    - P7-S3-C3
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
      pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
      source_review: _compare/relationships-2026-11-16/review-current/Casilio2025
      source_status_sha256: fae623c1d1149a0af1aaf3f6172088060c67200579700e57255d6a54ba4fc1cb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C13
      - Accounting without a linked unit P1-S1-C14
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C14
      - Accounting without a linked unit P6-S3-C3
      - Unaccounted source passage P6-S3-C3
      - Result passage disposed without unit P7-S3-C1
      - Result passage disposed without unit P7-S3-C3
      - Result passage disposed without unit P7-S3-C4
      - Result passage disposed without unit P7-S3-C5
      - Result passage disposed without unit P7-S3-C6
      - Result passage disposed without unit P7-S4-C2
      - Result passage disposed without unit P7-S4-C3
      - Result passage disposed without unit P11-S2-C1
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C3
      - Accounting without a linked unit P14-S3-C3
      - Accounting without a linked unit P14-S3-C4
      - Accounting without a linked unit P14-S4-C2
      - Accounting without a linked unit P14-S4-C3
      - Accounting without a linked unit P14-S4-C4
      - Accounting without a linked unit P15-S1-C1
      - Accounting without a linked unit P15-S1-C3
      - Unaccounted source passage P14-S3-C4
      - Unaccounted source passage P15-S1-C3
      - Unaccounted source passage P14-S4-C3
      - Unaccounted source passage P14-S3-C3
      - Unaccounted source passage P14-S4-C2
      - Unaccounted source passage P14-S4-C4
      - Unaccounted source passage P15-S1-C1
      - Result passage disposed without unit P15-S2-C4
      - Result passage disposed without unit P15-S2-C5
      - Result passage disposed without unit P15-S3-C7
      - Result passage disposed without unit P15-S4-C2
      - Result passage disposed without unit P15-S4-C3
      - Result passage disposed without unit P15-S4-C5
      - Accounting without a linked unit P15-S4-C6
      - Accounting without a linked unit P15-S4-C7
      - Unaccounted source passage P15-S4-C6
      - Unaccounted source passage P15-S4-C7
      - Result passage disposed without unit P15-S4-C9
      - Result passage disposed without unit P16-S1-C3
      - Result passage disposed without unit P16-S1-C4
      - Accounting without a linked unit P16-S1-C8
      - Accounting without a linked unit P16-S1-C9
      - Unaccounted source passage P16-S1-C8
      - Unaccounted source passage P16-S1-C9
      - Result passage disposed without unit P16-S3-C3
      - Result passage disposed without unit P17-S1-C2
      unattached_null_or_qualifier_ids:
      - P2-S4-C4
      - P2-S4-C5
      - P11-S2-C3
      - P14-S3-C3
      - P14-S3-C4
      - P14-S4-C4
      - P15-S1-C3
      - P16-S1-C9
      - P16-S3-C9
      suppressed_nonrepresented_units: 16
      default_disposition_count_requires_completeness_check: 207
      unselected_timing_passages:
      - P1-S1-C11
      - P2-S3-C5
      - P16-S3-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S4-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P16-S4-C2
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-1-page-4-2
      - TABLE-2-page-10-3
      unlinked_tables:
      - TABLE-1-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S1
        - P2-S2
        - P3-S1
        - P5-S1
        - P6-S1
        - P6-S3
        - P6-S4
        - P7-S2
        - P7-S3
        - P7-S4
        - P8-S1
        - P9-S1
        - P10-S1
        - P10-S2
        - P11-S1
        - P11-S2
        - P11-S3
        - P11-S4
        - P12-S1
        - P12-S2
        - P13-S1
        - P14-S1
        - P14-S2
        - P14-S3
        - P14-S4
        - P15-S1
        - P15-S2
        - P15-S3
        - P15-S4
        - P16-S1
        - P16-S2
        - P16-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
      source_review: _compare/relationships-2026-11-16/review-current/Casilio2025
      source_status_sha256: fae623c1d1149a0af1aaf3f6172088060c67200579700e57255d6a54ba4fc1cb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P2-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Participant exclusion counts
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Participant exclusion reasons
    - source_id: P5-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Imaging modality counts
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 21
      reason: Reports interrater agreement results
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of agreement reduction
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on individual differences
    - source_id: P7-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on APROCSA capture
    - source_id: P7-S3-C2
      disposition: represented
      result_indexes:
      - 20
      reason: Reports polyserial correlations for internal consistency
    - source_id: P7-S3-C3
      disposition: represented
      result_indexes:
      - 20
      reason: Reports McDonald's omega for internal consistency
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion distribution description
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion overlap peak location
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of ROI and voxel-wise results
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reporting structure description
    - source_id: P7-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General association statement for Paraphasia
    - source_id: P7-S3-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports Temporal ROI effect on Paraphasia
    - source_id: P7-S3-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies the direction of the Paraphasia-Temporal ROI association
    - source_id: P7-S3-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null ROI predictors for Paraphasia
    - source_id: P7-S3-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Reports voxel-wise cluster for Paraphasia
    - source_id: P7-S4-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Provides voxel-wise cluster metrics for Paraphasia
    - source_id: P7-S4-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Describes anatomical extent of Paraphasia cluster
    - source_id: P7-S4-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Describes white matter extension of Paraphasia cluster
    - source_id: P7-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General association statement for Logopenia
    - source_id: P7-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Logopenia ROI effects
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Reports Frontoparietal and Temporal ROI effects on Logopenia
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports variance explained by ROIs for Logopenia
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Qualifies the direction of Logopenia ROI associations
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General association statement for Agrammatism
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports null ROI predictors for Logopenia
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports voxel-wise cluster for Logopenia
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Describes anatomical extent of Logopenia cluster
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General association statement for Agrammatism
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports Frontoparietal ROI effect on Agrammatism
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Qualifies the direction of Agrammatism-Frontoparietal ROI association
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null ROI predictors for Agrammatism
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports voxel-wise cluster for Agrammatism and general ROI effect for
        Motor speech
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Qualifies the direction of Motor speech-Frontoparietal ROI association
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      reason: Reports null ROI predictors for Motor speech, voxel-wise cluster for
        Motor speech, and multivariate ROI results
    - source_id: P11-S2-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Reports unique regions for dimensions in multivariate voxel-wise analysis
    - source_id: P11-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of small overlap areas
    - source_id: P11-S2-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Reports multivariate spatial overlap (all pairs)
    - source_id: P11-S2-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Reports pairwise DSC for specific dimension pairs
    - source_id: P11-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Paraphasia-Logopenia overlap
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Logopenia-Agrammatism overlap
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Agrammatism-Motor speech overlap
    - source_id: P11-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on bias gradients
    - source_id: P11-S2-C9
      disposition: represented
      result_indexes:
      - 16
      reason: Reports bias results for Paraphasia-Logopenia
    - source_id: P11-S2-C10
      disposition: represented
      result_indexes:
      - 16
      reason: Reports bias results for Paraphasia-Logopenia
    - source_id: P11-S3-C2
      disposition: represented
      result_indexes:
      - 17
      reason: Reports bias results for Logopenia-Agrammatism
    - source_id: P11-S3-C3
      disposition: represented
      result_indexes:
      - 17
      reason: Reports bias results for Logopenia-Agrammatism
    - source_id: P11-S3-C4
      disposition: represented
      result_indexes:
      - 18
      reason: Reports bias results for Agrammatism-Motor speech
    - source_id: P11-S3-C5
      disposition: represented
      result_indexes:
      - 18
      reason: Reports bias results for Agrammatism-Motor speech
    - source_id: P11-S3-C6
      disposition: represented
      result_indexes:
      - 18
      reason: Reports bias results for Agrammatism-Motor speech
    - source_id: P12-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Restates Temporal ROI significance for Paraphasia
    - source_id: P14-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Logopenia correlates
    - source_id: P14-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Logopenia correlates
    - source_id: P14-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Restates Frontoparietal and Temporal ROI significance for Logopenia
    - source_id: P14-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Agrammatism correlates
    - source_id: P14-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Agrammatism correlates
    - source_id: P14-S3-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Restates Frontoparietal ROI significance for Agrammatism
    - source_id: P14-S3-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Restates null ROI findings for Agrammatism
    - source_id: P14-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Motor speech correlates
    - source_id: P14-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on Motor speech correlates
    - source_id: P14-S4-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Restates Frontoparietal ROI significance for Motor speech
    - source_id: P15-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Qualifies the Frontoparietal ROI finding for Motor speech
    - source_id: P16-S2-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null role for Other ROI in ROI analyses
    unresolved_coverage:
    - source_id: P7-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P16-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S4-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C13
    - P1-S1-C14
    - P1-S2-C3
    - P1-S2-C4
    - P2-S4-C4
    - P2-S4-C5
    - P5-S3-C10
    - P6-S3-C4
    - P7-S2-C12
    - P7-S3-C1
    - P7-S3-C4
    - P7-S3-C5
    - P7-S3-C6
    - P7-S3-C8
    - P7-S3-C10
    - P7-S4-C4
    - P7-S4-C5
    - P8-S1-C3
    - P9-S1-C1
    - P9-S1-C13
    - P10-S1-C1
    - P10-S1-C3
    - P11-S1-C1
    - P11-S2-C2
    - P11-S2-C5
    - P11-S2-C6
    - P11-S2-C7
    - P11-S2-C8
    - P11-S3-C8
    - P11-S3-C9
    - P11-S4-C4
    - P11-S4-C5
    - P13-S1-C9
    - P14-S1-C1
    - P14-S1-C2
    - P14-S1-C3
    - P14-S3-C1
    - P14-S3-C2
    - P14-S3-C3
    - P14-S3-C4
    - P14-S4-C2
    - P14-S4-C3
    - P14-S4-C4
    - P15-S1-C1
    - P15-S1-C3
    - P15-S2-C4
    - P15-S2-C5
    - P15-S2-C6
    - P15-S2-C7
    - P15-S3-C2
    - P15-S3-C3
    - P15-S3-C6
    - P15-S3-C7
    - P15-S4-C2
    - P15-S4-C3
    - P15-S4-C5
    - P15-S4-C6
    - P15-S4-C7
    - P15-S4-C9
    - P15-S4-C10
    - P16-S1-C3
    - P16-S1-C4
    - P16-S1-C8
    - P16-S1-C9
    - P16-S1-C10
    - P16-S2-C2
    - P16-S2-C3
    - P16-S2-C5
    - P16-S3-C3
    - P16-S3-C9
    - P17-S1-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-1-page-4-2
    - TABLE-2-page-10-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C11
      - P2-S3-C2
      - P2-S4-C3
      recruited_sample:
      - P2-S3-C8
      - P2-S3-C9
      - P2-S4-C3
      eligibility:
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C9
      - P2-S4-C1
      - P2-S4-C4
      - P2-S4-C5
      imaging_provenance:
      - P5-S3-C9
      imaging_timing:
      - P5-S3-C9
      outcome_timing:
      - P2-S3-C2
      outcome_definition:
      - P1-S1-C10
      - P4-S1-C3
      - P5-S1-C6
      validation:
      - P4-S1-C1
      - P6-S3-C5
      analysis_restrictions:
      - P6-S4-C4
      - P6-S4-C7
      - P7-S1-C2
      - P7-S1-C10
      - P11-S1-C1
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S2-C7
      - P6-S3-C8
      - P6-S3-C11
      limitations:
      - P16-S3-C7
      - P16-S3-C8
      - P16-S3-C9
      - P16-S3-C10
      - P16-S4-C1
      - P16-S4-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P7-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S3-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S4-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C4
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
      pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
      review_sha256: dcb397e9e63d8825a897f2390fd94a084db2132d66f0e10f1c9fce408f083dfa
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
      - P7-S3-C2
      - P7-S3-C3
      source_result: The study reported high internal consistency for the APROCSA
        dimension scores in acute post-stroke aphasia, evidenced by strong polyserial
        correlations (26 of 29 associations > 0.7) and high McDonald's omega coefficients
        (0.87–0.92).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the internal consistency validation of
            the APROCSA dimensions, which matches the source description of evaluating
            feature-dimension associations and reliability coefficients.
          source_ids:
          - P6-S3-C5
          - P6-S3-C6
          - P7-S3-C2
          - P7-S3-C3
        direction:
          answer: fits
          reason: The source explicitly states that internal consistency was high
            and correlations were strong, which aligns with the draft's claim of 'high
            internal consistency' and 'strong alignment'.
          source_ids:
          - P7-S3-C1
          - P7-S3-C2
          - P7-S3-C3
        construct:
          answer: fits
          reason: The exposure (APROCSA features) and outcome (dimension scores) are
            correctly identified as the components of the internal consistency analysis.
            The patient measurement is non-imaging (behavioral rating), which is correct
            for this specific analysis, distinct from the lesion mapping analyses.
          source_ids:
          - P4-S1-C1
          - P5-S1-C6
          - P6-S3-C6
        qualifications:
          answer: fits
          reason: The draft correctly includes the specific metrics (polyserial correlations
            and McDonald's omega) and the population (acute post-stroke) as qualifications.
            The limitation regarding sample skew is also correctly included.
          source_ids:
          - P7-S3-C2
          - P7-S3-C3
          - P16-S3-C7
          - P16-S3-C8
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft acknowledges the sample
            limitation which is the primary caveat for the generalizability of the
            internal consistency findings in this specific acute population.
          source_ids:
          - P16-S3-C7
          - P16-S3-C8
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R021
      exposure:
        text: APROCSA features
      outcome:
        text: APROCSA dimension scores
      analysis_label: Internal consistency analysis
      relation: association
      evidence_ids:
      - P7-S3-C2
      - P7-S3-C3
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
        pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
        source_review: _compare/relationships-2026-11-16/review-current/Casilio2025
        source_status_sha256: fae623c1d1149a0af1aaf3f6172088060c67200579700e57255d6a54ba4fc1cb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d1f08a3e63916e6392d3164e1fdefe85014b7d43bf35cd67d62a42b60869afa7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: bf188cead430cf397020ba4bb9e8b7ce33aa3280b2f1b7fb1eda00ae727bc4d4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C2
          page: 2
          text_layer_sha256: bf188cead430cf397020ba4bb9e8b7ce33aa3280b2f1b7fb1eda00ae727bc4d4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Materials and methods\nParticipants\nThe present study included\
          \ 118 participants with aphasia who were \nevaluated in the acute post-stroke\
          \ period (1–5 days post-onset) and \ndeemed to have a scorable naturalistic\
          \ language sample, as defined \nlater."
        anchor_text: "Materials and methods\nParticipants\nThe present study included\
          \ 118 participants with aphasia who were \nevaluated in the acute post-stroke\
          \ period (1–5 days post-onset) and \ndeemed to have a scorable naturalistic\
          \ language sample, as defined \nlater."
        excluded_fragments: []
        image_sha256: cf5f694cc7b6a87d8370733e66d05419538961881fef35a0ef496d59a785e21f
        transcription: 'Materials and methods

          Participants

          The present study included 118 participants with aphasia who were evaluated
          in the acute post-stroke period (1–5 days post-onset) and deemed to have
          a scorable naturalistic language sample, as defined later'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "\nEvaluation of naturalistic language production\nAuditory-perceptual rating\
    \ of connected speech in aphasia\nNaturalistic language production was quantified\
    \ using auditory- \nperceptual rating of connected speech in aphasia (APROCSA),25,58\
    \ a \npsychometrically robust and comprehensive measurement system \nvalidated\
    \ on a diverse sample of individuals with chronic aphasia.25\nBased on the gold-standard\
    \ auditory-perceptual approach for evalu­\nating neuromotor speech disorders,61-63\
    \ APROCSA involves rating \nmore than twenty salient features on a five-point\
    \ scale, where higher \nscores denote greater impairment."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
