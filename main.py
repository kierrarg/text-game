from story import Rooms

def main():
        print("Welcome to  would you like to play?")
        user = input(">>")
        #string handling
        if user.lower() == 'y':
            Rooms.bedroom()
        else:
            print("See you next time!")
            exit()

if __name__ == '__main__':
    main()