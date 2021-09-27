class Character:
    def __init__(self):
        self.level = 1
        self.health = 100

    def isAlive(self):
        return True

    def damage(self, oponent, damageAmount):
        oponent.health = oponent.health-damageAmount

