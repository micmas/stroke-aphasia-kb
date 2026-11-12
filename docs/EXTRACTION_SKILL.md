# Paper-extraction skill — instructions for the agent

> **Purpose.** Take one neuroscience / aphasia paper and produce one or
> more **draft** knowledge-base entries under the current schema
> (`schema.md`, v2.8), plus a
> color-annotated version of the source paper that lets the user
> visually verify what was extracted from where. The user reviews
> every draft before it enters the canonical knowledge base. **You
> never write directly to `regions/`, `impairments/`, `therapies/`,
> or `predictors/`.**

This file is the agent's instruction manual. It must be read **in full**
before any extraction. The schema is defined in `schema.md` (read that
too). This file tells you how to *use* the schema responsibly. Section
4b is the checklist every finding must pass before you write it.

## What v2.1 / v2.2 / v2.3 added (since v2.0)

From v2.1:

1. **Every finding's `source_passages` list is required and each entry
   carries a `supports` tag** (one of `claim` / `method` / `sample` /
   `statistics` / `confounders` / `region_definition` / `limitation` /
   `imaging_details`). The tags drive the colored highlights in the
   annotated PDF. No `source_passages`, no annotation, no extraction.
2. **Every imaging-based finding gets an `imaging_details` block** —
   reference space, atlases used, preprocessing pipeline, and any
   reported peak coordinates. Behavioral-only findings can omit it.

From v2.2:

3. **`method` can be a list** for multimodal papers
   (e.g. `[fMRI_activation, DTI]` instead of just one method).
4. **`imaging_details.modalities`** — per-modality acquisition blocks
   for multimodal papers (fMRI volume count, DTI b-values, etc.).
   Single-modality papers can stay with the flat `acquisition` block.
5. **`imaging_details.task`** — paradigm description for task-based
   fMRI findings.
6. **`relationship`** — required field on every finding. One of
   `causal` / `correlational` / `recruitment` / `responder`. Tells the
   reader what kind of claim the finding is making (see "Relationship
   semantics" below). `direction` is the *valence* (likely / unlikely);
   `relationship` is the *type* (causal vs correlational vs …).

From v2.3:

7. **`predictors/` bucket** — new entry kind for measurable variables
   (behavioural test scores, demographics, clinical characteristics,
   imaging-derived scalars) that the literature uses to predict
   outcomes. Each predictor entry declares a `predictor_type`:
   `behavioural` / `demographic` / `clinical` / `imaging_metric`.
   See "When to use predictor entries" below.
8. **`target_kind: predictor`** — findings in any bucket can now point
   to a predictor. Example: a region finding can claim "damage to
   left Heschl's gyrus → reduced WAB-AQ" with
   `target: wab_aq, target_kind: predictor`.

---

## 1. Workflow

For each paper the user gives you:

1. **Acknowledge what you have.** State whether you have the full PDF, an
   abstract only, a preprint, or a secondary description. If you only have
   the abstract, you may produce a draft but you **must** set
   `provenance.confidence: low` and add a flag.

2. **Identify the unit-of-extraction.** A single paper typically yields
   1–10 findings. Each finding is a single (region, impairment-or-therapy,
   direction) triple. A sentence that joins two observations ("X is
   predominantly left-sided, particularly in Y"; "lesions cause A and B")
   is two findings, or one finding whose every clause has its own quoted
   support. Never let one clause borrow the support of another. If a paper reports 5 regions for naming and 3 for
   fluency, that's 8 findings — but they may live in 5 region files (since
   findings are stored on the *region side*).

   **Anchor perspective rule (avoid duplication).** When a paper makes
   region-tied claims (which is most of the literature), put each
   finding in a *region* draft with the appropriate `target` /
   `target_kind`. Don't mirror the same finding into a second draft on
   the impairment or therapy side — the loader's
   `interpret_overlap()` already pulls findings *across* all region
   entries when you query "what predicts impairment X?", so the
   impairment view is automatically derived.

   Spawn a separate impairment- or therapy-anchored draft only when
   the paper's claim isn't tied to a specific region. Examples:
     * "Naming errors split into semantic vs phonological subtypes
       regardless of lesion location" → impairment draft.
     * "MIT efficacy across mixed-lesion non-fluent aphasia (RCT,
       n=80)" → therapy draft.

   **Multi-bucket papers.** If one paper legitimately produces drafts
   in multiple buckets (e.g., a region anchor draft for the LSM
   finding *and* a therapy anchor draft for an embedded RCT analysis),
   that's fine — write one draft per bucket. The annotator handles
   multi-draft mode (`--draft a.md --draft b.md --pdf paper.pdf`) so
   you produce one annotated PDF per paper, not per draft.

3. **Refuse early when in doubt.** See "Refusal rules" below. A refused
   paper is a clean outcome; an over-confident extraction is not.

4. **Write each finding into the appropriate `drafts/` subfolder.** File
   naming convention:
   `drafts/regions/<region_id>__<citation_key>.md`
   for example: `drafts/regions/ho-cort_44__Fridriksson2018.md`.
   If a region file for that combination already exists in `regions/`, your
   draft *adds findings* by mirroring the existing file, appending your
   findings to the `findings:` list, bumping `status: draft`, and updating
   `created_by` / `created_on` to your run.

5. **Run `annotate_paper.py`** on the draft + the source PDF. This
   produces `papers/<basename>_annotated.pdf` with colored highlights
   showing exactly which sentences you extracted for each finding-aspect.
   Hand the user both the draft and the annotated PDF — the annotated
   PDF is the user's primary verification tool.

6. **Update `logs/extraction_log.md`** with one line per paper processed:
   `2026-04-29 | @Fridriksson2018 | 4 drafts | confidence: medium | flags: 2 | agent: claude-opus-4-7`

7. **Stop and ask** if you encounter any of the conditions in "When to ask
   the user" below.

---

## 1b. When to use predictor entries (v2.3)

A *predictor* is any measurable variable (a number on a chart, a test
score, a demographic field, an imaging-derived scalar) that papers use
as an *input* to predict an outcome — distinct from a brain region
(`regions/`), a clinical syndrome (`impairments/`), or an intervention
(`therapies/`).

**Use a predictor draft (`drafts/predictors/`) when** the paper's claim
is "patients with high/low X tend to show outcome Y" and X is measured
the same way (or by a closely-related family of instruments) across
patients regardless of lesion location:

- `severity_metric` — overall aphasia severity, from any instrument
  (WAB-AQ, BDAE severity, CAT, AAT, ASRS). Tag the finding with the
  exact `instrument` used in that paper. Examples: "Patients with
  baseline WAB-AQ > 60 responded better to semantic feature analysis
  (n=42, β=0.41, p=.003)"; "Severe-baseline patients (BDAE 0–1)
  responded to MIT but moderate-baseline patients did not."
- `lesion_volume` — "After controlling for lesion location, total
  lesion volume independently predicted naming severity (R²=.18, p<.001)."
- `age` — "Younger patients (<55) showed greater post-therapy gains
  in naming than older patients (n=68, p=.012)."
- `time_post_onset` — "Patients enrolled within 6 months post-stroke
  showed steeper recovery slopes than chronic patients."

**Use the `severity_metric` umbrella, not one entry per battery.**
Different studies use different instruments to measure the same
construct. Rather than fragmenting the literature into `wab_aq`,
`bdae_severity`, `cat_score`, etc. — which would also fragment a
clinician's prognostic query when the patient was tested with a
different battery — a single `severity_metric` entry holds findings
from any instrument and tags each finding with its `instrument`,
`score_band`, and `interpretation`. The interpreter
(`interpret_predictors()`) preferentially weights findings whose
instrument matches the patient's, but still surfaces cross-instrument
evidence.

**Don't create a predictor entry for** outcome variables that the paper
just *measures* (post-therapy WAB-AQ as the dependent variable of a
trial → that's a `direction: likely` finding on `target: severity_metric,
target_kind: predictor` from a *therapy* draft, not a finding *inside*
the predictor entry).

**Anchor perspective rule for predictors.**

- The paper's claim is "X predicts Y." Anchor on whichever side has the
  richer claim space:
  - If the paper's main finding is about *which lesion patterns make
    patients responsive* and they happen to also report baseline WAB-AQ
    as a covariate → the finding belongs in a *region* draft with
    `target_kind: predictor` (or `target_kind: therapy` if the actual
    target is the therapy). The predictor entry stays untouched.
  - If the paper's main finding is "WAB-AQ at baseline predicts
    responsiveness to therapy" with no lesion-location claim → write
    the finding *into the predictor entry* (`drafts/predictors/wab_aq__<key>.md`),
    targeting the therapy.

**File-naming convention for predictor drafts:**
`drafts/predictors/<predictor_id>__<citation_key>.md`
(e.g., `drafts/predictors/wab_aq__Schlaug2008.md`).

**Findings inside a predictor entry** follow exactly the same schema as
findings inside a region/impairment/therapy entry — same identity,
method, sample, statistics, confounders, source_passages, etc. The only
difference is the `target` typically points to a therapy, impairment,
or prognosis, not to another region.

**A predictor entry's findings should rarely have `relationship: causal`.**
Most behavioural/demographic predictors are `correlational` (the
predictor co-varies with outcome) or `responder` (the predictor
moderates therapy response). Only use `causal` if the paper makes a
genuine causal claim (rare, and almost always restricted to
`imaging_metric` predictors like lesion-load on a tract).

---

## 1c. When to use narrative review entries (v2.4)

A *narrative review entry* captures a synthesized theoretical claim or
consensus position from a review article (narrative review, systematic
review without formal meta-analytic pooling, or an opinion piece with a
well-supported argument). It is **not** a primary data finding — it
describes what the review author says the field believes.

**Use `method: narrative_review` when:**
- The paper is a narrative or systematic review with explicit, citable
  claims about brain regions, syndromes, therapy effects, or prognosis.
- The claims are not simply reportable by extracting from the primary
  papers (e.g., the review offers a theoretical synthesis, identifies a
  consensus across heterogeneous methods, or argues for a particular
  model that is not captured in any single primary paper).
- The review covers older or harder-to-access primary literature that is
  unlikely to be extracted separately.

**Do NOT use `method: narrative_review` when:**
- The claims are directly traceable to a primary paper already in the KB.
  In that case, add the claim to the primary paper's entry instead.
- The paper is a pure opinion piece with no structured treatment of
  evidence (refuse instead).
- The paper is a formal meta-analysis with pooled effect size tables
  (use `method: meta-analysis` instead).

**Draft location:** `drafts/reviews/` (new bucket in v2.4).

**Filename:** `{topic}__{CitationKey}.md`
e.g. `subcortical_aphasia__NadeauCrosson1997.md`

**Required fields per finding:**
- `method: narrative_review`
- `design: narrative-review` (or `systematic-review` if PRISMA-registered)
- `relationship: synthesis`
- `evidence_quality: narrative-review`
- `strength: weak` (default; upgrade to `moderate` only if the review
  explicitly synthesizes a large, consistent body of evidence)
- `source_passages` (verbatim quotes as usual — annotation still works)
- `author_limitations`
- `provenance`

**Omitted fields** (not applicable to reviews):
- `sample` — omit entirely
- `statistics` — omit entirely
- `confounders_controlled` / `confounders_not_controlled` — omit
- `region_definition` — omit
- `imaging_details` — omit

**Optional file-level field (verified primary studies only):**
```yaml
primary_papers_cited:
  - "@Smith2010"
  - "@Jones2012"
```

**Who the review cites, exactly.** A review supports its claims with
numbered or author–year references. For each one you list:

- Resolve it in the paper's own reference list (the number in the
  sentence → the entry at that number), and read authors, year and title
  there. Do not resolve it from memory or from a similar-looking key.
- Use an existing `citations.md` key only when its first author, year
  **and** title match that reference-list entry. Same surname and a
  nearby year is not a match: two papers by one author are different
  papers.
- List **primary studies only** (studies with their own patients or
  data). When the reference is itself a review, a textbook or a model
  paper, do not put it in `primary_papers_cited`; add a flag
  `secondary source for this claim: <first author> <year>, <title as printed>`.
- A reference that has no `citations.md` key yet: do not invent one. Add
  a flag `unregistered reference: <first author> <year>, <title as printed>`.
- Take the references from the sentence you quote for the claim. A
  reference cited for a neighbouring sentence supports that sentence,
  not this one.

**Hedges, figures and the review's own doubts.**

- Keep the review's degree of certainty. "Is often reported", "may
  contribute to", "appears more frequent", "remains to be confirmed" are
  part of the claim; do not turn them into "is" or "causes".
- Summary figures and their legends are schematic and often more
  categorical than the text. Quote the body text that makes the same
  point; use a legend only when the body never says it, label the
  passage `section: "Figure N legend"`, and keep its hedges.
- When the review itself states evidence that cuts against the claim
  (another study, a general statement that the factor does not predict
  the outcome, a selection bias), record it in `author_limitations`
  (and in `contradictions` when it is a citable paper). Do not resolve
  the tension yourself.

**Minimal example:**
```yaml
---
schema_version: 2.4
id: subcortical_aphasia_thalamus
name: "Subcortical Aphasia — Thalamic Mechanisms"
kind: classical
status: draft
created_by: "agent:<the model id you are running as>"
created_on: 2026-05-06
hemisphere: left

findings:
  - id: f1
    target: subcortical_aphasia
    target_kind: impairment
    claim: >
      Thalamic aphasia arises from disruption of a lexical-semantic
      activation-gating mechanism, not from direct language-area
      destruction; thalamic nuclei modulate cortical activation during
      word retrieval.
    direction: likely
    relationship: synthesis
    citation: "@NadeauCrosson1997"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: weak
    author_limitations:
      - "Synthesis based on small case series; no voxel-level evidence available at time of publication."
    provenance:
      extracted_by: "agent:<the model id you are running as>"
      extracted_on: 2026-05-06
      paper_section: "Discussion, pages 380-395"
      confidence: high
      flags: []
    source_passages:
      - section: "Discussion"
        page: 12
        quote: "thalamic aphasia arises not from direct destruction"
        supports: claim
---
```

---

## 2. Refusal rules

Refuse to produce a draft (and explain why) when:

- The paper is an **editorial, commentary, or letter** without primary
  data.
- The paper is a **single-case report** *and* the finding is not novel
  enough to warrant a `case-study` entry. Default: extract single cases
  only when the user explicitly asks.
- You cannot identify the paper's **method**. If you can't choose a
  `method` value from the controlled vocabulary, you do not understand the
  paper well enough.
- The **direction of the claim is ambiguous** in the paper. Don't guess.
- The paper is an **opinion piece or letter** (no systematic treatment of
  the evidence). These offer no extractable claims.
- The paper is a **meta-analysis with only aggregate statistics** and the
  primary papers it synthesises are already (or should be) in the KB. If
  the meta-analysis has primary quantitative tables (pooled effect sizes,
  pooled coordinates) that add new synthesised knowledge, extract as
  `method: meta-analysis` instead.
- The paper makes claims about **non-human models** or **non-stroke
  etiologies** unless the user has scoped the request to those.

---

## 3. When to ask the user (don't proceed silently)

Ask before continuing if:

- The atlas the paper uses is **different from the LINDA pipeline's atlas**
  and you can't tell whether the regions are equivalent. Surface the
  mismatch; let the user decide whether to map across atlases.
- The paper reports a **direction opposite to existing approved entries**
  on the same (region, target) pair. This is a contradiction worth
  surfacing for review, not silently overwriting.
- The paper's `sample.population` does not match the KB's intended scope
  (e.g., the KB is for adult chronic stroke aphasia and the paper is on
  primary progressive aphasia or paediatric aphasia). Confirm before
  extracting.

---

## 4. Field-by-field extraction guidance

For each `finding` field listed in `schema.md`, here's how to fill it
honestly. Re-read this whenever you're unsure.

### `claim`
One sentence in your own words. Mirror the paper's *direction* (likely vs
unlikely) but use plain language. **Never paste a paper sentence here** —
that's what `source_passages` is for.

Bad: `"Cluster centered on left BA44 was significantly associated with the speech-fluency factor (p<.001 corrected)."`
Good: `"Damage to the left inferior frontal gyrus pars opercularis is associated with reduced speech fluency in chronic stroke."`

The claim carries the context a reader needs to use it, and nothing
stronger than the paper:

- **Which analysis.** If the result holds only in one model (a
  univariate test, a variable-selection step, a model without the usual
  covariates), the claim says so, and says what happened when those
  covariates were added (see `statistics`). A result that disappears
  after adjustment is never reported as an unqualified predictor.
- **What the outcome is.** Name the dependent variable as measured: a
  score at a follow-up time point, a change between time points, a
  proportion of potential recovery, a diagnosis or classification. A
  score *at* follow-up is an outcome level, not "recovery"; use
  recovery/improvement language only when the dependent variable is a
  change.
- **Who and when.** The population and phase the result applies to
  (e.g. chronic left-hemisphere stroke, at least 6 months post-onset;
  or the same patients assessed in the first week and again at 3 months) when they limit the claim.
- **How sure the paper is.** Keep the authors' hedges; do not upgrade
  "may", "was associated with" or "in this small sample" to a general
  law.

### `direction`
- `likely` / `unlikely`: positive / negative finding (use with any
  `relationship`).
- `likely_responder` / `unlikely_responder`: legacy v2.0/2.1 shortcut
  for therapy responsiveness. In v2.2 prefer `relationship: responder`
  + `direction: likely | unlikely`.
- `no_effect`: the paper specifically tested and found no significant
  association (a useful and under-recorded class of finding). A
  non-significant result is **not** evidence that the effect is zero,
  least of all in a small sample: write the claim as "no significant
  (independent) association was detected", name the model and its
  covariates, and keep `strength: weak` unless the paper reports an
  equivalence test or adequate power for the effect in question.
- `mixed`: the paper reports both supporting and contradicting evidence
  within the same study.

### `relationship` (v2.2, required)

| value           | use when…                                            |
|-----------------|------------------------------------------------------|
| `causal`        | LSM, VLSM, MLPA, lesion-network mapping, disconnectome — "damage to X is associated with Y." |
| `correlational` | fMRI_FC, rs_fMRI, DTI, NODDI, EEG, MEG — "activity / integrity of X tracks Y" without a causal claim. |
| `recruitment`   | task-based fMRI_activation — "X is recruited / active during the Y task." |
| `responder`     | clinical_RCT or behavioral_only — "patients with X lesion / region pattern respond to Y therapy." |

The combination `relationship` + `direction` tells the reader exactly
what the finding means. `causal + likely` = "damage causes Y";
`recruitment + likely` = "X lights up for Y task";
`correlational + unlikely` = "X activity does not correlate with Y."

`interpret_overlap()` (the per-patient lesion → literature aggregator)
treats all four `relationship` values with `direction: likely` as
"damage to this region predicts the impairment" — which is the right
inference whether the underlying evidence is causal or correlational.
The `relationship` field preserves the epistemic distinction for
human readers and downstream agents.

### `method`
**v2.2:** can be a single string OR a list of strings. Pick the closest
entry/entries from the vocabulary in `schema.md`. If you can't pick one,
refuse the extraction.

- Single-modality paper (most LSM, most fMRI, most DTI):
  `method: LSM` or `method: fMRI_activation`, etc.
- Multimodal paper (fMRI + DTI; T1 + lesion-network mapping; etc.):
  `method: [fMRI_activation, DTI]`. Order doesn't matter for the
  loader, but list the *primary* method used to derive the specific
  finding first.

Common ambiguities:
- "Univariate VLSM" → `VLSM`. "Multivariate / SVR-LSM" → `MLPA`.
- "Lesion network mapping" (using a normative connectome) → `lesion_network_mapping`.
- An fMRI paper that reports both activation and connectivity → list
  both: `[fMRI_activation, fMRI_FC]`, with the dominant one first.

### `sample`
Read the **Methods → Participants** section. If the paper splits its
sample into subgroups, extract the sample size of the subgroup the finding
applies to, not the overall study n.

If a sample field is genuinely not reported (common for `age_range`,
`handedness`), use the literal string `not_reported`. Do **not** guess.

- **Use the paper's own wording** where the field is inferred from a
  criterion: "left-handed participants excluded" rather than "all
  right-handed"; "tested in Spanish (n = 30) or English (n = 12)" rather
  than "Spanish or English".
- **Time points from Methods and tables.** Take `time_post_onset` from the
  Methods and the participant table (range and mean as reported), not
  from the abstract's summary. If they disagree, use the Methods/table
  value and flag the inconsistency (see `statistics`).
- **Population** names what limits the result: aetiology, lesion side,
  first or recurrent stroke, setting, phase, severity range.
- **Which scan, which test.** In a longitudinal study, say which time
  point supplied each predictor and the outcome. If the paper does not
  say, flag it instead of assuming.

### `statistics`
Read the relevant **Results** sentence and the corresponding figure / table.

**Name the model.** Every estimate comes from a model: a dependent
variable, a set of predictors and covariates, and sometimes a selection
procedure (stepwise, backwards, best subset). Record, in the finding,
which model the number comes from and what else was in it. When a paper
reports the same predictor in more than one model — a restricted one
(univariate, selection step, a subset of predictors) and an adjusted one
(with the baseline score, age, lesion size or similar) — and the results
differ, report both: write one finding per model (see "Splitting
findings" in 6b) and make each claim name its model. A predictor that
survives only the restricted model is weak, exploratory evidence.

**When the paper disagrees with itself.** The abstract, the Results
text, a table and a figure sometimes give different numbers for the same
thing (an effect size, an R², a sample size, a follow-up window). Do not
pick one silently and do not average. Record each value with where it is
(`"β = 0.42 (Results text, p. 6); β = 0.39 (Table 2, p. 8)"`), prefer the
Methods / Results / tables over the abstract for what you put in the
structured field, and add a flag `source inconsistency: <field>: <value>
(<location>) vs <value> (<location>)`. Copy symbols as printed (β, χ², η²),
not spelled out.
- For LSM/VLSM: the threshold is usually permutation-based; report it
  exactly as the paper does (e.g., `"permutation p<.05 corrected; minimum cluster size 100 voxels"`).
- For RCTs: report the omnibus test threshold and the per-comparison
  effect size + CI when the finding is about a treatment effect.
- If only a *figure* shows the result with no numeric reporting in the
  text, set `statistics.threshold: not_reported` and add a flag.

### `confounders_controlled` / `confounders_not_controlled`
Read the **Methods** + **Results** sections. Common controls to look for:
lesion volume, age, sex, time post-stroke, education, baseline severity.
List what's controlled in the analysis that produced *this finding*.
Things that aren't controlled go in `_not_controlled`. If the paper truly
controls for nothing relevant, use `[]` for `_controlled` — don't fake it.
These lists describe *this finding's model*. If the same paper adjusted
for a variable in another model, say so in that model's finding and in a
flag on this one — `[]` here must not suggest that the adjusted analysis
was never done.

### `region_definition`
Critical for cross-study comparison. **How did the paper define the brain
region the finding is about?** Three common patterns:
1. **`atlas`**: paper used a named atlas → fill `atlas` and (ideally) the
   atlas index.
2. **`peak_coord_sphere`**: paper reports a peak voxel and built a
   spherical ROI → fill `mni_peak` and `radius_mm`.
3. **`data_driven_cluster`**: paper let the data define the cluster (LSM,
   ICA, etc.) → fill `description` with one sentence.

This field is what allows a downstream interpreter to know whether two
papers are talking about the *same* region.

### `replications` / `contradictions`
Only fill if the paper itself cites the prior work. Don't go fishing in
your training data. Use the same `@Key` style as `citation`. If the paper
references work that isn't yet in `citations.md`, add a flag and surface
it to the user — they can decide whether to add the reference.

### `author_limitations`
Read the **Discussion → Limitations** subsection (or the paper's Discussion
generally if there's no dedicated Limitations heading). Transcribe the
authors' own caveats in your words, one per list item. Do **not** invent
limitations — if the paper claims none, write `[]` and add a flag.

### `evidence_quality` (the *paper's* class)
- `meta-analysis`: a coordinate-based or effect-size meta-analysis.
- `RCT`: randomized controlled therapy trial.
- `cohort`: a typical group-level lesion-symptom or imaging study.
- `case-study`: a single subject or 2–3 subjects.
- `tentative`: preliminary, exploratory, or methodologically limited
  findings (e.g., uncorrected statistics, very small samples).
- `narrative-review` (v2.4): a synthesized claim from a narrative or
  systematic review. Always paired with `method: narrative_review` and
  `relationship: synthesis`. Downstream tools weight this evidence
  lower than quantitative findings.

### `strength` (the *agent's* read)
- `strong`: large sample, robust correction, large effect, replicated
  elsewhere (per the paper itself), no fatal confounders.
- `moderate`: typical group study, plausibly correct but not airtight.
- `weak`: small sample, marginal correction, or a known limitation
  affects the interpretation.

Be cautious. Sample size, a single site and lack of replication are
limitations to weigh alongside precision, design and adjustment, not
automatic strength rules on their own. Use `weak` for a result from a
variable-selection step or a model without the covariates the paper
itself uses elsewhere; a result that is not significant after
adjustment; a borderline overall model; a discrepancy in the paper's own
numbers; a narrative review (see 1c). `moderate` needs an adequately
sized, adjusted analysis whose result the paper reports consistently.

`strength` is your call as the extractor. It's not the same as
`evidence_quality` (which classifies the *paper*). A weak finding can
appear in a high-quality paper.

### `provenance.confidence` (the agent's confidence in the *extraction*)
- `high`: you have the full paper, you understood the relevant section
  end-to-end, no ambiguities about what the finding is, no field had to
  be inferred, and you flagged no inconsistency in the paper. Any
  `source inconsistency` flag, inferred field or unresolved reference
  means `medium` at most.
- `medium`: you have the paper but had to infer at least one field, or
  there's a borderline judgment somewhere.
- `low`: abstract only, or you noticed multiple ambiguities, or the
  reporting is poor enough that you're partly guessing.

If `confidence: low`, the user should expect to need to verify most of
the extraction.

### `provenance.flags`
Specific, one-line concerns. Write the kind of flag a reviewer needs to
act on. Bad flags are vague ("uncertain"); good flags name the field and
the issue.

Bad: `"unsure"`
Good: `"sample n inferred from Figure 1 caption — not stated in text"`
Good: `"effect direction is positive in Table 2 but negative in Figure 4 — verify"`
Good: `"source inconsistency: follow-up window 3–6 months (Abstract, p. 1) vs 2–7 months (Table 1, p. 4)"`
Good: `"time point of the imaging predictor not stated (scans at both visits)"`

`provenance.extracted_on` is the date of this run; the pipeline records
it. Never write a placeholder or example date.

### `source_passages` (REQUIRED in v2.1)

A list of `{section, page, quote, supports}` objects. Each one is a
short verbatim quote (1–3 sentences) and the category of finding-aspect
it supports. The annotator uses these to produce the colored
highlighted PDF, so quotes must be **exact** — `Ctrl+F` should find
each one in the PDF.

- **Copy one contiguous run of text exactly**, including citation
  brackets and symbols as printed (`[24, 81]`, `β`, `R²`, `–`). Do not
  join sentences from different places with `...` or `…`: two pieces of
  evidence are two passages. Do not elide clauses inside a sentence
  either; copy a shorter contiguous span without changing its meaning.
- **`page` is the one-based page of the PDF file** — the first page of
  the file is 1 — not the page number printed in the journal header or
  footer. The whole quote must be on that page; when a sentence runs over
  a page break, quote the part on one page or make two passages.
- **`section` is where the text actually is**: `Abstract`, `Results`,
  `Discussion`, `Figure 2 legend`, `Table 1 note`. Use the heading the
  text sits under, not the section you expected it in.
- Each passage must support what its `supports` tag says. A `claim`
  passage must state the claim as the finding words it, with its
  qualifications; a passage cited for a neighbouring statement does not
  count.

**Prose only.** A passage is a run of sentences from the body text (or a
figure legend, labelled as such).
Never quote a table row, a figure caption cell, or a set of values
joined with `|`: a text-layer search cannot find those, so the quote
fails the fidelity check and the draft is rejected. When a number is
reported only in a table, quote the results sentence that refers to
the table, record the number in `statistics.effect_size` /
`statistics.threshold` with its locator (`"Table 3, p. 7"`), and keep any
disagreement with the text as a flag. If a claim has no sentence in the prose that
states it, the paper does not make that claim extractably — leave it
out.

Aim for one passage per `supports` category that the finding actually
makes a claim about. Typical complete set per finding:

  - `claim` (1×)  — the headline result sentence
  - `sample` (1×) — the cohort description
  - `method` (1×) — the analytical approach
  - `statistics` (1×) — the threshold / effect-size sentence
  - `imaging_details` (1×) — acquisition + preprocessing
  - `region_definition` (1×) — how the region was defined
  - `limitation` (1× or more) — the authors' own caveats
  - `confounders` (0–1×) — only if explicitly listed

**Body before abstract.** Quote the body of the paper (Results,
Methods, Discussion), not the abstract. An abstract rounds numbers,
drops conditions and states the headline the authors want remembered;
the body states what was actually found, with its qualifications. So:

  - the `claim` and `statistics` passages come from the body;
  - when the sentence you want is in the abstract, find the body
    sentence that says the same thing and quote that one instead — it
    is nearly always there, usually in the first paragraph of the
    Results or the Discussion; do not keep the abstract version as well;
  - an abstract passage is acceptable only for something the body does
    not state anywhere (rare); label it `section: "Abstract"` and add
    `abstract_only` to `provenance.flags` so the reviewer looks at it.

If you only have the abstract (not the full paper), label every passage
`section: "Abstract"`, add `abstract_only` to `provenance.flags` and
lower `provenance.confidence` to `low`. The user will know the annotator
can only highlight the abstract in that case.

### `imaging_details` (new in v2.1; required for imaging-based findings)

Skip only when `method` is `behavioral_only` / `clinical_RCT` /
`meta-analysis` / `computational_model`. For everything else, fill:

  - `field_strength` — `"3T"`, `"1.5T"`, etc., or `not_reported`.
  - `acquisition.{voxel_size_mm, TR_ms, TE_ms, sequence}` — pull from
    the Methods *Imaging Acquisition* / *MRI Acquisition* section. Any
    sub-field can be omitted if not reported, but at least try for
    voxel size and sequence.
  - `preprocessing_pipeline` — one-line summary of the preprocessing
    stack (e.g. `"FreeSurfer 6.0 + FSL FLIRT/FNIRT to MNI152"`,
    `"SPM12 unified segmentation + DARTEL"`, `"ANTs N4 + diffeomorphic
    registration"`). The single most important field after
    `reference_space` for cross-study compatibility.
  - `reference_space` — `MNI152` / `MNI305` / `Talairach` / `native` /
    `other` / `not_reported`. Required (will fail validation otherwise
    for imaging-based findings).
  - `atlases_used` — list of strings, e.g. `["AAL", "HarvardOxford"]`.
    Required (use `[]` if the paper used no atlas, e.g. pure
    voxel-wise LSM with manual tracings).
  - `coordinates_reported` — list of `{region, mni: [x,y,z]}` for any
    peak coordinates explicitly given. The most useful imaging field
    for downstream interpretation, since you can spatially compare
    these to the patient's lesion location. Skip if the paper reports
    only cluster maps without peak coordinates.

**v2.2 — multimodal acquisition (`modalities`):**
For papers with more than one modality (e.g., T1 anatomy + task fMRI +
DTI), use the `modalities` list instead of (or in addition to) the
single `acquisition` block:

```yaml
imaging_details:
  modalities:
    - modality: T1
      sequence: MPRAGE
      voxel_size_mm: [1, 1, 1]
      TR_ms: 2300
      TE_ms: 2.96
    - modality: fMRI
      sequence: EPI
      voxel_size_mm: [3, 3, 3]
      TR_ms: 2000
      TE_ms: 30
      volumes: 240
    - modality: DTI
      voxel_size_mm: [2, 2, 2]
      n_directions: 64
      b_values: [0, 1000]
```

Each entry needs a `modality` key; the rest is free-form per modality.

**v2.2 — fMRI task (`task`):**
For findings whose `method` includes `fMRI_activation`, fill the
`imaging_details.task` block:

```yaml
imaging_details:
  task:
    name: "Picture naming"
    description: "Subjects named line drawings of common objects."
    contrasts: ["Naming > Rest", "Naming > Scrambled"]
    baseline: "Visual fixation"
```

Add a corresponding `source_passages` entry with
`supports: imaging_details` so the acquisition / task sentences get
highlighted in the annotated PDF.

---

## 4b. Before you write a finding — checklist

Check every finding against the paper, not against your memory of it:

1. **Claim.** Every clause is stated by a quoted passage (not a
   neighbouring one); hedges kept; the analysis/model it holds in, the
   outcome as measured (level vs change), and the population/phase named
   where they limit it.
2. **Models.** If the paper also reports this predictor adjusted for
   other variables, that result is a finding too; a non-significant
   result is worded as "not detected", not "no effect".
3. **Numbers.** Statistics, n and time windows taken from Methods,
   Results and tables; every disagreement between abstract, text and
   tables recorded with locations and flagged, not resolved.
4. **Passages.** Each quote is one contiguous run copied exactly
   (symbols and citation brackets as printed), on the one-based PDF page
   given, under the section it is actually in; body text preferred over
   abstract and figure legends.
5. **References.** Each cited key matches the paper's reference-list
   entry by first author, year and title; secondary sources are flagged,
   not listed as primary; unregistered references flagged, not invented.
6. **Target.** The target's definition (not just its name) matches the
   paper's measure; otherwise a forward-looking id and a flag.
7. **Limitations and counter-evidence.** The authors' caveats, and any
   evidence the paper itself gives against the claim, recorded.
8. **Strength and confidence.** As low as the evidence warrants (see 4);
   any inferred field or inconsistency caps confidence at `medium`.

---

## 5. Output format

For each paper:

1. Produce one **draft markdown file per (region, paper)** combination,
   placed in `drafts/regions/`. Same convention for impairment-targeted
   findings → `drafts/impairments/`, therapy-targeted → `drafts/therapies/`.
2. The frontmatter follows schema v2 exactly. Validate with
   `python scripts/aphasia_kb.py --check drafts/`.
3. Append one line to `logs/extraction_log.md`.

### File-naming convention

`drafts/<bucket>/<entry_id>__<citation_key>.md`

- `bucket` ∈ `regions`, `impairments`, `therapies`, `predictors`.
- `entry_id` is the existing entry's `id` (e.g., `ho-cort_44`) or, for a
  new entry, the proposed `id` you assigned.
- `citation_key` is the paper's `@Key` minus the `@`.

Examples:
- `drafts/regions/ho-cort_44__Fridriksson2018.md`
- `drafts/impairments/naming__Mirman2015.md`
- `drafts/therapies/mit__Schlaug2008.md`
- `drafts/predictors/wab_aq__Schlaug2008.md`

### When the entry already exists

If `regions/ho-cort_44.md` already exists and you're adding new findings
for it from a new paper:

1. **Copy the approved file** into `drafts/` under the naming convention
   above.
2. **Bump `status: draft`** and update `created_by` / `created_on` to your
   run.
3. **Append** your new findings to the existing `findings:` list. Give
   them new `id`s (`f4`, `f5`, …) that don't collide with existing ones.
4. **Do not modify** existing findings. The reviewer decides whether to
   accept your additions.

---

## 6. Discipline rules (non-negotiable)

- **Never invent a citation.** A paper you reference must match an entry
  in `citations.md` by first author, year and title (see 1c). Otherwise
  flag it as unregistered, with the details as printed in the paper's
  reference list, so a person can add it.
- **Never invent statistics, effect sizes, or sample numbers.** If the
  paper doesn't report the field, use `not_reported`.
- **Never silently change `direction`** based on prior knowledge. The
  direction comes from *this paper*.
- **Never write outside `drafts/`, `papers/`, `logs/extraction_log.md`, and
  `citations.md`.** No exceptions.
- **Always set `status: draft` and `created_by: agent:<your-id>`.**
- **Always update `logs/extraction_log.md`** in the same run.

## 6b. Naming conventions (decided 2026-05-01)

These are the conventions for target IDs. They were settled after the
Yourganov / Alyahya / Barbieri extractions and are now binding for
new drafts. The full rationale is in `schema.md`; the operational
rules are below.

### Always prefix region target IDs with hemisphere

New region target IDs must include a `left_` or `right_` prefix.
Examples:
  - `left_angular_gyrus`, `right_anterior_middle_temporal_gyrus`
  - `left_posterior_arcuate_fasciculus`, `right_temporal_pole`
  - `left_heschls_gyrus`, `right_ifg_pars_triangularis`

Treat hemisphere as part of the region's identity, not a separate
attribute. Legacy IDs without the prefix (e.g., `ho-cort_44`,
`arcuate_fasciculus`) stay as-is for backward compat — but **do not**
create new unprefixed region IDs.

This rule applies to *region* target IDs only. Impairment IDs
(`agrammatism`, `phonological_production`, etc.), therapy IDs
(`treatment_of_underlying_forms`), and predictor IDs (`severity_metric`)
are not hemispheric and don't take a prefix.

### Forward-looking target IDs are accepted

You may target an ID that doesn't yet have a canonical file. Pick a
descriptive snake_case ID, explain the measured construct in file-level
`notes`, and add a per-finding `provenance.flags` entry that its mapping
requires review. A person maps or creates the target entry before the
finding is approved; the id must therefore say plainly what it means.

### Use `VBCM` for VBCM analyses

If the paper cites Tyler et al. 2005 or describes a continuous-intensity
voxel-based correlation, use `method: VBCM` (not `VLSM`). VBCM was added
to the controlled vocabulary on 2026-05-01.

### Cross-paper cohort overlap → `provenance.flags`

When the cohort overlaps with another paper already in the KB (or
expected to be added later), add a flag of the form:

```
"cohort overlaps with @OtherPaperKey (same n=X subgroup, same trial
NCTxxxxx); flag for downstream double-counting risk in
interpret_overlap()."
```

Identifying overlap is your responsibility — check the paper's
"Participants" section for references to a parent cohort, registry
number, or a "subset of a larger study" clause. Common patterns:
shared NIH grant (e.g., P50DC012283), shared trial registration
(e.g., NCT01927302), and authors who appear together on multiple
papers in the same year.

### Treatment-induced reorganization → `relationship: treatment_response`

When a paper reports that a treatment causes activation changes in a
region (typically pre-vs-post fMRI), use
`relationship: treatment_response` (not `causal`). This is a v2.3+
addition that disambiguates "damage → impairment" claims (`causal`)
from "treatment → activation change" claims (`treatment_response`)
and from "patients with X respond to therapy Y" claims (`responder`).

### Name the therapy (v2.8)

Every `treatment_response` or `responder` finding, and every finding
that targets a therapy, carries a `therapy` block:

```yaml
therapy:
  id: cueing_hierarchy_naming_treatment      # a therapies/ entry id when one exists, else a forward-looking id
  name: cueing hierarchy anomia treatment    # as the paper calls it
  dose: 3 h/day, 2 weeks                     # optional, as reported
```

An activation change or a responder profile is evidence about *that*
intervention only. "Treatment" in the claim is not enough; quote the
sentence that names the intervention with `supports: method`.

### Symptom, not syndrome (v2.8)

`impairments/` has two kinds of entry: symptoms a test measures
(`anomia`, `fluency`, `semantics`, `syntactic_processing`,
`form_to_meaning` …) and classified syndromes (`anomic_aphasia`,
`brocas_aphasia`, `wernickes_aphasia`, `conduction_aphasia`,
`global_aphasia`). A finding targets a syndrome only when the paper
classified patients by type and the claim is about the type (lesion
predicts Broca's aphasia; SVM separates anomic from conduction aphasia).
A test score — whatever the sample was called — targets the symptom
**whose definition matches what the test measures**. Naming deficits
target `anomia` (not `naming`, `confrontation_naming` or
`anomic_aphasia`); `object_naming` / `action_naming` only when the paper
dissociates them.

### Map by definition, not by the word (target meaning)

A target id is a label for a definition. Before you choose a target,
read its definition (the `short_definition` and `assessment` given for
each entry) and check that the paper's measure is what the definition
describes. The same word in the paper is not enough:

- **Fluency** names different constructs. Verbal (word-generation)
  fluency tasks — letter or category fluency — measure lexical retrieval
  under time pressure. Connected-speech fluency measures rate, length
  and amount of spontaneous speech. A clinical fluent / non-fluent
  classification is a syndrome-level judgement. Map each to the entry
  whose definition describes it; do not map one to another because they
  share a word.
- **Severity** may be an overall battery score, one subtest, or a
  clinician's rating; record the instrument as the paper describes it.
- **Recovery** may be a follow-up score or a change score (see `claim`).

If no entry's definition fits the paper's measure, use a forward-looking
id that names the construct as measured (e.g. `verbal_fluency_task`) and
add a flag that a person should decide the mapping. When an existing
entry is close but not equivalent, prefer the forward-looking id with a
flag over a confident wrong mapping.

`instrument` is optional. When you fill it, describe the measure as the
paper does (its subtests and range, e.g. a 0–30 composite of three
subtests); never invent a `score_band` or clinical cut-off the paper
does not give.

### Behavioural-only findings inside an fMRI paper

Common case: a paper is primarily an fMRI study, but the
treatment-efficacy claim itself is behavioural-only. Code those
findings as:

  - `method: clinical_RCT` (or `behavioral_only` for non-RCT)
  - `imaging: none`
  - `region_definition.kind: not_reported` with a description noting
    "behavioural-only treatment-efficacy finding — no specific brain
    region"
  - `imaging_details.reference_space: not_reported` and
    `atlases_used: []` (the validator skips imaging-detail checks
    for these methods)

Then put the imaging-based findings from the same paper in separate
`f2`, `f3`, … entries with `method: fMRI_activation` (or VBCM, etc.)
and full `imaging_details`.

### Splitting findings when one paper's analyses disagree

When the same paper reports a positive finding under one analytic
choice (e.g., voxel-level FWE-corrected, or a regression without the
baseline covariates) and a null under another (e.g., ROI-level with
covariates, or the fully adjusted regression), do **not** code as
`direction: mixed`, and never keep only the positive one. Split into two
separate findings:

  - One finding with the positive result (`direction: likely`), its
    specific method / threshold, and a claim that names the model
    ("in a model without baseline severity …").
  - A second finding with the null result (`direction: no_effect`), its
    model and covariates (`confounders_controlled`), and a claim worded
    "no significant independent association was detected after
    adjustment for …" — not "has no effect".

Each finding carries its own statistics, region_definition, and
source_passages. The `direction: mixed` value is reserved for cases
where the *paper itself* reports both supporting and contradicting
evidence on the same analysis (e.g., subgroup-by-subgroup
disagreement), not for cross-analysis disagreement within one paper.

### Multi-paper region consolidation (for `promote.py`)

When `promote.py` first encounters a target ID that has findings
from multiple drafts across multiple papers (e.g., `left_heschls_gyrus`
from both Yourganov 2015 and Alyahya 2018), it consolidates by:

1. Creating one canonical region entry.
2. Appending all findings (one per paper) into the entry's `findings:`
   list, preserving citation + provenance.
3. Renumbering finding IDs to be unique within the file.
4. Carrying forward the hemisphere prefix in the canonical `id`.

If two drafts disagree, both findings stay; cross-link via
`replications` / `contradictions` rather than overwriting.

---

## 7. Worked example

See `docs/examples/region_ifg_opercularis_fridriksson2018.md` for a fully
extracted v2 entry. Pay particular attention to:

- How `not_reported` is used for `sample.age_range` and several
  `statistics` fields.
- How `provenance.flags` records the specific things a reviewer needs to
  verify.
- How `confounders_not_controlled` makes the analysis gaps visible.
- How `source_passages` is filled (or not — the example currently has a
  placeholder, which the agent should replace when the PDF is available).

---

## 8. When the user asks you to extract from multiple papers at once

Process them one at a time and produce one draft set per paper. Do not
combine findings across papers into a single file — every finding has a
single `citation`, and conflating papers makes provenance impossible to
audit.

After all papers are processed, summarize for the user: papers processed,
drafts written, refusals and why, papers requiring user input before
proceeding.
