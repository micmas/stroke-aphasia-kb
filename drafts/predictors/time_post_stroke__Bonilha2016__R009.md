---
id: time_post_stroke
name: Time since stroke
kind: predictor
findings:
- id: f1
  target: naming_improvement
  target_kind: prognosis
  claim: Time since stroke in months was not significantly correlated with change in correct naming after treatment (r=.08, P=.71).
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: imaging performed at baseline; naming improvement measured as the difference between pretreatment and posttreatment (within 1 week after a 2-week intense intervention) in patients whose stroke occurred at least 6 months prior to enrollment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - ROIs based on Brodmann areas are large and may encompass regions with distinct functions
  - heterogeneous population pooling different aphasic syndromes
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Months elapsed since stroke at study enrollment. Reported r=.08, P=.71; not proof that spontaneous recovery is absent. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Restore selected analysis: time poststroke versus naming gain, not temporal-BC connectivity. Null correlation r=.08, P=.71 does not establish that spontaneous recovery made no contribution.'
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
  - section: Original source P3-S1-C5
    page: 3
    quote: "Baseline Language Testing\nA certified speech pathologist administered and scored lan-\nguage performance at baseline based on the Western \nAphasia Battery (WAB)32 and the Philadelphia Naming Test \n(PNT).33 Together, these tests provide a measure of (a) \naphasia type and severity (WAB) and (b) naming perfor-\nmance (PNT)."
    supports: method
  - section: Original source P5-S1-C6
    page: 5
    quote: "Thus, ROIs were grouped as follows: left frontal ROIs (BA \n= [44, 45, 46]), left parietal ROIs (BA = [7, 39, 40, 41]), \nand left temporal ROIs (BA = [20, 21, 22, 37, 38])."
    supports: method
  - section: Original source P5-S2-C2
    page: 5
    quote: "Treatment-related improvement in naming was defined \nbased on the difference between pre- and posttreatment per-\nformance on the PNT, adjusted based on the potential for \nrecovery, as follows: the number of new items correctly \nnamed on the PNT was divided by the total number of items \nin the PNT [175] minus the number of correctly named \nitems at baseline."
    supports: method
  - section: Original source P12-S1-C6
    page: 12
    quote: "Here, we evaluated \npatients within a week after a 2-week intense intervention."
    supports: method
  - section: Original source P11-S2-C7
    page: 11
    quote: "First, we recruited \na heterogeneous population of chronic stroke patients, \npooling together different aphasic syndromes."
    supports: limitation
  - section: Original source P12-S1-C3
    page: 12
    quote: "We acknowledge, nonetheless, that \nthe ROIs of this atlas are large, usually encompassing differ-\nent brain regions that serve distinct functions (eg, anterior \nand posterior aspects of the temporal gyri)."
    supports: limitation
  - section: Original source P6-S1-C5
    page: 6
    quote: "No \nsignificant correlation was found between changes in correct \nnaming and time (months) poststroke (r = .08, P = .71)."
    supports: claim
  - section: Original source P8-S3-C7
    page: 8
    quote: "Importantly, we found no correlation \nbetween time poststroke and changes in naming before and \nafter treatment, suggesting that the significant gains in nam-\ning that are reported here are probably not driven by spon-\ntaneous recovery."
    supports: claim
predictor_type: demographic
short_definition: Months elapsed since stroke at study enrollment.
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Bonilha2016
  proposal_id: R009
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a robust association between left temporal nodal betweenness centrality (BC) and treatment-related naming improvement in chronic aphasia patients, controlling for age, time since stroke, lesion size, and baseline severity.
    bucket: predictors
    entity_id: left_temporal_bc
    name: left temporal nodal betweenness centrality
    kind: network
    predictor_type: imaging_metric
    definition: Average nodal betweenness centrality (BC) of left-sided ROIs corresponding to Brodmann areas 20, 21, 22, 37, and 38, calculated from a structural connectome derived from pretreatment diffusion tensor imaging (DTI) fiber tracking.
    assessment:
    - Philadelphia Naming Test
    target: naming_improvement
    target_kind: prognosis
    claim: Higher left temporal nodal betweenness centrality is associated with greater treatment-related improvement in naming of untrained items.
    direction: likely
    method: DTI
    relationship: correlational
    therapy:
      id: anomia_treatment
      name: anomia treatment using semantic and phonological cueing hierarchies
    sample_n: 24
    population: patients with chronic aphasia resulting from a left hemisphere ischemic stroke
    timing: imaging performed at baseline; naming improvement measured as the difference between pretreatment and posttreatment (within 1 week after a 2-week intense intervention) in patients whose stroke occurred at least 6 months prior to enrollment
    qualifications:
    - controlled for age, time since stroke, stroke lesion size, and baseline aphasia severity (WAB-AQ)
    - improvement defined as the ratio of new items correctly named to the number of pretreatment incorrect responses on the PNT
    limitations:
    - ROIs based on Brodmann areas are large and may encompass regions with distinct functions
    - heterogeneous population pooling different aphasic syndromes
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P6-S2-C9
      supports: claim
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P3-S1-C5
      supports: method
    - source_id: P5-S1-C6
      supports: method
    - source_id: P5-S2-C2
      supports: method
    - source_id: P12-S1-C6
      supports: method
    - source_id: P11-S2-C7
      supports: limitation
    - source_id: P12-S1-C3
      supports: limitation
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
    proposal: R009
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 0.003748666997125838
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      original_mapping_sha256: 21079b8b4d1c3ffa6d134e3a396daf0e53fae02ed041b625c2bf311bec0142c6
      original_status_sha256: 7a5aefc4b0682d7ccfeace2ba22ca95c827d9c4237f2fa033a5bcbbb71fed297
      evidence_sha256: 5a1e799e3da87bcb49755f6532aee5748ba56e3a8601ff5d094548e784776f1c
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 3
      - 5
      - 6
      - 8
      note: 'Restore selected analysis: time poststroke versus naming gain, not temporal-BC connectivity. Null correlation r=.08, P=.71 does not establish that spontaneous recovery made no contribution.'
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
  note: 'Restore selected analysis: time poststroke versus naming gain, not temporal-BC connectivity. Null correlation r=.08, P=.71 does not establish that spontaneous recovery made no contribution.'
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
