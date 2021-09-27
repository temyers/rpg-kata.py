class Character:
    def __init__(self):
        self.level = 1
        self.health = 100

    def isAlive(self):
        if self.health == 0:
            return False
        else:
            return True

    def damage(self, oponent, damageAmount):
        if damageAmount >= oponent.health:
            oponent.health = 0
        else:
            oponent.health = oponent.health-damageAmount

