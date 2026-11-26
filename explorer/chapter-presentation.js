// Shared public presentation. Chapters supply content; structure belongs here.
export function element(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (value == null || value === false) continue;
    if (key === 'text') node.textContent = value;
    else node.setAttribute(key, value);
  }
  for (const child of children.flat(Infinity)) if (child != null) node.append(child);
  return node;
}
export function pageHeading(title, meta) {
  return element('div', {class:'page-head'}, element('h1', {text:title}),
    meta ? element('span', {class:'muted small', text:meta}) : null);
}
export function summaryTiles(items) {
  return element('div', {class:'tiles'}, items.map(({value, label, detail}) =>
    element('div', {class:'tile'}, element('div', {class:'value', text:value == null ? '\u00a0' : String(value)}),
      element('div', {class:'label', text:label}), detail == null ? null : element('div', {class:'detail', text:detail}))));
}
export function contentSection(title, text) {
  return element('section', {class:'chapter-empty'}, element('h2', {text:title}), element('p', {text}));
}
export function chapterHeading({title, eyebrow, overview = false}) {
  // Interior pages use Aphasia's page heading; only overview pages use a hero.
  return overview
    ? element('header', {class:'editorial-hero'}, element('p', {class:'eyebrow', text:eyebrow}), element('h1', {text:title}))
    : pageHeading(title);
}
export function coveragePage({meta, tiles = [], notice, flowIntro = [], diagram,
  afterDiagram, exclusions = [], reviewers = [], gaps = [], searches = [], candidates = []}) {
  const page = document.createDocumentFragment();
  page.append(pageHeading('Coverage', meta));
  if (notice) { page.append(notice); return page; }
  const append = (...nodes) => { for (const n of nodes.flat(Infinity)) if (n != null) page.append(n); };
  append(element('p', {class:'lead', text:'Follow the papers from search results to screening decisions and findings in the knowledge base.'}),
    summaryTiles(tiles), element('h2', {text:'Flow of papers (PRISMA 2020)'}), flowIntro,
    element('div', {class:'prisma-wrap'}, diagram), afterDiagram,
    element('div', {class:'grid-2'},
      element('section', {}, element('h2', {text:'Why candidates were excluded'}), exclusions),
      element('section', {}, element('h2', {text:'Who decided'}), reviewers)),
    element('h2', {text:'Coverage of the evidence gaps'}), gaps,
    element('section', {id:'database-searches'}, element('h2', {text:'Database searches'}), searches),
    element('h2', {id:'candidates', text:'Candidates'}), candidates);
  return page;
}
