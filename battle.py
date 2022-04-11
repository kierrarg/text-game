import random
from stats import Stats
import stats as stat
import nonPlay as npc
weapons = ['Sword made of Frautium', 'Spear made of Castrium', 'Laser made of Afralt']
boost = 0

class Battle():
    #defining the damage boost depending on damage
    #want to add boost to damage based on weapon choice 

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
#class for training scene 
class Training(Battle):
    def enterRoom():
        while True:
            stat.answer = 0
            npc.name = "Gungar:\n"
            while stat.answer == 0:
                print(npc.name, "'Alright gang, you know the drill\n--Arie, I guess you might not'")
                print(npc.name, "'Just head over to Sony near that rack of swords, she'll help you out'")

    