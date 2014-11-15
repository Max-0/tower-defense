import sys
sys.path.append("..")
import tkinter as tk
import config 
from random import random

class View(tk.Frame):
    """docstring for View"""
    def __init__(self, root, width, height, bg):
        super(View, self).__init__(root, width=width, height=height, bg=bg)

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
        self.displayBase()
        self.displayShip()

    def displayBase(self):
        self.base = Ressources(self, "base")
        self.base.getLabel().place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def displayShip(self):
        self.ship = Ressources(self, "ship")
        self.ship.getLabel().place(relx=random(), rely=random(), anchor=tk.CENTER)

class Ressources(object):
    """docstring for Ressources"""
    def __init__(self, root, ressource, backgroundColor=config.window["backgroundColor"]):
        super(Ressources, self).__init__()
        photo = tk.PhotoImage(file=config.getUrlRessource(ressource)+".gif")
        self.label = tk.Label(root, image=photo, bg=backgroundColor)
        self.label.image = photo # keep a reference!

    def getLabel(self):
        return (self.label)

class Application(tk.Tk):
    def __init__(self):
        super(Application, self).__init__()
        #self.geometry(str(self.width)+"x"+str(self.height))
        self.map = None
        self.menu = None
        self.displayMenu()
        self.displayMap()
        self.mainloop()

        #self.pack()
        #self.createWidgets()

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
