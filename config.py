import os
import json

currentDir = os.path.abspath('..')
ressourcesPath = currentDir + "/ressources/"

def getJsonRessource(ressource):
    json_data=open(ressourcesPath+ressource+".json")
    data = json.load(json_data)
    json_data.close()
    return (data)
    
def getUrlRessource(ressource):
	return (ressourcesPath+ressource)

window = getJsonRessource("window")