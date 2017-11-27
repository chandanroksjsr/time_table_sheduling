import random
from copy import deepcopy
from Value import *
from Group import *
from Subject import *
from CourseClass import *
from numpy.random import choice

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

#no of slots of a given class
def getSlots(s):
	for i in range(len(_subject)):
		if _subject[i][0]==s:
			return _subject[i][1]
	return -1

#checks if a class is already present in the list
def isPresent(l,k):
	for i in l:
		if i==k:
			return True
	return False

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
	print("Total Classes : "+str(len(_class)))

def displayTT(t,g):	#tt for a given group
	index=1
	for i in range(len(t.table)):
		print(str(index)+" : ",end='')
		for j in range(len(t.table[i][g-1])):
			print(t.table[i][g-1][j][1].subject,end=' ,')
		index=index+1
		print('')
	print('')

def writeToCSV(t,g,file_name):
	f = open(file_name,'w')
	f.write("MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,\n")
	for hr in range(Value.working_hours):
		for day in range(Value.working_days):
			for c in range(len(t.table[hr+Value.working_hours*day][g-1])):
				f.write(t.table[hr+Value.working_hours*day][g-1][c][1].subject+"+")
			f.write(',')
		f.write('\n')
	f.close()

class TimeTable:

	def __init__(self):
		self.fit_chromo=[]
		self.unfit_chromo=[]
		self.table= [[[] for x in range(Value.no_of_groups)] for y in range(Value.working_days*Value.working_hours)]
		self.fitness=-1
	
	#index of class in list
	def posInFit(self,static_pos):
		for i in range(len(self.fit_chromo)):
			if static_pos==self.fit_chromo[i][0]:
				return i
		return -1

	#return timing of the class
	def timeInFit(self,static_pos):
		for i in range(len(self.fit_chromo)):
			if static_pos==self.fit_chromo[i][0]:
				return self.fit_chromo[i][1].time
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
	def getUnfitMutSize(self):
		if Value.unfit_mutation_size<len(self.unfit_chromo):
			return Value.unfit_mutation_size
		return random.randint(0,len(self.unfit_chromo)+1)

	def getFitMutSize(self):
		if Value.fit_mutation_size<len(self.fit_chromo):
			return Value.fit_mutation_size
		return random.randint(0,len(self.fit_chromo)+1)

	#checks if a given time falls in regions of already fit classes
	def isFitTiming(self,c,time):
		for g in c[1].group:
			for d in range(0,c[1].duration):
				if len(self.table[time+d][int(g)-1])==1:
					return False
		return True

	#handles breaks(12:00pm ,2:00 pm) and class slot probabilities
	def getPreferableSlot(self,c):
		#limits boundary condition
		class_type=c[1].subject[len(c[1].subject)-1]
		max_time_slot=Value.working_hours-c[1].duration
		slots=range(0,Value.working_hours)
		prob=[]
		if class_type=='L':
			prob=Value.lec_slot_prob
		elif c[1].subject[len(c[1].subject)-1]=='P':
			prob=Value.prac_slot_prob
		elif c[1].subject[len(c[1].subject)-1]=='T':
			prob=Value.lec_slot_prob
		#handles lecture,tuts,practicals slots
		time=-1
		if class_type=='L':
			while time<0:
				time=int(choice(slots,1,p=prob))	#choice() does not return an integer????
				for d in range(c[1].duration):
					#class should not fall in regins of zero probabilities
					if prob[time+d]<=0 or time>max_time_slot:
						time=-1
						break
		elif class_type=='P':
			while time<0:
				time=int(choice(slots,1,p=prob))
				for d in range(c[1].duration):
					if prob[time+d]<=0 or time>max_time_slot:
						time=-1
						break		
		elif class_type=='T':
			while time<0:
				time=int(choice(slots,1,p=prob))
				for d in range(c[1].duration):
					if prob[time+d]<=0 or time>max_time_slot:
						time=-1
						break		
		return random.randint(0,Value.working_days-1)*Value.working_hours+time

	def delClass(self,static_pos):
		i=self.posInUnfit(static_pos)
		if i>=0:
			c=self.unfit_chromo[i]
			for d in range(c[1].duration):
				for g in c[1].group:
					self.table[c[1].time+d][int(g)-1].remove(c)
			del(self.unfit_chromo[i])
			return
		i=posInFit(static_pos)
		if i>=0:
			c=self.fit_chromo[i]
			for d in range(c[1].duration):
				for g in c[1].group:
					self.table[c[1].time+d][int(g)-1].remove(c)
			del(self.fit_chromo[i])
			return

	def insertClass(self,c):
		self.unfit_chromo.append(c);
		for d in range(c[1].duration):
			for g in c[1].group:
				self.table[c[1].time+d][int(g)-1].append(c)
	def calculateFitness(self):
		sum=0
		bad_genes=[]
		for i in range(len(self.table)):
			for j in range(len(self.table[0])):
				if(len(self.table[i][j])>1):
					for k in self.table[i][j]:
						if not isPresent(bad_genes,k):
							bad_genes.append(k)
							sum=sum+1
		#print(bad_genes)
		self.fitness=_max_fitness-sum
		return self.fitness

	def allotRandomClasses(self):
		i=0	#to mark index corresponding to indexing in _class
		for rc in _class:
			t_subject=rc.subject
			t_group=rc.group
			t_time=self.getPreferableSlot([i,rc])
			t_teacher="XYZ"
			t_room="XYZ"
			t_duration=rc.duration
			t_lab=False
			c=[i,CourseClass(t_subject,t_group,t_time,t_teacher,t_room,t_duration,t_lab)]
			self.insertClass(c)
			i=i+1
		self.calculateFitness()
		
#create initial population
def init_pop():
	for i in range(Value.max_pop):
		_population.append(TimeTable())
		_population[i].allotRandomClasses()

def showFitness():
	flist=[]
	for p in _population:
		flist.append(p.fitness)
	list.sort(flist,reverse=True)
	#fitness of best time-table
	print("Fitness = ",end=' ')
	print("{0:.2f}".format((flist[0]*100)/_max_fitness),end=" , ")
	#average fitness
	print("{0:.2f}".format(((sum(flist)/len(flist))*100)/_max_fitness))

#kills most unfit l individuals from current population
def killUnfit(l):
	list.sort(_population,reverse=True,key=TimeTable.calculateFitness)
	for i in range(l):
		del(_population[len(_population)-1])

#uniform crossover
def crossover(parent1,parent2):
	child=[]
	child.append(TimeTable())
	child.append(TimeTable())
	for i in range(len(_class)):
		#*check if pos1 and pos2 does not fall in regions of best chromosomes*
		pos1=parent1.posInFit(i)
		pos2=parent2.posInFit(i)
		if pos1>=0 and pos2>=0:
			if random.randint(1,2)==1:
				c1=deepcopy(parent1.fit_chromo[pos1])
				c2=deepcopy(parent2.fit_chromo[pos2])
				child[0].insertClass(c1)
				child[1].insertClass(c2)
			else:
				c1=deepcopy(parent1.fit_chromo[pos1])
				c2=deepcopy(parent2.fit_chromo[pos2])
				child[0].insertClass(c2)
				child[1].insertClass(c1)

		elif pos1>=0:
			c1=deepcopy(parent1.fit_chromo[pos1])
			c2=deepcopy(c1)
			child[0].insertClass(c1)
			child[1].insertClass(c2)
		elif pos2>=0:
			c1=deepcopy(parent2.fit_chromo[pos2])
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
def mutate(child,prob):
	if(random.random()<prob):
		#unfit classes
		mut_genes=random.sample(range(0, len(child.unfit_chromo)), child.getUnfitMutSize())
		for i in mut_genes:
			tc=child.unfit_chromo[i]
			c=deepcopy(tc)
			child.delClass(tc[0])
			#check if new time does not fall in regions of best chromosomes
			trails=0
			time=child.getPreferableSlot(c)
			while trails<Value.max_trials_for_free_slots and not child.isFitTiming(c,time):
				time=child.getPreferableSlot(c)
				trails=trails+1
			c[1].time=time
			child.insertClass(c)
		#fit classes
		'''mut_genes=random.sample(range(0, len(child.fit_chromo)), child.getFitMutSize())
		for i in mut_genes:
			tc=child.fit_chromo[i]
			c=deepcopy(tc)
			child.delClass(tc[0])
			#check if new time does not fall in regions of best chromosomes
			trails=0
			time=random.randint(0,len(child.table)-c[1].duration)
			while trails<Value.max_trials_for_free_slots and not child.isFitTiming(c,time):
				time=random.randint(0,len(child.table)-c[1].duration)
				trails=trails+1
			c[1].time=time
			child.insertClass(c)'''
		return True
	return False

def reproduce(parent1,parent2):
	child=crossover(parent1,parent2)
	child[0].calculateFitness()
	child[1].calculateFitness()
	#mutation in offsprings
	if mutate(child[0],Value.offspring_mutation_prob):
		child[0].calculateFitness()
	if mutate(child[1],Value.offspring_mutation_prob):	
		child[1].calculateFitness()
	return child
	

def algorithm():
	init_pop()
	writeToCSV(_population[0],4,"initial.csv")
	displayTT(_population[0],4)
	showFitness()
	i=0
	while i<1000 and _population[0].fitness<_max_fitness:
		#mutation in current population
		m=random.randint(0,len(_population)-1)
		if mutate(_population[m],Value.population_mutation_prob):
			_population[m].calculateFitness()

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
		i=i+1
	writeToCSV(_population[0],4,"final.csv")
	displayTT(_population[0],4)
	showFitness()	
	print("Iterations required = "+str(i))

initialise()
algorithm()