import Value
def readRoom():
	rooms = []
	f=open(Value.rooms_filename,"r")
	inp=f.read()
	#print(type(inp))
	rooms=inp.split("\n")
	#print(len(l))
	del(rooms[0])	#ignore first line
	del(rooms[len(rooms)-1])	#ignore last line
	#print(len(l))
	# for i in range(len(l)):
	# 	l[i]=l[i].split(",")
	# 	l[i][1]=l[i][1].split(":")
	# 	# print(l[i])
	# 	_subTeach[l[i][0]] =l[i][1] 
	return rooms

def readLab():
	lab = []
	f = open(Value.labs_filename,"r")
	read = f.read()

	lab = read.split('\n')
	del(lab[0])
	del(lab[len(lab)-1])
	return lab
def initRoom():
	rooms = readRoom()
	roomList = {}
	for j in rooms:
		roomList[j] = [0 for x in range(Value.working_days*Value.working_hours)]
	return roomList

def initLab():
	labs = readLab()
	labList = {}
	for j in labs:
		labList[j] = [0 for x in range(Value.working_days*Value.working_hours)]
	return labList

def printRooms(rooms):
	for i in rooms:
		print(i,"  ",rooms[i])
	
def printLabs(labs):
	for i in labs:
		print(i,"  ",labs[i])

# print(readRoom())
# printRooms(initRoom())
# print("\n\nLABS \n\n")
# # print(readLab())
# printLabs(initLab())