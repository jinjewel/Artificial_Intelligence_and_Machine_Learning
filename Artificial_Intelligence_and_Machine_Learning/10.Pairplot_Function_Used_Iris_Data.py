# pairplot 함수를 이용하여 iris 데이터 출력


# # 필요한 패키지 설치
# pip install scikit-learn
# pip install pyarrow


# 필요한 라이브러리 선언
from sklearn.model_selection import train_test_split # 데이터 셋을 분류하기 위한 라이브러리
from sklearn.datasets import load_iris # 붓꽃 데이터를 가져오기 위한 리아브러리
from matplotlib import pyplot as plt # 그래프 라이브러리

import pandas as pd # 데이터 프레임 변환을 위한 라이브러리
import numpy as np # 행렬 연산을 위한 라이브러리
import seaborn as sns # pairplot 함수를 사용하기 위한 라이브러리


# 데이터 선언
iris = load_iris()


# 데이터 프레임으로 변환
df = pd.DataFrame(data=iris.data, columns=iris.feature_names) # 꽃의 종류를 제외한 4가지 변수의 대한 데이터 저장
df['target'] = iris.target # 새로운 변수를 생성하여 데이터를 할당, 최종 150 * 5 행렬 
df['target'] = df['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"}) #  0.0, 1.0, 2.0으로 표현된 target_label을 해당 종 이름으로 매핑


# 슬라이싱을 통해 독립변수 데이터와 종속변수 데이터를 분리
x_data = df.iloc[:,:-1]
y_data = df.iloc[:,[-1]]


# Seaborn을 사용하여 pairplot 생성
sns.pairplot(df, # 사용할 데이터
             x_vars=["sepal length (cm)"], y_vars=["sepal width (cm)"], # x축과 y축의 이름 설정
             hue="target", # 범례 표시할 변수
             height=5) # 출력 창의 높이


# 그래프 출력
plt.show()
