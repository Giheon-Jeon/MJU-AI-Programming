# 6주차 학습 내용 요약 (객체 지향 프로그래밍 기초)

## 1. Class와 Object (객체)
- **Class (클래스):** 객체를 만들기 위한 **설계도** 또는 템플릿입니다. (예: `붕어빵 틀`, `블랙박스 설계도`)
- **Object (객체/인스턴스):** 클래스로부터 생성된 **실제 제품**입니다. (예: `붕어빵`, `내 차에 달린 블랙박스 b1`)
- **추상화:** 복잡한 내부 로직은 감추고 필요한 기능만 외부에 노출하는 것.

## 2. 클래스 구조와 `self`
`self`는 클래스 내부에서 **"현재 작업 중인 바로 그 객체"**를 가리키는 예약어입니다.

### 2.1. `__init__` 메서드 (생성자)
객체가 생성될 때 자동으로 호출되며, 객체의 초기 상태(속성)를 설정합니다.

### 2.2. `self` 사용 규칙
- **객체의 상태(데이터) 저장:** `self.name = name` (인스턴스 변수)
- **메서드 정의:** 모든 메서드의 첫 번째 인자는 반드시 `self`여야 합니다.
- **데이터 활용:** 다른 메서드에서 저장된 값을 꺼낼 때 `self.name` 사용.

## 3. 핵심 예제 코드
```python
class Student:
    def __init__(self, name, grade):
        self.name = name    # 인스턴스 변수 설정
        self.grade = grade
        self.attendance = 0 # 기본값 설정

    def introduce(self):
        # f-string에서 self를 통해 속성에 접근
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다.")

    def check_in(self):
        self.attendance += 1
        print(f"{self.name} 학생의 출석 횟수: {self.attendance}")

# 객체 생성 및 활용
s1 = Student("현준", 2)
s1.introduce()
s1.check_in()
```

## 💡 튜터의 꿀팁 (Pro-Tips)
1. **변수 스코프 구분:** 함수 내에서만 쓰는 지역 변수와 객체에 저장할 `self.변수`를 명확히 구분하세요.
2. **주머니(Memory) 개념:** `self.something`이라고 쓰는 순간, 그것은 그 객체의 고유한 메모리 주머니에 저장되어 객체가 사라질 때까지 유지됩니다.
3. **Naming:** 클래스 이름은 보통 `PascalCase`(첫 글자 대문자)를 사용합니다.
