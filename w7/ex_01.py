import pandas as pd
df = pd.read_csv("sales.csv")

print(df.head(2))
# print(df.shape)
# print(df.columns)
print(df.dtypes)
# print(df.isna().sum())