import csv

with open("card.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    rows = list(data)

total_price = 0

for row in rows:
    date = row[0].split("-")[1]
    if date == "12" and row[1] == "전표매입":
        total_price += int(row[-3])

print(f"12월 총 지출액은 {total_price}원 입니다.")