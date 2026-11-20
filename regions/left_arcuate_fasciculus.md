---
schema_version: 2.7
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
aliases:
- arcuate fasciculus (left)
- left AF
- left superior longitudinal fasciculus (arcuate component)
- Superior longitudinal fasciculus L
- Superior longitudinal fasciculus left
kind: tract
status: approved
review_tier: legacy
created_by: agent:claude-sonnet-4-6
created_on: 2026-05-06
hemisphere: left
members:
- left_posterior_superior_temporal_gyrus
- left_middle_temporal_gyrus
- left_inferior_frontal_gyrus_pars_opercularis
- left_temporoparietal_junction
networks:
- dorsal_language
findings: []
notes: "This draft covers all primary findings from Marchina et al. 2011 (Stroke 42:2251-2256).\n\
  \nThe paper's central contribution is quantifying left AF lesion load (volume of\
  \ tract\ndamaged) using probabilistic DTI maps from healthy controls overlaid onto\
  \ patient lesion\nmaps. Four findings are extracted (f1–f4): AF lesion load predicts\
  \ speech rate (WPM),\ninformativeness (%CIUs), overall efficiency (CIUs/min), and\
  \ confrontation naming (BNT).\nA fifth finding (f5) captures the null result for\
  \ extreme capsule, which is substantively\nmeaningful for dual-stream model interpretation.\n\
  \nKey methodological notes:\n- Relationship coded `correlational` throughout: the\
  \ paper uses a tract-lesion overlap\n  approach (not VLSM/LSM), and the probabilistic\
  \ tract maps come from healthy controls,\n  not from the patients' own DTI. The\
  \ lesion-load method is more analogous to ROI-based\n  structural analysis than\
  \ to direct LSM.\n- All four behavioral outcomes correlate most strongly with AF\
  \ (not EmC or UF), which\n  the authors discuss as inconsistent with strict dual-stream\
  \ predictions.\n- Target IDs for impairments (`speech_production_rate`, `speech_informativeness`,\n\
  \  `speech_efficiency`, `confrontation_naming`) and for the null-finding region\n\
  \  (`left_extreme_capsule`) are forward-looking — stubs should be created at promotion\
  \ time.\n- @Marchina2011 is already listed in citations.md as [cited]; update to\
  \ [extracted]\n  after promotion.\n"
reviewer: claude-cowork
reviewed_on: '2026-05-06'
last_reviewed: '2026-10-30'
---
