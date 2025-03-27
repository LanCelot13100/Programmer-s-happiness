character = input("Enter any character: ")
space = " "
while character == "" or character < str(len(space)):
    print("NOT OK")
    print("You didn't enter anything!")
    character = input("Enter any character again: ")
print("OK")
