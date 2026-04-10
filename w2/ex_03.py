# List, Tuple, Set, Dictionary 예제

# [List] 편의점 장바구니 예제
cart = ["우유", "삼각김밥", "콜라"]
cart.append("껌")        # 추가 가능
cart[0] = "저지방 우유"   # 수정 가능
print(cart)             # ['저지방 우유', '삼각김밥', '콜라', '껌']


#[Tuple] 지도 좌표 예제 (위도, 경도)
location = (37.5665, 126.9780)
# location[0] = 38.0  # 에러 발생! 수정 불가
print(location[0])    # 37.5665 (조회는 가능)


#[Set] 당첨 번호 예제 (중복 자동 제거)
lotto_numbers = {1, 5, 12, 5, 22, 1}
print(lotto_numbers)   # {1, 5, 12, 22} (중복된 5와 1은 한 번만 나옴)


#[Dictionary] 사용자 프로필 예제
user = {
    "name": "홍길동",
    "age": 25,
    "email": "hong@example.com"
}
print(user["name"])    # 홍길동
user["age"] = 26       # 수정 가능