# path_prediction
### 커스텀한 fast_dtw + agglomerative clustering 을 사용한 경로 군집화와 코사인 유사도를 활용한 경로 에측 프로젝트


<p align="center">
<img width="796" alt="Screenshot 2024-07-24 at 12 55 39 PM" src="https://github.com/user-attachments/assets/e5a7e2bd-440e-4c1e-b8ea-0820f1bcc582">
</p>
<p align="center">
  -- fig 1. 군집화된 유사경로들. --
</p>
<br/><br/>
* 데이터 : gelife trajectory 1.3 (https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/)
* 방법론 : d_stat_distance +fast_dtw + agglomerative clustering & cosine sim
* 개발언어 : python3
* 요약 : 경로 군집화로 대표 경로를 저장해놓고, 실시간 경로와 가장 유사도가 높은 대표 경로를 이용하여 실시간 경로의 진행 파악.
