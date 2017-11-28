from Shedule import *

_subTeach = {}
_teachers = {}
# displayTTComp(table)

def initSlot():
	global _subTeach
	global _teachers
	_subTeach = Teachers.read()
	# _subTeach = Teachers.read()
	# temp =
	for i in _subTeach:
		# for lis in _subTeach[i]:
			for j in _subTeach[i]:
				_teachers[j] = [0 for y in range(Value.working_days*Value.working_hours)]
	
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

def isAlloted(alt,grp,sub):

	for i in alt[grp]:
		if i == sub:
			return True
	return False

def isClass(clss):
	if clss is not None:
		return True
	return False
# def isNotSet(clss):
# 	if clss.set

def getTeacher(sub):
	tchrs = _subTeach[sub]
	tchr = tchrs.pop(0)
	tchrs.append(tchr)
	_subTeach[sub] = tchrs
	return tchr
def printSub():
	global _subTeach
	print("HERE")
	for i in _subTeach:
		print(i,end= '  ')
		print(_subTeach[i])

def dispTeachers():
	global _teachers
	# _teachers = CourseClass.read()
	# print(_teachers["SHM"])
	for i in _teachers:
		print(str(i) +"  ",end="  ")
		print( _teachers[i],end="\n\n" )

def allot(table):
	global _teachers
	global _subTeach
	initSlot()
	# print("SUBSS:  ")
	# printSub()
	# print("TEACHERSS\n\n")
	# dispTeachers()
	try:
		for grp in range(Value.no_of_groups):
			for i in range(len(table)):
				print(i,"    ",grp)
				if len(table[i][grp])>0:
					clss = table[i][grp][0][1]
					if isClass(clss) and not clss.set :
						grps = clss.group
						sub = clss.subject
						tchr = getTeacher(sub)
						# print(sub,"\tTeachers is : ",tchr)
						dur = clss.duration
						for rep in range(i,len(table)):
							if len(table[rep][grp])>0:# and isClass(table[rep][grp][0][1]) :
								if table[rep][grp][0][1].subject == sub:
									for d in range(dur):
										for g in range(len(grps)):
											if (grp+g) <Value.no_of_groups and (rep+d)<len(table):
												if len(table[rep+d][grp+g])>0:
													# print("\t",rep+d,"   ",grp+g)
													table[rep+d][grp+g][0][1].teacher = tchr
													table[rep+d][grp+g][0][1].set  = True
													table[rep+d][grp+g][0][1].frm  = grp+1

	except :
		displayTT(tableT,1)

tableT  = algorithm()
allot(tableT.table)
# printSub()
displayTT(tableT,5)


