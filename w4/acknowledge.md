# 4주차 학습 내용

## 주제
파이썬 디버깅, 파일 처리 및 라이브러리, 가상환경 관리

## 개념 요약
- **모듈 실행 방식 (`__name__ == '__main__'`)**:
  - 스크립트를 직접 실행 시 `__name__` 은 `'__main__'`이 됨.
  - 다른 파일에서 `import` 할 때는 모듈 이름이 됨. 이를 통해 직접 실행 시에만 동작할 테스트/실행 코드를 분리함.
- **디버깅(Debugging)**:
  - 에러 원인 추적: `IndexError`, `TypeError` 등에 대해 어디서 발생했는지 콜스택을 확인.
  - VS Code 디버거 활용: `launch.json` 셋팅, Breakpoint(중단점) 설정.
  - **Watch**: 변수나 조건식(expression)을 등록하여 실시간 상태 확인.
  - **Step Commands**: `Step Over(F10)`(함수 실행 넘기기), `Step Into(F11)`(함수 내부 진입), `Step Out(Shift+F11)`(함수 빠져나오기).
- **파일 입출력(File I/O)**:
  - `open()`, `read()`, `write()`, `close()` 패턴 이용.
  - 파일 모드: `r`(읽기), `w`(덮어쓰기), `a`(추가하기), `r+`(읽기+쓰기), `w+`, `a+`.
  - **with 구문**: `with open("file.txt", "r") as f:` 블록이 끝나면 파일이 안전하게 자동 종료되므로 권장됨.
  - 파일 포인터: `f.seek()`으로 위치 이동, `f.tell()`로 파일 포인터 확인.
- **파일 확장자**:
  - `txt`: 일반 메모장 텍스트 파일.
  - `csv` (Comma-separated values): 표 형태 배포 파일(쉼표로 구분됨). `csv.reader` 활용 읽기 가능.
  - `pickle`: 파이썬 객체 그대로 바이너리로 직렬화해 저장/불러오기 지원 (`import pickle`). 악성코드 위협이 있을 수 있으니 신뢰할 수 있는 소스만 로드할 것.
- **가상환경 및 패키지 관리**:
  - 모듈 > 패키지 > 라이브러리의 계층 관계.
  - `pip`: 패키지 설치(`install`), 삭제(`uninstall`), 목록(`list`).
  - `venv`: 격리된 파이썬 실행/패키지 공간. 버전 충돌 방지 (`python -m venv venv`, `activate`, `deactivate`).
  - `requirements.txt`: 의존성 리스트 (`pip freeze > requirements.txt`, `pip install -r requirements.txt`).

## 기억해야 할 꿀팁
- `import csv` 로 표류의 데이터를 다룰 때 `next(reader)` 를 이용하면 첫번째 row인 헤더 컬럼을 손쉽게 건너뛸 수 있음.
- 파일 읽을 때, 한글 깨짐이 발생하면 `encoding="utf-8"` (또는 상황에 따라 `"cp949"`) 옵션을 추가할 것.
- 코드의 줄바꿈 문자 `\n` 등을 정리하려면 `string.strip()` 함수를 이용.

## 코드 스니펫
```python
# main 블록 사용
def main():
    pass

if __name__ == '__main__':
    main()

# 파일 읽어오기 (with)
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# csv.reader 활용
import csv
with open("sales.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    header = next(data) # 헤더 추출
    rows = list(data)

# pickle 파일 저장
import pickle
sample_list = [1, 2, 3]
with open("data.pkl", "wb") as f:
    pickle.dump(sample_list, f)
```
