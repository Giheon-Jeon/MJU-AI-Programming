"""
입력에 따라 다른 모듈 실행하기

키보드의 입력을 받기
a -> a.py의 print_input()
b -> b.py의 print_input()
그 외 -> "잘못된 입력입니다"
"""

import importlib

data = input("input data >> ")
if data == "a": 
    mod = importlib.import_module("a")
    mod.print_input()
elif data == "b":
    mod = importlib.import_module("b")
    mod.print_input()
else:
    print("잘못된 입력입니다.")