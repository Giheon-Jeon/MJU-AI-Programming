class BlackBox:
	def __init__(self, name, price):
		self.name = name
		self.price = price
 
	def set_travel_mode(self, min): # 추가 인자
		print(f"{min} mins travel mode ON")

b1 = BlackBox("blackbox", 200000)
b1.set_travel_mode(100)
# 출력: 20 mins travel mode ON