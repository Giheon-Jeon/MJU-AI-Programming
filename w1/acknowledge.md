# 1주차 학습 내용

## 주제
파이썬 기초 I (강의 소개, 파이썬 설치 및 환경 세팅)

## 개념 요약
- **AI 프로그래밍의 중요성**: 양질의 도메인 데이터 전처리, 다양한 AI 모델 프로토타이핑을 통한 최적화.
- **Python**: 수많은 AI 관련 라이브러리 지원(numpy, pandas 등).
- **Antigravity**: AI 에이전트 기반 IDE.
- **Anaconda**: Python 패키지 관리 및 가상환경(Virtual Environment) 도구.
- **가상환경(Virtual Environment)**: 프로젝트마다 요구하는 패키지 버전이 다를 때 격리된 독립적인 환경을 제공함 (`conda create`, `conda activate`, `conda deactivate`).
- **requirements.txt / environment.yaml**: 패키지 목록을 추출하고 동일 환경을 복원할 때 사용.
- **Notion + MCP 연결**: 학습 내용을 정리해 자동으로 Notion에 업로드할 수 있게 연동.

## 기억해야 할 꿀팁
- **코드 자동 생성 옵션 끄기**: `Preferences > Antigravity Settings > Tab > Suggestions in Editor` 체크 해제하여 직접 코드를 작성하며 학습.
- **프로젝트 구성**: `ai_programming` 폴더 안에 `w1`, `w2` 등의 폴더를 나누어 주차별 `knowledge.md` 로 관리하고, 루트에 `tutor.md`(프롬프트)와 `status.md`를 둔다.
- **에이전트 명령어 (#init, #update, #help)**: 직접 학습 맥락을 관리하도록 프롬프트 룰을 셋팅.

## 코드 스니펫
```bash
# 가상환경 생성 및 활성화
conda create -n ai_env python=3.11
conda activate ai_env

# 패키지 추출 및 설치
conda env export > ai_env.yaml
conda env create -f ai_env.yaml
```
