def Outer():
	msg='hi'

	def inner():
		print(msg)
	return inner

myFunc=Outer()
myFunc()