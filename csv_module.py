import csv


#IMPORTING CSV FILE AND READING LINE BY LINE 
with open("student.csv",'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	#next(csv_reader)  skiiping the header or columns names which is the first line
	for line in csv_reader:
		print(line)
		break
#WRITING NEW CSV FILE AND USING UNIQUE DELIMITER BETWEEN COLUMNS
	with open("new_student.csv",'w') as new_file:
		csv_writer = csv.writer(new_file,delimiter='\t') 
		for line in csv_reader:
			csv_writer.writerow(line)



#READING THE CSV FILE USING DICTIONARY READER (DictReader)
with open("student.csv",'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for line in csv_reader:
		#print(line['Attendance'])
		pass


#WRITING INTO CSV FILE USING DICTWRITER 
	with open("new_student.csv",'r') as new_file:
		fieldnames=['Hours_Studied', 'Attendance', 'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours', 'Previous_Scores', 'Motivation_Level', 'Internet_Access', 'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home', 'Gender', 'Exam_Score']
		csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="\t")
		#csv_writer.writeheader()
		for line in csv_reader:
			csv_writer.writerow(line)



#DELETING A PARTICULAR FIELD
	with open("new_student.csv",'r') as new_file:
		fieldnames=['Hours_Studied', 'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours', 'Previous_Scores', 'Motivation_Level', 'Internet_Access', 'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home', 'Exam_Score']
		csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="\t")
		#csv_writer.writeheader()
		for line in csv_reader:
			del line['Attendance']
			del line['Gender']
			csv_writer.writerow(line)

