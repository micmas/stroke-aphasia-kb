# Stroke KB migration and compatibility contract

The target is one `stroke-kb` repository with Aphasia and Dysphagia as sibling
chapters. The current repository and deployments keep their existing names until
the dependent changes are ready. The first implementation is on the isolated
`feat/stroke-kb-chapters` branch; active extraction runs use their original checkout.

## Public addresses

- `stroke-kb.app`: shared project homepage linking to both chapters.
- `aphasia-kb.app`: permanent Aphasia chapter; retain current paths, queries,
  fragment routes, entry IDs and finding IDs. Do not send old links to the hub.
- `dysphagia-kb.app`: permanent Dysphagia chapter.
- `review.aphasia-kb.app` and `calmar.aphasia-kb.app`: retain during migration.
  Any new shared addresses must coexist with or preserve these old entry points.

## Compatibility boundary

Legacy evidence without chapter labels means Aphasia. `KnowledgeBase` defaults
to `chapter="aphasia"`; `chapter="dysphagia"` and `chapter="all"` are explicit
research-loading options. These options do not validate aphasia-specific clinical
interpretation rules for dysphagia. Existing browser exports remain Aphasia-only
and keep `stroke-aphasia-kb.json` and `stroke-aphasia-kb-drafts.json` filenames.
The additive chapter fields do not alter existing identifiers or review metadata.

Screening membership and eligibility are different. The new read adapter isolates
chapter decisions; existing CLI/portal writes and PRISMA calculations are still
Aphasia-only. Dysphagia writes must wait for a complete chapter-aware workflow,
including independently derived counts and duplicate/source provenance.

## Deployment dependencies to update before repository rename

- `.github/workflows/pages.yml`: existing GitHub Pages build and aphasia CNAME.
- `portal/wrangler.toml`: repository identity; keep existing R2 bucket names/data.
- Portal GitHub authorization, workflow dispatch, secrets and repository permissions.
- CALMaR `.gitmodules`, local KB discovery and notebook references.
- Neurodesk CALMaR sync workflow/script and export consumers.
- Repository URLs in documentation and public navigation.
- Domain DNS, hosting bindings and HTTPS certificates for each new site.
- Authentication/cookie origins if introducing a shared portal address. Browser
  preferences cannot be shared by a domain cookie across the three unrelated domains.

Do not globally replace every aphasia string: many refer to valid chapter names,
legacy public contracts, clinical rules or historical provenance.

## Release sequence and verification

1. Validate chapter loading with legacy, dysphagia-only and mixed findings.
2. Complete chapter-specific screening writes, filters and coverage tests.
3. Build hub and dysphagia pages with the existing CALMaR design; test responsive,
   light and dark layouts. Keep an honest empty state until evidence is approved.
4. Deploy new domain bindings alongside the existing Aphasia site, then verify HTTPS.
5. Rename the GitHub repository and update dependent deployment/integration
   references together. Keep the local active-run path intact.
6. Verify the existing root, `/explorer/` redirect, query options, paper/entry/finding
   hash links, PDFs, review authentication and CALMaR reports. Retain a known-good
   deployment and export snapshot for rollback.

The repository rename, public deployment and DNS changes are not performed by
this foundation change. No prior evidence is recertified or moved into a new queue.
