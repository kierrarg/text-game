#import story as rooms

inventory = []
health = 100
answer = 0

class Stats():
    def invalid():
        print("Invalid entry\nPlease try again:\n")

    
    def addInv():
        print(inventory, "has been added to your inventory!")

    
    def viewHeal():
        print("Player health:\n", health, "\n")


    def viewInv():
        print("Player inventory:\n", inventory, "\n")
        
    def aide():
        print("It's pretty self explanitory\n\n")

    
    def options():
        print("[3] View Inventory \n[4] View Health\n[5] Help\n[6] Exit")

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

