from model.loaders import *


class Model(object):
	def __init__(self, path):
		self.towers, self.towerFactories = [], {}
		self.missiles, self.missileFactories = [], {}
		self.troops, self.troopFactories = [], {}
		self.ennemyBase = EnnemyBase((0, 0), 500)
		loadMissiles(config.getUrlRessource("missiles.json"),
					 self.missiles, self.missileFactories)
		loadTowers(config.getUrlRessource("towers.json"),
				   self.towers, self.towerFactories, missileFactories)
		loadTroops(config.getUrlRessource("troops.json"),
				   self.troops, self.troopFactories)

	def getGameObjects(self):
		return self.towers + self.missiles + self.troops + [self.ennemyBase]

	def newRandomTower(self, maxX, maxY):
		self.towers.append(randomElem(self.towerFactories).new(randomCoord(maxX, maxY)))

	def newRandomMissile(self, maxX, maxY):
		self.missiles.append(randomElem(self.missileFactories).new(randomCoord(maxX, maxY)))

	def newRandomTroop(self, maxX, maxY):
		self.missiles.append(randomElem(self.troopFactories).new(randomCoord(maxX, maxY)))

	def newRandomTypeTower(self, x, y):
		self.towers.append(randomElem(self.towerFactories).new((x, y)))

	def newRandomTypeMissile(self, x, y):
		self.missiles.append(randomElem(self.missileFactories).new((x, y)))

	def randomTypeTroop(self, x, y):
		self.troops.append(randomElem(self.troopFactories).new(x, y))

	def update(self):
		m=0
		while(m < len(self.missiles)):
			self.missiles[m].nextMove()
			self.missiles[m].move()
			if(not self.missiles[m].exists):
				del self.missiles[m]
			else:
				m += 1
		t = 0
		while( t < len(self.troops)):
			t.nextMove()
			if(not self.troops[t].exists):
				del self.troops[t]
			else:
				t += 1
		t = 0
		while( t < len(self.towers)):
			for target in self.troops:
				if(self.towers[t].canShoot(target)):
					self.towers[t].shoot(target)
			t.nextMove()
			if(not self.towers[t].exists):
				del self.towers[t]
			else:
				t += 1

