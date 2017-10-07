#represents a class(L/T/P)
class CourseClass:
	def __init__(self,subject="XYZ",groups=[],teacher="XYZ",room="XYZ",duration=1,lab=False):
		self.subject=subject
		self.groups=groups
		self.teacher=teacher
		self.room=room
		self.duration=duration
		self.lab=lab
	def display(self):
		print("subject = ",self.subject,\
			"\ngroups = ",self.groups,\
			"\nteacher = ",self.teacher,\
			"\nroom = ",self.room,\
			"\nduration = ",self.duration,\
			"\nlab = ",self.lab,\
			"\n")

#c1=CourseClass("UCS406 L",[1,2,3],"RKS","F102","1",False)
#c1.display()