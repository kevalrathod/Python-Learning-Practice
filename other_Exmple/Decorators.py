def Outer():
	msg='hi'

	def inner():
		print(msg)
	return inner

myFunc=inner()
myFunc()