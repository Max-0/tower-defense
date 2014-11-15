from model.factory import *


def loadTowers(path, towers, towerTypes, missileTypes):
	l = []
	data = open(path)
	towersData = json.load(data)
	for k in towersData.keys():
		towers[k] = TowerFactory(towerTypes[towersData[k]["type"]],
								 towersData[k]["range"],
								 towersData[k]["firerate"],
								 missileTypes[towersData[k]["missiletype"]],
								 l,
								 towersData[k]["ressId"],
								 towersData[k]["size"])
	data.close()
	return l

def loadMissiles(path, missiles, missileTypes):
	l = []
	data = open(path)
	missilesData = json.load(data)
	for k in missilesData.keys():
		missiles[k] = MissileFactory(missileTypes[missilesData[k]["type"]],
									 missilesData[k]["dmg"],
									 missilesData[k]["maxspeed"],
									 l,
									 missilesData[k]["ressId"],
									 missilesData[k]["size"])
	data.close()
	return l


def loadTroop(path, troops, troopTypes):
	l = []
	data = open(path)
	troopsData = json.load(data)
	for k in troopsData.keys():
		troops[k] = TroopFactory(troopTypes[troopsData[k]["type"]],
								 [],
							     troopsData[k]["dmg"],
								 troopsData[k]["maxspeed"],
								 l,
								 troopsData[k]["ressId"],
								 troopsData[k]["size"])
	data.close()
	return l
