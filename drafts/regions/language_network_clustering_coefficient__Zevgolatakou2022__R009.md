---
id: language_network_clustering_coefficient
name: language network average clustering coefficient
kind: network
findings:
- id: f1
  target: phonology_and_semantics_deficits
  target_kind: impairment
  claim: Language network average clustering coefficient was a significant predictor
    of Phonology and Semantics deficit scores after controlling for overall lesion
    volume.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 58
    population: native English speakers, right-handed, with aphasia following left
      hemisphere stroke
    phase: not_reported
    time_post_onset: mostly chronic stage (at least 3 months post-onset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Exploratory analysis with a relatively large number of comparisons
  - Connectivity disruption was estimated using a population-averaged atlas rather
    than patient-specific diffusion data
  - Sample primarily consisted of mild-to-moderate aphasia severity (median WAB AQ
    = 81.0)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Average clustering coefficient of a left hemisphere
    language sub-network (comprising middle frontal gyrus, IFG, precentral gyrus,
    postcentral gyrus, insula, temporal pole, inferior/middle/superior temporal gyrus,
    SMG, and angular gyrus), estimated by overlaying patient lesion maps on a population-averaged
    HCP-842 tractography atlas to count preserved streamlines. Analysis controlled
    for overall lesion volume; The relationship was tested using multiple regression
    with robust standard error estimation. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P5-S1-C5, two-model
    agreement, human verification pending): . The analytic sample contained behavioural
    data from 69 participants and imaging data were available for 58 of these participants
    Original text-layer quotation is preserved below. PDF image reading (P5-S1-C6,
    two-model agreement, human verification pending): All but five participants were
    examined at the chronic stage

    of aphasia (at least 3 months post-onset), but the exclusion of

    these five participants did not change the results so the more

    inclusive analyses are reported here Original text-layer quotation is preserved
    below. PDF image reading (P13-S1-C4, two-model agreement, human verification pending):
    . This resulted in a sample size (N = 58) that

    was moderate relative to other LSM studies, with most of

    the participants in the mild-to-moderate range of aphasia se-

    verity (median WAB AQ = 81.0, IQR = 71.3–91.0), though it

    did include some participants with more severe aphasia Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:phonology_and_semantics_deficits
  citation: '@Zevgolatakou2022'
  source_passages:
  - section: Original source P11-S1-C5
    page: 11
    quote: "Language network average clustering coefficient was also a sig­\nnificant\
      \ predictor of Phonology [Estimate= −8.100, 95% CI= \n(−15.662, −0.538), P=0.036]\
      \ and Semantics [Estimate= \n9.036, 95% CI= (1.249, 16.823), P=0.023], and a\
      \ marginally \nsignificant predictor of Lexical syntax [Estimate=8.777, 95%\
      \ \nCI= (−0.501, 18.055), P=0.064]."
    supports: claim
  - section: Original source P7-S3-C2
    page: 7
    quote: "Structural connectivity matrices and corresponding graph \ntheoretical\
      \ measures were also generated for a language sub- \nnetwork comprised of the\
      \ following left hemisphere regions \nwithin the AAL3 atlas and based on prior\
      \ work using similar \nmethods32, 72-76 middle frontal gyrus, inferior frontal\
      \ gyrus \n(IFG) (pars opercularis, pars triangularis, and pars orbitalis), \n\
      precentral gyrus, postcentral gyrus, insula, superior portion \nof the temporal\
      \ pole, middle portion of the temporal pole, in­\nferior temporal gyrus, middle\
      \ temporal gyrus, superior tem­\nporal gyrus, supramarginal gyrus (SMG) and\
      \ angular gyrus."
    supports: method
  - section: Original source P7-S1-C9
    page: 7
    quote: "The toolkit calculates connectivity disruption \nby overlaying the lesion\
      \ files on an atlas of intact connectiv­\nity.69 This whole-brain connectivity\
      \ atlas was derived using \ndeterministic tractography on the population-averaged\
      \ \nHCP-842 data set with multiple turning angle thresholds to \nobtain 500\
      \ 000 population-level streamline trajectories (i.e. \nestimated white matter\
      \ fibre trajectories based on directional \ndiffusion information), which were\
      \ manually vetted and as­\nsigned to known white matter fibre tracts by a team\
      \ of \n"
    supports: method
  - section: Original source P10-S1-C7
    page: 10
    quote: "Therefore, the results reported \nhere are based on multiple regression\
      \ analyses that control \nfor lesion volume."
    supports: confounders
  - section: Original source P5-S1-C5
    page: 5
    quote: "The analytic sample contained behavioural data \nfrom 69 participants\
      \ and imaging data were available for \n58 of these participants."
    supports: sample
  - section: Original source P5-S1-C6
    page: 5
    quote: "All but five participants were examined at the chronic stage \nof aphasia\
      \ (at least 3 months post-onset), but the exclusion of \nthese five participants\
      \ did not change the results so the more \ninclusive analyses are reported here."
    supports: sample
  - section: Original source P13-S1-C4
    page: 13
    quote: "This resulted in a sample size (N = 58) that \nwas moderate relative to\
      \ other LSM studies, with most of \nthe participants in the mild-to-moderate\
      \ range of aphasia se­\nverity (median WAB AQ = 81.0, IQR = 71.3–91.0), though\
      \ it \ndid include some participants with more severe aphasia."
    supports: limitation
  - section: Original source P13-S2-C8
    page: 13
    quote: "Another key limitation is that diffusion data were not \navailable for\
      \ the participants, so connectivity disruption \nwas estimated by overlaying\
      \ each participant’s lesion map \non a tractography atlas derived from the HCP-842\
      \ data."
    supports: limitation
  - section: Original source P11-S1-C6
    page: 11
    quote: "These were exploratory analyses, not driven by strong hy­\npotheses, and\
      \ comprising a relatively large number of com­\nparisons, so these connectome\
      \ disruption results should be \ninterpreted with caution."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Zevgolatakou2022
  proposal_id: R009
  review_status_sha256: 3a0527a74768b3e32514e7874356784afdb7b88a0dfa14ba5c5a7f3acf751e41
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
        A/passages.json: 34d1dbcaeda65e008b224b62091549d9c4a2f6b214b305da8c22b59436fbf156
        A/raw.json: c51d250d6a4f6b3328a8b0f21393e7b04127659db8fe3fc21ed20708ad5c8066
        A/source-units.json: a9669d4e7b167d0009af759cfefac83ca40f20edde410efca5a69578ba402f65
        A/full-source-units.json: 823eb7e9a39a76b71f0b3e20ba69453a42f0947aaaf596df6809faf2078a5d36
        A/meta.json: 00c5108ab260bf1ac9abbe8f16190be383b3a260a5ed434f6f121f0ba24e7dff
        A/table-images/page-10.png: b7bb32726e00b183e43b093c53b30b37e3194f6fb8e12019d6ffbce56bada8a0
        A/table-images/page-11.png: 3270c49ce9b20ca34188ad83627ff878bc7668dc280aafa2cb0ed09ebe4a9184
        A/table-images/TABLE-3-page-11-1.png: 97f60bd48405a64f8f8d5d5774ae575504eb38e7b80bfb9a4f660736671911ef
        A/table-images/TABLE-1-page-6-1.png: 75f23d56c57bc4edefcbae926d143e9de9453a6f205aa4804545cb96240d6308
        A/table-images/page-6.png: 302378ce9a559f836c16a48e7307103d540e59069728e7db492102801a66ce15
        A/table-images/manifest.json: f125aaf256d185aa2036aaf676e3a06d437655fe2bf8b9171a191c3a7e4c0a36
        A/table-images/TABLE-2-page-10-1.png: 4f1f5b277e99208fdc02524727d29cad126520fa1a8c34d74a7f0a53071af856
        A/clauses/window-10/raw.json: bba5993c523865ea25681869775857de76c88dd03f87d0d06ce4c19ce2eec961
        A/clauses/window-10/prompt.txt: e3adfc52a3a23bccfcc1c2bc1824402f705120ccdcf0e31b1901031996ddc16c
        A/clauses/window-10/meta.json: a5d5981addc7908c578d97cdda25821a050366eabc5725cf740eccb871dbfc51
        A/clauses/window-03/raw.json: 0ba365b9d07ae135789898f5eec7c1fb95cbe61a19e156444c94ba0ff8c41712
        A/clauses/window-03/prompt.txt: 749fa2ef26a83745caf276711857658ba340b55b07a790dd24e42d0c82a9f6a4
        A/clauses/window-03/meta.json: 76e711b7650adbb4c62d94fdf4df37f420af7645d9a5c017c2d0f7f1b470b692
        A/clauses/window-04/raw.json: e70cf5a469322876659f73c2fdfecd3e191f5b70a498ab5b5398bbff2fe5f188
        A/clauses/window-04/prompt.txt: e7a6f9d106b410a52b0f0d33687983fbfc0093f60384af4f8c60b1f51dab7ecd
        A/clauses/window-04/meta.json: 74dd15612ff9cda303a36bdba59fd891e457bd086e7e710efd606ab406ba88d9
        A/clauses/window-05/raw.json: 6ea24a6f2ff6cf781d2509d8a111cd114f887fd8316817e1ba32a3e2259dfe6c
        A/clauses/window-05/prompt.txt: e00672f7b83ed5fe5447e7b9911d5187072780bc22e03ea019e00c1b5772f764
        A/clauses/window-05/meta.json: 2c44d46f9e92bbcfe14a3a971143ff8343abe0c10a5125249ebfbdaa29d10e5f
        A/clauses/window-02/raw.json: eef894e88b35b1115c500cdec62bcbe13e69f6feb9b29a609eecf4668de45bec
        A/clauses/window-02/prompt.txt: 4a0367a57d1892ec593ec5a0a8f54bab665b5f801175ef26e15fabb7822cc1d4
        A/clauses/window-02/meta.json: 42877b32a97bc70dcb7ef93eb829436b8cfea5c544f9f4238eceb07c589e7a1c
        A/clauses/window-09/raw.json: 24d70e4ebde8e030469efa9c4257d70fbb26099da8ac575b4d04a413b3a7b99e
        A/clauses/window-09/prompt.txt: a0468af0df7a62ec130cebcb6d155e5a243761132b25b1460fa2bfa92fc1dea2
        A/clauses/window-09/meta.json: d29e871c4f8d23014c8d5015283a5d6fd96be0cc5a1e81b2697cd037bbf9f4cb
        A/clauses/window-07/raw.json: e23af9929e9fcf7cbfe98d1055131b68ccced42d9e5bbb5f8e762aa420f9b6e4
        A/clauses/window-07/prompt.txt: d91376b842882c4bc75bb9c6e51664ed23e8be441fb65df6e6446860b1aa70b7
        A/clauses/window-07/meta.json: 047453db20a31216a717d87d5da8f7a744ca58458cc3762b279c800e8a0a4b5c
        A/clauses/window-01/raw.json: 0e0f123e622e79d2cdfaf00b8d7b32c9fc76572244c1ec5a69f4df88a1e66276
        A/clauses/window-01/prompt.txt: 44fc364321d0f264e024cf9a4465035e3d73a1c73fff8f675e097c55a164b1ea
        A/clauses/window-01/meta.json: 0527bd74c0e3c1210e5e7c7d6b005bed26e859224c601608edf4bcdfe23d0397
        A/clauses/window-06/raw.json: c077b0a5f567536e358ef2bbb825d4a218362c14a2fae86f06760aaad08861dd
        A/clauses/window-06/prompt.txt: 8023209306c9272f3f96271378ea184b6a3663781b1460cc7a5a2ed8e78f4292
        A/clauses/window-06/meta.json: 7241cc21464ad7b53c49b6380f675325c0df283296f1ef95605009aadb0d9542
        A/clauses/window-08/raw.json: 7795ba540308cd737a28e1dcc1eb88c6d05eeb4be2fae0355fa2433405fb68c3
        A/clauses/window-08/prompt.txt: 3166e0a7750f9a39076aaf985966f308fe1b1249da80ad8ac286eb21851aea27
        A/clauses/window-08/meta.json: 6613c5d8bd95be911975390a170f5fa0c488244f79cec68926f58726fb0f462a
        A/tables/TABLE-1-page-6-1/raw.json: 09f27a084c6ad39cc93c8c067e477a430ed7c7d0ad0d7374cac3ae7f1f51ea44
        A/tables/TABLE-1-page-6-1/prompt.txt: 79e811a1a808c17dfa475a2ac0a0e01291d76a6a59c631dc85294191c10cb111
        A/tables/TABLE-1-page-6-1/meta.json: c6db266ebec652ccf61c7bc6b568d26734831649b175f56dabce563973d0cba8
        A/tables/TABLE-3-page-11-3/raw.json: 6535b7f810489858bdad5722b2c41015626a6d9f7c5fe5cccf58285e7a430543
        A/tables/TABLE-3-page-11-3/prompt.txt: d72d11960711558dddfc1695d1126b9a7f18f0dedf41466bb2f1767236f33f61
        A/tables/TABLE-3-page-11-3/meta.json: b0c17debc2c12487c89cba5577c749c3ea305097e3658164c0c510edee298909
        A/tables/TABLE-2-page-10-2/raw.json: fd84df3b4e5e54f674a61960be9dc2d1d7e8728085f171059417666ab2e1184a
        A/tables/TABLE-2-page-10-2/prompt.txt: 05dc3326fa3abf4903b2e1e1e3d631416ae2e90af14bbbc4c3512d4146079fb9
        A/tables/TABLE-2-page-10-2/meta.json: 7d419d1a6d7a9355af06d33a9ce0ec16f3e9e6965fff7a22c27ec8c3e6f92b86
        B/passages.json: 34d1dbcaeda65e008b224b62091549d9c4a2f6b214b305da8c22b59436fbf156
        B/raw.json: d0d29ec37bb7b77e1e6edd046f768cb18f324048d668132ff8c95fb166d50277
        B/source-units.json: a9669d4e7b167d0009af759cfefac83ca40f20edde410efca5a69578ba402f65
        B/full-source-units.json: 823eb7e9a39a76b71f0b3e20ba69453a42f0947aaaf596df6809faf2078a5d36
        B/meta.json: 76476ba7053174f7c4eb3c288dc558eb22b59b236de25f6754028e7e2614d683
        B/table-images/page-10.png: b7bb32726e00b183e43b093c53b30b37e3194f6fb8e12019d6ffbce56bada8a0
        B/table-images/page-11.png: 3270c49ce9b20ca34188ad83627ff878bc7668dc280aafa2cb0ed09ebe4a9184
        B/table-images/TABLE-3-page-11-1.png: 97f60bd48405a64f8f8d5d5774ae575504eb38e7b80bfb9a4f660736671911ef
        B/table-images/TABLE-1-page-6-1.png: 75f23d56c57bc4edefcbae926d143e9de9453a6f205aa4804545cb96240d6308
        B/table-images/page-6.png: 302378ce9a559f836c16a48e7307103d540e59069728e7db492102801a66ce15
        B/table-images/manifest.json: 1adf99ceec849ce32352337b3af6b6a55ee2599b7e3bf55cd9acaa0b1af9a643
        B/table-images/TABLE-2-page-10-1.png: 4f1f5b277e99208fdc02524727d29cad126520fa1a8c34d74a7f0a53071af856
        B/clauses/window-10/raw.json: b091b8922f01d2818955e236493520bb0e950648d2d48c27fdf41113c773f54f
        B/clauses/window-10/prompt.txt: e3adfc52a3a23bccfcc1c2bc1824402f705120ccdcf0e31b1901031996ddc16c
        B/clauses/window-10/meta.json: b318801a39882745b7d20b0c35361f97d543159222f491858c7238a5d31bb8be
        B/clauses/window-03/raw.json: a15f45104ee8c4fc571fc18d6081e9c88a31e4f2e86286ba657aa634280a2c5c
        B/clauses/window-03/prompt.txt: 749fa2ef26a83745caf276711857658ba340b55b07a790dd24e42d0c82a9f6a4
        B/clauses/window-03/meta.json: c93c7ea70e4c94c766bb0e761eae4ea4056751bfe4095fa6bcfa0657d74a1f1f
        B/clauses/window-04/raw.json: 5ff2469176cfe9cece548225fefeb4fadf3ff2648c256870b29bc6631801993a
        B/clauses/window-04/prompt.txt: e7a6f9d106b410a52b0f0d33687983fbfc0093f60384af4f8c60b1f51dab7ecd
        B/clauses/window-04/meta.json: 871ac2c8beaa615390287913ce08e661265b6c416129c372a56e2f3fe7924d4f
        B/clauses/window-05/raw.json: adf3143bf90417327af2ace3da3f4164e7b4c12746eb19b0f8414412b1ff39eb
        B/clauses/window-05/prompt.txt: e00672f7b83ed5fe5447e7b9911d5187072780bc22e03ea019e00c1b5772f764
        B/clauses/window-05/meta.json: bbbf46ed7fb29235d88215f322c8b332ca836dc36517c121b3fc6ba67b0b1bfe
        B/clauses/window-02/raw.json: 4f7b79702f2a095940871fdb9ec21233d62383fc39630372d33097e874249a18
        B/clauses/window-02/prompt.txt: 4a0367a57d1892ec593ec5a0a8f54bab665b5f801175ef26e15fabb7822cc1d4
        B/clauses/window-02/meta.json: bc43a5565ea430502322c0b036ddff9d1dacb91a277116b370800adee79e871a
        B/clauses/window-09/raw.json: 35e47f29b9be1dd65a1174287195d398b5cad6e1228ae3e262727a053c69cb11
        B/clauses/window-09/prompt.txt: a0468af0df7a62ec130cebcb6d155e5a243761132b25b1460fa2bfa92fc1dea2
        B/clauses/window-09/meta.json: 1a00ce59030a9264383402139f295c9cf04801a521d355331b3f3042fe867732
        B/clauses/window-07/raw.json: 6ea15b3f3c3e2d25ef232e57166914e0735b18362415c20886c724def63961e0
        B/clauses/window-07/prompt.txt: d91376b842882c4bc75bb9c6e51664ed23e8be441fb65df6e6446860b1aa70b7
        B/clauses/window-07/meta.json: 4f89c75057bddad9161d36198b87f048144667f209b11ada1390e44000e8c3de
        B/clauses/window-01/raw.json: 699207a3802141e3d9ff0868d1cc7c5e3436249f7e01180f955f72db30d31f8f
        B/clauses/window-01/prompt.txt: 44fc364321d0f264e024cf9a4465035e3d73a1c73fff8f675e097c55a164b1ea
        B/clauses/window-01/meta.json: bc91ec0ed0d5c19adbff7280b2f6a4fb1c4d73a3b1d8f33fc34cb3fd203f2cfe
        B/clauses/window-06/raw.json: 4d21d7126d6aa1e507977a899a8ddff4f8aaf29bba9981f1ae2b39721ad8acab
        B/clauses/window-06/prompt.txt: 8023209306c9272f3f96271378ea184b6a3663781b1460cc7a5a2ed8e78f4292
        B/clauses/window-06/meta.json: c9c8c5bd5151a6ecbb85c2ccdc099569259cd2c57c323f2626b955ad523f00ee
        B/clauses/window-08/raw.json: 42f32bc8c5538f05b53f9582b92513f25449ae3c535b6464744517e88cb1e08b
        B/clauses/window-08/prompt.txt: 3166e0a7750f9a39076aaf985966f308fe1b1249da80ad8ac286eb21851aea27
        B/clauses/window-08/meta.json: 8a75f81190da14a62a6e7a477c3bb6484f22dfdfb0c84b66703ede502637ba24
        B/tables/TABLE-1-page-6-1/raw.json: b11b7ef8eda8af5bc68e4588da11d793cefa761af81fa26be55e1d7149041ebf
        B/tables/TABLE-1-page-6-1/prompt.txt: 79e811a1a808c17dfa475a2ac0a0e01291d76a6a59c631dc85294191c10cb111
        B/tables/TABLE-1-page-6-1/meta.json: 04a8182cc5e0635c3ec6d30aed6fe61c053c1b06ea33bef6457a928a4a54bdbe
        B/tables/TABLE-3-page-11-3/raw.json: 81428c877ff514cabc4c4c42b5316dba16331ad09d0700dca7d924f2f16c7a51
        B/tables/TABLE-3-page-11-3/prompt.txt: d72d11960711558dddfc1695d1126b9a7f18f0dedf41466bb2f1767236f33f61
        B/tables/TABLE-3-page-11-3/meta.json: 3f306a0f460ea1825c3c7cad5eece69d2982ce664cb9188df01c5e6468bace33
        B/tables/TABLE-2-page-10-2/raw.json: 4950529ca8266c449c333f5cd88a9f9cdfc08434d0487ae0b4fcbef817512a9d
        B/tables/TABLE-2-page-10-2/prompt.txt: 05dc3326fa3abf4903b2e1e1e3d631416ae2e90af14bbbc4c3512d4146079fb9
        B/tables/TABLE-2-page-10-2/meta.json: 24ab05f37101f42fd42379563b4d25424749567d4e2c0377fdf0671fa899bc17
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
      pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
      source_review: _compare/relationships-2026-11-16/review-current/Zevgolatakou2022
      source_status_sha256: ba5845a79a946e9d1a0a12fe0a7528fd0cc751bedded4fd6ab908e420d726b86
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: language network average clustering coefficient
    outcome:
      text: Phonology and Semantics factors
    analysis_label: Multiple Regression (Language Network)
    relation: association
    evidence_ids:
    - P1-S2-C4
    - P11-S1-C5
    - P11-S3-C3
    - P12-S4-C4
    qualifier_ids:
    - P1-S2-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
      source_review: _compare/relationships-2026-11-16/review-current/Zevgolatakou2022
      source_status_sha256: ba5845a79a946e9d1a0a12fe0a7528fd0cc751bedded4fd6ab908e420d726b86
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C9
      - Accounting without a linked unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Unaccounted source passage P5-S1-C2
      - Unaccounted source passage P5-S1-C3
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P9-S1-C11
      - Result passage disposed without unit P9-S3-C11
      - Result passage disposed without unit P11-S2-C3
      - Accounting without a linked unit P11-S2-C5
      - Accounting without a linked unit P11-S2-C6
      - Accounting without a linked unit P11-S2-C7
      - Result passage disposed without unit P12-S1-C3
      - Result passage disposed without unit P12-S1-C5
      - Unaccounted source passage P11-S2-C6
      - Unaccounted source passage P11-S2-C5
      - Unaccounted source passage P11-S2-C7
      - Result passage disposed without unit P12-S2-C3
      - Result passage disposed without unit P12-S2-C4
      - Result passage disposed without unit P12-S2-C6
      - Result passage disposed without unit P12-S3-C2
      - Result passage disposed without unit P12-S3-C4
      - Accounting without a linked unit P12-S3-C7
      - Result passage disposed without unit P12-S3-C9
      - Result passage disposed without unit P12-S4-C1
      - Accounting without a linked unit P12-S4-C2
      - Accounting without a linked unit P12-S4-C4
      - Unaccounted source passage P12-S4-C2
      - Unaccounted source passage P12-S3-C7
      - Unaccounted source passage P12-S4-C4
      - Result passage disposed without unit P13-S1-C9
      - Accounting without a linked unit P13-S2-C5
      - Accounting without a linked unit P13-S2-C6
      - Accounting without a linked unit P13-S2-C9
      - Unaccounted source passage P13-S2-C5
      - Unaccounted source passage P13-S2-C9
      - Unaccounted source passage P13-S2-C6
      - Result passage disposed without unit P13-S3-C1
      - Result passage disposed without unit P13-S3-C2
      - Result passage disposed without unit P13-S3-C3
      unattached_null_or_qualifier_ids:
      - P1-S2-C3
      - P1-S2-C4
      - P5-S1-C4
      - P12-S3-C2
      - P13-S2-C9
      - P13-S3-C3
      suppressed_nonrepresented_units: 17
      default_disposition_count_requires_completeness_check: 206
      unselected_timing_passages:
      - P4-S3-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P9-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P1-S1-C3
        - P4-S1-C8
        - P5-S3-C2
        - P5-S3-C6
        - P5-S3-C8
        - P5-S3-C10
        - P5-S3-C12
        - P6-S1-C6
        - P6-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P13-S1-C3
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        - P13-S2-C7
        - P13-S2-C8
        - P13-S2-C9
        - P13-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P4-S4-C1
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-10-2
      - TABLE-3-page-11-3
      unlinked_tables:
      - TABLE-1-page-6-1
      - TABLE-2-page-10-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S3
        - P8-S1
        - P8-S2
        - P9-S1
        - P9-S2
        - P9-S3
        - P9-S4
        - P10-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
      source_review: _compare/relationships-2026-11-16/review-current/Zevgolatakou2022
      source_status_sha256: ba5845a79a946e9d1a0a12fe0a7528fd0cc751bedded4fd6ab908e420d726b86
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Describes the four-factor PCA solution.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Associates complexity deficits with temporo-parietal region.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Associates lexical syntax factor with fronto-parietal regions.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Null finding for tract-based connectivity disruption.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Associates network efficiency and clustering coefficient with deficit
        scores.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA stability analysis.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes outlier identification.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes outlier exclusion.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes coder agreement.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares PCA to exploratory factor analysis.
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions supplementary figure for correlations.
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports KMO factorability.
    - source_id: P9-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes factor extraction criteria.
    - source_id: P9-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figure for factor loadings.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports variance accounted for by PCA factors.
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes bifactor rotation design.
    - source_id: P9-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the general factor.
    - source_id: P9-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the general factor.
    - source_id: P9-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the lexical syntax factor.
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the Phonology factor.
    - source_id: P9-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the Semantics factor.
    - source_id: P9-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes loadings of the Semantics factor.
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses individual measure observations.
    - source_id: P9-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage.
    - source_id: P9-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figure/table for LSM results.
    - source_id: P9-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage.
    - source_id: P9-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage.
    - source_id: P9-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figure/table for LSM results.
    - source_id: P9-S4-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Associates complexity deficits with temporo-parietal region.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies regions for complexity deficit association.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares result to previous severity patterns.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies regions for lexical syntax factor association.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Null result for Phonology and Semantics factors in LSM.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares behavioral scores to lesion volume.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces regression analysis.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports lesion volume effects on complexity, lexical syntax, semantics,
        and phonology.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Null result for tract associations.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Confirms lesion volume effects in graph theoretical analyses.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Associates language network efficiency with all four PCA factors.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Associates clustering coefficient with Phonology, Semantics, and Lexical
        syntax.
    - source_id: P11-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates PCA results for complexity.
    - source_id: P11-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports variance for complexity factor.
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports variance for lexical syntax factor.
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lexical syntax factor composition.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Phonology and Semantics factors.
    - source_id: P12-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates relationship between complexity and severity.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses ambiguous measures in PCA.
    - source_id: P12-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Associates complexity factor with parietal and posterior temporal regions.
    - source_id: P12-S2-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies regions for complexity factor association.
    - source_id: P12-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies regions for lexical syntax factor association.
    - source_id: P12-S3-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Null result for tract-based connectivity disruption.
    - source_id: P12-S3-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Associates global efficiency with all four PCA measures.
    - source_id: P12-S4-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Specifies positive association of efficiency with complexity, lexical
        syntax, and phonology.
    - source_id: P12-S4-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Specifies negative association of efficiency with semantic ability.
    - source_id: P12-S4-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Associates clustering coefficient with phonological, semantic, and lexical
        syntax measures.
    - source_id: P13-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses PCA results relative to other studies.
    - source_id: P13-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lexical syntax factor as a distinct dimension.
    - source_id: P13-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of complexity and severity relationship.
    - source_id: P13-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of lexical syntax and fronto-parietal regions.
    - source_id: P13-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of graph theoretic measures.
    unresolved_coverage:
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S2-C7
    - P6-S1-C10
    - P9-S1-C9
    - P9-S1-C10
    - P9-S1-C11
    - P9-S1-C12
    - P9-S2-C4
    - P9-S2-C5
    - P9-S2-C6
    - P9-S2-C9
    - P9-S2-C11
    - P9-S2-C12
    - P9-S3-C2
    - P9-S3-C3
    - P9-S3-C6
    - P9-S3-C8
    - P9-S3-C9
    - P9-S3-C11
    - P9-S3-C12
    - P10-S1-C3
    - P10-S1-C6
    - P10-S1-C8
    - P11-S1-C3
    - P11-S2-C3
    - P11-S2-C6
    - P11-S2-C7
    - P12-S1-C3
    - P12-S1-C5
    - P12-S1-C9
    - P12-S2-C3
    - P12-S2-C4
    - P12-S3-C4
    - P12-S3-C5
    - P12-S3-C9
    - P12-S4-C2
    - P13-S1-C9
    - P13-S2-C5
    - P13-S2-C6
    - P13-S2-C9
    - P13-S2-C11
    - P13-S3-C1
    - P13-S3-C2
    - P13-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-10-2
    - TABLE-3-page-11-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S1-C5
      recruited_sample:
      - P4-S3-C8
      eligibility:
      - P4-S3-C8
      imaging_provenance:
      - P7-S1-C9
      imaging_timing:
      - P5-S1-C6
      outcome_timing:
      - P5-S1-C6
      outcome_definition: []
      validation:
      - P4-S2-C3
      analysis_restrictions:
      - P10-S1-C7
      dependent_variable_statement:
      - P1-S1-C6
      - P4-S3-C6
      - P4-S3-C7
      - P9-S1-C6
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S2-C3
      - P1-S2-C4
      - P10-S1-C7
      - P11-S1-C3
      - P11-S3-C3
      - P12-S3-C3
      - P13-S3-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P6-S3-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P9-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P1-S1-C3
      - P4-S1-C8
      - P5-S3-C2
      - P5-S3-C6
      - P5-S3-C8
      - P5-S3-C10
      - P5-S3-C12
      - P6-S1-C6
      - P6-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P13-S1-C3
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      - P13-S2-C7
      - P13-S2-C8
      - P13-S2-C9
      - P13-S2-C10
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
      pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
      review_sha256: 3a0527a74768b3e32514e7874356784afdb7b88a0dfa14ba5c5a7f3acf751e41
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
      - P11-S1-C5
      - P12-S4-C4
      source_result: In multiple regression analyses controlling for overall lesion
        volume, the language network average clustering coefficient was a significant
        predictor of Phonology (Estimate = -8.100, P=0.036) and Semantics (Estimate
        = 9.036, P=0.023) deficit scores. The source notes these were exploratory
        analyses with a large number of comparisons and that connectivity was estimated
        via atlas overlay rather than patient diffusion data.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the multiple regression of
            language network graph metrics on PCA factor scores, specifically the
            average clustering coefficient predicting Phonology and Semantics factors,
            as described in P11-S1-C5 and P12-S4-C4.
          source_ids:
          - P11-S1-C5
          - P12-S4-C4
          - P9-S1-C6
        direction:
          answer: fits
          reason: The draft correctly identifies a significant association. The source
            reports significant predictors for both factors. While the signs of the
            estimates differ (negative for Phonology, positive for Semantics), the
            draft's use of 'likely' and 'association' is consistent with the source's
            reporting of significant predictors without over-specifying the directionality
            in the core claim, and the source explicitly states the association in
            P12-S4-C4.
          source_ids:
          - P11-S1-C5
          - P12-S4-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as the language network average
            clustering coefficient. The outcome is correctly identified as Phonology
            and Semantics factors. The patient measurement is correctly classified
            as template_lesion_overlap, as the source (P13-S2-C8, P7-S1-C9) explicitly
            states that connectivity was estimated by overlaying patient lesion maps
            on a population-averaged HCP-842 tractography atlas, not via patient-specific
            diffusion imaging.
          source_ids:
          - P11-S1-C5
          - P7-S3-C2
          - P13-S2-C8
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the analysis
            controlled for overall lesion volume (P10-S1-C7, P11-S1-C5). It also includes
            the limitation that the analysis was exploratory with many comparisons
            (P11-S1-C6) and the methodological limitation regarding the atlas-based
            estimation (P13-S2-C8).
          source_ids:
          - P10-S1-C7
          - P11-S1-C6
          - P13-S2-C8
        missing_material_caveat:
          answer: fits
          reason: The draft captures the material caveats regarding the exploratory
            nature of the analysis, the large number of comparisons, and the specific
            method of connectivity estimation (atlas overlay vs patient diffusion).
            No other material caveats that change the interpretation of this specific
            result appear to be missing from the provided source window.
          source_ids:
          - P11-S1-C6
          - P13-S2-C8
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R009
      exposure:
        text: language network average clustering coefficient
      outcome:
        text: Phonology and Semantics factors
      analysis_label: Multiple Regression (Language Network)
      relation: association
      evidence_ids:
      - P1-S2-C4
      - P11-S1-C5
      - P11-S3-C3
      - P12-S4-C4
      qualifier_ids:
      - P1-S2-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
        source_review: _compare/relationships-2026-11-16/review-current/Zevgolatakou2022
        source_status_sha256: ba5845a79a946e9d1a0a12fe0a7528fd0cc751bedded4fd6ab908e420d726b86
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 37a35e438343eab5b36086f04ed9141eb361a4f0b1d9ce3c6a35c593e271329d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C5
          page: 5
          text_layer_sha256: 37a35e438343eab5b36086f04ed9141eb361a4f0b1d9ce3c6a35c593e271329d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The analytic sample contained behavioural data \nfrom 69 participants\
          \ and imaging data were available for \n58 of these participants."
        anchor_text: "The analytic sample contained behavioural data \nfrom 69 participants\
          \ and imaging data were available for \n58 of these participants."
        excluded_fragments: []
        image_sha256: 3909480b9c2e5366373a8b45a9d1a94fbdd50f028e78bf1a19fc66b3f3198091
        transcription: . The analytic sample contained behavioural data from 69 participants
          and imaging data were available for 58 of these participants
      P5-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f7e6e39ee82ec63f0f0d85a66bd82f179e795f35f8bf4904935f862ff3715c84
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C6
          page: 5
          text_layer_sha256: f7e6e39ee82ec63f0f0d85a66bd82f179e795f35f8bf4904935f862ff3715c84
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All but five participants were examined at the chronic stage\
          \ \nof aphasia (at least 3 months post-onset), but the exclusion of \nthese\
          \ five participants did not change the results so the more \ninclusive analyses\
          \ are reported here."
        anchor_text: "All but five participants were examined at the chronic stage\
          \ \nof aphasia (at least 3 months post-onset), but the exclusion of \nthese\
          \ five participants did not change the results so the more \ninclusive analyses\
          \ are reported here."
        excluded_fragments: []
        image_sha256: 2b99ea07dae911209b7b893faaa74452edc7a7da74bb5bf516e966315b8a5d7a
        transcription: 'All but five participants were examined at the chronic stage

          of aphasia (at least 3 months post-onset), but the exclusion of

          these five participants did not change the results so the more

          inclusive analyses are reported here'
      P13-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7712a756795eb8829f11bc2a02ce0eebcb9003d950dcb50fd447c33e7cce9e62
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 24f9f0843ad7e0c27f59ed955b6b73e4dffaa4fb7a9254a623c066b1b122e1aa
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P13-S1-C4
          page: 13
          text_layer_sha256: 24f9f0843ad7e0c27f59ed955b6b73e4dffaa4fb7a9254a623c066b1b122e1aa
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "This resulted in a sample size (N = 58) that \nwas moderate\
          \ relative to other LSM studies, with most of \nthe participants in the\
          \ mild-to-moderate range of aphasia se­\nverity (median WAB AQ = 81.0, IQR\
          \ = 71.3–91.0), though it \ndid include some participants with more severe\
          \ aphasia."
        anchor_text: "This resulted in a sample size (N = 58) that \nwas moderate\
          \ relative to other LSM studies, with most of \nthe participants in the\
          \ mild-to-moderate range of aphasia se­\nverity (median WAB AQ = 81.0, IQR\
          \ = 71.3–91.0), though it \ndid include some participants with more severe\
          \ aphasia."
        excluded_fragments: []
        image_sha256: 45c00a0bbb9a6a0c2b08e303fe6c85a1a3e3267d546ab4dabe3185310118c4a8
        transcription: '. This resulted in a sample size (N = 58) that

          was moderate relative to other LSM studies, with most of

          the participants in the mild-to-moderate range of aphasia se-

          verity (median WAB AQ = 81.0, IQR = 71.3–91.0), though it

          did include some participants with more severe aphasia'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: "Language network average clustering coefficient was also a sig­\nnificant\
    \ predictor of Phonology [Estimate= −8.100, 95% CI= \n(−15.662, −0.538), P=0.036]\
    \ and Semantics [Estimate= \n9.036, 95% CI= (1.249, 16.823), P=0.023], and a marginally\
    \ \nsignificant predictor of Lexical syntax [Estimate=8.777, 95% \nCI= (−0.501,\
    \ 18.055), P=0.064]."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
