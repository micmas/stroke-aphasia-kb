# Agent workspace

Keep temporary Markdown decision, review and revision reports outside all GitHub
checkouts. For this project use `~/Documents/agent-work/stroke-aphasia-kb/`, with
one dated task directory. Do not create `_coordination/`, report archives or agent
journals inside the repository. Keep current product documentation and essential
source/approval audit records in the repository.

Do not change extraction code, prompts, settings or source PDFs used by an active
run. Preserve unrelated user edits. Use the current README and docs/HOWTO.md for
the product workflow; local source inventories do not approve KB findings.

Do not reintroduce retired drafts or promote model outputs to fill an empty queue.
Check logs/baseline/2026-11-12.json for review obligations before replacing findings.
Put new disposable diagnostics and development reports outside the checkout.

Git commits for this repository use micmas <michelemt8@gmail.com>. Do not add AI
authors or Co-authored-by trailers. Preserve actual model/reviewer provenance in
evidence and audit records; commit ownership does not imply human verification.

Public websites share the CALMaR palette and project navigation in
`explorer/project-shell.css` and `explorer/project-shell.js`. Keep a visible link
back to https://aphasia-kb.app/ and to the CALMaR webapp on every HTML page.
Use plain language, foreground human research responsibility, and keep source
and review provenance available. Theme changes must be checked in light and dark
mode and deployed to the explorer, portal and CALMaR notebook/demo site together.

## Preserve the public layout

The researcher has started showing the KB to other people. Preserve the established
layout across Stroke KB, Aphasia KB, Dysphagia KB and their review pages unless the
user explicitly requests a layout change. Keep navigation placement, page structure,
section order, spacing, typography and the overall visual design consistent.
Routine content updates, data refreshes and bug fixes must fit the existing layout;
do not bundle redesigns or unsolicited visual cleanup with them. A request to fix a
specific visual detail authorizes that detail only, not a broader layout change.

## Shared chapter presentation

Equivalent components across chapters must reuse the established presentation,
including headings, section order, summary tiles, tables, diagrams and navigation.
Pass chapter-specific data and wording into shared renderers instead of creating
a parallel layout. Use Aphasia as the default presentation. Shared components belong in
`explorer/chapter-presentation.js`; coverage content adapters supply data to its
`coveragePage` rather than owning page structure. See `docs/PRESENTATION.md`.
Flag sections that do not fit a chapter before inventing a different layout.
Unknown review totals remain blank, not zero.
