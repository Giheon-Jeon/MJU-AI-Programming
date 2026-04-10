# 문자열 슬라이싱 마스터하기 (slicingExample.py)

text = "Artificial Intelligence"

print("--- [LEVEL 1] 기본 인덱싱 ---")
print(f"1. 첫 번째 글자: {text[0]}")
print(f"2. 11번째 글자(I): {text[11]}")
print(f"3. 맨 뒤에서 첫 번째 글자: {text[-1]}")
print()

print("--- [LEVEL 2] 기본 슬라이싱 ---")
print(f"4. 앞부분 'Art': {text[0:3]}")
print(f"5. 'Intelligence'만 추출: {text[11:23]}")
print(f"6. 처음부터 10번까지: {text[:10]}") 
print(f"7. 11번부터 끝까지: {text[11:]}") 
print()

print("--- [LEVEL 3] 스텝(Step) 활용 ---")
nums = "0123456789"
print(f"8. 짝수만 출력: {nums[::2]}")  
print(f"9. 3의 배수 출력: {nums[3::3]}") 
print(f"10. 문자열 뒤집기: {text[::-1]}")
print()

print("--- [LEVEL 4] 실무 응용 ---")
file_path = "2026_AI_Final_Output.pdf"
extension = file_path[-3:]
filename = file_path[:-4]
print(f"11. 파일명: {filename}")
print(f"12. 확장자: {extension}")
print()

# [CHALLENGE] 스스로 풀어보기!
# ----------------------------------------
# 문제: quiz 문자열에서 슬라이싱을 사용하여 "IA"가 출력되도록 해보세요. (AI를 뒤집은 형태)
quiz = "I love AI programming"

# 여기에 코드를 작성해보세요 (예: answer = quiz[...])
answer = quiz[7:9][::-1]
print(answer)
