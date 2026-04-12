import numpy as np

# 브로드캐스팅(Broadcasting): 크기가 다른 배열끼리 연산이 가능하게 하는 규칙
# 규칙 1: 뒤쪽 차원(trailing dimension)부터 비교하여 크기가 같거나 어느 한쪽이 1이어야 함.

# 1. 스칼라와 배열의 연산 (가장 기본적인 브로드캐스팅)
print("--- 1. Scalar & Array ---")
a_scalar = np.array([1, 2, 3])
print(f"원본: {a_scalar}")
print(f"더하기 10:\n{a_scalar + 10}") # [11, 12, 13]
print()


# 2. 2D 배열과 1D 배열의 연산 (행 단위 브로드캐스팅) - 수업 자료 18p
print("--- 2. 2D Array & 1D Array (Row-wise) ---")
a = np.array([[1, 2, 3], 
              [4, 5, 6]]) # shape (2, 3)
b = np.array([10, 20, 30])  # shape (3,) -> (1, 3)으로 확장되어 각 행에 더해짐

print(f"a + b 결과:\n{a + b}")
# [[1+10, 2+20, 3+30],
#  [4+10, 5+20, 6+30]]
print()


# 3. 열 단위 브로드캐스팅 (Column-wise)
# shape (m, 1) 배열은 (m, n) 배열의 모든 열에 브로드캐스팅됩니다.
print("--- 3. Column-wise Broadcasting ---")
c = np.array([[1, 2, 3],
              [4, 5, 6]])      # shape (2, 3)
d = np.array([[10], [20]])     # shape (2, 1) -> 옆으로 확장되어 각 열에 동일하게 더해짐

print(f"c + d 결과:\n{c + d}")
# [[1+10, 2+10, 3+10],
#  [4+20, 5+20, 6+20]]
print()


# 4. 차원이 아예 다른 경우의 브로드캐스팅 (3, 1) + (1, 4)
print("--- 4. Shape (3, 1) + (1, 4) ---")
row_vec = np.array([1, 2, 3]).reshape(3, 1) # 열 벡터
col_vec = np.array([10, 20, 30, 40])        # 행 벡터 (1, 4)

# (3, 1)과 (1, 4)가 만나서 (3, 4) 행렬이 됨 (외적과 유사한 형태)
print(f"결과:\n{row_vec + col_vec}")
print()



# 5. 고차원 브로드캐스팅 예시 (수업 자료 19p)
print("--- 5. Higher Dimensional Example ---")
# 규칙: 오른쪽(뒤쪽) 차원부터 맞춥니다.
# a_4d: (2, 2, 3, 4)
# b_2d:       (3, 4)  <- 일치함!
a_4d = np.ones((2, 2, 3, 4))
b_2d = np.arange(12).reshape(3, 4)

result = a_4d + b_2d
print(f"4차원 연산 결과 shape: {result.shape}") # (2, 2, 3, 4)
print()


# 6. 고차원 브로드캐스팅 심화 1 (3D + 1D)
# 이미지 데이터(Channel, Height, Width) 처럼 생각하면 쉽습니다.
print("--- 6. 3D (2, 3, 4) + 1D (4,) ---")
# x: (2, 3, 4)  -> 2개의 채널, 3행 4열
# y:       (4,)  -> 4열 데이터 (각 행에 공통으로 적용됨)
x = np.zeros((2, 3, 4))
y = np.array([10, 20, 30, 40]) 

# y가 (1, 1, 4)처럼 취급되어 모든 채널의 모든 행에 더해집니다.
result_6 = x + y
print(f"결과 Shape: {result_6.shape}")
print(f"첫 채널의 첫 행 데이터: {result_6[0, 0, :]}") # [10, 20, 30, 40]
print()


# 7. 고차원 브로드캐스팅 심화 2 (3D + 2D)
print("--- 7. 3D (2, 3, 4) + 2D (3, 4) ---")
# x: (2, 3, 4)
# z:    (3, 4)  -> 3행 4열 행렬이 각 '채널'마다 통째로 더해짐
z = np.ones((3, 4)) * 100

result_7 = x + z
print(f"결과 Shape: {result_7.shape}")
print(f"0번 채널 결과:\n{result_7[0]}") # 모두 100
print(f"1번 채널 결과:\n{result_7[1]}") # 모두 100
print()


# 8. 앞쪽 차원이 1인 경우 (가장 헷갈리는 부분)
print("--- 8. Specific Axis Broadcasting (1, 3, 1) + (4, 1, 5) ---")
# 뒤쪽 차원부터 비교:
# arr_a: (1, 3, 1)
# arr_b: (4, 1, 5)
# 결과  : (4, 3, 5) <- 각 차원에서 1인 부분은 상대방 크기에 맞춰 확장됨
arr_a = np.ones((1, 3, 1))
arr_b = np.ones((4, 1, 5))

result_8 = arr_a + arr_b
print(f"복합 확장 결과 Shape: {result_8.shape}") # (4, 3, 5)



# 9. 브로드캐스팅 판정 마스터 (오른쪽 정렬 규칙)
# 핵심 규칙: 오른쪽(열)부터 비교하며, "값이 같거나" 또는 "한쪽이 1"이어야 함!

print("--- 9. Broadcasting Rule Master Case ---")

# [Case A] (2, 5, 3) + (5, 1) -> 성공
# A: 2 , 5 , 3
# B:     5 , 1 (1은 3으로 변신!)
# -------------
# R: 2 , 5 , 3
arr_a = np.ones((2, 5, 3))
arr_b = np.ones((5, 1))
print(f"Case A (2,5,3)+(5,1) 성공! Shape: {(arr_a + arr_b).shape}")

# [Case B] (2, 5, 3) + (2, 3) -> 실패
# A: 2 , 5 , 3
# B:     2 , 3 (5와 2가 충돌! 둘 다 1이 아님)
# -------------
print("\nCase B (2,5,3)+(2,3) 시도...")
try:
    arr_c = np.ones((2, 3))
    invalid_op = arr_a + arr_c
except ValueError as e:
    print(f"실패 원인: {e}")


# 10. 시각적 요약 다이어그램
"""
브로드캐스팅 가능 여부 판정법 (오른쪽 정렬 후 한 칸씩 비교)

사례 1: (3, 4, 5) & (4, 1)
   3 , 4 , 5  (배열 1)
       4 , 1  (배열 2)
  -----------
   3 , 4 , 5  => OK (1이 5로 변신 가능)

사례 2: (3, 4, 5) & (3, 5)
   3 , 4 , 5  (배열 1)
       3 , 5  (배열 2)
  -----------
   (X) 4와 3이 충돌! => 불가능
"""
