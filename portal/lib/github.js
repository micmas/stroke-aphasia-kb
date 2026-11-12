// The one way the portal writes to the repository: a new JSON record under
// logs/portal/inbox/ through the GitHub contents API (one commit per record).
// Shared by functions/api/reviews.js and functions/api/upload.js.

// Git ownership is separate from the authenticated reviewer in each audit record.
export const COMMIT_IDENTITY = { name: 'micmas', email: 'michelemt8@gmail.com' };

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

/** The record as written, and the file name it gets: <stamp>_<kind>_<reviewer>_<id>.json. */
function recordFile(reviewer, kind, id, body, now, seq = 0) {
  const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\.\d+Z$/, 'Z');
  const record = { ...body, kind, id, reviewer: reviewer.email, reviewer_name: reviewer.name, submitted: now.toISOString(), portal: 1 };
  const name = `${stamp}${seq ? `-${String(seq).padStart(2, '0')}` : ''}_${kind}_${slug(reviewer.email.split('@')[0])}_${slug(id.replace(/^drafts\//, '').replace(/\.md$/, ''))}.json`;
  return { name, record, text: JSON.stringify(record, null, 1) + '\n' };
}

/** Commit one record. `reviewer` is {email, name} from the Access check; `kind` and `id` name the file. */
export async function putRecord(env, reviewer, kind, id, body) {
  const now = new Date();
  const { name, record, text } = recordFile(reviewer, kind, id, body, now);
  const content = btoa(unescape(encodeURIComponent(text)));
  const res = await gh(env, `contents/${INBOX}/${name}`, {
    method: 'PUT',
    body: JSON.stringify({ message: `Portal ${kind}: ${id} by ${reviewer.email}`, content, branch: env.GITHUB_BRANCH || 'main', author: COMMIT_IDENTITY, committer: COMMIT_IDENTITY }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw Object.assign(new Error(`GitHub ${res.status}: ${text.slice(0, 200)}`), { status: 502 });
  }
  const out = await res.json();
  return { file: `${INBOX}/${name}`, commit: out.commit?.sha?.slice(0, 7), record };
}

/**
 * Commit several records at once: one commit, one file per record, so a "Send" of forty
 * screening decisions is one push (and one rebuild of the explorer) instead of forty.
 * Uses the git data API: read the branch head, build a tree on top of it, commit, move the ref.
 * `records` is [{kind, id, body}]. Returns {files, commit, records}.
 */
export async function putRecords(env, reviewer, records) {
  if (records.length === 1) {
    const { kind, id, body } = records[0];
    const one = await putRecord(env, reviewer, kind, id, body);
    return { files: [one.file], commit: one.commit, records: [one.record] };
  }
  const branch = env.GITHUB_BRANCH || 'main';
  const now = new Date();
  const files = records.map((r, i) => recordFile(reviewer, r.kind, r.id, r.body, now, i + 1));
  const kinds = [...new Set(records.map((r) => r.kind))].join(', ');
  const message = `Portal: ${records.length} ${kinds} records by ${reviewer.email}`;
  const fail = async (res, what) => { const text = await res.text(); throw Object.assign(new Error(`GitHub ${res.status} ${what}: ${text.slice(0, 200)}`), { status: 502 }); };
  for (let attempt = 0; attempt < 3; attempt += 1) {
    const refRes = await gh(env, `git/ref/heads/${encodeURIComponent(branch)}`);
    if (!refRes.ok) await fail(refRes, 'reading the branch');
    const head = (await refRes.json()).object.sha;
    const treeRes = await gh(env, 'git/trees', {
      method: 'POST',
      body: JSON.stringify({ base_tree: head, tree: files.map((f) => ({ path: `${INBOX}/${f.name}`, mode: '100644', type: 'blob', content: f.text })) }),
    });
    if (!treeRes.ok) await fail(treeRes, 'writing the tree');
    const tree = (await treeRes.json()).sha;
    const commitRes = await gh(env, 'git/commits', { method: 'POST', body: JSON.stringify({ message, tree, parents: [head], author: COMMIT_IDENTITY, committer: COMMIT_IDENTITY }) });
    if (!commitRes.ok) await fail(commitRes, 'writing the commit');
    const sha = (await commitRes.json()).sha;
    const moveRes = await gh(env, `git/refs/heads/${encodeURIComponent(branch)}`, { method: 'PATCH', body: JSON.stringify({ sha, force: false }) });
    if (moveRes.ok) return { files: files.map((f) => `${INBOX}/${f.name}`), commit: sha.slice(0, 7), records: files.map((f) => f.record) };
    if (moveRes.status !== 422 || attempt === 2) await fail(moveRes, 'moving the branch');   // 422: someone pushed meanwhile; rebuild on the new head
  }
  throw Object.assign(new Error('GitHub: the branch kept moving'), { status: 502 });
}
