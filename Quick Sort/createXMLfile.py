# First Run This File and Then it will Auto matically call Other quicksort.py file
#Keep Both files in same folder
import os
import random
import sys
name = input("Enter the name of file: ")+".xml"
file = open(name,'w')
file.write("<Numbers>\n")
for i in range(10):
	file.write("\t<integer num = \""+str(random.randint(0,800))+"\" ></integer>\n")
file.write("</Numbers>\n")
file.close()
temp =input(name+" file is written & press 1 to see its contents:")
if(temp==1):
	os.system("cat "+name)
	tmp=input("\npress 2 to start quickstart program: ")
	if(tmp==2):
		os.system("python quickSort.py "+name)
