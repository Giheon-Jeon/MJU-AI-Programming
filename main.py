import pandas as pd

df = pd.DataFrame({
	 "month": [1, 1, 2, 2, 3, 3],
	 "category": ["food", "book", "food", "traffic", "food", "book"],
	 "amount": [5000, 12000, 7000, 3000, 6500, 9000]
})

# reset_index() 없이
result = df.groupby("month")["amount"].sum()
print(result)
# label 기반 접근
print(result.loc[1])
# 위치 기반 접근
print(result.iloc[0])

# reset_index() 사용
result_df = df.groupby("month")["amount"].sum().reset_index()
print(result_df)
# month가 열 -> result_df["month]처럼 접근 가능