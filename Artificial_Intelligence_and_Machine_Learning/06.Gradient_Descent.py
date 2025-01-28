# 경사하강법의 과정

# 필요한 라이브러리 선언
import numpy as np
import matplotlib.pyplot as plt

# 함수 생성
def f(w0, w1):
    return w0**2 + 2*w0*w1 + 3

def df_dw0(w0,w1):
    return 2*w0 + 2*w1

def df_dw1(w0,w1):
    return 2*w0

# 데이터 생성
w_range = 2 # 범위 지정
dw = 0.25 # 간격 지정

w0 = np.arange(-w_range, w_range+dw, dw)
w1 = np.arange(-w_range, w_range+dw, dw)

wn = w0.shape[0]
ww0, ww1 = np.meshgrid(w0,w1)
ff = np.zeros((len(w0),len(w1)))
dff_dw0 = np.zeros((len(w0),len(w1)))
dff_dw1 = np.zeros((len(w0),len(w1)))

for i0 in range(wn):
    for i1 in range(wn):
        ff[i1, i0] = f(w0[i0], w1[i1])
        dff_dw0[i1, i0] = df_dw0(w0[i0], w1[i1])
        dff_dw1[i1, i0] = df_dw1(w0[i0], w1[i1])

plt.figure(figsize=(9,4))
plt.subplots_adjust(wspace=0.3)

# 첫번째 그림 생성 : f함수의 등고선 플롯
plt.subplot(1,2,1)
cont = plt.contour(ww0, ww1, ff, i0, colors='k') # f의 등고선
cont.clabel(fmt='%2.0f',fontsize=8)
plt.xticks(range(-w_range,w_range+1,1))
plt.yticks(range(-w_range,w_range+1,1))
plt.xlim(-w_range-0.5,w_range+0.5)
plt.ylim(-w_range-0.5,w_range+0.5)
plt.xlabel('$w_0$',fontsize=14)
plt.ylabel('$w_1$',fontsize=14)

# 두번째 그림 생성 : 기울기가 가장 큰 방향과 크기를 나타내는 벡터
plt.subplot(1,2,2)
plt.quiver(ww0, ww1, dff_dw0, dff_dw1) # f의 경사 벡터 표시
plt.xlabel('$w_0$',fontsize=14)
plt.ylabel('$w_1$',fontsize=14)
plt.xticks(range(-w_range,w_range+1,1))
plt.yticks(range(-w_range,w_range+1,1))
plt.xlim(-w_range-0.5,w_range+0.5)
plt.ylim(-w_range-0.5,w_range+0.5)

plt.show()












