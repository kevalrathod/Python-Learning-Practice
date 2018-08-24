class Person:
	age=25
	def printAge(clc):
		print("Age is :",age)
	Person.printAge=classmethod(Person.printAge)
Person.printAge()