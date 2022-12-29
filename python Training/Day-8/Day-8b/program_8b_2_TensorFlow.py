import tensorflow as tf

print("=" * 20)
print(tf.__version__)
print("=" * 20)
scalar = tf.constant(5)
print(scalar)
print("=" * 20)
print(scalar.ndim)
print("=" * 20)
vector = tf.constant([2, 5])
print(vector)
print("=" * 20)
print(vector.ndim)
print("=" * 20)
matrix = tf.constant([[2, 5],
                      [4, 7],
                      [3, 9]])
print("=" * 20)
print(matrix)
print("=" * 20)
print(matrix.ndim)
print("=" * 20)
