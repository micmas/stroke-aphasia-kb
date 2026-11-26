---
id: left_temporal_bc
name: left temporal betweenness centrality
kind: network
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: At baseline, lower left temporal nodal betweenness centrality showed a trend toward more severe aphasia (lower WAB-AQ), controlling for age, time poststroke and lesion size (model F=3.97, P=.011, R²=.58).
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke occurring at least 6 months prior to enrollment
    phase: not_reported
    time_post_onset: Baseline pretreatment assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The use of Brodmann areas as ROIs provides limited resolution to detect abnormalities within smaller or more localized subregions.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Average nodal betweenness centrality (BC) of left temporal regions of interest (BAs 20, 21, 22, 37, 38) derived from a structural connectome constructed via probabilistic DTI fiber tracking. Authors describe a trend; model F=3.97, P=.011, R²=.58; Adjusted for age, time poststroke and lesion size. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Restore selected analysis: baseline WAB-AQ, not treatment gain. Authors call the adjusted left temporal-BC relationship a trend (model P=.011); do not present this as a corrected significant prognostic effect.'
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
  - section: Original source P3-S2-C12
    page: 3
    quote: "Preprocessing of MRI Data and Connectome \nConstruction\nThe preprocessing steps involved in the construction of the \nindividual connectome involved the following: (a) segmen-\ntation of the probabilistic gray matter map (from \nT1-weighted images), further divided into cortical anatomi-\ncal regions of interest (ROIs) corresponding to BAs; (b) \nsegmentation of the probabilistic white matter map from \nT1-weighted images; (c) registration of the individual white \nmatter map and cortical ROIs into the individual DTI space; \n(d) probabilistic DTI fiber tracking; (e) iterative evaluation \nof the number of tractography streamlines connecting each \npossible pair of ROIs; (f) correction of each pair-wise con-\nnection strength (ie, number of streamlines) based on the \nvolume of the connected ROIs and the distance travelled by \n"
    supports: method
  - section: Original source P6-S2-C4
    page: 6
    quote: "Relationship Between Baseline Language \nPerformance and Structural Connectivity\nWe observed a relationship trend between more severe \naphasia (measured as lower WAB-AQ) and lower left tem-\nporal BC (F = 3.97, P = .011, model R = .76, model R2 = \n.58), controlling for age, time since the stroke, and stroke \nlesion size."
    supports: claim
  - section: Original source P6-S2-C6
    page: 6
    quote: "This trend suggests that loss of influence from left \ntemporal nodes onto the general network was associated \nwith more severe forms of aphasia at baseline (Figure 5 and \nSupplemental Table 2)."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Bonilha2016
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis of the relationship between left temporal nodal betweenness centrality and naming improvement is fully supported by the text, including the specific measurement method (DTI-based connectome), the population (chronic aphasia), and the specific control variables used in the regression.
    bucket: predictors
    entity_id: left_temporal_bc
    name: left temporal betweenness centrality
    kind: network
    predictor_type: imaging_metric
    definition: Average nodal betweenness centrality (BC) of left temporal regions of interest (BAs 20, 21, 22, 37, 38) derived from a structural connectome constructed via probabilistic DTI fiber tracking.
    assessment:
    - Philadelphia Naming Test
    target: naming_improvement
    target_kind: prognosis
    claim: Higher left temporal nodal betweenness centrality was associated with greater treatment-related improvement in naming, when controlling for age, time since stroke, stroke lesion size, and baseline aphasia severity.
    direction: likely
    method: DTI
    relationship: correlational
    therapy:
      id: anomia_treatment
      name: anomia treatment using semantic and phonological cueing hierarchies
    sample_n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke occurring at least 6 months prior to enrollment
    timing: Imaging and baseline assessment performed prior to a 2-week intense therapy period; outcome measured within 1 week after treatment completion.
    qualifications:
    - Treatment-related improvement was defined as the ratio of new items correctly named on the PNT to the number of pretreatment incorrect responses.
    limitations:
    - The use of Brodmann areas as ROIs provides limited resolution to detect abnormalities within smaller or more localized subregions.
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P6-S2-C9
      supports: claim
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P3-S1-C9
      supports: method
    - source_id: P5-S1-C6
      supports: claim
    - source_id: P3-S2-C12
      supports: method
    - source_id: P12-S1-C6
      supports: claim
    - source_id: P5-S2-C2
      supports: claim
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
    proposal: R007
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 0.005036250000557629
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      original_mapping_sha256: fe8e5ee1b52d028a59ac8dd670f24c1fda3112d810e43874ec4f161f36b3f0b3
      original_status_sha256: 77e6839099c5645a3daef961062b422d638a048446b448ccfec695b60c7d807b
      evidence_sha256: 5a1e799e3da87bcb49755f6532aee5748ba56e3a8601ff5d094548e784776f1c
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 3
      - 5
      - 6
      note: 'Restore selected analysis: baseline WAB-AQ, not treatment gain. Authors call the adjusted left temporal-BC relationship a trend (model P=.011); do not present this as a corrected significant prognostic effect.'
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
  note: 'Restore selected analysis: baseline WAB-AQ, not treatment gain. Authors call the adjusted left temporal-BC relationship a trend (model P=.011); do not present this as a corrected significant prognostic effect.'
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
