# 시그모이드 함수 구현


# 필요한 라이브러리 선언
import numpy as np
import matplotlib.pyplot as plt


# 시그모이드 함수 식 구현
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 변수 생성
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)


# 그래프 출력
plt.plot(x, y)
plt.plot([0, 0], [1.0, 0.0], ':')
plt.ylim(-0.1, 1.1)
plt.title('Sigmoid Function')
plt.show()