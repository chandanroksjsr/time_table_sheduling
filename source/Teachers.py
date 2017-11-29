#represents courses taught
import Value
from CourseClass import *

# _subTeach = {}
# _teachers = {}


class Teachers:
	def __init__(self,sub="",tcodes=[]):
		self.sub=sub
		self.tcodes=tcodes

	def display(self):
		print("name = ",self.sub,\
			"\nTcode = ",self.tcodes,\
			"\n")

	def read():
		_subTeach= {}
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
			# print(l[i])
			_subTeach[l[i][0]] =l[i][1] 
		return _subTeach

	def initSlot():
		# global _subTeach
		# global _teachers
		_subTeach = Teachers.read()
		# _subTeach = Teachers.read()
		# temp =
		_teachers={}
		for i in _subTeach:
			# for lis in _subTeach[i]:
				for j in _subTeach[i]:
					_teachers[j] = [0 for y in range(Value.working_days*Value.working_hours)]
		return _teachers

	def resetSlot():
		global _teachers
		for i in _teachers:
			_teachers[i] = [0 for y in range(Value.working_days*Value.working_hours)]

	def dispTeachers():
		global _teachers
		# _teachers = CourseClass.read()
		# print(_teachers["SHM"])
		for i in _teachers:
			print(str(i) +"  ",end="  ")
			print( _teachers[i],end="\n\n" )

#	def isAlloted(alt,grp,sub):
#
#		for i in alt[grp]:
#			if i == sub:
#				return True
#		return False

# 	def allotTeacher(table):				##  TimeTable from GA
# 		global _teachers
# 		global _subTeach
# 		Teachers.initSlot()
# 		alt = {} #{0:{"ABC":"XYZ"}}						#Dictionary of teacher alloted to a subject for\
# 											# each grp. Struct=> alt[grp][sub] = teacher OR   {grp:{sub:teacher}}
# 		# alt[20]={}
# 		# alt[20]["CDE"]="MNO"
# 		# alt[12]={}
# 		# alt[12]["CCCCDE"]="MMMMNO"

# 		for z in range(1,len(table[0])+1):
# 			alt[z]={}

# 		# print("testt")
# 		# for z in alt:
# 		# 	print(z)
# 		for grp in range(len(table[0])):
# 			# print("GRP :",int(grp),"  GP ",grp)
# 			# alt[int(grp)+1] ={}
# 			gref = int(grp)+1
# 			for i in range(int(len(table))):
# # 				for j in range(len(table[i][grp])):
# # 					# sub = _subTeach[table[i][grp][j][1].subject]
# # 					sub = table[i][grp][j][1].subject
# # 					groups = table[i][grp][j][1].group
# # 					# print(groups)
# # 					if sub in alt[int(grp)+1]:
# # 						# print("Test",end = '  ')
# # 						tchr = alt[int(grp)+1][sub]
# # 						# print(g, "  ",sub, "  ",tchr,"\n\n")
# # #						table[i][grp][j][1].teacher = tchr
# # 						# for g in groups:
# # 						# 	table[i][g][j][1].teacher = tchr
# # 						# 	alt[g][sub]=tchr
# # 						# _teachers[tchr][i]=1
# # 					else :
# # 						tchrs = _subTeach[sub]
# # 						tchr = tchrs.pop(0)
# # 						tchrs.append(tchr)
# # 						_subTeach[sub] = tchrs
# # 						# _subTeach[sub].append(tchr)

# # 					for g in groups:
# # 						# tempp = [char(' ') for z in range(g)]
# # 						# print("Chota G  ",sub,"   ",g)
# # 						table[i][int(g)-1][j][1].teacher = tchr
# # 						table[i][int(g)-1][j][1].frm = int(g)
# # 						if alt.get(g) is None:
# # 							alt[int(g)]={}
# # 						alt[int(g)][sub]=tchr
# # 					_teachers[tchr][i]=1
# 				for clss in table[i][grp]:
# 					if clss[1].set:
# 						continue
# 					# sub = _subTeach[table[i][grp][j][1].subject]
# 					sub = clss[1].subject
# 					groups = clss[1].group
# 					# print(groups)
# 					if sub in alt[gref]:
# 						# print("Test",end = '  ')
# 						tchr = alt[gref][sub]
# 						# print(g, "  ",sub, "  ",tchr,"\n\n")
# #						table[i][grp][j][1].teacher = tchr
# 						# for g in groups:
# 						# 	table[i][g][j][1].teacher = tchr
# 						# 	alt[g][sub]=tchr
# 						# _teachers[tchr][i]=1
# 					else :
# 						tchrs = _subTeach[sub]
# 						tchr = tchrs.pop(0)
# 						tchrs.append(tchr)
# 						_subTeach[sub] = tchrs
# 						# _subTeach[sub].append(tchr)

# 					for g in groups:
# 						# tempp = [char(' ') for z in range(g)]
# 						# print("Chota G  ",sub,"   ",g)
# 						if int(g)>=gref:
# 							table[i][int(g)-1][0][1].teacher = tchr
# 							table[i][int(g)-1][0][1].frm = int(g)
# 							table[i][int(g)-1][0][1].set = True
# 							if alt.get(g) is None:
# 								alt[int(g)]={}
# 							alt[int(g)][sub]=tchr
# 						_teachers[tchr][i]=1
# 		Teachers.dispALT(alt)
# 		# Teachers.dispTeachers()
# 		# print("\n\n")
# 		# return table
# 	def printSub():
# 		global _subTeach
# 		print("HERE")
# 		for i in _subTeach:
# 			print(i,end= '  ')
# 			print(_subTeach[i])

# 	def dispALT(alt):
# 		print("ALT")
# 		for g in alt:
# 			for i in alt[g]:
# 				print(g,i,alt[g][i])
# 		print("\nALT END\n\n\n")
# # Teachers.initSlot()
# # Teachers.printSub()
# # # print("\n\n\n")
# # Teachers.dispTeachers()
# # Teachers.resetSlot()
# # Teachers.dispTeachers()

# # dict ={1:10,3:30,4:40}
# # for i in range(1,5):
# # 	if dict[i]:
# # 		print (dict[i])
# # read()
