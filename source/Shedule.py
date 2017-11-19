import random
from copy import deepcopy
from Value import *
from Group import *
from Subject import *
from CourseClass import *

_subject=[]
_group=[]
_class=[]
_max_fitness=-1
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

'''def displayTT(t,g):	#tt for a gievn group
	for i in range(len(t.table)):
		print(t.table[i][g-1])'''

class TimeTable:

	def __init__(self):
		self.best_chromo=[]
		self.unfit_chromo=deepcopy(_class)
		self.table= [[[] for x in range(Value.no_of_groups)] for y in range(Value.working_days*Value.working_hours)]
		self.position=[-1 for i in range(len(_class))]

	def allot_classes(self):
		for i in range(len(_class)):
			pos=random.randint(0,len(self.table)-1)	#(a,b) : a,b inclusive
			for g in _class[i].group:
				self.table[pos][int(g)-1].append(i)
		
population=[]

def initialise():	#read input data in program
	global _subject
	global _group
	global _class
	global _max_fitness
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
	_max_fitness=len(_class)

def init_pop():
	for i in range(Value.max_pop):
		population.append(TimeTable())
		population[i].allot_classes()

def crossover(parent1,parent2):
	k=1

def mutate(child):
	k=1

def isBadGene(l,k):
	for i in l:
		if i==k:
			return True
	return False

def fitness(parent):
	sum=0
	bad_genes=[]
	for i in range(len(parent.table)):
		for j in range(len(parent.table[0])):
			if(len(parent.table[i][j])>1):
				for k in parent.table[i][j]:
					if not isBadGene(bad_genes,k):
						bad_genes.append(k)
						sum=sum+1
	return _max_fitness-sum

def algorithm():
	init_pop()

initialise()
algorithm()
print(_max_fitness)
for i in population:
	print(fitness(i))

#displayTT(population[0])