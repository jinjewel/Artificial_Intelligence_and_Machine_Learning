# 로그함수 생성 및 그래프 표현

# 필요한 라이브러리 선언
import numpy as np
import matplotlib.pyplot as plt

# 변수 생성
x = np.linspace(-8,8,100)
y = 2 ** x

x2 = np.linspace(0.001,8,100)
y2 = np.log(x2)/np.log(2)

# 그래프에 그릴 함수 설정
plt.figure(figsize=(5,5)) # 출력되는 그래프의 가로 세로 길이
plt.plot(x, y, 'black', linewidth = 3)
plt.plot(x2, y2, 'cornflowerblue', linewidth = 3)
plt.plot(x, x, 'black', linewidth = 1, linestyle='--')
plt.ylim(-8,8)
plt.xlim(-8,8)
plt.xlabel('$x$', fontsize=14) # x축에 나타낼 문자 
plt.ylabel('$y$', fontsize=14) # y축에 나타낼 문자 
plt.grid(True)
plt.show()
