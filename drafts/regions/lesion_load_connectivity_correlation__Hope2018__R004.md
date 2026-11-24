---
id: lesion_load_connectivity_correlation
name: lesion load and connectivity disruption correlation
kind: network
findings:
- id: f1
  target: connectivity_disruption
  target_kind: impairment
  claim: Every lesion load variable was correlated with at least one connectivity
    variable and vice versa, and significant pairwise correlations existed for every
    principal component explaining at least 1% of the total variance in the original
    data.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: stroke patients
    phase: not_reported
    time_post_onset: tested over a broad range of times post stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - connectivity disruption was inferred from T1-weighted MRI rather than measured
    directly with subject-specific diffusion data
  - lesions were segmented using an automatic toolbox (ALI) rather than manual segmentation
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Correlation between lesion load (measured as the proportion
    of each of 116 AAL grey-matter regions destroyed by the patient''s lesion) and
    connectivity disruption (mean disconnection implied by the lesion, calculated
    via the Network Modification toolbox using a reference connectome from 73 healthy
    controls). Bonferroni correction for multiple comparisons was applied; lesion
    load and connectivity variables were included only if they were affected by at
    least 3 patients'' lesions. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S1-C7, two-model
    agreement, human verification pending): Patient data


    Our patient data were extracted from our PLORAS database (Seghier et al., 2016),
    which associates stroke patients, tested over a broad range of times post stroke,
    with demographic data, behavioural test scores from the Comprehensive Aphasia
    Test (Swinburn et al., 2004), and high resolution T1-weighted MRI brain scans
    Original text-layer quotation is preserved below.'
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
    - proposed_concept:connectivity_disruption
  citation: '@Hope2018'
  source_passages:
  - section: Original source P5-S1-C6
    page: 5
    quote: 'Pairwise correlations between these variables

      revealed that every lesion load variable was correlated with at least one

      connectivity variable and vice versa, even after a Bonferroni correction

      for multiple comparisons.'
    supports: claim
  - section: Original source P5-S1-C7
    page: 5
    quote: 'These two sets of variables are highly cor-

      related.'
    supports: claim
  - section: Original source P5-S1-C9
    page: 5
    quote: 'Here again, and having

      also applied a Bonferroni correction for multiple comparisons, sig-

      niﬁcant pairwise correlations existed for every principle component

      which, individually, explained at least 1% of the total variance in the

      original data (11 components of the lesion load variables, and 13

      components of the connectivity variables).'
    supports: claim
  - section: Original source P5-S1-C10
    page: 5
    quote: 'Fig. 3 presents an example

      of this correspondence, plotting the ﬁrst principal components of each

      dataset against each other (r = −0.94).

      4.'
    supports: claim
  - section: Original source P5-S1-C4
    page: 5
    quote: 'First, we identiﬁed all of the lesion load and con-

      nectivity disruption variables which could reasonably be correlated: i.e.

      those that were aﬀected by at least 3 patients'' lesions.'
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: 'All of the 116

      lesion load variables met this criterion, but only 2420 connectivity

      variables were included.'
    supports: method
  - section: Original source P2-S2-C5
    page: 2
    quote: 'We examined models driven by

      both lesion load in these regions (i.e. the proportion of each region

      destroyed by each patient''s lesion), and by the disconnection of the

      white matter connections between them.'
    supports: method
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Disconnection was calculated

      via the Network Modiﬁcation toolbox (Kuceyeski et al., 2013), which

      generates the mean disconnection implied by each lesion, using struc-

      tural connectomes deﬁned for a separate sample of 73 neurologically

      normal controls.'
    supports: method
  - section: Original source P3-S3-C10
    page: 3
    quote: 'Lesion and language data

      There were a total of 818 patients in our sample, including 260

      women and 98 patients who were left-handed or ambidextrous pre-

      stroke.'
    supports: sample
  - section: Original source P2-S1-C7
    page: 2
    quote: 'Patient data

      Our patient data were extracted from our PLORAS database (Seghier

      et al., 2016), which associates stroke patients, tested over a broad range

      of times post stroke, with demographic data, behavioural test scores

      from the Comprehensive Aphasia Test (Swinburn et al., 2004), and high

      resolution T1-weighted MRI brain scans.'
    supports: sample
  - section: Original source P5-S1-C13
    page: 5
    quote: 'One caveat to these results is that we have inferred connectivity

      disruption from T1-weighted MRI, rather than measuring it “directly”

      with subject-speciﬁc diﬀusion data.'
    supports: limitation
  - section: Original source P6-S2-C2
    page: 6
    quote: 'Nevertheless, several recent studies have suggested that algorithmic

      approaches to binary lesion segmentation should be treated with cau-

      tion, at least in the sense that they may diverge from the presumed

      “gold standard” of manual segmentation by a neurologist (Pustina

      et al., 2016; Yourganov et al., 2016).'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hope2018
  proposal_id: R004
  review_status_sha256: 52ad424469a48b0ddd58ea633806ec71aa967db6af8337aace53af2ea0e8be52
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
        A/passages.json: ef39ae21f7e8981235056204f5ce690eeb49943a5e400fc8f60476cf687e8a55
        A/raw.json: 0bb5ad99b245e220f3e0cf93dbc7075ce5655f893cb1761c538e96928cde8460
        A/source-units.json: 425e635e604b37ac7cdd05c9e1a99872733b680eeb633bc506aab7a4f6e09726
        A/full-source-units.json: ba86b6847631777ccecf912c18c6e14c84326afb0fc79d3d7d639d88844e4eb6
        A/meta.json: f3b7cb8d4e56725ac822077fc6038c3a3e301ca82590dc2701c98d72af5511bf
        A/table-images/page-4.png: ee865f2d0ad3a29be9324e0be73b92dc489f5d7f1425ad67c95257abf76ba08d
        A/table-images/TABLE-1-page-4-1.png: 4b3ab872eabd2117d7d9d2d2899550d056fe0dad1e7df41d3ccfb7433edbb9e0
        A/table-images/manifest.json: 4df2437dfb1cd2396753c6fc915af10f333ae56de298ac4efd1522f30ae28156
        A/clauses/window-03/raw.json: 9141839d0aea93d713c54b72d0b63d24a533903c04dabde415d7cf5d7d60ff7f
        A/clauses/window-03/prompt.txt: e64c6f3fcb7afd77a8ea66a86e8d696b1e87710ea43681ae921d7b8535ffb1e5
        A/clauses/window-03/meta.json: 3cf89792d25e7ca392a33b75649672f3bd98e84683f7dc143bf66f6252234a62
        A/clauses/window-04/raw.json: 78c00ffdebcd0b83a724777cda384377dfb5f915928fe64bf82cffa163046c16
        A/clauses/window-04/prompt.txt: 98124b336dfa4e2705d67b4040286cd060b0f6717cf0b05c214587d409ac97bc
        A/clauses/window-04/meta.json: f0ebedb657fd21dd452cb4bafe7f34bd8dd516a360d62212ac9db06939d117e5
        A/clauses/window-05/raw.json: fbd594345e9bb78109dfa4f3f40b7fb18efbb1cdd5792f1e76ab384d939f936a
        A/clauses/window-05/prompt.txt: b02b6579a4fb08c6af9ee8c9b08cf27261b26abc47cba304610962dff171e33f
        A/clauses/window-05/meta.json: c15e53fb3664618bf3dc42447072245b83c8ee96209e59e070e43a62512f452d
        A/clauses/window-02/raw.json: b9cfb50827cdf19bfe4308f5e68d371f29fc5f8227834d959d3398a56e63681a
        A/clauses/window-02/prompt.txt: e12ad66f9396de9fd879da85d29b2f67d272a8715805345b442194a5095f7c50
        A/clauses/window-02/meta.json: f0d5808d3f5c3e6ca6f57a6df0ef3b42379b0029e751c4b6db3f1e002427ccbb
        A/clauses/window-07/raw.json: 18b92557faf9a84d68229e15d4723602d42355e7a7ec6ef79bedeb559bc3e16c
        A/clauses/window-07/prompt.txt: 8251fd743489df2798d9912cf8c22b2f86da400da75dfc90bcf583ff6e069fcb
        A/clauses/window-07/meta.json: 7bd698e0264ea520d5eeaf50b042f08db1e6f1a331dae3f5538ae1a994cb87f3
        A/clauses/window-01/raw.json: 29fd43ddbce4c3c4d0cb94b0b6de8af5bc23a531e70161aaa275f8780818fcee
        A/clauses/window-01/prompt.txt: 7199d3291ea147c0a296d33194ece147349e6de2ba1efa3d83b0822e42454743
        A/clauses/window-01/meta.json: 4208753c0d0172a3a85bf41998a77ee0e69117164c1321502ec768fa3e57a998
        A/clauses/window-06/raw.json: 443cf6bd38aa76c72aeedc990c027737aff3979abaf8767ce325f5f11925001c
        A/clauses/window-06/prompt.txt: 8725b59882194f4dd31ad6b4d4f5b3f1c4f420176bcab1eed2b9fee75cffecc5
        A/clauses/window-06/meta.json: 4a992be3fe847004c3cfef1208611f96f2094b08bd6a2efe5370e2ad3b11b83e
        A/tables/TABLE-1-page-4-1/raw.json: ec1990e096d1c824740ea471bb9cf4c7f00f023c33b1ab87f2f371b884f85892
        A/tables/TABLE-1-page-4-1/prompt.txt: fc98bb87d0d0d1d109b38e2a735be898b26b33b75b017a3fe2e92e0bb76f059e
        A/tables/TABLE-1-page-4-1/meta.json: 48693de374f314fe83feaa0bc9358a4254870049bba059490807b7264b2da4eb
        B/passages.json: ef39ae21f7e8981235056204f5ce690eeb49943a5e400fc8f60476cf687e8a55
        B/raw.json: 6a30e8b3c1cc21fea31b53e217a8c202297e90e6764bf50bdbc06065684662b9
        B/source-units.json: 425e635e604b37ac7cdd05c9e1a99872733b680eeb633bc506aab7a4f6e09726
        B/full-source-units.json: ba86b6847631777ccecf912c18c6e14c84326afb0fc79d3d7d639d88844e4eb6
        B/meta.json: f9711096fc6207765045c50dac8795ba08b73a59ee9eba3fb3b26734bedc3eaa
        B/table-images/page-4.png: ee865f2d0ad3a29be9324e0be73b92dc489f5d7f1425ad67c95257abf76ba08d
        B/table-images/TABLE-1-page-4-1.png: 4b3ab872eabd2117d7d9d2d2899550d056fe0dad1e7df41d3ccfb7433edbb9e0
        B/table-images/manifest.json: 71d4a73681adc5c65dddbf1eb82aa3190bff0974c467c441aee1f0a1198a983b
        B/clauses/window-03/raw.json: 00462d6feb228f4ef7d4019b2fb130357cd8120068d185d125a5bf64eefa3259
        B/clauses/window-03/prompt.txt: e64c6f3fcb7afd77a8ea66a86e8d696b1e87710ea43681ae921d7b8535ffb1e5
        B/clauses/window-03/meta.json: a46d33546928ff3d8826b33bfd11321d6c215e498f8f93f60aa44f2cf901e4fa
        B/clauses/window-04/raw.json: 3cc5974daf590d3b269c61f2169104b7b005f953bfc1bf218291b0fafea721c6
        B/clauses/window-04/prompt.txt: 98124b336dfa4e2705d67b4040286cd060b0f6717cf0b05c214587d409ac97bc
        B/clauses/window-04/meta.json: 3221a9cad26493cdcd56fac32b32d0bebee1201c920f100ed5b27e4b378f1b60
        B/clauses/window-05/raw.json: d8759ecd4eeab4155def6b35d298786ac77addd32ad0b15fb51852965df66cef
        B/clauses/window-05/prompt.txt: b02b6579a4fb08c6af9ee8c9b08cf27261b26abc47cba304610962dff171e33f
        B/clauses/window-05/meta.json: 6297ff76f70774a5f0b6dec4d61545b8a5dcd8bcd091cdc2b40574daf9161084
        B/clauses/window-02/raw.json: 52938591eaf94a600eaff451fa10b90e2a69568e5994d8441ee2508edd30b008
        B/clauses/window-02/prompt.txt: e12ad66f9396de9fd879da85d29b2f67d272a8715805345b442194a5095f7c50
        B/clauses/window-02/meta.json: bfe47fd8db9cd23cb6c122a0ee7610602e1079c4e86831aba5e5b0af7920ad06
        B/clauses/window-07/raw.json: 40adbe51e059067875b777d52330314121f93bc5e53dfe287a2b50bf376132b7
        B/clauses/window-07/prompt.txt: 8251fd743489df2798d9912cf8c22b2f86da400da75dfc90bcf583ff6e069fcb
        B/clauses/window-07/meta.json: c02ab6d2c955a18db4fe9a5bc9e1ab4d361b3a2ff1a76500b0a453029400c171
        B/clauses/window-01/raw.json: 68c0f537301b519b29fb1473370e458a40b45ad71139432d82493aa4c140d546
        B/clauses/window-01/prompt.txt: 7199d3291ea147c0a296d33194ece147349e6de2ba1efa3d83b0822e42454743
        B/clauses/window-01/meta.json: 54a9c045538ee3bb4e509bf29bad52b37c496c91f5bfc51067dd8eef8618adef
        B/clauses/window-06/raw.json: 17d7bce218abe0ac79ad9d8ae42ae75a82eed638f831e1fcaf452215ac2a81e2
        B/clauses/window-06/prompt.txt: 8725b59882194f4dd31ad6b4d4f5b3f1c4f420176bcab1eed2b9fee75cffecc5
        B/clauses/window-06/meta.json: 8ebec0909f56e607f2f0e0cd361b3da66a501b81d6c798eedfd0be22b102920a
        B/tables/TABLE-1-page-4-1/raw.json: d1e1e92a3e547ef76ebd4319ed9a9d14d75a5cf70bce272e12a174375c925059
        B/tables/TABLE-1-page-4-1/prompt.txt: fc98bb87d0d0d1d109b38e2a735be898b26b33b75b017a3fe2e92e0bb76f059e
        B/tables/TABLE-1-page-4-1/meta.json: 7d91a7a906d9eed54baeb288e2002f0693fbf0df03d7fff134af3a486e6a637f
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
      pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
      source_review: _compare/relationships-2026-11-16/review-current/Hope2018
      source_status_sha256: 9ede1a3a47746ac19b6d2f0bf889fa5957efd905d8b0a49e2aad81fadc747906
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: lesion load
    outcome:
      text: connectivity disruption
    analysis_label: Variable correlation analysis
    relation: association
    evidence_ids:
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C9
    - P5-S1-C10
    qualifier_ids:
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C8
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
      source_review: _compare/relationships-2026-11-16/review-current/Hope2018
      source_status_sha256: 9ede1a3a47746ac19b6d2f0bf889fa5957efd905d8b0a49e2aad81fadc747906
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C6
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S2-C6
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C7
      - Unaccounted source passage P5-S1-C7
      - Accounting without a linked unit P5-S2-C12
      - Accounting without a linked unit P5-S2-C7
      - Accounting without a linked unit P5-S3-C3
      - Accounting without a linked unit P6-S1-C8
      - Result passage disposed without unit P6-S1-C9
      - Unaccounted source passage P5-S2-C7
      - Unaccounted source passage P5-S3-C3
      - Unaccounted source passage P6-S1-C8
      - Unaccounted source passage P5-S2-C12
      - Accounting without a linked unit P6-S2-C5
      - Accounting without a linked unit P6-S3-C1
      - Unaccounted source passage P6-S3-C1
      - Unaccounted source passage P6-S2-C5
      - Result passage disposed without unit P6-S4-C5
      - Result passage disposed without unit P6-S4-C6
      unattached_null_or_qualifier_ids:
      - P5-S1-C5
      - P5-S2-C7
      - P6-S1-C3
      - P6-S1-C8
      - P6-S4-C6
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 152
      unselected_timing_passages:
      - P3-S3-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P3-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P2-S3-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_definition
        source_ids:
        - P1-S1-C8
        - P1-S1-C12
        - P2-S1-C7
        - P2-S3-C2
        - P2-S3-C5
        - P2-S3-C6
        - P3-S3-C6
        - P4-S1-C7
        - P4-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P5-S1-C13
        - P5-S2-C3
        - P6-S1-C10
        - P6-S2-C2
        - P6-S2-C8
        - P6-S2-C9
        - P6-S3-C5
        - P6-S3-C7
        - P6-S3-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - limitations
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P3-S4
        - P4-S1
        - P5-S1
        - P5-S2
        - P5-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
      source_review: _compare/relationships-2026-11-16/review-current/Hope2018
      source_status_sha256: 9ede1a3a47746ac19b6d2f0bf889fa5957efd905d8b0a49e2aad81fadc747906
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Abstract statement of no consistent evidence for connectivity disruption
        improving language score prediction.
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses correlation between variables as a possible reason for results.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion that connectivity disruption does not improve prediction
        over lesion load.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of variables remaining after feature selection.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary material.
    - source_id: P3-S4-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Finding that connectivity data improves naming prediction using linear
        SVM.
    - source_id: P3-S4-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Finding that Gaussian process models handle full connectivity datasets
        better.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Finding that GPMR inducer extinguished benefit of connectivity data
        for naming.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Finding that benefits were inducer-dependent (5/16 inducers).
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Finding no significant differences when using the best result for each
        configuration.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Conclusion that connectivity variables do not drive significantly better
        naming predictions.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Finding no evidence that connectivity disruption improves prediction
        for other language scores.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 2
      reason: Finding no connectivity model was significantly better than lesion load
        model for any score.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Restatement that no language score prediction was significantly improved.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis about shared information.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of variable inclusion criteria.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Finding that every lesion load variable correlated with at least one
        connectivity variable.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Finding that the two sets of variables are highly correlated.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Finding significant correlations between principal components of both
        datasets.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Finding high correlation (r = -0.94) between first principal components.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion that connectivity disruption does not improve language outcome
        relation.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion that connectivity data is not useful over lesion load data.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to other studies' results without correction for multiple
        comparisons.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Finding marginally significant benefit for stacked model using linear
        SVM (p=0.04).
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Finding no significant benefits for GPMR or best of 16 inducers.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to Pustina et al. results.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Finding that LC(r) models have significantly higher correlation coefficients
        than lesion load models.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Finding that the mean improvement in correlation coefficients is only
        0.005.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about predictive results being comparable to other
        work.
    - source_id: P6-S4-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Statement that the expected initial advantage of connectivity variables
        never emerged.
    - source_id: P6-S4-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion that language outcome prediction was not significantly improved
        by connectivity disruption.
    - source_id: P6-S5-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion that lesion load variables can serve as reliable proxies
        for connectivity disruption.
    unresolved_coverage:
    - source_id: P6-S4-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C6
    - P3-S1-C6
    - P3-S3-C8
    - P3-S4-C8
    - P4-S1-C1
    - P4-S1-C4
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C11
    - P5-S1-C12
    - P5-S2-C7
    - P5-S3-C3
    - P6-S1-C3
    - P6-S1-C9
    - P6-S2-C5
    - P6-S4-C5
    - P6-S4-C6
    - P6-S4-C9
    - P6-S5-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C8
      recruited_sample:
      - P1-S1-C8
      eligibility:
      - P1-S1-C9
      - P2-S1-C8
      - P2-S1-C10
      - P6-S4-C6
      imaging_provenance:
      - P2-S2-C2
      - P2-S2-C6
      - P5-S1-C13
      imaging_timing:
      - P2-S1-C7
      outcome_timing:
      - P2-S1-C7
      outcome_definition: []
      validation:
      - P3-S1-C9
      - P5-S2-C2
      analysis_restrictions:
      - P3-S1-C4
      - P3-S1-C8
      - P3-S2-C9
      - P5-S2-C11
      dependent_variable_statement:
      - P1-S1-C12
      - P2-S4-C2
      - P3-S4-C2
      - P4-S1-C7
      limitations: []
      personal_factors:
      - P2-S1-C9
      - P2-S3-C9
      - P3-S3-C10
      tested_personal_effects: []
      adjustment_roles:
      - P2-S3-C9
      - P2-S4-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C8
      - P2-S1-C9
      - P3-S3-C10
      - P3-S3-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: validation
      source_id: P3-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P2-S3-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_definition
      source_ids:
      - P1-S1-C8
      - P1-S1-C12
      - P2-S1-C7
      - P2-S3-C2
      - P2-S3-C5
      - P2-S3-C6
      - P3-S3-C6
      - P4-S1-C7
      - P4-S1-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P5-S1-C13
      - P5-S2-C3
      - P6-S1-C10
      - P6-S2-C2
      - P6-S2-C8
      - P6-S2-C9
      - P6-S3-C5
      - P6-S3-C7
      - P6-S3-C8
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
      pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
      review_sha256: 52ad424469a48b0ddd58ea633806ec71aa967db6af8337aace53af2ea0e8be52
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
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C9
      - P5-S1-C10
      source_result: The analysis found that lesion load variables and connectivity
        disruption variables are highly correlated. Specifically, every lesion load
        variable was correlated with at least one connectivity variable and vice versa,
        and significant pairwise correlations existed for every principal component
        explaining at least 1% of the total variance, even after Bonferroni correction.
        This correlation was used to explain why connectivity data did not add predictive
        value over lesion load in the main model comparisons.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the correlation between lesion load and
            connectivity disruption variables (Section 3.4), distinct from the model
            comparison analyses in Sections 3.1-3.3. The source IDs P5-S1-C6 to C10
            correctly identify this specific correlation analysis.
          source_ids:
          - P5-S1-C2
          - P5-S1-C6
          - P5-S1-C9
        direction:
          answer: fits
          reason: The source states that the variables are 'highly correlated' and
            that significant correlations were found (P5-S1-C6, P5-S1-C7). The proposed
            direction 'likely' is a weak but acceptable qualitative representation
            of a detected positive correlation (r=-0.94 for first PCs, implying inverse
            relationship between load and disconnection, or high collinearity). It
            does not claim a null effect.
          source_ids:
          - P5-S1-C6
          - P5-S1-C7
          - P5-S1-C10
        construct:
          answer: fits
          reason: The exposure is lesion load (proportion of AAL regions destroyed)
            and the outcome/target is connectivity disruption (inferred via Network
            Modification toolbox). The patient measurement is correctly identified
            as template_lesion_overlap (lesions overlaid on AAL atlas), not patient_diffusion,
            as the connectivity is inferred from T1 MRI using a reference connectome,
            not measured via patient diffusion data.
          source_ids:
          - P2-S2-C5
          - P2-S2-C6
          - P5-S1-C13
        qualifications:
          answer: fits
          reason: The proposed qualifications include the Bonferroni correction and
            the restriction to variables affected by at least 3 patients' lesions.
            These match the source text in P5-S1-C4, P5-S1-C5, and P5-S1-C6/C9.
          source_ids:
          - P5-S1-C4
          - P5-S1-C5
          - P5-S1-C6
          - P5-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The proposed limitations include the inference of connectivity from
            T1 MRI rather than diffusion, and the use of automatic lesion segmentation.
            These are the key caveats mentioned in the source (P5-S1-C13, P6-S2-C2).
            No material caveat changing the interpretation of the correlation result
            is omitted.
          source_ids:
          - P5-S1-C13
          - P6-S2-C2
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    normalizations:
    - field: bucket
      original: ingredients
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 818
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R004
      exposure:
        text: lesion load
      outcome:
        text: connectivity disruption
      analysis_label: Variable correlation analysis
      relation: association
      evidence_ids:
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C9
      - P5-S1-C10
      qualifier_ids:
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C8
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
        source_review: _compare/relationships-2026-11-16/review-current/Hope2018
        source_status_sha256: 9ede1a3a47746ac19b6d2f0bf889fa5957efd905d8b0a49e2aad81fadc747906
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fb879b257bdf5501cde2237568653e708cccedd55e3c5b90cbad6333650cbcad
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C10
          page: 3
          text_layer_sha256: fb879b257bdf5501cde2237568653e708cccedd55e3c5b90cbad6333650cbcad
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Lesion and language data

          There were a total of 818 patients in our sample, including 260

          women and 98 patients who were left-handed or ambidextrous pre-

          stroke.'
        anchor_text: 'Lesion and language data

          There were a total of 818 patients in our sample, including 260

          women and 98 patients who were left-handed or ambidextrous pre-

          stroke.'
        excluded_fragments: []
        image_sha256: 5b518cfe57ed6de44f1181fc09ebe5b0820929580a7b75102631a66dd22bcf30
      P2-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 427f0c5e550f7aff1978b860789234f94252025c5ea500cca5dfabd0af510d89
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b783e80103beaf4c40891a040f989b6aeda70a508340c9e6ced68201a8f023fe
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C7
          page: 2
          text_layer_sha256: b783e80103beaf4c40891a040f989b6aeda70a508340c9e6ced68201a8f023fe
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patient data

          Our patient data were extracted from our PLORAS database (Seghier

          et al., 2016), which associates stroke patients, tested over a broad range

          of times post stroke, with demographic data, behavioural test scores

          from the Comprehensive Aphasia Test (Swinburn et al., 2004), and high

          resolution T1-weighted MRI brain scans.'
        anchor_text: 'Patient data

          Our patient data were extracted from our PLORAS database (Seghier

          et al., 2016), which associates stroke patients, tested over a broad range

          of times post stroke, with demographic data, behavioural test scores

          from the Comprehensive Aphasia Test (Swinburn et al., 2004), and high

          resolution T1-weighted MRI brain scans.'
        excluded_fragments: []
        image_sha256: 3e65868cde207b087437d97c182842d9234c601a9e7f8f9ab416095fc4e4de5b
        transcription: 'Patient data


          Our patient data were extracted from our PLORAS database (Seghier et al.,
          2016), which associates stroke patients, tested over a broad range of times
          post stroke, with demographic data, behavioural test scores from the Comprehensive
          Aphasia Test (Swinburn et al., 2004), and high resolution T1-weighted MRI
          brain scans'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Pairwise correlations between these variables

    revealed that every lesion load variable was correlated with at least one

    connectivity variable and vice versa, even after a Bonferroni correction

    for multiple comparisons.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
