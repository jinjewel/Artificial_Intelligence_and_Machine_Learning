# 패키지를 사용하지 않고 직접 과정을 구현하여 만든 K-Means 군집화 구현

# 필요한 라이브러리 선언
from sklearn.datasets import load_iris # 붓꽃 데이터를 가져오기 위한 라이브러리
from matplotlib import pyplot as plt # 그래프 라이브러리
from copy import deepcopy # 참조된 객체 자체를 복사하기 위한 라이브러리

import numpy as np # 행렬 연산을 위한 라이브러리


# 데이터 선언
iris = load_iris()
samples = iris.data # sample 데이러를 생성
x = samples[:,0] # 첫번째 열 데이터를 저장
y = samples[:,1] # 두번째 열 데이터를 저장


# # 1번 데이터 시각화
# plt.figure(1)
# plt.scatter(x, y, alpha=0.5) # 첫번째 열과 두번째 열 변수들 간의 산점도 그리기
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
# plt.show() # 그래프 출력


# 임의의 3개의 중심 위치 배정
# np.random.uniform은 주어진 최소, 최댓값 사이에서 k개만큼 실수 난수를 생성
k = 3
centroids_x = np.random.uniform(min(x), max(x), k) # 랜덤으로 x 좌표 k개 생성
centroids_y = np.random.uniform(min(y), max(y), k) # 랜덤으로 y 좌표 k개 생성
centroids = list(zip(centroids_x, centroids_y)) # 생성한 좌표를 묶어서 리스트로 저장


# # 2번 데이터 시각화
# plt.figure(2)
# plt.scatter(x, y, alpha=0.5) # 실제 데이터를 산점도로 출력
# plt.scatter(centroids_x, centroids_y, marker='D', s=150) # 생성한 3개의 중심 좌표를 주황색 다이아몬드로 표시
# plt.show()


# 새로운 중심 위치로 데이터 배정
def distance(a, b): # a와 b사이의 거리를 구하기 위한 사용자 지정 함수
    return sum([(el_a - el_b)**2 for el_a, el_b in list(zip(a, b))]) ** 0.5

# zeros 함수는 0으로 가득 찬 array를 생성
labels = np.zeros(len(samples)) # 각 데이터 위치를 그룹화할 labels 생성 및 0으로 초기화

sepal_length_width = np.array(list(zip(x, y))) # 실제 데이터의 sepal_length, sepal_width를 묶어서 저장

for i in range(len(samples)): # 각 데이터를 순회하면서 centroids와의 거리 측정
    
    distances = np.zeros(k) # 각 데이터마다 중심까지의 거리 k개를 저장할 행렬 선언, 초기거리는 0으로 초기화
    
    for j in range(k): # 중심의 수만큼 반복
        distances[j] = distance(sepal_length_width[i], centroids[j]) # 해당 실제 데이터와 중심점들 사이의 거리들을 계산하여 distances 행렬에 저장
    
    # np.argmin() 함수는 입력된 행렬 중 가장 작은 값의 index 변환
    cluster = np.argmin(distances) # distances 행렬에 저장된 거리 중 가장 작은 거리의 인덱스를 저장
    labels[i] = cluster # 전체 데이터에 대한 새롭게 할당될 군집을 표시하기 위한 labels 행렬에 각 번호 당 할당된 군집의 번호를 저장
    
    
# # 3번 시각화
# plt.figure(3)
# plt.scatter(x, y, c=labels, alpha=0.5) # 새롭게 할당된 군집의 번호로 실제 데이터를 표시
# plt.scatter(centroids_x, centroids_y, c='red', marker='D', s=150) # 3개의 중심 좌표를 빨간색 다이아몬드로 표시
# plt.show()


# 중심 위치 갱신
centroids_old = np.array(deepcopy(centroids)) # 이전 중심을 깊은 복사를 통해 옛_중심에 저장
centroids_new = np.array(deepcopy(centroids)) # 이전 중심을 깊은 복사를 통해 새로운_중심에 저장

for i in range(k): # 중심의 수만큼 반복
    # 각 그룹에 속한 데이터만 골라 points에 저장한다
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    # points의 각 feature, 즉 각 좌표의 평균 지점을 centroid로 지정 
    centroids_new[i] = np.mean(points, axis=0)


# # 4번 그래프 출력
# plt.figure(4)
# plt.scatter(x, y, c=labels, alpha=0.5) # 새롭게 군집한 데이터 표시
# plt.scatter(centroids_old[:,0], centroids_old[:,1], c='blue', marker='D', s=150) # 옛 중심점을 파란색 다이아몬드 표시
# plt.scatter(centroids_new[:,0], centroids_new[:,1], c='red', marker='s', s=150) # 새롭게 생성한 중심점을 빨간색 사각형 표시
# plt.show()


# 중심점의 위치가 최적이 되도록 반복
centroids_old = np.zeros(np.array(centroids_new).shape) # 새로운 중심점을 저장할 행렬의 크기 만큼 0행렬 생성
labels = np.zeros(len(samples)) # 해당 데이터가 속할 군집을 표현하기 위해서 전체 데이터 수만큼의 0행렬 생성
error = np.zeros(k) # 각 군집별 error를 저장할 군집 개수만큼의 0행렬 저장, stop rule이 된다.

# 초기 에러 계산
for i in range(k):
    error[i] = distance(centroids_old[i], centroids_new[i])  

# error가 0에 수렴할 때까지 2~3단계 반복
while(error.all() != 0): 
    # STEP 2 : 가까운 centroids에 데이터를 할당
    for i in range(len(samples)):
        distances = np.zeros(k) # 초기거리는 모두 0으로 초기화
        for j in range(k):
            distances[j] = distance(sepal_length_width[i], centroids_new[j])
        cluster = np.argmin(distances) # np.argmin은 가장 작은 값의 index를 반환
        labels[i] = cluster
    # STEP 3 : centroids 업데이트
    centroids_old = deepcopy(centroids_new)
    for i in range(k):
        # 각 그룹에 속한 데이터들만 골라 points에 저장
        points = [ sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i ]
        # points의 각 features, 각 좌표의 평균 지점을 centroid로 지정
        centroids_new[i] = np.mean(points, axis=0)
    # 새롭게 centroids를 업데이트 했으니 error를 다시 계산
    for i in range(k):
        error[i] = distance(centroids_old[i], centroids_new[i])


# 5번째 그림 출력
plt.figure(5)
colors = ['r', 'g', 'b']
for i in range(k):
    points = np.array([sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i])
    plt.scatter(points[:,0], points[:,1], c=colors[i], alpha=0.5)
plt.scatter(centroids_new[:,0], centroids_new[:,1], marker='D', s=150) # 새롭게 만들어진 중심점을 파란색 다이아몬드로 표시    
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()
