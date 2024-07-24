# path_prediction
#### d_stat_distance +fast_dtw + agglomerative clustering 을 사용한 경로 군집화와 코사인 유사도를 활용한 경로 에측 프로젝트

* 데이터 : gelife trajectory 1.3 (https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/)
* 방법론 : d_stat_distance +fast_dtw + agglomerative clustering & cosine sim
* 요약 : 경로 군집화로 대표 경로를 저장해놓고, 실시간 경로와 가장 유사도가 높은 대표 경로를 이용하여 실시간 경로의 진행 파악.
