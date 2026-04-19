# Usage:
#   python this_verifier.py /path/to/student_file.py
# If no path is given, it tries ./student.py

import io
import sys
import runpy
import contextlib

PUBLIC_CASES = [
    (
        {
            "name": "해리 포터",
            "age": 17,
            "height": 165.0,
            "weight": 55.0,
            "blood_pressure": (110, 70),
            "activity_record": [8000, 7500, 9000, 10000, 7000]
        },
        """해리 포터 (17) 님의 건강 진단 결과:
- BMI: 20.2 → 정상 체중
- 혈압: 110/70 → 정상 혈압
- 활동량: 평균 8300걸음 → 활동량 충분"""
    ),
    (
        {
            "name": "다스 베이더",
            "age": 45,
            "height": 165.0,
            "weight": 110.0,
            "blood_pressure": (140, 90),
            "activity_record": [3000, 3500, 2800, 3100]
        },
        """다스 베이더 (45) 님의 건강 진단 결과:
- BMI: 40.4 → 비만
- 혈압: 140/90 → 고혈압 주의
- 활동량: 평균 3100걸음 → 활동량 부족"""
    ),
]


def normalize(text):
    lines = [line.rstrip() for line in text.strip().splitlines()]
    return "\n".join(lines)


def load_namespace(path):
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        namespace = runpy.run_path(path, run_name="__main__")
    return namespace


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "student.py"

    try:
        namespace = load_namespace(path)
    except Exception as e:
        print(f"[실패] 코드 실행 중 오류 발생: {e}")
        sys.exit(1)

    report_health = namespace.get("report_health")
    if not callable(report_health):
        print("[실패] report_health 함수가 정의되어 있지 않습니다.")
        sys.exit(1)

    passed = 0
    for idx, (case_input, expected) in enumerate(PUBLIC_CASES, start=1):
        captured = io.StringIO()
        try:
            with contextlib.redirect_stdout(captured):
                report_health(case_input)
        except Exception as e:
            print(f"[케이스 {idx} 실패] 함수 실행 오류: {e}")
            continue

        actual = normalize(captured.getvalue())
        expected = normalize(expected)

        if actual == expected:
            print(f"[케이스 {idx} 통과]")
            passed += 1
        else:
            print(f"[케이스 {idx} 실패]")
            print("기대한 출력:")
            print(expected)
            print("실제 출력:")
            print(actual)

    print(f"\n총 {passed} / {len(PUBLIC_CASES)} 케이스 통과")
    sys.exit(0 if passed == len(PUBLIC_CASES) else 1)


if __name__ == "__main__":
    main()
