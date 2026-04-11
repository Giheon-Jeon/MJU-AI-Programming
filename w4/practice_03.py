"""
날짜 리스트와 금액 리스트 만들기

card.csv 파일을 읽어라
카드 이용일자를 모두 리스트 1개에 저장하고 출력
카드 사용금액을 모두 리스트 1개에 저장하고 출력
"""
import csv

with open("card.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    rows = list(data)

date = []
price = []

for row in rows:
    date.append(row[0])
    price.append(row[-3])

print(f"dates = {date}")
print(f"prices = {price}")