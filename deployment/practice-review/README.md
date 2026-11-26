# Practice and lived experience review workspace

Private title/abstract screening, full-text screening and paper-level evidence review
for the initial aphasia meaningful-outcomes collection. Uses the existing review
layout, with separate storage and a dedicated Cloudflare Access application.

## Build and verify

From the repository root:

```sh
python3 scripts/build_practice.py --exports '/path/to/aphasia-meaningful-outcomes'
python3 scripts/build_stroke_staging.py --public --reuse-exports
python3 -m unittest discover -s scripts -p test_build_practice.py
node --test deployment/practice-review/worker.test.js
```

The import manifest is tracked. Licensed records/abstracts stay in ignored
`staging/practice/dist/`; private site assets are built into ignored
`deployment/practice-review/dist/`. The public build contains aggregate counts and
prepared queries only. Preserve the original export directory and correction audit.

## Production setup

The dedicated resources are configured in `wrangler.toml`. The Access application
(c1d8bc3a-6d20-42db-ad5a-f189386705c5) permits only the existing maintainer email.
The Worker refuses every request if `ACCESS_AUD` is empty.

The following describes provisioning/recovery; do not recreate existing resources.

1. Create a Cloudflare Access self-hosted application for `review.stroke-kb.app`,
   using the same authorised reviewer policy as the existing Stroke KB review
   applications. Do not create an allow-everyone or bypass policy. Put its distinct
   audience in `ACCESS_AUD` in `wrangler.toml`.
2. Create a private R2 bucket `stroke-kb-practice-private`, with no public URL.
3. Create a D1 database `stroke-kb-practice-screening`. Add its ID and the R2 binding
   to `wrangler.toml` as `SCREENING` and `PRIVATE`, respectively.
4. Apply `schema.sql` to that database. Upload the private import's `records.json`,
   all chunks named in it, and `record-ids.json` to R2 under `screening/`. Do not
   upload these records to Workers assets or the public website.
5. Add a custom-domain route for `review.stroke-kb.app`, then deploy this Worker.
   Keep `workers_dev = false`, `preview_urls = false` and `run_worker_first = true`.
6. Verify unauthenticated requests cannot fetch the index, API or record chunks;
   verify a signed-in reviewer can save/reload a decision before publishing the
   public practice navigation.

Example dedicated bindings (replace the database ID):

```toml
[[r2_buckets]]
binding = "PRIVATE"
bucket_name = "stroke-kb-practice-private"
[[d1_databases]]
binding = "SCREENING"
database_name = "stroke-kb-practice-screening"
database_id = "YOUR_NEW_DATABASE_ID"
[[routes]]
pattern = "review.stroke-kb.app"
custom_domain = true
```

The private assets deploy through `practice-review.yml`; records are uploaded
separately to private R2. The public site uses the existing `stroke-public.yml` workflow once this branch is
integrated; the practice manifest is already included in the public builder.

## Review behaviour

Decisions are attributed by verified identity, saved independently per reviewer,
and logged as append-only events. Revision checks reject conflicting saves. Later
stages require earlier inclusion; upstream changes preserve downstream notes but
hide them from eligible queues. Browser backups retain unsaved notes and CSV
exports label unsaved values. Counts include pending browser decisions and are
personal progress, not adjudicated PRISMA totals.

Full-text reading uses the source/publisher link and library access. This workspace
does not automatically acquire PDFs. Evidence notes require a supporting passage,
locator, perspective, limitations and appraisal. Marking reviewed does not publish
a KB claim. The public findings/papers/theme views remain explicitly empty until
source-checked findings are separately approved and published.
