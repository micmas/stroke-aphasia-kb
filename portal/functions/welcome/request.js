// POST /welcome/request   {name, email, affiliation, note}
//
// The one public endpoint of the portal: the "I'd like to become a reviewer" form on the
// welcome page (web/welcome/index.html). /welcome is open by Access policy, so the
// middleware does not ask for a token here and nothing below trusts the caller: the body is
// size-limited, trimmed and checked, kept privately (lib/requests.js) and the maintainer is
// told. It gives nothing back but "received": the page cannot be used to find out who has
// already asked, and nothing private is reachable from it.
import { notify, storeRequest, validate } from '../../lib/requests.js';

const MAX_BODY = 8 * 1024;
const json = (obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });

export async function onRequestPost({ request, env }) {
  if (!env.UPLOADS) return json({ error: 'Requests cannot be taken right now. Please write to the maintainer instead.' }, 503);
  if (!/^application\/json\b/i.test(request.headers.get('Content-Type') || '')) return json({ error: 'expected JSON' }, 415);
  const text = await request.text();
  if (text.length > MAX_BODY) return json({ error: 'That is too long. Please shorten the note.' }, 413);
  let body;
  try { body = JSON.parse(text); } catch { return json({ error: 'expected JSON' }, 400); }
  // A field people never see: programs that fill in every box give themselves away.
  if (String(body?.website || '').trim()) return json({ ok: true });
  const checked = validate(body);
  if (!checked.ok) return json({ error: checked.error }, 400);
  const kept = await storeRequest(env, checked.request);
  if (!kept.stored) return json({ error: 'Many requests are waiting already. Please try again in a few days.' }, 429);
  if (kept.isNew) await notify(env, kept.record, new URL(request.url).origin);
  return json({ ok: true });
}

// any other method (Pages calls onRequestPost for POST, this for the rest)
export const onRequest = () => json({ error: 'POST only' }, 405);
