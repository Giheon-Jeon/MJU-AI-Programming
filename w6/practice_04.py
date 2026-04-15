import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
food_df = df[df["category"] == "food"]

result = food_df.groupby("month")["amount"].sum().reset_index()
result = result.sort_values("month")
print(result)

plt.plot(result["month"], result["amount"])
plt.title("Monthly Food Sales (Line)")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.savefig("food_sales_line.png")
plt.show()