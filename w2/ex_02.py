# 복잡한 데이터 정리하기

"""
원본 데이터: "  User_Phone: 010-1234-5678.txt  "

목표 결과:

양쪽 공백을 제거할 것
확장자(.txt)를 제거할 것
하이픈(-)을 모두 제거할 것
최종적으로 숫자만 남았는지(isdigit) 확인하고 출력할 것

"""

data = "  User_Phone: 010-1234-5678.txt  "
new_data = data.strip()
new_data = new_data.replace(".txt", "")
new_data = new_data.replace("-", "")

phone_number = new_data.split(":")[1].strip()

if phone_number.isdigit():
    print(phone_number)