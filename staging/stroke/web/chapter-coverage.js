// The import manifest describes the original search batch, not live review decisions.
import {element as node, coveragePage} from './chapter-presentation.js';
const number = value => Number(value).toLocaleString();
const paragraph = text => node('p', {text});
const link = (text, href) => node('a', {text, href});

export function renderImportCoverage(manifest, prismaDiagram, {databases, searchHref, reviewHref, collectionName, gapText, auditNotes = []}) {
  const files = manifest?.files || [];
  const groups = Object.entries(databases).map(([id, name]) => {
    const exports = files.filter(file => file.database === id);
    return {id, name, exports, records: exports.reduce((total, file) => total + file.records, 0)};
  }).filter(group => group.exports.length);
  const date = manifest?.search_date
    ? new Intl.DateTimeFormat('en-AU', {day:'numeric', month:'long', year:'numeric', timeZone:'UTC'}).format(new Date(manifest.search_date + 'T00:00:00Z'))
    : 'Date not recorded';
  const meta = `${groups.length} databases · initial search batch · ${date}`;
  if (!manifest) return coveragePage({meta, notice:paragraph('Search import details are not available yet.')});
  const tiles = [
    {value:number(manifest.raw_records), label:'database records', detail:`${groups.length} databases · before deduplication`},
    ...['screened','included','in the knowledge base'].map(label => ({value:null, label, detail:'Not yet reported'})),
  ];
  // Reuse the Aphasia diagram, including its geometry, colours and responsive styling.
  // Missing downstream values stay blank; no Aphasia evidence is loaded here.
  const index = {screening:{
    prisma:{identification:{databases:{records:manifest.raw_records,
      byDatabase:Object.fromEntries(groups.map(group => [group.name, group.records]))},
      duplicatesRemoved:manifest.duplicates_collapsed, other:{}},
      screening:{}, other:{}, included:{}},
    searches:new Map(), sourceKinds:{}, reasonLabel:key => key,
  }};
  const diagram = prismaDiagram(index, {identificationOnly:true, initialScreeningRecords:manifest.unique_records});
  const searchSection = node('div', {},
    paragraph(`Search batch: ${date}. Counts below are records actually present in the supplied exports, before deduplication. A paper can appear in more than one database.`),
    node('p', {}, link('Read the search questions and database queries', searchHref)));
  const body = node('tbody');
  for (const group of groups) body.append(node('tr', {},
    node('th', {scope:'row', text:group.name}), node('td', {class:'num', text:number(group.records)}),
    node('td', {class:'num', text:String(group.exports.length)}),
    node('td', {text:group.id === 'pubmed' ? 'NBIB' : 'RIS'})));
  searchSection.append(node('div', {class:'cand-wrap'}, node('table', {class:'database-import-table'},
    node('caption', {class:'small muted', text:'Imported database records'}),
    node('thead', {}, node('tr', {}, ...['Database', 'Records', 'Export files', 'Format'].map(text => node('th', {scope:'col', text})))),
    body,
    node('tfoot', {}, node('tr', {}, node('th', {scope:'row', text:'Total'}),
      node('td', {class:'num', text:number(manifest.raw_records)}), node('td', {class:'num', text:String(files.length)}), node('td'))))));
  for (const warning of manifest.warnings || []) searchSection.append(node('p', {class:'notice',
    text:`Export check: ${warning} Totals use the actual file contents; check this discrepancy against the saved database search history.`}));
  searchSection.append(node('p', {class:'small muted', text:'Search completion was reported by the researcher. The exact queries, filters and database result totals still need to be checked against the saved search histories.'}));
  const audit = node('details', {class:'editorial-details', id:'duplicate-import-details'}, node('summary', {text:'Export files and import details'}),
    paragraph(`The import combined ${number(manifest.duplicates_collapsed)} duplicate occurrences, leaving ${number(manifest.unique_records)} unique candidates for screening. ${number(manifest.missing_abstracts)} candidates have no abstract. These are import statistics, not eligibility decisions.`),
    paragraph(manifest.deduplication),
    ...auditNotes.map(paragraph),
  );
  const fileList = node('ul', {class:'import-files small'});
  for (const file of files) fileList.append(node('li', {}, node('code', {text:file.file}), ` · ${number(file.records)} records`));
  audit.append(fileList);
  searchSection.append(audit);
  return coveragePage({meta, tiles, diagram,
    flowIntro:[
      node('p', {class:'small muted', text:'Database records, duplicates removed and the initial pool for title/abstract screening are populated. The screening pool is the number remaining after deduplication, not completed reviews. Later counts are left blank until screening, inclusion and extraction results are ready to report. Blank boxes do not mean zero.'}),
      paragraph('Select “Records from databases” to see the export details below.'),
    ],
    exclusions:[paragraph('Exclusion reasons will appear when screening results are ready to report.')],
    reviewers:[paragraph('Reviewer attribution will accompany published screening decisions.')],
    gaps:[paragraph(gapText)],
    searches:[searchSection],
    candidates:[paragraph(`Titles, abstracts and your current decisions are available in the separate ${collectionName} review workspace. This public page reports the original search batch.`),
      link('Open title & abstract screening', reviewHref)],
  });
}
