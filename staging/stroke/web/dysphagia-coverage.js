// The import manifest describes the original search batch, not live review decisions.
const DATABASES = {
  pubmed: 'PubMed', scopus: 'Scopus', psycinfo: 'PsycINFO', embase: 'Embase',
  cinahl: 'CINAHL', wos: 'Web of Science', central: 'CENTRAL', cdsr: 'Cochrane Reviews (CDSR)',
};
function node(tag, attrs = {}, ...children) {
  const element = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key === 'text') element.textContent = value;
    else element.setAttribute(key, value);
  }
  for (const child of children.flat(Infinity)) if (child != null) element.append(child);
  return element;
}
const number = value => Number(value).toLocaleString();
const paragraph = text => node('p', {text});
const link = (text, href) => node('a', {text, href});

export function renderDysphagiaCoverage(manifest, prismaDiagram) {
  const page = node('div', {class: 'dysphagia-coverage'});
  const files = manifest?.files || [];
  const groups = Object.entries(DATABASES).map(([id, name]) => {
    const exports = files.filter(file => file.database === id);
    return {id, name, exports, records: exports.reduce((total, file) => total + file.records, 0)};
  }).filter(group => group.exports.length);
  const date = manifest?.search_date
    ? new Intl.DateTimeFormat('en-AU', {day:'numeric', month:'long', year:'numeric', timeZone:'UTC'}).format(new Date(manifest.search_date + 'T00:00:00Z'))
    : 'Date not recorded';
  page.append(
    node('div', {class:'page-head'}, node('h1', {text:'Coverage'}),
      node('span', {class:'muted small', text:`${groups.length} databases · initial search batch · ${date}`})),
    node('p', {class:'lead', text:'Follow the papers from search results to screening decisions and findings in the knowledge base.'}),
  );
  if (!manifest) {
    page.append(paragraph('Search import details are not available yet.'));
    return page;
  }
  const tiles = node('div', {class:'tiles'});
  for (const [value, label, detail] of [
    [number(manifest.raw_records), 'database records', `${groups.length} databases · before deduplication`],
    ['', 'screened', 'Not yet reported'], ['', 'included', 'Not yet reported'],
    ['', 'in the knowledge base', 'Not yet reported'],
  ]) tiles.append(node('div', {class:'tile'}, node('div', {class:'value', text:value || '\u00a0'}),
    node('div', {class:'label', text:label}), node('div', {class:'detail', text:detail})));
  page.append(tiles, node('h2', {text:'Flow of papers (PRISMA 2020)'}),
    node('p', {class:'small muted', text:'Only the records imported from databases are populated. Later counts are left blank until screening, inclusion and extraction results are ready to report. Blank boxes do not mean zero.'}),
    paragraph('Select “Records from databases” to see the export details below.'),
  );
  // Reuse the Aphasia diagram, including its geometry, colours and responsive styling.
  // Missing downstream values stay blank; no Aphasia evidence is loaded here.
  const index = {screening:{
    prisma:{identification:{databases:{records:manifest.raw_records,
      byDatabase:Object.fromEntries(groups.map(group => [group.id, group.records]))}, other:{}},
      screening:{}, other:{}, included:{}},
    searches:new Map(), sourceKinds:{}, reasonLabel:key => key,
  }};
  page.append(node('div', {class:'prisma-wrap'}, prismaDiagram(index, {identificationOnly:true})));
  const searchSection = node('section', {id:'database-searches'},
    node('h2', {text:'Database searches'}),
    paragraph(`Search batch: ${date}. Counts below are records actually present in the supplied exports, before deduplication. A paper can appear in more than one database.`),
    paragraph(''),
  );
  searchSection.lastChild.append(link('Read the search questions and database queries', '/dysphagia/search/'));
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
  const audit = node('details', {class:'editorial-details'}, node('summary', {text:'Export files and import details'}),
    paragraph(`The import combined ${number(manifest.duplicates_collapsed)} duplicate occurrences, leaving ${number(manifest.unique_records)} unique candidates for screening. ${number(manifest.missing_abstracts)} candidates have no abstract. These are import statistics, not eligibility decisions.`),
    paragraph(manifest.deduplication),
    paragraph('The CENTRAL export has “cdsr” in its filename. Its folder and CN accession numbers identify it as CENTRAL; the original filename is retained.'),
  );
  const fileList = node('ul', {class:'import-files small'});
  for (const file of files) fileList.append(node('li', {}, node('code', {text:file.file}), ` · ${number(file.records)} records`));
  audit.append(fileList);
  searchSection.append(audit);
  page.append(searchSection,
    node('div', {class:'grid-2'},
      node('section', {}, node('h2', {text:'Why candidates were excluded'}), paragraph('Exclusion reasons will appear when screening results are ready to report.')),
      node('section', {}, node('h2', {text:'Who decided'}), paragraph('Reviewer attribution will accompany published screening decisions.'))),
    node('h2', {text:'Coverage of the evidence gaps'}),
    paragraph('Coverage by brain region, swallowing impairment, treatment and recovery predictor will appear after included studies have been extracted and reviewed.'),
    node('h2', {text:'Candidates'}),
    paragraph('Titles, abstracts and your current decisions are available in the separate Dysphagia review workspace. This public page reports the original search batch.'),
    link('Open title & abstract screening', '/dysphagia/screening/'),
  );
  return page;
}
