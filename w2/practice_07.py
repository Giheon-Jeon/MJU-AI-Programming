"""
기온 추천 시스템

기온을 입력받은 뒤 아래 규칙에 맞는 문장을 출력하라

30도 이상 : '너무 더워요'
10도 이상 30도 미만 : '야외 활동하기 좋아요'
0도 이상 10도 미만 : '외투를 챙기세요'
0도 미만 : '외출하지 마세요'
"""

temp = int(input("현재 기온 >> "))
temp_msg = ""

if temp >= 30: temp_msg = "너무 더워요"
elif temp >= 10: temp_msg = "야외 활동하기 좋아요"
elif temp >= 0: temp_msg = "외투를 챙기세요"
else: temp_msg = "외출하지 마세요"

print(temp_msg)