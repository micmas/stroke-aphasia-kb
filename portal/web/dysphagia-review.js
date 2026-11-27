// Dysphagia data adapter for the shared review UI. No Aphasia records are loaded.
import {prioritiseInstrumentalStudies} from './dysphagia-priority.js';
export const reasons = Object.fromEntries([
  ['wrong_population','Wrong population'], ['wrong_condition','Not swallowing / dysphagia'],
  ['wrong_question','Outside the research questions'], ['wrong_publication_type','Ineligible publication type'],
  ['outside_date_range','Outside date range'], ['duplicate','Duplicate report'], ['other','Other — explain in notes']
].map(([key,label])=>[key,{label}]));

export function candidate(record, ta, ft) {
  const history=[ta,ft].filter(Boolean).map(d=>({...d,by:d.reviewer}));
  let stage='awaiting_ta';
  if(ta?.decision==='exclude') stage='excluded';
  else if(ta?.decision==='unsure') stage='unsure_ta';
  else if(ta?.decision==='include') stage=ft?.decision==='include'?'included':ft?.decision==='exclude'?'excluded':ft?.decision==='unsure'?'unsure_ft':'awaiting_ft';
  return {...record,authors:Array.isArray(record.authors)?record.authors.join('; '):record.authors||'',stage,history};
}

export function createDysphagiaReview(api, storage = localStorage) {
  let records=[], snapshots={};
  async function refresh(){
    const [ta,ft]=await Promise.all([api('decisions'),api('full-text')]);
    snapshots={ta,ft};
    return {built:new Date().toISOString(),reasons,candidates:prioritiseInstrumentalStudies(records.map(r=>candidate(r,ta.decisions[r.id],ft.decisions[r.id])))};
  }
  return {
    async load(){
      const get=async path=>{const r=await fetch(path,{cache:'no-store'});if(!r.ok)throw new Error('Could not load Dysphagia records.');return r.json();};
      const manifest=await get('records.json');
      records=(await Promise.all(manifest.chunks.map(get))).flat();
      const screening=await refresh();
      // Preserve the old portal's browser backup, including notes and exclusion reasons.
      const legacy=JSON.parse(storage.getItem(`dysphagia-production:${snapshots.ta.reviewer}:${manifest.summary.search_date}`)||'{}');
      const storageKey=`dysphagia:${snapshots.ta.reviewer}:screen:ta`;
      const pending=JSON.parse(storage.getItem(storageKey)||'{}');
      for(const [id,d] of Object.entries(storage.getItem(storageKey+':legacy-imported')?{}:legacy))if(!pending[id]&&records.some(r=>r.id===id))pending[id]={decision:d.decision==='pending'?'':d.decision,reason:d.reason,note:d.notes};
      storage.setItem(storageKey,JSON.stringify(pending));
      storage.setItem(storageKey+':legacy-imported','1');
      return screening;
    },
    refresh,
    reviews(){return Object.values(snapshots).flatMap(s=>Object.values(s.decisions||{})).sort((a,b)=>String(b.date).localeCompare(String(a.date)));},
    async send(records){
      const stage=records[0]?.stage==='full_text'?'ft':'ta';
      if(records.some(r=>r.kind!=='screen'||r.stage!==(stage==='ft'?'full_text':'title_abstract')))throw new Error('Only one screening stage can be saved at a time.');
      let warning='';
      for(let i=0;i<records.length;i+=100){
        const result=await api(stage==='ft'?'full-text':'decisions',{method:'POST',body:JSON.stringify({sha:snapshots[stage].sha,decisions:records.slice(i,i+100).map(r=>({id:r.id,decision:r.decision,reason:r.reason||'',notes:r.note||''}))})});
        snapshots[stage]=result; warning=result.oaWarning||warning;
      }
      return {files:[],oaWarning:warning};
    }
  };
}
