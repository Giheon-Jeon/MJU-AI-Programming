# 1. List Comprehension
# [표현식 for 항목 in 반복가능객체 if 조건]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 골라내어 그 제곱을 리스트로 만들기
squares = [n**2 for n in numbers if n % 2 == 0]
print(f"1. List Comprehension 결과 (짝수의 제곱): {squares}")


# 2. Dictionary Comprehension (추가)
# {키: 값 for 항목 in 반복가능객체 if 조건}
# 숫자를 키로, 그 숫자의 '홀/짝' 여부를 값으로 가지는 딕셔너리 만들기
even_odd_dict = {n: ("even" if n % 2 == 0 else "odd") for n in range(1, 6)}
print(f"2. Dictionary Comprehension 결과: {even_odd_dict}")


# 3. enumerate
students = ["Alice", "Bob", "Charlie"]
print("\n3. enumerate 결과 (출석부):")
for i, name in enumerate(students, start=1):
    print(f"{i}번 학생: {name}")


# 4. zip
names = ["전기헌", "홍길동", "성춘향"]
scores = [95, 88, 72]

print("\n4. zip 결과 (학생 정보 매칭):")
for name, score in zip(names, scores):
    print(f"이름: {name}, 점수: {score}")


# [응용] zip과 dictionary comprehension 혼합
# 두 리스트를 합쳐서 성적 딕셔너리 만들기
student_scores = {name: score for name, score in zip(names, scores)}
print(f"\n[응용] zip + dict comprehension 결과: {student_scores}")

