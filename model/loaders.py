from factory import *


towers = {}
towerTypes = {"base" : Tower}
missiles = {}
missileTypes = {"base" : Missile}
troops = {}
troopTypes = {"base" : Troop}


def loadTowers(self, path):
	l = []
	data = open(path)
	towersData = json.load(data)
	for k in towersData.keys():
		towers[k] = TowerFactory(towerTypes[towersData[k]["type"]],
								 towersData[k]["range"],
								 towersData[k]["firerate"],
								 towersData[k]["missiletype"],
								 missiles[towersData[k]["missiles"]],
								 towersData[k]["ressId"],
								 towersData[k]["size"],
								 l)
	data.close()
	return l

def loadMissiles(self, path):
	l = []
	data = open(path)
	missilesData = json.load(data)
	for k in missilesData.keys():
		missiles[k] = MissileFactory(missileTypes[missilesData[k]["type"]],
									 missilesData[k]["dmg"],
									 missilesData[k]["maxspeed"],
									 missilesData[k]["ressId"],
									 missilesData[k]["size"],
									 l)
	data.close()
	return l


def loadTroop(self, path):
	l = []
	data = open(path)
	troopsData = json.load(data)
	for k in troopsData.keys():
		troops[k] = TroopFactory(troopTypes[troopsData[k]["type"]],
								 [],
							     troopsData[k]["dmg"],
								 troopsData[k]["maxspeed"],
								 troopsData[k]["ressId"],
								 troopsData[k]["size"],
								 l)
	data.close()
	return l
