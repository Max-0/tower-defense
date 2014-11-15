from time import *
import json


def distance(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def squareCollide(a, b):
	return not (b.pos[0] + b.size[0] < a.pos[0] or
	   			b.pos[0 > a.pos[0] + a.size[0]] or
	   			b.pos[1] + b.size[1] < a.pos[1] or
	   			b.pos[1] > a.pos[1] + a.size[1])

def normalizeSpeed(dir, maxSpeed):
	return (dir[0]/distance((0,  0), dir), dir[1]/distance((0,  0), dir)) * maxSpeed

def getDir(start, stop):
	return (stop[0]-start[0], stop[1]-start[1])

class GameObject(object):
	def __init__(self, pos, ressId = -1, onMap = False, speed = (0, 0), size = (1, 1)):
		super(object, self).__init__()
		self.pos = pos
		self.onMap = onMap
		self.speed = speed
		self.exists = True
		self.size = size
		self.ressId = ressId

	def hit(self, qty):
		pass