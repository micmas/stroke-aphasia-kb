// POST /api/reviews  — write one review record into the KB repository
//                      (logs/portal/inbox/<stamp>_<kind>_<reviewer>_<id>.json) through the GitHub API.
// GET  /api/reviews  — list the records in the inbox and in applied/ (names only), so the
//                      portal can show who already reviewed what.
//
// A record is data for scripts/portal_import.py, which applies it on the maintainer's machine:
// nothing here edits a draft, the register or a canonical entry directly.
import { listRecords, putRecord } from '../../lib/github.js';

const KINDS = new Set(['screen', 'verdict', 'edit', 'mark', 'comment']);

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
  const kind = String(body.kind || '');
  const id = String(body.id || '');
  if (!KINDS.has(kind)) return Response.json({ error: `kind must be one of ${[...KINDS].join(', ')}` }, { status: 400 });
  if (!id) return Response.json({ error: 'id is required (candidate id, or draft path for a draft review)' }, { status: 400 });
  if (JSON.stringify(body).length > 200_000) return Response.json({ error: 'record too large' }, { status: 413 });
  try {
    const { file, commit } = await putRecord(env, data.reviewer, kind, id, body);
    return Response.json({ ok: true, file, commit });
  } catch (e) {
    return Response.json({ error: e.message }, { status: e.status || 502 });
  }
}
