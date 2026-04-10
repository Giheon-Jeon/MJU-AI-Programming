import csv

with open("card.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    rows = list(data)

card_date = []
card_price = []

for row in rows:
    card_date.append(row[0])
    card_price.append(row[4])

print(f"dates = {card_date}")
print(f"prices = {card_price}")