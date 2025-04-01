print("Enter >help to open technical documentation to this game")
x = input(">")
while not x.lower() == "help":
    print("I don't understand that...")
    x = input(">")
print(">start - to start the car")
print(">stop - to stop the car")
print(">help - to open the documentation again")
print(">quit - to exit")
print("")
y = input(">").lower()
while y == "start" or y == "stop" or len(y) > 0 or y =="help" or y == "quit":
    if y == "start":
        print("Car started...Ready to go!")
        #print("I don't understand that...")
        y = input(">").lower()
    elif y == "stop":
        print("Car stopped!")
        y = input(">").lower()
    elif y == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit
help - to open the technical documentation again""")
        y = input(">").lower()
    elif y == "quit":
        print("The End.")
        break
    else:
        print("I don't understand that...")
        y = input(">")

