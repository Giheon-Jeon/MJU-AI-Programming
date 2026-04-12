import pandas as pd
import numpy as np

# 1. Series 만들기 (수업 자료 25p)
# Series는 1차원 데이터 구조로 인덱스(index)와 값(value)으로 구성됩니다.
print("--- 1. Pandas Series ---")

# (1) 리스트로 생성 (자동 인덱스 0, 1, 2, 3...)
s1 = pd.Series([10, 20, 30, 40])
print("자동 인덱스:\n", s1)

# (2) 사용자 지정 인덱스 사용
s2 = pd.Series([100, 200, 300], index=['A', 'B', 'C'])
print("\n사용자 지정 인덱스:\n", s2)

# (3) 딕셔너리로 생성 (키가 인덱스가 됨)
data_dict = {'서울': 990, '부산': 340, '대구': 240}
s3 = pd.Series(data_dict)
print("\n딕셔너리로 생성:\n", s3)
print()


# 2. DataFrame 만들기 (수업 자료 26p)
# DataFrame은 2차원 표 형태의 구조입니다.
print("--- 2. Pandas DataFrame ---")

data = {
    "종가": [157000, 51300, 68800, 140000],
    "PER": [39.88, 8.52, 10.03, 228.38],
    "PBR": [4.38, 1.45, 0.87, 2.16]
}
# 인덱스(행 이름) 지정
index = ["NAVER", "삼성전자", "LG전자", "카카오"]

df = pd.DataFrame(data, index=index)
print("주식 데이터 DataFrame:\n", df)
print()


# 3. 데이터 선택하기 (수업 자료 27p)
print("--- 3. Selecting Data ---")

# (1) 열(Column) 선택
print("1. '종가' 열만 선택:\n", df["종가"])

# (2) 위치 기반 행 선택 (iloc) - 0번째 행
print("\n2. 첫 번째 행 선택 (iloc[0]):\n", df.iloc[0])

# (3) 레이블 기반 행 선택 (loc) - 'NAVER' 행
print("\n3. 'NAVER' 행 선택 (loc['NAVER']):\n", df.loc["NAVER"])

# (4) 특정 조건 필터링
print("\n4. PER이 10보다 큰 종목만 선택:\n", df[df["PER"] > 10])
print()


# 4. DataFrame의 기본 속성 확인
print("--- 4. DataFrame Attributes ---")
print(f"Index(행): {df.index}")
print(f"Columns(열): {df.columns}")
print(f"Values(값):\n{df.values}")
print(f"Shape: {df.shape}")
print(f"Dtypes:\n{df.dtypes}")
