from datetime import datetime
first_name = "Abhinav    "
last_name = "Prakash"

#USING FORMAT() METHOD
sentence = 'My name is {} {}'.format(first_name,last_name)
print(sentence)


#USING F STRINGS 
sentence = f'My name is {first_name.strip()} {last_name.upper()}'
print(sentence)

#PRINING ELEMENTS OF THE DICTIONARY
person = {'name':'Abhinav','section':'G'}
sentence = 'My name is {} and my section is {}'.format(person['name'],person['section'])
print(sentence)

#PRINTING ELEMENTS OF THE DICTIONARY USING F STRINGS
sentence = f"My name is {person['name']} and my section is {person['section']}"#double quotes is required else it will give error 
print(sentence)

#DOING CALCULATION USING F STRINGS 
calculation = f'4 times 11 is equal to {4*11}'
print(calculation)

#PADDING VALUES 
for i in range(1,11):
	sentence = f'the value is {i:02}'
	print(sentence)

#FLOATING POINT NUMBERS 
pi = 3.142345678
sentence = f'the value of pi is {pi:.4f}'#upto 4 decimal point will be printed
sentence = f'the value of pi is {pi:.04}'#4 digits including total will be printed
print(sentence)

#PRINTING DATES IN STYLE FORMAT MORE CODES CAN BE FOUND ON WEB
birthday = datetime(2005,8,1)
sentence = f'Mahima has a birthday on {birthday:%B %d , %Y}'
print(sentence)