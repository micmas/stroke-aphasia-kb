---
id: object_cleft_training
name: training of object-cleft forms
kind: therapy
findings:
- id: f1
  target: object_relative_production
  target_kind: impairment
  claim: Training of object-cleft forms had no effect on the production of object-relative sentences.
  direction: no_effect
  relationship: treatment_response
  method: behavioral_only
  sample:
    n: 2
    population: Participants 2 and 4 with Broca aphasia and agrammatism who received object-cleft training first; two of the four study participants.
    phase: not_reported
    time_post_onset: measured during treatment probes
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size (N=4)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Training to comprehend and produce object-cleft sentences using a linguistic-specific treatment (TUF) involving active form sentences, constituent cards for derivation, and sentence production priming. generalization was defined as a performance change of at least 40% over observed baseline levels. Additional metadata has not been transcribed; review the pending-field flags before approval. Publication correction (human verification pending): Object-cleft-first training finding is restricted to Participants 2 and 4.'
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
    - proposed_concept:object_relative_production
    - publication_correction_pending_human_verification
  therapy:
    id: tuf
    name: TUF
  citation: '@Thompson2003'
  source_passages:
  - section: Original source P11-S1-C2
    page: 11
    quote: "Examination of the data for H.R. and K.G. fur- \nther showed that training object-cleft forms had no ef- \nfect on object relatives."
    supports: claim
  - section: Original source P4-S2-C11
    page: 4
    quote: "Method \nParticipants \nFour individuals with Broca’s aphasia with agram- \nmatism participated in the study."
    supports: sample
  - section: Original source P7-S1-C5
    page: 7
    quote: "Treatment \nParticipants were trained to comprehend and pro- \nduce each sentence type using TUF."
    supports: method
  - section: Original source P7-S2-C9
    page: 7
    quote: "Gen- \neralized production to untrained sentences was consid- \nered to have occurred when levels of performance changed \nby at least 40% over observed baseline levels."
    supports: confounders
  - section: Original source P6-S2-C14
    page: 6
    quote: "Sentence Production \nProduction of the three sentence types was tested \nusing a sentence production priming paradigm."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Thompson2003
  proposal_id: R003
  review_status_sha256: 43bbc24fec5b8c696fe292b23c4e17c81df386e1770eb369fd15244130cd1826
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
        A/passages.json: ca423bec1efda580154c80800c1016a520327282c35d8d2f68b32bca75fd4eb6
        A/raw.json: 3d74de9f282774090043341fc1438db72f65a577e86b5093c0d006dbf859d6f2
        A/source-units.json: e99c91a1704f253e676473a3f8e437b7ea9cc2b8d280e1769e2b42dec16e2428
        A/full-source-units.json: 903d1e42dc8f41ba4bca6d7d710c08875f3fea7a1e6493f7a4a6b8d680fcaf1b
        A/meta.json: 137c164776e9254a1df66ea3b4978fe99fed65aad10697179b2876b44d72c584
        A/table-images/TABLE-1-page-5-1.png: ced1edadd4b4fcf95b95f07382a88959eba6aac9d17557ea690d6a4cd05f393e
        A/table-images/page-10.png: e373f34e39f710ad3db5627ec42342faa602a32a7e1d0bea379ab82fa1ce8a07
        A/table-images/page-5.png: d2b2acd20a397b9da945f0489dd81a41879aca3b0de914fa951237389ec097f8
        A/table-images/manifest.json: 20e6e57f8339613b245ce26478669153d14e4a0666cabd043fac45c96d8e5c85
        A/table-images/TABLE-2-page-10-1.png: c11ef245bff90185538d119942cbb525848b681e96df5d563b2452f8431923b9
        A/clauses/window-11/raw.json: 197f64f654f477bd6cef81a67f54191dd472e211902e77d8a5695aca749ec42b
        A/clauses/window-11/prompt.txt: bd846e2b0257af0e8e8f27ff0c06eb39486a1c88e9cfc9e431622aba70e2aa43
        A/clauses/window-11/meta.json: 7eb518280adaae28c4c887411d6e273c701b19a95b2085cc0ff0b2974225113c
        A/clauses/window-10/raw.json: 1a4dbfcde5aa649e174f83e4a2c04a4f6d1502638658d5c96360c5062e340712
        A/clauses/window-10/prompt.txt: c87e75c1e807c21c90f0b51b380b475b0395955e3179d232f4c9bbaa2565e207
        A/clauses/window-10/meta.json: 82c41885465a849ebbfae66223c3409b2b767d0751e99ac173255601f9ec3a7f
        A/clauses/window-03/raw.json: f1af7aa53436b0c7d58a1300e1b8eee47ae7dde21a98fee5119e38592ba1a232
        A/clauses/window-03/prompt.txt: b1f2a142251a60154d0e215e5903680b31b0f4e3fb561f703a20d7246e677a8c
        A/clauses/window-03/meta.json: 41c53f7a476bc9ad0b3bcaa3d9a6aa2a9b69f233909c5a135e45297324d90226
        A/clauses/window-04/raw.json: cd2909e936b7af7de6da1a795e730b966de0558c3d39b246204d588a5d8ef68e
        A/clauses/window-04/prompt.txt: 7aa998dd08ef811f7bad6b2c19746d00b348eeae76388c1381360f6520e1f33a
        A/clauses/window-04/meta.json: 7e809dc9e3eb59de0acceb8659eae16540d2a0f07dc0fdad970a25bc621b32ca
        A/clauses/window-05/raw.json: c511dccacb9a216d4c567f56368d0252ba690ab8c273d4631300ebb67e1dda1b
        A/clauses/window-05/prompt.txt: e4ced7112463e84d97c9de29e5afba9b434c04d6be9a980f4694780b87fef7c5
        A/clauses/window-05/meta.json: 734761ceebeb90ef02b7fe09bb4ad6125d0bdfad19e25804e2cdc8d27ffcf296
        A/clauses/window-02/raw.json: d131395990f7657a7f6550272c73759e5fc853cfda409d99ef977509a4bd5bba
        A/clauses/window-02/prompt.txt: 2ffa95ea229a0f7458c9a33b497120bddcfe67debec375bcdce9ae723c5ffd81
        A/clauses/window-02/meta.json: dfeac0dd67767fa422d2f7281427b0ba6f36fea759008e3a9d6e5234ad055b3e
        A/clauses/window-12/raw.json: 1157ef0ce662fb80613b16572dcb3e0309545e04d95af14d39ef89eec8901dc1
        A/clauses/window-12/prompt.txt: 1e155408567ee27900adf5f4f9278d0c7e46c2b764cab17301bc0b894b2a8d06
        A/clauses/window-12/meta.json: 517e23b8b62044f446f01cf0db7a2396a8fff47d76ee271f401d0be6abbfdb06
        A/clauses/window-13/raw.json: f1bdf4c7081ee35affb2ea1e5d7b6c6ce657ea330631f992891f8cb90a2b28fc
        A/clauses/window-13/prompt.txt: b20b769f890fda706925bad31dbe6abf27085f560856aef479b7da20011be03a
        A/clauses/window-13/meta.json: b16f0b33b943f0aed98cd70c13064753ba36a06feac599eb52d582d8d443d0a2
        A/clauses/window-14/raw.json: ae0b5f25be6d15d3ec7a01e713b749c908560deaeba1af7cd6375b01152a58b6
        A/clauses/window-14/prompt.txt: 0e296e0584b8a280e5a48d68e4081fc893af8f3a71fa9f37740198664db5cc16
        A/clauses/window-14/meta.json: 2da93e8175408d3c171b00b6504be185fef4fbf11841215e4422fc972cf7d2a7
        A/clauses/window-09/raw.json: c098e094d5a50aabf1c910207789fd7f7c0007d684472c7c4d2cf83db8b0cb3a
        A/clauses/window-09/prompt.txt: aa7ebf6397f68aec76bac5be69d954230518b741b019196849e61bfdf304efd7
        A/clauses/window-09/meta.json: fe8447fa77e62f7708b326ad5a02b079de55a9a476dee0b684a90d69896f530e
        A/clauses/window-07/raw.json: 1a37d4337ac089b1f7f5a0754de2b8a4386b88c50b2a6c69f87e78718392bd1e
        A/clauses/window-07/prompt.txt: fa608e0e8de9c5703863cf5dc750bf48a1fb57583d02254aac52136cea6beb6b
        A/clauses/window-07/meta.json: 65dff2aaf1f370ea8e38c4ccf2041f4c4feed158de57012f530b58fdcbbb4b17
        A/clauses/window-01/raw.json: d494ebaeefedd5f5a0a2259e65273be8aab13d71cbf653528ef93f4c1a673b6d
        A/clauses/window-01/prompt.txt: d4abb026670445820dd7a4108c5b67ae0f44787697e754c3dd480cd1c455b64c
        A/clauses/window-01/meta.json: ca160f4197a252fb72d4e2b3e3e3a575ae745507288f2f439664316c8be086f1
        A/clauses/window-06/raw.json: ece34c3a5b91e3084fb11db7253987f215cea0958b865371d7a0a16ee65a8dd4
        A/clauses/window-06/prompt.txt: 1197fd20c06b0ed337adf2140c163b38763e9d2c98f256a0728a66cb740a2ecc
        A/clauses/window-06/meta.json: 275ebd075ebf41998e966854e5473b04754e78955b4a289583674d7450b40b12
        A/clauses/window-08/raw.json: 3c2b0bc9baaca41a7ed0cd6e3f60630a77cba6e976728799d919f07bc387f908
        A/clauses/window-08/prompt.txt: 24aa01403e4362e065ba87174a178dd2ef21c83a2abaa97db8cf777d1e2582be
        A/clauses/window-08/meta.json: e9e5f5841ebcf5a0c251fcf1a95aef31c1236dc07893cfd598cc06ed0a29575e
        A/tables/TABLE-1-page-5-1/raw.json: 56fba7b3053b56d4dab23ac2a14deaf74d173bcd7ae3ca330dd9f3cc69f94d41
        A/tables/TABLE-1-page-5-1/prompt.txt: 871d1a938671a6ac088ae82ddcbfdd14bac1968b183e6960fa8b6f64df33a29b
        A/tables/TABLE-1-page-5-1/meta.json: 285bf660432edde4088dc1af6372c1c54d4d3316928976c6dfb68bff2f6dddc5
        A/tables/TABLE-2-page-10-2/raw.json: 665d8f8ab7769c232b1b9b624c0dc30078b15dad240927fad91e4467838f1e59
        A/tables/TABLE-2-page-10-2/prompt.txt: e81f32b187680d532b64781287ebdc2a689f9d161fc1a136367ef70ef29fdf1e
        A/tables/TABLE-2-page-10-2/meta.json: 518660cf0d3467fa4ca10797144eedf63a65c9bb9beb2cbfcf61cca8da89e55b
        B/passages.json: ca423bec1efda580154c80800c1016a520327282c35d8d2f68b32bca75fd4eb6
        B/raw.json: 546c7d392406cfa9ab57b90085dea5d61e19aafd48da0dacd3e8ac15dbd4a80c
        B/source-units.json: e99c91a1704f253e676473a3f8e437b7ea9cc2b8d280e1769e2b42dec16e2428
        B/full-source-units.json: 903d1e42dc8f41ba4bca6d7d710c08875f3fea7a1e6493f7a4a6b8d680fcaf1b
        B/meta.json: 51f3c3e221b2abb1a02945c643eab4468630151a5d2a5629e273bb6c8b27dfa7
        B/table-images/TABLE-1-page-5-1.png: ced1edadd4b4fcf95b95f07382a88959eba6aac9d17557ea690d6a4cd05f393e
        B/table-images/page-10.png: e373f34e39f710ad3db5627ec42342faa602a32a7e1d0bea379ab82fa1ce8a07
        B/table-images/page-5.png: d2b2acd20a397b9da945f0489dd81a41879aca3b0de914fa951237389ec097f8
        B/table-images/manifest.json: ff9a739fbd8008c7ea3870aa2c393a8283723b71ed6dc07b9830baa9f57d91f7
        B/table-images/TABLE-2-page-10-1.png: c11ef245bff90185538d119942cbb525848b681e96df5d563b2452f8431923b9
        B/clauses/window-11/raw.json: 54e080cbb7295c792cf67300d7ac862448fa1ef2ff205e18ae950abbf5f72e4a
        B/clauses/window-11/prompt.txt: bd846e2b0257af0e8e8f27ff0c06eb39486a1c88e9cfc9e431622aba70e2aa43
        B/clauses/window-11/meta.json: b912d57a9739849742437cee4d1ce97169bb5307fcac6851407d8cbb37d7ef30
        B/clauses/window-10/raw.json: 7fe78bcc1ebc3f2f9df891abe1e0ca9983cf2ba4bca427197072de0b42c62afe
        B/clauses/window-10/prompt.txt: c87e75c1e807c21c90f0b51b380b475b0395955e3179d232f4c9bbaa2565e207
        B/clauses/window-10/meta.json: 8846a1634dc1e786cf1c4182c01b87b11532a2a477d5b9f698432da4510fe917
        B/clauses/window-03/raw.json: aca0a7692571d34db3cb002bd6f511ec1f84719ebf89e88f1fd8a427a7bca89b
        B/clauses/window-03/prompt.txt: b1f2a142251a60154d0e215e5903680b31b0f4e3fb561f703a20d7246e677a8c
        B/clauses/window-03/meta.json: 157773d04d5c9d513d70fe1579cf77dcc16e8ea3f729bc75754cac0c1e1c38b8
        B/clauses/window-04/raw.json: c4a9d267bc6cdd2fdf5b1069dd36dc987c09674385673fed8ceedf42a1fca905
        B/clauses/window-04/prompt.txt: 7aa998dd08ef811f7bad6b2c19746d00b348eeae76388c1381360f6520e1f33a
        B/clauses/window-04/meta.json: 6f48878182ddef08a6421bb3180b88c7fc258cbefc9f1a57b1062d6b43ebbdb6
        B/clauses/window-05/raw.json: c511dccacb9a216d4c567f56368d0252ba690ab8c273d4631300ebb67e1dda1b
        B/clauses/window-05/prompt.txt: e4ced7112463e84d97c9de29e5afba9b434c04d6be9a980f4694780b87fef7c5
        B/clauses/window-05/meta.json: 8c50ac8ee2f276170599bad7b3cc5d58006d468913b04736c89b01118ca36249
        B/clauses/window-02/raw.json: d28609809399c1b0ae060c7875d047ea1469585800360654ecca59c93f2e9993
        B/clauses/window-02/prompt.txt: 2ffa95ea229a0f7458c9a33b497120bddcfe67debec375bcdce9ae723c5ffd81
        B/clauses/window-02/meta.json: 7cc77a05dab47b6c354e1d248075512dafedf01b57dfea7800a08376a042d8b4
        B/clauses/window-12/raw.json: a9551b054aaaca805e077ffa8624bf222212210d20fa62c7bf10dafd7534c6d3
        B/clauses/window-12/prompt.txt: 1e155408567ee27900adf5f4f9278d0c7e46c2b764cab17301bc0b894b2a8d06
        B/clauses/window-12/meta.json: 15274358cd740a79cb73bd56ec2903ac0a9fcbd55c8c5eef892d5412e5a68435
        B/clauses/window-13/raw.json: f1bdf4c7081ee35affb2ea1e5d7b6c6ce657ea330631f992891f8cb90a2b28fc
        B/clauses/window-13/prompt.txt: b20b769f890fda706925bad31dbe6abf27085f560856aef479b7da20011be03a
        B/clauses/window-13/meta.json: 7b90562c63ba404bf747cb68e5f875d7db30f9e2e3383b1ffeee5be720291fde
        B/clauses/window-14/raw.json: 8e8bd4b29cd448aa1b4687341ef5afaafab279cf41491ae7bc4da03520b3f75a
        B/clauses/window-14/prompt.txt: 0e296e0584b8a280e5a48d68e4081fc893af8f3a71fa9f37740198664db5cc16
        B/clauses/window-14/meta.json: 8b7f249fe0af8987da87d98505b759209000a2a7192c5852af75b5e200c5e3ee
        B/clauses/window-09/raw.json: 8534137be3785d4080076b87e503c2a27a80f2ae4190f6e6e6f490474854e07c
        B/clauses/window-09/prompt.txt: aa7ebf6397f68aec76bac5be69d954230518b741b019196849e61bfdf304efd7
        B/clauses/window-09/meta.json: ff936fa38cd0acfdaa0d3bc313877fa5bf489403c6ee0f0b35df018d1a2a751c
        B/clauses/window-07/raw.json: 69ea746ab8fbd3ec715ddf76f5a78147fca6e44b05ac004628ae5341124b5f87
        B/clauses/window-07/prompt.txt: fa608e0e8de9c5703863cf5dc750bf48a1fb57583d02254aac52136cea6beb6b
        B/clauses/window-07/meta.json: 76eec41187efe6a79e4dd242e9906229678784b1304f3a06665f18cfe7677b51
        B/clauses/window-01/raw.json: fc6e4d06d4ca74cb101cd3b70650f863662e44f8134c656a52784233fe465b52
        B/clauses/window-01/prompt.txt: d4abb026670445820dd7a4108c5b67ae0f44787697e754c3dd480cd1c455b64c
        B/clauses/window-01/meta.json: 32d2b5460c35f26a093d4b5a70de077e0927d265c9d419014331fa5629298e12
        B/clauses/window-06/raw.json: 9bea9c08bdc6831dc20e6f8e252202de48abe6dcf0abe670c92515db6420ca55
        B/clauses/window-06/prompt.txt: 1197fd20c06b0ed337adf2140c163b38763e9d2c98f256a0728a66cb740a2ecc
        B/clauses/window-06/meta.json: 27ca92d80a173e637a85fa39f7d17897ba1d31387c761845a4c3b26735343eaa
        B/clauses/window-08/raw.json: a74d14821a1407b46c2b4158b524989b936944a8a6292a6d3ca0a7e23fd33b28
        B/clauses/window-08/prompt.txt: 24aa01403e4362e065ba87174a178dd2ef21c83a2abaa97db8cf777d1e2582be
        B/clauses/window-08/meta.json: d5f29e7fb6efaa6b5b620330d3102d779406ab2f364ca6bc96016f12aebcc681
        B/tables/TABLE-1-page-5-1/raw.json: 3cf778f0dbce869e12f4b3deabc9338338deed0d35b063d77e5a8d454a5b64b0
        B/tables/TABLE-1-page-5-1/prompt.txt: 871d1a938671a6ac088ae82ddcbfdd14bac1968b183e6960fa8b6f64df33a29b
        B/tables/TABLE-1-page-5-1/meta.json: 6e98b3210fbbb0bd7fd63e542fa10a37cc949aa46a705914841be34b059b2fc0
        B/tables/TABLE-2-page-10-2/raw.json: 6356f791c7882fd6624262d393d837a5f03b73f0ad5bf2b79d8bf3f0ff6fb09e
        B/tables/TABLE-2-page-10-2/prompt.txt: e81f32b187680d532b64781287ebdc2a689f9d161fc1a136367ef70ef29fdf1e
        B/tables/TABLE-2-page-10-2/meta.json: 018e8d48a3e3cc06277d62faeed48ac3f46f9bd918be1859789f398a75632c93
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      source_review: _compare/relationships-2026-11-16/review-current/Thompson2003
      source_status_sha256: 009442aff235ae288e57b97bd164d8f7febe3055587ebecb6c255a1151b70c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: training of object-cleft forms
    outcome:
      text: production of object-relative sentences
    analysis_label: Object-cleft training generalization
    relation: treatment_effect
    evidence_ids:
    - P9-S1-C7
    - P11-S1-C2
    qualifier_ids: []
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      source_review: _compare/relationships-2026-11-16/review-current/Thompson2003
      source_status_sha256: 009442aff235ae288e57b97bd164d8f7febe3055587ebecb6c255a1151b70c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C2
      - Unaccounted source passage P5-S1-C2
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C8
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C4
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C7
      - Accounting without a linked unit P6-S1-C8
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C8
      - Unaccounted source passage P6-S1-C9
      - Accounting without a linked unit P7-S2-C8
      - Unaccounted source passage P7-S2-C8
      - Result passage disposed without unit P7-S2-C12
      - Result passage disposed without unit P7-S3-C2
      - Result passage disposed without unit P7-S3-C3
      - Result passage disposed without unit P9-S1-C6
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P9-S2-C4
      - Result passage disposed without unit P9-S2-C5
      - Result passage disposed without unit P10-S1-C4
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P9-S2-C6
      - Result passage disposed without unit P10-S2-C2
      - Result passage disposed without unit P11-S1-C3
      - Accounting without a linked unit P11-S1-C6
      - Accounting without a linked unit P11-S1-C7
      - Unaccounted source passage P11-S1-C6
      - Unaccounted source passage P11-S1-C7
      - Accounting without a linked unit P11-S3-C3
      - Unaccounted source passage P11-S3-C3
      - Accounting without a linked unit P11-S3-C9
      - Accounting without a linked unit P12-S1-C4
      - Unaccounted source passage P11-S3-C9
      - Unaccounted source passage P12-S1-C4
      - Accounting without a linked unit P12-S1-C7
      - Accounting without a linked unit P12-S1-C8
      - Unaccounted source passage P12-S1-C7
      - Unaccounted source passage P12-S1-C8
      - Accounting without a linked unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C6
      - Accounting without a linked unit P12-S2-C7
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P12-S2-C7
      - Unaccounted source passage P12-S2-C6
      - Accounting without a linked unit P12-S3-C3
      - Accounting without a linked unit P12-S3-C4
      - Unaccounted source passage P12-S3-C4
      - Unaccounted source passage P12-S3-C3
      unattached_null_or_qualifier_ids:
      - P7-S3-C3
      - P11-S1-C3
      - P11-S1-C7
      - P12-S2-C6
      - P12-S3-C3
      suppressed_nonrepresented_units: 33
      default_disposition_count_requires_completeness_check: 268
      unselected_timing_passages:
      - P4-S2-C14
      - P7-S2-C10
      - P9-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C15
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C1
        - P4-S2-C11
        - P6-S2-C4
        - P7-S2-C13
        - P7-S3-C3
        - P8-S2-C2
        - P8-S2-C8
        - P8-S2-C12
        - P8-S2-C13
        - P8-S2-C14
        - P8-S2-C16
        - P9-S1-C2
        - P9-S1-C6
        - P9-S2-C3
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S2-C2
        - P10-S2-C3
        - P10-S2-C4
        - P10-S2-C5
        - P11-S1-C5
        - P12-S2-C7
        - P12-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P6-S2-C4
        - P7-S2-C10
        - P8-S1-C3
        - P8-S2-C3
        - P9-S1-C10
        - P9-S2-C2
        - P9-S2-C5
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S2-C2
        - P10-S2-C3
        - P12-S1-C4
        - P12-S1-C7
        - P12-S1-C8
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P6-S2-C9
        - P6-S2-C14
        - P6-S3-C8
        - P6-S3-C9
        - P7-S1-C1
        - P7-S1-C3
        - P7-S2-C8
        - P8-S2-C2
        - P8-S2-C7
        - P8-S2-C9
        - P8-S2-C12
        - P8-S2-C13
        - P8-S2-C14
        - P8-S2-C15
        - P9-S1-C2
        - P9-S2-C2
        - P9-S2-C5
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P10-S1-C7
        - P10-S2-C3
        - P10-S2-C4
        - P11-S1-C6
        - P11-S1-C7
        - P11-S3-C2
        - P12-S1-C4
        - P12-S1-C7
        - P12-S1-C8
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C1
        - P4-S2-C12
        - P4-S2-C13
        - P4-S2-C14
        - P4-S2-C15
        - P4-S2-C16
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C4
        - P6-S2-C4
        - P11-S1-C5
        - P11-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-10-2
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-10-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S1
        - P4-S2
        - P8-S1
        - P8-S2
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      source_review: _compare/relationships-2026-11-16/review-current/Thompson2003
      source_status_sha256: 009442aff235ae288e57b97bd164d8f7febe3055587ebecb6c255a1151b70c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: States results of generalization from object-relative vs who-question training.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient diagnosis.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline WAB scores.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline naming/reading abilities.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Motor speech exam results.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline verb argument production.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline sentence comprehension.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline sentence comprehension.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pretreatment narrative patterns.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pretreatment narrative patterns.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pretreatment narrative patterns.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pretreatment noun:verb ratios.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pretreatment open:closed class ratios.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of dependent variables.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability.
    - source_id: P7-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figures.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline production difficulty.
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline comprehension levels.
    - source_id: P7-S3-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Improvement in trained object relatives for P1.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Generalization to object clefts for P1.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Generalization to who-questions for P1.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improvement during treatment.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improvement for object clefts/relatives.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Improvement in trained object relatives for P3.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Generalization to object-cleft and who-questions for P3.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Production of all three types near 100% for P3.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improvements for P3.
    - source_id: P8-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline comprehension levels.
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension reached near perfect accuracy.
    - source_id: P8-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Who-question production improved for P2 and P4.
    - source_id: P8-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: No generalization to object-cleft or object-relative for P2 and P4.
    - source_id: P8-S2-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Direct training required for each type.
    - source_id: P8-S2-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Who-question improvement vs no generalization for P2.
    - source_id: P8-S2-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Object-cleft improvement vs no generalization to object-relatives for P2.
    - source_id: P8-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Direct training of object relatives improved production for P2.
    - source_id: P8-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improved for all types.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Who-question improvement vs no generalization for P4.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Object-cleft improvement vs no generalization to object-relatives for P4.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Direct training of object relatives improved production for P4.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improved for all structures.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Production and comprehension maintained at follow-up.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Changes seen on Verb Production Battery.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Improved verb naming and sentence production.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Improvement on Northwestern Sentence Comprehension Test.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Increases in comprehension of actives, passives, and subject relatives.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Changes in narrative discourse.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Increase in MLU and grammatical sentences in narratives.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Increase in verbs with correct argument structure in narratives.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Generalization from object-relatives vs lack of generalization from who-questions.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Lack of generalization from who-questions to object clefts/relatives.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Object-cleft training had no effect on object relatives.
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension improved during treatment.
    - source_id: P12-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Treatment improved narrative language ability.
    - source_id: P12-S2-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Increased utterance length and grammatical sentences in narratives.
    - source_id: P12-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Increased proportion of verbs with correct argument structure in narratives.
    - source_id: P12-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Improved verb naming and sentence production on Verb Production Battery.
    - source_id: P12-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Improved comprehension of all sentence types on Northwestern Sentence Comprehension Test.
    - source_id: P12-S3-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Fewer sessions required for complex forms first.
    - source_id: P12-S3-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Session counts for P1 and P3.
    - source_id: P12-S3-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Session counts for P2 and P4.
    unresolved_coverage:
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C6
    - P5-S1-C8
    - P5-S1-C10
    - P5-S1-C11
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P7-S2-C8
    - P7-S2-C12
    - P7-S2-C13
    - P7-S3-C2
    - P7-S3-C3
    - P7-S3-C4
    - P8-S1-C10
    - P8-S1-C12
    - P8-S1-C14
    - P8-S2-C7
    - P8-S2-C9
    - P8-S2-C12
    - P8-S2-C13
    - P8-S2-C14
    - P9-S1-C8
    - P9-S1-C12
    - P9-S2-C3
    - P9-S2-C4
    - P9-S2-C5
    - P9-S2-C6
    - P10-S1-C4
    - P10-S1-C6
    - P10-S2-C2
    - P10-S2-C5
    - P11-S1-C3
    - P11-S1-C6
    - P11-S1-C7
    - P11-S3-C2
    - P11-S3-C3
    - P11-S3-C9
    - P12-S1-C7
    - P12-S1-C8
    - P12-S2-C4
    - P12-S2-C6
    - P12-S2-C13
    - P12-S3-C8
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-10-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C1
      - P4-S2-C11
      - P6-S2-C4
      - P7-S2-C13
      - P7-S3-C3
      - P11-S1-C5
      - P11-S3-C9
      eligibility:
      - P4-S2-C15
      - P4-S2-C16
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P11-S1-C11
      dependent_variable_statement:
      - P3-S1-C12
      - P6-S2-C9
      - P6-S2-C14
      - P9-S2-C2
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P11-S1-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C15
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C1
      - P4-S2-C11
      - P6-S2-C4
      - P7-S2-C13
      - P7-S3-C3
      - P8-S2-C2
      - P8-S2-C8
      - P8-S2-C12
      - P8-S2-C13
      - P8-S2-C14
      - P8-S2-C16
      - P9-S1-C2
      - P9-S1-C6
      - P9-S2-C3
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S2-C2
      - P10-S2-C3
      - P10-S2-C4
      - P10-S2-C5
      - P11-S1-C5
      - P12-S2-C7
      - P12-S2-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P6-S2-C4
      - P7-S2-C10
      - P8-S1-C3
      - P8-S2-C3
      - P9-S1-C10
      - P9-S2-C2
      - P9-S2-C5
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S2-C2
      - P10-S2-C3
      - P12-S1-C4
      - P12-S1-C7
      - P12-S1-C8
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P6-S2-C9
      - P6-S2-C14
      - P6-S3-C8
      - P6-S3-C9
      - P7-S1-C1
      - P7-S1-C3
      - P7-S2-C8
      - P8-S2-C2
      - P8-S2-C7
      - P8-S2-C9
      - P8-S2-C12
      - P8-S2-C13
      - P8-S2-C14
      - P8-S2-C15
      - P9-S1-C2
      - P9-S2-C2
      - P9-S2-C5
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P10-S1-C7
      - P10-S2-C3
      - P10-S2-C4
      - P11-S1-C6
      - P11-S1-C7
      - P11-S3-C2
      - P12-S1-C4
      - P12-S1-C7
      - P12-S1-C8
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C1
      - P4-S2-C12
      - P4-S2-C13
      - P4-S2-C14
      - P4-S2-C15
      - P4-S2-C16
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P6-S2-C4
      - P11-S1-C5
      - P11-S3-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Object-cleft-first training finding is restricted to Participants 2 and 4.
    binding:
      source_pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      original_source_sha256: e6427dcc43022eb618ea2b0d4bf07fa39582da7430ae5596d0bbd7924a420528
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: training of object-cleft forms
      outcome:
        text: production of object-relative sentences
      analysis_label: Object-cleft training generalization
      relation: treatment_effect
      evidence_ids:
      - P9-S1-C7
      - P11-S1-C2
      qualifier_ids: []
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
        source_review: _compare/relationships-2026-11-16/review-current/Thompson2003
        source_status_sha256: 009442aff235ae288e57b97bd164d8f7febe3055587ebecb6c255a1151b70c0f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: e6427dcc43022eb618ea2b0d4bf07fa39582da7430ae5596d0bbd7924a420528
      source_pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      pdf_pages:
      - 8
      - 9
      note: Object-cleft-first training finding is restricted to Participants 2 and 4.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Object-cleft-first training finding is restricted to Participants 2 and 4.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P9-S1-C7
      - P11-S1-C2
      source_result: For participants H.R. and K.G., training on object-cleft forms resulted in improved production of object-clefts (0% to 100% for H.R., 0% to 100% for K.G.) but did not result in generalization to untrained object-relative sentences, which remained at 0% correct. This lack of generalization is explicitly stated in the discussion as 'training object-cleft forms had no effect on object relatives' for these participants.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: 'The selected analysis correctly identifies the specific comparison: training object-clefts vs. production of object-relatives. The source confirms this was a specific phase in the multiple baseline design for participants H.R. and K.G. (P8-S2-C13, P9-S1-C7).'
          source_ids:
          - P8-S2-C13
          - P9-S1-C7
          - P11-S1-C2
        direction:
          answer: fits
          reason: The claim 'no effect' aligns with the source finding that object-relative production remained at 0% during object-cleft training for the relevant participants, indicating no statistically detected generalization (P9-S1-C7, P11-S1-C2).
          source_ids:
          - P9-S1-C7
          - P11-S1-C2
        construct:
          answer: fits
          reason: Exposure is TUF training on object-clefts; outcome is production of object-relatives. The method is behavioral (sentence production priming), not imaging. The population is individuals with Broca's aphasia/agrammatism. All constructs match the source.
          source_ids:
          - P7-S1-C5
          - P6-S2-C14
          - P4-S2-C11
        qualifications:
          answer: fits
          reason: The qualification regarding the 40% threshold for generalization is correctly included (P7-S2-C9). The limitation of small sample size (N=4) is noted. The finding is specific to the participants who did not show generalization (H.R., K.G.), which is consistent with the source's distinction between participants who did and did not generalize.
          source_ids:
          - P7-S2-C9
          - P4-S2-C11
          - P11-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft correctly limits the 'no effect' claim to the specific context of object-cleft training not generalizing to object-relatives for the relevant participants. It does not overgeneralize to all participants or all sentence types. The source explicitly notes that for other participants (R.M., D.L.), training on more complex forms (object-relatives) *did* generalize to object-clefts, but the reverse (clefts to relatives) did not occur for H.R./K.G. The draft's focus on the 'no effect' direction is faithful to P11-S1-C2.
          source_ids:
          - P11-S1-C2
          - P11-S1-C1
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    original_profile: core
    original_binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      review_sha256: 43bbc24fec5b8c696fe292b23c4e17c81df386e1770eb369fd15244130cd1826
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: "Examination of the data for H.R. and K.G. fur- \nther showed that training object-cleft forms had no ef- \nfect on object relatives."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Object-cleft-first training finding is restricted to Participants 2 and 4. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
