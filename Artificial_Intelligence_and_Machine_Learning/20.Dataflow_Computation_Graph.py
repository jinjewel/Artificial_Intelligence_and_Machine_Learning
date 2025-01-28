# 데이터 플로우 계산 그래프

import tensorflow as tf

# 텐서 a와 b를 정의합니다.
a = tf.constant(4, name='a')
b = tf.constant(3, name='b')

# c와 d 연산을 정의합니다.
c = tf.multiply(a, b, name='c')
d = tf.add(a, b, name='d')

# e 연산을 정의합니다.
e = tf.add(c, d, name='e')

# 텐서 e의 값을 계산하고 출력합니다.
result = e.numpy()
print(result)

# TensorBoard 로그를 작성합니다.
logdir = "./log"
writer = tf.summary.create_file_writer(logdir)

# 그래프와 프로파일러를 기록합니다.
tf.summary.trace_on(graph=True, profiler=True, profiler_outdir=logdir)

# 실제 그래프 연산을 실행합니다.
with writer.as_default():
    tf.summary.trace_export(name="graph_trace", step=0, profiler_outdir=logdir)

writer.close()




