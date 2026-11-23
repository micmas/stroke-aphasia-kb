import {verifyAccessJwt} from '../../staging/dysphagia/functions/_middleware.js';
import {onRequest as decisions} from '../../staging/dysphagia/functions/api/decisions.js';
export default {
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
  if(!['GET','HEAD'].includes(request.method))return new Response('Method not allowed',{status:405});
  if(/^\/records(?:-\d{3})?\.json$/.test(url.pathname)){
   const object=await env.PRIVATE.get('screening'+url.pathname);
   if(!object)return new Response('Screening records unavailable',{status:404});
   return new Response(request.method==='HEAD'?null:object.body,{headers:{'Content-Type':'application/json','Cache-Control':'no-store'}});
  }
  return env.ASSETS.fetch(request);
 }
};
