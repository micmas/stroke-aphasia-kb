export function openAccessNote(id,onAvailable=()=>{}) {
  const box=document.createElement('p');box.className='small muted';
  box.textContent='Checking open-access copy…';
  const url=`/api/open-access?id=${encodeURIComponent(id)}`;
  fetch(url,{cache:'no-store'}).then(async response=>{
    if(!response.ok)throw new Error('unavailable');
    const data=await response.json();
    const labels={pending:'Open-access search queued.',not_found:'No licensed open-access PDF found yet.',retry:'Open-access retrieval will be retried.',excluded:'Collected PDF removed after exclusion.'};
    box.textContent=labels[data.status]||'Open-access copy unavailable.';
    if(data.status==='available'){
      const a=document.createElement('a');a.href=url+'&file=1';a.target='_blank';a.rel='noopener';a.textContent='Open collected PDF';
      const source=data.source||{};
      const version={acceptedVersion:'accepted manuscript',publishedVersion:'published copy',submittedVersion:'submitted manuscript'}[source.version]||'version not reported';
      box.replaceChildren(a,document.createTextNode(` · ${source.provider||'Open access'} · ${source.licence||'see source licence'} · ${version}`));
      if(source.provider==='PMC')box.append(document.createTextNode(' · Source: NLM PMC; downloaded snapshot, may not reflect later updates.'));
      onAvailable({url:a.href,label:'open-access PDF',source});
    }
  }).catch(()=>{box.textContent='Open-access collection status unavailable.';});
  return box;
}
