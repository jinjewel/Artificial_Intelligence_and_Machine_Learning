# 행렬의 곱셉 계산

# 필요한 라이브러리 선언
import numpy as np

def matrixmult(A, B): # 행렬의 곱셉을 numpy를 쓰지 않고 함수로 계산
    n = len(A)
    c = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k]*B[k][j]
    return c


if __name__ == "__main__":
    # 데이터 선언
    A_1 = [[2,3],[4,1]]
    B_1 = [[5,7],[6,8]]
    A_2 = np.array(A_1)
    B_2 = np.array(B_1)
    
    print('A = ', A_1, '\nB = ', B_1, '\nC = ', matrixmult(A_1, B_1)) # 행렬의 곱셉을 numpy를 쓰지 않고 함수로 계산
    print("\nA * B =\n",A_2 * B_2, "\n") # 행렬의 인덱스 곱
    print("\nA dot B =\n", np.dot(A_2,B_2), "\n") # 행렬 곱샘을 numpy를 써서 함수로 계산
    
    # 행렬의 곱을 응용하여 신경망에 적용

    x = np.array([5,10])
    w = np.array([[1,3,5],[2,4,6]])
    Y = np.dot(x,w)

    # A -(w)-> Y
    print(w,'\n',Y)