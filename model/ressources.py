from model.baseImports import *
import config


class Ressources(object):
    """docstring for Ressources"""
    def __init__(self):
        super(Ressources, self).__init__(ressource)
        self.photo = tk.PhotoImage(file=config.getUrlRessource(ressource)+".gif")

class RessourceManager(object):
	def __init__(self, ressListPath):
		super(RessourceManager, self).__init__()
		self.ressTable = {}
		self.defaultImg = None
		dataF = open(ressListPath)
		self.loadRessources(dataF[0])
		dataF.close()

	def loadRessources(self, ressourcesFile):
		for ress in ressourcesFile:
			if(ress["id"] != "default"):
				self.ressTable[ress["id"]] = Ressources(ress["path"])
			else:
				self.defaultImg = Ressources(ress["path"])

	def getRessource(self, id):
		if(id in self.ressTable):
			return self.ressTable[id]
		else:
			print("unloaded ressource : "+str(id))
			return self.defaultImg