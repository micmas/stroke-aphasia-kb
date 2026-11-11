"""Internal long-paper inventory extraction: full source coverage, independent model arms.

No summaries replace source text. Segment inventories are concatenated, never silently
merged or deduplicated; cross-segment duplicates and model attribution require review.
"""
import hashlib
import json
import time
from pathlib import Path
from extract import _extract_pdf_text
from extract_analysis_inventory import source_units, build_prompt, audit_inventory
from ollama_client import chat, autosize_num_ctx, RepetitionLoop
from strict_data import load_json


def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')


def plan_segments(units, max_chars):
    if not 10000 <= max_chars <= 100000:
        raise ValueError('segment_chars must be between 10000 and 100000')
    keys = list(units)
    groups, current, size = [], [], 0
    for key in keys:
        n = len(units[key]['text'])
        if n > max_chars: raise ValueError('A source unit exceeds the segment budget; prepare this source explicitly')
        if current and size+n > max_chars:
            groups.append(current); current=[]; size=0
        current.append(key); size+=n
    if current: groups.append(current)
    if not groups: raise ValueError('No source units')
    # Original front matter and adjacent original units provide context without summaries.
    front=[]; size=0
    for key in keys:
        if size+len(units[key]['text']) > 12000: break
        front.append(key);size+=len(units[key]['text'])
    plan=[]
    for group in groups:
        start=keys.index(group[0]); end=keys.index(group[-1])+1
        support=[k for k in keys[max(0,start-2):min(len(keys),end+2)]+front if k not in group]
        plan.append({'core_ids':group,'context_ids':list(dict.fromkeys(support))})
    return plan


def segment_prompt(units, citation, segment):
    ids=set(segment['core_ids']+segment['context_ids'])
    selected={k:v for k,v in units.items() if k in ids}
    instructions='''\nSEGMENTED MAIN-PAPER EXTRACTION. This is one segment, not the full paper.
Only inventory findings substantively reported in CORE source units. CONTEXT units
are original source text for interpretation; do not repeat findings appearing only
in context. If necessary methods, denominators or definitions are elsewhere, mark
that uncertainty rather than guessing. Do not treat references as new analyses.
For a segment with no substantive analyses/synthesis claims, return empty outcomes
and analyses arrays with an explicit coverage_notes explanation; never invent findings.
Keep every source ID unchanged. Flag cross-segment dependencies and image-only data.
CORE: '''+json.dumps(segment['core_ids'])+'\nCONTEXT: '+json.dumps(segment['context_ids'])+'\n'
    return build_prompt(selected,citation)+instructions,selected


def run_segmented(pdf, citation, output, model, max_tokens=32000, segment_chars=50000):
    output.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    meta={'status':'failed','approved':False,'model':model,'citation':citation,
          'source_scope':'main_paper_only','strategy':'complete_source_segments_v1',
          'max_output_tokens':max_tokens,'segment_chars':segment_chars,
          'temperature':0.0,'think':False,'automatic_retries':0}
    try:
        text,pages=_extract_pdf_text(pdf); units=source_units(text)
        if not any(u['text'].strip() for u in units.values()):raise ValueError('Empty source')
        plan=plan_segments(units,segment_chars)
        prompts=[segment_prompt(units,citation,s)[0] for s in plan]
        composite='\n\n'.join(f'=== SEGMENT {i+1} PROMPT ===\n{p}' for i,p in enumerate(prompts))
        (output/'prompt.txt').write_text(composite)
        meta.update(pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
                    prompt_sha256=hashlib.sha256(composite.encode()).hexdigest(),segment_count=len(plan))
        write(output/'source-units.json',units);write(output/'segment-plan.json',plan)
        combined={'citation':citation,'outcomes':[],'analyses':[],'discrepancies':[],
                  'coverage_notes':['Segmented full-main-PDF extraction. Overlap can duplicate findings; no automatic deduplication. Cross-segment model/denominator attribution requires review.']}
        empty_segments=[]
        for i,(segment,prompt) in enumerate(zip(plan,prompts),1):
            d=output/'segments'/f'{i:03d}';d.mkdir(parents=True)
            (d/'prompt.txt').write_text(prompt)
            _,subset=segment_prompt(units,citation,segment);write(d/'source-units.json',subset)
            sm={'status':'failed','approved':False,'core_ids':segment['core_ids'],'context_ids':segment['context_ids']}
            print(f'  Segment {i}/{len(plan)}: PDF pages {units[segment["core_ids"][0]]["page"]}–{units[segment["core_ids"][-1]]["page"]}',flush=True)
            try:
                response=chat(prompt,model=model,max_tokens=max_tokens,num_ctx=autosize_num_ctx(prompt,max_tokens),temperature=0.0,think=False,fmt='json',timeout=3600)
                (d/'raw.json').write_text(response['text']);sm['inference']={k:v for k,v in response.items() if k!='text'}
                if response.get('truncated_input') or response.get('truncated_output'):raise ValueError('Truncated segment; full paper remains failed')
                raw=load_json(response['text'])
                if not isinstance(raw,dict) or raw.get('citation')!=citation:raise ValueError('Invalid segment citation/object')
                for field in ['outcomes','analyses','discrepancies','coverage_notes']:
                    if not isinstance(raw.get(field),list):raise ValueError('Invalid segment '+field)
                if not raw['analyses']:
                    if not raw['coverage_notes']:raise ValueError('Empty segment lacks explanation')
                    empty_segments.append(i)
                ids=[a.get('id') for a in raw['analyses'] if isinstance(a,dict)]
                if len(ids)!=len(raw['analyses']) or any(not isinstance(x,str) or not x for x in ids) or len(set(ids))!=len(ids):raise ValueError('Invalid/duplicate segment analysis IDs')
                sm['issues']=audit_inventory(raw,subset,citation) if raw['analyses'] else ['No analyses: reviewer must verify segment exclusion']
                sm['status']='requires_review'
                for a in raw['analyses']:
                    a=dict(a);a['segment_original_id']=a['id'];a['id']=f's{i:03d}_'+a['id'];a['source_segment']=i
                    combined['analyses'].append(a)
                for name in raw['outcomes']:
                    if not isinstance(name,str):raise ValueError('Invalid outcome name')
                    if name not in combined['outcomes']:combined['outcomes'].append(name)
                combined['discrepancies'].extend(raw['discrepancies'])
                combined['coverage_notes'].extend(f'Segment {i}: {n}' for n in raw['coverage_notes'])
            except RepetitionLoop as e:
                (d/'raw.json').write_text(e.partial);sm['error']=str(e);raise
            except Exception as e:
                sm['error']=str(e);raise
            finally:write(d/'meta.json',sm)
        if not combined['analyses']:raise ValueError('No analyses in full paper; manual source check required')
        write(output/'raw.json',combined)
        issues=audit_inventory(combined,units,citation)
        meta.update(status='requires_review',issues=issues,analysis_count=len(combined['analyses']),
                    empty_segments_requiring_review=empty_segments,
                    inference={'segmented':True,'truncated_input':False,'truncated_output':False},
                    coverage={'pdf_pages':pages,'source_units':len(units),'core_units_processed':sum(len(s['core_ids']) for s in plan)})
        return 1 if issues else 0
    except Exception as e:
        meta['error']=str(e);raise
    finally:
        meta['seconds']=time.monotonic()-started;write(output/'meta.json',meta)
