# 행렬의 덧셈 계산

# 필요한 라이브러리 선언
import numpy as np

def sumMatrix_not_numpy(A, B):
    answer = []
    
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[i])):
            tmp.append(A[i][j] + B[i][j])
        answer.append(tmp)
    return answer

def sumMatrix_used_numpy(A, B):
    A = np.matrix(A)
    B = np.matrix(B)
    answer = A + B
    return answer

if __name__ == "__main__":
    print(sumMatrix_not_numpy([[1,2],[2,3]],[[3,4],[5,6]]),"\n") # 행렬의 덧셈을 numpy를 쓰지 않고 함수로 계산
    print(sumMatrix_used_numpy([[1,2],[2,3]],[[3,4],[5,6]]),"\n") # 행렬의 덧셈을 numpy를 써서 함수로 계산
    