import random
Game = True

while Game == True:
    Word = ["world","universe","ball","nintendo"]
    activeWord = (random.choice(Word))

    for char in activeWord:
       print ("/")
    guess = input()
    if guess.lower() in activeWord.lower():
        print ("Right")
        quit()
    else:
        print("Wrong")
        quit()

