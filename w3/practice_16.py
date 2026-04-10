# 실습 16: 성적 계산을 함수로 만들기
# - 함수 이름: get_grade(score)
# - 점수가 0~100 범위를 벗어나면 "잘못된 점수" 반환 (return)
# - 90 이상 A, 80 이상 B ... 그 외 F 반환 (return)
# - 함수 정의 후 아래쪽에서 점수를 입력받고 함수에 넣어 결과 출력
# - 참고: 함수 안에서는 print()가 아닌 return을 사용하여 결과를 돌려줍니다.

# === 함수 정의 위치 ===
def get_grade(score):
    if score>100 or score<0:
        return "잘못된 반환"
    elif score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

score_input = int(input("점수를 입력하세요: "))
result = get_grade(score_input)
print(f"결과: {result}")
