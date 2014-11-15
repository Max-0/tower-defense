from model.loaders import *


class Model(object):
	def __init__(self, path):
		self.towers, self.towerTypes = [], {}
		self.missiles, self.missileTypes = [], {}
		self.troops, self.troopTypes = [], {}
		self.ennemyBase = EnnemyBase((0, 0), 500)
		loadMissiles(config.getUrlRessource("missiles.json"),
					 self.missiles, self.missileTypes)
		loadTowers(config.getUrlRessource("towers.json"),
				   self.towers, self.towerTypes, missileTypes)
		loadTroops(config.getUrlRessource("troops.json"),
				   self.troops, self.troopTypes)

	def getGameObjects(self):
		return lambda x : x = self.towers + self.missiles + self.troops

	def newRandomTower(self, maxX, maxY):
		self.towers.append(randomElem(self.towerTypes).new(randomCoord(maxX, maxY)))

	def newRandomMissile(self, maxX, maxY):
		self.missiles.append(randomElem(self.missileTypes).new(randomCoord(maxX, maxY)))

	def newRandomTroop(self, maxX, maxY):
		self.missiles.append(randomElem(self.troopTypes).new(randomCoord(maxX, maxY)))

	def newRandomTypeTower(self, x, y):
		self.towers.append(randomElem(self.towerTypes).new((x, y)))

	def newRandomTypeMissile(self, x, y):
		self.missiles.append(randomElem(self.missileTypes).new((x, y)))

	def randomTypeTroop(self, x, y):
		self.troops.append(randomElem(self.troopTypes).new(x, y))

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

