import stats as stat
from stats import Stats
import fontstyle
name = ["Gungar:\n", "Siri:\n", "Centri:\n", "Rise:\n", "Evip:\n"]

class Npc():
    #defining first npc presented
    def gungarCaf():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print(name[0], "'Ah, you're finally awake!'\n'We have been waiting for you to join us for breakfast'\n[1] Thank god, I'm starving\n[2] What? Who are you?")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print("You begin eating with the rest of the crew\nYou still have no idea who they are, or where you are\nBut now is not the time for questions and you were always one to go with the flow")
                    print(name[0], "'Alright crew, it's time to head back to the stadium'\n'The travel ship leaves for the Alnorn Spaceport of Vide at midnight and we still have much work to do'\n[1] 'The what of what?'\n[2] Continue eating without saying a word")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name[0], "'Wow, you must have hit your head pretty good during training last night'\n'Tonight we are flying to the planet Vide where we will be meeting with the Videan ambassador Centri to disucss our plans to attack Gelni'\n'Ah you clearly don't remember, here take this'")
                        stat.inventory.append("diary")
#                        print(stat.inventory[1])
                        Stats.addInv(1)
                        return None
                    if stat.answer == 2:
                        print(name[0], "'Alright team, tonight we are flying to the planet Vide where we will be meeting with the Videan ambassador Centri to disucss our plans to attack Gelni'\n'Arien, it's incredibly important that you have your script memorized'")       
                        print("Everyone around the table is looking at you, am I Arien?\nMore importantly, how could I forget my own name")
                        return None   
                    else:
                        Stats.statsFuncs()
                        stat.answer = 1
                        continue        
                if stat.answer == 2:
                    print(name[0], "'You really don't remember me?'\n'I am Gungar, your space captain'\n'You must have hit your head pretty good during training last night'\n[1] 'Training? What are we training for'\n[2] 'Yeah, I guess I must have'")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name[0], "'Ah you clearly don't remember, here take this'") 
                        stat.inventory.append("diary")
                        Stats.addInv(1)
                        return None
                    if stat.answer == 2:
                        print(name[0], "'I'm sure you'll be fine, your memory should come back soon enough.'\n'All right crew, it time to prepare for our trip to Vide where we will be meeting with the Videan ambassador Centri.")
                        return None
                    else:
                        Stats.statsFuncs()
                        stat.answer = 2
                        continue
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue

    def gungarShipdiary():
        print(name[0], "'I'm glad you did, it was your mothers. In the end she married Keithua and has been his slave ever since.\nWhen I returned I told our people that she had died the people immediately wanted to avenge her death.\nI told them that she's long gone and not going anywhere, it's harsh but it's true.\nIf we immediately went back into war we never would've stood a fighting chance, now we do.'")
        print(name[0], "'I'm sorry I never told you, but you were so young\nI'm proud of the woman you have become and I am certain that with your help we can save your mother.'")
        print("You sit there and think about what Gungar had said and in your thought you begin to drift away and fall asleep")
        return None
    
    def gungarShipnoDie():
        print(name[0], "'Couldn't sleep hey? Neither could I. If it's not too much trouble,\nwould you mind keeping me company while we wait for the flight to be done?'")
        print(name[0], "'I'm not sure if you remember anything yet,\nbut when the Gelnian army killed our queen Astra the people immediately wanted to avenge her death.\nI told them that she's long gone and not going anywhere, it's harsh but it's true.\nIf we immediately went back into war we never would've stood a fighting chance, now we do.'")
        print("You sit there and think about what Gungar had said and in your thought you begin to drift away and fall asleep")
        return None
#definition of training room tech Sony
    def sony():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("You walk over to Sony, and think to yourself")
                font = fontstyle.apply('For someone who is considered a battle expert, she sure is small', 'italic')
                print(font)
                print(name[1], "'Hey Arien, you hit your head pretty good yesterday, hope it's feeling better'\n[1] Yes I am fine\n[2] Actually I can't remember a single thing")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print(name[1], "'Well that's good, but just in case I'll guide you through your training today'")
                    return None
                if stat.answer == 2:
                    print(name[1], "'Really!? That is quite concerning,\nI would recommend seeing if Gungar has anything that can help jog your memory.\nIt looks like I'll be needing to guide you through training today'")
                    return None
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
                        
    def centriMeeting():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("You and a few others follow Gungar off the ship, you proceed to go down a series of winding hallways until you reach a large wooden door\n approximately 15 feet tall.\nBehind the door lies a large room entirely made from marble, the room is of a circular shape\nand contains a circular marble table in the center.")
                print("A tall slender woman of African descent wearing all white approaches you guys")
                print(name[2], "'Welcome all, please take a seat")
                if Stats.diary == True:
                    print(name[0], "Centri this is Arien, Astra's daughter'")
                    print("Her eyes shoot wide open and a bead of sweat begins to roll down her face")
                    print(name[2], "'Ah Arien, well the years have flown by haven't they? It truly is a pleasure to see you again'\n[1] 'Yes they have, it's a pleasure to see you as well'\n[2] 'You look a little nervous, are you okay?'")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name[2], "'Well I believe it is time to begin discussing our plans'")
                        print("You notice Centri fidgetting with her fingers and shaking as\nshe begins to extend her arm gesturing to the table in the center of the room.")
                        return None
                    if stat.answer == 2:
                        print(name[0], "'She's right Centri, are you all right?'")
                        print(name[2], "'Yes I am fine, I believe it is time to begin discussing our plans'")
                        print("You notice Centri fidgetting with her fingers and shaking as\nshe begins to extend her arm gesturing to the table in the center of the room.")
                        return None
                    else:
                        Stats.statsFuncs()
                        stat.answer = 0
                        continue
                else: 
                    print(name[0], "'Centri this is my associate'\n")
                    print("Centri smiles at you and nods her head, her presence is warm and kind")
                    print(name[2], "'Well it is a pleasure to meet you, I hope you all had a safe trip'\n[1] 'Yes I managed to get some much needed rest'")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        print(name[2], "'Well with that all said and done, I believe it is time to discuss our plans'")
                        print("Centri smiles and extends her arm gesturing to the table in the center of the room.")
                        return None
                    else:
                        Stats.statsFuncs()
                        stat.answer = 0
                        continue
    
    def riseEvip():
        while True:
            print(name[0], "'Sounds good, just follow Rise and she'll get you set up'")
            print("You see a small woman waving at you, from looking at her you can immediately tell that she is related to Siri")
            stat.answer = 0
            while stat.answer == 0:
                print(name[3], "'Follow me'")
                print("You follow Rise outside and begin to walk through a long field\nyou see a group of people surrounded by weapons")
                print(name[3], "'Hey Evip, this is Arien. She'll be with us today'")
                print(name[4], "'Hey Arien, welcome to the squad'")
                print("Evip is a shorter man, though an adult he would easily be mistaken for a child\n[1] 'It's nice to meet you'\n[2] 'What exactly are we doing?'")
                