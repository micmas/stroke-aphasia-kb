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

export async function onRequestGet({ env, data }) {
  try {
    const [run, records] = await Promise.all([latestRun(env), listRecords(env)]);
    return Response.json({ maintainer: isMaintainer(env, data.reviewer?.email), inbox: records.inbox.length, run });
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
