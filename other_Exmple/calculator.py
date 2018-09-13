class Calculator:
	def __init__(self, input1,input2):
		self.input1=input1
		self.input2=input2
	def sumFun(self):
		# self.input1+self.input2
		# return
		return self.input1+self.input2
	def subFun(self):
		return self.input1-self.input2
	def mulFun(self):
		return self.input1*self.input2
	def divFun(self):
		return self.input1/self.input2
n=Calculator(int(input()),int(input()))
print("summation:",n.sumFun())
print("Subtraction: " ,n.subFun())
print("Multiplication :",n.mulFun())
print("Division: " ,n.divFun())
