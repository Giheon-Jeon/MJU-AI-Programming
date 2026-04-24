import numpy as np

# 1. 합계와 평균 - axis(축) 기준으로 보기 (수업 자료 10p)
# axis는 연산이 수행되는 방향을 결정합니다.
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("--- 1. Axis & Sum/Mean ---")
# axis=None (기본값): 전체 원소의 합
print(f"전체 합: {np.sum(arr_2d)}") # 21

# axis=0: 열 방향(위->아래) 집계. 각 열의 합을 구함.
# 결과의 shape은 (열의 개수,)가 됩니다.
print(f"열 방향 합 (axis=0): {np.sum(arr_2d, axis=0)}") # [5, 7, 9]

# axis=1: 행 방향(왼->오른) 집계. 각 행의 합을 구함.
# 결과의 shape은 (행의 개수,)가 됩니다.
print(f"행 방향 합 (axis=1): {np.sum(arr_2d, axis=1)}") # [6, 15]

# 평균 연산도 동일하게 axis 적용 가능
print(f"열 방향 평균 (axis=0): {np.mean(arr_2d, axis=0)}") # [2.5, 3.5, 4.5]
print()


# 2. NumPy 인덱싱 (수업 자료 11p)
# arr[row, col] 형태로 특정 원소나 범위를 선택합니다.
arr_idx = np.array([[10, 20, 30],
                    [40, 50, 60]])

print("--- 2. Indexing ---")
print(f"0행 1열 원소: {arr_idx[0, 1]}")   # 20
print(f"1행 전체 선택: {arr_idx[1]}")      # [40, 50, 60]
print(f"1열 전체 선택: {arr_idx[:, 1]}")   # [20, 50] (':'는 전체를 의미)
print()


# 3. NumPy 슬라이싱 (수업 자료 12p)
# 시작:끝 형태 (끝 인덱스는 포함되지 않음)
arr_slice = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

print("--- 3. Slicing ---")
# 상위 2행, 1열 이후 슬라이싱
# 행: 0~1 (2 전까지), 열: 1~끝
print("상위 2행, 1열 이후:\n", arr_slice[:2, 1:]) 
# [[2, 3], 
#  [5, 6]]

# 1행 이후, 처음 2열 슬라이싱
print("1행 이후, 처음 2열:\n", arr_slice[1:, :2])
# [[4, 5], 
#  [7, 8]]

# 마지막 행 전체 선택
print(f"마지막 행 전체: {arr_slice[2, :]}") # [7, 8, 9]
print()


# 4. 조건문으로 선택 - Boolean Indexing (수업 자료 13p)
# 특정 조건에 맞는 데이터만 필터링합니다.
arr_bool = np.array([10, 25, 30, 12, 40])

print("--- 4. Boolean Indexing ---")
mask = arr_bool >= 25
print(f"마스크 생성: {mask}") # [False, True, True, False, True]
print(f"25 이상인 값만 추출: {arr_bool[mask]}") # [25, 30, 40]

# 짝수만 추출하기 (직접 조건 대입)
print(f"짝수만 추출: {arr_bool[arr_bool % 2 == 0]}") # [10, 30, 12, 40]


# 5. 3차원 배열 - 인덱싱과 Axis (시험 출제 대비!)
# 3차원 배열의 Shape 구조: (Depth/Layer, Row, Column)
arr_3d = np.array([
    [[1, 2], [3, 4]],   # 0번 층 (2x2)
    [[5, 6], [7, 8]]    # 1번 층 (2x2)
])

print("\n--- 5. 3D Array & Axis ---")
# shape 확인: (2, 2, 2) -> 2개의 층, 각 층은 2행 2열
print(f"3D 배열 Shape: {arr_3d.shape}")

# 3차원 인덱싱: arr[layer, row, col]
# 예: 1번 층의 0행 1열 원소 (6)
print(f"1층 0행 1열 원소: {arr_3d[1, 0, 1]}") # 6

# 3차원에서의 Axis(축) 이해하기
# axis=0: '층(Layer)'을 관통하는 방향 (0층의 (r,c) + 1층의 (r,c))
# 결과는 각 층이 겹쳐서 더해진 2x2 행렬이 됩니다.
print("axis=0 합계 (층끼리 더하기):\n", np.sum(arr_3d, axis=0))
# [[1+5, 2+6], [3+7, 4+8]] -> [[6, 8], [10, 12]]

# axis=1: 각 층 내부에서 '행(Row)'을 관통하는 방향 (위->아래)
# 결과는 각 층별로 열의 합이 계산됩니다.
print("axis=1 합계 (층별 열 합계):\n", np.sum(arr_3d, axis=1))
# [[1+3, 2+4], [5+7, 6+8]] -> [[4, 6], [12, 14]]


# axis=2: 각 층의 각 행 내부에서 '열(Column)'을 관통하는 방향 (왼->오)
# 결과는 각 행의 가로 합이 계산됩니다.
print("axis=2 합계 (행별 가로 합계):\n", np.sum(arr_3d, axis=2))
# [[1+2, 3+4], [5+6, 7+8]] -> [[3, 7], [11, 15]]


# 6. 심화: 3차원 배열 인덱싱 & 슬라이싱 마스터하기 (복잡한 케이스)
# 3차원 배열 준비: shape (3, 4, 5) -> 3개의 층, 각 층은 4행 5열
# 0부터 59까지의 숫자로 채워진 배열을 생성합니다.
arr_complex = np.arange(60).reshape(3, 4, 5)

print("\n" + "="*50)
print("--- 6. Complex 3D Indexing & Slicing ---")
print(f"배열 구조:\n{arr_complex}")
print(f"Shape: {arr_complex.shape}")

# [Q1] 중간 층(1번 층)의 마지막 2행, 마지막 3열만 추출하기
# 슬라이싱: layer=1, row=2: (2행부터 끝), col=2: (2열부터 끝)
q1 = arr_complex[1, 2:, 2:]
print("\n[Q1] 중간 층의 마지막 2행 & 마지막 3열:\n", q1)

# [Q2] 모든 층에서 0번 행과 2번 행만 선택하되, 열은 1번부터 3번까지(포함) 추출
# 슬라이싱: layer=:, row=[0, 2], col=1:4
q2 = arr_complex[:, [0, 2], 1:4]
print("\n[Q2] 전 층의 0,2행 & 1~3열:\n", q2)

# [Q3] 각 층의 '역순' 배치 (층의 순서만 2->1->0으로 뒤집기)
# 슬라이싱: layer=::-1, row=:, col=:
q3 = arr_complex[::-1, :, :]
print("\n[Q3] 층의 순서 역순 배치 (첫 원소 확인 - 40부터 시작):\n", q3[0, 0, 0]) # 40

# [Q4] 모든 층, 모든 행에 대해 '짝수 번째 열'만 추출 (0, 2, 4열)
# 슬라이싱: layer=:, row=:, col=::2
q4 = arr_complex[:, :, ::2]
print("\n[Q4] 모든 데이터 중 짝수 번째 열만 추출 (Shape 확인):\n", q4.shape) # (3, 4, 3)

# [Q5] 특정 조건(Boolean Indexing)과 차원 유지
# 전체 배열에서 7의 배수만 추출 (1차원으로 반환됨)
q5 = arr_complex[arr_complex % 7 == 0]
print("\n[Q5] 전체 원소 중 7의 배수만 추출:\n", q5)

# [Q6] 복합 슬라이싱: 0번과 2번 층에서, 1행부터 끝까지, 열은 뒤에서 2번째부터 끝까지
# 슬라이싱: layer=[0, 2], row=1:, col=-2:
q6 = arr_complex[[0, 2], 1:, -2:]
print("\n[Q6] 0,2층 / 1행~끝 / 뒤에서 2열~끝:\n", q6)

# [Q7] Ellipsis (...) 사용하기
# 모든 차원을 생략하고 특정 열만 선택할 때 유용합니다.
# 예: 모든 층, 모든 행의 마지막 열(index -1)
q7 = arr_complex[..., -1]
print("\n[Q7] 모든 층, 모든 행의 마지막 열 데이터:\n", q7)
print(f"결과 Shape: {q7.shape}") # (3, 4) -> 3층 x 4행의 마지막 열들이 모임

