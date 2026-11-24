---
id: right_slf_fa
name: right superior longitudinal fasciculus cluster
kind: network
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: Patients with mild-to-moderate aphasia exhibited significantly greater fractional
    anisotropy in the right superior longitudinal fasciculus than patients with severe
    aphasia.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: not_reported
    population: Patients with chronic left hemisphere stroke and aphasia
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and
      timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Heterogeneous types of aphasia among participants
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Fractional anisotropy (FA) values in the right superior
    longitudinal fasciculus, identified using the Harvard–Oxford Cortical and Subcortical
    Atlas. Mild-to-moderate group (n=11) compared to severe group (n=12). Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S1-C11, two-model agreement, human verification pending):
    . Patients were assigned to one of

    two groups on the basis of aphasia severity – mild to

    moderate (group 1; 11 patients) and severe (group 2; 12

    patients; Table 1) aphasia groups Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:aphasia_severity
  citation: '@Lee2018'
  source_passages:
  - section: Original source P3-S1-C2
    page: 3
    quote: 'Group 1 exhibited significantly greater FA in the right

      superior longitudinal fasciculus than group 2 (P < 0.05;

      Table 3).'
    supports: claim
  - section: Original source P2-S1-C3
    page: 2
    quote: 'Patients

      Twenty-three patients with left hemisphere stroke with

      aphasia were recruited in accordance with the following

      criteria: (a) native Korean speaker; (b) first ever stroke in

      the left hemisphere, confirmed by MRI or computed

      tomography; (c) supra tentorial stroke; (d) at least 18 years

      of age; (e) right handedness before the stroke; (f) more

      than 6 months since onset of stroke; and (g) mild to

      severe speech disturbance, determined by standardized

      language evaluation.'
    supports: sample
  - section: Original source P2-S1-C11
    page: 2
    quote: 'Patients were assigned to one of

      two groups on the basis of aphasia severity – mild to

      moderate (group 1; 11 patients) and severe (group 2; 12

      patients; Table 1) aphasia groups.'
    supports: sample
  - section: Original source P2-S2-C10
    page: 2
    quote: 'Finally, gray and white

      matter volumes were determined by voxel-based mor-

      phometric methods, and FA values of specific language-

      related areas of the brain (including pars opercularis; pars

      triangularis; superior temporal, angular, and supramar-

      ginal gyri; and superior/inferior longitudinal fasciculus)

      were determined.'
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Specific areas of the brain were iden-

      tified in accordance with the Harvard–Oxford Cortical

      and Subcortical Atlas inbuilt in FSL 5.0.10.'
    supports: method
  - section: Original source P2-S1-C1
    page: 2
    quote: '

      All patients underwent MRI and language testing at the

      same time.'
    supports: method
  - section: Original source P5-S2-C3
    page: 5
    quote: 'Our study has several limitations, with the first one being

      its small sample size.'
    supports: limitation
  - section: Original source P5-S1-C11
    page: 5
    quote: 'First, patients included in this study

      had variable types of aphasia, which implies highly het-

      erogeneous conditions.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lee2018
  proposal_id: R005
  review_status_sha256: f8027a770804a5679e356524670b9968b5d633b1541b73fac77611c102d93c10
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
        A/passages.json: 88e4d02e0fde8539aa436fe9c2a8de6157a184af56cb0ce1b3d28eb2dbcbee3b
        A/raw.json: 77b559b4582fa5c82d234a270c0ab35bf23668b702e64d7f2fdfe218fc68f37f
        A/source-units.json: 235a29ceaebaea95add8f955d1ebe2fad9be566e0c463522427dad0ee71e9c6b
        A/full-source-units.json: bd44a81926fd8d8ccfb398ed8638dd407e236c7c70dd8caf0d942e3b08fa3fed
        A/meta.json: f97b532c7f3ea16e76321b25417069a71a95298bf9c9d07e263095f989b7e02c
        A/table-images/TABLE-1-page-3-1.png: 457f148b9f508050a02b3de32d842f4be8bd225430ce379d0c760a9cd0241a99
        A/table-images/page-3.png: 9ca6ce72e6497eec63e1712ed15ee1d5e11c33b97eec138023167bc00a07720d
        A/table-images/page-4.png: 574655fd264c1f2b1b0c821d155502bb5335151cce3b922630395c73d8398ca7
        A/table-images/TABLE-3-page-4-2.png: 75edfc5826d3bb755a194d651594189df7d662ab7162e70dca2780784e7333dc
        A/table-images/manifest.json: 2cb54357916175b1f29349d93b48e8a45f7a1ef966990f20d9b7e777c1423054
        A/table-images/TABLE-2-page-4-1.png: fd48330a446a351f18e635e1d0864fe21a246ebda14f11f6612328dccc932fc2
        A/clauses/window-03/raw.json: a8258c7f3d46270d89c1d21b98330625734a9d7413b695b75e25cb217854e95a
        A/clauses/window-03/prompt.txt: f4e13afc443db49316fd0c00bbea36fa5ebfd5e762672ff1fdac49494a89192a
        A/clauses/window-03/meta.json: 89b721b498f869b35341e59f2504a99258a1c7ba44f4de63306daff414dfefb6
        A/clauses/window-04/raw.json: 6a7e8a8afdac13c892544402bb8bada348ec4f8178767f85b329d695ad733a28
        A/clauses/window-04/prompt.txt: b801c0a9b16f16707dfe0c1955b2566c498f29421c20eab7bf8ae33261890429
        A/clauses/window-04/meta.json: 972f8b3160560fcbc87a678807e5d1f95e65350d932159d95a356ce83378c8e2
        A/clauses/window-02/raw.json: 271ae73f46ab17c236a3654e3d7d46a914600de881fe399c6598faef18d17531
        A/clauses/window-02/prompt.txt: 2b3a3c862ece179fed73a70be74d2f1f72969c05c6d23875ebbac5bc6d1a38c2
        A/clauses/window-02/meta.json: 2bc77b16ec42a9ee75454435dc95285cc9fbf9147ce64eda8fabeb8781e8179e
        A/clauses/window-01/raw.json: 5359363b3682f98d9c8e66df7b180cdde6bf9cd911bf0caa5848d1dbf026dfeb
        A/clauses/window-01/prompt.txt: a559f7abd5a1eef879179397b9ba062330b1a68ca244d2326799d0fa9899830e
        A/clauses/window-01/meta.json: 6342916a4761e8a98122ba8e3e55cd03f4943de2a9ba18c0c581225404cbee63
        A/tables/TABLE-1-page-3-1/raw.json: df868718f1f385638710c21376e0e7529d9309348cce6ac7abe641af51977be9
        A/tables/TABLE-1-page-3-1/prompt.txt: e91296239c33125f9cb7731b74df8e3600fa94f7b3f8c603afa24beddb0c8610
        A/tables/TABLE-1-page-3-1/meta.json: ef47aad4142d1077b6cde52b28af52abc86bd07e6a72814effae04501ed193f0
        A/tables/TABLE-3-page-4-3/raw.json: adf1d67c8455bca4066d6d6d2d9d63dd88444304756232ec2e00fc07a1050795
        A/tables/TABLE-3-page-4-3/prompt.txt: 08e4a547b7cef8de8a089ebc7fce70dc7b37cac26946d3a261b28d5bf65f90eb
        A/tables/TABLE-3-page-4-3/meta.json: 6d4b008011d1b7c39b10156fa0408fc69440e30f7bdeaa5b1a77f38d830c3f69
        A/tables/TABLE-2-page-4-2/raw.json: a46b9ff9b5d5ca5fe194299af7859c224be1e198ba8dea7b85b3cc85fa849211
        A/tables/TABLE-2-page-4-2/prompt.txt: 0803322b9832a451eb58a17a04e806b2ef96558d9bbad64e487e2ee3f4ce8223
        A/tables/TABLE-2-page-4-2/meta.json: 1f824e79c8507154547b6d8d19edf5217c9d8d8ae43d4c35490a2d74987fda78
        B/passages.json: 88e4d02e0fde8539aa436fe9c2a8de6157a184af56cb0ce1b3d28eb2dbcbee3b
        B/raw.json: 26cfa107ec34a561d36983d4435de09c5ce0cfaf6698d510e3dd4ff6d4767a92
        B/source-units.json: 235a29ceaebaea95add8f955d1ebe2fad9be566e0c463522427dad0ee71e9c6b
        B/full-source-units.json: bd44a81926fd8d8ccfb398ed8638dd407e236c7c70dd8caf0d942e3b08fa3fed
        B/meta.json: 1cb69cba4ecb721af59fd3d1c27a7beafeef8a18f0ac060b85c3acaa32868159
        B/table-images/TABLE-1-page-3-1.png: 457f148b9f508050a02b3de32d842f4be8bd225430ce379d0c760a9cd0241a99
        B/table-images/page-3.png: 9ca6ce72e6497eec63e1712ed15ee1d5e11c33b97eec138023167bc00a07720d
        B/table-images/page-4.png: 574655fd264c1f2b1b0c821d155502bb5335151cce3b922630395c73d8398ca7
        B/table-images/TABLE-3-page-4-2.png: 75edfc5826d3bb755a194d651594189df7d662ab7162e70dca2780784e7333dc
        B/table-images/manifest.json: be548c3cecb5974647dd535134b5302980235d01da80a06d07a04132d8de8ac4
        B/table-images/TABLE-2-page-4-1.png: fd48330a446a351f18e635e1d0864fe21a246ebda14f11f6612328dccc932fc2
        B/clauses/window-03/raw.json: 4efb4bc490d07c6a3be4ad991e24a33ae42908149cec214dab868c388c2ba77a
        B/clauses/window-03/prompt.txt: f4e13afc443db49316fd0c00bbea36fa5ebfd5e762672ff1fdac49494a89192a
        B/clauses/window-03/meta.json: 01762c54b141bb4083178474f44379361ee9c62daba2d559139350b07e491c64
        B/clauses/window-04/raw.json: 009c06d54b8cc24c6782b9ac62aa5e447946e75c49f7944dc7a5a3924b05877b
        B/clauses/window-04/prompt.txt: b801c0a9b16f16707dfe0c1955b2566c498f29421c20eab7bf8ae33261890429
        B/clauses/window-04/meta.json: 0dca92aacbb6c498ddec5d6f3a74bec58047ef87efea4c0c0c87f6b4b4863f54
        B/clauses/window-02/raw.json: c78467b9b7982d5915402a17c21f6538a1bbf4b9ee92d0672eecadf68b1a2bf1
        B/clauses/window-02/prompt.txt: 2b3a3c862ece179fed73a70be74d2f1f72969c05c6d23875ebbac5bc6d1a38c2
        B/clauses/window-02/meta.json: 672908037b2bd9c06ac27e93a06a015b62bd2f57033fbd5bfa223026bdc8afeb
        B/clauses/window-01/raw.json: 14e002ca1a3824af62cab380000651841c3d295ffd1bf01260d40069080cb714
        B/clauses/window-01/prompt.txt: a559f7abd5a1eef879179397b9ba062330b1a68ca244d2326799d0fa9899830e
        B/clauses/window-01/meta.json: e04bd723c1a9fcf2dea7e6af206e425bfe54fa90755cb010a8e3f78cbef64766
        B/tables/TABLE-1-page-3-1/raw.json: e6e7b05a8cc2aad6d7b3aaeb93304658142e0300332afb5c2f801c6572bde7f9
        B/tables/TABLE-1-page-3-1/prompt.txt: e91296239c33125f9cb7731b74df8e3600fa94f7b3f8c603afa24beddb0c8610
        B/tables/TABLE-1-page-3-1/meta.json: e1f7018aebbddf1f10a87430dceb06b37fd13e9346d428c1b429151aabdf919c
        B/tables/TABLE-3-page-4-3/raw.json: 24cdaefe9c2364302cc80a9c6db909e001ed50df461e6f8528a56f22aae0c0cc
        B/tables/TABLE-3-page-4-3/prompt.txt: 08e4a547b7cef8de8a089ebc7fce70dc7b37cac26946d3a261b28d5bf65f90eb
        B/tables/TABLE-3-page-4-3/meta.json: de5f9511a17a3be33dc6b3c6d30aad472c113cde49f5c1561df8144e5b7957d5
        B/tables/TABLE-2-page-4-2/raw.json: d8bb8a09f38c401fae6179f9b316fbb5f9d7daa3cbbc4c886096dbbe8a9838b7
        B/tables/TABLE-2-page-4-2/prompt.txt: 0803322b9832a451eb58a17a04e806b2ef96558d9bbad64e487e2ee3f4ce8223
        B/tables/TABLE-2-page-4-2/meta.json: 4d08698ab27db48598a80db03bf669e9778eb2a8b4b81e7f48cd041c66615a9b
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
      pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
      source_review: _compare/relationships-2026-11-16/review-current/Lee2018
      source_status_sha256: bc27e07987d1b4d499016f9e031d7b2c6468fc2097367674e270e6cd356449df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: mild-to-moderate aphasia (group 1)
    outcome:
      text: FA in the right superior longitudinal fasciculus
    analysis_label: Diffusion tensor imaging (DTI) analysis
    relation: association
    evidence_ids:
    - P3-S1-C2
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
      pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
      source_review: _compare/relationships-2026-11-16/review-current/Lee2018
      source_status_sha256: bc27e07987d1b4d499016f9e031d7b2c6468fc2097367674e270e6cd356449df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C4
      - Result passage disposed without unit P2-S3-C5
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C9
      - Accounting without a linked unit P5-S2-C8
      - Unaccounted source passage P5-S2-C8
      - Result passage disposed without unit P5-S2-C9
      unattached_null_or_qualifier_ids:
      - P5-S1-C9
      - P5-S1-C12
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 87
      unselected_timing_passages:
      - P2-S1-C3
      - P4-S1-C6
      - P5-S1-C15
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: limitations
        source_ids:
        - P5-S1-C6
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C15
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C5
        - P5-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-3
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
      source_review: _compare/relationships-2026-11-16/review-current/Lee2018
      source_status_sha256: bc27e07987d1b4d499016f9e031d7b2c6468fc2097367674e270e6cd356449df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Restatement of findings regarding white matter volume and FA in severe
        aphasia group.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contains demographic age data.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contains descriptive stroke duration data.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding regarding demographics (age/duration).
    - source_id: P2-S3-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Establishes lesion volume difference between groups.
    - source_id: P2-S3-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes lower left hemispheric white matter volume in group 2.
    - source_id: P2-S3-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes null difference in other segmented volumes.
    - source_id: P2-S3-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes trend of greater right hemisphere gray matter volume in
        patients.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes lower FA in specific bilateral regions for group 2.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes greater FA in right SLF for group 1 vs group 2.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion statement.
    - source_id: P4-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of left white matter volume finding.
    - source_id: P4-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of structural integrity (FA) findings.
    - source_id: P4-S2-C6
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of right hemisphere gray matter volume trend.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of asymmetry.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of asymmetry in severe group.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretive statement about gray matter hypertrophy and prognosis.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretive statement linking FA to functional outcome.
    - source_id: P5-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of lack of change in specific areas.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of data reflecting global changes.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about study limitation (sample size).
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C6
    - P2-S3-C4
    - P2-S3-C5
    - P2-S3-C6
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C3
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C9
    - P5-S1-C12
    - P5-S2-C4
    - P5-S2-C8
    - P5-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-4-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C3
      - P2-S1-C5
      recruited_sample:
      - P2-S1-C3
      - P2-S1-C5
      eligibility:
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C6
      imaging_provenance:
      - P2-S2-C10
      - P2-S2-C11
      imaging_timing:
      - P2-S1-C1
      outcome_timing:
      - P2-S1-C1
      outcome_definition:
      - P2-S1-C10
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S2-C13
      - P2-S2-C14
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P4-S1-C6
      - P5-S1-C13
      - P5-S1-C15
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: limitations
      source_ids:
      - P5-S1-C6
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C15
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
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
      pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
      review_sha256: f8027a770804a5679e356524670b9968b5d633b1541b73fac77611c102d93c10
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
      - P3-S1-C2
      source_result: Group 1 (mild-to-moderate aphasia) exhibited significantly greater
        fractional anisotropy (FA) in the right superior longitudinal fasciculus than
        Group 2 (severe aphasia) (P < 0.05).
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the comparison of FA in the
            right superior longitudinal fasciculus between the mild-to-moderate and
            severe aphasia groups, as described in P3-S1-C2. The proposed core correctly
            identifies this specific comparison.
          source_ids:
          - P3-S1-C2
          - P2-S1-C11
        direction:
          answer: fits
          reason: 'The source states that Group 1 (mild-to-moderate) had significantly
            greater FA than Group 2 (severe). The proposed core claim preserves this
            direction: ''Patients with mild-to-moderate aphasia exhibited significantly
            greater fractional anisotropy... than patients with severe aphasia.'''
          source_ids:
          - P3-S1-C2
        construct:
          answer: fits
          reason: The exposure is aphasia severity (grouped), the outcome is FA in
            the right SLF, and the method is DTI. The source confirms FA was determined
            in specific language-related areas including the superior longitudinal
            fasciculus (P2-S2-C10) and that the comparison was made between the two
            aphasia groups (P3-S1-C2). The patient measurement is voxel-based tissue
            analysis (FA maps), not template lesion overlap or patient diffusion tractography.
          source_ids:
          - P2-S2-C10
          - P3-S1-C2
          - P2-S2-C6
        qualifications:
          answer: fits
          reason: The proposed core includes the group definitions (mild-to-moderate
            vs severe) and limitations (small sample size, heterogeneous aphasia types)
            which are supported by P2-S1-C11, P5-S2-C3, and P5-S1-C11. No material
            qualifiers are lost.
          source_ids:
          - P2-S1-C11
          - P5-S2-C3
          - P5-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The core captures the primary finding and relevant limitations.
            The unresolved image reading disagreements in P2-S1-C3 and P4-S1-C6 do
            not alter the core relationship of FA in the right SLF between the two
            groups, as the group definitions and the specific FA result are clearly
            stated in other passages (P2-S1-C11, P3-S1-C2).
          source_ids:
          - P3-S1-C2
          - P5-S2-C3
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 23
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: Concurrent assessment; more than 6 months since onset of stroke (average
        60.2 to 88.3 months)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6, 60.2, 88.3'
    analysis_identity:
      id: R005
      exposure:
        text: mild-to-moderate aphasia (group 1)
      outcome:
        text: FA in the right superior longitudinal fasciculus
      analysis_label: Diffusion tensor imaging (DTI) analysis
      relation: association
      evidence_ids:
      - P3-S1-C2
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
        pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
        source_review: _compare/relationships-2026-11-16/review-current/Lee2018
        source_status_sha256: bc27e07987d1b4d499016f9e031d7b2c6468fc2097367674e270e6cd356449df
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 48902e81684e4ddb5f1b0c74518f6e1deeb21d419a3b40b1087bc4279e1c1f81
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C3
          page: 2
          text_layer_sha256: 48902e81684e4ddb5f1b0c74518f6e1deeb21d419a3b40b1087bc4279e1c1f81
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Patients

          Twenty-three patients with left hemisphere stroke with

          aphasia were recruited in accordance with the following

          criteria: (a) native Korean speaker; (b) first ever stroke in

          the left hemisphere, confirmed by MRI or computed

          tomography; (c) supra tentorial stroke; (d) at least 18 years

          of age; (e) right handedness before the stroke; (f) more

          than 6 months since onset of stroke; and (g) mild to

          severe speech disturbance, determined by standardized

          language evaluation.'
        anchor_text: 'Patients

          Twenty-three patients with left hemisphere stroke with

          aphasia were recruited in accordance with the following

          criteria: (a) native Korean speaker; (b) first ever stroke in

          the left hemisphere, confirmed by MRI or computed

          tomography; (c) supra tentorial stroke; (d) at least 18 years

          of age; (e) right handedness before the stroke; (f) more

          than 6 months since onset of stroke; and (g) mild to

          severe speech disturbance, determined by standardized

          language evaluation.'
        excluded_fragments: []
        image_sha256: 4e43d4298377eac7c2cc7262a8498ab31fcde04f5ba1e371b2678bf2a819d201
      P2-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 652de4db2eb03604e38a7a2ee6caf7f283c3008ce0f3b624e2a7059aa9133ecf
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c58916b0c614be2e839ca26a874d69b7e268613d738029bf1a3898c00f08c0c2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C11
          page: 2
          text_layer_sha256: c58916b0c614be2e839ca26a874d69b7e268613d738029bf1a3898c00f08c0c2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients were assigned to one of

          two groups on the basis of aphasia severity – mild to

          moderate (group 1; 11 patients) and severe (group 2; 12

          patients; Table 1) aphasia groups.'
        anchor_text: 'Patients were assigned to one of

          two groups on the basis of aphasia severity – mild to

          moderate (group 1; 11 patients) and severe (group 2; 12

          patients; Table 1) aphasia groups.'
        excluded_fragments: []
        image_sha256: 0b1cb3333e8a41bcca563dfd821736d9b95d15b5ed0147ffb916ee74a7ee652c
        transcription: '. Patients were assigned to one of

          two groups on the basis of aphasia severity – mild to

          moderate (group 1; 11 patients) and severe (group 2; 12

          patients; Table 1) aphasia groups'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'Group 1 exhibited significantly greater FA in the right

    superior longitudinal fasciculus than group 2 (P < 0.05;

    Table 3).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
