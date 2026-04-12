import numpy as np
import pandas as pd

# 1. NumPy Boolean Indexing 기초 (수업 자료 13p)
# 조건식을 사용해 True/False 마스크를 생성하고 데이터를 추출합니다.
print("--- 1. NumPy Basic Boolean Masking ---")
arr = np.array([10, 25, 30, 12, 40])

# 마스크 생성 (25 이상인 원소 체크)
mask = (arr >= 25)
print(f"원본 배열: {arr}")
print(f"마스크(arr >= 25): {mask}")
print(f"필터링 결과: {arr[mask]}") # [25, 30, 40]

# 직접 조건 대입 (짝수만 추출)
even_vals = arr[arr % 2 == 0]
print(f"짝수 원소 추출: {even_vals}") # [10, 30, 12, 40]
print()


# 2. NumPy 다중 조건 마스크 (논리 연산자 활용)
# 마스크 결합 시 &, |, ~ (and, or, not) 연산자를 사용하며, 각 조건은 괄호()로 묶어야 합니다.
print("--- 2. NumPy Multiple Conditions ---")
arr2 = np.arange(1, 11) # 1~10

# 3보다 크고 8보다 작은 값 추출 (AND)
mask_and = (arr2 > 3) & (arr2 < 8)
print(f"3 < arr < 8: {arr2[mask_and]}") # [4, 5, 6, 7]

# 3의 배수이거나 짝수인 값 추출 (OR)
mask_or = (arr2 % 3 == 0) | (arr2 % 2 == 0)
print(f"3의 배수 or 짝수: {arr2[mask_or]}") # [2, 3, 4, 6, 8, 9, 10]
print()


# 3. 마스크를 이용한 값 수정
print("--- 3. Modifying Values with Mask ---")
arr_mod = np.array([1, -5, 10, -2, 3])
print(f"수정 전: {arr_mod}")

# 음수인 값들을 모두 0으로 바꾸기
arr_mod[arr_mod < 0] = 0
print(f"음수 제거 후: {arr_mod}") # [1, 0, 10, 0, 3]
print()


# 4. Pandas 조건 필터링 (수업 자료 27p)
# DataFrame에서도 동일한 논리로 특정 행을 골라낼 수 있습니다.
print("--- 4. Pandas Boolean Masking ---")
data = {
    '이름': ['민수', '지연', '현우', '수빈'],
    '점수': [90, 75, 82, 64],
    'PER': [12.5, 8.2, 10.1, 7.8]
}
df = pd.DataFrame(data)

# PER이 10보다 큰 행만 필터링
per_over_10 = df[df['PER'] > 10]
print("PER > 10 인 데이터:\n", per_over_10)

# 점수가 80점 이상인 사람의 이름만 추출
high_scorers = df[df['점수'] >= 80]['이름']
print(f"\n80점 이상인 학생: {high_scorers.tolist()}")
print()


# 5. 전처리: 마스크로 새 열 만들기 (수업 자료 29p)
print("--- 5. Creating New Column with Mask ---")
# 점수가 80점 이상이면 'True', 아니면 'False'인 '통과' 열 추가
df['통과'] = df['점수'] >= 80
print("통과 여부 추가 결과:\n", df)

# 다중 조건을 통한 Pandas 필터링 (AND)
# 이름이 '민수'이고 점수가 80점 이상인 행
filtered_df = df[(df['이름'] == '민수') & (df['점수'] >= 80)]
print("\n이름이 민수이고 80점 이상:\n", filtered_df)
