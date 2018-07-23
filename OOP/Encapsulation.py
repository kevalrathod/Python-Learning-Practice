#Encapsulation is hiding the actual implementation of the code. 
#With the help of access specifier like public private and protected you can do encapsulation


class Dog:
	_speed=0
	_speak=""
	def __init__(self):
		self._speed = 100
		self._speak= "haow"
		self._update()

	def Decription(self):
		return "speed is {} and speak like {}".format(self._speed, self
		._speak)
	
	def _update(self):
		print("I am private.!")

	def setMaxSpeed(self,m_speed):
		self._speed=m_speed
obj1 = Dog()
print(obj1.Decription())
obj1._speed = 200
print(obj1.Decription())

obj1.setMaxSpeed(350)
print(obj1.Decription())

