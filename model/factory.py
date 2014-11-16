from model.gameObjs import *


class MissileFactory(object):
	def __init__(self, dmg, maxSpeed, missileList, ressId, size):
		super(object, self).__init__()
		self.dmg = dmg
		self.maxSpeed = maxSpeed
		self.missileList = missileList
		self.ressId = ressId
		self.size = size
		self.missileList = missileList

	def new(self, start, target):
		self.missileList.append(Missile(self.dmg, target, self.maxSpeed, start))
		self.missileList[-1].ressId = self.ressId
		self.missileList[-1].size = self.size		


class TowerFactory(object):
	def __init__(self, range, firerate, missileFactory, towerList, ressId, size):
		super(object, self).__init__()
		self.range = range
		self.firerate = firerate
		self.missileFactory = missileFactory
		self.ressId = ressId
		self.size = size
		self.towerList = towerList

	def new(self, at):
		self.towerList.append(Tower(self.range, self.firerate, self.missileFactory, at))
		self.towerList[-1].ressId = self.ressId
		self.towerList[-1].size = self.size


class TroopFactory(object):
	def __init__(self, flagPath, finalTarget, dmg, maxSpeed, troopList, ressId, size):
		super(object, self).__init__()
		self.flagPath = flagPath
		self.dmg = dmg
		self.maxSpeed = maxSpeed
		self.ressId = ressId
		self.size = size
		self.troopList = troopList
		self.finalTarget = finalTarget

	def new(self, at):
		self.troopList.append(Troop(self.flagPath, self.dmg, self.maxSpeed, self.finalTarget, at))
		self.troopList[-1].ressId = self.ressId
		self.troopList[-1].size = self.size

