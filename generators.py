#USING  YEILDING 
def square_nums(nums):
	for i in nums:
			yield (i*i)
mynums = square_nums([1,2,3,4,5,6,7,8])
#print (next(mynums)) #prints each i*i
#print (next(mynums))
#print (next(mynums))
print(list(mynums))
#for i in mynums:
#	print (i)


#USING GENERATORS TO YIELD
mynums = (x*x for x in [1,2,3,4,5,6,7,8])
print(mynums)

#USING GENERATORS IN LIST
mynums = [x*x for x in [1,2,3,4,5,6,7,8]]
print(mynums)
