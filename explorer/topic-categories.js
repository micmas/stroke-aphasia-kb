// Browsing taxonomy only. Never changes extraction files, concept IDs or atlas mappings.
export const ANATOMY = 'Brain regions and pathways';
export const FACTORS = 'Clinical and imaging factors';
export const ANATOMY_GROUPS = ['Grey-matter regions', 'White-matter regions and pathways', 'Mixed or distributed regions', 'Anatomical definition to check'];
export const FACTOR_GROUPS = ['Personal characteristics', 'Clinical characteristics', 'Lesion and imaging measures'];
const grey = new Set(['brocas_area','left_spgi','superior_tip_precentral_gyrus_insula','mtg_cluster','anterior_insula','left_angular_gyrus','left_ifg_pars_opercularis','left_ifg_pars_triangularis','left_middle_temporal_gyrus','wernickes_area','ifgpo','insula','left_insula','left_insular_precentral_gyrus_cluster','temporobasal_cluster']);
const white = new Set(['posterior_bottleneck_cluster','anterior_bottleneck_cluster','left_frontal_white_matter_bottleneck','left_slf','arcuate_fasciculus','left_arcuate_fasciculus','dorsal_white_matter_pathways','ventral_white_matter_pathways','medial_lemniscus']);
const distributed = new Set(['frontoparietal_roi','semantic_factor_cluster','perisylvian_language_network_cluster','salience_network']);
export function topicCategory(id, entry = {}, kind = '', presentation = null) {
  const name = String(id || '').toLowerCase();
  const personal = /^(age|sex|gender|education|handedness)(_|$)/.test(name);
  const clinical = /^(initial_(?:aphasia_)?severity|baseline_(?:aphasia_)?severity|stroke_severity|time_post_onset|chronicity)(_|$)/.test(name);
  const measure = /^(?:(?:total|overall)_)?lesion_(?:volume|size)(_|$)/.test(name)
    || /(?:_lesion_load|_lesion_percentage|_injury_volume|_fa(?:_change)?|_md|_volume)$/.test(name);
  if (personal || clinical || measure || ['predictor','personal_factor'].includes(kind) || entry.bucket === 'predictors') {
    const subcategory = personal || (kind === 'personal_factor' && !/time|chronicity|enroll?ment/.test(name)) ? FACTOR_GROUPS[0]
      : measure || (!clinical && entry.predictor_type === 'imaging_metric') ? FACTOR_GROUPS[2] : FACTOR_GROUPS[1];
    return {category: FACTORS, subcategory};
  }
  if (kind === 'region' || entry.bucket === 'regions') {
    let subcategory = ANATOMY_GROUPS[3];
    if (white.has(name) || entry.kind === 'tract') subcategory = ANATOMY_GROUPS[1];
    else if (grey.has(name)) subcategory = ANATOMY_GROUPS[0];
    else if (distributed.has(name)) subcategory = ANATOMY_GROUPS[2];
    return {category: ANATOMY, subcategory};
  }
  return {category: ({impairment:'Language difficulties',therapy:'Therapies',prognosis:'Outcomes',ingredient:'Treatment ingredients'})[kind] || kind || 'Other', subcategory: 'Not applicable'};
}
