# AI 프로그래밍 중간/기말 대비 통합 정리본 (w1~w7)

안녕하세요! 지금까지 열심히 달려온 내용을 한눈에 볼 수 있도록 핵심 개념과 예제 코드를 정리해 드립니다. 이 파일은 시험 전 마지막 복습용으로 활용하면 아주 좋습니다.

---

## 1. 파이썬 기초 및 환경 (w1-w2)
- **가상환경:** 프로젝트별 독립된 패키지 환경 (`conda create`, `pip install`).
- **자료형:** `int`, `float`, `str`, `bool` 및 형변환.
- **문자열 슬라이싱:** `text[start:end:step]` (end는 포함 X).
- **데이터 구조:** 
  - `List []`: 순서 O, 수정 O
  - `Tuple ()`: 순서 O, 수정 X
  - `Set {}`: 중복 X, 순서 X
  - `Dict {K:V}`: 키-값 쌍

```python
# [핵심 예제] 리스트와 문자열 처리
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[::-1])  # 리스트 뒤집기

info = "20240425-Sun"
date = info[:8]      # '20240425' 추출
```

---

## 2. 제어 흐름과 함수 (w3)
- **반복문:** `for` (범위/리스트 순회), `while` (조건부 반복).
- **함수 정의:** `def` 키워드, 매개변수(`parameter`), 반환값(`return`).
- **가변 인자:** `*args`(튜플), `**kwargs`(딕셔너리).

```python
# [핵심 예제] 가변 인자를 활용한 함수
def print_scores(name, *scores):
    total = sum(scores)
    avg = total / len(scores) if scores else 0
    print(f"{name}님의 평균 점수: {avg:.2f}")

print_scores("김현준", 90, 85, 95)
```

---

## 3. 파일 처리 및 디버깅 (w4)
- **파일 모드:** `r`(읽기), `w`(쓰기), `a`(추가), `r+`(읽기/쓰기).
- **Context Manager:** `with open(...) as f:` (자동 close).
- **바이너리 저장:** `pickle` (파이썬 객체 저장).
- **디버깅:** Breakpoint, Step Over(F10), Step Into(F11).

```python
# [핵심 예제] CSV 파일 읽기 및 데이터 처리
import csv
import pickle

# CSV 읽기 (헤더 제외)
def read_csv_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        return list(reader)

# 객체 저장 (Pickle)
data = {"points": [10, 20, 30]}
with open("game_data.pkl", "wb") as f:
    pickle.dump(data, f)
```

---

## 4. 객체 지향 프로그래밍 (w6)
- **클래스(Class):** 객체를 만들기 위한 설계도.
- **인스턴스(Instance):** 클래스로부터 생성된 실제 객체.
- **self:** 객체 자기 자신을 가리키며, 메서드의 첫 번째 인자로 필수.

```python
# [핵심 예제] 기본 클래스 구조
class Student:
    def __init__(self, name, grade):
        self.name = name  # 인스턴스 변수
        self.grade = grade

    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다.")

s1 = Student("현준", 2)
s1.introduce()
```

---

## 5. NumPy & 데이터 분석 기초 (w7)
- **Axis (축):** 
  - `axis=0`: 행 방향 (위->아래, 열별 연산)
  - `axis=1`: 열 방향 (좌->우, 행별 연산)
- **Shape 이해:** (Depth, Row, Col) 순서.
- **Pandas 기초:** `read_csv()`, `head()`, `shape`.

```python
import numpy as np

# [핵심 예제] 2차원 배열 Axis 연산
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print(arr.sum(axis=0))  # [5, 7, 9] (열별 합)
print(arr.sum(axis=1))  # [6, 15]   (행별 합)

# linspace와 타입
x = np.linspace(0, 10, 5) # [ 0.   2.5  5.   7.5 10. ] (항상 float)
```

---

## 💡 튜터의 시험 대비 꿀팁 (Pro-Tips)
1. **타입 체크:** `type()`과 `.dtype` (NumPy)을 확인하는 습관을 들이세요. `linspace`처럼 실수(`float`)를 반환하는 함수들을 주의 깊게 보세요.
2. **Axis의 직관적 이해:** "해당 축을 따라(along) 요소를 뭉친다"라고 생각하면 쉽습니다. `axis=0`을 연산하면 0번 인덱스(행)가 사라지고 열만 남습니다.
3. **디버깅 실력:** 시험 문제에서 에러 코드가 나왔을 때, `IndexError`(범위 초과)인지 `TypeError`(연산 불가)인지 구분하는 능력이 중요합니다.

**열공해서 좋은 결과 있길 바랍니다! 추가로 궁금한 부분이 있으면 언제든 물어보세요!**
