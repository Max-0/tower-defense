from model.loaders import *


class Model(object):
	def __init__(self):
		self.towers, self.towerTypes, self.towerFactories = [], {"base": Tower}, {}
		self.missiles, self.missileTypes, self.missileFactories = [], {"base": Missile}, {}
		self.troops, self.troopTypes, self.troopFactories = [], {"base": Troop}, {}
		self.ennemyBase = EnnemyBase((0, 0), 500)


		
		self.missiles = loadMissiles(config.getUrlRessource("missiles.json"),
					 self.missileFactories, self.missileTypes)


		self.towers = loadTowers(config.getUrlRessource("towers.json"),
				   self.towerFactories, self.towerTypes, self.missileTypes)



		self.troops  = loadTroops(config.getUrlRessource("troops.json"),
				   self.troopFactories, self.troopTypes)



		self.ressourceManager = RessourceManager(config.getUrlRessource("package.json"))
		self.flags = FlagPath()

	def getGameObjects(self):
		return self.towers + self.missiles + self.troops + self.flags.l + list(ennemyBase)

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

	def changeFlags(self, flags):
		newPath = FlagPath(flags)
		for key in self.troopFactories.keys():
			self.troopFactories[key].flagPath = newPath
		self.flags = newPath
