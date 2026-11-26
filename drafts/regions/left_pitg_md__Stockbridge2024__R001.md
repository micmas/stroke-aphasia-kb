---
id: left_pitg_md
name: left posterior inferior temporal gyrus cluster
kind: network
findings:
- id: f1
  target: picture_naming_accuracy
  target_kind: impairment
  claim: Picture naming accuracy significantly correlated with lower mean diffusivity (higher microstructural integrity) in the left posterior inferior temporal gyrus.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    phase: not_reported
    time_post_onset: Concurrent association at baseline (within three months of stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Heterogeneous aphasia subtypes
  - Atlas-based segmentation performed in native diffusion space rather than coregistered with T1w or T2w maps
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient mean diffusivity (MD) in the left posterior inferior temporal gyrus (pITG), measured via atlas-based segmentation of diffusion tensor imaging (DTI) and manually refined. The correlation was described as significant but weak. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy.'
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
  citation: '@Stockbridge2024'
  source_passages:
  - section: Original source P1-S2-C7
    page: 1
    quote: "Picture naming accuracy significantly correlated with lower mean diffusivity (higher \nmicrostructural integrity) in the left posterior inferior temporal gyrus."
    supports: claim
  - section: Original source P4-S1-C7
    page: 4
    quote: "Picture \nnaming performance demonstrated a significant but weak \ncorrelation with lower mean diffusivity in the left pITG."
    supports: claim
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      Brain Structure and Function (2024) 229:2207–2217

      Results

      Participant description

      Twenty-two participants completed diffusion tensor imag­

      ing, summarized in Tables 1, 2 and 3.'
    supports: sample
  - section: Original source P2-S3-C2
    page: 2
    quote: "Included individu­\nals were right-handed, adult English speakers within three \nmonths of ischemic left hemisphere stroke who were diag­\nnosed with aphasia using the Western Aphasia Battery-\nRevised (WAB-R; Kertesz 2007)."
    supports: sample
  - section: Original source P3-S1-C3
    page: 3
    quote: "Evaluation\nParticipants completed the 175-item color Philadelphia \nNaming Test  (PNT; naming pictures of objects, Walker \nand Schwartz 2012)."
    supports: method
  - section: Original source P3-S2-C12
    page: 3
    quote: "Atlas based segmentation\nWe obtained DTI maps such as fractional anisotropy (FA; \nµ ± σ), mean (MD), radial (RD) and axial diffusivity maps \n(10 − 3 mm2 s − 1) by processing data in DSI studio."
    supports: method
  - section: Original source P3-S2-C13
    page: 3
    quote: "Once \nthe maps are generated, we used embedded maps Brainnec­\ntome, FreeSurfer, Human Connectome Project tractography \n(HCP842) maps to generate regions left posterior pSTG \n(merged regions STG L 6_2, 6_4; Brainnectome map), \npMTG (MTG 4_3; Brainnectome map), pITG (merged \nregions ITG 7_2, 7_5; Brainnectome map), AG (IPL 6_5; \nBrainnectome map), AF (HCP842 map), IFOF (HCP842 \nmap), ILF (HCP842 map), and SLF (HCP842 map)."
    supports: method
  - section: Original source P3-S3-C5
    page: 3
    quote: "Also, for better \naccuracy, once the region or tracts of interest were gener­\nated, we visually inspected these parcellations and manually \nmodified them (moving in 3D space, eroding/dilating) on b0 \nmap with neuroanatomy guidance (Keser et al. 2023)."
    supports: method
  - section: Original source P9-S2-C2
    page: 9
    quote: 'Limitations

      One of the main limitations is small sample size with het­

      erogenous aphasia subtypes.'
    supports: limitation
  - section: Original source P9-S2-C6
    page: 9
    quote: "Our study performed atlas-based segmentation in \nnative diffusion space rather than coregistering diffusion \nmaps with each subject’s T1w or T2w maps."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Stockbridge2024
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study reports a significant correlation between baseline mean diffusivity (MD) in the left posterior inferior temporal gyrus (pITG) and picture naming accuracy in subacute stroke patients.
    bucket: regions
    entity_id: left_pitg_md
    name: left posterior inferior temporal gyrus cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient mean diffusivity (MD) in the left posterior inferior temporal gyrus (pITG), measured via atlas-based segmentation of diffusion tensor imaging (DTI) and manually refined.
    assessment:
    - Philadelphia Naming Test
    target: picture_naming_accuracy
    target_kind: impairment
    claim: Picture naming accuracy significantly correlated with lower mean diffusivity (higher microstructural integrity) in the left posterior inferior temporal gyrus.
    direction: likely
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 22
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    timing: Concurrent association at baseline (within three months of stroke)
    qualifications:
    - The correlation was described as significant but weak
    limitations:
    - Small sample size
    - Heterogeneous aphasia subtypes
    - Atlas-based segmentation performed in native diffusion space rather than coregistered with T1w or T2w maps
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S2-C7
      supports: claim
    - source_id: P4-S1-C7
      supports: claim
    - source_id: P4-S1-C1
      supports: sample
    - source_id: P2-S3-C2
      supports: sample
    - source_id: P3-S1-C3
      supports: method
    - source_id: P3-S2-C12
      supports: method
    - source_id: P3-S2-C13
      supports: method
    - source_id: P3-S3-C5
      supports: method
    - source_id: P9-S2-C2
      supports: limitation
    - source_id: P9-S2-C6
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
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      review_sha256: 01ee30b75663c276f40282f4eae59ba41fd1bf921642665edca50810faa0759f
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
      - P1-S2-C7
      - P4-S1-C7
    seconds_this_run: 81.86044570800732
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      original_mapping_sha256: c0eaf06d662c38c9284658ea9dd6c3d31eef9be63e90f3fccf20556a53416118
      original_status_sha256: 83523806e824ac2b6631bd00e6abec126890f445ba168b517c22093f719411df
      evidence_sha256: 78c8dc8c32f3d43df3988c6cfd2c3a9b1fa29d40a141fc4610bd80ab934e5d63
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 9
      note: Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy.
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
  note: Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
