import sys
sys.path.append("..")
import config 
from view.view import *
from model.model import *

class MainController(object):
	"""docstring for MainController"""
	def __init__(self):
		super(MainController, self).__init__()
		self.view = Application()
		self.model = Model("")
		self.view.initialize(self.model)
		self.test()
		self.view.delay(self.loop, 41)
		self.view.mainloop()

	def test(self):
		self.model.changeFlags([(600, 100), (500, 500), (250, 250)])
		self.model.newRandomTower(1000, 1000)
		self.model.newRandomTower(1000, 1000)
		self.model.newRandomTroop(1000, 1000)
		self.model.newRandomMissile(1000, 1000, self.model.troops[0])


	def loop(self):
		self.model.update()
		self.view.map.refresh(self.model.getGameObjects())
		self.view.delay(self.loop, 41)


MainController()