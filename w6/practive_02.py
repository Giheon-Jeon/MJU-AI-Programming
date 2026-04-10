import pandas as pd

data = {
 "종가": [157000, 51300, 68800, 140000],
 "PER": [39.88, 8.52, 10.03, 228.38],
 "PBR": [4.38, 1.45, 0.87, 2.16]
}

index = ["NAVER", "삼성전자", "LG전자", "카카오"]

df = pd.DataFrame(data, index=index)
print(df)

print()
print(df["종가"])
print(df.iloc[0])
print(df.loc["NAVER"])
print(df[df["PER"] > 10])