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
712-555-4321
123.533.1234
Mr. Schafer
Ms Smith
Mr Davis 
Mrs. Robinson
Mr. T
bat 
mat
hat
cat
'''
sentence = " Start a sentence then bring it to end"
#print(r'\tTab')



#TO SEARCH A STRING IN ANOTHER STRING
pattern = re.compile('abc')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)#returns span(1,4)
	#print(text_to_search[1:4])



#TO SEARCH A SPECIAL CHARACTER LIKE (.\{}[]) IN ANOTHER STRING
pattern = re.compile('.') #this will return every character from the searched string because (.) is special character in regex
pattern2= re.compile(r'\.')#this is the correct way to search for special characters (\.)
matches = pattern2.finditer(text_to_search)
for match in matches:
	pass

#TO SEARCH A URL IN ANOTHER STRING
pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)


#TO SEARCH A digit IN ANOTHER STRING
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)

#TO DO REGEX SEARCH ON A FILE
with open("search.txt",'r') as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		pass
		#print(match.group()) #to get only matched characters and remove everything else

#TO SEARCH A range of digit IN ANOTHER STRING
pattern = re.compile(r'[1-3]\d\d[-.]\d\d\d[-.]\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)


#TO LEAVE CHARACTERS IN [] OR NOT[]
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)

#USING QUANTIFIERS to denote number of digits
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)

#USING QUANTIFIERS TO DENOTE TO Search for 0 OR 1 OF THOSE CHARACTER (?)
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
	pass
	#print(match)


#TO SEARCH FOR RANGE OR GROUP LIKE (MR. MRS. MS.)
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

r"""
.       - Any Character Except New Line
\\d      - Digit (0-9)
\\D      - Not a Digit (0-9)
\\w      - Word Character (a-z, A-Z, 0-9, _)
\\W      - Not a Word Character
\\s      - Whitespace (space, tab, newline)
\\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""\	
