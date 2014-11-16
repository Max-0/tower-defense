from model.loaders import *


class Model(object):
	def __init__(self, path):
		self.towers, self.towerFactories = [], {}
		self.missiles, self.missileFactories = [], {}
		self.troops, self.troopFactories = [], {}
		self.ennemyBase = EnnemyBase((0, 0), 500)
		self.ennemyBase.ressId = 3
		self.ennemyBase.size = (40, 40)
		loadMissiles(config.getUrlRessource("missiles.json"),
					 self.missiles, self.missileFactories)
		loadTowers(config.getUrlRessource("towers.json"),
				   self.towers, self.towerFactories, self.missileFactories)
		loadTroops(config.getUrlRessource("troops.json"),
				   self.troops, self.troopFactories, self.ennemyBase)
		self.ressourceManager = RessourceManager(config.getUrlRessource("package.json"))
		self.flags = FlagPath()

	def getGameObjects(self):
		return self.towers + self.missiles + self.troops + [self.ennemyBase] + self.flags.l

	def newRandomTower(self, maxX, maxY):
		randomElem(self.towerFactories).new(randomCoord(maxX, maxY))

	def newRandomMissile(self, maxX, maxY, target):
		randomElem(self.missileFactories).new(randomCoord(maxX, maxY), target)

	def newRandomTroop(self, maxX, maxY):
		randomElem(self.troopFactories).new(randomCoord(maxX, maxY))

	def newRandomTypeTower(self, x, y):
		randomElem(self.towerFactories).new((x, y))

	def newRandomTypeMissile(self, x, y):
		randomElem(self.missileFactories).new((x, y))

	def randomTypeTroop(self, x, y):
		randomElem(self.troopFactories).new(x, y)

	def update(self):
		m=0
		while(m < len(self.missiles)):
			self.missiles[m].nextMove()
			self.missiles[m].move()
			if(not self.missiles[m].exists):
				print("deleted missile")
				del self.missiles[m]
			else:
				m += 1
		t = 0
		while( t < len(self.troops)):
			self.troops[t].nextMove()
			self.troops[t].move()
			if(not self.troops[t].exists):
				print("deleted troop")
				del self.troops[t]
			else:
				t += 1
		t = 0
		while( t < len(self.towers)):
			for target in self.troops:
				if(self.towers[t].canShoot(target)):
					self.towers[t].shoot(target)
			if(not self.towers[t].exists):
				print("deleted tower")
				del self.towers[t]
			else:
				t += 1

	def changeFlags(self, flags):
		newPath = FlagPath(flags)
		for key in self.troopFactories.keys():
			self.troopFactories[key].flagPath = newPath
		self.flags = newPath