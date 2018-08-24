# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# person = Person('Adam', 19)
# person.display()

# person1=Person.fromBirthYear('John',  1985)
# person1.display()

class FactoryMethod:
	rais_amount=3.14
	def __init__(self, fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
	def fullName(self):
		 return '{} {}'.format(self.fname,self.lname)
	def amount_raise(self):
		self.pay = int(self.pay*self.rais_amount)
	@classmethod #classmethod  take cls and return class method.
	def rais_amt(cls,amt):
		cls.rais_amount=amt
	@staticmethod #static method is genral function
	def is_weekday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True
per1=FactoryMethod('Mike','Hoott',20000)
per2=FactoryMethod('Lime','Neon',30000)
print(per1.fullName())
print(FactoryMethod.rais_amount)
print(per1.pay)
FactoryMethod.rais_amt(4.20)
print(per1.rais_amount)
str='Luke-brown-23000'
fname,lname,pay=str.split('-')
new_emp=FactoryMethod(fname,lname,pay)
print(new_emp.fullName())
print(new_emp.rais_amount)

import datetime
mydate=datetime.date(2018,8,16)
print(FactoryMethod.is_weekday(mydate))