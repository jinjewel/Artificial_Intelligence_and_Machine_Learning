## 로지스틱 회귀를 이용한 생존분석 구현


# 필요 패키지 선언
from sklearn.linear_model import LogisticRegression # 로지스틱회귀분석을 이용하기 위한 라이브러리
from sklearn.model_selection import train_test_split # 데이터 분할을 위한 라이브러리
from sklearn.preprocessing import StandardScaler # 정규화를 위한 라이브러리
import pandas as pd # 타이타닉 데이터를 가져오기 위한 라이브러리
import numpy as np # 행렬 데이터를 다루기 위한 라이브러리


# 데이터 불러오기
passengers = pd.read_csv('2.Titanic_train.csv')
print(passengers.shape) # 데이터의 행, 열 개수 확인하기
print(passengers.head()) #컬럼확인


# 데이터 전처리
passengers['Sex'] = passengers['Sex'].map({'female':1,'male':0}) # 문자열 데이터를 숫자로 변환
passengers['Age'].fillna(value=passengers['Age'].mean(), inplace=True) # 결측치 채우기
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0) # 좌적 중 1등급 좌석 필드 추가
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0) # 좌석 중 2등급 좌석 필드 추가
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']] # 독립변수 열을 따로 저장
survival = passengers['Survived'] # 종속변수 열을 따로 저장


# 학습 데이터와 테스트 데이터 분리
train_features, test_features, train_labels, test_labels = train_test_split(features, survival)


# 정규화
scaler = StandardScaler() # 평균 0, 표준편차 1로 정규화 함수 가져오기
train_features = scaler.fit_transform(train_features) # 열이 여러 개일 때 정규화 
test_features = scaler.transform(test_features) # 열이 한 개일 때 정규화


# 모델생성 및 적합
model = LogisticRegression(random_state = 0, solver='lbfgs')
model.fit(train_features, train_labels)


# 모델 적합 결과 출력
print(model.score(train_features, train_labels)) # 학습데이터 정확도 출력
print(model.score(test_features, test_labels)) # 테스트 데이터 정확도 출력
print(model.coef_) # 특징의 계수 확인 : 어던 특징이 생존에 가장 큰 영향을 주는 지 알아보기 위해 


# 새로운 데이터 생성
Hong = np.array([0.0, 20.0, 1.0, 0.0])
Park = np.array([1.0, 17.0, 0.0, 0.0])
Kim = np.array([0.0, 40.0, 1.0, 0.0])
sample_passengers = np.array([Hong, Park, Kim]) # 새로운 데이터를 하나의 행렬 데이터로 변환
sample_passengers = scaler.transform(sample_passengers) # 정규화 진행


# 새로운 데이터에 대해서 적합 진행
print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))
