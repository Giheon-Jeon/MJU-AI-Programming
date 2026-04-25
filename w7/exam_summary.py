"""
AI 프로그래밍 통합 복습 예제 코드 (w1 ~ w7)
이 파일은 지금까지 배운 주요 문법과 라이브러리 활용법을 직접 실행하며 확인할 수 있도록 구성되었습니다.
"""

import numpy as np
import csv
import pickle
import os

# --- 1. 기초 자료형 및 데이터 구조 (w2) ---
def review_basics():
    print("\n=== 1. Basics & Data Structures ===")
    text = "Python Programming"
    # 슬라이싱: [start:end:step]
    print(f"Slicing [0:6]: {text[0:6]}") # Python
    print(f"Reverse: {text[::-1]}")     # gnimmargorP nohtyP
    
    # 리스트와 딕셔너리
    my_list = [10, 20, 30]
    my_dict = {"name": "AI", "ver": 3.11}
    print(f"List Append: {my_list + [40]}")
    print(f"Dict Access: {my_dict['name']}")

# --- 2. 제어문과 함수 (w3) ---
def review_control_flow(name, *scores, threshold=80):
    print("\n=== 2. Control Flow & Functions ===")
    # 가변 인자 *scores 사용
    avg = sum(scores) / len(scores) if scores else 0
    
    # 조건문
    if avg >= threshold:
        result = "Pass"
    else:
        result = "Fail"
    
    print(f"{name} Result: {result} (Avg: {avg:.2f})")
    
    # 반복문 (range)
    print("Range Loop: ", end="")
    for i in range(1, 4):
        print(i, end=" ")
    print()

# --- 3. 파일 입출력 및 예외 처리 (w4) ---
def review_file_io():
    print("\n=== 3. File I/O & Serialization ===")
    filename = "test_data.pkl"
    sample_data = {"key": "value", "list": [1, 2, 3]}
    
    # Pickle 저장 (Binary Write)
    with open(filename, "wb") as f:
        pickle.dump(sample_data, f)
    
    # Pickle 로드 (Binary Read)
    with open(filename, "rb") as f:
        loaded_data = pickle.load(f)
        print(f"Loaded Pickle: {loaded_data}")
    
    # CSV 파일 생성 예시 (간략)
    csv_name = "sample.csv"
    with open(csv_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Score"])
        writer.writerow(["A01", 95])
    print(f"'{csv_name}' created.")

# --- 4. 클래스와 객체 (w6) ---
class Calculator:
    def __init__(self, owner):
        self.owner = owner # self를 통한 인스턴스 변수 설정
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def show_history(self):
        print(f"[{self.owner}'s History]: {self.history}")

def review_oop():
    print("\n=== 4. Object-Oriented Programming ===")
    calc = Calculator("Hyunjun")
    calc.add(10, 20)
    calc.add(5, 7)
    calc.show_history()

# --- 5. NumPy & Axis (w7) ---
def review_numpy():
    print("\n=== 5. NumPy & Axis Concepts ===")
    # 2D Array
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Original Array:\n{arr}")
    
    # Axis 연산 (중요!)
    # axis=0: 열방향 (세로로 합침) -> 결과 (3,)
    print(f"Sum (axis=0): {arr.sum(axis=0)}") 
    # axis=1: 행방향 (가로로 합침) -> 결과 (2,)
    print(f"Sum (axis=1): {arr.sum(axis=1)}")
    
    # linspace (실수형 반환)
    ls = np.linspace(0, 1, 3)
    print(f"Linspace (float): {ls}")

# --- 실행부 ---
if __name__ == "__main__":
    review_basics()
    review_control_flow("Student_A", 85, 90, 78)
    review_file_io()
    review_oop()
    review_numpy()
    
    print("\n" + "="*30)
    print("모든 복습 예제가 실행되었습니다!")
