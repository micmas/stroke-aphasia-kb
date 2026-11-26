import {contentSection as section, chapterHeading, summaryTiles} from './chapter-presentation.js';
import {renderImportCoverage} from './chapter-coverage.js';
const topics=[['Meaningful outcomes and measurement','What changes matter, and how are they recognised?'],['Lived experience and priorities','Recovery, identity, participation and personal priorities.'],['Goals and communication','Collaborative goals and conversations about progress.'],['Experiences of care','Access, acceptability and experiences of rehabilitation.']];
const names={pubmed:'PubMed',medline_ebsco:'MEDLINE (EBSCO)',embase_com:'Embase',cinahl_ebsco:'CINAHL',psycinfo_ebsco:'PsycINFO',scopus:'Scopus',web_of_science:'Web of Science'};
const titles={findings:'Findings',matrix:'Themes and outcomes',papers:'Papers',coverage:'Coverage',searches:'Searches',licences:'Paper licences',models:'Methods',involve:'Get involved',review:'Review workspace'};
function el(tag,text,cls){const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;}
function link(text,href){const n=el('a',text);n.href=href;return n;}
const fmt=n=>Number(n).toLocaleString();
export function initPractice({prismaDiagram}){
 const manifest=window.PRACTICE_IMPORT||{},main=document.getElementById('main');
 document.querySelector('.header-tools').replaceChildren(el('span','Aphasia collection · screening in progress','source-badge'));
 function render(){
  const route=location.hash.replace(/^#\//,'').split('?')[0]||'';main.replaceChildren();document.title=`${titles[route]||'Practice and lived experience'} · Stroke KB`;
  for(const a of document.querySelectorAll('.nav a')){a.toggleAttribute('aria-current',a.hash==='#/'+route);if(a.hash==='#/'+route)a.setAttribute('aria-current','page');}
  const header=chapterHeading({title:titles[route]||'What makes recovery meaningful?',eyebrow:'STROKE KB / PRACTICE AND LIVED EXPERIENCE',overview:!route});main.append(header);
  if(!route){
   header.append(el('p','Evidence about what matters to people after stroke and how that knowledge informs practice. This shared section begins with meaningful outcomes and lived experience in aphasia.','lead'));
   main.append(summaryTiles([[manifest.raw_records||0,'exported records'],[manifest.unique_records||0,'candidates to screen'],[0,'published findings']].map(([n,label])=>({value:fmt(n),label}))));
   main.append(section('A shared section, with condition-specific evidence','Each study retains its clinical population and whose perspective it represents. Aphasia findings are not assumed to generalise to all stroke survivors. Imported records are candidates, not included evidence.'));
   const grid=el('div','','chapter-grid');for(const [title,text]of topics)grid.append(section(title,text));main.append(grid);
   const nav=el('div','','section-links');nav.append(link('Review the evidence','#/review'),link('Search provenance and coverage','#/coverage'));main.append(nav);
  }else if(route==='coverage'){
   main.replaceChildren(renderImportCoverage(manifest, prismaDiagram, {
    databases:names, searchHref:'#/searches', reviewHref:'https://review.stroke-kb.app/',
    collectionName:'Practice and lived experience',
    gapText:'Coverage by meaningful outcomes, lived experience, goals and communication, and experiences of care will appear after included studies have been extracted and reviewed.',
    auditNotes:['The researcher confirmed and corrected swapped CINAHL/PsycINFO exports and filename counts. File contents were preserved. Exact executed query settings remain subject to search-history verification.'],
   }));
  }else if(route==='searches'){
   main.append(section('Two complementary questions','Q1: experiences, priorities and living well. Q2: meaningful outcomes and interpretation of change. Both search routes run from inception with no proposed language filter. Stroke aetiology is assessed at screening.'));
   main.append(el('p','Strategies adapt and expand Manning et al. (2019), rather than reproduce its searches unchanged. The queries below are the prepared queries associated with the supplied exports; they are not independently verified execution histories.'));
   const unique=new Map();for(const f of manifest.files||[])unique.set(f.database+':'+f.strategy,f);
   for(const f of unique.values()){const d=el('details','','editorial-details');d.append(el('summary',`${names[f.database]||f.database} · ${f.strategy.toUpperCase()}`));const pre=el('pre',f.query);pre.style.whiteSpace='pre-wrap';pre.style.overflowWrap='anywhere';d.append(pre);main.append(d);}
   main.append(link('Published search foundation','https://doi.org/10.1371/journal.pone.0214200'));
  }else if(route==='review'){
   main.append(section('Practice and lived experience review','Screen titles and abstracts, assess full texts, then record source-supported evidence notes. Your decisions, pending work and review progress remain separate from Aphasia and Dysphagia screening.'));
   const nav=el('div','','section-links');nav.append(link('Open review dashboard','https://review.stroke-kb.app/'));main.append(nav);
   main.append(section('Review stages','Title & abstract → Full text → Evidence notes & review. Later stages open after inclusion in the preceding stage. Reviewed paper notes stay private; publication requires source-checked individual findings.'));
  }else if(route==='models'){
   main.append(section('Evidence suited to the question','Preserve themes, source passages, participant context, perspective, limitations and appraisal. Patient, family and clinician perspectives remain distinguishable. Numeric meaningful-change estimates retain the instrument, anchor and recovery phase.'));
   main.append(section('Review and accountability','Independent screening and reconciliation precede final review counts. Qualitative and mixed-methods findings need appropriate appraisal; a model output is not approval. This section does not use lesion-response categories or inherit imaging eligibility rules.'));
   main.append(section('Publication status','Search records are loaded. No automated practice extraction has been validated, and no practice findings have been published. PRISMA 2020, PRISMA-S and ENTREQ guide reporting.'));
  }else if(route==='involve'){
   main.append(section('Help build evidence about practice','Contribute to screening, lived-experience interpretation, source checks, appraisal and qualitative synthesis. People with aphasia and family members can help judge whether interpretations preserve the meaning of their perspectives.'));main.append(link('Open the review workspace','https://review.stroke-kb.app/'));
  }else if(route==='matrix'){
   const grid=el('div','','chapter-grid');for(const [title,text]of topics)grid.append(section(title,text+' No reviewed findings are published in this topic yet.'));main.append(grid);
  }else if(route==='papers')main.append(section('No included papers published yet','The private workspace contains search candidates and full-text queues. Final included-paper lists will follow screening and reconciliation.'));
  else if(route==='licences')main.append(section('Source access and reuse','Original database exports and abstracts remain in private review storage. No source PDFs are published here. Record each source’s access and licence before sharing it.'));
  else main.append(section('No findings published yet','Source-supported findings will appear after screening, extraction, appraisal and review. Existing lesion-based Aphasia findings are not shown as practice evidence.'));
  document.getElementById('footerVersion').textContent='Practice and lived experience · Aphasia search collection · no published findings';window.scrollTo(0,0);
  if(route==='coverage'&&new URLSearchParams(location.hash.split('?')[1]).get('arm')==='databases'){
   const details=document.getElementById('database-searches');
   if(details)window.scrollTo(0,details.getBoundingClientRect().top+window.scrollY-document.querySelector('.app-header').getBoundingClientRect().height-24);
  }
 }
 window.addEventListener('hashchange',render);render();
}
