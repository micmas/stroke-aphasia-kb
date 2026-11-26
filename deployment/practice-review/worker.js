import {verifyAccessJwt} from '../../staging/dysphagia/functions/_middleware.js';
export const stages=['title_abstract','full_text','evidence_review'];
const fields=['claim','passage','locator','perspective','limitations','appraisal','source_url'];
export function validate(body,ids,saved){
 if(!Array.isArray(body?.decisions)||!body.decisions.length||body.decisions.length>50)return 'Send 1–50 decisions.';
 const seen=new Set();
 for(const d of body.decisions){
  const key=d.stage+':'+d.id;
  if(seen.has(key))return 'Duplicate decision in batch.';seen.add(key);
  if(!ids.has(d.id)||!/^PLE-[a-f0-9]{16}$/.test(d.id)||!stages.includes(d.stage))return 'Unknown record or stage.';
  if(!['include','exclude','unsure','pending'].includes(d.decision))return 'Invalid decision.';
  if(typeof d.reason!=='string'||d.reason.length>1000||typeof d.notes!=='string'||d.notes.length>4000)return 'Invalid reason or notes.';
  if(d.decision==='exclude'&&!d.reason.trim())return 'Give an exclusion reason.';
  const before=stages.slice(0,stages.indexOf(d.stage));
  if(before.some(stage=>saved[stage+':'+d.id]?.decision!=='include'))return 'Complete the preceding screening stages first.';
  for(const field of fields)if(d.evidence?.[field]!=null&&(typeof d.evidence[field]!=='string'||d.evidence[field].length>12000))return 'Invalid evidence field.';
  if(d.evidence?.source_url&&!/^https?:\/\//i.test(d.evidence.source_url))return 'Source link must use HTTP or HTTPS.';
  if(d.stage==='evidence_review'&&d.decision==='include'&&fields.filter(f=>f!=='source_url').some(f=>!d.evidence?.[f]?.trim()))return 'A reviewed evidence note needs a claim, source passage, locator, perspective, limitations and appraisal.';
 }
 // Do not allow a batch to invalidate another decision's prerequisite.
 const next={...saved};for(const d of body.decisions)next[d.stage+':'+d.id]=d;
 for(const d of body.decisions)if(stages.slice(0,stages.indexOf(d.stage)).some(s=>next[s+':'+d.id]?.decision!=='include'))return 'Conflicting stage changes.';
 return null;
}
export async function decisions(request,env,reviewer){
 const state=await env.SCREENING.prepare('SELECT * FROM reviewer_state WHERE reviewer = ?').bind(reviewer).first();
 const rows=await env.SCREENING.prepare('SELECT stage,record_id,value FROM practice_decisions WHERE reviewer = ?').bind(reviewer).all();
 const saved=Object.fromEntries(rows.results.map(r=>[r.stage+':'+r.record_id,JSON.parse(r.value)]));const revision=state?.revision||0;
 if(request.method==='GET')return Response.json({reviewer,sha:revision,decisions:saved},{headers:{'Cache-Control':'no-store'}});
 if(request.method!=='POST')return new Response('Method not allowed',{status:405});
 let body;try{body=await request.json();}catch{return Response.json({error:'Invalid JSON'},{status:400});}
 const object=await env.PRIVATE.get('screening/record-ids.json');if(!object)return Response.json({error:'Record register unavailable'},{status:503});
 const error=validate(body,new Set(await object.json()),saved);if(error)return Response.json({error},{status:400});
 if(body.sha!==revision)return Response.json({error:'Another tab changed these decisions. Reload; your pending choices remain in this browser.'},{status:409});
 const now=new Date().toISOString(),writeId=crypto.randomUUID();
 const changes=body.decisions.map(d=>({id:d.id,stage:d.stage,decision:d.decision,reason:d.reason,notes:d.notes,evidence:Object.fromEntries(fields.map(f=>[f,d.evidence?.[f]||''])),reviewer,date:now,section:'practice',clinical_domain:'aphasia'}));
 const results=await env.SCREENING.batch([
 env.SCREENING.prepare('INSERT OR IGNORE INTO reviewer_state (reviewer) VALUES (?)').bind(reviewer),
 env.SCREENING.prepare('UPDATE reviewer_state SET revision=revision+1,write_id=? WHERE reviewer=? AND revision=?').bind(writeId,reviewer,revision),
 ...changes.map(d=>env.SCREENING.prepare('INSERT INTO practice_decisions (reviewer,stage,record_id,value) SELECT ?,?,?,? WHERE EXISTS (SELECT 1 FROM reviewer_state WHERE reviewer=? AND write_id=?) ON CONFLICT(reviewer,stage,record_id) DO UPDATE SET value=excluded.value').bind(reviewer,d.stage,d.id,JSON.stringify(d),reviewer,writeId)),
 env.SCREENING.prepare('INSERT INTO decision_events (write_id,reviewer,saved_at,revision,changes) SELECT ?,?,?,revision,? FROM reviewer_state WHERE reviewer=? AND write_id=?').bind(writeId,reviewer,now,JSON.stringify(changes),reviewer,writeId)
 ]);
 if(!results[1].meta.changes)return Response.json({error:'Concurrent save: reload before retrying.'},{status:409});
 for(const d of changes)saved[d.stage+':'+d.id]=d;
 return Response.json({ok:true,sha:revision+1,decisions:saved},{headers:{'Cache-Control':'no-store'}});
}
export default {async fetch(request,env){
 const url=new URL(request.url);let reviewer;
 if(!env.ACCESS_AUD)return new Response('Practice review sign-in has not been configured.',{status:503});
 try{const token=request.headers.get('Cf-Access-Jwt-Assertion');if(!token)throw Error();const identity=await verifyAccessJwt(token,env);reviewer=String(identity.email).toLowerCase();}catch{return new Response('Sign in through Cloudflare Access.',{status:401});}
 try{
  if(url.pathname==='/api/decisions')return await decisions(request,env,reviewer);
  if(!['GET','HEAD'].includes(request.method))return new Response('Method not allowed',{status:405});
  if(/^\/records(?:-\d{3})?\.json$/.test(url.pathname)){
   const obj=await env.PRIVATE.get('screening'+url.pathname);if(!obj)return new Response('Records unavailable',{status:404});
   return new Response(request.method==='HEAD'?null:obj.body,{headers:{'Content-Type':'application/json','Cache-Control':'no-store'}});
  }
  return env.ASSETS.fetch(request);
 }catch{return Response.json({error:'Service unavailable. Pending choices remain in your browser.'},{status:502});}
}};
