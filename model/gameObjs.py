from model.ressources import *


class Tower(GameObject):
    def __init__(self, range, firerate, missileFactory,
                 pos=(-1, -1), lastFire=None):
        super(Tower, self).__init__(pos)
        self.range = range
        self.firerate = firerate
        self.missileFactory = missileFactory
        if(not lastFire):
            self.lastFire = time.time()

    def canShoot(self, target):
        return time.time() - self.lastFire < self.firerate and distance(target.pos, self.pos) < self.range

    def shoot(self):
        missileFactory.new(self, target)
        self.lastFire = time.time()


class Missile(GameObject):
    def __init__(self, dmg, target, maxSpeed, pos=(-1, -1)):
        super(Missile, self).__init__(pos)
        self.dmg = dmg
        self.target = target
        self.maxSpeed = maxSpeed

    def nextMove(self):
        if(self.target.exists and self.exists):
            if(squareCollide(self, self.target)):
                self.target.hit(self.dmg)
                self.exists = False
            else:
                self.speed = normalizeSpeed(getDir(self.pos, self.target.pos), self.maxSpeed)
        else:
            self.exists = False

    def move(self):
        self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])



class Flag(GameObject):
    def __init__(self, pos=(-1, -1)):
        super(Flag, self).__init__(pos)
        self.ressId = 4
        self.size = (10, 10)


class FlagPath(object):
    def __init__(self, arg=[]):
        super(object, self).__init__()
        self.l = [Flag(i) for i in arg]


class Troop(Missile):
    def __init__(self, flagPath, dmg, maxSpeed, finalTarget, pos = (-1, -1)):
        super(Troop, self).__init__(dmg, None, maxSpeed, pos)
        self.flagPath = flagPath
        self.finalTarget = finalTarget
        self.actFlag = 0
        self.nextTarget()

    def nextTarget(self):
        if(self.actFlag < len(self.flagPath.l)-1):
            self.actFlag += 1
            self.target = self.flagPath.l[self.actFlag]
        else:
            self.target = self.finalTarget

    def nextMove(self):
        if(self.exists and self.target.exists):
            if(squareCollide(self, self.target)):
                if(self.target is self.finalTarget):
                    self.target.hit(self.dmg)
                    self.exists = False
                else:
                    self.nextTarget()
            self.speed = normalizeSpeed(getDir(self.pos, self.target.pos), self.maxSpeed)
        else:
            self.exists = False

    def move(self):
        self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])

class EnnemyBase(GameObject):
    def __init__(self, pos, lifePoints):
        super(EnnemyBase, self).__init__(pos)
        self.lifePoints = lifePoints

    def hit(self, qty):
        self.lifePoints -= qty
        if(self.lifePoints <= 0):
            self.exists = False
