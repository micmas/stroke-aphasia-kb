// The one way the portal writes to the repository: a new JSON record under
// logs/portal/inbox/ through the GitHub contents API (one commit per record).
// Shared by functions/api/reviews.js and functions/api/upload.js.

export const INBOX = 'logs/portal/inbox';
export const APPLIED = 'logs/portal/applied';

export const slug = (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40) || 'x';

export async function gh(env, path, init = {}) {
  return fetch(`https://api.github.com/repos/${env.GITHUB_REPO}/${path}`, {
    ...init,
    headers: { Authorization: `Bearer ${env.GITHUB_TOKEN}`, Accept: 'application/vnd.github+json', 'User-Agent': 'stroke-aphasia-kb-portal', 'X-GitHub-Api-Version': '2022-11-28', ...(init.headers || {}) },
  });
}

/** Names of the JSON records in inbox/ and applied/ (so the portal can show who reviewed what). */
export async function listRecords(env) {
  const branch = env.GITHUB_BRANCH || 'main';
  const out = { inbox: [], applied: [] };
  for (const [key, dir] of [['inbox', INBOX], ['applied', APPLIED]]) {
    const res = await gh(env, `contents/${dir}?ref=${encodeURIComponent(branch)}`);
    if (res.status === 404) continue;
    if (!res.ok) throw Object.assign(new Error(`GitHub ${res.status} listing ${dir}`), { status: 502 });
    const items = await res.json();
    out[key] = (Array.isArray(items) ? items : []).filter((x) => x.type === 'file' && x.name.endsWith('.json')).map((x) => x.name);
  }
  return out;
}

/** Commit one record. `reviewer` is {email, name} from the Access check; `kind` and `id` name the file. */
export async function putRecord(env, reviewer, kind, id, body) {
  const now = new Date();
  const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\.\d+Z$/, 'Z');
  const record = { ...body, kind, id, reviewer: reviewer.email, reviewer_name: reviewer.name, submitted: now.toISOString(), portal: 1 };
  const name = `${stamp}_${kind}_${slug(reviewer.email.split('@')[0])}_${slug(id.replace(/^drafts\//, '').replace(/\.md$/, ''))}.json`;
  const content = btoa(unescape(encodeURIComponent(JSON.stringify(record, null, 1) + '\n')));
  const res = await gh(env, `contents/${INBOX}/${name}`, {
    method: 'PUT',
    body: JSON.stringify({ message: `Portal ${kind}: ${id} by ${reviewer.email}`, content, branch: env.GITHUB_BRANCH || 'main' }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw Object.assign(new Error(`GitHub ${res.status}: ${text.slice(0, 200)}`), { status: 502 });
  }
  const out = await res.json();
  return { file: `${INBOX}/${name}`, commit: out.commit?.sha?.slice(0, 7), record };
}
