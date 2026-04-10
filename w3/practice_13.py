# 실습 13: 2단부터 9단까지 구구단 모두 출력하기
# - 2단 ~ 9단 출력 (바깥 for문: range(2, 10))
# - 각 단마다 1~9까지 곱하기 (안쪽 for문: range(1, 10))
# - 단이 바뀔 때 보기 좋게 한 줄 띄우기 ( print() 사용 )

# 여기에 코드를 작성하세요.

for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print()