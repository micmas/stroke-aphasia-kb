// The maintainer's "Apply now" button.
//   POST /api/apply   start the apply workflow (.github/workflows/portal-apply.yml) through the
//                     GitHub API: it runs portal_import.py on the inbox, commits, and the explorer
//                     and this portal rebuild from that push. Only emails in MAINTAINERS may call it.
//   GET  /api/apply   the latest run of that workflow (status, conclusion, when, link) and how
//                     many records wait in the inbox, so the page can show progress.
// The token needs Actions: read and write on the repository, besides Contents.
import { gh, listRecords } from '../../lib/github.js';

export const WORKFLOW = 'portal-apply.yml';

const maintainers = (env) => String(env.MAINTAINERS || '').toLowerCase().split(/[\s,;]+/).filter(Boolean);
export const isMaintainer = (env, email) => maintainers(env).includes(String(email || '').toLowerCase());

async function latestRun(env) {
  const res = await gh(env, `actions/workflows/${WORKFLOW}/runs?per_page=1`);
  if (res.status === 404) return null;                       // the workflow file is not on the branch yet
  if (!res.ok) throw Object.assign(new Error(`GitHub ${res.status} reading the workflow runs`), { status: 502 });
  const run = (await res.json()).workflow_runs?.[0];
  return run ? { status: run.status, conclusion: run.conclusion, started: run.run_started_at || run.created_at, updated: run.updated_at, url: run.html_url, event: run.event } : null;
}

/** Separate records the hosted workflow can act on from local PDF intake and orphan edits.
 * Keep attention records in the inbox: their content must not be silently discarded.
 */
export async function inboxSummary(env, records) {
  let ready = 0, pdf = 0;
  const attention = [];
  for (const file of records.inbox) {
    if (file.includes('_pdf_')) { pdf += 1; continue; }
    if (['_edit_', '_mark_', '_comment_'].some((kind) => file.includes(kind))) {
      const response = await gh(env, `contents/logs/portal/inbox/${encodeURIComponent(file)}?ref=${encodeURIComponent(env.GITHUB_BRANCH || 'main')}`);
      if (!response.ok) throw new Error(`Cannot inspect pending record ${file}`);
      let record;
      try {
        const body = await response.json();
        record = JSON.parse(new TextDecoder().decode(Uint8Array.from(atob(body.content.replace(/\s/g, '')), (c) => c.charCodeAt(0))));
      } catch { attention.push({ file, reason: 'This record could not be read; maintainer review is needed.' }); continue; }
      const path = String(record.id || '');
      if (!/^drafts\/[a-z0-9_/-]+\.md$/i.test(path) || path.includes('..')) {
        attention.push({ file, reason: 'This record does not identify a valid draft.' }); continue;
      }
      const draft = await gh(env, `contents/${path}?ref=${encodeURIComponent(env.GITHUB_BRANCH || 'main')}`);
      if (draft.status === 404) {
        attention.push({ file, draft: path, reason: 'The original draft is no longer pending (it may have been approved). This edit is preserved for maintainer review.' }); continue;
      }
      if (!draft.ok) throw new Error(`Cannot check draft ${path}`);
    }
    ready += 1;
  }
  return { ready, pdf, attention };
}

export async function onRequestGet({ env, data }) {
  try {
    const [run, records] = await Promise.all([latestRun(env), listRecords(env)]);
    const summary = await inboxSummary(env, records);
    return Response.json({ maintainer: isMaintainer(env, data.reviewer?.email), inbox: records.inbox.length, ...summary, run });
  } catch (e) {
    return Response.json({ error: e.message }, { status: e.status || 502 });
  }
}

export async function onRequestPost({ env, data }) {
  if (!isMaintainer(env, data.reviewer?.email)) return Response.json({ error: 'only a maintainer can apply the inbox' }, { status: 403 });
  try {
    const current = await latestRun(env);
    if (current && ['queued', 'in_progress', 'waiting', 'pending', 'requested'].includes(current.status)) {
      return Response.json({ ok: true, alreadyRunning: true, run: current });
    }
    const summary = await inboxSummary(env, await listRecords(env));
    if (!summary.ready) return Response.json({ ok: true, nothingToApply: true, ...summary });
    const res = await gh(env, `actions/workflows/${WORKFLOW}/dispatches`, {
      method: 'POST',
      body: JSON.stringify({ ref: env.GITHUB_BRANCH || 'main', inputs: { requested_by: data.reviewer.email } }),
    });
    if (res.status !== 204) {
      const text = await res.text();
      const hint = res.status === 403 ? ' (the GitHub token needs Actions: read and write)' : res.status === 404 ? ' (is .github/workflows/portal-apply.yml on the branch?)' : '';
      throw Object.assign(new Error(`GitHub ${res.status} starting the workflow${hint}: ${text.slice(0, 160)}`), { status: 502 });
    }
    return Response.json({ ok: true, started: new Date().toISOString() });
  } catch (e) {
    return Response.json({ error: e.message }, { status: e.status || 502 });
  }
}
