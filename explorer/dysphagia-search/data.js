// Search protocol draft: no database run or screening approval is implied.
export const VERSION = 'dysphagia-initial-v0.1';
export const stroke = 'stroke* OR poststroke OR "post-stroke" OR cerebrovascular OR "cerebral infarct*" OR "brain infarct*" OR "cerebral hemorrhag*" OR "cerebral haemorrhag*" OR "intracerebral hemorrhag*" OR "intracerebral haemorrhag*"';
export const swallow = 'dysphagi* OR swallow* OR deglutition';
const ebsco = `(TI (${stroke}) OR AB (${stroke})) AND (TI (${swallow}) OR AB (${swallow}))`;
const cochrane = `(${stroke}):ti,ab,kw AND (${swallow}):ti,ab,kw`;
export const DATABASES = [
 {id:'pubmed',name:'MEDLINE / PubMed',platform:'PubMed',url:'https://pubmed.ncbi.nlm.nih.gov/advanced/', established:true,
 query:'("Stroke"[Mesh] OR "Brain Ischemia"[Mesh] OR "Intracranial Hemorrhages"[Mesh] OR stroke*[tiab] OR poststroke[tiab] OR "post-stroke"[tiab] OR cerebrovascular[tiab] OR "cerebral infarct*"[tiab] OR "brain infarct*"[tiab] OR "cerebral hemorrhag*"[tiab] OR "cerebral haemorrhag*"[tiab] OR "intracerebral hemorrhag*"[tiab] OR "intracerebral haemorrhag*"[tiab]) AND ("Deglutition Disorders"[Mesh] OR dysphagi*[tiab] OR swallow*[tiab] OR deglutition[tiab])',
 instructions:'Paste into Advanced Search. Inspect Search Details and any phrase warnings. This combines MeSH with title/abstract terms; do not limit to MEDLINE-only records.',
 export:'Save all results as a PubMed-format text file (.nbib or .txt). Include abstracts; retain the search details and total count. Use a reference manager to export RIS if you want the screening-sheet converter below.',
 headings:'MeSH headings are included. Check retrieval against benchmark papers before locking the protocol.',
 source:'https://pubmed.ncbi.nlm.nih.gov/help/'},
 {id:'scopus',name:'Scopus',platform:'Scopus Advanced Search',url:'https://www.scopus.com/search/form.uri?display=advanced', established:true,
 query:`TITLE-ABS-KEY(${stroke}) AND TITLE-ABS-KEY(${swallow})`,
 instructions:'Open Scopus through UQ Library and paste into Advanced Search. Record the displayed query after applying the publication-year filter.',
 export:'Export all batches as RIS, including citation information, abstracts, keywords and identifiers. Keep batch ranges and the original files.',
 headings:'Scopus uses title, abstract and keyword searching; there is no MeSH/Emtree block to add.',source:'https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search'},
 {id:'psycinfo',name:'APA PsycINFO',platform:'EBSCOhost',url:'https://www.library.uq.edu.au/', established:true,query:ebsco,
 instructions:'Select APA PsycINFO only in EBSCOhost via UQ Library. Use Advanced Search with Boolean/Phrase mode; paste the query with its TI and AB field codes.',
 export:'Export all result batches as RIS with abstracts and identifiers. Save the database name and exact query with each batch.',
 headings:'This runnable pilot uses title/abstract terms. Before the formal search, check the APA Thesaurus for stroke and swallowing-disorder headings, OR them into their respective concept blocks, and retain the final query. Do not assume CINAHL headings apply.',source:'https://www.apa.org/pubs/databases/training/search-guides.html'},
 {id:'embase',name:'Embase',platform:'Embase.com — confirm library platform',url:'https://www.embase.com/',query:`(${stroke}):ti,ab,kw AND (${swallow}):ti,ab,kw`,
 instructions:'This version is for Embase.com, not Ovid. Open through library access and confirm the platform before pasting. If your access is Ovid, request a translation rather than reusing these field codes.',
 export:'Export article results in RIS with abstracts, keywords and identifiers. Record source collections, all batch ranges and hit counts. Keep clinical-trial registry records separate if displayed.',
 headings:'Text-word pilot. Before the formal run, use Emtree to select and explode the stroke and dysphagia headings, OR each with its text-word block, and save the resulting query.',source:'https://www.elsevier.support/embase/answer/what-field-codes-can-i-use-in-embase'},
 {id:'cinahl',name:'CINAHL',platform:'EBSCOhost — confirm edition',url:'https://www.library.uq.edu.au/',query:ebsco,
 instructions:'Select CINAHL only in EBSCOhost. Record the subscribed edition. Use Advanced Search in Boolean/Phrase mode with the TI and AB codes shown.',
 export:'Export all batches as RIS, retaining abstracts and identifiers. Do not select a full-text-only limiter.',
 headings:'Text-word pilot. Check CINAHL Headings for stroke and deglutition/swallowing disorders before locking; OR the verified exploded headings into the relevant blocks.',source:'https://eis1.my.site.com/ebsco/s/article/CINAHL-Plus-with-Full-Text-Help-Sheet?language=en_US'},
 {id:'wos',name:'Web of Science',platform:'Core Collection',url:'https://www.webofscience.com/wos/woscc/advanced-search',query:`TS=(${stroke}) AND TS=(${swallow})`,
 instructions:'Select Core Collection and Advanced Search. Record the indexes and coverage years included in your subscription. Apply the publication-year range in the interface.',
 export:'Export all batches using a reference-manager-compatible format, with full records and abstracts. Record batch ranges; preserve the original export even if converted to RIS.',
 headings:'Topic searches include the indexed topic fields; no MeSH/Emtree block is required.',source:'https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-field-tags.htm'},
 {id:'central',name:'Cochrane CENTRAL',platform:'Cochrane Library · Trials',url:'https://www.cochranelibrary.com/advanced-search/search-manager',query:cochrane,
 instructions:'Enter the expression in Search Manager, then select Trials (CENTRAL). Apply publication dates, not a Cochrane issue date. Record any unavailable date limiter and apply the date rule during screening.',
 export:'Export CENTRAL results separately as RIS with abstracts where available. Record the CENTRAL count, not the total across all Cochrane collections.',
 headings:'Text-word pilot. For the formal strategy, OR MeSH Stroke/Brain Ischemia/Intracranial Hemorrhages with the stroke block and MeSH Deglutition Disorders with the swallowing block, using the MeSH browser.',source:'https://www.cochrane.org/authors/handbooks-and-manuals/handbook/chapter04-tech-supplonlinepdfv65270924'},
 {id:'cdsr',name:'Cochrane Reviews',platform:'Cochrane Database of Systematic Reviews',url:'https://www.cochranelibrary.com/advanced-search/search-manager',query:cochrane,
 instructions:'Run the same Search Manager expression and select Cochrane Reviews. Keep this result set separate from CENTRAL. Review protocols are not completed reviews; identify them at screening.',
 export:'Export reviews separately as RIS, retaining abstracts. Record the reviews count and any date-filter limitations.',
 headings:'Use the same verified MeSH expansion as CENTRAL before the formal run; record this collection as a separate source.',source:'https://www.cochrane.org/authors/handbooks-and-manuals/handbook/chapter04-tech-supplonlinepdfv65270924'}
];
export function queryFor(db, date) {
 if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || date < '2000-01-01') throw new Error('Choose a search date on or after 1 January 2000.');
 if (db.id === 'pubmed') return `${db.query} AND ("2000/01/01"[Date - Publication] : "${date.replaceAll('-','/')}"[Date - Publication])`;
 if (db.id === 'scopus') return `${db.query} AND PUBYEAR > 1999 AND PUBYEAR < ${Number(date.slice(0,4))+1}`;
 return db.query;
}
export function csv(rows) {
 return '\uFEFF' + rows.map(row=>row.map(value=>{
  let s=String(value ?? '');
  if (/^[\s]*[=+@-]/.test(s)) s="'"+s;
  return '"'+s.replaceAll('"','""')+'"';
 }).join(',')).join('\r\n');
}
export const SCREEN_COLUMNS = ['record_id','chapter','title','abstract','authors','year','doi','source_file','all_database_sources','duplicate_of','stage','decision','exclusion_reason','reviewer','decision_date','notes'];
export function parseRIS(text, filename) {
 const records=[]; let item=null, last=null;
 for (const line of text.replace(/^\uFEFF/,'').split(/\r?\n/)) {
  const m=line.match(/^([A-Z0-9]{2})\s{2}-\s?(.*)$/);
  if (m) {
   const [,tag,value]=m;
   if (tag==='TY') { if(item) throw new Error(`${filename}: a record has no ER end tag.`); item={}; }
   if (!item) continue;
   if (tag==='ER') {records.push(item);item=null;last=null;continue;}
   (item[tag] ||= []).push(value);last=tag;
  } else if (item && last && line.trim()) item[last][item[last].length-1]+=' '+line.trim();
 }
 if(item) throw new Error(`${filename}: the last record has no ER end tag.`);
 if(!records.length) throw new Error(`${filename}: no RIS records found. Use a RIS export, not a PubMed NBIB file.`);
 return records.map((r,i)=>[`${filename}:${i+1}`,'dysphagia',(r.TI||r.T1||[''])[0],(r.AB||r.N2||['']).join('\n'),(r.AU||r.A1||[]).join('; '),(r.PY||r.Y1||[''])[0],(r.DO||[''])[0],filename,'','','title_abstract','','','','','']);
}
