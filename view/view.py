import sys
sys.path.append("..")
import config 
import tkinter as tk


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
    def __init__(self, root, ressourceManager, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(menuView, self).__init__(root, width=config.window["width"])
        self.ressourceManager = ressourceManager
        self.clearButtonRessource = self.ressourceManager.getRessource(5).photo
        self.clearButton = ImageLabel(self, self.clearButtonRessource)
        self.clearButton.pack()
        self.clearButton.bind("<Button-1>", root.wipeFlag)
        
class mapView(tk.Canvas):
    """docstring for mapView"""
    def __init__(self, root, ressourceManager, width=config.window["width"], height=config.window["height"], bg=config.window["backgroundColor"]):
        super(mapView, self).__init__(root, width = width, height=height)
        self.config(background=bg, borderwidth=0)
        self.ressourceManager = ressourceManager
        #self.title = tk.Label(self, text="Map", bg=bg)
        #self.menuButton = tk.Button(self, text="Menu", command=root.displayMenu, bg=bg)
        #self.menuButton.place(relx=0.9, rely=0.01, anchor=tk.CENTER)
        #self.title.place(relx=0.5, rely=0.01, anchor=tk.CENTER)

    def refresh(self, objects):
        self.delete("all")
        self.displayObjects(objects)

    def displayObjects(self, objects):
        for obj in objects:
            self.create_image((obj.pos[0], obj.pos[1]), image=self.ressourceManager.getRessource(obj.ressId).photo)

class Application(tk.Tk):
    def __init__(self):
        super(Application, self).__init__()
        self.geometry(str(config.window["width"])+"x"+str(config.window["height"]))
        

    def initialize(self, model):
        self.map = None
        self.menu = None
        self.model = model
        self.flagPath = []
        self.displayMap()
        self.displayMenu()


        #self.pack()
        #self.createWidgets()
    def delay(self, callback, time=2000):
        self.after(time, callback)

    def displayMenu(self):
        if (self.menu):
            self.menu.place(relx=1, rely=0, anchor=tk.NE)
            self.menu.lift()
        else:
            self.menu = menuView(self, self.model.ressourceManager)
            self.menu.place(relx=1, rely=0, anchor=tk.NE)
            self.menu.lift()

    def addFlag(self, event):
        self.flagPath.append((event.x,event.y))
        self.model.changeFlags(self.flagPath)

    def initMap(self):
        self.map = mapView(self, self.model.ressourceManager)
        self.map.bind("<Button-1>", self.addFlag)

    def wipeFlag(self, event):
        self.model.changeFlags([])

    def displayMap(self):
        if (self.map):
            self.map.place(anchor=tk.NW)
        else:
            self.initMap()
            self.map.place(anchor=tk.NW)





"""
onclick (x, y){
    self.listFlag.append((x,y))
    .append()
}

"""

