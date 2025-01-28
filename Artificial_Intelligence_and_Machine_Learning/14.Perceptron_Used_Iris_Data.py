# 퍼셉트론 구현하여 class 예측하기

# 필요한 라이브러리 선언
from sklearn.linear_model import Perceptron # 퍼셉트론을 사용하기 위한 라이브러리
from sklearn.datasets import load_iris # iris 데이터를 사용하기 위한 라이브러리 
from sklearn.preprocessing import StandardScaler # 정규화를 사용하기 위한 라이브러리
from sklearn.model_selection import train_test_split # 데이터 셋을 사용하기 위한 라이브러리
from sklearn.metrics import accuracy_score # 두 행렬에 대한 정확도를 측정하기 위한 라이브러리

import numpy as np


# 데이터 불러오기
iris = load_iris() 
X = iris.data # 독립변수
y = iris.target # 종속변수
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 훈련데이터와 테스트데이터를 3:7비율로 나눔


# 데이터 정규화
sc = StandardScaler() # 정규화를 위한 메소드 선언
sc.fit(X_train) # 정규화를 사용하기 위해 훈련데이터를 적합(모수 측정)
X_train_std = sc.transform(X_train) # 훈련데이터 독립변수를 정규화 함
X_test_std = sc.transform(X_test) # 테스트데이터 독립변수를 정규화 함


# 퍼셉트론 모델 생성 및 적합, 예측
pn = Perceptron(max_iter=40, eta0=0.1, random_state=0) # 학습률(eta0) : 0.1 , 훈련세트반복횟수(max_iter) : 40 , Epoch마다 훈련데이터를 썩은 결과가 그대로 재현되도록 값(random_state) 지정
pn.fit(X_train_std, y_train)
y_pred = pn.predict(X_test_std)


# 정확도 출력
# accuracy_score() 함수를 사용하여 두 행렬에 대한 정확도를 측정
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred)) 
