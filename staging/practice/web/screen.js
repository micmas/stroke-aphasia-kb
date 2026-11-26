const $=id=>document.getElementById(id),stages=['title_abstract','full_text','evidence_review'];
let records=[],saved={},pending={},sha=0,reviewer='',key='',index=0,saving=false;
const stage=()=>$('stage').value,empty=()=>({decision:'pending',reason:'',notes:'',evidence:{}});
const decision=(id,s=stage())=>pending[s+':'+id]||saved[s+':'+id]||empty();
const eligible=(r,s=stage())=>stages.slice(0,stages.indexOf(s)).every(before=>decision(r.id,before).decision==='include');
function el(tag,text,cls){const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;}
function message(t){$('message').textContent=t;}
function persist(){try{localStorage.setItem(key,JSON.stringify(pending));}catch{message('Browser backup unavailable. Save before leaving.');}}
function change(r,patch){pending[stage()+':'+r.id]={...decision(r.id),...patch,id:r.id,stage:stage()};persist();progress();}
function filtered(){const q=$('search').value.trim().toLowerCase(),f=$('filter').value;return records.filter(r=>eligible(r)&&(f==='all'||decision(r.id).decision===f)&&(!q||[r.title,r.doi,r.id,...r.authors].join(' ').toLowerCase().includes(q)));}
function progress(){
 $('dashboard').replaceChildren();
 for(const [s,label]of [['title_abstract','Title & abstract'],['full_text','Full text'],['evidence_review','Evidence review']]){const pool=records.filter(r=>eligible(r,s));const complete=pool.filter(r=>['include','exclude'].includes(decision(r.id,s).decision)).length;const n=el('p',`${label}: ${complete.toLocaleString()} decided / ${pool.length.toLocaleString()} eligible`);$('dashboard').append(n);}
 const pool=records.filter(r=>eligible(r));const counts={pending:0,include:0,exclude:0,unsure:0};for(const r of pool)counts[decision(r.id).decision]++;
 $('progress').textContent=`${pool.length.toLocaleString()} in this stage · ${counts.pending} awaiting decision · ${counts.include} included/reviewed · ${counts.exclude} excluded/rejected · ${counts.unsure} unsure · ${Object.keys(pending).length} unsaved`;
 $('save').disabled=saving||!Object.keys(pending).length;$('download').disabled=!records.length;
}
function render(keep){
 const list=filtered();index=Math.max(0,Math.min(index,list.length-1));const r=(keep&&records.find(r=>r.id===keep))||list[index];const panel=$('paper');panel.replaceChildren();progress();
 $('position').textContent=r?`${list.length.toLocaleString()} in this view · ${r.id}`:'No records in this view';$('previous').disabled=index<=0;$('next').disabled=!list.length;
 if(!r){panel.append(el('p',stage()==='title_abstract'?'No records match this view.':'Include papers in the preceding stage to populate this queue.'));return;}
 const a=el('article','');a.append(el('h2',r.title),el('p',`${r.authors.join('; ')} · ${r.year||'Year unavailable'} · ${r.journal}`,'meta'));
 if(r.doi){const link=el('a','Open publisher / source');link.href='https://doi.org/'+encodeURIComponent(r.doi);link.target='_blank';link.rel='noopener';a.append(link);}
 a.append(el('h3','Abstract'),el('p',r.abstract||'No abstract supplied. Retain as unsure if the title is insufficient.','abstract'));
 if(stage()!=='title_abstract')a.append(el('p','Read the full source before deciding. A publisher link may require library access. Record the source and page/section in your notes.'));
 if(stage()==='evidence_review'){
  const form=el('div','','form');
  for(const [field,label]of [['claim','Evidence claim'],['passage','Exact supporting source passage'],['locator','Page / table / section'],['perspective','Perspective: person with aphasia, family, clinician; keep distinctions'],['limitations','Study context and limitations; for MIC: instrument, anchor and recovery phase'],['appraisal','Appraisal and source-check notes'],['source_url','Source / licensed PDF URL (optional)']]){
   const l=el('label',label),input=document.createElement('textarea');input.maxLength=12000;input.value=decision(r.id).evidence?.[field]||'';input.oninput=()=>change(r,{evidence:{...decision(r.id).evidence,[field]:input.value}});l.append(input);form.append(l);
  }a.append(form,el('p','Marking reviewed saves a private paper-level evidence note. It does not publish an approved KB finding.'));
 }
 const choices=el('div','','choices');for(const [v,label]of [['include',stage()==='evidence_review'?'Mark reviewed':'Include'],['exclude',stage()==='evidence_review'?'Reject note':'Exclude'],['unsure','Unsure / needs work'],['pending','Clear decision']]){const b=el('button',label,decision(r.id).decision===v?'selected':'');b.setAttribute('aria-pressed',String(decision(r.id).decision===v));b.onclick=()=>{change(r,{decision:v,reason:v==='exclude'?decision(r.id).reason:''});render(r.id);};choices.append(b);}a.append(choices);
 const form=el('div','','form'),reasonLabel=el('label','Exclusion / rejection reason'),reason=document.createElement('select');
 for(const [v,label]of [['','Choose a reason'],['wrong_population','Not adults with post-stroke aphasia'],['not_separable','Relevant population or perspective not separable'],['wrong_question','Outside practice / meaningful-outcome questions'],['wrong_publication_type','No eligible research findings'],['insufficient_source','Source does not support this note'],['duplicate','Duplicate report'],['other','Other — explain in notes']]){const o=el('option',label);o.value=v;reason.append(o);}reason.value=decision(r.id).reason;reason.disabled=decision(r.id).decision!=='exclude';reason.onchange=()=>change(r,{reason:reason.value});reasonLabel.append(reason);form.append(reasonLabel);
 const label=el('label','Notes'),notes=document.createElement('textarea');notes.maxLength=4000;notes.value=decision(r.id).notes;notes.oninput=()=>change(r,{notes:notes.value});label.append(notes);form.append(label);a.append(form);
 const provenance=document.createElement('details');provenance.append(el('summary','Original export records'));for(const s of r.sources)provenance.append(el('p',`${s.database} · ${s.strategy} · ${s.file} · record ${s.record}`));a.append(provenance);panel.append(a);
}
async function api(options){const res=await fetch('/api/decisions',{cache:'no-store',...options});let out;try{out=await res.json();}catch{throw Error('Sign-in or review service unavailable.');}if(!res.ok)throw Error(out.error||'Unable to save.');return out;}
$('save').onclick=async()=>{
 const deferred=Object.values(pending).filter(d=>!eligible({id:d.id},d.stage));
 const todo=Object.values(pending).filter(d=>eligible({id:d.id},d.stage)).sort((a,b)=>stages.indexOf(a.stage)-stages.indexOf(b.stage));
 if(todo.some(d=>d.decision==='exclude'&&!d.reason.trim())){message('Choose a reason for every exclusion.');return;}
 saving=true;progress();message('Saving…');
 try{ // Save each stage in order so later-stage prerequisites are durable.
  for(const s of stages){const items=todo.filter(d=>d.stage===s);for(let n=0;n<items.length;n+=50){const batch=items.slice(n,n+50);const out=await api({method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sha,decisions:batch})});sha=out.sha;saved=out.decisions;for(const d of batch){const k=d.stage+':'+d.id;if(JSON.stringify(pending[k])===JSON.stringify(d))delete pending[k];}persist();}}
  message('Saved with reviewer attribution and an audit record.'+(deferred.length?` ${deferred.length} later-stage notes remain in your browser until preceding stages are included again.`:''));
 }catch(e){message(e.message);}finally{saving=false;render();}
};
for(const id of ['stage','filter'])$(id).onchange=()=>{index=0;render();};$('search').oninput=()=>{index=0;render();};$('previous').onclick=()=>{index--;render();};$('next').onclick=()=>{const list=filtered(),id=$('position').textContent.split(' · ').at(-1),at=list.findIndex(r=>r.id===id);index=at<0?index:at+1;render();};
$('download').onclick=()=>{const rows=[['id','title','stage','decision','reason','notes','claim','passage','locator','perspective','limitations','appraisal','source_url','reviewer','saved_date','save_status']];for(const r of records)for(const s of stages){const k=s+':'+r.id,d=pending[k]||saved[k];if(d)rows.push([r.id,r.title,s,d.decision,d.reason,d.notes,...['claim','passage','locator','perspective','limitations','appraisal','source_url'].map(f=>d.evidence?.[f]||''),reviewer,d.date||'',pending[k]?'unsaved':'saved']);}const csv=rows.map(row=>row.map(v=>'"'+String(v??'').replace(/^[\s]*[=+@-]/,"'$&").replaceAll('"','""')+'"').join(',')).join('\r\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'}));a.download='practice-review-decisions.csv';a.click();URL.revokeObjectURL(a.href);};
window.addEventListener('beforeunload',e=>{if(Object.keys(pending).length){e.preventDefault();e.returnValue='';}});
try{
 const res=await fetch('records.json',{cache:'no-store'});if(!res.ok)throw Error('Screening records unavailable.');const data=await res.json();records=(await Promise.all(data.chunks.map(async name=>{const r=await fetch(name,{cache:'no-store'});if(!r.ok)throw Error('A record batch could not be loaded.');return r.json();}))).flat();
 const remote=await api();saved=remote.decisions;sha=remote.sha;reviewer=remote.reviewer;key=`practice-review:${reviewer}:${data.summary.search_date}`;try{pending=JSON.parse(localStorage.getItem(key)||'{}');}catch{pending={};}
 const ids=new Set(records.map(r=>r.id));pending=Object.fromEntries(Object.entries(pending).filter(([k,d])=>ids.has(d.id)&&stages.includes(d.stage)&&k===d.stage+':'+d.id));
 $('identity').textContent=`Signed in as ${reviewer}`;$('sources').append(el('p',`${data.summary.raw_records.toLocaleString()} imported occurrences; ${records.length.toLocaleString()} candidates after deduplication; ${data.summary.missing_abstracts} without abstracts.`));for(const w of data.summary.warnings||[])$('sources').append(el('p',w));render();
}catch(e){message(e.message);$('paper').replaceChildren(el('p','The queue is unavailable until sign-in and saved decisions load. Browser backups are unchanged.'));}
