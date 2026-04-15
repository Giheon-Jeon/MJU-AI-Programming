import pandas as pd
df = pd.DataFrame({
 "이름": ["민수", "지연", "현우", "수빈"],
 "중간": [88, 76, 93, 64],
 "기말": [92, 81, 89, 70]
})

df["avg"] = (df["중간"] + df["기말"]) / 2
result = df[df["avg"] >= 50]
result = result.sort_values("avg", ascending=False)

print(result[["이름", "avg"]])
# print(result.iloc[:][["이름", "avg"]])
# print(result.iloc[0:2, [0, 3]])