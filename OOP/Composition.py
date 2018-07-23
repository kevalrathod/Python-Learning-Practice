#In composition, we do not inherit from the base class 
#but establish relationships between classes through the use of instance variables 
#that are references to other objects. 
class Description:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def Breed(self,breed):
		return "{} and breed is {}".format(self.name, breed)


class Dog:
	def __init__(self, name, age, voice):
		self.description=Description(name, age)
		self.voice =voice
	def Speak(self):
		return "{} speak like {}".format(self.description.name,self.voice)
obj1 = Dog("Mike", 21, "hahwhhaw")
obj2 = Description("Lax",23)
print(obj1.Speak())
print(obj2.Breed("Labradore"))

