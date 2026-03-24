class Employee:
	raise_amount = 1.04
	def __init__(self,firstname,lastname,pay):
		self.firstname = firstname
		self.lastname = lastname
		self.pay = pay
		print(f"hello ! {firstname} {lastname}")
	def fullname(self):
		print(f"{self.firstname} {self.lastname} pay :{self.pay}")


emp_1 = Employee("abhinav","prakash",10000)
emp_2 = Employee("mahima",'yadav',200000)
print(emp_1)
print(emp_2)

emp_1.firstname = "abhinav"
emp_1.lastname  = "prakash"
emp_2.firstname = "mahima"
emp_2.lastname  = "yadav"
emp_1.age = 34
emp_1.fullname()