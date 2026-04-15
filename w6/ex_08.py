import pandas as pd

df = pd.DataFrame({
	 "month": [1, 1, 2, 2, 3, 3],
	 "category": ["food", "book", "food", "traffic", "food", "book"],
	 "amount": [5000, 12000, 7000, 3000, 6500, 9000]
})

print(df.groupby("month")["amount"].sum())