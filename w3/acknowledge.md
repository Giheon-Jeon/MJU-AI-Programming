# 3주차 학습 내용

## 주제
제어 흐름과 함수 (for, while, 내장 함수, 커스텀 함수)

## 개념 요약
- **내장 함수(Built-in Functions)**: 파이썬에서 기본 제공하는 함수.
  - `abs()`, `round()`, `len()`, `sum()`, `min()`, `max()` 등.
  - 모듈 내장: `import math`, `import random`을 통해 다양한 기능 활용 (`random.randint`, `math.sqrt` 등).
- **제어 흐름 (반복문)**: 
  - **for문**: 정해진 횟수나 범위, 리스트 등 `iterable`한 요소를 반복할 때 사용.
  - **range()**: 연속된 숫자를 생성 (`range(start, end, step)`).
  - **while문**: 조건이 참(`True`)인 동안 계속 반복. 반복 횟수가 불명확하거나 조건부 반복이 필요할 때 사용 (무한루프에 주의하고 탈출 조건을 명확히 해야 함).
- **함수 (def)**: 반복되는 코드 블록을 이름으로 묶어 재사용.
  - 정의: `def 함수이름(매개변수):` 형식으로 선언.
  - **매개변수(parameter)** 와 **전달인자(argument)**: 함수 정의 시 선언하는 변수가 파라미터, 호출 시 넘기는 값이 아규먼트.
  - **반환값(return)**: 함수의 처리 결과를 반환하며 함수 실행을 즉시 종료함. 생략 시 `None`을 반환.
  - 매개변수의 기본값(Default value): `def get_price(is_vip=False):`처럼 주면 인수 생략 시 기본값 사용.
  - 위치 인자(positional) 및 키워드 인자(keyword).
  - 인자 개수가 유동적인 경우 `*args` (튜플), `**kwargs` (딕셔너리) 사용.
- **변수의 스코프(Scope)**: 
  - 지역 변수(local): 함수 내부에서 만들어진 변수, 밖에서는 접근 불가.
  - 전역 변수(global): 함수 외부에서 선언된 범위. 함수 내부에서 수정하려면 `global` 키워드로 선언 필요 (`UnboundLocalError` 주의).

## 기억해야 할 꿀팁
- `while`문 작성 시 반복문 내에서 무조건 **조건 변수가 업데이트**되는 구문(`i += 1` 등)이 있는지 점검하여 무한 루프를 방지할 것.
- 함수 이름은 용도를 직관적으로 알 수 있는 동사형으로 작명할 것.
- 중첩 루프(nested loop) 사용 시 들여쓰기에 주의하고 바깥 루프 1회당 안쪽 루프 전체가 돈다는 흐름을 명확히 인지.

## 코드 스니펫
```python
# for문과 range
# 구구단 2~9단 출력
for dan in range(2, 10):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

# 함수 정의와 반환
def calculate_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    else: return "C"

# 가변 길이 인자
def visit(day, *customers):
    for c in customers:
        print(f"{day}: {c}")

visit("Monday", "Kim", "Lee")
```
