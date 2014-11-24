import time
from model.buffs import *
import datetime
import json
import tkinter as tk
import random
import pdb
import atexit
import config




def distance(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def squareCollide(a, b):
	return not (b.pos[0] + b.size[0] < a.pos[0] or #B trop a gauche
	   			b.pos[0] > a.pos[0] + a.size[0] or #B trop a droite
	   			b.pos[1] + b.size[1] < a.pos[1] or #B trop a dessus
	   			b.pos[1] > a.pos[1] + a.size[1])   #B trop en dessus

def normalizeSpeed(dir, maxSpeed):
	return (dir[0]/distance((0,  0), dir) * maxSpeed, dir[1]/distance((0,  0), dir) * maxSpeed)

def getDir(start, stop):
	return (stop[0]-start[0], stop[1]-start[1])

def randomElem(l):
	elem = None
	if(isinstance(l, dict)):
		elem = l[list(l.keys())[random.randint(0, len(list(l.keys()))-1)]]
	elif(isinstance(l, list)):
		elem = l[random.randint(0, len(l)-1)]
	return elem

def randomCoord(maxX, maxY, minX=0, minY=0):
	return (random.randint(minX, maxX), random.randint(minY, maxY))


programStartedToken = "#########################################################\n"+\
					  "                         started\n" + \
                      "#########################################################\n"


class GameLog(object):
	#design pattern singleton
    class __GameLog(object):
        def __init__(self, logTo):
            self.__log = []
            self.logTo = logTo

        def log(self, toLog):
        	self.__log.append([str(datetime.datetime.now()), toLog])

        def dump(self):
        	for entry in self.__log:
        		self.logTo.write(entry[0]+":\n"+indentRepr(entry[1]))
        	self.log = []

    logs = None
    def __init__(self, logList):
        if (not GameLog.logs):
            GameLog.logs = {}
            for log in logList:
            	GameLog.logs[log[0]] = GameLog.__GameLog(open(config.currentDir+"/"+log[1], 'w'))
            for log in GameLog.logs.keys():
            	GameLog.logs[log].log(programStartedToken)

    def clean(self):
    	for log in GameLog.logs.keys():
    		GameLog.logs[log].logTo.close()

    def log(self, logTo, toLog):
    	GameLog.logs[logTo].log(toLog)

    def dumpAll(self):
    	for log in GameLog.logs.keys():
    		GameLog.logs[log].dump()

    def dump(self, toDump):
    	GameLog.logs[toDump].dump()
        

class GameIds(object):
	#design pattern singleton
    class __GameIds(object):
        def __init__(self):
            self.nbId = 0

        def getNewId(self):
        	res = self.nbId
        	self.nbId += 1
        	return res

    instance = None
    def __init__(self):
        if (not GameIds.instance):
            GameIds.instance = GameIds.__GameIds()

    def __getattr__(self, name):
        return getattr(self.instance, name)


gameIdDispatcher = GameIds()
gameLogger = GameLog([["debug", "logs/debug.log"],
					 ["general", "logs/gen.log"],
					 ["errors", "logs/err.log"]])
atexit.register(gameLogger.clean)
atexit.register(gameLogger.dumpAll)


def indentRepr(rep):
	res = ""
	temp = rep.split("\n")
	for line in temp:
		res += "    " + line + "\n"
	return res


class GameObject(object):
	def __init__(self, pos, ressId = -1, speed = (0, 0), size = (1, 1)):
		super(object, self).__init__()
		self.pos = pos
		self.speed = speed
		self.exists = True
		self.size = size
		self.ressId = ressId
		self.lifePoints = 0
		self.maxLifePoints = 0
		self.id = gameIdDispatcher.getNewId()
		self.buffs = []

	def hit(self, qty):
		pass

	def addBuff(self, buff):
		self.buffs.append(buff)
		buff.apply(self)

	def __str__(self):
		res = "GameObject "+str(self.id)+" : \n" + \
			  "    Position " + "(" + str(self.pos[0]) + ", " + str(self.pos[1]) + ")\n" + \
			  "    Vitesse " + "(" + str(self.speed[0]) + ", " + str(self.speed[1]) + ")\n" + \
			  "    Existe " + ("True\n" if(self.exists) else "False\n") + \
			  "    Taille " +  "(" + str(self.size[0]) + ", " + str(self.size[1]) + ")\n" + \
			  "    RessId " + str(self.ressId) + "\n" + \
			  "    Points de vie " + str(self.lifePoints) + "/" +str(self.maxLifePoints) + "\n"
		return res

	def refreshBuffs(self):
		i = 0
		while(i < len(self.buffs)):
			if(not self.buffs[i].isDone):
				self.buffs[i].apply(self)
				i += 1
			else:
				self.buffs[i].remove(self)
				del self.buffs[i]
