import sys
sys.path.append("..")
import tkinter as tk
import config 
import random
import model.loaders as model

class View(tk.Frame):
    """docstring for View"""
    def __init__(self, root, width, height, bg):
        super(View, self).__init__(root, width=width, height=height, bg=bg)


class Ressources(object):
    """docstring for Ressources"""
    def __init__(self, root, ressource, backgroundColor=config.window["backgroundColor"]):
        super(Ressources, self).__init__()
        self.root = root
        self.photo = tk.PhotoImage(file=config.getUrlRessource(ressource)+".gif")


class ImageLabel(tk.Label):
    """docstring for Image"""
    def __init__(self, root, imageData, bg=config.window["backgroundColor"]):
        super(ImageLabel, self).__init__(root, image=imageData, bg=bg)

    def moveLabel(self):
        self.place_configure(relx=random.random(), rely=random.random())

class menuView(View):
    """docstring for menuView"""
    def __init__(self, root, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(menuView, self).__init__(root, width, height, bg)
        self.title = tk.Label(self, text="Map", bg=bg)
        self.view = tk.Button(self, text="Menu", command=root.displayMap, bg=bg)
        self.view.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class mapView(View):
    """docstring for mapView"""
    def __init__(self, root, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(mapView, self).__init__(root, width, height, bg)
        self.root = root
        self.bg = bg
        self.title = tk.Label(self, text="Map", bg=bg)
        self.menuButton = tk.Button(self, text="Menu", command=root.displayMenu, bg=bg)
        self.menuButton.place(relx=0.9, rely=0.01, anchor=tk.CENTER)
        self.title.place(relx=0.5, rely=0.01, anchor=tk.CENTER)
        self.sprites = []
        self.towersRessource = Ressources(self, "towers").photo
        self.displayBase()
        self.displayTowers()


    def displayBase(self):
        self.base = Ressources(self, "base")

    def displayTowers(self):
        for tower in self.root.game["towers"]:
            element = ImageLabel(self, self.towersRessource)
            element.place(relx=tower.pos[0]/config.window["width"],rely=tower.pos[1]/config.window["height"])
            self.sprites.append(element)

class Application(tk.Tk):
    def __init__(self):
        super(Application, self).__init__()
        #self.geometry(str(self.width)+"x"+str(self.height))
        self.map = None
        self.menu = None
        self.game = {}
        self.game["missiles"] = model.loadMissiles(config.getUrlRessource("missiles.json"))
        self.game["towers"] = model.loadTowers(config.getUrlRessource("towers.json"))
        self.game["troops"] = model.loadTroop(config.getUrlRessource("troops.json"))
        model.towers["fast"].new((200, 300))
        model.towers["fast"].new((600, 600))
        self.displayMenu()
        self.displayMap()

        self.mainloop()

        #self.pack()
        #self.createWidgets()
    def delay(self, callback, time=2000):
        self.after(time, callback)

    def displayMenu(self):
        if (self.map):
            self.map.pack_forget()
        if (self.menu):
            self.menu.pack()
        else:
            self.menu = menuView(self)
            self.menu.pack()

    def displayMap(self):
        if (self.menu):
            self.menu.pack_forget()
        if (self.map):
            self.map.pack()
        else:
            self.map = mapView(self)
            self.map.pack()

app = Application()




"""
onclick (x, y){
    self.listFlag.append((x,y))
    .append()
}

"""

