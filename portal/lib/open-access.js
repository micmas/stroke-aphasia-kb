// Private, automatically collected copies; never working or annotated source PDFs.
export const OA = 'open-access/';
export const validId = id => /^(?:C\d+|U[a-f0-9]{32}|DYS-[a-f0-9]{16})$/.test(id || '');
export const pdfKey = id => `${OA}pdf/${id}.pdf`;
const hash = async value => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value)))].map(x => x.toString(16).padStart(2,'0')).join('');
export async function excluded(bucket, id) {
  let cursor;
  do {
    const page=await bucket.list({prefix:`${OA}decisions/${id}/`,cursor,include:['customMetadata']});
    for(const item of page.objects){
      if(item.customMetadata?.decision){if(item.customMetadata.decision==='exclude')return true;continue;}
      const row=await bucket.get(item.key);if(row && (await row.json()).decision==='exclude')return true;
    }
    cursor=page.truncated?page.cursor:undefined;
  }while(cursor);
  return false;
}
export async function syncOaDecisions(bucket, reviewer, decisions) {
  if (!bucket) return;
  const who = await hash(reviewer);
  for (const d of decisions) {
    if (!validId(d.id) || d.role || !['title_abstract','full_text'].includes(d.stage)
        || !['include','exclude','unsure','pending'].includes(d.decision)) continue;
    const suffix = `${d.id}/${who}-${d.stage}.json`;
    const receipt = `${OA}decisions/${suffix}`;
    const date=d.date || new Date().toISOString();
    const value=JSON.stringify({id:d.id,stage:d.stage,decision:d.decision,date});
    let changed=false,stored=false;
    for(let attempt=0;attempt<5;attempt++){
      const old=await bucket.get(receipt),oldText=old?await old.text():null;
      if(oldText && JSON.parse(oldText).date>date){stored=true;break;}
      if(oldText===value){stored=true;break;}
      const written=await bucket.put(receipt,value,{
        onlyIf:new Headers(old?{'If-Match':old.httpEtag}:{'If-None-Match':'*'}),
        customMetadata:{id:d.id,decision:d.decision,stage:d.stage,date},
      });
      if(written){changed=true;stored=true;break;}
    }
    if(!stored)throw new Error('Concurrent PDF state update; reconciliation will retry.');
    // Read current atomic state again: a stale pass cannot clear a newer exclusion.
    if(await excluded(bucket,d.id))await bucket.delete(pdfKey(d.id));
    else if(changed && d.decision==='include')await bucket.put(`${OA}retry/${d.id}.json`,JSON.stringify({id:d.id,at:new Date().toISOString()}));
  }
}
export async function serveOpenAccess(request,bucket) {
  if (!bucket) return Response.json({error:'Open-access collection is unavailable.'},{status:503});
  if (!['GET','HEAD'].includes(request.method)) return new Response('Method not allowed',{status:405});
  const url=new URL(request.url),id=url.searchParams.get('id');
  const headers={'Cache-Control':'private, no-store','X-Robots-Tag':'noindex'};
  if (!validId(id)) return Response.json({error:'Invalid record.'},{status:400,headers});
  const blocked=await excluded(bucket,id);
  if (url.searchParams.get('file')==='1') {
    if (blocked) return new Response('Copy removed after exclusion.',{status:404,headers});
    const obj=await bucket.get(pdfKey(id));
    if (!obj) return new Response('PDF not available.',{status:404,headers});
    return new Response(request.method==='HEAD'?null:obj.body,{headers:{...headers,'Content-Type':'application/pdf','Content-Length':String(obj.size),'Content-Disposition':`inline; filename="${id}.pdf"`}});
  }
  const object=await bucket.get(`${OA}status/${id}.json`);
  const status=object?await object.json():{status:'pending'};
  if (blocked) status.status='excluded';
  if (status.status==='available' && !(await bucket.head(pdfKey(id)))) status.status='pending';
  return Response.json(status,{headers});
}
