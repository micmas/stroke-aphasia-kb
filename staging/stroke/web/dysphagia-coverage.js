import {renderImportCoverage} from './chapter-coverage.js';
const DATABASES = {
  pubmed: 'PubMed', scopus: 'Scopus', psycinfo: 'PsycINFO', embase: 'Embase',
  cinahl: 'CINAHL', wos: 'Web of Science', central: 'CENTRAL', cdsr: 'Cochrane Reviews (CDSR)',
};
export function renderDysphagiaCoverage(manifest, prismaDiagram) {
  return renderImportCoverage(manifest, prismaDiagram, {
    databases: DATABASES,
    searchHref: '/dysphagia/search/',
    reviewHref: '/dysphagia/screening/',
    collectionName: 'Dysphagia',
    gapText: 'Coverage by brain region, swallowing impairment, treatment and recovery predictor will appear after included studies have been extracted and reviewed.',
    auditNotes: ['The CENTRAL export has “cdsr” in its filename. Its folder and CN accession numbers identify it as CENTRAL; the original filename is retained.'],
  });
}
