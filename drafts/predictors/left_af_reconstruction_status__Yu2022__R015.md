---
id: left_af_reconstruction_status
name: left AF reconstruction status
kind: predictor
findings:
- id: f1
  target: left_af_diffusion_indices
  target_kind: impairment
  claim: Diffusion indices (FA value and fiber number) of the anterior and long segments
    (LSAF) of the left AF were significantly higher in patients with completely reconstructed
    AF (group A) compared to those with non-reconstructed (group B) or partially reconstructed
    (group C) AF.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 26
    population: Right-handed Chinese speakers with aphasia secondary to first-ever
      left hemispheric stroke
    phase: not_reported
    time_post_onset: Mean time post-stroke 39.46 days (SD 32.02)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - High co-occurring injury rate and heterogeneity of ASAF and LSAF in the partially
    reconstructed group (group C)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Classification of patients into three groups based
    on the reconstruction of the left arcuate fasciculus (AF) using deterministic
    fiber-tracking (FACT algorithm) with three ROIs: completely reconstructed (group
    A), non-reconstructed (group B), and partially reconstructed (group C). Diffusion
    indices on the PSAF in group A and group C were significantly higher than those
    in group B; No significant difference in the anterior and LSAF was found between
    group B and group C. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P1-S1-C9, two-model agreement,
    human verification pending): . All patients were classified into three groups
    according to the reconstruction of the left AF: completely reconstructed (group
    A, 8 cases), non-reconstructed (group B, 6 cases), and partially reconstructed
    (group C, 12 cases) Original text-layer quotation is preserved below. PDF image
    reading (P2-S2-C9, two-model agreement, human verification pending): Subjects

    Twenty-six right-handed patients (20 males and 6 females, mean age = 54.50 years,
    SD = 11.30, mean duration of education = 10.92 years, SD = 3.19, mean time post-stroke
    = 39.46 days, SD = 32.02) with various types of aphasia secondary to left hemispheric
    strokes were recruited in the department of rehabilitation medicine of our hospital
    between March 2020 and May 2022 (See Table 1) Original text-layer quotation is
    preserved below.'
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
    - proposed_concept:left_af_diffusion_indices
  citation: '@Yu2022'
  source_passages:
  - section: Original source P1-S1-C9
    page: 1
    quote: 'All patients were classiﬁed into three groups according to the

      reconstruction of the left AF: completely reconstructed (group A, 8 cases),
      non-reconstructed (group B,

      6 cases), and partially reconstructed (group C, 12 cases).'
    supports: sample
  - section: Original source P2-S2-C9
    page: 2
    quote: 'Subjects

      Twenty-six right-handed patients (20 males and 6 females, mean age = 54.50 years,
      SD = 11.30,

      mean duration of education = 10.92 years, SD = 3.19, mean time post-stroke =
      39.46 days,

      SD = 32.02) with various types of aphasia secondary to left hemispheric strokes
      were

      recruited in the department of rehabilitation medicine of our hospital between
      March 2020

      and May 2022 (See Table 1).'
    supports: sample
  - section: Original source P5-S1-C3
    page: 5
    quote: 'A three-ROIs approach was applied to accomplish the virtual dissection
      of

      the bilateral AFs based on a deterministic ﬁber-tracking algorithm (ﬁber assignment
      by

      continuous tracking—FACT algorithm): a frontal ROI (ROI 1, the green 2D disk)
      was placed

      on the coronal slice at the entrance to the frontal lobe (anterior to the central
      sulcus), a

      parietal ROI (ROI 2, the red 3D sphere) was placed tangent to the inferior parietal
      cortex,

      and a temporal ROI (ROI 3, the blue 3D sphere) was placed on the axial slice
      at the entrance

      to the temporal lobe (below the Sylvian ﬁssure) [15,24] (see Figure 1).'
    supports: method
  - section: Original source P11-S1-C11
    page: 11
    quote: 'Post-hoc tests revealed that the diffusion

      indices on the anterior and LSAF in group A were signiﬁcantly higher than those
      in group

      B and group C and that the diffusion indices on the PSAF in group A and group
      C were

      signiﬁcantly higher than those in group B.'
    supports: claim
  - section: Original source P11-S1-C12
    page: 11
    quote: 'Neither signiﬁcance in the PSAF was found

      between group A and group C, nor in the anterior and LSAF between group B and
      group C.'
    supports: claim
  - section: Original source P16-S1-C4
    page: 16
    quote: 'First, the number of patients

      was somewhat limited, especially considering the high co-occurring injury rate
      and het-

      erogeneity of the ASAF and LSAF in patients in group C.'
    supports: limitation
predictor_type: imaging_metric
short_definition: 'Classification of patients into three groups based on the reconstruction
  of the left arcuate fasciculus (AF) using deterministic fiber-tracking (FACT algorithm)
  with three ROIs: completely reconstructed (group A), non-reconstructed (group B),
  and partially reconstructed (group C).'
assessment:
- DTI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yu2022
  proposal_id: R015
  review_status_sha256: 418a7dec67278575a2093eaeeb8737c887f46fa9cd652895cd2d415c14354abb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
        A/passages.json: a3ebde29f9200ec8f74e7a3b2ff1addcdc56ebe9f14e64da0c30f2063d070275
        A/raw.json: 83fc57dfc20cfc55d1be51bac24bd5ed3ce31277c797528bd2bacb949b073390
        A/source-units.json: ec334959493b634d5e1cb8a2b45a71c496c33e59322aba2934d8fb4464281544
        A/full-source-units.json: ca7e6e32fb7861958d3f52df26a3aaef163cc4c76e32aa4aee3f456ae47a6644
        A/meta.json: 47bc7a58601003bed11b75dc9043c11358a242fbdac47619ce139a221bc6a6c2
        A/table-images/TABLE-7-page-12-1.png: e5f82fceec3a3279574172b040b4c570d040c1112d97518e7dff43eb4028db6f
        A/table-images/TABLE-1-page-3-1.png: 8dcb5b8d70fcf06117362ecd4a392e2a8dcc1dfd0abfe478b23f3a8b6a18cd36
        A/table-images/TABLE-4-page-10-1.png: 3a470fd2fdc63f7c9a01914d08b1257fddecbf1139a92e02a762e331c3dc2c03
        A/table-images/page-12.png: 87670e1e2a5996aa3b74cb16c3fd725121efbb125231819f8dc1f8a46b2c6986
        A/table-images/page-10.png: 5b8f166a976f65458e8afc22bbc9d054428fb76dad811dd03306b89ba8064047
        A/table-images/page-11.png: 65ba65eba1edcccdeb2af5b2fed96237e7033c059d28d08a5225d8d9fb0d6f7a
        A/table-images/TABLE-2-page-8-1.png: a29b3b8529715c8ec71c91b0c87a6c439ad29c3803b37a54b4b9f728c9ad2c59
        A/table-images/page-3.png: 35d31a14332e1f2b3cc8eb4634390ee207595c324b569a55735e6888e048573a
        A/table-images/TABLE-3-page-8-2.png: a29b3b8529715c8ec71c91b0c87a6c439ad29c3803b37a54b4b9f728c9ad2c59
        A/table-images/page-8.png: 701d943f4a770c226785c7c4a8ba01f1246ffd93c5fe73266a8a874dee60a471
        A/table-images/TABLE-6-page-11-1.png: 06a960caf800cf7ecc0800eed84f635389a64107ff5bc650090ebd9c51e4bab3
        A/table-images/manifest.json: 36a93fce7d4ffd1d02054271260dc4bc6ffd9501acc21961c5cc929222e20efb
        A/table-images/TABLE-5-page-10-2.png: 60ac67d1b1a32483874bd96c0b85e3dbf2de8fbe11530dda5785229216c72dcf
        A/clauses/window-03/raw.json: 2783da2ce97d71b0d012118bd3dfa0eb6998a6028d99ccacd5e38667c188d090
        A/clauses/window-03/prompt.txt: bb62db1fa2e02950e7c4a8f3ab579dae16be6ccc46668c697ebd21e8a03b1e9a
        A/clauses/window-03/meta.json: 5a319fb2d4d420232c6caa5074785e395b2723e6a74bc6aaeaf2b13ec49a65be
        A/clauses/window-04/raw.json: ac0c8f4fbeeb034bdef9f2413037a0017c895a08c67ac242e9cac60f9aad4215
        A/clauses/window-04/prompt.txt: e30c5f2b9da5b8b2863974f83b6915d48f66dc8e68f21e7e7f779382a51c9908
        A/clauses/window-04/meta.json: 872a2289e916fea64e4efde3cc1df001e25eff12fe63419546514401287f01ad
        A/clauses/window-05/raw.json: 3bfe19ce114d7d5c37606bc6b59555327fc1bad4ac69d7930e2dc9d920d39b7d
        A/clauses/window-05/prompt.txt: b6ee58f4c37db41c5a43809c5e428f1b0f6cf1d095d4f5ebe5642cd488ddd98c
        A/clauses/window-05/meta.json: fb4bd8bdef47f534b8960fbfb51384940b9423d5bf51f04e5d18e9642a9b74d0
        A/clauses/window-02/raw.json: 767a79a78ecf7acb98bc279db0888ac45c9438e98e0138236785aa4a561a9d0e
        A/clauses/window-02/prompt.txt: 40e610fb8201ef9189bb5853a95ac1c85886c018366504090d28028ab9dc24e1
        A/clauses/window-02/meta.json: 8693bc5543ed9c4d67ae45c4e0f9be23e8a0db8b23830258b89f4f26c7be9a51
        A/clauses/window-09/raw.json: d1acec1c5d0f39cdcfb218e2277d0c97a82333b842cacfd75f46d5765ec715a1
        A/clauses/window-09/prompt.txt: 308847acbecf86f6a4f7f238a260f4330d51f14e52644d23f1489d0fc5c34ed1
        A/clauses/window-09/meta.json: 668444b8d1def71a6ae503c643689804c9661194bfb11f62c841488a49f18777
        A/clauses/window-07/raw.json: 9fc3d619958fe3e7f919e5caf90a553940c59d86fad8ea39fbd5c2677fa83b32
        A/clauses/window-07/prompt.txt: 76b2749b4d967944ae155aa38e4d933ac488d9db726f5bdfb94e0d0a446b5cfe
        A/clauses/window-07/meta.json: 742adcfa6839c665f5a4c993ed951fdb102154ad67ec95a9f567ebd4eecf2a89
        A/clauses/window-01/raw.json: e7bd8d02ba17100eca39aa3e72e4a10bd77e6e4630d3443d6d845e062c3c9f6d
        A/clauses/window-01/prompt.txt: c6669a8568102af41d3db7d9e924d6c5cdc785198c6f0cfbdf69b6cb26721abc
        A/clauses/window-01/meta.json: e6306bde8f83f080adc768fa4fc737254dab47eb1980cfe2863bb28eb5fdcb62
        A/clauses/window-06/raw.json: 36141b48d0447ba05f916e57a2009c5a10fe695f1a780a830e5c77383bf1a06b
        A/clauses/window-06/prompt.txt: 6b80bc94f2cb07b9c37bba463abcf04384d592e2a28d8408106e61ca3a43c30d
        A/clauses/window-06/meta.json: dcfd9f354afee60db9b5be09ccdf1743c20e9d7d1733cee6efeb1998c5ecf9cf
        A/clauses/window-08/raw.json: 54676f5568444e5dcb727287e3263efdfbfe4b04ee490da99b571a77ad7e98d1
        A/clauses/window-08/prompt.txt: 175f78c2533777da5306099aa6e3bd570cf6e17bd0a4923cf81f3dd19ea42cdd
        A/clauses/window-08/meta.json: a8bf605b1cb67fe79a0c5fd58713919c9f75ddb1b501223e219bbaa8cbbbc0aa
        A/tables/TABLE-6-page-11-6/raw.json: e912c529174a48fac64fd002b62672cc90167304697a62d5fd74332b0836f91d
        A/tables/TABLE-6-page-11-6/prompt.txt: b47988a7fde5c780e91b7e0d116266cbf68d2158c256ddda6a40d6a269b16763
        A/tables/TABLE-6-page-11-6/meta.json: 0247d8cf6c19808836e2162c494c2b758c6d0fca1ee7448860058f32ea2bd18d
        A/tables/TABLE-7-page-12-7/raw.json: fd0d1a74c900ac1bc976df9e19207ef186c165f36a5bf16a1630fe10a233ac6c
        A/tables/TABLE-7-page-12-7/prompt.txt: 163334b6d91ca511e272895a4ce5611119ca844b8ee81cddc2c63e51fd4038f7
        A/tables/TABLE-7-page-12-7/meta.json: 3faff6bf201f0f2758887581a3bb620885b67e22bba93bf6eb61bd9c65a4a72f
        A/tables/TABLE-2-page-8-2/raw.json: a2d8e1538f2b0716a0c9a2f1a98cf7f9839d8b66f634c84e648b33e73a476e1c
        A/tables/TABLE-2-page-8-2/prompt.txt: 608984c4f2c0683e14f0011bbe4f01f3913c1303b9bbac3fbe2b43ac7ba35686
        A/tables/TABLE-2-page-8-2/meta.json: 13fcd16ea8ef60b0a34556537f6d78750d9c06d137681be7a1ccad09a874805c
        A/tables/TABLE-3-page-8-3/raw.json: 41aff600cf032e50185e5e0d1a134501ca273e1839d62647502853dac7f5d84f
        A/tables/TABLE-3-page-8-3/prompt.txt: d1aedad05c0a902b7f886e1d2fa0b3af0aeb7c6ba3ceda363128e00cef92a018
        A/tables/TABLE-3-page-8-3/meta.json: dfe46e9105981c00450fff670c87d2a6af635c007feecc3c2ee9b1afea01de22
        A/tables/TABLE-1-page-3-1/raw.json: 481493200c6299521269abc0444af7456cfc1d7ebde72fa2fc9fe1a2f82123da
        A/tables/TABLE-1-page-3-1/prompt.txt: 5f328bddf40c3f1e21853b819fd91805a342ee0fbb5fe4d01054910c97b693d9
        A/tables/TABLE-1-page-3-1/meta.json: a31e72857f0639ba11149b62b929d5aa403a2f71299265d331521e800e6f7cea
        A/tables/TABLE-5-page-10-5/raw.json: f0c92a34f1c443cd9e6e3541c4522c8265c7598cbab518f4405817dc224e984a
        A/tables/TABLE-5-page-10-5/prompt.txt: 06a283e8a3eb9152f2985799eb324cde13b59045e8f1634baed1fa5f094ff026
        A/tables/TABLE-5-page-10-5/meta.json: 2e25a54eb62c665593f1f8106e29efd0111e987f1e9a450d6076edfc006241ee
        A/tables/TABLE-4-page-10-4/raw.json: 39541c82902ee788abb29adb845f924466883be32a50b4f7eab3027b3c805655
        A/tables/TABLE-4-page-10-4/prompt.txt: ae8c4944e8211562e90bf86c829ec1511ed0e4a36c20776a65017e58e65f3b40
        A/tables/TABLE-4-page-10-4/meta.json: f4cdb5dc9ac64ed95169ed63219a69ae970e2df7577bde629c5aa0c7581ba39b
        B/passages.json: a3ebde29f9200ec8f74e7a3b2ff1addcdc56ebe9f14e64da0c30f2063d070275
        B/raw.json: cadb22ef6500996b5acfc76e69cabaddbdc045cf4f022a2ebb44dc478d6f10a8
        B/source-units.json: ec334959493b634d5e1cb8a2b45a71c496c33e59322aba2934d8fb4464281544
        B/full-source-units.json: ca7e6e32fb7861958d3f52df26a3aaef163cc4c76e32aa4aee3f456ae47a6644
        B/meta.json: 4c0d71e497728f46ece331483d366f6bc2ffb32fedc5cb8f28782007e98c0271
        B/table-images/TABLE-7-page-12-1.png: e5f82fceec3a3279574172b040b4c570d040c1112d97518e7dff43eb4028db6f
        B/table-images/TABLE-1-page-3-1.png: 8dcb5b8d70fcf06117362ecd4a392e2a8dcc1dfd0abfe478b23f3a8b6a18cd36
        B/table-images/TABLE-4-page-10-1.png: 3a470fd2fdc63f7c9a01914d08b1257fddecbf1139a92e02a762e331c3dc2c03
        B/table-images/page-12.png: 87670e1e2a5996aa3b74cb16c3fd725121efbb125231819f8dc1f8a46b2c6986
        B/table-images/page-10.png: 5b8f166a976f65458e8afc22bbc9d054428fb76dad811dd03306b89ba8064047
        B/table-images/page-11.png: 65ba65eba1edcccdeb2af5b2fed96237e7033c059d28d08a5225d8d9fb0d6f7a
        B/table-images/TABLE-2-page-8-1.png: a29b3b8529715c8ec71c91b0c87a6c439ad29c3803b37a54b4b9f728c9ad2c59
        B/table-images/page-3.png: 35d31a14332e1f2b3cc8eb4634390ee207595c324b569a55735e6888e048573a
        B/table-images/TABLE-3-page-8-2.png: a29b3b8529715c8ec71c91b0c87a6c439ad29c3803b37a54b4b9f728c9ad2c59
        B/table-images/page-8.png: 701d943f4a770c226785c7c4a8ba01f1246ffd93c5fe73266a8a874dee60a471
        B/table-images/TABLE-6-page-11-1.png: 06a960caf800cf7ecc0800eed84f635389a64107ff5bc650090ebd9c51e4bab3
        B/table-images/manifest.json: 25c8253cf269ccba9ef1596c738e8f12569b9d6ed1311c23c6ae9184f621f54b
        B/table-images/TABLE-5-page-10-2.png: 60ac67d1b1a32483874bd96c0b85e3dbf2de8fbe11530dda5785229216c72dcf
        B/clauses/window-03/raw.json: 85cbcf6254bee9d133fe38b42a769e9295ee4fade255c19330818b7ce3f0d7ff
        B/clauses/window-03/prompt.txt: bb62db1fa2e02950e7c4a8f3ab579dae16be6ccc46668c697ebd21e8a03b1e9a
        B/clauses/window-03/meta.json: 848e6238a723d238fcfb6ad1afd86cdfb1d2c46b50a3a9d038ad1de4353bdf10
        B/clauses/window-04/raw.json: 536ec390675e34e72084ed01f5e5ab2be6b821122859ca85e9f583c5ddc27e7f
        B/clauses/window-04/prompt.txt: e30c5f2b9da5b8b2863974f83b6915d48f66dc8e68f21e7e7f779382a51c9908
        B/clauses/window-04/meta.json: b47778701f0b36d19d11231691c888ae2d38186b8a64d909f48e6df27c3aa1ab
        B/clauses/window-05/raw.json: 33393844244dea4696285721e27a4ca2c10a3f69b6df870501e840d174c7ce8f
        B/clauses/window-05/prompt.txt: b6ee58f4c37db41c5a43809c5e428f1b0f6cf1d095d4f5ebe5642cd488ddd98c
        B/clauses/window-05/meta.json: 6e766695cda614252e993632fe26f2040099c42bd287ede4a5b7020bb535f361
        B/clauses/window-02/raw.json: ccc270ca7b209564a7300b5111097a06b84ee10fb677a32d621640687e3e427b
        B/clauses/window-02/prompt.txt: 40e610fb8201ef9189bb5853a95ac1c85886c018366504090d28028ab9dc24e1
        B/clauses/window-02/meta.json: 91812d8821e7cb7a5168cd6fb5a2a5a70e00d75565c2c77fdfa51b869f03015f
        B/clauses/window-09/raw.json: 5025bbb5038622c1b0d5c5727f2fb9404706090f2964574aa31e61792cf658e9
        B/clauses/window-09/prompt.txt: 308847acbecf86f6a4f7f238a260f4330d51f14e52644d23f1489d0fc5c34ed1
        B/clauses/window-09/meta.json: 39d57f9f9cf33fcbc43850c531c3033f33731b94610a54ce1d201660afb658d8
        B/clauses/window-07/raw.json: 38f9edade1f61d3e834999630c2a49cf7e39476a8121777a2055cc2d679cfd71
        B/clauses/window-07/prompt.txt: 76b2749b4d967944ae155aa38e4d933ac488d9db726f5bdfb94e0d0a446b5cfe
        B/clauses/window-07/meta.json: e753b0a173516f6628daaa974623b5a5f341c64d47d477f0ec9565072d6a6897
        B/clauses/window-01/raw.json: de7c65746a9e3a25cc266c7d9c236196565dd043835ecf85e71457e1351d0984
        B/clauses/window-01/prompt.txt: c6669a8568102af41d3db7d9e924d6c5cdc785198c6f0cfbdf69b6cb26721abc
        B/clauses/window-01/meta.json: 9399185235956bbedd2ffa93c5e6148ca1fc6fce3c52645d54aa86db88b28dbc
        B/clauses/window-06/raw.json: 8a5eb13a4ece4fd35b56b8caf43a18022ff814d21efbb2c1f04b4f579761f9d7
        B/clauses/window-06/prompt.txt: 6b80bc94f2cb07b9c37bba463abcf04384d592e2a28d8408106e61ca3a43c30d
        B/clauses/window-06/meta.json: 982636b9feda7f3763e3364c80daccfb782fe17bc402e5001500cddcb46e38ae
        B/clauses/window-08/raw.json: 4297df2b6c0e803e215092113ab6cb44c24c96fcede8557e58bdc2c80be152e8
        B/clauses/window-08/prompt.txt: 175f78c2533777da5306099aa6e3bd570cf6e17bd0a4923cf81f3dd19ea42cdd
        B/clauses/window-08/meta.json: 46cd173bc3e4afc29352f823200a28823f1969a0bb05d5666655b9227214a002
        B/tables/TABLE-6-page-11-6/raw.json: e49590233aa675e96a1e519c1b0995593a85a129bccc8b83bb977589ae8f968e
        B/tables/TABLE-6-page-11-6/prompt.txt: b47988a7fde5c780e91b7e0d116266cbf68d2158c256ddda6a40d6a269b16763
        B/tables/TABLE-6-page-11-6/meta.json: a50cc6fa5e966eaafb0755ee80a5dfdbef638448b68f5e8512e7f6eda8e91843
        B/tables/TABLE-7-page-12-7/raw.json: 0873abf8509584676c19d861477fe9fc21f3a5bd2c58568acdbf975ab6edd006
        B/tables/TABLE-7-page-12-7/prompt.txt: 163334b6d91ca511e272895a4ce5611119ca844b8ee81cddc2c63e51fd4038f7
        B/tables/TABLE-7-page-12-7/meta.json: 7349f437bba4b1bf3928924dd2353ad86986cdfb7342dd38db02dab63fd3b517
        B/tables/TABLE-2-page-8-2/raw.json: 22c8f31f8301c23a88844c7a113931d4a9e7de5ced81d18fa638c0c36120bc4c
        B/tables/TABLE-2-page-8-2/prompt.txt: 608984c4f2c0683e14f0011bbe4f01f3913c1303b9bbac3fbe2b43ac7ba35686
        B/tables/TABLE-2-page-8-2/meta.json: b3a95ac8b1755c3c7d1f339fb88b736e2d938f15972e8e7e8d63816da784c743
        B/tables/TABLE-3-page-8-3/raw.json: 19d00e1e205e4715b6d4b5cd2e6d78d6a93055976e233a6e67182f9883b1144b
        B/tables/TABLE-3-page-8-3/prompt.txt: d1aedad05c0a902b7f886e1d2fa0b3af0aeb7c6ba3ceda363128e00cef92a018
        B/tables/TABLE-3-page-8-3/meta.json: 12dfbd7d7b8b975f5bd13e5908a60812e45537fe4c5d570685dc575820ed0aa5
        B/tables/TABLE-1-page-3-1/raw.json: 60550033dafab96380fed099842525d3f2fc0c938c30c3144a3258e2befd372f
        B/tables/TABLE-1-page-3-1/prompt.txt: 5f328bddf40c3f1e21853b819fd91805a342ee0fbb5fe4d01054910c97b693d9
        B/tables/TABLE-1-page-3-1/meta.json: a0be8c87e5abbb2389be473e54f84b66119d99154b895c4002e2b023720580f8
        B/tables/TABLE-5-page-10-5/raw.json: be2049dc978c743768e53c18777fae6080ee4a77a9873dff8a51eae29e3131c1
        B/tables/TABLE-5-page-10-5/prompt.txt: 06a283e8a3eb9152f2985799eb324cde13b59045e8f1634baed1fa5f094ff026
        B/tables/TABLE-5-page-10-5/meta.json: bd6952811451b2c42e989618529861fdefcc48b60480dbf24fc850f6f4763005
        B/tables/TABLE-4-page-10-4/raw.json: 217529bc1d7e129577192c3fb24da7e83b7ade0cc047523f1ad558d6a0e54d69
        B/tables/TABLE-4-page-10-4/prompt.txt: ae8c4944e8211562e90bf86c829ec1511ed0e4a36c20776a65017e58e65f3b40
        B/tables/TABLE-4-page-10-4/meta.json: 19de56082c3e31c2234ef9f202fdabac84d987298b9a7fcde66ba21b07d84bbe
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
      pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
      source_review: _compare/relationships-2026-11-16/review-current/Yu2022
      source_status_sha256: 885d1600631513e68766d9c2ed191ec371d6be96146d01de40308c11df703bdf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R015
    exposure:
      text: reconstruction of the left AF (Group A vs Group B and Group C)
    outcome:
      text: diffusion indices on the anterior and LSAF
    analysis_label: Intergroup analysis
    relation: association
    evidence_ids:
    - P11-S1-C11
    - P12-S1-C4
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
      pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
      source_review: _compare/relationships-2026-11-16/review-current/Yu2022
      source_status_sha256: 885d1600631513e68766d9c2ed191ec371d6be96146d01de40308c11df703bdf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C12
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C7
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C7
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P9-S1-C1
      - Accounting without a linked unit P9-S1-C12
      - Accounting without a linked unit P9-S1-C2
      - Accounting without a linked unit P9-S1-C3
      - Accounting without a linked unit P9-S1-C4
      - Result passage disposed without unit P9-S1-C5
      - Unaccounted source passage P9-S1-C12
      - Unaccounted source passage P9-S1-C2
      - Unaccounted source passage P9-S1-C4
      - Unaccounted source passage P9-S1-C3
      - Unresolved source passage P10-S1-C12
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Accounting without a linked unit P12-S2-C2
      - Accounting without a linked unit P12-S2-C7
      - Unaccounted source passage P12-S2-C7
      - Unaccounted source passage P12-S2-C2
      - Result passage disposed without unit P13-S1-C7
      - Accounting without a linked unit P13-S2-C10
      - Unaccounted source passage P13-S2-C10
      - Result passage disposed without unit P13-S3-C4
      - Unresolved source passage P13-S3-C5
      - Unresolved source passage P14-S1-C11
      - Result passage disposed without unit P14-S1-C8
      - Result passage disposed without unit P14-S2-C14
      - Accounting without a linked unit P15-S1-C2
      - Unaccounted source passage P15-S1-C2
      unattached_null_or_qualifier_ids:
      - P7-S2-C3
      - P11-S1-C5
      - P13-S1-C7
      - P13-S2-C10
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 196
      unselected_timing_passages:
      - P2-S2-C10
      - P2-S3-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P16-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids:
      - P2-S3-C1
      - P2-S3-C2
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-8-2
      - TABLE-3-page-8-3
      - TABLE-4-page-10-4
      - TABLE-5-page-10-5
      - TABLE-6-page-11-6
      - TABLE-7-page-12-7
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-8-2
      - TABLE-3-page-8-3
      - TABLE-4-page-10-4
      - TABLE-5-page-10-5
      - TABLE-6-page-11-6
      - TABLE-7-page-12-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P6-S1
        - P7-S2
        - P8-S1
        - P9-S1
        - P10-S1
        - P11-S1
        - P13-S3
        - P14-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
      source_review: _compare/relationships-2026-11-16/review-current/Yu2022
      source_status_sha256: 885d1600631513e68766d9c2ed191ec371d6be96146d01de40308c11df703bdf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes: []
      reason: Abstract restatement of results found in P7 and P8.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Abstract restatement of partial correlation results.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      - 13
      - 14
      reason: Abstract restatement of intergroup differences.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Abstract restatement of null result for ASAF.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of fiber tracking in Group C.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about data presentation.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Classification of aphasia types.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of aphasia severity range.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for demographic variables.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Direct result of lesion volume and load correlations.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Direct result of AF segment correlations.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Direct result of partial correlation analysis.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Direct null result for ASAF.
    - source_id: P7-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to tables.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Intergroup difference in aphasia severity.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for other demographic metrics.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive range of lesion volumes.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean lesion volumes per group.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive total volume of cortical language areas.
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive range/mean of lesion load.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory phrase for lesion volume data.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion load per group.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Significant difference in lesion load among groups.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Post-hoc result for lesion load (Group A vs B).
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for lesion volume among groups.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 4b.
    - source_id: P9-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Intergroup differences in language subsets.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Post-hoc results for language subsets.
    - source_id: P9-S1-C14
      disposition: represented
      result_indexes:
      - 12
      reason: Null result for Group A vs Group C language subsets.
    - source_id: P9-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to tables/figures.
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient distribution across groups.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Detailed reconstruction status in Group C.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of non-reconstruction rates.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of damage in Group C.
    - source_id: P11-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P11-S1-C10
      disposition: represented
      result_indexes:
      - 13
      reason: Intergroup differences in FA and fiber number.
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Post-hoc results for diffusion indices.
    - source_id: P11-S1-C12
      disposition: represented
      result_indexes:
      - 16
      - 17
      reason: Null post-hoc results for diffusion indices.
    - source_id: P11-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to tables.
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 15
      reason: Discussion summary of PSAF and lesion load importance.
    - source_id: P12-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Discussion of lesion load's linguistic role.
    - source_id: P12-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Discussion of cortical language area influence.
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      reason: Discussion of intergroup language differences vs lesion load.
    - source_id: P13-S2-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Discussion of null ASAF relationship.
    - source_id: P14-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Discussion of LSAF intergroup differences.
    - source_id: P15-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Discussion of PSAF relationship to comprehension/repetition.
    - source_id: P15-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Discussion of PSAF relationship to comprehension/repetition.
    - source_id: P15-S3-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Discussion of null PSAF-naming intergroup difference.
    - source_id: P15-S3-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Discussion of PSAF/LSAF partial correlation with naming.
    - source_id: P16-S1-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Conclusion regarding PSAF and comprehension/repetition.
    unresolved_coverage:
    - source_id: P1-S2-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P15-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P6-S1-C8
    - P7-S1-C9
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C3
    - P7-S2-C10
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C8
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C15
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C13
    - P12-S1-C6
    - P12-S2-C2
    - P12-S2-C7
    - P13-S1-C6
    - P13-S1-C7
    - P13-S2-C10
    - P13-S3-C4
    - P14-S1-C8
    - P14-S2-C14
    - P15-S1-C2
    - P15-S2-C8
    - P15-S2-C10
    - P15-S3-C3
    - P16-S1-C2
    - P16-S1-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-8-2
    - TABLE-3-page-8-3
    - TABLE-4-page-10-4
    - TABLE-5-page-10-5
    - TABLE-6-page-11-6
    - TABLE-7-page-12-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P6-S1-C2
      recruited_sample:
      - P2-S2-C9
      eligibility:
      - P2-S3-C1
      - P2-S3-C2
      imaging_provenance:
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S2-C6
      - P5-S1-C3
      imaging_timing:
      - P2-S2-C9
      outcome_timing:
      - P2-S2-C9
      outcome_definition:
      - P4-S1-C5
      - P4-S1-C6
      validation: []
      analysis_restrictions:
      - P7-S1-C5
      - P13-S1-C3
      - P13-S3-C4
      - P14-S2-C14
      - P15-S3-C4
      dependent_variable_statement:
      - P7-S1-C14
      limitations:
      - P16-S1-C4
      - P16-S1-C5
      - P16-S1-C6
      - P16-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S2-C4
      - P7-S2-C7
      - P8-S1-C2
      - P8-S1-C7
      explicitly_not_adjusted:
      - P13-S1-C3
      descriptive_personal_factors:
      - P2-S2-C9
      - P3-S1-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P16-S1-C4
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
      pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
      review_sha256: 418a7dec67278575a2093eaeeb8737c887f46fa9cd652895cd2d415c14354abb
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
      - P11-S1-C11
      source_result: Intergroup analysis of diffusion indices (FA and fiber number)
        in the left AF segments. Significant differences were found among groups for
        all segments. Specifically, diffusion indices on the anterior and LSAF in
        group A were significantly higher than in group B and group C. No significant
        difference was found between group B and group C for the anterior and LSAF
        segments.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the intergroup comparison of diffusion
            indices based on left AF reconstruction status (Groups A, B, C). The source
            P11-S1-C11 explicitly describes this analysis and its results.
          source_ids:
          - P11-S1-C11
          - P11-S1-C9
        direction:
          answer: fits
          reason: 'The claim states that diffusion indices in Group A were significantly
            higher than in Groups B and C. This matches the source text in P11-S1-C11:
            ''diffusion indices on the anterior and LSAF in group A were significantly
            higher than those in group B and group C''.'
          source_ids:
          - P11-S1-C11
        construct:
          answer: fits
          reason: The exposure is the reconstruction status of the left AF (categorical
            grouping). The outcome is the diffusion indices (FA and fiber number)
            of the specific segments (anterior/ASAF and LSAF). The measurement is
            patient-specific diffusion metrics derived from DTI tractography, not
            template overlap. The proposed core correctly identifies the exposure,
            outcome, and measurement type.
          source_ids:
          - P11-S1-C11
          - P6-S1-C3
          - P5-S1-C5
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that no significant
            difference was found between Group B and Group C for the anterior and
            LSAF segments, which is explicitly stated in P11-S1-C12. It also notes
            the PSAF findings as a separate qualification, which is accurate to the
            source.
          source_ids:
          - P11-S1-C12
          - P11-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The core includes limitations regarding sample size and heterogeneity
            in Group C (P16-S1-C4). It does not omit material caveats that would change
            the interpretation of the specific intergroup difference claim. The distinction
            between 'anterior' (ASAF) and 'LSAF' is preserved.
          source_ids:
          - P16-S1-C4
          - P11-S1-C5
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
      id: R015
      exposure:
        text: reconstruction of the left AF (Group A vs Group B and Group C)
      outcome:
        text: diffusion indices on the anterior and LSAF
      analysis_label: Intergroup analysis
      relation: association
      evidence_ids:
      - P11-S1-C11
      - P12-S1-C4
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
        pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
        source_review: _compare/relationships-2026-11-16/review-current/Yu2022
        source_status_sha256: 885d1600631513e68766d9c2ed191ec371d6be96146d01de40308c11df703bdf
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: afeeb902d7ef64278b3f1d004b2674ccc4902ac1b1b4165da0a5b86dd73bca0c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C9
          page: 1
          text_layer_sha256: afeeb902d7ef64278b3f1d004b2674ccc4902ac1b1b4165da0a5b86dd73bca0c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients were classiﬁed into three groups according to
          the

          reconstruction of the left AF: completely reconstructed (group A, 8 cases),
          non-reconstructed (group B,

          6 cases), and partially reconstructed (group C, 12 cases).'
        anchor_text: 'All patients were classiﬁed into three groups according to the

          reconstruction of the left AF: completely reconstructed (group A, 8 cases),
          non-reconstructed (group B,

          6 cases), and partially reconstructed (group C, 12 cases).'
        excluded_fragments: []
        image_sha256: 5ae107f95cf708256efc0e5a8e9040fdf88271e12f5f374cbd1550419f065bf1
        transcription: '. All patients were classified into three groups according
          to the reconstruction of the left AF: completely reconstructed (group A,
          8 cases), non-reconstructed (group B, 6 cases), and partially reconstructed
          (group C, 12 cases)'
      P2-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bafbfa255008564d612a84eb59f53dfcd1de32ae706f546d6165e177286d97f0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fd97d36e43e4acb8e9056475dc8f16cf256cecc36b70596a607fe7d1f309fedf
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C9
          page: 2
          text_layer_sha256: fd97d36e43e4acb8e9056475dc8f16cf256cecc36b70596a607fe7d1f309fedf
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Subjects

          Twenty-six right-handed patients (20 males and 6 females, mean age = 54.50
          years, SD = 11.30,

          mean duration of education = 10.92 years, SD = 3.19, mean time post-stroke
          = 39.46 days,

          SD = 32.02) with various types of aphasia secondary to left hemispheric
          strokes were

          recruited in the department of rehabilitation medicine of our hospital between
          March 2020

          and May 2022 (See Table 1).'
        anchor_text: 'Subjects

          Twenty-six right-handed patients (20 males and 6 females, mean age = 54.50
          years, SD = 11.30,

          mean duration of education = 10.92 years, SD = 3.19, mean time post-stroke
          = 39.46 days,

          SD = 32.02) with various types of aphasia secondary to left hemispheric
          strokes were

          recruited in the department of rehabilitation medicine of our hospital between
          March 2020

          and May 2022 (See Table 1).'
        excluded_fragments: []
        image_sha256: bab58dd96a9e463372d59104649cd50a25cb5dd93939bdc6f1349b63fa6d1c3c
        transcription: 'Subjects

          Twenty-six right-handed patients (20 males and 6 females, mean age = 54.50
          years, SD = 11.30, mean duration of education = 10.92 years, SD = 3.19,
          mean time post-stroke = 39.46 days, SD = 32.02) with various types of aphasia
          secondary to left hemispheric strokes were recruited in the department of
          rehabilitation medicine of our hospital between March 2020 and May 2022
          (See Table 1)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'All patients were classiﬁed into three groups according to the

    reconstruction of the left AF: completely reconstructed (group A, 8 cases), non-reconstructed
    (group B,

    6 cases), and partially reconstructed (group C, 12 cases).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
