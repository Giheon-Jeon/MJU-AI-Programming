# 실습 11: 점수 입력 받아 학점 출력 및 잘못된 입력 처리
# - 점수는 0 이상 100 이하만 정상 (바깥 if문)
# - 범위를 벗어나면 "점수는 0 ~ 100 사이여야 합니다." 출력
# - 정상 범위이면 A/B/C/D/F 출력 (안쪽 if/elif/else 블록)
#   - A: 90 이상
#   - B: 80 이상 90 미만
#   - F: 60 미만

score = int(input("점수를 입력하세요: "))

# 여기에 코드를 작성하세요. (중첩 if문 활용)
if 0 <= score <= 100:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("점수는 0 ~ 100 사이여야 합니다.")