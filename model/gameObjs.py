from model.ressources import *


class Tower(GameObject):
    def __init__(self, range, firerate, missileFactory,
                 pos=(-1, -1), lastFire=None):
        super(Tower, self).__init__(pos)
        self.range = range
        self.firerate = firerate
        self.missileFactory = missileFactory
        self.lastFire = time.time()*1000.0

    def canShoot(self, target):
        return (time.time()*1000.0 - self.lastFire) >= self.firerate and distance(target.pos, self.pos) < self.range

    def shoot(self, target):
        self.missileFactory.new(self.pos, target)
        self.lastFire = time.time()*1000.0


    def __str__(self):
        res = "Tower " + str(self.id) + " :\n" + \
              "    range " + str(self.range) + "\n" + \
              "    fire rate " + str(self.firerate) + "\n" + \
              "    last fire " + str(self.lastFire) + "\n"
        return res + indentRepr(super(Tower, self).__str__())


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

    def __str__(self):
        res = "Missile " + str(self.id) + " : \n" + \
              "    dammages " + str(self.dmg) + "\n" + \
              "    max speed " + str(self.maxSpeed) + "\n" + \
              "    targetId " + str(self.target.id) + "\n"
        return res+indentRepr(super(Missile, self).__str__())


class Flag(GameObject):
    def __init__(self, pos=(-1, -1)):
        super(Flag, self).__init__(pos)
        self.ressId = 4
        self.size = (10, 10)

    def __str__(self):
        res = "Flag " + str(self.id) + " : \n"
        return res + indentRepr(super(Flag, self).__str__())


class FlagPath(object):
    def __init__(self, arg=[]):
        super(object, self).__init__()
        self.l = [Flag(i) for i in arg]

    def __str__(self):
        res = "FlagPath : \n"
        for flag in self.l:
            res += indentRepr(str(flag))
        return res + indentRepr(super(FlagPath, self).__str__())


class Troop(Missile):
    def __init__(self, flagPath, dmg, maxSpeed, finalTarget, pos = (-1, -1)):
        super(Troop, self).__init__(dmg, None, maxSpeed, pos)
        self.flagPath = flagPath
        self.finalTarget = finalTarget
        self.actFlag = -1
        self.nextTarget()

    def nextTarget(self):
        if(self.actFlag < len(self.flagPath.l)-1):
            self.actFlag += 1
            self.target = self.flagPath.l[self.actFlag]
        else:
            self.target = self.finalTarget

    def nextMove(self):
        if(self.exists and self.target.exists and self.finalTarget.exists):
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

    def hit(self, qty):
        self.lifePoints -= qty
        if(self.lifePoints <= 0):
            self.exists = False

    def __str__(self):
        res = "Troop " + str(self.id) + " : \n" + \
              "    flag path " + indentRepr(str(self.flagPath)) + \
              "    finalTarget " + indentRepr(str(self.finalTarget)) + \
              "    actFlagIndex " + str(self.actFlag) + "\n"
        return res + indentRepr(super(Troop, self).__str__())

class EnnemyBase(GameObject):
    def __init__(self, pos, lifePoints):
        super(EnnemyBase, self).__init__(pos)
        self.lifePoints = lifePoints
        self.maxLifePoints = lifePoints

    def hit(self, qty):
        self.lifePoints -= qty
        if(self.lifePoints <= 0):
            self.exists = False
    def __str__(self):
        res = "EnnemyBase " + str(self.id) + " \n"
        return res + indentRepr(super(EnnemyBase, self).__str__())
