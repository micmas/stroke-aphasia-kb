# Collect and sync open-access PDFs

There are two terminal commands. Neither uses AI/model tokens or starts extraction.

| Command, from the repository root | What it does |
| --- | --- |
| `./collect-pdfs.command` | Finds licensed PDFs for all non-excluded candidates and stores them in Cloudflare. Runs Aphasia, Dysphagia and Practice/lived experience concurrently. |
| `./sync-pdfs.command` | Downloads only saved, kept papers into named local incoming folders. Preserves existing working PDFs. |

On the maintainer's current Mac, the shortcuts are:

```sh
/Users/uqmmasso/GITHUB/run-stroke-kb-pdfs.command
/Users/uqmmasso/GITHUB/sync-stroke-kb-pdfs.command
```

These shortcuts forward to the versioned launchers above. For another checkout,
use the repository commands rather than copying machine-specific paths.

## First-time setup

Use the project Python environment described in [README](../README.md). It needs
PyYAML and PyMuPDF. Install the portal dependencies and sign in to Cloudflare once:

```sh
(cd portal && npm ci)
portal/node_modules/.bin/wrangler login
```

The launchers find `.venv` and Wrangler in this checkout or its primary checkout.
They use the existing Wrangler sign-in and refresh it when needed. Credentials are
never printed or committed. `deployment/open-access.json` contains the non-secret
project account ID. An authorised environment can instead set
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Optional overrides are
`STROKE_KB_PYTHON`, `STROKE_KB_WRANGLER` and `STROKE_KB_WORKING_REPO`.

## 1. Collect into Cloudflare

```sh
./collect-pdfs.command
```

One independent process runs per collection, capped at three processes. Each has
its own progress counter and checkpoint; slow downloads in one collection do not
hold up the others. Wrangler credential refresh is serialized between processes.
The local launcher allows up to 50,000 attempts per collection within a 24-hour
budget. Only records due for a lookup are attempted. For a shorter run:

```sh
./collect-pdfs.command --minutes 60 --max-records 500
```

Use `--chapter aphasia`, `--chapter dysphagia` or `--chapter practice` for one
collection. Keep the computer awake and terminal open. Ctrl+C stops the run and
flushes completed checkpoints. Run the same command again to resume. If an older
sequential collector is running, stop it before starting the parallel version.
Never run two collectors for the same collection at the same time.

Example progress:

```text
Running aphasia, dysphagia, practice together, one process per collection.
[aphasia 13/20718] C0118 — available | 23 PDFs stored | 20705 checks left
```

| Status | Meaning |
| --- | --- |
| `available` | A licensed, identifier-matched, readable PDF was stored. |
| `not_found` | No explicitly licensed downloadable copy was found in the sources checked. The paper may still be accessible through a library or publisher. |
| `retry` | A temporary lookup/download failure occurred. |
| `excluded` | The collected copy is removed or withheld because of screening. |

The collector uses NLM PMC's current cloud dataset and Unpaywall DOI lookup.
When identifiers are missing, Europe PMC can supply them only for a single exact
match on title, publication year and first author. Original reference records are
unchanged. Explicit Creative Commons licences, identifiers, PDF format, readability,
size and checksum are checked. Manuscripts and published copies are labelled
separately. Subscription credentials and paywall bypasses are not used.

Temporary failures retry after a day; unsuccessful licensed-copy searches retry
after 30 days. Saving an include requests a prioritised new attempt. Collection
is not an eligibility assessment, extraction approval or published finding.

References: [PMC Cloud Service](https://pmc.ncbi.nlm.nih.gov/tools/cloud/),
[PMC dataset documentation](https://pmc-oa-opendata.s3.amazonaws.com/README.txt),
[Unpaywall API](https://data.unpaywall.org/products/api).

## 2. Sync kept papers locally

Save the inclusion in the review website first, then run:

```sh
./sync-pdfs.command
```

Only saved title/abstract or full-text includes qualify, with no current screening
exclusion. Unsaved browser choices and Practice evidence-note verdicts do not count.
You can sync while collection continues, and rerun as you keep more papers.

The destination defaults to the working repository's resolved `papers/` directory:

```text
papers/_incoming/open-access/
  aphasia/
  dysphagia/
  practice/
```

On the maintainer's Mac, `papers/` points to:

```text
/Users/uqmmasso/Library/CloudStorage/OneDrive-TheUniversityofQueensland/Documents/calmar-papers
```

Registered papers use `RecordID_CitationKey.pdf`, such as
`C0010_Fridriksson2018BDNF.pdf`. Other papers use `RecordID_AuthorYear.pdf`, such as
`PLE-09d2311a55cab8b6_Brady2025.pdf`. The record ID prevents name collisions; an
author/year filename does not itself register a citation key.

Each new PDF has a `.source.json` sidecar with its DOI, title, source, licence,
version and checksum. Each collection also has `.open-access-sync.json`, recording
local paths, sync outcomes and current eligibility. Preview without downloading:

```sh
./sync-pdfs.command --dry-run
./sync-pdfs.command --chapter practice --dry-run
```

Sync verifies downloaded checksums and rechecks screening before writing. Identical
incoming copies are skipped. For Aphasia, matching working files and retained
`_originals` are reused without alteration. Different working versions and modified
incoming files are preserved and reported; nothing replaces an active source PDF.
Previously downloaded local files are not automatically deleted when screening
changes. The manifest updates their eligibility; Cloudflare removal is separate.

`--destination /path/to/incoming` overrides the incoming root. `--limit 5` limits a
preview/test to five selected records per collection. Only one local sync can write
a given incoming root at a time.

## 3. Prepare and extract separately

For Aphasia, complete full-text eligibility and register the included paper before
extraction. The existing registration command is:

```sh
.venv/bin/python scripts/screen.py register --execute
```

Then the existing guarded intake can import matching registered sources that have
no working PDF, preserve originals, remove cover pages and OCR as needed:

```sh
.venv/bin/python kb.py intake --from papers/_incoming/open-access/aphasia --execute --wait
```

`--wait` waits for active KB processing to finish. Intake does not replace an
existing working version. Create a fresh `kb.py prepare` manifest for the selected
citation keys afterward; model extraction remains an explicit separate action.
Follow [Prepare, extract and review papers](HOWTO.md) for the full workflow.

Dysphagia and Practice sources stay in their own incoming folders. They are not
added to the Aphasia bibliography or fed into its extraction assumptions.
Chapter-specific registration and extraction adaptation remain separate work.

The existing `kb.py sync` handles PDFs uploaded by reviewers. Use
`sync-pdfs.command` for the automatically collected open-access copies.

## Shared papers, exclusions and storage

| Collection | Private Cloudflare bucket |
| --- | --- |
| Aphasia | `stroke-aphasia-kb-pdfs` |
| Dysphagia | `dysphagia-kb-private` |
| Practice and lived experience | `stroke-kb-practice-private` |

Cloudflare keys remain stable: `open-access/pdf/<RecordID>.pdf`. Status, source URL,
licence, version, date, page count, size and checksum are retained under
`open-access/status/`, `history/`, `index.json` and `summary.json`. Paper licences
remain their own licences; the project's non-commercial licence does not replace
them. NLM PMC copies are credited and labelled as downloaded snapshots.

The same publication can have a record and PDF copy in several collections.
Copies are currently retrieved and stored independently, without merging screening
decisions across collections. Excluding a paper from one collection removes only
that collection's automatically collected copy. Working PDFs, annotations, uploads,
local extraction inputs and source/audit history are preserved.

Saving a screening exclusion first writes an atomic per-reviewer/stage marker,
which blocks serving and re-uploading during an in-flight retrieval. Another
reviewer's include cannot override that reviewer's exclusion. Changing an exclusion
to include clears that reviewer's marker and requests collection again. Rejecting
a Practice evidence note is not a paper exclusion and leaves its PDF available.

Dysphagia and Practice reconcile durable decision events every 15 minutes to repair
interrupted storage updates; the initial reconciliation must finish before their
first collection. Their PDF routes also check saved exclusions. Aphasia collection
additionally reconciles its register and pending receipts. A storage failure does
not undo a saved decision; removal is retried. Review pages show an **Open collected
PDF** link when a copy is available, with source/licence/version details.

## GitHub workflow and troubleshooting

The `open-access-papers` workflow is **manual only** while local collection is in
use. In Actions → open-access-papers → Run workflow, select a collection or `all`.
It uses the existing Cloudflare secrets, with up to 500 records per collection and
a 45-minute budget by default. It does not use AI. Do not run it for a collection
already being processed in your terminal. GitHub jobs share a concurrency group.

- **Cloudflare sign-in unavailable:** run Wrangler login, then resume the command.
- **No local files synced:** save an include first; a licensed collected PDF must
  also exist. Unsure/excluded/unsaved choices do not qualify.
- **`not_found`:** this is a retrieval result, not a screening exclusion or proof
  that the paper cannot be accessed through a library.
- **`local_copy_changed`:** the local file was preserved. Compare versions before
  replacing anything; sync never overwrites it.
- **Collection progress:** inspect each bucket's `open-access/summary.json`.
- **Local sync progress:** inspect the incoming collection's `.open-access-sync.json`.
