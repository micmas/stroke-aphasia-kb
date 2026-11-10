---
schema_version: 2.8
id: speech_and_language_therapy
name: "Speech and Language Therapy (General)"
kind: therapy
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-11
targets_impairments: ["anomia", "form_to_meaning", "fluency"]
notes: "This entry captures general dosage and intensity findings from the RELEASE network meta-analysis."

findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "The greatest gains in overall language and auditory comprehension are associated with a total therapy dosage of 20 to 50 hours."
    direction: likely
    relationship: responder
    citation: "@Brady2022Dosage"
    method: meta-analysis
    design: meta-analysis
    strength: strong
    evidence_quality: meta-analysis
    sample:
      n: 959
      population: "people with aphasia after stroke"
      time_post_onset: "median 61 days (IQR 7-487)"
      phase: mixed
      age_range: "median 63.0 (IQR 54.1-74.0)"
      handedness: "95.5% right-handed"
      language: "multilingual (English 26.6%, Dutch 20.8%, German 19.0%, etc.)"
      cohort: "RELEASE"
    statistics:
      threshold: "95% CI"
      effect_size: "18.37 [10.58-26.16] WAB-AQ; 5.23 [1.51-8.95] AAT-TT"
    confounders_controlled: ["age", "sex", "time poststroke", "baseline aphasia severity"]
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "behavioral-only meta-analysis of therapy dosage"
    therapy:
      id: speech_and_language_therapy
      name: "speech and language therapy"
      dose: "20 to 50 total hours"
    author_limitations:
      - "Some networks lacked randomized comparisons."
      - "Data set was predominantly from English-speaking participants from high-income countries."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 956"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 956
        quote: "Greatest gains in overall language and comprehension were associated with >20 to 50 hours SLT dosage (18.37 [10.58-26.16] Western Aphasia Battery-Aphasia Quotient; 5.23 [1.51-8.95] Aachen Aphasia Test-Token Test)."
        supports: claim
      - section: "Methods"
        page: 957
        quote: "Our 1-stage network meta-analysis... adjusting for a priori-defined covariates (age, sex, time poststroke, and baseline aphasia severity)."
        supports: confounders
      - section: "Discussion"
        page: 964
        quote: "some networks lacked randomized comparisons and our data set was predominantly from English-speaking participants, high-income countries"
        supports: limitation

  - id: f2
    target: severity_metric
    target_kind: predictor
    claim: "The greatest clinical gains in overall language and functional communication are associated with a therapy intensity of 2 to 4 hours per week or 9+ hours per week."
    direction: likely
    relationship: responder
    citation: "@Brady2022Dosage"
    method: meta-analysis
    design: meta-analysis
    strength: strong
    evidence_quality: meta-analysis
    sample:
      n: 959
      population: "people with aphasia after stroke"
      time_post_onset: "median 61 days (IQR 7-487)"
      phase: mixed
      cohort: "RELEASE"
    statistics:
      threshold: "not_reported"
      effect_size: "not_reported"
    confounders_controlled: ["age", "sex", "time poststroke", "baseline aphasia severity"]
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "behavioral-only meta-analysis of therapy intensity"
    therapy:
      id: speech_and_language_therapy
      name: "speech and language therapy"
      dose: "2-4 or 9+ hours/week"
    author_limitations:
      - "Some networks lacked randomized comparisons."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 956"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 956
        quote: "Greatest clinical overall language, functional communication, and comprehension gains were associated with 2 to 4 and 9+ SLT hours/week."
        supports: claim

  - id: f3
    target: severity_metric
    target_kind: predictor
    claim: "Prescribed home practice is associated with greater gains in overall language and auditory comprehension."
    direction: likely
    relationship: responder
    citation: "@Brady2022Dosage"
    method: meta-analysis
    design: meta-analysis
    strength: moderate
    evidence_quality: meta-analysis
    sample:
      n: 959
      population: "people with aphasia after stroke"
      time_post_onset: "median 61 days (IQR 7-487)"
      phase: mixed
      cohort: "RELEASE"
    statistics:
      threshold: "not_reported"
      effect_size: "16.69 [10.01-23.37] WAB-AQ; 5.28 [2.19-8.37] AAT-TT"
    confounders_controlled: ["age", "sex", "time poststroke", "baseline aphasia severity"]
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "behavioral-only meta-analysis of home practice"
    therapy:
      id: speech_and_language_therapy
      name: "speech and language therapy with prescribed home practice"
    author_limitations:
      - "Prescribed home practice regimen data were unavailable; analysis based on presence/absence of component."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 962"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 962
        quote: "Prescribed home practice was associated with greater gains in overall language (16.69 [10.01-23.37] WAB-AQ) and auditory comprehension (5.28 [2.19-8.37] AAT-TT)."
        supports: claim
      - section: "Results"
        page: 962
        quote: "Prescribed home practice regimen data were unavailable. Therefore, our analysis was based on whether home practice was an intervention component or not."
        supports: limitation
---
