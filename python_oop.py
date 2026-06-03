class Employee:
	raise_amount = 1.04
	numofemployees = 0
	def __init__(self,firstname,lastname,pay):
		self.firstname = firstname
		self.lastname = lastname
		self.pay = pay
		print(f"hello ! {firstname} {lastname}")
		Employee.numofemployees+=1 #because no of employees shud be same for all instances
	def fullname(self):
		print(f"{self.firstname} {self.lastname} pay :{self.pay}")

		#CLASS METHODS
	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount=amount

		#STATIC METHODS
	@staticmethod
	def isweekday(day):
		if day.weekday()==5 or  day.weekday()==6:
			return False
		return True

		#DUNDER 
	def __repr__(self):
		print(f'Employee {self.firstname} {self.lastname}')
	def __str__(self):
		print(f"Employee : {self.raise_amount}")
	def __add__(self,other):
		return self.pay+other.pay
	def __len__(self):
		return len(self.fullname)

emp_1 = Employee("abhinav","prakash",10000)
emp_2 = Employee("mahima",'yadav',200000)
emp_1.__str__()
emp_2.__repr__()

emp_1.firstname = "abhinav"
emp_1.lastname  = "prakash"
emp_2.firstname = "mahima"
emp_2.lastname  = "yadav"

#ACCESSING THE CLASS VARIABLES
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount=1.04
Employee.raise_amount=5

#ACCESSING THE PARAMETERS OF THE CLASS AND ITS VALUES
#print(emp_1.__dict__)
#print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)


Employee.set_raise_amount(100)

import datetime
today = datetime.date.today()
print(Employee.isweekday(today))


#CREATING SUBCLASS
class Developer(Employee):
	Employee.raise_amount=33
	prog_lang='html'
	def __init__(self,firstname,lastname,pay,prog_lang=None):
		super().__init__(firstname,lastname,pay)
		self.prog_lang=prog_lang

class Manager(Employee):
	employees = None
	def __init__(self,firstname,lastname,pay,employees=None):
		super().__init__(firstname,lastname,pay)
		if employees == None:
			self.employees=[]
		else:
			self.employees=employees
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)


dev_1 = Developer("dev","sin",1000000)
print(dev_1.fullname())
print(Developer.raise_amount)

man_1 = Manager('Spidy','singh',[dev_1])
#GETTING HELP
#print(help(Developer))
#print(isinstance(man_1,Employee))
#print(issubclass(Manager,Employee))
man_1.__repr__()

print(int.__add__(1,2))
print(emp_1+emp_2)
print('abhinav'.__len__())
