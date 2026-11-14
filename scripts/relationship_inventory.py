"""Relationship-focused extraction contract; no inference, mapping or approval here."""
from pathlib import Path
import re

VERSION = 'relationships-v1'
PROMPT = Path(__file__).with_name('relationship_prompt.txt')
KINDS = {'imaging', 'personal', 'clinical', 'intervention', 'context'}
ROLES = {'tested_predictor', 'candidate_predictor', 'joint_model_feature', 'adjustment_only',
         'effect_modifier', 'mediator', 'eligibility', 'descriptive', 'matching'}
RELATIONS = {'association', 'longitudinal_prediction', 'contemporaneous_prediction',
             'treatment_effect', 'treatment_response_association', 'effect_modification',
             'mediation', 'group_difference', 'descriptive', 'synthesis', 'hypothesis'}


def build_prompt(units, citation):
    from relationship_context import _eligible_units
    units = _eligible_units(units)
    source = '\n\n'.join(f'[{key}; PDF page {v["page"]}]\n{v["text"]}'
                         for key, v in units.items())
    return PROMPT.read_text().replace('{{CITATION}}', citation).replace('{{SOURCE}}', source)


def review_checklist(result, units):
    """Surface source passages independently of the model's completeness claim.

    These lexical cues may include background or methods: a reviewer must decide
    relevance. Even a cited unit does not prove that every relationship in it was
    captured. Never mark a passage covered automatically.
    """
    factor = re.compile(r'\b(age|gender|sex|education|handedness|severity|baseline|time post[- ](?:onset|stroke))\b', re.I)
    finding = re.compile(r'associat|correlat|significan|difference|predict|higher|lower|related', re.I)
    null = re.compile(r'no (?:significant |detectable )?(?:association|relationship|correlation)|not significant|did not', re.I)
    rows = []
    for key, unit in units.items():
        text = unit['text']
        if re.search(r'^\s*references\s*$', text, re.I | re.M):
            break
        cues = []
        for match in factor.finditer(text):
            if finding.search(text[max(0,match.start()-180):match.end()+400]):
                cues.append('personal_or_clinical_factor_passage'); break
        if null.search(text):
            cues.append('null_or_qualification_passage')
        if not cues: continue
        analyses = result.get('analyses')
        cited = []
        for a in analyses if isinstance(analyses, list) else []:
            passages = a.get('evidence') if isinstance(a, dict) else None
            if isinstance(passages, list) and any(isinstance(e, dict) and e.get('source_id') == key for e in passages):
                cited.append(a.get('id'))
        rows.append({'source_id':key, 'pdf_page':unit['page'], 'cues':cues,
                     'analyses_citing_unit':cited, 'status':'source_review_required',
                     'note':'A citation to this unit does not establish capture of every factor or null finding.'})
    return rows


def audit(result, units):
    """Structural/role guards only; passing does not establish semantic accuracy."""
    if result.get('schema_version') == 'relationships-v2':
        return audit_compact(result, units)
    from quote_check import PaperText, grade_quote
    issues = []

    def evidence(items, label):
        if not isinstance(items, list) or not items:
            issues.append(f'{label}: source evidence required')
            return
        for item in items:
            if not isinstance(item, dict):
                issues.append(f'{label}: invalid evidence'); continue
            unit = units.get(item.get('source_id')) if isinstance(item.get('source_id'), str) else None
            quote = item.get('quote')
            if not unit or not isinstance(quote, str) or not quote.strip() or grade_quote(quote, PaperText.from_text(unit['text'])) != 'exact':
                issues.append(f'{label}: evidence not exact in declared source')

    if result.get('schema_version') != VERSION:
        issues.append('relationship schema version missing or changed')
    if result.get('approved') is not False:
        issues.append('relationship extraction must be explicitly unapproved')
    study = result.get('study')
    if not isinstance(study, dict):
        issues.append('study context required')
    else:
        for field in ['design', 'population', 'sample', 'timing', 'setting', 'eligibility', 'limitations']:
            if not isinstance(study.get(field), str) or not study[field].strip():
                issues.append(f'study: {field} required (not_reported allowed)')
        evidence(study.get('evidence'), 'study')
    analyses = result.get('analyses', [])
    if not isinstance(analyses, list):
        return issues + ['analyses must be a list']
    ids = {a.get('id') for a in analyses if isinstance(a, dict) and isinstance(a.get('id'), str)}
    for row in analyses:
        if not isinstance(row, dict): continue
        label = str(row.get('id', '?'))
        if row.get('relationship_type') not in RELATIONS:
            issues.append(f'{label}: invalid relationship_type')
        if row.get('evidence_origin') not in {'current_study', 'secondary_synthesis', 'author_hypothesis'}:
            issues.append(f'{label}: evidence_origin required')
        if not isinstance(row.get('applicability'), str) or not row['applicability'].strip():
            issues.append(f'{label}: applicability required')
        factors = row.get('factors')
        if not isinstance(factors, list) or not factors:
            issues.append(f'{label}: factors required'); factors = []
        focal = []
        for factor in factors:
            if not isinstance(factor, dict):
                issues.append(f'{label}: invalid factor'); continue
            if factor.get('kind') not in KINDS or factor.get('role') not in ROLES:
                issues.append(f'{label}: invalid factor kind/role')
            if not isinstance(factor.get('name'), str) or not factor['name'].strip():
                issues.append(f'{label}: factor name required')
            if factor.get('role') in {'tested_predictor', 'joint_model_feature', 'effect_modifier', 'mediator'}:
                focal.append(factor)
            if row.get('relationship_type') in {'contemporaneous_prediction', 'longitudinal_prediction'} and factor.get('role') == 'tested_predictor':
                issues.append(f'{label}: prediction input needs joint-feature versus independent-effect source review')
            evidence(factor.get('evidence'), f'{label} factor {factor.get("name")}')
            if factor.get('kind') == 'imaging':
                for field in ['measurement', 'hemisphere', 'spatial_reference', 'mapping_basis']:
                    if not isinstance(factor.get(field), str) or not factor[field].strip():
                        issues.append(f'{label}: imaging {field} required')
                if factor.get('mapping_basis') not in {'directly_measured', 'lesion_atlas_overlap',
                        'normative_connectome_inferred', 'model_derived', 'not_reported'}:
                    issues.append(f'{label}: imaging mapping cannot be invented by extractor')
        if not focal and row.get('relationship_type') not in {'descriptive', 'synthesis', 'hypothesis'}:
            issues.append(f'{label}: no tested/joint/modifier/mediator factor; context alone is not a finding')
        if row.get('result_status') not in {'association_detected', 'predictive_performance', 'not_detected', 'mixed',
                'trend_only', 'descriptive', 'hypothesis', 'unclear'}:
            issues.append(f'{label}: result_status required')
        if not isinstance(row.get('scope_limits'), list) or not row['scope_limits']:
            issues.append(f'{label}: scope_limits required')
        if row.get('relationship_type') in {'contemporaneous_prediction', 'longitudinal_prediction'}:
            validation = row.get('validation')
            if not isinstance(validation, dict):
                issues.append(f'{label}: prediction validation scope required')
            else:
                for field in ['design', 'training_population', 'evaluation_population', 'participant_overlap', 'feature_selection_scope']:
                    if not isinstance(validation.get(field), str) or not validation[field].strip():
                        issues.append(f'{label}: validation {field} required')
                evidence(validation.get('evidence'), f'{label} validation')
        if row.get('interpretation'):
            issues.append(f'{label}: free-form clinical interpretation is outside extraction; source review required')
    coverage = result.get('relationship_coverage')
    if not isinstance(coverage, list) or not coverage:
        issues.append('relationship coverage required')
    else:
        covered = set()
        for item in coverage:
            if not isinstance(item, dict):
                issues.append('invalid coverage item'); continue
            refs = item.get('analysis_ids')
            if not isinstance(refs, list) or any(not isinstance(x, str) or x not in ids for x in refs):
                issues.append('coverage refers to unknown analysis'); continue
            covered.update(refs)
            if item.get('status') not in {'captured', 'null_summary', 'unresolved', 'context_only'}:
                issues.append('invalid coverage status')
            if item.get('status') in {'captured', 'null_summary'} and not refs:
                issues.append('captured coverage has no linked relationship')
            if not isinstance(item.get('source_id'), str) or item['source_id'] not in units:
                issues.append('coverage source_id missing or unknown')
            if not isinstance(item.get('reason'), str) or not item['reason'].strip():
                issues.append('coverage reason required')
        if ids - covered:
            issues.append('relationships missing from coverage ledger: ' + ', '.join(sorted(ids-covered)))
    return issues


def audit_focused_pass(result, units, stage):
    """Check scoped source selections without rewriting or approving model output.

    These are targeted review flags, not a semantic validator. In particular,
    two independently stated nulls may legitimately share the same quote/p value.
    Context exclusions remain visible even when another model selected them.
    """
    from quote_check import PaperText, grade_quote
    from annotate_paper import _normalize
    flags = []

    def flag(path, reason):
        flags.append({'path': path, 'reason': reason, 'status': 'needs_source_resolution'})

    if not isinstance(result, dict):
        flag('', 'Expected a source-pass object')
        return flags
    if stage == 'context':
        required = re.compile(r'\brepeat\w*\b|more than once|\brecords\b|\btrained\b|'
                              r'cross.validation|\bvalidation\b|leave.one.out|\bremaining\b|'
                              r'\beliminated\b|\bn\s*=', re.I)
        seen = set()
        for group in ('selected', 'excluded'):
            for i, row in enumerate(result.get(group, [])):
                path = f'{group}.{i}'
                source_id = row.get('source_id')
                if source_id not in units:
                    flag(path, 'Unknown source selection')
                    continue
                if source_id in seen:
                    flag(path, 'Source selected or excluded more than once')
                seen.add(source_id)
                text = units[source_id]['text']
                if group == 'excluded' and required.search(text):
                    flag(path, 'Excluded passage may define sample, timing or validation; retain for review')
                if group == 'selected' and row.get('scope') == 'database_or_registry' and re.search(
                        r'limitations of the current study|criticism of the system', text, re.I):
                    flag(path, 'Discussion statement classified as database scope; check against eligibility')
        for source_id in units.keys() - seen:
            flag(source_id, 'Source passage has no disposition')
        return flags
    if stage != 'factors':
        raise ValueError('Unknown focused extraction stage')

    factor_names = {
        'age': r'\bage\b|\bages\b',
        'sex_or_gender': r'\b(?:sex|gender|females?|males?|women|men)\b',
        'time_since_stroke': r'time.{0,35}(?:stroke|onset)|post.stroke|post.onset',
        'lesion_burden': r'lesion (?:volume|size)|lateralised (?:lesion|volume)|lateralized (?:lesion|volume)',
        'severity': r'severity|baseline (?:score|performance|language)',
        'education': r'educat', 'handedness': r'handed',
        'language_background': r'first language|native.like|bilingual|multilingual|language proficiency',
        'head_size_or_tiv': r'intracranial|\bTIV\b|head size',
        'cognition': r'cognit|semantic|Pyramids|\bPPT\b', 'comorbidity': r'comorbid|neurological condition',
        'treatment': r'treatment|therap', 'dose': r'\bdose\b|dosage|intensity',
        'site': r'recruitment site|study site',
    }
    anatomy = re.compile(r'\bAF\b|HMOA|fascicul|\bgyrus\b|\bgyri\b|\btract\b|\bsegment\b|'
                         r'frontal|temporal|parietal|atlas|\bregion\b|lesion load|cortex', re.I)
    seen = set()
    for i, row in enumerate(result.get('dispositions', [])):
        source_id = row.get('source_id')
        if source_id not in units or source_id in seen:
            flag(f'dispositions.{i}', 'Unknown or duplicate source disposition')
        seen.add(source_id)
    for source_id in units.keys() - seen:
        flag(source_id, 'Factor source passage has no disposition')
    for group in ('roles', 'findings'):
        for i, row in enumerate(result.get(group, [])):
            path = f'{group}.{i}'
            evidence = row.get('evidence') or []
            if not evidence:
                flag(path, 'Missing source evidence')
            for item in evidence:
                unit = units.get(item.get('source_id'), {})
                if grade_quote(item.get('quote', ''), PaperText.from_text(unit.get('text', ''))) not in {'exact', 'elided'}:
                    flag(path, 'Quote is not exact in its declared source')
            quote = ' '.join(_normalize(e.get('quote', '')) for e in evidence)
            if group == 'roles':
                factor = row.get('factor', '')
                category = row.get('factor_group')
                pattern = factor_names.get(category)
                if pattern and not re.search(pattern, factor, re.I):
                    flag(path, 'Role name does not establish its canonical factor category')
                scope = row.get('analysis_scope', '')
                families = [r'\bVBM\b|voxel.based morphometry', r'\bVLSM\b|voxel.based lesion',
                            r'connectom', r'\bTBSS\b', r'tractograph', r'lesion.load']
                if sum(bool(re.search(x, scope, re.I)) for x in families) > 1 or re.search(r'models?\s*\d\s*[-–—]\s*\d', scope, re.I):
                    flag(path, 'Role spans different analyses; verify controls separately')
                if row.get('role') in {'adjustment_only', 'joint_model_input', 'selected_model_input'}:
                    source_text = ' '.join(units.get(e.get('source_id'), {}).get('text', '') for e in evidence)
                    if re.search(r'not.{0,45}(?:includ|adjust|control|covariat)|without.{0,25}(?:adjust|control|covariat)', source_text, re.I):
                        flag(path, 'Source contains explicit non-adjustment; check claimed role and analysis scope')
                    if re.search(r'(?:the|this) analysis', quote, re.I) and not any(re.search(x, quote, re.I) for x in families):
                        flag(path, 'Generic analysis reference needs its assigning Methods context')
                if anatomy.search(row.get('factor', '')):
                    flag(path, 'Regional anatomy entered as a personal/global lesion factor')
                if row.get('role') == 'joint_model_input' and re.search(r'partial|correlational', row.get('analysis_scope', ''), re.I) and re.search(r'covariate|control|adjust', quote, re.I):
                    flag(path, 'Adjustment may have been labelled as a joint prediction input')
                if row.get('role') == 'adjustment_only' and re.search(r'matching|matched', row.get('analysis_scope', ''), re.I):
                    flag(path, 'Matching and statistical adjustment need separate analysis scopes')
                if row.get('role') == 'selected_model_input' and not re.search(r'ARD|automatic relevance|stepwise|lasso|feature.selection|best subset', quote, re.I):
                    flag(path, 'Selected-input role needs its feature-selection methods evidence')
                continue
            for factor in row.get('factors', []):
                pattern = factor_names.get(factor)
                if pattern and not re.search(pattern, quote, re.I):
                    flag(path, 'Factor identity is not established by its quoted evidence: ' + factor)
            if len(row.get('factors', [])) != 1:
                flag(path, 'Individual finding must identify exactly one factor')
            if re.search(r'R[²2]|AUC|area under|predictive accuracy', quote, re.I):
                flag(path, 'Whole-model performance appears in an individual-factor finding')
            if re.search(r'feature.selection|ARD|relevance|best subset|selected|configuration', row.get('analysis_scope', '') + ' ' + quote, re.I):
                flag(path, 'Feature selection or configuration is not an individual effect')
            direction = row.get('direction')
            cues = {'positive': r'positiv|increase|higher|greater',
                    'negative': r'negativ|decrease|lower|less',
                    'higher': r'higher|greater|better', 'lower': r'lower|less|worse'}
            if direction in cues and not re.search(cues[direction], quote, re.I):
                flag(path, 'Direction is not explicitly supported by the evidence')
            if direction in cues and ';' in row.get('outcome', '') and ';' in quote:
                flag(path, 'Separate outcome clauses before assigning a common direction')
            statistic = row.get('statistic_as_printed', 'not_reported')
            if statistic != 'not_reported' and not any(grade_quote(statistic, PaperText.from_text(e.get('quote', ''))) == 'exact' for e in evidence):
                flag(path, 'Statistic not found in the supporting quote')
            correction = row.get('correction')
            if correction not in {None, '', 'not_reported'} and str(correction).casefold() not in quote.casefold():
                flag(path, 'Correction needs explicit supporting methods evidence')
    return flags


def audit_compact(result, units):
    """Validate compact references and evidence. This does not certify findings."""
    import jsonschema
    from quote_check import PaperText, grade_quote
    def obj(fields):
        return {'type': 'object', 'properties': fields, 'required': list(fields), 'additionalProperties': False}
    def arr(item): return {'type': 'array', 'items': item}
    def enum(*items): return {'type': 'string', 'enum': list(items)}
    string = {'type': 'string', 'minLength': 1}
    ids = arr(string)
    evidence = arr(obj({'source_id': string, 'quote': string}))
    feature = obj(dict(id=string, name=string, kind=enum(*sorted(KINDS)), measurement=string,
        hemisphere=string, measurement_source=string, region_definition=string, spatial_reference=string, mapping_basis=enum('directly_measured',
        'lesion_atlas_overlap', 'normative_connectome_inferred', 'model_derived', 'not_reported'), evidence=evidence))
    finding = obj(dict(id=string, feature_ids=ids, outcomes=ids, context_source_ids=ids,
        outcome_timing=enum('current_level','later_level','change','not_reported'),
        effect_unit=enum('individual_feature','joint_model','added_feature_set','group_comparison','descriptive','selected_feature_rank'),
        comparison=string, status=enum('detected','not_detected','trend','performance','descriptive','unclear'),
        direction=enum('positive','negative','higher','lower','not_detected','not_applicable','not_reported','mixed'),
        correction=string, estimates=arr(obj(dict(feature_ids=ids,outcome=string,statistic=string,value=string,p=string,uncertainty=string))),
        evidence=evidence,table_locator=string))
    analysis = obj(dict(id=string,method=string,relationship_type=enum(*sorted(RELATIONS)),
        evidence_origin=enum('current_study','secondary_synthesis','author_hypothesis'),
        context_source_ids=ids,inputs=ids,adjustments=ids,explicit_non_adjustments=ids,evidence=evidence,
        validation=obj(dict(design=enum('in_sample','cross_validation','independent_external','repeated_patients','not_applicable','not_reported'),
            training_source_ids=ids,evaluation_source_ids=ids,overlap_source_ids=ids,selection_source_ids=ids)),
        results=arr(finding),scope_limits=evidence))
    spec = obj(dict(schema_version=enum('relationships-v2'),citation=string,approved={'const':False},
        features=arr(feature),analyses=arr(analysis),unresolved=arr(obj(dict(source_ids=ids,reason=string)))))
    errors = list(jsonschema.Draft202012Validator(spec).iter_errors(result))
    issues = ['.'.join(map(str,e.path))+': '+e.message for e in errors]
    if errors:
        return issues
    features = {f['id']: f for f in result['features']}
    if len(features) != len(result['features']): issues.append('Duplicate feature IDs')
    analysis_ids = [a['id'] for a in result['analyses']]
    if len(set(analysis_ids)) != len(analysis_ids): issues.append('Duplicate analysis IDs')
    if not analysis_ids: issues.append('No analyses extracted; source review required')
    cited = set()
    result_ids = set()
    def source_ids(items, label):
        for key in items:
            if key not in units: issues.append(f'{label}: unknown source ID {key}')
    def check_evidence(items, label, required=True):
        if required and not items: issues.append(f'{label}: evidence required')
        for item in items:
            source_ids([item['source_id']], label)
            unit = units.get(item['source_id'])
            if unit and grade_quote(item['quote'], PaperText.from_text(unit['text'])) != 'exact':
                issues.append(f'{label}: quote not exact in declared source')
    def refs(items, label):
        for key in items:
            if key not in features: issues.append(f'{label}: unknown feature ID {key}')
    for f in features.values():
        check_evidence(f['evidence'], f['id'])
        if re.search(r'volume', f['measurement'], re.I) and re.search(r'\bHMOA\b|\bFA\b|diffus', f['measurement'], re.I):
            issues.append(f'{f["id"]}: distinct imaging measurements combined in one feature')
    for a in result['analyses']:
        label = a['id']
        check_evidence(a['evidence'], label)
        source_ids(a['context_source_ids'], label)
        check_evidence(a['scope_limits'], label+' limitations', required=False)
        for key in ('inputs','adjustments','explicit_non_adjustments'): refs(a[key], label)
        if set(a['adjustments']) & set(a['explicit_non_adjustments']):
            issues.append(f'{label}: same feature adjusted and explicitly not adjusted')
        v = a['validation']
        for key,value in v.items():
            if key.endswith('_source_ids'): source_ids(value, label+' validation')
        if (v['design'] == 'cross_validation' or re.search(r'cross.validation|leave.one.out',a['method'],re.I)) and a['relationship_type'] == 'association':
            issues.append(f'{label}: cross-validated prediction labelled association')
        if a['relationship_type'] in {'longitudinal_prediction','contemporaneous_prediction'}:
            for key in a['inputs']:
                f = features.get(key, {})
                if re.search(r'baseline|initial assessment|earlier assessment',f.get('name',''),re.I):
                    issues.append(f'{label}: baseline/earlier assessment input requires explicit predictor evidence, not training-label evidence')
            if not v['training_source_ids'] or not v['evaluation_source_ids']:
                issues.append(f'{label}: prediction training/evaluation evidence missing')
        if not a['results']: issues.append(f'{label}: no results')
        for r in a['results']:
            label_r = label+'/'+r['id']
            if r['id'] in result_ids: issues.append(f'{label_r}: duplicate result ID')
            result_ids.add(r['id'])
            refs(r['feature_ids'],label_r)
            source_ids(r['context_source_ids'],label_r+' subset')
            for estimate in r['estimates']:
                refs(estimate['feature_ids'],label_r+' estimate')
                if estimate['outcome'] not in r['outcomes']:
                    issues.append(f'{label_r}: estimate outcome outside result scope')
            if any(outcome in features for outcome in r['outcomes']):
                issues.append(f'{label_r}: outcome must be named, not a feature ID')
            if not r['outcomes']: issues.append(f'{label_r}: missing outcome')
            table = r['table_locator'] not in {'not_applicable','not_reported'}
            check_evidence(r['evidence'],label_r,required=not table)
            cited.update(e['source_id'] for e in r['evidence'])
            if table:
                if not re.search(r'table\s*\d',r['table_locator'],re.I) or not re.search(r'(?:page\s*|\bP)\d',r['table_locator'],re.I):
                    issues.append(f'{label_r}: incomplete table locator')
            if r['effect_unit'] in {'joint_model','added_feature_set'} and r['direction'] != 'not_applicable':
                issues.append(f'{label_r}: joint performance cannot establish an individual effect direction')
            if r['effect_unit'] == 'individual_feature' and len(r['feature_ids']) != 1:
                issues.append(f'{label_r}: individual effect has multiple/absent features')
    for item in result['unresolved']: source_ids(item['source_ids'],'unresolved')
    # Independently surface performance passages; never trust a self-rated ledger.
    for key, unit in units.items():
        if re.search(r'^\s*references\s*$',unit['text'],re.I|re.M): break
        if re.search(r'\bAUC\b|area under.{0,30}curve|\bROC\b',unit['text'],re.I) and key not in cited:
            issues.append(f'{key}: ROC/AUC source passage not cited by a result; check completeness')
    return issues
