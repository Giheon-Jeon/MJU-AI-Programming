import numpy as np

# =========================================================
# [NumPy np.dot() Exercise]
# 각 연산의 결과값 또는 결과 Shape를 예측해 보세요.
# 행렬 곱셈은 '안쪽 차원'이 일치해야 함을 잊지 마세요!
# =========================================================

# --- 문제 1: 벡터 내적 (1D Dot Product) ---
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("--- Question 1 ---")
# 1-1. result_v = np.dot(v1, v2)
print("1-1 (Vector Dot):", np.dot(v1, v2))


# --- 문제 2: 행렬 곱셈 (2D Matrix Multiplication) ---
M1 = np.ones((2, 3))
M2 = np.ones((3, 4))
M3 = np.ones((2, 3))

print("\n--- Question 2 ---")
# 2-1. result_m1 = np.dot(M1, M2)
print("2-1 (M1 dot M2) Shape:", np.dot(M1, M2).shape)

# 2-2. result_m2 = np.dot(M1, M3)
try:
    print("2-2 (M1 dot M3) Shape:", np.dot(M1, M3).shape)
except ValueError as e:
    print("2-2 Error:", e)


# --- 문제 3: 행렬과 벡터의 곱 ---
M4 = np.array([[1, 2], 
               [3, 4], 
               [5, 6]]) # Shape: (3, 2)
v3 = np.array([10, 20])   # Shape: (2,)

print("\n--- Question 3 ---")
# 3-1. result_mv = np.dot(M4, v3)
print("3-1 Value:", np.dot(M4, v3), "| Shape:", np.dot(M4, v3).shape)


# [💡 Quiz Tip]
# np.dot(A, B) 에서
# A의 Shape가 (m, n)이고 B의 Shape가 (n, k)일 때만 가능!
# 결과 Shape는 항상 (m, k)가 됩니다.