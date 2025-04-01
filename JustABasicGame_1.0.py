print("This is the starship game:")
print("Enter >help to open technical documentation to this game")
start_the_game = input(">")
while not start_the_game.lower() == "help":
    print("I don't understand that...")
    start_the_game = input(">")
print("start - to start the spaceship")
print("rise - raise the spaceship into the air")
print("lower - lower the spaceship on the ground")
print("stop - to stop the spaceship")
print("quit - to exit")
print("")
press_button = input(">")
while press_button == "start" or press_button == "stop" or press_button == "rise" or press_button == "lower" or len(press_button) > 0:
    if press_button == "start":
        print("Spaceship started!")
        press_button = input(">")
    elif press_button == "rise":
            print("Spaceship was just risen")
            print("You are flying!")
            press_button = input(">")


            if press_button == "stop":
                print("You will destroy the spaceship if you stop this now")
                print("Maybe you need to lower the spaceship first?")
                print(">stop to stop the spaceship")
                print(">lower to lower the spaceship")
                press_button = input(">")
                if press_button == "stop":
                    print("The spaceship got out of energy and you fell down...")
                    print("...")
                    press_button = input(">")
                    print("The spaceship was destroyed")
                    print("You didn't survive this")
                    print("")
                    print("Game Over!")
                    break

    elif press_button == "lower":
            print("You lowered the spaceship on the ground")
            press_button = input(">")

    elif press_button == "stop":
            print("Spaceship stopped!")
            print("This flight was nice!")
            print("")
            print(">start to start your spaceship again")
            print(">quit to quit the game")
            press_button = input(">")
            if press_button == "quit":
                print("You played the game well...")
                press_button = input(">")
                print("Thank you for playing my game!")
                print("")
                print("You quit the game.")
                print("The End.")
                break
    elif press_button == "quit":
            print("You quit the game.")
            print("Thanks for playing!")
            break
    else:
            print("I don't understand that...")
            press_button = input(">")

