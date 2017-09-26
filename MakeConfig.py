# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:23:11 2017

@author: Ekam
"""

def configTeachers(csvFile,newFile):
    tfile = open(csvFile,"r")
    nfile = open(newFile,"a")
    i=1
   
    for line in tfile.readlines():
        s=line.split(",")
        if s[0] == "":
            continue
        l=[]
        l.append("#prof\n")
        l.append("\tid = "+ (str)(i))
        l.append("\n\tname = "+s[0])
        l.append("\n#end\n\n")
        nfile.writelines(l)
        i+=1


def configRoom(csvFile,newFile):
    tfile = open(csvFile,"r")
    nfile = open(newFile,"a")
    for line in tfile.readlines():
        s=line.split(",")
        if s[0] == "":
            continue
        l=[]
        l.append("#room")
        l.append("\n\tname = "+s[0])
        print (s[2])
        
        if s[2] == "rl\n":
            l.append("\n\tlab = true")
            l.append("\n\tsize = 30")
        else :
            l.append("\n\tlab = false")
            l.append("\n\tsize = 100")
        l.append("\n#end\n\n")
        nfile.writelines(l)

def configGroups(newFile):
#    tfile = open(csvFile,"r")
    nfile = open(newFile,"a")
    j = 1
    l=[]
    for i in range(1,13):
        l.append("#group")
        l.append("\n\tid = "+ (str)(j))
        l.append("\n\tname = COE"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1
    for i in range(1,5):
        l.append("#group")
        l.append("\n\tid = "+ (str)(i))
        l.append("\n\tname = CML"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1
    for i in range(1,4):
        l.append("#group")
        l.append("\n\tid = "+ (str)(i))
        l.append("\n\tname = CAG"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1 
    for i in range(1,4):
        l.append("#group")
        l.append("\n\tid = "+ (str)(i))
        l.append("\n\tname = SEM"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1
    for i in range(1,10):
        l.append("#group")
        l.append("\n\tid = "+ (str)(i))
        l.append("\n\tname = ECE"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1
    for i in range(1,4):
        l.append("#group")
        l.append("\n\tid = "+ (str)(i))
        l.append("\n\tname = ENC"+ (str)(i))
        l.append("\n\tsize = 25")
        l.append("\n#end\n\n")
        j+=1

    nfile.writelines(l)
     
    
configTeachers("C:\\\\Users\\Ekam\\Desktop\\GA\\Raw Data\\teachers.csv"\
               ,"C:\\\\Users\\Ekam\\Desktop\\GA\\Raw Data\\teach.txt")
configRoom("C:\\Users\\Ekam\\Desktop\\GA\\Raw Data\\rooms.csv"\
               ,"C:\\\\Users\\Ekam\\Desktop\\GA\\Raw Data\\room.txt")
configGroups("C:\\Users\\Ekam\\Desktop\\GA\\Raw Data\\group.txt")

        