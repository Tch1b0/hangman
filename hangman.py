import random
Game = True
charnum = 0
gcharnum = 0
while Game == True:
    Word = ["world","universe","ball",]
    activeWord = (random.choice(Word))

    for char in activeWord:
       print ("/")
       charnum = charnum + 1
    guess = input()
    for char in guess:
        gcharnum = gcharnum + 1

    if gcharnum == 1:
        if guess.lower() in activeWord:
            print ("Right letter")
            quit()
        else:
            print ("That letter isn't in the Word")
            quit()
    elif gcharnum >= 1:
        if guess.lower() == activeWord:
            print("That's the word!")
            quit() 
        elif guess.lower() != activeWord:
            print("That's the wrong word.")
            quit()