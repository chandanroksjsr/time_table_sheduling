#represents the smallest group
class Group:
	def __init__(self,name="",strength=1):
		self.name=name
		self.strength=strength
	def display(self):
		print("name = ",self.name,\
			"\nstrength = ",self.strength,\
			"\n")

#g1=Group("COE4",27)
#g1.display()