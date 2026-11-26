---
id: left_frontal_parietal_network_measures
name: Left frontal and parietal network measures
kind: predictor
findings:
- id: f1
  target: naming_improvement
  target_kind: prognosis
  claim: Regional network measures from left frontal and parietal areas were not significantly associated with treatment-related naming improvement.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke occurring at least 6 months prior to enrollment
    phase: not_reported
    time_post_onset: Imaging and baseline assessment performed prior to a 2-week intense therapy period; naming improvement measured within 1 week after treatment completion.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Use of large predefined Brodmann area ROIs may limit resolution to detect abnormalities in smaller subregions
  - Heterogeneous population pooling different aphasic syndromes
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Regional network measures from left frontal (BA44,45,46) and parietal (BA7,39,40,41) nodes of patient-specific probabilistic diffusion tractography connectomes. Regional frontal/parietal null contrasts are distinct from the positive left temporal BC finding. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Restore selected analysis: frontal/parietal regional-network null results, not the temporal-BC positive result already captured by R001. Patient-specific connectomes confirmed.'
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
  therapy:
    id: anomia_treatment
    name: anomia treatment using semantic and phonological cueing hierarchies
  citation: '@Bonilha2016'
  source_passages:
  - section: Original source P2-S3-C4
    page: 2
    quote: "Methods\nSubjects\nWe studied 24 individuals recruited from the local com-\nmunity with chronic aphasia as a result of a left hemi-\nsphere ischemic stroke that occurred at least 6 months \nprior to enrolling in this study."
    supports: sample
  - section: Original source P3-S1-C9
    page: 3
    quote: "Baseline MRI Scanning\nAll subjects underwent MRI scanning at USC in a 3T \nSiemens Trio equipped with a 12-channel head coil in \naccordance with the following protocol: (a) T1-weighted \nimages (3D MP-RAGE, TR = 2250 ms, TE = 4.15 ms, 256 \n× 256 matrix, 256 × 256 mm FOV, parallel imaging \nGRAPPA = 2, 80 reference lines, TA = 377 s); (b) Diffusion \nEPI scan (30-directions with b = 1000 s/mm2 and b = 2000 \ns/mm2, TR = 6100 ms, TE = 101 ms, 82 × 82 matrix, 222 × \n222mm FOV, parallel imaging GRAPPA = 2, 80 45 contigu-\nous 2.7 mm axial slices, TA = 390 s)."
    supports: method
  - section: Original source P5-S2-C1
    page: 5
    quote: "influence network architecture or naming improvement, \nsuch as age (at the time of the study enrollment), time since \nthe stroke, overall aphasia severity (WAB-AQ), and the vol-\nume of the necrotic stroke lesion."
    supports: confounders
  - section: Original source P6-S2-C11
    page: 6
    quote: "We did not observe a significant relationship between \ntreatment-related improvement in naming and regional net-\nwork measures from the frontal or parietal areas \n(Supplemental Table 2)."
    supports: claim
  - section: Original source P8-S2-C4
    page: 8
    quote: "Fourth, we did not observe a relationship between \nstructural integrity of other brain regions (frontal or parietal) \nand treatment-related improvement."
    supports: claim
predictor_type: imaging_metric
short_definition: Regional network measures from left frontal (BA44,45,46) and parietal (BA7,39,40,41) nodes of patient-specific probabilistic diffusion tractography connectomes.
assessment:
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Bonilha2016
  proposal_id: R004
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a robust association between higher left temporal nodal betweenness centrality (BC) and treatment-related improvement in naming, controlling for age, time since stroke, lesion size, and baseline aphasia severity. It also explicitly reports a null finding for frontal and parietal BC.
    bucket: predictors
    entity_id: left_temporal_bc
    name: left temporal BC cluster
    kind: network
    predictor_type: imaging_metric
    definition: Average nodal betweenness centrality (BC) of left-sided ROIs corresponding to Brodmann areas 20, 21, 22, 37, and 38, derived from a structural connectome constructed via probabilistic DTI fiber tracking and adjusted for ROI volume and streamline distance.
    assessment:
    - Philadelphia Naming Test
    target: naming_improvement
    target_kind: prognosis
    claim: Higher left temporal nodal betweenness centrality (BC) is associated with greater treatment-related improvement in naming, while regional network measures from frontal or parietal areas showed no significant relationship with naming improvement.
    direction: likely
    method: DTI
    relationship: correlational
    therapy:
      id: anomia_treatment
      name: anomia treatment using semantic and phonological cueing hierarchies
    sample_n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke occurring at least 6 months prior to enrollment
    timing: Imaging and baseline assessment performed prior to a 2-week intense therapy period; naming improvement measured within 1 week after treatment completion.
    qualifications:
    - Analysis controlled for age, time since stroke, stroke lesion size, and baseline aphasia severity (WAB-AQ)
    - Naming improvement was defined as the ratio of new items correctly named on the PNT to the number of pretreatment incorrect responses
    limitations:
    - Small sample size
    - Use of large predefined Brodmann area ROIs may limit resolution to detect abnormalities in smaller subregions
    - Heterogeneous population pooling different aphasic syndromes
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P6-S2-C9
      supports: claim
    - source_id: P6-S2-C11
      supports: claim
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P3-S1-C9
      supports: method
    - source_id: P5-S1-C6
      supports: claim
    - source_id: P5-S2-C2
      supports: claim
    - source_id: P12-S1-C6
      supports: claim
    - source_id: P5-S2-C1
      supports: confounders
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      review_sha256: 30e5e988583897e38833369847bb311ba30b35e2168057e5f40d9744755cc14a
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
    proposal: R004
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P6-S2-C11
      - P8-S2-C4
    seconds_this_run: 0.009886124997137813
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      original_mapping_sha256: b9f242ff59c9c13176a599d2839a94734735015fb4cbcacbb3f1390d3c8b6ae3
      original_status_sha256: 4be553ff0416263f2fc4fe3d22806270e091ccd38f537320b7f18c870ef12635
      evidence_sha256: 5a1e799e3da87bcb49755f6532aee5748ba56e3a8601ff5d094548e784776f1c
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 3
      - 4
      - 5
      - 6
      - 8
      - 12
      note: 'Restore selected analysis: frontal/parietal regional-network null results, not the temporal-BC positive result already captured by R001. Patient-specific connectomes confirmed.'
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round3.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round3
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: 'Restore selected analysis: frontal/parietal regional-network null results, not the temporal-BC positive result already captured by R001. Patient-specific connectomes confirmed.'
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
