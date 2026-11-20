// Presentation only: conservative reading guidance from saved extraction fields.
// No clinical diagnosis, new source claim, atlas correspondence or numerical prediction.
export const CONTEXT_VERSION = 'clinical-context-v1';
const text = v => typeof v === 'string' ? v.trim() : '';
const label = (kb, id) => kb.entries?.[id]?.name || String(id || 'the measured outcome').replaceAll('_', ' ');
export function clinicalContext(f, kb = {}) {
  if (!(f.flags || []).includes('core_profile_machine_prepared')) return null;
  const unit = f.source_check?.analysis_identity || {};
  const exposure = text(unit.exposure?.text) || label(kb, f.source_id);
  const outcome = text(unit.outcome?.text) || label(kb, f.target);
  const methods = Array.isArray(f.method) ? f.method : [f.method];
  const notes = text(f.notes).split('Additional metadata has not been transcribed')[0];
  const content = [exposure, f.claim, notes].join(' ');
  const measurement = notes.replace(/^Exposure measurement:\s*/, '').trim();
  const featureText = exposure + ' ' + measurement.split(/[.!?](?:\s|$)/)[0];
  const status = f.source_check?.core_review?.result_status;
  const personal = /\b(age|aged|sex|gender|chronicity|enrollment|enrolment|time since|time post|time from)\b/i.test(exposure);
  const spatialMethod = ['VBM','VBCM','VLSM','LSM','DTI','NODDI','tractography','fMRI_activation','fMRI_connectivity','rsfMRI'].some(m => methods.includes(m));
  const materials = !spatialMethod && /\b(noun|verb|imageability|word class|psycholinguistic|word frequency|age.of.acquisition)\b/i.test(exposure);
  const behavioral = methods.includes('behavioral_only');
  const imaging = !behavioral && !materials && (!personal || /\b(lesion|connectom|tract|grey matter|gray matter|activation)\b/i.test(exposure)) &&
    (['VBM','VBCM','VLSM','LSM','DTI','NODDI','tractography','fMRI_activation','fMRI_connectivity','rsfMRI','MVPA'].some(m => methods.includes(m)) || /\b(lesion|connectome|tractography|connectivity|grey matter|gray matter|fMRI)\b/i.test(exposure));
  const prediction = /\b(SVM|random forest|classifier|machine.learning)\b/i.test(content) && /\b(performance|predict|classification|accuracy|F1)\b/i.test(content);
  let match, category;
  if (prediction) {
    category = 'Prediction model';
    match = 'Requires the complete feature set, preprocessing and fitted model—not just one overlapping lesion or an individual tract measure. A performance result is not a ready-to-use patient prediction.';
  } else if (!imaging) {
    category = personal && !materials ? 'Personal or timing factor' : materials ? 'Assessment or task factor' : 'Clinical or behavioural factor';
    match = 'Relates to patient characteristics, timing or assessment information, rather than a particular lesion location or tract.';
  } else if (/template|reference tract|population tract|normative/i.test(featureText)) {
    category = 'Lesion overlap with a reference network';
    match = 'Compare the patient’s lesion mask with the same reference tract or network definition and overlap measure. This is not interchangeable with a tract measured in that patient or a generic disconnectome probability.';
  } else if (/\bgraph\b|efficiency|transitivity|clustering coefficient|path length/i.test(featureText)) {
    category = 'Network graph measure';
    match = 'Requires the same graph metric, network extent and connectivity construction. Diffusion-derived and lesion-estimated networks, whole-brain and language-only networks, and individual tract measures are not interchangeable.';
  } else if (/diffusion|tractography|\bDTI\b|\bNODDI\b/i.test(methods.join(' '))) {
    category = 'Patient diffusion or tract measure';
    match = 'Compare the same tract and diffusion/connectivity measure, with compatible processing and sampling. Lesion overlap alone does not reproduce this measurement.';
  } else if (/fMRI|activation|functional/i.test(methods.join(' '))) {
    category = 'Functional imaging';
    match = 'Requires a comparable task or resting-state measure, contrast/network definition and processing. Structural lesion overlap alone is not a match.';
  } else if (/total.*lesion|overall.*lesion|lesion volume/i.test(exposure)) {
    category = 'Lesion volume';
    match = 'Use total lesion volume in compatible units with a comparable segmentation method. A particular lesion location or a tract-disconnection score is a different feature.';
  } else if (/VBCM|VBM/.test(methods.join(' '))) {
    category = 'Voxelwise tissue or lesion measure';
    match = 'Anatomical overlap can identify potentially relevant literature, but the voxelwise tissue/lesion measure and study-defined cluster must be checked. A named atlas ROI or a tract label is not automatically the measured feature.';
  } else {
    category = 'Lesion location or regional load';
    match = 'Check the actual study region/cluster, reference space and lesion-load definition. A similarly named parcel in another atlas establishes a possible match, not an equivalent one.';
  }
  let relevance;
  if (status === 'lost_after_adjustment') {
    relevance = `This result limits the independence of the reported relationship with ${outcome}: the association was lost after the stated adjustment. Preserve that adjustment when considering its relevance to a patient.`;
  } else if (f.direction === 'no_effect') {
    relevance = `This analysis did not establish the reported association or difference for ${outcome}. It provides a limit on the evidence for this particular feature or comparison, rather than reassurance that an individual’s function is preserved.`;
  } else if (f.direction === 'mixed') {
    relevance = `The evidence concerning ${outcome} is mixed or conditional. Keep the analysis-specific qualifications visible; it does not support a single general conclusion for a patient.`;
  } else if (prediction) {
    relevance = `This result concerns prediction of ${outcome} by a particular model. Its usefulness depends on the full model and validation population; it does not establish that every included feature independently predicts the outcome.`;
  } else if (materials) {
    relevance = `This finding helps interpret ${outcome} in relation to the assessment materials or language construct. Check those conditions before attributing a score difference to a lesion location or to a specific language deficit.`;
  } else if (personal && !imaging) {
    relevance = `This finding supplies context for ${outcome} in relation to patient characteristics or timing. It does not localise a lesion or establish an individual recovery ceiling. Differences between age or enrollment-time groups do not by themselves establish effects of treatment timing.`;
  } else if (imaging) {
    relevance = `This is potentially relevant literature when discussing ${outcome} alongside a comparable imaging feature. Use the reported direction and qualifications together with the patient’s clinical assessment; anatomical overlap alone does not determine the presence or severity of a deficit.`;
  } else {
    relevance = `This result can help interpret ${outcome} in its recorded clinical or assessment context. It does not by itself establish a lesion-to-symptom mapping.`;
  }
  const limits = [];
  if (f.direction === 'no_effect') limits.push('Failure to detect an association or difference is not proof of equivalence or absence of a relationship.');
  if (/PCA|principal component|latent factor/i.test(content)) limits.push('The study’s composite/PCA factor is not automatically interchangeable with a single clinical test or an everyday functional ability.');
  if (/relaxed|reduced.*significance|only reached|only.*threshold/i.test(notes)) limits.push('The saved qualifications describe threshold or adjustment sensitivity; use the qualified result rather than an unqualified positive association.');
  if (prediction) limits.push('Internal validation alone does not establish performance in a new patient population.');
  const reviewNotes = [];
  if ((f.flags || []).some(x => /not_transcribed:(region_definition|imaging_details)/.test(x)) && imaging) reviewNotes.push('Imaging definition/atlas metadata are still pending. An exact scan-feature match has not been verified.');
  return { version: CONTEXT_VERSION, origin: 'rule_based_saved_evidence', review_status: 'unreviewed',
    relevance, applies_to: match, limits: limits.join(' '), category, feature: exposure, outcome,
    recorded_measurement: measurement, match_status: imaging || prediction ? 'requires_feature_verification' : 'no_direct_imaging_match',
    review_notes: reviewNotes, basis: { source_path: f.source_path, finding_id: f.id, citation: f.citation,
      pages: [...new Set((f.source_passages || []).map(p => p.page).filter(p => p != null))] } };
}
