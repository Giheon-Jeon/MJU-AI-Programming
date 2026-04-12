import pandas as pd
import numpy as np

# 수업 자료 29p 기초 전처리 예제
print("--- 1. 데이터 프레임 생성 (결측치 포함) ---")
data = {
    "이름": ["민수", "지연", "현우", "수빈"],
    "점수": [90, np.nan, 78, 93], # 지연이 점수가 NaN(결측치)
    "반": ["A", "A", "B", "B"]
}
df = pd.DataFrame(data)
print("초기 데이터:\n", df)
print()


# 1. 결측치 채우기 (fillna)
# NaN으로 표시된 비어있는 값을 특정 값으로 채웁니다.
print("--- 2. fillna (결측치 처리) ---")
# 점수 열의 결측치를 0으로 채우기
df["점수"] = df["점수"].fillna(0)
print("결측치 0으로 채운 결과:\n", df)
print()


# 2. 데이터 타입 변경 (astype)
# 실수형(float)이었던 점수를 정수형(int)으로 변경합니다.
print("--- 3. astype (형 변환) ---")
df["점수"] = df["점수"].astype(int)
print(f"점수 열의 현재 타입: {df['점수'].dtype}")
print()


# 3. 데이터 정렬 (sort_values)
# 질문하신 것처럼 descending 옵션 대신 'ascending=False'를 사용합니다.
print("--- 4. sort_values (데이터 정렬) ---")

# 점수 기준 내림차순 (큰 점수가 위로)
# ascending=False는 "오름차순이 아니다" 즉, 내림차순을 뜻합니다.
sorted_df = df.sort_values(by="점수", ascending=False)
print("점수 내림차순 정렬 결과:\n", sorted_df)

# 여러 기준으로 정렬 (반 순서대로, 같은 반이면 점수 내림차순)
sorted_multi = df.sort_values(by=["반", "점수"], ascending=[True, False])
print("\n반(오름차순) & 점수(내림차순) 정렬:\n", sorted_multi)
print()


# 4. 조건문으로 새 열 만들기 (Derive Column)
# 특정 조건에 따라 'True/False' 또는 새로운 값을 가지는 열을 추가합니다.
print("--- 5. Conditional New Column ---")
# 80점 이상이면 '통과' 합격 여부 마스크 생성
df["통과"] = df["점수"] >= 80

# 조금 더 심층적으로, 평균 열을 만들어 전처리하기 (수업 자료 30p 응용)
# 예: 중간, 기말 점수가 있다고 가정 시 평균 계산 후 필터링 가능
print("합격 여부 추가 결과:\n", df)
print("\n최종 합격자 명단:\n", df[df["통과"] == True])
