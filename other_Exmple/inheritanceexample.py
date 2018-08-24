class Employee:
	amount=2.5
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.email=self.fname+'.'+self.lname+'@domain.com'
		self.pay=pay
	def Full_Name(self):
		return '{} {}'.format(self.fname,self.lname)
	def apply_rasie(self):
		self.pay= int(self.pay*self.amount)
		print("New pay of "+self.fname+'-->',self.pay)
	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.fname,self.lname,self.pay)
	def __str__(self):
		return '{}-->{}'.format(self.Full_Name(),self.email)
	def __add__(self,other):
		return self.pay+other.pay
 	
class Developer(Employee):
	 def __init__(self,fname,lname,pay,lang):
	 	super().__init__(fname,lname,pay)
	 	self.lang=lang
class Manager(Employee):
		def __init__(self,fname,lname,pay,employee=None):
			super().__init__(fname,lname,pay)
			if employee is None:
				self.employee=[]
			else:
				self.employee=employee
		def Add_emp(self,emp):
			if emp not in self.employee:
				self.employee.append(emp)
		def remove(self,emp):
			if emp in self.employee:
				self.employee.remove(emp)
		def print_employee(self):
			for emp in self.employee:
				print("---->",emp.Full_Name())

			
emp1=Employee('abc','cbd',21000)
emp2=Employee('sudo','Diy',22000)
dev1=Developer('Sui','Chan',23000,'C++')

print(emp1.email)
print(emp1.Full_Name())
print(dev1.email)
print(dev1.lang)



mng=Manager('Joe','Moskow',30000,[dev1])
print(mng.Full_Name())
print(mng.email)
mng.Add_emp(emp2)
mng.print_employee()

#isinstance is return True or False if object is instance of your object or not.

print(isinstance(mng,Manager)) # Return True
print(isinstance(mng,Employee)) # Return True
print(isinstance(mng,Developer)) #Return False

#issubclass is return true or false if the subclass is found or not.
#First is Class and second arg is for subclass
print(issubclass(Developer,Employee)) #True
print(issubclass(Employee,Developer)) #Fasle



emp1.apply_rasie()
print(str(emp1))
print(repr(emp1))

print(emp1+emp2)
