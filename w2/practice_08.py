"""
1-100까지의 합 구하기

for문 사용
range() 사용
합계를 저장할 변수 사용
마지막에 결과 출력
"""
tot = 0

for i in range(1, 101):
    tot += i

print(f"1 to 100 합계: {tot}")