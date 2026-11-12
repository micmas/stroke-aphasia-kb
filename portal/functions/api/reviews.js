// POST /api/reviews  — write review records into the KB repository
//                      (logs/portal/inbox/<stamp>_<kind>_<reviewer>_<id>.json) through the GitHub API.
//                      One record as {kind, id, …}, or several as {records: [{kind, id, …}, …]}:
//                      a batch is one commit, so a "Send" is one push however many decisions it holds.
// GET  /api/reviews  — list the records in the inbox and in applied/ (names only), so the
//                      portal can show who already reviewed what.
//
// A record is data for scripts/portal_import.py, which applies it on the maintainer's machine:
// nothing here edits a draft, the register or a canonical entry directly.
import { listRecords, putRecords } from '../../lib/github.js';

const KINDS = new Set(['screen', 'verdict', 'edit', 'mark', 'comment']);
const MAX_BATCH = 200;
const DIGEST = /^sha256:[0-9a-f]{64}$/;

/** A record as the client sent it → {kind, id, body}, or a string saying what is wrong with it. */
function check(body) {
  const kind = String(body?.kind || '');
  const id = String(body?.id || '');
  if (!KINDS.has(kind)) return `kind must be one of ${[...KINDS].join(', ')}`;
  if (!id) return 'id is required (candidate id, or draft path for a draft review)';
  if (JSON.stringify(body).length > 200_000) return 'record too large';
  if (kind === 'verdict') {
    // bound to the draft as the reviewer saw it (portal/dist/drafts.json); portal_import.py
    // recomputes the digest and records a verdict on a changed draft as an opinion only
    if (!DIGEST.test(String(body.draft_digest || ''))) return 'a verdict must carry draft_digest (reload the portal: the page is older than the review binding)';
    const ids = body.finding_ids;
    if (!Array.isArray(ids) || ids.length > 500 || !ids.every((x) => typeof x === 'string' && x.length <= 40)) return 'a verdict must carry finding_ids, the ids of the findings reviewed';
  }
  return { kind, id, body };
}

export async function onRequestGet({ env }) {
  try {
    return Response.json(await listRecords(env));
  } catch (e) {
    return Response.json({ error: e.message }, { status: e.status || 502 });
  }
}

export async function onRequestPost({ request, env, data }) {
  let body;
  try { body = await request.json(); } catch { return Response.json({ error: 'JSON body expected' }, { status: 400 }); }
  const batch = Array.isArray(body?.records) ? body.records : [body];
  if (!batch.length) return Response.json({ error: 'no records' }, { status: 400 });
  if (batch.length > MAX_BATCH) return Response.json({ error: `at most ${MAX_BATCH} records per send` }, { status: 413 });
  const checked = batch.map(check);
  const bad = checked.find((c) => typeof c === 'string');
  if (bad) return Response.json({ error: bad }, { status: bad === 'record too large' ? 413 : 400 });
  try {
    const { files, commit } = await putRecords(env, data.reviewer, checked);
    return Response.json({ ok: true, file: files[0], files, commit });
  } catch (e) {
    return Response.json({ error: e.message }, { status: e.status || 502 });
  }
}
