import sqlite3

#conn = sqlite3.connect(':memory:') #IN MEMORY DATABASE

conn = sqlite3.connect('employee.db')

c = conn.cursor()

#CREATING COLUMNS IN THE TABLE "emoployees"
'''
c.execute("""CREATE TABLE employees(
	first text,
	last text,
	pay integer
	)""")

'''

first = input("Enter the first name : ")
last  = input("Enter the last name :")
pay = int(input("Enter the pay : "))
#c.execute("INSERT INTO employees VALUES('mahima','yadav',10000)")
c.execute("SELECT * FROM employees")
print(c.fetchall())
conn.commit()
conn.close()