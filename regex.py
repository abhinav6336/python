import re

#declaring string to search from it 
text_to_search='''
abcdefghijklmonpqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped)
. ^ $ * + ? { } [ ]  | ()
coreyms.com
321-555-4321
123.533.1234
Mr.Abhinav
Mr sanskar
Ms. mahima
MRS. komal
Mr.T
'''
sentence = " Start a sentence then bring it to end"
#print(r'\tTab')



#TO SEARCH A STRING IN ANOTHER STRING
pattern = re.compile('abc')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)#returns span(1,4)
	print(text_to_search[1:4])



#TO SEARCH A SPECIAL CHARACTER LIKE (.\{}[]) IN ANOTHER STRING
pattern = re.compile('.') #this will return every character from the searched string because (.) is special character in regex
pattern2= re.compile('\\.')#this is the correct way to search for special characters (\.)
matches = pattern2.finditer(text_to_search)
for match in matches:
	pass
	#print(match)#returns span(1,4)
	#print(text_to_search[1:4])

#TO SEARCH A URL IN ANOTHER STRING
pattern = re.compile('coreyms\\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)#returns span(1,4)
	#print(text_to_search[1:4])
