# [실습 2 - AI 스터디 모임 날짜 정하기 (random 모듈 활용)]
import random

# TODO: 이번 달 6일부터 25일 사이의 난수(정수)를 발생시켜 보세요. (힌트: random.randint 등 활용)
meeting_day = random.randint(6, 25)

# 결과 출력
print(f"AI 스터디 모임 날짜는 매월 {meeting_day}일입니다.")
