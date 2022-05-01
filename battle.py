import random
from stats import Stats
import stats as stat
import fontstyle
weapons = ["Laser made of Frautium", "Gun with Castrium bullets", "Laser made of Afralt", "Gun with Frautium bullets"]
boost = 0
weapon = 0

class Battle():
    weaponChosen = ""
    attackMethod = ""
    weaponChosen = ""
    #defining the damage boost depending on damage
    #want to add boost to damage based on weapon choice 
    def checkValid():
        if 0 <= weapon < len(weapons):
            Battle.weaponChosen = weapons[weapon]
            print("You have chosen:\n", Battle.weaponChosen)
            print("Skye writes that down in her notebook")
            return None
        else:
            print("Invalid entry")
            return None
        

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
            print(stat.name[0], "'Alright gang, you know the drill\n--Arie, I guess you might not'")
            print(stat.name, "'Just head over to Sony near that rack of swords, she'll help you out'")
            Training.sony()
            print(stat.name[1], "'Now let's practice your fighting, lets fight the bot in front of us.'")
            while stat.nonPlayHealth > 0:
                Battle.battleOp()
                Battle.attackMethod = input(">>")
                Battle.checkMethod()
                if stat.nonPlayHealth <= 0: 
                    print(stat.name[1], "'You were always a natural, would you like to train again?\n[1] Yes\n[2] No")
                    stat.answer = int(input())
                    if stat.answer == "1":
                        stat.nonPlayHealth = 100
                        stat.health = 100
                    else:
                        stat.health = 100
                        Training.afterTraining()
                        return None
    
    #definition of training room tech Sony
    def sony():
        while True:
            stat.answer = "0"
            while stat.answer == "0":
                print("You walk over to Sony, and think to yourself")
                font = fontstyle.apply('For someone who is considered a battle expert, she sure is small', 'italic')
                print(font)
                print(stat.name[1], "'Hey Arien, you hit your head pretty good yesterday, hope it's feeling better'\n[1] Yes I am fine\n[2] Actually I can't remember a single thing")
                Stats.options()
                stat.answer = input(">>")
                while stat.answer == "1":
                    print(stat.name[1], "'Well that's good, but just in case I'll guide you through your training today'")
                    return None
                if stat.answer == "2":
                    print(stat.name[1], "'Really!? That is quite concerning,\nI would recommend seeing if Gungar has anything that can help jog your memory.\nIt looks like I'll be needing to guide you through training today'")
                    return None
                else:
                    Stats.statsFuncs()
                    stat.answer = "0"
                    continue
        
    def afterTraining():
        while True:
            print(stat.name[1], "'Now, when you're on the battle field it is imperative that you stay alive,\ntake these health shots and use them to replenish your health'")
            stat.inventory.append("healthshot")
            stat.inventory.append("healthshot")
            stat.inventory.append("healthshot")
            Stats.addInv(2)
            stat.answer = "0"
            while stat.answer == "0":
                print(stat.name[0], "'Alright crew, this was our last training!\nIt is time to board the ship and travel to Vide'\nThe crew and yourself head towards Gungar\n[1] Let's go!")
                Stats.options()
                stat.answer = input(">>")
                if stat.answer == "1":
                    return None
                else:
                    Stats.statsFuncs()
                    stat.answer = "0"
                    continue 