# 개인정보를 받아 BMI, 혈압, 활동량을 진단 및 출력
def report_health(info):
    name = info["name"]                             #이름 str
    age = info["age"]                               # 나이 int
    height = info["height"]                         # cm 키 float
    weight = info["weight"]                         # kg 몸무게 float
    systolic, diastolic = info["blood_pressure"]    #혈압 정보 / 수축, 이완 tuple of int
    activity_record = info["activity_record"]       # 일일걸음 수 list of int

    # (1) BMI 진단
    bmi = weight / (height / 100) ** 2
    bmi_round = round(bmi, 1)
    
    if bmi_round < 18.5:
        bmi_status = "저체중"
    elif bmi_round < 25:
        bmi_status = "정상 체중"
    elif bmi_round < 30:
        bmi_status = "과체중"
    else:
        bmi_status = "비만"

    # (2) 혈압 진단
    if diastolic < 80:
        if systolic < 120:
            bp_status = "정상 혈압"
        elif systolic < 130:
            bp_status = "고혈압 전단계"
        else:
            bp_status = "고혈압 주의"
    else:
        bp_status = "고혈압 주의"

    # (3) 활동량 진단
    avg_steps = int(sum(activity_record)/len(activity_record))

    if avg_steps >= 15000:
        activity_status = "활동량 과도"
    elif avg_steps >= 7000:
        activity_status = "활동량 충분"
    else:
        activity_status = "활동량 부족"

    # 결과 출력
    print(f"{name} ({age}) 님의 건강 진단 결과:")
    print(f"- BMI: {bmi_round} → {bmi_status}")
    print(f"- 혈압: {systolic}/{diastolic} → {bp_status}")
    print(f"- 활동량: 평균 {avg_steps}걸음 → {activity_status}")

# dictionary 생성 및 함수 호출
in_health = {
    "name": "해리 포터",
    "age": 17,
    "height": 165.0,
    "weight": 55.0,
    "blood_pressure": (110, 70),
    "activity_record": [8000, 7500, 9000, 10000, 7000]
}

report_health(in_health)