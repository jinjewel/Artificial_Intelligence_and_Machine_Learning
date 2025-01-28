## 선형회귀를 이용한 키 예측 구현


# 필요 패키지 선언
import matplotlib.pylab as plt # 그래프 라이브러리
from sklearn.linear_model import LinearRegression # 선형회귀 모델 라이브러리


# 데이터 생성
x = [[174],[152],[138],[128],[186]]
y = [71,55,46,38,88]


# 모형 생성 및 적합
reg = LinearRegression() # 선형 회귀모델 생성
reg.fit(x, y) # 선형 회귀모델 적합


# 새로운 값에 대한 예측
print(reg.predict([[165]])) # X=165에 대한 y예측 값 출력
y_pred = reg.predict(x) # 학습 데이터를 입력하여 예측값을 계산한다.


# 그래프 시각화
plt.scatter(x, y, color='black') # 실제 학습 데이터로 산점도 그리기
plt.plot(x, y_pred, color='blue', linewidth=3) # 예측 데이터로 
plt.show() # 그래프 출력
