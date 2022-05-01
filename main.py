from concurrent.futures.process import _ThreadWakeup
from story import Rooms
from stats import Stats
import stats as stat

def main():
        print("Welcome to  would you like to play?")
        user = input(">>")
        Stats.diary = True
        Stats.confession = True
        #string handling
        if user.lower() == 'y' or user.lower() == 'yes':
            Rooms.riomia()
        else:
            print("See you next time!")
            exit()

if __name__ == '__main__':
    main()