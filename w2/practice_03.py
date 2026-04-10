"""
사이트별 비밀번호 만들기

조건 1 http:// 부분은 제외한다
조건 2 첫 번째 점 이후 부분도 제거한다
조건 3 처음 세 글자 + 글자 수 + 'e'의 개수 + '!'로 비밀번호를 구성한다
"""

url = "http://naver.com"
pwd_data = url.replace("http://", "")
pwd_data = pwd_data[:pwd_data.index('.')]

print(f"{pwd_data[:3]}{len(pwd_data)}{pwd_data.count('e')}!")




# 추가. 여러 프로토콜과 형식을 고려한 방식
url = "https://www.google.com"
pwd_data = url.replace("http://", "").replace("https://", "").replace("www.", "")
pwd_data = pwd_data.split('.')[0] # index() 대신 split() 사용

print(f"{pwd_data[:3]}{len(pwd_data)}{pwd_data.count('e')}!")