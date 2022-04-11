import stats as stat
from stats import Stats
import fontstyle
name = ""

class Npc():
    #defining first npc presented
    def gungarCaf():
        name = "Gungar:\n"
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print(name, "'Ah, you're finally awake!'\n'We have been waiting for you to join us for breakfast'\n[1] Thank god, I'm starving\n[2] What? Who are you?")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print("You begin eating with the rest of the crew\nYou still have no idea who they are, or where you are\nBut now is not the time for questions and you were always one to go with the flow")
                    print(name, "'Alright crew, it's time to head back to the stadium'\n'The travel ship leaves for the Alnorn Spaceport of Vide at midnight and we still have much work to do'\n[1] 'The what of what?'\n[2] Continue eating without saying a word")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name, "'Wow, you must have hit your head pretty good during training last night'\n'Tonight we are flying to the planet Vide where we will be meeting with the Videan ambassador Centri to disucss our plans to attack Gelni'\n'Ah you clearly don't remember, here take this'")
                        stat.inventory.append("diary")
#                        print(stat.inventory[1])
                        Stats.addInv(1)
                        return None
                    if stat.answer == 2:
                        print(name, "'Alright team, tonight we are flying to the planet Vide where we will be meeting with the Videan ambassador Centri to disucss our plans to attack Gelni'\n'Arien, it's incredibly important that you have your script memorized'")       
                        print("Everyone around the table is looking at you, am I Arien?\nMore importantly, how could I forget my own name")
                        return None   
                    else:
                        Stats.statsFuncs()
                        stat.answer = 1
                        continue        
                if stat.answer == 2:
                    print(name, "'You really don't remember me?'\n'I am Gungar, your space captain'\n'You must have hit your head pretty good during training last night'\n[1] 'Training? What are we training for'\n[2] 'Yeah, I guess I must have'")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name, "'Ah you clearly don't remember, here take this'") 
                        stat.inventory.append("diary")
                        Stats.addInv()
                        return None
                    if stat.answer == 2:
                        print(name, "'I'm sure you'll be fine, your memory should come back soon enough.'\n'All right crew, it time to prepare for our trip to Vide where we will be meeting with the Videan ambassador Centri.")
                        return None
                    else:
                        Stats.statsFuncs()
                        stat.answer = 2
                        continue
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
#definition of training room tech Sony
    def sony():
        name = "Sony:\n"
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("You walk over to Sony, and think to yourself")
                font = fontstyle.apply('For someone who is considered a battle expert, she sure is small', 'italic')
                print(font)
                print(name, "'Hey Arie, you hit your head pretty good yesterday, hope it's feeling better'\n[1] Yes I am fine\n[2] Actually I can't remember a single thing")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print(name, "'Well that's good, but just in case I'll guide you through your training today")
                    return None
                if stat.answer == 2:
                    print(name, "'Really!? That is quite concerning,\nI would recommend seeing if Gungar has anything that can help jog your memory.\nIt looks like I'll be needing to guide you through training today'")
                    return None
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
                        