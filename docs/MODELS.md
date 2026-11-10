# Choosing the local model

Every model the knowledge base uses runs on the maintainer's own
computer through Ollama; which one does which job is one line each in
`models.yaml`. Today the extractor is Gemma 4 31B (`gemma4:31b`)
and the independent reviewer Gemma 4 26B (`gemma4:26b`). This page is
about how those choices are made, so that the next person (or you in six
months) can see why, and can test a newer model the same way.

The short version: there is no best local model, only the best one you
have measured on papers you have already curated. Library pages and
benchmarks are hints; the measurement that counts here is whether the
model quotes the paper exactly, fills the schema, finds what a person
found, and does not over-claim. `benchmark_models.py` does that
measurement in one command (§3); the decision log (§5) keeps every
result, failures included.

---

## 1. What each role actually needs

The three roles stress a model differently. Upgrade `extract` first; it
is where quality is won or lost.

| Role | What it does | What matters, in order | What matters less |
|---|---|---|---|
| `extract` | Reads a full paper (30–80K tokens) and emits draft entries with **verbatim** `source_passages`. | 1. Long-context recall — can it find and quote text from page 14 accurately? 2. Reliable structured JSON. 3. Calibration — not inflating `strength`/`confidence`. | Reasoning depth, coding, vision, speed. |
| `review` | Short prompt, skeptical second opinion on a flagged draft. Can promote into the KB (with guardrails). | Judgement on a short context; honouring the JSON schema (decoding is schema-constrained, so this is mostly handled). | Context length. |
| `rag` | Summarises KB entries it is handed into a narrative report. Nothing is written back. | Speed. Fluency. | Almost everything else — a small model is fine. |

A model that is a better coder or reasoner is not automatically a better
extractor. The property that predicts extraction quality best is
**long-context retrieval fidelity**: the model must locate a specific
sentence deep in a long document and reproduce it exactly. A fabricated
or paraphrased quote is not a quality difference, it is a disqualifier
(see `compare_extraction.py`'s docstring).

### Does it need vision?

Not for the pipeline as it stands. The model never sees the PDF:

- `extract.py` opens the PDF with PyMuPDF and sends the model
  **plain text**, one `=== PAGE n ===` block per page (`get_text()`).
- `annotate_paper.py` is deterministic. It takes each `source_passage`
  from the draft, searches for it in the same extracted text, and
  draws the highlight with PyMuPDF. No model is involved.
- `batch_ocr.py` handles image-only (scanned) PDFs *upstream*, so by
  the time `extract.py` runs, every paper is text.

This is a design choice, not an oversight. The KB's integrity check is
"does this quote appear verbatim in the extracted text?" If the model
read page images instead, its quotes would be its own transcription of
pixels and would drift from the `get_text()` string the annotator and
`compare_extraction.py` search for — more false "absent quote" failures,
not fewer.

Where vision *would* help, and what it would cost:

- **Tables and figures.** Text extraction mangles multi-column tables
  and loses figures entirely (lesion overlap maps, forest plots). A
  vision model fed rendered page images alongside the text could read
  an effect size out of a table that `get_text()` scrambled. That is a
  pipeline change (render pages → send as images → still require the
  quote to match the text layer), not a model-selection change.
- **Badly OCR'd scans.** Same story: fix it at `batch_ocr.py` (a better
  OCR engine, e.g. a dedicated OCR model) rather than in `extract`.

Practically: most current workstation candidates have vision anyway
(`gemma4:*` and `qwen3.8:27b` are Text + Image; `granite4.2` is
text-only), so it does not narrow the choice. Just do not pay for it —
do not pick a weaker text model because it has a better vision encoder.

---

## 2. Hard constraints (check these before anything else)

1. **Context window ≥ 128K.** Papers run 30–80K tokens, and `extract.py`
   sizes `num_ctx` from the prompt. A 32K model silently truncates.
2. **Fits in memory with the KV cache.** Weights are only part of the
   cost; a 60K-token context adds several GB on top. Rule of thumb on a
   Mac with unified memory: weights + ~0.15 GB per 1K tokens of
   `num_ctx` must stay well under physical RAM. If it does not, Ollama
   spills to CPU without erroring and extraction slows ~10×. Watch
   `ollama ps` mid-run: anything other than `100% GPU` is the tell.
3. **Supports Ollama's `format` (JSON-schema constrained decoding).**
   All current Ollama models do; it is a server-side feature. Listed
   for completeness.
4. **Runs locally.** Tags ending in `-cloud` run on Ollama's servers and
   send the paper text off-machine. Never use them for the `extract`
   role on copyrighted PDFs — it defeats the purpose of this branch.
   `ollama_client.is_local()` warns, but only about the host, not the tag.

Rough memory tiers (Q4 quantisation, which is what a bare tag pulls):

| Machine RAM | Comfortable for `extract` | Notes |
|---|---|---|
| 16 GB | `gemma4:12b` (7.7 GB) | Keep `num_ctx` ≤ 48K. |
| 32 GB | `gemma4:26b` (16–19 GB) | Default today. Cap `num_ctx` around 64K. |
| 48 GB+ | `gemma4:31b`, `qwen3.8:27b`, `granite4.2:30b` (18–20 GB) | Full-paper context is fine. |
| 64 GB+ | Any of the above at a higher-precision quant (`-q8_0` tags) | Better quote fidelity; roughly double the weight size. |
| 128 GB (M5 Max MacBook Pro — the current dev machine) | `gemma4:31b-it-q8_0` (34 GB) or `gemma4:31b-it-bf16` (63 GB); `qwen3.5:122b` (81 GB); `nemotron-3.5-super:120b` (80–90 GB, 12B active) | Full-paper context with headroom. Two models can stay resident at once, so `extract` and `review` need not reload each other. Prefer MLX tags (`-mlx`, `-mxfp8`) on Apple Silicon for speed; they are text-only, which is fine here. |

Quantisation matters more for this job than for most. A Q4 model's
reasoning survives quantisation well; its ability to reproduce a long
string *exactly* survives it less well. When memory allows, prefer
`q8_0` (near-lossless) over the bare tag, and `bf16` over `q8_0` only
if the comparison shows a difference — it is twice the memory and
roughly half the speed for usually no measurable gain.

---

## 3. The decision procedure

Run this for every candidate before changing `models.yaml`. It touches
nothing in the canonical KB.

### 3.1 In one command

```bash
python scripts/benchmark_models.py --list-references
python scripts/benchmark_models.py --models qwen3.8:27b ornith-1.5:122b --papers Alyahya2018NounVerb Bonilha2014
python scripts/benchmark_models.py --models qwen3.8:27b --papers Alyahya2018NounVerb --skip-extract --append-log
python scripts/benchmark_models.py --models qwen3.8:27b --auto-papers 2 --min-findings 5 --seed 7
python scripts/benchmark_models.py --untested --sandboxes --resume --papers Alyahya2018NounVerb Bonilha2014 --publish
```

The last line is how to carry on after a run was interrupted, and how
to publish: `--resume` keeps the drafts already in `_compare/` and only
extracts what is missing, `--sandboxes` scores every model that has a
sandbox so the table is complete, and `--publish` writes
`export/model-benchmark.json`, the numbers-only summary behind the
explorer's **Models** page (commit and push it). A draft a model writes
so badly that it cannot be parsed is counted against that model as a
schema issue; it does not stop the run.

`--untested` lets the script choose the models too: every candidate in
the §4 tables that fits this machine and has neither a row in §5 nor a
sandbox in `_compare/` yet, pulled if needed. Rows the tables mark as
superseded or lower quality are skipped unless `--all-candidates`. So
the full check-up is one line:

```bash
python scripts/benchmark_models.py --untested --auto-papers 2 --seed 7 --append-log
```

`--auto-papers N` lets the script choose the papers: N reference papers at random,
each with at least `--min-findings` canonical findings and a PDF, from
N different buckets (so a candidate is tried on, say, a lesion-symptom
paper and a therapy trial, not two of the same kind). Human-reviewed
papers are preferred; `--seed` makes the draw repeatable and the pick
is written into the results.

`benchmark_models.py` runs the steps below for every model × paper, adds
the incumbent from `models.yaml` for comparison, scores each run and
prints two tables: one row per model × paper, and one verdict per model.
Results go to `_compare/benchmark_<date>.{md,json}`; `--append-log`
copies the rows into §5 with the Decision column left for you.

### 3.2 How we decide — the metrics, and why these

| Metric | What is measured | Why it matters | Passing |
|---|---|---|---|
| **Fidelity** | Every `source_passage` graded against the PDF text (`quote_check.py`): exact / elided / table are verified; anchored and near are real but not verbatim; **absent** means the passage is nowhere in the paper | The KB's claim is that every finding can be checked against the paper. A fabricated quote is not a quality difference, it is a disqualifier | 0 absent on every test paper |
| **Schema** | Validation issues across the drafts (`aphasia_kb.py`) | Every issue is reviewer time on every paper | No more than the incumbent |
| **Coverage** | Findings and entries vs the curated reference; *link recall*: the share of the reference's entry ↔ target links (say, left angular gyrus ↔ phonological production) the candidate also produced, whichever entry it filed the finding under and under whichever spelling of the id; *link precision*: the share of the candidate's links the reference has too | Fewer findings may be a miss or restraint; recall says whether the known results were found. Links the reference lacks can be real finds or noise — read them. A finding whose target is its own entry links nothing and counts for nothing | Informative, not pass/fail |
| **Calibration** | Mean strength and confidence vs the reference | Over-claiming is the classic small-model failure. A model that under-claims is the safer extractor | Not more over-claiming than the incumbent (+0.2 tolerance) |
| **Support** | Source passages per finding | Thin support means the reviewer has to go and find the evidence | Informative |
| **Cost** | Wall-clock per paper; `ollama ps` processor split during the run | A CPU spill makes a model unusable in practice; twice as slow is acceptable if it never fabricates | Informative |

The reference papers are the ones whose canonical findings a person
approved after reading the PDF (`--list-references` lists them; it also
says which papers are not usable yet because their findings are legacy
or model-reviewed). Use two or three papers of different kinds; a model
that passes on a lesion-symptom mapping study can fail on a therapy
trial.

**Eligible** means: zero absent quotes on every paper, and schema issues
and calibration no worse than the incumbent. Eligible is not adopted:
read the claims (`compare_extraction.py --show-claims`), weigh speed
and memory, write the row in §5 with your decision and reasons.
Failures are logged too; they save the next person an afternoon.

### 3.3 By hand

```bash
# 0. Pick 2–3 papers you have ALREADY curated and are confident in.
#    Choose different kinds: a lesion-symptom mapping study, a therapy RCT,
#    a review. One paper is not enough — results vary by paper type.
PAPERS="Goldenberg1994 Fridriksson2018 Brady2016"

# 1. Pull the candidate
ollama pull qwen3.8:27b

# 2. Sandbox extraction, one directory per model
for p in $PAPERS; do
  APHASIA_EXTRACT_MODEL=qwen3.8:27b \
    python scripts/extract.py --pdf papers/$p.pdf \
      --out-dir _compare/qwen3.8-27b
done

# 3. Compare each against the approved entries
for p in $PAPERS; do
  python scripts/compare_extraction.py --citation @$p \
    --candidate-dir _compare/qwen3.8-27b --show-claims
done

# 4. Note wall-clock and `ollama ps` PROCESSOR while step 2 runs.
```

(`_compare/` is git-ignored — it contains verbatim paper text.)

Read the four sections of the comparison output in this order and stop
at the first failure:

1. **Quote fidelity.** Any `absent` source passage disqualifies the
   model for `extract`, full stop. Do not rationalise it. The KB's
   whole design rests on every quote being checkable against the PDF.
2. **Schema validity.** Drafts that would not pass `auto_review` cost
   you time on every paper. A few warnings are tolerable; errors are not.
3. **Coverage.** More or fewer findings than the curated version is *not*
   automatically good or bad — read the claims. A candidate that finds a
   real result the earlier pass missed is a point in its favour.
4. **Calibration.** Systematically higher `strength` or `confidence`
   than the curated entries is the classic small-model failure. Prefer
   a model that under-claims.

Only then weigh speed and memory. A model that is twice as slow but
never fabricates a quote is the better extractor.

**Known limit — output length, not model.** A dense paper (Alyahya
2018: 33 curated findings, ~155 passages) needs ~40K output tokens to
extract in full; the `extract` role caps at `max_tokens: 16000`, so a
single call returns the headline finding per region and stops. Raising
`max_tokens` costs time roughly linearly (31b-q8 writes ~7 tok/s). The
alternative is a second pass per paper ("here are the findings already
drafted; what significant results in the Results text are not yet
covered?"), which is on the to-do list for `extract.py`.

**Decision rule:** change `roles.extract.model` only if the candidate
has zero absent quotes on all test papers **and** is at least as good
as the incumbent on schema validity and calibration. Log the result in
§5 either way, including the failures — a logged "tried X, fabricated
quotes on paper Y" saves someone else an afternoon.

For `review`, the bar is lower (schema-constrained output, short
context, guardrails downgrade `override_approve` unless
`--allow-local-override`). Reuse the extract model unless it is too slow.
For `rag`, use the fastest model that writes acceptable prose.

---

## 4. Landscape snapshot — *perishable, re-check before trusting*

Checked against the Ollama library on **2026-10-16**, re-checked
**2026-11-09** (no change in the 48 GB class; one new 120B-class
candidate, Ornith-1.5 122B, added below). Local models move fast; treat
anything older than ~3 months here as stale and re-run §3.

Candidates for `extract` that satisfy the hard constraints and fit a
32–48 GB workstation:

| Tag | Arch | Weights (Q4) | Context | Why it is on the list | Caveat |
|---|---|---|---|---|---|
| `gemma4:26b` | MoE, 3.8B active | 16–19 GB | 256K | **Current default.** Fast (few active params), fits 32 GB. | Weakest long-context recall of the Gemma 4 workstation models: 44.1% on MRCR v2 8-needle 128k vs 66.4% for the 31B dense. That benchmark is the closest public proxy to "quote page 14 verbatim". |
| `gemma4:31b` | Dense | 19–20 GB | 256K | **Current extractor (2026-11-10).** Same family, markedly better long-context recall (66.4% MRCR). | Dense → noticeably slower per token than the 26B MoE. |
| `gemma4:12b` | Dense | 7.7 GB | 256K | Fits 16 GB machines. | Lower quality; expect more review work. |
| `qwen3.8:27b` | Dense | 18 GB | 256K | Newest Qwen; strong on "professional work / research" tasks; vision support irrelevant here. | No public long-context number on the Ollama page; measure it. |
| `granite4.2:30b` | Dense | 18 GB | 128K | IBM explicitly trains for structured JSON output and RAG; Apache 2.0. | 128K ceiling (fine for papers, tight for long reviews). |
| `qwen3.6:27b`, `qwen3.5:27b` | Dense | ~18 GB | 256K | Previous Qwen generations, very widely used. | Superseded by 3.8; only if 3.8 misbehaves. |

Only for ≥ 96 GB machines (so, the 128 GB M5 Max):

| Tag | Arch | Weights | Context | Why it is on the list | Caveat |
|---|---|---|---|---|---|
| `gemma4:31b-it-q8_0` | Dense, 8-bit | 34 GB | 256K | **Extractor from 2026-10-19 to 2026-11-10**; replaced by plain `31b`, which did no worse at half the cost (§5). Same model as `31b`, near-lossless quant. `31b-mxfp8` (34 GB, MLX) is the Apple-Silicon-native equivalent. | ~Half the speed of the 26B MoE. Fine for batch runs. |
| `gemma4:31b-it-bf16` | Dense, full precision | 63 GB | 256K | Removes quantisation as a variable entirely. | Slow; only to settle whether q8 is losing anything. |
| `qwen3.5:122b` | MoE | 81 GB | 256K | Largest Qwen that fits. | 7 months old; Qwen 3.8 is a newer generation at 27B. Measure rather than assume bigger wins. |
| `nemotron-3.5-super:120b` | MoE, 12B active, hybrid Mamba-2 | 80–90 GB | 1M | NVIDIA pitches it for document understanding; MoE so it is fast for its size; released this week. | Leaves ~40 GB for KV cache — set `num_ctx` explicitly. OpenMDW licence; check it suits the KB's licence. |
| `ornith-1.5:122b` | Dense-class 122B (vendor: "frontier-level, superior instruction following") | 73–77 GB | 256K | Released 2026-10-20; the only new entrant in this class since the last check. Untested here. | Leaves ~50 GB for the KV cache; licence to check. Run §3 before believing the pitch. |

Considered and set aside:

- **`medgemma:27b`** — medical fine-tune, but of Gemma **3**, which
  scores far below Gemma 4 on every reported benchmark (MRCR 13.5%).
  Domain vocabulary does not compensate for weak long-context recall.
- **The "decision model" wave** (`clef`, `nimble`, `kev`, `tev1`, …) —
  small models that take a text state plus a typed-question schema and
  return a decision in one forward pass. Not extractors. Possibly
  interesting for the `review` role later; untested.
- **Anything tagged `cloud`** (`muse-spark-open`, `mistral-large-4`,
  `glm-5.3`, `kimi-k3`, `deepseek-v4.1-flash`, …) — these are stronger
  models but run off-machine. Excluded by constraint 4.
- **MoE "always-on agent" models** (`nemotron-3.5-lightning`,
  `muse-glimmer`, `laguna-xs-2.1`, 30B total / ~3B active) — fast and
  cheap, built for tool loops rather than long-document reading. Worth
  a run for `rag`, not for `extract`.

**Recommended experiments on the 128 GB M5 Max, in order:**

1. `gemma4:31b-it-q8_0` for `extract` (or `31b-mxfp8` if MLX proves
   faster on this machine — try both on one paper and keep the faster).
   `gemma4:26b` stays on `review` and `rag`. This is the likely new
   default; it only needs to pass §3.
2. `qwen3.8:27b` for `extract` — a different family, so its failure
   modes differ. If it beats Gemma on calibration, consider it for
   `review` even if Gemma stays on `extract`.
3. `nemotron-3.5-super:120b` — the "does a much bigger model actually
   help?" experiment. Expect it to be better at tables and dense
   methods sections; verify it does not cost quote fidelity.

If on a 32–48 GB machine instead: `gemma4:31b` (Q4) if it fits, else
stay on `26b`.

---

## 5. Decision log

Append one row per experiment. Keep failures; they are the useful part.

| Date | Role | Candidate | Papers | Absent quotes | Schema | Coverage vs curated | Calibration | Speed / GPU | Decision | By |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-24 | extract | `gemma4:26b` | — | — | — | — | — | — | Adopted as initial default (fits 32 GB; MoE speed). Not yet benchmarked with `compare_extraction.py`. | branch author |
| 2026-10-16 | extract | `gemma4:31b-it-q8_0` run 1 | Fridriksson2018Anatomy | 9/18 absent | 10 issues (`method: RLSM` not in vocab) | 10 findings / 5 entries vs 8 / 2 | 2.50 vs 2.75 (under-claims) | 20 m 21 s, 58K in / 8.4K out, 100 % GPU, RAM 69 % | **Not adopted yet.** All 9 "absent" quotes were table rows written as `a \| b \| 0.60` — real cells, wrong form. Fixes: prose-only passage rule in the prompt + skill; `RLSM` added to vocab (v2.5). | michele + Claude |
| 2026-10-19 | extract | `gemma4:31b-it-q8_0` run 2 | Fridriksson2018Anatomy | **0/16 absent** (6 exact, 4 elided, 3 table, 3 anchored) | 0 | 7 findings / 5 entries vs 8 / 2 (dropped the naming→AG finding) | 2.71 vs 2.75 | 22 m 43 s, 58K in / 9.3K out, 100 % GPU | **Passes fidelity on paper 1.** Still cites table cells for statistics despite the rule; thin on sample/method/limitation passages (16 vs 60). Reference entries for this paper are `legacy`, so coverage/calibration need a human-reviewed paper next: Alyahya2018NounVerb, Bonilha2014, then Goldenberg1994 (OCR). | michele + Claude |
| 2026-10-19 | extract | `gemma4:31b-it-q8_0` | Alyahya2018NounVerb (human-reviewed reference) | **0/37 absent** (14 exact, 16 elided, 7 anchored) | 8 issues: `author_limitations` omitted on every draft; empty `region_definition` on the predictor draft | 8 findings / 8 entries vs 33 / 6 | 2.12 vs 2.18 | 30 m 37 s, 67K in / 12.2K out, 100 % GPU | **Passes fidelity on paper 2.** Coverage is the gap: one headline finding per region, and 33 full findings would need ~40K output tokens against a 16K `max_tokens` cap — dense papers cannot be extracted in one call. Fixes: limitations rule in the prompt; `extract.py` now fills `author_limitations: []` with a verify flag (→ Tier B), drops empty predictor `region_definition`, and keeps the citation key's case (`NounVerb`, not `Nounverb`). Next: run `gemma4:26b` on both papers for the incumbent comparison the rule asks for. | michele + Claude |
| 2026-11-10 | extract | `gemma4:31b-it-q8_0` (incumbent) | Alyahya2018NounVerb, Robson2019 (random pick, seed 7; references 17/33 and 2/6 human-reviewed) | 0/21 and **2/6 absent** (one elided limitations passage, used in two drafts, whose fragments are not in the paper) | 0 | 4 + 2 findings vs 33 + 6; **4 of 24 known links** | 2.25 vs 2.18; 2.0 vs 1.0 | 20 m 0 s and 9 m 38 s, 100 % GPU | Fails its own rule on this run. Note the spread between runs of the same model on Alyahya: 8 findings on 2026-10-19, 4 today. | michele |
| 2026-11-10 | extract | `gemma4:31b` | same | **0/32 and 0/6 absent** | 0 | 7 + 2 findings; **7 of 24 known links** (5 of 22, 2 of 2), precision 78 % | 2.0 vs 2.18; 2.0 vs 1.0 | 11 m 43 s and 3 m 11 s, 100 % GPU | **Adopted for `extract`.** Same weights as the incumbent at the default quantisation: no fabricated quote, no schema issue, at least as many known links, about half the time and memory. Two papers cannot show it is better in quality; they show the 8-bit quantisation buys nothing measurable here, so the cheaper model wins. Re-test when the reference papers are fully human-reviewed. | michele |
| 2026-11-10 | extract | `qwen3.8:27b` | same | 0/30 and 0/6 absent | 4 issues (Robson2019) | 5 + 2 findings; 2 of 24 known links — on Alyahya every finding targets its own entry, so no region is named | 1.8 vs 2.18 (under-claims) | 7 m 10 s and 1 m 44 s, 100 % GPU | Not adopted: fastest and honest with quotes, but loses the region ↔ impairment link, which is the point of the KB. Worth a second look for `review`. | michele |
| 2026-11-10 | extract | `granite4.2:30b` | same | **8/30 absent** (table-like "Psycholinguistic variable: …" strings and a sentence about lesion volume that the paper does not contain) | 3 issues: both Robson2019 drafts are unparsable YAML | 10 + 0 findings; 1 of 24 known links, precision 10 % | 2.0 vs 2.18 | 39 m 35 s and 14 m 26 s, 100 % GPU | **Rejected for `extract`:** fabricates, slowest, and wrote files the pipeline cannot read. | michele |
| | | | | | | | | | | |

---

## 6. Housekeeping

- `python scripts/model_config.py` shows which model each role
  resolved to, which layer won (CLI → role env → `APHASIA_LOCAL_MODEL`
  → `models.yaml` → `default`), and whether it is pulled.
- `--pick-model` on `extract.py` lists pulled models interactively for a
  one-off run. (As of the branch's first commit it filters to tags
  containing "gemma" — see `extract.py`, the `name_filter` argument —
  so widen or drop that filter before A/B-ing a Qwen or Granite model.)
- When you change `models.yaml`, add a §5 row in the same commit.
- `ollama list` shows what is pulled and how much disk it takes;
  `ollama rm <tag>` removes a losing candidate.
