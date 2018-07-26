class Circle:
	def __init__(self, radius,color):
		self.radius = radius
		self.color =  color
	def Draw(self):
		return "radius is {} and color is  {}".format(self.radius,self.color)
	def Draw(self, Dmtr):
		return "radius is {} and diameter is {}".format(self.radius,Dmtr)
	def Draw(self, area , volume):
		return "area is {} and volume is {}".format(area,volume)
obj = Circle(4,"red")

print(obj.Draw())
print(obj.Draw(45,81))
print(obj,Draw(8))


