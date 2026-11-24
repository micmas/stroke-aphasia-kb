import {ANATOMY, ANATOMY_GROUPS} from './topic-categories.js';
import {anatomicalGroup} from './evidence-groups.js';

// Group navigation labels; retain doses, comparisons, safety outcomes and study IDs.
export function therapyTopic(id, entry = {}) {
  const name = `${id} ${entry.name || ''}`.toLowerCase().replace(/[_–-]/g, ' ');
  if (/\bsfa\b|semantic feature analysis/.test(name)) return 'Semantic Feature Analysis';
  if (/\btdcs\b|transcranial direct current stimulation/.test(name)) return 'Brain stimulation (tDCS)';
  if (/cueing hierarchy|cueing hierarchies|word finding approach/.test(name)) return 'Word-finding and cueing approaches';
  if (/intention treatment/.test(name)) return 'Intention treatment';
  if (/treatment deferral|control treatment|verse.*uc plus/.test(name)) return 'Treatment comparisons and control conditions';
  if (/intensiv|intensity/.test(name)) return 'Speech and language therapy intensity';
  if (/functional.*pragmatic|functionally tailored/.test(name)) return 'Functional communication approaches';
  if (/auditory discrimination|vocoded speech|healthy training/.test(name)) return 'Auditory and speech-perception training';
  if (/thrombolysis/.test(name)) return 'Acute stroke treatment';
  if (/slt tailoring|mixed expressive receptive|semantic phonological recovery|behavioural therapy repetition/.test(name)) return 'Targeted language therapy';
  return entry.name || String(id).replaceAll('_', ' ');
}

export function overviewLabel(id, entry, finding) {
  if (entry.category === 'Therapies') return therapyTopic(id, entry);
  if (entry.category === ANATOMY) {
    if (entry.subcategory === ANATOMY_GROUPS[1]) return 'White-matter regions and pathways';
    const broad = anatomicalGroup(finding, id)[0];
    if (broad === 'White matter') return 'White-matter regions and pathways';
    if (['Subcortical structures','Subcortical grey matter'].includes(broad)) return 'Subcortical regions';
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
