# Browsing categories

The explorer separates **Brain regions and pathways** (locations) from
**Clinical and imaging factors** (characteristics and measurements).

Anatomy subdivisions are grey-matter regions, white-matter regions and pathways,
and mixed or distributed regions. Unclassified anatomy is explicitly marked
“Anatomical definition to check”; missing definitions never imply mixed tissue.
Factors are subdivided into personal characteristics, clinical characteristics,
and lesion and imaging measures. A pathway and a measurement of that pathway
are different concepts.

The browsing rules live in `explorer/topic-categories.js`. They operate on copies
of exported records; they do not change source records, extraction instructions,
atlas mappings, scoring, review status or concept IDs. Original source and target
kinds remain available in the index. Existing links and study-specific definitions
are retained. Lesion size and volume are not merged without measurement review.
Study-defined clusters remain intact and are not split into invented effects.

Keep these presentation changes separate from the active source-check batch.
Expand anatomical classifications only with adequate source definitions.
