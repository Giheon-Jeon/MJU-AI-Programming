# Usage:
#   python this_verifier.py /path/to/student_file.py
# If no path is given, it tries ./student.py

import ast
import io
import re
import sys
import runpy
import contextlib

ALLOWED_ACTIONS = {"몸통 박치기", "크게 할퀴기", "강력한 공격", "휴식"}


def normalize_lines(text):
    return [line.rstrip() for line in text.splitlines() if line.strip() != ""]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "student.py"

    captured = io.StringIO()
    try:
        with contextlib.redirect_stdout(captured):
            runpy.run_path(path, run_name="__main__")
    except Exception as e:
        print(f"[실패] 코드 실행 중 오류 발생: {e}")
        sys.exit(1)

    lines = normalize_lines(captured.getvalue())
    if len(lines) != 8:
        print("[실패] 출력 줄 수가 올바르지 않습니다. (공백 줄 제외 8줄 필요)")
        print("실제 줄 수:", len(lines))
        sys.exit(1)

    expected_headers = [
        "문제 3-1: 최적 체력 감소",
        "문제 3-2: 최적 기력",
    ]
    if lines[0] != expected_headers[0] or lines[4] != expected_headers[1]:
        print("[실패] 문제 제목 형식이 올바르지 않습니다.")
        print("실제 제목:", lines[0], "/", lines[4])
        sys.exit(1)

    for offset in (1, 5):
        line = lines[offset]
        if not line.startswith("행동 조합 : "):
            print("[실패] 행동 조합 줄 형식이 올바르지 않습니다.")
            print("실제:", line)
            sys.exit(1)
        try:
            seq = ast.literal_eval(line.split(":", 1)[1].strip())
        except Exception:
            print("[실패] 행동 조합을 리스트로 해석할 수 없습니다.")
            sys.exit(1)
        if not isinstance(seq, list) or len(seq) != 8:
            print("[실패] 행동 조합은 길이 8의 리스트여야 합니다.")
            sys.exit(1)
        if any(action not in ALLOWED_ACTIONS for action in seq):
            print("[실패] 행동 조합에 허용되지 않은 행동 이름이 있습니다.")
            print("실제:", seq)
            sys.exit(1)

    hp_pattern = re.compile(r"^최종 상대 체력 : \d+$")
    energy_pattern = re.compile(r"^최종 남은 기력 : \d+$")

    if not hp_pattern.match(lines[2]) or not energy_pattern.match(lines[3]):
        print("[실패] 문제 3-1의 수치 출력 형식이 올바르지 않습니다.")
        sys.exit(1)
    if not hp_pattern.match(lines[6]) or not energy_pattern.match(lines[7]):
        print("[실패] 문제 3-2의 수치 출력 형식이 올바르지 않습니다.")
        sys.exit(1)

    print("[통과] 문제 3 공개용 verifier: 출력 포맷이 올바릅니다.")
    sys.exit(0)


if __name__ == "__main__":
    main()
