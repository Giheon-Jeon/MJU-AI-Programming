#물건의 가격
choco_price = 1500
candy_price = 1000
ice_price = 2000

#물건의 개수
choco_count = 2
candy_count = 3
ice_count = 1

#물건별 총 가격
choco_total = choco_price * choco_count
candy_total = candy_price * candy_count
ice_total = ice_price * ice_count

#최종 가격
total = choco_total + candy_total + ice_total

# f-string을 활용한 결과 출력
print(f"초콜릿 {choco_count}개는 {choco_total}원, "
      f"사탕 {candy_count}개는 {candy_total}원, "
      f"아이스크림 {ice_count}개는 {ice_total}원으로 "
      f"총 {total}원을 지불해야 합니다.")