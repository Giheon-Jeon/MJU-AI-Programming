"""
practice.txt 파일 단어 치환

Java -> Python으로 변경에서 파일에 저장
"""

with open("w4/practice.txt", "r", encoding="utf-8") as f:
    data = f.read()

new_data = data.replace("Java", "Python")

with open("w4/practice.txt", "w", encoding="utf-8") as f:
    f.write(new_data)