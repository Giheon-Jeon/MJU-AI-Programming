"""
랜덤 구구단 퀴즈 만들기

질문은 5번
랜덤한 구구단 생성
정답 입력받기
맞으면 "정답입니다!"
틀리면 "땡! 정답은 x입니다." 출력
"""
import random

for term in range(5):
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    ans = int(input(f"{a} x {b} ? >> "))
    if ans == a*b: print("정답입니다!")
    else: print(f"땡! 정답은 {a*b}입니다.")