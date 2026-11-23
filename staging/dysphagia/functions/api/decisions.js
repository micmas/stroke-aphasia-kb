// Isolated staging D1 database with per-reviewer state and append-only audit events.
export const BRANCH = 'feat/dysphagia-screening-staging';
export function validate(body) {
  if (!body || !Array.isArray(body.decisions) || body.decisions.length > 100) return 'Send 1–100 decisions at a time.';
  if (!body.decisions.length) return 'No decisions supplied.';
  for (const d of body.decisions) {
    if (!/^DYS-[a-f0-9]{16}$/.test(d.id || '') || !['include','exclude','unsure','pending'].includes(d.decision)) return 'Invalid record or decision.';
    if (typeof d.reason !== 'string' || d.reason.length > 1000 || typeof d.notes !== 'string' || d.notes.length > 4000) return 'Invalid reason or notes.';
    if (d.decision === 'exclude' && !d.reason.trim()) return 'Give a reason for exclusion.';
  }
  return null;
}
export async function onRequest({request,env,data}) {
  if (!(env.GITHUB_BRANCH === BRANCH || (env.GITHUB_BRANCH === 'main' && env.SCREENING_CHAPTER === 'dysphagia')) || !env.SCREENING) return Response.json({error:'Screening storage configuration mismatch.'},{status:503});
  const email=data.reviewer.email;
  try {
    const file=await env.SCREENING.prepare('SELECT * FROM reviewer_state WHERE reviewer = ?').bind(email).first();
    const rows=await env.SCREENING.prepare('SELECT record_id,value FROM screening_decisions WHERE reviewer = ?').bind(email).all();
    const saved=Object.fromEntries(rows.results.map(row=>[row.record_id,JSON.parse(row.value)]));
    const revision=file?.revision||0;
    if(request.method==='GET') return Response.json({reviewer:email,decisions:saved,sha:revision,branch:BRANCH});
    if(request.method!=='POST') return new Response('Method not allowed',{status:405});
    const body=await request.json(); const error=validate(body);
    if(error) return Response.json({error},{status:400});
    if((body.sha||0)!==revision) return Response.json({error:'Decisions changed in another tab. Reload before saving; your pending choices remain in this browser.'},{status:409});
    const now=new Date().toISOString(),writeId=crypto.randomUUID();
    for(const d of body.decisions) saved[d.id]={id:d.id,decision:d.decision,reason:d.reason,notes:d.notes,reviewer:email,date:now,stage:'title_abstract',chapter:'dysphagia'};
    const results=await env.SCREENING.batch([
      env.SCREENING.prepare('INSERT OR IGNORE INTO reviewer_state (reviewer) VALUES (?)').bind(email),
      env.SCREENING.prepare('UPDATE reviewer_state SET revision = revision + 1, write_id = ? WHERE reviewer = ? AND revision = ?').bind(writeId,email,revision),
      ...body.decisions.map(d=>env.SCREENING.prepare('INSERT INTO screening_decisions (reviewer,record_id,value) SELECT ?,?,? WHERE EXISTS (SELECT 1 FROM reviewer_state WHERE reviewer = ? AND write_id = ?) ON CONFLICT(reviewer,record_id) DO UPDATE SET value = excluded.value').bind(email,d.id,JSON.stringify(saved[d.id]),email,writeId)),
      env.SCREENING.prepare('INSERT INTO decision_events (write_id,reviewer,saved_at,revision,changes) SELECT ?,?,?,revision,? FROM reviewer_state WHERE reviewer = ? AND write_id = ?').bind(writeId,email,now,JSON.stringify(body.decisions),email,writeId)
    ]);
    if(!results[1].meta.changes) return Response.json({error:'Another save arrived first. Reload before saving; pending choices are retained.'},{status:409});
    return Response.json({ok:true,sha:revision+1,decisions:saved});
  } catch(e) { return Response.json({error:'Unable to save or load decisions. Your browser backup is retained.'},{status:502}); }
}
