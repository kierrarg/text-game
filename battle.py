import random
from stats import Stats
import stats as stat
weapons = ['Sword made of Frautium', 'Spear made of Castrium', 'Laser made of Afralt']
boost = 0

class Battle():
    #defining the damage boost depending on damage
    def Boost():
        for weapons in weapons:
            if weapons == 'Sword made of Frautium':
                boost = 10
            elif weapons == 'Spear made of Castrium':
                boost = 7
            else:
                boost = 13
    #defining when a player chooses to block
    def Block():
        stat.damage = random.randint(0, 5)
        print("You blocked a hit:\n")
        stat.health -= stat.damage
        Stats.damageReceived()
    #defining when player chooses to attack
    def Attack():
        stat.damage = random.randint(0, 25)
        print("You attacked with your sword:")
        stat.nonPlayHealth -= (stat.damage + boost)
        Stats.damageGiven()
        stat.damage = random.randint(0, 15)
        stat.health -= stat.damage
        Stats.damageReceived()
    #defining when player chooses to dodge
    def dodge():
        didDodge = random.randint(0, 3)
        if didDodge <= 1:
            print("You have successfully dodged an attack")
        if didDodge >= 2:
            print("You failed to dodge the attack")
            stat.damage = random.randint(0, 25)
            stat.health -=  stat.damage
            Stats.damageReceived()
    