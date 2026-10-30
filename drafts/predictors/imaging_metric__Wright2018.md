---
schema_version: 2.8
id: imaging_metric
name: "Imaging Metric"
kind: predictor
predictor_type: imaging_metric
short_definition: "Scalar imaging-derived measures of brain tissue health or damage."
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Severe leukoaraiosis in the right hemisphere is independently associated with poorer object naming outcomes in post-stroke aphasia."
    direction: likely
    relationship: correlational
    citation: "@Wright2018"
    method: behavioral_only
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 42
      population: "adults who had sustained a single left hemisphere ischemic stroke resulting in aphasia"
      time_post_onset: "3 to 157 (mean \u00b1 SD 39 \u00b1 36, median 28, mode 12) months after stroke"
      phase: chronic
      age_range: "mean \u00b1 SD 56.1 \u00b1 15.0 years"
      handedness: "right-handed"
      language: "fluent speaker of English before stroke"
    statistics:
      threshold: "p = 0.027"
      effect_size: "95% confidence interval -2.23 to -0.13"
    confounders_controlled:
      - "lesion volume"
      - "months since stroke"
      - "comorbid conditions (hypertension, diabetes mellitus, and depression)"
      - "damage to specific locations (left STG, SLF, and pIFG)"
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "Right hemisphere leukoaraiosis rated using the Cardiovascular Health Study (CHS) white matter rating scale."
    author_limitations:
      - "relatively small sample size"
      - "unable to control for the amount or type of language rehabilitation"
      - "did not evaluate the influence of other cognitive impairments"
      - "absence of information about initial severity"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page e528"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Severity of leukoaraiosis was associated with degree of naming outcome with the use of both measures after controlling for lesion volume, months since stroke, comorbid conditions, and damage to specific locations."
        supports: claim
      - section: "Methods - Participants"
        page: 2
        quote: "We carried out a cross-sectional study of a convenience sample of a consecutive series of 42 adults who had sustained a single left hemisphere ischemic stroke resulting in aphasia, were at least 3 months after the onset of stroke..."
        supports: sample
      - section: "Methods - Imaging and image analysis"
        page: 3
        quote: "FLAIR images were also rated for the severity of leukoaraiosis in the noninfarcted hemisphere by a neurologist and a technician masked to the language scores using the Cardiovascular Health Study (CHS) white matter rating scale (ranging from 0–9, with 9 being most extensive)."
        supports: method
      - section: "Results"
        page: 4
        quote: "severity of RH leukoaraiosis was independently associated with outcome (95% confidence interval -2.23 to -0.13, p = 0.027)"
        supports: statistics
      - section: "Discussion"
        page: 5
        quote: "Limitations of the study include the relatively small sample size... We also were not able to control for the amount or type of language rehabilitation."
        supports: limitation
  - id: f2
    target: fluency
    target_kind: impairment
    claim: "Right hemisphere leukoaraiosis is independently associated with poorer word fluency outcomes in post-stroke aphasia."
    direction: likely
    relationship: correlational
    citation: "@Wright2018"
    method: behavioral_only
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 42
      population: "adults who had sustained a single left hemisphere ischemic stroke resulting in aphasia"
      time_post_onset: "3 to 157 (mean \u00b1 SD 39 \u00b1 36, median 28, mode 12) months after stroke"
      phase: chronic
      age_range: "mean \u00b1 SD 56.1 \u00b1 15.0 years"
      handedness: "right-handed"
      language: "fluent speaker of English before stroke"
    statistics:
      threshold: "p = 0.020"
      effect_size: "coefficient -0.73"
    confounders_controlled:
      - "left STG infarct"
      - "left SLF infarct"
      - "left pIFG infarct"
      - "months since stroke"
      - "hypertension"
      - "diabetes mellitus"
      - "depression"
      - "infarct volume"
    confounders_not_controlled: []
    region_definition:
      kind: not_reported
      description: "Right hemisphere leukoaraiosis rated using the Cardiovascular Health Study (CHS) white matter rating scale."
    author_limitations:
      - "relatively small sample size"
      - "unable to control for the amount or type of language rehabilitation"
      - "did not evaluate the influence of other cognitive impairments"
      - "absence of information about initial severity"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page e528"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Severity of leukoaraiosis at onset correlated with object naming (\u03c1 = -0.56, p = 0.0008) and word fluency (\u03c1 = -0.37, p = 0.01) outcomes."
        supports: claim
      - section: "Results"
        page: 4
        quote: "severity of RH leukoaraiosis and damage to left STG were the only independent (negative) predictors of word fluency outcome (table 2)."
        supports: statistics
      - section: "Discussion"
        page: 5
        quote: "Limitations of the study include the relatively small sample size..."
        supports: limitation
---
