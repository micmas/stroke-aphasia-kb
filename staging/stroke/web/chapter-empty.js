import {contentSection as section, chapterHeading, summaryTiles} from './chapter-presentation.js';
import {renderDysphagiaCoverage} from './dysphagia-coverage.js';
const titles={findings:'Findings',matrix:'Matrix',papers:'Papers',coverage:'Coverage',involve:'Get involved',searches:'Search strategy',licences:'Paper licences',models:'Extraction & review methods',review:'Review workspace',drafts:'Drafts',fulltext:'Full-text screening',pdfs:'PDFs'};
const messages={findings:['No findings yet','Findings will appear after papers have been included, extracted and reviewed. No Aphasia findings are shown in this chapter.'],matrix:['No evidence links yet','The brain-region, swallowing-impairment and treatment matrices will populate when Dysphagia findings are available.'],papers:['No included papers yet','Database search results are candidates for screening, not included evidence. Included studies will appear here after eligibility assessment.'],licences:['No included-paper licences yet','Paper-specific access and reuse terms will be recorded as studies enter the chapter.'],drafts:['No extraction drafts yet','Drafts will appear after included papers have been processed.'],fulltext:['No full-text queue published yet','Title-and-abstract decisions are saved in the separate screening workspace. A full-text queue will be prepared from those decisions.'],pdfs:['No chapter PDFs yet','PDFs will be linked to included studies with their access and licence information.'],models:['Extraction adaptation has not started','The Dysphagia extraction method and its validation results will be documented here. Aphasia model evaluations are not evidence of performance for swallowing research.']};
function el(tag,text,cls){const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;}
function link(text,url){const a=el('a',text);a.href=url;return a;}
export function renderChapterExtra(chapter,views={}){
 const route=location.hash.replace(/^#\//,'').split('?')[0]||'';
 if(chapter==='aphasia'&&route!=='review')return false;
 const main=document.getElementById('main');main.replaceChildren();
 if(chapter==='aphasia'){
 main.append(el('h1','Aphasia review'),section('Explore the review material','Draft findings are available in this staging explorer. Active screening and source-PDF review remain in the existing Aphasia review portal.'));
 const nav=el('div','','section-links');nav.append(link('Browse Aphasia drafts','?kb=drafts#/findings'),link('Aphasia review portal (production)','https://review.aphasia-kb.app/'));main.append(nav);return true;
 }
 document.title=`${titles[route]||'Overview'} · Dysphagia KB · staging`;
 for(const a of document.querySelectorAll('.nav a')){if(a.hash==='#/'+route)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');}
 const heading=chapterHeading({title:titles[route]||'What can research tell us about swallowing after stroke?',eyebrow:'STROKE KB / DYSPHAGIA',overview:!route});main.append(heading);
 if(!route){
 heading.append(el('p','Explore brain injury, swallowing difficulties, treatment and recovery. This chapter has the same sections as Aphasia; evidence will be added as screening, extraction and review progress.','lead'));
 const counts=el('div','','project-counts');for(const text of ['0 included papers published','0 extracted findings','0 extraction drafts'])counts.append(el('p',text));main.append(counts);
 main.append(section('A chapter ready to grow','Searches have been run across eight databases. Their exported references are available for title-and-abstract screening. They have not been promoted into the knowledge base.'));
 const nav=el('div','','section-links');nav.append(link('Start title & abstract screening','/dysphagia/screening/'),link('Read the search strategy','/dysphagia/search/'));main.append(nav);
 const grid=el('div','','chapter-grid');for(const [title,text] of [['Brain regions & swallowing','No region–swallowing findings have been extracted.'],['Therapies & recovery predictors','No treatment-response or predictor findings have been extracted.']])grid.append(section(title,text));main.append(grid);
 }else if(route==='coverage'){
 main.replaceChildren(renderDysphagiaCoverage(window.DYSPHAGIA_IMPORT,views.prismaDiagram));
 }else if(route==='searches'){
 main.append(section('Search strategy and exports','The pilot search strategy covers PubMed, Scopus, PsycINFO, Embase, CINAHL, Web of Science, CENTRAL and Cochrane Reviews. Exact executed searches and limits still need their final audit.'));main.append(link('Open database queries and search log','/dysphagia/search/'));
 }else if(route==='involve'){
 main.append(section('Help build the Dysphagia chapter','Contribute to eligibility screening, source checking, adapting extraction to swallowing research, or reviewing findings. Review responsibility stays with a named person.'));main.append(link('Open the screening workspace','/dysphagia/screening/'));
 }else if(route==='review'){
 main.append(section('Dysphagia review workspace','Screen search records now. Extraction drafts, source PDFs and full-text review will become available as the chapter progresses.'));
 const nav=el('div','','section-links');for(const [text,url]of [['Title & abstract screening','/dysphagia/screening/'],['Full-text screening','#/fulltext'],['Drafts','#/drafts'],['PDFs','#/pdfs']])nav.append(link(text,url));main.append(nav);
 }else {const [title,text]=messages[route]||['Nothing here yet','Choose a section from the chapter navigation.'];main.append(section(title,text));}
 document.getElementById('footerVersion').textContent='Dysphagia · no extracted evidence published';window.scrollTo(0,0);
 if(route==='coverage'&&new URLSearchParams(location.hash.split('?')[1]).get('arm')==='databases'){
  const details=document.getElementById('database-searches');
  if(details)window.scrollTo(0,details.getBoundingClientRect().top+window.scrollY-document.querySelector('.app-header').getBoundingClientRect().height-24);
 }
 return true;
}
export function initEmptyChapter(views){
 document.querySelector('.header-tools').replaceChildren(el('span','Evidence not yet populated','source-badge'));
 window.addEventListener('hashchange',()=>renderChapterExtra('dysphagia',views));renderChapterExtra('dysphagia',views);
}
