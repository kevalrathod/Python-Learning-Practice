#Leran Property getter setter in python.

class Employee:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
	@property	
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)
	@property
	def email(self):
		return '{}.{}@company.com'.format(self.fname, self.lname)
	@fullname.setter
	def fullname(self,name):
		fname,lname= name.split(' ')
		self.fname=fname
		self.lname=lname
	@fullname.deleter
	def fullname(self):
		print("Name Delted")
		self.fname=None
		self.lname=None
	
emp1=Employee('Mike','Shonda')
emp1.fullname='Tyson mada'
print(emp1.fullname)
print(emp1.email)
del emp1.fullname
