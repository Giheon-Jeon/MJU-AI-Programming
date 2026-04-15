import pandas as pd

df = pd.read_csv("sales.csv")
food_df = df[df["category"] == "food"]

result = food_df.groupby("month")["amount"].sum().reset_index()
result = result.sort_values("month")
print(result)
