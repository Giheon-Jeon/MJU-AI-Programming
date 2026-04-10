# 실습 14: 랜덤 구구단 퀴즈 만들기
# - 질문은 총 5번 (for, range)
# - 랜덤한 구구단 문제 생성 (random.randint(1, 9) 혹은 (2, 9) 활용)
# - 정답 입력 받기
# - 맞으면 "정답입니다!" 출력
# - 틀리면 "땡! 정답은 n입니다." 출력

import random

for i in range(1, 6): #1-5까지 5번
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    
    ans = int(input(f"{num1} x {num2} = "))
    if ans == num1*num2:
        print("정답입니다!")
    else:
        print(f"땡! 정답은 {num1*num2}입니다.")