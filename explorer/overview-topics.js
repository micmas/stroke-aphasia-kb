import {ANATOMY, FACTORS, ANATOMY_GROUPS} from './topic-categories.js';
import {anatomicalGroup} from './evidence-groups.js';

export function overviewLabel(id, entry, finding) {
  if (entry.category === ANATOMY) {
    if (entry.subcategory === ANATOMY_GROUPS[1]) return 'White-matter regions and pathways';
    const broad = anatomicalGroup(finding, id)[0];
    if (broad === 'White matter') return 'White-matter regions and pathways';
    if (broad === 'Subcortical structures') return 'Subcortical grey matter';
    if (['Multi-region anatomy','Distributed functional networks','Cross-region map comparisons'].includes(broad)) return 'Mixed or distributed regions';
    return broad === 'Anatomy awaiting classification' ? 'Other brain regions' : broad;
  }
  // Topic membership is navigation, not equivalence of measurements or models.
  const name = `${id} ${entry.name || ''}`.toLowerCase().replace(/[_–-]/g,' ');
  if (/\bage\b|\baged\b|\bolder\b|\byounger\b/.test(name) && !/age of acquisition/.test(name)) return 'Age';
  if (/\bsex\b|\bgender\b|\bmale\b|\bfemale\b/.test(name)) return 'Sex and gender';
  if (/\beducation\b/.test(name)) return 'Education';
  if (/\bhandedness\b/.test(name)) return 'Handedness';
  if (/\b(?:initial|baseline)\b.*\bseverity\b/.test(name)) return 'Initial severity';
  if (/\bchronicity\b|\btime (?:post|since)\b|\benrol{1,2}ment\b/.test(name)) return 'Time since stroke';
  if (/\blesion (?:volume|size)\b/.test(name)) return 'Lesion size and volume';
  if (/\bslt\b|\btherapy\b|\bdosage\b|\bintensity\b|\bfrequency\b/.test(name)) return 'Treatment characteristics';
  if (entry.subcategory === 'Lesion and imaging measures') return 'Other imaging measures';
  if (entry.subcategory === 'Personal characteristics') return 'Other personal characteristics';
  return 'Other clinical characteristics';
}

export function overviewTopics(index, category) {
  const topics = new Map();
  for (const f of index.findings) {
    for (const id of new Set([f.source_id, f.target])) {
      const entry = index.entries[id];
      if (entry?.category !== category) continue;
      const label = overviewLabel(id, entry, f);
      if (!topics.has(label)) topics.set(label,{id:label,label,keys:new Set(),entries:new Map()});
      const topic=topics.get(label);topic.keys.add(f.key);
      if (!topic.entries.has(id)) topic.entries.set(id,{id,label:index.name(id),keys:new Set()});
      topic.entries.get(id).keys.add(f.key);
    }
  }
  return [...topics.values()].map(t=>({...t,n:t.keys.size,entries:[...t.entries.values()].map(e=>({...e,n:e.keys.size})).sort((a,b)=>b.n-a.n||a.label.localeCompare(b.label))}))
    .sort((a,b)=>b.n-a.n||a.label.localeCompare(b.label));
}
