# 텐서플로우 기반 선형회귀모델 구현

# 시간에 따른 수입 예상

import tensorflow as tf

# 데이터
x_data = [1.0, 2.0, 3.0]  # 1시간, 2시간, 3시간 (float형으로 변경)
y_data = [10000.0, 20000.0, 30000.0]  # 10000원, 20000원, 30000원 (float형으로 변경)

# 학습을 통해 구할 변수 지정
W = tf.Variable(tf.random.normal([1]), name='weight')
b = tf.Variable(tf.random.normal([1]), name='bias')

# 가설
def hypothesis(X):
    return X * W + b

# 비용함수: 최소제곱법을 사용
def cost_fn(X, Y):
    return tf.reduce_mean(tf.square(hypothesis(X) - Y))

# 비용함수 최소화 알고리즘: GradientDescent 알고리즘
optimizer = tf.optimizers.SGD(learning_rate=1e-2)

# 학습 함수
def train_step(X, Y):
    with tf.GradientTape() as tape:
        cost = cost_fn(X, Y)
    gradients = tape.gradient(cost, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))
    return cost

# 학습을 위한 데이터셋 생성
dataset = tf.data.Dataset.from_tensor_slices((x_data, y_data)).batch(len(x_data))

# 2000번 학습
for step in range(2001):
    for X, Y in dataset:
        cost_val = train_step(X, Y)
    if step % 20 == 0:
        print(step, "Cost:", cost_val.numpy(), "\tW:", W.numpy(), "\tb:", b.numpy())

# 예측
print("H(4) 예측:", hypothesis([4.0]).numpy())  # 입력 데이터도 float형으로 변경
