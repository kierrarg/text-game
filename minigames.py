import stats as stat
from stats import Stats
import random
import fontstyle
class MiniGame():
    ships = ["HWSS Inquisitor", "LWSS Jellyfish", "STS Rampart", "SSE Harmony", "SSE Eagle"]
    fuel = 0

    def fuelShip():
        while True:
            print("Rise:\n", "'When fueling the ships it is important that we know how much fuel each ships takes so we know how much to give it,\nyou must remember the tank size of each ship and calculate how much fuel they need.'")
            MiniGame.shipInfo()
            count = 0
            while count <= 15:
                ship = random.randint(0, 4)
                print("\n\n\n", MiniGame.ships[ship])
                MiniGame.shipMiniGame()
                stat.answer = int(input())
                MiniGame.fuel += stat.answer
                if ship == 0:
                    if MiniGame.fuel == 300:
                        print("Correct")
                        count += 1
                    else:
                        print("Try again")
                elif ship == 1:
                    if MiniGame.fuel == 250:
                        print("Correct")
                        count += 1
                    else:
                        print("Try again")
                elif ship == 2:
                    if MiniGame.fuel == 450:
                        print("Correct")
                        count += 1
                    else:
                        print("Try again")
                elif ship == 3:
                    if MiniGame.fuel == 380:
                        print("Correct")
                        count += 1
                    else:
                        print("Try again")
                elif ship == 4:
                    if MiniGame.fuel == 290:
                        print("Correct")
                        count += 1
                    else:
                        print("Try again")
            if count > 15:
                return False
                

    def shipMiniGame():
        MiniGame.fuel = random.randint(0, 70)
        print("There are", MiniGame.fuel, "L of fuel in this ship\nHow many litres of fuel should we add?")

    def shipInfo():
        print("The HWSS Inquisitor needs 300L of fuel")
        print("The LWSS Jellyfish needs 250L of fuel")
        print("The STS Rampart needs 450L of fuel")
        print("The SSE Harmony needs 380L of fuel")
        print("The SSE Eagle needs 290L of fuel")
    

    def riddlesPrint():
        while True:
                print("At night they come without being fetched,\nAnd by day they are lost without being stolen.")
                stat.answer = input(">>")
                while stat.answer.lower() == 'stars':
                    print("What is a spaceman's favorite chocolate?")
                    stat.answer = input(">>")
                    while stat.answer.lower() == 'a mars bar' or stat.answer.lower() == 'marsbar':
                        print("Why did the cow go to outer space?")
                        stat.answer = input(">>")
                        while stat.answer.lower() == 'milkyway' or stat.answer.lower() == 'to visit the milky way':
                            print("What is an astronauts favorite key on the keyboard?")
                            stat.answer = input(">>")
                            while stat.answer.lower() == 'space bar' or stat.answer.lower() == 'the space bar':
                                return False
                            else:
                                print("Try again")
                                stat.answer = "milkyway"
                                continue
                        else:
                            print("Try again")
                            stat.answer = "marsbar"
                            continue
                    else:
                        print("Try again")
                        stat.answer = "stars"
                        continue

                else:
                    print("Try again")
    
    def questions():
        while True:
            counter = 0
            stat.answer = 0
            while stat.answer == 0:
                print("You look at the clock, you will only have enough time to ask 4 questions.\nWhat should you ask?")
                while counter <= 3:
                    print("[1] What do you plan to do once we finish this war?\n[2] Do we have everything we will need?\n[3] What is your favourite colour?\n[4] How do we plan on attacking?\n[5] Who will be taking the lead during the war?\n[6] How soon will we be leaving?")
                    stat.answer = input(">>")
                    if stat.answer == "1":
                        print("Centri:\n'Well Gungar and I have discussed splitting the land, Gelni is the only nation which exports Afralt.\nHaving control of Afralt exports would drastically improve both of our economies.'")
                        if Stats.diary == True and Stats.confession == True:
                            font = fontstyle.apply('I remember mothers diary mentioning we exported Castrium and Frautium,\nnow if Gelni is the only nation to export Afralt and we have had turmoil with them for years\na third party must have been giving us Afralt.\nVide must have been the middle man, selling us Afralt and selling Gelni Frautium and Castrium', 'italic')
                            print("You think to yourself,", font)
                            counter += 1
                            stat.answer = "0"
                        else:
                            counter += 1
                            stat.answer = "0"
                    elif stat.answer == "2":
                        print("Centri:\n'Ideally my men would have more Castrium and Frautium weapons, they are the most powerful of elements afterall'")
                        if Stats.diary == True and Stats.confession == True:
                            print("Gungar:\n'My dear Centri, we do not have enough stock and my top priority is ensuring that my men are armed'")
                            print("Gungar looks over at you and clenches his jaw, he is clearly lying to her.\nCould he also believe that Vide are the traitors?")
                            counter += 1
                            stat.answer = "0"
                        else:
                            print("Gungar:\n'My dear Centri, we do not have enough stock and my top priority is ensuring that my men are armed'")   
                            counter += 1
                            stat.answer = "0"   
                    elif stat.answer == "3":
                        print("Centri:\n'What a foolish question, why waste both of our time on it?\nThat is surely enough for today'")
                        counter = 3   
                        return None
                    elif stat.answer == "4":
                        print("Centri:\n'Well being that your men have the majority of the weapons, we will be following behind you into battle\nthough I would not be opposed to my men being given more weapons.'")
                        if Stats.diary == True and Stats.confession == True:
                            print("Gungar:\n'We simply cannot, we do not have enough weapons to spare any'")
                            print("Gungar looks at you, it appears that he has planned for this. It would be risky to be caught between two enemies.")
                            counter += 1
                            stat.answer = "0"
                        else: 
                            print("Gungar:\n'We simply cannot, we do not have enough weapons to spare any'")
                            counter += 1
                            stat.answer = "0"
                    elif stat.answer == "5":
                        print("Centri:\n'I expect Gungar will lead, I know we discussed my general would lead us into battle I believe Gungar is more qualified'")
                        if Stats.diary == True and Stats.confession == True:
                            print("Gungar:\n'Centri you wound me, if I didn't know any better I'd say you want me to be the first one dead'\nThey both begin laughing but behind those laughs is discomfort, as though the joke was no joke at all.")
                            counter += 1
                            stat.answer = "0"
                        else: 
                            print("Gungar:\n'Centri you wound me, if I didn't know any better I'd say you want me to be the first one dead'\nThey both begin laughing")
                            counter += 1
                            stat.answer = "0"
                    elif stat.answer == "6":
                        print("Centri:\n'As long as the weapons are all packed up we should be leaving right when we're done this meeting'")
                        counter += 1
                        stat.answer = "0"
                    else:
                        Stats.statsFuncs()
                        stat.answer = "0"
                        continue
                while counter >= 3:
                    return None
                                                            

                    
