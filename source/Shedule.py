import random
from copy import deepcopy
from Value import *
from Group import *
from Subject import *
from CourseClass import *

_population=[]
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
			s=getSlots(rc[0])
			for k in range(s):	#for each slot
				_class.append(cc)
	_max_fitness=len(_class)

def displayTT(t):	#complete tt
	for i in range(len(t.table)):
		print(t.table[i])

'''def displayTT(t,g):	#tt for a gievn group
	for i in range(len(t.table)):
		print(t.table[i][g-1])'''

class TimeTable:

	def __init__(self):
		self.best_chromo=[]
		self.unfit_chromo=[]
		self.table= [[[] for x in range(Value.no_of_groups)] for y in range(Value.working_days*Value.working_hours)]
		self.fitness=-1
	
	#index of class in list
	def posInBest(self,static_pos):
		for i in range(len(self.best_chromo)):
			if static_pos==self.best_chromo[i][0]:
				return i
		return -1

	#return timing of the class
	def timeInBest(self,static_pos):
		for i in range(len(self.best_chromo)):
			if static_pos==self.best_chromo[i][0]:
				return self.best_chromo[i][1].time
		return -1

	#index of class in list
	def posInUnfit(self,static_pos):
		for i in range(len(self.unfit_chromo)):
			if static_pos==self.unfit_chromo[i][0]:
				return i
		return -1

	#return position of the class according to best chromosomes list
	def timeInUnfit(self,static_pos):
		for i in range(len(self.unfit_chromo)):
			if static_pos==self.unfit_chromo[i][0]:
				return self.unfit_chromo[i][1].time
		return -1

	def delClass(self,static_pos):
		i=self.posInUnfit(static_pos)
		if i>=0:
			c=self.unfit_chromo[i]
			for d in range(c[1].duration):
				for g in c[1].group:
					self.table[c[1].time+d][int(g)-1].remove(c)
			del(self.unfit_chromo[i])
			return
		i=posInBest(static_pos)
		if i>=0:
			c=self.best_chromo[i]
			for d in range(c[1].duration):
				for g in c[1].group:
					self.table[c[1].time+d][int(g)-1].remove(c)
			del(self.best_chromo[i])
			return

	def insertClass(self,c):
		self.unfit_chromo.append(c);
		for d in range(c[1].duration):
			for g in c[1].group:
				self.table[c[1].time+d][int(g)-1].append(c)

	def allotRandomClasses(self):
		i=0	#to mark index corresponding to indexing in _class
		for rc in _class:
			t_subject=rc.subject
			t_group=rc.group
			t_time=random.randint(0,len(self.table)-rc.duration)
			t_teacher="XYZ"
			t_room="XYZ"
			t_duration=rc.duration
			t_lab=False
			c=[i,CourseClass(t_subject,t_group,t_time,t_teacher,t_room,t_duration,t_lab)]
			self.insertClass(c)
			i=i+1
		
#create initial population
def init_pop():
	for i in range(Value.max_pop):
		_population.append(TimeTable())
		_population[i].allotRandomClasses()

#checks if a class is already present in the list of bad genes
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
	for i in _population:
		flist.append(fitness(i))
	#print(flist)
	print(sum(flist)/len(flist))

#kills most unfit l individuals from current population
def killUnfit(l):
	list.sort(_population,reverse=True,key=fitness)
	for i in range(l):
		del(_population[len(_population)-1])

def crossover(parent1,parent2):
	child=[]
	child.append(TimeTable())
	child.append(TimeTable())
	#uniform crossover
	for i in range(len(_class)):
		#*check if pos1 and pos2 does not fall in regions of best chromosomes*
		pos1=parent1.posInBest(i)
		pos2=parent2.posInBest(i)
		if pos1>=0 and pos2>=0:
			if random.randint(1,2)==1:
				c1=deepcopy(parent1.best_chromo[pos1])
				c2=deepcopy(parent2.best_chromo[pos2])
				child[0].insertClass(c1)
				child[1].insertClass(c2)
			else:
				c1=deepcopy(parent1.best_chromo[pos1])
				c2=deepcopy(parent2.best_chromo[pos2])
				child[0].insertClass(c2)
				child[1].insertClass(c1)

		elif pos1>=0:
			c1=deepcopy(parent1.best_chromo[pos1])
			c2=deepcopy(c1)
			child[0].insertClass(c1)
			child[1].insertClass(c2)
		elif pos2>=0:
			c1=deepcopy(parent2.best_chromo[pos2])
			c2=deepcopy(c1)
			child[0].insertClass(c1)
			child[1].insertClass(c2)
		else:
			#*check if pos1 and pos2 does not fall in regions of best chromosomes*
			pos1=parent1.posInUnfit(i)
			pos2=parent2.posInUnfit(i)
			if random.randint(1,2)==1:
				c1=deepcopy(parent1.unfit_chromo[pos1])
				c2=deepcopy(parent2.unfit_chromo[pos2])
				child[0].insertClass(c1)
				child[1].insertClass(c2)
			else:
				c1=deepcopy(parent1.unfit_chromo[pos1])
				c2=deepcopy(parent2.unfit_chromo[pos2])
				child[0].insertClass(c2)
				child[1].insertClass(c1)
		
	return child

#*affects positioning of chromosomes, deletes from middle inserts at the end*
def mutate(child):
	if(random.random()<Value.mutation_prob):
		mut_genes=random.sample(range(0, len(child.unfit_chromo)), Value.mutation_size)
		for i in mut_genes:
			tc=child.unfit_chromo[i]
			c=deepcopy(tc)
			#*check if pos1 and pos2 does not fall in regions of best chromosomes*
			c[1].time=random.randint(0,len(child.table)-tc[1].duration)
			child.delClass(tc[0])
			child.insertClass(c)
		

def reproduce(parent1,parent2):
	child=crossover(parent1,parent2)
	mutate(child[0])
	mutate(child[1])
	return child
	

def algorithm():
	init_pop()
	showFitness()
	for i in range(60):
		#showFitness()
		#kill unfit
		killUnfit(_max_pop//2)
		#populate
		while len(_population)<_max_pop:
			#selection
			p1=random.randint(0,len(_population)-1)
			#p2 should be different from p1 and random as well
			p2=p1
			while p2==p1:
				p2=random.randint(0,len(_population)-1)
			#reproduction
			child=reproduce(_population[p1],_population[p2])
			#add to population
			_population.append(child[0])
			_population.append(child[1])
	showFitness()

initialise()
algorithm()


#displayTT(population[0])