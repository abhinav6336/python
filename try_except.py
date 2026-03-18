#CATCHING A GENERAL EXCEPTION 
try:
	f = open("test.txt")
except FileNotFoundError:
	print("Sorry. This file does not exist ! ")
except Exception:
	print("some error occured !!")
else:
	print(f.read())
	f.close()
finally:
	print("executing finally")


#CATCHING A PARTICULAR EXCEPTION 
try:
	f=10/0
except ZeroDivisionError:
	print("u can not divide by zero")


#RAISING UR OWN EXCEPTION
try:
	f=open("test.txt")
	if f.name=='test.txt':
		raise Exception
except Exception as e:
	print("Error occured")