import {verifyAccessJwt} from '../../staging/dysphagia/functions/_middleware.js';
import {onRequest as decisions} from '../../staging/dysphagia/functions/api/decisions.js';
import {serveOpenAccess,syncOaDecisions} from '../../portal/lib/open-access.js';
export default {
 async scheduled(controller,env){
  const progress=await env.PRIVATE.get('open-access/decision-cursor.json');
  const cursor=progress?(await progress.json()).cursor:0;
  const rows=await env.SCREENING.prepare('SELECT rowid,reviewer,value FROM screening_decisions WHERE rowid > ? ORDER BY rowid LIMIT 100').bind(cursor).all();
  for(const row of rows.results)await syncOaDecisions(env.PRIVATE,row.reviewer,[JSON.parse(row.value)]);
  const next=rows.results.length===100?rows.results.at(-1).rowid:0;
  await env.PRIVATE.put('open-access/decision-cursor.json',JSON.stringify({cursor:next}));
  if(!next)await env.PRIVATE.put('open-access/decisions-ready.json',JSON.stringify({at:new Date().toISOString()}));
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
