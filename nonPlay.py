import stats as stat
from stats import Stats

class Npc():
    name = ""
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