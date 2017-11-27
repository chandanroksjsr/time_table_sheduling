#represents courses taught
import Value
class Subject:
	def __init__(self,name="",slots=1,duration=1):
		self.name=name
		self.slots=slots
		self.duration=duration
	def display(self):
		print("name = ",self.name,\
			"\nslots = ",self.slots,\
			"\nduration = ",self.duration,\
			"\n")
	def read():
		f=open(Value.subjects_filename,"r")
		inp=f.read()
		#print(type(inp))
		l=inp.split("\n")
		#print(len(l))
		del(l[0])	#ignore first line
		del(l[len(l)-1])	#ignore last line
		#print(len(l))
		for i in range(len(l)):
			l[i]=l[i].split(",")
			l[i][1]=int(l[i][1]);
			l[i][2]=int(l[i][2]);
		return l

#s1=Subject("UCS606 L",3,1)
#s1.display()