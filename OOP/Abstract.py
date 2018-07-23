class Food:
	def eat(): #create empty method no need to i=create object for this method
		pass
class Veg(Food):
	def eat(self):
		print("Vegetaria eats roti...")
class nonVeg(Food):
	def eat(self):
		print("Non veg eats chicken...")
obj1 = Veg()
obj1.eat()
obj2 = nonVeg()
obj2.eat()


