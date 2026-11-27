const PREFIX='uploads/';
const LIMIT=60*1024*1024;
export async function uploads(request,env,reviewer){
 const url=new URL(request.url),id=url.searchParams.get(request.method==='GET'?'file':'id');
 const headers={'Cache-Control':'private, no-store','X-Robots-Tag':'noindex'};
 if(request.method==='GET'&&!id){
  const uploads=[];let cursor;
  do{const page=await env.PRIVATE.list({prefix:PREFIX,cursor,include:['customMetadata']});
   for(const o of page.objects){const m=o.customMetadata||{};uploads.push({...m,object:o.key,bytes:o.size});}
   cursor=page.truncated?page.cursor:undefined;
  }while(cursor);
  return Response.json({uploads},{headers});
 }
 if(!/^DYS-[a-f0-9]{16}$/.test(id||''))return Response.json({error:'Choose a Dysphagia screening record.'},{status:400});
 const key=PREFIX+id+'.pdf';
 if(request.method==='GET'){
  const obj=await env.PRIVATE.get(key);
  return obj?new Response(obj.body,{headers:{...headers,'Content-Type':'application/pdf','Content-Disposition':`inline; filename="${id}.pdf"`}}):new Response('Not found',{status:404});
 }
 if(request.method!=='POST')return new Response('Method not allowed',{status:405});
 if(Number(request.headers.get('Content-Length'))>LIMIT)return Response.json({error:'PDF exceeds 60 MB.'},{status:413});
 const manifest=await env.PRIVATE.get('screening/records.json');
 if(!manifest)return Response.json({error:'Screening records unavailable.'},{status:503});
 let known=false;
 for(const chunk of (await manifest.json()).chunks){const obj=await env.PRIVATE.get('screening/'+chunk);if(obj&&(await obj.json()).some(r=>r.id===id)){known=true;break;}}
 if(!known)return Response.json({error:'Unknown screening record.'},{status:404});
 const bytes=await request.arrayBuffer();
 if(bytes.byteLength>LIMIT)return Response.json({error:'PDF exceeds 60 MB.'},{status:413});
 if(bytes.byteLength<1024||!new TextDecoder().decode(bytes.slice(0,8)).startsWith('%PDF-'))return Response.json({error:'Choose a PDF file.'},{status:400});
 const sha256=[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');
 const old=await env.PRIVATE.head(key);
 if(old){if(old.customMetadata?.sha256===sha256)return Response.json({ok:true,object:key});return Response.json({error:'A PDF is already stored for this paper. It has been preserved.'},{status:409});}
 const name=(url.searchParams.get('name')||'paper.pdf').replace(/[^\w.() -]/g,'_').slice(0,120);
 const result=await env.PRIVATE.put(key,bytes,{onlyIf:{etagDoesNotMatch:'*'},httpMetadata:{contentType:'application/pdf'},customMetadata:{id,name,by:reviewer.email,uploaded:new Date().toISOString(),sha256}});
 if(!result)return Response.json({error:'Another PDF was uploaded first. Reload to view it.'},{status:409});
 return Response.json({ok:true,object:key,bytes:bytes.byteLength},{headers});
}
