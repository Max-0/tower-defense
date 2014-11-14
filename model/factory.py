class MissileFactory(object):
	def __init__(self, missileType, dmg, maxSpeed, missileList):
		super(object, self).__init__()
		self.missileType = missileType
		self.dmg = dmg
		self.maxSpeed = maxSpeed
		self.missileList = missileList

	def new(self, start, target):
		self.missileList.append(self.missileType(self.dmg, self.target, self.maxSpeed, start.pos))


class TowerFactory(object):
	def __init__(self, towerType, range, firerate, missileFactory, towerList):
		super(object, self).__init__()
		self.towerType = towerType
		self.range = range
		self.firerate = firerate
		self.missileFactory = missileFactory

	def new(self, at):
		self.towerList.append(self.towerType(self.range, self.firerate, self.missileFactory, at))


class TroopFactory(object):
	def __init__(self, troopType, flagPath, dmg, maxSpeed, troopList):
		super(object, self).__init__()
		self.troopType = troopType
		self.flagPath = flagPath
		self.dmg = dmg
		self.maxSpeed = maxSpeed

	def new(self, at):
		self.troopList.append(troopList(self.flagPath, self.dmg, self.maxSpeed, at))

