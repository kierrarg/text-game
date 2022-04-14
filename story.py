import stats as stat
from stats import Stats
import fontstyle
from nonPlay import Npc
import nonPlay as npc
from battle import Training

class Rooms():
#definition implementing the first room in the game
    def bedroom():
        stat.inventory.append("flashlight")
        while True:
            while stat.answer == 0:
                print("\nYou awake in a dark room with no idea how you got there.\n")
                print("You feel around and feel a flashlight.\n")
                Stats.addInv(0)
                print("Do you wish to:\n[1] Turn on the flashlight\n[2] Stumble around in the dark")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print("You appear to be in some form of hostel \nThere are around 10 beds but no one else in the room \nYou see a hallway, will you follow it? \n[1] Yes \n[2] No")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        stat.answer = 0
                        Rooms.hallway()
                    if stat.answer == 2:
                        print("There's nothing else to see here,\nYou should go down the hallway\n[1] Yes\n[2] No")
                        stat.answer = int(input())
                        while stat.answer == 1:
                            Rooms.hallway()
                        if stat.answer == 2:
                            print("You clearly don't want to play")
                            exit()
                    else: 
                        Stats.statsFuncs()
                        stat.answer = 1
                        continue

                if stat.answer == 2:
                    print("It seems like you don't want to play")
                    exit()
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
    #defining and implementing hallway room
    def hallway():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("You follow along the brightly lit hallway, on each side of the walls you see incubators with a milky looking substance\n\n Would you like to take a closer look:\n[1] Yes \n[2] No")
                Stats.options()
                stat.answer = int(input())
                while stat.answer == 1:
                    print("Upon closer examination you realize there is something floating in the substance \nIs that a person?")
                    print("Below the incubator is a plaque that reads:")
                    font = fontstyle.apply('In the name of our queen Astra', 'bold/italic/white')
                    print(font)
                    print("Astra, who is Astra?\nShould you take a look at the other incubators:\n[1] Yes \n[2] No")
                    Stats.options()
                    stat.answer = int(input())
                    while stat.answer == 1:
                        font = fontstyle.apply('Astra', 'bold/italic/white')
                        print("The remaining incubators are also filled with people\nEach of them containing a plaque referecing this woman named", font)
                        font = fontstyle.apply('Long live our queen...', 'bold/italic/white')
                        print(font)
                        font = fontstyle.apply('Gone but never forgotten', 'bold/italic/white')
                        print(font)
                        font = fontstyle.apply('We will take back what was ours in her name', 'bold/italic/white')
                        print(font)
                        font = fontstyle.apply('A victim of war', 'bold/italic/white')
                        print(font)
                        print("War!? What war?")
                        print("You continue down the hallway until you reach a door\nYou notice that the door is unlocked") 

                        Rooms.caf()

                    if stat.answer == 2:
                        print("You continue down the hallway until you reach a door\nYou notice that the door is unlocked")

                        Rooms.caf()
                    
                    else:
                        Stats.statsFuncs()
                        stat.answer = 1
                        continue
                if stat.answer == 2:
                    print("You continue down the hallway until you reach a door\nYou notice that the door is unlocked\nWhat could be behind this door?\n")

                    Rooms.caf()

                else: 
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
#definition of third room in story
    def caf():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("...\n...")
                print("Behind the door you see a stark white room full of people wearing all black uniforms, \nthe contrast is blinding\nThey are all huddled around a tall man of African descent\nHe is wearing a white uniform, his chest covered in medalions\nOn his face you see a futuristic looking pair of glasses which are emitting a hologram onto the table in front of him")
                Npc.gungarCaf()
              #  npc.name = "Gungar:"
                print(npc.name, "'Let's do one last training session before heading out to Vide")
                Rooms.training()
#implementing training room    
    def training():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("...\n...")
                print("You follow Gungar and the rest of the crew through a locked white door,\nyou go down a long skinny hallway\nthe walls and floor are bright white.\nYou go through a heavy black door\n")
                Training.enterRoom()
                Rooms.ship()

#implementing spaceship scene
    def ship():
        while True:
            stat.answer = 0
            npc.name = ("Gungar:\n")
            print("You follow the crew into a large garage behind the training facility,\nit is stocked full of various spaceships")
            print(npc.name, "'We'll be boarding onto the ISS Starfall'\nHe points over to a 500 square meters matte black spaceship")
            print(npc.name, "'You guys should get some rest,\nit will be approximately ten hours before we arrive at the Videan spaceport'")
            while stat.answer == 0:
                print("[1] Get some rest\n[2] Stay awake for a bit")
                Stats.options()
                stat.answer = int(input())
                if stat.answer == 1:
                    #cut to videan scene
                    Rooms.vide()
                elif stat.answer == 2:
                    #give option to look around and read diary 
                    Rooms.shipDiary()
                else:
                    Stats.statsFuncs()
                    stat.answer = 0
                    continue
    
    def shipDiary():
        while True:
            stat.answer = 0
            while stat.answer == 0:
                print("You have about 10 hours to kill, should you:\n[1] Wander around the ship\n[2] Read the diary Gungar gave you")
                Stats.options()
                stat.answer = int(input())
                if stat.answer == 1:
                    #prompt conversation with gungar, conversation if dependant on whether or not you have read the diary
                elif stat.answer == 2:
                    Stats.diaryRead()
                else:
                    Stats.statsFuncs()
                    stat.answer == 0
                    continue

#implementing the spaceship landing and meeting with the videan ambassador
    def vide():
        print("Ship landed lol")