def multiply_all(*args):
    """모든 숫자를 곱하는 함수 (*args 예제)"""
    result = 1
    print(f"전달받은 모든 위치 인자(args): {args}")
    
    for num in args:
        result *= num
    return result

def print_user_info(**kwargs):
    """사용자 정보를 출력하는 함수 (**kwargs 예제)"""
    print(f"전달받은 키워드 인자(kwargs): {kwargs}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("-" * 20)

# 1. *args 사용 결과
print("[*args 테스트]")
print(f"결과: {multiply_all(1, 2, 3)}")       # 3개 전달
print(f"결과: {multiply_all(1, 2, 3, 4, 5)}") # 5개 전달
print("\n")

# 2. **kwargs 사용 결과
print("[**kwargs 테스트]")
# 필요한 만큼 키워드를 마음대로 추가할 수 있습니다.
print_user_info(name="전기헌", major="AI")
print_user_info(name="김철수", age=25, city="Seoul", status="In school")

# 3. 혼합 사용
def super_function(*args, **kwargs):
    print(f"위치 인자들: {args}")
    print(f"키워드 인자들: {kwargs}")

print("[혼합 사용 테스트]")
super_function(1, 2, 3, a=10, b=20)
