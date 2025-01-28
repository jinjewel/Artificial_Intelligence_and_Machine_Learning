# 벡터 합을 내적으로 나타내기

# 필요한 라이브러리 선언
import numpy as np

# 변수생성
num1 = np.ones(1000) # 1 * 1000 size 0 행렬
num2 = np.arange(1, 1001) # 1 * 1000 size [1,2,...,1000] 행렬

# 행렬 곱을 이용하여 내적 구하기
dotOp = num1.dot(num2)
print(dotOp)