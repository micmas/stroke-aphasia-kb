// Navigation only: these labels never change extraction, atlas mappings or scoring.
// Broad anatomical names are not assertions of parcel equivalence.
const anatomyRules = [
  ['Frontal lobe', 'Inferior frontal gyrus — pars triangularis', /(?:ifg.*(?:triangular|45)|ba_45)/],
  ['Frontal lobe', 'Inferior frontal gyrus — pars opercularis', /(?:ifg.*opercular|ifgpo|ho-cort_44)/],
  ['Frontal lobe', 'Inferior frontal gyrus — orbital part', /ifg.*orbital/],
  ['Frontal lobe', 'Inferior frontal cortex / Broca’s area', /broca|lifc/],
  ['Frontal lobe', 'Precentral gyrus', /precentral/],
  ['Frontal lobe', 'Middle frontal gyrus', /middle_frontal/],
  ['Frontal lobe', 'Medial frontal / anterior cingulate cortex', /dacc|midline_frontal/],
  ['Temporal lobe', 'Superior temporal gyrus — posterior', /posterior_stg|posterior_superior_temporal/],
  ['Temporal lobe', 'Superior temporal gyrus', /superior_temporal|ba_22/],
  ['Temporal lobe', 'Middle temporal gyrus', /middle_temporal|mtg/],
  ['Temporal lobe', 'Anterior temporal cortex', /anterior_temporal/],
  ['Temporal lobe', 'Inferior / basal temporal cortex', /inferior_temporal|temporobasal/],
  ['Temporal lobe', 'Planum temporale / area Spt', /(?:^|_)spt(?:_|$)/],
  ['Parietal lobe', 'Angular gyrus', /angular_gyrus/],
  ['Parietal lobe', 'Supramarginal gyrus', /supramarginal/],
  ['Parietal lobe', 'Inferior parietal cortex', /inferior_parietal|lipl/],
  ['Parietal lobe', 'Precuneus', /precuneus/],
  ['Insula and opercular cortex', 'Insular cortex', /insula|spgi/],
  ['Subcortical grey matter', 'Basal ganglia / putamen', /basal_ganglia|putamen/],
  ['Subcortical grey matter', 'Thalamus', /thalami|thalamus/],
  ['White matter', 'Arcuate fasciculus', /arcuate|(?:^|_)af(?:_|$)|asaf/],
  ['White matter', 'Superior longitudinal fasciculus', /(?:^|_)slf(?:_|$)|superior_longitudinal/],
  ['White matter', 'Inferior longitudinal fasciculus', /(?:^|_)ilf(?:_|$)|inferior_longitudinal/],
  ['White matter', 'Uncinate fasciculus', /uncinate|(?:^|_)uf(?:_|$)/],
  ['White matter', 'Frontal aslant tract', /aslant/],
  ['White matter', 'Anterior thalamic radiation', /(?:^|_)atr(?:_|$)/],
  ['White matter', 'Corpus callosum — forceps', /forceps/],
  ['White matter', 'Extreme capsule', /extreme_capsule/],
  ['White matter', 'White matter — location not further grouped', /white_matter/],
];
// Finding-specific descriptions checked against saved source passages. Compound
// clusters stay compound; they are NOT split into invented parcel-level effects.
const describedClusters = {
  '@Basilakos2015/aphasia_aos_production_cluster': ['Multi-region anatomy', 'Left temporal and inferior precentral cortex — distributed cluster'],
  '@Casilio2025/aprocsa_dimension_overlap': ['Cross-region map comparisons', 'Left temporal, parietal and frontal/opercular maps — overlap comparison'],
  '@Casilio2025/aprocsa_multivariate_overlap': ['Cross-region map comparisons', 'Left Rolandic operculum and supramarginal gyrus — shared map overlap'],
};
// Anatomical descriptions taken from the saved claims, scoped to paper + entry.
// These navigation annotations remain subject to the finding's human review.
const describedAnatomy = {
  "@Casilio2025/agrammatism_motor_speech_bias_cluster": [
    "Cross-region map comparisons",
    "Left opercular, precentral and inferior parietal maps \u2014 comparison"
  ],
  "@Casilio2025/agrammatism_null_roi_predictors": [
    "Multi-region anatomy",
    "Prefrontal, temporal and remaining study ROIs"
  ],
  "@Basilakos2015/aos_motor_somatosensory_cluster": [
    "Multi-region anatomy",
    "Precentral and postcentral gyri \u2014 combined cluster"
  ],
  "@Baldo2006/category_fluency_cluster": [
    "Multi-region anatomy",
    "Posterior temporal and parietal cortex"
  ],
  "@Butler2014/delayed_non_word_repetition_cluster": [
    "Multi-region anatomy",
    "Superior/middle temporal gyri and posterior insula"
  ],
  "@Alyahya2020/executive_function_cluster": [
    "Multi-region anatomy",
    "Left frontal cortex and frontal aslant tract"
  ],
  "@Casilio2025/frontoparietal_roi": [
    "Multi-region anatomy",
    "Frontoparietal study ROI"
  ],
  "@Brownsett2014/healthy_task_intelligibility_interaction_cluster": [
    "Multi-region anatomy",
    "Left inferior/middle frontal and anterior insular cortex, dACC/SFG"
  ],
  "@Akkad2023/left_frontal_executive_cluster": [
    "Frontal lobe",
    "Left dorsolateral prefrontal and inferior frontal cortex"
  ],
  "@Breier2008/left_hemisphere_fa_comparison": [
    "White matter",
    "Left SLF, arcuate and uncinate fasciculi \u2014 comparison"
  ],
  "@Biondo2024/left_mid_posterior_temporal_ipl_cluster": [
    "Multi-region anatomy",
    "Left posterior temporal, inferior parietal and underlying white matter"
  ],
  "@Baldo2013/left_naming_network_cluster": [
    "Multi-region anatomy",
    "Left temporal, inferior parietal and underlying white matter"
  ],
  "@Akkad2023/left_parietal_phonology_cluster": [
    "Parietal lobe",
    "Left superior/inferior parietal cortex and intraparietal sulcus"
  ],
  "@Baldo2006/left_posterior_category_fluency_cluster": [
    "Multi-region anatomy",
    "Left temporal, parietal, insular cortex and putamen"
  ],
  "@Casilio2025/left_posterior_temporoparietal_cluster": [
    "Multi-region anatomy",
    "Left posterior temporal and parietal cortex"
  ],
  "@Biondo2024/left_sentence_comprehension_tract_disconnection": [
    "White matter",
    "Left temporal association pathways and callosal disconnection"
  ],
  "@Biondo2024/left_temporal_complex_sentence_cluster": [
    "Multi-region anatomy",
    "Left middle/superior temporal cortex and underlying white matter"
  ],
  "@Bi2015/left_tool_concept_tract_cluster": [
    "White matter",
    "Eight left frontal\u2013temporal/parietal pathways \u2014 combined result"
  ],
  "@Basilakos2019/lesion_volume": [
    "Global lesion measures",
    "Overall lesion volume"
  ],
  "@Baldo2006/letter_fluency_cluster": [
    "Multi-region anatomy",
    "Frontal, parietal, anterior temporal, insular cortex and putamen"
  ],
  "@Baldo2006/letter_fluency_subtraction_cluster": [
    "Multi-region anatomy",
    "Frontal, parietal, anterior temporal, insular cortex and putamen"
  ],
  "@Brownsett2014/listen_repeat_activation_cluster": [
    "Distributed functional networks",
    "Bilateral cortical, subcortical and cerebellar activation"
  ],
  "@Brownsett2014/listen_vs_repeat_activation": [
    "Distributed functional networks",
    "Listening\u2013repetition activation contrast"
  ],
  "@Casilio2025/logopenia_agrammatism_bias_cluster": [
    "Cross-region map comparisons",
    "Left inferior parietal, ventral precentral and opercular maps"
  ],
  "@Alyahya2020/motor_speech_cluster": [
    "Multi-region anatomy",
    "Sensorimotor, opercular, temporal cortex and white matter"
  ],
  "@Alyahya2018NounVerb/naming_vs_comprehension_cluster": [
    "Multi-region anatomy",
    "Left temporoparietal/frontal cortex and arcuate pathway"
  ],
  "@Alyahya2018NounVerb/noun_verb_comprehension_network": [
    "Multi-region anatomy",
    "Left temporoparietal/occipital cortex and white matter"
  ],
  "@Alyahya2018NounVerb/noun_verb_naming_overlap": [
    "Multi-region anatomy",
    "Left temporoparietal/occipital cortex and white matter"
  ],
  "@BlomSmink2020/other_language_tracts_fa_change": [
    "White matter",
    "Bilateral dorsal/ventral language tracts, excluding right ILF"
  ],
  "@Casilio2025/paraphasia_logopenia_bias_cluster": [
    "Cross-region map comparisons",
    "Left posterior temporal and supramarginal maps"
  ],
  "@Casilio2025/paraphasia_roi_nulls": [
    "Multi-region anatomy",
    "Prefrontal, frontoparietal and remaining study ROIs"
  ],
  "@Alyahya2020/phonological_production_cluster": [
    "Multi-region anatomy",
    "Parietal/opercular cortex and white-matter pathways"
  ],
  "@Alyahya2020/phonological_recognition_semantic_processing_cluster": [
    "Multi-region anatomy",
    "Left temporal/occipital cortex and ILF"
  ],
  "@Butler2014/phonology_cluster": [
    "Multi-region anatomy",
    "Left auditory/temporal cortex, posterior insula and arcuate pathway"
  ],
  "@Casilio2025/prefrontal_other_roi_logopenia": [
    "Multi-region anatomy",
    "Prefrontal and remaining study ROIs"
  ],
  "@Akkad2023/semantic_factor_cluster": [
    "Multi-region anatomy",
    "Left temporal pole, temporal gyri and insula"
  ],
  "@Butler2014/semantic_factor_cluster": [
    "Multi-region anatomy",
    "Left anterior temporal cortex and temporal stem pathways"
  ],
  "@Alyahya2020/semantic_processing_cluster": [
    "Multi-region anatomy",
    "Occipital/temporal cortex and ventral white matter"
  ],
  "@Adezati2022/sentence_comprehension_sccan_cluster": [
    "Multi-region anatomy",
    "Posterior superior temporal cortex, IFG pars triangularis and frontal white matter"
  ],
  "@Butler2014/spoken_word_to_picture_matching_cluster": [
    "Temporal lobe",
    "Left anterior temporal cortex"
  ],
  "@Cote2007/subcortical_lesion_rh": [
    "Subcortical structures",
    "Right subcortical lesions \u2014 structures not specified"
  ],
  "@Butler2014/synonym_judgement_cluster": [
    "Multi-region anatomy",
    "Lentiform nucleus/putamen and left inferior frontal white matter"
  ],
  "@Casilio2025/temporal_roi_paraphasia": [
    "Temporal lobe",
    "Temporal study ROI"
  ],
  "@Bi2015/tool_concept_vlsm_vfsm_cluster": [
    "White matter",
    "Left ATR, IFOF, SLF and uncinate \u2014 overlapping pathways"
  ],
  "@Bi2015/tool_use_concept_dissociation": [
    "White matter",
    "Tool-use and tool-concept pathways \u2014 comparison"
  ],
  "@Bi2015/tool_use_tracts": [
    "White matter",
    "Three tool-use pathways \u2014 combined result"
  ],
  "@Alyahya2018NounVerb/verb_comprehension_cluster": [
    "Multi-region anatomy",
    "Left postcentral/supramarginal cortex and anterior arcuate pathway"
  ],
  "@Alyahya2020/verbal_quality_cluster": [
    "Multi-region anatomy",
    "Left frontal, superior parietal, occipital and cingulate cortex"
  ],
  "@Alyahya2020/verbal_quantity_cluster": [
    "Multi-region anatomy",
    "Sensorimotor/inferior frontal/opercular cortex and white matter"
  ],
  "@Akkad2023/verbal_working_memory_cluster": [
    "Multi-region anatomy",
    "Left posterior temporal cortex, hippocampus and white matter"
  ],
  "@Bi2015/vfsm_tool_use_cluster": [
    "White matter",
    "Left putamen\u2013frontal white matter"
  ]
};
export function anatomicalGroup(f, id) {
  const special = describedClusters[`${f.citation}/${id}`] || describedAnatomy[`${f.citation}/${id}`];
  if (special) return special;
  const hits = anatomyRules.filter(([, , re]) => re.test(id));
  // Prefer a more precise subdivision of the same named structure.
  const names = [...new Set(hits.map(([, name]) => name))];
  if (names.includes('Superior temporal gyrus — posterior') && names.includes('Superior temporal gyrus')) names.splice(names.indexOf('Superior temporal gyrus'), 1);
  if (names.length > 1) {
    const broad = [...new Set(hits.map(([group]) => group))];
    return [broad.length === 1 ? broad[0] : 'Multi-region anatomy', `${side(id)}${names.join(' + ')} — compound region`];
  }
  if (hits.length) return [hits[0][0], `${side(id)}${hits[0][1]}`];
  if (/wernicke/.test(id)) return ['Multi-region anatomy', 'Posterior language cortex — Wernicke’s area (study-defined)'];
  if (/salience_network|dmn_/.test(id)) return ['Distributed functional networks', /dmn/.test(id) ? 'Default mode network' : 'Salience network'];
  return ['Anatomy awaiting classification', 'Anatomy awaiting classification'];
}
function side(id) { return /^left_|^lif/.test(id) ? 'Left ' : /^right_/.test(id) ? 'Right ' : /^bilateral_/.test(id) ? 'Bilateral ' : 'Side not specified — '; }

export function clinicalGroup(id) {
  const t = id.toLowerCase();
  if (/brain_|neural_|grey_matter|activity|activation|fa_values|session_effect|network/.test(t)) return ['Imaging measures', 'Imaging measures'];
  if (/aprocsa_dimensions|aprocsa_dimension_scores|aprocsa_feature|fundamental_language|language_impairment_dissociation|and_naming|naming_and_comprehension|phonological_recognition_semantic|aos_and_aphasic|paraphasia_logopenia|logopenia_agrammatism|agrammatism_motor|overall_language_and|linguistic_and_qol/.test(t)) return ['Combined domains / composite outcomes', 'Combined domains / composite outcomes'];
  if (/sentence|token_test|sequential_commands/.test(t) && !/repeat/.test(t)) return ['Language comprehension', 'Sentence comprehension'];
  if (/comprehension|word_to_picture|picture_to_word/.test(t)) return ['Language comprehension', 'Word / auditory comprehension'];
  if (/reading|alexia/.test(t)) return ['Written language', /sublexical/.test(t) ? 'Sublexical reading' : /lexical_reading/.test(t) ? 'Lexical reading' : 'Reading'];
  if (/repeat|repetition/.test(t)) return ['Repetition', /non_word|nonword/.test(t) ? 'Nonword repetition' : 'Word / sentence repetition'];
  if (/apraxia_of_speech|aos_|articulat|motor_speech|consonant/.test(t)) return ['Motor speech', /aos|apraxia/.test(t) ? 'Apraxia of speech' : 'Articulation / motor speech'];
  if (/naming|bnt_|pnt_|confrontation|picture_naming/.test(t)) return ['Word retrieval', 'Naming'];
  if (/fluency|category_member/.test(t) && !/speech_fluency|wab_fluency/.test(t)) return ['Word retrieval', /letter/.test(t) ? 'Letter fluency' : /category/.test(t) ? 'Category fluency' : 'Verbal fluency'];
  if (/semantic|synonym|tool_concept/.test(t)) return ['Semantic processing', /tool/.test(t) ? 'Tool concepts' : 'Semantic knowledge / processing'];
  if (/phonolog|phonology|paraphasia|aphasic_speech_errors/.test(t)) return ['Phonological processing', /working_memory/.test(t) ? 'Phonological working memory' : 'Phonological processing / errors'];
  if (/agrammat|morphosynt/.test(t)) return ['Speech and discourse', 'Grammar in production'];
  if (/discourse|connected_speech|cius|picture_description|lexical_diversity|word_finding_behaviors/.test(t)) return ['Speech and discourse', 'Connected speech / discourse'];
  if (/speech_|verbal_quality|verbal_quantity|logopenia|wab_fluency/.test(t)) return ['Speech and discourse', 'Speech output / fluency'];
  if (/communication|communicative|fcp_/.test(t)) return ['Functional communication', 'Everyday communication'];
  if (/executive|processing_speed|cognitive_effort/.test(t)) return ['Cognition', 'Executive function / processing speed'];
  if (/memory/.test(t)) return ['Cognition', 'Memory'];
  if (/tool_use|limb_apraxia/.test(t)) return ['Other clinical domains', 'Praxis / tool use'];
  if (/behavioral|motor_deficits/.test(t)) return ['Other clinical domains', 'Multiple behavioural / motor domains'];
  if (/recovery|outcome|gains|change|respons|treatment_success|generalization/.test(t)) return ['Overall language and recovery', 'Recovery / treatment outcomes'];
  if (/aphasia|language|wab_|pica_|aq_|comprehension_aq/.test(t)) return ['Overall language and recovery', 'Overall language / aphasia severity'];
  return ['Clinical domain awaiting classification', 'Clinical domain awaiting classification'];
}

export function groupedMatrix(index, kind, level = 'broad') {
  const rows = new Map(), cols = new Map(), cells = new Map(), labels = new Map();
  const findingKeys = new Set();
  for (const f of index.findings) {
    if (f.pair?.kind !== kind) continue;
    const {row, col} = f.pair;
    const regionRows = kind.startsWith('region-');
    const rlabel = regionRows ? anatomicalGroup(f, row)[level === 'specific' ? 1 : 0] : index.name(row);
    const clabel = kind === 'region-region' ? anatomicalGroup(f, col)[level === 'specific' ? 1 : 0] : clinicalGroup(col)[level === 'specific' ? 1 : 0];
    const r = `group:${rlabel}`, c = `group:${clabel}`;
    labels.set(r, rlabel); labels.set(c, clabel);
    rows.set(r, (rows.get(r) || 0) + 1); cols.set(c, (cols.get(c) || 0) + 1);
    const key = `${r}\0${c}`;
    if (!cells.has(key)) cells.set(key, []);
    cells.get(key).push(f); findingKeys.add(f.key);
  }
  const order = m => [...m.keys()].sort((a,b) => m.get(b)-m.get(a) || labels.get(a).localeCompare(labels.get(b)));
  return {rows:order(rows),cols:order(cols),rowTotals:rows,colTotals:cols,cells,
    cell:(r,c)=>cells.get(`${r}\0${c}`)||[],name:id=>labels.get(id)||index.name(id), total: findingKeys.size};
}
