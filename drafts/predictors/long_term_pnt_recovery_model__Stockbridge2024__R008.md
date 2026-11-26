---
id: long_term_pnt_recovery_model
name: Long-term picture naming recovery predictor
kind: predictor
findings:
- id: f1
  target: pnt_improvement
  target_kind: prognosis
  claim: Long-term improvement in picture naming (averaged 5- and 20-weeks post-treatment) was significantly predicted by days since stroke and baseline mean diffusivity of the pMTG, pITG, AF, and SLF, where lower diffusivity in the pMTG and SLF and higher diffusivity in the pITG and AF were associated with better recovery.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    phase: not_reported
    time_post_onset: Baseline imaging and days since stroke used to predict improvement measured at an average of 5 and 20 weeks post-treatment
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
  - Analysis combined patients who received active tDCS and sham tDCS
  - Atlas-based segmentation performed in native diffusion space rather than coregistering with T1w or T2w maps
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A regression model using baseline mean diffusivity (MD) of the pMTG, pITG, AF, and SLF (measured via atlas-based segmentation of DTI) and the number of days from stroke to start of therapy. Model controlled for age; Long-term recovery is defined as the average of performance measured 5 and 20 weeks from the end of treatment. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified original PDF pp.2-5 and Table 4 p.9. DTI/MD was measured in the patients; atlases defined ROIs in native diffusion space and were manually refined. This is not lesion overlap with a normative tract template. MRI cohort n=22; regression-specific denominators follow Table 4. Active and sham tDCS groups were pooled, so these observational imaging associations do not estimate tDCS efficacy.'
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
  - section: Original source P5-S1-C13
    page: 5
    quote: "Models predicting long-term improvement (the average \nof performance measured 5- and 20-weeks from the end of \ntreatment) from microstructural integrity was significant \nfor both measures considered, PNT and informational effi­\nciency."
    supports: claim
  - section: Original source P5-S2-C2
    page: 5
    quote: "PNT improvement was significantly predicted by \nlower diffusivity in the pMTG and SLF and higher diffusiv­\nity in the pITG and AF."
    supports: claim
  - section: Original source P6-S2-C4
    page: 6
    quote: "Prediction \nof long-term recovery of picture naming relied on simi­\nlar factors with similar success."
    supports: claim
  - section: Original source P6-S2-C5
    page: 6
    quote: "In addition to days since \nstroke, MDs of the pMTG, pITG, AF, and SLF also con­\ntributed significantly to the prediction."
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
  - section: Original source P4-S2-C2
    page: 4
    quote: "In order to determine the predictive value of baseline \nmicrostructural integrity on improvement of language skills, \na series of regressions were calculated controlling for age \nand the number of days between stroke and the start of the \nstudy (days post onset)."
    supports: method
  - section: Original source P9-S2-C2
    page: 9
    quote: 'Limitations

      One of the main limitations is small sample size with het­

      erogenous aphasia subtypes.'
    supports: limitation
  - section: Original source P9-S2-C3
    page: 9
    quote: "Another limitation is we have \nanalyzed together patients who received active tDCS and \nthose who received sham tDCS due to small sample size."
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
short_definition: A regression model using baseline mean diffusivity (MD) of the pMTG, pITG, AF, and SLF (measured via atlas-based segmentation of DTI) and the number of days from stroke to start of therapy.
assessment:
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Stockbridge2024
  proposal_id: R008
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The analysis predicts long-term picture naming improvement using a model based on baseline mean diffusivity (MD) of specific white matter regions and days since stroke.
    bucket: predictors
    entity_id: long_term_pnt_recovery_model
    name: Long-term picture naming recovery predictor
    kind: predictor
    predictor_type: imaging_metric
    definition: A regression model using baseline mean diffusivity (MD) of the pMTG, pITG, AF, and SLF (measured via atlas-based segmentation of DTI) and the number of days from stroke to start of therapy.
    assessment:
    - Philadelphia Naming Test
    target: pnt_improvement
    target_kind: prognosis
    claim: Long-term improvement in picture naming (averaged 5- and 20-weeks post-treatment) was significantly predicted by days since stroke and baseline mean diffusivity of the pMTG, pITG, AF, and SLF, where lower diffusivity in the pMTG and SLF and higher diffusivity in the pITG and AF were associated with better recovery.
    direction: likely
    method: DTI
    relationship: correlational
    therapy:
      id: computer_delivered_lexical_treatment
      name: computer-delivered speech and language naming therapy
    sample_n: 22
    population: Right-handed adult English speakers within three months of ischemic left hemisphere stroke diagnosed with aphasia
    timing: Baseline imaging and days since stroke used to predict improvement measured at an average of 5 and 20 weeks post-treatment
    qualifications:
    - Model controlled for age
    - Long-term recovery is defined as the average of performance measured 5 and 20 weeks from the end of treatment
    limitations:
    - Small sample size
    - Heterogeneous aphasia subtypes
    - Analysis combined patients who received active tDCS and sham tDCS
    - Atlas-based segmentation performed in native diffusion space rather than coregistering with T1w or T2w maps
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S1-C13
      supports: claim
    - source_id: P5-S2-C2
      supports: claim
    - source_id: P6-S2-C4
      supports: claim
    - source_id: P6-S2-C5
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
    - source_id: P4-S2-C2
      supports: method
    - source_id: P9-S2-C2
      supports: limitation
    - source_id: P9-S2-C3
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
    proposal: R008
    status: hold
    reason: Reference-template construction must not be coded as diffusion/tractography measured in patients.
    material_issues:
    - issue: Reference-template construction must not be coded as diffusion/tractography measured in patients.
      source_ids:
      - P5-S1-C13
      - P5-S2-C2
      - P6-S2-C4
      - P6-S2-C5
    seconds_this_run: 92.09687183398637
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 5ffb60c16f560d9d52bd2b772024bf2985f76f4f04f85576b777eca63b55d9b0
      original_mapping_sha256: c1fec082726fd905680b726ecabb5698b2f65db02247b2ec11644afdc21d9655
      original_status_sha256: 7e265ca0d37fdc89256a801d8461dc5c6053a6786d9ec232d3020ba93beaeb4a
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
