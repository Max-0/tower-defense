import time
import json
import tkinter as tk
import random


def distance(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def squareCollide(a, b):
	print("a")
	print(a.pos)
	print("b")
	print(b.pos)
	return not (b.pos[0] + b.size[0] < a.pos[0] or
	   			b.pos[0 > a.pos[0] + a.size[0]] or
	   			b.pos[1] + b.size[1] < a.pos[1] or
	   			b.pos[1] > a.pos[1] + a.size[1])

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


class GameObject(object):
	def __init__(self, pos, ressId = -1, onMap = False, speed = (0, 0), size = (1, 1)):
		super(object, self).__init__()
		self.pos = pos
		self.onMap = onMap
		self.speed = speed
		self.exists = True
		self.size = size
		self.ressId = ressId
		self.lifePoints = 0

	def hit(self, qty):
		pass