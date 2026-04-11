"""
잘못된 입력 처리

점수는 0-100만 유효함 
인풋 : "점수를 입력하세요: "
아웃풋 : 
범위를 벗어나는 경우 "점수는 0 ~ 100 사이여야 합니다."
정상 범위인 경우 A/B/C/D/F 출력 (100 이하 90 이상 A / 90 미만 80 이상 B ...)
"""

score = int(input("점수를 입력하세요: "))
grade = ""
is_check = True

if score < 0 or score > 100:
    print("점수는 0 ~ 100 사이여야 합니다.")
    is_check = False
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grage = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if is_check:
    print(grade)