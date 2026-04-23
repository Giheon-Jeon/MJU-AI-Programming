count = 1
def increment():
	global count #전역변수를 함수 안에서 수정하겠다고 선언
	count += 1
increment()
print(count) # 2