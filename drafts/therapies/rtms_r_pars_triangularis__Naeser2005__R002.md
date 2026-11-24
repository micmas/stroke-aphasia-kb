---
id: rtms_r_pars_triangularis
name: 1 Hz rTMS to R pars triangularis
kind: therapy
findings:
- id: f1
  target: picture_naming
  target_kind: impairment
  claim: Application of 1 Hz rTMS to the right pars triangularis significantly improved
    picture naming on the BNT (first 20 items) and BDAE (Animal and Tools/Implements
    subtests) at 2 months post-treatment, with the Tools/Implements naming improvement
    remaining significant at 8 months.
  direction: likely
  relationship: treatment_response
  method: TMS
  sample:
    n: 4
    population: Right-handed chronic aphasia patients (5-11 years post-left middle
      cerebral artery stroke)
    phase: not_reported
    time_post_onset: Measured at baseline, 2 weeks, 2 months, and 8 months post-10th
      rTMS treatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Open-protocol study without a sham rTMS control group
  - Small sample size (N=4)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Daily application of 1 Hz repetitive transcranial
    magnetic stimulation (1200 pulses, 20 min) for 10 treatments over 2 weeks to the
    right pars triangularis (defined as the gyrus immediately rostral to the anterior
    ascending ramus of the Sylvian fissure), guided by 3D MPRAGE MRI and a frameless
    stereotactic system. Patients were required to name at least 3 pictures on the
    first 20 items of the BNT to qualify; Patients did not receive individualized
    speech therapy during the study. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S3-C3, two-model
    agreement, human verification pending): Patients


    Four right-handed, chronic aphasia patients participated, at 5–11 years post-L
    middle cerebral artery stroke Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-25'
    paper_section: Main paper; qualitative core draft
    confidence: low
    flags:
    - core_profile_machine_prepared
    - human_approval_pending
    - core_text_check_only
    - paper_completeness_pending
    - pdf_visual_review_pending
    - not_transcribed:statistics
    - not_transcribed:confounders_controlled
    - not_transcribed:confounders_not_controlled
    - not_transcribed:region_definition
    - not_transcribed:imaging_details.reference_space
    - not_transcribed:imaging_details.atlases_used
    - not_transcribed:lesion_mapping
    - not_transcribed:sample.phase
    - not_transcribed:strength
    - proposed_concept:picture_naming
  therapy:
    id: rtms_1hz
    name: 1 Hz repetitive transcranial magnetic stimulation
  citation: '@Naeser2005'
  source_passages:
  - section: Original source P7-S1-C3
    page: 7
    quote: 'We found a signiﬁcant main eﬀect of testing

      time on the ﬁrst 20 items on the BNT (f = 5.69;

      df = 3,9; and p = .018) and the BDAE subtests Animal

      Naming (f = 4.67; df = 3,9; and p = .03) and Tools/Im-

      plements Naming (f = 7.39; df = 3,9; and p = .008).'
    supports: claim
  - section: Original source P7-S1-C6
    page: 7
    quote: 'At 2 weeks, there was sig-

      niﬁcant improvement on the BDAE subtest, Animal

      Naming (p = .02).'
    supports: claim
  - section: Original source P7-S1-C7
    page: 7
    quote: 'At 2 months, there was signiﬁcant

      improvement on three naming tests: (1) BNT (ﬁrst 20

      items) (p = .003); (2) BDAE subtest, Animal Naming

      (p = .02); and (3) BDAE subtest, Tools/Implements

      (p = .04).'
    supports: claim
  - section: Original source P7-S1-C8
    page: 7
    quote: 'At 8 months, all three naming scores contin-

      ued to improve relative to pre-rTMS, but only Tools/

      Implements was signiﬁcant (p = .003).'
    supports: claim
  - section: Original source P7-S1-C9
    page: 7
    quote: 'BNT and Animal

      Naming failed to reach signiﬁcance because of P3 (Fig.

      4).'
    supports: claim
  - section: Original source P3-S3-C3
    page: 3
    quote: 'Patients

      Four right-handed, chronic aphasia patients partici-

      pated, at 5–11 years post-L middle cerebral artery

      stroke.'
    supports: sample
  - section: Original source P6-S1-C12
    page: 6
    quote: 'On each day

      of treatment, rTMS was applied at 1 Hz frequency for

      20 min (1200 pulses) at 90% of motor threshold (left,

      ﬁrst dorsal interosseus muscle), using a Super-Rapid

      High Frequency MagStim Magnetic Stimulator and a

      ﬁgure 8-shaped coil (MagStim, NY).'
    supports: method
  - section: Original source P6-S2-C3
    page: 6
    quote: "A frameless ste-\nreotaxic system (Brainsight, Rogue Industries, Mon-\n\
      treal) guided the position of the TMS coil on the\npatient\x01s scalp."
    supports: method
  - section: Original source P8-S1-C11
    page: 8
    quote: 'Nevertheless, our results should be considered preli-

      minary, as this was an open-protocol study, and no pa-

      tients received sham rTMS.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Naeser2005
  proposal_id: R002
  review_status_sha256: 789a22df9cc63e82e4f45c1933b77f7829fbb4e8103dc768d49967d46d4a3cf1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
        A/passages.json: 74999280efec955703701aecdce64acb4ac444fb6e7cbcfee282aa663c176c54
        A/raw.json: 2b4adc35d94ea1cd55fc6b8d048e524f2526f182cd814aeeee5d370c65d4f4d0
        A/source-units.json: d08fe84902f87a4581c02daafee412d2e49d44dbb3e5071c03027d70f94c5960
        A/full-source-units.json: 8360845c469d6341de6fbb66eb7b357b4666be3348f0f7f40d4375bec552d4f5
        A/meta.json: 508f803480023519560a26b1c49e7264cdd4125a4d867e081ee202d7a5523528
        A/table-images/page-7.png: 8f7c852ad5aafe24dd28f67fcba3f83ff86be65653c222de2e05ba56aa698855
        A/table-images/page-4.png: 42b216c5d7f414ddcba9295098c757cb0ffb39b5816e38e262ad02ed294704d4
        A/table-images/TABLE-1-page-4-1.png: b9e607a39d72d23de45fae15a451f36bb6f2541ab0aaed09f94b58cbf9cd79e1
        A/table-images/manifest.json: 6220672d4e46db26cdb8e0ffe71c2c228b13941e0306a0e65e835d2ae13d90fc
        A/table-images/TABLE-2-page-7-1.png: 20eddec0244247897dc86683b6d05355ca47abbc23a691182e1b7c1aaaf7fd39
        A/clauses/window-03/raw.json: 0618befa6ce222e095aff0e32170c87e4b17316c04f83cf240fe3816120827dc
        A/clauses/window-03/prompt.txt: eb39ef5229a30659bf80620d9a127b1eb747f2cca40769e8a420d13a77dd1690
        A/clauses/window-03/meta.json: b6a9602d80ce5dcbb5ef3d7aed64d9a098a7ab24141c5f01bcfe89404698f3cd
        A/clauses/window-04/raw.json: 9cc3c65e77f3ca3abc1292a2fd3d913a3547bb0d32ee2000b482c7cff339f560
        A/clauses/window-04/prompt.txt: d7e290f01c3cde3b20be6470a9cfe3f8f6fb8169bf0c6357ca37de0965b265c0
        A/clauses/window-04/meta.json: 08ea22fd389e2a55aa89ae904f64749dc8b3901ac404d4c98ae351193d24ed66
        A/clauses/window-05/raw.json: dd575391af80cbe47e4d8a2a444f9f3ca61f6dc57cc0e37207ac4eca2acd8c96
        A/clauses/window-05/prompt.txt: 6dc36bdc950debbe5efebcdd7013ed668c12720fa8669c693e9a2c6ea00c2c58
        A/clauses/window-05/meta.json: 4279bbf1afacc678c3d2594f453de8d66ea77b25e7394959fa6553618f6e18ad
        A/clauses/window-02/raw.json: 6cbfc516310e0344b253f4c769a382523eecfc86cadb84750ae2ee87c3d61d0b
        A/clauses/window-02/prompt.txt: 79e7d851d910e8fe29c83268786b60732dc24ff5135ad42202f059d28c92f963
        A/clauses/window-02/meta.json: be9e8e9b1e694787790213231cf2b778b2220ed725787554d5dde259e9855b6e
        A/clauses/window-07/raw.json: 2a9e7bcdcc00aad811927752be86308b2b1f4d4f6774393a54f399dae0ff8095
        A/clauses/window-07/prompt.txt: 8bec2adfc3aafda9aab7640d8ff15410852554e8b4922f764322ac921f03afed
        A/clauses/window-07/meta.json: a8d80d38a3013e296cbb364b8ae0287a0381a25c7082d201f8e0e244f6bc9970
        A/clauses/window-01/raw.json: e5cddb5dcea94782f287e3090554053cbf6bfc256d9c94b245c20523760853b8
        A/clauses/window-01/prompt.txt: 650f8b08a47c14dbcc156a843836f18a231cffbf12ad56aa1d77c920ad261f4f
        A/clauses/window-01/meta.json: 0d2354c74747f8116b151fe834709aa0107ae28b29ec3fc9cccd4b6305b04b73
        A/clauses/window-06/raw.json: 7fcb3901d2537b538c2416364c548fc16c08af1594994fb2fceccd24dd1eff07
        A/clauses/window-06/prompt.txt: 479d3f94004d4b76e388ef9469d46d860bf4bc55f7a3d65398f27411df80a096
        A/clauses/window-06/meta.json: 18aac0ae4f07b6cd34c3e7371d535db1ccced05237edec3d04cafde39aaf4f34
        A/tables/TABLE-2-page-7-2/raw.json: 1104c386f71169a6659582bc6ab3b73ca4367bea266bd678d49fdf84325c9bac
        A/tables/TABLE-2-page-7-2/prompt.txt: 0192b92a5b9181cf88ad75dfde959bc41e8c78a047b6d04490683b4b959ec992
        A/tables/TABLE-2-page-7-2/meta.json: 4ae89a292f646f67e027f392331960961c2159f583448e3cfda2aa7a5d2bf8d3
        A/tables/TABLE-1-page-4-1/raw.json: 305f7b5574b8543bf3ea3bf502dd5a23d18935d4d7cc2203719669f85e096b9b
        A/tables/TABLE-1-page-4-1/prompt.txt: e1f287e8d26a4dbb1cd86e5358721243fb29ffc585461f5dbdd28468227df389
        A/tables/TABLE-1-page-4-1/meta.json: 4cd208c1a6b911edf77fe7b4c7d90ff23bf84c04212cd3a9718eadbd47040c58
        B/passages.json: 74999280efec955703701aecdce64acb4ac444fb6e7cbcfee282aa663c176c54
        B/raw.json: 560b2cc0097470eac4e245b00308c23d585a77736b3f1a889004366981705c46
        B/source-units.json: d08fe84902f87a4581c02daafee412d2e49d44dbb3e5071c03027d70f94c5960
        B/full-source-units.json: 8360845c469d6341de6fbb66eb7b357b4666be3348f0f7f40d4375bec552d4f5
        B/meta.json: a4427eb497e5710a66f24c5a642b02f42abe2765589281dfc492a0b68433ce7f
        B/table-images/page-7.png: 8f7c852ad5aafe24dd28f67fcba3f83ff86be65653c222de2e05ba56aa698855
        B/table-images/page-4.png: 42b216c5d7f414ddcba9295098c757cb0ffb39b5816e38e262ad02ed294704d4
        B/table-images/TABLE-1-page-4-1.png: b9e607a39d72d23de45fae15a451f36bb6f2541ab0aaed09f94b58cbf9cd79e1
        B/table-images/manifest.json: 989e9503f70455ff90f713d45b18602f786aae92d4d1636ff08efbe23c12b6f3
        B/table-images/TABLE-2-page-7-1.png: 20eddec0244247897dc86683b6d05355ca47abbc23a691182e1b7c1aaaf7fd39
        B/clauses/window-03/raw.json: b00c4ca050a1d738b63fd65da6e755c6b306398132351469d5eb1b73e4248c16
        B/clauses/window-03/prompt.txt: eb39ef5229a30659bf80620d9a127b1eb747f2cca40769e8a420d13a77dd1690
        B/clauses/window-03/meta.json: 976f9303f8a9fb1649e81037131b6357193e33a6c7ae6519f004ae196cb3e740
        B/clauses/window-04/raw.json: 0226cbdcddd3b6b2b73ed28b2c49a16040f13e6af24dcac29c77cef78cfde426
        B/clauses/window-04/prompt.txt: d7e290f01c3cde3b20be6470a9cfe3f8f6fb8169bf0c6357ca37de0965b265c0
        B/clauses/window-04/meta.json: 1f348d0ca39d9a25d287dba18acf4bc420423e78de3fb677f8548cdbad05a858
        B/clauses/window-05/raw.json: bc3116b36d42273c5c1ac3bb105b09dd50476a558cff9bbc8cb2740ec4eb8077
        B/clauses/window-05/prompt.txt: 6dc36bdc950debbe5efebcdd7013ed668c12720fa8669c693e9a2c6ea00c2c58
        B/clauses/window-05/meta.json: 4d88f2364f3f78c5c4ac367cf16a9e72e8331a0910f0da62415f51bc3cbf6841
        B/clauses/window-02/raw.json: 3ea732fc18cc2a7945554aa7bb0f320c6edba7fdc6656287db25e9961cefcfd6
        B/clauses/window-02/prompt.txt: 79e7d851d910e8fe29c83268786b60732dc24ff5135ad42202f059d28c92f963
        B/clauses/window-02/meta.json: 4191d07d77795dfbd9ceb4f5262a4991c0827fb5abb897f31da32ba19142c665
        B/clauses/window-07/raw.json: bdcee954643326352538edbd4ac70e4af71cc5427e42924c6cfa968b14a587b0
        B/clauses/window-07/prompt.txt: 8bec2adfc3aafda9aab7640d8ff15410852554e8b4922f764322ac921f03afed
        B/clauses/window-07/meta.json: b8232fcdf46bd8ba46e49f10e041cec3b6da8184e2176a6f6731d0f1633f01eb
        B/clauses/window-01/raw.json: 5d152c58ba19e54753928f232423ba866e77fcc0bdf84cbb1c221727a466e710
        B/clauses/window-01/prompt.txt: 650f8b08a47c14dbcc156a843836f18a231cffbf12ad56aa1d77c920ad261f4f
        B/clauses/window-01/meta.json: 07d734eb840b1fa04bfbee407889cf3cab30ac08cfbf5d15928af4a9ef498582
        B/clauses/window-06/raw.json: cb8c26c2c1a523ff6fe49c88e44b787a8c44e05d689b01a6bd0f6863900f9747
        B/clauses/window-06/prompt.txt: 479d3f94004d4b76e388ef9469d46d860bf4bc55f7a3d65398f27411df80a096
        B/clauses/window-06/meta.json: 20724b52e3eff62c7d32385e6e77754ce58abcaa314982035c85a5d472119541
        B/tables/TABLE-2-page-7-2/raw.json: 294108487b5be9f21472116d245c219b01709cc131271dcbb2ebdf5ee3194c14
        B/tables/TABLE-2-page-7-2/prompt.txt: 0192b92a5b9181cf88ad75dfde959bc41e8c78a047b6d04490683b4b959ec992
        B/tables/TABLE-2-page-7-2/meta.json: 066c8bef77cff253cedb2f029e5c9be5e12b837d92c880245afa5368b871de61
        B/tables/TABLE-1-page-4-1/raw.json: 5495d4b1d9e8e01c5bf047ba64b6a89d5422f61fdf487ecc6db2c479caba5a1c
        B/tables/TABLE-1-page-4-1/prompt.txt: e1f287e8d26a4dbb1cd86e5358721243fb29ffc585461f5dbdd28468227df389
        B/tables/TABLE-1-page-4-1/meta.json: 7ff9c1f7236c16e3418355c9dbd7ed57d0da32ae9908ba28fad1f75649f06998
      code:
        relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
        relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
        ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
        strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
      model: gemma4:26b
      model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
      host: http://localhost:11434
      max_output_tokens: 20000
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
      source_review: _compare/relationships-2026-11-16/review-current/Naeser2005
      source_status_sha256: ce0f22780262253a8fab2e9fe28b450b69e70738be7a838cd00bc0b5525ae710
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: 1 Hz rTMS to R pars triangularis
    outcome:
      text: Boston Naming Test (first 20 items), BDAE Animal Naming, and BDAE Tools/Implements
        Naming
    analysis_label: Standardized language testing (BNT/BDAE)
    relation: treatment_effect
    evidence_ids:
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    qualifier_ids:
    - P7-S1-C9
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
      source_review: _compare/relationships-2026-11-16/review-current/Naeser2005
      source_status_sha256: ce0f22780262253a8fab2e9fe28b450b69e70738be7a838cd00bc0b5525ae710
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C8
      - Unaccounted source passage P1-S1-C8
      - Accounting without a linked unit P4-S1-C11
      - Accounting without a linked unit P5-S1-C11
      - Accounting without a linked unit P5-S2-C10
      - Accounting without a linked unit P5-S2-C6
      - Accounting without a linked unit P5-S2-C7
      - Accounting without a linked unit P5-S2-C9
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C9
      - Unaccounted source passage P4-S1-C11
      - Unaccounted source passage P5-S2-C7
      - Unaccounted source passage P5-S2-C10
      - Unaccounted source passage P5-S1-C11
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C5
      - Result passage disposed without unit P6-S2-C7
      - Result passage disposed without unit P7-S1-C1
      unattached_null_or_qualifier_ids:
      - P5-S2-C6
      - P6-S1-C3
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 158
      unselected_timing_passages:
      - P1-S1-C7
      - P3-S3-C3
      - P8-S1-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P8-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P3-S3-C8
        - P4-S1-C4
        - P5-S1-C12
        - P6-S2-C9
        - P7-S1-C2
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P8-S1-C2
        - P8-S1-C3
        - P8-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P3-S3-C8
        - P4-S1-C3
        - P4-S1-C4
        - P5-S1-C7
        - P6-S2-C9
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C8
        - P8-S1-C2
        - P8-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - outcome_definition
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
      source_review: _compare/relationships-2026-11-16/review-current/Naeser2005
      source_status_sha256: ce0f22780262253a8fab2e9fe28b450b69e70738be7a838cd00bc0b5525ae710
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Abstract restatement of standardized naming results.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results from a previous study (Naeser et al., 2002).
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results from a previous study (Naeser et al., 2002).
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results from a previous study (Naeser et al., 2002).
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pilot testing on normal subjects.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pilot testing regarding learning/priming effects.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient lesion description.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes monitoring of coil targeting.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 3
      reason: States no negative side effects reported.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant increase in pictures named post-rTMS.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant reduction in reaction time post-rTMS.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies that effects were consistent in all patients.
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of S&V results.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant main effect of time on BNT and BDAE naming.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement referring to Table 2.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant improvement in Animal Naming at 2 weeks.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant improvement in BNT, Animal Naming, and Tools/Implements
        at 2 months.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant improvement in Tools/Implements at 8 months.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifies why BNT and Animal Naming failed significance at 8 months.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null findings for other changes.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Reports improvement in phrase length at 2 months.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Provides specific phrase length increases for P2 and P3.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports loss of phrase length effect at 8 months.
    - source_id: P7-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion statement.
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of BNT and BDAE results.
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of S&V results.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of BDAE results.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of 8-month naming results.
    - source_id: P8-S2-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of 2-month naming results.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about individual patient improvement.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Conclusion that rTMS appears safe.
    unresolved_coverage:
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P3-S2-C3
    - P3-S2-C4
    - P3-S2-C6
    - P4-S1-C11
    - P5-S1-C11
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C9
    - P5-S2-C10
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S2-C4
    - P6-S2-C11
    - P7-S1-C1
    - P7-S1-C5
    - P7-S1-C9
    - P7-S1-C10
    - P7-S1-C13
    - P7-S1-C14
    - P7-S2-C2
    - P7-S2-C4
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S2-C2
    - P8-S2-C7
    - P8-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C3
      recruited_sample:
      - P3-S3-C3
      eligibility:
      - P3-S3-C3
      - P4-S1-C2
      imaging_provenance:
      - P3-S2-C2
      - P5-S1-C14
      - P6-S1-C11
      imaging_timing:
      - P3-S2-C2
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S3-C8
      - P4-S1-C3
      - P5-S1-C7
      - P7-S1-C2
      limitations:
      - P8-S1-C11
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P3-S3-C7
      descriptive_personal_factors:
      - P4-S2-C1
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P8-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P3-S3-C8
      - P4-S1-C4
      - P5-S1-C12
      - P6-S2-C9
      - P7-S1-C2
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P8-S1-C2
      - P8-S1-C3
      - P8-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P3-S3-C8
      - P4-S1-C3
      - P4-S1-C4
      - P5-S1-C7
      - P6-S2-C9
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C8
      - P8-S1-C2
      - P8-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: core
    scope: Independent model text review of core meaning; not human approval or complete
      PDF verification
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
      review_sha256: 789a22df9cc63e82e4f45c1933b77f7829fbb4e8103dc768d49967d46d4a3cf1
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: &id001
        - gemma4:31b
        - qwen3.8:27b
        digests: &id002
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P7-S1-C3
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      source_result: The study reports a significant main effect of testing time on
        the first 20 items of the Boston Naming Test (BNT) and the BDAE subtests for
        Animal Naming and Tools/Implements Naming. Post-hoc comparisons indicated
        significant improvement relative to pre-rTMS at 2 weeks for Animal Naming,
        at 2 months for BNT, Animal Naming, and Tools/Implements, and at 8 months
        for Tools/Implements. BNT and Animal Naming did not reach significance at
        8 months due to one patient's performance.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the univariate one-way repeated
            measures ANOVAs on standardized language tests (BNT and BDAE subtests)
            described in P7-S1-C2 and P7-S1-C3. The proposed core correctly identifies
            these as the primary outcome measures.
          source_ids:
          - P7-S1-C2
          - P7-S1-C3
          - P3-S3-C8
        direction:
          answer: fits
          reason: The source reports significant improvement (increased scores) in
            naming tasks following rTMS. The proposed core claims 'significantly improved
            picture naming', which aligns with the detected positive association.
            The nuance regarding 8-month results (only Tools/Implements significant)
            is captured in the claim text.
          source_ids:
          - P7-S1-C3
          - P7-S1-C7
          - P7-S1-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as 1 Hz rTMS to the right pars
            triangularis (P6-S1-C7, P6-S1-C12). The outcome is correctly identified
            as BNT (first 20 items) and BDAE Animal/Tools naming (P7-S1-C3). The patient
            measurement is non-imaging (behavioral language testing), not diffusion
            or template overlap.
          source_ids:
          - P6-S1-C7
          - P6-S1-C12
          - P7-S1-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the entry criterion (naming at least
            3 pictures on BNT) and the lack of individualized speech therapy. It also
            notes the open-protocol nature. The specific finding that BNT/Animal naming
            failed to reach significance at 8 months due to P3 (P7-S1-C9) is a detail
            of the result pattern, but the core claim focuses on the 2-month significance
            and 8-month Tools/Implements significance, which is faithful to the source's
            summary of 'lasting improved naming'.
          source_ids:
          - P4-S1-C2
          - P3-S3-C7
          - P8-S1-C11
          - P7-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The core includes the limitation that the study was open-protocol
            without sham control (P8-S1-C11) and the small sample size. The specific
            reason for the non-significance at 8 months for BNT/Animal (P3's performance)
            is a detail of the statistical outcome rather than a general caveat that
            changes the interpretation of the treatment effect itself, which is supported
            by the 2-month data and the 8-month Tools/Implements data.
          source_ids:
          - P8-S1-C11
          - P3-S3-C3
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R002
      exposure:
        text: 1 Hz rTMS to R pars triangularis
      outcome:
        text: Boston Naming Test (first 20 items), BDAE Animal Naming, and BDAE Tools/Implements
          Naming
      analysis_label: Standardized language testing (BNT/BDAE)
      relation: treatment_effect
      evidence_ids:
      - P7-S1-C3
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      qualifier_ids:
      - P7-S1-C9
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
        source_review: _compare/relationships-2026-11-16/review-current/Naeser2005
        source_status_sha256: ce0f22780262253a8fab2e9fe28b450b69e70738be7a838cd00bc0b5525ae710
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ef236b992c615c3d8da08182998fc318d0290dc0572ba3f3ed82ecfc8e6f87de
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ce2a7061051b3cdd32b846c034d8b1bf8e952b6d1d054074aad1e318bd05c381
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C3
          page: 3
          text_layer_sha256: ce2a7061051b3cdd32b846c034d8b1bf8e952b6d1d054074aad1e318bd05c381
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients

          Four right-handed, chronic aphasia patients partici-

          pated, at 5–11 years post-L middle cerebral artery

          stroke.'
        anchor_text: 'Patients

          Four right-handed, chronic aphasia patients partici-

          pated, at 5–11 years post-L middle cerebral artery

          stroke.'
        excluded_fragments: []
        image_sha256: ed5a8d853293f27a4252273944633fe11a1f0d6e7772ea4532c815a958a164f8
        transcription: 'Patients


          Four right-handed, chronic aphasia patients participated, at 5–11 years
          post-L middle cerebral artery stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'We found a signiﬁcant main eﬀect of testing

    time on the ﬁrst 20 items on the BNT (f = 5.69;

    df = 3,9; and p = .018) and the BDAE subtests Animal

    Naming (f = 4.67; df = 3,9; and p = .03) and Tools/Im-

    plements Naming (f = 7.39; df = 3,9; and p = .008).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
