import random
Game = True

if Game == True:
    Word = ["World","Universe","Ball","Nintendo"]
    activeWord = (random.choice(Word))

    for char in activeWord:
       print ("/")
    guess = input()
    if guess in activeWord:
        print ("Right")
        quit()
    else:
        print("Wrong")
        quit()

