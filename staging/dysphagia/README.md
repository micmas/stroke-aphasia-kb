# Dysphagia screening staging

Isolated title/abstract screening for the 23 November 2026 exports. This does not
write to the Aphasia screening register or the production review inbox.

Build from the unchanged OneDrive exports:

```sh
python scripts/build_dysphagia_staging.py --exports /path/to/search-exports/dysphagia/2026-11-23
```

The import manifest tracks hashes, source counts, deduplication rules and unresolved
export discrepancies. Original exports and abstract bundles are not committed.
The generated `dist/` includes every imported record and source locator; no record
is excluded automatically. An include decision retains a paper for full-text review.
Exact queries/limits are not reconstructed as if verified from the filenames.

Deploy only a preview, from this directory, using the existing review Pages project:

```sh
wrangler pages deploy dist --project-name stroke-aphasia-kb-review --branch dysphagia-staging
```

Do not deploy this build with `--branch main`. All assets require the existing
Cloudflare Access identity. The separate D1 database `dysphagia-screening-staging`
stores reviewer state and append-only save events. Initialize with `wrangler d1
execute dysphagia-screening-staging --remote --file schema.sql`. No GitHub write
credential is needed. No production apply/upload endpoints are shipped in this
preview and no R2 objects are overwritten.

The decision API refuses a configured branch other than
`feat/dysphagia-screening-staging`. Every save uses a D1 transaction and revision
check to reject stale writes. Unsaved choices are backed up in the browser per
reviewer; the interface distinguishes saved from unsaved decisions. CSV download
is available. A future chapter-aware integration must explicitly import these
decisions; screening does not automatically approve findings or run extraction.
