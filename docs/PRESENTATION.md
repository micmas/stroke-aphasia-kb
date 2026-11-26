# Shared chapter presentation

Aphasia is the presentation baseline. Chapters supply content and evidence; they
do not maintain independent copies of the layout. A change to a shared source is
built into every chapter. Never edit generated `dist` files as source code.

| Change | Shared source |
| --- | --- |
| Main page shell, header, footer | `explorer/index.html` |
| Typography, spacing, tiles, tables, diagrams | `explorer/styles.css` |
| Project navigation and colour themes | `explorer/project-shell.js` and `.css` |
| Chapter bar | `staging/stroke/web/chapter-bar.js` |
| Page headings, cards, summary tiles, coverage section order | `explorer/chapter-presentation.js` |
| PRISMA geometry and interactions | `prismaDiagram` in `explorer/app.js` |
| Chapter routes and public build | `scripts/build_stroke_staging.py` |

`coveragePage` is the single coverage layout for Aphasia, Dysphagia and Practice.
Aphasia supplies its live evidence register, filters and candidate table.
`staging/stroke/web/chapter-coverage.js` adapts import manifests for chapters that
have not yet published screening results. Dysphagia and Practice pass their database
labels, counts, links and explanatory text. These adapters do not define the order
of headings, tiles, diagram, exclusion/reviewer sections, searches or candidates.

The build copies shared files into chapter URLs because the public site is static.
Those deployment copies are generated outputs, not independently editable sources.
The standalone Aphasia explorer uses the same components directly.

## Chapter-specific content and sections that need discussion

Keep the same presentation and navigation when data differ. Never imply that an
unreported screening total is zero, or display Aphasia evidence in another chapter.

Practice's themes/outcomes do not map directly to the anatomical relationships in
Aphasia's Matrix. Its evidence-gap categories also differ: meaningful outcomes,
lived experience, goals/communication and experiences of care. Retain shared
components and flag the content-model difference to the researcher rather than
creating an alternate visual layout. Extraction-method sections must describe the
actual validated process for that chapter, not inherit Aphasia performance claims.

New components should be added to the shared presentation layer first. Chapters
may choose content or supply a clearly documented specialised body; they should
not copy and modify a common component. Preserve existing interactions when moving
markup into shared components, and check the resulting pages in the browser.

After a complete public build, `python3 scripts/build_stroke_staging.py --public
--presentation-only` updates shared UI assets without regenerating or replacing
clinical evidence exports. A normal public build still refreshes both data and UI.
