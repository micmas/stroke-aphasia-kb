# Local models

The supported extraction workflow uses two independent local extractors, followed
by a separate local source reviewer. See [HOWTO](HOWTO.md) for the complete process.
Models run through Ollama on the local machine. Install the chosen model tags
before starting a batch; available hardware and context capacity constrain the
size of paper that can be processed.

| Role | Configuration | Current behavior |
|---|---|---|
| Extractor A and B | `kb.py extract --models MODEL_A MODEL_B` | Defaults: `gemma4:31b`, `qwen3.8:27b`; independent source-text prompts, serial calls |
| Source reviewer | `kb.py review --model MODEL` | Required explicitly; first reads source blind, then reconciles both outputs |
| Visual verification | Separate review task | Neither batch extraction nor source reconciliation currently sends page images |

A reviewer must differ from both extractors. The reviewer checks model tags and
currently installed digests to reject aliases of the same weights. Historical
extraction runs did not record extraction-time digests, so current digest checks
cannot establish which weights a tag referred to in the past. Prefer a different
model family, record the chosen version, and inspect a small review pilot before
running the whole corpus. No reviewer is yet established as the most accurate.

Both extraction and review default to 20,000 output tokens per call. Set
`--max-output-tokens` explicitly when necessary. Input capacity and output allowance
are different limits: segment a paper whose input is too large rather than merely
raising the output allowance. Preparation accepts `--segment-chars 50000` for
bounded extraction. Whole-paper local review still has an input limit and does
not yet implement segmented reconciliation.

## What has been established

Manual source audits found complementary coverage from the two extractors and
errors shared by both. Reconciliation can identify omissions and disagreements,
but valid JSON, matching quotations and agreement do not establish semantic
accuracy. A controlled, source-verified comparison has not established a numerical
accuracy advantage over single-model extraction. The dual workflow is the current
corpus evaluation workflow, not a claim of validated superiority.

Compare methods against the same independently checked main PDFs, counting
unsupported or incorrect claims, omitted important results, and critical errors in
numbers, anatomy, adjustment or interpretation. Include difficult tables, null
results, long papers and diverse study designs. Keep the reference review separate
from the model outputs and report disagreements and uncertainty. Adopt a common
method across the KB once this comparison supports it; every replacement still
needs source verification and approval.

## Other configuration

`models.yaml` serves existing screening, report-generation and compatibility tools.
It does **not** choose the models for `kb.py extract` or `kb.py review`; those use
the command options above. Saved run settings, prompts and hashes are the record
of what was used. Do not modify code, prompts or settings underneath an active run.

Consult each model's own licence before deployment or redistribution. Repository
code licensing does not grant rights to model weights or source papers.
