#represents courses taught
import Value
import CourseClass

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
		_teachers = CourseClass.read()
		# print(_teachers["SHM"])
		for i in _teachers:
			print(str(i) +"  ",end=" ")
			print( _teachers[i],end="\n\n" )

	def isAlloted(alt,grp,sub):

		for i in alt[grp]:
			if i == sub:
				return True
		return False

	def allotTeacher(table):				##  TimeTable from GA
		global _teachers
		global _subTeach
		initSlot()
		alt = {{}}						#Dictionary of teacher alloted to a subject for\
											# each grp. Struct=> alt[grp][sub] = teacher OR   {grp:{sub:teacher}}

		for grp in range(len(table[0])):
			for i in range(len(table)):
				for j in range(len(table[i][grp])):
					sub = _subTeach[table[i][grp][j][1].subject]
					groups = table[i][grp][j][1].group
					if isAlloted(alt,grp,sub):
						tchr = alt[grp][sub]
#						table[i][grp][j][1].teacher = tchr
						# for g in groups:
						# 	table[i][g][j][1].teacher = tchr
						# 	alt[g][sub]=tchr
						# _teachers[tchr][i]=1
					else :
						tchr = _subTeach[sub].pop(0)
						_subTeach[sub].append(tchr)

					for g in groups:
						table[i][g][j][1].teacher = tchr
						alt[g][sub]=tchr
					_teachers[tchr][i]=1
		# return table


# Teacher.initSlot()
# Teacher.dispTeachers()
# print("\n\n\n")
# Teacher.resetSlot()
# Teacher.dispTeachers()

# dict ={1:10,3:30,4:40}
# for i in range(1,5):
# 	if dict[i]:
# 		print (dict[i])
# read()
