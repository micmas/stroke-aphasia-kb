# Maintaining the knowledge base

The user interface is root `kb.py`; [HOWTO](../HOWTO.md) is the authoritative user
workflow. Keep implementation modules under `scripts/` so existing imports,
automation and in-progress runs remain compatible. Avoid presenting their older
extraction paths as competing user choices.

## Implementation map

| Responsibility | Modules |
|---|---|
| Source manifest | `prepare_dual_batch.py` |
| Independent extraction | `batch_dual_extract.py`, `dual_extract.py`, `extract_analysis_inventory.py`, `source_inventory_segments.py` |
| Source reconciliation | `review_dual_extract.py` |
| KB validation and queries | `aphasia_kb.py` |
| Existing draft review and approval | `review_app.py`, `auto_review.py`, `promote.py` |
| Source intake and screening | `intake_papers.py`, `screen.py` |
| Publication and portal records | `publish_portal.py`, portal-related modules |

The single-model `extract.py` and focused extraction tools remain dependencies and
compatibility tools. Do not remove or rename them during a running batch. Retiring
an implementation requires checking imports, CI, portal actions and downstream
callers, not just removing its user documentation. `docs/EXTRACTION_SKILL.md` is
also consumed by compatibility code and must not be moved casually.

## Validation

From the repository root:

```bash
.venv/bin/python -m pytest -q
npm test
.venv/bin/python kb.py status
```

Use focused tests for the changed behavior first. Validate modified KB data with
`kb.py validate --check PATH`. The user CLI only dispatches; it must preserve child
arguments, exit status and interrupts and must not duplicate inference logic.

## Approval and publication

Source inventories are not KB drafts. Review the source, resolve visual checks,
map to the schema, and then use the existing draft approval tools under
[governance](../GOVERNANCE.md). Maintainers can inspect `scripts/promote.py --help`
for approval and rejection operations; never approve as a side effect of a batch.
For portal synchronization and publication follow [PORTAL](../PORTAL.md); for
export and website maintenance follow [EXPLORER](../EXPLORER.md). Preserve private
PDF access boundaries and do not commit source PDFs or local `_compare/` runs.

### Complete a passage-only edit after approval

If a portal edit only adds source passages and its original draft has already
been promoted, an explicitly authorized maintainer correction can use
`promote.py --resolve-passage-edit RECORD --canonical ENTRY --source-pdf PDF
--actor agent:NAME` (or `human:NAME`). The default is a preview; add `--execute`
after inspecting the cited PDF page. This operation requires one unambiguous
approved finding for that paper and entry, verifies each quotation on its stated
page, and refuses edits to claim fields. It preserves the original approval and
finding ID, records the actual correction operator and source hash, and archives
the original portal record with its resolution. Recoverable promotion journals
prevent duplicate evidence after interruption. This is not a route to approve new
findings or make substantive changes to approved claims.

CALMaR pins this repository as a submodule. Updating the KB does not automatically
update that consumer; bump its pointer only after the intended KB revision is
available on its integration branch.

## Evaluation and migration

Use the comparison criteria in [Models](../MODELS.md). Apply the selected method to
all registered KB source papers, including already published findings. Track
preparation, extraction, reconciliation, visual verification, mapping and approval
separately. A complete extraction count is not a complete migration. Replacements
must preserve source attribution and pass approval before superseding existing
findings; retain the audit history without creating a permanent second-class tier.

## Agent working reports

Keep agent decision logs, review reports, revision notes and experiment narratives
outside the repository. Use `~/Documents/agent-work/stroke-aphasia-kb/` locally,
with a dated subfolder for each task. Current user documentation belongs here;
source provenance, approval records and tests remain versioned with the product.
Superseded committed documents remain recoverable through Git history.
