const chapter=location.pathname.startsWith('/aphasia/')?'aphasia':location.pathname.startsWith('/dysphagia/')?'dysphagia':null;
window.STROKE_CHAPTER=chapter;
document.addEventListener('DOMContentLoaded',()=>{
 const bar=document.createElement('div');bar.className='staging-bar';const label=document.createElement('strong');label.textContent='STAGING · Stroke KB';bar.append(label);
 const nav=document.createElement('nav');nav.setAttribute('aria-label','Chapters');for(const [text,url,id] of [['Stroke KB home','/',null],['Aphasia','/aphasia/','aphasia'],['Dysphagia','/dysphagia/','dysphagia']]){const a=document.createElement('a');a.textContent=text;a.href=url;if(chapter===id)a.setAttribute('aria-current','page');nav.append(a);}bar.append(nav);document.body.prepend(bar);
});
