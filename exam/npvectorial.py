import numpy as np
a = np.array([1, 2, 3])
print(a)
print(a.shape)
# 1.产生行向量的方法
row_vector1 = a.reshape(1, -1)
row_vector2 = np.array([[1, 2, 3]])
row_vector3 = np.expand_dims(a, 0)
print('行向量：')
print(row_vector1)
print(row_vector2)
print(row_vector3)
print(row_vector1.shape, row_vector2.shape, row_vector3.shape)

# 2.产生列向量的方法
col_vector1 = a.reshape(-1, 1)
col_vector2 = np.array([[1], [2], [3]])
col_vector3 = row_vector1.T  # 向量转置
col_vector4 = np.expand_dims(a, axis=1)
print('列向量：')
print(col_vector1)
print(col_vector2)
print(col_vector3)
print(col_vector4)
print(col_vector1.shape, col_vector2.shape, col_vector3.shape, col_vector4.shape)
