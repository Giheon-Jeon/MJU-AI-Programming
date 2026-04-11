"""
practice.py 파일에서 특정 단어 찾기

Programming 단어 찾으면 "Found"
못 찾으면 "Not Found" 출력
"""

with open("w4/practice.txt", "r", encoding="utf-8") as f:
    data = f.read()

index = data.find("Programming")

if index != 1:
    print("Found")
else:
    print("Not Found")