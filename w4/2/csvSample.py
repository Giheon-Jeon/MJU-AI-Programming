import csv

with open("card.csv", "r", encoding="utf-8") as f:
	data = csv.reader(f)
	next(data) # 첫 번째 행 (헤더) 건너뛰기
	rows = list(data)
	print(rows)