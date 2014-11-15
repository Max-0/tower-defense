import os
import json

currentDir = os.path.abspath('..')
ressourcesPath = currentDir + "/ressources/"

def getRessource(ressource):
    json_data=open(ressourcesPath+ressource+".json")
    data = json.load(json_data)
    print(data)
    json_data.close()
    return (data)

window = getRessource("window")