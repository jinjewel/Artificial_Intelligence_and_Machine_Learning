# 지수함수 생성 및 그래프 출력

# 필요한 라이브러리 출력
import numpy as np
import matplotlib.pyplot as plt

# 변수 생성
x = np.linspace(-4,4,100) # -4부터 4까지 등간격 변수 100개 생성

y = 2 ** x # 증가하는 지수함수
y2 = 3 ** x # 증가하는 지수함수
y3 = 0.5 ** x # 감소하는 지수함수

# 그래프 출력
plt.figure(figsize=(5,5)) # 출력되는 그래프의 사이즈
plt.plot(x, y, 'black', linewidth = 3, label = '$y=2^x$')
plt.plot(x, y2, 'cornflowerblue', linewidth = 3, label = '$y=3^x$')
plt.plot(x, y3, 'gray', linewidth = 3, label = '$y=0.5^x$')
plt.ylim(-2,6) # x 범위
plt.xlim(-4,4) # y 범위
plt.grid(True) # 격자 표시
plt.legend(loc='lower right') # 범례 설정
plt.show() 
