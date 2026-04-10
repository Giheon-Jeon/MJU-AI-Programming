# 6주차 학습 내용

## 주제
데이터 처리 라이브러리 (NumPy, Pandas, Matplotlib)

## 개념 요약
- **데이터 처리 파이프라인**: 
  데이터 수집 -> 전처리(변환/정리) -> 모델 입력 -> 분석 과정에서 데이터 처리 능력이 모델 성능만큼 중요함.
- **NumPy (Numerical Python)**:
  - `ndarray` 다차원 배열 연산 지원. 리스트보다 빠르고 메모리 효율이 좋음.
  - 속성: `.shape`(차원 튜플), `.ndim`(차원 수), `.dtype`(자료형).
  - 배열 초기화: `zeros()`, `ones()`, `full()`, `empty()`, `arange()`, `linspace()`.
  - 기본 연산 규칙: 크기가 다를 때 **Broadcasting(브로드캐스팅)**이 일어나 차원이 자동으로 복제·확장됨. 요소별 연산(Element-wise)이 기본.
  - 배열 내적(Dot product): `np.dot()`을 활용해 행렬 곱 연산.
  - 선택/인덱싱: `arr[row, col]`, 슬라이싱 `arr[0:2, :]`, boolean indexing(마스크 필터링).
- **Pandas**:
  - `Series`(1차원, 인덱스 공유)와 `DataFrame`(2차원 표 형태, 행+열).
  - 데이터 로드: `pd.read_csv()` 
  - 기본 확인/조회: `.head()`, `.shape`, `.columns`, `.dtypes`, `.isna().sum()` (결측치).
  - 전처리: `.fillna()` 결측치 보간, `.astype()` 형변환.
  - 필터링(조건): `df[df['amount'] > 1000]`.
  - 정렬: `.sort_values("col_name", ascending=False)` 내림차순.
  - **groupby**: `df.groupby("key_col")["val_col"].sum()` 으로 키별 집계 수행. 결과를 다시 DF로 쓰려면 `.reset_index()`.
- **Matplotlib**:
  - 데이터 결과를 직관적으로 시각화하는 기본 라이브러리. `import matplotlib.pyplot as plt`.
  - 선 그래프 (추이 파악): `plt.plot()`.
  - 막대 그래프 (항목 간 크기 비교): `plt.bar()`.
  - 제목/축 레이블/저장: `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.savefig()`, `plt.show()`.

## 기억해야 할 꿀팁
- NumPy는 단일 배열 내에서 모든 요소가 **동일한 자료형(dtype)**이어야 함.
- Pandas 데이터 프레임에서 문자열 형태의 숫자값("10")을 정렬/연산하려면 사전에 `astype(int)`로 변환해야 결과 오류를 피할 수 있음.
- 데이터 집계 후(pandas groupby 등) 차트 시각화(line/bar plot)까지 이어지는 일련의 데이터 처리 파이프라인 흐름을 체화하자.

## 코드 스니펫
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Numpy 배열 슬라이싱 및 브로드캐스팅
arr = np.array([[1, 2], [3, 4]])
arr_multiplied = arr * 10
print(arr[:, 1]) # 모든 행의 1번 인덱스 열

# Pandas 파일 읽기 및 결측치, 형변환
df = pd.read_csv("sales.csv")
df["amount"] = df["amount"].fillna(0).astype(int)

# Groupby 집계 및 정렬
summary = df.groupby("month")["amount"].sum().reset_index()
summary = summary.sort_values("month", ascending=True)

# Matplotlib 시각화
plt.plot(summary["month"], summary["amount"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.savefig("sales_plot.png")
```
