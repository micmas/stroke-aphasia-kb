# Evidence fidelity in local extraction

The extractor supplies canonical target definitions and assessments, not just IDs, and a final evidence checklist after the paper text. The checklist requires model-specific adjustment context, exact outcomes and time points, source discrepancies, reference identity, and cautious confidence. It contains no answers specific to the papers used to develop it. The configured local model and its weights are unchanged.

For every newly saved finding, the extractor records the actual model identity and extraction date. It does not rewrite dates in existing drafts. When extracting from a PDF, it checks each quotation against the **declared one-based PDF page**, using the shared quote normalizer. Anything other than an exact single-page match receives a `verify evidence` provenance flag. A quotation found on another page is reported but not relocated automatically. Existing low confidence stays low; otherwise an evidence issue caps confidence at medium. Flags make the draft require human review under the existing policy.

A failed text match can result from PDF layout, glyphs or edited quotation formatting; it is not proof of fabrication. A successful match establishes neither semantic support nor correct statistical interpretation. No claim, coefficient, citation, effect direction or quote is automatically corrected by the evidence checker, and nothing is approved by it.

## Evaluate a saved run

Keep baseline and candidate outputs in different directories and retain raw responses. Use the same local model/settings and PDFs. The read-only report separates whole-paper quote matches from page-location issues:

```sh
python scripts/evaluate_extraction_accuracy.py \
  --draft-dir /path/to/run/drafts \
  --pdf /path/to/Paper.pdf \
  --output /path/to/run/evidence-report.json
```

Use a directory containing drafts from that paper only. An empty run exits unsuccessfully. Schema and quote scores are diagnostics, not scientific accuracy scores. Independently assess claim fidelity and coverage against the original PDF, including tables, figure captions and limitations; a shorter extraction that simply omits difficult results is not automatically better.

Predeclare evaluation criteria, freeze the prompts, include held-out papers, and retain failures. Report source inconsistencies separately from extraction errors. Identify the raw-model contribution separately from deterministic date stamping and review flags. Repeated runs and broader human-curated references are needed before claiming general accuracy gains or changing the default model.

## Experimental second pass

`python scripts/verify_extraction.py --input /path/to/raw.json --pdf /path/to/Paper.pdf --citation @Paper2020 --output-dir /path/to/new-run`

This optional command asks the same local model to check the complete paper against its draft, with focused instructions about statistical models, contradictory results, quotations, definitions and references. It retains the original response and writes the verification prompt, response, hash, change notes and new drafts in a new directory. Validation errors produce an unsuccessful exit; no result is approved or promoted. This is model self-checking, not independent review, and is not enabled in the default extraction path.

Postprocessing accepts missing/null provenance and flags as empty containers, but rejects other incorrect types. Malformed canonical metadata is ignored. The evaluation report records malformed YAML as an error rather than abandoning the entire report. These robustness fixes do not change the frozen model prompts.
