'''from Subject import *
f=open("../data/subjects.csv","r")
inp=f.read()
print(type(inp))
l=inp.split("\n")
print(type(l))
print(len(l))
print(len(l[34]))
s1=Subject("UCS606 L",3,1)
s1.display()'''
'''i=0
for s in inp:
	i=i+1
	if i == 20:
		break
	print(s,"\n")'''
def display(l):
	for i in range(len(l)):
		print(l[i])
from CourseClass import *
subjects=CourseClass.read()
print(len(subjects))
#print(len(subjects[0]))
print(type(subjects))
print(type(subjects[1]))
display(subjects[:6])