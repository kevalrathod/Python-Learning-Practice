class Employee:
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.email=self.fname+'.'+self.lname+'@domain.com'
		self.pay=pay
	def Full_Name(self):
		return '{} {}'.format(self.fname,self.lname)
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