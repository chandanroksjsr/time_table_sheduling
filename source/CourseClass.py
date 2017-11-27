#represents a class(L/T/P)
import Value
class CourseClass:
	def __init__(self,subject="XYZ",group=[],time=-1,teacher="XYZ",room="XYZ",duration=1,lab=False):
		self.subject=subject
		self.group=group
		self.time=time
		self.teacher=teacher
		self.room=room
		self.duration=duration
		self.lab=lab
	def display(self):
		print("subject = ",self.subject,\
			"\ngroup = ",self.group,\
			"\nteacher = ",self.teacher,\
			"\nroom = ",self.room,\
			"\nduration = ",self.duration,\
			"\nlab = ",self.lab,\
			"\n")
	def read():
		f=open(Value.classes_filename,"r")
		inp=f.read()
		#print(type(inp))
		l=inp.split("\n")
		#print(len(l))
		del(l[0])	#ignore first line
		del(l[len(l)-1])	#ignore last line
		#print(len(l))
		for i in range(len(l)):
			l[i]=l[i].split(",")
			l[i][1]=l[i][1].split("=")
			for j in range(len(l[i][1])):
				l[i][1][j]=l[i][1][j].split(":")
		# print("read done")
		return l

# c1=CourseClass("UCS406 L",[1,2,3],"RKS","F102","1",False)
# c1.display()
# c1.read()