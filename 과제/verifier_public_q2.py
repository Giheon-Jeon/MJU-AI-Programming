# Usage:
#   python this_verifier.py /path/to/student_file.py
# If no path is given, it tries ./student.py

import io
import sys
import runpy
import contextlib

PUBLIC_CASES = [
    (
        [
            12.0, 12.5, 9.5, 9.0, 9.8, 15.0, 20.0, 26.0, 27.0, 29.0,
            48.0, 50.5, 51.0, 49.0, 47.5, 45.0, 44.0, 35.0, 29.0, 22.0,
            25.0, 26.0, 26.0, 26.5
        ],
        """이상한 온도 - 너무 높은 온도: 12시 ~ 13시
이상한 온도 - 너무 낮은 온도: 3시 ~ 5시
이상한 온도 변화 - 너무 급격히 높아짐: 5시 ~ 8시
이상한 온도 변화 - 너무 급격히 높아짐: 10시 ~ 11시
이상한 온도 변화 - 너무 급격히 낮아짐: 17시 ~ 20시"""
    ),
    (
        [
            20.0, 20.0, 20.0, 20.0, 20.0, 20.0,
            26.0, 32.0, 38.0, 39.0,
            39.0, 39.0, 39.0, 39.0,
            33.0, 27.0, 26.0,
            39.0, 39.0, 39.0, 39.0, 39.0, 39.0, 38.0
        ],
        """이상한 온도 변화 - 너무 급격히 높아짐: 6시 ~ 9시
이상한 온도 변화 - 너무 급격히 높아짐: 17시 ~ 18시
이상한 온도 변화 - 너무 급격히 낮아짐: 14시 ~ 16시"""
    ),
]


def normalize(text):
    lines = [line.rstrip() for line in text.strip().splitlines() if line.strip() != ""]
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

    anomaly_temp = namespace.get("anomaly_temp")
    if not callable(anomaly_temp):
        print("[실패] anomaly_temp 함수가 정의되어 있지 않습니다.")
        sys.exit(1)

    passed = 0
    for idx, (temp_list, expected) in enumerate(PUBLIC_CASES, start=1):
        captured = io.StringIO()
        try:
            with contextlib.redirect_stdout(captured):
                anomaly_temp(temp_list)
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
