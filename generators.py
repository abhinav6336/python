def square_nums(nums):
	for i in nums:
			yield (i*i)
mynums = square_nums([1,2,3,4,5,6,7,8])
print (next(mynums))
print (next(mynums))
print (next(mynums))