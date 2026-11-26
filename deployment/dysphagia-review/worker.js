import {verifyAccessJwt} from '../../staging/dysphagia/functions/_middleware.js';
import {onRequest as decisions} from '../../staging/dysphagia/functions/api/decisions.js';
import {serveOpenAccess,syncOaDecisions} from '../../portal/lib/open-access.js';
export default {
 async scheduled(controller,env){
  const progress=await env.PRIVATE.get('open-access/decision-cursor.json');
  const cursor=progress?await progress.json():{};
  // Follow append-only changes, reading each record's current value. A correction
  // is handled next even if the reviewer has already screened thousands of papers.
  const rows=await env.SCREENING.prepare(`SELECT e.rowid AS event_id,CAST(j.key AS INTEGER) AS item_index,e.reviewer,d.value
   FROM decision_events e,json_each(e.changes) j
   JOIN screening_decisions d ON d.reviewer=e.reviewer AND d.record_id=json_extract(j.value,'$.id')
   WHERE e.rowid > ? OR (e.rowid = ? AND CAST(j.key AS INTEGER) > ?)
   ORDER BY e.rowid,CAST(j.key AS INTEGER) LIMIT 100`).bind(cursor.event||0,cursor.event||0,cursor.item??-1).all();
  const groups=new Map();
  for(const row of rows.results){const value=JSON.parse(row.value);if(!groups.has(row.reviewer))groups.set(row.reviewer,new Map());groups.get(row.reviewer).set(value.id,value);}
  for(const [reviewer,items]of groups)await syncOaDecisions(env.PRIVATE,reviewer,[...items.values()]);
  const last=rows.results.at(-1);
  if(last)await env.PRIVATE.put('open-access/decision-cursor.json',JSON.stringify({event:last.event_id,item:last.item_index}));
  if(rows.results.length<100)await env.PRIVATE.put('open-access/decisions-ready.json',JSON.stringify({at:new Date().toISOString()}));
 },
 async fetch(request,env){
  const url=new URL(request.url);
  if(!env.ACCESS_AUD)return new Response('Dysphagia review sign-in is being configured.',{status:503});
  let reviewer;
  try{
   const token=request.headers.get('Cf-Access-Jwt-Assertion');
   if(!token)throw new Error('No sign-in');
   const identity=await verifyAccessJwt(token,env);
   reviewer={email:String(identity.email).toLowerCase(),name:identity.name||null};
  }catch{return new Response('Sign in through Cloudflare Access to open Dysphagia review.',{status:401});}
  if(url.pathname==='/api/decisions')return decisions({request,env,data:{reviewer}});
  if(url.pathname==='/api/open-access'){
   const id=url.searchParams.get('id');
   const rows=await env.SCREENING.prepare('SELECT reviewer,value FROM screening_decisions WHERE record_id = ?').bind(id).all();
   const exclusions=rows.results.filter(row=>JSON.parse(row.value).decision==='exclude');
   if(exclusions.length){
    for(const row of exclusions)await syncOaDecisions(env.PRIVATE,row.reviewer,[JSON.parse(row.value)]);
   }
   return serveOpenAccess(request,env.PRIVATE);
  }
  if(!['GET','HEAD'].includes(request.method))return new Response('Method not allowed',{status:405});
  if(/^\/records(?:-\d{3})?\.json$/.test(url.pathname)){
   const object=await env.PRIVATE.get('screening'+url.pathname);
   if(!object)return new Response('Screening records unavailable',{status:404});
   return new Response(request.method==='HEAD'?null:object.body,{headers:{'Content-Type':'application/json','Cache-Control':'no-store'}});
  }
  return env.ASSETS.fetch(request);
 }
};
