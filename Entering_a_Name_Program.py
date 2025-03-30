
name = input("Enter your name: ")
while len(name) < 3 or len(name) > 50:
    if len(name) < 3:
        print("Your name must be at least 3 symbols.")
        name = input("Enter your name again: ")
    elif len(name) > 50:
        print("Your name can be maximum of 50 symbols.")
        name = input("Enter your name again: ")
print("Your name looks good!")