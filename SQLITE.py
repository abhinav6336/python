import sqlite3
from Employee import Employee

#CONNECTING TO THE EXISTING DATABASE IN THE FOLDER
conn = sqlite3.connect('employee.db')

#STARTING A TEMPORARY DATABASE FOR TESTING (RESETS EVERY TIME)
conn = sqlite3.connect(':memory:') #IN MEMORY DATABASE

c = conn.cursor()

#CREATING COLUMNS IN THE TABLE "emoployees"
c.execute("""CREATE TABLE employees(
	first text,
	last text,
	pay integer
	)""")

#USING METHODS FOR EACH OPERATIONS TO PERFORM ON DATABASE


#ENTERTING DATA INTO DATABASE CORRECT METHOD SAFE FROM SQL INJECTION 
#==?WARNING!!!?== (DONT USE .FORMAT OR F_STRING )
def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
#                                                     OR
#        c.execute("INSERT INTO employees VALUES(?,?,?)",(emp_2.first,emp_2.last,emp_2.pay))

#GETTING INFORMATION FROM DATABASE USING SPECIFIC CONDITION
def get_emps_by_name(emp):
	with conn:
		c.execute("SELECT * FROM employees WHERE (first=:first AND last=:last) ",{'first':emp.first,'last':emp.last})
		return c.fetchall()

#UPDATING THE INFORMATION OR VALUES IN THE DATABASE
def update_pay(emp,pay):
	with conn:
		c.execute("""UPDATE employees SET pay=:pay WHERE first=:first AND last=:last""",{'first':emp.first,'last':emp.last})

#DELETING DATA FROM THE DATABASE ON THE BASIS OF SPECIFIC CONDITION
def remove_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first=:first AND last=:last",{'first':emp.first,'last':emp_last})


n = int(input("Enter the number of employees : "))
for i in range(0,n):
	firstname = input("Enter the first name of the employee : ")
	lastname = input("Enter the last name of the employee : ")
	pay = float(input("Enter the pay of the employee : "))
	insert_emp(Employee(firstname,lastname,pay))

c.execute("SELECT * FROM employees")
l = c.fetchall()
for li in l:
	print(li)
conn.commit()
conn.close()