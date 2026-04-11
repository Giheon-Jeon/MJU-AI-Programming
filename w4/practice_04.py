"""
12월 총 지출액 구하기

card.csv를 with 구문으로 읽기
12월 데이터만 필터링
상태가 전표매입인 경우만 금액을 더할 것
출력 "12월 총 지출액은 x원 입니다."
"""

import csv

with open("card.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    rows = list(data)

tot_price = 0

for row in rows:
    month = int(row[0].split("-")[1])
    if month == 12 and row[1] == "전표매입":
        tot_price += int(row[-3])

print(f"12월 총 지출액은 {tot_price}원 입니다.")