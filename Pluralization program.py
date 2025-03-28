print("This is the program that turns the singular nouns into the plural ones, ")
print("In short, you enter the singular noun and it gives you the plural one,")
print("Let's try it out!")
print("")
word = str(input("Enter any singular noun: "))
the_last_character = word[-1]
the_second_last_variable = word[-2]
vowel_letters = "aeiouy"
if the_last_character == "y" and the_second_last_variable in str(vowel_letters):
    print(f"{word}s")
elif the_last_character == "y":
    x = word.replace("y","i")
    print(f"{x}es")
else:
    print(f"{word}s")

