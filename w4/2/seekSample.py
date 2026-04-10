with open("w4/2/practice.txt", "r+", encoding="utf-8") as f:
	data = f.read()
	print("현재 위치: ", f.tell()) #파일 끝 위치
	f.seek(0) #처음으로 이동
	f.write("수정된 첫 줄\n")