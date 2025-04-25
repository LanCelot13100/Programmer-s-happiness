# This program shows the two different the dog's conditions (When it's hungry and when it's not hungry)
# Using 'def' function!
#hunger = "hungry"
def dog(hunger = 'yes'):
    print("1. You have a dog!")
    if hunger == "yes":
        print(f"2. Your dog is hungry today!")
    else:
        print(f"2. Your dog is not hungry today!")


dog("not hungry")
print("")
dog()

