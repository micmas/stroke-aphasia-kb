// "I'd like to become a reviewer": the requests people send from the public welcome page.
//
// Where they are kept: the private R2 bucket bound as UPLOADS, one small JSON object per
// person under requests/ (named after a hash of the email, so a second request from the
// same address replaces the first instead of piling up). They are never written to the
// repository, which is public: a request holds a name and an email.
//
// How the maintainer hears about one, in this order:
//   1. email, when a mail Worker is bound as MAILER (portal/mailer/, Cloudflare Email
//      Routing): the request itself, sent to the maintainers' addresses;
//   2. otherwise GitHub: the workflow .github/workflows/portal-request.yml is started, which
//      opens (or comments on) an issue saying a request is waiting. No personal detail goes
//      to GitHub; the details are in the portal, on the maintainer's Home page.
// Either way the request waits in the portal's list until the maintainer removes it.
import { gh } from './github.js';

export const PREFIX = 'requests/';
export const WORKFLOW = 'portal-request.yml';
export const MAX_WAITING = 200;          // a public form: stop storing when this many wait
export const NOTIFY_EVERY_MS = 10 * 60 * 1000;   // GitHub route: at most one notification per 10 minutes
const MARKER = `${PREFIX}_notified`;
export const LIMITS = { name: 120, email: 200, affiliation: 200, note: 1500 };

const clean = (v, max) => String(v ?? '').replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '').trim().slice(0, max);

/** {ok, request} or {ok: false, error}: what a person typed, trimmed and checked. */
export function validate(body) {
  const request = {
    name: clean(body?.name, LIMITS.name).replace(/\s+/g, ' '),
    email: clean(body?.email, LIMITS.email).toLowerCase(),
    affiliation: clean(body?.affiliation, LIMITS.affiliation).replace(/\s+/g, ' '),
    note: clean(body?.note, LIMITS.note),
  };
  if (!request.name) return { ok: false, error: 'Please give your name.' };
  if (!/^[^\s@<>"',;]+@[^\s@<>"',;]+\.[a-z]{2,}$/i.test(request.email)) return { ok: false, error: 'That email address does not look right.' };
  return { ok: true, request };
}

export async function keyFor(email) {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(String(email).toLowerCase()));
  return `${PREFIX}${[...new Uint8Array(digest)].slice(0, 12).map((b) => b.toString(16).padStart(2, '0')).join('')}.json`;
}

export const idOf = (key) => key.slice(PREFIX.length, -'.json'.length);

/** Every request waiting, oldest first. */
export async function listRequests(env) {
  const out = [];
  let cursor;
  do {
    const page = await env.UPLOADS.list({ prefix: PREFIX, cursor });
    for (const obj of page.objects || []) {
      if (!obj.key.endsWith('.json')) continue;
      const got = await env.UPLOADS.get(obj.key);
      if (!got) continue;
      try { out.push({ id: idOf(obj.key), ...(await got.json()) }); } catch { /* not ours */ }
    }
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);
  return out.sort((a, b) => String(a.requested).localeCompare(String(b.requested)));
}

async function countWaiting(env) {
  let n = 0;
  let cursor;
  do {
    const page = await env.UPLOADS.list({ prefix: PREFIX, cursor });
    n += (page.objects || []).filter((o) => o.key.endsWith('.json')).length;
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);
  return n;
}

/** Keep the request. Returns {stored, isNew} or {stored: false, full: true}. */
export async function storeRequest(env, request, now = new Date()) {
  const key = await keyFor(request.email);
  const existing = await env.UPLOADS.head(key);
  if (!existing && (await countWaiting(env)) >= MAX_WAITING) return { stored: false, full: true };
  const record = { ...request, requested: now.toISOString() };
  await env.UPLOADS.put(key, JSON.stringify(record, null, 1), { httpMetadata: { contentType: 'application/json' } });
  return { stored: true, isNew: !existing, id: idOf(key), record };
}

export async function removeRequest(env, id) {
  if (!/^[0-9a-f]{24}$/.test(String(id))) return false;
  const key = `${PREFIX}${id}.json`;
  if (!(await env.UPLOADS.head(key))) return false;
  await env.UPLOADS.delete(key);
  return true;
}

const maintainers = (env) => String(env.MAINTAINERS || '').toLowerCase().split(/[\s,;]+/).filter(Boolean);

/** Tell the maintainer. Never throws: a request that is stored must not look failed to the person. */
export async function notify(env, record, portalUrl, now = new Date()) {
  if (env.MAILER) {
    try {
      const res = await env.MAILER.fetch('https://mailer/send', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ to: maintainers(env), request: record, portalUrl }),
      });
      if (res.ok) return { by: 'email' };
    } catch { /* fall through to GitHub */ }
  }
  try {
    const last = await env.UPLOADS.head(MARKER);
    const lastAt = Date.parse(last?.customMetadata?.at || '') || 0;
    if (now.getTime() - lastAt < NOTIFY_EVERY_MS) return { by: 'github', skipped: 'notified recently' };
    const res = await gh(env, `actions/workflows/${WORKFLOW}/dispatches`, { method: 'POST', body: JSON.stringify({ ref: env.GITHUB_BRANCH || 'main' }) });
    if (res.status !== 204) return { by: 'none', error: `GitHub ${res.status}` };
    await env.UPLOADS.put(MARKER, '', { customMetadata: { at: now.toISOString() } });
    return { by: 'github' };
  } catch (e) {
    return { by: 'none', error: e.message };
  }
}
