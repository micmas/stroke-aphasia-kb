# Independent local extraction development — 11 November 2026

Two models independently extracted two known papers, using the same frozen main-PDF source and prompt per paper. Claude reconciled the two outputs against the sources; Codex audited the reconciled records. Supplementary files were excluded by explicit user scope. This is development on previously reviewed papers, not a new held-out evaluation.

## Local inference

Model tags: `gemma4:31b` and `qwen3.8:27b`. Temperature 0, thinking off, maximum output 10,000 tokens, context 32,768. Runs were serial, and neither model received the other's response. The installed model digests were captured in the experiment directory. No weights changed and no model was installed.

| Paper | Model | Analysis records | Exact-source audit issues | Approximate model time |
|---|---|---:|---:|---:|
| OsaGarcia2020 | Gemma | 11 | 4 | 110 s |
| OsaGarcia2020 | Qwen | 12 | 1 | 179 s |
| Thye2018 | Gemma | 20 | 9 | 157 s |
| Thye2018 | Qwen | 15 | 2 | 185 s |

Audit issues are quotation/source-unit mismatches, not a scientific accuracy score. Counts of analysis records are not directly comparable because the models split and combine analyses differently. All four outputs require review. The model times are single observations, affected by caching and resource conditions.

## What changed

The new prompt inventories the source's outcomes and statistical models before any KB mapping. On Thye, both models now include the five outcome-specific comparisons of template lesion load after accounting for lesion size, which were missing from the earlier KB-shaped extractions. Both preserve the central distinction between the added location information for production/recognition and the adjusted nulls for broader scores. This is encouraging evidence on a known paper, not evidence of generalisation.

On Osa, both identify the diffusion-only backwards model separately from the adjusted hierarchical models. Qwen includes a first hierarchical block that Gemma omits. However, both misuse `selected_predictors` for a coefficient that is significant in an entered model; source review corrects that shared error. Qwen also mistakes R² from different blocks for a source discrepancy and incorrectly says VIF values are absent. Both omit some main-paper information.

Independent extraction therefore helps expose differences and recover coverage, but agreement cannot substitute for source checking. The third-model review itself needed a correction: its initial prose overgeneralised initial severity's significance to every multivariable model, including a diffusion-only model that did not contain that variable. Codex requested a source-grounded restriction to the relevant hierarchical models.

## Data integrity and implementation

Claude's delayed blind review of the earlier Thye baseline discovered duplicate YAML `source_passages` keys: a permissive loader silently kept only two of eight raw passages. Strict JSON/YAML loading now rejects duplicate fields at extraction/KB parsing boundaries. Explicit YAML merge overrides remain valid.

The optional dual-extraction command preserves both raw inventories and prepares a source-review packet; it never creates approved findings. The current inventory runner preserves truncated/partial responses and fails rather than silently retrying with instructions to be selective. These transport protections were added after the four runs; logs show that those runs did not retry or truncate, and their prompts are unchanged.

Automated verification: **143 Python tests passed**, with five existing PyMuPDF/SWIG deprecation warnings. Tests cover duplicate-key evidence loss, independent input paths, source/prompt mismatch refusal, evidence locations, missing inventoried outcomes, truncation preservation, empty-source rejection, failed-run preservation and overwrite refusal, alongside the existing suite.

## Scope and artifacts

Local experiment directory: `/Users/uqmmasso/GITHUB/_coordination/extraction-accuracy-round2-2026-11-11`.

- `freeze.json`, `scope.json`, `installed-models.json`: design, source scope and model provenance.
- `<Paper>/` and `second/<Paper>/`: original prompts, source units, raw responses and metadata.
- `review-packets/<Paper>/`: both outputs with matching source/prompt checksums and review instructions.
- `final/<Paper>/`: reconciled inventory, decision trail, readable extraction and completeness ledger.
- `inspection/` and `claude-inspection/`: local page images used for table/figure checks.

Supplements downloaded before the scope clarification are separate unused archival files. They were not in either model prompt and must not contribute to the final main-paper extraction. Supplement-dependent details remain outside scope, not inferred.

The final versions are reconciled research extractions. Neither paper has been promoted into canonical findings; no clinical validation or general accuracy percentage is claimed. The review stage remains a separate, source-based activity rather than an unattended production model call. See [DUAL_EXTRACTION.md](DUAL_EXTRACTION.md) for the reusable workflow and evaluation requirements.

## Completed final-source audit

The reconciled main-paper versions contain 16 Osa analysis records and 33 Thye records. All 53 Osa and 187 Thye quoted passages (including reuse) pass the declared-source-unit checks. Codex checked the ten adjusted Thye associations against main Results and visually checked the main regional table, regression table and relevant figure values. This is scoped source verification, not a claim of 100% scientific accuracy. The final coverage ledgers explicitly retain unreported details and exclude supplements. Final file checksums and audit results are in `final-audit.json` in the experiment directory; the readable entry point is `RESULTS.md`.
