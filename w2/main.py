import random

# 정수 난수
print(random.randint(1, 6)) # 1 ~ 6
print(random.randrange(0, 10, 2))
# 0,2,4,6,8 중 하나.

# 실수 난수
print(random.random())
# 0.0 이상 1.0 미만

print(random.uniform(1.5, 3.5))
# 1.5 ~ 3.5 사이 실수

# 시드 고정
random.seed(42)
print(random.randint(1, 100)) #항상 같은 값