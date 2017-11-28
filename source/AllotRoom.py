# from Shedule import *
import Room
from AllotTeacher import *

_roomList = Room.readRoom()		#List of all rooms
_labList = Room.readLab()		#List of all Labs
_roomD = Room.initRoom() 		#Dictionay of rooms nd there time slots 
_labD = Room.initLab()			#Dict of labs nd There time Slots


def isClass(clss):
	if clss is not None:
		return True
	return False

def getRoom():
	room = _roomList.pop(0)
	_roomList.append(room)
	return room

def getLab():
	lab = _labList.pop(0)
	_labList.append(lab)
	return lab

# def roomAval(room,i):
# 	return _room[room][i]==0


def allotRoom(t):
	global _roomList
	global _roomD
	global _labList
	global _labD

	table = t.table
	# try:
	for grp in range(Value.no_of_groups):
		room = getRoom()
		lab = getLab()
		for i in range(len(table)):
			# print(i,"    ",grp)
			if len(table[i][grp])>0:
				clss = table[i][grp][0][1]
				if isClass(clss) and not clss.rset :
					if clss.subject[len(clss.subject)-1]=='P':
						clss.lab = True
					grps = clss.group
					sub = clss.subject
					dur = clss.duration
					cur = room
					if not clss.lab :
						if _roomD[room][i]==1:
							for x in _roomD:
								if _roomD[x][i] ==0:
									cur = x
									break
						else:
							cur = room
						_roomD[cur][i]= 1

					if clss.lab :
						if _labD[lab][i] == 1:
							for x in _labD:
								if _labD[x][i] ==0:
									cur = x
									break		
						else:
							cur = lab
						_labD[cur][i] = 1

					for d in range(dur):
						for g in range(len(grps)):
							if (grp+g) <Value.no_of_groups and (i+d)<len(table):
								if len(table[i+d][grp+g])>0:
									# print("\t",rep+d,"   ",grp+g)
									table[i+d][grp+g][0][1].room = cur
									table[i+d][grp+g][0][1].rset  = True
									# table[rep+d][grp+g][0][1].frm  = grp+1

	return t

	# except :
	# 	print()
	# 	displayTT(t,0)
print("  Starting ...\n")
table = algorithm()
print("   Time Slots Assigned\n\n Now Assigning Teachers\n")
allotTeacher(table)
print("   Teachers Assigned Successfully\n")
print("   Now Assigning Rooms\n")
allotRoom(table)

print("     Rooms Alloted\n\n \t\t Time Table Formation Completed\n")

# displayTTComp(table )

writeToCSV(table,"finalx.csv")
print("    Write Successful, Check CSV file for Time Table\n")