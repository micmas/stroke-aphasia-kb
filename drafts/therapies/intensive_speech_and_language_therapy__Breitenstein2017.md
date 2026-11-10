---
schema_version: 2.8
id: intensive_speech_and_language_therapy
name: "Intensive Speech and Language Therapy"
kind: therapy
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
targets_impairments: ["anomia", "fluency", "form_to_meaning", "syntactic_processing"]
dosage: "3 weeks, >=10 h per week"

findings:
  - id: f1
    target: form_to_meaning
    target_kind: impairment
    claim: "Three weeks of intensive speech and language therapy (>=10 h/week) significantly improves everyday verbal communication in patients with chronic aphasia."
    direction: likely
    relationship: causal
    citation: "@Breitenstein2017"
    method: clinical_RCT
    design: RCT
    strength: strong
    evidence_quality: RCT
    therapy:
      id: intensive_speech_and_language_therapy
      name: "intensive speech and language therapy"
      dose: "3 weeks, >=10 h per week"
    sample:
      n: 156
      population: "chronic aphasia after stroke"
      time_post_onset: "6 months or more"
      phase: chronic
      age_range: "18-70 years"
      handedness: not_reported
      language: "German"
      cohort: "FCET2EC"
    statistics:
      threshold: "p=0.0004"
      effect_size: "Cohen's d 0.58"
      p_value: 0.0004
    confounders_controlled: ["baseline ANELT A-scale score"]
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "behavioural-only treatment-efficacy finding"
    imaging: none
    author_limitations:
      - "Low-intensity therapy provided to control group and during follow-up might have supported maintenance of effects."
      - "Study did not address if a critical time window exists for maximum effects."
      - "Findings cannot predict if other approaches or different intensity levels (e.g. 6 h/week) would be equally effective."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 1533"
      confidence: high
      flags: []
    source_passages:
      - section: "Summary"
        page: 1
        quote: "Verbal communication was significantly improved from baseline to after intensive speech and language treatment (mean difference 2.61 points [SD 4.94]; 95% CI 1.49 to 3.72), but not from baseline to after treatment deferral... between-group difference Cohen's d 0.58; p=0.0004."
        supports: claim
      - section: "Participants"
        page: 3
        quote: "Inclusion criteria... were chronic aphasia... lasting 6 months or more after an ischaemic or haemorrhagic stroke, age 18-70 years, German as first language..."
        supports: sample
      - section: "Study design"
        page: 2
        quote: "We did a randomised, open-label, blinded-endpoint, multicentre, stratified-by-centre, waiting-list-controlled, parallel-group, superiority trial to evaluate the effectiveness of 3 weeks of intensive speech and language therapy versus 3 weeks of treatment deferral."
        supports: method
      - section: "Statistical analysis"
        page: 5
        quote: "We used an ANCOVA model to assess the primary outcome with the ANELT A-scale score after 3 weeks of speech and language therapy or treatment deferral as a dependent variable, treatment group as an independent variable, and baseline ANELT A-scale score as a covariate."
        supports: statistics
      - section: "Discussion"
        page: 10
        quote: "First, low intensity speech and language therapy was provided to the control group during the treatment deferral period and to both groups during the 6-month follow-up... we cannot rule out that low-intensity therapy after the intensive study intervention could have supported the maintenance of the treatment effect."
        supports: limitation

  - id: f2
    target: anomia
    target_kind: impairment
    claim: "Intensive speech and language therapy significantly improves linguistic performance across lexicon, syntax, and language comprehension domains."
    direction: likely
    relationship: causal
    citation: "@Breitenstein2017"
    method: clinical_RCT
    design: RCT
    strength: strong
    evidence_quality: RCT
    therapy:
      id: intensive_speech_and_language_therapy
      name: "intensive speech and language therapy"
      dose: "3 weeks, >=10 h per week"
    sample:
      n: 156
      population: "chronic aphasia after stroke"
      time_post_onset: "6 months or more"
      phase: chronic
      age_range: "18-70 years"
      handedness: not_reported
      language: "German"
      cohort: "FCET2EC"
    statistics:
      threshold: "p<0.05"
      effect_size: not_reported
      p_value: 0.05
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "behavioural-only treatment-efficacy finding"
    imaging: none
    author_limitations:
      - "Low-intensity therapy provided to control group and during follow-up might have supported maintenance of effects."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 1532"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 1532
        quote: "Scores on the linguistic screening measure (SAPS; total score, and lexicon, syntax, language comprehension, and language production subtotals)... were significantly improved from baseline to after the 3-week intensive therapy compared with from baseline to after the 3-week treatment deferral (all p<0.05; table 2; figure 4)."
        supports: claim
      - section: "Discussion"
        page: 10
        quote: "First, low intensity speech and language therapy was provided to the control group during the treatment deferral period and to both groups during the 6-month follow-up."
        supports: limitation
---
