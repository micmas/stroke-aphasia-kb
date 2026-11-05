// POST /api/reviews  — write one review record into the KB repository
//                      (logs/portal/inbox/<stamp>_<kind>_<reviewer>_<id>.json) through the GitHub API.
// GET  /api/reviews  — list the records in the inbox and in applied/ (names only), so the
//                      portal can show who already reviewed what.
//
// A record is data for scripts/portal_import.py, which applies it on the maintainer's machine:
// nothing here edits a draft, the register or a canonical entry directly.

const KINDS = new Set(['screen', 'verdict', 'edit', 'mark', 'comment']);
const INBOX = 'logs/portal/inbox';
const APPLIED = 'logs/portal/applied';

const slug = (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40) || 'x';

async function gh(env, path, init = {}) {
  const res = await fetch(`https://api.github.com/repos/${env.GITHUB_REPO}/${path}`, {
    ...init,
    headers: { Authorization: `Bearer ${env.GITHUB_TOKEN}`, Accept: 'application/vnd.github+json', 'User-Agent': 'stroke-aphasia-kb-portal', 'X-GitHub-Api-Version': '2022-11-28', ...(init.headers || {}) },
  });
  return res;
}

export async function onRequestGet({ env }) {
  const branch = env.GITHUB_BRANCH || 'main';
  const out = { inbox: [], applied: [] };
  for (const [key, dir] of [['inbox', INBOX], ['applied', APPLIED]]) {
    const res = await gh(env, `contents/${dir}?ref=${encodeURIComponent(branch)}`);
    if (res.status === 404) continue;
    if (!res.ok) return Response.json({ error: `GitHub ${res.status} listing ${dir}` }, { status: 502 });
    const items = await res.json();
    out[key] = (Array.isArray(items) ? items : []).filter((x) => x.type === 'file' && x.name.endsWith('.json')).map((x) => x.name);
  }
  return Response.json(out);
}

export async function onRequestPost({ request, env, data }) {
  let body;
  try { body = await request.json(); } catch { return Response.json({ error: 'JSON body expected' }, { status: 400 }); }
  const kind = String(body.kind || '');
  const id = String(body.id || '');
  if (!KINDS.has(kind)) return Response.json({ error: `kind must be one of ${[...KINDS].join(', ')}` }, { status: 400 });
  if (!id) return Response.json({ error: 'id is required (candidate id, or draft path for a draft review)' }, { status: 400 });
  if (JSON.stringify(body).length > 200_000) return Response.json({ error: 'record too large' }, { status: 413 });
  const now = new Date();
  const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\.\d+Z$/, 'Z');
  const record = { ...body, kind, id, reviewer: data.reviewer.email, reviewer_name: data.reviewer.name, submitted: now.toISOString(), portal: 1 };
  const name = `${stamp}_${kind}_${slug(data.reviewer.email.split('@')[0])}_${slug(id.replace(/^drafts\//, '').replace(/\.md$/, ''))}.json`;
  const content = btoa(unescape(encodeURIComponent(JSON.stringify(record, null, 1) + '\n')));
  const res = await gh(env, `contents/${INBOX}/${name}`, {
    method: 'PUT',
    body: JSON.stringify({ message: `Portal ${kind}: ${id} by ${data.reviewer.email}`, content, branch: env.GITHUB_BRANCH || 'main' }),
  });
  if (!res.ok) {
    const text = await res.text();
    return Response.json({ error: `GitHub ${res.status}: ${text.slice(0, 200)}` }, { status: 502 });
  }
  const out = await res.json();
  return Response.json({ ok: true, file: `${INBOX}/${name}`, commit: out.commit?.sha?.slice(0, 7) });
}
