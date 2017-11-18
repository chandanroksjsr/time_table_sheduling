#represents the smallest group
import Value
class Group:
	def __init__(self,name="",strength=1):
		self.name=name
		self.strength=strength
	def display(self):
		print("name = ",self.name,\
			"\nstrength = ",self.strength,\
			"\n")
	def read():
		f=open(Value.groups_filename,"r")
		inp=f.read()
		#print(type(inp))
		l=inp.split("\n")
		#print(len(l))
		del(l[0])	#ignore first line
		del(l[len(l)-1])	#ignore last line
		#print(len(l))
		return l
#g1=Group("COE4",27)
#g1.display()