---
schema_version: 2.8
id: intention_treatment
name: "Intention Treatment"
kind: therapy
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
short_description: "A treatment for anomia that uses complex left-hand movements to initiate word-finding trials, designed to shift language production to the right frontal lobe."
targets_impairments: ["anomia"]
dosage: "3 phases (naming 1, naming 2, category generation), 10 sessions per week per phase"

findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Intention treatment evokes greater generalization to untrained category and picture-naming probes compared to a control treatment without hand movements."
    direction: likely
    relationship: causal
    citation: "@Benjamin2014"
    method: behavioral_only
    design: RCT
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 14
      population: "chronic left-hemisphere stroke aphasia"
      time_post_onset: ">6 months"
      phase: chronic
      age_range: "mean 67.5 (combined)"
      handedness: "premorbidly right-handed"
      language: "English"
    statistics:
      threshold: "P < .01"
      effect_size: "t = 3.77 (naming), t = 3.33 (categories)"
    confounders_controlled: ["
      stratified random sampling for naming impairment and frontal lesion extent"
    ]
    confounders_not_controlled: ["gender composition", "education level"]
    region_definition:
      kind: not_reported
      description: "behavioural-only treatment-efficacy finding — no specific brain region"
    imaging_details:
      reference_space: not_reported
      atlases_used: []
    author_limitations:
      - "Small sample size."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 550"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 550
        quote: "when untrained probes alone were considered in group analyses, only IT showed significant improvement (t = 3.77, df = 5, P < .01 for IT on picture-naming; t = 3.33, df = 6, P < .01 for IT on categories)"
        supports: claim
      - section: "Discussion"
        page: 551
        quote: "effects of IT generalized to untrained items but effects of CT did not."
        supports: claim
      - section: "Method"
        page: 547
        quote: "Subjects were assigned to Intention (IT) or Control (CT) treatments using stratified random sampling"
        supports: method
      - section: "Discussion"
        page: 552
        quote: "Because of the small number of subjects in the groups..."
        supports: limitation
---
