import random
from stats import Stats
import stats as stat
import nonPlay as npc
from nonPlay import Npc
weapons = ['Sword made of Frautium', 'Spear made of Castrium', 'Laser made of Afralt']
boost = 0
weapon = ""

class Battle():
    attackMethod = ""
    #defining the damage boost depending on damage
    #want to add boost to damage based on weapon choice 
    def boost():
        print("Must add weapons boost depending on players chosen weapon")

        

    #defining when a player chooses to block
    def block():
        stat.damage = random.randint(0, 5)
        print("You blocked a hit:\n")
        stat.health -= stat.damage
        Stats.damageReceived()
        print("Remaining health: ", stat.health, "\nEnemy Health: ", stat.nonPlayHealth)
    #defining when player chooses to attack
    def attack():
        stat.damage = random.randint(0, 25)
        print("You attacked:")
        stat.nonPlayHealth -= (stat.damage + boost)
        Stats.damageGiven()
        stat.damage = random.randint(0, 15)
        stat.health -= stat.damage
        Stats.damageReceived()
        print("Remaining health: ", stat.health, "\nEnemy health: ", stat.nonPlayHealth)
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
        print("Remaining Health: ", stat.health, "\nEnemy health: ", stat.nonPlayHealth)
    #printing attack options 
    def battleOp():
        print("[a] Attack\n[b] Block\n[d] Dodge")
    #checking whether the player has chosen to attack, block or dodge and calling said definition
    def checkMethod():
        if 'b' == Battle.attackMethod.lower():
            Battle.block()
        elif 'a' == Battle.attackMethod.lower():
            Battle.attack()
        elif 'd' == Battle.attackMethod.lower():
            Battle.dodge()
        #need to add option to drink health potion
        else:
            print("Invalid attack entry\nPlease try again")
            
#class for training scene 
class Training(Battle):
    def enterRoom():
        while True:
            print(npc.name[0], "'Alright gang, you know the drill\n--Arie, I guess you might not'")
            print(npc.name, "'Just head over to Sony near that rack of swords, she'll help you out'")
            Npc.sony()
            print(npc.name[1], "'Now let's practice your fighting, lets fight the bot in front of us.'")
            while stat.nonPlayHealth > 0:
                Battle.battleOp()
                Battle.attackMethod = input(">>")
                Battle.checkMethod()
                if stat.nonPlayHealth <= 0: 
                    print(npc.name[1], "'You were always a natural, would you like to train again?\n[1] Yes\n[2] No")
                    stat.answer = int(input())
                    if stat.answer == "1":
                        stat.nonPlayHealth = 100
                        stat.health = 100
                    else:
                        stat.health = 100
                        Training.afterTraining()
                        return None
        
    def afterTraining():
        while True:
            print(npc.name[1], "'Now, when you're on the battle field it is imperative that you stay alive,\ntake these health shots and use them to replenish your health'")
            stat.inventory.append("healthshot")
            stat.inventory.append("healthshot")
            stat.inventory.append("healthshot")
            Stats.addInv(2)
            stat.answer = "0"
            while stat.answer == "0":
                print(npc.name[0], "'Alright crew, this was our last training!\nIt is time to board the ship and travel to Vide'\nThe crew and yourself head towards Gungar\n[1] Let's go!")
                Stats.options()
                stat.answer = input(">>")
                if stat.answer == "1":
                    return None
                else:
                    Stats.statsFuncs()
                    stat.answer = "0"
                    continue 