import json #javascript object notation

people_string = '''
{
"people": [
             {
             "name" : "sanny",
             "phone": "34352",
             "emails": "abiha#gmail.com",
             "lica" : true
             },
             {
             "name" : "abhinav",
             "phone" : 4343,
             "emails":  null,
             "lica" : "yes"
             }

          ]
}
             '''
#LOADING A STRING AS JSON

data = json.loads(people_string)
print(type(data))
print(data)
print("\n\n")
print(data['people'][0]['name'])
print("\n\n")

#ITERATING THROUGH DICTIONARIES

for person in data['people']:
	del person['phone'] #DELETING A FIELD IN DICTIONARIES
new_string = json.dumps(data)
print(new_string)
print("\n\n")
new_string = json.dumps(data, indent = 2) #pretty print with exponential indentation
print(new_string)
print("\n\n")
new_string = json.dumps(data, indent = 2 , sort_keys=True) #sorting the keys 
print(new_string)

#IMPORTING A JSON FILE 

with open("countries.json",'r') as f:
	data = json.load(f)
	country = input("Enter the name of the country : ")
	for list in data['countries']:
		if(list['name']==country):
			print(list)
#WRITING INTO A FILE 
with open("writing.json",'w') as f:

	json.dump(data['countries'], f , indent = 2) #WRITING IN JSON FORMAT
	
#WRITING ONLY THE COUNTRIES IN STRING FORMAT USING WRITE()
	for list in data['countries']:
		f.write(list['name'])
		f.write('\n')
 
 #REAL WORLD EXAMPLE

import json
from urllib.request import urlopen 

with urlopen("https://jsonplaceholder.typicode.com/todos/1") as response:
	source = response.read()

new_string = json.loads(source)
print(json.dumps(new_string , indent = 2 ))