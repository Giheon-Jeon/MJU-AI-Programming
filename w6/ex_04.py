import numpy as np

# 벡터 내적 및 행렬 곱: dot vs matmul(@)
# 1D, 2D에서는 결과가 같지만, 3D(배치) 데이터에서 결정적인 차이가 발생합니다.

# 1. 1D 벡터 내적 (결과 동일)
print("--- 1. 1D Vector Dot Product ---")
v1 = np.array([1, 2])
v2 = np.array([3, 4])
print(f"dot: {np.dot(v1, v2)}")   # 1*3 + 2*4 = 11
print(f"matmul: {np.matmul(v1, v2)}") 
print(f"@: {v1 @ v2}")
print()


# 2. 2D 행렬 곱 (결과 동일)
print("--- 2. 2D Matrix Multiplication ---")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(f"dot:\n{np.dot(m1, m2)}")
print(f"@:\n{m1 @ m2}")
print()


# 3. 3D 배치(Batch) 행렬 곱 (결정적 차이!)
# 보통 (Batch, Row, Col) 구조를 가집니다.
# 예: 2개의 배치, 각 2x3 행렬
print("--- 3. 3D Batch Matrix Multiplication ---")
batch_a = np.ones((2, 2, 3)) # (Batch=2, R=2, C=3)
batch_b = np.ones((2, 3, 4)) # (Batch=2, R=3, C=4)

# [A] matmul (@) 사용 시
# 각 배치별로 독립적인 행렬 곱을 수행합니다. (2x3) @ (3x4) -> (2x4) 가 2개 생김
res_matmul = batch_a @ batch_b
print(f"matmul(@) 결과 Shape: {res_matmul.shape}") # (2, 2, 4) -> 성공! 배치가 유지됨.

# [B] dot 사용 시
# 앞 배열의 마지막 축(3)과 뒤 배열의 뒤에서 두 번째 축(3)을 곱하지만,
# 배치 차원까지 모두 조합하여 차원이 뻥튀기됩니다.
res_dot = np.dot(batch_a, batch_b)
print(f"dot 결과 Shape: {res_dot.shape}") # (2, 2, 2, 4) -> 전혀 다른 결과!
print()


# 4. 결론: 왜 dot보다 @(matmul)을 써야 하는가?
"""
1. 인공지능(DL) 데이터는 항상 Batch(배치) 차원이 포함되어 있습니다.
2. 우리는 각 데이터별로 행렬 곱이 수행되길 원하지, 배치끼리 섞이길 원하지 않습니다.
3. matmul(@)은 'Batch Matrix Multiplication'을 기본으로 설계되어 있어 안전합니다.
4. 따라서 딥러닝 코드나 다차원 배열 연산 시에는 무조건 @ 또는 np.matmul을 권장합니다.
"""

print("--- 4. Summary ---")
print("딥러닝(텐서 연산)에서는 항상 '@' 또는 'np.matmul'을 사용하세요!")
