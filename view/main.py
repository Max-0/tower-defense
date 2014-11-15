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

class ImageLabel(tk.Label):
    """docstring for Image"""
    def __init__(self, root, imageData, bg=config.window["backgroundColor"]):
        super(ImageLabel, self).__init__(root, image=imageData, bg=bg)

class homeView(tk.Frame):
    """docstring for menuView"""
    def __init__(self, root, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(menuView, self).__init__(root, width, height, bg)
        self.title = tk.Label(self, text="Map", bg=bg)
        self.view = tk.Button(self, text="Menu", command=root.displayMap, bg=bg)
        self.view.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

class menuView(tk.Frame):
    """docstring for menuView"""
    def __init__(self, root, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(menuView, self).__init__(root, width=config.window["width"])
        self.clearButtonRessource = Ressources(self, "clearButton").photo
        self.clearButton = ImageLabel(self, self.clearButtonRessource)
        self.clearButton.pack();
        self.clearButton.bind("<Button-1>", root.wipeFlag)
        
class mapView(tk.Canvas):
    """docstring for mapView"""
    def __init__(self, root, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(mapView, self).__init__(root, width = width, height=height)
        self.config(background=bg, borderwidth=0)
        self.root = root
        self.bg = bg
        #self.title = tk.Label(self, text="Map", bg=bg)
        #self.menuButton = tk.Button(self, text="Menu", command=root.displayMenu, bg=bg)
        #self.menuButton.place(relx=0.9, rely=0.01, anchor=tk.CENTER)
        #self.title.place(relx=0.5, rely=0.01, anchor=tk.CENTER)
        self.sprites = []
        self.towersRessource = Ressources(self, "towers").photo
        self.flagRessource = Ressources(self, "flag").photo
        self.displayBase()
        self.displayTowers()

    def refresh(self):
        self.delete("all")
        self.displayBase()
        self.displayTowers()
        self.displayFlags()

    def displayFlags(self):
        for flag in self.root.flagPath:
            self.create_image((flag.pos[0], flag.pos[1]), image=self.flagRessource)

    def displayBase(self):
        self.base = model.Ressources(self, "base")

    def displayTowers(self):
        for tower in self.root.game["towers"]:
            self.create_image((tower.pos[0], tower.pos[1]), image=self.towersRessource)

class Application(tk.Tk):
    def __init__(self):
        super(Application, self).__init__()
        self.geometry(str(config.window["width"])+"x"+str(config.window["height"]))
        self.map = None
        self.menu = None
        self.game = {}
        self.flagPath = model.FlagPath().l
        self.game["missiles"] = model.loadMissiles(config.getUrlRessource("missiles.json"))
        self.game["towers"] = model.loadTowers(config.getUrlRessource("towers.json"))
        self.game["troops"] = model.loadTroop(config.getUrlRessource("troops.json"))
        model.towers["fast"].new((200, 300))
        model.towers["fast"].new((600, 600))
        self.displayMap()
        self.displayMenu()
        self.mainloop()



        #self.pack()
        #self.createWidgets()
    def delay(self, callback, time=2000):
        self.after(time, callback)

    def displayMenu(self):
        if (self.menu):
            self.menu.place(relx=1, rely=0, anchor=tk.NE)
            self.menu.lift()
        else:
            self.menu = menuView(self)
            self.menu.place(relx=1, rely=0, anchor=tk.NE)
            self.menu.lift()

    def addFlag(self, event):
        self.flagPath.append(model.Flag((event.x,event.y)))
        self.map.refresh()

    def initMap(self):
        self.map = mapView(self)
        self.map.bind("<Button-1>", self.addFlag)
    def wipeFlag(self, event):
        self.flagPath = []
        self.map.refresh()

    def displayMap(self):
        if (self.map):
            self.map.place(anchor=tk.NW)
        else:
            self.initMap()
            self.map.place(anchor=tk.NW)


app = Application()




"""
onclick (x, y){
    self.listFlag.append((x,y))
    .append()
}

"""

