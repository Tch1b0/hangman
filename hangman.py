import random
Game = True
charnum = 0
while Game == True:
    Word = ["world","universe","ball","nintendo"]
    activeWord = (random.choice(Word))

    for char in activeWord:
       print ("/")
       charnum = charnum + 1
    print (charnum)
    guess = input()
    if guess.lower() in activeWord.lower():
        print ("Right letter")
        quit()
    elif guess.lower() is activeWord.lower():
        print("Completely Right!")
        quit()
    else:
        print("Wrong")
        quit()

