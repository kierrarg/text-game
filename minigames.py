import stats as stat
from stats import Stats
import random
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