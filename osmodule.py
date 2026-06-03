import os
from datetime import datetime
#PRINTING CURRENT DIRECTORY 
print(os.getcwd())

#CHANGING DIRECTORY 
os.chdir("/home/abhinav/Downloads")
print(os.getcwd())

#LISTING THE CONTENTS OF THE DIRECTORY
ls = os.listdir()

#MAKING A FOLDER
os.mkdir("game")
os.makedirs("mygame/thisismygame")

#DELETING A FOLDER
os.rmdir("game")
os.removedirs("mygame/thisismygame")

#RENAMING THE FILE 
os.rename("test.py","odd.py")
os.rename("odd.py","test.py")

#STATS OF THE FILE 
print(os.stat("test.py"))
modtime = os.stat("test.py").st_mtime
print(datetime.fromtimestamp(modtime))

#TRAVERSING THE DIRECTORY TREEE
for dirpaths,dirnames,filenames in os.walk(os.getcwd()):
	pass
	#print("dirpath : ",dirpaths)
	#print("dirnames : ",dirnames)
	#print(f"files : {filenames} \n\n")

#ENVIRONMENT VARIABLES
print(os.environ.get('USER'))

#JOINING PATHS 
filepath = os.path.join("/home/abhinav",'test.txt')
basename = os.path.basename(filepath) #gives only test.txt
dirname  = os.path.dirname(filepath)
both     = os.path.split(filepath)
exists   = os.path.exists(basename) #whether the file present or not 
isdir    = os.path.isdir(filepath)
serparatetype =os.path.splitext(filepath)
print(serparatetype)