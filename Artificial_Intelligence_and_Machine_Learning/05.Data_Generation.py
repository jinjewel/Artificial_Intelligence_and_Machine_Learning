# 회귀 직선 모델을 적합하기 위한 데이터 생성

# 필요한 라이브러리 선언
import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
np.random.seed(1) # 난수 고정
X_n = 16 # 생성하려는 인원 수 선언
Hg_C = [170, 108, 0.2] # 키를 만드는 매개변수 

X = 5 + 25*np.random.rand(X_n) # 나이 생성
T = Hg_C[0] - Hg_C[1] * np.exp(-Hg_C[2]*X) + 4*np.random.rand(X_n) # 키 생성

# 생성한 데이터 출력
for i in range(len(X)):
    print("(나이 : %.2f, 키 : %.2f)"%(X[i], T[i]))

# 그래프 그리기
plt.figure(figsize=(4,4))
plt.plot(X, T, marker='o', linestyle='None', markeredgecolor='black', color='cornflowerblue')
plt.xlim(4, 30)
plt.grid(True)
plt.show()










