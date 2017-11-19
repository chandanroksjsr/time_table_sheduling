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
_max_pop=Value.max_pop
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
	#print(bad_genes)
	return _max_fitness-sum

def showFitness():
	flist=[]
	for i in population:
		flist.append(fitness(i))
	print(flist)
	print(sum(flist)/len(flist))

def killUnfit(l):
	list.sort(population,reverse=True,key=fitness)
	for i in range(l):
		del(population[len(population)-1])

def crossover(parent1,parent2):
	child=[]
	child.append(TimeTable())
	child.append(TimeTable())
	#for i in range(len(_class))
	return child

def mutate(child):
	if(random.random()<Value.mutation_prob):
		pass

def reproduce(parent1,parent2):
	child=crossover(parent1,parent2)
	mutate(child[0])
	mutate(child[1])
	return child
	

def algorithm():
	init_pop()
	for i in range(10):
		showFitness()
		#kill unfit
		killUnfit(_max_pop//2)
		#populate
		while len(population)<_max_pop:
			#selection
			p1=random.randint(0,len(population)-1)
			p2=p1
			while p2==p1:
				p2=random.randint(0,len(population)-1)
			#reproduction
			child=reproduce(population[p1],population[p2])
			#add to population
			population.append(child[0])
			population.append(child[1])

initialise()
algorithm()


#displayTT(population[0])