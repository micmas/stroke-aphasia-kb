---
id: left_temporal_bc
name: left temporal BC
kind: predictor
findings:
- id: f1
  target: pnt_improvement
  target_kind: prognosis
  claim: Higher left temporal nodal betweenness centrality (BC) is associated with greater treatment-related improvement in naming.
  direction: likely
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
  - ROIs based on Brodmann areas are large and may encompass regions with distinct functions
  - Analysis relies on predefined regions of interest (a priori anatomical assumptions)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Average nodal betweenness centrality (BC) of left temporal regions of interest (BAs 20, 21, 22, 37, 38), derived from pretreatment probabilistic DTI fiber tracking and connectome construction. Association was found when controlling for age, time since stroke, stroke lesion size, and baseline aphasia severity (WAB-AQ); Baseline aphasia severity (WAB-AQ) was also associated with naming improvement, with less severe aphasia achieving higher improvement. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified pretreatment diffusion acquisition and patient-specific probabilistic tractography. BA atlas labels define nodes, not normative connectivity substituted for patient measurements. Outcome is PNT change after two weeks of anomia therapy; n=24, observational association adjusted for age, time, lesion size and baseline AQ.'
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
  - section: Original source P6-S2-C9
    page: 6
    quote: "Relationship Between Naming Improvement and \nRegional and Global Structural Connectivity\nWe observed a robust relationship between treatment-related \nimprovement in naming and a higher left temporal BC (con-\ntrolling for age, time since the stroke, stroke lesion size, and \nWAB-AQ) (model F = 6.79, P = .00077, model R = .86, \nmodel R2 = .74; Figure 5, Supplemental Table 2)."
    supports: claim
  - section: Original source P8-S1-C9
    page: 8
    quote: "Second, if temporal lobe regions \nremain integrated with the remaining network (ie, temporal \nlobe BC), a higher treatment-related improvement is also \nmore likely to occur."
    supports: claim
  - section: Original source P9-S3-C6
    page: 9
    quote: "Left Temporal Cortex Influence on the Global \nNetwork\nWe observed that the average BC from specific left temporal \ncortical ROIs was associated with naming recovery."
    supports: claim
  - section: Original source P2-S3-C4
    page: 2
    quote: "Methods\nSubjects\nWe studied 24 individuals recruited from the local com-\nmunity with chronic aphasia as a result of a left hemi-\nsphere ischemic stroke that occurred at least 6 months \nprior to enrolling in this study."
    supports: sample
  - section: Original source P5-S1-C6
    page: 5
    quote: "Thus, ROIs were grouped as follows: left frontal ROIs (BA \n= [44, 45, 46]), left parietal ROIs (BA = [7, 39, 40, 41]), \nand left temporal ROIs (BA = [20, 21, 22, 37, 38])."
    supports: method
  - section: Original source P3-S2-C3
    page: 3
    quote: "During each 3-hour treatment session, \nthe subject underwent clinician-administered anomia \ntreatment using semantic and phonemic cueing hierar-\nchies.31 As indicated earlier, the treatment approach used \nhere was not selected based on the cognitive-linguistic \nimpairment profile of any single patient or a subgroup of \npatients."
    supports: method
  - section: Original source P12-S1-C6
    page: 12
    quote: "Here, we evaluated \npatients within a week after a 2-week intense intervention."
    supports: method
  - section: Original source P6-S2-C10
    page: 6
    quote: "In this \nmodel, WAB-AQ was also associated with treatment-related \nimprovement in naming (T = 2.45, P = .03); patients with \nless severe aphasia achieved a higher naming improvement."
    supports: confounders
  - section: Original source P12-S1-C3
    page: 12
    quote: "We acknowledge, nonetheless, that \nthe ROIs of this atlas are large, usually encompassing differ-\nent brain regions that serve distinct functions (eg, anterior \nand posterior aspects of the temporal gyri)."
    supports: limitation
predictor_type: imaging_metric
short_definition: Average nodal betweenness centrality (BC) of left temporal regions of interest (BAs 20, 21, 22, 37, 38), derived from pretreatment probabilistic DTI fiber tracking and connectome construction.
assessment:
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Bonilha2016
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study identifies a robust association between pretreatment left temporal nodal betweenness centrality (BC) and subsequent naming improvement following an intense speech therapy intervention in chronic aphasia patients.
    bucket: predictors
    entity_id: left_temporal_bc
    name: left temporal BC
    kind: predictor
    predictor_type: imaging_metric
    definition: Average nodal betweenness centrality (BC) of left temporal regions of interest (BAs 20, 21, 22, 37, 38), derived from pretreatment probabilistic DTI fiber tracking and connectome construction.
    assessment:
    - Philadelphia Naming Test
    target: pnt_improvement
    target_kind: prognosis
    claim: Higher left temporal nodal betweenness centrality (BC) is associated with greater treatment-related improvement in naming.
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
    - Association was found when controlling for age, time since stroke, stroke lesion size, and baseline aphasia severity (WAB-AQ)
    - Baseline aphasia severity (WAB-AQ) was also associated with naming improvement, with less severe aphasia achieving higher improvement
    limitations:
    - ROIs based on Brodmann areas are large and may encompass regions with distinct functions
    - Analysis relies on predefined regions of interest (a priori anatomical assumptions)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P6-S2-C9
      supports: claim
    - source_id: P8-S1-C9
      supports: claim
    - source_id: P9-S3-C6
      supports: claim
    - source_id: P2-S3-C4
      supports: sample
    - source_id: P5-S1-C6
      supports: method
    - source_id: P3-S2-C3
      supports: method
    - source_id: P12-S1-C6
      supports: method
    - source_id: P6-S2-C10
      supports: confounders
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
    proposal: R001
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P6-S2-C9
      - P8-S1-C9
      - P9-S3-C6
    seconds_this_run: 0.011480333003419219
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1d5bdbddb82128be34f01363d54c6fff1d2ef675fb8c47d80d22dcc29fc809a6
      original_mapping_sha256: c060863178d52ce68995a673a014cf687d2f1fa84fa3b1473e95da803754c38f
      original_status_sha256: 8b14c6514f9ff2a672e44c3070c4f1ccca6146925bfdba1dee220362b423b674
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
      note: Verified pretreatment diffusion acquisition and patient-specific probabilistic tractography. BA atlas labels define nodes, not normative connectivity substituted for patient measurements. Outcome is PNT change after two weeks of anomia therapy; n=24, observational association adjusted for age, time, lesion size and baseline AQ.
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
  note: Verified pretreatment diffusion acquisition and patient-specific probabilistic tractography. BA atlas labels define nodes, not normative connectivity substituted for patient measurements. Outcome is PNT change after two weeks of anomia therapy; n=24, observational association adjusted for age, time, lesion size and baseline AQ.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
