import random
from copy import deepcopy
from Value import *
from Group import *
from Subject import *
from CourseClass import *

_subject=[]
_group=[]
_class=[]

def getDuration(s):
	for i in range(len(_subject)):
		if _subject[i][0]==s:
			return _subject[i][2]
	return -1

def getSlots(s):
	for i in range(len(_subject)):
		if _subject[i][0]==s:
			return _subject[i][1]
	return -1

def displayTT(t):	#complete tt
	for i in range(len(t.table)):
		print(t.table[i])
def displayTT(t,g):	#tt for a gievn group
	for i in range(len(t.table)):
		print(t.table[i][g-1])

class TimeTable:
	def __init__(self):
		self.best_chromo=[]
		self.unfit_chromo=deepcopy(_class)
		self.table= [[[] for x in range(Value.no_of_groups)] for y in range(Value.working_days*Value.working_hours)]
		self.position=[-1 for i in range(len(_class))]
	def allot_classes(self):
		#print(len(self.table))
		for i in range(len(_class)):
			pos=random.randint(0,len(self.table)-1)	#(a,b) : a,b inclusive
			for g in _class[i].group:
				self.table[pos][int(g)-1].append(i)
		


class Shedule:
	population=[]
	def initialise():
		global _subject
		global _group
		global _class
		_subject=Subject.read()
		_group=Group.read()
		temp=CourseClass.read()
		for i in range(len(temp)):	#raw class data from .csv file
			rc=temp[i]	#raw class
			d=getDuration(rc[0])
			for j in range(len(rc[1])):	#for each major(lecture) group
				cc=CourseClass(subject=rc[0],group=rc[1][j],duration=d)
				for k in range(getSlots(rc[0])):	#for each slot
					_class.append(cc)

	def init_pop():
		for i in range(Value.max_pop):
			Shedule.population.append(TimeTable())
			Shedule.population[i].allot_classes()
	def algorithm():
		k=1

Shedule.initialise()
Shedule.init_pop()
Shedule.algorithm()
displayTT(Shedule.population[0],1)
print("---------------")
displayTT(Shedule.population[15],1)