#JUST A NORMAL NESTED FUNCTION
def outer_function(msg):
	def innter_function():
		print(msg)
	return innter_function
hifunc = outer_function("hi")
byefunc = outer_function("bye")
#hifunc()
#byefunc()


#DECORATOR FUNCTION 
def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		return original_function(*args,**kwargs)
	return wrapper_function
def display():
	print('display function ran')
decorated_display = decorator_function(display)
decorated_display()


#SAME AS DECORATOR FUNCTION 
@decorator_function   # same as display = decorator_function(display)
def display():
	print("display function ran")


#INCLUDING A PARAMATERISED FUNCTION IN DECORATOR  we need *args,**kwargs
@decorator_function
def display_info(name,age):
	print('display_info ran with arguments ({},{})'.format(name,age))
display_info('john',25)