import json


towers = {}
towerTypes = {"base" : Tower}
missiles = {}
missileTypes = {"base" : Missile}
troops = {}
troopTypes = {"base" : Troop}


def loadTowers(self, path):
	l = []
	data = open(path+"/towers")
	towersData = json.load(data)
	for k in towersData.keys():
		towers[k] = TowerFactory(towerTypes[towersData[k]["type"]],
								 towersData[k]["range"],
								 towersData[k]["firerate"],
								 towersData[k]["missiletype"],
								 missiles[towersData[k]["missiles"]],
								 l)
	data.close()
	return l

def loadMissiles(self, path):
	l = []
	data = open(path+"/missiles")
	missilesData = json.load(data)
	for k in missilesData.keys():
		missiles[k] = MissileFactory(missileTypes[missilesData[k]["type"]],
									 missilesData[k]["dmg"],
									 missilesData[k]["maxspeed"],
									 l)
	data.close()
	return l


def loadTroop(self, path):
	l = []
	data = open(path+"/troops")
	troopsData = json.load(data)
	for k in troopsData.keys():
		troops[k] = TroopFactory(troopTypes[troopsData[k]["type"]],
								 [],
							     troopsData[k]["dmg"],
								 troopsData[k]["maxspeed"],
								 l)
	data.close()
	return l
