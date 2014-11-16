from model.factory import *


def formatSize(s):
	ret = s
	ret = ret.replace(" ", "")
	ret = ret.replace("(", "")
	ret = ret.replace(")", "")
	ret = ret.split(",")
	return (int(ret[0]), int(ret[1]))


def loadTowers(path, towers, towerFactories, missileFactories):
	data = open(path)
	towersData = json.load(data)
	for k in towersData.keys():
		towerFactories[k] = TowerFactory(towersData[k]["range"],
								 towersData[k]["firerate"],
								 missileFactories[towersData[k]["missiletype"]],
								 towers,
								 towersData[k]["ressId"],
								 formatSize(towersData[k]["size"]))
	data.close()

def loadMissiles(path, missiles, missileFactories):
	data = open(path)
	missilesData = json.load(data)
	for k in missilesData.keys():
		missileFactories[k] = MissileFactory(missilesData[k]["dmg"],
									 missilesData[k]["maxspeed"],
									 missiles,
									 missilesData[k]["ressId"],
									 formatSize(missilesData[k]["size"]))
	data.close()


def loadTroops(path, troops, troopFactories, finalTarget):
	data = open(path)
	troopsData = json.load(data)
	for k in troopsData.keys():
		troopFactories[k] = TroopFactory(FlagPath(),
								 finalTarget,
							     troopsData[k]["dmg"],
								 troopsData[k]["maxspeed"],
								 troops,
								 troopsData[k]["ressId"],
								 formatSize(troopsData[k]["size"]))
	data.close()
