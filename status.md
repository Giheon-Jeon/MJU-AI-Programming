### [2026-04-24 / w7 세션 업데이트]
- **학습 내용 (Topics Covered):**
  - NumPy `axis`의 개념과 다차원 배열(2D, 3D)에서의 동작 원리 학습
  - `np.sum()` 함수를 활용하여 각 축 방향으로의 데이터 압축 및 합계 계산 실습
  - 다차원 배열의 인덱싱(Indexing) 및 슬라이싱(Slicing)을 통한 데이터 추출 실습
  - NumPy 브로드캐스팅(Broadcasting)의 3대 규칙 이해 및 연산 가능 여부 판단 실습
  - `np.dot()`을 활용한 벡터 내적 및 행렬 곱셈 연산과 차원 일치 조건 학습
  - **추가 학습:** Python 파일 입출력(`r+`, `seek`, `tell`) 및 NumPy/Pandas 기본 데이터 확인법
- **주요 성취 및 강점 (Strengths & Progress):**
  - 브로드캐스팅 및 행렬 곱셈의 차원 일치 원리를 완벽하게 파악함.
  - 데이터의 타입(`dtype`) 표현(예: `0.`)이나 CSV 헤더 처리 등 세밀한 라이브러리 동작 원리에 대해 깊이 있는 질문을 던지며 이해도를 높임.
- **취약점 및 고질적 실수 (Vulnerabilities & Chronic Mistakes):**
  - 파일 모드(`r+`)에서의 커서 위치 변화에 대한 초기 혼동이 있었으나, `read()`와 `seek()`의 관계를 통해 해결함.
- **다음 학습을 위한 가이드 (Actionable Insights & Review Plan):**
  - Pandas의 다양한 데이터 필터링 기법 및 시각화 기초로 진도를 확장할 예정.

### [2026-04-25 / 시험 대비 통합 정리 업데이트]
- **학습 내용 (Topics Covered):**
  - 1주차(환경 설정)부터 7주차(NumPy)까지의 전 과정 핵심 개념 복습
  - `exam_summary.md` 및 `exam_summary.py`를 통한 통합 예제 코드 구현 및 정리
- **주요 성취 및 강점 (Strengths & Progress):**
  - 기초 문법(Slicing, Data Structures)부터 심화 개념(OOP, Axis)까지 전체적인 흐름을 파악하고 통합 예제로 구현함.
- **취약점 및 고질적 실수 (Vulnerabilities & Chronic Mistakes):**
  - 주차별로 산재된 개념들이 섞일 수 있으므로, 각 도구(List vs NumPy)의 차이점(예: Vectorization 여부)을 명확히 구분하는 연습이 필요함.
- **다음 학습을 위한 가이드 (Actionable Insights & Review Plan):**
    - 생성된 `exam_summary.py`를 직접 실행하며 출력 결과를 예측해보고, 틀린 부분은 `knowledge.md`의 상세 설명을 다시 확인할 것.

### [2026-04-26 / w7 세션 업데이트]
- **학습 내용 (Topics Covered):**
  - 기존 주차별 `knowledge.md` 파일들의 누락된 개념(OOP 예제, Broadcasting 규칙, 행렬 곱셈 등) 보완 및 동기화
  - 시험 대비 통합 정리본(`exam_summary.md`)의 내용을 각 주차별 지식 저장소로 분산 업데이트
- **주요 성취 및 강점 (Strengths & Progress):**
  - 학습한 모든 내용을 체계적으로 구조화하여 나중에 다시 보기 편하도록 정리함.
- **취약점 및 고질적 실수 (Vulnerabilities & Chronic Mistakes):**
  - Broadcasting 규칙 3가지를 명확히 구분하는 것에 주의가 필요함.
- **다음 학습을 위한 가이드 (Actionable Insights & Review Plan):**
  - 이제 모든 지식 파일이 최신화되었으므로, 다음 세션부터는 Pandas의 심화 기능(Data Cleaning, GroupBy) 실습으로 진입할 예정.

