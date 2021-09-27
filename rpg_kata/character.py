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

    def damage(self, opponent, damageAmount):
        if self == opponent:
            # do nothing
            return
            
        if damageAmount >= opponent.health:
            opponent.health = 0
        else:
            opponent.health = opponent.health-damageAmount

    def heal(self, opponent, healAmount):
        if opponent.isAlive() == True:
            opponent.health = opponent.health + healAmount
            if opponent.health > STARTING_HEALTH:
               opponent.health = STARTING_HEALTH
        
        

