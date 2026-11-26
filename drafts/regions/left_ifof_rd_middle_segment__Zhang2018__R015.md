---
id: left_ifof_rd_middle_segment
name: left IFOF middle segment cluster
kind: network
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: Compared with healthy controls, patients classified as having post-stroke aphasia had increased RD in the middle left IFOF (nodes 30–46 and 60–73). This is a group contrast; TBSS did not detect significant RD-language correlations.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: 11 analyzed patients classified as having post-stroke aphasia and 11 healthy controls; 3 recruited patients were excluded.
    phase: not_reported
    time_post_onset: MRI scans completed 14 ± 2 days after stroke; behavioral assessment 10 ± 2 days after onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient diffusion tensor metrics measured by AFQ for group contrasts or TBSS for language associations, as specified in the claim. Patient-control differences must not be interpreted as correlations with aphasia severity. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - agent_source_repair_pending_human_review
  citation: '@Zhang2018'
  source_passages:
  - section: Original source P5-S3-C2
    page: 5
    quote: "AD in the left IFOF was mainly reduced in the \noccipital and posterior temporal sections (0–43th point), whilst \nRD increased in the middle segment (30–46th and 60th–73rd \npoint)."
    supports: claim
  - section: Original source P8-S1-C5
    page: 8
    quote: "The vertical scale refers to diffusion metrics, and the segments \nwith significant difference are marked in different colors, yellow for FA, light blue for AD, and pink for RD (all corrected p < 0.05)."
    supports: claim
  - section: Original source P3-S3-C11
    page: 3
    quote: "Automated Fiber Quantification\nWe performed AFQ (version 1.2; Stanford University, California, \nUSA;2) to enable further quantitative analysis along the major \ntracts."
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: "Finally, 100 equidistant nodes were resampled along the central \nportion of the tract in each fiber group, and the mean location \nof each node in the fiber group core was calculated."
    supports: method
  - section: Original source P4-S2-C7
    page: 4
    quote: "Language function was \nassessed 10 ± 2 days after onset, and MRI scans were completed \nafter 14 ± 2 days."
    supports: sample
  - section: Original source P4-S2-C8
    page: 4
    quote: "Two patients were removed because of obvious \nhead motion, and one sample with damaged data storage was \nexcluded."
    supports: sample
  design: cross-sectional
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2018
  proposal_id: R015
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study used AFQ to compare diffusion metrics of the left IFOF between subacute aphasic patients and healthy controls, finding a significant increase in radial diffusivity (RD) specifically in the middle segment of the tract.
    bucket: regions
    entity_id: left_ifof_rd_middle_segment
    name: left IFOF middle segment cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient radial diffusivity (RD) measured via automated fiber quantification (AFQ) in the middle segment (nodes 30-46 and 60-73) of the left inferior fronto-occipital fasciculus (IFOF).
    assessment:
    - Automated Fiber Quantification (AFQ)
    target: post_stroke_aphasia
    target_kind: impairment
    claim: Radial diffusivity (RD) in the middle segment of the left IFOF was increased in patients with post-stroke aphasia compared to healthy controls.
    direction: likely
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 14
    population: subacute post-stroke patients with left hemisphere infarction and aphasia
    timing: MRI scans completed 14 ± 2 days after stroke; behavioral assessment 10 ± 2 days after onset
    qualifications:
    - Comparison made against 11 age-, sex- and education-matched healthy controls
    - Point-wise comparison identified the middle segment (30-46th and 60th-73rd points) as the area of increased RD
    limitations:
    - Small sample size
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S3-C2
      supports: claim
    - source_id: P2-S3-C12
      supports: sample
    - source_id: P4-S2-C7
      supports: method
    - source_id: P3-S3-C11
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      review_sha256: 905ac8d1292336fa44ac6fa433bde54c7249a3a1ffbf24814f53692ea7de7fd5
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    proposal: R015
    status: hold
    reason: 'analysis_identity: The selected analysis label is ''AFQ point-wise comparison'' and the evidence ID P5-S3-C2 describes a between-group difference (patients vs. controls) in RD. However, the proposed core defines the outcome as ''post-stroke aphasia'' (implying a correlation with language scores) and the relationship as ''correlational''. The source explicitly separates group differences (P5-S2-C8, P5-S3-C2) from correlations with language performance (P5-S3-C7, P5-S3-C9). P5-S3-C2 is a group comparison, not a correlation with aphasia severity.; direction: The proposed core claims an association between RD and ''post-stroke aphasia'' (implying higher RD correlates with worse/better aphasia). The source P5-S3-C2 reports that RD was *increased* in patients compared to controls. While increased RD is associated with the presence of aphasia (group difference), the proposed core frames it as a correlational relationship with the outcome ''post-stroke aphasia'' without specifying if
      it correlates with severity or just presence. More critically, the source distinguishes this group difference from the correlation analyses. If the core intends to represent the group difference, the outcome should be ''presence of aphasia'' or ''group status'', not ''post-stroke aphasia'' as a continuous outcome in a correlational model. If it intends to represent the correlation, P5-S3-C2 is the wrong evidence ID (correlations are in P5-S3-C9/P6-S1-C10). Given the evidence ID P5-S3-C2, the direction is ''increased in patients'', which is a group difference, not a correlation direction.; construct: The exposure is ''left IFOF RD (middle segment)'' which matches P5-S3-C2. However, the outcome is ''post-stroke aphasia'' and the relationship is ''correlational''. P5-S3-C2 is a between-group t-test (patients vs controls), not a correlation with aphasia scores. The correlation analyses are described in P5-S3-C7 and P5-S3-C9, which focus on FA, not RD (P5-S2-C7 states no significant correlations
      for RD). Therefore, the construct of ''RD correlates with aphasia'' is not supported by P5-S3-C2, and the construct of ''RD differs by group'' is mislabeled as ''correlational'' with outcome ''aphasia'' (which usually implies severity).; missing_material_caveat: The core fails to distinguish between the group difference (P5-S3-C2) and the correlation analysis. It also omits the fact that RD did not show significant correlations with language scores (P5-S2-C7), which is a material caveat if the core implies a relationship with aphasia severity. The core conflates a group difference finding with a correlational outcome.'
    material_issues:
    - issue: 'analysis_identity: The selected analysis label is ''AFQ point-wise comparison'' and the evidence ID P5-S3-C2 describes a between-group difference (patients vs. controls) in RD. However, the proposed core defines the outcome as ''post-stroke aphasia'' (implying a correlation with language scores) and the relationship as ''correlational''. The source explicitly separates group differences (P5-S2-C8, P5-S3-C2) from correlations with language performance (P5-S3-C7, P5-S3-C9). P5-S3-C2 is a group comparison, not a correlation with aphasia severity.'
      source_ids:
      - P5-S3-C2
      - P5-S3-C7
      - P5-S3-C9
    - issue: 'direction: The proposed core claims an association between RD and ''post-stroke aphasia'' (implying higher RD correlates with worse/better aphasia). The source P5-S3-C2 reports that RD was *increased* in patients compared to controls. While increased RD is associated with the presence of aphasia (group difference), the proposed core frames it as a correlational relationship with the outcome ''post-stroke aphasia'' without specifying if it correlates with severity or just presence. More critically, the source distinguishes this group difference from the correlation analyses. If the core intends to represent the group difference, the outcome should be ''presence of aphasia'' or ''group status'', not ''post-stroke aphasia'' as a continuous outcome in a correlational model. If it intends to represent the correlation, P5-S3-C2 is the wrong evidence ID (correlations are in P5-S3-C9/P6-S1-C10). Given the evidence ID P5-S3-C2, the direction is ''increased in patients'', which is a
        group difference, not a correlation direction.'
      source_ids:
      - P5-S3-C2
      - P5-S3-C9
    - issue: 'construct: The exposure is ''left IFOF RD (middle segment)'' which matches P5-S3-C2. However, the outcome is ''post-stroke aphasia'' and the relationship is ''correlational''. P5-S3-C2 is a between-group t-test (patients vs controls), not a correlation with aphasia scores. The correlation analyses are described in P5-S3-C7 and P5-S3-C9, which focus on FA, not RD (P5-S2-C7 states no significant correlations for RD). Therefore, the construct of ''RD correlates with aphasia'' is not supported by P5-S3-C2, and the construct of ''RD differs by group'' is mislabeled as ''correlational'' with outcome ''aphasia'' (which usually implies severity).'
      source_ids:
      - P5-S3-C2
      - P5-S2-C7
      - P5-S3-C9
    - issue: 'missing_material_caveat: The core fails to distinguish between the group difference (P5-S3-C2) and the correlation analysis. It also omits the fact that RD did not show significant correlations with language scores (P5-S2-C7), which is a material caveat if the core implies a relationship with aphasia severity. The core conflates a group difference finding with a correlational outcome.'
      source_ids:
      - P5-S2-C7
      - P5-S3-C2
    seconds_this_run: 124.0392644170206
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      original_mapping_sha256: a7fa3d857053a4ae9c884966ca23475baeb92b23c7fbffaa051802fff8211dac
      original_status_sha256: 2c139f611a5a70222afdf81c86ab468ca936717012d770e0b5f1b7374500fff9
      evidence_sha256: 92d3763f80a751a9af742b6f8c638079625c24b6eeac041030cfd095d71d8913
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      note: Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
