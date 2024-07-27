---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: Dmeta-embedding
  results:
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 65.60825224706932
    - type: cos_sim_spearman
      value: 71.12862586297193
    - type: euclidean_pearson
      value: 70.18130275750404
    - type: euclidean_spearman
      value: 71.12862586297193
    - type: manhattan_pearson
      value: 70.14470398075396
    - type: manhattan_spearman
      value: 71.05226975911737
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 65.52386345655479
    - type: cos_sim_spearman
      value: 64.64245253181382
    - type: euclidean_pearson
      value: 73.20157662981914
    - type: euclidean_spearman
      value: 64.64245253178956
    - type: manhattan_pearson
      value: 73.22837571756348
    - type: manhattan_spearman
      value: 64.62632334391418
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 44.925999999999995
    - type: f1
      value: 42.82555191308971
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 71.35236446393156
    - type: cos_sim_spearman
      value: 72.29629643702184
    - type: euclidean_pearson
      value: 70.94570179874498
    - type: euclidean_spearman
      value: 72.29629297226953
    - type: manhattan_pearson
      value: 70.84463025501125
    - type: manhattan_spearman
      value: 72.24527021975821
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 40.24232916894152
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 39.167806226929706
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 88.48837920106357
    - type: mrr
      value: 90.36861111111111
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 89.17878171657071
    - type: mrr
      value: 91.35805555555555
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 25.751
    - type: map_at_10
      value: 38.946
    - type: map_at_100
      value: 40.855000000000004
    - type: map_at_1000
      value: 40.953
    - type: map_at_3
      value: 34.533
    - type: map_at_5
      value: 36.905
    - type: mrr_at_1
      value: 39.235
    - type: mrr_at_10
      value: 47.713
    - type: mrr_at_100
      value: 48.71
    - type: mrr_at_1000
      value: 48.747
    - type: mrr_at_3
      value: 45.086
    - type: mrr_at_5
      value: 46.498
    - type: ndcg_at_1
      value: 39.235
    - type: ndcg_at_10
      value: 45.831
    - type: ndcg_at_100
      value: 53.162
    - type: ndcg_at_1000
      value: 54.800000000000004
    - type: ndcg_at_3
      value: 40.188
    - type: ndcg_at_5
      value: 42.387
    - type: precision_at_1
      value: 39.235
    - type: precision_at_10
      value: 10.273
    - type: precision_at_100
      value: 1.627
    - type: precision_at_1000
      value: 0.183
    - type: precision_at_3
      value: 22.772000000000002
    - type: precision_at_5
      value: 16.524
    - type: recall_at_1
      value: 25.751
    - type: recall_at_10
      value: 57.411
    - type: recall_at_100
      value: 87.44
    - type: recall_at_1000
      value: 98.386
    - type: recall_at_3
      value: 40.416000000000004
    - type: recall_at_5
      value: 47.238
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 83.59591100420926
    - type: cos_sim_ap
      value: 90.65538153970263
    - type: cos_sim_f1
      value: 84.76466651795673
    - type: cos_sim_precision
      value: 81.04073363190446
    - type: cos_sim_recall
      value: 88.84732288987608
    - type: dot_accuracy
      value: 83.59591100420926
    - type: dot_ap
      value: 90.64355541781003
    - type: dot_f1
      value: 84.76466651795673
    - type: dot_precision
      value: 81.04073363190446
    - type: dot_recall
      value: 88.84732288987608
    - type: euclidean_accuracy
      value: 83.59591100420926
    - type: euclidean_ap
      value: 90.6547878194287
    - type: euclidean_f1
      value: 84.76466651795673
    - type: euclidean_precision
      value: 81.04073363190446
    - type: euclidean_recall
      value: 88.84732288987608
    - type: manhattan_accuracy
      value: 83.51172579675286
    - type: manhattan_ap
      value: 90.59941589844144
    - type: manhattan_f1
      value: 84.51827242524917
    - type: manhattan_precision
      value: 80.28613507258574
    - type: manhattan_recall
      value: 89.22141688099134
    - type: max_accuracy
      value: 83.59591100420926
    - type: max_ap
      value: 90.65538153970263
    - type: max_f1
      value: 84.76466651795673
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 63.251000000000005
    - type: map_at_10
      value: 72.442
    - type: map_at_100
      value: 72.79299999999999
    - type: map_at_1000
      value: 72.80499999999999
    - type: map_at_3
      value: 70.293
    - type: map_at_5
      value: 71.571
    - type: mrr_at_1
      value: 63.541000000000004
    - type: mrr_at_10
      value: 72.502
    - type: mrr_at_100
      value: 72.846
    - type: mrr_at_1000
      value: 72.858
    - type: mrr_at_3
      value: 70.39
    - type: mrr_at_5
      value: 71.654
    - type: ndcg_at_1
      value: 63.541000000000004
    - type: ndcg_at_10
      value: 76.774
    - type: ndcg_at_100
      value: 78.389
    - type: ndcg_at_1000
      value: 78.678
    - type: ndcg_at_3
      value: 72.47
    - type: ndcg_at_5
      value: 74.748
    - type: precision_at_1
      value: 63.541000000000004
    - type: precision_at_10
      value: 9.115
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 26.379
    - type: precision_at_5
      value: 16.965
    - type: recall_at_1
      value: 63.251000000000005
    - type: recall_at_10
      value: 90.253
    - type: recall_at_100
      value: 97.576
    - type: recall_at_1000
      value: 99.789
    - type: recall_at_3
      value: 78.635
    - type: recall_at_5
      value: 84.141
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 23.597
    - type: map_at_10
      value: 72.411
    - type: map_at_100
      value: 75.58500000000001
    - type: map_at_1000
      value: 75.64800000000001
    - type: map_at_3
      value: 49.61
    - type: map_at_5
      value: 62.527
    - type: mrr_at_1
      value: 84.65
    - type: mrr_at_10
      value: 89.43900000000001
    - type: mrr_at_100
      value: 89.525
    - type: mrr_at_1000
      value: 89.529
    - type: mrr_at_3
      value: 89
    - type: mrr_at_5
      value: 89.297
    - type: ndcg_at_1
      value: 84.65
    - type: ndcg_at_10
      value: 81.47
    - type: ndcg_at_100
      value: 85.198
    - type: ndcg_at_1000
      value: 85.828
    - type: ndcg_at_3
      value: 79.809
    - type: ndcg_at_5
      value: 78.55
    - type: precision_at_1
      value: 84.65
    - type: precision_at_10
      value: 39.595
    - type: precision_at_100
      value: 4.707
    - type: precision_at_1000
      value: 0.485
    - type: precision_at_3
      value: 71.61699999999999
    - type: precision_at_5
      value: 60.45
    - type: recall_at_1
      value: 23.597
    - type: recall_at_10
      value: 83.34
    - type: recall_at_100
      value: 95.19800000000001
    - type: recall_at_1000
      value: 98.509
    - type: recall_at_3
      value: 52.744
    - type: recall_at_5
      value: 68.411
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 53.1
    - type: map_at_10
      value: 63.359
    - type: map_at_100
      value: 63.9
    - type: map_at_1000
      value: 63.909000000000006
    - type: map_at_3
      value: 60.95
    - type: map_at_5
      value: 62.305
    - type: mrr_at_1
      value: 53.1
    - type: mrr_at_10
      value: 63.359
    - type: mrr_at_100
      value: 63.9
    - type: mrr_at_1000
      value: 63.909000000000006
    - type: mrr_at_3
      value: 60.95
    - type: mrr_at_5
      value: 62.305
    - type: ndcg_at_1
      value: 53.1
    - type: ndcg_at_10
      value: 68.418
    - type: ndcg_at_100
      value: 70.88499999999999
    - type: ndcg_at_1000
      value: 71.135
    - type: ndcg_at_3
      value: 63.50599999999999
    - type: ndcg_at_5
      value: 65.92
    - type: precision_at_1
      value: 53.1
    - type: precision_at_10
      value: 8.43
    - type: precision_at_100
      value: 0.955
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 23.633000000000003
    - type: precision_at_5
      value: 15.340000000000002
    - type: recall_at_1
      value: 53.1
    - type: recall_at_10
      value: 84.3
    - type: recall_at_100
      value: 95.5
    - type: recall_at_1000
      value: 97.5
    - type: recall_at_3
      value: 70.89999999999999
    - type: recall_at_5
      value: 76.7
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 48.303193535975375
    - type: f1
      value: 35.96559358693866
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 85.06566604127579
    - type: ap
      value: 52.0596483757231
    - type: f1
      value: 79.5196835127668
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 74.48499423626059
    - type: cos_sim_spearman
      value: 78.75806756061169
    - type: euclidean_pearson
      value: 78.47917601852879
    - type: euclidean_spearman
      value: 78.75807199272622
    - type: manhattan_pearson
      value: 78.40207586289772
    - type: manhattan_spearman
      value: 78.6911776964119
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/Mmarco-reranking
      name: MTEB MMarcoReranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 24.75987466552363
    - type: mrr
      value: 23.40515873015873
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 58.026999999999994
    - type: map_at_10
      value: 67.50699999999999
    - type: map_at_100
      value: 67.946
    - type: map_at_1000
      value: 67.96600000000001
    - type: map_at_3
      value: 65.503
    - type: map_at_5
      value: 66.649
    - type: mrr_at_1
      value: 60.20100000000001
    - type: mrr_at_10
      value: 68.271
    - type: mrr_at_100
      value: 68.664
    - type: mrr_at_1000
      value: 68.682
    - type: mrr_at_3
      value: 66.47800000000001
    - type: mrr_at_5
      value: 67.499
    - type: ndcg_at_1
      value: 60.20100000000001
    - type: ndcg_at_10
      value: 71.697
    - type: ndcg_at_100
      value: 73.736
    - type: ndcg_at_1000
      value: 74.259
    - type: ndcg_at_3
      value: 67.768
    - type: ndcg_at_5
      value: 69.72
    - type: precision_at_1
      value: 60.20100000000001
    - type: precision_at_10
      value: 8.927999999999999
    - type: precision_at_100
      value: 0.9950000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 25.883
    - type: precision_at_5
      value: 16.55
    - type: recall_at_1
      value: 58.026999999999994
    - type: recall_at_10
      value: 83.966
    - type: recall_at_100
      value: 93.313
    - type: recall_at_1000
      value: 97.426
    - type: recall_at_3
      value: 73.342
    - type: recall_at_5
      value: 77.997
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 71.1600537995965
    - type: f1
      value: 68.8126216609964
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.54068594485541
    - type: f1
      value: 73.46845879869848
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 54.900000000000006
    - type: map_at_10
      value: 61.363
    - type: map_at_100
      value: 61.924
    - type: map_at_1000
      value: 61.967000000000006
    - type: map_at_3
      value: 59.767
    - type: map_at_5
      value: 60.802
    - type: mrr_at_1
      value: 55.1
    - type: mrr_at_10
      value: 61.454
    - type: mrr_at_100
      value: 62.016000000000005
    - type: mrr_at_1000
      value: 62.059
    - type: mrr_at_3
      value: 59.882999999999996
    - type: mrr_at_5
      value: 60.893
    - type: ndcg_at_1
      value: 54.900000000000006
    - type: ndcg_at_10
      value: 64.423
    - type: ndcg_at_100
      value: 67.35900000000001
    - type: ndcg_at_1000
      value: 68.512
    - type: ndcg_at_3
      value: 61.224000000000004
    - type: ndcg_at_5
      value: 63.083
    - type: precision_at_1
      value: 54.900000000000006
    - type: precision_at_10
      value: 7.3999999999999995
    - type: precision_at_100
      value: 0.882
    - type: precision_at_1000
      value: 0.097
    - type: precision_at_3
      value: 21.8
    - type: precision_at_5
      value: 13.98
    - type: recall_at_1
      value: 54.900000000000006
    - type: recall_at_10
      value: 74
    - type: recall_at_100
      value: 88.2
    - type: recall_at_1000
      value: 97.3
    - type: recall_at_3
      value: 65.4
    - type: recall_at_5
      value: 69.89999999999999
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 75.15666666666667
    - type: f1
      value: 74.8306375354435
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 83.10774228478614
    - type: cos_sim_ap
      value: 87.17679348388666
    - type: cos_sim_f1
      value: 84.59302325581395
    - type: cos_sim_precision
      value: 78.15577439570276
    - type: cos_sim_recall
      value: 92.18585005279832
    - type: dot_accuracy
      value: 83.10774228478614
    - type: dot_ap
      value: 87.17679348388666
    - type: dot_f1
      value: 84.59302325581395
    - type: dot_precision
      value: 78.15577439570276
    - type: dot_recall
      value: 92.18585005279832
    - type: euclidean_accuracy
      value: 83.10774228478614
    - type: euclidean_ap
      value: 87.17679348388666
    - type: euclidean_f1
      value: 84.59302325581395
    - type: euclidean_precision
      value: 78.15577439570276
    - type: euclidean_recall
      value: 92.18585005279832
    - type: manhattan_accuracy
      value: 82.67460747157553
    - type: manhattan_ap
      value: 86.94296334435238
    - type: manhattan_f1
      value: 84.32327166504382
    - type: manhattan_precision
      value: 78.22944896115628
    - type: manhattan_recall
      value: 91.4466737064414
    - type: max_accuracy
      value: 83.10774228478614
    - type: max_ap
      value: 87.17679348388666
    - type: max_f1
      value: 84.59302325581395
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 93.24999999999999
    - type: ap
      value: 90.98617641063584
    - type: f1
      value: 93.23447883650289
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 41.071417937737856
    - type: cos_sim_spearman
      value: 45.049199344455424
    - type: euclidean_pearson
      value: 44.913450096830786
    - type: euclidean_spearman
      value: 45.05733424275291
    - type: manhattan_pearson
      value: 44.881623825912065
    - type: manhattan_spearman
      value: 44.989923561416596
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 41.38238052689359
    - type: cos_sim_spearman
      value: 42.61949690594399
    - type: euclidean_pearson
      value: 40.61261500356766
    - type: euclidean_spearman
      value: 42.619626605620724
    - type: manhattan_pearson
      value: 40.8886109204474
    - type: manhattan_spearman
      value: 42.75791523010463
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 62.10977863727196
    - type: cos_sim_spearman
      value: 63.843727112473225
    - type: euclidean_pearson
      value: 63.25133487817196
    - type: euclidean_spearman
      value: 63.843727112473225
    - type: manhattan_pearson
      value: 63.58749018644103
    - type: manhattan_spearman
      value: 63.83820575456674
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 79.30616496720054
    - type: cos_sim_spearman
      value: 80.767935782436
    - type: euclidean_pearson
      value: 80.4160642670106
    - type: euclidean_spearman
      value: 80.76820284024356
    - type: manhattan_pearson
      value: 80.27318714580251
    - type: manhattan_spearman
      value: 80.61030164164964
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 66.26242871142425
    - type: mrr
      value: 76.20689863623174
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.240999999999996
    - type: map_at_10
      value: 73.009
    - type: map_at_100
      value: 76.893
    - type: map_at_1000
      value: 76.973
    - type: map_at_3
      value: 51.339
    - type: map_at_5
      value: 63.003
    - type: mrr_at_1
      value: 87.458
    - type: mrr_at_10
      value: 90.44
    - type: mrr_at_100
      value: 90.558
    - type: mrr_at_1000
      value: 90.562
    - type: mrr_at_3
      value: 89.89
    - type: mrr_at_5
      value: 90.231
    - type: ndcg_at_1
      value: 87.458
    - type: ndcg_at_10
      value: 81.325
    - type: ndcg_at_100
      value: 85.61999999999999
    - type: ndcg_at_1000
      value: 86.394
    - type: ndcg_at_3
      value: 82.796
    - type: ndcg_at_5
      value: 81.219
    - type: precision_at_1
      value: 87.458
    - type: precision_at_10
      value: 40.534
    - type: precision_at_100
      value: 4.96
    - type: precision_at_1000
      value: 0.514
    - type: precision_at_3
      value: 72.444
    - type: precision_at_5
      value: 60.601000000000006
    - type: recall_at_1
      value: 26.240999999999996
    - type: recall_at_10
      value: 80.42
    - type: recall_at_100
      value: 94.118
    - type: recall_at_1000
      value: 98.02199999999999
    - type: recall_at_3
      value: 53.174
    - type: recall_at_5
      value: 66.739
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 52.40899999999999
    - type: f1
      value: 50.68532128056062
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 65.57616085176686
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 58.844999922904925
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 58.4
    - type: map_at_10
      value: 68.64
    - type: map_at_100
      value: 69.062
    - type: map_at_1000
      value: 69.073
    - type: map_at_3
      value: 66.567
    - type: map_at_5
      value: 67.89699999999999
    - type: mrr_at_1
      value: 58.4
    - type: mrr_at_10
      value: 68.64
    - type: mrr_at_100
      value: 69.062
    - type: mrr_at_1000
      value: 69.073
    - type: mrr_at_3
      value: 66.567
    - type: mrr_at_5
      value: 67.89699999999999
    - type: ndcg_at_1
      value: 58.4
    - type: ndcg_at_10
      value: 73.30600000000001
    - type: ndcg_at_100
      value: 75.276
    - type: ndcg_at_1000
      value: 75.553
    - type: ndcg_at_3
      value: 69.126
    - type: ndcg_at_5
      value: 71.519
    - type: precision_at_1
      value: 58.4
    - type: precision_at_10
      value: 8.780000000000001
    - type: precision_at_100
      value: 0.968
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 25.5
    - type: precision_at_5
      value: 16.46
    - type: recall_at_1
      value: 58.4
    - type: recall_at_10
      value: 87.8
    - type: recall_at_100
      value: 96.8
    - type: recall_at_1000
      value: 99
    - type: recall_at_3
      value: 76.5
    - type: recall_at_5
      value: 82.3
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 86.21000000000001
    - type: ap
      value: 69.17460264576461
    - type: f1
      value: 84.68032984659226
license: apache-2.0
language:
- zh
- en
---

<div align="center">
<img src="logo.png" alt="icon" width="100px"/>
</div>

<h1 align="center">Dmeta-embedding</h1>
<h4 align="center">
    <p>
      <a href="https://huggingface.co/DMetaSoul/Dmeta-embedding/README.md">English</a>  |
      <a href="https://huggingface.co/DMetaSoul/Dmeta-embedding/blob/main/README_zh.md">中文</a>
    </p>
    <p>
        <a href=#usage>用法</a>  |
        <a href="#evaluation">评测（可复现）</a> |
        <a href=#faq>FAQ</a> |
        <a href="#contact">联系</a> |
        <a href="#license">版权（免费商用）</a> 
    <p>
</h4>

**重磅更新：**

- **2024.02.07**, 发布了基于 Dmeta-embedding 模型的 **Embedding API** 产品，现已开启内测，[点击申请](https://dmetasoul.feishu.cn/share/base/form/shrcnu7mN1BDwKFfgGXG9Rb1yDf)即可免费获得 **4 亿 tokens** 使用额度，可编码大约 GB 级别汉字文本。

    - 我们的初心。既要开源优秀的技术能力，又希望大家能够在实际业务中使用起来，用起来的技术才是好技术、能落地创造价值的技术才是值得长期投入的。帮助大家解决业务落地最后一公里的障碍，让大家把 Embedding 技术低成本的用起来，更多去关注自身的商业和产品服务，把复杂的技术部分交给我们。
    - 申请和使用。[点击申请](https://dmetasoul.feishu.cn/share/base/form/shrcnu7mN1BDwKFfgGXG9Rb1yDf)，填写一个表单即可，48小时之内我们会通过 <aigc@dmetasoul.com> 给您答复邮件。Embedding API 为了兼容大模型技术生态，使用方式跟 OpenAI 一致，具体用法我们将在答复邮件中进行说明。
    - 加入社群。后续我们会不断在大模型/AIGC等方向发力，为社区带来有价值、低门槛的技术，可以[点击图片](https://huggingface.co/DMetaSoul/Dmeta-embedding/resolve/main/weixin.jpeg)，扫面二维码来加入我们的微信社群，一起在 AIGC 赛道加油呀！

------

**Dmeta-embedding** 是一款跨领域、跨任务、开箱即用的中文 Embedding 模型，适用于搜索、问答、智能客服、LLM+RAG 等各种业务场景，支持使用 Transformers/Sentence-Transformers/Langchain 等工具加载推理。

优势特点如下：

- 多任务、场景泛化性能优异，目前已取得 **[MTEB](https://huggingface.co/spaces/mteb/leaderboard) 中文榜单第二成绩**（2024.01.25）
- 模型参数大小仅 **400MB**，对比参数量超过 GB 级模型，可以极大降低推理成本
- 支持上下文窗口长度达到 **1024**，对于长文本检索、RAG 等场景更适配

## Usage

目前模型支持通过 [Sentence-Transformers](#sentence-transformers), [Langchain](#langchain), [Huggingface Transformers](#huggingface-transformers) 等主流框架进行推理，具体用法参考各个框架的示例。

### Sentence-Transformers

Dmeta-embedding 模型支持通过 [sentence-transformers](https://www.SBERT.net) 来加载推理：

```
pip install -U sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

texts1 = ["胡子长得太快怎么办？", "在香港哪里买手表好"]
texts2 = ["胡子长得快怎么办？", "怎样使胡子不浓密！", "香港买手表哪里好", "在杭州手机到哪里买"]

model = SentenceTransformer('DMetaSoul/Dmeta-embedding')
embs1 = model.encode(texts1, normalize_embeddings=True)
embs2 = model.encode(texts2, normalize_embeddings=True)

# 计算两两相似度
similarity = embs1 @ embs2.T
print(similarity)

# 获取 texts1[i] 对应的最相似 texts2[j]
for i in range(len(texts1)):
    scores = []
    for j in range(len(texts2)):
        scores.append([texts2[j], similarity[i][j]])
    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    print(f"查询文本：{texts1[i]}")
    for text2, score in scores:
        print(f"相似文本：{text2}，打分：{score}")
    print()
```

示例输出如下：

```
查询文本：胡子长得太快怎么办？
相似文本：胡子长得快怎么办？，打分：0.9535336494445801
相似文本：怎样使胡子不浓密！，打分：0.6776421070098877
相似文本：香港买手表哪里好，打分：0.2297907918691635
相似文本：在杭州手机到哪里买，打分：0.11386542022228241

查询文本：在香港哪里买手表好
相似文本：香港买手表哪里好，打分：0.9843372106552124
相似文本：在杭州手机到哪里买，打分：0.45211508870124817
相似文本：胡子长得快怎么办？，打分：0.19985519349575043
相似文本：怎样使胡子不浓密！，打分：0.18558596074581146
```

### Langchain

Dmeta-embedding 模型支持通过 LLM 工具框架 [langchain](https://www.langchain.com/) 来加载推理：

```
pip install -U langchain
```

```python
import torch
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings

model_name = "DMetaSoul/Dmeta-embedding"
model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)

texts1 = ["胡子长得太快怎么办？", "在香港哪里买手表好"]
texts2 = ["胡子长得快怎么办？", "怎样使胡子不浓密！", "香港买手表哪里好", "在杭州手机到哪里买"]

embs1 = model.embed_documents(texts1)
embs2 = model.embed_documents(texts2)
embs1, embs2 = np.array(embs1), np.array(embs2)

# 计算两两相似度
similarity = embs1 @ embs2.T
print(similarity)

# 获取 texts1[i] 对应的最相似 texts2[j]
for i in range(len(texts1)):
    scores = []
    for j in range(len(texts2)):
        scores.append([texts2[j], similarity[i][j]])
    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    print(f"查询文本：{texts1[i]}")
    for text2, score in scores:
        print(f"相似文本：{text2}，打分：{score}")
    print()
```

### HuggingFace Transformers

Dmeta-embedding 模型支持通过 [HuggingFace Transformers](https://huggingface.co/docs/transformers/index) 框架来加载推理：

```
pip install -U transformers
```

```python
import torch
from transformers import AutoTokenizer, AutoModel


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def cls_pooling(model_output):
    return model_output[0][:, 0]


texts1 = ["胡子长得太快怎么办？", "在香港哪里买手表好"]
texts2 = ["胡子长得快怎么办？", "怎样使胡子不浓密！", "香港买手表哪里好", "在杭州手机到哪里买"]

tokenizer = AutoTokenizer.from_pretrained('DMetaSoul/Dmeta-embedding')
model = AutoModel.from_pretrained('DMetaSoul/Dmeta-embedding')
model.eval()

with torch.no_grad():
    inputs1 = tokenizer(texts1, padding=True, truncation=True, return_tensors='pt')
    inputs2 = tokenizer(texts2, padding=True, truncation=True, return_tensors='pt')

    model_output1 = model(**inputs1)
    model_output2 = model(**inputs2)
    embs1, embs2 = cls_pooling(model_output1), cls_pooling(model_output2)
    embs1 = torch.nn.functional.normalize(embs1, p=2, dim=1).numpy()
    embs2 = torch.nn.functional.normalize(embs2, p=2, dim=1).numpy()

# 计算两两相似度
similarity = embs1 @ embs2.T
print(similarity)

# 获取 texts1[i] 对应的最相似 texts2[j]
for i in range(len(texts1)):
    scores = []
    for j in range(len(texts2)):
        scores.append([texts2[j], similarity[i][j]])
    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    print(f"查询文本：{texts1[i]}")
    for text2, score in scores:
        print(f"相似文本：{text2}，打分：{score}")
    print()
```

## Evaluation

Dmeta-embedding 模型在 [MTEB 中文榜单](https://huggingface.co/spaces/mteb/leaderboard)取得开源第一的成绩（2024.01.25，Baichuan 榜单第一、未开源），具体关于评测数据和代码可参考 MTEB 官方[仓库](https://github.com/embeddings-benchmark/mteb)。

**MTEB Chinese**:   

该[榜单数据集](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB)由智源研究院团队（BAAI）收集整理，包含 6 个经典任务共计 35 个中文数据集，涵盖了分类、检索、排序、句对、STS 等任务，是目前 Embedding 模型全方位能力评测的全球权威榜单。

| Model                                                                                                    | Vendor | Embedding dimension | Avg   | Retrieval | STS   | PairClassification | Classification | Reranking | Clustering |
|:-------------------------------------------------------------------------------------------------------- | ------ |:-------------------:|:-----:|:---------:|:-----:|:------------------:|:--------------:|:---------:|:----------:|
| [Dmeta-embedding](https://huggingface.co/DMetaSoul/Dmeta-embedding)                                      | 数元灵    | 768                | 67.51 | 70.41     | 64.09 | 88.92              | 70             | 67.17     | 50.96      |
| [gte-large-zh](https://huggingface.co/thenlper/gte-large-zh)                                             | 阿里达摩院  | 1024                | 66.72 | 72.49     | 57.82 | 84.41              | 71.34          | 67.4      | 53.07      |
| [BAAI/bge-large-zh-v1.5](https://huggingface.co/BAAI/bge-large-zh-v1.5)                                  | 智源     | 1024                | 64.53 | 70.46     | 56.25 | 81.6               | 69.13          | 65.84     | 48.99      |
| [BAAI/bge-base-zh-v1.5](https://huggingface.co/BAAI/bge-base-zh-v1.5)                                    | 智源     | 768                 | 63.13 | 69.49     | 53.72 | 79.75              | 68.07          | 65.39     | 47.53      |
| [text-embedding-ada-002(OpenAI)](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) | OpenAI | 1536                | 53.02 | 52.0      | 43.35 | 69.56              | 64.31          | 54.28     | 45.68      |
| [text2vec-base](https://huggingface.co/shibing624/text2vec-base-chinese)                                 | 个人     | 768                 | 47.63 | 38.79     | 43.41 | 67.41              | 62.19          | 49.45     | 37.66      |
| [text2vec-large](https://huggingface.co/GanymedeNil/text2vec-large-chinese)                              | 个人     | 1024                | 47.36 | 41.94     | 44.97 | 70.86              | 60.66          | 49.16     | 30.02      |

## FAQ

<details>
  <summary>1. 为何模型多任务、场景泛化能力优异，可开箱即用适配诸多应用场景？</summary>

<!-- ### 为何模型多任务、场景泛化能力优异，可开箱即用适配诸多应用场景？ -->

简单来说，模型优异的泛化能力来自于预训练数据的广泛和多样，以及模型优化时面向多任务场景设计了不同优化目标。

具体来说，技术要点有：

1）首先是大规模弱标签对比学习。业界经验表明开箱即用的语言模型在 Embedding 相关任务上表现不佳，但由于监督数据标注、获取成本较高，因此大规模、高质量的弱标签学习成为一条可选技术路线。通过在互联网上论坛、新闻、问答社区、百科等半结构化数据中提取弱标签，并利用大模型进行低质过滤，得到 10 亿级别弱监督文本对数据。

2）其次是高质量监督学习。我们收集整理了大规模开源标注的语句对数据集，包含百科、教育、金融、医疗、法律、新闻、学术等多个领域共计 3000 万句对样本。同时挖掘难负样本对，借助对比学习更好的进行模型优化。

3）最后是检索任务针对性优化。考虑到搜索、问答以及 RAG 等场景是 Embedding 模型落地的重要应用阵地，为了增强模型跨领域、跨场景的效果性能，我们专门针对检索任务进行了模型优化，核心在于从问答、检索等数据中挖掘难负样本，借助稀疏和稠密检索等多种手段，构造百万级难负样本对数据集，显著提升了模型跨领域的检索性能。

</details>

<details>
  <summary>2. 模型可以商用吗？</summary>

<!-- ### 模型可以商用吗 -->

我们的开源模型基于 Apache-2.0 协议，完全支持免费商用。

</details>

<details>
  <summary>3. 如何复现 MTEB 评测结果？</summary>

<!-- ### 如何复现 MTEB 评测结果？ -->

我们在模型仓库中提供了脚本 mteb_eval.py，您可以直接运行此脚本来复现我们的评测结果。

</details>

<details>
  <summary>4. 后续规划有哪些？</summary>

<!-- ### 后续规划有哪些？ -->

我们将不断致力于为社区提供效果优异、推理轻量、多场景开箱即用的 Embedding 模型，同时我们也会将 Embedding 逐步整合到目前已经的技术生态中，跟随社区一起成长！

</details>

## Contact

您如果在使用过程中，遇到任何问题，欢迎前往[讨论区](https://huggingface.co/DMetaSoul/Dmeta-embedding/discussions)建言献策。

您也可以联系我们：赵中昊 <zhongh@dmetasoul.com>, 肖文斌 <xiaowenbin@dmetasoul.com>, 孙凯 <sunkai@dmetasoul.com>

同时我们也开通了微信群，可扫码加入我们（人数超200了，先加管理员再拉进群），一起共建 AIGC 技术生态！

<image src="https://huggingface.co/DMetaSoul/Dmeta-embedding/resolve/main/weixin.jpeg" style="display: block; margin-left: auto; margin-right: auto; width: 256px; height: 358px;"/>

## License

Dmeta-embedding 模型采用 Apache-2.0 License，开源模型可以进行免费商用私有部署。