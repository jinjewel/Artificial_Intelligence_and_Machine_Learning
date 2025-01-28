# placeholder와 feed_dict 예제

import tensorflow as tf  # TensorFlow 라이브러리를 임포트합니다.

# tf.function 데코레이터를 사용하여 함수를 정의합니다.
def add_tensors(a):  # 입력 텐서 a를 받아들이는 함수를 정의합니다.
    b = tf.constant([7, 7, 7], dtype=tf.float32)  # 값이 [7, 7, 7]인 상수 텐서를 정의합니다.
    return a + b  # 입력 텐서 a와 상수 텐서 b를 더한 결과를 반환합니다.

# 입력 텐서 a를 정의합니다.
a = tf.constant([1, 2, 3], dtype=tf.float32)

# 함수를 호출하여 결과를 얻습니다.
result = add_tensors(a)

# 결과 텐서를 출력합니다.
print(result)

