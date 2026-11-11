# Local source review of completed extraction pairs

`review_dual_extract.py` implements an optional local **text reconciliation**
stage. It does not approve findings, replace drafts, or certify completeness.
The running full-corpus extraction scripts and their frozen prompts are unchanged.
Command consolidation is deferred until that extraction run is finished.

## Run from the normal checkout

Stop extraction with Ctrl-C first. Completed pairs remain usable; an interrupted
pair is skipped. The reviewer holds the extraction batch's lock, preventing that
batch from restarting while review runs. Do not start competing inference jobs
through other commands.

Preview without inference:

```sh
.venv/bin/python scripts/review_dual_extract.py \
  --run-dir _compare/full-corpus-2026-11-11/run \
  --output-dir _compare/full-corpus-2026-11-11/local-review \
  --model granite4.2:30b --limit 3
```

Add `--run` to execute. `granite4.2:30b` was installed on the development machine
and differs from the extraction models; it is an example, **not an evaluated
best reviewer**. Choose an installed reviewer with `--model`; no model is
silently selected, downloaded or substituted. Run the three-paper check first
and inspect the resulting audit and decisions before removing `--limit 3`.

The same command reuses previously completed review outputs only when source,
model digest, budget, code and output hashes match. Newly completed paper pairs
can subsequently be reviewed with the same output directory. Failed or
interrupted review attempts are preserved: use a new output directory for a
retry. The reviewer does not change or retry failed extraction attempts.

## What runs locally

For each completed paper pair:

1. Verify the PDF hash, both extraction metadata records, saved prompts and
   source units. Reproduce the units from the actual main PDF. Reject partial,
   mismatched or truncated inputs. Preserve extraction audit warnings for review.
2. Obtain a fresh source-first inventory from the reviewer using only the
   original main-paper text, before showing either extractor's answer.
3. Ask the same reviewer to reconcile the original text, its blind inventory,
   both extractions and their audit warnings. Require a decision for every
   original analysis and coverage accounting for every source-text unit.
4. Audit the reconciled schema, original-to-final decision links, coverage links
   and exact source evidence. Record uncertainties and missing visual checks.

Ollama must use a loopback address. Temperature is zero, thinking is off, and
output budget defaults to 20,000 tokens **per call**. Each paper therefore uses
two reviewer calls. Prompts, raw answers, settings, model digest, input hashes,
audit results, errors and timings are saved. There are no silent retries or
truncation-based fallbacks. Large reviews may still exceed context/output limits;
these require a separate segmentation design, not silent text removal.

A different installed digest and model tag from both extractors are required.
The old extraction runner did not capture model digests at extraction time:
identity comparisons use its recorded tags and their current installed digests.
This limitation is recorded in each review's status; the check cannot prove that
an old tag never changed. Different models can still share the same mistake.

## Outputs and meaning

Each paper gets `source-first/` and `reconciliation/` prompt/raw/metadata files,
`inventory.json`, `decisions.json`, `coverage.json`, `audit.json`,
`provisional-extraction.txt`, `visual-review-required.json` and `status.json`.

- `failed`: generation, input integrity, transport, parsing or truncation failure.
- `requires_revision`: reconciliation has quotation, schema, coverage or decision
  validation issues. Raw outputs and diagnostics remain available.
- `requires_visual_review`: those deterministic checks passed. This is **not**
  a semantic accuracy guarantee or final approval.

Every status has `approved: false`. Study context and narrative synthesis remain
model-generated text; the deterministic audit does not prove their accuracy.
Complete source-unit accounting also cannot prove that every result was noticed.

**Visual review is not implemented in this command.** It supplies text only and
marks every main-PDF page as still eligible for visual checking. It cannot verify
image-only estimates, table alignment, figure labels or OCR fidelity. The absence
of a model-reported visual issue never clears that requirement. Source tables and
figures must be checked in the subsequent review stage before claiming a complete
extraction. Supplements remain outside scope. A future local vision stage needs
its own evaluation and documented behavior.

## Validation

Regression tests use mocked model responses to check source preservation,
independent source-first input, evidence and coverage failures, truncation,
model aliases, concurrent extraction, output integrity and safe resume. They
establish software behavior, not reviewer scientific accuracy. No real reviewer
inference was started while building this stage during the extraction run.
