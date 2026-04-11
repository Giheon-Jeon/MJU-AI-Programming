"""
성적 계산을 함수로 만들기

함수 이름은 get_grade(score)
점수가 0-100 범위를 벗어나면 "잘못된 점수" 반환
90 이상 A / 80 이상 B / 70 이상 C / 60 이상 D / 그 외 F
"""

def get_grade(score):
    if score < 0 or score > 100: return "잘못된 점수"
    elif score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

ip_score = int(input("점수 입력 >> "))
print(get_grade(ip_score))