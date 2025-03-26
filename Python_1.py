x = "I was born in the USA"
alphabet = " abcdefghijklmnopqrstuvwxyz"
for box in x:
    y = alphabet.find(box.lower())
    w = alphabet[y]
    e = w.upper()
    space = ""
    if y > 9:
        print(f"The first letter: {box}     Number: {y}   The second uppercase letter: {e}")
    else:
        print(f"The first letter: {box}     Number: {y}    The second uppercase letter: {e}")

