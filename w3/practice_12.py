"""
유아 / 청소년 / 성인 분류

나이 입력 받기 : "나이를 입력하세요: "
0살 미만이면 "나이는 0 이상이어야 합니다."
8살 미만은 "유아", 20살 미만은 "청소년", 그 외 "청년"
청소년의 경우 13살 이하는 "초등학생", 16살 이하는 "중학생", 그 외는 "고등학생"
"""

age = int(input("나이를 입력하세요: "))
is_check = True
result = ""

if age < 0:
    print("나이는 0 이상이어야 합니다.")
    is_check = False
elif age < 8: result = "유아"
elif age < 20:
    if age <= 13: result = "초등학생"
    elif age <= 16: result = "중학생"
    else: result = "고등학생"
else: result = "청년"

if is_check:
    print(result)