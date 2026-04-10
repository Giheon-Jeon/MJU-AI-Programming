# 실습 9: 입력 받은 단의 구구단 출력
# - 몇 단을 출력할지 입력 받기 (input(), int() 변환 필수)
# - 1부터 9까지 곱하기 (for, range(1, 10))
# - "7 x 1 = 7" 형태로 출력

dan = int(input("몇 단을 출력할까요?: "))

for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")