---
id: right_frontal_operculum
name: right frontal operculum cluster
kind: network
findings:
- id: f1
  outcome_measurement:
    status: identified
    instruments:
    - name: Aprosodia Battery
    note: Task-specific production, repetition or comprehension conditions remain in the claim and source
      passages; this is not approval.
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: spontaneous_affective_prosody
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  target: spontaneous_affective_prosody
  target_kind: impairment
  claim: Injury to the right frontal operculum (specifically combining 'Large' and
    'Small' lesion categories) is associated with deficits in spontaneous affective
    prosody, whereas 'Very Small' lesions of the right frontal operculum were not
    associated with these deficits.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 21
    population: Individuals with right hemisphere brain damage (RBD) due to focal
      ischemic infarctions predominantly involving cortex and adjacent white matter.
    phase: not_reported
    time_post_onset: Assessment completed 3 to 8 weeks post-stroke; MRI scans obtained
      2 to 6 weeks post-stroke.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The lack of deficit in 'Very Small' lesions may be due to insufficient cortical
    destruction or rapid recovery not captured by the 3-to-8-week assessment window
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a standard right hemisphere
    template, categorized by size as ''Large'', ''Small'', or ''Very Small'' frontal
    operculum lesions. The association was most robust when combining ''Large'' and
    ''Small'' frontal operculum lesions; Right frontal operculum lesions often, but
    not always, involve the anterior insula. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S3-C4, two-model
    agreement, human verification pending): . The primary patient group consisted
    of 21 individuals with RBD due to focal ischemic infarctions limited to the right
    hemisphere that predominantly involved cortex and adjacent white matter Original
    text-layer quotation is preserved below. PDF image reading (P4-S1-C4, two-model
    agreement, human verification pending): Testing of the brain-damaged patients
    was completed

    within three to eight weeks post-stroke to exclude any acute

    and potentially reversible pathophysiologic deficits, such as

    diaschisis, ischemic penumbra or edema (Croquelois, Win-

    termatk, Reichart, Meuli, & Bogousslavsky, 2003; Nguyen

    & Botez, 1998; Shaw, Alvord, & Berry, 1959; approxi-

    mately 1–3 weeks post-stroke), and before the occurrence

    of long-term improvement from spontaneous recovery

    due to neural reorganization (Kertesz, 1979, chap. 15;

    Rosen et al., 2005; 3–5 months post-stroke and beyond) Original text-layer quotation
    is preserved below. PDF image reading (P4-S1-C5, two-model agreement, human verification
    pending): MRI scans were obtained between 2 and 6 weeks post-

    stroke Original text-layer quotation is preserved below.'
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
    - proposed_concept:spontaneous_affective_prosody
  citation: '@Ross2008'
  source_passages:
  - section: Original source P9-S1-C4
    page: 9
    quote: 'Spontaneous aﬀective prosody

      Data in Table 8 indicates that ‘Very Small Frontal Oper-

      culum’ lesions (Fig. 3) were not associated with deﬁcits of

      Spontaneous aﬀective prosody because none of the four

      patients evinced Spontaneous deﬁcits.'
    supports: claim
  - section: Original source P9-S1-C6
    page: 9
    quote: 'Of the remaining cortical distributions

      only patients with ‘Large Frontal Operculum’ and ‘Anterior

      Insula’ lesions showed signiﬁcant associations with Sponta-

      neous deﬁcits (p0s 6 .002).'
    supports: claim
  - section: Original source P9-S1-C9
    page: 9
    quote: 'However, by combining

      patients with ‘Large Frontal Operculum’ and ‘Small frontal

      Operculum’ lesions using an ‘‘or’’ function (‘Large Frontal

      Operculum or Small Frontal Operculum’; Table 8), all 21

      patients in our cohort were correctly classiﬁed regarding

      their

      performance

      on

      Spontaneous

      aﬀective

      prosody

      (p = .000003).'
    supports: claim
  - section: Original source P9-S2-C1
    page: 9
    quote: 'lesions, injury to the right frontal operculum that most often,

      but not always, involves the anterior insula produces acute

      deﬁcits in Spontaneous aﬀective prosody with extraordinary

      robustness (Figs. 4 and 5).

      3.4.2.'
    supports: claim
  - section: Original source P3-S3-C4
    page: 3
    quote: 'The primary patient group con-

      sisted of 21 individuals with RBD due to focal ischemic

      infarctions limited to the right hemisphere that predomi-

      nantly involved cortex and adjacent white matter.'
    supports: sample
  - section: Original source P4-S1-C4
    page: 4
    quote: 'Testing of the brain-damaged patients was completed

      within three to eight weeks post-stroke to exclude any acute

      and potentially reversible pathophysiologic deﬁcits, such as

      diaschisis, ischemic penumbra or edema (Croquelois, Win-

      termatk, Reichart, Meuli, & Bogousslavsky, 2003; Nguyen

      & Botez, 1998; Shaw, Alvord, & Berry, 1959; approxi-

      mately 1–3 weeks post-stroke), and before the occurrence

      of long-term improvement from spontaneous recovery

      due to neural reorganization (Kertesz, 1979, chap. 15;

      Rosen et al., 2005; 3–5 months post-stroke and beyond).'
    supports: method
  - section: Original source P4-S1-C5
    page: 4
    quote: 'MRI scans were obtained between 2 and 6 weeks post-

      stroke.'
    supports: method
  - section: Original source P5-S2-C9
    page: 5
    quote: 'Template mapping and categorization of RBD and LBD

      lesions for functional–anatomic correlations

      All ischemic infarctions were mapped onto a standard

      lateral and, if needed, medial right hemisphere template

      using a projection technique that isomorphically adjusts

      for normal variations in brain width, height and depth

      (Ross et al., 1997).'
    supports: method
  - section: Original source P9-S2-C4
    page: 9
    quote: 'This may be due to either the lesion not destroy-

      ing enough cortex or, possibly, rapid recovery of function

      that was not captured by our formal examination because

      patients were assessed 3 to 8 weeks post-stroke.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Ross2008
  proposal_id: R007
  review_status_sha256: 6c9bbbabb5eca56ccdf57dea1d621656c8b7d0073cebfa791f5590ca4bdfe1ff
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
        A/passages.json: ab782e9157cf800893d7c110cee870a76ed812a06ec0a6bf074c95b476bfbd75
        A/raw.json: 0f49f112fc77fa443b06973443570e37f55919179026d13cfa469c0ddc44b2bb
        A/source-units.json: 0f1f0ae86406027dc526f99c9ad81e389adf095a9f98ff0afa95f33420eb3d6e
        A/full-source-units.json: a61e92ad051960b9d90486ab070c14d1d5da4a7272066a0ca26d5d194e7f98b8
        A/meta.json: 573699e2b13e2ad217de9a12184d4b827f33aa89097933aa0ca49bcee4524128
        A/table-images/page-15.png: 1d552aa9be6bc3922b4e49f99a2fb606b4dadaefbab968cbcb0fbf09ce4d6618
        A/table-images/page-12.png: 5fff0e8d46fc518d68e6de24679c0138e06939a76296b05bd43cc2a6a9445933
        A/table-images/TABLE-11-page-15-1.png: 1fa94c1ee0b75e06ee995056a96644aecb8fa8a22f4a3d24096351e1af84a8ac
        A/table-images/page-11.png: 2114e55474caa314b195cf7677d4205e55999adfe9b73f7fa1b71631b53d66ee
        A/table-images/TABLE-9-page-11-1.png: 3ad146f81cc0d2129f777b659b1959c6d98ea55e5afc4e5433384629e5cbed69
        A/table-images/TABLE-8-page-9-1.png: 788b7af958d53275431ba2ea89bcaa73101a99254249d6e638d2ab07694d46e7
        A/table-images/page-6.png: 2713ad278e20f2b0ecfc412d0d94665f487a7dda614b4d876b75618d777e3744
        A/table-images/page-7.png: bba9d6ed0d01c3d98b5646bee62f2c28419dd8ff4464c8bd8c73f51d834d4ddd
        A/table-images/TABLE-1-page-4-2.png: a32aff1d86525372d8b5b6c28adc4d98ec0653b524bd76290c4a499c53b98452
        A/table-images/page-5.png: 19958d0b47e37d0f39716383b97d8df5977fdf895711ae675d0d7b2b48d9fc03
        A/table-images/page-4.png: 8536947c7e73258fcdc4fae4563a1632a2263f81b7d4a55884d774a844c1ff2f
        A/table-images/TABLE-1-page-4-1.png: 56911efac9d62181f727e5dd3a47543404b772704313352449b63655db24315c
        A/table-images/TABLE-6-page-8-1.png: 2dcf8544abcea2bef4a2d116ef5b6b041eeec35e55eee6ece33dc214c1c25349
        A/table-images/page-9.png: 709f09bfeac1026d9f65e595cfc4b862316927247ab6eb9b5f8776f17603e4d9
        A/table-images/TABLE-4-page-6-1.png: aa6584f549904f704424550611bb74c52da09fa4445d9ae36eb0a67ef203f1c1
        A/table-images/page-8.png: 1c89aa03c9a1402a73beab7e0866017a882df8fa93bb50d2617c661904bb2e41
        A/table-images/TABLE-10-page-12-1.png: 256a6be4c793399749e37e568efa4ac7063601ebe1c6f030ced0f12e5e3aadc3
        A/table-images/manifest.json: 73300e70b2cf07c1b6a18a9b3811813589c5f96fa60ae30f0b56326b5aab2d94
        A/table-images/TABLE-3-page-5-2.png: 11e6fca4ae32b00bcd5e922bb52449515635def2847671255ed71e2eb0e46ca7
        A/table-images/TABLE-2-page-5-1.png: 76578d59d7cc304fbdc133f55447a04e1d24a7330e09ca282899ad5a89bab00c
        A/table-images/TABLE-7-page-9-2.png: 9ed686e665acd3cb4a52736ccc8d298d6c80c299f90bb5e10d03ceebe1591159
        A/table-images/TABLE-5-page-7-1.png: 65fa4c48cf07dab3695dd5dd98bd57d7afa42a323e333e400f01bf9a5b7ba1b7
        A/clauses/window-11/raw.json: 23723baadcdf8f2272ef9899a51264654f5616d63a29484e7ef0ba13aae317e2
        A/clauses/window-11/prompt.txt: de6b56dc83b1f74becaf7ab2535da48f2d67d6a8a5e8e8b48f7d7f934a013911
        A/clauses/window-11/meta.json: ef91703e1b459e4d7b4df253d1e93417c96485ab81bb7f98d22b33fc405110a2
        A/clauses/window-10/raw.json: 1b663bc633dec118eccf912f715ecd1e285cf023dc1c0d2f4382d9ede88b3cbf
        A/clauses/window-10/prompt.txt: dad238c7f479f1add760fe42153a417f12ae969b3b15252f54183647772d75c8
        A/clauses/window-10/meta.json: eae95c3de1b940d43be763ad4bb043aee239dc5204e30bf460d153b7998259d5
        A/clauses/window-03/raw.json: c8a26bb5de9e66f989de920298417525509a8619b53a84e3cdd4592003ca3dda
        A/clauses/window-03/prompt.txt: f0629478437066f274db14951ae5daff6bbad3450811842103667a1f4ab7c16d
        A/clauses/window-03/meta.json: e0ef8647d3bdbe153a4758b2d7db75b3d8c48600c101494d58869fa8e1fc4669
        A/clauses/window-04/raw.json: 4a366f0ea706ec303f3f7ca9fd7a474591cf47c4c9b544c0da2b0f3dfe3a0d7d
        A/clauses/window-04/prompt.txt: 4bf4cdabc50f0e884fbf31546daa31db0ca3d43f79ddd49a9e2099f75bb223c3
        A/clauses/window-04/meta.json: 20f18f958925e19e466df658646b213567d4de047ad9c98f74210512803cbfe3
        A/clauses/window-05/raw.json: 7d1e5aad97ee7e3b465a5e0bf7d6353f7162a7407107de90d68eef94656955f7
        A/clauses/window-05/prompt.txt: be195f1fd367826e0ecd7cad9faddc3de232411c549a73cccc5a82075987c5b3
        A/clauses/window-05/meta.json: 8b4a927e1a2dd07105f5ee656047a8bc90e64a6c1e9f48794f5e1163ce6baa7d
        A/clauses/window-02/raw.json: 2383b839085e1c5d1fce23001e2ccb298002da0e90dd17ccba1eed4f8d65f1ba
        A/clauses/window-02/prompt.txt: d4412923bdacd3dbf3c6c4043b68c7ab167241702e66630940150abcdf3d7739
        A/clauses/window-02/meta.json: b986145d8e715e86ac7dfab10a268b99676bc083d211c8e6b5193c49fc42e916
        A/clauses/window-12/raw.json: c052ac1501fe2ca06a561bf81c8f1248acf14196c2eb378b3ee613ed0b5a3a52
        A/clauses/window-12/prompt.txt: e0d6cc10925ad5fb62704e68a3ace993ea10d4f6efa9d9213110038f9a0f0e07
        A/clauses/window-12/meta.json: 16e1950a95904a2844a101f3299353c6bbfff6f659e19331551372a8212037de
        A/clauses/window-13/raw.json: 527d9f8c290fad53f4c2af9ab0aa1779d099f4a7efed93963af287b0197c4d3b
        A/clauses/window-13/prompt.txt: b99ff20af964940fab8f799fbebca00711dfaedd7bee70a8eecd466031707fae
        A/clauses/window-13/meta.json: 0aa61ce1696d0c88dc1174be28aa7d1d913f7d291aab1b68a8a578bc3cdbd0ff
        A/clauses/window-14/raw.json: a26bcf0442e29a949a7fd7b79529239b4e5af1d24b3c981b27dae1ccd10d30bf
        A/clauses/window-14/prompt.txt: 338233f03bb8a77a1e5e93d85cce41c039348d4d19812afaa8ec84e2a085cda7
        A/clauses/window-14/meta.json: dce6366b752477b5b21925f062c48f512ea6015ef6a13fb65602c1c16710d375
        A/clauses/window-09/raw.json: ab4bdb21a7652d407110ab26d89ab8935e850bd3570ba3856316c85ebcf3a347
        A/clauses/window-09/prompt.txt: 483a5fc73b93be69528f1308ef871a59c89b42b19f1a915b61a758610dedd173
        A/clauses/window-09/meta.json: fda50f6afc32c8b4177b5a6487f2aecdd22d2624038172bdc08186baeed8526a
        A/clauses/window-07/raw.json: bc11c779e70c4245b885ab61d240d8f3c01ec4769f44026ff5c03c02d3236f8c
        A/clauses/window-07/prompt.txt: 85cf0ee0f835b796b85c5202d2e004f11b569dfe5e105eb217e0904f677367b2
        A/clauses/window-07/meta.json: 20f2c8753b2ece15242494689d08bd68d603034e274486cc47d952af08e3b730
        A/clauses/window-01/raw.json: cb97fc1ae27f3fc708c6f14f989db7e1b2ab4c6e0e18b1cd0be91f0bf6ef96a0
        A/clauses/window-01/prompt.txt: 4a2c1ddc82cb2a0c65fb6daa12be4aaddd96f38960996bf57c0e65d84b58df4b
        A/clauses/window-01/meta.json: 3f4c0adbf5444cd434d9560a283acbc69d820c3381fd13986b809c382d6ed308
        A/clauses/window-06/raw.json: e73e609c21c0a20a807a3ae0c57d9ba0596b6601c8b42ba6c90a255ef643a65b
        A/clauses/window-06/prompt.txt: 36440442f343c91f5bd18d08f944a4e7151a078cbe4c0d8f044c24c8e62491e0
        A/clauses/window-06/meta.json: 01a52d3c86fb023442a102c1ca9df5b66d3ed4be5cc38b7a1b139cee0b8027ba
        A/clauses/window-08/raw.json: dd8406c0d39edcbcd4800fff5b9eaababcf8de5d9f7d55eb70987601d1e1a0ec
        A/clauses/window-08/prompt.txt: 25cf36150c7c7511095dc511bbb3bd9afa902692a43f66fda3c2b9c078b58bd9
        A/clauses/window-08/meta.json: 51e052b5656b014be12a2b40aa863dc1e1801b7f1759e4884c3a13a45f208a59
        A/tables/TABLE-4-page-6-4/raw.json: 9c853b65ee9065b6db16aab625ef0b53e86d2a5033e1dd1edfc4f1332e11995c
        A/tables/TABLE-4-page-6-4/prompt.txt: af62ef892c6b9dfa5a94a60c3cf01450db90eb24c5223c43bf390a77c3fe244d
        A/tables/TABLE-4-page-6-4/meta.json: 96c3aa510d8ee735c2e9043d16daa518721201e0d2ed813992e916fc396fad92
        A/tables/TABLE-3-page-5-3/raw.json: bb57acfc92876e6ef5d550cdaab6a72373644a2e6c1852dc153073b84ee27463
        A/tables/TABLE-3-page-5-3/prompt.txt: 4cec32c3e05769019eaf42d7e6c66a2b4008c298a7f019976d5d0956cb82fde5
        A/tables/TABLE-3-page-5-3/meta.json: 67a87621e0b38b1a7679865052de7f8f917813ea99c19316c883457b97563d00
        A/tables/TABLE-8-page-9-7/raw.json: 9096e99a07b755a461f8e9149a66fb8d7ebdbcfa381cf5055f1adb43fedf106a
        A/tables/TABLE-8-page-9-7/prompt.txt: a1bc1d1503659af6bf228fdcc64108183b48b4eb3a0c661c592265b3d4a98ba7
        A/tables/TABLE-8-page-9-7/meta.json: f07e9b1ce5bca5d7e2456719858eee1041aebfed867716ea83edbb1b93066389
        A/tables/TABLE-2-page-5-2/raw.json: f19d235fb8b6d76b8ad27a03bdd380667666bad60e6dc53608d364fe38b07fb7
        A/tables/TABLE-2-page-5-2/prompt.txt: 4afb66da04d9c1052f68146384d19f9ad5a8688b55ffed282f6710e3caab741f
        A/tables/TABLE-2-page-5-2/meta.json: d33ed4cc47b494d4b3149dbcc1d84527326063bf1a03ff2c780c06f7da354d2d
        A/tables/TABLE-6-page-8-6/raw.json: 3e9658d0bc7ec4474d969193a07a1c3a99831401ceba43a32ed439568b30321f
        A/tables/TABLE-6-page-8-6/prompt.txt: a98f5ebe8b21af24d388d3495d5080814cb532482c49bc017ef75acc7893a032
        A/tables/TABLE-6-page-8-6/meta.json: 842c3d041477146c01f7255df61dc7ea519b224f92508f514b2d03a0aa42e2fa
        A/tables/TABLE-11-page-15-11/raw.json: a56954dff7bd1c0d22ba8ed470ff9555cc5c2a74549d193cc4853592241d61a6
        A/tables/TABLE-11-page-15-11/prompt.txt: b05a1fd5d857bbe9df86323000704f9ee47ba36c67486ff6d0d4fa7b2939d283
        A/tables/TABLE-11-page-15-11/meta.json: c348320be7565779bb677e883d0155660dd6a0dd6520a0108ccff9e62f068060
        A/tables/TABLE-9-page-11-9/raw.json: 97a4c8adebf9323c41df91407f378526fbf3fefc00d22071c880fd738a360d2e
        A/tables/TABLE-9-page-11-9/prompt.txt: 8f28a168b45ab8980a101dd8a5f2e2457c8b5ed211e428d06c57e4934f830fb5
        A/tables/TABLE-9-page-11-9/meta.json: f19a0d21c431120f200b1249857114a72ab801e6b2565a22370df47da4980f9c
        A/tables/TABLE-10-page-12-10/raw.json: c6086c0983e6d2e87044e2e55a4bc011d124ad8364de9258706b42b49d8f18f4
        A/tables/TABLE-10-page-12-10/prompt.txt: 6d2ad87ec7e43ff4a89abf94a40a3ad091f9c159b8106a2e6c7e502f1088ac62
        A/tables/TABLE-10-page-12-10/meta.json: 7c8d2cd64bd7b250d94e61e9fe78bb48439ac98f9c68b0a87885c1e7d87d68b3
        A/tables/TABLE-1-page-4-1/raw.json: 6690aa9ec8c218d7e5218bbb0f6ebea56e64be43fe3dde1f83ca5158ee63b2a8
        A/tables/TABLE-1-page-4-1/prompt.txt: d60e84f416355d6a94b41345adfb324bff56f632126ea4468771d7784090408f
        A/tables/TABLE-1-page-4-1/meta.json: aeb56ea272ab8a12cf41b935ed429ea9a49625b91b785dfc0014bdde92074edd
        A/tables/TABLE-5-page-7-5/raw.json: 821c479685a95157cfbcd8b0f1a79491403c3c331ac98c63a72a2cee1d39dccc
        A/tables/TABLE-5-page-7-5/prompt.txt: 1e89fb458e71617ca27d71f47b437983408bee830c1ff5c0bd490f93fa128c3d
        A/tables/TABLE-5-page-7-5/meta.json: fd1a8364f8b46524d746bd9707c2a7d44945b18715d7cb8deb56d14c94bdec74
        A/tables/TABLE-7-page-9-8/raw.json: c1d344ce40efccc4414ba19fdfaee78c17a4895b31d17191e419ab3757250619
        A/tables/TABLE-7-page-9-8/prompt.txt: 1828c69475c7ce38b4f75cc1f22ed1065943ea979cf4d42ee7001abd92dc09c1
        A/tables/TABLE-7-page-9-8/meta.json: a32018a1836d12714042dad0c76f1611b4b46b4f2c12eae3bb24a01566bb1914
        B/passages.json: ab782e9157cf800893d7c110cee870a76ed812a06ec0a6bf074c95b476bfbd75
        B/raw.json: 2a772d7730dc95d3decaca568b78557e0cb7391ae78ef23c4d56803303d970c3
        B/source-units.json: 0f1f0ae86406027dc526f99c9ad81e389adf095a9f98ff0afa95f33420eb3d6e
        B/full-source-units.json: a61e92ad051960b9d90486ab070c14d1d5da4a7272066a0ca26d5d194e7f98b8
        B/meta.json: c82ad6b3fa6c203e758efe31d8f9873c9a980657fd4befc3ab7f83557b1b0594
        B/table-images/page-15.png: 1d552aa9be6bc3922b4e49f99a2fb606b4dadaefbab968cbcb0fbf09ce4d6618
        B/table-images/page-12.png: 5fff0e8d46fc518d68e6de24679c0138e06939a76296b05bd43cc2a6a9445933
        B/table-images/TABLE-11-page-15-1.png: 1fa94c1ee0b75e06ee995056a96644aecb8fa8a22f4a3d24096351e1af84a8ac
        B/table-images/page-11.png: 2114e55474caa314b195cf7677d4205e55999adfe9b73f7fa1b71631b53d66ee
        B/table-images/TABLE-9-page-11-1.png: 3ad146f81cc0d2129f777b659b1959c6d98ea55e5afc4e5433384629e5cbed69
        B/table-images/TABLE-8-page-9-1.png: 788b7af958d53275431ba2ea89bcaa73101a99254249d6e638d2ab07694d46e7
        B/table-images/page-6.png: 2713ad278e20f2b0ecfc412d0d94665f487a7dda614b4d876b75618d777e3744
        B/table-images/page-7.png: bba9d6ed0d01c3d98b5646bee62f2c28419dd8ff4464c8bd8c73f51d834d4ddd
        B/table-images/TABLE-1-page-4-2.png: a32aff1d86525372d8b5b6c28adc4d98ec0653b524bd76290c4a499c53b98452
        B/table-images/page-5.png: 19958d0b47e37d0f39716383b97d8df5977fdf895711ae675d0d7b2b48d9fc03
        B/table-images/page-4.png: 8536947c7e73258fcdc4fae4563a1632a2263f81b7d4a55884d774a844c1ff2f
        B/table-images/TABLE-1-page-4-1.png: 56911efac9d62181f727e5dd3a47543404b772704313352449b63655db24315c
        B/table-images/TABLE-6-page-8-1.png: 2dcf8544abcea2bef4a2d116ef5b6b041eeec35e55eee6ece33dc214c1c25349
        B/table-images/page-9.png: 709f09bfeac1026d9f65e595cfc4b862316927247ab6eb9b5f8776f17603e4d9
        B/table-images/TABLE-4-page-6-1.png: aa6584f549904f704424550611bb74c52da09fa4445d9ae36eb0a67ef203f1c1
        B/table-images/page-8.png: 1c89aa03c9a1402a73beab7e0866017a882df8fa93bb50d2617c661904bb2e41
        B/table-images/TABLE-10-page-12-1.png: 256a6be4c793399749e37e568efa4ac7063601ebe1c6f030ced0f12e5e3aadc3
        B/table-images/manifest.json: 9cfb165bb504518766cd79d480bc531f6f5c4b90135145488fa2e1b0f0657dc5
        B/table-images/TABLE-3-page-5-2.png: 11e6fca4ae32b00bcd5e922bb52449515635def2847671255ed71e2eb0e46ca7
        B/table-images/TABLE-2-page-5-1.png: 76578d59d7cc304fbdc133f55447a04e1d24a7330e09ca282899ad5a89bab00c
        B/table-images/TABLE-7-page-9-2.png: 9ed686e665acd3cb4a52736ccc8d298d6c80c299f90bb5e10d03ceebe1591159
        B/table-images/TABLE-5-page-7-1.png: 65fa4c48cf07dab3695dd5dd98bd57d7afa42a323e333e400f01bf9a5b7ba1b7
        B/clauses/window-11/raw.json: 7f3b919856d95680e6c06f3a52da967481683a57b8009e7f97f09fcf3eab2566
        B/clauses/window-11/prompt.txt: de6b56dc83b1f74becaf7ab2535da48f2d67d6a8a5e8e8b48f7d7f934a013911
        B/clauses/window-11/meta.json: 85033b80e1bb83169b9817c1fa09ad5a6c6ecf6cbb3277ba9f92edc7e9b131d3
        B/clauses/window-10/raw.json: 73e9b173b2d942f793aa79f2aa01783fdf1cf90cb0621b017cc03d2e090b1e7e
        B/clauses/window-10/prompt.txt: dad238c7f479f1add760fe42153a417f12ae969b3b15252f54183647772d75c8
        B/clauses/window-10/meta.json: 2dff692ddacb644baacd9301c571b14a916b687070e959f55ec49994dc64fd98
        B/clauses/window-03/raw.json: 720000c2d1f6e871e282fbdb6dadf07e6590fac8576de26d97b2a42293f11a49
        B/clauses/window-03/prompt.txt: f0629478437066f274db14951ae5daff6bbad3450811842103667a1f4ab7c16d
        B/clauses/window-03/meta.json: 89bb06cf0d69b52da139d654a10ab8fc9ffef3c96c929dee289fe8f9ab88a2a7
        B/clauses/window-04/raw.json: 6cf0be3297cb2017d5a7137fb7952c07c36280d6aa44031462fa5b13a5c2eb07
        B/clauses/window-04/prompt.txt: 4bf4cdabc50f0e884fbf31546daa31db0ca3d43f79ddd49a9e2099f75bb223c3
        B/clauses/window-04/meta.json: b10b70de64f1a339ea9e6788b575ff80ac7367465cafecb00527815c6e0c8292
        B/clauses/window-05/raw.json: 042db00d8267f5dbe9c41db9c0fa2b22cf9be21cbd4760c9d02857fc6015c880
        B/clauses/window-05/prompt.txt: be195f1fd367826e0ecd7cad9faddc3de232411c549a73cccc5a82075987c5b3
        B/clauses/window-05/meta.json: 14d73722aa8f7e299887b566a58854b7809c7de9a997cb8d7d067bd91ddfcbf2
        B/clauses/window-02/raw.json: 0403c886a28c9727a4b82071f37e7a7d90048a2219188b9f339175d62526c705
        B/clauses/window-02/prompt.txt: d4412923bdacd3dbf3c6c4043b68c7ab167241702e66630940150abcdf3d7739
        B/clauses/window-02/meta.json: fad3f01f2a188ac84c3c1bb46dcff6b2163fc53275bb4f753eb46080ac43b35d
        B/clauses/window-12/raw.json: cc7d12daa214f7a23a4a73bf5328034619abbde491a9e9941e634649d8e0c7f9
        B/clauses/window-12/prompt.txt: e0d6cc10925ad5fb62704e68a3ace993ea10d4f6efa9d9213110038f9a0f0e07
        B/clauses/window-12/meta.json: bd30c381fa63e0f88bf143cc3eb168264ba88a82d568de3efe2e67c6129171b0
        B/clauses/window-13/raw.json: 505e77b697de6e36797f958cbf50878cd48e21f6b3020eb0a08703ce68086ee9
        B/clauses/window-13/prompt.txt: b99ff20af964940fab8f799fbebca00711dfaedd7bee70a8eecd466031707fae
        B/clauses/window-13/meta.json: 3136d8bc561af237c10706588624319645bd6f20f4d49cb9652245bdfa1f66fd
        B/clauses/window-14/raw.json: a26bcf0442e29a949a7fd7b79529239b4e5af1d24b3c981b27dae1ccd10d30bf
        B/clauses/window-14/prompt.txt: 338233f03bb8a77a1e5e93d85cce41c039348d4d19812afaa8ec84e2a085cda7
        B/clauses/window-14/meta.json: bfbb0ae1c520cb0cb3c4412091cc403e7ec0ba5cb56abeebb2297a1c110b69fd
        B/clauses/window-09/raw.json: ae1ae2419d6f145e824c28023269216109b46845552254c5ded252ac3727230a
        B/clauses/window-09/prompt.txt: 483a5fc73b93be69528f1308ef871a59c89b42b19f1a915b61a758610dedd173
        B/clauses/window-09/meta.json: 83230147683473ecc12b7081af1eb92542b23d2da12a64ed103c760ed906280e
        B/clauses/window-07/raw.json: 647e7eba46be0c13715b70004a9327cea26e3ecf623dbfc48eeb3a6b66576d0d
        B/clauses/window-07/prompt.txt: 85cf0ee0f835b796b85c5202d2e004f11b569dfe5e105eb217e0904f677367b2
        B/clauses/window-07/meta.json: 96cb41f271dccdc154c09f4ef154f635bbb928da071cc6433680ce69a46d9baf
        B/clauses/window-01/raw.json: d29b77e3b14ac5145a9eb26f04ba60c0818c597cf0fdb9f8244da5649a118e4d
        B/clauses/window-01/prompt.txt: 4a2c1ddc82cb2a0c65fb6daa12be4aaddd96f38960996bf57c0e65d84b58df4b
        B/clauses/window-01/meta.json: f19cb9ba045a1aab5f9b41e2e1411a7b1daea2b64a259d5c740444db766a1dee
        B/clauses/window-06/raw.json: d01c5333cb78e391cb21a906d18ec764b53806c0ab564dab8e865e3ce2942482
        B/clauses/window-06/prompt.txt: 36440442f343c91f5bd18d08f944a4e7151a078cbe4c0d8f044c24c8e62491e0
        B/clauses/window-06/meta.json: 18fb79d940470849006a9dfbc7daaaf963726e3e556c8624b2a0c212dcbada2c
        B/clauses/window-08/raw.json: 377824e064ac679874c69db29c06a0498bc308cc4801b8d1c54728ee1f5e0eff
        B/clauses/window-08/prompt.txt: 25cf36150c7c7511095dc511bbb3bd9afa902692a43f66fda3c2b9c078b58bd9
        B/clauses/window-08/meta.json: f942002d5b4f54af0d9fe08bfda735a371b968f12fa3572022f264932e35a2a8
        B/tables/TABLE-4-page-6-4/raw.json: 2b684a20473d753516446c81cda51b55082e2422bbcfc525ebaa28e3ef3887d2
        B/tables/TABLE-4-page-6-4/prompt.txt: af62ef892c6b9dfa5a94a60c3cf01450db90eb24c5223c43bf390a77c3fe244d
        B/tables/TABLE-4-page-6-4/meta.json: c54c1527fa6cd8b8b3970384fe2972fab10eb0e13b0671fec9e626cfdc2f1923
        B/tables/TABLE-3-page-5-3/raw.json: f635d50aec2c919ba134bf06e63542e79acede4e515d184e1954fcc47a05be20
        B/tables/TABLE-3-page-5-3/prompt.txt: 4cec32c3e05769019eaf42d7e6c66a2b4008c298a7f019976d5d0956cb82fde5
        B/tables/TABLE-3-page-5-3/meta.json: 1788f6205f5fc43326563fa97ca22c4aa01341ffab84092b3a718f790ef9d50d
        B/tables/TABLE-8-page-9-7/raw.json: 192c51bef401d6f3cfb3b7339e7f79b8c9fdf0372417507f96e0abd315e76cc2
        B/tables/TABLE-8-page-9-7/prompt.txt: a1bc1d1503659af6bf228fdcc64108183b48b4eb3a0c661c592265b3d4a98ba7
        B/tables/TABLE-8-page-9-7/meta.json: 638c2f4e5cab23790d08925fddfcbdf02af3ed7c9f540116fb0118ab8ff5347a
        B/tables/TABLE-2-page-5-2/raw.json: d0c64b29f1779aedfac132d544a190fd9e3798786b136d542de42b7b96390114
        B/tables/TABLE-2-page-5-2/prompt.txt: 4afb66da04d9c1052f68146384d19f9ad5a8688b55ffed282f6710e3caab741f
        B/tables/TABLE-2-page-5-2/meta.json: 3f5021673dd65af5e9a086a07ceab35a82964714e45e622212a889c8a585d687
        B/tables/TABLE-6-page-8-6/raw.json: 5aa8fee648e6874d0d9c27112095f4e24ae0c002762756aa5838c2bb65e8c7cc
        B/tables/TABLE-6-page-8-6/prompt.txt: a98f5ebe8b21af24d388d3495d5080814cb532482c49bc017ef75acc7893a032
        B/tables/TABLE-6-page-8-6/meta.json: a9ad875a32d86bc3ad30e753dfcf9eb1c3f7cff4eb9096c5fd06fb9ed446649e
        B/tables/TABLE-11-page-15-11/raw.json: 1bdfd605950283b857e707731cabcdcfd6648f18cefd8fdd065527303ffaf4a7
        B/tables/TABLE-11-page-15-11/prompt.txt: b05a1fd5d857bbe9df86323000704f9ee47ba36c67486ff6d0d4fa7b2939d283
        B/tables/TABLE-11-page-15-11/meta.json: 81002ae5e03e1b84889c90af3a5bdf1b759954243abc5e0caee815db23fd95c8
        B/tables/TABLE-9-page-11-9/raw.json: 254154ea65d2129b3375058f1090d9149d3953668739fdd59479dcf8c169e9d0
        B/tables/TABLE-9-page-11-9/prompt.txt: 8f28a168b45ab8980a101dd8a5f2e2457c8b5ed211e428d06c57e4934f830fb5
        B/tables/TABLE-9-page-11-9/meta.json: 1b56d006cdddcbac29336a2bf79463ca95c9c51e69d1ef9f91f636803bfc6431
        B/tables/TABLE-10-page-12-10/raw.json: bf72435acbfb78584e1e6e1a7c8622b746a5e48ee5a33d8fa0531868f502ecf8
        B/tables/TABLE-10-page-12-10/prompt.txt: 6d2ad87ec7e43ff4a89abf94a40a3ad091f9c159b8106a2e6c7e502f1088ac62
        B/tables/TABLE-10-page-12-10/meta.json: 53730333a66d6e7bc43b8771275e7aed7fe0332f539d1528589f14b1b15edfb2
        B/tables/TABLE-1-page-4-1/raw.json: a422a9020effab88eaf376e5741034ce7c8a25b0be6de246a3f4e4afad667758
        B/tables/TABLE-1-page-4-1/prompt.txt: d60e84f416355d6a94b41345adfb324bff56f632126ea4468771d7784090408f
        B/tables/TABLE-1-page-4-1/meta.json: 77d3e78801eade48e1221063c7b3f5e9e14b4aa6c1acf193835d419f401d330c
        B/tables/TABLE-5-page-7-5/raw.json: b98978efd4219296843224281d54190b83007de5cf03e42d11c8b5e66218634b
        B/tables/TABLE-5-page-7-5/prompt.txt: 1e89fb458e71617ca27d71f47b437983408bee830c1ff5c0bd490f93fa128c3d
        B/tables/TABLE-5-page-7-5/meta.json: 28b9fa2a47159364977d59dec98dbd98571e8cd57f90e02ce89557f6f7b51efb
        B/tables/TABLE-7-page-9-8/raw.json: d46e7ff49a9e2bdd42b48572972ff12c58de21f3834779dd3724cb5253799c8b
        B/tables/TABLE-7-page-9-8/prompt.txt: 1828c69475c7ce38b4f75cc1f22ed1065943ea979cf4d42ee7001abd92dc09c1
        B/tables/TABLE-7-page-9-8/meta.json: 9b087fe3444867b2da4c058fc95e793354dccc426ff144f4cff89a66669a5656
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
      pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
      source_review: _compare/relationships-2026-11-16/review-current/Ross2008
      source_status_sha256: 4d52ba7e6aa519dd8202c9290b79580c6d5d54c905a184ba46a3294768bf90ef
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: Right frontal operculum (Large or Small)
    outcome:
      text: Spontaneous affective prosody
    analysis_label: Cortical Lesion Localization - Spontaneous Production (RBD)
    relation: association
    evidence_ids:
    - P9-S1-C6
    - P9-S1-C9
    qualifier_ids:
    - P9-S1-C4
    - P9-S1-C5
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
      source_review: _compare/relationships-2026-11-16/review-current/Ross2008
      source_status_sha256: 4d52ba7e6aa519dd8202c9290b79580c6d5d54c905a184ba46a3294768bf90ef
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C4
      - Accounting without a linked unit P2-S3-C6
      - Accounting without a linked unit P2-S3-C8
      - Unaccounted source passage P2-S3-C6
      - Unaccounted source passage P2-S3-C8
      - Accounting without a linked unit P3-S1-C2
      - Accounting without a linked unit P3-S1-C3
      - Unaccounted source passage P3-S1-C3
      - Unaccounted source passage P3-S1-C2
      - Accounting without a linked unit P6-S2-C10
      - Accounting without a linked unit P6-S2-C11
      - Accounting without a linked unit P6-S2-C12
      - Unaccounted source passage P6-S2-C12
      - Unaccounted source passage P6-S2-C11
      - Unaccounted source passage P6-S2-C10
      - 'window 6: invalid/duplicate disposition P6-S2-C13'
      - 'window 6: invalid/duplicate disposition P7-S1-C6'
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P8-S1-C7
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P9-S1-C4
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P12-S1-C8
      - Accounting without a linked unit P12-S1-C10
      - Accounting without a linked unit P12-S1-C11
      - Accounting without a linked unit P12-S1-C12
      - Accounting without a linked unit P12-S2-C1
      - Accounting without a linked unit P12-S2-C2
      - Accounting without a linked unit P12-S2-C3
      - Accounting without a linked unit P12-S2-C5
      - Unaccounted source passage P12-S1-C12
      - Unaccounted source passage P12-S2-C2
      - Unaccounted source passage P12-S2-C1
      - Unaccounted source passage P12-S1-C10
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P12-S1-C11
      - Unaccounted source passage P12-S2-C3
      - Result passage disposed without unit P12-S2-C12
      - Accounting without a linked unit P12-S2-C7
      - Accounting without a linked unit P12-S2-C8
      - Accounting without a linked unit P12-S3-C2
      - Accounting without a linked unit P12-S3-C3
      - Accounting without a linked unit P13-S1-C2
      - Unaccounted source passage P13-S1-C2
      - Unaccounted source passage P12-S2-C8
      - Unaccounted source passage P12-S3-C3
      - Unaccounted source passage P12-S2-C7
      - Unaccounted source passage P12-S3-C2
      - Result passage disposed without unit P13-S1-C10
      - Result passage disposed without unit P13-S1-C5
      - Result passage disposed without unit P13-S1-C6
      - Result passage disposed without unit P13-S1-C7
      - Accounting without a linked unit P13-S2-C2
      - Accounting without a linked unit P13-S2-C3
      - Accounting without a linked unit P13-S2-C4
      - Unaccounted source passage P13-S2-C2
      - Unaccounted source passage P13-S2-C4
      - Unaccounted source passage P13-S2-C3
      - Accounting without a linked unit P13-S2-C11
      - Result passage disposed without unit P13-S2-C6
      - Result passage disposed without unit P13-S2-C8
      - Unaccounted source passage P13-S2-C11
      - Result passage disposed without unit P16-S2-C3
      - Accounting without a linked unit P16-S2-C4
      - Accounting without a linked unit P16-S3-C8
      - Unaccounted source passage P16-S3-C8
      - Unaccounted source passage P16-S2-C4
      unattached_null_or_qualifier_ids:
      - P1-S1-C4
      - P2-S3-C8
      - P6-S2-C12
      - P8-S1-C7
      - P10-S1-C10
      - P11-S1-C3
      - P12-S1-C7
      - P12-S1-C10
      - P12-S2-C5
      - P12-S2-C8
      - P12-S2-C12
      - P12-S3-C2
      - P12-S3-C3
      - P13-S2-C2
      - P13-S2-C6
      - P13-S2-C11
      - P16-S3-C8
      suppressed_nonrepresented_units: 23
      default_disposition_count_requires_completeness_check: 273
      unselected_timing_passages:
      - P3-S3-C7
      - P4-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C4
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
        source_id: P9-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
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
        source_id: P12-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C2
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
        source_id: P13-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S3-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P4-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P12-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P12-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S3-C6
        - P4-S1-C1
        - P4-S1-C2
        - P4-S1-C3
        - P4-S3-C5
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S2-C1
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C7
        - P5-S2-C8
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C11
        - P5-S2-C12
        - P6-S1-C1
        - P6-S1-C10
        - P6-S1-C11
        - P6-S1-C12
        - P6-S1-C13
        - P6-S1-C14
        - P6-S1-C15
        - P6-S1-C16
        - P6-S1-C2
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S2-C1
        - P6-S2-C10
        - P6-S2-C11
        - P6-S2-C12
        - P6-S2-C13
        - P6-S2-C14
        - P6-S2-C15
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C6
        - P6-S2-C7
        - P6-S2-C8
        - P6-S2-C9
        - P6-S3-C2
        - P6-S3-C3
        - P6-S3-C4
        - P6-S3-C5
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C2
        - P7-S2-C3
        - P7-S2-C4
        - P7-S2-C5
        - P7-S2-C6
        - P7-S2-C7
        - P7-S3-C1
        - P7-S3-C2
        - P7-S3-C3
        - P7-S3-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P4-S2-C13
      - P5-S3-C1
      - P15-S1-C2
      - P18-S1-C10
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-10-page-12-10
      - TABLE-11-page-15-11
      - TABLE-2-page-5-2
      - TABLE-3-page-5-3
      - TABLE-4-page-6-4
      - TABLE-5-page-7-5
      - TABLE-6-page-8-6
      - TABLE-7-page-9-8
      - TABLE-8-page-9-7
      - TABLE-9-page-11-9
      unlinked_tables:
      - TABLE-4-page-6-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S2
        - P8-S3
        - P9-S1
        - P10-S1
        - P10-S2
        - P11-S1
        - P11-S2
        - P13-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
      source_review: _compare/relationships-2026-11-16/review-current/Ross2008
      source_status_sha256: 4d52ba7e6aa519dd8202c9290b79580c6d5d54c905a184ba46a3294768bf90ef
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of goals/concepts
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Ross et al., 1997)
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Ross et al., 1997)
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Geigenberger & Ziegler, 2001)
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Ross et al., 1997)
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Ross et al., 1997)
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about missing analysis in prior work
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior research (Orbelo et al., 2005, 2003; Ross et al.,
        2005)
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior research (Orbelo et al., 2005, 2003; Ross et al.,
        2005)
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior research (Orbelo et al., 2005, 2003; Ross et al.,
        2005)
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group ANOVA (not a clinical relationship)
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group variance analysis
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group ANOVA
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group variance analysis
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Defines the dependent variable for Spontaneous Production analysis
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Reports main effect for group in Spontaneous Production
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Reports post-hoc results for intact patients
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports post-hoc results for poor performance patients
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Defines the dependent variable for Repetition analysis
    - source_id: P6-S2-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Reports main effects and interaction for Repetition
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports post-hoc results for intact patients in Repetition
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Reports non-significant post-hoc ANOVA for intact patients
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports main effects and interaction for poor performance Repetition
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Explains interaction as improved performance in LBD vs RBD
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Reports regression results for LBD vs RBD Repetition patterns
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Defines the dependent variable for Comprehension analysis
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports main effects and interaction for Comprehension
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Reports post-hoc results for intact patients in Comprehension
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports non-significant post-hoc ANOVA for intact patients
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports main effects and interaction for poor performance Comprehension
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports regression results for LBD vs RBD Comprehension patterns
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient cohort description
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports non-significant relationships for deep lesions
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Notes specific deep lesion associations
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Details specific deep lesion associations
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Details specific deep lesion associations
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports non-significant discriminant analysis for deep lesions
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null association for very small frontal operculum
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Reports non-significant association for small frontal operculum
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports significant association for large frontal operculum and anterior
        insula
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports combined 'or' function result for large frontal operculum/anterior
        insula
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Qualifies the combined result
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports high classification accuracy for large or small frontal operculum
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Notes no other combination yielded this result
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Reports significant association for temporal opercula lesions
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports non-significant associations for other cortical localizations
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological advice on imaging
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports combined cortical 'or' function results
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Reports combined cortical and deep lesion results
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Reports classification accuracy after removing exception
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Qualifies the relationship between thalamus and putamen
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of a specific patient case
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of a specific patient case
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of fetal alcohol exposure (prior study)
    - source_id: P12-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of fetal alcohol exposure (prior study)
    - source_id: P12-S1-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null association for small frontal operculum
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Reports significant association for large frontal operculum and anterior
        insula
    - source_id: P12-S1-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Reports combined 'or' function result
    - source_id: P12-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Qualifies the combined result
    - source_id: P12-S2-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Qualifies the combined result
    - source_id: P12-S2-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Reports unexpected finding for very small vs small frontal operculum
    - source_id: P12-S2-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Reports combined 'or' function result for large and very small frontal
        operculum
    - source_id: P12-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Reports discriminant analysis for Repetition
    - source_id: P13-S1-C2
      disposition: represented
      result_indexes:
      - 13
      reason: Reports non-significant regression for RCPM and WAIS-R
    - source_id: P13-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient cohort description for neglect
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Reports non-significant regression for left-sided omissions
    - source_id: P13-S1-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports non-significant discriminant analysis for neglect
    - source_id: P13-S1-C10
      disposition: represented
      result_indexes:
      - 14
      reason: Reports non-significant discriminant analyses for aphasic vs aprosodic
        deficits
    - source_id: P13-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Reports significant associations for mid-white matter and posterior
        insula
    - source_id: P13-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Details specific LBD lesion associations
    - source_id: P13-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Qualifies the relationship between posterior insula and mid-white matter
    - source_id: P13-S2-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Reports combined 'or' function result for LBD spontaneous production
    - source_id: P13-S2-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Reports significant association for mid-white matter in Repetition
    - source_id: P13-S2-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Details specific LBD lesion associations for Repetition
    - source_id: P13-S2-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Reports non-significant associations for LBD comprehension
    - source_id: P13-S2-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Reports non-significant discriminant analysis for LBD comprehension
    - source_id: P14-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of functional imaging
    unresolved_coverage:
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P2-S3-C6
    - P2-S3-C8
    - P2-S3-C9
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C5
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C8
    - P6-S2-C8
    - P6-S2-C13
    - P6-S3-C4
    - P7-S1-C6
    - P7-S1-C9
    - P8-S1-C5
    - P8-S1-C7
    - P8-S1-C8
    - P8-S2-C1
    - P8-S2-C4
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C10
    - P9-S2-C3
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C6
    - P10-S1-C8
    - P10-S1-C11
    - P11-S1-C3
    - P11-S1-C4
    - P11-S2-C3
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C11
    - P12-S1-C12
    - P12-S2-C1
    - P12-S2-C2
    - P12-S2-C6
    - P12-S2-C7
    - P12-S2-C8
    - P12-S2-C12
    - P12-S3-C2
    - P12-S3-C3
    - P13-S1-C5
    - P13-S2-C3
    - P13-S2-C4
    - P13-S2-C6
    - P13-S2-C8
    - P13-S3-C2
    - P14-S1-C8
    - P14-S2-C1
    - P14-S3-C6
    - P16-S1-C11
    - P16-S2-C3
    - P16-S2-C4
    - P16-S3-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-10-page-12-10
    - TABLE-11-page-15-11
    - TABLE-2-page-5-2
    - TABLE-3-page-5-3
    - TABLE-4-page-6-4
    - TABLE-5-page-7-5
    - TABLE-6-page-8-6
    - TABLE-7-page-9-8
    - TABLE-8-page-9-7
    - TABLE-9-page-11-9
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C4
      - P3-S3-C5
      recruited_sample:
      - P3-S3-C1
      - P3-S3-C4
      - P3-S3-C5
      eligibility:
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C8
      - P3-S3-C9
      - P3-S3-C10
      - P4-S1-C4
      imaging_provenance:
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P5-S2-C9
      imaging_timing:
      - P4-S1-C4
      - P4-S1-C5
      outcome_timing:
      - P4-S1-C4
      outcome_definition:
      - P4-S2-C4
      - P4-S2-C9
      - P4-S2-C10
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
      validation: []
      analysis_restrictions:
      - P5-S1-C4
      - P5-S1-C9
      - P5-S2-C1
      dependent_variable_statement:
      - P6-S2-C9
      - P6-S2-C14
      - P7-S1-C7
      - P8-S1-C2
      limitations:
      - P12-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C4
      - P5-S1-C9
      - P6-S1-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C4
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
      source_id: P9-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
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
      source_id: P12-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C2
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
      source_id: P13-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S3-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P4-S2-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P12-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P12-S1-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S3-C6
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      - P4-S3-C5
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C1
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P5-S2-C8
      - P5-S2-C9
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P6-S1-C1
      - P6-S1-C10
      - P6-S1-C11
      - P6-S1-C12
      - P6-S1-C13
      - P6-S1-C14
      - P6-S1-C15
      - P6-S1-C16
      - P6-S1-C2
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P6-S2-C1
      - P6-S2-C10
      - P6-S2-C11
      - P6-S2-C12
      - P6-S2-C13
      - P6-S2-C14
      - P6-S2-C15
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P6-S2-C7
      - P6-S2-C8
      - P6-S2-C9
      - P6-S3-C2
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C2
      - P7-S2-C3
      - P7-S2-C4
      - P7-S2-C5
      - P7-S2-C6
      - P7-S2-C7
      - P7-S3-C1
      - P7-S3-C2
      - P7-S3-C3
      - P7-S3-C6
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
      pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
      review_sha256: 6c9bbbabb5eca56ccdf57dea1d621656c8b7d0073cebfa791f5590ca4bdfe1ff
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
      - P9-S1-C6
      - P9-S1-C9
      source_result: The source reports that 'Large Frontal Operculum' lesions showed
        a significant association with deficits in Spontaneous affective prosody (p
        < .002). It further states that combining 'Large Frontal Operculum' and 'Small
        Frontal Operculum' lesions using an 'or' function correctly classified all
        21 patients regarding their performance (p = .000003). Conversely, 'Very Small
        Frontal Operculum' lesions were not associated with deficits as none of the
        four patients in that group showed deficits.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the functional-anatomic correlation
            in RBD patients (Section 3.4.1) using lesion localization on a template
            map to predict Spontaneous affective prosody deficits. The source explicitly
            identifies the 'Large Frontal Operculum' and the combination of 'Large
            or Small' as the significant predictors.
          source_ids:
          - P9-S1-C3
          - P9-S1-C6
          - P9-S1-C9
        direction:
          answer: fits
          reason: 'The claim correctly identifies the direction of the association:
            injury to the right frontal operculum (Large/Small) is associated with
            deficits, while Very Small lesions are not. The source confirms that Large
            lesions are significantly associated and the combination of Large/Small
            correctly classifies all patients, whereas Very Small lesions showed no
            deficits.'
          source_ids:
          - P9-S1-C4
          - P9-S1-C6
          - P9-S1-C9
        construct:
          answer: fits
          reason: The exposure is correctly identified as right frontal operculum
            lesions (categorized by size). The outcome is Spontaneous affective prosody.
            The measurement method is template lesion overlap (mapping patient lesions
            onto a standard template), not patient diffusion or functional imaging.
            The population is RBD patients.
          source_ids:
          - P5-S2-C9
          - P9-S1-C3
          - P3-S3-C4
        qualifications:
          answer: fits
          reason: The draft includes the material qualification that the association
            is most robust when combining Large and Small lesions, and notes the involvement
            of the anterior insula. It also correctly includes the limitation regarding
            Very Small lesions and the assessment window. The source notes that Large
            lesions often involve the anterior insula, which is captured.
          source_ids:
          - P9-S1-C8
          - P9-S1-C9
          - P9-S2-C4
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft captures the distinction
            between Large/Small (associated) and Very Small (not associated), the
            combination logic, and the temporal limitation regarding recovery. The
            source's note that 'Large' lesions often involve 'Anterior Insula' is
            included as a qualification.
          source_ids:
          - P9-S1-C8
          - P9-S2-C4
      optional_pending:
      - Specific p-values for individual lesion categories (e.g., p=.002 for Large,
        p=.000003 for Large/Small combination) are not transcribed in the draft but
        are present in the source text.
      - Table 8 readings are unverified and not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values for individual lesion categories (e.g., p=.002 for Large,
      p=.000003 for Large/Small combination) are not transcribed in the draft but
      are present in the source text.
    - Table 8 readings are unverified and not transcribed.
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: Right frontal operculum (Large or Small)
      outcome:
        text: Spontaneous affective prosody
      analysis_label: Cortical Lesion Localization - Spontaneous Production (RBD)
      relation: association
      evidence_ids:
      - P9-S1-C6
      - P9-S1-C9
      qualifier_ids:
      - P9-S1-C4
      - P9-S1-C5
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
        source_review: _compare/relationships-2026-11-16/review-current/Ross2008
        source_status_sha256: 4d52ba7e6aa519dd8202c9290b79580c6d5d54c905a184ba46a3294768bf90ef
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8d70f99de6bd15650b219e6ae52805ac46cc3820c3fcd4576c60a2810427856a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C4
          page: 3
          text_layer_sha256: 8d70f99de6bd15650b219e6ae52805ac46cc3820c3fcd4576c60a2810427856a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The primary patient group con-

          sisted of 21 individuals with RBD due to focal ischemic

          infarctions limited to the right hemisphere that predomi-

          nantly involved cortex and adjacent white matter.'
        anchor_text: 'The primary patient group con-

          sisted of 21 individuals with RBD due to focal ischemic

          infarctions limited to the right hemisphere that predomi-

          nantly involved cortex and adjacent white matter.'
        excluded_fragments: []
        image_sha256: f267f007427647c7a838f293e04b842f5af5a4b8ff513cac971511bd9fe58b3e
        transcription: . The primary patient group consisted of 21 individuals with
          RBD due to focal ischemic infarctions limited to the right hemisphere that
          predominantly involved cortex and adjacent white matter
      P4-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 181508546eec114f78961699acf9d3c93ea8b6c7e985e347448ca3669eb72c9a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C4
          page: 4
          text_layer_sha256: 181508546eec114f78961699acf9d3c93ea8b6c7e985e347448ca3669eb72c9a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Testing of the brain-damaged patients was completed

          within three to eight weeks post-stroke to exclude any acute

          and potentially reversible pathophysiologic deﬁcits, such as

          diaschisis, ischemic penumbra or edema (Croquelois, Win-

          termatk, Reichart, Meuli, & Bogousslavsky, 2003; Nguyen

          & Botez, 1998; Shaw, Alvord, & Berry, 1959; approxi-

          mately 1–3 weeks post-stroke), and before the occurrence

          of long-term improvement from spontaneous recovery

          due to neural reorganization (Kertesz, 1979, chap. 15;

          Rosen et al., 2005; 3–5 months post-stroke and beyond).'
        anchor_text: 'Testing of the brain-damaged patients was completed

          within three to eight weeks post-stroke to exclude any acute

          and potentially reversible pathophysiologic deﬁcits, such as

          diaschisis, ischemic penumbra or edema (Croquelois, Win-

          termatk, Reichart, Meuli, & Bogousslavsky, 2003; Nguyen

          & Botez, 1998; Shaw, Alvord, & Berry, 1959; approxi-

          mately 1–3 weeks post-stroke), and before the occurrence

          of long-term improvement from spontaneous recovery

          due to neural reorganization (Kertesz, 1979, chap. 15;

          Rosen et al., 2005; 3–5 months post-stroke and beyond).'
        excluded_fragments: []
        image_sha256: 5a99364cf5c1684fb055254b6dd0f4f95ef051bd7352fe8f47e7b88c00148f28
        transcription: 'Testing of the brain-damaged patients was completed

          within three to eight weeks post-stroke to exclude any acute

          and potentially reversible pathophysiologic deficits, such as

          diaschisis, ischemic penumbra or edema (Croquelois, Win-

          termatk, Reichart, Meuli, & Bogousslavsky, 2003; Nguyen

          & Botez, 1998; Shaw, Alvord, & Berry, 1959; approxi-

          mately 1–3 weeks post-stroke), and before the occurrence

          of long-term improvement from spontaneous recovery

          due to neural reorganization (Kertesz, 1979, chap. 15;

          Rosen et al., 2005; 3–5 months post-stroke and beyond)'
      P4-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 191a5e51741546cad5254b5740e8c765c1b2ddffe48075cb87974632d98a7239
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1b496a822c29872f726b9334f94c89aeb56296ae121fad06dbec38796a147d62
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C5
          page: 4
          text_layer_sha256: 1b496a822c29872f726b9334f94c89aeb56296ae121fad06dbec38796a147d62
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'MRI scans were obtained between 2 and 6 weeks post-

          stroke.'
        anchor_text: 'MRI scans were obtained between 2 and 6 weeks post-

          stroke.'
        excluded_fragments: []
        image_sha256: e5fee820dd20b24e0f482a9eb9d4b8550b5e03683b3f5dc559ff026a0fc69b32
        transcription: 'MRI scans were obtained between 2 and 6 weeks post-

          stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'Spontaneous aﬀective prosody

    Data in Table 8 indicates that ‘Very Small Frontal Oper-

    culum’ lesions (Fig. 3) were not associated with deﬁcits of

    Spontaneous aﬀective prosody because none of the four

    patients evinced Spontaneous deﬁcits.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
