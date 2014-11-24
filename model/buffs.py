class Buff(object):
	def __init__(self, lifeTime):
		super(Buff, self).__init__()
		self.lifeTime = lifeTime
		self.started = time.time()*1000

	def applyFirst(self, target):
		pass

	def apply(self, target):
		pass

	def remove(self, target):
		pass

	def isDone(self):
		return time.time()*1000 - self.started > self.lifeTime


class SlowingBuff(Buff):
	def __init__(self, lifeTime, slowingPercentage):
		super(SlowingBuff, self).__init__()
		self.slowingPercentage = slowingPercentage
		self.initialSpeed = 0

	def applyFirst(self, target):
		self.initialSpeed = target.maxSpeed
		target.maxSpeed *= 100/self.slowingPercentage

	def apply(self):
		pass

	def remove(self, target):
		target.maxSpeed = self.initialSpeed


class TimeDamageBuff(Buff):
	def __init__(self, lifeTime, dmgRate, dmgQty):
		super(lifeTime, self).__init__()
		self.dmgRate = dmgRate
		self.dmgQty = dmgQty
		self.last = time.time() * 1000

	def applyFirst(self, target):
		pass

	def apply(self, target):
		if(time.time()*1000 - self.last > self.dmgRate):
			self.last = time.time() * 1000
			self.target.hit(self.dmgQty)

	def remove(self):
		pass
