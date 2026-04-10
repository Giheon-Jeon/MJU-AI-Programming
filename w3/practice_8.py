# 실습 8: 1~100까지 숫자의 합 구하기
# - for문 사용
# - range() 사용
# - 합계를 저장할 변수 사용 (초기값 0)
# - 마지막에 결과 출력

total = 0

for i in range(1, 101):
    total += i

print(f"1 to 100 합계: {total}")
