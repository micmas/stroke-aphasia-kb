---
id: phonology_cluster
name: phonology cluster
kind: network
findings:
- id: f1
  target: phonology_factor
  target_kind: impairment
  claim: Performance on the phonological factor was uniquely correlated with a large
    cluster of a number of left hemisphere regions.
  direction: likely
  relationship: correlational
  method: VBCM
  sample:
    n: 43
    population: chronic post-stroke aphasic patients with persistent impairments in
      producing and/or understanding spoken language
    phase: not_reported
    time_post_onset: at least 12 months post-stroke at the time of scanning and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - lesion volume was not controlled for in the main analysis
  - significant results within areas correlated with lesion volume must be interpreted
    with caution regarding specificity
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient tissue concentration (voxel integrity) in
    a large left-hemisphere cluster including the frontal pole, middle frontal gyrus,
    inferior frontal gyrus, frontal and central opercular cortex, posterior insular
    cortex, temporal pole, planum polare, Heschl’s gyrus, planum temporale, superior
    temporal gyrus, middle temporal gyrus, parietal opercular cortex, and posterior
    supramarginal gyrus. the phonological factor was distilled using principal components
    analysis (PCA) from a large neuropsychological battery; the cluster overlapped
    with the anterior and posterior segments of the arcuate fasciculus. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S3-C3, two-model agreement, human verification pending):
    .

    All patients were at least 12 months post-stroke at the time

    of scanning and assessment, and were native English speakers

    with normal or corrected-to-normal hearing and vision Original text-layer quotation
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
    - proposed_concept:phonology_factor
  citation: '@Woollams2018'
  source_passages:
  - section: Original source P9-S1-C1
    page: 9
    quote: "\n3777\nBrain Structure and Function (2018) 223:3769–3786\t\n1 3\nPerformance\
      \ on the phonological factor was uniquely cor-\nrelated with a large cluster\
      \ of a number of left hemisphere \nregions: frontal pole, middle frontal gyrus\
      \ (MFG), inferior \nfrontal gyrus (IFG) (triangularis and orbitalis), frontal\
      \ and \ncentral opercular cortex, posterior insular cortex, temporal \npole,\
      \ planum polare, Heschl’s gyrus, planum temporale, \nsuperior temporal gyrus\
      \ (STG), middle temporal gyrus \n(MTG), parietal opercular cortex, and posterior\
      \ supramar-\nginal gyrus (SMG)."
    supports: claim
  - section: Original source P9-S1-C2
    page: 9
    quote: "The phonological cluster, therefore, \noverlapped with the anterior and\
      \ posterior segments of the \narcuate fasciculus, a key aspect of the dorsal\
      \ language path-\nway (Wise 2003; Catani and ffytche 2005; Catani et al. 2005;\
      \ \nTable 4   Results of the whole-\nbrain VBCM analyses for \nspeech measures\n\
      All peaks fall within the left hemisphere\nContrast\nCluster FWE\nk\nT\nx\n\
      y\nz\nAnatomy\nPhonology\n< 0.0005\n11,602\n5.98\n− 44\n− 10\n2\nInsular\n5.50\n\
      − 70\n− 22\n− 12\nMiddle temporal gyrus pos\n4.47\n− 58\n16\n− 8\nTemporal pole\n\
      4.28\n− 62\n− 54\n34\nMiddle temporal gyrus temocc\n4.26\n− 60\n− 4\n− 24\n\
      Middle temporal gyrus ant\n4.19\n− 56\n28\n0\nInferior frontal gyrus p tri\n\
      4.17\n− 52\n24\n− 12\nFrontal orbital cortex\n4.02\n− 62\n6\n2\nPrecentral gyrus\n\
      4.01\n− 46\n22\n4\nInferior frontal gyrus p tri\n3.96\n− 48\n32\n8\nInferior\
      \ frontal gyrus p tri\n3.92\n− 42\n− 42\n10\nSuperior longitudinal fasciculus\n\
      3.91\n− 42\n44\n12\nFrontal pole\n3.77\n− 68\n− 48\n16\nSupramarginal gyrus\
      \ pos\nSemantics\n0.003\n1456\n4.93\n− 56\n− 8\n− 26\nMiddle temporal gyrus\
      \ ant\n4.73\n− 40\n− 6\n− 26\nInferior longitudinal fas\n3.38\n− 28\n− 18\n\
      − 14\nHippocampus\nFluency\n< 0.0005\n5711\n5.04\n− 58\n2\n34\nPrecentral gyrus\n\
      4.75\n− 60\n− 2\n8\nPrecentral gyrus\n4.74\n− 62\n4\n22\nPrecentral gyrus\n\
      4.26\n− 44\n10\n50\nMiddle frontal gyrus\n3.97\n− 20\n8\n52\nSuperior frontal\
      \ gyrus\n3.62\n− 42\n− 8\n60\nPrecentral gyrus\n3.31\n− 24\n− 8\n32\nCorticospinal\
      \ tract\n3.18\n− 30\n− 4\n22\nPutamen\n2.98\n− 46\n18\n0\nFrontal operculum\
      \ cortex\n2.96\n− 32\n− 12\n66\nPrecentral gyrus\n2.96\n− 26\n− 16\n56\nPrecentral\
      \ gyrus\n2.91\n− 20\n− 10\n48\nPrecentral gyrus\n2.80\n− 6\n− 2\n36\nCingulum\
      \ cingulate\n2.79\n− 12\n18\n30\nCingulate gyrus ant\n0.021\n999\n3.72\n− 14\n\
      44\n20\nParacingulate gyrus\n3.40\n− 16\n52\n− 10\nInferior frontal occipital\
      \ fas\n"
    supports: claim
  - section: Original source P3-S3-C2
    page: 3
    quote: "Materials and methods\nParticipants\nForty-three chronic stroke patients\
      \ (either ischaemic or \nhaemorrhagic) were recruited, who had persistent impair-\n\
      ments in producing and/or understanding spoken language."
    supports: sample
  - section: Original source P3-S3-C3
    page: 3
    quote: "All patients were at least 12 months post-stroke at the time \nof scanning\
      \ and assessment, and were native English speak-\ners with normal or corrected-to-normal\
      \ hearing and vision."
    supports: sample
  - section: Original source P6-S1-C6
    page: 6
    quote: "Brain regions where tissue concentration (as represented \nby the continuous\
      \ values of the abnormality map from the \nunified segmentation–normalisation\
      \ procedure) were related \nto behavioural measures were identified using voxel-based\
      \ \ncorrelational methodology (VBCM) (Tyler et al. 2005), a \nvariant of voxel-based\
      \ lesion-symptom mapping (VSLM) \n(Bates et al. 2003) in which both the behaviour\
      \ and tissue \nconcentration measures are treated as continuous variables \n\
      (conducted in SPM8 using voxel-based morphometry)."
    supports: method
  - section: Original source P3-S2-C8
    page: 3
    quote: "Third, we were able to isolate and quantify \neach patient’s primary systems\
      \ capacities by using princi-\npal components analysis to distil optimal orthogonal\
      \ meas-\nures of semantic and phonological ability from a large neu-\nropsychological\
      \ battery (Lambon Ralph et al. 2002, 2003)."
    supports: method
  - section: Original source P8-S3-C4
    page: 8
    quote: "For \nthis reason, we did not control for lesion volume in our main \n\
      analyses, but we do provide the results controlled for lesion \nvolume controlled\
      \ in Table S1."
    supports: limitation
  - section: Original source P8-S3-C5
    page: 8
    quote: "It must be kept in mind that \nthe significant results within areas correlated\
      \ with lesion \nvolume must be interpreted with caution with respect to the\
      \ \nspecificity of their involvement in a particular behaviour."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Woollams2018
  proposal_id: R012
  review_status_sha256: 3a811daa8bfe79a3c6a6ce793b58e669d2cc950e88683604f958f1ce337a4040
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
        A/passages.json: 164fbd84a28609fa571fe7b37ea8bdefa275927c5c3ca9ecbce7ff4575baa192
        A/raw.json: 8d32f4083c7e964accf67ae1d1400bd4346ac236b9804c22e1068c5f3d2608ee
        A/source-units.json: b22b00489330b1e4f92817ad643cabf82bef1594dc8b87a33095a849a7edb60f
        A/full-source-units.json: 8bfe86e7eb24470a40687a4e54447be6e9f72ce60c244e15cb9069f6c689252b
        A/meta.json: 33109161e46898e5da56e9a74d497c0744415c09ca744729b21e59b89d5afcf0
        A/table-images/TABLE-1-page-5-1.png: 6208e2aa18021647362197fd7b90278277e5b1eee46c3b293924306949a39b9e
        A/table-images/TABLE-4-page-9-1.png: 8a41ea5325e9a9001bdabc4c395d36ab37b2d115535ef15f049d287b51da3108
        A/table-images/page-10.png: cfe2267d36f32301b0c39f86171a84c5e42d0c4e18abb772c2c6aa39461e08c6
        A/table-images/TABLE-1-page-6-1.png: 30e97a807461df3e57e69730b4f2289687ef054b6ab545e78157fe326c26518a
        A/table-images/page-6.png: d43ec4e7dcb2346f159fa654164162bdb1c4941203ef9fd0ca3768bd7d7ba15b
        A/table-images/TABLE-4-page-8-1.png: 5d60465a2234767a56cb61df13de83e8a55757f39853e87da3aba9620b7a28c3
        A/table-images/page-5.png: c834c690fed781263eb021a97d0c12f6374c7a2ad60961a9f543a277b4f58a19
        A/table-images/TABLE-3-page-8-2.png: 5d60465a2234767a56cb61df13de83e8a55757f39853e87da3aba9620b7a28c3
        A/table-images/page-9.png: fb5a7d06c5bde69028b98a6f34d72df8a28d7fb4a8080ab30426d3c5a13b33ad
        A/table-images/page-8.png: 37db358c98e6d1c9dd59252231bcd146ea6f4ffd38828f9ab3f6eef9b5e6f677
        A/table-images/manifest.json: 8411566a099766bb624c3f81a01b4c74190cb425a144dc6de1b6afe6e7e21bb0
        A/table-images/TABLE-2-page-6-2.png: 34f344b082565a79e10be49a0a46693bb826bae24455d08883f0db356e8b0d99
        A/table-images/TABLE-5-page-10-1.png: c7086a7b01c7bb15074ec4e69f7c7f2b90c8839390bc85bd98538aa3b02cefda
        A/clauses/window-10/raw.json: 2bee76f7b651f5d1b5bfc140d92ca35bd6e7e15322fd29fddb084cf54d9f2502
        A/clauses/window-10/prompt.txt: 5f54a1b5bfc9c18ba6208c0136687649bcd3e79e8c4680a90df32a4bfa171d85
        A/clauses/window-10/meta.json: 0d91368fc635c817fc42520dc97f738fe5de81207276781047a6f5db9e631933
        A/clauses/window-03/raw.json: 867ba93b64e27abc40072c4e05f11e35159e305f6af5ee89fc424d31e9aaf1a7
        A/clauses/window-03/prompt.txt: 5132b9bf033899f4181c947a846918b5e1d25c7a8ba23129582c3b54ac0aadb7
        A/clauses/window-03/meta.json: 1f1088ab103f460faeaa9f00b383be7a6ddc984da84a907fb95e3b5b54cc6528
        A/clauses/window-04/raw.json: 26776603de6e8a9ef6a150fb4d61555061566fc80d0865225230a65f370979d7
        A/clauses/window-04/prompt.txt: 63dc04717cbaa524cf666d7d479e3dd7b9596c0c1d5f17c6a53f242e400b8807
        A/clauses/window-04/meta.json: 77742126bf70fb2029f3812cdbd66f9fa5fb40168d7609f85b52dbde53ad6a9a
        A/clauses/window-05/raw.json: e9c64c055e7e7dca53899f4e6867f318e6052a28f6b24588d73e96e15cb665e8
        A/clauses/window-05/prompt.txt: 3a0e655efa32d14d74aa7f85124da0e6642224baf172da6472e731a7ee4ed395
        A/clauses/window-05/meta.json: f27a3d47f06f064c1fc2a7eafb2a9e5114d8f85faf7266b4a1587b747b478476
        A/clauses/window-02/raw.json: 65e302aecad317fbcee093bcd2eaf202aa8bfa782ef131185753fe90112ecfaa
        A/clauses/window-02/prompt.txt: 54f20862bc941549d9db12c85825cd60dfd0d4834adc4588510f43685b09b010
        A/clauses/window-02/meta.json: 40c8fd530f67c31c14c74e6d283468a027f40d80c964cb4d413ea34b20400b45
        A/clauses/window-09/raw.json: 10fcf0bc582745b0946a97669d206a17c1654fe38e5c1f32d5d71d2b89eed11b
        A/clauses/window-09/prompt.txt: 05bffadcf09af90035683f6e6d0f0808789a628b2496451b28be75903159611b
        A/clauses/window-09/meta.json: c9d16db7f0dd77becfcde3a1aae2f6d23165c5303032f4ec5fedef60c399e818
        A/clauses/window-07/raw.json: 68d1a5e5cbd95d27727e49f3990ba71aeeab494239dc6f78c60406c2fa5df7ee
        A/clauses/window-07/prompt.txt: e3fa98495fd5c74791472caf03f3ba1566c29377a681edda8b60bc3eed742618
        A/clauses/window-07/meta.json: a1513fe724f33f5f50294a5a8ad4b7f14bd3102d3e0f42edde9c0853d46a4cf7
        A/clauses/window-01/raw.json: eff1cb2a76a43be8ef599e16a21187cfe4e5b6fbc67a7e27402a4e776afa4536
        A/clauses/window-01/prompt.txt: 75e3940931014e10507d183cf19a737ed57fc4aeb46392102026bb8406c5a114
        A/clauses/window-01/meta.json: e71554dfc032c3800e0ecb73917e3dde18d8c473793696854cdb7033c9d410af
        A/clauses/window-06/raw.json: 83348ecf2ec1cbc49833a4ff19de5a67f7db1cfe9c4b8833f6819ff874b98902
        A/clauses/window-06/prompt.txt: 8e67cb6f3054405b10d8668090402567484740f1c1f2b9233e5b8804583682eb
        A/clauses/window-06/meta.json: 9b946fa9c666af68455dd2b0961aa3940a6c301b356b258b284ed0d38d6e0b15
        A/clauses/window-08/raw.json: 8da13c37fef348b91f10ccd9872ce2e38053a2485eb96fa3b76dfb34ba6b1c5f
        A/clauses/window-08/prompt.txt: 2a4386699eaf64cc9131bb5202264d81ba354381d1fca43ba2c1cc2a4025a1cb
        A/clauses/window-08/meta.json: 1319ae624bfa308d230154d5199af10eaa5a50d2960fd0b9d2da0fdc20eb1895
        A/tables/TABLE-1-page-5-1/raw.json: 344b9aac4a5ebd6839fdc586304503603fdb1a7401f2b2325ef6a33332a72fb7
        A/tables/TABLE-1-page-5-1/prompt.txt: 26d9fded3e4005164d54127eb47db4769f428b78d160c95e8ff16274c08f36bc
        A/tables/TABLE-1-page-5-1/meta.json: 120ce923bc56c96b8f896e95d94fdc69371df59998b64b0996d394fd36b6a35a
        A/tables/TABLE-4-page-8-4/raw.json: c3da5bf346c9d2d52f0926757dfc324015ed60fe0f97df181c3949e8868cbd63
        A/tables/TABLE-4-page-8-4/prompt.txt: 3cc63f0f9755d6a43340fd9ccb137415b0d51ef8294bde9786385fac528ac046
        A/tables/TABLE-4-page-8-4/meta.json: f26c7eef381632a15e9ac7e9d85b2a337285cfa6ed412c0812b492d328ce8358
        A/tables/TABLE-5-page-10-7/raw.json: ec05d006ab9398a3841ce2b9a6b277c27ab586ac3ecc6ab65a04d2cb8b0ab183
        A/tables/TABLE-5-page-10-7/prompt.txt: e7c189992f3a17403b11ee3f3f6003b6ff26c27d2c833be98626c0a7904a7fbf
        A/tables/TABLE-5-page-10-7/meta.json: 4e0b954d1fd1f4a1134e4dd2c4ab4a6cbbc841b962a20cc587e38d6deb342966
        A/tables/TABLE-4-page-9-6/raw.json: 7bec6cd1d3307d9d81558a7c2fafbaca228e0a024e366f7631caaee8299a8d87
        A/tables/TABLE-4-page-9-6/prompt.txt: a08795886e3ed820b3a78c9d02de387b9e942138c87a641d9ddf8c0fce43cb77
        A/tables/TABLE-4-page-9-6/meta.json: e229b07f2defda540d61931fafc4f6249c06cd9dfebcb46d6b551d97d686f409
        A/tables/TABLE-3-page-8-5/raw.json: 66e743768073d2c5276fe78443bb4656c312ed1ecb305670a5f69ba60537df0d
        A/tables/TABLE-3-page-8-5/prompt.txt: dcdcf0b07365fe627ae89b1db231632520e2669aab66389f5789be1f34660a3e
        A/tables/TABLE-3-page-8-5/meta.json: 1ee6ccebdefcd4afbe8de3e856922e1a07ea19a822337fd9a8146a2629fc9b72
        A/tables/TABLE-2-page-6-3/raw.json: 411745520a1a9fa27164d94a82b39c0b984238041dbe75326b4e9275801d8490
        A/tables/TABLE-2-page-6-3/prompt.txt: 2e2b133766002cb2ead3a775a4175003b7b4a2849f642628eabc061cf376ab96
        A/tables/TABLE-2-page-6-3/meta.json: 4b757c5357db9d644b6ead865be09aa2bfe094bc2430e4e4a6b9de3b8ac9d183
        A/tables/TABLE-1-page-6-2/raw.json: 2139f199fab2035bf12d53200d1acea3e41475afa21099940b40d4b33af080bc
        A/tables/TABLE-1-page-6-2/prompt.txt: 92918a6992b6df3d90b98916e6d7aea8b1d4e3f8a486a29d364f5062e07915e0
        A/tables/TABLE-1-page-6-2/meta.json: 8ef058615d45225ad53be6ff2fb1cd41a619ad778526c2091a18b9fd522e3fc3
        B/passages.json: 164fbd84a28609fa571fe7b37ea8bdefa275927c5c3ca9ecbce7ff4575baa192
        B/raw.json: ada6d9d30112edc6cec40eef43037b9ed6cf21262253788c2a1db57ad4b95003
        B/source-units.json: b22b00489330b1e4f92817ad643cabf82bef1594dc8b87a33095a849a7edb60f
        B/full-source-units.json: 8bfe86e7eb24470a40687a4e54447be6e9f72ce60c244e15cb9069f6c689252b
        B/meta.json: c1524a2d3fc98b606e5dc869d12dfdf45fa00cc14952fba311ee7717e86e78b2
        B/table-images/TABLE-1-page-5-1.png: 6208e2aa18021647362197fd7b90278277e5b1eee46c3b293924306949a39b9e
        B/table-images/TABLE-4-page-9-1.png: 8a41ea5325e9a9001bdabc4c395d36ab37b2d115535ef15f049d287b51da3108
        B/table-images/page-10.png: cfe2267d36f32301b0c39f86171a84c5e42d0c4e18abb772c2c6aa39461e08c6
        B/table-images/TABLE-1-page-6-1.png: 30e97a807461df3e57e69730b4f2289687ef054b6ab545e78157fe326c26518a
        B/table-images/page-6.png: d43ec4e7dcb2346f159fa654164162bdb1c4941203ef9fd0ca3768bd7d7ba15b
        B/table-images/TABLE-4-page-8-1.png: 5d60465a2234767a56cb61df13de83e8a55757f39853e87da3aba9620b7a28c3
        B/table-images/page-5.png: c834c690fed781263eb021a97d0c12f6374c7a2ad60961a9f543a277b4f58a19
        B/table-images/TABLE-3-page-8-2.png: 5d60465a2234767a56cb61df13de83e8a55757f39853e87da3aba9620b7a28c3
        B/table-images/page-9.png: fb5a7d06c5bde69028b98a6f34d72df8a28d7fb4a8080ab30426d3c5a13b33ad
        B/table-images/page-8.png: 37db358c98e6d1c9dd59252231bcd146ea6f4ffd38828f9ab3f6eef9b5e6f677
        B/table-images/manifest.json: beea01b5e24b439ce8ebf16aaee56e8af21514ae90eae2768687acb07a2d60cb
        B/table-images/TABLE-2-page-6-2.png: 34f344b082565a79e10be49a0a46693bb826bae24455d08883f0db356e8b0d99
        B/table-images/TABLE-5-page-10-1.png: c7086a7b01c7bb15074ec4e69f7c7f2b90c8839390bc85bd98538aa3b02cefda
        B/clauses/window-10/raw.json: aa4dcc5534a0719ff9e9cc5381eaa62b584fe7477088e515178e8e96e2c4bdef
        B/clauses/window-10/prompt.txt: 5f54a1b5bfc9c18ba6208c0136687649bcd3e79e8c4680a90df32a4bfa171d85
        B/clauses/window-10/meta.json: 3f12e60ee3bf085a3ac44ec8fdf80e5d0b2260ea05d7cbf85ee33dada6aeb570
        B/clauses/window-03/raw.json: de7e6403a48c79b538aec7ce04148eacb6a49960de96fa5cad6e77ee99d1472e
        B/clauses/window-03/prompt.txt: 5132b9bf033899f4181c947a846918b5e1d25c7a8ba23129582c3b54ac0aadb7
        B/clauses/window-03/meta.json: c24e81e8e98402ecbb1a3ebc310691089e2124acaede3e44f38c7faf7a2ba36c
        B/clauses/window-04/raw.json: 2b3763e5ee47f284adce12e9f53925b02f37784dc15755fb5d3d2868f5679a6a
        B/clauses/window-04/prompt.txt: 63dc04717cbaa524cf666d7d479e3dd7b9596c0c1d5f17c6a53f242e400b8807
        B/clauses/window-04/meta.json: 11278017fc21acccf7799ca7431a6139ded0f44b5c960c581650ec6c4717a023
        B/clauses/window-05/raw.json: 951b69fd79295750cc911f8d920f7dbd89d693fce0c07f7b1a2f800da935e033
        B/clauses/window-05/prompt.txt: 3a0e655efa32d14d74aa7f85124da0e6642224baf172da6472e731a7ee4ed395
        B/clauses/window-05/meta.json: 8ee0908ea6810da3dbfe8042aac23a8c2c4419a3d4908f77ddea7448bcd810fa
        B/clauses/window-02/raw.json: 5ffa00e2b7f184ce98afffe788136faba432545a6ad9d1a748df5802a016d86a
        B/clauses/window-02/prompt.txt: 54f20862bc941549d9db12c85825cd60dfd0d4834adc4588510f43685b09b010
        B/clauses/window-02/meta.json: 35ae425adf5af516891d80ebeae43e9ffcef06eb57b3f469290a94745004cd13
        B/clauses/window-09/raw.json: 9b9255285964b722fb184ec102534a1f64fd867bab7b4d212e0907991ef17b29
        B/clauses/window-09/prompt.txt: 05bffadcf09af90035683f6e6d0f0808789a628b2496451b28be75903159611b
        B/clauses/window-09/meta.json: bfe0744ad953b685876101bc5a883cf89b3ba9ca9c75251ac71bd6a63cc7c8f9
        B/clauses/window-07/raw.json: d410b9faf3ed1cb6dd9a56a5cf26b17583cd9387bf51e5927352473eb4111418
        B/clauses/window-07/prompt.txt: e3fa98495fd5c74791472caf03f3ba1566c29377a681edda8b60bc3eed742618
        B/clauses/window-07/meta.json: 1608bc718b10ec55b53c0daa0d86f202087012c6d26530dbbba3ccd40c8be953
        B/clauses/window-01/raw.json: 63262788b013b5d05132b339765a96320528e2ca4ffffce18a5b4de793c499cf
        B/clauses/window-01/prompt.txt: 75e3940931014e10507d183cf19a737ed57fc4aeb46392102026bb8406c5a114
        B/clauses/window-01/meta.json: 571d24a17d1d86b00f8da03b3015b225d0b1dd1f7501affd36238f4fd69c87c1
        B/clauses/window-06/raw.json: 3f51365025a1598b3a5be52d2cc9d92315617e90cde79105996a83f991e8d90a
        B/clauses/window-06/prompt.txt: 8e67cb6f3054405b10d8668090402567484740f1c1f2b9233e5b8804583682eb
        B/clauses/window-06/meta.json: 5f8e306010f4d8d4e132de5739b19f8a85a8ffcfe3508b25f38a39c2b64e20ec
        B/clauses/window-08/raw.json: c1193cddc2030dbf561d97b230ebf9d4fba91715c5e0db624a9cf09d79dd2347
        B/clauses/window-08/prompt.txt: 2a4386699eaf64cc9131bb5202264d81ba354381d1fca43ba2c1cc2a4025a1cb
        B/clauses/window-08/meta.json: a20e6b2fe64f1e0e1e0a96524ffaedc0f8141d55c3f5b206a137af14e9235f65
        B/tables/TABLE-1-page-5-1/raw.json: 270c1c397f2292f554683fc6e25ec2f7d39c99c865648ef7f25e9cc2ebfc8a6c
        B/tables/TABLE-1-page-5-1/prompt.txt: 26d9fded3e4005164d54127eb47db4769f428b78d160c95e8ff16274c08f36bc
        B/tables/TABLE-1-page-5-1/meta.json: e2da737469171f2c18c367a0e860548407b47a49abe2cc3b369ec92b1f9bd98d
        B/tables/TABLE-4-page-8-4/raw.json: 0ed7f4b1e3a6e293e0f3516767eebeb1ab2c5071ae8bb44ea656859a6ac7a0b1
        B/tables/TABLE-4-page-8-4/prompt.txt: 3cc63f0f9755d6a43340fd9ccb137415b0d51ef8294bde9786385fac528ac046
        B/tables/TABLE-4-page-8-4/meta.json: 6fae8977870bdfb2891fb4a568d1ed2d642a46cf1e4b9873b25c5f181ac604bd
        B/tables/TABLE-5-page-10-7/raw.json: e3ddbb86fef1d5eb323d80b4124f0ec6a17d684f6a8cd876a0d5ad996d3fbd04
        B/tables/TABLE-5-page-10-7/prompt.txt: e7c189992f3a17403b11ee3f3f6003b6ff26c27d2c833be98626c0a7904a7fbf
        B/tables/TABLE-5-page-10-7/meta.json: 39a72f5601186013523d29cb77cd03e95c0829b6a1b57e6ad873f66ad9faa7f2
        B/tables/TABLE-4-page-9-6/raw.json: dbc3d865a3e5684f52996fa6a81567e4e9a02caad3fe28fe2dab68b0dd2eb29a
        B/tables/TABLE-4-page-9-6/prompt.txt: a08795886e3ed820b3a78c9d02de387b9e942138c87a641d9ddf8c0fce43cb77
        B/tables/TABLE-4-page-9-6/meta.json: 8582c5b645e502984968b7ecd73a0b504f39bf993bc1f1f2ca2024192bf0c003
        B/tables/TABLE-3-page-8-5/raw.json: 0ed7f4b1e3a6e293e0f3516767eebeb1ab2c5071ae8bb44ea656859a6ac7a0b1
        B/tables/TABLE-3-page-8-5/prompt.txt: dcdcf0b07365fe627ae89b1db231632520e2669aab66389f5789be1f34660a3e
        B/tables/TABLE-3-page-8-5/meta.json: e65c14091b8838afded10ffaf799199a9441a225a1ca09228226d14e8b20f9b7
        B/tables/TABLE-2-page-6-3/raw.json: 36d3262688c25bd40b02df11bf077b1e406e2652b8fd62b2f45fa1608aaf0d83
        B/tables/TABLE-2-page-6-3/prompt.txt: 2e2b133766002cb2ead3a775a4175003b7b4a2849f642628eabc061cf376ab96
        B/tables/TABLE-2-page-6-3/meta.json: 713a12ed8586e550fb09597baf7b195f68dd40233bfd56163c11227f0614842b
        B/tables/TABLE-1-page-6-2/raw.json: b6f8f98c5f018c8680426ec43036dbe3b01468debeed8d3949228251988a1376
        B/tables/TABLE-1-page-6-2/prompt.txt: 92918a6992b6df3d90b98916e6d7aea8b1d4e3f8a486a29d364f5062e07915e0
        B/tables/TABLE-1-page-6-2/meta.json: 1632ba156c794899e126ebfff5b3ab5dec5c408f9e137c3443937b8a9b634987
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
      pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
      source_review: _compare/relationships-2026-11-16/review-current/Woollams2018
      source_status_sha256: 993ec54f5bd528cfdc2b36c34d1eb0093d2c8829d25329c5473158de3e0635db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: phonology factor
    outcome:
      text: neural integrity (left hemisphere regions)
    analysis_label: VBCM (Primary Systems)
    relation: association
    evidence_ids:
    - P9-S1-C1
    - P9-S1-C2
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
      pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
      source_review: _compare/relationships-2026-11-16/review-current/Woollams2018
      source_status_sha256: 993ec54f5bd528cfdc2b36c34d1eb0093d2c8829d25329c5473158de3e0635db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P2-S2-C2
      - Result passage disposed without unit P2-S2-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S1-C9
      - Result passage disposed without unit P11-S2-C1
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P11-S2-C4
      - Result passage disposed without unit P11-S2-C7
      - Result passage disposed without unit P11-S2-C8
      - Result passage disposed without unit P11-S3-C4
      - Result passage disposed without unit P11-S3-C11
      - Result passage disposed without unit P11-S3-C5
      - Result passage disposed without unit P11-S3-C6
      - Result passage disposed without unit P11-S3-C7
      - Result passage disposed without unit P11-S3-C8
      - Result passage disposed without unit P11-S3-C9
      - Result passage disposed without unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C11
      - Result passage disposed without unit P12-S1-C4
      - Result passage disposed without unit P12-S1-C5
      - Result passage disposed without unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S1-C8
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P13-S1-C2
      - Accounting without a linked unit P13-S1-C5
      - Result passage disposed without unit P13-S1-C6
      - Result passage disposed without unit P13-S1-C7
      - Unaccounted source passage P13-S1-C5
      - Result passage disposed without unit P14-S1-C1
      - 'window 13: invalid/duplicate disposition P14-S1-C2'
      - Result passage disposed without unit P15-S1-C2
      - Result passage disposed without unit P15-S1-C3
      - Result passage disposed without unit P15-S1-C5
      - Result passage disposed without unit P15-S1-C6
      - Unresolved source passage P15-S3-C2
      - Accounting without a linked unit P15-S3-C4
      - Result passage disposed without unit P15-S3-C5
      - Accounting without a linked unit P15-S3-C6
      - Accounting without a linked unit P15-S3-C7
      - Accounting without a linked unit P16-S1-C4
      - Accounting without a linked unit P16-S1-C5
      - Unaccounted source passage P16-S1-C5
      - Unaccounted source passage P15-S3-C4
      - Unaccounted source passage P15-S3-C7
      - Unaccounted source passage P16-S1-C4
      - Unaccounted source passage P15-S3-C6
      unattached_null_or_qualifier_ids:
      - P7-S1-C5
      - P11-S2-C2
      - P12-S1-C7
      - P13-S1-C1
      - P13-S1-C7
      - P15-S1-C2
      - P16-S1-C5
      suppressed_nonrepresented_units: 31
      default_disposition_count_requires_completeness_check: 174
      unselected_timing_passages:
      - P1-S1-C4
      - P2-S1-C3
      - P3-S2-C5
      - P3-S2-C7
      - P3-S3-C2
      - P3-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C7
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
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C5
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
        source_id: P13-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C1
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
        source_id: P14-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S2-C10
        - P6-S1-C6
        - P6-S1-C8
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C9
        - P8-S3-C6
        - P8-S3-C7
        - P11-S1-C4
        - P11-S1-C5
        - P11-S1-C6
        - P11-S1-C7
        - P11-S1-C8
        - P11-S1-C9
        - P11-S2-C1
        - P11-S2-C2
        - P11-S2-C3
        - P11-S2-C5
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S3-C3
        - P11-S3-C4
        - P11-S3-C5
        - P11-S3-C6
        - P11-S3-C7
        - P11-S3-C8
        - P11-S3-C9
        - P11-S3-C10
        - P11-S3-C11
        - P12-S1-C1
        - P12-S1-C2
        - P12-S1-C3
        - P12-S1-C4
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C8
        - P12-S1-C9
        - P12-S1-C10
        - P12-S1-C11
        - P12-S1-C12
        - P12-S1-C13
        - P12-S2-C3
        - P12-S2-C4
        - P12-S2-C5
        - P12-S2-C6
        - P13-S1-C1
        - P13-S1-C2
        - P13-S1-C3
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        - P13-S2-C3
        - P13-S2-C5
        - P14-S1-C1
        - P14-S1-C2
        - P14-S1-C3
        - P14-S1-C4
        - P14-S1-C5
        - P14-S1-C6
        - P14-S1-C7
        - P14-S1-C9
        - P14-S2-C1
        - P14-S2-C3
        - P15-S1-C1
        - P15-S1-C2
        - P15-S1-C3
        - P15-S1-C4
        - P15-S1-C5
        - P15-S1-C6
        - P15-S1-C7
        - P15-S1-C8
        - P15-S1-C9
        - P15-S2-C2
        - P15-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-1-page-6-2
      - TABLE-2-page-6-3
      - TABLE-3-page-8-5
      - TABLE-4-page-8-4
      - TABLE-4-page-9-6
      - TABLE-5-page-10-7
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-1-page-6-2
      - TABLE-2-page-6-3
      - TABLE-3-page-8-5
      - TABLE-5-page-10-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S1
        - P7-S1
        - P8-S1
        - P8-S2
        - P8-S3
        - P11-S1
        - P11-S2
        - P11-S3
        - P12-S1
        - P12-S2
        - P13-S1
        - P13-S2
        - P14-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
      source_review: _compare/relationships-2026-11-16/review-current/Woollams2018
      source_status_sha256: 993ec54f5bd528cfdc2b36c34d1eb0093d2c8829d25329c5473158de3e0635db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Study objective statement
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P2-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Study objective statement
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prior study result (Crisp and Lambon Ralph 2006)
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prior study result (Crisp and Lambon Ralph 2006)
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Normative data for controls
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of PCA methodology
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes: []
      reason: Sensitivity result for semantic cluster (not a distinct relationship
        but a qualification of the main analysis)
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of deficits
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance reporting
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor loading description
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor loading description
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor loading description
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor loading description
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Direct behavioural correlation results
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Null result for cognitive factor
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: ANCOVA results for phonology factor
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: ANCOVA results for semantics factor
    - source_id: P8-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Summary of behavioural results
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion map
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion map
    - source_id: P8-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on lesion volume
    - source_id: P8-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to results in figures/tables
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: VBCM results for phonology factor
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 11
      reason: VBCM results for phonology factor
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: VBCM results for phonology factor
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 11
      reason: VBCM results for phonology factor (Table 4)
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of phonology cluster
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: VBCM results for semantics factor
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 12
      reason: VBCM results for semantics factor
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to results in figures/tables
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 17
      reason: Core reading network association
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 17
      reason: Core reading network association
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: White-matter connectivity description
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 18
      reason: Association for nonword and abstract word reading
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 19
      reason: Association for abstract and concrete word reading
    - source_id: P11-S2-C1
      disposition: represented
      result_indexes:
      - 19
      reason: Association for abstract and concrete word reading
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 20
      reason: Null result for nonword and concrete word reading
    - source_id: P11-S2-C3
      disposition: represented
      result_indexes:
      - 21
      reason: Specific association for nonword reading
    - source_id: P11-S2-C4
      disposition: represented
      result_indexes:
      - 21
      reason: Specific association for nonword reading
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 22
      reason: Specific association for abstract word reading
    - source_id: P11-S2-C6
      disposition: represented
      result_indexes:
      - 23
      reason: Specific association for concrete word reading
    - source_id: P11-S2-C7
      disposition: repeated
      result_indexes:
      - 21
      - 22
      - 23
      reason: Summary of specific reading associations
    - source_id: P11-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of map extents
    - source_id: P11-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figures
    - source_id: P11-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 11
      - 13
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      - 21
      - 22
      - 23
      reason: General summary of phonological relationship
    - source_id: P11-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of map locations
    - source_id: P11-S3-C5
      disposition: represented
      result_indexes:
      - 24
      reason: Overlap of nonword reading and phonology map
    - source_id: P11-S3-C6
      disposition: represented
      result_indexes:
      - 24
      reason: Overlap of nonword reading and phonology map
    - source_id: P11-S3-C7
      disposition: represented
      result_indexes:
      - 25
      reason: Overlap of abstract word reading and phonology map
    - source_id: P11-S3-C8
      disposition: represented
      result_indexes:
      - 25
      reason: Overlap of abstract word reading and phonology map
    - source_id: P11-S3-C9
      disposition: represented
      result_indexes:
      - 26
      reason: Overlap of concrete/abstract word reading and phonology map
    - source_id: P11-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on relationship strength
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 27
      - 28
      - 29
      reason: Summary of semantic relationship strength
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 27
      reason: Minimal overlap of nonword reading and semantics map
    - source_id: P12-S1-C5
      disposition: represented
      result_indexes:
      - 28
      reason: Considerable overlap of abstract word reading and semantics map
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 28
      - 29
      reason: Overlap of abstract and concrete word reading and semantics map
    - source_id: P12-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of areas outside primary systems
    - source_id: P13-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of non-overlapping region
    - source_id: P13-S1-C5
      disposition: represented
      result_indexes:
      - 30
      reason: Behavioural correlation between fluency and reading
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes:
      - 31
      reason: Overlap between fluency and nonword reading maps
    - source_id: P13-S1-C7
      disposition: represented
      result_indexes:
      - 31
      reason: Overlap between fluency and nonword reading maps
    - source_id: P14-S1-C3
      disposition: represented
      result_indexes:
      - 32
      - 33
      - 34
      reason: Partial correlation results for fluency
    - source_id: P15-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of nonword/phonology correlation
    - source_id: P15-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      - 4
      reason: Restatement of abstract word/phonology and semantics correlation
    - source_id: P15-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of concrete word/phonology and semantics correlation
    - source_id: P15-S1-C5
      disposition: repeated
      result_indexes:
      - 31
      reason: Restatement of fluency component
    - source_id: P16-S1-C4
      disposition: represented
      result_indexes:
      - 31
      reason: Overlap between fluency and nonword reading maps
    - source_id: P16-S1-C5
      disposition: represented
      result_indexes:
      - 32
      reason: Restatement of partial correlation for nonwords
    unresolved_coverage:
    - source_id: P7-S1-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P2-S1-C3
    - P2-S2-C2
    - P2-S2-C4
    - P4-S2-C2
    - P4-S2-C7
    - P7-S1-C5
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C10
    - P7-S1-C11
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C10
    - P8-S2-C2
    - P8-S2-C3
    - P8-S2-C10
    - P8-S3-C6
    - P11-S1-C1
    - P11-S1-C4
    - P11-S1-C7
    - P11-S2-C7
    - P11-S2-C8
    - P11-S2-C10
    - P11-S3-C4
    - P11-S3-C11
    - P12-S1-C1
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S1-C11
    - P13-S1-C1
    - P13-S1-C2
    - P14-S1-C1
    - P14-S1-C2
    - P15-S1-C5
    - P15-S1-C6
    - P15-S2-C3
    - P15-S2-C5
    - P15-S2-C7
    - P15-S3-C4
    - P15-S3-C5
    - P15-S3-C6
    - P15-S3-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-1-page-6-2
    - TABLE-2-page-6-3
    - TABLE-3-page-8-5
    - TABLE-4-page-8-4
    - TABLE-4-page-9-6
    - TABLE-5-page-10-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C2
      - P3-S3-C6
      recruited_sample:
      - P3-S3-C2
      eligibility:
      - P3-S3-C3
      - P3-S3-C4
      imaging_provenance:
      - P4-S3-C2
      - P6-S1-C3
      imaging_timing:
      - P4-S3-C3
      outcome_timing:
      - P4-S3-C3
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P8-S2-C8
      - P8-S2-C9
      dependent_variable_statement:
      - P4-S2-C10
      - P6-S1-C6
      - P6-S1-C8
      - P8-S1-C6
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C8
      - P8-S2-C11
      explicitly_not_adjusted:
      - P8-S3-C4
      descriptive_personal_factors:
      - P3-S3-C2
      - P3-S3-C3
      - P5-S1-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C7
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
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C5
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
      source_id: P13-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C1
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
      source_id: P14-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S2-C10
      - P6-S1-C6
      - P6-S1-C8
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C9
      - P8-S3-C6
      - P8-S3-C7
      - P11-S1-C4
      - P11-S1-C5
      - P11-S1-C6
      - P11-S1-C7
      - P11-S1-C8
      - P11-S1-C9
      - P11-S2-C1
      - P11-S2-C2
      - P11-S2-C3
      - P11-S2-C5
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S3-C3
      - P11-S3-C4
      - P11-S3-C5
      - P11-S3-C6
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C9
      - P11-S3-C10
      - P11-S3-C11
      - P12-S1-C1
      - P12-S1-C2
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      - P12-S1-C10
      - P12-S1-C11
      - P12-S1-C12
      - P12-S1-C13
      - P12-S2-C3
      - P12-S2-C4
      - P12-S2-C5
      - P12-S2-C6
      - P13-S1-C1
      - P13-S1-C2
      - P13-S1-C3
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C6
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      - P13-S2-C3
      - P13-S2-C5
      - P14-S1-C1
      - P14-S1-C2
      - P14-S1-C3
      - P14-S1-C4
      - P14-S1-C5
      - P14-S1-C6
      - P14-S1-C7
      - P14-S1-C9
      - P14-S2-C1
      - P14-S2-C3
      - P15-S1-C1
      - P15-S1-C2
      - P15-S1-C3
      - P15-S1-C4
      - P15-S1-C5
      - P15-S1-C6
      - P15-S1-C7
      - P15-S1-C8
      - P15-S1-C9
      - P15-S2-C2
      - P15-S2-C3
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
      pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
      review_sha256: 3a811daa8bfe79a3c6a6ce793b58e669d2cc950e88683604f958f1ce337a4040
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
      - P9-S1-C1
      - P9-S1-C2
      source_result: Performance on the phonological factor was uniquely correlated
        with a large cluster of left hemisphere regions, including frontal pole, middle
        frontal gyrus, inferior frontal gyrus, opercular cortex, insular cortex, temporal
        pole, Heschl's gyrus, planum temporale, superior and middle temporal gyri,
        parietal opercular cortex, and posterior supramarginal gyrus. This cluster
        overlapped with the anterior and posterior segments of the arcuate fasciculus.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VBCM analysis of the phonology
            factor. The source explicitly links the phonological factor to the identified
            left hemisphere cluster in P9-S1-C1 and P9-S1-C2. The method is VBCM,
            which correlates tissue concentration (voxel integrity) with the behavioral
            factor score.
          source_ids:
          - P9-S1-C1
          - P9-S1-C2
          - P6-S1-C6
        direction:
          answer: fits
          reason: The source states that performance on the phonological factor was
            'uniquely correlated' with the cluster. The proposed draft uses 'likely'
            direction, which is a reasonable qualitative representation of a significant
            correlation without specifying the sign (positive/negative) which is not
            explicitly detailed in the prose summary, though Table 4 shows T-values.
            The core relationship is an association.
          source_ids:
          - P9-S1-C1
        construct:
          answer: fits
          reason: The exposure is the 'phonology factor' derived from PCA. The outcome
            is 'neural integrity' in left hemisphere regions. The measurement is correctly
            identified as template_lesion_overlap (VBCM uses tissue concentration/abnormality
            maps relative to controls, not patient diffusion tractography). The regions
            listed in the draft match the source text in P9-S1-C1.
          source_ids:
          - P9-S1-C1
          - P3-S2-C8
          - P6-S1-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the factor was distilled
            using PCA and that the cluster overlapped with the arcuate fasciculus.
            It also includes the limitation that lesion volume was not controlled
            for in the main analysis, which is a material caveat mentioned in P8-S3-C4
            and P8-S3-C5. The draft correctly identifies this as a limitation/qualification
            rather than a standalone finding about lesion volume.
          source_ids:
          - P9-S1-C2
          - P8-S3-C4
          - P8-S3-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveat regarding lesion volume not being
            controlled for in the main analysis, which is explicitly stated as a reason
            for caution in interpreting specificity (P8-S3-C5). No other material
            caveats appear to be missing from the provided source window that would
            change the interpretation of this specific association.
          source_ids:
          - P8-S3-C5
      optional_pending:
      - Specific T-values and coordinates from Table 4 are not transcribed in the
        draft, which is acceptable for a qualitative draft.
      - The exact sign of the correlation (positive/negative) is not explicitly stated
        in the prose, only that it is 'uniquely correlated'.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific T-values and coordinates from Table 4 are not transcribed in the draft,
      which is acceptable for a qualitative draft.
    - The exact sign of the correlation (positive/negative) is not explicitly stated
      in the prose, only that it is 'uniquely correlated'.
    normalizations: []
    analysis_identity:
      id: R012
      exposure:
        text: phonology factor
      outcome:
        text: neural integrity (left hemisphere regions)
      analysis_label: VBCM (Primary Systems)
      relation: association
      evidence_ids:
      - P9-S1-C1
      - P9-S1-C2
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
        pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
        source_review: _compare/relationships-2026-11-16/review-current/Woollams2018
        source_status_sha256: 993ec54f5bd528cfdc2b36c34d1eb0093d2c8829d25329c5473158de3e0635db
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fc0401355b3c6086f7230cbb31af68ebc26633b6a812c3fa3e7e981132bfd730
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 62c99388a0937a9aab803d988cd88c1dcb06cc470975710cc98d7c2b8e832141
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C3
          page: 3
          text_layer_sha256: 62c99388a0937a9aab803d988cd88c1dcb06cc470975710cc98d7c2b8e832141
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All patients were at least 12 months post-stroke at the time\
          \ \nof scanning and assessment, and were native English speak-\ners with\
          \ normal or corrected-to-normal hearing and vision."
        anchor_text: "All patients were at least 12 months post-stroke at the time\
          \ \nof scanning and assessment, and were native English speak-\ners with\
          \ normal or corrected-to-normal hearing and vision."
        excluded_fragments: []
        image_sha256: 48a83b6d71ff57336389bf00186c347a974889a9310539a53c3bd4fb4b53cc18
        transcription: '.

          All patients were at least 12 months post-stroke at the time

          of scanning and assessment, and were native English speakers

          with normal or corrected-to-normal hearing and vision'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: "\n3777\nBrain Structure and Function (2018) 223:3769–3786\t\n1 3\nPerformance\
    \ on the phonological factor was uniquely cor-\nrelated with a large cluster of\
    \ a number of left hemisphere \nregions: frontal pole, middle frontal gyrus (MFG),\
    \ inferior \nfrontal gyrus (IFG) (triangularis and orbitalis), frontal and \n\
    central opercular cortex, posterior insular cortex, temporal \npole, planum polare,\
    \ Heschl’s gyrus, planum temporale, \nsuperior temporal gyrus (STG), middle temporal\
    \ gyrus \n(MTG), parietal opercular cortex, and posterior supramar-\nginal gyrus\
    \ (SMG)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
