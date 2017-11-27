#represents courses taught
import Value

_subTeach =[]
_teachers = {}


class Teacher:
	def __init__(self,sub="",tcodes=[]):
		self.sub=sub
		self.tcodes=tcodes

	def display(self):
		print("name = ",self.sub,\
			"\nTcode = ",self.tcodes,\
			"\n")

	def read(self):
		f=open(Value.teachers_filename,"r")
		inp=f.read()
		#print(type(inp))
		l=inp.split("\n")
		#print(len(l))
		del(l[0])	#ignore first line
		del(l[len(l)-1])	#ignore last line
		#print(len(l))
		for i in range(len(l)):
			l[i]=l[i].split(",")
			l[i][1]=l[i][1].split(":")
			print(l[i])

		return l

	def initSlot():
		global _subTeach
		global _teachers
		_subTeach = Teacher().read()
		# temp =
		for i in _subTeach:
			for j in i[1]:
				_teachers[j] = [0 for y in range(Value.working_days*Value.working_hours)]

	def resetSlot():
		global _teachers
		for i in _teachers:
			_teachers[i] = [0 for y in range(Value.working_days*Value.working_hours)]

	def dispTeachers():
		global _teachers

		# print(_teachers["SHM"])
		for i in _teachers:
			print(str(i) +"  ",end=" ")
			print( _teachers[i],end="\n\n" )


Teacher.initSlot()
Teacher.dispTeachers()
print("\n\n\n")
Teacher.resetSlot()
Teacher.dispTeachers()