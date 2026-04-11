def introduce_student(name, age, major):
    """학생을 소개하는 함수 (함수 정의)"""
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"전공: {major}")
    print("-" * 20)

# 1. 위치 인자 (Positional Arguments) 사용
# 정의된 순서(name, age, major)를 정확히 지켜야 합니다.
print("[방법 1] 위치 인자 사용:")
introduce_student("전기헌", 20, "컴퓨터공학")

# 만약 순서를 바꾸면? (원치 않는 결과 발생)
# introduce_student(20, "컴퓨터공학", "전기헌") 
# -> 이름: 20, 나이: 컴퓨터공학... 처럼 잘못 나옵니다.


# 2. 키워드 인자 (Keyword Arguments) 사용
# 인자의 이름을 명시하면 순서가 바뀌어도 상관없습니다.
print("[방법 2] 키워드 인자 사용:")
introduce_student(age=21, major="인공지능", name="홍길동")


# 3. 혼합 사용 (Mixing Both) - 주의사항 포함
# 위치 인자를 먼저 쓰고, 그 뒤에 키워드 인자를 쓸 수 있습니다.
print("[방법 3] 혼합 사용:")
introduce_student("이몽룡", major="경영학", age=22)

# 주의: 키워드 인자 뒤에 위치 인자가 올 수는 없습니다!
# 예: introduce_student(name="성춘향", 23, "법학") -> SyntaxError 발생
