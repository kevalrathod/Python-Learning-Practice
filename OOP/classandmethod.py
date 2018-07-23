#class and object example
class Dog:
	def __init__(self, name, age):
		self.name=name
		self.age=age
mike = Dog("mike",3)
lexy = Dog("lexy",6)

print(mike.name)
print(mike.age)

mike.species="mammal"
lexy.breed = "Husky"
print(mike.species)
print(lexy.breed)

