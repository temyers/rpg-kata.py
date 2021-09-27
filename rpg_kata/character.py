STARTING_HEALTH=100

class Character:
    def __init__(self):
        self.level = 1
        self.health = STARTING_HEALTH

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

    def heal(self, oponent, healAmount):
        if oponent.isAlive() == True:
            oponent.health = oponent.health + healAmount
            if oponent.health > STARTING_HEALTH:
               oponent.health = STARTING_HEALTH
        
        

