import {DATABASES,VERSION,queryFor,csv,SCREEN_COLUMNS,parseRIS} from './data.js';
const $=id=>document.getElementById(id);
const STORAGE='stroke-kb-dysphagia-search-v0.1';
const today=new Intl.DateTimeFormat('en-CA',{timeZone:'Australia/Brisbane',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
let saved={};
try {saved=JSON.parse(localStorage.getItem(STORAGE)||'{}');} catch {}
if(!saved || typeof saved!=='object' || Array.isArray(saved)) saved={};
saved.records ||= {};
if(typeof saved.records!=='object' || Array.isArray(saved.records)) saved.records={};
$('searchDate').value=saved.endDate || today;
$('researcher').value=saved.researcher || '';
function message(text){$('status').textContent=text;}
function save(){
 saved.endDate=$('searchDate').value;saved.researcher=$('researcher').value;
 try {localStorage.setItem(STORAGE,JSON.stringify(saved));$('saveStatus').textContent='Saved in this browser. Download the CSV to keep a portable record.';}
 catch {$('saveStatus').textContent='Browser storage is unavailable. Download the CSV before leaving this page.';}
}
function download(name,text,type='text/plain;charset=utf-8'){
 const url=URL.createObjectURL(new Blob([text],{type})); const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function el(tag,text,cls){const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e;}
function link(text,url){const a=el('a',text);a.href=url;a.target='_blank';a.rel='noopener';return a;}
const queryBoxes={};
for(const [i,db] of DATABASES.entries()){
 const card=el('article',null,'db-card');card.id=db.id;
 const head=el('div',null,'db-head');const title=el('div');title.append(el('h3',`${String(i+1).padStart(2,'0')} / ${db.name}`),el('p',db.platform,'platform'));head.append(title,link('Open database ↗',db.url));card.append(head);
 card.append(el('p',db.instructions));
 const query=el('textarea',null,'query');query.readOnly=true;query.setAttribute('aria-label',`${db.name} search query`);queryBoxes[db.id]=query;card.append(query);
 const actions=el('div',null,'actions');const copy=el('button','Copy query');copy.onclick=async()=>{try{await navigator.clipboard.writeText(query.value);copy.textContent='Copied';setTimeout(()=>copy.textContent='Copy query',1600);}catch{query.focus();query.select();message('Select and copy the highlighted query manually.');}};
 const record=el('button','Use this query in my log');record.onclick=()=>{const q=$(`log-${db.id}-query`);q.value=query.value;saved.records[db.id].query=query.value;save();message(`${db.name}: query copied to your log. Record the actual run date, count, filters and any changes.`);};actions.append(copy,record,link('Syntax guidance',db.source));card.append(actions);
 const details=el('details');details.append(el('summary','Subject headings, export and exact query record'),el('p',db.headings),el('p',db.export));
 const qlabel=el('label',`${db.name}: exact query actually run (edit after any database changes)`);const qlog=el('textarea');qlog.id=`log-${db.id}-query`;qlog.rows=4;qlog.value=saved.records[db.id]?.query || '';qlabel.append(qlog);details.append(qlabel);card.append(details);$('databaseCards').append(card);
 const entry=saved.records[db.id] || {};saved.records[db.id]=entry;
 qlog.addEventListener('input',()=>{entry.query=qlog.value;save();});
 const row=el('tr');row.append(el('th',db.name));
 for(const [field,type,label] of [['date','date','Run date'],['hits','number','Hit count'],['files','textarea','Export files and batches'],['notes','textarea','Platform, filters, amendments or access gap']]){
  const td=el('td');const input=document.createElement(type==='textarea'?'textarea':'input');if(type!=='textarea')input.type=type;if(type==='number'){input.min='0';input.step='1';}input.setAttribute('aria-label',`${db.name}: ${label}`);input.value=entry[field] || '';input.addEventListener('input',()=>{entry[field]=input.value;save();});td.append(input);row.append(td);
 }
 $('logRows').append(row);
}
function refresh(){try{for(const db of DATABASES)queryBoxes[db.id].value=queryFor(db,$('searchDate').value);$('downloadQueries').disabled=false;message('');save();}catch(e){$('downloadQueries').disabled=true;message(e.message);}}
$('searchDate').addEventListener('change',refresh);$('researcher').addEventListener('input',save);refresh();
$('downloadQueries').onclick=()=>{
 const header=`Stroke KB — Dysphagia initial search\nVersion: ${VERSION}\nProject-owned search strategy: non-commercial only; https://aphasia-kb.app/licensing.html\nStatus: pilot; not a locked or validated systematic-search protocol\nPublication window: 2000-01-01 through ${$('searchDate').value}\nApply interface date limits where not encoded. No language/full-text/age/design limiters.\n\n`;
 download(`dysphagia-queries-${$('searchDate').value}.txt`,header+DATABASES.map(db=>`${db.name} — ${db.platform}\n${queryFor(db,$('searchDate').value)}\n\n${db.instructions}\n${db.headings}\nExport: ${db.export}\nSyntax: ${db.source}`).join('\n\n---\n\n'));
};
$('downloadLog').onclick=()=>{
 const rows=[['strategy_version','chapter','database','platform_template','run_date','run_by','hit_count','export_files_batches','exact_query_run','actual_platform_filters_amendments_access_gaps','status']];
 for(const db of DATABASES){const r=saved.records[db.id];rows.push([VERSION,'dysphagia',db.name,db.platform,r.date,$('researcher').value,r.hits,r.files,r.query,r.notes,'pilot']);}
 download('dysphagia-search-log.csv',csv(rows),'text/csv;charset=utf-8');
};
$('template').onclick=()=>download('dysphagia-screening-template.csv',csv([SCREEN_COLUMNS]),'text/csv;charset=utf-8');
$('risFiles').addEventListener('change',async event=>{
 try{
  const rows=[];const files=[...event.target.files];
  for(const file of files){if(file.size>20*1024*1024)throw new Error(`${file.name}: use an export batch smaller than 20 MB.`);rows.push(...parseRIS(await file.text(),file.name));}
  if(!rows.length)return;
  download('dysphagia-pilot-screening.csv',csv([SCREEN_COLUMNS,...rows]),'text/csv;charset=utf-8');
  $('risStatus').textContent=`Prepared ${rows.length} rows from ${files.length} RIS file(s). No deduplication or screening decisions were applied. Fill in database provenance before screening.`;
 }catch(e){$('risStatus').textContent=e.message;}
 event.target.value='';
});
