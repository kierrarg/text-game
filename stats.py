import fontstyle

inventory = []
nonPlayHealth = 100
health = 100
answer = 0
damage = 0

class Stats():
    diary = False
    confession = False
    def invalid():
        print("Invalid entry\nPlease try again:\n")
   
    def addInv(i):
        print(inventory[i], "has been added to your inventory!")
  
    def viewHeal():
        print("Player health:\n", health, "\n")

    def viewInv():
        print("Player inventory:\n", inventory, "\n")
        
    def aide():
        print("It's pretty self explanitory\n\n")

    def options():
        print("[3] View Inventory \n[4] View Health\n[5] Help\n[6] Exit")
    
    def damageReceived():
        print("You recieved", damage, "damage")
    
    def damageGiven():
        print("You caused", damage, "damage")

    def statsFuncs():
        if 3 == answer:
            Stats.viewInv()
        elif 4 == answer:
            Stats.viewHeal()
        elif 5 == answer:
            Stats.aide()
        elif 6 == answer:
            exit()
        else:
            Stats.invalid()
    
    def diaryRead():
        while True:
            answer = 0
            while answer == 0:
                font = fontstyle.apply("The rising demand of the elements Frautium and Castrium have done wonders for our economy\nthough I worry that the brewing conflicts with the nation of Gelni will worsen.\nTheir leader Keithua is still upset that I rejected his proposal,\nhowever, it was not in good faith.\nWe must protect ourselves and our allies from this hostile and aggressive nation.\n\n-A\n\n...", 'black/italic/blink')
                print(font)
                print("[1] Continue Reading")
                answer = int(input())
                while answer == 1:
                    #continue diary
                    font = fontstyle.apply("Our sources have told us that Keithua and his army have boarded warships and are headed our way.\nIn an effort to protect my people, myself, my trusted friend Gungar, and our army will be setting off into space.\nI only hope that I return,\nbut in the event I do not Gungar has agreed to raise my daughter.\n\n-A\n\n...", 'black/italic/blink')
                    print(font)
                    print("[2] Continue Reading")
                    answer = int(input())
                    while answer == 2:
                        #continue diary
                        font = fontstyle.apply("The war has commenced and we are clearly outnumbered.\nIt appears one of our allies has betrayed us and traded Frautium and Castrium with the nation of Gelni.\nThey have more weapons and men than we do and are threatening to come for my people once they finish us off.\nI will be surrendering myself to them, to protect my nation\nI can only hope that one day my sacrifice will be avenged.\n\n-A\n\n...", 'black/italic/blink')
                        Stats.diary = True
                        return None
                    else:
                        Stats.statsFuncs()
                        answer = 1
                        continue
                else:
                    Stats.statsFuncs()
                    answer = 0
                    continue