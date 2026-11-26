# Automatic open-access collection

Stroke KB collects licensed main-article PDFs for all imported Aphasia,
Dysphagia and Practice/lived experience candidates, except excluded and duplicate records. Collection is not
a screening decision, full-text eligibility assessment or extraction approval.

The `open-access-papers` GitHub workflow resumes from its R2 index. Automatic
hourly runs are currently disabled while the maintainer runs the collector in a
local terminal. Do not run a GitHub collection and a local collection at the same
time. Each
run attempts up to 500 records per chapter within a 45-minute budget. The three
collections run independently, so a slow provider in one does not delay the other.
Large initial collections therefore finish over multiple runs. Saved includes
prioritise another attempt. Temporary failures retry after a day; papers without
a licensed downloadable copy are checked again after 30 days. Manual GitHub runs use the same concurrency group and checkpoints.

The collector uses the current NLM PMC Cloud Service and Unpaywall DOI lookup.
For records missing identifiers, Europe PMC may supply them only when a single
result matches the title, publication year and first author; ambiguous matches
are left for review and the original imported record is unchanged.
It verifies identifiers, an explicit Creative Commons licence, PDF format,
readability, size and checksum. Accepted manuscripts are labelled separately
from published versions. Missing identifiers, missing licence details, blocked
downloads and papers without a downloadable PDF remain unresolved; they are not
excluded. Subscription access, browser sessions and paywall bypasses are not used.

References: [PMC Cloud Service](https://pmc.ncbi.nlm.nih.gov/tools/cloud/),
[PMC dataset technical documentation](https://pmc-oa-opendata.s3.amazonaws.com/README.txt),
[Unpaywall API](https://data.unpaywall.org/products/api).
NLM PMC is credited as the source of its copies. Stored PDFs are downloaded
snapshots and may not reflect subsequent publisher or NLM updates.

## Storage and screening

The collection uses `open-access/` in the existing separate private buckets:

| Chapter | Bucket |
| --- | --- |
| Aphasia | `stroke-aphasia-kb-pdfs` |
| Dysphagia | `dysphagia-kb-private` |
| Practice and lived experience | `stroke-kb-practice-private` |

`pdf/<record-id>.pdf` holds bytes; `status/`, `history/`, `index.json` and
`summary.json` preserve retrieval status, dates, source URL, licence, version,
page count, byte size and checksum. Paper licences remain their own licences;
the project's non-commercial licence does not replace them. Copies are available
only in the signed-in review sites, via `/api/open-access?id=...&file=1`.

Saving a title/abstract or full-text exclusion writes a removal marker before
deleting that record's collected PDF. The marker also prevents serving or
re-uploading a copy during an in-flight download. Another reviewer's include
cannot override that reviewer's exclusion. Changing the exclusion to include
clears that reviewer's marker and requests retrieval again. Full-text and
title/abstract markers are independent. Check-screening opinions do not change
collection. Retrieval history and screening audit remain after PDF removal.

This removal applies only to automatically collected copies. Working source PDFs,
annotated PDFs, user uploads and extraction inputs use other prefixes and are
never overwritten or removed by this collector.

Aphasia's collector also reconciles the canonical register and pending
screening receipts. Dysphagia and Practice follow their append-only D1 decision events in batches
of 100 changes every 15 minutes, repairing interrupted storage updates. Corrections
do not wait for a full rescan of previously screened papers. Each first complete
reconciliation must finish before initial collection starts. A storage failure
does not undo a saved screening decision; removal is retried. The signed-in
Dysphagia and Practice download routes also checks the saved D1 exclusions.

## Running and inspecting

Use GitHub Actions → **open-access-papers** → **Run workflow** to choose a chapter
and batch size. The workflow uses the existing Cloudflare publishing secrets;
no provider credentials or PDFs are committed to Git.

For an authorised local run, set `CLOUDFLARE_API_TOKEN` and
`CLOUDFLARE_ACCOUNT_ID` in the process environment, then run:

```sh
python scripts/collect_open_access.py --chapter all --max-records 500 --minutes 45
```

Inspect each bucket's `open-access/summary.json` for counts and the number of
records remaining in the current pass. Each review record shows the copy's
availability, provider, licence and manuscript/publication version. Full-text
review and extraction still require human assessment of the retrieved paper.

For a local run, `--wrangler /path/to/wrangler --account-id ACCOUNT_ID` uses and
refreshes an existing Wrangler sign-in without printing credentials. Each completed
record prints a batch counter, PDFs stored and checks remaining. Re-running resumes
from the stored index; keep the terminal and computer running during collection.

## Papers shared between collections

Each collection retains its own record, screening decisions and private PDF copy.
The collector currently retrieves and stores these copies independently; it does not
merge records across collections or use a shared PDF whose deletion could affect
another collection. An exclusion removes only that collection's automatically
collected copy. DOI matches can identify the same publication but do not imply that
it meets every collection's inclusion criteria. Rejecting a Practice evidence note
is not a paper exclusion and does not remove the PDF; title/abstract and full-text
exclusions do.

`--chapter all` runs Aphasia, Dysphagia and Practice concurrently, with one
independent process per collection (at most three processes). This keeps all
collections moving without waiting for a slow provider in another collection.
Each process has its own progress counter and checkpoint; the time limit applies
to the whole run. Wrangler sign-in refreshes are serialized between processes. Use
`--chapter practice` for just the new collection. A process already running when
this support was added retains its original behaviour. Stop with Ctrl+C and
restart to use parallel collection. Completed record checkpoints are flushed on
interruption. Never run two collectors for the same collection at once.

## Sync kept papers into local source folders

`scripts/sync_open_access.py` downloads only papers with a saved title/abstract or
full-text inclusion and no current exclusion. Unsaved browser choices and evidence
note verdicts do not qualify a paper. Run it repeatedly as screening progresses.
It does not run models, formatting, OCR, registration or publication, and it does
not overwrite working PDFs. The collector can continue running during this sync.

```sh
python scripts/sync_open_access.py --repo /path/to/stroke-kb \
  --wrangler /path/to/wrangler --account-id ACCOUNT_ID --execute
```

Without `--execute` (or with `--dry-run`) it previews the sync. `--chapter practice`
selects one collection. By default, it writes to the resolved `papers/` folder's
`_incoming/open-access/{aphasia,dysphagia,practice}/` subfolders. On the maintainer's
machine, `papers/` already points to the OneDrive `calmar-papers` directory.

Cloudflare filenames remain stable record IDs (`open-access/pdf/C1234.pdf`,
`DYS-….pdf`, `PLE-….pdf`). Incoming local copies use `RecordID_CitationKey.pdf` for
registered citations, otherwise `RecordID_AuthorYear.pdf`. The record ID prevents
filename collisions. A `.source.json` sidecar and `.open-access-sync.json` manifest
retain the DOI, title, citation key, original source, licence, version and checksum.
An author/year label is not a newly registered citation key.

Sync checks the actual downloaded bytes against the stored checksum, rechecks the
saved screening decision before writing, and resumes without downloading identical
local copies again. For Aphasia, matching working files and retained `_originals`
are reused without alteration. Different working versions are preserved; a new
source may be staged separately for comparison. Modified incoming copies are also
preserved and reported. Previously downloaded local files are not automatically
deleted when screening changes; the sync manifest updates their current eligibility.
Cloudflare removal remains separate and applies only to collected remote copies.

For Aphasia, finish full-text eligibility and register included papers before
extraction. The existing `kb.py screen register --execute` registers fully included
candidates. The guarded intake can then copy matching registered sources from the
incoming folder, preserve originals, remove cover pages and OCR as needed:

```sh
.venv/bin/python kb.py intake --from papers/_incoming/open-access/aphasia --execute --wait
```

`--from` only imports sources matching registered citations that have no working
PDF; it does not replace an existing version. Prepare a fresh extraction manifest
for the selected citation keys afterward, using `kb.py prepare`. Extraction remains
a separate explicit command. See `docs/HOWTO.md` for the established workflow.

Dysphagia and Practice incoming files remain in their own folders. Their records
are not added to the Aphasia bibliography or fed into its extraction assumptions;
chapter-specific registration and extraction adaptation are separate work. The
existing `kb.py sync` handles reviewer uploads, not these collected open-access
copies; use this new sync command for the latter.
