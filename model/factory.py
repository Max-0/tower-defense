from model.gameObjs import *


class MissileFactory(object):
	def __init__(self, missileType, dmg, maxSpeed, missileList, ressId, size):
		super(object, self).__init__()
		self.missileType = missileType
		self.dmg = dmg
		self.maxSpeed = maxSpeed
		self.missileList = missileList
		self.ressId = ressId
		self.size = size
		self.missileList = missileList

	def new(self, start, target):
		self.missileList.append(self.missileType(self.dmg, self.target, self.maxSpeed, start.pos))
		self.missileList[-1].ressId = self.ressId
		self.missileList[-1].size = self.size


class TowerFactory(object):
	def __init__(self, towerType, range, firerate, missileFactory, towerList, ressId, size):
		super(object, self).__init__()
		self.towerType = towerType
		self.range = range
		self.firerate = firerate
		self.missileFactory = missileFactory
		self.ressId = ressId
		self.size = size
		self.towerList = towerList

	def new(self, at):
		self.towerList.append(self.towerType(self.range, self.firerate, self.missileFactory, at))
		self.towerList[-1].ressId = self.ressId
		self.towerList[-1].size = self.size


class TroopFactory(object):
	def __init__(self, troopType, flagPath, dmg, maxSpeed, troopList, ressId, size):
		super(object, self).__init__()
		self.troopType = troopType
		self.flagPath = flagPath
		self.dmg = dmg
		self.maxSpeed = maxSpeed
		self.ressId = ressId
		self.size = size
		self.troopList = troopList

	def new(self, at):
		self.troopList.append(troopList(self.flagPath, self.dmg, self.maxSpeed, at))
		self.troopList[-1].ressId = ressId
		self.troopList[-1].size = self.size

