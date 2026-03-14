#context managers (autmatically closes the file)
with open("test.txt",'r') as f:
	f_contents = f.read() #print entire file
	f_contents2 = f.readlines() #this returns a list of all the lines of the file
	f_contents3 = f.readline() #reads the first line from the file 
	#print(f_contents,end='') #end to remove extra new lines 


#OPENING A FILE
f = open("test.txt",'r')


#f.read() MADNESS
lines = f.read(17)#number of characters to read


#setting position of the pointer at 0 index
f.seek(0)


#reading small chunks 
nolines = 3
f_contents = f.read(nolines)
while len(f_contents) > 0:
	print(f_contents)
	print(f.tell()) #tells the position of the pointer
	f_contents = f.read(nolines)

#iterating the file
for line in f:
	pass
	#print(line,end="")


#printing the name of the file 
name = f.name


#printing the mode in which file is opened 
mode = f.mode


#closing the file 
f.close()


#opening a file in append mode (use w for write mode)
with open("test.txt",'a') as f:
	f.write("test\n")
	f.seek(0)
	f.write("R")


#reading and writing into a file 
with open("test.txt",'r') as rf:
	with open("test_copy.txt",'w') as wf:
		for line in rf:
			wf.write(line)

#reading a image 
with open("image.jpeg",'rb') as rf:
	with open("image_copy.jpeg",'wb') as wf:
		for line in rf:
			wf.write(line)
			

