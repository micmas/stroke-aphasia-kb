---
id: speech_language_disorder_fatigue_association__Riley2021__R002
name: speech-language disorder and post-stroke fatigue association
kind: review
findings:
- id: f1
  target: post_stroke_fatigue
  target_kind: impairment
  claim: Riley2021 reports, based on five reviewed studies with varied and sometimes contradictory results, that results from studies reporting data on the relationship between speech-language disorders and fatigue varied, but some concluded that speech disorders significantly predict post-stroke fatigue, that language domain scores on the NIH Stroke Scale correlate with fatigue, and that there is a greater prevalence of fatigue in those with speech impairments compared to those without at 2-years post-stroke.
  direction: mixed
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Riley2021; secondary evidence, not a newly recruited cohort. Attribution: five reviewed studies with varied and sometimes contradictory results'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary report.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Results occasionally contradicted one another
  - Unable to separate differences between speech vs. language disorders or receptive vs. expressive impairments due to limited detail in original articles
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to five reviewed studies with varied and sometimes contradictory results. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to five reviewed studies with varied and sometimes contradictory results. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
  imaging_details:
    reference_space: not_applicable
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
  citation: '@Riley2021'
  source_passages:
  - section: Original source P8-S1-C3
    page: 8
    quote: "It is \nimportant to note the primary focus of these four studies was not to investigate the fatigue/speech-language disorder relationship but \ninstead to determine prevalence of post-stroke fatigue, investigate a variety of other factors as predictors of fatigue, or to develop a \nstroke-specific Quality of Life measure (Appelros , 2006; Buck et al., 2004; Choi-Kwon et al., 2005; Glader et al., 2002)."
    supports: limitation
  - section: Original source P11-S3-C11
    page: 11
    quote: "Given the limited detail of many articles’ participant descriptions, we were also unable to separate \nout any potential differences between speech vs. language disorders or receptive vs. expressive impairments."
    supports: limitation
  - section: Original source P7-S2-C3
    page: 7
    quote: "Relationship between fatigue and speech-language disorders \nOf the five studies reporting data that could potentially address this relationship, results varied and occasionally contradicted \nresults of another."
    supports: claim
  - section: Original source P8-S1-C1
    page: 8
    quote: "\nJournal of Communication Disorders 93 (2021) 106145\n8\nwhereas Choi-Kwon and colleagues concluded that speech disorder did significantly predict post-stroke fatigue (Appelros , 2006; \nChoi-Kwon et al., 2005)."
    supports: claim
  - section: Original source P8-S1-C2
    page: 8
    quote: "Like the Choi-Kwon et al. study, Buck and colleagues found that score on the language domain of the NIH \nStroke Scale significantly correlated with fatigue, and Glader and colleagues reported that at 2-years post-stroke, there is a greater \nprevalence of fatigue in those with speech impairments as compared to those without (Buck et al., 2004; Glader et al., 2002)."
    supports: claim
  - section: Original source P1-S1-C8
    page: 1
    quote: "Methods:  A systematic scoping review was conducted to identify studies measuring post-stroke \nfatigue."
    supports: method
  - section: Original source P7-S1-C8
    page: 7
    quote: "From this process, another 241 articles were excluded, leaving 161 articles that were included in our final \nanalysis (see Fig. 1)."
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Riley2021
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The scoping review synthesizes findings from multiple studies regarding the association between speech-language disorders and post-stroke fatigue, noting that while results vary, several studies found a significant positive association.
    bucket: reviews
    entity_id: speech_language_disorder_fatigue_association
    name: speech-language disorder and post-stroke fatigue association
    kind: review
    predictor_type: clinical
    definition: Presence of aphasia and/or a motor speech disorder resulting from left hemisphere stroke, identified via clinician observation, previous diagnosis, general stroke screening (e.g., NIH Stroke Scale), or specific language tests (e.g., Token Test).
    assessment:
    - NIH Stroke Scale
    - Token Test
    target: post_stroke_fatigue
    target_kind: impairment
    claim: Results from studies reporting data on the relationship between speech-language disorders and fatigue varied, but some concluded that speech disorders significantly predict post-stroke fatigue, that language domain scores on the NIH Stroke Scale correlate with fatigue, and that there is a greater prevalence of fatigue in those with speech impairments compared to those without at 2-years post-stroke.
    direction: likely
    method: meta-analysis
    relationship: synthesis
    therapy: null
    sample_n: 161
    population: persons with stroke
    timing: including 2-years post-stroke
    qualifications:
    - The synthesis is based on a small number of studies (five) that reported data directly addressing this relationship
    - Four of the five studies did not have the fatigue/speech-language disorder relationship as their primary focus
    limitations:
    - Results occasionally contradicted one another
    - Unable to separate differences between speech vs. language disorders or receptive vs. expressive impairments due to limited detail in original articles
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P7-S2-C3
      supports: claim
    - source_id: P8-S1-C1
      supports: claim
    - source_id: P8-S1-C2
      supports: claim
    - source_id: P8-S1-C3
      supports: limitation
    - source_id: P11-S3-C11
      supports: limitation
    - source_id: P3-S2-C11
      supports: method
    - source_id: P8-S1-C6
      supports: method
    - source_id: P7-S1-C8
      supports: sample
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: c692b1c38bf63a3cd745f21f7a29fb3c962cfbd79ced781ca245540010642491
      review_sha256: b6915557c03aaaa7c62433c45c72c8d407da475efc7bcc9e455f294dea6c7e94
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
    proposal: R002
    status: hold
    reason: 'analysis_identity: The proposed core labels the method as ''meta-analysis'', but the source explicitly identifies the study as a ''systematic scoping review'' (P1-S1-C8, P4-S1-C4) and the analysis as a synthesis of findings from five studies (P7-S2-C3). A scoping review is not a meta-analysis.'
    material_issues:
    - issue: 'analysis_identity: The proposed core labels the method as ''meta-analysis'', but the source explicitly identifies the study as a ''systematic scoping review'' (P1-S1-C8, P4-S1-C4) and the analysis as a synthesis of findings from five studies (P7-S2-C3). A scoping review is not a meta-analysis.'
      source_ids:
      - P1-S1-C8
      - P4-S1-C4
      - P7-S2-C3
    seconds_this_run: 81.52724908301025
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c692b1c38bf63a3cd745f21f7a29fb3c962cfbd79ced781ca245540010642491
      original_mapping_sha256: 9131fe00edaaf76b0936edfacf2502cbe7256372afccdca3dc2de0b2fa4d901f
      original_status_sha256: 3bbf81ef9f21a10cbe8eb70e765ec57b65986a4552bc59493a7da09259a957de
      evidence_sha256: ddfbd7e05d83116652fedd512c73f34b0aa2a412390656c2cb684b9a3390c885
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 7
      - 8
      note: Reconstructed as a secondary review summary attributed to five reviewed studies with varied and sometimes contradictory results. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to five reviewed studies with varied and sometimes contradictory results. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
