---
id: baseline_md_discourse_content_prediction
name: Baseline MD prediction of discourse content recovery
kind: predictor
findings:
- id: f1
  target: discourse_content_change
  target_kind: prognosis
  claim: Baseline microstructural integrity of the analyzed regions of interest did not significantly predict short-term change in discourse content (Content Units) on the Cookie Theft task.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 20
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    phase: not_reported
    time_post_onset: Short-term recovery measured one week after treatment
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
  - Conventional DTI used rather than advanced multi-shell protocols
  - Atlas-based segmentation performed in native diffusion space without coregistration to T1w or T2w maps
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Baseline mean diffusivity (MD) of regions of interest (left pSTG, pMTG, pITG, AG, AF, IFOF, ILF, and SLF) measured via atlas-based segmentation of DTI data. Regression models controlled for age and days post-onset; Analysis included participants regardless of whether they received active or sham tDCS. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy. The n=20 content-unit model was nonsignificant (R²=0.54, p=0.47); this does not demonstrate absence of all associations.'
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
    id: slt_tdcs
    name: computer-delivered naming therapy with active or sham tDCS (pooled)
  citation: '@Stockbridge2024'
  source_passages:
  - section: Original source P5-S1-C10
    page: 5
    quote: "The model predicting \nchange in content on the Cookie Theft was not significant."
    supports: claim
  - section: Original source P6-S2-C3
    page: 6
    quote: "Short-term recovery of content \nwas not predicted significantly by these factors."
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
  - section: Original source P4-S2-C3
    page: 4
    quote: "For each behavioral outcome mea­\nsure (PNT, CU, and Syllables/CU), a separate regression \nwas calculated to predict change in that variable sub-acutely \n(one week after treatment) and chronically (combining per­\nformance five- and twenty-weeks post-treatment to maxi­\nmize the data available for analysis)."
    supports: method
  - section: Original source P3-S2-C12
    page: 3
    quote: "Atlas based segmentation\nWe obtained DTI maps such as fractional anisotropy (FA; \nµ ± σ), mean (MD), radial (RD) and axial diffusivity maps \n(10 − 3 mm2 s − 1) by processing data in DSI studio."
    supports: method
  - section: Original source P4-S2-C2
    page: 4
    quote: "In order to determine the predictive value of baseline \nmicrostructural integrity on improvement of language skills, \na series of regressions were calculated controlling for age \nand the number of days between stroke and the start of the \nstudy (days post onset)."
    supports: confounders
  - section: Original source P9-S2-C2
    page: 9
    quote: 'Limitations

      One of the main limitations is small sample size with het­

      erogenous aphasia subtypes.'
    supports: limitation
  - section: Original source P9-S2-C5
    page: 9
    quote: "Our study also utilized a conventional DTI \nrather than advanced diffusion techniques (i.e., high resolu­\ntion, multi-shell protocols with a greater number of direc­\ntions)."
    supports: limitation
  - section: Original source P9-S2-C6
    page: 9
    quote: "Our study performed atlas-based segmentation in \nnative diffusion space rather than coregistering diffusion \nmaps with each subject’s T1w or T2w maps."
    supports: limitation
  - section: Table 4, visually verified analysis denominators and coefficients
    page: 9
    quote: "Table 4  Prediction of recovery from microstructural integrity of each region\nShort-term maintenance\n(1-week after therapy)\nLong-term maintenance\n(5- and 20-weeks after therapy)\nPNT\n(N = 21)\nCU\n(N = 20)\nSyllables/CU\n(N = 20)\nPNT\n(N = 22)\nSyllables/CU\n(N = 20)\nConstant\n70.1\n-31.0\n287.6\n82.4\n25.6\nAge\n-0.26\n0.61\n0.78*\n-0.24\n0.28\nDays\n-0.83*\n-0.77\n0.31\n-0.97**\n0.49\npSTG\n0.02\n-0.08\n-0.32\n0.02\n-0.51\npMTG\n-0.86*\n-0.02\n0.55\n-0.87*\n0.38\npITG\n0.47\n0.81\n-0.52*\n0.57*\n-0.73*\nAG\n0.12\n-0.39\n0.97*\n0.18\n0.46\nAF\n1.24*\n1.06\n-1.80*\n1.42*\n-2.06*\nIFOF\n0.22\n-0.31\n0.37\n0.15\n0.89*\nILF\n0.11\n0.19\n-0.34\n0.13\n-0.72*\nSLF\n-1.50*\n-1.39\n1.33*\n-1.75**\n1.56*\nF(df)\n3.58(10, 10)\n1.05(10, 9)\n8.19(10, 9)\n6.36(10, 11)\n3.85(10, 10)\nR2\n0.78\n0.54\n0.90\n0.72\n0.79\np\n0.03\n0.47\n0.002\n0.003\n0.02\n*p < 0.05, **p < 0.001. Variables of interest reflect change in scores from baseline, not raw scores at each timepoint. Standardized\
      \ coefficients \nare reported for variables of interest. Days: Days from stroke to start of therapy\n1 3\n2215\n"
    supports: sample
  - section: Table 4, visually verified results
    page: 9
    quote: "Table 4  Prediction of recovery from microstructural integrity of each region\nShort-term maintenance\n(1-week after therapy)\nLong-term maintenance\n(5- and 20-weeks after therapy)\nPNT\n(N = 21)\nCU\n(N = 20)\nSyllables/CU\n(N = 20)\nPNT\n(N = 22)\nSyllables/CU\n(N = 20)\nConstant\n70.1\n-31.0\n287.6\n82.4\n25.6\nAge\n-0.26\n0.61\n0.78*\n-0.24\n0.28\nDays\n-0.83*\n-0.77\n0.31\n-0.97**\n0.49\npSTG\n0.02\n-0.08\n-0.32\n0.02\n-0.51\npMTG\n-0.86*\n-0.02\n0.55\n-0.87*\n0.38\npITG\n0.47\n0.81\n-0.52*\n0.57*\n-0.73*\nAG\n0.12\n-0.39\n0.97*\n0.18\n0.46\nAF\n1.24*\n1.06\n-1.80*\n1.42*\n-2.06*\nIFOF\n0.22\n-0.31\n0.37\n0.15\n0.89*\nILF\n0.11\n0.19\n-0.34\n0.13\n-0.72*\nSLF\n-1.50*\n-1.39\n1.33*\n-1.75**\n1.56*\nF(df)\n3.58(10, 10)\n1.05(10, 9)\n8.19(10, 9)\n6.36(10, 11)\n3.85(10, 10)\nR2\n0.78\n0.54\n0.90\n0.72\n0.79\np\n0.03\n0.47\n0.002\n0.003\n0.02\n*p < 0.05, **p < 0.001. Variables of interest reflect change in scores from baseline, not raw scores at each timepoint. Standardized\
      \ coefficients \nare reported for variables of interest. Days: Days from stroke to start of therapy\n1 3\n2215\n"
    supports: claim
predictor_type: imaging_metric
short_definition: Baseline mean diffusivity (MD) of regions of interest (left pSTG, pMTG, pITG, AG, AF, IFOF, ILF, and SLF) measured via atlas-based segmentation of DTI data.
assessment:
- Cookie Theft picture (Content Units)
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Stockbridge2024
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis tests whether baseline microstructural integrity (MD) of specific regions predicts short-term recovery of discourse content (CU). The source explicitly states that the model for this specific outcome was not significant.
    bucket: predictors
    entity_id: baseline_md_discourse_content_prediction
    name: Baseline MD prediction of discourse content recovery
    kind: predictor
    predictor_type: imaging_metric
    definition: Baseline mean diffusivity (MD) of regions of interest (left pSTG, pMTG, pITG, AG, AF, IFOF, ILF, and SLF) measured via atlas-based segmentation of DTI data.
    assessment:
    - Cookie Theft picture (Content Units)
    target: discourse_content_change
    target_kind: prognosis
    claim: Baseline microstructural integrity of the analyzed regions of interest did not significantly predict short-term change in discourse content (Content Units) on the Cookie Theft task.
    direction: no_effect
    method: DTI
    relationship: correlational
    therapy:
      id: tdcs_slt
      name: anodal tDCS combined with computer-delivered speech and language naming therapy
    sample_n: 22
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    timing: Short-term recovery measured one week after treatment
    qualifications:
    - Regression models controlled for age and days post-onset
    - Analysis included participants regardless of whether they received active or sham tDCS
    limitations:
    - Small sample size
    - Heterogeneous aphasia subtypes
    - Conventional DTI used rather than advanced multi-shell protocols
    - Atlas-based segmentation performed in native diffusion space without coregistration to T1w or T2w maps
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S1-C10
      supports: claim
    - source_id: P6-S2-C3
      supports: claim
    - source_id: P4-S1-C1
      supports: sample
    - source_id: P2-S3-C2
      supports: sample
    - source_id: P4-S2-C3
      supports: method
    - source_id: P3-S2-C12
      supports: method
    - source_id: P4-S2-C2
      supports: confounders
    - source_id: P9-S2-C2
      supports: limitation
    - source_id: P9-S2-C5
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
    proposal: R007
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P5-S1-C10
      - P6-S2-C3
    seconds_this_run: 88.11013637500582
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      original_mapping_sha256: 3f2babbd96b1d890d1bf47f3bab8e44f2fe4f9709e0a7800543f34607b8a4933
      original_status_sha256: 10575c25795f65ca413b9ebebff851d2dfa198a113cb408ca08182ba1a1cae12
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
      note: Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy. The n=20 content-unit model was nonsignificant (R²=0.54, p=0.47); this does not demonstrate absence of all associations.
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
  note: Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy. The n=20 content-unit model was nonsignificant (R²=0.54, p=0.47); this does not demonstrate absence of all associations.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
