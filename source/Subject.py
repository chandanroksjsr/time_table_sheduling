#represents the smallest group
class Subject:
	def __init__(self,name="",slots=1,duration=1):
		self.name=name
		self.slots=slots
		self.duration=duration
	def display(self):
		print("name = ",self.name,\
			"\nslots = ",self.slots,\
			"\nduration = ",self.duration,\
			"\n")

#s1=Subject("UCS606 L",3,1)
#s1.display()