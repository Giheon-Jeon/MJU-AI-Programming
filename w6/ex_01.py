class BlackBox:
	def __init__(self, name, price):
		self.name = name
		self.price = price
 
	def set_travel_mode(self):
		print("travel mode ON")

b1 = BlackBox("blackbox", 200000)
b1.set_travel_mode()
# 출력: travel mode ON