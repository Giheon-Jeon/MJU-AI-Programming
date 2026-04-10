import importlib

ipData = input("어떤 모듈을 실행할까요?(a 또는 b): ")

if ipData == 'a':
    #a 입력받은 경우
    mod = importlib.import_module("a")
    mod.print_input()
elif ipData == 'b':
    #b 입력받은 경우
    mod = importlib.import_module("b")
    mod.print_input()
else:
    #잘못된 입력
    print("잘못된 입력입니다.")